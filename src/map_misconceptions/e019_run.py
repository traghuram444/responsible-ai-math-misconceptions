"""E019 stage 2: historical reconstruction, global freeze, then aggregate scoring."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import time
import numpy as np
import pandas as pd
from . import e019_checker as checker
from . import e019_metrics as m
from . import e017 as previous
from .e019_integrity import preserve,verify_files
from .data_contract import combined_label,load_training_data
from .resilient_status import ResilientStatus
from .e011_publication import same

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/e019_attempt01'


def verify_cache(root,out,lock):
    path=root/'artifacts/e019_setup/catalogue.json'
    receipt=json.loads((out/'checker_completion.json').read_text())
    if receipt['status']!='COMPLETED' or checker.sha(path)!=lock['catalogue_sha256']:
        raise ValueError('Incomplete or changed checker inputs.')
    if checker.sha(out/'checker_cache_private.json')!=receipt['cache_sha256']:
        raise ValueError('Checker cache changed.')
    pairs=checker.load_catalogue(path); results=json.loads((out/'checker_cache_private.json').read_text())
    if len(pairs)!=len(results) or len(pairs)!=lock['pairs']: raise ValueError('Incomplete cache.')
    for r in results:
        if r['reason'] not in checker.REASONS: raise ValueError('Unknown processing reason.')
    return pairs,results,receipt


def freeze_predictions(out,prepared,plans,development,constant):
    files={}
    for fold in range(5):
        memory=prepared[fold][1]
        arrays={f'memory_{k}':v for k,v in memory.items() if isinstance(v,np.ndarray)}
        for arm in m.ARMS:
            for scale in ('raw','final'):
                arrays.update({f'{arm}_{scale}_{k}':v for k,v in plans[fold][arm][scale].items()})
            arrays[f'{arm}_order']=plans[fold][arm]['order']
        if any(v.flags.writeable for v in arrays.values()): raise ValueError('Mutable prediction state.')
        path=out/f'fold_{fold}_frozen_private.npz'
        with path.open('xb') as f: np.savez_compressed(f,**arrays)
        files[path.name]=checker.sha(path)
    checker.write_new(out/'frozen_development.json',{'development':development,'constant':constant,
        'private_prediction_sha256':files,'all_predictions_and_review_orders_frozen':True,'model_fits':50})
    return checker.sha(out/'frozen_development.json'),files


def reproduce(prepared,truths,root):
    ref11=json.loads((root/'results/E011_aggregates.json').read_text())
    ref16=json.loads((root/'results/E016_aggregates.json').read_text())
    ref17=json.loads((root/'results/E017_aggregates.json').read_text())
    for fold in range(5):
        d,mem,_=prepared[fold]
        m.prior.check_reproduction(d,mem,truths[fold],ref11)
        same({'learning_arm':'E011',**d},next(x for x in ref16['development'] if x['learning_arm']=='E011' and x['fold']==fold))
        for arm,model in (('F','frequency'),('L','E011')):
            memory=previous.frequency_memory(mem) if arm=='F' else mem
            expected=[{k:v for k,v in r.items() if k!='shuffled'} for r in ref16['records'] if r['model']==model and r['fold']==fold]
            same(previous.original_records(model,fold,memory,truths[fold]),expected)
            same(m.historical.category_records(model,fold,memory,truths[fold]),[r for r in ref16['category'] if r['model']==model and r['fold']==fold])
            same(m.core.evaluate(d,memory,truths[fold])['risk_coverage'],next(r['budgets'] for r in ref16['routing'] if r['model']==model and r['fold']==fold))
            top,pred=m.prior.rank_labels(memory['prob'],memory['classes'])
            records=previous.exact_records('F' if arm=='F' else 'E011',fold,m.prior.scopes(memory,truths[fold]),m.prior.row_scores(truths[fold],top,pred))
            same(records,[r for r in ref17['real_prediction']['records'] if r['arm']==records[0]['arm'] and r['fold']==fold])


def correctness_audit(prepared,truths,signals,pair_indices,reasons,constant):
    records=[]; control=[]; pairs=[]; unknown=[]
    for fold in range(5):
        memory=prepared[fold][1]; true=m.prefixes(truths[fold]); sig=signals[fold]
        for question in [None,*sorted(set(memory['questions'].tolist()))]:
            mask=np.ones(len(true),dtype=bool) if question is None else memory['questions']==question
            records.append(m.audit_record(fold,question,true[mask],sig[mask]))
            cm=m.audit_record(fold,question,true[mask],np.full(int(mask.sum()),int(constant[fold]['majority_correctness'])))
            control.append({'fold':fold,'question':question,'stratum':'all','n':cm['n'],
                'confusion_counts':[row[:2] for row in cm['confusion_counts']],
                'confusion_row_normalized':[row[:2] for row in cm['confusion_row_normalized']],
                'metrics':{k:cm['metrics'][k] for k in ('all_row_agreement','all_row_balanced_accuracy')}})
            ids=np.unique(pair_indices[fold][mask]); counts=Counter(reasons[i] for i in ids)
            pairs.append({'fold':fold,'question':question,'distinct_pairs':len(ids),
                'predicted_false':counts['false'],'predicted_true':counts['true'],
                'unknown':sum(v for k,v in counts.items() if k.startswith('unknown_'))})
            counts=Counter(reasons[i] for i in pair_indices[fold][mask])
            unknown.append({'fold':fold,'question':question,'n':int(mask.sum()),
                            'reason_counts':{r:counts[r] for r in checker.REASONS}})
    pooled=np.sum([r['confusion_counts'] for r in records if r['question'] is None],axis=0)
    return {'records':records,'aggregate':m.summarize(records,('stratum',)),
        'majority_records':control,'majority_aggregate':m.summarize(control,('stratum',)),
        'pair_counts':pairs,'row_reason_counts':unknown,'pooled_confusion_counts':pooled.tolist(),
        'pooled_confusion_row_normalized':[[float(x/row.sum()) if row.sum() else None for x in row] for row in pooled]}


def distribution(values):
    values=[x for x in values if x is not None]
    return {'n':len(values),'total':sum(values),'min':min(values) if values else None,
            'median':float(np.median(values)) if values else None,'max':max(values) if values else None}


def run(args):
    lock=json.loads((ROOT/'experiments/e019_lock.json').read_text())
    if args.image_id!=lock['statistical_image_id'] or os.getuid()!=10001 or os.getgid()!=10001:
        raise ValueError('Execution identity mismatch.')
    verify_files(ROOT,lock); preserve(ROOT)
    m.core.verify_frozen_inputs(ROOT/'data/raw/train.csv',ROOT/'artifacts/splits',
        expected_data_sha=m.core.DATA_SHA,expected_manifest_sha=m.core.MANIFEST_SHA,expected_assignments_sha=m.core.ASSIGN_SHA)
    pairs,cache,receipt=verify_cache(ROOT,OUT,lock)
    lookup={pair:i for i,pair in enumerate(pairs)}; reasons=[r['reason'] for r in cache]
    checker.write_new(OUT/'statistical_started.json',{'git_revision':args.git_revision,'image_id':args.image_id})
    started=time.monotonic(); fits=0
    with ResilientStatus(OUT/'statistics_status.json',experiment_id='E019',total=56) as live:
        frame=load_training_data(ROOT/'data/raw/train.csv')
        alignment_frame=pd.read_csv(ROOT/'data/raw/train.csv',usecols=['QuestionText','MC_Answer'],dtype=str,keep_default_na=False)
        assignments=pd.read_csv(ROOT/'artifacts/splits/grouped_fold_assignments.csv',keep_default_na=False)
        if len(frame)!=36696 or frame.QuestionId.nunique()!=15: raise ValueError('Dataset population changed.')
        prepared={}; plans={}; signals={}; pair_indices={}; constant=[]
        for fold in range(5):
            def fitted():
                nonlocal fits
                fits+=1
                live.update(f'Historical E011 fold {fold+1}/5; reconstruction fits {fits}/50',completed=fits)
            prepared[fold]=m.historical.prepare(frame,assignments,fold,'E011',fitted)
            memory=prepared[fold][1]
            features=alignment_frame.iloc[memory['positions']]
            ids=np.asarray([lookup[checker.normalize(q),checker.normalize(a)] for q,a in zip(features.QuestionText,features.MC_Answer)])
            signals[fold]=np.asarray([{'false':0,'true':1}.get(reasons[i],-1) for i in ids])
            signals[fold].setflags(write=False); ids.setflags(write=False); pair_indices[fold]=ids
            plans[fold],description=m.prepare_arms(memory,signals[fold],fold); constant.append(description)
        if fits!=50: raise ValueError('Fit count changed.')
        positions=np.concatenate([prepared[f][1]['positions'] for f in range(5)])
        if sorted(positions.tolist())!=list(range(len(frame))): raise ValueError('Evaluation row accounting.')
        development=[prepared[f][0] for f in range(5)]
        freeze_sha,frozen_files=freeze_predictions(OUT,prepared,plans,development,constant)
        # Evaluation truth boundary: all five folds, all arms, both scales and review orders frozen.
        truths={f:combined_label(frame.iloc[prepared[f][1]['positions']]).to_numpy() for f in range(5)}
        reproduce(prepared,truths,ROOT)
        live.update('All historical reproduction gates passed; scoring frozen arms',completed=51)
        collected=[[],[],[],[],[]]
        for fold in range(5):
            for dest,values in zip(collected,m.score_fold(fold,prepared[fold][1],truths[fold],plans[fold],signals[fold])):
                dest.extend(values)
            scores={r['arm']:r['metrics']['map_at_3'] for r in collected[0] if r['fold']==fold and r['question'] is None and r['stratum']=='all'}
            live.update(f'Aggregate scoring fold {fold+1}/5',completed=52+fold,
                latest_metrics={'F_A MAP@3':scores['F_A'],'F baseline MAP@3':scores['F'],'F_A minus F':scores['F_A']-scores['F']})
        result={'experiment_id':'E019','status':'COMPLETED','development':development,'constant_development':constant,
            **m.build_panels(*collected),
            'correctness_audit':correctness_audit(prepared,truths,signals,pair_indices,reasons,constant)}
        for name,digest in frozen_files.items():
            if checker.sha(OUT/name)!=digest: raise ValueError('Frozen predictions changed.')
        if checker.sha(OUT/'frozen_development.json')!=freeze_sha: raise ValueError('Development freeze changed.')
        verify_cache(ROOT,OUT,lock); verify_files(ROOT,lock); preserved=preserve(ROOT)
        result['resource_summary']={'pairs':len(pairs),'reason_counts':receipt['reason_counts'],
            'input_tokens':distribution(receipt['input_tokens']),'generated_tokens':distribution(receipt['generated_tokens']),
            'checker_seconds':receipt['wall_seconds'],'statistical_seconds':time.monotonic()-started,
            'solver_image_id':lock['solver_image_id'],'statistical_image_id':lock['statistical_image_id'],
            'model_manifest_sha256':checker.sha(ROOT/'experiments/e019_model_manifest.json'),
            'environment_lock_sha256':checker.sha(ROOT/'experiments/e019_environment_lock.json'),
            'cpu_count':os.cpu_count(),'architecture':platform.machine(),'solver_memory_limit_bytes':17179869184}
        result['integrity']={'git_revision':args.git_revision,'lock_sha256':checker.sha(ROOT/'experiments/e019_lock.json'),
            'cache_sha256':receipt['cache_sha256'],'frozen_development_sha256':freeze_sha,'preserved_files':preserved,
            'preservation_verified':True,'global_freeze_verified':True,'e018_remains_blocked':True,
            'fit_warnings':0,'model_fits':50,'reproduction_model_folds':10,'row_level_outputs':False,'uid':10001,'gid':10001}
        from .e019_publication import validate
        validate(result)
        checker.write_new(OUT/'aggregate_results.json',result)
        checker.write_new(OUT/'execution.json',{'status':'COMPLETED','results_sha256':checker.sha(OUT/'aggregate_results.json'),
            'git_revision':args.git_revision,'finished_utc':datetime.now(timezone.utc).isoformat()})
        print('E019 complete: all registered aggregate panels serialized; interpretation withheld.',flush=True)


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--git-revision',required=True); parser.add_argument('--image-id',required=True)
    args=parser.parse_args()
    try: run(args)
    except BaseException as exc:
        checker.write_new(OUT/'statistical_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False})
        raise


if __name__=='__main__': main()
