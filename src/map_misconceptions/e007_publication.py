"""Strict aggregate-only E007 schema, verification, and deterministic report."""
from __future__ import annotations

import json
import math
from pathlib import Path
import re

from .threshold_transfer import METRICS, STRATA, TARGETS, RULES, aggregate

N = ("number",)
I = ("integer",)
B = ("boolean",)
def nullable(spec): return ("nullable", spec)
def listing(spec): return ("list", spec)
def enum(*values): return ("enum", values)
def pattern(value): return ("pattern", value)
NN = nullable(N)
NB = nullable(B)
HASH = pattern(r"[0-9a-f]{64}")
VARIANT = enum("explanation_only", "question_plus_explanation")
RULE = enum(*RULES)
TARGET = nullable(enum(*TARGETS))
STAT = {"mean": NN, "sd": NN, "defined_folds": I}
GROUP = {name: NN for name in METRICS}
GROUP.update({k: I for k in ("original_n", "retained_n", "correct_n", "incorrect_n")})
GROUP.update({"calibration_ineligible_reasons": listing(enum("n_below_200", "correct_below_20", "incorrect_below_20")),
              "target_exceeded": NB, "risk_target_met": NB, "count_floor_met": B, "coverage_floor_met": B})
GROUPS = {name: GROUP for name in STRATA}
DEV = {"role_index": enum(0, 1), "original_n": I, "retained_n": I, "incorrect_n": I,
       "coverage": N, "risk": NN}
POLICY = {"target_percent": enum(*TARGETS), "status": enum("SELECTED", "NO_ADMISSIBLE_THRESHOLD"),
          "threshold": NN, "candidate_count": I, "admissible_candidate_count": I, "development": listing(DEV)}
HYPER = {"params": {"ngram_range": listing(I), "min_df": enum(2, 5), "C": enum(0.5, 1.0, 2.0)},
         "inner_mean_map_at_3": N}
DEVELOPMENT = {"variant": VARIANT, "fold": enum(0, 1, 2, 3, 4), "temperature": N,
               "temperature_n": I, "temperature_supported_n": I, "temperature_supported_fraction": N,
               "temperature_fallback": B, "role_counts": listing(I), "derived_role_sha256": HASH,
               "selected_hyperparameters": HYPER, "policies": {rule: listing(POLICY) for rule in RULES}}
QUESTION = {"QuestionId": I, "groups": GROUPS, "risk_minus_development": NN}
RECORD = {"variant": VARIANT, "fold": enum(0, 1, 2, 3, 4), "rule": RULE, "target_percent": TARGET,
          "policy": nullable(POLICY), "evaluation": {"groups": GROUPS, "questions": listing(QUESTION)}}
SUMMARY = {"variant": VARIANT, "rule": RULE, "target_percent": TARGET,
           "groups": {name: {metric: STAT for metric in METRICS} for name in STRATA},
           "admissible_folds": nullable(I), "nonempty_questions": I, "count_floor_questions": I,
           "coverage_floor_questions": I, "both_floors_questions": I, "risk_met_questions": nullable(I),
           "risk_exceeded_questions": nullable(I), "maximum_question_risk": NN, "useful_transfer": NB}
PAIRED_FOLD = {"fold": I, "left_coverage": N, "right_coverage": N,
               "coverage_difference": N, "risk_difference": NN}
PAIRED = {"variant": VARIANT, "target_percent": enum(*TARGETS), "left": RULE, "right": RULE,
          "folds": listing(PAIRED_FOLD), "coverage_difference": STAT, "risk_difference": STAT}
CHECK = {"model": enum("tfidf_logreg", "frequency_baseline"), "metric": enum("top1_accuracy", "map_at_3"),
         "actual": N, "reference": N, "absolute_difference": N}
PROVENANCE = {"started_utc": pattern(r"[0-9T:+.Z-]+"), "finished_utc": pattern(r"[0-9T:+.Z-]+"),
              "wall_seconds": N, "git_revision": pattern(r"[0-9a-f]{40}"),
              "docker_image_id": pattern(r"sha256:[0-9a-f]{64}"), "uid": enum(10001), "gid": enum(10001),
              "seed": enum(20260831), "protocol_sha256": HASH, "configuration_sha256": HASH,
              "frozen_policies_sha256": HASH, "preserved_files": I, "preservation_verified": enum(True),
              "all_cutoffs_frozen_before_evaluation": enum(True), "model_fitting_calls": enum(100),
              "reproduction_checks_passed": enum(40), "data_sha256": HASH, "manifest_sha256": HASH,
              "assignments_sha256": HASH, "packages": {name: pattern(r"[A-Za-z0-9.+_-]{1,50}")
                for name in ("numpy", "pandas", "scipy", "scikit-learn", "PyYAML")},
              "row_level_artifacts_serialized": enum(False)}
