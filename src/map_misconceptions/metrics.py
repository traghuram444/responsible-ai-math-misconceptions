"""Metrics for top-k classification, calibration, and selective prediction."""

from __future__ import annotations

import numpy as np
from sklearn.metrics import accuracy_score, f1_score


def map_at_3(y_true: np.ndarray, probabilities: np.ndarray, classes: np.ndarray) -> float:
    top = np.argsort(-probabilities, axis=1)[:, :3]
    scores = []
    for truth, row in zip(y_true, top, strict=True):
        ranks = np.where(classes[row] == truth)[0]
        scores.append(0.0 if len(ranks) == 0 else 1.0 / (int(ranks[0]) + 1))
    return float(np.mean(scores))


def expected_calibration_error(confidence: np.ndarray, correct: np.ndarray, bins: int = 10) -> float:
    """Equal-width ECE; the reported bin count is part of the experiment record."""
    edges = np.linspace(0.0, 1.0, bins + 1)
    result = 0.0
    for lower, upper in zip(edges[:-1], edges[1:], strict=True):
        membership = (confidence >= lower) & ((confidence < upper) if upper < 1 else (confidence <= upper))
        if membership.any():
            result += membership.mean() * abs(confidence[membership].mean() - correct[membership].mean())
    return float(result)


def multiclass_brier(y_true: np.ndarray, probabilities: np.ndarray, classes: np.ndarray) -> float:
    targets = (classes[None, :] == y_true[:, None]).astype(float)
    return float(np.mean(np.sum((probabilities - targets) ** 2, axis=1)))


def classification_summary(y_true: np.ndarray, probabilities: np.ndarray, classes: np.ndarray) -> dict[str, float]:
    predictions = classes[np.argmax(probabilities, axis=1)]
    correct = (predictions == y_true).astype(float)
    return {
        "n": int(len(y_true)),
        "top1_accuracy": float(accuracy_score(y_true, predictions)),
        "macro_f1_all_eval_labels": float(f1_score(y_true, predictions, average="macro", zero_division=0)),
        "map_at_3": map_at_3(y_true, probabilities, classes),
        "ece_10_equal_width": expected_calibration_error(probabilities.max(axis=1), correct, bins=10),
        "multiclass_brier": multiclass_brier(y_true, probabilities, classes),
    }


def risk_coverage(y_true: np.ndarray, probabilities: np.ndarray, classes: np.ndarray) -> list[dict[str, float]]:
    predictions = classes[np.argmax(probabilities, axis=1)]
    confidence = probabilities.max(axis=1)
    correct = predictions == y_true
    output: list[dict[str, float]] = []
    for review_rate in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5):
        retained = max(1, int(np.ceil(len(y_true) * (1.0 - review_rate))))
        keep = np.argsort(-confidence)[:retained]
        retained_accuracy = float(correct[keep].mean())
        output.append(
            {
                "human_review_rate": review_rate,
                "ai_coverage": retained / len(y_true),
                "ai_handled_n": retained,
                "ai_handled_accuracy": retained_accuracy,
                "ai_handled_risk": 1.0 - retained_accuracy,
            }
        )
    return output
