"""E022 one-shot: prepare, globally freeze, reproduce, score, validate."""
import argparse
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import time
import numpy as np
import pandas as pd
from . import e022_selection as selection,e022_metrics as metrics,e019_checker as c
from .e022_integrity import preserve,no_failures,IMAGE,PROTOCOL,REFERENCE,FROZEN,CACHE,OUT
from .e020_map_integrity import verify_map,verify_caches
from .e011_publication import same
from .data_contract import load_training_data,combined_label
from .resilient_status import ResilientStatus
ROOT=Path(__file__).resolve().parents[2]


def freeze(out,development,policies,memories,fits):
    if fits!=50 or len(development)!=15 or len(policies)!=45 or set(memories)!=set(range(5)):
        raise ValueError('Incomplete global preparation.')
    files={}
    for fold,memory in memories.items():
        if any(v.flags.writeable for v in memory.values()): raise ValueError('Mutable freeze state.')
        path=out/f'fold_{fold}_frozen_private.npz'
        with path.open('xb') as stream: np.savez_compressed(stream,**memory)
        files[path.name]=c.sha(path)
    c.write_new(out/'frozen_development_private.json',{'development':development,'policies':policies,
        'prediction_sha256':files,'model_fits':fits,'all_folds_policies_predictions_masks_frozen':True})
    return c.sha(out/'frozen_development_private.json')


def verify_freeze(out,digest):
    if c.sha(out/'frozen_development_private.json')!=digest: raise ValueError('Global freeze receipt changed.')
    frozen=json.loads((out/'frozen_development_private.json').read_text())
    if frozen['model_fits']!=50 or frozen['all_folds_policies_predictions_masks_frozen'] is not True or len(frozen['policies'])!=45 or len(frozen['development'])!=15:
        raise ValueError('Incomplete freeze receipt.')
    if set(frozen['prediction_sha256'])!={f'fold_{f}_frozen_private.npz' for f in range(5)}: raise ValueError('Freeze fold grid.')
    for name,digest in frozen['prediction_sha256'].items():
        if c.sha(out/name)!=digest: raise ValueError('Frozen arrays changed.')
    return frozen


def reproduce_private(root,development,memories):
    if c.sha(root/'artifacts/e021_attempt01/frozen_development_private.json')!=FROZEN or c.sha(root/'results/E021_aggregates.json')!=REFERENCE:
        raise ValueError('Historical evidence hash differs.')
    frozen=json.loads((root/'artifacts/e021_attempt01/frozen_development_private.json').read_text())
    historical=json.loads((root/'results/E021_aggregates.json').read_text())['development']
    roles=json.loads((root/'results/E007_aggregates.json').read_text())['development']
    for fold,memory in memories.items():
        d=next(r for r in development if r['arm']=='L7' and r['fold']==fold)
        h=next(r for r in historical if r['fold']==fold)
        same(d['selection'],h['selection'])
        for k in ('n_train','n_calibration','n_evaluation'): same(d[k],h[k])
        hashes={r['derived_role_sha256'] for r in roles if r['fold']==fold}
        if hashes!={d['derived_role_sha256']}: raise ValueError('E007 question allocation differs.')
        name=f'fold_{fold}_frozen_private.npz'; path=root/'artifacts/e021_attempt01'/name
        if c.sha(path)!=frozen['prediction_sha256'][name]: raise ValueError('E021 frozen prediction hash differs.')
        with np.load(path,allow_pickle=True) as original:
            for key in ('classes','positions','questions','train_labels','train_questions'):
                if not np.array_equal(memory[key],original['memory_'+key]): raise ValueError('Historical alignment differs.')
            for arm in selection.ARMS:
                raw=memory[arm+'_raw']
                if not np.allclose(raw,original[arm+'_raw_prob'],atol=1e-10,rtol=0): raise ValueError('Historical raw predictions differ.')
                pred,top=selection.ranks(raw)
                if not np.array_equal(pred,original[arm+'_raw_predicted']) or not np.array_equal(top,original[arm+'_raw_top']):
                    raise ValueError('Historical ranks differ.')


def reproduce_scores(root,unfiltered):
    ref=json.loads((root/'results/E021_aggregates.json').read_text())['exact']['records']
    wanted={(r['arm'],r['fold'],r['question'],r['stratum']):r for r in ref if r['arm'] in selection.ARMS and r['scale']=='raw'}
    actual={(r['arm'],r['fold'],r['question'],r['stratum']):r['group'] for r in unfiltered if r['scale']=='raw'}
    if set(wanted)!=set(actual): raise ValueError('Historical metric grid differs.')
    for key,g in actual.items():
        same(g['original_n'],wanted[key]['n'])
        for k in ('map_at_3','top1_accuracy'): same(g[k],wanted[key]['metrics'][k])


