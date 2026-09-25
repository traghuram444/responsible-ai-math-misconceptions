"""E007 fixed-cutoff selection. No evaluation labels enter policy construction."""
from __future__ import annotations

from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
import hashlib

import numpy as np

from .metrics import expected_calibration_error, map_at_3
from .metrics_v2 import union_label_brier_score

TARGETS = (10, 20, 30)
RULES = ("confidence_only", "support_aware", "frequency")
STRATA = ("all", "unsupported", "rare", "frequent", "well_supported")
METRICS = ("original_n", "retained_n", "correct_n", "incorrect_n", "coverage",
           "review_fraction", "share_of_retained", "top1_accuracy", "map_at_3", "risk",
           "mean_confidence", "ece", "brier", "error_minus_target")


def canonical_question(value) -> int:
    if isinstance(value, (bool, np.bool_)):
        raise ValueError("Boolean question identifier.")
    try:
        number = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("Invalid question identifier.") from exc
    if not number.is_finite() or number < 0 or number != number.to_integral_value():
        raise ValueError("Question identifiers must be nonnegative integers.")
    return int(number)


def calibration_roles(question_ids, fold):
    if fold not in range(5):
        raise ValueError("Invalid fold.")
    questions = sorted({canonical_question(q) for q in question_ids})
    if len(questions) != 3:
        raise ValueError("Exactly three calibration questions required.")
    def key(q):
        message = f"E007|fold={fold}|QuestionId={q}|seed=20260831"
        return hashlib.sha256(message.encode("utf-8")).hexdigest(), q
    ordered = sorted(questions, key=key)
    return ordered[0], tuple(ordered[1:])


def routing_scores(probabilities, classes, training_labels, rule):
    prob = np.asarray(probabilities, dtype=np.float64)
    classes = np.asarray(classes)
    counts = Counter(training_labels)
    if rule not in RULES or set(classes) != set(counts):
        raise ValueError("Invalid rule or training vocabulary.")
    if prob.ndim != 2 or prob.shape[1] != len(classes) or not len(prob):
        raise ValueError("Invalid probability shape.")
    if not np.isfinite(prob).all() or (prob < 0).any() or (prob > 1).any():
        raise ValueError("Invalid probabilities.")
    if not np.allclose(prob.sum(axis=1), 1, atol=1e-8, rtol=0):
        raise ValueError("Probabilities do not sum to one.")
    score = prob.max(axis=1)
    if rule == "frequency" and not np.array_equal(prob, np.broadcast_to(prob[0], prob.shape)):
        raise ValueError("Frequency probabilities must be constant.")
    if rule == "support_aware":
        predicted = classes[np.argmax(prob, axis=1)]
        score = score * np.log1p([counts[p] for p in predicted]) / np.log1p(max(counts.values()))
    return score


def apply_cutoff(scores, policy):
    scores = np.asarray(scores, dtype=np.float64)
    if scores.ndim != 1 or not np.isfinite(scores).all():
        raise ValueError("Invalid selection scores.")
    if policy["status"] == "NO_ADMISSIBLE_THRESHOLD":
        if policy["threshold"] is not None:
            raise ValueError("Absent policy must have null threshold.")
        return np.zeros(len(scores), dtype=bool)
    if policy["status"] != "SELECTED" or policy["threshold"] is None:
        raise ValueError("Invalid policy.")
    if not np.isfinite(policy["threshold"]):
        raise ValueError("Nonfinite cutoff.")
    return scores >= policy["threshold"]


