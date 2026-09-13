"""Runner safety checks using only invented data and the approved public files."""

from copy import deepcopy
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from map_misconceptions import e001, e006
from map_misconceptions.splits import build_grouped_folds


class RecordingLive:
    def __init__(self):
        self.updates = []

    def update(self, stage, **kwargs):
        self.updates.append((stage, kwargs))


def approved_files(tmp_path):
    root = Path(__file__).resolve().parents[1]
    for relative in (
        "docs/E006_REVIEW_ADDENDUM.md",
        "experiments/e006_review_addendum.yaml",
        "experiments/e006_approval.yaml",
    ):
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text((root / relative).read_text(encoding="utf-8"), encoding="utf-8")
    return tmp_path


def test_approved_config_requires_the_exact_locked_protocol_and_configuration(tmp_path):
    root = approved_files(tmp_path)
    config = e006.approved_config(root)
    assert config["experiment_id"] == "E006"
    assert config["framework"]["seed"] == e001.SEED
    assert config["routing"]["review_fractions"] == [0, 0.1, 0.2, 0.3, 0.4, 0.5]
    assert config["preflight"]["reproduction_gate"]["absolute_tolerance"] == 1e-10
    assert config["preflight"]["reproduction_gate"]["relative_tolerance"] == 0
    assert e006.canonical_sha(root / "docs/E006_REVIEW_ADDENDUM.md") == e006.APPROVED_PROTOCOL_SHA
    assert e006.canonical_sha(root / "experiments/e006_review_addendum.yaml") == e006.APPROVED_CONFIG_SHA


@pytest.mark.parametrize("relative", ["docs/E006_REVIEW_ADDENDUM.md", "experiments/e006_review_addendum.yaml"])
def test_protocol_or_configuration_content_change_blocks_execution(tmp_path, relative):
    root = approved_files(tmp_path)
    target = root / relative
    target.write_text(target.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Approved protocol content changed"):
        e006.approved_config(root)


def test_canonical_fingerprint_accepts_only_the_documented_newline_normalization(tmp_path):
    root = approved_files(tmp_path)
    protocol = root / "docs/E006_REVIEW_ADDENDUM.md"
    text = protocol.read_text(encoding="utf-8")
    protocol.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))
    assert e006.approved_config(root)["experiment_id"] == "E006"
    protocol.write_bytes((text + " ").encode("utf-8"))
    with pytest.raises(ValueError):
        e006.approved_config(root)


@pytest.mark.parametrize("field,value", [
    ("status", "proposed_for_user_review"),
    ("protocol_canonical_lf_sha256", "0" * 64),
    ("configuration_canonical_lf_sha256", "0" * 64),
])
def test_missing_approval_or_mismatched_approval_fingerprint_blocks_execution(tmp_path, field, value):
    root = approved_files(tmp_path)
    path = root / "experiments/e006_approval.yaml"
    approval = yaml.safe_load(path.read_text(encoding="utf-8"))
    approval[field] = value
    path.write_text(yaml.safe_dump(approval), encoding="utf-8")
    with pytest.raises(ValueError):
        e006.approved_config(root)


def test_reproduction_gate_has_absolute_only_inclusive_one_e_minus_ten_tolerance():
    reference = {metric: 0.0 for metric in e006.GATE_METRICS}
    actual = {metric: 1e-10 for metric in e006.GATE_METRICS}
    passed = e006.reproduction_gate(actual, reference, "tfidf_logreg")
    assert len(passed) == 3 and all(item["passed"] for item in passed)
    assert all(item["absolute_difference"] == 1e-10 for item in passed)
    actual["map_at_3"] = 1.01e-10
    with pytest.raises(e006.ReproductionMismatch) as captured:
        e006.reproduction_gate(actual, reference, "tfidf_logreg")
    assert not captured.value.comparisons[0]["passed"]
    # This difference would pass numpy's default relative tolerance but must fail here.
    reference = {metric: 0.8 for metric in e006.GATE_METRICS}
    actual = {metric: 0.8 + 1e-8 for metric in e006.GATE_METRICS}
    with pytest.raises(e006.ReproductionMismatch):
        e006.reproduction_gate(actual, reference, "frequency_baseline")


@pytest.mark.parametrize("invalid", [float("nan"), float("inf"), float("-inf")])
@pytest.mark.parametrize("side", ["actual", "reference"])
def test_reproduction_gate_rejects_nonfinite_metrics_and_failure_is_json_safe(invalid, side):
    actual = {metric: 0.5 for metric in e006.GATE_METRICS}
    reference = dict(actual)
    (actual if side == "actual" else reference)["ece_10_equal_width"] = invalid
    with pytest.raises(e006.ReproductionMismatch) as captured:
        e006.reproduction_gate(actual, reference, "tfidf_logreg")
    assert not captured.value.comparisons[-1]["passed"]
    # Required so the runner can write failure.json using allow_nan=False.
    json.dumps(captured.value.comparisons, allow_nan=False)


