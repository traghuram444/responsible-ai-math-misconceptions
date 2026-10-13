"""Synthetic E011/E012 checks only; no MAP data, model weights or research run."""
from copy import deepcopy
import inspect
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from map_misconceptions import e001
from map_misconceptions import e011_context as c
from map_misconceptions import e011_publication as pub
from map_misconceptions.e007_publication import validate_schema

ROOT = Path(__file__).resolve().parents[1]


def frame():
    rows = []
    for q in range(15):
        for i in range(8):
            rows.append({'QuestionId': q, 'QuestionText': f'synthetic exercise topic {q}',
                'MC_Answer': str(i % 2 + 1), 'StudentExplanation': 'synthetic correct method' if i % 2 else 'synthetic wrong method',
                'Category': 'True_Correct' if i % 2 else 'False_Misconception', 'Misconception': 'NA' if i % 2 else 'SyntheticError'})
    return pd.DataFrame(rows)


def assignments(f):
    return pd.DataFrame({'fold_0': np.where(f.QuestionId < 9, 'train', np.where(f.QuestionId < 12, 'calibration', 'evaluation'))})


def test_input_fields_exclude_labels_identifiers_and_preserve_reference():
    f = frame()
    for arm in c.ARMS:
        before = c.input_text(f, arm)
        changed = f.assign(Category='secret changed label', Misconception='unseen secret', QuestionId=-999, row_id='secret identifier')
        assert before.equals(c.input_text(changed, arm))
    assert c.input_text(f, 'question_plus_explanation').equals(e001.text_input(f, 'question_plus_explanation'))
    f.StudentExplanation = 'PRIVATE_SENTINEL'
    assert not c.input_text(f, 'question_plus_answer').str.contains('PRIVATE_SENTINEL').any()
    assert c.input_text(f, 'full_context').str.contains('[ANSWER]', regex=False).all()


@pytest.mark.parametrize('deltas,expected', [([.02] * 5, True), ([.019] * 5, False), ([.04, .04, .04, 0., 0.], False),
                                            ([.04, .04, .04, .04, -.01], True), ([0.] * 5, False)])
def test_meaningful_margin_and_sign_are_both_required(deltas, expected):
    assert c.meaningful(deltas)['criterion_met'] is expected


@pytest.mark.parametrize('deltas', [[], [1.] * 4, [float('nan')] * 5, [float('inf')] * 5])
def test_invalid_primary_values_stop(deltas):
    with pytest.raises(ValueError): c.meaningful(deltas)


def test_inner_selection_uses_only_disjoint_training_questions_and_first_tie(monkeypatch):
    f = frame().loc[lambda d: d.QuestionId < 9]
    fitted_questions, calls = [], []
    def fit(train, arm, model, params):
        fitted_questions.append(set(train.QuestionId))
        assert not any(q >= 9 for q in train.QuestionId)
        return set(train.QuestionId)
    def predict(training_questions, validation, arm):
        assert training_questions.isdisjoint(set(validation.QuestionId))
        return np.full((len(validation), 2), .5), np.array(['False_Misconception:SyntheticError', 'True_Correct:NA'])
    monkeypatch.setattr(c, 'fit_model', fit); monkeypatch.setattr(c, 'predict', predict)
    selected = c.select_params(f, 'full_context', 'logistic', lambda: calls.append(1))
    assert len(calls) == 9 and len(fitted_questions) == 9 and selected['selected_index'] == 0
    assert len(selected['candidates']) == 3


@pytest.mark.parametrize('model,arm,fit_count', [('logistic', 'full_context', 10), ('complement_nb', 'full_context', 19)])
def test_prepare_is_independent_of_evaluation_labels(model, arm, fit_count):
    f = frame(); calls = []
    d, memory = c.prepare(f, assignments(f), arm, model, 0, lambda: calls.append(1))
    changed = f.copy(); changed.loc[changed.QuestionId >= 12, ['Category', 'Misconception']] = ['SECRET', 'OUTCOME']
    d2, memory2 = c.prepare(changed, assignments(f), arm, model, 0, lambda: None)
    assert d == d2 and len(calls) == fit_count
    np.testing.assert_array_equal(memory['prob'], memory2['prob'])
    np.testing.assert_array_equal(memory['order'], memory2['order'])
    assert not memory['prob'].flags.writeable and not memory['order'].flags.writeable


