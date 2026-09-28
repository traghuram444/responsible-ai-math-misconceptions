"""Strict scalar/count allowlist and deterministic full E008 results report."""
from __future__ import annotations

import json
from pathlib import Path

from .e007_publication import (N, I, B, NN, HASH, VARIANT, RULE, DEVELOPMENT, PROVENANCE,
                               enum, pattern, listing, nullable, validate_schema, _same)
from .feasibility_diagnostics import (CODES, HIST_KEYS, COUNT_KEYS, VARIANTS, aggregate,
                                      histogram_counts, metric_names, oracle_bound)
from .threshold_transfer import TARGETS

ROLE = enum(0, 1)
FOLD = enum(0, 1, 2, 3, 4)
TARGET = enum(*TARGETS)
OID = pattern(r"(?:tfidf_logreg:(?:explanation_only|question_plus_explanation)|frequency_baseline:shared_frequency):[0-4]:[01]")
HIST = {key: I for key in HIST_KEYS}
COUNTS = {key: I for key in COUNT_KEYS}
WITNESS = {"threshold": N, "retained_n": I, "incorrect_n": I, "coverage": N, "risk": N}
MINIMUM = {**WITNESS, "error_minus_target": N, "oracle_risk_gap": N}
STATUS = enum("FOUND", "NO_FEASIBLE_FLOOR")
ORACLE = {"oracle_id": OID, "variant": enum(*VARIANTS, "shared_frequency"),
          "model": enum("tfidf_logreg", "frequency_baseline"), "fold": FOLD, "role_index": ROLE,
          "original_n": I, "correct_n": I, "coverage_minimum_n": I, "minimum_n": I,
          "stronger_floor": enum("count", "coverage", "equal"), "minimum_risk": NN,
          "targets": listing({"target_percent": TARGET, "maximum_retained_n": I, "maximum_coverage": N, "feasible": B})}
QUESTION = {"role_index": ROLE, "oracle_id": OID, "histogram": HIST, "counts": COUNTS,
            "individual_feasible": B, "oracle_feasible": B, "fixed_prediction_limit": B, "score_selection_limit": B,
            "minimum_status": STATUS, "minimum": nullable(MINIMUM)}
RECORD = {"variant": VARIANT, "fold": FOLD, "rule": RULE, "target_percent": TARGET,
          "candidate_count": I, "joint_histogram": HIST, "joint_counts": COUNTS,
          "shared_feasible_count": enum(0), "shared_minimum_status": STATUS,
          "shared_minimax": nullable({"threshold": N, "worst_risk": N, "error_minus_target": N,
                                       "questions": listing({"role_index": ROLE, **WITNESS})}),
          "questions": listing(QUESTION), "outcome": enum(*CODES)}
PROV = {key: value for key, value in PROVENANCE.items() if key not in
        ("frozen_policies_sha256", "all_cutoffs_frozen_before_evaluation", "reproduction_checks_passed")}
PROV.update({"e007_result_sha256": HASH, "e007_frozen_policies_sha256": HASH,
             "outer_evaluation_prediction_calls": enum(0), "reproduced_policy_records": enum(90)})
CHECK = {"variant": VARIANT, "fold": FOLD, "temperature_absolute_difference": N,
         "inner_mean_map_at_3_absolute_difference": N, "exact_fields_match": enum(True), "policy_records_matched": enum(9)}
SUMMARY = {"variant": VARIANT, "rule": RULE, "target_percent": TARGET,
           "outcome_counts": {code: I for code in CODES},
           "metrics": {key: {"mean": NN, "sd": NN, "defined_folds": I, "fold_values": listing(NN)} for key in metric_names()}}
SCHEMA = {"experiment_id": enum("E008"), "status": enum("COMPLETED"), "provenance": PROV,
          "development": listing(DEVELOPMENT), "reproduction": listing(CHECK), "oracles": listing(ORACLE),
          "records": listing(RECORD), "aggregate": listing(SUMMARY)}


def _witness(witness, oracle):
    n, e = witness["retained_n"], witness["incorrect_n"]
    if not (0 <= e <= n <= oracle["original_n"] and n >= oracle["minimum_n"]
            and 0 <= witness["threshold"] <= 1 and n - e <= oracle["correct_n"]
            and e <= oracle["original_n"] - oracle["correct_n"]):
        raise ValueError("Invalid diagnostic witness counts or bounds.")
    _same(witness["coverage"], n / oracle["original_n"])
    _same(witness["risk"], e / n)


