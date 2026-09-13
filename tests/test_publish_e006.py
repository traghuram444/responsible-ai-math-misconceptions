"""Synthetic-only publication allowlist and immutable-output tests."""

from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


publisher = load_module("e006_publisher", ROOT / "scripts/publish_e006_results.py")
synthetic = load_module("e006_synthetic_fixture", ROOT / "tests/test_selective_report.py")


def fixture_payload():
    results = synthetic.synthetic_results()
    for arm in results:
        for fold in arm["folds"]:
            fold.update({
                "n_train": 1000, "n_calibration": 1000, "n_evaluation": 1000,
                "temperature": 1.2, "calibration_supported_n": 900,
                "selected_hyperparameters": {"params": {"C": 0.5, "min_df": 2, "ngram_range": [1, 1]}, "inner_mean_map_at_3": 0.5},
                "reproduction_comparisons": [],
            })
            for model in publisher.GATE_MODELS:
                for route in fold[model]["routing"]:
                    for budget in route["budgets"]:
                        for group in budget["groups"].values():
                            reasons = [reason for metric, threshold, reason in publisher.REASON_RULES if group[metric] < threshold]
                            group["calibration_ineligible_reason"] = ";".join(reasons) if reasons else None
                base = fold[model]["routing"][0]["budgets"][0]["groups"]["all"]
                fold["reproduction_comparisons"].extend({
                    "model": model, "metric": metric, "actual": base[metric], "reference": base[metric],
                    "absolute_difference": 0.0, "passed": True,
                } for metric in publisher.GATE_METRICS)
    return {
        "experiment_id": "E006", "status": "COMPLETED", "results": results,
        "aggregate": {"unsafe_stale_text": "SHOULD_NOT_COPY"},
        "provenance": {
            "started_utc": "2026-09-13T20:00:00+00:00", "finished_utc": "2026-09-13T20:10:00.123456+00:00",
            "wall_seconds": 600.0, "git_revision": "a" * 40, "docker_image_id": "sha256:" + "b" * 64,
            "python": "3.11.11", "uid": 10001, "gid": 10001, "logical_cpu_count": 8,
            "thread_limits": {key: "1" for key in publisher.THREAD_KEYS},
            "packages": {name: "1.2.3" for name in publisher.PACKAGES}, "seed": 20260831,
            "frozen_inputs": {
                "data_sha256": "c" * 64, "manifest_sha256": "d" * 64,
                "assignment_sha256_observed_2026_09_13": "e" * 64,
                "rows": 3000, "questions": 15,
                "ordered_rows_and_targets_match": True, "roles_question_disjoint": True,
                "each_row_evaluated_once": True, "deterministic_split_reconstruction_matches": True,
                "note": publisher.FROZEN_NOTE,
            },
            "protocol_canonical_lf_sha256": "f" * 64,
            "configuration_canonical_lf_sha256": "0" * 64,
            "source_canonical_lf_sha256": {path: "1" * 64 for path in publisher.SOURCE_PATHS},
            "reproduction_checks_passed": 60, "model_fitting_calls": 100,
            "row_level_artifacts_serialized": False,
        },
    }


def write_fixture(root, payload=None):
    source = root / "artifacts/e006/results.json"
    source.parent.mkdir(parents=True)
    source.write_text(json.dumps(payload or fixture_payload(), allow_nan=False), encoding="utf-8")
    return source


def test_sanitization_preserves_complete_values_and_recomputes_aggregate():
    payload = fixture_payload()
    original = deepcopy(payload)
    cleaned = publisher.sanitize_payload(payload, "2" * 64)
    assert cleaned["results"] == payload["results"]
    assert len(cleaned["aggregate"]["variants"]) == 2
    assert cleaned["source_artifact_sha256"] == "2" * 64
    assert "unsafe_stale_text" not in cleaned["aggregate"]
    assert payload == original


def test_unknown_text_is_dropped_at_every_level_and_never_rendered():
    payload = fixture_payload()
    marker = "PRIVATE_STUDENT_TEXT_DO_NOT_COPY"
    payload["student_response"] = marker
    payload["provenance"]["local_path"] = marker
    payload["provenance"]["thread_limits"]["PRIVATE_TOKEN"] = marker
    payload["provenance"]["packages"][marker] = marker
    payload["provenance"]["source_canonical_lf_sha256"][marker] = marker
    payload["provenance"]["frozen_inputs"]["note"] = marker
    payload["results"][0]["question_text"] = marker
    fold = payload["results"][0]["folds"][0]
    fold["predictions"] = [marker]
    fold["selected_hyperparameters"]["raw_text"] = marker
    fold["selected_hyperparameters"]["params"]["student_text"] = marker
    fold["reproduction_comparisons"][0]["student_text"] = marker
    fold["tfidf_logreg"]["probabilities"] = [marker]
    fold["tfidf_logreg"]["routing"][0]["ranking"] = [marker]
    budget = fold["tfidf_logreg"]["routing"][0]["budgets"][0]
    budget["raw_text"] = marker
    budget["groups"][marker] = {"text": marker}
    budget["groups"]["all"]["response"] = marker
    cleaned = publisher.sanitize_payload(payload, "2" * 64)
    assert marker not in json.dumps(cleaned)
    assert marker not in publisher.render_results_report(cleaned)