SCHEMA = {"experiment_id": enum("E007"), "status": enum("COMPLETED"), "provenance": PROVENANCE,
          "development": listing(DEVELOPMENT),
          "reproduction": listing({"variant": VARIANT, "fold": I, "checks": listing(CHECK)}),
          "records": listing(RECORD), "aggregate": {"summaries": listing(SUMMARY), "paired": listing(PAIRED)}}


def validate_schema(value, schema):
    """Reject unknown fields and free text; never echo offending private content."""
    if isinstance(schema, dict):
        if not isinstance(value, dict) or set(value) != set(schema):
            raise ValueError("Public object has missing or unapproved fields.")
        for key, child in schema.items():
            validate_schema(value[key], child)
        return
    kind = schema[0]
    if kind == "nullable":
        if value is not None:
            validate_schema(value, schema[1])
    elif kind == "list":
        if not isinstance(value, list):
            raise ValueError("Expected list.")
        for child in value:
            validate_schema(child, schema[1])
    elif kind == "enum":
        if not any(type(value) is type(item) and value == item for item in schema[1]):
            raise ValueError("Unapproved enum value.")
    elif kind == "pattern":
        if not isinstance(value, str) or not re.fullmatch(schema[1], value):
            raise ValueError("Unapproved string value.")
    elif kind == "boolean":
        if type(value) is not bool:
            raise ValueError("Expected boolean.")
    elif kind == "integer":
        if type(value) is not int or value < 0:
            raise ValueError("Expected nonnegative integer.")
    elif kind == "number":
        if type(value) not in (int, float) or not math.isfinite(value):
            raise ValueError("Expected finite number.")
    else:
        raise ValueError("Unknown schema type.")


def _same(actual, expected):
    if actual is None or expected is None:
        if actual is not expected:
            raise ValueError("Null metric mismatch.")
    elif abs(actual - expected) > 1e-12:
        raise ValueError("Aggregate arithmetic mismatch.")


def validate_groups(groups, target):
    all_n = groups["all"]["retained_n"]
    for group in groups.values():
        original, n, errors = group["original_n"], group["retained_n"], group["incorrect_n"]
        if not 0 <= errors <= n <= original or group["correct_n"] + errors != n:
            raise ValueError("Invalid count identity.")
        _same(group["coverage"], n / original if original else None)
        _same(group["review_fraction"], 1 - n / original if original else None)
        _same(group["share_of_retained"], n / all_n if all_n else None)
        _same(group["risk"], errors / n if n else None)
        _same(group["top1_accuracy"], (n - errors) / n if n else None)
        _same(group["error_minus_target"], errors / n - target / 100 if n and target else None)
        if group["count_floor_met"] != (n >= 100) or group["coverage_floor_met"] != (original > 0 and n * 10 >= original):
            raise ValueError("Coverage/count decision mismatch.")
        if group["risk_target_met"] != (errors * 100 <= target * n if n and target else None):
            raise ValueError("Risk decision mismatch.")
        if group["target_exceeded"] != (errors * 100 > target * n if n and target else None):
            raise ValueError("Risk exceedance mismatch.")
        reasons = (["n_below_200"] if n < 200 else []) + (["correct_below_20"] if n - errors < 20 else []) + (["incorrect_below_20"] if errors < 20 else [])
        if group["calibration_ineligible_reasons"] != reasons:
            raise ValueError("Eligibility mismatch.")
        if any((group[k] is None) != bool(reasons) for k in ("ece", "brier")):
            raise ValueError("Calibration null mismatch.")
        if not n and any(group[k] is not None for k in ("map_at_3", "mean_confidence")):
            raise ValueError("Empty group metric mismatch.")
        if n and (not 0 <= group["map_at_3"] <= 1 or not 0 <= group["mean_confidence"] <= 1):
            raise ValueError("Metric outside range.")
    for field in ("original_n", "retained_n", "correct_n", "incorrect_n"):
        if sum(groups[g][field] for g in ("unsupported", "rare", "frequent")) != groups["all"][field]:
            raise ValueError("Support partition mismatch.")
        if groups["well_supported"][field] > groups["frequent"][field]:
            raise ValueError("Nested support mismatch.")
    if groups["unsupported"]["correct_n"] != 0:
        raise ValueError("Unsupported label marked correct.")


