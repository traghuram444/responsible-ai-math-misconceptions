"""E014 approved nested probability shrinkage; no historical modules are edited."""
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
from sklearn.model_selection import GroupKFold
from . import e011_context as core
from . import e013 as prior
from .e013 import (repetition, rank_labels, row_scores, calibration, agreement, scopes,
                  probability_diagnostic)
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import write_new
from .e011_publication import same
from .e012_retry import sanitized_exception
from .resilient_status import ResilientStatus
from .selective import _routing_order

ROOT = Path(__file__).resolve().parents[2]
MODELS = ('mixture', 'E011', 'frequency')
CONDITIONS = ('explanation_shuffle',)
METRICS = prior.METRICS
REPLICATES = prior.REPLICATES
PERMUTATION_SEED = prior.PERMUTATION_SEED
WEIGHTS = (0., .10, .25, .50, .75, 1.)
ATTEMPT = 'e014_attempt01'
FEATURES = ['QuestionId', 'QuestionText', 'MC_Answer', 'StudentExplanation']


def mix(frequency, logistic, frequency_classes, logistic_classes, weight):
    if weight not in WEIGHTS or not np.array_equal(frequency_classes, logistic_classes):
        raise ValueError('Registered weight and matching training-only classes required.')
    if frequency.shape != logistic.shape: raise ValueError('Probability shape mismatch.')
    if weight == 0: return frequency
    if weight == 1: return logistic
    return (1 - weight) * frequency + weight * logistic


def select(train, completed_fit):
    splits = list(GroupKFold(3).split(train, combined_label(train), train.QuestionId.astype(str)))
    candidates, memories = [], []
    for params in core.e001.GRID:
        scores, parts = [], []
        for left, right in splits:
            inner_train, validation = train.iloc[left], train.iloc[right]
            fitted = core.fit_model(inner_train, 'full_context', 'logistic', params)
            prob, classes = core.predict(fitted, validation[FEATURES], 'full_context')
            fp, fc = core.e001.frequency_probabilities(inner_train, validation[FEATURES])
            mix(fp, prob, fc, classes, 0.)  # alignment gate, with no global class inventory
            truth = combined_label(validation).to_numpy()
            scores.append(core.map_at_3(truth, prob, classes))
            parts.append((fp, prob, fc, classes, truth))
            completed_fit()
        candidates.append({'params': {**params, 'ngram_range': list(params['ngram_range'])},
            'inner_fold_map_at_3': scores, 'inner_mean_map_at_3': float(np.mean(scores))})
        memories.append(parts)
    winner = max(range(len(candidates)), key=lambda i: candidates[i]['inner_mean_map_at_3'])
    weight_candidates = []
    for weight in WEIGHTS:
        scores = [core.map_at_3(y, mix(fp, p, fc, c, weight), c)
                  for fp, p, fc, c, y in memories[winner]]
        weight_candidates.append({'weight': weight, 'inner_fold_map_at_3': scores,
                                  'inner_mean_map_at_3': float(np.mean(scores))})
    selected = max(range(len(WEIGHTS)), key=lambda i: weight_candidates[i]['inner_mean_map_at_3'])
    return {'selected_index': winner, 'candidates': candidates}, {
        'selected_index': selected, 'selected_weight': WEIGHTS[selected], 'candidates': weight_candidates}


def calibrate_mixture(weight, cal_raw, eval_raw, cal_frequency, eval_frequency,
                      classes, frequency_classes, calibration_truth, logistic_temperature, logistic_scaled):
    cal_mix = mix(cal_frequency, cal_raw, frequency_classes, classes, weight)
    raw = mix(eval_frequency, eval_raw, frequency_classes, classes, weight)
    supported = int(np.isin(calibration_truth, classes).sum())
    if weight == 0:
        return raw, raw, 1., supported, 'unscaled_frequency'
    if weight == 1:
        return raw, logistic_scaled, logistic_temperature, supported, 'e011_temperature'
    temperature, count = core.e001.temperature_scale(calibration_truth, cal_mix, classes)
    return raw, core.e001.apply_temperature(raw, temperature), temperature, count, 'mixture_temperature'


