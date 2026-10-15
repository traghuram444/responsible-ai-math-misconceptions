"""E013 fixed response-permutation diagnostic; historical scientific code is reused."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import time

import numpy as np
import pandas as pd

from . import e011_context as core
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import write_new
from .e011_publication import same
from .e012_retry import sanitized_exception, verify_amendment
from .resilient_status import ResilientStatus
from .selective import _routing_order
from .threshold_transfer import support_masks, summarize_group

ROOT = Path(__file__).resolve().parents[2]
MODELS = ('E011', 'E012', 'frequency')
CONDITIONS = ('explanation_shuffle', 'pair_shuffle')
METRICS = ('map_at_3', 'top1_accuracy')
REPLICATES = 100
PERMUTATION_SEED = 20261014
ATTEMPT = 'e013_attempt01'


def mappings(metadata, positions, fold):
    """No labels accepted. Return local donor indices and private cell membership."""
    if set(metadata) != {'QuestionId', 'QuestionText', 'MC_Answer', 'StudentExplanation'}:
        raise ValueError('Label-free metadata columns required.')
    positions = np.asarray(positions)
    if len(positions) != len(metadata) or len(np.unique(positions)) != len(positions):
        raise ValueError('Unique source positions required.')
    if fold not in range(5): raise ValueError('Invalid fold.')
    q = metadata.QuestionId.to_numpy()
    text = metadata.QuestionText.fillna('').astype(str).to_numpy()
    answer = metadata.MC_Answer.fillna('').astype(str).to_numpy()
    for question in set(q):
        if len(set(text[q == question])) != 1: raise ValueError('Question text varies inside QuestionId.')
    result = {}
    for condition_id, condition in enumerate(CONDITIONS, 1):
        keys = [(int(q[i]), answer[i]) if condition_id == 1 else (int(q[i]),) for i in range(len(q))]
        cells = []
        for key in sorted(set(keys)):
            idx = np.array([i for i, k in enumerate(keys) if k == key], dtype=int)
            cells.append(idx[np.argsort(positions[idx], kind='stable')])
        donors = np.empty((REPLICATES, len(q)), dtype=np.int64)
        for r in range(REPLICATES):
            for cell_index, idx in enumerate(cells):
                rng = np.random.Generator(np.random.PCG64(np.random.SeedSequence(
                    [PERMUTATION_SEED, condition_id, fold, r, cell_index])))
                donors[r, idx] = rng.permutation(idx)
        donors.setflags(write=False)
        result[condition] = {'donors': donors, 'cells': cells}
    return result


def prepare(frame, assignments, model, fold, completed_fit):
    """Capture the last raw prediction without changing the historical prepare call."""
    original_predict = core.predict
    captured = {}
    def capture(fitted, part, arm):
        probability, classes = original_predict(fitted, part, arm)
        captured.update(raw=probability, fitted=fitted)
        return probability, classes
    try:
        core.predict = capture
        description, memory = core.prepare(frame, assignments, 'full_context',
            'logistic' if model == 'E011' else 'complement_nb', fold, completed_fit)
    finally:
        core.predict = original_predict
    memory.update(raw=captured['raw'], fitted=captured['fitted'])
    for key in ('raw', 'prob', 'positions', 'questions', 'classes', 'frequency_prob', 'frequency_classes'):
        memory[key].setflags(write=False)
    return description, memory


def check_reproduction(description, memory, truth, reference):
    expected = next(d for d in reference['development'] if d['arm'] == 'full_context' and d['fold'] == description['fold'])
    same(description, expected)
    for frequency in (False, True):
        actual = core.evaluate(description, memory, truth, frequency=frequency)
        expected = next(r for r in reference['records'] if r['fold'] == description['fold'] and
                        r['arm'] == ('frequency' if frequency else 'full_context'))
        same(actual, expected)


def repetition(values):
    a = np.asarray(values, dtype=float)
    if not len(a): return {'values': [], 'mean': None, 'sd': None, 'p025': None, 'p975': None}
    if a.ndim != 1 or not np.isfinite(a).all(): raise ValueError('Invalid aggregate replicates.')
    return {'values': a.tolist(), 'mean': float(a.mean()), 'sd': float(a.std(ddof=1)) if len(a) > 1 else None,
            'p025': float(np.percentile(a, 2.5, method='linear')), 'p975': float(np.percentile(a, 97.5, method='linear'))}


def rank_labels(prob, classes):
    return classes[np.argsort(-prob, axis=1)[:, :3]], classes[np.argmax(prob, axis=1)]


def row_scores(truth, top, predicted):
    hits = truth[:, None] == top
    rr = (hits / np.arange(1, top.shape[1] + 1)).sum(axis=1)
    return {'map_at_3': rr, 'top1_accuracy': (truth == predicted).astype(float)}


def calibration(truth, prob, classes, mask):
    g = summarize_group(truth, prob, classes, mask, np.ones(len(truth), dtype=bool), None)
    return {'n': g['original_n'], 'correct_n': g['correct_n'], 'incorrect_n': g['incorrect_n'],
            'accuracy': g['top1_accuracy'], 'mean_confidence': g['mean_confidence'],
            'confidence_minus_accuracy': g['mean_confidence'] - g['top1_accuracy'] if g['original_n'] else None,
            'ece': g['ece'], 'brier': g['brier'], 'ineligible_reasons': g['calibration_ineligible_reasons']}


def agreement(scores, baseline, top, prediction, freq_top, freq_prediction, mask):
    n = int(mask.sum())
    result = {'n': n, 'top1_agreement': float((prediction[mask] == freq_prediction[mask]).mean()) if n else None,
              'ordered_top3_agreement': float((top[mask] == freq_top[mask]).all(axis=1).mean()) if n else None}
    for metric in METRICS:
        difference = scores[metric][mask] - baseline[metric][mask]
        result[metric] = {'wins': int((difference > 0).sum()), 'ties': int((difference == 0).sum()),
            'losses': int((difference < 0).sum()),
            'gain': float(np.maximum(difference, 0).mean()) if n else None,
            'loss': float(np.maximum(-difference, 0).mean()) if n else None,
            'net': float(difference.mean()) if n else None}
    return result


def scopes(memory, truth):
    masks = support_masks(truth, memory['train_labels'], memory['train_questions'])
    result = []
    for question in [None, *sorted(set(memory['questions'].tolist()))]:
        scope = np.ones(len(truth), dtype=bool) if question is None else memory['questions'] == question
        for stratum in core.STRATA:
            result.append((question, stratum, scope & masks[stratum]))
    return result


def score_fold(model, fold, memory, truth, interventions, completed_replicate):
    prob, classes = memory['prob'], memory['classes']
    top, prediction = rank_labels(prob, classes)
    freq_top, freq_prediction = rank_labels(memory['frequency_prob'], memory['frequency_classes'])
    scores, baseline = row_scores(truth, top, prediction), row_scores(truth, freq_top, freq_prediction)
    domains = scopes(memory, truth)
    rows = []
    for question, stratum, mask in domains:
        n = int(mask.sum())
        rows.append({'model': model, 'fold': fold, 'question': question, 'stratum': stratum, 'n': n,
            'original': {metric: float(scores[metric][mask].mean()) if n else None for metric in METRICS},
            'shuffled': {condition: {metric: [] for metric in METRICS} for condition in CONDITIONS},
            'agreement': agreement(scores, baseline, top, prediction, freq_top, freq_prediction, mask),
            'calibration': {kind: calibration(truth, p, classes, mask)
                            for kind, p in (('raw', memory['raw']), ('scaled', prob))}})
    for condition in CONDITIONS:
        for r, donors in enumerate(interventions[condition]['donors']):
            changed = row_scores(truth, top[donors], prediction[donors])
            for row, (_, _, mask) in zip(rows, domains, strict=True):
                if row['n']:
                    for metric in METRICS:
                        value = float(changed[metric][mask].mean())
                        if model == 'frequency': same(value, row['original'][metric])
                        row['shuffled'][condition][metric].append(value)
            completed_replicate(condition, r)
    for row in rows:
        for condition in CONDITIONS:
            for metric in METRICS:
                values = row['shuffled'][condition][metric]
                row['shuffled'][condition][metric] = {'score': repetition(values),
                    'original_minus_shuffled': repetition([row['original'][metric] - v for v in values])}
    return rows


def opportunity(metadata, positions, fold, interventions, truth):
    q = metadata.QuestionId.to_numpy()
    inputs = core.input_text(metadata, 'full_context').to_numpy()
    result = []
    for condition in CONDITIONS:
        cells, donors = (interventions[condition][k] for k in ('cells', 'donors'))
        for question in [None, *sorted(set(q.tolist()))]:
            mask = np.ones(len(q), dtype=bool) if question is None else q == question
            local_cells = [c for c in cells if mask[c[0]]]
            mixed = sum(len(c) for c in local_cells if len(set(truth[c])) > 1)
            n = int(mask.sum())
            result.append({'fold': fold, 'question': question, 'condition': condition, 'n': n,
                'cells': len(local_cells), 'singleton_rows': sum(len(c) for c in local_cells if len(c) == 1),
                'movable_rows': sum(len(c) for c in local_cells if len(c) >= 2),
                'label_mixed_rows': mixed, 'label_mixed_share': mixed / n,
                'donor_changed_n': repetition([(positions[d][mask] != positions[mask]).sum() for d in donors]),
                'input_changed_n': repetition([(inputs[d][mask] != inputs[mask]).sum() for d in donors])})
    return result


def probability_diagnostic(model, fold, description, memory):
    raw, scaled, classes = memory['raw'], memory['prob'], memory['classes']
    rt, rp = rank_labels(raw, classes); st, sp = rank_labels(scaled, classes)
    t = description['temperature']
    return {'model': model, 'fold': fold, 'temperature': t,
        'calibration_supported_n': description['calibration_supported_n'],
        'lower_boundary': bool(abs(np.log(t) + 3) <= 1e-5), 'upper_boundary': bool(abs(np.log(t) - 3) <= 1e-5),
        'raw_at_clip_floor_fraction': float((raw <= 1e-12).mean()),
        'top1_change_fraction': float((rp != sp).mean()),
        'ordered_top3_change_fraction': float((rt != st).any(axis=1).mean())}


def summarize(rows):
    output = []
    for model in MODELS:
        for stratum in core.STRATA:
            parts = sorted([r for r in rows if r['model'] == model and r['stratum'] == stratum and r['question'] is None],
                           key=lambda r: r['fold'])
            if [r['fold'] for r in parts] != list(range(5)): raise ValueError('Missing fold grid.')
            item = {'model': model, 'stratum': stratum,
                'original': {m: core.stat([r['original'][m] for r in parts]) for m in METRICS}, 'shuffled': {},
                'calibration': {}, 'agreement': {}}
            for condition in CONDITIONS:
                item['shuffled'][condition] = {}
                for metric in METRICS:
                    item['shuffled'][condition][metric] = {}
                    for kind in ('score', 'original_minus_shuffled'):
                        reps = [r['shuffled'][condition][metric][kind] for r in parts]
                        values = [x['values'] for x in reps if x['values']]
                        item['shuffled'][condition][metric][kind] = {
                            'fold_stat': core.stat([x['mean'] for x in reps]),
                            'paired_replicates': repetition(np.asarray(values).mean(axis=0) if values else [])}
            for metric in ('accuracy', 'mean_confidence', 'confidence_minus_accuracy', 'ece', 'brier'):
                raw, scaled = ([r['calibration'][kind][metric] for r in parts] for kind in ('raw', 'scaled'))
                item['calibration'][metric] = {'raw': core.stat(raw), 'scaled': core.stat(scaled),
                    'raw_minus_scaled': core.stat([a - b if a is not None and b is not None else None for a, b in zip(raw, scaled)])}
            for metric in ('top1_agreement', 'ordered_top3_agreement'):
                item['agreement'][metric] = core.stat([r['agreement'][metric] for r in parts])
            for metric in METRICS:
                item['agreement'][metric] = {key: core.stat([r['agreement'][metric][key] for r in parts])
                                             for key in ('wins', 'ties', 'losses', 'gain', 'loss', 'net')}
            output.append(item)
    return output


def primary(rows):
    results = []
    for model in ('E011', 'E012'):
        parts = sorted([r for r in rows if r['model'] == model and r['stratum'] == 'all' and r['question'] is None], key=lambda r: r['fold'])
        delta = [r['shuffled']['explanation_shuffle']['map_at_3']['original_minus_shuffled']['mean'] for r in parts]
        results.append({'model': model, **core.meaningful(delta)})
    return {'models': results, 'concordant': all(r['criterion_met'] for r in results)}


def verify_lock(root, image_id, private=True):
    lock = json.loads((root / 'experiments/e013_lock.json').read_text())
    if image_id != lock['docker_image_id']: raise ValueError('Image identity changed.')
    verify_amendment(root, local_failed=root / 'artifacts/e012' if private else None)
    for group in ('files', 'preserved'):
        for name, sha in lock[group].items():
            p = (root / name).resolve()
            if not p.is_relative_to(root.resolve()) or core.canonical_sha(p) != sha: raise ValueError('Locked file changed.')
    if private:
        for name, sha in lock['private_evidence'].items():
            if file_sha256(root / name) != sha: raise ValueError('Historical attempt evidence changed.')
    return lock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-revision', required=True); parser.add_argument('--image-id', required=True)
    args = parser.parse_args()
    if not re.fullmatch('[0-9a-f]{40}', args.git_revision) or os.getuid() != 10001 or os.getgid() != 10001:
        raise ValueError('Pinned revision and non-root identity required.')
    lock = verify_lock(ROOT, args.image_id)
    output = ROOT / 'artifacts' / ATTEMPT
    if not output.is_dir() or any(output.iterdir()): raise ValueError('Empty new attempt required.')
    started, clock = datetime.now(timezone.utc).isoformat(), time.monotonic()
    write_new(output / 'attempt.json', {'experiment_id': 'E013', 'git_revision': args.git_revision, 'started_utc': started})
    live = ResilientStatus(output / 'live_status.json', experiment_id='E013', total=3146)
    try:
        with live:
            def frozen(): return core.verify_frozen_inputs(ROOT / 'data/raw/train.csv', ROOT / 'artifacts/splits',
                expected_data_sha=core.DATA_SHA, expected_manifest_sha=core.MANIFEST_SHA, expected_assignments_sha=core.ASSIGN_SHA)
            frozen()
            frame = load_training_data(ROOT / 'data/raw/train.csv')
            assignments = pd.read_csv(ROOT / 'artifacts/splits/grouped_fold_assignments.csv', keep_default_na=False)
            references = {m: json.loads((ROOT / f'results/{m}_aggregates.json').read_text()) for m in ('E011', 'E012')}
            prepared, maps, metadata = {}, {}, {}
            fits = 0
            for model in ('E011', 'E012'):
                for fold in range(5):
                    def fitted():
                        nonlocal fits
                        fits += 1
                        live.update(f'{model} reconstruction fold {fold + 1}/5; fits {fits}/145', completed=fits)
                    live.update(f'{model} reconstruction fold {fold + 1}/5; nested fitting')
                    prepared[model, fold] = prepare(frame, assignments, model, fold, fitted)
                    if model == 'E011':
                        memory = prepared[model, fold][1]
                        metadata[fold] = frame.iloc[memory['positions']][['QuestionId','QuestionText','MC_Answer','StudentExplanation']].copy()
                        maps[fold] = mappings(metadata[fold], memory['positions'], fold)
                    print(json.dumps({'phase': 'prepared', 'model': model, 'fold': fold, 'fits': fits}), flush=True)
            if fits != 145: raise ValueError('Fit count changed.')
            descriptions = {m: [prepared[m, f][0] for f in range(5)] for m in ('E011', 'E012')}
            write_new(output / 'frozen_development.json', {'development': descriptions, 'replicates': REPLICATES,
                'permutation_seed': PERMUTATION_SEED, 'model_fits': fits, 'all_predictions_and_mappings_frozen': True,
                'lock_sha256': file_sha256(ROOT / 'experiments/e013_lock.json')})
            freeze_sha = file_sha256(output / 'frozen_development.json')
            # Global barrier: no new held-out metrics were computed above this line.
            live.update('All models and mappings frozen; checking historical reproduction')
            truths = {f: combined_label(frame.iloc[prepared['E011', f][1]['positions']]).to_numpy() for f in range(5)}
            for (model, fold), (description, memory) in prepared.items():
                check_reproduction(description, memory, truths[fold], references[model])
            # No new diagnostic score is produced unless every reference gate passed.
            rows, opportunities, diagnostics = [], [], []
            completed = fits
            for fold in range(5):
                memory = prepared['E011', fold][1]
                opportunities.extend(opportunity(metadata[fold], memory['positions'], fold, maps[fold], truths[fold]))
                for model in MODELS:
                    if model == 'frequency':
                        memory = dict(prepared['E011', fold][1])
                        memory.update(prob=memory['frequency_prob'], raw=memory['frequency_prob'], classes=memory['frequency_classes'])
                    else:
                        description, memory = prepared[model, fold]
                        diagnostics.append(probability_diagnostic(model, fold, description, memory))
                    def scored(condition, replicate):
                        nonlocal completed
                        completed += 1
                        if replicate % 10 == 9:
                            live.update(f'{model} fold {fold + 1}/5; {condition} replicate {replicate + 1}/100', completed=completed)
                    part = score_fold(model, fold, memory, truths[fold], maps[fold], scored)
                    rows.extend(part)
                    all_row = next(r for r in part if r['question'] is None and r['stratum'] == 'all')
                    live.update(f'{model} fold {fold + 1}/5 scored', completed=completed,
                        latest_metrics={'Original MAP@3 latest fold': all_row['original']['map_at_3'],
                                        'Explanation delta latest fold': all_row['shuffled']['explanation_shuffle']['map_at_3']['original_minus_shuffled']['mean']})
            frozen(); verify_lock(ROOT, args.image_id)
            if freeze_sha != file_sha256(output / 'frozen_development.json'): raise ValueError('Development freeze changed.')
            payload = {'experiment_id':'E013', 'status':'COMPLETED', 'development': descriptions,
                'records':rows, 'aggregate':summarize(rows), 'opportunity':opportunities,
                'probability_diagnostics':diagnostics, 'primary':primary(rows),
                'provenance': {'git_revision':args.git_revision, 'image_id':args.image_id,
                    'lock_sha256':file_sha256(ROOT / 'experiments/e013_lock.json'), 'frozen_development_sha256':freeze_sha,
                    'started_utc':started, 'finished_utc':datetime.now(timezone.utc).isoformat(),
                    'wall_seconds':time.monotonic()-clock, 'model_fits':fits, 'fit_warnings':0,
                    'reproduction_model_folds':10, 'global_freeze_verified':True, 'preservation_verified':True,
                    'uid':os.getuid(), 'gid':os.getgid(), 'replicates':REPLICATES, 'permutation_seed':PERMUTATION_SEED,
                    'row_level_outputs':False, 'preserved_files':len(lock['preserved'])}}
            from .e013_publication import validate
            validate(payload)
            write_new(output / 'results.json', payload)
            live.update('Complete aggregate artifact serialized', completed=live.total)
        write_new(output / 'execution.json', {'status':'COMPLETED', 'results_sha256':file_sha256(output / 'results.json'),
            'monitor':live.diagnostics(), 'git_revision':args.git_revision, 'lock_sha256':file_sha256(ROOT / 'experiments/e013_lock.json')})
        print(json.dumps({'experiment_id':'E013','status':'COMPLETED','primary':payload['primary']}), flush=True)
    except BaseException as exc:
        write_new(output / 'failure.json', {'experiment_id':'E013','status':'FAILED','exception':sanitized_exception(exc)})
        raise RuntimeError('E013 stopped; no automatic retry; sanitized diagnostics only.') from None


if __name__ == '__main__': main()
