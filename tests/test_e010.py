"""Synthetic E010 tests only; no MAP fitting or evaluation."""
from copy import deepcopy
import hashlib
import inspect
import json
from pathlib import Path

import numpy as np
import pytest

from map_misconceptions import e010, e009_metrics
from map_misconceptions.e009_reliability import RULES as OLD_RULES
from map_misconceptions.e010_metrics import (BUDGETS, RULES, aggregate, evaluate_fold, freeze_counts,
                                          primary_decision, retention_masks, review_group)
from map_misconceptions.e010_publication import report, validate_public_payload


def scores(n): return {r: np.full(n, .5) for r in OLD_RULES}


@pytest.mark.parametrize('n', [1, 3, 7, 10, 101, 333])
def test_integer_budgets_hash_ties_nested_and_immutable(n):
    rows = np.arange(n)
    masks = retention_masks(scores(n), rows, 2)
    expected = sorted(rows, key=lambda i: (hashlib.sha256(f'fold=2;source_row={i};seed=20260831'.encode()).hexdigest(), i))
    for rule in RULES:
        prev = np.ones(n, bool)
        for budget in BUDGETS:
            mask = masks[rule][budget]
            assert int((~mask).sum()) == n * budget // 100
            assert set(np.flatnonzero(mask)) == set(expected[:n - n * budget // 100])
            assert np.all(~mask | prev) and not mask.flags.writeable
            with pytest.raises(ValueError): mask[0] = False
            prev = mask


def test_permutation_invariance_and_exact_unrounded_scores():
    n = 101
    s = scores(n); s['learned_reliability'] = np.linspace(0, 1, n)
    perm = np.random.default_rng(1).permutation(n)
    a = retention_masks(s, np.arange(n), 0)
    b = retention_masks({r: v[perm] for r, v in s.items()}, np.arange(n)[perm], 0)
    for rule in RULES:
        for budget in BUDGETS: np.testing.assert_array_equal(a[rule][budget], b[rule][budget][np.argsort(perm)])
    assert set(np.flatnonzero(a['learned_reliability'][50])) == set(range(50, 101))


def test_hash_collision_falls_back_to_source_position(monkeypatch):
    class Collision:
        def hexdigest(self): return '0' * 64
    monkeypatch.setattr(hashlib, 'sha256', lambda *a, **k: Collision())
    masks = retention_masks(scores(10), np.arange(10)[::-1], 0)
    assert set(np.arange(10)[::-1][masks['hash_only'][50]]) == set(range(5))


@pytest.mark.parametrize('bad', ['duplicate', 'negative', 'float_position', 'nan', 'shape', 'missing', 'frequency', 'fold'])
def test_bad_routing_inputs_rejected(bad):
    s, rows, fold = scores(10), np.arange(10), 0
    if bad == 'duplicate': rows[0] = 1
    if bad == 'negative': rows[0] = -1
    if bad == 'float_position': rows = rows.astype(float)
    if bad == 'nan': s['raw_confidence'][0] = np.nan
    if bad == 'shape': s['raw_confidence'] = np.ones(9)
    if bad == 'missing': s.pop('raw_confidence')
    if bad == 'frequency': s['frequency'][0] = .6
    if bad == 'fold': fold = True
    with pytest.raises(ValueError): retention_masks(s, rows, fold)


def memory_fixture(fold=0):
    truth = np.tile(['a'] * 240 + ['b'] * 30 + ['unsupported'] * 30, 3)
    m = {'learned_prob': np.tile([.8, .2], (900, 1)), 'frequency_prob': np.tile([.8, .2], (900, 1)),
         'classes': np.array(['a', 'b']), 'frequency_classes': np.array(['a', 'b']),
         'train_labels': np.tile(['a'] * 80 + ['b'] * 20, 9), 'train_questions': np.repeat(np.arange(9), 100),
         'evaluation_questions': np.repeat(np.arange(fold * 3, fold * 3 + 3), 300),
         'evaluation_positions': np.arange(900), 'scores': {r: np.full(900, .8) for r in OLD_RULES}}
    m['scores']['learned_reliability'] = np.where(truth == 'a', .9, .2)
    return truth, m


def test_perfect_reverse_error_capture_and_original_denominators():
    truth, m = memory_fixture()
    d = {'variant': 'explanation_only', 'fold': 0}
    masks = retention_masks(m['scores'], m['evaluation_positions'], 0)
    rows = evaluate_fold(d, m, truth, masks)
    g = next(r for r in rows if r['rule'] == 'learned_reliability' and r['review_percent'] == 20)['evaluation']['groups']['all']
    assert (g['original_error_n'], g['reviewed_error_n'], g['incorrect_n']) == (180, 180, 0)
    assert g['error_capture_fraction'] == g['review_error_precision'] == 1
    assert g['remaining_errors_per_100'] == 0 and g['captured_errors_per_100'] == 20
    m['scores']['learned_reliability'] = 1 - m['scores']['learned_reliability']
    reverse = evaluate_fold(d, m, truth, retention_masks(m['scores'], m['evaluation_positions'], 0))
    g = next(r for r in reverse if r['rule'] == 'learned_reliability' and r['review_percent'] == 20)['evaluation']['groups']['all']
    assert g['reviewed_error_n'] == 0 and g['remaining_errors_per_100'] == 20


def test_label_changes_do_not_change_fixed_masks_or_review_counts():
    truth, m = memory_fixture()
    d = {'variant': 'explanation_only', 'fold': 0}
    masks = retention_masks(m['scores'], m['evaluation_positions'], 0)
    a = evaluate_fold(d, m, truth, masks)
    b = evaluate_fold(d, m, np.full(len(truth), 'unsupported'), masks)
    for x, y in zip(a, b):
        assert x['evaluation']['groups']['all']['retained_n'] == y['evaluation']['groups']['all']['retained_n']
        assert y['evaluation']['groups']['all']['correct_n'] == 0
    assert tuple(inspect.signature(retention_masks).parameters) == ('scores', 'source_positions', 'fold')


def test_empty_error_free_and_zero_review_nulls_and_calibration_boundary():
    p = np.tile([.8, .2], (200, 1)); c = np.array(['a', 'b']); all_rows = np.ones(200, bool)
    for truth, eligible in [(np.array(['a'] * 180 + ['b'] * 20), True), (np.array(['a'] * 181 + ['b'] * 19), False)]:
        g = review_group(truth, p, c, all_rows, all_rows)
        assert (g['ece'] is not None) == eligible
        assert g['review_error_precision'] is None and g['error_capture_fraction'] == 0
    free = review_group(np.full(200, 'a'), p, c, all_rows, all_rows)
    assert free['error_capture_fraction'] is None and free['remaining_errors_per_100'] == 0
    empty = review_group(np.full(200, 'a'), p, c, np.zeros(200, bool), all_rows)
    assert empty['remaining_errors_per_100'] is None and empty['reviewed_n'] == 0


def test_primary_exact_boundary_and_no_posthoc_arm_selection():
    assert primary_decision([2.] * 5)['criterion_met']
    assert not primary_decision([2. - 1e-12] * 5)['criterion_met']
    assert not primary_decision([5., 5., 5., -1., -1.])['criterion_met']
    assert primary_decision([3., 3., 3., 3., -1.])['criterion_met']


@pytest.fixture(scope='module')
def payload():
    from test_e009 import synthetic_payload
    old = synthetic_payload()
    records, plans, checks = [], [], []
    for d in old['development']:
        truth, m = memory_fixture(d['fold'])
        masks = retention_masks(m['scores'], m['evaluation_positions'], d['fold'])
        records.extend(evaluate_fold(d, m, truth, masks))
        plans.extend(freeze_counts(d['variant'], d['fold'], masks))
        checks.append(e010.reproduction_gate(d, m, truth, old))
    prov = {k: v for k, v in old['provenance'].items() if k not in ('frozen_policies_sha256','all_cutoffs_frozen_before_evaluation',
        'e007_result_sha256','e008_result_sha256','development_policies_reproduced','evaluation_records_reproduced')}
    prov.update({'frozen_plan_sha256': 'b'*64, 'e009_result_sha256': 'b'*64, 'all_masks_frozen_before_evaluation': True,
                 'development_records_reproduced': 10, 'evaluation_records_reproduced': 200, 'ranking_records_reproduced': 50})
    return {'experiment_id': 'E010', 'status': 'COMPLETED', 'provenance': prov, 'development': old['development'],
            'batch_counts': plans, 'reproduction': checks, 'records': records, 'aggregate': aggregate(records)}


def test_full_grid_primary_report_and_serialization(payload):
    validate_public_payload(payload)
    assert len(payload['records']) == 360
    assert sum(len(r['evaluation']['questions']) for r in payload['records']) == 1080
    assert all(s['criterion_met'] for s in payload['aggregate']['primary'])
    assert 'All fold and question results' in report(payload)
    json.dumps(payload, allow_nan=False)


@pytest.mark.parametrize('field', ['StudentExplanation', 'row_id', 'masks', 'scores', 'weights', 'coefficients'])
def test_private_fields_rejected(payload, field):
    p = deepcopy(payload); p['records'][0][field] = ['private']
    with pytest.raises(ValueError): validate_public_payload(p)


@pytest.mark.parametrize('mutation', ['grid','plan','counts','capture','primary','calibration','frequency','question','original'])
def test_corrupted_aggregate_rejected(payload, mutation):
    p = deepcopy(payload)
    g = p['records'][0]['evaluation']['groups']['all']
    if mutation == 'grid': p['records'].pop()
    if mutation == 'plan': p['batch_counts'][0]['retained_n'] -= 1
    if mutation == 'counts': g['reviewed_error_n'] += 1
    if mutation == 'capture': g['error_capture_fraction'] = .123
    if mutation == 'primary': p['aggregate']['primary'][0]['criterion_met'] = False
    if mutation == 'calibration': p['records'][0]['evaluation']['groups']['unsupported']['ece'] = 0.
    if mutation == 'frequency': p['records'][-1]['evaluation']['groups']['all']['map_at_3'] = .1
    if mutation == 'question': p['records'][0]['evaluation']['questions'][0]['QuestionId'] = 999
    if mutation == 'original': p['records'][1]['evaluation']['groups']['all']['original_error_n'] -= 1
    with pytest.raises((ValueError, KeyError)): validate_public_payload(p)


def test_reference_mismatch_stops():
    from test_e009 import synthetic_payload
    ref = synthetic_payload(); d = ref['development'][0]; truth, m = memory_fixture()
    e010.reproduction_gate(d, m, truth, ref)
    ref['ranking'][0]['all']['auroc'] -= 1e-8
    with pytest.raises(ValueError): e010.reproduction_gate(d, m, truth, ref)


def test_barrier_hash_lock_and_preservation_excludes_new_files(tmp_path):
    source = inspect.getsource(e010.main)
    assert source.index("write_new(output / 'frozen_plan.json'") < source.index("truth = combined_label(frame.iloc[memory['evaluation_positions']])") < source.index('reproduction_gate(description')
    root = Path(__file__).resolve().parents[1]
    assert e010.approved_config(root)['primary_review_percent'] == 20
    for name in ('docs/E010_PROTOCOL.md','experiments/e010_review.yaml','experiments/e010_approval.yaml'):
        dest = tmp_path/name; dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text((root/name).read_text(encoding='utf-8'), encoding='utf-8')
    (tmp_path/'experiments/e010_review.yaml').write_text('changed', encoding='utf-8')
    with pytest.raises(ValueError): e010.approved_config(tmp_path)
    files = e010.preservation_snapshot(root)
    assert 'src/map_misconceptions/e009.py' in files and 'results/E009_aggregates.json' in files
    assert not any('e010' in k.lower() for k in files)
