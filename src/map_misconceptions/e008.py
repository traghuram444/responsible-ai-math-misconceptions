"""Locked E008: development-only reconstruction and feasibility decomposition."""
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

from . import e001, e007
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import canonical_sha, monitored_fits, write_new
from .feasibility_diagnostics import VARIANTS, aggregate, diagnose_rule, oracle_bound
from .live_status import LiveStatus
from .threshold_transfer import RULES, TARGETS, calibration_roles, canonical_question, routing_scores, select_cutoff

PROTOCOL_SHA = "2e3eb90239d0d9cba1e324208329f0d50455cf2dc2959a0accef29a435b14b6b"
CONFIG_SHA = "b0e0b7a43324eaf62db968e8c4533ed30a91dff31e0e516afcb9d4b1cf9c5375"


def approved_config(root):
    approval = yaml.safe_load((root / "experiments/e008_approval.yaml").read_text(encoding="utf-8"))
    if approval["status"] != "approved_locked_for_execution":
        raise ValueError("E008 approval required.")
    for path, key, expected in (("docs/E008_PROTOCOL.md", "protocol_sha256", PROTOCOL_SHA),
                                ("experiments/e008_feasibility.yaml", "configuration_sha256", CONFIG_SHA)):
        if canonical_sha(root / path) != expected or approval[key] != expected:
            raise ValueError("Approved E008 document changed.")
    return yaml.safe_load((root / "experiments/e008_feasibility.yaml").read_text(encoding="utf-8"))


def preservation_snapshot(root):
    paths = set()
    for directory in ("docs", "experiments", "results", "artifacts"):
        base = root / directory
        for path in base.rglob("*"):
            if path.is_file() and re.search(r"(^|/)e00[1-7](?:[_./]|$)", path.relative_to(base).as_posix().lower()):
                paths.add(path)
    for directory in ("src", "scripts", "tests"):
        for path in (root / directory).rglob("*"):
            if (path.suffix in (".py", ".ps1") and "e008" not in path.name
                    and "feasibility_diagnostics" not in path.name):
                paths.add(path)
    return {path.relative_to(root).as_posix(): file_sha256(path) for path in sorted(paths)}


def reference_records(root, config):
    paths = (("results/E007_aggregates.json", "e007_result_sha256"),
             ("artifacts/e007/frozen_policies.json", "e007_frozen_policies_sha256"))
    for path, key in paths:
        if file_sha256(root / path) != config[key]:
            raise ValueError("E007 reference fingerprint changed.")
    public = json.loads((root / paths[0][0]).read_text(encoding="utf-8"))["development"]
    frozen = json.loads((root / paths[1][0]).read_text(encoding="utf-8"))["policies"]
    if public != frozen or len(public) != 10:
        raise ValueError("E007 development references disagree.")
    return {(r["variant"], r["fold"]): r for r in public}