def select_cutoff(scores, correct, question_roles, target_percent):
    """Exhaustive distinct-score search using cumulative counts, not monotonic risk."""
    score = np.asarray(scores, dtype=np.float64)
    correct = np.asarray(correct)
    groups = np.asarray(question_roles)
    if target_percent not in TARGETS:
        raise ValueError("Unregistered target.")
    if (score.ndim != 1 or not len(score) or correct.shape != score.shape
            or groups.shape != score.shape or correct.dtype != bool
            or set(groups.tolist()) != {0, 1} or not np.isfinite(score).all()
            or (score < 0).any() or (score > 1).any()):
        raise ValueError("Invalid development inputs.")
    candidates = np.unique(np.concatenate(([0.0], score)))
    counts, errors, original = [], [], []
    for group in (0, 1):
        mask = groups == group
        order = np.argsort(score[mask], kind="stable")
        group_score = score[mask][order]
        group_error = (~correct[mask][order]).astype(np.int64)
        prefix = np.concatenate(([0], np.cumsum(group_error)))
        starts = np.searchsorted(group_score, candidates, side="left")
        counts.append(len(order) - starts)
        errors.append(prefix[-1] - prefix[starts])
        original.append(len(order))
    counts, errors = np.asarray(counts), np.asarray(errors)
    admissible = ((counts >= 100) & (counts * 10 >= np.asarray(original)[:, None])
                  & (errors * 100 <= target_percent * counts)).all(axis=0)
    eligible = np.flatnonzero(admissible)
    winner = int(eligible[np.argmax(counts[:, eligible].sum(axis=0))]) if len(eligible) else None
    threshold = float(candidates[winner]) if winner is not None else None
    development = []
    for group in (0, 1):
        n = int(counts[group, winner]) if winner is not None else 0
        e = int(errors[group, winner]) if winner is not None else 0
        development.append({"role_index": group, "original_n": original[group],
                            "retained_n": n, "incorrect_n": e,
                            "coverage": n / original[group], "risk": e / n if n else None})
    return {"target_percent": target_percent,
            "status": "SELECTED" if winner is not None else "NO_ADMISSIBLE_THRESHOLD",
            "threshold": threshold, "candidate_count": len(candidates),
            "admissible_candidate_count": int(admissible.sum()), "development": development}


def support_masks(truth, train_labels, train_questions):
    counts = Counter(train_labels)
    questions = defaultdict(set)
    for label, q in zip(train_labels, train_questions, strict=True):
        questions[label].add(q)
    n = np.asarray([counts[label] for label in truth])
    qn = np.asarray([len(questions[label]) for label in truth])
    return {"all": np.ones(len(truth), dtype=bool), "unsupported": n == 0,
            "rare": (n >= 1) & (n <= 19), "frequent": n >= 20,
            "well_supported": (n >= 20) & (qn >= 2)}


def summarize_group(truth, probabilities, classes, membership, retained, target_percent):
    keep = membership & retained
    original = int(membership.sum())
    n = int(keep.sum())
    confidence = probabilities.max(axis=1)
    correct = classes[np.argmax(probabilities, axis=1)] == truth
    correct_n = int(correct[keep].sum())
    errors = n - correct_n
    risk = errors / n if n else None
    reasons = []
    if n < 200:
        reasons.append("n_below_200")
    if correct_n < 20:
        reasons.append("correct_below_20")
    if errors < 20:
        reasons.append("incorrect_below_20")
    eligible = not reasons
    return {"original_n": original, "retained_n": n, "correct_n": correct_n,
            "incorrect_n": errors, "coverage": n / original if original else None,
            "review_fraction": 1 - n / original if original else None,
            "share_of_retained": n / int(retained.sum()) if retained.any() else None,
            "top1_accuracy": correct_n / n if n else None,
            "map_at_3": map_at_3(truth[keep], probabilities[keep], classes) if n else None,
            "risk": risk, "mean_confidence": float(confidence[keep].mean()) if n else None,
            "ece": expected_calibration_error(confidence[keep], correct[keep], 10) if eligible else None,
            "brier": union_label_brier_score(truth[keep], probabilities[keep], classes) if eligible else None,
            "calibration_ineligible_reasons": reasons,
            "error_minus_target": risk - target_percent / 100 if n and target_percent is not None else None,
            "target_exceeded": bool(errors * 100 > target_percent * n) if n and target_percent is not None else None,
            "risk_target_met": bool(errors * 100 <= target_percent * n) if n and target_percent is not None else None,
            "count_floor_met": n >= 100,
            "coverage_floor_met": bool(original > 0 and n * 10 >= original)}


def evaluate_policy(truth, probabilities, classes, train_labels, train_questions,
                    evaluation_questions, score, policy):
    truth, prob, classes = np.asarray(truth), np.asarray(probabilities), np.asarray(classes)
    union_label_brier_score(truth, prob, classes)  # Validate shape and probabilities.
    questions = np.asarray(evaluation_questions)
    if questions.shape != truth.shape or len(score) != len(truth):
        raise ValueError("Evaluation shapes differ.")
    retained = (np.ones(len(truth), dtype=bool) if policy is None else apply_cutoff(score, policy))
    target = None if policy is None else policy["target_percent"]
    masks = support_masks(truth, train_labels, train_questions)
    def summary(scope):
        # Denominator for share_of_retained is within this question/fold scope.
        scoped_retained = retained & scope
        return {name: summarize_group(truth, prob, classes, mask & scope, scoped_retained, target)
                for name, mask in masks.items()}
    development_risk = (float(np.mean([q["risk"] for q in policy["development"]]))
                        if policy is not None and policy["status"] == "SELECTED" else None)
    per_question = []
    for question in sorted(set(questions.tolist())):
        groups = summary(questions == question)
        risk = groups["all"]["risk"]
        per_question.append({"QuestionId": canonical_question(question), "groups": groups,
                             "risk_minus_development": risk - development_risk
                             if risk is not None and development_risk is not None else None})
    return {"groups": summary(np.ones(len(truth), dtype=bool)), "questions": per_question}


