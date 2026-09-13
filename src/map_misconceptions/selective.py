"""E006's fixed, aggregate-only selective prediction evaluation.

Routing uses probabilities, training-label counts and unlabeled source positions.
True-label support is used only for reporting after global batch retention. This
module never fits a model, chooses a threshold, or returns per-response outputs.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
from math import ceil
from numbers import Integral

import numpy as np
from sklearn.metrics import roc_auc_score

from .metrics import expected_calibration_error, map_at_3, multiclass_brier
from .metrics_v2 import union_label_brier_score


REVIEW_FRACTIONS = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5)
GROUP_NAMES = ("all", "unsupported", "rare", "frequent", "well_supported")
RULE_NAMES = ("confidence_only", "support_aware", "frequency")


def _unsigned_integer(value, name: str) -> int:
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral) or value < 0:
        raise ValueError(f"{name} must be an unsigned integer.")
    return int(value)


def _routing_order(score: np.ndarray, source_rows: list[int], fold: int, seed: int) -> np.ndarray:
    """Resolve score ties using exactly the approved UTF-8 serialization."""
    digests = [
        hashlib.sha256(f"fold={fold};source_row={row};seed={seed}".encode("utf-8")).hexdigest()
        for row in source_rows
    ]
    return np.asarray(
        sorted(range(len(score)), key=lambda i: (-float(score[i]), digests[i], source_rows[i])),
        dtype=np.int64,
    )


def _group_summary(
    truth: np.ndarray,
    probabilities: np.ndarray,
    classes: np.ndarray,
    correct: np.ndarray,
    confidence: np.ndarray,
    membership: np.ndarray,
    retained: np.ndarray,
    all_retained_n: int,
) -> dict:
    original_n = int(membership.sum())
    keep = retained[membership[retained]]
    retained_n = int(len(keep))
    correct_n = int(correct[keep].sum())
    incorrect_n = retained_n - correct_n
    accuracy = float(correct[keep].mean()) if retained_n else None
    risk = 1.0 - accuracy if accuracy is not None else None
    original_risk = 1.0 - float(correct[membership].mean()) if original_n else None
    reasons = []
    if retained_n < 200:
        reasons.append("retained_n_below_200")
    if correct_n < 20:
        reasons.append("correct_n_below_20")
    if incorrect_n < 20:
        reasons.append("incorrect_n_below_20")
    eligible = not reasons
    return {
        "original_n": original_n,
        "retained_n": retained_n,
        "retention_fraction_of_original_group": retained_n / original_n if original_n else None,
        "fraction_of_all_retained_cases": retained_n / all_retained_n if all_retained_n else None,
        "top1_accuracy": accuracy,
        "map_at_3": map_at_3(truth[keep], probabilities[keep], classes) if retained_n else None,
        "risk": risk,
        "absolute_risk_reduction_vs_own_zero_review": (
            original_risk - risk if original_risk is not None and risk is not None else None
        ),
        "correct_n": correct_n,
        "incorrect_n": incorrect_n,
        "calibration_eligible": eligible,
        "calibration_ineligible_reason": ";".join(reasons) if reasons else None,
        "ece_10_equal_width": (
            expected_calibration_error(confidence[keep], correct[keep], bins=10) if eligible else None
        ),
        "legacy_multiclass_brier": (
            multiclass_brier(truth[keep], probabilities[keep], classes) if eligible else None
        ),
        "union_label_brier": (
            union_label_brier_score(truth[keep], probabilities[keep], classes) if eligible else None
        ),
    }


def evaluate_routing(
    y_true,
    probabilities,
    classes,
    train_labels,
    train_question_ids,
    source_rows,
    fold,
    seed=20260831,
    rules=("confidence_only", "support_aware"),
) -> dict:
    """Evaluate the locked six review budgets without returning row-level data.

    Counts and distinct question counts refer exclusively to the supplied training
    role. Classes must be precisely that role's label set. Empty reporting groups
    have null performance, not zero performance. Count ratios with a nonzero
    denominator remain defined, including a zero share of the global retained set.
    """
    truth = np.asarray(y_true)
    prob = np.asarray(probabilities, dtype=np.float64)
    labels = np.asarray(classes)
    training = np.asarray(train_labels)
    questions = np.asarray(train_question_ids)
    rows_array = np.asarray(source_rows)
    fold = _unsigned_integer(fold, "fold")
    seed = _unsigned_integer(seed, "seed")
    if any(array.ndim != 1 for array in (truth, labels, training, questions, rows_array)):
        raise ValueError("Labels, training questions, and source rows must be one-dimensional.")
    if not len(truth) or not len(training) or len(training) != len(questions):
        raise ValueError("Nonempty evaluation and matching nonempty training labels/questions required.")
    if len(rows_array) != len(truth):
        raise ValueError("Each evaluation case needs one source-row position.")
    rows = [_unsigned_integer(row, "source_row") for row in rows_array.tolist()]
    if len(set(rows)) != len(rows):
        raise ValueError("Source-row positions must be unique.")
    # Reuse the corrected metric's shape, uniqueness and probability validation.
    # The returned score is intentionally unused and never used for routing.
    union_label_brier_score(truth, prob, labels)
    counts = Counter(training.tolist())
    if set(labels.tolist()) != set(counts):
        raise ValueError("Model classes must equal the training-role label set.")
    rules = tuple(rules)
    if not rules or len(set(rules)) != len(rules) or any(rule not in RULE_NAMES for rule in rules):
        raise ValueError("Routing rules must be a nonempty, unique subset of the registered rules.")
    if "frequency" in rules and not np.array_equal(prob, np.broadcast_to(prob[0], prob.shape)):
        raise ValueError("The frequency rule requires identical fold-local probabilities for every case.")

    label_questions = defaultdict(set)
    for label, question in zip(training.tolist(), questions.tolist(), strict=True):
        label_questions[label].add(question)
    support = np.asarray([counts[label] for label in truth], dtype=np.int64)
    question_support = np.asarray([len(label_questions[label]) for label in truth], dtype=np.int64)
    groups = {
        "all": np.ones(len(truth), dtype=bool),
        "unsupported": support == 0,
        "rare": (support >= 1) & (support <= 19),
        "frequent": support >= 20,
        "well_supported": (support >= 20) & (question_support >= 2),
    }
    # Preserve E001's argmax and MAP@3 class-tie semantics; only routing ties use SHA-256.
    predicted = labels[np.argmax(prob, axis=1)]
    correct = predicted == truth
    confidence = prob.max(axis=1)
    predicted_count = np.asarray([counts[label] for label in predicted], dtype=np.float64)
    factor = np.log1p(predicted_count) / np.log1p(max(counts.values()))
    scores = {"confidence_only": confidence, "support_aware": confidence * factor, "frequency": confidence}
    routing = []
    for rule in rules:
        order = _routing_order(scores[rule], rows, fold, seed)
        budgets = []
        for review_fraction in REVIEW_FRACTIONS:
            retained_n = ceil(len(truth) * (1.0 - review_fraction))
            retained = order[:retained_n]
            budgets.append(
                {
                    "review_fraction": review_fraction,
                    "groups": {
                        name: _group_summary(
                            truth, prob, labels, correct, confidence, membership, retained, retained_n
                        )
                        for name, membership in groups.items()
                    },
                }
            )
        routing.append({"rule": rule, "budgets": budgets})
    confidence_auroc = (
        float(roc_auc_score(correct, confidence))
        if any(rule != "frequency" for rule in rules) and correct.any() and (~correct).any()
        else None
    )
    return {"confidence_auroc": confidence_auroc, "routing": routing}
