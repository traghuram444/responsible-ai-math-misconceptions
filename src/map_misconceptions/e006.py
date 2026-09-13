"""Approved selective-prediction experiment; frozen E001 fit code is reused unchanged."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
import os
from pathlib import Path
import re
import sys
import time

import numpy as np
import pandas as pd
import yaml
from sklearn.model_selection import GroupKFold

from . import e001
from .data_contract import combined_label, file_sha256, load_training_data
from .frozen_validation import verify_frozen_inputs
from .live_status import LiveStatus
from .metrics import classification_summary
from .selective import evaluate_routing
from .selective_report import aggregate_results


VARIANTS = ("explanation_only", "question_plus_explanation")
GATE_METRICS = ("map_at_3", "top1_accuracy", "ece_10_equal_width")
APPROVED_PROTOCOL_SHA = "f8993a5f21c16de36878f1b251ed2b9e365c021543c71dcf3105de2cce9579a1"
APPROVED_CONFIG_SHA = "d18f60520635d297b50290c7d7c75e00add86c6656163ede789358fac826b042"


def canonical_sha(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def approved_config(root: Path) -> dict:
    approval = yaml.safe_load((root / "experiments/e006_approval.yaml").read_text(encoding="utf-8"))
    if approval["status"] != "approved_locked_for_execution":
        raise ValueError("Explicit locked approval is required.")
    paths = [("docs/E006_REVIEW_ADDENDUM.md", APPROVED_PROTOCOL_SHA),
             ("experiments/e006_review_addendum.yaml", APPROVED_CONFIG_SHA)]
    for relative, expected in paths:
        if canonical_sha(root / relative) != expected:
            raise ValueError("Approved protocol content changed; do not execute.")
    if (approval["protocol_canonical_lf_sha256"] != APPROVED_PROTOCOL_SHA
            or approval["configuration_canonical_lf_sha256"] != APPROVED_CONFIG_SHA):
        raise ValueError("Approval fingerprints do not match the approved protocol.")
    return yaml.safe_load((root / paths[1][0]).read_text(encoding="utf-8"))


class ReproductionMismatch(RuntimeError):
    def __init__(self, comparisons: list[dict]):
        super().__init__("E001 reproduction gate failed; no protocol changes permitted.")
        self.comparisons = comparisons


def reproduction_gate(actual: dict, reference: dict, model: str) -> list[dict]:
    comparisons = []
    for metric in GATE_METRICS:
        value, target = float(actual[metric]), float(reference[metric])
        delta = value - target
        passed = bool(np.isfinite(value) and np.isfinite(target) and abs(delta) <= 1e-10)
        comparisons.append({"model": model, "metric": metric,
                            "actual": value if np.isfinite(value) else None,
                            "reference": target if np.isfinite(target) else None,
                            "absolute_difference": abs(delta) if np.isfinite(delta) else None,
                            "passed": passed})
    if not all(row["passed"] for row in comparisons):
        raise ReproductionMismatch(comparisons)
    return comparisons


@contextmanager
def monitored_fits(live: LiveStatus, label: str, prior_fits: int):
    """Only wrap timing/progress; original fitter and every argument are unchanged."""
    original = e001.fit_tfidf_lr
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        number = count + 1
        stage = f"{label}: inner fit {number}/9" if number <= 9 else f"{label}: final fit"
        live.update(stage, completed=prior_fits + count)
        result = original(*args, **kwargs)
        count += 1
        live.update(stage, completed=prior_fits + count)
        return result

    e001.fit_tfidf_lr = wrapper
    try:
        yield
    finally:
        e001.fit_tfidf_lr = original


def run_fold(frame, assignments, variant, fold, reference, live, prior_fits):
    role = assignments[f"fold_{fold}"].to_numpy()
    train = frame.iloc[np.flatnonzero(role == "train")]
    calibration = frame.iloc[np.flatnonzero(role == "calibration")]
    indices = np.flatnonzero(role == "evaluation")
    evaluation = frame.iloc[indices]
    label = f"{variant}, fold {fold + 1}/5"
    with monitored_fits(live, label, prior_fits):
        inner_groups = train.QuestionId.astype(str)
        selected = e001.score_params(train, variant, GroupKFold(n_splits=min(3, inner_groups.nunique())),
                                     groups=inner_groups)
        fitted = e001.fit_tfidf_lr(train, variant, {
            **selected["params"], "ngram_range": tuple(selected["params"]["ngram_range"])})
    live.update(f"{label}: original temperature calibration")
    calibration_prob, classes = e001.predict(fitted, calibration, variant)
    temperature, supported_n = e001.temperature_scale(combined_label(calibration).to_numpy(), calibration_prob, classes)
    probabilities, _ = e001.predict(fitted, evaluation, variant)
    probabilities = e001.apply_temperature(probabilities, temperature)
    truth = combined_label(evaluation).to_numpy()
    freq_prob, freq_classes = e001.frequency_probabilities(train, evaluation)
    # Both gates pass before any routing of this fold; ground truth never tunes a score.
    learned = classification_summary(truth, probabilities, classes)
    frequency = classification_summary(truth, freq_prob, freq_classes)
    gates = reproduction_gate(learned, reference["tfidf_logreg"], "tfidf_logreg")
    gates += reproduction_gate(frequency, reference["frequency_baseline"], "frequency_baseline")
    live.update(f"{label}: fixed-budget selection and aggregate scoring", latest_metrics={
        "MAP@3 (all rows)": learned["map_at_3"], "Baseline": frequency["map_at_3"],
        "Delta": learned["map_at_3"] - frequency["map_at_3"]})
    common = dict(y_true=truth, train_labels=combined_label(train).to_numpy(),
                  train_question_ids=train.QuestionId.astype(str).to_numpy(),
                  source_rows=indices, fold=fold, seed=e001.SEED)
    output = {"fold": fold, "n_train": len(train), "n_calibration": len(calibration),
              "n_evaluation": len(evaluation), "selected_hyperparameters": selected,
              "temperature": temperature, "calibration_supported_n": supported_n,
              "reproduction_comparisons": gates,
              "frequency_baseline": evaluate_routing(probabilities=freq_prob, classes=freq_classes,
                                                       rules=("frequency",), **common),
              "tfidf_logreg": evaluate_routing(probabilities=probabilities, classes=classes, **common)}
    # Only aggregate output escapes this scope. No predictions or weights are saved.
    return output


def write_new(path: Path, payload: dict) -> None:
    serialized = json.dumps(payload, indent=2, allow_nan=False) + "\n"
    with path.open("x", encoding="utf-8") as stream:
        stream.write(serialized)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git-revision", required=True)
    parser.add_argument("--image-id", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-f0-9]{40}", args.git_revision):
        raise ValueError("Require exact pre-run Git revision.")
    if not re.fullmatch(r"sha256:[a-f0-9]{64}", args.image_id):
        raise ValueError("Require inspected Docker image identity.")
    root = Path(__file__).resolve().parents[2]
    output_dir = root / "artifacts/e006"
    if any((output_dir / name).exists() for name in ("results.json", "failure.json", "attempt.json")):
        print("E006 attempt already recorded; refusing automatic rerun or overwrite.")
        return 1
    output_dir.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    clock = time.monotonic()
    write_new(output_dir / "attempt.json", {"experiment_id": "E006", "started_utc": started,
                                           "git_revision": args.git_revision, "docker_image_id": args.image_id})
    results = []
    active = {"variant": None, "fold": None}
    try:
        with LiveStatus(output_dir / "live_status.json", total=100) as live:
            live.update("Validating approval, frozen inputs, and E001 reference", completed=0)
            config = approved_config(root)
            preflight = config["preflight"]
            frozen = verify_frozen_inputs(root / "data/raw/train.csv", root / "artifacts/splits",
                expected_data_sha=preflight["training_csv_sha256"],
                expected_manifest_sha=preflight["split_manifest_sha256"],
                expected_assignments_sha=preflight["assignments_sha256"])
            reference_path = root / "artifacts/e001_results.json"
            if file_sha256(reference_path) != preflight["e001_aggregate_reference_sha256"]:
                raise ValueError("E001 reference fingerprint mismatch.")
            reference = json.loads(reference_path.read_text(encoding="utf-8"))
            frame = load_training_data(root / "data/raw/train.csv")
            assignments = pd.read_csv(root / "artifacts/splits/grouped_fold_assignments.csv", keep_default_na=False)
            for variant_index, variant in enumerate(VARIANTS):
                expected = next(item for item in reference["results"]
                                if item["variant"] == variant and item["split"] == "QuestionId-grouped")
                folds = []
                results.append({"variant": variant, "folds": folds})
                for fold in range(5):
                    active = {"variant": variant, "fold": fold}
                    ref_fold = next(item for item in expected["folds"] if item["fold"] == fold)
                    fold_result = run_fold(frame, assignments, variant, fold, ref_fold, live,
                                           prior_fits=(variant_index * 5 + fold) * 10)
                    folds.append(fold_result)
                    print(json.dumps({"experiment_id": "E006", "variant": variant, "fold": fold,
                                      "status": "fold_complete", "reproduction_checks_passed": 6,
                                      "elapsed_seconds": round(time.monotonic() - clock, 1)}), flush=True)
            live.update("All folds complete: validating and serializing aggregate report", completed=100)
            aggregate = aggregate_results(results)
            source_paths = ["src/map_misconceptions/" + name for name in (
                "e001.py", "metrics.py", "metrics_v2.py", "frozen_validation.py", "splits.py",
                "data_contract.py", "e006.py", "selective.py", "selective_report.py", "live_status.py")]
            payload = {"experiment_id": "E006", "status": "COMPLETED",
                "provenance": {"started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(),
                    "wall_seconds": time.monotonic() - clock, "git_revision": args.git_revision,
                    "docker_image_id": args.image_id, "python": sys.version.split()[0],
                    "uid": os.getuid(), "gid": os.getgid(), "logical_cpu_count": os.cpu_count(),
                    "thread_limits": {key: os.environ.get(key) for key in (
                        "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                    "packages": {name: metadata.version(name) for name in (
                        "numpy", "pandas", "scipy", "scikit-learn", "PyYAML")},
                    "seed": e001.SEED, "frozen_inputs": frozen,
                    "protocol_canonical_lf_sha256": APPROVED_PROTOCOL_SHA,
                    "configuration_canonical_lf_sha256": APPROVED_CONFIG_SHA,
                    "source_canonical_lf_sha256": {path: canonical_sha(root / path) for path in source_paths},
                    "reproduction_checks_passed": 60, "model_fitting_calls": 100,
                    "row_level_artifacts_serialized": False}, "results": results, "aggregate": aggregate}
            # Recheck immutable inputs at the end, before declaring this a completed run.
            verify_frozen_inputs(root / "data/raw/train.csv", root / "artifacts/splits",
                expected_data_sha=preflight["training_csv_sha256"],
                expected_manifest_sha=preflight["split_manifest_sha256"],
                expected_assignments_sha=preflight["assignments_sha256"])
            write_new(output_dir / "results.json", payload)
            live.finish("COMPLETED", "Aggregate result written; no row-level outputs")
            print(json.dumps({"experiment_id": "E006", "status": "COMPLETED",
                              "wall_seconds": payload["provenance"]["wall_seconds"]}), flush=True)
        return 0
    except (Exception, KeyboardInterrupt) as exc:
        failure = {"experiment_id": "E006", "status": "FAILED", "started_utc": started,
                   "finished_utc": datetime.now(timezone.utc).isoformat(), "active_fold": active,
                   "failure_type": type(exc).__name__, "partial_results": results,
                   "note": "Not a complete E006 result. Investigate; do not relax protocol or rerun automatically."}
        if isinstance(exc, ReproductionMismatch):
            failure["reproduction_comparisons"] = exc.comparisons
        write_new(output_dir / "failure.json", failure)
        print(json.dumps({"experiment_id": "E006", "status": "FAILED",
                          "failure_type": type(exc).__name__, **active}), flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