def test_monitored_fits_preserves_identity_arguments_return_values_and_restores(monkeypatch):
    calls = []
    returned = object()

    def original(*args, **kwargs):
        calls.append((args, kwargs))
        return returned

    monkeypatch.setattr(e001, "fit_tfidf_lr", original)
    train, params = object(), {"C": 0.5}
    live = RecordingLive()
    with e006.monitored_fits(live, "synthetic fold", 30):
        assert e001.fit_tfidf_lr is not original
        assert e001.fit_tfidf_lr(train, "explanation_only", params=params) is returned
        assert e001.fit_tfidf_lr(train, "question_plus_explanation", params=params) is returned
    assert e001.fit_tfidf_lr is original
    assert calls[0][0][0] is train and calls[0][1]["params"] is params
    assert calls[1][0][0] is train and calls[1][1]["params"] is params
    assert [item[1]["completed"] for item in live.updates] == [30, 31, 31, 32]


def test_monitored_fits_restores_after_fitting_exception_without_swallowing_it(monkeypatch):
    def broken(*args, **kwargs):
        raise ValueError("synthetic fitting error")

    monkeypatch.setattr(e001, "fit_tfidf_lr", broken)
    live = RecordingLive()
    with pytest.raises(ValueError, match="synthetic fitting error"):
        with e006.monitored_fits(live, "synthetic fold", 10):
            e001.fit_tfidf_lr(object(), "explanation_only", {})
    assert e001.fit_tfidf_lr is broken
    # A failed fitting call must not be displayed as completed work.
    assert [item[1]["completed"] for item in live.updates] == [10]


def synthetic_frame():
    rows = []
    for question in range(15):
        for response in range(8):
            misconception = "synthetic_addition" if response % 2 else "synthetic_subtraction"
            word = "addition" if response % 2 else "subtraction"
            if response >= 6:
                word = "shared"
            rows.append({
                "QuestionId": question,
                "QuestionText": f"SYNTHETIC_QUESTION_TEXT_ONLY compute integer question {question}",
                "MC_Answer": "A",
                "StudentExplanation": f"SYNTHETIC_STUDENT_TEXT_ONLY used {word} integer calculation",
                "Category": "False_Misconception",
                "Misconception": misconception,
            })
    return pd.DataFrame(rows)


def every_key(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from every_key(item)
    elif isinstance(value, list):
        for item in value:
            yield from every_key(item)


@pytest.mark.parametrize("variant", e006.VARIANTS)
def test_run_fold_reproduces_exact_e001_functions_then_returns_only_aggregates(monkeypatch, variant):
    # Tiny CPU-only synthetic reconstruction, using the same reduced grid for the
    # reference and runner. Production GRID, source files and MAP data are untouched.
    monkeypatch.setattr(e001, "GRID", ({"ngram_range": (1, 1), "min_df": 2, "C": 0.5},))
    frame = synthetic_frame()
    assignments = build_grouped_folds(frame, n_splits=5, seed=e001.SEED)
    reference = e001.run_grouped(frame, assignments[["fold_0"]], variant)["folds"][0]
    original_fitter = e001.fit_tfidf_lr
    original_gate = e006.reproduction_gate
    original_routing = e006.evaluate_routing
    event_order = []

    def gate(actual, expected, model):
        event_order.append(f"gate:{model}")
        return original_gate(actual, expected, model)

    def routing(**kwargs):
        assert event_order[:2] == ["gate:tfidf_logreg", "gate:frequency_baseline"]
        event_order.append("routing")
        return original_routing(**kwargs)

    monkeypatch.setattr(e006, "reproduction_gate", gate)
    monkeypatch.setattr(e006, "evaluate_routing", routing)
    result = e006.run_fold(frame, assignments, variant, 0, reference, RecordingLive(), prior_fits=0)
    assert e001.fit_tfidf_lr is original_fitter
    assert event_order == ["gate:tfidf_logreg", "gate:frequency_baseline", "routing", "routing"]
    assert result["selected_hyperparameters"] == reference["selected_hyperparameters"]
    assert result["temperature"] == reference["temperature"]
    assert result["calibration_supported_n"] == reference["calibration_supported_n"]
    assert len(result["reproduction_comparisons"]) == 6
    assert all(item["passed"] and item["absolute_difference"] == 0 for item in result["reproduction_comparisons"])
    assert result["n_train"] + result["n_calibration"] + result["n_evaluation"] == len(frame)
    forbidden = {
        "QuestionId", "QuestionText", "StudentExplanation", "source_row", "source_rows", "row_id",
        "y_true", "classes", "probabilities", "predictions", "rankings", "weights",
    }
    assert not forbidden.intersection(every_key(result))
    serialized = json.dumps(result, allow_nan=False)
    assert "SYNTHETIC_QUESTION_TEXT_ONLY" not in serialized
    assert "SYNTHETIC_STUDENT_TEXT_ONLY" not in serialized
    # In particular, a frequency mismatch must also stop all routing; the learned
    # gate alone is not enough to produce or report selective results.
    incorrect_reference = deepcopy(reference)
    incorrect_reference["frequency_baseline"]["map_at_3"] += 0.01
    event_order.clear()
    with pytest.raises(e006.ReproductionMismatch):
        e006.run_fold(frame, assignments, variant, 0, incorrect_reference, RecordingLive(), prior_fits=0)
    assert event_order == ["gate:tfidf_logreg", "gate:frequency_baseline"]
    assert e001.fit_tfidf_lr is original_fitter
