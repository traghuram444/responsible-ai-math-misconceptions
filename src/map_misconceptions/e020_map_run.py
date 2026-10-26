"""Approved E020 MAP statistics: training/calibration, global freeze, then scoring."""
import argparse
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import time
import numpy as np
import pandas as pd
from . import e020_selection as selection,e020_map_selection as map_selection,e020_map_metrics as metrics,e019_checker as c
from .e020_checker import REASONS
from .e020_integrity import preserve_e020
from .e020_map_integrity import verify_map,verify_caches,no_failures,verify_readiness_evidence
from .e019_run import reproduce as historical_reproduction
from .e011_publication import same
from .data_contract import load_training_data,combined_label
from .resilient_status import ResilientStatus

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/e020_attempt01/map'


def freeze_predictions(out,prepared,plans,development,ensembles,ids,fits):
    if fits!=50 or set(prepared)!=set(range(5)) or set(plans)!=set(range(5)): raise ValueError('Incomplete global preparation.')
    files={}
    for fold in range(5):
        memory=prepared[fold][1]
        arrays={f'memory_{k}':v for k,v in memory.items() if isinstance(v,np.ndarray)}
        arrays['pair_indices']=ids[fold]
        for arm in metrics.ARMS:
            for scale in ('raw','final'): arrays.update({f'{arm}_{scale}_{k}':v for k,v in plans[fold][arm][scale].items()})
            arrays[f'{arm}_order']=plans[fold][arm]['order']
        if any(v.flags.writeable for v in arrays.values()): raise ValueError('Mutable prediction state.')
        path=out/f'fold_{fold}_frozen_private.npz'
        with path.open('xb') as stream: np.savez_compressed(stream,**arrays)
        files[path.name]=c.sha(path)
    c.write_new(out/'frozen_development_private.json',{'development':development,'ensemble_development':ensembles,
        'prediction_sha256':files,'all_predictions_and_review_orders_frozen':True,'model_fits':fits})
    return c.sha(out/'frozen_development_private.json'),files


def reproduce(prepared,truths,panels,ensembles,root):
    historical_reproduction(prepared,truths,root)
    ref=json.loads((Path(root)/'results/E019_aggregates.json').read_text())
    same([prepared[f][0] for f in range(5)],ref['development'])
    constants=[{k:r[k] for k in ('fold','majority_correctness','training_counts')} for r in ensembles]
    same(constants,ref['constant_development'])
    ref_exact=ref['original_input_controls']['records']+ref['constant_filter_control']['records']
    def matched(actual,expected,keys):
        ai={tuple(r[k] for k in keys):r for r in actual if r['arm'] in ('F','L','F_M')}
        bi={tuple(r[k] for k in keys):r for r in expected if r['arm'] in ('F','L','F_M')}
        if set(ai)!=set(bi): raise ValueError('Historical control grid differs.')
        for k in ai: same(ai[k],bi[k])
    matched(panels['exact']['records'],ref_exact,('arm','fold','question','stratum'))
    matched(panels['calibration']['records'],ref['calibration']['records'],('arm','fold','question','stratum','scale'))
    matched(panels['review']['records'],ref['review']['records'],('arm','fold','review_percent'))