def test_inner_vocabulary_excludes_unseen_text():
    f = frame().loc[lambda d: d.QuestionId < 9]
    fit = c.fit_model(f, 'full_context', 'logistic', e001.GRID[0])
    assert 'evaluationonlytoken' not in fit[0].vocabulary_
    evaluation = f.iloc[:2].copy(); evaluation.StudentExplanation = 'evaluationonlytoken'
    c.predict(fit, evaluation, 'full_context')
    assert 'evaluationonlytoken' not in fit[0].vocabulary_


def test_character_model_keeps_short_answer_information():
    f = frame().loc[lambda d: d.QuestionId < 9]
    fit = c.fit_model(f, 'full_context', 'complement_nb', c.NB_GRID[0])
    assert any('1' in term for term in fit[0].vocabulary_)
    diagnostics = c.answer_diagnostics(frame())
    assert diagnostics['all'] == {'n': 120, 'blank_n': 0, 'zero_word_tokens_n': 120}


def test_category_uses_six_fixed_labels_and_summed_probabilities():
    truth = np.array(['True_Correct:NA', 'False_Misconception:one'])
    classes = np.array(['False_Misconception:one', 'True_Correct:NA', 'False_Misconception:two'])
    probs = np.array([[.3, .4, .3], [.6, .3, .1]])
    result = c.category_summary(truth, probs, classes)
    assert result['accuracy'] == .5
    assert result['macro_f1_six'] == pytest.approx((2 / 3) / 6)


def test_support_empty_and_unsupported_calibration_remain_explicit():
    truth = np.array(['True_Correct:NA', 'False_Misconception:unknown'])
    classes = np.array(['True_Correct:NA'])
    memory = {'prob': np.ones((2, 1)), 'classes': classes, 'questions': np.array([1, 1]),
        'train_labels': np.repeat(classes, 30), 'train_questions': np.repeat([3, 4], 15), 'order': np.arange(2)}
    result = c.evaluate({'arm': 'full_context', 'fold': 0}, memory, truth)
    assert result['groups']['unsupported']['map_at_3'] == 0
    assert result['groups']['unsupported']['brier'] is None
    assert result['groups']['rare']['map_at_3'] is None
    assert result['groups']['well_supported']['original_n'] == 1
    for budget in result['risk_coverage']:
        assert budget['all']['retained_n'] == 2 - 2 * budget['review_percent'] // 100


def test_e012_failure_gate_does_not_accept_operational_failure_or_success(monkeypatch):
    monkeypatch.setattr(pub, 'validate_public_payload', lambda p: None if p['status'] == 'COMPLETED' else (_ for _ in ()).throw(ValueError()))
    c.gate_e012({'experiment_id': 'E011', 'status': 'COMPLETED', 'primary': {'criterion_met': False}})
    for p in [{'experiment_id': 'E011', 'status': 'FAILED', 'primary': {'criterion_met': False}},
              {'experiment_id': 'E011', 'status': 'COMPLETED', 'primary': {'criterion_met': True}}]:
        with pytest.raises(ValueError): c.gate_e012(p)


@pytest.mark.parametrize('field', ['StudentExplanation', 'row_id', 'probabilities', 'coefficients', 'MC_Answer', 'private_path'])
def test_unknown_public_fields_rejected(field):
    with pytest.raises(ValueError): validate_schema({field: 'PRIVATE'}, pub.payload_schema('E011'))


