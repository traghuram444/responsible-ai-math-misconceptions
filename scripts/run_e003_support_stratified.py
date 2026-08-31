"""Run preregistered E003 support-stratified grouped baseline evaluation."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from map_misconceptions.data_contract import file_sha256, load_training_data
from map_misconceptions.e001 import aggregate, run_grouped


def compact_result(result: dict) -> dict:
    fields = (
        "fold",
        "n_train",
        "n_calibration",
        "n_evaluation",
        "unsupported_evaluation_label_rate",
        "frequency_baseline",
        "tfidf_logreg",
        "supported_label_subset",
    )
    folds = [{field: fold[field] for field in fields} for fold in result["folds"]]
    supported = {}
    for model in ("frequency_baseline", "tfidf_logreg"):
        metric_names = ("top1_accuracy", "macro_f1_all_eval_labels", "map_at_3", "ece_10_equal_width", "multiclass_brier")
        supported[model] = {
            metric: float(np.mean([fold["supported_label_subset"][model]["metrics"][metric] for fold in folds]))
            for metric in metric_names
        }
    return {"variant": result["variant"], "all_evaluation": aggregate(result), "supported_label_subset_mean": supported, "folds": folds}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run E003 support-stratified grouped evaluation.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--splits", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    frame = load_training_data(args.input)
    assignments = pd.read_csv(args.splits / "grouped_fold_assignments.csv", keep_default_na=False)
    manifest_path = args.splits / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["input_sha256"] != file_sha256(args.input):
        raise ValueError("Input SHA-256 differs from frozen split manifest.")
    results = [compact_result(run_grouped(frame, assignments, variant)) for variant in ("explanation_only", "question_plus_explanation")]
    payload = {
        "experiment_id": "E003",
        "input_sha256": file_sha256(args.input),
        "split_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "protocol": "support_stratified_grouped_e001_reproduction_v1",
        "output_policy": "aggregate_only_no_text_no_row_level_outputs",
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote aggregate-only E003 results to {args.output}")


if __name__ == "__main__":
    main()
