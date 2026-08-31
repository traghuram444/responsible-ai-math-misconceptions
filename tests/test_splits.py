import pandas as pd

from map_misconceptions.splits import assert_no_group_leakage, build_grouped_folds


def test_grouped_folds_are_question_disjoint() -> None:
    frame = pd.DataFrame(
        {
            "QuestionId": [f"q{i}" for i in range(5) for _ in range(3)],
            "QuestionText": ["question"] * 15,
            "MC_Answer": ["answer"] * 15,
            "StudentExplanation": ["explanation"] * 15,
            "Category": ["False_Misconception"] * 15,
            "Misconception": ["Wrong_operation"] * 15,
        }
    )
    assignments = build_grouped_folds(frame, n_splits=5, seed=7)
    assert_no_group_leakage(assignments, n_splits=5)
    for fold in range(5):
        assert set(assignments[f"fold_{fold}"]) == {"train", "calibration", "evaluation"}
