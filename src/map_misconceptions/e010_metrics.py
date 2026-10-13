"""Fixed-capacity E010 routing; no labels enter retention construction."""
from __future__ import annotations

import numpy as np

from .e009_reliability import VARIANTS
from .e009_metrics import HEAD_METRICS, head_summary, stat
from .metrics_v2 import union_label_brier_score
from .selective import _routing_order
from .threshold_transfer import METRICS, STRATA, canonical_question, summarize_group, support_masks

RULES = ('learned_reliability', 'confidence_only', 'support_aware', 'raw_confidence', 'hash_only', 'frequency')
BUDGETS = (0, 10, 20, 30, 40, 50)
EXTRA_METRICS = ('original_error_n', 'reviewed_n', 'reviewed_error_n', 'reviewed_correct_n',
                 'remaining_errors_per_100', 'captured_errors_per_100', 'error_capture_fraction', 'review_error_precision')
ALL_METRICS = (*METRICS, *EXTRA_METRICS)
PAIRED_METRICS = ('remaining_errors_per_100', 'error_capture_fraction', 'review_error_precision', 'risk')


def retention_masks(scores, source_positions, fold):
    """Only label-blind input. Exact quotas, fixed hash ties, immutable masks."""
    positions = np.asarray(source_positions)
    if positions.ndim != 1 or not len(positions) or positions.dtype.kind not in 'iu' or (positions < 0).any():
        raise ValueError('Invalid source positions.')
    if len(np.unique(positions)) != len(positions) or type(fold) is not int or fold not in range(5):
        raise ValueError('Invalid fold or duplicate positions.')
    if set(scores) != set(RULES) - {'hash_only'}:
        raise ValueError('Unexpected score rules.')
    masks = {}
    for rule in RULES:
        values = np.zeros(len(positions)) if rule == 'hash_only' else np.asarray(scores[rule])
        if values.shape != positions.shape or not np.isfinite(values).all() or (values < 0).any() or (values > 1).any():
            raise ValueError('Invalid scores.')
        if rule == 'frequency' and not np.all(values == values[0]):
            raise ValueError('Frequency score must be constant.')
        order = _routing_order(values, positions.tolist(), fold, 20260831)
        masks[rule] = {}
        for budget in BUDGETS:
            n = len(positions) - len(positions) * budget // 100
            retained = np.zeros(len(positions), dtype=bool)
            retained[order[:n]] = True
            retained.flags.writeable = False
            masks[rule][budget] = retained
    return masks


def freeze_counts(variant, fold, masks):
    return [{'variant': variant, 'fold': fold, 'rule': rule, 'review_percent': b,
             'original_n': len(mask), 'retained_n': int(mask.sum()), 'reviewed_n': int((~mask).sum())}
            for rule in RULES for b, mask in masks[rule].items()]


def review_group(truth, prob, classes, membership, retained):
    g = summarize_group(truth, prob, classes, membership, retained, None)
    correct = classes[prob.argmax(axis=1)] == truth
    errors = int((membership & ~correct).sum())
    reviewed = g['original_n'] - g['retained_n']
    captured = errors - g['incorrect_n']
    N = g['original_n']
    return {**g, 'original_error_n': errors, 'reviewed_n': reviewed,
            'reviewed_error_n': captured, 'reviewed_correct_n': reviewed - captured,
            'remaining_errors_per_100': 100 * g['incorrect_n'] / N if N else None,
            'captured_errors_per_100': 100 * captured / N if N else None,
            'error_capture_fraction': captured / errors if errors else None,
            'review_error_precision': captured / reviewed if reviewed else None}


