"""Invented data only: E008 exact diagnostics, role barrier and safe publication."""
from contextlib import nullcontext
from copy import deepcopy
from fractions import Fraction
import itertools
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from map_misconceptions import e001, e008
from map_misconceptions.feasibility_diagnostics import (
    CODES, HIST_KEYS, VARIANTS, _candidate_counts, aggregate, diagnose_rule, histogram_counts, oracle_bound,
)
from map_misconceptions.e008_publication import validate_public_payload, report
from map_misconceptions.threshold_transfer import RULES, TARGETS, calibration_roles, select_cutoff


def bounds(scores, correct, roles, variant=VARIANTS[0], fold=0, rule="confidence_only"):
    return [oracle_bound(int((roles == q).sum()), int(correct[roles == q].sum()), variant=variant,
                         fold=fold, model="frequency_baseline" if rule == "frequency" else "tfidf_logreg",
                         role_index=q) for q in (0, 1)]


def diagnose(scores, correct, roles, **kwargs):
    context = {"variant": VARIANTS[0], "fold": 0, "rule": "confidence_only", **kwargs}
    return diagnose_rule(scores, correct, roles, bounds(scores, correct, roles, **context), **context)


def test_oracle_exhaustive_invented_counts():
    for n in range(1, 41):
        for c in range(n + 1):
            oracle = oracle_bound(n, c, variant=VARIANTS[0], fold=0, model="tfidf_logreg", role_index=0)
            for b in oracle["targets"]:
                valid = [k for k in range(n + 1) if 100 * max(0, k - c) <= b["target_percent"] * k]
                assert b["maximum_retained_n"] == max(valid)
                assert not b["feasible"]  # all N<100; zero coverage is not observed zero risk
            assert oracle["minimum_risk"] is None
    for n in (99, 100, 101, 999, 1000, 1001, 1011, 2001):
        for c in (0, 1, n // 2, n - 1, n):
            o = oracle_bound(n, c, variant=VARIANTS[0], fold=0, model="tfidf_logreg", role_index=0)
            assert o["minimum_n"] == max(100, -(-n // 10))
            for b in o["targets"]:
                valid = [k for k in range(n + 1) if 100 * max(0, k - c) <= b["target_percent"] * k]
                assert b["maximum_retained_n"] == max(valid)
                assert b["feasible"] == any(k >= o["minimum_n"] for k in valid)


def test_all_diagnostic_outcomes_and_ties():
    roles = np.repeat([0, 1], 500)
    score = np.r_[np.full(100, .8), np.full(400, .6), np.full(400, .5), np.full(100, .9)]
    correct = np.r_[np.ones(100, bool), np.zeros(400, bool), np.ones(400, bool), np.zeros(100, bool)]
    rows = diagnose(score, correct, roles)
    assert [r["outcome"] for r in rows] == [CODES[1], CODES[2], CODES[2]]
    assert rows[1]["shared_minimax"]["threshold"] == 0.0  # risk ties -> more rows -> lower cutoff
    assert rows[1]["questions"][0]["minimum"]["risk"] == 0
    assert rows[1]["questions"][1]["minimum"]["risk"] == .2
    assert diagnose(np.full(1000, .5), np.zeros(1000, bool), roles)[0]["outcome"] == CODES[0]
    correct = np.tile(np.arange(500) < 200, 2)
    tied = diagnose(np.full(1000, .5), correct, roles)
    assert all(r["outcome"] == CODES[1] for r in tied)
    assert all(r["candidate_count"] == 2 for r in tied)
    assert tied[0]["questions"][0]["minimum"]["threshold"] == 0


def test_disconnected_feasible_set_and_positive_retention():
    # q0 has separated feasible cutoffs at .9 and .7, but not .8 or .6; q1 is always wrong.
    s0 = np.repeat([.9, .8, .7, .6], [100, 40, 200, 200])
    c0 = np.repeat([True, False, True, False], [100, 40, 200, 200])
    scores = np.r_[s0, np.full(120, .95)]
    correct = np.r_[c0, np.zeros(120, bool)]
    roles = np.repeat([0, 1], [len(s0), 120])
    row = diagnose(scores, correct, roles)[1]
    assert row["questions"][0]["counts"]["all_three"] == 2
    assert row["questions"][0]["histogram"]["000"] == 1  # empty q0 at .95 is not risk-pass
    assert row["outcome"] == CODES[0]


@pytest.mark.parametrize("target", TARGETS)
def test_exact_integer_boundary_and_overlapping_failures(target):
    # q0 passes at exactly a/100; q1 forces absent shared policy.
    scores = np.r_[np.full(100, .8), np.full(100, .9)]
    roles = np.repeat([0, 1], 100)
    correct = np.r_[np.arange(100) >= target, np.zeros(100, bool)]
    row = next(r for r in diagnose(scores, correct, roles) if r["target_percent"] == target)
    assert row["questions"][0]["individual_feasible"]
    correct[99] = False
    row = next(r for r in diagnose(scores, correct, roles) if r["target_percent"] == target)
    assert not row["questions"][0]["individual_feasible"]
    for n, retained, expected_cell in [(500, 50, "011"), (2000, 100, "101"), (2000, 50, "001")]:
        scores = np.r_[np.full(retained, .8), np.full(n - retained, .1), np.full(100, .9)]
        correct = np.r_[np.ones(retained, bool), np.zeros(n - retained + 100, bool)]
        roles = np.repeat([0, 1], [n, 100])
        row = diagnose(scores, correct, roles)[1]
        assert row["questions"][0]["histogram"][expected_cell] > 0


def test_no_feasible_floor_and_shared_reproduction_stop():
    roles = np.repeat([0, 1], [99, 100])
    rows = diagnose(np.ones(199), np.ones(199, bool), roles)
    assert all(r["shared_minimum_status"] == "NO_FEASIBLE_FLOOR" and r["shared_minimax"] is None for r in rows)
    assert rows[0]["questions"][0]["minimum"] is None
    with pytest.raises(ValueError, match="REPRODUCTION_MISMATCH"):
        diagnose(np.ones(200), np.ones(200, bool), np.repeat([0, 1], 100))


@pytest.mark.parametrize("seed", range(12))
def test_independent_exhaustive_score_and_minimax(seed):
    rng = np.random.default_rng(seed)
    roles = np.repeat([0, 1], [500, 1300])
    scores = rng.choice([.1, .2, .4, .7, .9], len(roles))
    correct = rng.random(len(roles)) < .35
    rows = diagnose(scores, correct, roles)
    candidates = sorted(set([0., *scores.tolist()]))
    for row in rows:
        target = row["target_percent"]
        h = {k: 0 for k in HIST_KEYS}
        qh = [{k: 0 for k in HIST_KEYS} for _ in range(2)]
        individual, shared = [[], []], []
        for threshold in candidates:
            stats, conditions = [], []
            for q in (0, 1):
                mask = (roles == q) & (scores >= threshold)
                n, e, total = int(mask.sum()), int((mask & ~correct).sum()), int((roles == q).sum())
                bits = (n >= 100, 10 * n >= total, n > 0 and 100 * e <= target * n)
                qh[q]["".join(str(int(b)) for b in bits)] += 1
                conditions.append(bits)
                stats.append((n, e))
                if bits[0] and bits[1]: individual[q].append((Fraction(e, n), -n, threshold))
            joint = tuple(all(x[k] for x in conditions) for k in range(3))
            h["".join(str(int(b)) for b in joint)] += 1
            if joint[0] and joint[1]:
                shared.append((max(Fraction(e, n) for n, e in stats), -sum(n for n, e in stats), threshold))
        assert row["joint_histogram"] == h
        for q in (0, 1):
            assert row["questions"][q]["histogram"] == qh[q]
            expected = min(individual[q])
            actual = row["questions"][q]["minimum"]
            assert (Fraction(actual["incorrect_n"], actual["retained_n"]), -actual["retained_n"], actual["threshold"]) == expected
        expected = min(shared)
        actual = row["shared_minimax"]
        assert (max(Fraction(q["incorrect_n"], q["retained_n"]) for q in actual["questions"]),
                -sum(q["retained_n"] for q in actual["questions"]), actual["threshold"]) == expected


class Live:
    def update(self, *args, **kwargs): pass


def test_development_never_predicts_outer_evaluation(monkeypatch):
    frame = pd.DataFrame({"QuestionId": np.repeat(np.arange(15), 120), "Category": "A", "Misconception": "x"})
    assignments = pd.DataFrame({"fold_0": np.repeat(["train", "calibration", "evaluation"], [9 * 120, 3 * 120, 3 * 120])})
    selected = {"params": {"ngram_range": [1, 1], "min_df": 2, "C": .5}, "inner_mean_map_at_3": .4}
    seen = []
    def predict(model, rows, variant):
        seen.append(set(rows.QuestionId))
        assert set(rows.QuestionId) <= {9, 10, 11}
        return np.ones((len(rows), 1)), np.array(["A:x"])
    def select(rows, *args, **kwargs):
        assert set(rows.QuestionId) == set(range(9))
        assert kwargs["groups"].equals(rows.QuestionId.astype(str))
        return deepcopy(selected)
    monkeypatch.setattr(e008, "monitored_fits", lambda *a: nullcontext())
    monkeypatch.setattr(e001, "score_params", select)
    monkeypatch.setattr(e001, "fit_tfidf_lr", lambda *a: object())
    monkeypatch.setattr(e001, "predict", predict)
    monkeypatch.setattr(e001, "temperature_scale", lambda y, p, c: (1., len(y)))
    description, memory = e008.prepare_development(frame, assignments, VARIANTS[0], 0, Live(), 0)
    tq, sq = calibration_roles([9, 10, 11], 0)
    assert seen == [{tq}, set(sq)]
    assert set(memory) == set(RULES)
    assert description["role_counts"] == [9, 1, 2, 3]
    assert e008.reproduction_gate(description, deepcopy(description))["exact_fields_match"]
    changed = deepcopy(description)
    changed["temperature"] += 2e-10
    with pytest.raises(ValueError): e008.reproduction_gate(description, changed)
    changed = deepcopy(description)
    changed["policies"]["frequency"][0]["candidate_count"] += 1
    with pytest.raises(ValueError): e008.reproduction_gate(description, changed)


def fixture_payload():
    records, oracles, development, checks = [], {}, [], []
    score = np.full(400, .5)
    correct = np.tile(np.arange(200) < 80, 2)
    roles = np.repeat([0, 1], 200)
    for variant, fold in itertools.product(VARIANTS, range(5)):
        d = {"variant": variant, "fold": fold, "temperature": 1., "temperature_n": 200,
             "temperature_supported_n": 200, "temperature_supported_fraction": 1., "temperature_fallback": False,
             "role_counts": [9, 1, 2, 3], "derived_role_sha256": "a" * 64,
             "selected_hyperparameters": {"params": {"ngram_range": [1, 1], "min_df": 2, "C": .5}, "inner_mean_map_at_3": .4},
             "policies": {rule: [select_cutoff(score, correct, roles, t) for t in TARGETS] for rule in RULES}}
        memory = {rule: (score, correct, roles) for rule in RULES}
        rows, obs = e008.analyze_development(d, memory)
        records.extend(rows)
        for o in obs: oracles[o["oracle_id"]] = o
        development.append(d)
        checks.append(e008.reproduction_gate(d, d))
    prov = {"started_utc": "2026-09-28T00:00:00+00:00", "finished_utc": "2026-09-28T00:01:00+00:00",
            "wall_seconds": 60., "git_revision": "b" * 40, "docker_image_id": "sha256:" + "c" * 64,
            "uid": 10001, "gid": 10001, "seed": 20260831, "preserved_files": 50, "preservation_verified": True,
            "model_fitting_calls": 100, "outer_evaluation_prediction_calls": 0, "reproduced_policy_records": 90,
            "row_level_artifacts_serialized": False,
            "packages": {p: "1.0.0" for p in ("numpy", "pandas", "scipy", "scikit-learn", "PyYAML")}}
    for key in ("protocol_sha256", "configuration_sha256", "e007_result_sha256", "e007_frozen_policies_sha256", "data_sha256", "manifest_sha256", "assignments_sha256"):
        prov[key] = "a" * 64
    obs = list(oracles.values())
    return {"experiment_id": "E008", "status": "COMPLETED", "provenance": prov, "development": development,
            "reproduction": checks, "oracles": obs, "records": records, "aggregate": aggregate(records, obs)}


def test_complete_publication_and_descriptive_fold_statistics():
    p = fixture_payload()
    validate_public_payload(p)
    text = report(p)
    assert "Results only" in text and "Complete numeric fold summaries" in text
    assert len(p["records"]) == 90 and len(p["oracles"]) == 30
    for s in p["aggregate"]:
        assert sum(s["outcome_counts"].values()) == 5
        for v in s["metrics"].values():
            assert len(v["fold_values"]) == 5 and v["defined_folds"] == 5
            assert v["sd"] == pytest.approx(0, abs=1e-15)


@pytest.mark.parametrize("field", ["StudentExplanation", "row_id", "scores", "predictions", "weights", "oracle_selection", "candidate_thresholds"])
def test_publication_rejects_private_extensions(field):
    p = fixture_payload()
    p["records"][0]["questions"][0][field] = ["private"]
    with pytest.raises(ValueError): validate_public_payload(p)


@pytest.mark.parametrize("mutation", ["count", "oracle", "grid", "aggregate", "duplicate", "witness", "frequency"])
def test_publication_rejects_inconsistent_numbers(mutation):
    p = fixture_payload()
    if mutation == "count": p["records"][0]["joint_histogram"]["000"] += 1
    if mutation == "oracle": p["oracles"][0]["targets"][0]["maximum_retained_n"] += 1
    if mutation == "grid": p["records"].pop()
    if mutation == "aggregate": p["aggregate"][0]["metrics"]["candidate_count"]["mean"] += 1
    if mutation == "duplicate": p["oracles"][0] = p["oracles"][1]
    if mutation == "witness": p["records"][0]["questions"][0]["minimum"]["risk"] = .1
    if mutation == "frequency": p["records"][-1]["variant"] = VARIANTS[0]
    with pytest.raises(ValueError): validate_public_payload(p)


def test_approval_lock_and_no_old_scientific_edits():
    root = Path(__file__).resolve().parents[1]
    config = e008.approved_config(root)
    assert config["outer_evaluation_predictions"] == "prohibited"
    assert config["target_percent"] == [10, 20, 30]
    assert config["minimum_retained_per_question"] == 100


def test_e008_viewer_retries_without_touching_experiment():
    from map_misconceptions.e008_monitor import read_status
    events = iter([FileNotFoundError(), '{"status":"RUNNING"}'])
    pauses = []
    def reader():
        item = next(events)
        if isinstance(item, Exception): raise item
        return item
    assert read_status(None, reader=reader, pause=pauses.append)["status"] == "RUNNING"
    assert pauses == [.2]
