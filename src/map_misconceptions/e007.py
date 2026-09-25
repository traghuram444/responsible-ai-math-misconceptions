"""E007 two-phase execution: freeze ALL development cutoffs before evaluation."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
import os
from pathlib import Path
import re
import time

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold
import yaml

from . import e001
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import canonical_sha, monitored_fits, write_new
from .frozen_validation import verify_frozen_inputs
from .live_status import LiveStatus
from .metrics import map_at_3
from .threshold_transfer import (TARGETS, RULES, calibration_roles, canonical_question,
                                 routing_scores, select_cutoff, evaluate_policy, aggregate)

PROTOCOL_SHA = "699a3e5691a2bf41bd27311e11f94f548aaff5466e497167ed702196ea21676e"
CONFIG_SHA = "815142c1b25fb6edd0859f971bdda3e955f56b91b9998420606146a165b5d630"
VARIANTS = ("explanation_only", "question_plus_explanation")


def approved_config(root):
    approval = yaml.safe_load((root / "experiments/e007_approval.yaml").read_text(encoding="utf-8"))
    if approval["status"] != "approved_locked_for_execution":
        raise ValueError("E007 approval required.")
    for path, key, expected in (("docs/E007_PROTOCOL.md", "protocol_sha256", PROTOCOL_SHA),
                                ("experiments/e007_threshold_transfer.yaml", "configuration_sha256", CONFIG_SHA)):
        if canonical_sha(root / path) != expected or approval[key] != expected:
            raise ValueError("Approved E007 document changed.")
    return yaml.safe_load((root / "experiments/e007_threshold_transfer.yaml").read_text(encoding="utf-8"))


def frozen_check(root, config):
    return verify_frozen_inputs(root / "data/raw/train.csv", root / "artifacts/splits",
        expected_data_sha=config["input_sha256"], expected_manifest_sha=config["manifest_sha256"],
        expected_assignments_sha=config["assignments_sha256"])


def preservation_snapshot(root):
    paths = set()
    for directory in ("docs", "experiments", "results", "artifacts"):
        base = root / directory
        for path in base.rglob("*"):
            relative = path.relative_to(base).as_posix().lower()
            if path.is_file() and re.search(r"(^|/)e00[1-6](?:[_./]|$)", relative):
                paths.add(path)
    for name in ("e001.py", "e006.py", "metrics.py", "metrics_v2.py", "selective.py",
                 "selective_report.py", "frozen_validation.py", "splits.py", "data_contract.py", "live_status.py"):
        paths.add(root / "src/map_misconceptions" / name)
    return {path.relative_to(root).as_posix(): file_sha256(path) for path in sorted(paths)}


def prepare_fold(frame, assignments, variant, fold, live, prior_fits):
    roles = assignments[f"fold_{fold}"].to_numpy()
    train = frame.iloc[np.flatnonzero(roles == "train")]
    calibration = frame.iloc[np.flatnonzero(roles == "calibration")]
    evaluation = frame.iloc[np.flatnonzero(roles == "evaluation")]
    train_q = {canonical_question(q) for q in train.QuestionId}
    cal_q = {canonical_question(q) for q in calibration.QuestionId}
    eval_q = {canonical_question(q) for q in evaluation.QuestionId}
    if (len(train_q), len(cal_q), len(eval_q)) != (9, 3, 3) or train_q & cal_q or train_q & eval_q or cal_q & eval_q:
        raise ValueError("Question role contract violated.")
    temp_q, selection_q = calibration_roles(calibration.QuestionId, fold)
    cq = calibration.QuestionId.map(canonical_question)
    temp = calibration.loc[cq == temp_q]
    selection = calibration.loc[cq.isin(selection_q)]
    role_indices = np.asarray([selection_q.index(canonical_question(q)) for q in selection.QuestionId])
    with monitored_fits(live, f"{variant}, fold {fold + 1}/5", prior_fits):
        groups = train.QuestionId.astype(str)
        selected = e001.score_params(train, variant, GroupKFold(n_splits=3), groups=groups)
        fitted = e001.fit_tfidf_lr(train, variant, {**selected["params"],
                              "ngram_range": tuple(selected["params"]["ngram_range"])})
    live.update(f"{variant}, fold {fold + 1}/5: separate temperature and cutoff fitting")
    temp_prob, classes = e001.predict(fitted, temp, variant)
    temperature, supported_n = e001.temperature_scale(combined_label(temp).to_numpy(), temp_prob, classes)
    if not np.isfinite(temperature) or temperature <= 0:
        raise ValueError("Nonfinite or nonpositive temperature.")
    dev_prob, _ = e001.predict(fitted, selection, variant)
    dev_prob = e001.apply_temperature(dev_prob, temperature)
    eval_prob, _ = e001.predict(fitted, evaluation, variant)
    eval_prob = e001.apply_temperature(eval_prob, temperature)
    freq_dev, freq_classes = e001.frequency_probabilities(train, selection)
    freq_eval, _ = e001.frequency_probabilities(train, evaluation)
    train_labels = combined_label(train).to_numpy()
    dev_truth = combined_label(selection).to_numpy()
    policies = {}
    for rule in RULES:
        p, c = (freq_dev, freq_classes) if rule == "frequency" else (dev_prob, classes)
        score = routing_scores(p, c, train_labels, rule)
        correct = c[np.argmax(p, axis=1)] == dev_truth
        policies[rule] = [select_cutoff(score, correct, role_indices, target) for target in TARGETS]
    role_serial = json.dumps({"fold": fold, "temperature": temp_q, "threshold": selection_q},
                            sort_keys=True, separators=(",", ":"))
    description = {"variant": variant, "fold": fold, "temperature": float(temperature),
                   "temperature_n": len(temp), "temperature_supported_n": supported_n,
                   "temperature_supported_fraction": supported_n / len(temp),
                   "temperature_fallback": supported_n == 0, "role_counts": [9, 1, 2, 3],
                   "derived_role_sha256": hashlib.sha256(role_serial.encode()).hexdigest(),
                   "selected_hyperparameters": selected, "policies": policies}
    # All row-level objects remain memory-only; never included in description.
    memory = dict(truth=combined_label(evaluation).to_numpy(), learned_prob=eval_prob, classes=classes,
                  frequency_prob=freq_eval, frequency_classes=freq_classes, train_labels=train_labels,
                  train_questions=train.QuestionId.to_numpy(), evaluation_questions=evaluation.QuestionId.to_numpy())
    return description, memory


def reproduction_checks(description, memory, reference):
    if description["selected_hyperparameters"]["params"] != reference["selected_hyperparameters"]["params"]:
        raise ValueError("Historical inner-selected hyperparameters differ.")
    checks = []
    for model, p, c in (("tfidf_logreg", memory["learned_prob"], memory["classes"]),
                        ("frequency_baseline", memory["frequency_prob"], memory["frequency_classes"])):
        truth = memory["truth"]
        metrics = {"top1_accuracy": float((c[np.argmax(p, axis=1)] == truth).mean()),
                   "map_at_3": map_at_3(truth, p, c)}
        for metric, actual in metrics.items():
            expected = reference[model][metric]
            difference = abs(actual - expected)
            if not np.isfinite(actual) or difference > 1e-10:
                raise ValueError("E007 historical prediction-rank reproduction failed.")
            checks.append({"model": model, "metric": metric, "actual": actual,
                           "reference": expected, "absolute_difference": difference})
    return checks


def evaluate_fold(description, memory, reference):
    checks = reproduction_checks(description, memory, reference)
    records = []
    for rule in RULES:
        p, c = ((memory["frequency_prob"], memory["frequency_classes"]) if rule == "frequency"
                else (memory["learned_prob"], memory["classes"]))
        score = routing_scores(p, c, memory["train_labels"], rule)
        for policy in (None, *description["policies"][rule]):
            evaluation = evaluate_policy(memory["truth"], p, c, memory["train_labels"],
                memory["train_questions"], memory["evaluation_questions"], score, policy)
            records.append({"variant": description["variant"], "fold": description["fold"], "rule": rule,
                            "target_percent": None if policy is None else policy["target_percent"],
                            "policy": policy, "evaluation": evaluation})
    return checks, records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git-revision", required=True)
    parser.add_argument("--image-id", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-f0-9]{40}", args.git_revision):
        raise ValueError("Exact pre-run revision required.")
    root = Path(__file__).resolve().parents[2]
    config = approved_config(root)
    if args.image_id != config["docker_image_id"] or os.getuid() != 10001 or os.getgid() != 10001:
        raise ValueError("Audited image and non-root identity required.")
    output = root / "artifacts/e007"
    output.mkdir(exist_ok=True)
    if any((output / n).exists() for n in ("attempt.json", "results.json", "failure.json")):
        raise ValueError("E007 attempt already exists; no silent retry.")
    start = datetime.now(timezone.utc).isoformat()
    clock = time.monotonic()
    write_new(output / "attempt.json", {"experiment_id": "E007", "started_utc": start,
                                         "git_revision": args.git_revision})
    try:
        with LiveStatus(output / "live_status.json", experiment_id="E007", total=111) as live:
            live.update("Verifying approved documents and frozen inputs")
            frozen = frozen_check(root, config)
            before = preservation_snapshot(root)
            write_new(output / "preservation.json", before)
            reference_path = root / "artifacts/e001_results.json"
            if file_sha256(reference_path) != config["reference_sha256"]:
                raise ValueError("Historical reference changed.")
            reference = json.loads(reference_path.read_text(encoding="utf-8"))
            frame = load_training_data(root / "data/raw/train.csv")
            assignments = pd.read_csv(root / "artifacts/splits/grouped_fold_assignments.csv", keep_default_na=False)
            prepared = []
            for vi, variant in enumerate(VARIANTS):
                for fold in range(5):
                    prepared.append(prepare_fold(frame, assignments, variant, fold, live, (vi * 5 + fold) * 10))
                    print(json.dumps({"experiment_id": "E007", "phase": "development_frozen",
                                      "variant": variant, "fold": fold}), flush=True)
            # Hard barrier: publish aggregate-only policy choices before reading evaluation correctness.
            policies = [description for description, _ in prepared]
            write_new(output / "frozen_policies.json", {"experiment_id": "E007", "policies": policies})
            policy_sha = file_sha256(output / "frozen_policies.json")
            live.update("All development cutoffs frozen; starting evaluation", completed=100)
            results, checks = [], []
            for index, (description, memory) in enumerate(prepared):
                arm = next(r for r in reference["results"] if r["variant"] == description["variant"]
                           and r["split"] == "QuestionId-grouped")
                ref = next(r for r in arm["folds"] if r["fold"] == description["fold"])
                fold_checks, records = evaluate_fold(description, memory, ref)
                checks.append({"variant": description["variant"], "fold": description["fold"], "checks": fold_checks})
                results.extend(records)
                live.update(f"Evaluation complete: {description['variant']}, fold {description['fold'] + 1}/5",
                            completed=101 + index, latest_metrics={"All-row MAP@3": records[0]["evaluation"]["groups"]["all"]["map_at_3"]})
            live.update("Validating complete aggregate grid and preservation hashes", completed=110)
            summaries = aggregate(results)
            frozen_check(root, config)
            approved_config(root)
            if before != preservation_snapshot(root) or file_sha256(output / "frozen_policies.json") != policy_sha:
                raise ValueError("Preserved history or frozen policies changed.")
            payload = {"experiment_id": "E007", "status": "COMPLETED", "provenance": {
                "started_utc": start, "finished_utc": datetime.now(timezone.utc).isoformat(),
                "wall_seconds": time.monotonic() - clock, "git_revision": args.git_revision,
                "docker_image_id": args.image_id, "uid": os.getuid(), "gid": os.getgid(),
                "seed": 20260831, "protocol_sha256": PROTOCOL_SHA, "configuration_sha256": CONFIG_SHA,
                "frozen_policies_sha256": policy_sha, "preserved_files": len(before),
                "preservation_verified": True, "all_cutoffs_frozen_before_evaluation": True,
                "model_fitting_calls": 100, "reproduction_checks_passed": 40,
                "data_sha256": frozen["data_sha256"], "manifest_sha256": config["manifest_sha256"],
                "assignments_sha256": config["assignments_sha256"],
                "packages": {name: metadata.version(name) for name in ("numpy", "pandas", "scipy", "scikit-learn", "PyYAML")},
                "row_level_artifacts_serialized": False},
                "development": policies, "reproduction": checks, "records": results, "aggregate": summaries}
            from .e007_publication import validate_public_payload
            validate_public_payload(payload)
            write_new(output / "results.json", payload)
            live.update("E007 complete: all aggregate, fold and question results serialized", completed=111)
        print("E007 COMPLETED", flush=True)
        return 0
    except Exception as exc:
        write_new(output / "failure.json", {"experiment_id": "E007", "status": "FAILED",
                                            "exception_type": type(exc).__name__})
        print(f"E007 FAILED ({type(exc).__name__}); no automatic retry.", flush=True)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
