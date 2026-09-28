"""Locked E009 execution: nested reliability learning, freeze, then evaluate."""
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
import yaml

from . import e001, e007, e008
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import canonical_sha, write_new
from .e009_reliability import RULES, VARIANTS, crossfit_training, features, fit_router, text_view, tuned_fit
from .e009_metrics import aggregate, evaluate_fold
from .live_status import LiveStatus
from .threshold_transfer import RULES as OLD_RULES, TARGETS, calibration_roles, canonical_question, routing_scores, select_cutoff

PROTOCOL_SHA = "8dfa8d5036a9cc0ce23153633bbc7a63f6f42b637985f02db36c4901d6e006ef"
CONFIG_SHA = "1988c4e76b32116e4db7b913742ad262629c79443accc38922ca5e48209336e4"


def approved_config(root):
    approval = yaml.safe_load((root / "experiments/e009_approval.yaml").read_text(encoding="utf-8"))
    if approval["status"] != "approved_locked_for_execution":
        raise ValueError("Locked E009 approval required.")
    for path, key, expected in (("docs/E009_PROTOCOL.md", "protocol_sha256", PROTOCOL_SHA),
                                ("experiments/e009_reliability.yaml", "configuration_sha256", CONFIG_SHA)):
        if canonical_sha(root / path) != expected or approval[key] != expected:
            raise ValueError("Approved E009 document changed.")
    return yaml.safe_load((root / "experiments/e009_reliability.yaml").read_text(encoding="utf-8"))


def references(root, config):
    e007.approved_config(root)
    old_config = e008.approved_config(root)
    e008.reference_records(root, old_config)
    if file_sha256(root / "results/E008_aggregates.json") != config["e008_result_sha256"]:
        raise ValueError("E008 reference changed.")
    return json.loads((root / "results/E007_aggregates.json").read_text(encoding="utf-8"))


def preservation_snapshot(root):
    paths = set()
    for directory in ("docs", "experiments", "results", "artifacts"):
        base = root / directory
        for path in base.rglob("*"):
            if path.is_file() and re.search(r"(^|/)e00[1-8](?:[_./]|$)", path.relative_to(base).as_posix().lower()):
                paths.add(path)
    for directory in ("src", "scripts", "tests"):
        paths.update(p for p in (root / directory).rglob("*") if p.suffix in (".py", ".ps1") and "e009" not in p.name)
    return {p.relative_to(root).as_posix(): file_sha256(p) for p in sorted(paths)}


def compare_reference(actual, expected):
    """Exact structures/discrete values; float-only tolerance, no private error echo."""
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(actual) != set(expected):
            raise ValueError("Reference fields differ.")
        for key in expected:
            compare_reference(actual[key], expected[key])
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise ValueError("Reference list differs.")
        for a, e in zip(actual, expected): compare_reference(a, e)
    elif type(expected) is float:
        if type(actual) not in (float, int) or not np.isfinite(actual) or abs(actual - expected) > 1e-10:
            raise ValueError("Reference numeric mismatch.")
    elif type(actual) is not type(expected) or actual != expected:
        raise ValueError("Reference discrete mismatch.")