def validate_public_payload(payload):
    validate_schema(payload, SCHEMA)
    development = {(d["variant"], d["fold"]): d for d in payload["development"]}
    if len(payload["development"]) != 10 or len(development) != 10:
        raise ValueError("Incomplete development grid.")
    for d in development.values():
        if d["role_counts"] != [9, 1, 2, 3]:
            raise ValueError("Role counts changed.")
        _same(d["temperature_supported_fraction"], d["temperature_supported_n"] / d["temperature_n"])
        if d["temperature_fallback"] != (d["temperature_supported_n"] == 0) or d["temperature"] <= 0:
            raise ValueError("Invalid temperature record.")
        for policies in d["policies"].values():
            if [p["target_percent"] for p in policies] != list(TARGETS):
                raise ValueError("Target grid changed.")
            for p in policies:
                if [q["role_index"] for q in p["development"]] != [0, 1]:
                    raise ValueError("Development roles changed.")
                selected = p["status"] == "SELECTED"
                if selected != (p["threshold"] is not None) or selected != (p["admissible_candidate_count"] > 0):
                    raise ValueError("Policy status inconsistent.")
                for q in p["development"]:
                    n, e, orig = q["retained_n"], q["incorrect_n"], q["original_n"]
                    _same(q["coverage"], n / orig)
                    _same(q["risk"], e / n if n else None)
                    if selected and not (n >= 100 and n * 10 >= orig and e * 100 <= p["target_percent"] * n):
                        raise ValueError("Selected development threshold is inadmissible.")
                    if not selected and n != 0:
                        raise ValueError("Absent policy retained development cases.")
    for record in payload["records"]:
        p, target = record["policy"], record["target_percent"]
        expected = None if target is None else next(p for p in development[(record["variant"], record["fold"])]["policies"][record["rule"]] if p["target_percent"] == target)
        if p != expected:
            raise ValueError("Evaluation policy differs from frozen development policy.")
        evaluation = record["evaluation"]
        validate_groups(evaluation["groups"], target)
        if len(evaluation["questions"]) != 3:
            raise ValueError("Evaluation question count differs.")
        for q in evaluation["questions"]:
            validate_groups(q["groups"], target)
            risk = q["groups"]["all"]["risk"]
            devrisk = sum(item["risk"] for item in p["development"]) / 2 if p and p["status"] == "SELECTED" else None
            _same(q["risk_minus_development"], risk - devrisk if risk is not None and devrisk is not None else None)
        for group in STRATA:
            for field in ("original_n", "retained_n", "correct_n", "incorrect_n"):
                if sum(q["groups"][group][field] for q in evaluation["questions"]) != evaluation["groups"][group][field]:
                    raise ValueError("Question/fold totals mismatch.")
        if p and p["status"] == "NO_ADMISSIBLE_THRESHOLD" and evaluation["groups"]["all"]["retained_n"] != 0:
            raise ValueError("Deferral-only policy retained cases.")
        if target is None and evaluation["groups"]["all"]["coverage"] != 1:
            raise ValueError("Unfiltered reference did not retain all cases.")
    if aggregate(payload["records"]) != payload["aggregate"]:
        raise ValueError("Serialized aggregate differs from recomputation.")
    checks = payload["reproduction"]
    if len(checks) != 10 or len({(c["variant"], c["fold"]) for c in checks}) != 10:
        raise ValueError("Reproduction grid incomplete.")
    for row in checks:
        if len(row["checks"]) != 4:
            raise ValueError("Reproduction checks incomplete.")
        for check in row["checks"]:
            _same(check["absolute_difference"], abs(check["actual"] - check["reference"]))
            if check["absolute_difference"] > 1e-10:
                raise ValueError("Failed reproduction gate.")


