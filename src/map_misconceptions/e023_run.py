"""E023 one-shot execution: nested preparation, freeze, reproduction, reporting."""
import argparse
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import time
import numpy as np
import pandas as pd
from . import e023_selection as selection,e023_metrics as metrics,e019_checker as c
from . import e022_run as old_run,e022_metrics as old_metrics
from .e023_integrity import preserve,no_failures,IMAGE,PROTOCOL,REFERENCE,FROZEN,CACHE,OUT
from .e020_map_integrity import verify_map,verify_caches
from .e011_publication import same
from .data_contract import load_training_data,combined_label
from .resilient_status import ResilientStatus
ROOT=Path(__file__).resolve().parents[2]


def freeze(out,development,policies,routers,crossfit,review_counts,memories,fits):
    if fits!=200 or len(development)!=15 or len(policies)!=165 or len(routers)!=20 or len(crossfit)!=5 or len(review_counts)!=390 or set(memories)!=set(range(5)):
        raise ValueError('Incomplete global preparation.')
    files={}
    for fold,memory in memories.items():
        if any(v.flags.writeable for v in memory.values()): raise ValueError('Mutable freeze state.')
        n=len(memory['positions'])
        for a,r in selection.REVIEW:
            for b in selection.BUDGETS:
                keep=memory[f'review_{a}_{r}_{b}']
                if keep.shape!=(n,) or keep.dtype!=bool or int(keep.sum())!=n-n*b//100: raise ValueError('Review freeze accounting.')
        for a,r in selection.AUTO:
            for t in selection.TARGETS:
                keep=memory[f'auto_{a}_{r}_{t}']
                if keep.shape!=(n,) or keep.dtype!=bool: raise ValueError('Automation freeze shape.')
        path=out/f'fold_{fold}_frozen_private.npz'
        with path.open('xb') as stream: np.savez_compressed(stream,**memory)
        files[path.name]=c.sha(path)
    c.write_new(out/'frozen_development_private.json',{'development':development,'policies':policies,'routers':routers,'crossfit':crossfit,
        'review_counts':review_counts,'prediction_sha256':files,'model_fits':fits,'all_folds_policies_predictions_masks_frozen':True})
    return c.sha(out/'frozen_development_private.json')


def verify_freeze(out,digest):
    if c.sha(out/'frozen_development_private.json')!=digest: raise ValueError('Global freeze receipt changed.')
    frozen=json.loads((out/'frozen_development_private.json').read_text())
    if frozen['model_fits']!=200 or frozen['all_folds_policies_predictions_masks_frozen'] is not True: raise ValueError('Freeze identity.')
    for k,n in [('development',15),('policies',165),('routers',20),('crossfit',5),('review_counts',390)]:
        if len(frozen[k])!=n: raise ValueError('Freeze counts.')
    if set(frozen['prediction_sha256'])!={f'fold_{f}_frozen_private.npz' for f in range(5)}: raise ValueError('Freeze fold grid.')
    for name,digest in frozen['prediction_sha256'].items():
        if c.sha(out/name)!=digest: raise ValueError('Frozen arrays changed.')
    return frozen


def reproduce_private(root,development,policies,memories):
    if c.sha(root/'results/E022_aggregates.json')!=REFERENCE: raise ValueError('E022 aggregate changed.')
    original=old_run.verify_freeze(root/'artifacts/e022_attempt01',FROZEN)
    same(development,original['development'])
    selected=[{k:r[k] for k in ('arm','fold','policy')} for r in policies if r['rule'] in ('confidence','frequency')]
    sort=lambda rows:sorted(rows,key=lambda r:(r['fold'],r['arm'],r['policy']['target_percent']))
    same(sort(selected),sort(original['policies']))
    for fold,memory in memories.items():
        with np.load(root/'artifacts/e022_attempt01'/f'fold_{fold}_frozen_private.npz',allow_pickle=True) as old:
            for key in old.files:
                if key.endswith(('_raw','_final')):
                    if not np.allclose(memory[key],old[key],atol=1e-10,rtol=0): raise ValueError('E022 probabilities differ.')
                    if any(not np.array_equal(a,b) for a,b in zip(selection.old.ranks(memory[key]),selection.old.ranks(old[key]))): raise ValueError('E022 ranks differ.')
                elif not np.array_equal(memory[key],old[key]): raise ValueError('E022 alignment/masks differ.')


def reproduce_metrics(root,unfiltered,retained):
    original=json.loads((root/'results/E022_aggregates.json').read_text())
    same(unfiltered,original['unfiltered']['records']); same(retained,original['retained']['records'])