def prepare_fold(frame, assignments, variant, fold, live, prior_steps, reference):
    roles = assignments[f"fold_{fold}"].to_numpy()
    train = frame.iloc[np.flatnonzero(roles == "train")]
    calibration = frame.iloc[np.flatnonzero(roles == "calibration")]
    eval_positions = np.flatnonzero(roles == "evaluation")
    evaluation = text_view(frame.iloc[eval_positions])
    eval_questions = frame.QuestionId.iloc[eval_positions].to_numpy()
    tq, cq, eq = ({canonical_question(q) for q in qs} for qs in (train.QuestionId, calibration.QuestionId, eval_questions))
    if (len(tq), len(cq), len(eq)) != (9, 3, 3) or tq & cq or tq & eq or cq & eq:
        raise ValueError("Frozen question roles violated.")
    x, correct, crossfit = crossfit_training(train, variant, fold, live, prior_steps)
    live.update(f"{variant}, fold {fold + 1}/5: weighted reliability fit", completed=prior_steps + 30)
    router, router_meta = fit_router(x, correct, train.QuestionId)
    del x, correct
    live.update(f"{variant}, fold {fold + 1}/5: reliability fit complete", completed=prior_steps + 31)
    fitted, selected, final_counts = tuned_fit(train, variant, live,
        f"{variant}, fold {fold + 1}/5, final classifier", prior_steps + 31)
    temp_q, selection_q = calibration_roles(calibration.QuestionId, fold)
    canonical = calibration.QuestionId.map(canonical_question)
    temp, selection = calibration.loc[canonical == temp_q], calibration.loc[canonical.isin(selection_q)]
    dev_roles = np.asarray([selection_q.index(canonical_question(q)) for q in selection.QuestionId])
    temp_prob, classes = e001.predict(fitted, text_view(temp), variant)
    temperature, supported_n = e001.temperature_scale(combined_label(temp).to_numpy(), temp_prob, classes)
    if not np.isfinite(temperature) or temperature <= 0:
        raise ValueError("Invalid temperature.")
    raw_dev, _ = e001.predict(fitted, text_view(selection), variant)
    prob_dev = e001.apply_temperature(raw_dev, temperature)
    freq_dev, freq_classes = e001.frequency_probabilities(train, selection)
    train_labels, dev_truth = combined_label(train).to_numpy(), combined_label(selection).to_numpy()
    original_policies = {}
    for rule in OLD_RULES:
        p, c = (freq_dev, freq_classes) if rule == "frequency" else (prob_dev, classes)
        score = routing_scores(p, c, train_labels, rule)
        original_policies[rule] = [select_cutoff(score, c[p.argmax(axis=1)] == dev_truth, dev_roles, target) for target in TARGETS]
    serial = json.dumps({"fold": fold, "temperature": temp_q, "threshold": selection_q}, sort_keys=True, separators=(",", ":"))
    old_description = {"variant": variant, "fold": fold, "temperature": float(temperature),
        "temperature_n": len(temp), "temperature_supported_n": supported_n, "temperature_supported_fraction": supported_n / len(temp),
        "temperature_fallback": supported_n == 0, "role_counts": [9, 1, 2, 3],
        "derived_role_sha256": hashlib.sha256(serial.encode()).hexdigest(), "selected_hyperparameters": selected, "policies": original_policies}
    gate = e008.reproduction_gate(old_description, reference)
    live.update(f"{variant}, fold {fold + 1}/5: label-blind similarity and routing scores")
    dev_x = features(fitted, train, selection, variant, raw_dev, classes)
    learned_score = router.score(dev_x)
    dev_correct = classes[prob_dev.argmax(axis=1)] == dev_truth
    policies = dict(original_policies)
    for rule, scores in (("learned_reliability", learned_score), ("raw_confidence", raw_dev.max(axis=1))):
        policies[rule] = [select_cutoff(scores, dev_correct, dev_roles, target) for target in TARGETS]
    # Only text enters predictions/features; evaluation correctness is read in phase B.
    raw_eval, _ = e001.predict(fitted, evaluation, variant)
    prob_eval = e001.apply_temperature(raw_eval, temperature)
    freq_eval, _ = e001.frequency_probabilities(train, evaluation)
    eval_x = features(fitted, train, evaluation, variant, raw_eval, classes)
    scores = {"learned_reliability": router.score(eval_x), "raw_confidence": raw_eval.max(axis=1)}
    for rule in OLD_RULES:
        p, c = (freq_eval, freq_classes) if rule == "frequency" else (prob_eval, classes)
        scores[rule] = routing_scores(p, c, train_labels, rule)
    description = {"variant": variant, "fold": fold, "reference_development": old_description,
                   "crossfit": crossfit, "router": router_meta, "final_classifier_fits": final_counts, "policies": policies}
    memory = {"learned_prob": prob_eval, "classes": classes, "frequency_prob": freq_eval,
              "frequency_classes": freq_classes, "train_labels": train_labels, "train_questions": train.QuestionId.to_numpy(),
              "evaluation_questions": eval_questions, "evaluation_positions": eval_positions, "scores": scores}
    return description, memory, gate