def validate_public_payload(payload):
    validate_schema(payload, SCHEMA)
    oracles = {o["oracle_id"]: o for o in payload["oracles"]}
    if len(oracles) != 30 or len(payload["oracles"]) != 30:
        raise ValueError("Oracle grid incomplete.")
    expected_ids = {f"{model}:{arm}:{fold}:{role}" for model, arm in
                    [("tfidf_logreg", v) for v in VARIANTS] + [("frequency_baseline", "shared_frequency")]
                    for fold in range(5) for role in (0, 1)}
    if set(oracles) != expected_ids:
        raise ValueError("Oracle contexts changed.")
    for oracle in oracles.values():
        expected = oracle_bound(oracle["original_n"], oracle["correct_n"], variant=oracle["variant"],
                                fold=oracle["fold"], model=oracle["model"], role_index=oracle["role_index"])
        if oracle != expected:
            raise ValueError("Oracle formula mismatch.")
    development = {(d["variant"], d["fold"]): d for d in payload["development"]}
    contexts = {(v, f) for v in VARIANTS for f in range(5)}
    if len(payload["development"]) != 10 or set(development) != contexts:
        raise ValueError("Development grid incomplete.")
    for d in development.values():
        if d["role_counts"] != [9, 1, 2, 3] or d["temperature"] <= 0 or not 0 <= d["temperature_supported_n"] <= d["temperature_n"]:
            raise ValueError("Development role/temperature mismatch.")
        _same(d["temperature_supported_fraction"], d["temperature_supported_n"] / d["temperature_n"])
        if d["temperature_fallback"] != (d["temperature_supported_n"] == 0):
            raise ValueError("Temperature fallback mismatch.")
        for policies in d["policies"].values():
            if [p["target_percent"] for p in policies] != list(TARGETS):
                raise ValueError("Policy target grid changed.")
            for p in policies:
                if p["status"] != "NO_ADMISSIBLE_THRESHOLD" or p["threshold"] is not None or p["admissible_candidate_count"] != 0:
                    raise ValueError("E007 policy contradiction.")
                if [q["role_index"] for q in p["development"]] != [0, 1]:
                    raise ValueError("Policy role grid changed.")
                for q in p["development"]:
                    if q["original_n"] <= 0 or q["retained_n"] or q["incorrect_n"] or q["coverage"] != 0 or q["risk"] is not None:
                        raise ValueError("Nonempty absent policy.")
    checks = payload["reproduction"]
    if len(checks) != 10 or {(c["variant"], c["fold"]) for c in checks} != contexts:
        raise ValueError("Reproduction grid incomplete.")
    for c in checks:
        if any(not 0 <= c[key] <= 1e-10 for key in ("temperature_absolute_difference", "inner_mean_map_at_3_absolute_difference")):
            raise ValueError("Failed reproduction gate.")
    for r in payload["records"]:
        target = r["target_percent"]
        policy = next(p for p in development[(r["variant"], r["fold"])]["policies"][r["rule"]] if p["target_percent"] == target)
        if r["candidate_count"] != policy["candidate_count"] or r["joint_counts"] != histogram_counts(r["joint_histogram"]):
            raise ValueError("Candidate grid or joint partition mismatch.")
        if r["joint_counts"]["total"] != r["candidate_count"] or r["joint_histogram"]["111"] != 0:
            raise ValueError("Shared feasibility contradiction.")
        if [q["role_index"] for q in r["questions"]] != [0, 1]:
            raise ValueError("Question grid changed.")
        for q in r["questions"]:
            oracle = oracles[q["oracle_id"]]
            arm = "shared_frequency" if r["rule"] == "frequency" else r["variant"]
            if (oracle["variant"], oracle["fold"], oracle["role_index"]) != (arm, r["fold"], q["role_index"]):
                raise ValueError("Question references wrong oracle.")
            if oracle["original_n"] != policy["development"][q["role_index"]]["original_n"]:
                raise ValueError("Development sample count mismatch.")
            if q["counts"] != histogram_counts(q["histogram"]) or q["counts"]["total"] != r["candidate_count"]:
                raise ValueError("Question partition mismatch.")
            feasible = next(b["feasible"] for b in oracle["targets"] if b["target_percent"] == target)
            individual = q["counts"]["all_three"] > 0
            if (q["individual_feasible"] != individual or q["oracle_feasible"] != feasible
                    or q["fixed_prediction_limit"] != (not feasible) or q["score_selection_limit"] != (feasible and not individual)
                    or (individual and not feasible)):
                raise ValueError("Feasibility flags mismatch.")
            minimum = q["minimum"]
            if (minimum is not None) != (q["counts"]["both_floors"] > 0) or q["minimum_status"] != ("FOUND" if minimum else "NO_FEASIBLE_FLOOR"):
                raise ValueError("Question minimum status mismatch.")
            if minimum is not None:
                _witness(minimum, oracle)
                _same(minimum["error_minus_target"], minimum["risk"] - target / 100)
                _same(minimum["oracle_risk_gap"], minimum["risk"] - oracle["minimum_risk"])
                if minimum["oracle_risk_gap"] < 0 or individual != (100 * minimum["incorrect_n"] <= target * minimum["retained_n"]):
                    raise ValueError("Question optimized risk contradicts feasibility.")
        common = r["shared_minimax"]
        if (common is not None) != (r["joint_counts"]["both_floors"] > 0) or r["shared_minimum_status"] != ("FOUND" if common else "NO_FEASIBLE_FLOOR"):
            raise ValueError("Shared minimum status mismatch.")
        if common is not None:
            if [q["role_index"] for q in common["questions"]] != [0, 1]:
                raise ValueError("Shared witness roles changed.")
            for q, witness in zip(r["questions"], common["questions"]):
                _witness(witness, oracles[q["oracle_id"]])
                if witness["threshold"] != common["threshold"] or witness["risk"] < q["minimum"]["risk"]:
                    raise ValueError("Shared witness inconsistent.")
            _same(common["worst_risk"], max(q["risk"] for q in common["questions"]))
            _same(common["error_minus_target"], common["worst_risk"] - target / 100)
        outcome = (CODES[0] if any(q["fixed_prediction_limit"] for q in r["questions"]) else
                   CODES[1] if any(not q["individual_feasible"] for q in r["questions"]) else CODES[2])
        if outcome != r["outcome"]:
            raise ValueError("Outcome order changed.")
    if payload["aggregate"] != aggregate(payload["records"], payload["oracles"]):
        raise ValueError("Aggregate arithmetic mismatch.")


