"""Locked E011/E012: input ablation and conditional complement classifier."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import time
import warnings

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import GroupKFold
from sklearn.naive_bayes import ComplementNB

from . import e001
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import write_new
from .frozen_validation import verify_frozen_inputs
from .live_status import LiveStatus
from .metrics import expected_calibration_error, map_at_3
from .metrics_v2 import union_label_brier_score
from .selective import _routing_order
from .threshold_transfer import support_masks, summarize_group

SEED = 20260831
ARMS = ('question_plus_explanation', 'full_context', 'question_plus_answer')
STRATA = ('all', 'unsupported', 'rare', 'frequent', 'well_supported')
CATEGORIES = ('False_Correct', 'False_Misconception', 'False_Neither', 'True_Correct', 'True_Misconception', 'True_Neither')
DATA_SHA = '0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c'
MANIFEST_SHA = '93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94'
ASSIGN_SHA = 'b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd'
NB_GRID = tuple({'ngram_range': span, 'min_df': 2, 'alpha': a} for span in ((2, 5), (3, 5)) for a in (.1, 1., 10.))


def canonical_sha(path):
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def checked_lock(root, image_id):
    lock = json.loads((root / 'experiments/e011_e012_lock.json').read_text(encoding='utf-8'))
    if lock['status'] != 'authorized_locked_before_execution' or image_id != lock['docker_image_id']:
        raise ValueError('Locked execution identity required.')
    for group in ('files', 'preserved'):
        for name, sha in lock[group].items():
            path = (root / name).resolve()
            if not path.is_relative_to(root.resolve()) or canonical_sha(path) != sha:
                raise ValueError('Locked or preserved input changed.')
    return lock


def input_text(frame, arm):
    def field(name): return frame[name].fillna('').astype(str)
    if arm == 'question_plus_explanation': return e001.text_input(frame, arm)
    answer = '[QUESTION] ' + field('QuestionText') + ' [ANSWER] ' + field('MC_Answer')
    if arm == 'full_context': return answer + ' [EXPLANATION] ' + field('StudentExplanation')
    if arm == 'question_plus_answer': return answer
    raise ValueError('Unknown input arm.')


def fit_model(train, arm, model, params):
    if model == 'logistic':
        vectorizer = TfidfVectorizer(ngram_range=tuple(params['ngram_range']), min_df=params['min_df'], sublinear_tf=True)
        classifier = LogisticRegression(C=params['C'], max_iter=2000, class_weight=None, random_state=SEED, n_jobs=1)
    elif model == 'complement_nb':
        vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=tuple(params['ngram_range']), min_df=2,
                                     max_features=100000, sublinear_tf=True)
        classifier = ComplementNB(alpha=params['alpha'], norm=True, fit_prior=False, force_alpha=True)
    else: raise ValueError('Unknown classifier.')
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        matrix = vectorizer.fit_transform(input_text(train, arm))
        classifier.fit(matrix, combined_label(train))
    if caught: raise RuntimeError('Classifier fit emitted a warning; no silent retry.')
    return vectorizer, classifier


def predict(fitted, frame, arm):
    vectorizer, classifier = fitted
    return classifier.predict_proba(vectorizer.transform(input_text(frame, arm))), classifier.classes_


def select_params(train, arm, model, completed_fit):
    grid = e001.GRID if model == 'logistic' else NB_GRID
    splits = list(GroupKFold(3).split(train, combined_label(train), train.QuestionId.astype(str)))
    candidates = []
    for params in grid:
        scores = []
        for left, right in splits:
            fit = fit_model(train.iloc[left], arm, model, params)
            prob, classes = predict(fit, train.iloc[right], arm)
            scores.append(map_at_3(combined_label(train.iloc[right]).to_numpy(), prob, classes))
            completed_fit()
        candidates.append({'params': {**params, 'ngram_range': list(params['ngram_range'])},
                           'inner_fold_map_at_3': scores, 'inner_mean_map_at_3': float(np.mean(scores))})
    winner = max(range(len(candidates)), key=lambda i: candidates[i]['inner_mean_map_at_3'])
    return {'selected_index': winner, 'candidates': candidates}


def prepare(frame, assignments, arm, model, fold, completed_fit):
    roles = assignments[f'fold_{fold}'].to_numpy()
    parts = {role: np.flatnonzero(roles == role) for role in ('train', 'calibration', 'evaluation')}
    train, cal, evaluation = (frame.iloc[parts[r]] for r in ('train', 'calibration', 'evaluation'))
    if [part.QuestionId.nunique() for part in (train, cal, evaluation)] != [9, 3, 3]:
        raise ValueError('Question roles changed.')
    selection = select_params(train, arm, model, completed_fit)
    fitted = fit_model(train, arm, model, selection['candidates'][selection['selected_index']]['params'])
    completed_fit()
    cal_prob, classes = predict(fitted, cal, arm)
    temperature, supported = e001.temperature_scale(combined_label(cal).to_numpy(), cal_prob, classes)
    prob, eval_classes = predict(fitted, evaluation, arm)
    if not np.array_equal(classes, eval_classes): raise ValueError('Class alignment changed.')
    prob = e001.apply_temperature(prob, temperature)
    # Frequency sees only training labels and evaluation length, not evaluation labels.
    fp, fc = e001.frequency_probabilities(train, evaluation)
    description = {'arm': arm, 'model': model, 'fold': fold, 'n_train': len(train), 'n_calibration': len(cal),
        'n_evaluation': len(evaluation), 'role_question_counts': [9, 3, 3], 'selection': selection,
        'temperature': temperature, 'calibration_supported_n': supported, 'fits': len(selection['candidates']) * 3 + 1}
    memory = {'prob': prob, 'classes': classes, 'frequency_prob': fp, 'frequency_classes': fc,
        'positions': parts['evaluation'], 'questions': evaluation.QuestionId.to_numpy(),
        'train_labels': combined_label(train).to_numpy(), 'train_questions': train.QuestionId.to_numpy()}
    # Fixed routing orders exist before any evaluation outcome is accessed.
    for key, p in (('order', prob), ('frequency_order', fp)):
        memory[key] = _routing_order(p.max(axis=1), memory['positions'].tolist(), fold, SEED)
        memory[key].setflags(write=False)
    for key in ('prob', 'frequency_prob'): memory[key].setflags(write=False)
    return description, memory


def stat(values):
    defined = [v for v in values if v is not None]
    return {'fold_values': values, 'mean': float(np.mean(defined)) if defined else None,
            'sd': float(np.std(defined, ddof=1)) if len(defined) > 1 else None, 'defined_folds': len(defined)}


def meaningful(delta):
    if len(delta) != 5 or not np.isfinite(delta).all(): raise ValueError('Five finite deltas required.')
    return {**stat(delta), 'positive_folds': sum(v > 0 for v in delta),
            'criterion_met': bool(np.mean(delta) >= .020 and sum(v > 0 for v in delta) >= 4)}


def primary(records, comparison):
    full = [next(r for r in records if r['fold'] == f and r['arm'] == 'full_context')['groups']['all']['map_at_3'] for f in range(5)]
    comparisons = []
    for label, control in comparison.items():
        vals = [full[f] - control[f] for f in range(5)]
        comparisons.append({'comparator': label, **meaningful(vals)})
    return {'comparisons': comparisons, 'criterion_met': all(c['criterion_met'] for c in comparisons)}


def category_summary(truth, prob, classes):
    truecat = np.asarray([x.split(':', 1)[0] for x in truth])
    classcat = np.asarray([x.split(':', 1)[0] for x in classes])
    if not set(truecat).issubset(CATEGORIES) or not set(classcat).issubset(CATEGORIES): raise ValueError('Unknown Category.')
    catprob = np.column_stack([prob[:, classcat == category].sum(axis=1) for category in CATEGORIES])
    predicted = np.asarray(CATEGORIES)[catprob.argmax(axis=1)]
    return {'n': len(truth), 'accuracy': float(np.mean(predicted == truecat)),
            'macro_f1_six': float(f1_score(truecat, predicted, labels=list(CATEGORIES), average='macro', zero_division=0))}


def metrics_group(truth, prob, classes, membership, retained):
    g = summarize_group(truth, prob, classes, membership, retained, None)
    keep = membership & retained
    g['macro_f1_union'] = (float(f1_score(truth[keep], classes[prob[keep].argmax(axis=1)], average='macro', zero_division=0))
                           if keep.any() else None)
    return g


def evaluate(description, memory, truth, *, frequency=False):
    p, c = (memory['frequency_prob'], memory['frequency_classes']) if frequency else (memory['prob'], memory['classes'])
    union_label_brier_score(truth, p, c)
    masks = support_masks(truth, memory['train_labels'], memory['train_questions'])
    all_rows = np.ones(len(truth), dtype=bool)
    def groups(scope): return {s: metrics_group(truth, p, c, m & scope, scope) for s, m in masks.items()}
    questions = []
    for question in sorted(set(memory['questions'].tolist())):
        mask = memory['questions'] == question
        questions.append({'QuestionId': int(question), 'groups': groups(mask), 'category': category_summary(truth[mask], p[mask], c)})
    order = memory['frequency_order'] if frequency else memory['order']
    routing = []
    for budget in (0, 10, 20, 30, 40, 50):
        retained = np.zeros(len(truth), dtype=bool)
        retained[order[:len(truth) - len(truth) * budget // 100]] = True
        routing.append({'review_percent': budget, 'all': metrics_group(truth, p, c, all_rows, retained)})
    return {'arm': 'frequency' if frequency else description['arm'], 'fold': description['fold'],
            'groups': groups(all_rows), 'category': category_summary(truth, p, c), 'questions': questions, 'risk_coverage': routing}


def answer_diagnostics(frame):
    tokenizer = TfidfVectorizer().build_analyzer()
    def counts(part):
        answers = part.MC_Answer.fillna('').astype(str)
        return {'n': len(part), 'blank_n': int(answers.str.strip().eq('').sum()),
                'zero_word_tokens_n': int(sum(not tokenizer(a) for a in answers))}
    return {'all': counts(frame), 'questions': [{'QuestionId': int(q), **counts(part)} for q, part in frame.groupby('QuestionId', sort=True)]}


def reference_gate(description, memory, truth, reference, *, frequency_only=False):
    prior = next(f for r in reference['results'] if r['variant'] == 'question_plus_explanation' for f in r['folds'] if f['fold'] == description['fold'])
    checks = 0
    for name, p, c in [('tfidf_logreg', memory['prob'], memory['classes']),
                       ('frequency_baseline', memory['frequency_prob'], memory['frequency_classes'])]:
        if frequency_only and name == 'tfidf_logreg': continue
        correct = c[p.argmax(axis=1)] == truth
        actual = {'map_at_3': map_at_3(truth, p, c), 'top1_accuracy': float(correct.mean()),
                  'ece_10_equal_width': expected_calibration_error(p.max(axis=1), correct, 10)}
        for metric, value in actual.items():
            expected = next(x['reference'] for x in prior['reproduction_comparisons'] if x['model'] == name and x['metric'] == metric)
            if not np.isclose(value, expected, rtol=0, atol=1e-10): raise ValueError('Historical baseline reproduction failed.')
            checks += 1
    return checks


def aggregate(records):
    names = ('top1_accuracy', 'map_at_3', 'macro_f1_union', 'risk', 'mean_confidence', 'ece', 'brier', 'original_n')
    output = []
    for arm in sorted({r['arm'] for r in records}):
        rows = sorted([r for r in records if r['arm'] == arm], key=lambda r: r['fold'])
        if [r['fold'] for r in rows] != list(range(5)): raise ValueError('Incomplete fold grid.')
        output.append({'arm': arm, 'groups': {s: {m: stat([r['groups'][s][m] for r in rows]) for m in names} for s in STRATA},
            'category': {m: stat([r['category'][m] for r in rows]) for m in ('accuracy', 'macro_f1_six')},
            'risk_coverage': [{'review_percent': b, 'metrics': {m: stat([r['risk_coverage'][i]['all'][m] for r in rows])
                for m in names}} for i, b in enumerate((0, 10, 20, 30, 40, 50))]})
    return output


def gate_e012(prior):
    from .e011_publication import validate_public_payload
    validate_public_payload(prior)
    if prior['experiment_id'] != 'E011' or prior['primary']['criterion_met']:
        raise ValueError('E012 requires a valid completed negative E011.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment', choices=('E011', 'E012'), required=True)
    parser.add_argument('--git-revision', required=True)
    parser.add_argument('--image-id', required=True)
    parser.add_argument('--e011-sha')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    lock = checked_lock(root, args.image_id)
    if not re.fullmatch('[0-9a-f]{40}', args.git_revision) or os.getuid() != 10001 or os.getgid() != 10001:
        raise ValueError('Non-root identity and exact revision required.')
    prior = None
    if args.experiment == 'E012':
        reference_path = root / 'results/E011_aggregates.json'
        if not args.e011_sha or file_sha256(reference_path) != args.e011_sha: raise ValueError('Pinned E011 reference required.')
        prior = json.loads(reference_path.read_text(encoding='utf-8'))
        gate_e012(prior)
    output = root / 'artifacts' / args.experiment.lower()
    output.mkdir(exist_ok=True)
    if any((output / name).exists() for name in ('attempt.json', 'results.json', 'failure.json')):
        raise ValueError('Existing attempt; no automatic rerun.')
    started, clock = datetime.now(timezone.utc).isoformat(), time.monotonic()
    write_new(output / 'attempt.json', {'experiment_id': args.experiment, 'git_revision': args.git_revision, 'started_utc': started})
    model, arms = ('logistic', ARMS) if args.experiment == 'E011' else ('complement_nb', ('full_context',))
    total_fits = 150 if args.experiment == 'E011' else 95
    try:
        with LiveStatus(output / 'live_status.json', experiment_id=args.experiment, total=total_fits + 5 * len(arms) + 1) as live:
            def frozen(): return verify_frozen_inputs(root / 'data/raw/train.csv', root / 'artifacts/splits',
                expected_data_sha=DATA_SHA, expected_manifest_sha=MANIFEST_SHA, expected_assignments_sha=ASSIGN_SHA)
            frozen()
            frame = load_training_data(root / 'data/raw/train.csv')
            assignments = pd.read_csv(root / 'artifacts/splits/grouped_fold_assignments.csv', keep_default_na=False)
            reference = json.loads((root / 'results/E006_aggregates.json').read_text(encoding='utf-8'))
            prepared, fits = [], 0
            for arm in arms:
                for fold in range(5):
                    def completed_fit():
                        nonlocal fits
                        fits += 1
                        live.update(f'{arm}: fold {fold + 1}/5; completed classifier fits', completed=fits)
                    live.update(f'{arm}: fold {fold + 1}/5; nested training/calibration')
                    prepared.append(prepare(frame, assignments, arm, model, fold, completed_fit))
                    print(json.dumps({'phase': 'prepared', 'arm': arm, 'fold': fold, 'completed_fits': fits}), flush=True)
            if fits != total_fits: raise ValueError('Unexpected fit count.')
            write_new(output / 'frozen_development.json', [d for d, _ in prepared])
            frozen_sha = file_sha256(output / 'frozen_development.json')
            live.update('All models, temperatures, probabilities and ranks frozen; evaluating', completed=fits)
            records, reproduction = [], 0
            for index, (description, memory) in enumerate(prepared):
                truth = combined_label(frame.iloc[memory['positions']]).to_numpy()
                if description['arm'] == arms[0]:
                    reproduction += reference_gate(description, memory, truth, reference, frequency_only=args.experiment == 'E012')
                    frequency = evaluate(description, memory, truth, frequency=True)
                    if prior is not None:
                        from .e011_publication import same
                        same(frequency, next(r for r in prior['records'] if r['arm'] == 'frequency' and r['fold'] == description['fold']))
                    records.append(frequency)
                row = evaluate(description, memory, truth)
                records.append(row)
                metric = row['groups']['all']['map_at_3']
                baseline = next(r['groups']['all']['map_at_3'] for r in records if r['arm'] == 'frequency' and r['fold'] == description['fold'])
                live.update(f'Evaluated {description["arm"]}: fold {description["fold"] + 1}/5', completed=fits + index + 1,
                    latest_metrics={'MAP@3 latest fold': metric, 'Frequency latest fold': baseline, 'Delta latest fold': metric - baseline})
            control = records if prior is None else prior['records']
            control_arm = 'question_plus_explanation' if prior is None else 'full_context'
            comparisons = {'frequency': [next(r for r in records if r['arm'] == 'frequency' and r['fold'] == f)['groups']['all']['map_at_3'] for f in range(5)],
                'question_plus_explanation' if prior is None else 'e011_full_context': [next(r for r in control if r['arm'] == control_arm and r['fold'] == f)['groups']['all']['map_at_3'] for f in range(5)]}
            frozen(); checked_lock(root, args.image_id)
            if frozen_sha != file_sha256(output / 'frozen_development.json'): raise ValueError('Development freeze changed.')
            payload = {'experiment_id': args.experiment, 'status': 'COMPLETED',
                'provenance': {'git_revision': args.git_revision, 'docker_image_id': args.image_id,
                    'lock_sha256': file_sha256(root / 'experiments/e011_e012_lock.json'), 'data_sha256': DATA_SHA,
                    'manifest_sha256': MANIFEST_SHA, 'assignments_sha256': ASSIGN_SHA, 'e011_sha256': args.e011_sha,
                    'started_utc': started, 'finished_utc': datetime.now(timezone.utc).isoformat(), 'wall_seconds': time.monotonic() - clock,
                    'uid': os.getuid(), 'gid': os.getgid(), 'seed': SEED, 'model_fits': fits, 'fit_warnings': 0,
                    'preserved_files': len(lock['preserved']), 'preservation_verified': True, 'global_freeze_verified': True,
                    'reproduction_checks': reproduction, 'frozen_development_sha256': frozen_sha, 'row_level_outputs': False},
                'development': [d for d, _ in prepared], 'answer_diagnostics': answer_diagnostics(frame),
                'records': records, 'aggregate': aggregate(records), 'primary_control_map_at_3': comparisons,
                'primary': primary(records, comparisons)}
            from .e011_publication import validate_public_payload
            validate_public_payload(payload)
            write_new(output / 'results.json', payload)
            live.update('Aggregate checks complete; results serialized', completed=live.total,
                        latest_metrics={'Primary criterion met': int(payload['primary']['criterion_met'])})
            print(json.dumps({'experiment_id': args.experiment, 'status': 'COMPLETED', 'primary': payload['primary']}), flush=True)
    except BaseException as exc:
        if not (output / 'failure.json').exists():
            write_new(output / 'failure.json', {'experiment_id': args.experiment, 'status': 'FAILED', 'error_type': type(exc).__name__})
        raise RuntimeError('Run stopped; no automatic retry. Private details suppressed.') from None


if __name__ == '__main__': main()
