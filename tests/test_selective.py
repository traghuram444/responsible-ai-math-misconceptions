"""Synthetic E006 regressions; never load MAP data or fit a model."""

import hashlib
import json
from math import ceil

import numpy as np
import pytest

from map_misconceptions.metrics import expected_calibration_error, map_at_3
from map_misconceptions.selective import REVIEW_FRACTIONS, _routing_order, evaluate_routing


def training_fixture():
    # Boundary cases: a=20 across two questions; b=20 on one; c=19; d=1.
    training = np.array(["a"] * 20 + ["b"] * 20 + ["c"] * 19 + ["d"])
    questions = np.array([1] * 10 + [2] * 10 + [1] * 20 + [1] * 19 + [2])
    return training, questions


def evaluate(truth, probabilities, *, rows=None, rules=("confidence_only", "support_aware"), fold=2):
    training, questions = training_fixture()
    return evaluate_routing(
        np.asarray(truth), np.asarray(probabilities), np.array(["a", "b", "c", "d"]),
        training, questions, np.arange(len(truth)) if rows is None else rows, fold, rules=rules,
    )


def budget(result, rule="confidence_only", review=0.5):
    route = next(route for route in result["routing"] if route["rule"] == rule)
    return next(point for point in route["budgets"] if point["review_fraction"] == review)["groups"]


def test_all_six_budgets_ceil_counts_and_aggregate_only_schema():
    truth = np.array(["a", "b", "c", "d", "unseen", "a", "b"])
    prob = np.tile([0.7, 0.1, 0.1, 0.1], (len(truth), 1))
    result = evaluate(truth, prob)
    assert set(result) == {"confidence_auroc", "routing"}
    for route in result["routing"]:
        assert [entry["review_fraction"] for entry in route["budgets"]] == list(REVIEW_FRACTIONS)
        for point in route["budgets"]:
            assert point["groups"]["all"]["retained_n"] == ceil(len(truth) * (1 - point["review_fraction"]))
            assert set(point["groups"]) == {"all", "unsupported", "rare", "frequent", "well_supported"}
    serialized = json.dumps(result, allow_nan=False)
    for forbidden in ("source_row", "probabilities", "predictions", "rankings"):
        assert forbidden not in serialized


def test_sha256_exact_ties_and_input_order_invariance():
    rows = np.array([90, 2, 131, 0, 8, 17, 42, 31])
    truth = np.array(["a", "b", "c", "d", "unseen", "a", "b", "a"])
    prob = np.tile([0.7, 0.1, 0.1, 0.1], (len(truth), 1))
    expected = sorted(
        range(len(rows)),
        key=lambda i: hashlib.sha256(f"fold=2;source_row={rows[i]};seed=20260831".encode("utf-8")).hexdigest(),
    )
    assert _routing_order(prob.max(axis=1), rows.tolist(), 2, 20260831).tolist() == expected
    result = evaluate(truth, prob, rows=rows, rules=("frequency",))
    assert budget(result, "frequency")["all"]["top1_accuracy"] == pytest.approx((truth[expected[:4]] == "a").mean())
    permutation = np.array([7, 3, 2, 0, 5, 1, 6, 4])
    assert evaluate(truth[permutation], prob[permutation], rows=rows[permutation], rules=("frequency",)) == result
    assert result["confidence_auroc"] is None


def test_hash_collision_falls_back_to_source_position(monkeypatch):
    class Collision:
        def hexdigest(self):
            return "0" * 64

    monkeypatch.setattr("map_misconceptions.selective.hashlib.sha256", lambda value: Collision())
    assert _routing_order(np.array([0.5, 0.9, 0.5]), [9, 8, 1], 0, 20260831).tolist() == [1, 2, 0]