def evaluate_fold(description, memory, truth, masks):
    truth = np.asarray(truth)
    questions = memory['evaluation_questions']
    strata = support_masks(truth, memory['train_labels'], memory['train_questions'])
    records = []
    for rule in RULES:
        prob, classes = ((memory['frequency_prob'], memory['frequency_classes']) if rule == 'frequency'
                         else (memory['learned_prob'], memory['classes']))
        union_label_brier_score(truth, prob, classes)
        correct = classes[prob.argmax(axis=1)] == truth
        for budget in BUDGETS:
            retained = masks[rule][budget]
            if retained.shape != truth.shape or retained.dtype != bool or retained.flags.writeable:
                raise ValueError('Frozen routing mask required.')
            def scoped(scope):
                return {s: review_group(truth, prob, classes, member & scope, retained & scope)
                        for s, member in strata.items()}
            def head(scope):
                return {s: head_summary(memory['scores']['learned_reliability'][member & scope & retained],
                                        correct[member & scope & retained]) for s, member in strata.items()}
            all_rows = np.ones(len(truth), dtype=bool)
            scopes = [(canonical_question(q), questions == q) for q in sorted(set(questions.tolist()))]
            records.append({'variant': description['variant'], 'fold': description['fold'], 'rule': rule,
                'review_percent': budget, 'evaluation': {'groups': scoped(all_rows), 'questions': [
                    {'QuestionId': q, 'groups': scoped(scope)} for q, scope in scopes]},
                'reliability': {'groups': head(all_rows), 'questions': [
                    {'QuestionId': q, 'groups': head(scope)} for q, scope in scopes]} if rule == 'learned_reliability' else None})
    return records


def primary_decision(benefits):
    if len(benefits) != 5 or any(x is None or not np.isfinite(x) for x in benefits):
        raise ValueError('Five finite primary differences required.')
    return {**stat(benefits), 'positive_folds': sum(x > 0 for x in benefits),
            'criterion_met': bool(np.mean(benefits) >= 2.0 and sum(x > 0 for x in benefits) >= 4)}


def aggregate(records):
    lookup = {(r['variant'], r['fold'], r['rule'], r['review_percent']): r for r in records}
    expected = {(v, f, rule, b) for v in VARIANTS for f in range(5) for rule in RULES for b in BUDGETS}
    if len(records) != 360 or set(lookup) != expected:
        raise ValueError('Incomplete or duplicate E010 grid.')
    summaries, pairs, primary = [], [], []
    for variant in VARIANTS:
        for rule in RULES:
            for budget in BUDGETS:
                rows = [lookup[variant, f, rule, budget] for f in range(5)]
                qs = [q['QuestionId'] for row in rows for q in row['evaluation']['questions']]
                if len(qs) != 15 or len(set(qs)) != 15:
                    raise ValueError('Question partition mismatch.')
                summaries.append({'variant': variant, 'rule': rule, 'review_percent': budget,
                    'groups': {s: {m: stat([r['evaluation']['groups'][s][m] for r in rows]) for m in ALL_METRICS} for s in STRATA},
                    'reliability': {s: {m: stat([r['reliability']['groups'][s][m] for r in rows]) for m in HEAD_METRICS} for s in STRATA}
                    if rule == 'learned_reliability' else None})
        for control in RULES[1:]:
            for budget in BUDGETS[1:]:
                fold_rows = []
                for f in range(5):
                    left = lookup[variant, f, 'learned_reliability', budget]['evaluation']['groups']['all']
                    right = lookup[variant, f, control, budget]['evaluation']['groups']['all']
                    diff = {m: left[m] - right[m] if left[m] is not None and right[m] is not None else None for m in PAIRED_METRICS}
                    fold_rows.append({'fold': f, 'left_original_error_n': left['original_error_n'], 'right_original_error_n': right['original_error_n'],
                        'left_review_fraction': left['review_fraction'], 'right_review_fraction': right['review_fraction'], 'differences': diff})
                pairs.append({'variant': variant, 'control': control, 'review_percent': budget, 'folds': fold_rows,
                              'differences': {m: stat([r['differences'][m] for r in fold_rows]) for m in PAIRED_METRICS}})
        benefits = [lookup[variant, f, 'support_aware', 20]['evaluation']['groups']['all']['remaining_errors_per_100'] -
                    lookup[variant, f, 'learned_reliability', 20]['evaluation']['groups']['all']['remaining_errors_per_100'] for f in range(5)]
        primary.append({'variant': variant, 'review_percent': 20, 'control': 'support_aware', **primary_decision(benefits)})
    for f in range(5):
        for b in BUDGETS:
            a, z = (lookup[v, f, 'frequency', b] for v in VARIANTS)
            if {k: x for k, x in a.items() if k != 'variant'} != {k: x for k, x in z.items() if k != 'variant'}:
                raise ValueError('Frequency duplicate references differ.')
    return {'summaries': summaries, 'paired': pairs, 'primary': primary}
