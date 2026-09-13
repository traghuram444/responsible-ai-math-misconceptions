"""Synthetic-only E006 aggregation and publication-safety checks."""

from copy import deepcopy
import math
from statistics import mean, stdev

import pytest

from map_misconceptions.selective_report import (
    BUDGETS, GROUPS, ROUTES, VARIANTS, aggregate_results, render_results_report,
)


def metric_group(original=1000, retained=1000, risk=0.6, zero_risk=0.6):
    correct = round(retained * (1 - risk))
    incorrect = retained - correct
    actual_risk = incorrect / retained if retained else None
    eligible = retained >= 200 and correct >= 20 and incorrect >= 20
    return {
        "original_n": original,
        "retained_n": retained,
        "retention_fraction_of_original_group": retained / original if original else None,
        "fraction_of_all_retained_cases": 1.0 if retained else 0.0,
        "top1_accuracy": correct / retained if retained else None,
        "map_at_3": min(1.0, correct / retained + 0.1) if retained else None,
        "risk": actual_risk,
        "absolute_risk_reduction_vs_own_zero_review": zero_risk - actual_risk if retained else None,
        "correct_n": correct,
        "incorrect_n": incorrect,
        "calibration_eligible": eligible,
        "calibration_ineligible_reason": None if eligible else "fixed_count_rule",
        "ece_10_equal_width": 0.1 if eligible else None,
        "legacy_multiclass_brier": 0.4 if eligible else None,
        "union_label_brier": 0.5 if eligible else None,
    }


def synthetic_results():
    results = []
    for variant in VARIANTS:
        folds = []
        for fold in range(5):
            models = {
                "frequency_baseline": {"confidence_auroc": None, "routing": []},
                "tfidf_logreg": {"confidence_auroc": 0.6 + fold / 100, "routing": []},
            }
            for model, rule in ROUTES:
                start_risk = 0.6
                end_risk = {"frequency": 0.6, "confidence_only": 0.4, "support_aware": 0.56}[rule]
                if variant == "question_plus_explanation":
                    if rule == "frequency":
                        start_risk = end_risk = 0.3
                    elif rule == "support_aware":
                        end_risk = 0.25
                budgets = []
                for budget in BUDGETS:
                    retained = math.ceil(1000 * (1 - budget))
                    risk = start_risk + 2 * budget * (end_risk - start_risk)
                    groups = {
                        group: metric_group(retained=retained, risk=risk, zero_risk=start_risk)
                        for group in GROUPS
                    }
                    groups["rare"] = metric_group(original=0, retained=0)
                    groups["unsupported"] = metric_group(original=100, retained=math.ceil(100 * (1 - budget)), risk=1, zero_risk=1)
                    groups["unsupported"]["fraction_of_all_retained_cases"] = groups["unsupported"]["retained_n"] / retained
                    budgets.append({"review_fraction": budget, "groups": groups})
                models[model]["routing"].append({"rule": rule, "budgets": budgets})
            folds.append({"fold": fold, **models})
        results.append({"variant": variant, "folds": folds})
    return results


def group_at(results, *, fold=0, model="tfidf_logreg", route=0, budget=5, group="all"):
    return results[0]["folds"][fold][model]["routing"][route]["budgets"][budget]["groups"][group]


def disable_calibration(group):
    zero_risk = group["risk"] + group["absolute_risk_reduction_vs_own_zero_review"]
    group["correct_n"] = 19
    group["incorrect_n"] = group["retained_n"] - 19
    group["top1_accuracy"] = 19 / group["retained_n"]
    group["risk"] = 1 - group["top1_accuracy"]
    group["absolute_risk_reduction_vs_own_zero_review"] = zero_risk - group["risk"]
    group["calibration_eligible"] = False
    group["calibration_ineligible_reason"] = "correct_n_below_20"
    for name in ("ece_10_equal_width", "legacy_multiclass_brier", "union_label_brier"):
        group[name] = None


def test_complete_grid_and_equal_weight_sample_sd():
    results = synthetic_results()
    aggregate = aggregate_results(results)
    assert len(aggregate["variants"]) == 2
    summary = aggregate["variants"][0]["confidence_auroc"]
    expected = [0.6, 0.61, 0.62, 0.63, 0.64]
    assert summary["mean"] == pytest.approx(mean(expected))
    assert summary["sample_sd"] == pytest.approx(stdev(expected))
    assert summary["eligible_fold_count"] == 5
    assert [value["fold"] for value in summary["fold_values"]] == list(range(5))
    assert len(aggregate["variants"][0]["routing"]) == 3
    assert len(aggregate["variants"][0]["routing"][0]["budgets"]) == 6
    assert len(aggregate["variants"][0]["paired_comparisons"]) == 6


def test_calibration_pairing_uses_intersection_not_difference_of_eligible_means():
    results = synthetic_results()
    learned = [0.8, 0.2, 0.3, 0.4, 0.5]
    frequency = [0.0, 0.1, 0.2, 0.9, 0.4]
    for fold in range(5):
        group_at(results, fold=fold)["ece_10_equal_width"] = learned[fold]
        group_at(results, fold=fold, model="frequency_baseline")["ece_10_equal_width"] = frequency[fold]
    disable_calibration(group_at(results, fold=0))
    disable_calibration(group_at(results, fold=3, model="frequency_baseline"))
    aggregate = aggregate_results(results)["variants"][0]
    comparison = aggregate["paired_comparisons"][0]["budgets"][5]["groups"]["all"]["ece_10_equal_width"]
    assert comparison["eligible_fold_count"] == 3
    assert comparison["mean"] == pytest.approx(0.1)
    assert [item["value"] for item in comparison["fold_values"]] == [None, pytest.approx(0.1), pytest.approx(0.1), None, pytest.approx(0.1)]
    individual = [route["budgets"][5]["groups"]["all"]["ece_10_equal_width"] for route in aggregate["routing"][:2]]
    assert all(summary["eligible_fold_count"] == 4 for summary in individual)
    assert comparison["mean"] != pytest.approx(individual[1]["mean"] - individual[0]["mean"])


