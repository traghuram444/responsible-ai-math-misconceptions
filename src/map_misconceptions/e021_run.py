"""Approved E021: prepare all folds, freeze, reproduce, then score and report."""
import argparse
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import time
import numpy as np
import pandas as pd
from . import e021_selection as selection,e021_metrics as metrics,e021_shuffle as shuffle
from . import e019_checker as c
from .e021_integrity import preserve,no_failures,IMAGE,PROTOCOL,REFERENCE,CACHE,OUT
from .e020_map_integrity import verify_map,verify_caches
from .e019_run import reproduce as historical_reproduction
from .e011_publication import same
from .data_contract import load_training_data,combined_label
from .resilient_status import ResilientStatus
ROOT=Path(__file__).resolve().parents[2]


def freeze(out,prepared,plans,ensembles,shuffles,fits):
    if fits!=50 or any(set(x)!=set(range(5)) for x in (prepared,plans,shuffles)): raise ValueError('Incomplete global preparation.')
    files={}
    for fold in range(5):
        arrays={'memory_'+k:v for k,v in prepared[fold][1].items()}
        arrays['shuffle_donors']=shuffles[fold]['donors']
        cells=np.empty(len(prepared[fold][1]['positions']),dtype=np.int64)
        for i,idx in enumerate(shuffles[fold]['cells']): cells[idx]=i
        cells.setflags(write=False); arrays['shuffle_cells']=cells
        for a in selection.ARMS:
            for scale in metrics.SCALES:
                arrays.update({f'{a}_{scale}_{k}':v for k,v in plans[fold][a][scale].items()})
            arrays[a+'_order']=plans[fold][a]['order']
        if any(v.flags.writeable for v in arrays.values()): raise ValueError('Mutable freeze state.')
        path=out/f'fold_{fold}_frozen_private.npz'
        with path.open('xb') as stream: np.savez_compressed(stream,**arrays)
        files[path.name]=c.sha(path)
    c.write_new(out/'frozen_development_private.json',{'development':[prepared[f][0] for f in range(5)],
        'ensemble_development':ensembles,'opportunities':[r for f in range(5) for r in shuffles[f]['opportunities']],
        'prediction_sha256':files,'model_fits':fits,'all_folds_predictions_orders_and_mappings_frozen':True})
    return c.sha(out/'frozen_development_private.json')


def verify_freeze(out,digest):
    path=out/'frozen_development_private.json'
    if c.sha(path)!=digest: raise ValueError('Frozen development changed.')
    frozen=json.loads(path.read_text())
    if frozen['model_fits']!=50 or frozen['all_folds_predictions_orders_and_mappings_frozen'] is not True:
        raise ValueError('Incomplete freeze receipt.')
    if set(frozen['prediction_sha256'])!={f'fold_{f}_frozen_private.npz' for f in range(5)}: raise ValueError('Frozen fold grid.')
    for name,sha in frozen['prediction_sha256'].items():
        if c.sha(out/name)!=sha: raise ValueError('Frozen prediction or mapping changed.')
    return frozen


