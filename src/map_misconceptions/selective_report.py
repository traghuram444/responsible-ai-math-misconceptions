"""Aggregate-only, fixed-protocol reporting for E006.

This module neither fits models nor accepts student-level inputs. It validates the
complete registered grid before reporting, and never interpolates missing folds.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import math
from numbers import Real
from statistics import mean, stdev


VARIANTS = ("explanation_only", "question_plus_explanation")
FOLDS = (0, 1, 2, 3, 4)
BUDGETS = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5)
GROUPS = ("all", "unsupported", "rare", "frequent", "well_supported")
ROUTES = (
    ("frequency_baseline", "frequency"),
    ("tfidf_logreg", "confidence_only"),
    ("tfidf_logreg", "support_aware"),
)
COUNT_METRICS = ("original_n", "retained_n", "correct_n", "incorrect_n")
CALIBRATION_METRICS = (
    "ece_10_equal_width", "legacy_multiclass_brier", "union_label_brier",
)
NUMERIC_METRICS = (
    "original_n", "retained_n", "retention_fraction_of_original_group",
    "fraction_of_all_retained_cases", "top1_accuracy", "map_at_3", "risk",
    "absolute_risk_reduction_vs_own_zero_review", "correct_n", "incorrect_n",
    *CALIBRATION_METRICS,
)


def _finite_or_none(value, context: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value):
        raise ValueError(f"Expected finite number or null: {context}")
    return float(value)


def _summary(values: Mapping[int, float | None]) -> dict:
    """Use complete visible fold IDs, with available-fold descriptive SD only."""
    valid = [float(values[fold]) for fold in FOLDS if values[fold] is not None]
    return {
        "mean": mean(valid) if valid else None,
        "sample_sd": stdev(valid) if len(valid) >= 2 else None,
        "eligible_fold_count": len(valid),
        "fold_values": [{"fold": fold, "value": values[fold]} for fold in FOLDS],
    }


def _exact_index(items, key: str, expected: Sequence, context: str) -> dict:
    if not isinstance(items, (list, tuple)):
        raise ValueError(f"Expected complete list: {context}")
    index = {}
    for item in items:
        if not isinstance(item, Mapping) or key not in item:
            raise ValueError(f"Missing registered key: {context}")
        value = item[key]
        if isinstance(value, bool) or value not in expected or value in index:
            raise ValueError(f"Unknown or duplicate registered value: {context}")
        index[value] = item
    if set(index) != set(expected):
        raise ValueError(f"Incomplete registered grid: {context}")
    return index


def _validate_metric_group(group: dict) -> None:
    if not isinstance(group, Mapping):
        raise ValueError("Expected metric group")
    for metric in NUMERIC_METRICS:
        if metric not in group:
            raise ValueError(f"Missing registered metric: {metric}")
        value = _finite_or_none(group[metric], metric)
        if metric in COUNT_METRICS and (
            value is None or value < 0 or not value.is_integer()
        ):
            raise ValueError(f"Expected nonnegative integer count: {metric}")
    if not isinstance(group.get("calibration_eligible"), bool):
        raise ValueError("Missing boolean calibration eligibility")
    eligible = group["calibration_eligible"]
    expected = group["retained_n"] >= 200 and group["correct_n"] >= 20 and group["incorrect_n"] >= 20
    if eligible != expected:
        raise ValueError("Calibration eligibility violates registered counts")
    for metric in CALIBRATION_METRICS:
        if (group[metric] is not None) != eligible:
            raise ValueError("Calibration metrics must match registered eligibility")
    if group["retained_n"] > group["original_n"]:
        raise ValueError("Retained count exceeds original group size")
    if group["correct_n"] + group["incorrect_n"] != group["retained_n"]:
        raise ValueError("Correct/incorrect counts do not partition retained group")
    if not group["retained_n"]:
        for metric in ("top1_accuracy", "map_at_3", "risk", "absolute_risk_reduction_vs_own_zero_review"):
            if group[metric] is not None:
                raise ValueError("Empty retained group must have null performance")
    else:
        for metric in ("top1_accuracy", "map_at_3", "risk"):
            if group[metric] is None or not 0 <= group[metric] <= 1:
                raise ValueError("Nonempty group must have bounded performance")
        if not math.isclose(group["risk"], 1 - group["top1_accuracy"], abs_tol=1e-12, rel_tol=0):
            raise ValueError("Risk must equal one minus top-1 accuracy")
        if not math.isclose(group["top1_accuracy"], group["correct_n"] / group["retained_n"], abs_tol=1e-12, rel_tol=0):
            raise ValueError("Top-1 accuracy must match correct/retained counts")


def _index_results(results: list) -> dict:
    variants = _exact_index(results, "variant", VARIANTS, "variants")
    index = {}
    for variant in VARIANTS:
        folds = _exact_index(variants[variant].get("folds"), "fold", FOLDS, "folds")
        indexed_folds = {}
        for fold in FOLDS:
            source = folds[fold]
            indexed_routes = {}
            for model in ("frequency_baseline", "tfidf_logreg"):
                if not isinstance(source.get(model), Mapping):
                    raise ValueError("Missing registered model")
                expected_rules = [rule for candidate, rule in ROUTES if candidate == model]
                routing = _exact_index(source[model].get("routing"), "rule", expected_rules, "routing rules")
                for rule in expected_rules:
                    budgets = _exact_index(routing[rule].get("budgets"), "review_fraction", BUDGETS, "review budgets")
                    for budget in BUDGETS:
                        groups = budgets[budget].get("groups")
                        if not isinstance(groups, Mapping) or set(groups) != set(GROUPS):
                            raise ValueError("Incomplete registered strata")
                        for group in GROUPS:
                            _validate_metric_group(groups[group])
                    indexed_routes[(model, rule)] = budgets
            if "confidence_auroc" not in source["tfidf_logreg"]:
                raise ValueError("Missing registered confidence AUROC")
            if source["frequency_baseline"].get("confidence_auroc") is not None:
                raise ValueError("Frequency confidence AUROC is outside the registered report")
            auroc = _finite_or_none(source["tfidf_logreg"]["confidence_auroc"], "confidence_auroc")
            if auroc is not None and not 0 <= auroc <= 1:
                raise ValueError("AUROC must be between zero and one")
            all_cases = indexed_routes[("tfidf_logreg", "confidence_only")][0.0]["groups"]["all"]
            auc_eligible = all_cases["correct_n"] > 0 and all_cases["incorrect_n"] > 0
            if (auroc is not None) != auc_eligible:
                raise ValueError("Confidence AUROC eligibility must match correct/incorrect outcomes")
            indexed_folds[fold] = {"routes": indexed_routes, "confidence_auroc": auroc}
        index[variant] = indexed_folds
    return index


def aggregate_results(results: list) -> dict:
    """Return registered equal-fold summaries, paired deltas, and four decisions.

    Each paired metric uses only folds where *both* values exist. In particular,
    calibration differences never subtract two differently eligible fold means.
    Unregistered metadata in the supplied records is not copied to this output.
    """
    indexed = _index_results(results)
    output = {"variants": []}
    for variant in VARIANTS:
        folds = indexed[variant]

        def values(model, rule, budget, group, metric):
            return {
                fold: folds[fold]["routes"][(model, rule)][budget]["groups"][group][metric]
                for fold in FOLDS
            }

        def summarize_pair(left, right, budget, group, metric, right_budget=None):
            lhs = values(*left, budget, group, metric)
            rhs = values(*right, budget if right_budget is None else right_budget, group, metric)
            return _summary({
                fold: None if lhs[fold] is None or rhs[fold] is None else lhs[fold] - rhs[fold]
                for fold in FOLDS
            })

        record = {
            "variant": variant,
            "confidence_auroc": _summary({fold: folds[fold]["confidence_auroc"] for fold in FOLDS}),
            "routing": [],
            "paired_comparisons": [],
            "criteria": [],
        }
        for model, rule in ROUTES:
            record["routing"].append({
                "model": model,
                "rule": rule,
                "budgets": [
                    {
                        "review_fraction": budget,
                        "groups": {
                            group: {
                                metric: _summary(values(model, rule, budget, group, metric))
                                for metric in NUMERIC_METRICS
                            }
                            for group in GROUPS
                        },
                    }
                    for budget in BUDGETS
                ],
            })
        comparisons = [
            ("learned_minus_frequency", ("tfidf_logreg", rule), ROUTES[0], NUMERIC_METRICS, False)
            for rule in ("confidence_only", "support_aware")
        ]
        comparisons.append(("support_aware_minus_confidence_only", ROUTES[2], ROUTES[1], NUMERIC_METRICS, False))
        comparisons.extend(
            ("retained_minus_own_zero_review", route, route, ("risk",), True)
            for route in ROUTES
        )
        for name, left, right, metrics, zero_reference in comparisons:
            record["paired_comparisons"].append({
                "comparison": name,
                "left_model": left[0], "left_rule": left[1],
                "right_model": right[0], "right_rule": right[1],
                "right_review_fraction": 0.0 if zero_reference else "same_budget",
                "budgets": [
                    {
                        "review_fraction": budget,
                        "groups": {
                            group: {
                                metric: summarize_pair(left, right, budget, group, metric, 0.0 if zero_reference else None)
                                for metric in metrics
                            }
                            for group in GROUPS
                        },
                    }
                    for budget in BUDGETS
                ],
            })
        for rule in ("confidence_only", "support_aware"):
            own = summarize_pair(("tfidf_logreg", rule), ("tfidf_logreg", rule), 0.5, "all", "risk", 0.0)
            difference = summarize_pair(("tfidf_logreg", rule), ROUTES[0], 0.5, "all", "risk")
            if own["eligible_fold_count"] != 5 or difference["eligible_fold_count"] != 5:
                raise ValueError("All five all-case folds are required for the fixed criterion")
            reduction = -own["mean"]
            meets_minimum = reduction >= 0.05
            beats_frequency = difference["mean"] < 0
            record["criteria"].append({
                "rule": rule, "review_fraction": 0.5,
                "mean_absolute_risk_reduction": reduction,
                "mean_risk_difference_vs_frequency": difference["mean"],
                "meets_minimum_risk_reduction": meets_minimum,
                "beats_frequency": beats_frequency,
                "passes": meets_minimum and beats_frequency,
            })
        output["variants"].append(record)
    return output


def _number(value, digits=4) -> str:
    return "null" if value is None else f"{value:.{digits}f}"


def _mean_sd(summary: dict, digits=4) -> str:
    return f"{_number(summary['mean'], digits)} ± {_number(summary['sample_sd'], digits)} [{summary['eligible_fold_count']}]"


def _table(headers, rows) -> list[str]:
    return [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *("| " + " | ".join(str(cell) for cell in row) + " |" for row in rows),
        "",
    ]


def render_results_report(payload: dict) -> str:
    """Render the complete registered aggregate grid without arbitrary strings.

    Only literal labels and validated numeric fields are emitted. Provenance and
    any other caller metadata remain outside this renderer's publication scope.
    """
    if payload.get("experiment_id") != "E006" or payload.get("status") != "COMPLETED":
        raise ValueError("Only a completed E006 artifact may be rendered")
    aggregates = aggregate_results(payload.get("results"))
    lines = [
        "# E006 — registered selective-prediction results", "",
        "Status: **COMPLETED**. Results below are descriptive; no interpretation or next-experiment proposal is included.", "",
        "[Full aggregate and fold-level JSON](../results/E006_aggregates.json) contains every registered budget and stratum, counts, eligibility, both Brier fields, and paired fold values.", "",
        "Summary cells show equal-fold mean ± sample SD [eligible folds]. Counts in aggregate tables are mean counts, not pooled totals. Null means undefined or excluded by the fixed calibration eligibility rule. Fold summaries do not provide independent-fold inferential evidence.", "",
        "Risk = 1 − top-1 accuracy. Positive risk reduction means improvement versus the same rule at 0% review; negative paired risk difference means lower risk for the left-hand rule. ECE uses ten equal-width bins. Brier below is union-label-corrected; legacy Brier is retained in the JSON.", "",
    ]
    indexed = _index_results(payload["results"])
    route_labels = {"frequency": "Frequency", "confidence_only": "Confidence", "support_aware": "Support-aware"}
    arm_labels = {"explanation_only": "Explanation only", "question_plus_explanation": "Question plus explanation"}

    for variant in aggregates["variants"]:
        name = variant["variant"]
        lines.extend([f"## {arm_labels[name]} — all-case aggregate results", ""])
        rows = []
        for route in variant["routing"]:
            for budget in route["budgets"]:
                group = budget["groups"]["all"]
                rows.append([
                    route_labels[route["rule"]], f"{budget['review_fraction']:.0%}",
                    _mean_sd(group["retained_n"], 1),
                    *(_mean_sd(group[metric]) for metric in (
                        "retention_fraction_of_original_group", "top1_accuracy", "map_at_3", "risk",
                        "absolute_risk_reduction_vs_own_zero_review", "ece_10_equal_width", "union_label_brier",
                    )),
                ])
        lines.extend(_table(["Rule", "Review", "Retained n", "Coverage", "Top-1", "MAP@3", "Risk", "Risk reduction", "ECE", "Brier"], rows))
        lines.extend([f"### {arm_labels[name]} — support strata at 50% review", ""])
        rows = []
        for route in variant["routing"]:
            for group_name in GROUPS[1:]:
                group = next(b for b in route["budgets"] if b["review_fraction"] == 0.5)["groups"][group_name]
                rows.append([
                    route_labels[route["rule"]], group_name,
                    _mean_sd(group["original_n"], 1), _mean_sd(group["retained_n"], 1),
                    *(_mean_sd(group[metric]) for metric in (
                        "retention_fraction_of_original_group", "fraction_of_all_retained_cases",
                        "top1_accuracy", "map_at_3", "risk", "absolute_risk_reduction_vs_own_zero_review",
                        "ece_10_equal_width", "union_label_brier",
                    )),
                ])
        lines.extend(_table(["Rule", "Stratum", "Original n", "Retained n", "Stratum retained fraction", "Share of retained set", "Top-1", "MAP@3", "Risk", "Risk reduction", "ECE", "Brier"], rows))
        lines.extend([f"### {arm_labels[name]} — paired all-case differences", "",
                      "Every cell uses the same-fold intersection where both values exist. Differences are left minus right.", ""])
        rows = []
        for comparison in variant["paired_comparisons"]:
            left = route_labels[comparison["left_rule"]]
            right = "own 0%" if comparison["comparison"] == "retained_minus_own_zero_review" else route_labels[comparison["right_rule"]]
            for budget in comparison["budgets"]:
                group = budget["groups"]["all"]
                rows.append([
                    f"{left} − {right}", f"{budget['review_fraction']:.0%}",
                    *(_mean_sd(group[metric]) if metric in group else "—" for metric in (
                        "top1_accuracy", "map_at_3", "risk", "ece_10_equal_width", "union_label_brier",
                    )),
                ])
        lines.extend(_table(["Comparison", "Review", "Δ Top-1", "Δ MAP@3", "Δ Risk", "Δ ECE", "Δ Brier"], rows))

    lines.extend(["## Confidence separation — all five folds", ""])
    rows = []
    for variant in aggregates["variants"]:
        auc = variant["confidence_auroc"]
        rows.append([arm_labels[variant["variant"]], *(_number(item["value"]) for item in auc["fold_values"]), _mean_sd(auc)])
    lines.extend(_table(["Input arm", "Fold 0", "Fold 1", "Fold 2", "Fold 3", "Fold 4", "AUROC mean ± SD [n]"], rows))
    for variant in VARIANTS:
        lines.extend([f"## {arm_labels[variant]} — all-case fold results", ""])
        for model, rule in ROUTES:
            lines.extend([f"### {route_labels[rule]}", ""])
            rows = []
            for fold in FOLDS:
                for budget in BUDGETS:
                    group = indexed[variant][fold]["routes"][(model, rule)][budget]["groups"]["all"]
                    rows.append([
                        fold, f"{budget:.0%}", group["original_n"], group["retained_n"],
                        *(_number(group[metric]) for metric in (
                            "retention_fraction_of_original_group", "top1_accuracy", "map_at_3", "risk",
                            "absolute_risk_reduction_vs_own_zero_review", "ece_10_equal_width", "union_label_brier",
                        )),
                    ])
            lines.extend(_table(["Fold", "Review", "Original n", "Retained n", "Coverage", "Top-1", "MAP@3", "Risk", "Risk reduction", "ECE", "Brier"], rows))

    lines.extend(["## Registered relative-benefit decisions — reported after raw tables", "",
                  "Each input-arm/rule pair must independently meet both conditions at 50% review: mean absolute risk reduction ≥0.05 and strictly lower retained risk than frequency. Calibration is descriptive, not a binary gate. These are relative criteria, not a deployment-safety threshold.", ""])
    rows = []
    for variant in aggregates["variants"]:
        for criterion in variant["criteria"]:
            rows.append([
                arm_labels[variant["variant"]], route_labels[criterion["rule"]],
                _number(criterion["mean_absolute_risk_reduction"]),
                _number(criterion["mean_risk_difference_vs_frequency"]),
                "yes" if criterion["meets_minimum_risk_reduction"] else "no",
                "yes" if criterion["beats_frequency"] else "no",
                "PASS" if criterion["passes"] else "FAIL",
            ])
    lines.extend(_table(["Input arm", "Rule", "Mean risk reduction", "Mean risk − frequency", "Reduction ≥0.05", "Lower risk than frequency", "Decision"], rows))
    return "\n".join(lines)
