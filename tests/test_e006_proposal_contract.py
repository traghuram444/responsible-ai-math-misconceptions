"""Validate the unapproved E006 proposal without loading data or fitting models."""

from __future__ import annotations

import ast
from pathlib import Path
import re

import pytest
import yaml


PROJECT = Path(__file__).resolve().parents[1]


def read_yaml(relative_path: str) -> dict:
    document = yaml.safe_load((PROJECT / relative_path).read_text(encoding="utf-8"))
    assert isinstance(document, dict)
    return document


@pytest.fixture(scope="module")
def original() -> dict:
    return read_yaml("experiments/e006_selective_prediction.yaml")


@pytest.fixture(scope="module")
def proposal() -> dict:
    return read_yaml("experiments/e006_review_addendum.yaml")


def test_both_documents_are_proposals_and_preserve_experiment_history(original, proposal):
    assert original["experiment_id"] == proposal["experiment_id"] == "E006"
    assert original["status"] == "proposed_awaiting_review"
    assert proposal["status"] == "proposed_for_user_review_not_approved_not_run"
    assert proposal["supersedes_original_files"] is False
    assert proposal["preserve_experiments"] == ["E001", "E002", "E003", "E004", "E005"]
    assert proposal["protocol"] == "docs/E006_REVIEW_ADDENDUM.md"
    # Documentation is intentionally excluded from the legacy Docker image.
    document_path = PROJECT / proposal["protocol"]
    if document_path.exists():
        document = document_path.read_text(encoding="utf-8")
        assert "proposed for user review; not approved and not run" in document.lower()


def test_frozen_framework_and_original_six_budgets_are_retained(original, proposal):
    framework = proposal["framework"]
    assert framework["reference"] == "E001"
    assert framework["seed"] == 20260831
    assert framework["fold_ids"] == [0, 1, 2, 3, 4]
    assert framework["variants"] == ["explanation_only", "question_plus_explanation"]
    assert framework["models"] == ["tfidf_logreg", "frequency_baseline"]
    assert framework["inputs_target_inner_tuning_temperature_calibration"] == "unchanged"
    assert framework["random_reference_rerun"] is False
    assert proposal["routing"]["review_fractions"] == original["review_budgets"] == [
        0.0, 0.1, 0.2, 0.3, 0.4, 0.5,
    ]
    assert proposal["routing"]["curves"] == "six_registered_points_only_coverage_50_to_100_percent"
    # Parse the inherited seed without importing or executing the experiment module.
    source = ast.parse((PROJECT / "src/map_misconceptions/e001.py").read_text(encoding="utf-8"))
    seeds = [
        ast.literal_eval(statement.value)
        for statement in source.body
        if isinstance(statement, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "SEED" for target in statement.targets)
    ]
    assert seeds == [framework["seed"]]


def test_support_is_training_only_and_strata_follow_global_selection(original, proposal):
    strata = proposal["support_strata"]
    assert original["support_reporting"] == ["unsupported", "rare", "frequent", "well_supported"]
    assert strata["unsupported"] == "exact_label_count_equals_0"
    assert strata["rare"] == "exact_label_count_1_to_19"
    assert strata["frequent"] == "exact_label_count_at_least_20"
    assert strata["well_supported"] == "exact_label_count_at_least_20_and_at_least_2_training_QuestionIds"
    assert strata["definition_role"] == "train_only"
    assert strata["well_supported_nested_in_frequent"] is True
    assert strata["selection"] == "intersect_strata_after_global_fold_retention"
    routing = proposal["routing"]
    assert routing["support_counts_role"] == "train_only"
    assert routing["true_labels_or_true_support_used"] is False
    assert routing["retained_count"] == "ceil_n_times_one_minus_review_fraction"
    assert routing["ties"]["applies_to"] == "all_rules"
    assert routing["ties"]["serialization"] == "fold={fold};source_row={source_row};seed={seed}"
    assert routing["ties"]["trailing_newline"] is False


