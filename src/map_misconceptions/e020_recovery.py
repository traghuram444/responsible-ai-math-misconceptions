"""Report E020 from globally frozen predictions; never fit, tune or infer."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import time
import numpy as np
import pandas as pd
from . import e019_checker as c, e020_map_metrics as metrics
from .e016 import marginalize
from .e020_map_run import reproduce
from .e020_map_integrity import verify_caches, no_failures
from .e020_recovery_integrity import verify, SOURCE, OUT, LOCK
from .e020_map_publication import validate
from .data_contract import load_training_data, combined_label
from .resilient_status import ResilientStatus
from .e011_publication import same
from . import e020_selection as selection

ROOT = Path(__file__).resolve().parents[2]


def restore_category(memory):
    """Exact historical E011 view; no target, calibration or ranking dependency."""
    if 'category_raw' in memory:
        raise ValueError('Recovery applies only to the documented missing field.')
    category = marginalize(memory['raw'], memory['classes'])
    category.setflags(write=False)
    return {**memory, 'category_raw': category}


def load_frozen(source, frozen):
    expected = {f'fold_{f}_frozen_private.npz' for f in range(5)}
    if set(frozen['prediction_sha256']) != expected or frozen['model_fits'] != 50 or frozen['all_predictions_and_review_orders_frozen'] is not True:
        raise ValueError('Incomplete global freeze.')
    prepared, plans, ids = {}, {}, {}
    for fold in range(5):
        path = source/f'fold_{fold}_frozen_private.npz'
        if c.sha(path) != frozen['prediction_sha256'][path.name]:
            raise ValueError('Frozen predictions changed.')
        # These local archives are authenticated twice by verify() before use.
        with np.load(path, allow_pickle=True) as archive:
            arrays = {k: archive[k] for k in archive.files}
        for value in arrays.values(): value.setflags(write=False)
        memory = {k[len('memory_'):]: v for k,v in arrays.items() if k.startswith('memory_')}
        plans[fold] = {a: {
            scale: {k[len(a+'_'+scale+'_'):]: v for k,v in arrays.items() if k.startswith(a+'_'+scale+'_')}
            for scale in ('raw','final')} | {'order': arrays[a+'_order']} for a in metrics.ARMS}
        d = frozen['development'][fold]
        if d['fold'] != fold or frozen['ensemble_development'][fold]['fold'] != fold:
            raise ValueError('Frozen development order changed.')
        prepared[fold] = (d, restore_category(memory), None)
        ids[fold] = arrays['pair_indices']
    return prepared, plans, ids


def validate_alignment(prepared, plans, ids, frame, assignments, all_ids):
    positions = []
    for fold in range(5):
        memory = prepared[fold][1]
        roles = assignments[f'fold_{fold}'].to_numpy()
        expected = np.flatnonzero(roles == 'evaluation')
        train = np.flatnonzero(roles == 'train')
        for a,b in ((memory['positions'], expected),
                    (memory['questions'], frame.iloc[expected].QuestionId.to_numpy()),
                    (memory['train_labels'], combined_label(frame.iloc[train]).to_numpy()),
                    (memory['train_questions'], frame.iloc[train].QuestionId.to_numpy()),
                    (ids[fold], all_ids[expected]),
                    (memory['raw'], plans[fold]['L']['raw']['prob']),
                    (memory['prob'], plans[fold]['L']['final']['prob']),
                    (memory['frequency_prob'], plans[fold]['F']['final']['prob']),
                    (memory['order'], plans[fold]['L']['order']),
                    (memory['frequency_order'], plans[fold]['F']['order'])):
            if not np.array_equal(a,b): raise ValueError('Frozen alignment changed.')
        positions.extend(expected.tolist())
    if sorted(positions) != list(range(36696)):
        raise ValueError('Population accounting changed.')


def run(args):
    out = ROOT/OUT
    no_failures(out)
    lock, frozen, recovery = verify(ROOT)
    if args.image_id != lock['statistical_image_id'] or (os.getuid(),os.getgid()) != (10001,10001):
        raise ValueError('Execution identity changed.')
    start_receipt = json.loads((out/'started.json').read_text())
    if start_receipt['git_revision'] != args.git_revision or start_receipt['lock_sha256'] != c.sha(ROOT/LOCK):
        raise ValueError('Recovery start receipt changed.')
    source = ROOT/SOURCE
    started = time.monotonic()
    with ResilientStatus(out/'status.json', experiment_id='E020', total=5) as live:
        live.update('Recovery: verify saved predictions; zero new model calls or fits', completed=0)
        selection.core.verify_frozen_inputs(ROOT/'data/raw/train.csv',ROOT/'artifacts/splits',
            expected_data_sha=selection.core.DATA_SHA,expected_manifest_sha=selection.core.MANIFEST_SHA,
            expected_assignments_sha=selection.core.ASSIGN_SHA)
        pairs,caches,receipts = verify_caches(ROOT,source,lock)
        frozen_cache = {k:r['cache_sha256'] for k,r in receipts.items()}
        same(json.loads((source/'checker_caches_frozen.json').read_text()), {
            'cache_sha256':frozen_cache, 'catalogue_sha256':lock['catalogue_sha256'],
            'before_training_selection_and_agreement':True})
        prepared,plans,ids = load_frozen(source,frozen)
        frame = load_training_data(ROOT/'data/raw/train.csv')
        features = pd.read_csv(ROOT/'data/raw/train.csv',usecols=['QuestionText','MC_Answer'],dtype=str,keep_default_na=False)
        assignments = pd.read_csv(ROOT/'artifacts/splits/grouped_fold_assignments.csv',keep_default_na=False)
        lookup = {pair:i for i,pair in enumerate(pairs)}
        all_ids = np.array([lookup[c.normalize(q),c.normalize(a)] for q,a in zip(features.QuestionText,features.MC_Answer)])
        validate_alignment(prepared,plans,ids,frame,assignments,all_ids)
        # Only after authenticated global prediction freeze and alignment checks.
        truths = {f:combined_label(frame.iloc[prepared[f][1]['positions']]).to_numpy() for f in range(5)}
        collected = [[],[],[],[],[]]
        for fold in range(5):
            for dest,rows in zip(collected,metrics.score_fold(fold,prepared[fold][1],truths[fold],plans[fold])):
                dest.extend(rows)
            live.update(f'Recovery: frozen aggregate scoring fold {fold+1}/5',completed=fold+1)
        panels = metrics.build_panels(*collected)
        reproduce(prepared,truths,panels,frozen['ensemble_development'],ROOT)
        live.update('Recovery: all historical controls reproduced; validating publication',completed=5)
        result = {'experiment_id':'E020','status':'COMPLETED','development':frozen['development'],
            'ensemble_development':frozen['ensemble_development'],**panels,
            'correctness_audit':metrics.correctness(prepared,truths,ids,caches,frozen['ensemble_development'])}
        checkers = []
        from .e020_checker import REASONS
        for key,rows in caches.items():
            r = receipts[key]
            checkers.append({'model':key,'pairs':60,'reason_counts':{reason:sum(x['reason']==reason for x in rows) for reason in REASONS},
                'truncated_rationales':sum(x['truncated_rationale'] for x in rows),
                **{name:metrics.distribution([x[name] for x in rows]) for name in ('input_tokens','generated_tokens','readout_tokens','candidate_mass')},
                'generation_seconds':sum(x['generation_seconds'] for x in rows),'readout_seconds':sum(x['readout_seconds'] for x in rows),
                'checker_seconds':r['wall_seconds'],'peak_rss_bytes':r['peak_rss_bytes'],'container_peak_bytes':r['container_peak_bytes']})
        verify(ROOT); verify_caches(ROOT,source,lock); no_failures(out)
        elapsed = time.monotonic()-started
        original_elapsed = json.loads((source/'statistics_status.json').read_text())['elapsed_seconds']
        original_revision = json.loads((source/'started.json').read_text())['git_revision']
        result['resource_summary'] = {'checkers':checkers,'statistical_seconds':original_elapsed+elapsed,
            'solver_image_id':lock['solver_image_id'],'statistical_image_id':lock['statistical_image_id'],
            'environment_lock_sha256':c.sha(ROOT/'experiments/e020_environment_lock.json'),'solver_memory_limit_bytes':24*1024**3}
        result['integrity'] = {'git_revision':original_revision,'lock_sha256':c.sha(ROOT/'experiments/e020_map_lock.json'),
            'readiness_result_sha256':c.sha(ROOT/'results/E020_readiness.json'),'cache_sha256':frozen_cache,
            'frozen_development_sha256':recovery['frozen_development_sha256'],'preserved_files':664,
            'preservation_verified':True,'global_freeze_verified':True,'e018_remains_blocked':True,'fit_warnings':0,
            'model_fits':50,'reproduction_model_folds':15,'row_level_outputs':False,'uid':10001,'gid':10001}
        validate(result)
        c.write_new(out/'aggregate_results.json',result)
        c.write_new(out/'execution.json',{'experiment_id':'E020','status':'COMPLETED','phase':'reporting_recovery',
            'results_sha256':c.sha(out/'aggregate_results.json'),'original_git_revision':original_revision,
            'recovery_git_revision':args.git_revision,'recovery_lock_sha256':c.sha(ROOT/LOCK),
            'original_map_lock_sha256':c.sha(ROOT/'experiments/e020_map_lock.json'),
            'failed_attempt_inventory_sha256':recovery['failed_attempt_inventory_sha256'],
            'failed_attempt_files':recovery['failed_attempt_files'],
            'frozen_development_sha256':recovery['frozen_development_sha256'],
            'source_failure_types':['KeyError','CalledProcessError'],'failed_attempt_preserved':True,
            'category_view_reconstructed':True,'new_model_calls':0,'new_classifier_fits':0,
            'original_statistical_seconds':original_elapsed,'recovery_seconds':elapsed,
            'finished_utc':datetime.now(timezone.utc).isoformat()})
        print('Recovery completed; frozen predictions unchanged; all historical controls reproduced.',flush=True)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--git-revision',required=True); p.add_argument('--image-id',required=True)
    args=p.parse_args()
    try: run(args)
    except BaseException as exc:
        c.write_new(ROOT/OUT/'recovery_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False})
        raise


if __name__ == '__main__': main()