def report(payload):
    validate_public_payload(payload)
    def num(x): return "null" if x is None else format(x, ".8g")
    def hist(h): return ", ".join(str(h[k]) for k in HIST_KEYS)
    lines = ["# E008 — development feasibility diagnostics", "",
             "Status: **COMPLETED**. Results only; interpretation and the next experiment await user review.", "",
             "Prespecified exploratory diagnostic, not independent confirmatory evidence. No outer-evaluation predictions were made. Diagnostic witnesses are optimized on development correctness, not deployable policies or unbiased estimates. Frequency is the same reference across input arms and is not independent replicated evidence.", "",
             "[Complete scalar/count JSON](../results/E008_aggregates.json). All five fold values, equal-fold mean, sample SD and defined-fold count are included below. No confidence intervals or hypothesis tests. Anonymous role slots may repeat questions across folds.", "",
             "## Outcome counts (out of five folds)", "",
             "| Target | Arm | Rule | FIXED_PREDICTION_LIMIT | SCORE_SELECTION_LIMIT | COMMON_CUTOFF_INCOMPATIBILITY |",
             "|---|---|---|---|---|---|"]
    for target in (20, 10, 30):
        for s in payload["aggregate"]:
            if s["target_percent"] == target:
                lines.append(f"| {target}% | {s['variant']} | {s['rule']} | " + " | ".join(str(s['outcome_counts'][c]) for c in CODES) + " |")
    lines += ["", "## All fold-level constraint and feasibility records", "",
              "Histogram order is C/V/R bits: 000, 001, 010, 011, 100, 101, 110, 111. C=count, V=coverage, R=risk; joint bits require each condition on both questions. Single-condition failures are cells 011/101/110. Counts are grid properties, not comparable performance scores.", "",
              "| Arm | Fold | Rule | Target | Candidates | Joint histogram | A0 size | A1 size | Intersection | Outcome | Minimax risk | Risk minus target | Witness cutoff |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in payload["records"]:
        w = r["shared_minimax"]
        lines.append(f"| {r['variant']} | {r['fold']} | {r['rule']} | {r['target_percent']}% | {r['candidate_count']} | {hist(r['joint_histogram'])} | {r['questions'][0]['counts']['all_three']} | {r['questions'][1]['counts']['all_three']} | {r['shared_feasible_count']} | {r['outcome']} | {num(None if w is None else w['worst_risk'])} | {num(None if w is None else w['error_minus_target'])} | {num(None if w is None else w['threshold'])} |")
    lines += ["", "## All development-question score diagnostics", "",
              "F=fixed-prediction-limit flag; S=oracle-feasible but score-infeasible flag. Minima use the fixed count/coverage floors; null means NO_FEASIBLE_FLOOR. Cutoffs are scalar diagnostic witnesses only. Signed error differences are absolute risk minus target.", "",
              "| Arm | Fold | Rule | Target | Role | Histogram | Feasible | F | S | Min cutoff | Retained | Errors | Coverage | Min risk | Risk minus target | Oracle gap | Shared retained | Shared errors | Shared coverage | Shared risk |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in payload["records"]:
        for q in r["questions"]:
            w, shared = q["minimum"], r["shared_minimax"]
            sw = None if shared is None else shared["questions"][q["role_index"]]
            values = [None if w is None else w[k] for k in ("threshold", "retained_n", "incorrect_n", "coverage", "risk", "error_minus_target", "oracle_risk_gap")]
            values += [None if sw is None else sw[k] for k in ("retained_n", "incorrect_n", "coverage", "risk")]
            lines.append(f"| {r['variant']} | {r['fold']} | {r['rule']} | {r['target_percent']}% | {q['role_index']} | {hist(q['histogram'])} | {q['individual_feasible']} | {q['fixed_prediction_limit']} | {q['score_selection_limit']} | " + " | ".join(num(v) for v in values) + " |")
    lines += ["", "## Fixed-prediction oracle bounds (deduplicated)", "",
              "These are correctness-informed count bounds, not observed selector performance. Effective m=max(100,ceil(N/10)); stronger floor identifies the redundant weaker constraint. K=0 means no possible coverage, not an observed zero error. Each oracle is shared by both learned rules; frequency is shared by both arms.", "",
              "| Model / arm | Fold | Role | N | Correct | Coverage floor n | m | Stronger floor | Oracle min risk at m | K10 | Max coverage10 | Feasible10 | K20 | Max coverage20 | Feasible20 | K30 | Max coverage30 | Feasible30 |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for o in payload["oracles"]:
        values = []
        for b in o["targets"]:
            values += [str(b["maximum_retained_n"]), num(b["maximum_coverage"]), str(b["feasible"])]
        lines.append(f"| {o['model']} / {o['variant']} | {o['fold']} | {o['role_index']} | {o['original_n']} | {o['correct_n']} | {o['coverage_minimum_n']} | {o['minimum_n']} | {o['stronger_floor']} | {num(o['minimum_risk'])} | " + " | ".join(values) + " |")
    lines += ["", "## Complete numeric fold summaries", "", "Values are folds 0–4. Question means weight the two development questions equally; an undefined component leaves that mean null. SD uses ddof=1 and is null with fewer than two defined folds."]
    for s in payload["aggregate"]:
        lines += ["", f"### {s['variant']} / {s['rule']} / {s['target_percent']}%", "",
                  "| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for key, v in s["metrics"].items():
            lines.append(f"| {key} | " + " | ".join(num(x) for x in [*v['fold_values'], v['mean'], v['sd'], v['defined_folds']]) + " |")
    p = payload["provenance"]
    lines += ["", "## Execution checks", "", f"Runtime: {p['wall_seconds']:.3f} seconds. Pre-run revision: `{p['git_revision']}`. Reproduced development policies: 90/90. Preserved files: {p['preserved_files']}. Outer-evaluation prediction calls: 0. No response-level outputs or candidate arrays serialized.", ""]
    return "\n".join(lines)


def publish(root):
    payload = json.loads((root / "artifacts/e008/results.json").read_text(encoding="utf-8"))
    validate_public_payload(payload)
    contents = {root / "results/E008_aggregates.json": json.dumps(payload, indent=2, allow_nan=False) + "\n",
                root / "docs/E008_RESULTS.md": report(payload)}
    for path, content in contents.items():
        if path.exists() and path.read_text(encoding="utf-8") != content:
            raise ValueError("Refusing to overwrite different published results.")
    for path, content in contents.items():
        if not path.exists():
            with path.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(content)


if __name__ == "__main__":
    publish(Path(__file__).resolve().parents[2])