def test_benefit_requires_both_conditions_and_calibration_is_descriptive(proposal):
    criterion = proposal["benefit_criterion"]
    assert criterion["review_fraction"] == 0.5
    assert criterion["required_all"] == [
        "mean_risk_reduction_vs_own_zero_review_at_least_0.05",
        "mean_retained_risk_strictly_lower_than_frequency_at_equal_budget",
    ]
    assert criterion["failure"] == "either_required_condition_not_met"
    assert criterion["scope"] == "each_learned_input_arm_and_routing_rule_independently"
    assert criterion["winner_selection"] == "prohibited"
    assert criterion["deployment_readiness_claim"] == "prohibited"
    calibration = proposal["metrics"]["calibration"]
    assert calibration["binary_calibration_gate"] == "none_descriptive_only_requires_review"
    assert (calibration["minimum_n"], calibration["minimum_correct"], calibration["minimum_incorrect"]) == (200, 20, 20)
    assert calibration["ece_bins"] == 10


def test_corrected_brier_is_separate_and_legacy_field_remains(proposal):
    calibration = proposal["metrics"]["calibration"]
    assert calibration["fields"] == [
        "ece_10_equal_width", "legacy_multiclass_brier", "union_label_brier",
    ]
    assert calibration["corrected_brier_function"] == "metrics_v2.union_label_brier_score"
    assert calibration["original_metric_implementation"] == "preserved_unchanged"
    assert calibration["primary_brier_comparison"] == "union_label_brier"
    assert calibration["corrected_brier_formula"] == "legacy_multiclass_brier_plus_unsupported_fraction_of_scored_cases"
    source = ast.parse((PROJECT / "src/map_misconceptions/metrics_v2.py").read_text(encoding="utf-8"))
    assert any(
        isinstance(statement, ast.FunctionDef) and statement.name == "union_label_brier_score"
        for statement in source.body
    )


def test_reproduction_preflight_cannot_silently_relax_protocol(proposal):
    preflight = proposal["preflight"]
    for name in (
        "training_csv_sha256", "split_manifest_sha256", "assignments_sha256",
        "e001_aggregate_reference_sha256",
    ):
        assert re.fullmatch(r"[0-9a-f]{64}", preflight[name])
    gate = preflight["reproduction_gate"]
    assert gate["metrics"] == ["map_at_3", "top1_accuracy", "ece_10_equal_width"]
    assert gate["absolute_tolerance"] == 1e-10
    assert gate["relative_tolerance"] == 0.0
    assert gate["mismatch_action"] == "stop_and_report_do_not_adjust_protocol_or_history"
    assert proposal["framework"]["reconstruct_probabilities"] == "in_memory_only"
    assert proposal["publication"]["never_serialize"] == [
        "student_text", "row_identifiers", "row_probabilities", "row_predictions", "rankings", "model_caches",
    ]


def test_project_startup_does_not_automatically_launch_e006():
    if not (PROJECT / "compose.yaml").exists() or not (PROJECT / "Dockerfile").exists():
        pytest.skip("Repository-only startup audit: run with the full project mounted read-only.")
    compose = read_yaml("compose.yaml")
    for service in compose.get("services", {}).values():
        for key in ("command", "entrypoint", "post_start"):
            assert "e006" not in str(service.get(key, "")).lower()
    dockerfile = (PROJECT / "Dockerfile").read_text(encoding="utf-8")
    startup = [line for line in dockerfile.splitlines() if re.match(r"^\s*(CMD|ENTRYPOINT)\b", line)]
    assert startup
    assert all("e006" not in line.lower() for line in startup)
    workflows = PROJECT / ".github/workflows"
    for path in sorted({*workflows.glob("*.yml"), *workflows.glob("*.yaml")}):
        workflow = yaml.safe_load(path.read_text(encoding="utf-8"))
        for job in workflow.get("jobs", {}).values():
            for step in job.get("steps", []):
                assert not re.search(r"\brun_e006[^\s]*\.py\b", str(step.get("run", "")), flags=re.I)