def test_global_retention_then_disjoint_and_nested_support_strata():
    truth = np.array(["unseen", "c", "d", "b", "a", "a"])
    confidence = np.array([0.95, 0.90, 0.85, 0.80, 0.75, 0.70])
    prob = np.column_stack([confidence, (1 - confidence) / 3, (1 - confidence) / 3, (1 - confidence) / 3])
    result = evaluate(truth, prob)
    full = budget(result, review=0.0)
    selected = budget(result)
    assert [full[name]["original_n"] for name in ("unsupported", "rare", "frequent", "well_supported")] == [1, 2, 3, 2]
    assert [selected[name]["retained_n"] for name in ("unsupported", "rare", "frequent", "well_supported")] == [1, 2, 0, 0]
    assert sum(selected[name]["retained_n"] for name in ("unsupported", "rare", "frequent")) == selected["all"]["retained_n"]
    assert selected["unsupported"]["retention_fraction_of_original_group"] == 1
    assert selected["unsupported"]["fraction_of_all_retained_cases"] == pytest.approx(1 / 3)
    assert selected["frequent"]["top1_accuracy"] is None
    assert selected["frequent"]["absolute_risk_reduction_vs_own_zero_review"] is None
    assert selected["unsupported"]["top1_accuracy"] == 0
    assert selected["unsupported"]["map_at_3"] == 0
    assert selected["unsupported"]["risk"] == 1


def test_empty_original_stratum_has_null_performance_and_undefined_retention_ratio():
    result = evaluate(["a", "b"], [[0.7, 0.1, 0.1, 0.1]] * 2)
    empty = budget(result)["unsupported"]
    assert empty["original_n"] == empty["retained_n"] == 0
    assert empty["retention_fraction_of_original_group"] is None
    assert empty["fraction_of_all_retained_cases"] == 0
    for key in ("top1_accuracy", "map_at_3", "risk", "ece_10_equal_width", "legacy_multiclass_brier", "union_label_brier"):
        assert empty[key] is None


def test_support_weighting_changes_route_without_using_true_support():
    # c's count is 19 and d's is one; confidence favors d while support weighting favors c.
    prob = np.array([[0.02, 0.02, 0.02, 0.94], [0.03, 0.03, 0.91, 0.03]])
    result = evaluate(["unseen", "c"], prob)
    assert budget(result, "confidence_only")["all"]["top1_accuracy"] == 0
    assert budget(result, "support_aware")["all"]["top1_accuracy"] == 1
    assert budget(result, "confidence_only")["unsupported"]["retained_n"] == 1
    assert budget(result, "support_aware")["unsupported"]["retained_n"] == 0
    swapped = evaluate(["a", "a"], prob)
    assert budget(swapped, "confidence_only")["all"]["retained_n"] == 1
    # Direct expected index check protects the score's predicted-count definition.
    training, _ = training_fixture()
    factor = np.log1p([np.sum(training == "d"), np.sum(training == "c")]) / np.log1p(20)
    assert np.argmax(prob.max(axis=1) * factor) == 1


def test_eligible_calibration_uses_original_probabilities_and_corrected_brier():
    truth = np.array(["a"] * 100 + ["b"] * 80 + ["unseen"] * 20)
    prob = np.tile([0.7, 0.1, 0.1, 0.1], (200, 1))
    unchanged = prob.copy()
    result = evaluate(truth, prob)
    full = budget(result, review=0.0)["all"]
    assert full["calibration_eligible"]
    assert full["calibration_ineligible_reason"] is None
    assert full["ece_10_equal_width"] == pytest.approx(0.2)
    assert full["union_label_brier"] - full["legacy_multiclass_brier"] == pytest.approx(0.1)
    assert np.array_equal(prob, unchanged)
    reduced = budget(result)["all"]
    assert reduced["retained_n"] == 100
    assert not reduced["calibration_eligible"]
    assert "retained_n_below_200" in reduced["calibration_ineligible_reason"]
    assert reduced["union_label_brier"] is None


