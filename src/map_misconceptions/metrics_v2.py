"""Corrected metrics for future work; historical metrics.py is intentionally frozen."""

from __future__ import annotations

import numpy as np


def union_label_brier_score(
    y_true: np.ndarray, probabilities: np.ndarray, classes: np.ndarray
) -> float:
    """Unnormalized multiclass Brier over predicted AND observed outcome labels.

    An unseen true label has predicted probability zero, but its one-hot target
    still contributes one. Consequently this score equals the historical score
    plus the unsupported true-label fraction (not the predicted-label fraction).
    The range is [0, 2]. This function does not modify or renormalize probabilities.
    """
    truth = np.asarray(y_true)
    labels = np.asarray(classes)
    prob = np.asarray(probabilities, dtype=np.float64)
    if truth.ndim != 1 or labels.ndim != 1 or prob.ndim != 2:
        raise ValueError("Expected one-dimensional labels and a probability matrix.")
    if not len(truth) or not len(labels) or prob.shape != (len(truth), len(labels)):
        raise ValueError("Nonempty labels and matching probability dimensions required.")
    if len(np.unique(labels)) != len(labels):
        raise ValueError("Predicted classes must be unique.")
    if not np.isfinite(prob).all() or (prob < 0).any() or (prob > 1).any():
        raise ValueError("Probabilities must be finite and in [0, 1].")
    if not np.allclose(prob.sum(axis=1), 1.0, rtol=0, atol=1e-8):
        raise ValueError("Each probability row must sum to one.")
    true_probability = (prob * (truth[:, None] == labels[None, :])).sum(axis=1)
    losses = np.square(prob).sum(axis=1) - 2 * true_probability + 1
    return float(losses.mean())