def test_zero_eligible_and_single_eligible_fold_sd_are_null():
    results = synthetic_results()
    for fold in range(4):
        disable_calibration(group_at(results, fold=fold))
    aggregate = aggregate_results(results)["variants"][0]["routing"][1]["budgets"][5]["groups"]
    assert aggregate["all"]["ece_10_equal_width"]["eligible_fold_count"] == 1
    assert aggregate["all"]["ece_10_equal_width"]["sample_sd"] is None
    assert aggregate["rare"]["risk"]["eligible_fold_count"] == 0
    assert aggregate["rare"]["risk"]["mean"] is None
    assert aggregate["rare"]["risk"]["sample_sd"] is None
    assert aggregate["rare"]["original_n"]["mean"] == 0
    assert aggregate["rare"]["fraction_of_all_retained_cases"]["mean"] == 0
    assert aggregate["rare"]["retention_fraction_of_original_group"]["mean"] is None


def test_criterion_is_independent_and_requires_both_conditions():
    aggregate = aggregate_results(synthetic_results())["variants"]
    first = aggregate[0]["criteria"]
    second = aggregate[1]["criteria"]
    assert first[0]["passes"] is True
    assert first[1]["meets_minimum_risk_reduction"] is False
    assert first[1]["beats_frequency"] is True
    assert first[1]["passes"] is False
    assert second[0]["meets_minimum_risk_reduction"] is True
    assert second[0]["beats_frequency"] is False
    assert second[0]["passes"] is False
    assert second[1]["passes"] is True
    assert first[0]["mean_absolute_risk_reduction"] == pytest.approx(0.2)
    assert first[0]["mean_risk_difference_vs_frequency"] == pytest.approx(-0.2)


def test_zero_review_risk_difference_has_opposite_sign_from_risk_reduction():
    aggregate = aggregate_results(synthetic_results())["variants"][0]
    comparison = next(c for c in aggregate["paired_comparisons"] if c["comparison"] == "retained_minus_own_zero_review" and c["left_rule"] == "confidence_only")
    difference = comparison["budgets"][5]["groups"]["all"]["risk"]
    assert difference["mean"] == pytest.approx(-0.2)
    assert set(comparison["budgets"][5]["groups"]["all"]) == {"risk"}


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf"), "secret", True])
def test_nonfinite_and_nonnumeric_declared_metrics_are_rejected(value):
    results = synthetic_results()
    group_at(results)["map_at_3"] = value
    with pytest.raises(ValueError, match="finite number or null"):
        aggregate_results(results)


@pytest.mark.parametrize("remove", ["variant", "fold", "budget", "group", "route"])
def test_incomplete_registered_grid_is_rejected(remove):
    results = synthetic_results()
    if remove == "variant":
        results.pop()
    elif remove == "fold":
        results[0]["folds"].pop()
    elif remove == "budget":
        results[0]["folds"][0]["tfidf_logreg"]["routing"][0]["budgets"].pop()
    elif remove == "group":
        del results[0]["folds"][0]["tfidf_logreg"]["routing"][0]["budgets"][0]["groups"]["rare"]
    else:
        results[0]["folds"][0]["tfidf_logreg"]["routing"].pop()
    with pytest.raises(ValueError, match="Incomplete"):
        aggregate_results(results)


def test_duplicate_fold_is_rejected_and_input_is_not_mutated():
    results = synthetic_results()
    preserved = deepcopy(results)
    aggregate_results(results)
    assert results == preserved
    results[0]["folds"][4]["fold"] = 0
    with pytest.raises(ValueError, match="duplicate"):
        aggregate_results(results)


def test_wrong_calibration_eligibility_or_nonnull_excluded_value_rejected():
    results = synthetic_results()
    group_at(results)["calibration_eligible"] = False
    with pytest.raises(ValueError, match="eligibility"):
        aggregate_results(results)
    results = synthetic_results()
    group_at(results, group="rare")["ece_10_equal_width"] = 0
    with pytest.raises(ValueError, match="eligibility"):
        aggregate_results(results)


def test_report_contains_raw_tables_before_decisions_and_never_unknown_text():
    results = synthetic_results()
    results[0]["private_note"] = "STUDENT_RESPONSE_SENTINEL"
    group_at(results)["calibration_ineligible_reason"] = "STUDENT_RESPONSE_SENTINEL"
    payload = {
        "experiment_id": "E006", "status": "COMPLETED", "results": results,
        "provenance": {"private_path": "STUDENT_RESPONSE_SENTINEL"},
    }
    report = render_results_report(payload)
    assert "STUDENT_RESPONSE_SENTINEL" not in report
    assert "../results/E006_aggregates.json" in report
    assert "Confidence separation — all five folds" in report
    assert report.index("all-case fold results") < report.index("Registered relative-benefit decisions")
    assert report.count("| 4 | 50% |") == 6
    assert "null ± null [0]" in report
    assert "legacy Brier is retained in the JSON" in report
    assert "E007" not in report


@pytest.mark.parametrize("status", ["RUNNING", "FAILED", "PARTIAL"])
def test_partial_artifact_never_renders_as_completed(status):
    with pytest.raises(ValueError, match="completed E006"):
        render_results_report({"experiment_id": "E006", "status": status, "results": synthetic_results()})
