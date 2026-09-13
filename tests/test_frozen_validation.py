import pandas as pd
import pytest

from map_misconceptions.frozen_validation import validate_assignments
from map_misconceptions.splits import build_grouped_folds


def fixture():
    frame = pd.DataFrame({
        "QuestionId": [str(q) for q in range(15) for _ in range(2)],
        "Category": ["False_Misconception"] * 30,
        "Misconception": ["synthetic"] * 30,
    })
    return frame, build_grouped_folds(frame, 5, 20260831)


def test_accepts_original_ordered_group_disjoint_split():
    frame, assignments = fixture()
    validate_assignments(frame, assignments, 5)


@pytest.mark.parametrize("mutation", ["reorder", "question", "target", "role", "leakage", "evaluation_twice"])
def test_rejects_invalid_frozen_assignment(mutation):
    frame, assignments = fixture()
    if mutation == "reorder":
        assignments = assignments.iloc[::-1].reset_index(drop=True)
    elif mutation == "question":
        assignments.loc[0, "QuestionId"] = "other"
    elif mutation == "target":
        assignments.loc[0, "target"] = "other"
    elif mutation == "role":
        assignments.loc[0, "fold_0"] = "unused"
    elif mutation == "leakage":
        assignments.loc[0, "fold_0"] = (
            "evaluation" if assignments.loc[1, "fold_0"] != "evaluation" else "train"
        )
    else:
        # Group-disjoint but evaluated twice: replace one entire fold with another.
        assignments["fold_1"] = assignments["fold_0"]
    with pytest.raises(ValueError):
        validate_assignments(frame, assignments, 5)
