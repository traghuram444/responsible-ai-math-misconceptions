import numpy as np

from map_misconceptions.e001 import supported_label_summary


def test_supported_label_summary_excludes_unavailable_labels_only() -> None:
    summary = supported_label_summary(
        np.array(["A", "B", "C"]),
        np.array([[0.9, 0.1], [0.2, 0.8], [0.7, 0.3]]),
        np.array(["A", "B"]),
    )
    assert summary["n"] == 2
    assert summary["rate"] == 2 / 3
    assert summary["metrics"]["top1_accuracy"] == 1.0