def prepare_parts(train, calibration_frame, evaluation_features, positions, fold, completed_fit):
    if set(evaluation_features) != set(FEATURES): raise ValueError('Evaluation features must be label-free.')
    if [part.QuestionId.nunique() for part in (train, calibration_frame, evaluation_features)] != [9, 3, 3]:
        raise ValueError('Frozen role counts changed.')
    question_sets = [set(x.QuestionId) for x in (train, calibration_frame, evaluation_features)]
    if any(question_sets[i] & question_sets[j] for i in range(3) for j in range(i)):
        raise ValueError('Question roles overlap.')
    selection, weight_selection = select(train, completed_fit)
    fitted = core.fit_model(train, 'full_context', 'logistic',
                            selection['candidates'][selection['selected_index']]['params'])
    completed_fit()
    cal_raw, classes = core.predict(fitted, calibration_frame[FEATURES], 'full_context')
    raw, eval_classes = core.predict(fitted, evaluation_features, 'full_context')
    if not np.array_equal(classes, eval_classes): raise ValueError('Class alignment changed.')
    fp, fc = core.e001.frequency_probabilities(train, evaluation_features)
    cal_fp, cal_fc = core.e001.frequency_probabilities(train, calibration_frame[FEATURES])
    if not np.array_equal(fc, cal_fc): raise ValueError('Frequency classes changed.')
    cal_truth = combined_label(calibration_frame).to_numpy()
    temperature, supported = core.e001.temperature_scale(cal_truth, cal_raw, classes)
    scaled = core.e001.apply_temperature(raw, temperature)
    description = {'arm': 'full_context', 'model': 'logistic', 'fold': fold,
        'n_train': len(train), 'n_calibration': len(calibration_frame), 'n_evaluation': len(evaluation_features),
        'role_question_counts': [9, 3, 3], 'selection': selection, 'temperature': temperature,
        'calibration_supported_n': supported, 'fits': 10}
    memory = {'prob': scaled, 'raw': raw, 'classes': classes, 'frequency_prob': fp, 'frequency_classes': fc,
        'positions': np.asarray(positions), 'questions': evaluation_features.QuestionId.to_numpy(),
        'train_labels': combined_label(train).to_numpy(), 'train_questions': train.QuestionId.to_numpy()}
    weight = weight_selection['selected_weight']
    mr, mp, mt, ms, method = calibrate_mixture(weight, cal_raw, raw, cal_fp, fp, classes, fc,
                                               cal_truth, temperature, scaled)
    mixture = {**memory, 'prob': mp, 'raw': mr}
    frequency = {**memory, 'prob': fp, 'raw': fp, 'classes': fc}
    memories = {'E011': memory, 'mixture': mixture, 'frequency': frequency}
    for item in memories.values():
        item['order'] = _routing_order(item['prob'].max(axis=1), positions.tolist(), fold, core.SEED)
        item['frequency_order'] = _routing_order(fp.max(axis=1), positions.tolist(), fold, core.SEED)
        for value in item.values():
            if isinstance(value, np.ndarray): value.setflags(write=False)
    return {'E011': description, 'weight_selection': weight_selection, 'mixture_temperature': mt,
            'mixture_calibration_supported_n': ms, 'mixture_calibration_method': method}, memories


def prepare(frame, assignments, fold, completed_fit):
    roles = assignments[f'fold_{fold}'].to_numpy()
    positions = np.flatnonzero(roles == 'evaluation')
    return prepare_parts(frame.iloc[np.flatnonzero(roles == 'train')],
                         frame.iloc[np.flatnonzero(roles == 'calibration')],
                         frame.iloc[positions][FEATURES].copy(), positions, fold, completed_fit)


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
    def values(model):
        return [next(r['original']['map_at_3'] for r in rows if r['model'] == model
                     and r['fold'] == f and r['question'] is None and r['stratum'] == 'all') for f in range(5)]
    mixture = values('mixture')
    logistic_delta = [a-b for a,b in zip(mixture, values('E011'))]
    return {'frequency': core.meaningful([a-b for a,b in zip(mixture, values('frequency'))]),
            'E011': {**core.stat(logistic_delta), 'positive_folds': sum(x>0 for x in logistic_delta)}}


def contrasts(rows):
    result = []
    for row in rows:
        if row['model'] != 'mixture': continue
        base = {model: next(r for r in rows if r['model'] == model and
                 all(r[k] == row[k] for k in ('fold', 'question', 'stratum'))) for model in ('E011', 'frequency')}
        result.append({**{k: row[k] for k in ('fold','question','stratum','n')},
            'deltas': {model: {metric: row['original'][metric]-ref['original'][metric] if row['n'] else None
                               for metric in METRICS} for model,ref in base.items()},
            'contribution_change_from_E011': {key: row['agreement']['map_at_3'][key]-
                base['E011']['agreement']['map_at_3'][key] if row['n'] else None for key in ('gain','loss','net')}})
    return result


def routing(description, memory, truth, model):
    records = core.evaluate(description, memory, truth)
    return {'model': model, 'fold': description['fold'], 'budgets': records['risk_coverage']}