@pytest.mark.parametrize("field,value", [
    ("git_revision", "PRIVATE_TEXT"), ("docker_image_id", "sha256:PRIVATE_TEXT"),
    ("python", "3.11.11/private/path"), ("started_utc", "2026-09-13 PRIVATE_TEXT"),
    ("finished_utc", "2026-13-99T00:00:00Z"), ("wall_seconds", float("nan")),
    ("uid", 0), ("reproduction_checks_passed", 59), ("row_level_artifacts_serialized", True),
])
def test_unsafe_known_provenance_fields_are_rejected(field, value):
    payload = fixture_payload()
    payload["provenance"][field] = value
    with pytest.raises(ValueError):
        publisher.sanitize_payload(payload, "2" * 64)


def test_unknown_calibration_reason_and_failed_reproduction_are_rejected():
    payload = fixture_payload()
    group = payload["results"][0]["folds"][0]["tfidf_logreg"]["routing"][0]["budgets"][0]["groups"]["rare"]
    group["calibration_ineligible_reason"] = "PRIVATE_TEXT"
    with pytest.raises(ValueError, match="registered count-derived"):
        publisher.sanitize_payload(payload, "2" * 64)
    payload = fixture_payload()
    payload["results"][0]["folds"][0]["reproduction_comparisons"][0]["passed"] = False
    with pytest.raises(ValueError, match="Completion evidence"):
        publisher.sanitize_payload(payload, "2" * 64)


def test_hyperparameters_outside_grid_and_nonfinite_metrics_are_rejected():
    payload = fixture_payload()
    payload["results"][0]["folds"][0]["selected_hyperparameters"]["params"]["C"] = 3.0
    with pytest.raises(ValueError, match="frozen E001 grid"):
        publisher.sanitize_payload(payload, "2" * 64)
    payload = fixture_payload()
    payload["results"][0]["folds"][0]["frequency_baseline"]["routing"][0]["budgets"][0]["groups"]["all"]["map_at_3"] = float("inf")
    with pytest.raises(ValueError, match="finite number"):
        publisher.sanitize_payload(payload, "2" * 64)


def test_check_mode_creates_nothing_and_publish_is_idempotent(tmp_path):
    source = write_fixture(tmp_path)
    original = source.read_bytes()
    summary = publisher.publish(tmp_path, check=True)
    assert summary["status"] == "CHECKED"
    assert not (tmp_path / "results").exists()
    assert not (tmp_path / "docs").exists()
    summary = publisher.publish(tmp_path)
    assert summary["status"] == "PUBLISHED"
    assert source.read_bytes() == original
    assert summary["source_artifact_sha256"] == hashlib.sha256(original).hexdigest()
    first_bytes = [(tmp_path / name).read_bytes() for name in publisher.OUTPUTS]
    publisher.publish(tmp_path)
    publisher.publish(tmp_path, check=True)
    assert [(tmp_path / name).read_bytes() for name in publisher.OUTPUTS] == first_bytes


def test_conflicting_existing_file_blocks_both_outputs_before_writes(tmp_path):
    write_fixture(tmp_path)
    report = tmp_path / publisher.OUTPUTS[1]
    report.parent.mkdir(parents=True)
    report.write_bytes(b"existing report must survive")
    with pytest.raises(FileExistsError, match="Refusing to overwrite"):
        publisher.publish(tmp_path)
    assert not (tmp_path / publisher.OUTPUTS[0]).exists()
    assert report.read_bytes() == b"existing report must survive"


@pytest.mark.parametrize("status", ["FAILED", "RUNNING", "PARTIAL"])
def test_incomplete_run_cannot_be_published(tmp_path, status):
    payload = fixture_payload()
    payload["status"] = status
    write_fixture(tmp_path, payload)
    with pytest.raises(ValueError, match="completed E006"):
        publisher.publish(tmp_path)
    assert not (tmp_path / "results").exists()


def test_duplicate_json_keys_and_nonfinite_constants_are_rejected(tmp_path):
    source = tmp_path / "artifacts/e006/results.json"
    source.parent.mkdir(parents=True)
    source.write_text('{"status":"COMPLETED","status":"FAILED"}', encoding="utf-8")
    with pytest.raises(ValueError, match="Duplicate JSON key"):
        publisher.publish(tmp_path)
    source.write_text('{"unknown":NaN}', encoding="utf-8")
    with pytest.raises(ValueError, match="Nonfinite JSON"):
        publisher.publish(tmp_path)
