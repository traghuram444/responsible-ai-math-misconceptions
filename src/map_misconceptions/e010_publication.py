"""E010 strict aggregate schema, arithmetic verification and numerical report."""
from __future__ import annotations

import json
from pathlib import Path

from . import e007_publication as old, e009_publication as prior
from .e009_metrics import HEAD_METRICS
from .e010_metrics import ALL_METRICS, BUDGETS, EXTRA_METRICS, PAIRED_METRICS, RULES, aggregate
from .e009_reliability import VARIANTS
from .threshold_transfer import STRATA

N, I, NN = old.N, old.I, old.NN
enum, listing, nullable = old.enum, old.listing, old.nullable
RULE, BUDGET = enum(*RULES), enum(*BUDGETS)
GROUP = {**old.GROUP, **{k: I if k.endswith('_n') else NN for k in EXTRA_METRICS}}
GROUPS = {s: GROUP for s in STRATA}
CONTEXT = {'variant': old.VARIANT, 'fold': enum(0, 1, 2, 3, 4), 'rule': RULE, 'review_percent': BUDGET}
RECORD = {**CONTEXT, 'evaluation': {'groups': GROUPS, 'questions': listing({'QuestionId': I, 'groups': GROUPS})},
          'reliability': nullable(prior.HEAD_EVAL)}
PLAN = {**CONTEXT, 'original_n': I, 'retained_n': I, 'reviewed_n': I}
SUMMARY = {'variant': old.VARIANT, 'rule': RULE, 'review_percent': BUDGET,
           'groups': {s: {m: prior.STAT for m in ALL_METRICS} for s in STRATA},
           'reliability': nullable({s: {m: prior.STAT for m in HEAD_METRICS} for s in STRATA})}
PAIR = {'variant': old.VARIANT, 'control': enum(*RULES[1:]), 'review_percent': enum(*BUDGETS[1:]),
        'folds': listing({'fold': enum(0, 1, 2, 3, 4), 'left_original_error_n': I, 'right_original_error_n': I,
            'left_review_fraction': N, 'right_review_fraction': N, 'differences': {m: NN for m in PAIRED_METRICS}}),
        'differences': {m: prior.STAT for m in PAIRED_METRICS}}
PROVENANCE = {k: v for k, v in prior.PROV.items() if k not in ('frozen_policies_sha256', 'all_cutoffs_frozen_before_evaluation',
    'e007_result_sha256', 'e008_result_sha256', 'development_policies_reproduced', 'evaluation_records_reproduced')}
PROVENANCE.update({'e009_result_sha256': old.HASH, 'frozen_plan_sha256': old.HASH,
    'all_masks_frozen_before_evaluation': enum(True), 'development_records_reproduced': enum(10),
    'evaluation_records_reproduced': enum(200), 'ranking_records_reproduced': enum(50)})
SCHEMA = {'experiment_id': enum('E010'), 'status': enum('COMPLETED'), 'provenance': PROVENANCE,
    'development': listing(prior.DEVELOPMENT), 'batch_counts': listing(PLAN),
    'reproduction': listing({'variant': old.VARIANT, 'fold': enum(0, 1, 2, 3, 4), 'evaluation_records': enum(20), 'ranking_records': enum(5)}),
    'records': listing(RECORD), 'aggregate': {'summaries': listing(SUMMARY), 'paired': listing(PAIR),
        'primary': listing({'variant': old.VARIANT, 'review_percent': enum(20), 'control': enum('support_aware'),
                           **prior.STAT, 'positive_folds': I, 'criterion_met': old.B})}}


