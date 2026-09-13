"""Publish a completed E006 through a strict aggregate-only allowlist.

The source artifact is treated as untrusted. No metadata dictionary or arbitrary
string is copied wholesale. This script neither executes E006 nor loads MAP data.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from numbers import Real
from pathlib import Path
import re
import sys


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from map_misconceptions.selective_report import (  # noqa: E402
    BUDGETS, FOLDS, GROUPS, NUMERIC_METRICS, ROUTES, VARIANTS,
    aggregate_results, render_results_report,
)


SOURCE_PATHS = tuple("src/map_misconceptions/" + name for name in (
    "e001.py", "metrics.py", "metrics_v2.py", "frozen_validation.py", "splits.py",
    "data_contract.py", "e006.py", "selective.py", "selective_report.py", "live_status.py",
))
PACKAGES = ("numpy", "pandas", "scipy", "scikit-learn", "PyYAML")
THREAD_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")
GATE_MODELS = ("tfidf_logreg", "frequency_baseline")
GATE_METRICS = ("map_at_3", "top1_accuracy", "ece_10_equal_width")
REASON_RULES = (("retained_n", 200, "retained_n_below_200"),
                ("correct_n", 20, "correct_n_below_20"),
                ("incorrect_n", 20, "incorrect_n_below_20"))
FROZEN_NOTE = "Assignment hash is a current snapshot, not proof of historical file identity."
OUTPUTS = ("results/E006_aggregates.json", "docs/E006_RESULTS.md")


def _object(value, name):
    if not isinstance(value, dict):
        raise ValueError(f"Expected object: {name}")
    return value


def _number(value, name, *, nullable=False, minimum=None, maximum=None):
    if value is None and nullable:
        return None
    if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value):
        raise ValueError(f"Expected finite number: {name}")
    if minimum is not None and value < minimum or maximum is not None and value > maximum:
        raise ValueError(f"Number outside allowed range: {name}")
    return value


def _integer(value, name, *, minimum=0):
    value = _number(value, name, minimum=minimum)
    if not isinstance(value, int):
        raise ValueError(f"Expected integer: {name}")
    return value


def _hash(value, name, length=64):
    if not isinstance(value, str) or re.fullmatch(f"[a-f0-9]{{{length}}}", value) is None:
        raise ValueError(f"Invalid fingerprint: {name}")
    return value


def _version(value, name):
    if not isinstance(value, str) or re.fullmatch(r"\d{1,4}(?:\.\d{1,4}){1,3}(?:(?:a|b|rc|\.post|\.dev)\d{1,4})?", value) is None:
        raise ValueError(f"Invalid numeric version: {name}")
    return value


def _utc(value, name):
    if not isinstance(value, str) or re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|\+00:00)", value) is None:
        raise ValueError(f"Invalid UTC timestamp: {name}")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise ValueError(f"Invalid UTC timestamp: {name}") from None
    if parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise ValueError(f"Non-UTC timestamp: {name}")
    return value


def _true(value, name):
    if value is not True:
        raise ValueError(f"Completion evidence must be true: {name}")
    return True


def _indexed(items, key, expected, name):
    if not isinstance(items, list):
        raise ValueError(f"Expected registered list: {name}")
    indexed = {}
    for item in items:
        item = _object(item, name)
        value = item.get(key)
        if isinstance(value, bool) or value not in expected or value in indexed:
            raise ValueError(f"Unknown/duplicate registered value: {name}")
        indexed[value] = item
    if set(indexed) != set(expected):
        raise ValueError(f"Incomplete registered values: {name}")
    return indexed


def _provenance(source):
    source = _object(source, "provenance")
    result = {
        key: _utc(source.get(key), key) for key in ("started_utc", "finished_utc")
    }
    if datetime.fromisoformat(result["finished_utc"].replace("Z", "+00:00")) < datetime.fromisoformat(result["started_utc"].replace("Z", "+00:00")):
        raise ValueError("Completion precedes experiment start")
    result["wall_seconds"] = _number(source.get("wall_seconds"), "wall_seconds", minimum=0)
    result["git_revision"] = _hash(source.get("git_revision"), "git_revision", length=40)
    image = source.get("docker_image_id")
    if not isinstance(image, str) or not image.startswith("sha256:"):
        raise ValueError("Invalid Docker image fingerprint")
    result["docker_image_id"] = "sha256:" + _hash(image[7:], "docker_image_id")
    result["python"] = _version(source.get("python"), "python")
    for key in ("uid", "gid", "logical_cpu_count"):
        result[key] = _integer(source.get(key), key, minimum=1)
    limits = _object(source.get("thread_limits"), "thread_limits")
    if any(limits.get(key) != "1" for key in THREAD_KEYS):
        raise ValueError("Expected the registered one-thread environment")
    result["thread_limits"] = {key: "1" for key in THREAD_KEYS}
    packages = _object(source.get("packages"), "packages")
    result["packages"] = {name: _version(packages.get(name), name) for name in PACKAGES}
    if source.get("seed") != 20260831:
        raise ValueError("Unexpected experiment seed")
    result["seed"] = 20260831
    frozen = _object(source.get("frozen_inputs"), "frozen_inputs")
    result["frozen_inputs"] = {
        key: _hash(frozen.get(key), key) for key in (
            "data_sha256", "manifest_sha256", "assignment_sha256_observed_2026_09_13",
        )
    }
    for key in ("rows", "questions"):
        result["frozen_inputs"][key] = _integer(frozen.get(key), key, minimum=1)
    for key in ("ordered_rows_and_targets_match", "roles_question_disjoint", "each_row_evaluated_once", "deterministic_split_reconstruction_matches"):
        result["frozen_inputs"][key] = _true(frozen.get(key), key)
    # Explanatory prose is a source-code literal, never copied from the artifact.
    result["frozen_inputs"]["note"] = FROZEN_NOTE
    for key in ("protocol_canonical_lf_sha256", "configuration_canonical_lf_sha256"):
        result[key] = _hash(source.get(key), key)
    hashes = _object(source.get("source_canonical_lf_sha256"), "source_canonical_lf_sha256")
    result["source_canonical_lf_sha256"] = {path: _hash(hashes.get(path), "source hash") for path in SOURCE_PATHS}
    for key, expected in (("reproduction_checks_passed", 60), ("model_fitting_calls", 100)):
        if _integer(source.get(key), key) != expected:
            raise ValueError("Incomplete registered execution evidence")
        result[key] = expected
    if source.get("row_level_artifacts_serialized") is not False:
        raise ValueError("Row-level serialization must be explicitly false")
    result["row_level_artifacts_serialized"] = False
    return result


def _metric_group(source):
    source = _object(source, "metric group")
    if any(metric not in source for metric in NUMERIC_METRICS):
        raise ValueError("Missing registered numerical metric")
    group = {
        metric: _number(source.get(metric), metric, nullable=True)
        for metric in NUMERIC_METRICS
    }
    if not isinstance(source.get("calibration_eligible"), bool):
        raise ValueError("Missing boolean calibration eligibility")
    group["calibration_eligible"] = source["calibration_eligible"]
    reasons = []
    for metric, threshold, reason in REASON_RULES:
        if _integer(group[metric], metric) < threshold:
            reasons.append(reason)
    expected_reason = ";".join(reasons) if reasons else None
    if source.get("calibration_ineligible_reason") != expected_reason:
        raise ValueError("Calibration reason is not the registered count-derived literal")
    group["calibration_ineligible_reason"] = expected_reason
    return group


def _model(source, model):
    source = _object(source, "model")
    rules = tuple(rule for candidate, rule in ROUTES if candidate == model)
    routing = _indexed(source.get("routing"), "rule", rules, "rules")
    result = {"confidence_auroc": _number(source.get("confidence_auroc"), "confidence_auroc", nullable=True, minimum=0, maximum=1), "routing": []}
    for rule in rules:
        budgets = _indexed(routing[rule].get("budgets"), "review_fraction", BUDGETS, "budgets")
        result["routing"].append({"rule": rule, "budgets": []})
        for budget in BUDGETS:
            groups = _object(budgets[budget].get("groups"), "strata")
            if any(group not in groups for group in GROUPS):
                raise ValueError("Missing registered stratum")
            result["routing"][-1]["budgets"].append({
                "review_fraction": budget,
                "groups": {group: _metric_group(groups[group]) for group in GROUPS},
            })
    return result


def _fold(source, fold, total_rows):
    result = {"fold": fold}
    for key in ("n_train", "n_calibration", "n_evaluation"):
        result[key] = _integer(source.get(key), key, minimum=1)
    if sum(result[key] for key in ("n_train", "n_calibration", "n_evaluation")) != total_rows:
        raise ValueError("Fold roles do not partition the registered row count")
    result["calibration_supported_n"] = _integer(source.get("calibration_supported_n"), "calibration_supported_n")
    if result["calibration_supported_n"] > result["n_calibration"]:
        raise ValueError("Supported calibration count exceeds calibration count")
    result["temperature"] = _number(source.get("temperature"), "temperature", minimum=0)
    if result["temperature"] == 0:
        raise ValueError("Temperature must be positive")
    selection = _object(source.get("selected_hyperparameters"), "selected_hyperparameters")
    params = _object(selection.get("params"), "selected params")
    c = _number(params.get("C"), "C")
    minimum = _integer(params.get("min_df"), "min_df", minimum=1)
    ngram = params.get("ngram_range")
    if not isinstance(ngram, list) or len(ngram) != 2 or any(not isinstance(v, int) or isinstance(v, bool) for v in ngram):
        raise ValueError("Invalid registered ngram range")
    if (c, minimum, tuple(ngram)) not in ((0.5, 2, (1, 1)), (1.0, 2, (1, 2)), (2.0, 5, (1, 2))):
        raise ValueError("Hyperparameters outside the frozen E001 grid")
    result["selected_hyperparameters"] = {"params": {"C": c, "min_df": minimum, "ngram_range": ngram.copy()},
        "inner_mean_map_at_3": _number(selection.get("inner_mean_map_at_3"), "inner_mean_map_at_3", minimum=0, maximum=1)}
    for model in GATE_MODELS:
        result[model] = _model(source.get(model), model)
        base = result[model]["routing"][0]["budgets"][0]["groups"]["all"]
        if base["original_n"] != result["n_evaluation"] or base["retained_n"] != result["n_evaluation"]:
            raise ValueError("Zero-review size differs from fold evaluation size")
    comparisons = source.get("reproduction_comparisons")
    if not isinstance(comparisons, list) or len(comparisons) != 6:
        raise ValueError("Exactly six reproduction comparisons are required per fold")
    indexed = {}
    for comparison in comparisons:
        comparison = _object(comparison, "reproduction comparison")
        model, metric = comparison.get("model"), comparison.get("metric")
        if model not in GATE_MODELS or metric not in GATE_METRICS or (model, metric) in indexed:
            raise ValueError("Unregistered or duplicate reproduction comparison")
        actual = _number(comparison.get("actual"), "actual", minimum=0, maximum=1)
        reference = _number(comparison.get("reference"), "reference", minimum=0, maximum=1)
        difference = _number(comparison.get("absolute_difference"), "absolute_difference", minimum=0, maximum=1e-10)
        if abs(actual - reference) > 1e-10 or not math.isclose(difference, abs(actual - reference), rel_tol=0, abs_tol=1e-16):
            raise ValueError("Reproduction comparison does not satisfy locked tolerance")
        _true(comparison.get("passed"), "reproduction comparison passed")
        base_actual = result[model]["routing"][0]["budgets"][0]["groups"]["all"][metric]
        if base_actual is None or not math.isclose(actual, base_actual, rel_tol=0, abs_tol=1e-12):
            raise ValueError("Reproduction comparison differs from zero-review result")
        indexed[(model, metric)] = {"model": model, "metric": metric, "actual": actual,
            "reference": reference, "absolute_difference": difference, "passed": True}
    result["reproduction_comparisons"] = [indexed[(model, metric)] for model in GATE_MODELS for metric in GATE_METRICS]
    return result


def sanitize_payload(payload: dict, source_artifact_sha256: str) -> dict:
    """Return only known aggregate fields, rejecting unsafe known-field values."""
    payload = _object(payload, "artifact")
    if payload.get("experiment_id") != "E006" or payload.get("status") != "COMPLETED":
        raise ValueError("Only a completed E006 may be published")
    provenance = _provenance(payload.get("provenance"))
    variants = _indexed(payload.get("results"), "variant", VARIANTS, "variants")
    results = []
    for variant in VARIANTS:
        folds = _indexed(variants[variant].get("folds"), "fold", FOLDS, "folds")
        results.append({"variant": variant, "folds": [
            _fold(folds[fold], fold, provenance["frozen_inputs"]["rows"]) for fold in FOLDS
        ]})
    return {
        "experiment_id": "E006", "status": "COMPLETED",
        "source_artifact_sha256": _hash(source_artifact_sha256, "source_artifact_sha256"),
        "provenance": provenance, "results": results,
        "aggregate": aggregate_results(results),
    }


def _no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key in source artifact")
        result[key] = value
    return result


def _reject_constant(_value):
    raise ValueError("Nonfinite JSON constant in source artifact")


def _project_path(root, relative):
    path = root / relative
    if not path.resolve().is_relative_to(root):
        raise ValueError("Artifact path escapes project root")
    return path


def publish(root: Path = PROJECT, *, check: bool = False) -> dict:
    """Validate and write only new (or already byte-identical) public artifacts."""
    root = Path(root).resolve()
    source = _project_path(root, "artifacts/e006/results.json")
    raw = source.read_bytes()
    payload = json.loads(raw, object_pairs_hook=_no_duplicate_keys, parse_constant=_reject_constant)
    sanitized = sanitize_payload(payload, hashlib.sha256(raw).hexdigest())
    contents = (
        (json.dumps(sanitized, indent=2, ensure_ascii=True, allow_nan=False) + "\n").encode("utf-8"),
        render_results_report(sanitized).encode("utf-8"),
    )
    destinations = [_project_path(root, name) for name in OUTPUTS]
    # Preflight both destinations before any creation, so a conflicting existing
    # report cannot leave behind a newly created JSON file (or vice versa).
    for destination, content in zip(destinations, contents, strict=True):
        if destination.exists() and destination.read_bytes() != content:
            raise FileExistsError("Refusing to overwrite a different published E006 artifact")
    if not check:
        for destination, content in zip(destinations, contents, strict=True):
            if not destination.exists():
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("xb") as stream:
                    stream.write(content)
    return {
        "experiment_id": "E006", "status": "CHECKED" if check else "PUBLISHED",
        "source_artifact_sha256": sanitized["source_artifact_sha256"],
        "outputs": {relative: hashlib.sha256(content).hexdigest() for relative, content in zip(OUTPUTS, contents, strict=True)},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate/render in memory only; do not write")
    args = parser.parse_args()
    try:
        summary = publish(check=args.check)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        # Do not echo exception values: an untrusted artifact may contain data.
        print(json.dumps({"experiment_id": "E006", "status": "PUBLICATION_BLOCKED", "error_type": type(exc).__name__}))
        return 1
    print(json.dumps(summary, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
