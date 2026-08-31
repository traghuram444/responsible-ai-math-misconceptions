"""Question-grouped cross-validation manifests.

No response from a QuestionId can occur in both train and evaluation portions of a fold.
"""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd
from sklearn.model_selection import GroupKFold, GroupShuffleSplit

from .data_contract import combined_label, file_sha256, load_training_data


def build_grouped_folds(
    frame: pd.DataFrame, n_splits: int, seed: int, calibration_fraction: float = 0.2
) -> pd.DataFrame:
    """Return row-level fold assignments with train/calibration/evaluation roles.

    Each outer evaluation fold is completely question-disjoint from the inner training
    pool. Calibration is then selected by QuestionId from that pool, preserving the
    separation needed for post-hoc temperature scaling.
    """
    groups = frame["QuestionId"].astype(str)
    if groups.nunique() < n_splits:
        raise ValueError("n_splits cannot exceed the number of unique QuestionId groups.")
    if not 0 < calibration_fraction < 1:
        raise ValueError("calibration_fraction must be between 0 and 1.")

    result = pd.DataFrame(
        {
            "source_row": frame.index,
            "QuestionId": groups,
            "target": combined_label(frame),
        }
    )
    outer = GroupKFold(n_splits=n_splits)
    for fold, (train_pool_idx, eval_idx) in enumerate(outer.split(frame, groups=groups)):
        train_pool_groups = groups.iloc[train_pool_idx]
        if train_pool_groups.nunique() < 2:
            raise ValueError("At least two training QuestionId groups are needed for calibration.")
        inner = GroupShuffleSplit(
            n_splits=1, test_size=calibration_fraction, random_state=seed + fold
        )
        inner_train_rel, calibration_rel = next(
            inner.split(train_pool_idx, groups=train_pool_groups)
        )
        train_idx = train_pool_idx[inner_train_rel]
        calibration_idx = train_pool_idx[calibration_rel]
        result[f"fold_{fold}"] = "unused"
        result.loc[result.index[train_idx], f"fold_{fold}"] = "train"
        result.loc[result.index[calibration_idx], f"fold_{fold}"] = "calibration"
        result.loc[result.index[eval_idx], f"fold_{fold}"] = "evaluation"
    return result


def assert_no_group_leakage(assignments: pd.DataFrame, n_splits: int) -> None:
    for fold in range(n_splits):
        roles = assignments[["QuestionId", f"fold_{fold}"]].drop_duplicates()
        counts = roles.groupby("QuestionId")[f"fold_{fold}"].nunique()
        leaked = counts[counts != 1]
        if not leaked.empty:
            raise AssertionError(f"QuestionId leakage in fold {fold}: {leaked.index.tolist()}")


def write_fold_artifacts(
    input_path: Path, output_dir: Path, n_splits: int, seed: int
) -> None:
    frame = load_training_data(input_path)
    assignments = build_grouped_folds(frame, n_splits=n_splits, seed=seed)
    assert_no_group_leakage(assignments, n_splits=n_splits)
    output_dir.mkdir(parents=True, exist_ok=True)
    assignments.to_csv(output_dir / "grouped_fold_assignments.csv", index=False)
    manifest = {
        "created_utc": datetime.now(UTC).isoformat(),
        "input_file": input_path.name,
        "input_sha256": file_sha256(input_path),
        "rows": len(frame),
        "question_groups": int(frame["QuestionId"].nunique()),
        "n_splits": n_splits,
        "seed": seed,
        "group_column": "QuestionId",
        "inner_calibration_fraction": 0.2,
        "target": "Category:Misconception",
        "protocol_version": "1.0",
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create frozen QuestionId-grouped folds.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--n-splits", type=int, default=5)
    parser.add_argument("--seed", type=int, default=20260831)
    args = parser.parse_args()
    write_fold_artifacts(args.input, args.output, args.n_splits, args.seed)


if __name__ == "__main__":
    main()