def validate_groups(groups):
    old.validate_groups(groups, None)
    for g in groups.values():
        N, n, E, e, d, c = (g[k] for k in ('original_n', 'retained_n', 'original_error_n', 'incorrect_n', 'reviewed_n', 'reviewed_error_n'))
        if not (0 <= E <= N and e <= E and d == N - n and c == E - e and 0 <= c <= d and g['reviewed_correct_n'] == d - c):
            raise ValueError('Review partition mismatch.')
        for k, expected in [('remaining_errors_per_100', 100 * e / N if N else None),
                            ('captured_errors_per_100', 100 * c / N if N else None),
                            ('error_capture_fraction', c / E if E else None),
                            ('review_error_precision', c / d if d else None)]:
            old._same(g[k], expected)
        for k, upper in [('ece', 1), ('brier', 2), ('map_at_3', 1)]:
            if g[k] is not None and not 0 <= g[k] <= upper:
                raise ValueError('Metric out of range.')
    if groups['unsupported']['original_error_n'] != groups['unsupported']['original_n']:
        raise ValueError('Unsupported original count mismatch.')
    for k in EXTRA_METRICS[:4]:
        if sum(groups[s][k] for s in ('unsupported', 'rare', 'frequent')) != groups['all'][k] or groups['well_supported'][k] > groups['frequent'][k]:
            raise ValueError('Review support partition mismatch.')


def validate_public_payload(p):
    old.validate_schema(p, SCHEMA)
    context = {(v, f) for v in VARIANTS for f in range(5)}
    if len(p['development']) != 10 or {(d['variant'], d['fold']) for d in p['development']} != context:
        raise ValueError('Development grid mismatch.')
    if len(p['reproduction']) != 10 or {(c['variant'], c['fold']) for c in p['reproduction']} != context:
        raise ValueError('Reproduction grid mismatch.')
    fit_counts = []
    for d in p['development']:
        if d['reference_development']['role_counts'] != [9, 1, 2, 3] or d['router']['convergence_warnings']:
            raise ValueError('Development contract mismatch.')
        if [b['block'] for b in d['crossfit']['blocks']] != [0, 1, 2]:
            raise ValueError('Cross-fit grid mismatch.')
        fit_counts.extend([b['fits'] for b in d['crossfit']['blocks']] + [d['final_classifier_fits']])
        for policies in d['policies'].values():
            if [q['target_percent'] for q in policies] != [10, 20, 30]:
                raise ValueError('Historical policy target mismatch.')
            for policy in policies: prior._validate_policy(policy)
    if any(c['attempted'] != 10 or c['successful'] + c['failed'] != 10 for c in fit_counts):
        raise ValueError('Fitting count mismatch.')
    if p['provenance']['classifier_fits'] != {k: sum(c[k] for c in fit_counts) for k in prior.FITS}:
        raise ValueError('Total fitting mismatch.')
    if p['provenance']['router_fitting_calls'] != sum(d['router']['fitting_calls'] for d in p['development']):
        raise ValueError('Router count mismatch.')
    if p['provenance']['router_fallbacks'] != sum(d['router']['status'] != 'FITTED' for d in p['development']):
        raise ValueError('Router fallback mismatch.')
    key = lambda r: (r['variant'], r['fold'], r['rule'], r['review_percent'])
    plans = {key(r): r for r in p['batch_counts']}
    records = {key(r): r for r in p['records']}
    if len(plans) != 360 or len(p['batch_counts']) != 360 or set(plans) != set(records):
        raise ValueError('Frozen plan grid mismatch.')
    for r in p['records']:
        g, plan, qs = r['evaluation']['groups'], plans[key(r)], r['evaluation']['questions']
        validate_groups(g)
        for k in ('original_n', 'retained_n', 'reviewed_n'):
            if g['all'][k] != plan[k]: raise ValueError('Frozen plan count mismatch.')
        if plan['reviewed_n'] != plan['original_n'] * r['review_percent'] // 100:
            raise ValueError('Batch quota changed.')
        if len(qs) != 3 or len({q['QuestionId'] for q in qs}) != 3:
            raise ValueError('Question grid mismatch.')
        for q in qs: validate_groups(q['groups'])
        for s in STRATA:
            for k in ('original_n', 'retained_n', 'correct_n', 'incorrect_n', *EXTRA_METRICS[:4]):
                if sum(q['groups'][s][k] for q in qs) != g[s][k]:
                    raise ValueError('Question count partition mismatch.')
        h = r['reliability']
        if (h is not None) != (r['rule'] == 'learned_reliability'):
            raise ValueError('Reliability metrics on wrong rule.')
        if h is not None:
            if [q['QuestionId'] for q in h['questions']] != [q['QuestionId'] for q in qs]:
                raise ValueError('Reliability question mismatch.')
            for hg, cg in [(h['groups'], g), *[(a['groups'], b['groups']) for a, b in zip(h['questions'], qs)]]:
                for s in STRATA: prior._check_binary(hg[s], cg[s], ('mean_predicted_correctness', 'binary_brier', 'binary_ece'))
        zero = records[r['variant'], r['fold'], r['rule'], 0]
        for a, b in [(g, zero['evaluation']['groups']), *[(q['groups'], z['groups']) for q, z in zip(qs, zero['evaluation']['questions'])]]:
            for s in STRATA:
                if (a[s]['original_n'], a[s]['original_error_n']) != (b[s]['original_n'], b[s]['original_error_n']):
                    raise ValueError('Original denominator changed with budget.')
        if r['rule'] != 'frequency':
            baseline = records[r['variant'], r['fold'], 'learned_reliability', 0]
            if zero['evaluation'] != baseline['evaluation']:
                raise ValueError('Same-classifier zero-review results differ.')
        if r['review_percent'] > 0:
            previous = records[r['variant'], r['fold'], r['rule'], r['review_percent'] - 10]
            for a, b in [(g, previous['evaluation']['groups']), *[(q['groups'], z['groups']) for q, z in zip(qs, previous['evaluation']['questions'])]]:
                for s in STRATA:
                    for k in ('retained_n', 'correct_n', 'incorrect_n'):
                        if a[s][k] > b[s][k]: raise ValueError('Non-nested retained counts.')
    if p['aggregate'] != aggregate(p['records']):
        raise ValueError('Aggregate arithmetic mismatch.')