def run(args):
    out=ROOT/OUT; no_failures(out)
    if args.image_id!=IMAGE or (os.getuid(),os.getgid())!=(10001,10001): raise ValueError('Execution identity differs.')
    began=time.monotonic(); fits=0; policy_count=0; router_count=0
    with ResilientStatus(out/'status.json',experiment_id='E023',total=390) as live:
        live.update('Integrity preflight; no fits or outcomes yet',completed=0)
        lock=preserve(ROOT); maplock=verify_map(ROOT); start=json.loads((out/'started.json').read_text())
        if start['git_revision']!=args.git_revision or start['lock_sha256']!=c.sha(ROOT/'experiments/e023_lock.json'): raise ValueError('Start provenance differs.')
        core=selection.core
        def frozen_inputs():
            core.verify_frozen_inputs(ROOT/'data/raw/train.csv',ROOT/'artifacts/splits',expected_data_sha=core.DATA_SHA,expected_manifest_sha=core.MANIFEST_SHA,expected_assignments_sha=core.ASSIGN_SHA)
        frozen_inputs()
        pairs,caches,receipts=verify_caches(ROOT,ROOT/'artifacts/e020_attempt01/map',maplock)
        if receipts['G7']['cache_sha256']!=CACHE: raise ValueError('G7 cache differs.')
        c.write_new(out/'cache_receipt.json',{'cache_sha256':CACHE,'pairs':60,'new_model_calls':0})
        frame=load_training_data(ROOT/'data/raw/train.csv')
        if len(frame)!=36696 or frame.QuestionId.nunique()!=15: raise ValueError('Population differs.')
        features=pd.read_csv(ROOT/'data/raw/train.csv',usecols=['QuestionText','MC_Answer'],dtype=str,keep_default_na=False)
        assignments=pd.read_csv(ROOT/'artifacts/splits/grouped_fold_assignments.csv',keep_default_na=False)
        lookup={pair:i for i,pair in enumerate(pairs)}; ids=np.array([lookup[c.normalize(q),c.normalize(a)] for q,a in zip(features.QuestionText,features.MC_Answer)])
        signals=np.array([r['scores'] for r in caches['G7']],dtype=np.float64)[ids]
        development=[]; policies=[]; routers=[]; crossfit=[]; review_counts=[]; memories={}
        for fold in range(5):
            roles=assignments[f'fold_{fold}'].to_numpy(); train,cal,ev=(np.flatnonzero(roles==r) for r in ('train','calibration','evaluation'))
            def fitted():
                nonlocal fits
                fits+=1; live.update(f'Training: classifier fits {fits}/200; fold {fold+1}/5',completed=fits+router_count+policy_count)
            def router_ready():
                nonlocal router_count
                router_count+=1; live.update(f'Routers: preparations {router_count}/20; fold {fold+1}/5',completed=fits+router_count+policy_count)
            def selected():
                nonlocal policy_count
                policy_count+=1; live.update(f'Development: policies {policy_count}/165; fold {fold+1}/5',completed=fits+router_count+policy_count)
            d,p,r,x,counts,memory=selection.prepare(frame.iloc[train],frame.iloc[cal],frame.iloc[ev][selection.FEATURES],ev,fold,signals[train],signals[cal],signals[ev],fitted,router_ready,selected)
            development.extend(d); policies.extend(p); routers.extend(r); crossfit.append(x); review_counts.extend(counts); memories[fold]=memory
        if policy_count!=165 or router_count!=20 or sorted(np.concatenate([m['positions'] for m in memories.values()]).tolist())!=list(range(36696)): raise ValueError('Preparation accounting.')
        freeze_sha=freeze(out,development,policies,routers,crossfit,review_counts,memories,fits)
        reproduce_private(ROOT,development,policies,memories)
        # Global truth barrier: every fold's predictions, policies and both mask families are frozen.
        truths={f:combined_label(frame.iloc[memories[f]['positions']]).to_numpy() for f in range(5)}
        unfiltered=[]; retained=[]
        for fold in range(5):
            u,r=old_metrics.evaluate(fold,memories[fold],truths[fold]); unfiltered.extend(u); retained.extend(r)
        reproduce_metrics(ROOT,unfiltered,retained)
        review=[]; automation=[]; ranking=[]
        for fold in range(5):
            live.update(f'Scoring: evaluation folds {fold}/5; global freeze and E022 reproduction passed',completed=385+fold)
            r,a,k=metrics.evaluate(fold,memories[fold],truths[fold]); review.extend(r); automation.extend(a); ranking.extend(k)
        panels=metrics.panels(review,automation,ranking,policies)
        live.update('Validating registered tables and preservation',completed=390,
            latest_metrics={r['arm']+' review benefit per100':r['mean'] for r in panels['review']['decisions']})
        verify_freeze(out,freeze_sha); preserve(ROOT); verify_caches(ROOT,ROOT/'artifacts/e020_attempt01/map',maplock); frozen_inputs(); no_failures(out)
        result={'experiment_id':'E023','status':'COMPLETED','development':development,'policies':policies,'routers':routers,'crossfit':crossfit,**panels,
            'resources':{'image_id':IMAGE,'wall_seconds':time.monotonic()-began},
            'integrity':{'git_revision':args.git_revision,'lock_sha256':c.sha(ROOT/'experiments/e023_lock.json'),'protocol_sha256':PROTOCOL,'reference_sha256':REFERENCE,
                'g7_cache_sha256':CACHE,'freeze_sha256':freeze_sha,'preserved_files':lock['preserved_files'],'preservation_verified':True,'global_freeze_verified':True,
                'e018_remains_blocked':True,'model_fits':200,'router_preparations':20,'router_fits':sum(r['fitting_calls'] for r in routers),'new_model_calls':0,'fit_warnings':0,
                'reproduced_model_folds':15,'reproduced_unfiltered_records':600,'reproduced_cutoff_records':900,'reproduced_policies':45,
                'policies':165,'review_masks':390,'seed':20260831,'uid':10001,'gid':10001,'row_level_public_outputs':False}}
        from .e023_publication import validate
        validate(result); c.write_new(out/'aggregate_results.json',result)
        c.write_new(out/'execution.json',{'status':'COMPLETED','results_sha256':c.sha(out/'aggregate_results.json'),'git_revision':args.git_revision,
            'lock_sha256':c.sha(ROOT/'experiments/e023_lock.json'),'finished_utc':datetime.now(timezone.utc).isoformat()})
        print('E023 completed; separate review and automation numerical results, interpretation withheld.',flush=True)


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--git-revision',required=True); parser.add_argument('--image-id',required=True)
    try: run(parser.parse_args())
    except BaseException as exc:
        c.write_new(ROOT/OUT/'statistics_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False}); raise


if __name__=='__main__': main()