def test_mutated_group_counts_and_calibration_rejected():
    truth = np.repeat('True_Correct:NA', 250); prob = np.ones((250, 1)); classes = np.array(['True_Correct:NA'])
    g = c.metrics_group(truth, prob, classes, np.ones(250, bool), np.ones(250, bool))
    pub.check_group(g)
    wrong = deepcopy(g); wrong['incorrect_n'] = 1
    with pytest.raises(ValueError): pub.check_group(wrong)
    wrong = deepcopy(g); wrong['brier'] = 0.
    with pytest.raises(ValueError): pub.check_group(wrong)


def test_historical_reference_mismatch_stops():
    description = {'fold': 0}
    memory = {'prob': np.ones((1, 1)), 'classes': np.array(['True_Correct:NA']),
              'frequency_prob': np.ones((1, 1)), 'frequency_classes': np.array(['True_Correct:NA'])}
    reference = {'results': [{'variant': 'question_plus_explanation', 'folds': [{'fold': 0,
        'reproduction_comparisons': [{'model': 'tfidf_logreg', 'metric': 'map_at_3', 'reference': 0.}]}]}]}
    with pytest.raises(ValueError, match='reproduction'): c.reference_gate(description, memory, np.array(['True_Correct:NA']), reference)


def test_source_global_freeze_precedes_evaluation_and_lock_matches_when_present():
    source = inspect.getsource(c.main)
    assert source.index("write_new(output / 'frozen_development.json'") < source.index('truth = combined_label')
    path = ROOT / 'experiments/e011_e012_lock.json'
    if path.exists():
        lock = json.loads(path.read_text(encoding='utf-8'))
        assert c.checked_lock(ROOT, lock['docker_image_id']) == lock


def synthetic_payload():
    records, development = [], []
    for arm in (*c.ARMS, 'frequency'):
        for fold in range(5):
            n = 7340 if fold == 0 else 7339
            classes = np.array(['False_Misconception:synthetic', 'True_Correct:NA'])
            truth = np.resize(classes, n)
            prob = np.tile([.55, .45], (n, 1))
            questions = np.resize(np.arange(fold * 3, fold * 3 + 3), n)
            memory = {'prob': prob, 'classes': classes, 'frequency_prob': prob, 'frequency_classes': classes,
                'questions': questions, 'train_labels': np.tile(classes, 30), 'train_questions': np.repeat([100, 101], 30),
                'order': np.arange(n), 'frequency_order': np.arange(n)}
            records.append(c.evaluate({'arm': arm, 'fold': fold}, memory, truth, frequency=arm == 'frequency'))
            if arm != 'frequency':
                development.append({'arm': arm, 'model': 'logistic', 'fold': fold, 'n_train': 20000,
                    'n_calibration': 36696 - n - 20000, 'n_evaluation': n, 'role_question_counts': [9, 3, 3],
                    'selection': {'selected_index': 0, 'candidates': [{'params': {**p, 'ngram_range': list(p['ngram_range'])},
                        'inner_fold_map_at_3': [.5] * 3, 'inner_mean_map_at_3': .5} for p in e001.GRID]},
                    'temperature': 1., 'calibration_supported_n': 100, 'fits': 10})
    controls = {a: [next(r for r in records if r['arm'] == a and r['fold'] == f)['groups']['all']['map_at_3'] for f in range(5)]
                for a in ('frequency', 'question_plus_explanation')}
    diag = [{'QuestionId': q['QuestionId'], 'n': q['groups']['all']['original_n'], 'blank_n': 0, 'zero_word_tokens_n': 0}
            for r in records if r['arm'] == 'frequency' for q in r['questions']]
    return {'experiment_id': 'E011', 'status': 'COMPLETED', 'development': development, 'records': records,
        'aggregate': c.aggregate(records), 'primary_control_map_at_3': controls, 'primary': c.primary(records, controls),
        'answer_diagnostics': {'all': {'n': 36696, 'blank_n': 0, 'zero_word_tokens_n': 0}, 'questions': diag},
        'provenance': {'git_revision': 'a' * 40, 'docker_image_id': 'sha256:' + 'b' * 64,
            **{k: 'c' * 64 for k in ('lock_sha256', 'data_sha256', 'manifest_sha256', 'assignments_sha256', 'frozen_development_sha256')},
            'e011_sha256': None, 'started_utc': '2026-10-13T00:00:00+00:00', 'finished_utc': '2026-10-13T00:01:00+00:00',
            'wall_seconds': 60., 'uid': 10001, 'gid': 10001, 'seed': 20260831, 'model_fits': 150, 'fit_warnings': 0,
            'preserved_files': 163, 'preservation_verified': True, 'global_freeze_verified': True, 'reproduction_checks': 30, 'row_level_outputs': False}}