def report(p):
    validate_public_payload(p)
    def n(x): return 'null' if x is None else format(x, '.8g')
    def st(x): return f"{n(x['mean'])} ± {n(x['sd'])} [{x['defined_folds']}]"
    lines = ['# E010 review prioritization results', '', 'Status: **COMPLETED**. Numerical results only; interpretation awaits user review.', '',
        'Fixed-budget, retrospective batch routing on the reused 15-question benchmark. No human corrections are assumed. This does not change E009 or establish deployment safety. Equal-fold means ± sample SD [defined folds] are descriptive.', '',
        '[Complete aggregate-only JSON](../results/E010_aggregates.json) includes all five values for every fold summary, all question/stratum counts, paired differences, separate classifier/reliability calibration and eligibility reasons.', '',
        '## Primary comparison at 20% review', '',
        'Benefit = support-aware minus learned remaining errors per 100 original responses. Criterion: mean benefit >=2.0 and positive in at least 4/5 folds, separately for each arm.', '',
        '| Input | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] | Positive folds | Criterion met |', '|---|---|---|---|---|---|---|---|---|']
    for s in p['aggregate']['primary']:
        lines.append(f"| {s['variant']} | " + ' | '.join(n(x) for x in s['fold_values']) + f" | {st(s)} | {s['positive_folds']}/5 | {s['criterion_met']} |")
    metrics = ('review_fraction', 'remaining_errors_per_100', 'error_capture_fraction', 'review_error_precision', 'risk', 'map_at_3', 'ece', 'brier')
    lines += ['', '## Aggregate all-case results', '', '| Input | Rule | Review % | Actual review | Remaining errors/100 | Error capture | Review error precision | Retained risk | MAP@3 | Classifier ECE | Multiclass Brier |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for s in p['aggregate']['summaries']:
        lines.append(f"| {s['variant']} | {s['rule']} | {s['review_percent']} | " + ' | '.join(st(s['groups']['all'][m]) for m in metrics) + ' |')
    lines += ['', '## All fold and question results', '', 'Budgets apply to pooled folds; achieved per-question review fractions are outcomes, not enforced quotas. Frequency changes the classifier; other rules share predictions.', '',
        '| Input | Fold | Scope | Rule | Review % | N | Original errors | Retained | Retained errors | Reviewed errors | Actual review | Remaining errors/100 | Error capture | Review precision | Risk | MAP@3 | ECE | Brier |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in p['records']:
        for scope, gs in [('All', r['evaluation']['groups']), *[(q['QuestionId'], q['groups']) for q in r['evaluation']['questions']]]:
            g = gs['all']
            counts = [g[k] for k in ('original_n', 'original_error_n', 'retained_n', 'incorrect_n', 'reviewed_error_n')]
            lines.append(f"| {r['variant']} | {r['fold']} | {scope} | {r['rule']} | {r['review_percent']} | " + ' | '.join(n(x) for x in counts + [g[m] for m in metrics]) + ' |')
    lines += ['', '## Paired fold comparisons', '', 'Differences are learned minus control. Negative residual-error/risk differences favor learned; positive capture/precision differences favor learned. Frequency has a different original error set.', '',
        '| Input | Control | Review % | Fold | Learned original errors | Control original errors | Learned actual review | Control actual review | Remaining errors/100 difference | Capture difference | Precision difference | Risk difference |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for s in p['aggregate']['paired']:
        for f in s['folds']:
            vals = [f[k] for k in ('left_original_error_n', 'right_original_error_n', 'left_review_fraction', 'right_review_fraction')]
            lines.append(f"| {s['variant']} | {s['control']} | {s['review_percent']} | {f['fold']} | " + ' | '.join(n(x) for x in vals + [f['differences'][m] for m in PAIRED_METRICS]) + ' |')
        lines.append(f"| {s['variant']} | {s['control']} | {s['review_percent']} | Summary | — | — | — | — | " + ' | '.join(st(s['differences'][m]) for m in PAIRED_METRICS) + ' |')
    lines += ['', '## Support-stratum aggregate results', '', '| Input | Rule | Review % | Stratum | Original n | Retained n | Actual review | Remaining errors/100 | Error capture | Retained risk | ECE | Brier |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for s in p['aggregate']['summaries']:
        for group in STRATA[1:]:
            lines.append(f"| {s['variant']} | {s['rule']} | {s['review_percent']} | {group} | " + ' | '.join(st(s['groups'][group][m]) for m in ('original_n','retained_n','review_fraction','remaining_errors_per_100','error_capture_fraction','risk','ece','brier')) + ' |')
    lines += ['', '## Reliability calibration by fold and question', '', 'Correctness-probability diagnostics, distinct from classifier calibration. All three require n>=200, correct>=20 and incorrect>=20.', '',
        '| Input | Fold | Scope | Review % | n | Correct | Incorrect | Mean predicted correctness | Binary Brier | Binary ECE | Ineligible reasons |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for r in p['records']:
        if r['reliability'] is None: continue
        for scope, gs in [('All',r['reliability']['groups']), *[(q['QuestionId'],q['groups']) for q in r['reliability']['questions']]]:
            g = gs['all']
            lines.append(f"| {r['variant']} | {r['fold']} | {scope} | {r['review_percent']} | " + ' | '.join(n(g[m]) for m in HEAD_METRICS) + f" | {', '.join(g['ineligible_reasons']) or 'none'} |")
    v = p['provenance']
    lines += ['', '## Execution and verification', '', f"Runtime: {v['wall_seconds']:.3f} seconds. Pre-run revision: `{v['git_revision']}`. E009 reproduction: 10 development records, 200 evaluation records and 50 ranking records. Preserved files: {v['preserved_files']}. Classifier fits: {v['classifier_fits']['attempted']} attempted, {v['classifier_fits']['successful']} successful, {v['classifier_fits']['failed']} failed; warnings {v['classifier_fits']['warnings']}, including {v['classifier_fits']['convergence_warnings']} convergence warnings. Router fits: {v['router_fitting_calls']}; constant fallbacks: {v['router_fallbacks']}.", '', 'No row-level outputs or fitted parameters are serialized. No interpretation or new experiment is included.', '']
    return '\n'.join(lines)


def publish(root):
    p = json.loads((root / 'artifacts/e010/results.json').read_text(encoding='utf-8'))
    validate_public_payload(p)
    contents = {root / 'results/E010_aggregates.json': json.dumps(p, indent=2, allow_nan=False) + '\n',
                root / 'docs/E010_RESULTS.md': report(p)}
    for path, content in contents.items():
        if path.exists() and path.read_text(encoding='utf-8') != content:
            raise ValueError('Refusing to overwrite different published E010 results.')
    for path, content in contents.items():
        if not path.exists():
            with path.open('x', encoding='utf-8', newline='\n') as stream: stream.write(content)


if __name__ == '__main__':
    publish(Path(__file__).resolve().parents[2])