def mean_sd(values):
    valid = [float(value) for value in values if value is not None]
    return {"mean": float(np.mean(valid)) if valid else None,
            "sd": float(np.std(valid, ddof=1)) if len(valid) >= 2 else None,
            "defined_folds": len(valid)}


def aggregate(records):
    """Strict registered grid; no data-dependent groups or winning-pair selection."""
    output, paired = [], []
    for variant in ("explanation_only", "question_plus_explanation"):
        for rule in RULES:
            for target in (None, *TARGETS):
                rows = [r for r in records if (r["variant"], r["rule"], r["target_percent"]) ==
                        (variant, rule, target)]
                if len(rows) != 5 or sorted(r["fold"] for r in rows) != list(range(5)):
                    raise ValueError("Incomplete or duplicate E007 fold grid.")
                questions = [q for r in rows for q in r["evaluation"]["questions"]]
                if len(questions) != 15 or len({q["QuestionId"] for q in questions}) != 15:
                    raise ValueError("Exactly 15 distinct evaluation questions required.")
                groups = {s: {m: mean_sd([r["evaluation"]["groups"][s][m] for r in rows])
                              for m in METRICS} for s in STRATA}
                all_q = [q["groups"]["all"] for q in questions]
                admitted = sum(r["policy"] is not None and r["policy"]["status"] == "SELECTED" for r in rows)
                nonempty = sum(q["retained_n"] > 0 for q in all_q)
                count_met = sum(q["count_floor_met"] for q in all_q)
                coverage_met = sum(q["coverage_floor_met"] for q in all_q)
                both_met = sum(q["count_floor_met"] and q["coverage_floor_met"] for q in all_q)
                risk_met = sum(q["risk_target_met"] is True for q in all_q)
                exceed = sum(q["target_exceeded"] is True for q in all_q)
                max_risk = max((q["risk"] for q in all_q if q["risk"] is not None), default=None)
                output.append({"variant": variant, "rule": rule, "target_percent": target,
                               "groups": groups, "admissible_folds": admitted if target else None,
                               "nonempty_questions": nonempty, "count_floor_questions": count_met,
                               "coverage_floor_questions": coverage_met, "both_floors_questions": both_met,
                               "risk_met_questions": risk_met if target else None,
                               "risk_exceeded_questions": exceed if target else None,
                               "maximum_question_risk": max_risk,
                               "useful_transfer": bool(admitted == 5 and both_met == 15 and risk_met == 15)
                               if target else None})
        for target in TARGETS:
            for left, right in (("support_aware", "confidence_only"),
                                ("confidence_only", "frequency"), ("support_aware", "frequency")):
                left_rows = sorted([r for r in records if (r["variant"], r["rule"], r["target_percent"]) ==
                                    (variant, left, target)], key=lambda r: r["fold"])
                right_rows = sorted([r for r in records if (r["variant"], r["rule"], r["target_percent"]) ==
                                     (variant, right, target)], key=lambda r: r["fold"])
                folds = []
                for a, b in zip(left_rows, right_rows, strict=True):
                    ga, gb = a["evaluation"]["groups"]["all"], b["evaluation"]["groups"]["all"]
                    folds.append({"fold": a["fold"], "left_coverage": ga["coverage"],
                                  "right_coverage": gb["coverage"],
                                  "coverage_difference": ga["coverage"] - gb["coverage"],
                                  "risk_difference": ga["risk"] - gb["risk"]
                                  if ga["risk"] is not None and gb["risk"] is not None else None})
                paired.append({"variant": variant, "target_percent": target, "left": left, "right": right,
                               "folds": folds, "coverage_difference": mean_sd([f["coverage_difference"] for f in folds]),
                               "risk_difference": mean_sd([f["risk_difference"] for f in folds])})
    if len(records) != 120:
        raise ValueError("Unexpected E007 records.")
    return {"summaries": output, "paired": paired}