def evaluation_gate(records, reference):
    count = 0
    lookup = {(r["variant"], r["fold"], r["rule"], r["target_percent"]): r for r in reference}
    for row in records:
        if row["rule"] in OLD_RULES:
            stripped = {k: v for k, v in row.items() if k != "reliability"}
            compare_reference(stripped, lookup[row["variant"], row["fold"], row["rule"], row["target_percent"]])
            count += 1
    if count != 12:
        raise ValueError("Incomplete E007 evaluation reproduction.")
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git-revision", required=True)
    parser.add_argument("--image-id", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    config, historical = approved_config(root), e007.approved_config(root)
    if (not re.fullmatch(r"[a-f0-9]{40}", args.git_revision) or args.image_id != config["docker_image_id"]
            or os.getuid() != 10001 or os.getgid() != 10001):
        raise ValueError("Audited revision/image/non-root identity required.")
    output = root / "artifacts/e009"
    output.mkdir(exist_ok=True)
    if any((output / n).exists() for n in ("attempt.json", "results.json", "failure.json")):
        raise ValueError("Existing E009 attempt; no silent retry.")
    started, clock = datetime.now(timezone.utc).isoformat(), time.monotonic()
    write_new(output / "attempt.json", {"experiment_id": "E009", "git_revision": args.git_revision, "started_utc": started})
    try:
        with LiveStatus(output / "live_status.json", experiment_id="E009", total=431) as live:
            live.update("Verifying locked approvals, inputs and history")
            frozen = e007.frozen_check(root, historical)
            ref, before = references(root, config), preservation_snapshot(root)
            write_new(output / "preservation.json", before)
            frame = load_training_data(root / "data/raw/train.csv")
            assignments = pd.read_csv(root / "artifacts/splits/grouped_fold_assignments.csv", keep_default_na=False)
            prepared, dev_checks = [], []
            for vi, variant in enumerate(VARIANTS):
                for fold in range(5):
                    index = vi * 5 + fold
                    old = next(d for d in ref["development"] if d["variant"] == variant and d["fold"] == fold)
                    description, memory, gate = prepare_fold(frame, assignments, variant, fold, live, index * 42, old)
                    prepared.append((description, memory))
                    dev_checks.append(gate)
                    live.update(f"Development complete: {variant}, fold {fold + 1}/5", completed=(index + 1) * 42,
                                latest_metrics={"Prepared fold-arms": index + 1, "Reproduced policies": 9 * (index + 1)})
                    print(json.dumps({"experiment_id": "E009", "phase": "development_prepared", "variant": variant, "fold": fold}), flush=True)
            development = [d for d, _ in prepared]
            write_new(output / "frozen_policies.json", {"experiment_id": "E009", "development": development})
            policy_sha = file_sha256(output / "frozen_policies.json")
            live.update("ALL policies frozen: evaluation correctness now permitted", completed=420)
            records, ranking, eval_checks = [], [], []
            for index, (description, memory) in enumerate(prepared):
                truth = combined_label(frame.iloc[memory["evaluation_positions"]]).to_numpy()
                rows, rank = evaluate_fold(description, memory, truth)
                matched = evaluation_gate(rows, ref["records"])
                eval_checks.append({"variant": description["variant"], "fold": description["fold"], "matched_records": matched})
                records.extend(rows)
                ranking.extend(rank)
                live.update(f"Evaluation verified: {description['variant']}, fold {description['fold'] + 1}/5", completed=421 + index,
                            latest_metrics={"Verified evaluation fold-arms": index + 1, "Reproduced evaluation records": 12 * (index + 1)})
            summaries = aggregate(records, ranking)
            e007.frozen_check(root, e007.approved_config(root))
            references(root, approved_config(root))
            if before != preservation_snapshot(root) or policy_sha != file_sha256(output / "frozen_policies.json"):
                raise ValueError("Frozen policies or preserved history changed.")
            counts = [b["fits"] for d in development for b in d["crossfit"]["blocks"]] + [d["final_classifier_fits"] for d in development]
            total_counts = {key: sum(c[key] for c in counts) for key in counts[0]}
            if total_counts["attempted"] != 400:
                raise ValueError("Unexpected execution fitting count.")
            payload = {"experiment_id": "E009", "status": "COMPLETED", "provenance": {
                "started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(), "wall_seconds": time.monotonic() - clock,
                "git_revision": args.git_revision, "docker_image_id": args.image_id, "uid": os.getuid(), "gid": os.getgid(),
                "seed": 20260831, "protocol_sha256": PROTOCOL_SHA, "configuration_sha256": CONFIG_SHA,
                "frozen_policies_sha256": policy_sha, "e007_result_sha256": file_sha256(root / "results/E007_aggregates.json"),
                "e008_result_sha256": config["e008_result_sha256"], "preserved_files": len(before), "preservation_verified": True,
                "all_cutoffs_frozen_before_evaluation": True, "classifier_fits": total_counts,
                "router_fitting_calls": sum(d["router"]["fitting_calls"] for d in development),
                "router_fallbacks": sum(d["router"]["status"] != "FITTED" for d in development),
                "development_policies_reproduced": 90, "evaluation_records_reproduced": 120,
                "data_sha256": frozen["data_sha256"], "manifest_sha256": historical["manifest_sha256"], "assignments_sha256": historical["assignments_sha256"],
                "packages": {name: metadata.version(name) for name in ("numpy", "pandas", "scipy", "scikit-learn", "PyYAML")},
                "row_level_artifacts_serialized": False}, "development": development,
                "reproduction": {"development": dev_checks, "evaluation": eval_checks},
                "records": records, "ranking": ranking, "aggregate": summaries}
            from .e009_publication import validate_public_payload
            validate_public_payload(payload)
            write_new(output / "results.json", payload)
            live.update("E009 complete: all aggregate/fold/question results serialized", completed=431)
        print("E009 COMPLETED", flush=True)
        return 0
    except Exception as exc:
        write_new(output / "failure.json", {"experiment_id": "E009", "status": "FAILED", "exception_type": type(exc).__name__})
        print(f"E009 FAILED ({type(exc).__name__}); no automatic retry.", flush=True)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