def contrast_summary(records):
    output = []
    for stratum in core.STRATA:
        parts = sorted([r for r in records if r['question'] is None and r['stratum']==stratum],key=lambda r:r['fold'])
        if [r['fold'] for r in parts]!=list(range(5)): raise ValueError('Paired contrast grid.')
        output.append({'stratum':stratum,
            'deltas':{m:{k:core.stat([r['deltas'][m][k] for r in parts]) for k in METRICS} for m in ('frequency','E011')},
            'contribution_change_from_E011':{k:core.stat([r['contribution_change_from_E011'][k] for r in parts]) for k in ('gain','loss','net')}})
    return output


def routing_summary(records):
    return [{'model': model, 'review_percent': b, 'metrics': {
        metric: core.stat([next(x for x in next(r for r in records if r['model'] == model and r['fold'] == f)['budgets']
                                if x['review_percent'] == b)['all'][metric] for f in range(5)])
        for metric in ('original_n','retained_n','top1_accuracy','map_at_3','risk','mean_confidence','ece','brier')}}
        for model in MODELS for b in (0,10,20,30,40,50)]


def reproduction_diagnostic(rows, opportunities, diagnostics, reference):
    for row in rows:
        expected = next(r for r in reference['records'] if all(r[k] == row[k] for k in ('model','fold','question','stratum')))
        expected = {**expected, 'shuffled': {'explanation_shuffle': expected['shuffled']['explanation_shuffle']}}
        same(row, expected)
    for row in opportunities:
        same(row, next(r for r in reference['opportunity'] if all(r[k] == row[k] for k in ('fold','question','condition'))))
    for row in diagnostics:
        same(row, next(r for r in reference['probability_diagnostics'] if r['model']=='E011' and r['fold']==row['fold']))