def run(args):
    lock=verify_map(ROOT); no_failures(OUT.parent); preserve_e020(ROOT)
    verify_readiness_evidence(ROOT,lock)
    if args.image_id!=lock['statistical_image_id'] or (os.getuid(),os.getgid())!=(10001,10001): raise ValueError('Execution identity.')
    selection.core.verify_frozen_inputs(ROOT/'data/raw/train.csv',ROOT/'artifacts/splits',
        expected_data_sha=selection.core.DATA_SHA,expected_manifest_sha=selection.core.MANIFEST_SHA,expected_assignments_sha=selection.core.ASSIGN_SHA)
    pairs,caches,receipts=verify_caches(ROOT,OUT,lock)
    frozen_cache={key:r['cache_sha256'] for key,r in receipts.items()}
    c.write_new(OUT/'checker_caches_frozen.json',{'cache_sha256':frozen_cache,'catalogue_sha256':lock['catalogue_sha256'],
        'before_training_selection_and_agreement':True})
    c.write_new(OUT/'statistics_started.json',{'git_revision':args.git_revision,'image_id':args.image_id})
    started=time.monotonic(); fits=0
    with ResilientStatus(OUT/'statistics_status.json',experiment_id='E020',total=50) as live:
        frame=load_training_data(ROOT/'data/raw/train.csv')
        features=pd.read_csv(ROOT/'data/raw/train.csv',usecols=['QuestionText','MC_Answer'],dtype=str,keep_default_na=False)
        assignments=pd.read_csv(ROOT/'artifacts/splits/grouped_fold_assignments.csv',keep_default_na=False)
        if len(frame)!=36696 or frame.QuestionId.nunique()!=15: raise ValueError('Population changed.')
        lookup={pair:i for i,pair in enumerate(pairs)}
        all_ids=np.array([lookup[c.normalize(q),c.normalize(a)] for q,a in zip(features.QuestionText,features.MC_Answer)])
        all_scores={key:np.array([r['scores'] for r in rows],dtype=np.float64)[all_ids] for key,rows in caches.items()}
        all_fallback={key:np.array([r['reason']!='readout_completed' for r in rows],dtype=bool)[all_ids] for key,rows in caches.items()}
        prepared={}; plans={}; pair_indices={}; ensembles=[]
        for fold in range(5):
            roles=assignments[f'fold_{fold}'].to_numpy()
            positions={r:np.flatnonzero(roles==r) for r in ('train','calibration','evaluation')}
            def fitted():
                nonlocal fits
                fits+=1; live.update(f'Frozen training roles: fold {fold+1}/5; classifier fits {fits}/50',completed=fits)
            train,cal,ev=(positions[r] for r in ('train','calibration','evaluation'))
            d,mem,plan,ens=map_selection.prepare(frame.iloc[train],frame.iloc[cal],frame.iloc[ev][selection.FEATURES],
                ev,fold,all_scores['G7'][train],{k:p[cal] for k,p in all_scores.items()},
                {k:p[ev] for k,p in all_scores.items()},{k:p[cal] for k,p in all_fallback.items()},
                {k:p[ev] for k,p in all_fallback.items()},fitted)
            prepared[fold]=(d,mem,None); plans[fold]=plan; ensembles.append(ens)
            pair_indices[fold]=all_ids[ev].copy(); pair_indices[fold].setflags(write=False)
        positions=np.concatenate([prepared[f][1]['positions'] for f in range(5)])
        if sorted(positions.tolist())!=list(range(len(frame))): raise ValueError('Evaluation row accounting.')
        development=[prepared[f][0] for f in range(5)]
        freeze_sha,files=freeze_predictions(OUT,prepared,plans,development,ensembles,pair_indices,fits)
        # Global evaluation truth boundary: all arms/scales/orders for all five folds are frozen above.
        truths={f:combined_label(frame.iloc[prepared[f][1]['positions']]).to_numpy() for f in range(5)}
        collected=[[],[],[],[],[]]
        for fold in range(5):
            live.update(f'Global freeze complete; aggregate scoring fold {fold+1}/5',completed=50)
            for dest,rows in zip(collected,metrics.score_fold(fold,prepared[fold][1],truths[fold],plans[fold])): dest.extend(rows)
        panels=metrics.build_panels(*collected)
        reproduce(prepared,truths,panels,ensembles,ROOT)
        summary={r['arm']:r['metrics']['map_at_3']['mean'] for r in panels['exact']['aggregate'] if r['stratum']=='all'}
        live.update('Historical controls reproduced; validating registered aggregate panels',completed=50,
            latest_metrics={'H MAP@3':summary['H'],'F baseline MAP@3':summary['F'],'H minus F':summary['H']-summary['F']})
        result={'experiment_id':'E020','status':'COMPLETED','development':development,'ensemble_development':ensembles,
            **panels,'correctness_audit':metrics.correctness(prepared,truths,pair_indices,caches,ensembles)}
        for name,digest in files.items():
            if c.sha(OUT/name)!=digest: raise ValueError('Frozen predictions changed.')
        if c.sha(OUT/'frozen_development_private.json')!=freeze_sha: raise ValueError('Frozen development changed.')
        verify_caches(ROOT,OUT,lock); verify_map(ROOT); preserved=preserve_e020(ROOT); no_failures(OUT.parent)
        verify_readiness_evidence(ROOT,lock)
        checkers=[]
        for key,rows in caches.items():
            r=receipts[key]
            checkers.append({'model':key,'pairs':60,'reason_counts':{reason:sum(x['reason']==reason for x in rows) for reason in REASONS},
                'truncated_rationales':sum(x['truncated_rationale'] for x in rows),
                **{name:metrics.distribution([x[name] for x in rows]) for name in ('input_tokens','generated_tokens','readout_tokens','candidate_mass')},
                'generation_seconds':sum(x['generation_seconds'] for x in rows),'readout_seconds':sum(x['readout_seconds'] for x in rows),
                'checker_seconds':r['wall_seconds'],'peak_rss_bytes':r['peak_rss_bytes'],'container_peak_bytes':r['container_peak_bytes']})
        result['resource_summary']={'checkers':checkers,'statistical_seconds':time.monotonic()-started,
            'solver_image_id':lock['solver_image_id'],'statistical_image_id':lock['statistical_image_id'],
            'environment_lock_sha256':c.sha(ROOT/'experiments/e020_environment_lock.json'),'solver_memory_limit_bytes':24*1024**3}
        result['integrity']={'git_revision':args.git_revision,'lock_sha256':c.sha(ROOT/'experiments/e020_map_lock.json'),
            'readiness_result_sha256':c.sha(ROOT/'results/E020_readiness.json'),'cache_sha256':frozen_cache,
            'frozen_development_sha256':freeze_sha,'preserved_files':preserved,'preservation_verified':True,'global_freeze_verified':True,
            'e018_remains_blocked':True,'fit_warnings':0,'model_fits':50,'reproduction_model_folds':15,'row_level_outputs':False,'uid':10001,'gid':10001}
        from .e020_map_publication import validate
        validate(result); c.write_new(OUT/'aggregate_results.json',result)
        c.write_new(OUT/'execution.json',{'status':'COMPLETED','results_sha256':c.sha(OUT/'aggregate_results.json'),
            'git_revision':args.git_revision,'finished_utc':datetime.now(timezone.utc).isoformat()})
        print('E020 completed: all registered aggregates serialized; interpretation withheld.',flush=True)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--git-revision',required=True); p.add_argument('--image-id',required=True)
    args=p.parse_args()
    try: run(args)
    except BaseException as exc:
        c.write_new(OUT/'statistics_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False}); raise


if __name__=='__main__': main()
