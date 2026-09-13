"""Synthetic regressions: no MAP data needed."""

import numpy as np
import pytest

from map_misconceptions.metrics import multiclass_brier
from map_misconceptions.metrics_v2 import union_label_brier_score


def test_supported_matches_legacy():
    truth = np.array(["a", "b"])
    classes = np.array(["a", "b"])
    prob = np.array([[0.8, 0.2], [0.3, 0.7]])
    assert union_label_brier_score(truth, prob, classes) == pytest.approx(0.13)
    assert union_label_brier_score(truth, prob, classes) == pytest.approx(
        multiclass_brier(truth, prob, classes)
    )


def test_unsupported_adds_missing_one_hot_term():
    classes = np.array(["a", "b"])
    truth = np.array(["unseen"])
    prob = np.array([[0.8, 0.2]])
    assert multiclass_brier(truth, prob, classes) == pytest.approx(0.68)
    assert union_label_brier_score(truth, prob, classes) == pytest.approx(1.68)


def test_explicit_union_equals_implicit_union():
    truth = np.array(["a", "unseen", "other_unseen"])
    classes = np.array(["a", "b"])
    prob = np.array([[0.8, 0.2], [0.3, 0.7], [0.5, 0.5]])
    full_classes = np.array(["a", "b", "unseen", "other_unseen"])
    full_prob = np.pad(prob, ((0, 0), (0, 2)))
    corrected = union_label_brier_score(truth, prob, classes)
    assert corrected == pytest.approx(multiclass_brier(truth, full_prob, full_classes))
    assert corrected - multiclass_brier(truth, prob, classes) == pytest.approx(2 / 3)


def test_model_difference_cancels_only_on_same_population():
    truth = np.array(["a", "unseen"])
    classes = np.array(["a", "b"])
    first = np.array([[0.8, 0.2], [0.3, 0.7]])
    second = np.full((2, 2), 0.5)
    assert (
        union_label_brier_score(truth, first, classes)
        - union_label_brier_score(truth, second, classes)
    ) == pytest.approx(
        multiclass_brier(truth, first, classes) - multiclass_brier(truth, second, classes)
    )
    assert union_label_brier_score(truth[1:], first[1:], classes) - multiclass_brier(
        truth[1:], first[1:], classes
    ) == pytest.approx(1)
    assert union_label_brier_score(truth[:1], first[:1], classes) - multiclass_brier(
        truth[:1], first[:1], classes
    ) == pytest.approx(0)


@pytest.mark.parametrize("prob", [[[0.2, 0.2]], [[-0.1, 1.1]], [[float('nan'), 0.5]]])
def test_rejects_invalid_probabilities(prob):
    with pytest.raises(ValueError):
        union_label_brier_score(np.array(["a"]), np.array(prob), np.array(["a", "b"]))


def test_rejects_empty_duplicate_and_mismatched_inputs():
    with pytest.raises(ValueError):
        union_label_brier_score(np.array([]), np.empty((0, 2)), np.array(["a", "b"]))
    with pytest.raises(ValueError):
        union_label_brier_score(np.array(["a"]), np.array([[0.5, 0.5]]), np.array(["a", "a"]))
    with pytest.raises(ValueError):
        union_label_brier_score(np.array(["a", "b"]), np.array([[1.0]]), np.array(["a"]))
