import json

import pandas as pd

from map_misconceptions import e001
from map_misconceptions.splits import write_fold_artifacts


def test_e001_runs_with_frozen_splits_without_outer_fold_tuning(tmp_path, monkeypatch) -> None:
    rows = []
    for question in range(15):
        for response in range(10):
            label = "Wrong_operation" if response % 2 else "Incomplete"
            rows.append(
                {
                    "QuestionId": f"q{question}",
                    "QuestionText": f"Compute value for question {question}",
                    "MC_Answer": "A",
                    "StudentExplanation": f"student explanation {label} {response}",
                    "Category": "False_Misconception",
                    "Misconception": label,
                }
            )
    source = tmp_path / "train.csv"
    pd.DataFrame(rows).to_csv(source, index=False)
    split_dir = tmp_path / "splits"
    write_fold_artifacts(source, split_dir, n_splits=5, seed=20260831)
    monkeypatch.setattr(e001, "GRID", ({"ngram_range": (1, 1), "min_df": 2, "C": 1.0},))
    output = tmp_path / "e001.json"
    monkeypatch.setattr(
        "sys.argv",
        ["run_e001.py", "--input", str(source), "--splits", str(split_dir), "--output", str(output)],
    )
    e001.main()
    result = json.loads(output.read_text(encoding="utf-8"))
    assert result["experiment_id"] == "E001"
    assert len(result["results"]) == 4
