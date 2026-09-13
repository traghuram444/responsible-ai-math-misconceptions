"""Read-only, aggregate-only validation; never regenerate or overwrite frozen files."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from .data_contract import combined_label, file_sha256, load_training_data
from .splits import build_grouped_folds


def validate_assignments(frame: pd.DataFrame, assignments: pd.DataFrame, n_splits: int) -> None:
    columns = [f"fold_{fold}" for fold in range(n_splits)]
    required = {"source_row", "QuestionId", "target", *columns}
    if set(assignments.columns) != required or len(frame) != len(assignments):
        raise ValueError("Assignment shape/columns differ from frozen contract.")
    if not np.array_equal(assignments.source_row, np.arange(len(frame))):
        raise ValueError("Assignment source rows must preserve exact input order.")
    if not np.array_equal(assignments.QuestionId.astype(str), frame.QuestionId.astype(str)):
        raise ValueError("Assignment questions do not match ordered input.")
    if not np.array_equal(assignments.target.astype(str), combined_label(frame)):
        raise ValueError("Assignment targets do not match ordered input.")
    for column in columns:
        if set(assignments[column]) != {"train", "calibration", "evaluation"}:
            raise ValueError("Every fold must contain exactly the three registered roles.")
        if (assignments.groupby("QuestionId")[column].nunique() != 1).any():
            raise ValueError("A question spans roles within an outer fold.")
    if not (assignments[columns].eq("evaluation").sum(axis=1) == 1).all():
        raise ValueError("Each row must be evaluated in exactly one outer fold.")


def verify_frozen_inputs(
    input_path: Path, split_dir: Path, *, expected_data_sha: str,
    expected_manifest_sha: str, expected_assignments_sha: str,
) -> dict:
    manifest_path = split_dir / "manifest.json"
    assignment_path = split_dir / "grouped_fold_assignments.csv"
    expected = [(input_path, expected_data_sha), (manifest_path, expected_manifest_sha),
                (assignment_path, expected_assignments_sha)]
    for path, digest in expected:
        if file_sha256(path) != digest:
            raise ValueError("A frozen input fingerprint differs; do not regenerate the split.")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["input_sha256"] != expected_data_sha or manifest["n_splits"] != 5:
        raise ValueError("Manifest contract differs from the five-fold study.")
    if manifest["seed"] != 20260831 or manifest["inner_calibration_fraction"] != 0.2:
        raise ValueError("Frozen seed or calibration fraction differs.")
    frame = load_training_data(input_path)
    assignments = pd.read_csv(assignment_path, keep_default_na=False)
    if len(frame) != manifest["rows"] or frame.QuestionId.nunique() != manifest["question_groups"]:
        raise ValueError("Manifest data shape mismatch.")
    validate_assignments(frame, assignments, n_splits=5)
    # Deterministic comparison is in memory only; no replacement manifest is saved.
    regenerated = build_grouped_folds(frame, n_splits=5, seed=20260831)
    for column in regenerated:
        if not np.array_equal(regenerated[column].astype(str), assignments[column].astype(str)):
            raise ValueError("Current assignments differ from the original deterministic algorithm.")
    return {
        "data_sha256": expected_data_sha,
        "manifest_sha256": expected_manifest_sha,
        "assignment_sha256_observed_2026_09_13": expected_assignments_sha,
        "rows": len(frame), "questions": int(frame.QuestionId.nunique()),
        "ordered_rows_and_targets_match": True, "roles_question_disjoint": True,
        "each_row_evaluated_once": True, "deterministic_split_reconstruction_matches": True,
        "note": "Assignment hash is a current snapshot, not proof of historical file identity.",
    }