def reproduce(prepared,plans,ensembles,truths,panels,root):
    historical_reproduction(prepared,truths,root)
    ref=json.loads((root/'results/E020_aggregates.json').read_text())
    same([prepared[f][0] for f in range(5)],ref['development'])
    frozen=json.loads((root/'artifacts/e020_attempt01/map/frozen_development_private.json').read_text())
    for fold in range(5):
        path=root/f'artifacts/e020_attempt01/map/fold_{fold}_frozen_private.npz'
        if c.sha(path)!=frozen['prediction_sha256'][path.name]: raise ValueError('Historical frozen arrays changed.')
        with np.load(path,allow_pickle=True) as data:
            mem=prepared[fold][1]
            for name in ('classes','positions','questions','train_labels','train_questions','frequency_classes'):
                if not np.array_equal(data['memory_'+name],mem[name]): raise ValueError('Historical alignment differs.')
            for a in selection.CONTROLS:
                same(ensembles[fold]['calibration'][a],ref['ensemble_development'][fold]['calibration'][a])
                if not np.array_equal(data[a+'_order'],plans[fold][a]['order']): raise ValueError('Historical review order differs.')
                for scale in metrics.SCALES:
                    for key,value in plans[fold][a][scale].items():
                        original=data[f'{a}_{scale}_{key}']
                        good=np.allclose(value,original,atol=1e-10,rtol=0) if key in ('prob','confidence') else np.array_equal(value,original)
                        if not good: raise ValueError('Historical prediction differs.')
    for panel in ('exact','calibration','review'):
        actual=[r for r in panels[panel]['records'] if r['arm'] in selection.CONTROLS and (panel!='exact' or r['scale']=='final')]
        if panel=='exact': actual=[{k:v for k,v in r.items() if k!='scale'} for r in actual]
        expected=[r for r in ref[panel]['records'] if r['arm'] in selection.CONTROLS]
        keys=('arm','fold','question','stratum')+(('scale',) if panel=='calibration' else ('review_percent',) if panel=='review' else ())
        ai={tuple(r[k] for k in keys):r for r in actual}; bi={tuple(r[k] for k in keys):r for r in expected}
        if set(ai)!=set(bi): raise ValueError('Historical reporting grid differs.')
        for key in ai: same(ai[key],bi[key])