def prepare_development(frame, assignments, variant, fold, live, prior_steps):
    """Only training and calibration frames are materialized; never evaluation rows."""
    roles = assignments[f"fold_{fold}"].to_numpy()
    train = frame.iloc[np.flatnonzero(roles == "train")]
    calibration = frame.iloc[np.flatnonzero(roles == "calibration")]
    train_q = {canonical_question(q) for q in train.QuestionId}
    cal_q = {canonical_question(q) for q in calibration.QuestionId}
    if (len(train_q), len(cal_q)) != (9, 3) or train_q & cal_q:
        raise ValueError("Development question role contract violated.")
    temp_q, selection_q = calibration_roles(calibration.QuestionId, fold)
    cq = calibration.QuestionId.map(canonical_question)
    temp = calibration.loc[cq == temp_q]
    selection = calibration.loc[cq.isin(selection_q)]
    role_indices = np.asarray([selection_q.index(canonical_question(q)) for q in selection.QuestionId])
    with monitored_fits(live, f"{variant}, fold {fold + 1}/5", prior_steps):
        selected = e001.score_params(train, variant, GroupKFold(n_splits=3), groups=train.QuestionId.astype(str))
        fitted = e001.fit_tfidf_lr(train, variant, {**selected["params"], "ngram_range": tuple(selected["params"]["ngram_range"])})
    live.update(f"{variant}, fold {fold + 1}/5: development reconstruction gate")
    temp_prob, classes = e001.predict(fitted, temp, variant)
    temperature, supported_n = e001.temperature_scale(combined_label(temp).to_numpy(), temp_prob, classes)
    if not np.isfinite(temperature) or temperature <= 0:
        raise ValueError("Invalid reconstructed temperature.")
    dev_prob, _ = e001.predict(fitted, selection, variant)
    dev_prob = e001.apply_temperature(dev_prob, temperature)
    freq_prob, freq_classes = e001.frequency_probabilities(train, selection)
    train_labels, truth = combined_label(train).to_numpy(), combined_label(selection).to_numpy()
    policies, memory = {}, {}
    for rule in RULES:
        p, c = (freq_prob, freq_classes) if rule == "frequency" else (dev_prob, classes)
        score = routing_scores(p, c, train_labels, rule)
        correct = c[np.argmax(p, axis=1)] == truth
        policies[rule] = [select_cutoff(score, correct, role_indices, target) for target in TARGETS]
        memory[rule] = (score, correct, role_indices)
    serial = json.dumps({"fold": fold, "temperature": temp_q, "threshold": selection_q}, sort_keys=True, separators=(",", ":"))
    description = {"variant": variant, "fold": fold, "temperature": float(temperature),
                   "temperature_n": len(temp), "temperature_supported_n": supported_n,
                   "temperature_supported_fraction": supported_n / len(temp), "temperature_fallback": supported_n == 0,
                   "role_counts": [9, 1, 2, 3], "derived_role_sha256": hashlib.sha256(serial.encode()).hexdigest(),
                   "selected_hyperparameters": selected, "policies": policies}
    return description, memory


def reproduction_gate(actual, expected):
    differences = {}
    for key in ("temperature", "inner_mean_map_at_3"):
        left = actual[key] if key == "temperature" else actual["selected_hyperparameters"][key]
        right = expected[key] if key == "temperature" else expected["selected_hyperparameters"][key]
        delta = abs(left - right)
        if not np.isfinite(delta) or delta > 1e-10:
            raise ValueError("E007 development numeric reproduction mismatch.")
        differences[key + "_absolute_difference"] = delta
    for key in actual:
        if key in ("temperature", "selected_hyperparameters"):
            continue
        if actual[key] != expected[key]:
            raise ValueError("E007 development exact reproduction mismatch.")
    if actual["selected_hyperparameters"]["params"] != expected["selected_hyperparameters"]["params"]:
        raise ValueError("E007 selected hyperparameters differ.")
    return {"variant": actual["variant"], "fold": actual["fold"], **differences,
            "exact_fields_match": True, "policy_records_matched": 9}