def verify_lock(root, image_id, private=True):
    lock = json.loads((root / 'experiments/e014_lock.json').read_text())
    if image_id != lock['docker_image_id']: raise ValueError('Image identity changed.')
    prior.verify_lock(root, image_id, private=private)
    approval = json.loads((root / 'experiments/e014_approval.json').read_text())
    if core.canonical_sha(root / 'docs/E014_PROTOCOL.md') != approval['protocol_sha256_lf']:
        raise ValueError('Approved protocol changed.')
    for group in ('files','preserved'):
        for name, sha in lock[group].items():
            path = (root/name).resolve()
            if not path.is_relative_to(root.resolve()) or core.canonical_sha(path) != sha:
                raise ValueError('Locked file changed.')
    if private:
        for name, sha in lock['private_evidence'].items():
            if file_sha256(root/name) != sha: raise ValueError('Prior attempt evidence changed.')
    return lock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-revision', required=True); parser.add_argument('--image-id', required=True)
    args = parser.parse_args()
    if not re.fullmatch('[0-9a-f]{40}', args.git_revision) or os.getuid()!=10001 or os.getgid()!=10001:
        raise ValueError('Exact revision and non-root identity required.')
    lock = verify_lock(ROOT, args.image_id)
    output = ROOT/'artifacts'/ATTEMPT
    if not output.is_dir() or any(output.iterdir()): raise ValueError('Empty new attempt required.')
    started, clock = datetime.now(timezone.utc).isoformat(), time.monotonic()
    write_new(output/'attempt.json', {'experiment_id':'E014','git_revision':args.git_revision,'started_utc':started})
    live = ResilientStatus(output/'live_status.json', experiment_id='E014', total=1551)
    try:
        with live:
            def frozen():
                return core.verify_frozen_inputs(ROOT/'data/raw/train.csv', ROOT/'artifacts/splits',
                    expected_data_sha=core.DATA_SHA, expected_manifest_sha=core.MANIFEST_SHA,
                    expected_assignments_sha=core.ASSIGN_SHA)
            frozen()
            frame = load_training_data(ROOT/'data/raw/train.csv')
            assignments = pd.read_csv(ROOT/'artifacts/splits/grouped_fold_assignments.csv', keep_default_na=False)
            ref11 = json.loads((ROOT/'results/E011_aggregates.json').read_text())
            ref13 = json.loads((ROOT/'results/E013_aggregates.json').read_text())
            prepared, maps, metadata = {}, {}, {}
            fits = 0
            for fold in range(5):
                def fitted():
                    nonlocal fits
                    fits += 1
                    live.update(f'Fold {fold+1}/5; completed fits {fits}/50', completed=fits)
                live.update(f'Fold {fold+1}/5; nested model and weight selection')
                prepared[fold] = prepare(frame, assignments, fold, fitted)
                memory = prepared[fold][1]['E011']
                metadata[fold] = frame.iloc[memory['positions']][FEATURES].copy()
                maps[fold] = mappings(metadata[fold], memory['positions'], fold)
                print(json.dumps({'phase':'prepared','fold':fold,'fits':fits}), flush=True)
            if fits != 50: raise ValueError('Fit count changed.')
            development = [prepared[f][0] for f in range(5)]
            write_new(output/'frozen_development.json', {'development':development,'model_fits':fits,
                'all_predictions_and_mappings_frozen':True,'lock_sha256':file_sha256(ROOT/'experiments/e014_lock.json')})
            freeze_sha = file_sha256(output/'frozen_development.json')
            # Global barrier: evaluation truths are accessed only after every development choice is frozen.
            truths = {f:combined_label(frame.iloc[prepared[f][1]['E011']['positions']]).to_numpy() for f in range(5)}
            live.update('All folds frozen; verifying historical full-record reproduction')
            for fold in range(5):
                d, memories = prepared[fold]
                prior.check_reproduction(d['E011'], memories['E011'], truths[fold], ref11)
            rows, opportunities, diagnostics, routes = [], [], [], []
            completed = fits
            # Reconstruct both controls and all E013 gates before any selected-mixture score.
            for model in ('E011','frequency','mixture'):
                for fold in range(5):
                    d, memories = prepared[fold]; memory = memories[model]
                    description = dict(d['E011'])
                    if model == 'mixture':
                        description.update(temperature=d['mixture_temperature'],
                                           calibration_supported_n=d['mixture_calibration_supported_n'])
                    elif model == 'frequency': description['temperature'] = 1.
                    diagnostics.append(probability_diagnostic(model,fold,description,memory))
                    def scored(condition, replicate):
                        nonlocal completed
                        completed += 1
                        if replicate % 10 == 9:
                            live.update(f'{model} fold {fold+1}/5; explanation shuffle {replicate+1}/100',completed=completed)
                    part = score_fold(model,fold,memory,truths[fold],maps[fold],scored)
                    rows.extend(part)
                    routes.append(routing(d['E011'],memory,truths[fold],model))
                    if model == 'E011':
                        opportunities.extend(opportunity(metadata[fold],memory['positions'],fold,maps[fold],truths[fold]))
                    if model == 'frequency' and fold == 4:
                        reproduction_diagnostic(rows,opportunities,[r for r in diagnostics if r['model']=='E011'],ref13)
                        live.update('All historical gates passed; selected-mixture scoring begins')
                    if model == 'mixture':
                        all_row = next(r for r in part if r['question'] is None and r['stratum']=='all')
                        baseline = next(r for r in rows if r['model']=='frequency' and r['fold']==fold and r['question'] is None and r['stratum']=='all')
                        live.update(f'Mixture fold {fold+1}/5 scored',completed=completed,latest_metrics={
                            'MAP@3 latest fold':all_row['original']['map_at_3'],
                            'Frequency latest fold':baseline['original']['map_at_3'],
                            'Delta latest fold':all_row['original']['map_at_3']-baseline['original']['map_at_3']})
            frozen(); verify_lock(ROOT,args.image_id)
            if freeze_sha!=file_sha256(output/'frozen_development.json'): raise ValueError('Freeze changed.')
            payload = {'experiment_id':'E014','status':'COMPLETED','development':development,'records':rows,
                'aggregate':summarize(rows),'primary':primary(rows),'contrasts':contrasts(rows),
                'contrast_aggregate':contrast_summary(contrasts(rows)),
                'opportunity':opportunities,'probability_diagnostics':diagnostics,
                'routing':routes,'routing_aggregate':routing_summary(routes),
                'provenance':{'git_revision':args.git_revision,'image_id':args.image_id,
                    'lock_sha256':file_sha256(ROOT/'experiments/e014_lock.json'),'frozen_development_sha256':freeze_sha,
                    'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),
                    'wall_seconds':time.monotonic()-clock,'model_fits':fits,'fit_warnings':0,'reproduction_model_folds':5,
                    'global_freeze_verified':True,'preservation_verified':True,'uid':os.getuid(),'gid':os.getgid(),
                    'replicates':REPLICATES,'permutation_seed':PERMUTATION_SEED,'row_level_outputs':False,
                    'preserved_files':len(lock['preserved'])}}
            from .e014_publication import validate
            validate(payload)
            write_new(output/'results.json',payload)
            live.update('Complete aggregate artifact serialized',completed=live.total)
        write_new(output/'execution.json',{'status':'COMPLETED','results_sha256':file_sha256(output/'results.json'),
            'monitor':live.diagnostics(),'git_revision':args.git_revision,'lock_sha256':file_sha256(ROOT/'experiments/e014_lock.json')})
        print(json.dumps({'experiment_id':'E014','status':'COMPLETED','primary':payload['primary']}),flush=True)
    except BaseException as exc:
        write_new(output/'failure.json',{'experiment_id':'E014','status':'FAILED','exception':sanitized_exception(exc)})
        raise RuntimeError('E014 stopped; no automatic retry; sanitized diagnostics only.') from None


if __name__ == '__main__': main()