def run(args):
    out=ROOT/OUT; no_failures(out)
    if args.image_id!=IMAGE or (os.getuid(),os.getgid())!=(10001,10001): raise ValueError('Execution identity differs.')
    started=time.monotonic(); fits=0
    with ResilientStatus(out/'status.json',experiment_id='E021',total=555) as live:
        live.update('Integrity preflight; no model fits or results yet',completed=0)
        lock=preserve(ROOT); maplock=verify_map(ROOT)
        start=json.loads((out/'started.json').read_text())
        if start['git_revision']!=args.git_revision or start['lock_sha256']!=c.sha(ROOT/'experiments/e021_lock.json'): raise ValueError('Start provenance differs.')
        core=selection.core
        core.verify_frozen_inputs(ROOT/'data/raw/train.csv',ROOT/'artifacts/splits',expected_data_sha=core.DATA_SHA,
            expected_manifest_sha=core.MANIFEST_SHA,expected_assignments_sha=core.ASSIGN_SHA)
        pairs,caches,receipts=verify_caches(ROOT,ROOT/'artifacts/e020_attempt01/map',maplock)
        if receipts['G7']['cache_sha256']!=CACHE: raise ValueError('Approved cache differs.')
        c.write_new(out/'cache_receipt.json',{'cache_sha256':CACHE,'pairs':60,'new_model_calls':0})
        frame=load_training_data(ROOT/'data/raw/train.csv')
        features=pd.read_csv(ROOT/'data/raw/train.csv',usecols=['QuestionText','MC_Answer'],dtype=str,keep_default_na=False)
        assignments=pd.read_csv(ROOT/'artifacts/splits/grouped_fold_assignments.csv',keep_default_na=False)
        if len(frame)!=36696 or frame.QuestionId.nunique()!=15: raise ValueError('Population differs.')
        lookup={pair:i for i,pair in enumerate(pairs)}
        ids=np.array([lookup[c.normalize(q),c.normalize(a)] for q,a in zip(features.QuestionText,features.MC_Answer)])
        signals=np.array([r['scores'] for r in caches['G7']],dtype=np.float64)[ids]
        fallback=np.array([r['reason']!='readout_completed' for r in caches['G7']],dtype=bool)[ids]
        prepared={}; plans={}; shuffles={}; ensembles=[]
        for fold in range(5):
            roles=assignments[f'fold_{fold}'].to_numpy()
            train,cal,ev=(np.flatnonzero(roles==r) for r in ('train','calibration','evaluation'))
            def fitted():
                nonlocal fits
                fits+=1; live.update(f'Training: classifier fits {fits}/50; fold {fold+1}/5',completed=fits)
            prepared[fold],plans[fold],ens=selection.prepare(frame.iloc[train],frame.iloc[cal],frame.iloc[ev][selection.FEATURES],ev,fold,
                signals[train],signals[cal],signals[ev],fallback[cal],fallback[ev],fitted)
            ensembles.append(ens)
            shuffles[fold]=shuffle.prepare(frame.iloc[ev][selection.FEATURES],ev,fold,signals[ev])
            shuffle.verify_invariance(plans[fold],shuffles[fold])
        if sorted(np.concatenate([prepared[f][1]['positions'] for f in range(5)]).tolist())!=list(range(36696)): raise ValueError('Evaluation accounting.')
        frozen_sha=freeze(out,prepared,plans,ensembles,shuffles,fits)
        # Global truth boundary: all choices, probabilities, orders and mappings are now frozen.
        truths={f:combined_label(frame.iloc[prepared[f][1]['positions']]).to_numpy() for f in range(5)}
        collected=[[],[],[],[],[]]
        for fold in range(5):
            for dest,rows in zip(collected,metrics.score_fold(fold,prepared[fold][1],truths[fold],plans[fold])): dest.extend(rows)
            live.update(f'Scoring original: fold {fold+1}/5; globally frozen predictions',completed=51+fold)
        panels=metrics.build_panels(*collected)
        reproduce(prepared,plans,ensembles,truths,panels,ROOT)
        primary=panels['comparisons']['decisions']['comparisons'][0]['mean']
        live.update('Historical controls reproduced; original-input panels complete',completed=55,
            latest_metrics={'Fixed C50 minus U50 MAP@3':primary})
        reps=0; shuffled=[]; opportunities=[]
        for fold in range(5):
            def completed():
                nonlocal reps
                reps+=1
                live.update(f'Exploratory explanation permutations: {reps}/500; fold {fold+1}/5',completed=55+reps)
            rows,opp=shuffle.score_fold(fold,prepared[fold][1],truths[fold],plans[fold],shuffles[fold],completed)
            shuffled.extend(rows); opportunities.extend(opp)
        if reps!=500: raise ValueError('Permutation accounting.')
        live.update('Verifying complete aggregate grids and preservation',completed=555)
        verify_freeze(out,frozen_sha); preserve(ROOT); verify_caches(ROOT,ROOT/'artifacts/e020_attempt01/map',maplock)
        core.verify_frozen_inputs(ROOT/'data/raw/train.csv',ROOT/'artifacts/splits',expected_data_sha=core.DATA_SHA,
            expected_manifest_sha=core.MANIFEST_SHA,expected_assignments_sha=core.ASSIGN_SHA)
        no_failures(out)
        result={'experiment_id':'E021','status':'COMPLETED','development':[prepared[f][0] for f in range(5)],
            'ensemble_development':ensembles,**panels,'explanation_shuffle':{'records':shuffled,'aggregate':shuffle.summarize(shuffled),'opportunity':opportunities},
            'resources':{'image_id':IMAGE,'wall_seconds':time.monotonic()-started},
            'integrity':{'git_revision':args.git_revision,'lock_sha256':c.sha(ROOT/'experiments/e021_lock.json'),'protocol_sha256':PROTOCOL,
                'e020_results_sha256':REFERENCE,'g7_cache_sha256':CACHE,'frozen_development_sha256':frozen_sha,
                'preserved_files':lock['preserved_files'],'preservation_verified':True,'global_freeze_verified':True,
                'e018_remains_blocked':True,'model_fits':50,'new_model_calls':0,'fit_warnings':0,'reproduction_model_folds':20,
                'shuffle_replicates_per_fold':100,'shuffle_seed':20261014,'seed':20260831,'row_level_outputs':False,'uid':10001,'gid':10001}}
        from .e021_publication import validate
        validate(result); c.write_new(out/'aggregate_results.json',result)
        c.write_new(out/'execution.json',{'status':'COMPLETED','results_sha256':c.sha(out/'aggregate_results.json'),
            'git_revision':args.git_revision,'lock_sha256':c.sha(ROOT/'experiments/e021_lock.json'),
            'finished_utc':datetime.now(timezone.utc).isoformat()})
        print('E021 complete: fixed and tuned results remain separate; interpretation withheld.',flush=True)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--git-revision',required=True); p.add_argument('--image-id',required=True); args=p.parse_args()
    try: run(args)
    except BaseException as exc:
        c.write_new(ROOT/OUT/'statistics_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False}); raise


if __name__=='__main__': main()