def run(args):
    out=ROOT/OUT; no_failures(out)
    if args.image_id!=IMAGE or (os.getuid(),os.getgid())!=(10001,10001): raise ValueError('Execution identity differs.')
    began=time.monotonic(); fits=0; policy_count=0
    with ResilientStatus(out/'status.json',experiment_id='E022',total=100) as live:
        live.update('Integrity preflight; no fits or outcomes yet',completed=0)
        lock=preserve(ROOT); maplock=verify_map(ROOT)
        start=json.loads((out/'started.json').read_text())
        if start['git_revision']!=args.git_revision or start['lock_sha256']!=c.sha(ROOT/'experiments/e022_lock.json'): raise ValueError('Start provenance differs.')
        core=selection.core
        def frozen_inputs():
            core.verify_frozen_inputs(ROOT/'data/raw/train.csv',ROOT/'artifacts/splits',expected_data_sha=core.DATA_SHA,
                expected_manifest_sha=core.MANIFEST_SHA,expected_assignments_sha=core.ASSIGN_SHA)
        frozen_inputs()
        pairs,caches,receipts=verify_caches(ROOT,ROOT/'artifacts/e020_attempt01/map',maplock)
        if receipts['G7']['cache_sha256']!=CACHE: raise ValueError('G7 cache differs.')
        c.write_new(out/'cache_receipt.json',{'cache_sha256':CACHE,'pairs':60,'new_model_calls':0})
        frame=load_training_data(ROOT/'data/raw/train.csv')
        if len(frame)!=36696 or frame.QuestionId.nunique()!=15: raise ValueError('Population differs.')
        features=pd.read_csv(ROOT/'data/raw/train.csv',usecols=['QuestionText','MC_Answer'],dtype=str,keep_default_na=False)
        assignments=pd.read_csv(ROOT/'artifacts/splits/grouped_fold_assignments.csv',keep_default_na=False)
        lookup={pair:i for i,pair in enumerate(pairs)}
        ids=np.array([lookup[c.normalize(q),c.normalize(a)] for q,a in zip(features.QuestionText,features.MC_Answer)])
        signals=np.array([r['scores'] for r in caches['G7']],dtype=np.float64)[ids]
        development=[]; policies=[]; memories={}
        for fold in range(5):
            roles=assignments[f'fold_{fold}'].to_numpy()
            train,cal,ev=(np.flatnonzero(roles==r) for r in ('train','calibration','evaluation'))
            def fitted():
                nonlocal fits
                fits+=1; live.update(f'Training: classifier fits {fits}/50; fold {fold+1}/5',completed=fits+policy_count)
            def selected():
                nonlocal policy_count
                policy_count+=1; live.update(f'Development: policies {policy_count}/45; fold {fold+1}/5',completed=fits+policy_count)
            d,p,memory=selection.prepare(frame.iloc[train],frame.iloc[cal],frame.iloc[ev][selection.FEATURES],ev,fold,
                signals[cal],signals[ev],fitted,selected)
            development.extend(d); policies.extend(p); memories[fold]=memory
        if policy_count!=45 or sorted(np.concatenate([m['positions'] for m in memories.values()]).tolist())!=list(range(36696)):
            raise ValueError('Policy or evaluation accounting differs.')
        freeze_sha=freeze(out,development,policies,memories,fits)
        reproduce_private(ROOT,development,memories)
        # Global evaluation truth boundary: all policies, predictions and masks frozen.
        truths={f:combined_label(frame.iloc[memories[f]['positions']]).to_numpy() for f in range(5)}
        unfiltered=[]; retained=[]
        for fold in range(5):
            u,r=metrics.evaluate(fold,memories[fold],truths[fold]); unfiltered.extend(u); retained.extend(r)
            live.update(f'Scoring: evaluation folds {fold+1}/5; all policies frozen',completed=96+fold)
        reproduce_scores(ROOT,unfiltered)
        panels=metrics.panels(unfiltered,retained,policies)
        live.update('Historical reproduction passed; validating aggregates and preservation',completed=100,
            latest_metrics={r['arm']+' primary questions passing':r['joint_pass_questions'] for r in panels['decisions'] if r['primary']})
        verify_freeze(out,freeze_sha); preserve(ROOT); verify_caches(ROOT,ROOT/'artifacts/e020_attempt01/map',maplock); frozen_inputs(); no_failures(out)
        result={'experiment_id':'E022','status':'COMPLETED','development':development,'policies':policies,**panels,
            'resources':{'image_id':IMAGE,'wall_seconds':time.monotonic()-began},
            'integrity':{'git_revision':args.git_revision,'lock_sha256':c.sha(ROOT/'experiments/e022_lock.json'),'protocol_sha256':PROTOCOL,
                'reference_sha256':REFERENCE,'g7_cache_sha256':CACHE,'freeze_sha256':freeze_sha,'preserved_files':lock['preserved_files'],
                'preservation_verified':True,'global_freeze_verified':True,'e018_remains_blocked':True,'model_fits':50,'new_model_calls':0,
                'fit_warnings':0,'reproduced_model_folds':15,'policies':45,'seed':20260831,'uid':10001,'gid':10001,'row_level_public_outputs':False}}
        from .e022_publication import validate
        validate(result); c.write_new(out/'aggregate_results.json',result)
        c.write_new(out/'execution.json',{'status':'COMPLETED','results_sha256':c.sha(out/'aggregate_results.json'),
            'git_revision':args.git_revision,'lock_sha256':c.sha(ROOT/'experiments/e022_lock.json'),'finished_utc':datetime.now(timezone.utc).isoformat()})
        print('E022 complete: separate L7 and C50 primary outcomes; interpretation withheld.',flush=True)


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--git-revision',required=True); parser.add_argument('--image-id',required=True)
    try: run(parser.parse_args())
    except BaseException as exc:
        c.write_new(ROOT/OUT/'statistics_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False}); raise


if __name__=='__main__': main()