def test_support_score_never_replaces_calibration_probability():
    # All predictions are rare d, so support score is below pmax for every row.
    truth = np.array(["d"] * 100 + ["a"] * 100)
    prob = np.tile([0.05, 0.05, 0.05, 0.85], (200, 1))
    result = evaluate(truth, prob)
    for rule in ("support_aware", "confidence_only"):
        assert budget(result, rule, 0.0)["all"]["ece_10_equal_width"] == pytest.approx(0.35)


@pytest.mark.parametrize("truth,reason", [(["a"] * 181 + ["b"] * 19, "incorrect_n_below_20"), (["a"] * 19 + ["b"] * 181, "correct_n_below_20")])
def test_calibration_correct_and_incorrect_boundary(truth, reason):
    group = budget(evaluate(truth, [[0.7, 0.1, 0.1, 0.1]] * 200), review=0.0)["all"]
    assert not group["calibration_eligible"]
    assert group["calibration_ineligible_reason"] == reason
    assert group["ece_10_equal_width"] is None


def test_calibration_eligible_at_exact_boundaries():
    group = budget(evaluate(["a"] * 20 + ["b"] * 180, [[0.7, 0.1, 0.1, 0.1]] * 200), review=0.0)["all"]
    assert group["calibration_eligible"]
    assert group["correct_n"] == 20
    assert group["incorrect_n"] == 180


def test_unsupported_calibration_excluded_even_with_large_n():
    group = budget(evaluate(["unseen"] * 300, [[0.7, 0.1, 0.1, 0.1]] * 300), review=0.0)["unsupported"]
    assert group["retained_n"] == 300
    assert group["calibration_ineligible_reason"] == "correct_n_below_20"
    assert group["top1_accuracy"] == group["map_at_3"] == 0
    assert group["risk"] == 1
    assert group["union_label_brier"] is None


def test_confidence_auroc_both_outcomes_required():
    separated = evaluate(["a", "b"], [[0.9, 0.04, 0.03, 0.03], [0.6, 0.2, 0.1, 0.1]])
    assert separated["confidence_auroc"] == 1
    assert evaluate(["a", "a"], [[0.7, 0.1, 0.1, 0.1]] * 2)["confidence_auroc"] is None
    assert evaluate(["unseen", "unseen"], [[0.7, 0.1, 0.1, 0.1]] * 2)["confidence_auroc"] is None


def test_legacy_class_tie_semantics_are_preserved():
    truth = np.array(["a", "b", "c", "d"])
    prob = np.full((4, 4), 0.25)
    group = budget(evaluate(truth, prob), review=0.0)["all"]
    assert group["top1_accuracy"] == pytest.approx(0.25)
    assert group["map_at_3"] == map_at_3(truth, prob, np.array(["a", "b", "c", "d"]))


@pytest.mark.parametrize("rows", [[0, 0], [0, -1], [0.0, 1.0], [False, True]])
def test_invalid_source_identifiers_rejected(rows):
    with pytest.raises(ValueError):
        evaluate(["a", "b"], [[0.7, 0.1, 0.1, 0.1]] * 2, rows=rows)


def test_invalid_probability_rule_training_and_fold_inputs_rejected():
    with pytest.raises(ValueError):
        evaluate(["a"], [[0.3, 0.1, 0.1, 0.1]])
    with pytest.raises(ValueError):
        evaluate(["a"], [[0.7, 0.1, 0.1, 0.1]], rules=("unregistered",))
    with pytest.raises(ValueError):
        evaluate(["a"], [[0.7, 0.1, 0.1, 0.1]], fold=-1)
    with pytest.raises(ValueError):
        evaluate(["a", "b"], [[0.7, 0.1, 0.1, 0.1], [0.6, 0.2, 0.1, 0.1]], rules=("frequency",))
    with pytest.raises(ValueError):
        evaluate_routing(["a"], [[0.7, 0.3]], ["a", "b"], ["a"], [1], [0], 0)
