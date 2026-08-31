import pandas as pd

from map_misconceptions.diagnostics import run_support_overlap_diagnostic


def test_diagnostic_emits_aggregate_counts_without_text() -> None:
    frame = pd.DataFrame(
        {
            "QuestionId": ["q1", "q1", "q2", "q3"],
            "QuestionText": ["one", "one", "two", "three"],
            "MC_Answer": ["a", "a", "b", "c"],
            "StudentExplanation": ["same answer", "unique response", "same answer", "new thought"],
            "Category": ["True", "True", "True", "False"],
            "Misconception": ["NA", "NA", "NA", "M1"],
        }
    )
    assignments = pd.DataFrame(
        {
            "source_row": [0, 1, 2, 3],
            "QuestionId": ["q1", "q1", "q2", "q3"],
            "fold_0": ["train", "train", "evaluation", "evaluation"],
        }
    )

    result = run_support_overlap_diagnostic(frame, assignments, n_splits=1)

    fold = result["folds"][0]
    assert fold["evaluation_rows_with_exact_train_explanation"] == 1
    assert fold["evaluation_rows_with_unsupported_label"] == 1
    assert "same answer" not in str(result)
