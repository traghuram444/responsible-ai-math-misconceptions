"""E007 checks use invented data only; no MAP fitting before approval lock."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from map_misconceptions import e001, e007
from map_misconceptions.threshold_transfer import (
    TARGETS, RULES, aggregate, apply_cutoff, calibration_roles, canonical_question,
    evaluate_policy, mean_sd, routing_scores, select_cutoff,
)
from map_misconceptions.e007_publication import validate_public_payload, report


@pytest.mark.parametrize("value,expected", [("0012", 12), (12.0, 12), ("12.000", 12), (0, 0)])
def test_canonical_ids(value, expected):
    assert canonical_question(value) == expected


@pytest.mark.parametrize("value", [True, -1, "2.2", "nan", "Infinity", "word"])
def test_bad_ids(value):
    with pytest.raises(ValueError): canonical_question(value)


def test_exact_role_hash_and_order_independence():
    qs = [11, 12, 13]
    expected = sorted(qs, key=lambda q: (hashlib.sha256(f"E007|fold=2|QuestionId={q}|seed=20260831".encode()).hexdigest(), q))
    assert calibration_roles(qs * 10, 2) == (expected[0], tuple(expected[1:]))
    assert calibration_roles(qs[::-1], 2) == calibration_roles(qs, 2)
    with pytest.raises(ValueError): calibration_roles([1, 2], 2)


def brute(scores, correct, groups, target):
    candidates = sorted(set([0.0, *scores.tolist()]))
    admitted = []
    for threshold in candidates:
        mask = scores >= threshold
        valid = True
        for g in (0, 1):
            qmask = groups == g
            n = int((mask & qmask).sum())
            errors = int((mask & qmask & ~correct).sum())
            if n < 100 or n * 10 < int(qmask.sum()) or errors * 100 > target * n:
                valid = False
        if valid: admitted.append((int(mask.sum()), threshold))
    if not admitted: return None, 0
    return sorted(admitted, key=lambda x: (-x[0], x[1]))[0][1], len(admitted)


@pytest.mark.parametrize("seed", range(8))
@pytest.mark.parametrize("target", TARGETS)
def test_vectorized_selection_matches_independent_exhaustive_search(seed, target):
    rng = np.random.default_rng(seed)
    groups = np.repeat([0, 1], 550)
    scores = np.round(rng.uniform(0, 1, len(groups)), 2)
    # Deliberately nonmonotone correctness with mixed easy/hard score regions.
    correct = rng.uniform(size=len(groups)) < np.where((scores > .3) & (scores < .8), .97, .55)
    expected, count = brute(scores, correct, groups, target)
    policy = select_cutoff(scores, correct, groups, target)
    assert policy["threshold"] == expected
    assert policy["admissible_candidate_count"] == count


@pytest.mark.parametrize("target", TARGETS)
def test_rational_boundary_and_frequency_ties(target):
    groups = np.repeat([0, 1], 100)
    correct = np.tile(np.arange(100) >= target, 2)
    policy = select_cutoff(np.full(200, .75), correct, groups, target)
    assert policy["threshold"] == 0.0  # maximal count tie -> lowest threshold
    assert apply_cutoff([.1, .75, 1], policy).all()
    correct[99] = False
    rejected = select_cutoff(np.full(200, .75), correct, groups, target)
    assert rejected["threshold"] is None
    assert not apply_cutoff([.75, 1], rejected).any()


def test_count_and_coverage_floors_are_per_question():
    groups = np.repeat([0, 1], [99, 1000])
    assert select_cutoff(np.ones(1099), np.ones(1099, bool), groups, 20)["threshold"] is None
    groups = np.repeat([0, 1], 2000)
    score = np.tile(np.r_[np.full(100, .9), np.full(1900, .1)], 2)
    correct = score == .9
    assert select_cutoff(score, correct, groups, 20)["threshold"] is None


def test_nonmonotonic_risk_search_does_not_stop_at_bad_prefix():
    groups = np.repeat([0, 1], 300)
    scores = np.tile(np.r_[np.full(100, .9), np.full(100, .7), np.full(100, .2)], 2)
    correct = np.tile(np.r_[np.zeros(30, bool), np.ones(170, bool), np.zeros(100, bool)], 2)
    policy = select_cutoff(scores, correct, groups, 20)
    assert policy["threshold"] == .7
    assert [q["retained_n"] for q in policy["development"]] == [200, 200]


def test_cutoff_is_independent_of_evaluation_batch_labels_and_order():
    policy = {"status": "SELECTED", "threshold": .6}
    assert apply_cutoff([.6], policy)[0]
    assert apply_cutoff([.99, .6, .05], policy)[1]
    assert apply_cutoff([.05, .6, .99], policy)[1]
    assert not apply_cutoff([.59999], policy)[0]
    # Interface accepts no evaluation labels or batch quantile.
    with pytest.raises(TypeError): apply_cutoff([.6], policy, y_true=["private"])


def test_support_score_uses_predicted_label_not_true_support():
    p = np.array([[.8, .2], [.1, .9]])
    classes = np.array(["A", "B"])
    train = ["A"] * 100 + ["B"] * 10
    np.testing.assert_allclose(routing_scores(p, classes, train, "support_aware"),
                               [.8, .9 * np.log1p(10) / np.log1p(100)])
    with pytest.raises(ValueError): routing_scores(p, classes, train, "frequency")


def evaluation_inputs():
    return dict(truth=np.tile(np.array(["A"] * 160 + ["B"] * 20 + ["U"] * 20), 3),
                probabilities=np.tile([.8, .2], (600, 1)), classes=np.array(["A", "B"]),
                train_labels=np.array(["A", "B"] * 200), train_questions=np.tile([1, 1, 2, 2], 100),
                evaluation_questions=np.repeat([0, 1, 2], 200), score=np.full(600, .8))


def test_empty_policy_null_risk_and_unsupported_inclusion():
    inputs = evaluation_inputs()
    policy = select_cutoff(np.full(400, .8), np.zeros(400, bool), np.repeat([0, 1], 200), 20)
    result = evaluate_policy(**inputs, policy=policy)
    assert result["groups"]["all"]["risk"] is None
    assert result["groups"]["all"]["coverage"] == 0
    result = evaluate_policy(**inputs, policy=None)
    g = result["groups"]["unsupported"]
    assert g["original_n"] == 60 and g["incorrect_n"] == 60
    assert g["risk"] == 1 and g["brier"] is None
    all_g = result["groups"]["all"]
    assert all_g["risk"] == .2
    # A loss .08; B loss 1.28; unsupported loss 1.68.
    assert all_g["brier"] == pytest.approx(.8 * .08 + .1 * 1.28 + .1 * 1.68)


def test_mean_sd_keeps_empty_denominators():
    assert mean_sd([None] * 5) == {"mean": None, "sd": None, "defined_folds": 0}
    assert mean_sd([0, None])["defined_folds"] == 1
    assert mean_sd([0, None])["sd"] is None
    assert mean_sd([1, 3])["sd"] == pytest.approx(np.sqrt(2))


def synthetic_payload():
    records, development, reproduction = [], [], []
    for variant in e007.VARIANTS:
        for fold in range(5):
            inputs = evaluation_inputs()
            inputs["evaluation_questions"] += fold * 3
            policies = {rule: [select_cutoff(np.full(400, .8), np.tile(np.arange(200) >= 20, 2),
                                            np.repeat([0, 1], 200), target) for target in TARGETS] for rule in RULES}
            development.append({"variant": variant, "fold": fold, "temperature": 1., "temperature_n": 200,
                "temperature_supported_n": 200, "temperature_supported_fraction": 1., "temperature_fallback": False,
                "role_counts": [9, 1, 2, 3], "derived_role_sha256": "0" * 64,
                "selected_hyperparameters": {"params": {"ngram_range": [1, 1], "min_df": 2, "C": .5},
                                             "inner_mean_map_at_3": .5}, "policies": policies})
            reproduction.append({"variant": variant, "fold": fold, "checks": [
                {"model": model, "metric": metric, "actual": .5, "reference": .5, "absolute_difference": 0.}
                for model in ("tfidf_logreg", "frequency_baseline") for metric in ("top1_accuracy", "map_at_3")]})
            for rule in RULES:
                for policy in (None, *policies[rule]):
                    records.append({"variant": variant, "fold": fold, "rule": rule,
                        "target_percent": None if policy is None else policy["target_percent"], "policy": policy,
                        "evaluation": evaluate_policy(**inputs, policy=policy)})
    provenance = {"started_utc": "2026-09-25T00:00:00+00:00", "finished_utc": "2026-09-25T00:01:00+00:00",
        "wall_seconds": 60., "git_revision": "a" * 40, "docker_image_id": "sha256:" + "a" * 64,
        "uid": 10001, "gid": 10001, "seed": 20260831, "protocol_sha256": "a" * 64,
        "configuration_sha256": "a" * 64, "frozen_policies_sha256": "a" * 64, "preserved_files": 10,
        "preservation_verified": True, "all_cutoffs_frozen_before_evaluation": True,
        "model_fitting_calls": 100, "reproduction_checks_passed": 40, "data_sha256": "a" * 64,
        "manifest_sha256": "a" * 64, "assignments_sha256": "a" * 64,
        "packages": {name: "1.0.0" for name in ("numpy", "pandas", "scipy", "scikit-learn", "PyYAML")},
        "row_level_artifacts_serialized": False}
    return {"experiment_id": "E007", "status": "COMPLETED", "provenance": provenance,
            "development": development, "reproduction": reproduction, "records": records,
            "aggregate": aggregate(records)}


@pytest.fixture(scope="module")
def payload(): return synthetic_payload()


def test_complete_grid_schema_and_report(payload):
    validate_public_payload(payload)
    text = report(payload)
    assert "all per-question results" in text and "Unfiltered" in text
    assert len(payload["records"]) == 120
    primary = [s for s in payload["aggregate"]["summaries"] if s["target_percent"] == 20]
    assert all(s["useful_transfer"] for s in primary)
    assert not any(s["useful_transfer"] for s in payload["aggregate"]["summaries"] if s["target_percent"] == 10)
    json.dumps(payload, allow_nan=False)


@pytest.mark.parametrize("mutation", ["private_field", "private_string", "zero_empty_risk", "aggregate", "missing_fold", "threshold", "eligibility"])
def test_publication_rejects_injection_or_corruption(payload, mutation):
    bad = deepcopy(payload)
    record = bad["records"][1]
    if mutation == "private_field": bad["student_response"] = "not allowed"
    elif mutation == "private_string": record["rule"] = "private row content"
    elif mutation == "zero_empty_risk": record["evaluation"]["groups"]["rare"]["risk"] = 0
    elif mutation == "aggregate": bad["aggregate"]["summaries"][0]["groups"]["all"]["risk"]["mean"] = .001
    elif mutation == "missing_fold": bad["records"].pop()
    elif mutation == "threshold": record["policy"] = deepcopy(record["policy"]); record["policy"]["threshold"] = .999
    elif mutation == "eligibility": record["evaluation"]["groups"]["all"]["ece"] = None
    with pytest.raises(ValueError): validate_public_payload(bad)


def test_approved_protocol_exact_hash():
    root = Path(__file__).resolve().parents[1]
    assert e007.approved_config(root)["target_percent"] == list(TARGETS)


def test_prepare_uses_disjoint_roles_and_no_evaluation_metrics(monkeypatch):
    frame = pd.DataFrame({"QuestionId": np.repeat(np.arange(15), 240),
                          "Category": np.tile(["A"] * 216 + ["B"] * 24, 15),
                          "Misconception": "NA", "StudentExplanation": "invented", "QuestionText": "invented"})
    assignments = pd.DataFrame({"fold_0": np.repeat(["train"] * 9 + ["calibration"] * 3 + ["evaluation"] * 3, 240)})
    seen = []
    params = {"params": {"ngram_range": [1, 1], "min_df": 2, "C": .5}, "inner_mean_map_at_3": .5}
    def tune(train, *args, **kwargs):
        assert set(train.QuestionId) == set(range(9))
        return params
    monkeypatch.setattr(e001, "score_params", tune)
    monkeypatch.setattr(e001, "fit_tfidf_lr", lambda *args: None)
    def predict(model, rows, variant):
        seen.append(set(rows.QuestionId))
        return np.tile([.9, .1], (len(rows), 1)), np.array(["A:NA", "B:NA"])
    monkeypatch.setattr(e001, "predict", predict)
    class Live:
        def update(self, *args, **kwargs): pass
    description, memory = e007.prepare_fold(frame, assignments, "explanation_only", 0, Live(), 0)
    assert list(map(len, seen)) == [1, 2, 3]
    assert seen[0].isdisjoint(seen[1]) and (seen[0] | seen[1]) == {9, 10, 11}
    assert seen[2] == {12, 13, 14}
    assert "truth" not in description and "learned_prob" not in description
    assert len(memory["truth"]) == 720
    assert description["temperature_supported_n"] == 240


def test_temperature_unsupported_exclusion_and_fallback():
    classes = np.array(["A", "B"])
    p = np.tile([.8, .2], (400, 1))
    truth = np.array(["A"] * 200 + ["U"] * 200)
    t, n = e001.temperature_scale(truth, p, classes)
    reference, _ = e001.temperature_scale(truth[:200], p[:200], classes)
    assert n == 200 and t == reference
    assert e001.temperature_scale(np.array(["U"] * 400), p, classes) == (1., 0)


@pytest.mark.parametrize("path", ["docs/E007_PROTOCOL.md", "experiments/e007_threshold_transfer.yaml"])
def test_changed_approved_document_blocks_execution(tmp_path, path):
    root = Path(__file__).resolve().parents[1]
    for name in ("docs/E007_PROTOCOL.md", "experiments/e007_threshold_transfer.yaml", "experiments/e007_approval.yaml"):
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text((root / name).read_text(encoding="utf-8"), encoding="utf-8")
    target = tmp_path / path
    target.write_text(target.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(ValueError): e007.approved_config(tmp_path)


def test_reproduction_rejects_retuning_and_changed_metrics():
    inputs = evaluation_inputs()
    memory = {"truth": inputs["truth"], "learned_prob": inputs["probabilities"], "classes": inputs["classes"],
              "frequency_prob": inputs["probabilities"], "frequency_classes": inputs["classes"]}
    selected = {"params": {"C": .5}}
    description = {"selected_hyperparameters": selected}
    ref = {"selected_hyperparameters": deepcopy(selected),
           "tfidf_logreg": {"top1_accuracy": .8, "map_at_3": .85},
           "frequency_baseline": {"top1_accuracy": .8, "map_at_3": .85}}
    assert len(e007.reproduction_checks(description, memory, ref)) == 4
    ref["selected_hyperparameters"]["params"]["C"] = 1.
    with pytest.raises(ValueError): e007.reproduction_checks(description, memory, ref)
    ref["selected_hyperparameters"] = selected
    ref["tfidf_logreg"]["top1_accuracy"] += 1e-8
    with pytest.raises(ValueError): e007.reproduction_checks(description, memory, ref)


def test_source_hard_barrier_precedes_any_evaluation_call():
    import inspect
    source = inspect.getsource(e007.main)
    assert source.index('write_new(output / "frozen_policies.json"') < source.index("evaluate_fold(")
    prepare = inspect.getsource(e007.prepare_fold)
    assert "reproduction_checks(" not in prepare and "evaluate_policy(" not in prepare


def test_changing_evaluation_labels_does_not_change_retention():
    inputs = evaluation_inputs()
    policy = select_cutoff(np.full(400, .8), np.ones(400, bool), np.repeat([0, 1], 200), 20)
    first = evaluate_policy(**inputs, policy=policy)
    inputs["truth"] = np.full(600, "U")
    second = evaluate_policy(**inputs, policy=policy)
    assert first["groups"]["all"]["retained_n"] == second["groups"]["all"]["retained_n"] == 600
    assert second["groups"]["all"]["risk"] == 1


def test_all_abstained_complete_grid_never_counts_as_success(payload):
    records = []
    for r in payload["records"]:
        inputs = evaluation_inputs()
        inputs["evaluation_questions"] += r["fold"] * 3
        target = r["target_percent"]
        policy = None if target is None else select_cutoff(np.ones(400), np.zeros(400, bool), np.repeat([0, 1], 200), target)
        records.append({**r, "policy": policy, "evaluation": evaluate_policy(**inputs, policy=policy)})
    result = aggregate(records)
    for s in result["summaries"]:
        if s["target_percent"] is not None:
            assert s["useful_transfer"] is False
            assert s["groups"]["all"]["risk"]["defined_folds"] == 0
            assert s["groups"]["all"]["coverage"]["defined_folds"] == 5
