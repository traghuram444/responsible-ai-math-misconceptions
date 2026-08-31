"""Run the preregistered E002 support and overlap diagnostic."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from map_misconceptions.data_contract import file_sha256, load_training_data
from map_misconceptions.diagnostics import manifest_sha256, run_support_overlap_diagnostic


def main() -> None:
    parser = argparse.ArgumentParser(description="Run E002 aggregate-only diagnostics.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--splits", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    manifest_path = args.splits / "manifest.json"
    assignments_path = args.splits / "grouped_fold_assignments.csv"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    frame = load_training_data(args.input)
    assignments = pd.read_csv(assignments_path, keep_default_na=False)
    result = run_support_overlap_diagnostic(frame, assignments, n_splits=int(manifest["n_splits"]))
    result.update(
        {
            "experiment_id": "E002",
            "input_sha256": file_sha256(args.input),
            "split_manifest_sha256": manifest_sha256(manifest_path),
            "protocol": "support_and_cross_question_overlap_v1",
            "output_policy": "aggregate_only_no_text_no_row_level_outputs",
        }
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Wrote aggregate-only E002 diagnostics to {args.output}")


if __name__ == "__main__":
    main()