@pytest.fixture(scope='module')
def payload(): return synthetic_payload()


def test_complete_synthetic_payload_validates_and_renders(payload):
    pub.validate_public_payload(payload)
    for record in payload['records']:
        for question in record['questions']:
            assert question['groups']['all']['share_of_retained'] == 1.
    report = pub.render(payload)
    assert 'Overall primary criterion met: **False**' in report
    assert 'All fold and question support groups' in report
    c.gate_e012(payload)


@pytest.mark.parametrize('mutation', ['duplicate', 'primary', 'aggregate', 'question', 'unknown', 'selection', 'budget', 'category'])
def test_complete_payload_tampering_blocked(payload, mutation):
    p = deepcopy(payload)
    if mutation == 'duplicate': p['records'].append(p['records'][0])
    elif mutation == 'primary': p['primary']['criterion_met'] = True
    elif mutation == 'aggregate': p['aggregate'][0]['groups']['all']['map_at_3']['mean'] += .01
    elif mutation == 'question': p['records'][0]['questions'][0]['groups']['all']['original_n'] += 1
    elif mutation == 'unknown': p['records'][0]['StudentExplanation'] = 'PRIVATE'
    elif mutation == 'selection': p['development'][0]['selection']['selected_index'] = 2
    elif mutation == 'budget': p['records'][0]['risk_coverage'][1]['review_percent'] = 20
    elif mutation == 'category': p['records'][0]['category']['n'] += 1
    with pytest.raises(ValueError): pub.validate_public_payload(p)


def test_complete_synthetic_e012_validates_and_renders(payload):
    p = deepcopy(payload)
    p['experiment_id'] = 'E012'
    p['records'] = [r for r in p['records'] if r['arm'] in ('full_context', 'frequency')]
    p['development'] = [d for d in p['development'] if d['arm'] == 'full_context']
    for d in p['development']:
        d['model'], d['fits'] = 'complement_nb', 19
        d['selection']['candidates'] = [{'params': {**g, 'ngram_range': list(g['ngram_range'])},
            'inner_fold_map_at_3': [.5] * 3, 'inner_mean_map_at_3': .5} for g in c.NB_GRID]
    p['provenance'].update(model_fits=95, reproduction_checks=15, e011_sha256='d' * 64)
    p['primary_control_map_at_3']['e011_full_context'] = p['primary_control_map_at_3'].pop('question_plus_explanation')
    p['primary'] = c.primary(p['records'], p['primary_control_map_at_3'])
    p['aggregate'] = c.aggregate(p['records'])
    pub.validate_public_payload(p)
    assert 'Overall primary criterion met: **False**' in pub.render(p, payload)


@pytest.mark.parametrize('experiment', ['E011', 'E012'])
def test_published_results_validate_when_available(experiment):
    path = ROOT / f'results/{experiment}_aggregates.json'
    if not path.exists():
        pytest.skip('No research results yet; no fitting occurs in tests.')
    p = json.loads(path.read_text(encoding='utf-8'))
    pub.validate_public_payload(p)
    previous = json.loads((ROOT / 'results/E011_aggregates.json').read_text(encoding='utf-8')) if experiment == 'E012' else None
    report = (ROOT / f'docs/{experiment}_RESULTS.md').read_text(encoding='utf-8')
    assert report == pub.render(p, previous)