def analyze_development(description, memory):
    variant, fold = description["variant"], description["fold"]
    records, oracles = [], {}
    for rule in RULES:
        scores, correct, roles = memory[rule]
        model = "frequency_baseline" if rule == "frequency" else "tfidf_logreg"
        bounds = [oracle_bound(int((roles == q).sum()), int(correct[roles == q].sum()),
                               variant=variant, fold=fold, model=model, role_index=q) for q in (0, 1)]
        for bound in bounds:
            if bound["oracle_id"] in oracles and oracles[bound["oracle_id"]] != bound:
                raise ValueError("Routing rules changed fixed predictions.")
            oracles[bound["oracle_id"]] = bound
        diagnosed = diagnose_rule(scores, correct, roles, bounds, variant=variant, fold=fold, rule=rule)
        for record, policy in zip(diagnosed, description["policies"][rule]):
            if (record["candidate_count"] != policy["candidate_count"]
                    or record["shared_feasible_count"] != policy["admissible_candidate_count"]):
                raise ValueError("Diagnostic grid differs from reproduced E007 grid.")
        records.extend(diagnosed)
    return records, list(oracles.values())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git-revision", required=True)
    parser.add_argument("--image-id", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    config, historical_config = approved_config(root), e007.approved_config(root)
    if (not re.fullmatch(r"[a-f0-9]{40}", args.git_revision) or args.image_id != config["docker_image_id"]
            or os.getuid() != 10001 or os.getgid() != 10001):
        raise ValueError("Audited revision/image/non-root identity required.")
    output = root / "artifacts/e008"
    output.mkdir(exist_ok=True)
    if any((output / name).exists() for name in ("attempt.json", "results.json", "failure.json")):
        raise ValueError("Existing E008 attempt; no silent retry.")
    start, clock = datetime.now(timezone.utc).isoformat(), time.monotonic()
    write_new(output / "attempt.json", {"experiment_id": "E008", "started_utc": start, "git_revision": args.git_revision})
    try:
        with LiveStatus(output / "live_status.json", experiment_id="E008", total=111) as live:
            live.update("Verifying approved documents, history and frozen inputs")
            frozen = e007.frozen_check(root, historical_config)
            references, before = reference_records(root, config), preservation_snapshot(root)
            write_new(output / "preservation.json", before)
            frame = load_training_data(root / "data/raw/train.csv")
            assignments = pd.read_csv(root / "artifacts/splits/grouped_fold_assignments.csv", keep_default_na=False)
            development, checks, records, oracles = [], [], [], {}
            for vi, variant in enumerate(VARIANTS):
                for fold in range(5):
                    index = vi * 5 + fold
                    description, memory = prepare_development(frame, assignments, variant, fold, live, index * 11)
                    checks.append(reproduction_gate(description, references[(variant, fold)]))
                    development.append(description)
                    rows, bounds = analyze_development(description, memory)
                    records.extend(rows)
                    for bound in bounds:
                        if bound["oracle_id"] in oracles and oracles[bound["oracle_id"]] != bound:
                            raise ValueError("Duplicated frequency oracle differs.")
                        oracles[bound["oracle_id"]] = bound
                    del memory
                    live.update(f"Development diagnostics verified: {variant}, fold {fold + 1}/5", completed=(index + 1) * 11,
                                latest_metrics={"Verified fold-arms": index + 1, "Reproduced policies": 9 * (index + 1)})
                    print(json.dumps({"experiment_id": "E008", "phase": "development_verified", "variant": variant, "fold": fold}), flush=True)
            live.update("Validating complete diagnostic grid and preserved history", completed=110)
            bounds = list(oracles.values())
            summaries = aggregate(records, bounds)
            e007.frozen_check(root, e007.approved_config(root))
            reference_records(root, approved_config(root))
            if before != preservation_snapshot(root):
                raise ValueError("Preserved history changed.")
            payload = {"experiment_id": "E008", "status": "COMPLETED", "provenance": {
                "started_utc": start, "finished_utc": datetime.now(timezone.utc).isoformat(), "wall_seconds": time.monotonic() - clock,
                "git_revision": args.git_revision, "docker_image_id": args.image_id, "uid": os.getuid(), "gid": os.getgid(),
                "seed": 20260831, "protocol_sha256": PROTOCOL_SHA, "configuration_sha256": CONFIG_SHA,
                "e007_result_sha256": config["e007_result_sha256"], "e007_frozen_policies_sha256": config["e007_frozen_policies_sha256"],
                "preserved_files": len(before), "preservation_verified": True, "model_fitting_calls": 100,
                "outer_evaluation_prediction_calls": 0, "reproduced_policy_records": 90,
                "data_sha256": frozen["data_sha256"], "manifest_sha256": historical_config["manifest_sha256"],
                "assignments_sha256": historical_config["assignments_sha256"],
                "packages": {name: metadata.version(name) for name in ("numpy", "pandas", "scipy", "scikit-learn", "PyYAML")},
                "row_level_artifacts_serialized": False}, "development": development, "reproduction": checks,
                "oracles": bounds, "records": records, "aggregate": summaries}
            from .e008_publication import validate_public_payload
            validate_public_payload(payload)
            write_new(output / "results.json", payload)
            live.update("E008 complete: aggregate, fold and development-question diagnostics serialized", completed=111)
        print("E008 COMPLETED", flush=True)
        return 0
    except Exception as exc:
        write_new(output / "failure.json", {"experiment_id": "E008", "status": "FAILED", "exception_type": type(exc).__name__})
        print(f"E008 FAILED ({type(exc).__name__}); no automatic retry.", flush=True)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
