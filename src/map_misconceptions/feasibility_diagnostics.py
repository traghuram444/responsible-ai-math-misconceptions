"""E008 development-only feasibility diagnostics; no row arrays escape analysis."""
from __future__ import annotations

from fractions import Fraction
import itertools

import numpy as np

from .threshold_transfer import RULES, TARGETS, mean_sd

VARIANTS = ("explanation_only", "question_plus_explanation")
CODES = ("FIXED_PREDICTION_LIMIT", "SCORE_SELECTION_LIMIT", "COMMON_CUTOFF_INCOMPATIBILITY")
HIST_KEYS = tuple("".join(bits) for bits in itertools.product("01", repeat=3))
COUNT_KEYS = ("total", "count_pass", "coverage_pass", "risk_pass", "both_floors",
              "all_three", "count_only_failure", "coverage_only_failure", "risk_only_failure")


def oracle_bound(n, correct, *, variant, fold, model, role_index):
    if type(n) is not int or type(correct) is not int or not 0 <= correct <= n or n <= 0:
        raise ValueError("Invalid oracle counts.")
    coverage_min = (n + 9) // 10
    minimum = max(100, coverage_min)
    arm = "shared_frequency" if model == "frequency_baseline" else variant
    return {"oracle_id": f"{model}:{arm}:{fold}:{role_index}", "variant": arm, "model": model,
            "fold": fold, "role_index": role_index, "original_n": n, "correct_n": correct,
            "coverage_minimum_n": coverage_min, "minimum_n": minimum,
            "stronger_floor": "count" if 100 > coverage_min else "coverage" if coverage_min > 100 else "equal",
            "minimum_risk": max(0, minimum - correct) / minimum if minimum <= n else None,
            "targets": [{"target_percent": target,
                         "maximum_retained_n": min(n, 100 * correct // (100 - target)),
                         "maximum_coverage": min(n, 100 * correct // (100 - target)) / n,
                         "feasible": min(n, 100 * correct // (100 - target)) >= minimum}
                        for target in TARGETS]}


def _candidate_counts(scores, correct, roles):
    score, correct, roles = np.asarray(scores, dtype=np.float64), np.asarray(correct), np.asarray(roles)
    if (score.ndim != 1 or not len(score) or correct.shape != score.shape or correct.dtype != bool
            or roles.shape != score.shape or set(roles.tolist()) != {0, 1}
            or not np.isfinite(score).all() or (score < 0).any() or (score > 1).any()):
        raise ValueError("Invalid development diagnostic inputs.")
    thresholds = np.unique(np.r_[0., score])
    counts, errors, original = [], [], []
    for role in (0, 1):
        group = roles == role
        order = np.argsort(score[group], kind="stable")
        sorted_score = score[group][order]
        prefix = np.r_[0, np.cumsum((~correct[group][order]).astype(np.int64))]
        starts = np.searchsorted(sorted_score, thresholds, side="left")
        counts.append(len(order) - starts)
        errors.append(prefix[-1] - prefix[starts])
        original.append(len(order))
    return thresholds, np.asarray(counts), np.asarray(errors), np.asarray(original)


def histogram(count, coverage, risk):
    result = {key: 0 for key in HIST_KEYS}
    encoded = count.astype(int) * 4 + coverage.astype(int) * 2 + risk.astype(int)
    for index, n in enumerate(np.bincount(encoded, minlength=8)):
        result[format(index, "03b")] = int(n)
    return result


def histogram_counts(hist):
    return {"total": sum(hist.values()),
            "count_pass": sum(n for key, n in hist.items() if key[0] == "1"),
            "coverage_pass": sum(n for key, n in hist.items() if key[1] == "1"),
            "risk_pass": sum(n for key, n in hist.items() if key[2] == "1"),
            "both_floors": hist["110"] + hist["111"], "all_three": hist["111"],
            "count_only_failure": hist["011"], "coverage_only_failure": hist["101"],
            "risk_only_failure": hist["110"]}


def _minimum_index(thresholds, counts, errors, eligible, *, shared=False, role=0):
    best, key = None, None
    for i in np.flatnonzero(eligible):
        risks = [Fraction(int(errors[q, i]), int(counts[q, i])) for q in (0, 1)] if shared else [Fraction(int(errors[role, i]), int(counts[role, i]))]
        n = int(counts[:, i].sum()) if shared else int(counts[role, i])
        candidate = (max(risks), -n, float(thresholds[i]))
        if key is None or candidate < key:
            key, best = candidate, int(i)
    return best


def _question_witness(index, thresholds, counts, errors, original, role):
    if index is None:
        return None
    n, e = int(counts[role, index]), int(errors[role, index])
    return {"threshold": float(thresholds[index]), "retained_n": n, "incorrect_n": e,
            "coverage": n / int(original[role]), "risk": e / n}


def diagnose_rule(scores, correct, roles, oracles, *, variant, fold, rule):
    """Report the fixed three-target grid; never return candidate or response arrays."""
    if variant not in VARIANTS or rule not in RULES or fold not in range(5):
        raise ValueError("Invalid diagnostic context.")
    thresholds, counts, errors, original = _candidate_counts(scores, correct, roles)
    count_ok, coverage_ok = counts >= 100, counts * 10 >= original[:, None]
    floor_ok = count_ok & coverage_ok
    individual = [_minimum_index(thresholds, counts, errors, floor_ok[q], role=q) for q in (0, 1)]
    shared = _minimum_index(thresholds, counts, errors, floor_ok.all(axis=0), shared=True)
    records = []
    for target in TARGETS:
        risk_ok = (counts > 0) & (errors * 100 <= target * counts)
        feasible = floor_ok & risk_ok
        joint = histogram(count_ok.all(axis=0), coverage_ok.all(axis=0), risk_ok.all(axis=0))
        if joint["111"]:
            raise ValueError("REPRODUCTION_MISMATCH: shared feasible cutoff contradicts E007.")
        questions = []
        for role in (0, 1):
            oracle = oracles[role]
            expected_correct = int(np.asarray(correct)[np.asarray(roles) == role].sum())
            if oracle["original_n"] != int(original[role]) or oracle["correct_n"] != expected_correct:
                raise ValueError("Oracle counts differ from fixed development predictions.")
            bound = next(t for t in oracle["targets"] if t["target_percent"] == target)
            h = histogram(count_ok[role], coverage_ok[role], risk_ok[role])
            minimum = _question_witness(individual[role], thresholds, counts, errors, original, role)
            if minimum is not None:
                minimum.update({"error_minus_target": minimum["risk"] - target / 100,
                                "oracle_risk_gap": minimum["risk"] - oracle["minimum_risk"]})
            possible = bool(feasible[role].any())
            if possible and not bound["feasible"]:
                raise ValueError("Score selection cannot exceed the correctness oracle.")
            questions.append({"role_index": role, "oracle_id": oracle["oracle_id"],
                              "histogram": h, "counts": histogram_counts(h),
                              "individual_feasible": possible, "oracle_feasible": bound["feasible"],
                              "fixed_prediction_limit": not bound["feasible"],
                              "score_selection_limit": bound["feasible"] and not possible,
                              "minimum_status": "FOUND" if minimum is not None else "NO_FEASIBLE_FLOOR",
                              "minimum": minimum})
        common = None
        if shared is not None:
            witnesses = [{"role_index": q, **_question_witness(shared, thresholds, counts, errors, original, q)} for q in (0, 1)]
            worst = max(w["risk"] for w in witnesses)
            common = {"threshold": float(thresholds[shared]), "worst_risk": worst,
                      "error_minus_target": worst - target / 100, "questions": witnesses}
        code = ("FIXED_PREDICTION_LIMIT" if any(q["fixed_prediction_limit"] for q in questions)
                else "SCORE_SELECTION_LIMIT" if any(not q["individual_feasible"] for q in questions)
                else "COMMON_CUTOFF_INCOMPATIBILITY")
        records.append({"variant": variant, "fold": fold, "rule": rule, "target_percent": target,
                        "candidate_count": len(thresholds), "joint_histogram": joint,
                        "joint_counts": histogram_counts(joint), "shared_feasible_count": joint["111"],
                        "shared_minimum_status": "FOUND" if common is not None else "NO_FEASIBLE_FLOOR",
                        "shared_minimax": common, "questions": questions, "outcome": code})
    return records


def numeric_metrics(record, oracle_by_id):
    """Fixed scalar metric names, including equal-question (not pooled-row) means."""
    output = {"candidate_count": record["candidate_count"], "shared_feasible_count": record["shared_feasible_count"]}
    for key in HIST_KEYS:
        output[f"joint.histogram.{key}"] = record["joint_histogram"][key]
    for key in COUNT_KEYS:
        output[f"joint.counts.{key}"] = record["joint_counts"][key]
    shared = record["shared_minimax"]
    for key in ("threshold", "worst_risk", "error_minus_target"):
        output[f"shared.{key}"] = None if shared is None else shared[key]
    for q in record["questions"]:
        role, minimum = q["role_index"], q["minimum"]
        oracle = oracle_by_id[q["oracle_id"]]
        bound = next(b for b in oracle["targets"] if b["target_percent"] == record["target_percent"])
        for key in HIST_KEYS:
            output[f"q{role}.histogram.{key}"] = q["histogram"][key]
        for key in COUNT_KEYS:
            output[f"q{role}.counts.{key}"] = q["counts"][key]
        for key in ("threshold", "retained_n", "incorrect_n", "coverage", "risk", "error_minus_target", "oracle_risk_gap"):
            output[f"q{role}.minimum.{key}"] = None if minimum is None else minimum[key]
        for key in ("original_n", "correct_n", "coverage_minimum_n", "minimum_n", "minimum_risk"):
            output[f"q{role}.oracle.{key}"] = oracle[key]
        for key in ("maximum_retained_n", "maximum_coverage"):
            output[f"q{role}.oracle.{key}"] = bound[key]
        for key in ("retained_n", "incorrect_n", "coverage", "risk"):
            output[f"q{role}.shared.{key}"] = None if shared is None else shared["questions"][role][key]
    for suffix in ("minimum.risk", "minimum.coverage", "minimum.oracle_risk_gap", "oracle.minimum_risk",
                   "oracle.maximum_coverage", "shared.risk", "shared.coverage"):
        values = [output[f"q{role}.{suffix}"] for role in (0, 1)]
        output[f"question_mean.{suffix}"] = sum(values) / 2 if all(v is not None for v in values) else None
    return output


def metric_names():
    keys = ["candidate_count", "shared_feasible_count"]
    keys += [f"joint.histogram.{k}" for k in HIST_KEYS] + [f"joint.counts.{k}" for k in COUNT_KEYS]
    keys += [f"shared.{k}" for k in ("threshold", "worst_risk", "error_minus_target")]
    for role in (0, 1):
        keys += [f"q{role}.histogram.{k}" for k in HIST_KEYS] + [f"q{role}.counts.{k}" for k in COUNT_KEYS]
        keys += [f"q{role}.minimum.{k}" for k in ("threshold", "retained_n", "incorrect_n", "coverage", "risk", "error_minus_target", "oracle_risk_gap")]
        keys += [f"q{role}.oracle.{k}" for k in ("original_n", "correct_n", "coverage_minimum_n", "minimum_n", "minimum_risk", "maximum_retained_n", "maximum_coverage")]
        keys += [f"q{role}.shared.{k}" for k in ("retained_n", "incorrect_n", "coverage", "risk")]
    keys += [f"question_mean.{k}" for k in ("minimum.risk", "minimum.coverage", "minimum.oracle_risk_gap", "oracle.minimum_risk", "oracle.maximum_coverage", "shared.risk", "shared.coverage")]
    return tuple(keys)


def aggregate(records, oracles):
    if len(records) != 90 or len(oracles) != 30:
        raise ValueError("Incomplete E008 diagnostic grid.")
    oracle_by_id = {o["oracle_id"]: o for o in oracles}
    if len(oracle_by_id) != 30:
        raise ValueError("Duplicate oracle records.")
    summaries = []
    for variant in VARIANTS:
        for rule in RULES:
            for target in (20, 10, 30):
                rows = sorted([r for r in records if (r["variant"], r["rule"], r["target_percent"]) ==
                               (variant, rule, target)], key=lambda r: r["fold"])
                if [r["fold"] for r in rows] != list(range(5)):
                    raise ValueError("Missing or duplicate fold.")
                values = [numeric_metrics(r, oracle_by_id) for r in rows]
                if any(set(v) != set(metric_names()) for v in values):
                    raise ValueError("Numeric metric contract changed.")
                summaries.append({"variant": variant, "rule": rule, "target_percent": target,
                                  "outcome_counts": {code: sum(r["outcome"] == code for r in rows) for code in CODES},
                                  "metrics": {key: {**mean_sd([v[key] for v in values]),
                                                     "fold_values": [v[key] for v in values]} for key in metric_names()}})
    for fold in range(5):
        for target in TARGETS:
            aligned = [r for r in records if r["rule"] == "frequency" and r["fold"] == fold and r["target_percent"] == target]
            stripped = [{k: v for k, v in r.items() if k != "variant"} for r in aligned]
            if len(stripped) != 2 or stripped[0] != stripped[1]:
                raise ValueError("Frequency duplicate arms differ.")
    return summaries