def report(payload):
    validate_public_payload(payload)
    def number(x): return "—" if x is None else f"{x:.4f}"
    def stat(x): return f"{number(x['mean'])} ± {number(x['sd'])} [{x['defined_folds']}]"
    lines = ["# E007 — fixed-cutoff transfer results", "", "Status: **COMPLETED**. Numerical results only; no interpretation or subsequent experiment proposal.", "",
             "Equal-fold mean ± sample SD [defined folds]. Undefined risk is null, not zero. Coverage includes deferral-only folds; risk averages may be conditional on fewer folds. Primary error target: 20%; secondary: 10%/30%.", "",
             "The frozen outer folds/classifiers are preserved. Unlike E006, temperature fitting uses one calibration question and cutoff selection uses two separate questions. Cutoffs were fixed before all evaluation scoring; no evaluation-batch quota was imposed.", "",
             "[Full aggregate/fold/question/stratum JSON](../results/E007_aggregates.json) includes all registered metrics, eligibility reasons, development counts and paired comparisons.", "",
             "## Aggregate all-case results", "",
             "| Arm | Rule | Target | Admissible folds | Coverage | Accuracy | MAP@3 | Risk | ECE | Brier |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for s in payload["aggregate"]["summaries"]:
        g = s["groups"]["all"]
        target = "Unfiltered" if s["target_percent"] is None else f"{s['target_percent']}%"
        lines.append(f"| {s['variant']} | {s['rule']} | {target} | {s['admissible_folds'] if s['admissible_folds'] is not None else '—'} | " + " | ".join(stat(g[k]) for k in ("coverage", "top1_accuracy", "map_at_3", "risk", "ece", "brier")) + " |")
    for variant in ("explanation_only", "question_plus_explanation"):
        lines += ["", f"## {variant}: all fold-level results", "",
                  "| Fold | Rule | Target | Cutoff | Retained / original | Coverage | Accuracy | MAP@3 | Risk | ECE | Brier |",
                  "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in payload["records"]:
            if r["variant"] != variant: continue
            g, p = r["evaluation"]["groups"]["all"], r["policy"]
            target = "Unfiltered" if p is None else f"{r['target_percent']}%"
            cutoff = "Unfiltered" if p is None else ("NONE" if p["threshold"] is None else format(p["threshold"], ".17g"))
            lines.append(f"| {r['fold']} | {r['rule']} | {target} | {cutoff} | {g['retained_n']} / {g['original_n']} | " + " | ".join(number(g[k]) for k in ("coverage", "top1_accuracy", "map_at_3", "risk", "ece", "brier")) + " |")
        lines += ["", f"## {variant}: all per-question results", "",
                  "| Fold | Question | Rule | Target | Retained / original | Coverage | Accuracy | MAP@3 | Risk | Error minus target | Risk minus development | ECE | Brier |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in payload["records"]:
            if r["variant"] != variant: continue
            for q in r["evaluation"]["questions"]:
                g = q["groups"]["all"]
                target = "Unfiltered" if r["target_percent"] is None else f"{r['target_percent']}%"
                values = [g[k] for k in ("coverage", "top1_accuracy", "map_at_3", "risk", "error_minus_target")] + [q["risk_minus_development"], g["ece"], g["brier"]]
                lines.append(f"| {r['fold']} | {q['QuestionId']} | {r['rule']} | {target} | {g['retained_n']} / {g['original_n']} | " + " | ".join(number(v) for v in values) + " |")
    lines += ["", "## Registered criterion counts", "",
              "| Arm | Rule | Target | Admissible / 5 | Nonempty / 15 | Count floor / 15 | Coverage floor / 15 | Both floors / 15 | Risk met / 15 | Exceeded / nonempty | Max question risk | Criterion met |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in payload["aggregate"]["summaries"]:
        if s["target_percent"] is None: continue
        lines.append(f"| {s['variant']} | {s['rule']} | {s['target_percent']}% | {s['admissible_folds']} | {s['nonempty_questions']} | {s['count_floor_questions']} | {s['coverage_floor_questions']} | {s['both_floors_questions']} | {s['risk_met_questions']} | {s['risk_exceeded_questions']} / {s['nonempty_questions']} | {number(s['maximum_question_risk'])} | {s['useful_transfer']} |")
    lines += ["", "## Paired fold summaries at the same target", "",
              "Different rules can retain different populations and coverage. Undefined risk pairs remain absent, not zero differences.", "",
              "| Arm | Target | Left | Right | Coverage difference | Risk difference |",
              "|---|---|---|---|---|---|"]
    for p in payload["aggregate"]["paired"]:
        lines.append(f"| {p['variant']} | {p['target_percent']}% | {p['left']} | {p['right']} | {stat(p['coverage_difference'])} | {stat(p['risk_difference'])} |")
    lines += ["", "## Execution", "", f"Runtime: {payload['provenance']['wall_seconds']:.3f} seconds. Pre-run revision: `{payload['provenance']['git_revision']}`. Reproduction gates: 40/40. Preserved file hashes verified: {payload['provenance']['preserved_files']}.", "",
              "No raw responses, row-level predictions, probabilities, rankings, or fitted models are published. Calibration and subgroup details remain in the complete JSON. All uncertainty is descriptive; this repeatedly examined 15-question benchmark does not supply a deployment guarantee.", ""]
    return "\n".join(lines)


def publish(root):
    payload = json.loads((root / "artifacts/e007/results.json").read_text(encoding="utf-8"))
    validate_public_payload(payload)
    contents = {root / "results/E007_aggregates.json": json.dumps(payload, indent=2, allow_nan=False) + "\n",
                root / "docs/E007_RESULTS.md": report(payload)}
    for path, content in contents.items():
        if path.exists() and path.read_text(encoding="utf-8") != content:
            raise ValueError("Refusing to overwrite different published results.")
    for path, content in contents.items():
        if not path.exists():
            with path.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(content)


if __name__ == "__main__":
    publish(Path(__file__).resolve().parents[2])
