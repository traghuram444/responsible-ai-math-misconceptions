"""Strict aggregate publication and independent consistency checks for E011/E012."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from . import e007_publication as schema
from .e011_context import (ARMS, NB_GRID, STRATA, aggregate, primary, stat)
from .e001 import GRID

N, I, NN = schema.N, schema.I, schema.NN
enum, listing, nullable = schema.enum, schema.listing, schema.nullable
STAT = {'fold_values': listing(NN), 'mean': NN, 'sd': NN, 'defined_folds': I}
GROUP = {**schema.GROUP, 'macro_f1_union': NN}
GROUPS = {s: GROUP for s in STRATA}
CATEGORY = {'n': I, 'accuracy': N, 'macro_f1_six': N}
METRICS = ('top1_accuracy', 'map_at_3', 'macro_f1_union', 'risk', 'mean_confidence', 'ece', 'brier', 'original_n')
BUDGET = enum(0, 10, 20, 30, 40, 50)


def same(actual, expected):
    if type(actual) is dict and type(expected) is dict:
        if set(actual) != set(expected): raise ValueError('Comparison keys differ.')
        for k in actual: same(actual[k], expected[k])
    elif type(actual) is list and type(expected) is list:
        if len(actual) != len(expected): raise ValueError('Comparison lengths differ.')
        for a, e in zip(actual, expected): same(a, e)
    elif isinstance(actual, (int, float)) and not isinstance(actual, bool) and isinstance(expected, (int, float)) and not isinstance(expected, bool):
        if not math.isfinite(actual) or not math.isfinite(expected) or abs(actual - expected) > 1e-10:
            raise ValueError('Numerical comparison differs.')
    elif type(actual) is not type(expected) or actual != expected: raise ValueError('Comparison differs.')


def payload_schema(experiment):
    logistic = experiment == 'E011'
    arms = (*ARMS, 'frequency') if logistic else ('full_context', 'frequency')
    params = {'ngram_range': listing(I), 'min_df': enum(2, 5), 'C': enum(.5, 1., 2.)} if logistic else {
        'ngram_range': listing(I), 'min_df': enum(2), 'alpha': enum(.1, 1., 10.)}
    comparators = ('frequency', 'question_plus_explanation') if logistic else ('frequency', 'e011_full_context')
    record = {'arm': enum(*arms), 'fold': enum(0, 1, 2, 3, 4), 'groups': GROUPS, 'category': CATEGORY,
        'questions': listing({'QuestionId': I, 'groups': GROUPS, 'category': CATEGORY}),
        'risk_coverage': listing({'review_percent': BUDGET, 'all': GROUP})}
    summary = {'arm': enum(*arms), 'groups': {s: {m: STAT for m in METRICS} for s in STRATA},
        'category': {m: STAT for m in ('accuracy', 'macro_f1_six')},
        'risk_coverage': listing({'review_percent': BUDGET, 'metrics': {m: STAT for m in METRICS}})}
    counts = {'n': I, 'blank_n': I, 'zero_word_tokens_n': I}
    provenance = {'git_revision': schema.pattern('[0-9a-f]{40}'), 'docker_image_id': schema.pattern('sha256:[0-9a-f]{64}'),
        **{k: schema.HASH for k in ('lock_sha256', 'data_sha256', 'manifest_sha256', 'assignments_sha256', 'frozen_development_sha256')},
        'e011_sha256': enum(None) if logistic else schema.HASH,
        'started_utc': schema.pattern('[0-9T:+.Z-]+'), 'finished_utc': schema.pattern('[0-9T:+.Z-]+'), 'wall_seconds': N,
        'uid': enum(10001), 'gid': enum(10001), 'seed': enum(20260831), 'model_fits': enum(150 if logistic else 95),
        'fit_warnings': enum(0), 'preserved_files': I, 'preservation_verified': enum(True), 'global_freeze_verified': enum(True),
        'reproduction_checks': enum(30 if logistic else 15), 'row_level_outputs': enum(False)}
    development = {'arm': enum(*(ARMS if logistic else ('full_context',))), 'model': enum('logistic' if logistic else 'complement_nb'),
        'fold': enum(0, 1, 2, 3, 4), 'n_train': I, 'n_calibration': I, 'n_evaluation': I, 'role_question_counts': listing(I),
        'selection': {'selected_index': I, 'candidates': listing({'params': params, 'inner_fold_map_at_3': listing(N), 'inner_mean_map_at_3': N})},
        'temperature': N, 'calibration_supported_n': I, 'fits': enum(10 if logistic else 19)}
    return {'experiment_id': enum(experiment), 'status': enum('COMPLETED'), 'provenance': provenance,
        'development': listing(development), 'answer_diagnostics': {'all': counts, 'questions': listing({'QuestionId': I, **counts})},
        'records': listing(record), 'aggregate': listing(summary),
        'primary_control_map_at_3': {c: listing(N) for c in comparators},
        'primary': {'comparisons': listing({'comparator': enum(*comparators), **STAT, 'positive_folds': I, 'criterion_met': schema.B}), 'criterion_met': schema.B}}


def check_group(g):
    n, total, correct, errors = (g[k] for k in ('retained_n', 'original_n', 'correct_n', 'incorrect_n'))
    if not 0 <= correct <= n <= total or correct + errors != n: raise ValueError('Count identity.')
    for name, value in [('top1_accuracy', correct / n if n else None), ('risk', errors / n if n else None),
                        ('coverage', n / total if total else None), ('review_fraction', 1 - n / total if total else None)]: same(g[name], value)
    reasons = (['n_below_200'] if n < 200 else []) + (['correct_below_20'] if correct < 20 else []) + (['incorrect_below_20'] if errors < 20 else [])
    if g['calibration_ineligible_reasons'] != reasons: raise ValueError('Calibration eligibility.')
    for k, bound in [('ece', 1), ('brier', 2), ('map_at_3', 1), ('macro_f1_union', 1), ('mean_confidence', 1)]:
        if g[k] is not None and not 0 <= g[k] <= bound: raise ValueError('Metric range.')
    for k in ('ece', 'brier'):
        if (g[k] is None) != bool(reasons): raise ValueError('Calibration missingness.')
    for k in ('map_at_3', 'macro_f1_union', 'mean_confidence'):
        if (g[k] is None) != (n == 0): raise ValueError('Empty metric missingness.')


def validate_public_payload(p):
    experiment = p.get('experiment_id')
    if experiment not in ('E011', 'E012'): raise ValueError('Unexpected experiment.')
    schema.validate_schema(p, payload_schema(experiment))
    arms = ARMS if experiment == 'E011' else ('full_context',)
    expected = {(arm, f) for arm in (*arms, 'frequency') for f in range(5)}
    records = {(r['arm'], r['fold']): r for r in p['records']}
    if set(records) != expected or len(p['records']) != len(expected): raise ValueError('Record grid.')
    if len(p['development']) != 5 * len(arms) or {(r['arm'], r['fold']) for r in p['development']} != {(a, f) for a in arms for f in range(5)}:
        raise ValueError('Development grid.')
    grid = GRID if experiment == 'E011' else NB_GRID
    for d in p['development']:
        if d['role_question_counts'] != [9, 3, 3] or d['n_train'] + d['n_calibration'] + d['n_evaluation'] != 36696:
            raise ValueError('Frozen role counts.')
        if not 0 <= d['calibration_supported_n'] <= d['n_calibration'] or not math.exp(-3) <= d['temperature'] <= math.exp(3):
            raise ValueError('Temperature contract.')
        candidates = d['selection']['candidates']
        if len(candidates) != len(grid): raise ValueError('Search grid changed.')
        for candidate, params in zip(candidates, grid):
            same(candidate['params'], {**params, 'ngram_range': list(params['ngram_range'])})
            scores = candidate['inner_fold_map_at_3']
            if len(scores) != 3 or any(not 0 <= x <= 1 for x in scores): raise ValueError('Inner scores invalid.')
            same(candidate['inner_mean_map_at_3'], sum(scores) / 3)
        if d['selection']['selected_index'] != max(range(len(candidates)), key=lambda i: candidates[i]['inner_mean_map_at_3']):
            raise ValueError('Inner selection changed.')
        if d['n_evaluation'] != records[d['arm'], d['fold']]['groups']['all']['original_n']: raise ValueError('Evaluation count changed.')
    question_sets = []
    for arm in (*arms, 'frequency'):
        question_ids = []
        if sum(records[arm, f]['groups']['all']['original_n'] for f in range(5)) != 36696: raise ValueError('Total evaluated count.')
        for f in range(5):
            row = records[arm, f]
            scopes = [row, *row['questions']]
            if len(row['questions']) != 3: raise ValueError('Question count.')
            question_ids.extend(q['QuestionId'] for q in row['questions'])
            for scope in scopes:
                schema.validate_groups(scope['groups'], None)
                for g in scope['groups'].values():
                    check_group(g)
                    if g['retained_n'] != g['original_n']: raise ValueError('Unfiltered group changed.')
                category = scope['category']
                if category['n'] != scope['groups']['all']['original_n'] or any(not 0 <= category[k] <= 1 for k in ('accuracy', 'macro_f1_six')):
                    raise ValueError('Category metric.')
            for s in STRATA:
                for k in ('original_n', 'retained_n', 'correct_n', 'incorrect_n'):
                    if sum(q['groups'][s][k] for q in row['questions']) != row['groups'][s][k]: raise ValueError('Question partition.')
            if [r['review_percent'] for r in row['risk_coverage']] != [0, 10, 20, 30, 40, 50]: raise ValueError('Budget grid.')
            same(row['risk_coverage'][0]['all'], row['groups']['all'])
            for r in row['risk_coverage']:
                check_group(r['all'])
                n = row['groups']['all']['original_n']
                if r['all']['original_n'] != n or r['all']['retained_n'] != n - n * r['review_percent'] // 100: raise ValueError('Review count.')
        if len(set(question_ids)) != 15: raise ValueError('Duplicate questions.')
        question_sets.append(set(question_ids))
    if any(q != question_sets[0] for q in question_sets): raise ValueError('Question arms differ.')
    diag = p['answer_diagnostics']
    if {q['QuestionId'] for q in diag['questions']} != question_sets[0] or len(diag['questions']) != 15: raise ValueError('Answer diagnostic questions.')
    for k in ('n', 'blank_n', 'zero_word_tokens_n'):
        if sum(q[k] for q in diag['questions']) != diag['all'][k]: raise ValueError('Answer diagnostic counts.')
    if diag['all']['n'] != 36696: raise ValueError('Answer diagnostic total.')
    for q in (diag['all'], *diag['questions']):
        if not 0 <= q['blank_n'] <= q['zero_word_tokens_n'] <= q['n']: raise ValueError('Answer token counts.')
    controls = p['primary_control_map_at_3']
    for label, vals in controls.items():
        if len(vals) != 5 or any(not 0 <= v <= 1 for v in vals): raise ValueError('Primary control values.')
        if label in ('frequency', 'question_plus_explanation'):
            same(vals, [records[label, f]['groups']['all']['map_at_3'] for f in range(5)])
    same(p['aggregate'], aggregate(p['records']))
    same(p['primary'], primary(p['records'], controls))


def render(p, previous=None):
    validate_public_payload(p)
    lines = [f"# {p['experiment_id']} complete numerical results", '',
        'Equal-fold means and sample SD are descriptive only. No inferential evidence or deployment claim.', '',
        '## Primary comparisons', '', '| Comparator | MAP@3 delta mean | SD | Positive folds | Criterion |', '|---|---:|---:|---:|---|']
    for c in p['primary']['comparisons']:
        lines.append(f"| {c['comparator']} | {c['mean']:.6f} | {c['sd']:.6f} | {c['positive_folds']}/5 | {c['criterion_met']} |")
    lines += ['', f"Overall primary criterion met: **{p['primary']['criterion_met']}**.", '', '## Aggregate exact labels and Category', '',
        '| Arm | MAP@3 | Accuracy | ECE | Corrected Brier | Category accuracy | Category macro-F1 (six) |', '|---|---:|---:|---:|---:|---:|---:|']
    def number(x): return 'null' if x is None else f'{x:.6f}'
    for a in p['aggregate']:
        g = a['groups']['all']
        vals = [g[m]['mean'] for m in ('map_at_3', 'top1_accuracy', 'ece', 'brier')] + [a['category'][m]['mean'] for m in ('accuracy', 'macro_f1_six')]
        lines.append('| ' + a['arm'] + ' | ' + ' | '.join(map(number, vals)) + ' |')
    lines += ['', '## All primary fold deltas', '', '| Comparator | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 |', '|---|---:|---:|---:|---:|---:|']
    for c in p['primary']['comparisons']: lines.append('| ' + c['comparator'] + ' | ' + ' | '.join(map(number, c['fold_values'])) + ' |')
    # Secondary paired comparisons are fixed in the protocols, not selected from results.
    controls = {'frequency': p}
    if p['experiment_id'] == 'E011': controls.update({'question_plus_explanation': p, 'question_plus_answer': p})
    elif previous is not None: controls['e011_full_context'] = previous
    lines += ['', '## Prespecified secondary paired differences', '', '| Comparator | Metric | Mean | SD | Fold values |', '|---|---|---:|---:|---|']
    for label, control in controls.items():
        arm = 'full_context' if label == 'e011_full_context' else label
        for metric in ('map_at_3', 'top1_accuracy', 'ece', 'brier'):
            diffs = []
            for fold in range(5):
                left = next(r for r in p['records'] if r['arm'] == 'full_context' and r['fold'] == fold)['groups']['all'][metric]
                right = next(r for r in control['records'] if r['arm'] == arm and r['fold'] == fold)['groups']['all'][metric]
                diffs.append(left - right if left is not None and right is not None else None)
            s = stat(diffs)
            lines.append(f"| {label} | {metric} | {number(s['mean'])} | {number(s['sd'])} | {', '.join(map(number, diffs))} |")
    lines += ['', '## All fold and question support groups', '',
        '| Arm | Fold | Question (all=pooled) | Stratum | n | Accuracy | MAP@3 | Macro-F1 union | ECE | Brier | Calibration exclusions |',
        '|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|']
    for row in p['records']:
        for scope in [{'QuestionId': 'all', 'groups': row['groups']}, *row['questions']]:
            for s, g in scope['groups'].items():
                values = [g[m] for m in ('top1_accuracy', 'map_at_3', 'macro_f1_union', 'ece', 'brier')]
                lines.append(f"| {row['arm']} | {row['fold']} | {scope['QuestionId']} | {s} | {g['original_n']} | " + ' | '.join(map(number, values)) + f" | {', '.join(g['calibration_ineligible_reasons']) or 'eligible'} |")
    lines += ['', '## All fold and question Category results', '', '| Arm | Fold | Question | n | Accuracy | Macro-F1 six |', '|---|---:|---|---:|---:|---:|']
    for row in p['records']:
        for q in [{'QuestionId': 'all', 'category': row['category']}, *row['questions']]:
            c = q['category']; lines.append(f"| {row['arm']} | {row['fold']} | {q['QuestionId']} | {c['n']} | {number(c['accuracy'])} | {number(c['macro_f1_six'])} |")
    lines += ['', '## Every fixed review budget and fold', '', '| Arm | Fold | Review % | Retained n | Risk | MAP@3 | ECE | Brier |', '|---|---:|---:|---:|---:|---:|---:|---:|']
    for row in p['records']:
        for r in row['risk_coverage']:
            g = r['all']; lines.append(f"| {row['arm']} | {row['fold']} | {r['review_percent']} | {g['retained_n']} | " + ' | '.join(number(g[k]) for k in ('risk', 'map_at_3', 'ece', 'brier')) + ' |')
    lines += ['', '## Aggregate input diagnostics', '', '| Question | n | Blank selected answer | Zero word tokens in selected answer |', '|---|---:|---:|---:|']
    for q in [{'QuestionId': 'all', **p['answer_diagnostics']['all']}, *p['answer_diagnostics']['questions']]:
        lines.append(f"| {q['QuestionId']} | {q['n']} | {q['blank_n']} | {q['zero_word_tokens_n']} |")
    lines += ['', '## Provenance', '', '```json', json.dumps(p['provenance'], indent=2), '```', '',
        'The accompanying aggregate JSON includes full five-value summary statistics, selection scores, temperatures, counts and eligibility. No row-level prediction, response, selected-answer text or fitted parameter is published.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment', choices=('E011', 'E012'))
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    p = json.loads((root / f'artifacts/{args.experiment.lower()}/results.json').read_text(encoding='utf-8'))
    previous = json.loads((root / 'results/E011_aggregates.json').read_text(encoding='utf-8')) if args.experiment == 'E012' else None
    if previous is not None:
        from .data_contract import file_sha256
        if file_sha256(root / 'results/E011_aggregates.json') != p['provenance']['e011_sha256']: raise ValueError('E011 reference changed.')
        same(p['primary_control_map_at_3']['e011_full_context'], [next(r for r in previous['records'] if r['arm'] == 'full_context' and r['fold'] == f)['groups']['all']['map_at_3'] for f in range(5)])
    report = render(p, previous)
    outputs = {f'results/{args.experiment}_aggregates.json': json.dumps(p, indent=2, allow_nan=False) + '\n',
               f'docs/{args.experiment}_RESULTS.md': report}
    for name, text in outputs.items():
        path = root / name
        if path.exists() and path.read_text(encoding='utf-8') != text: raise ValueError('Refusing to overwrite differing public result.')
    if not args.check:
        for name, text in outputs.items():
            path = root / name
            if not path.exists(): path.write_text(text, encoding='utf-8', newline='\n')
    print(json.dumps({'experiment_id': args.experiment, 'status': 'CHECKED' if args.check else 'PUBLISHED', 'primary': p['primary']}))


if __name__ == '__main__': main()
