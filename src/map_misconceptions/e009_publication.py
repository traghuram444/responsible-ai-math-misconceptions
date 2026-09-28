"""E009 strict aggregate-only export; no fitted or response-level objects."""
from __future__ import annotations

import json
from pathlib import Path

from . import e007_publication as old
from .e009_reliability import RULES, VARIANTS
from .e009_metrics import HEAD_METRICS, aggregate
from .threshold_transfer import METRICS, STRATA, TARGETS

N, I, B, NN, HASH = old.N, old.I, old.B, old.NN, old.HASH
enum, listing, nullable, pattern = old.enum, old.listing, old.nullable, old.pattern
FOLD, RULE = enum(0, 1, 2, 3, 4), enum(*RULES)
STAT = {**old.STAT, "fold_values": listing(NN)}
REASONS = listing(enum("n_below_200", "correct_below_20", "incorrect_below_20"))
FITS = {k: I for k in ("attempted", "successful", "failed", "warnings", "convergence_warnings")}
ROUTER = {"n": I, "correct_n": I, "incorrect_n": I, "question_count": enum(9), "feature_count": enum(5),
          "weight_sum": N, "status": enum("FITTED", "CONSTANT_CORRECTNESS_FALLBACK"),
          "constant": nullable(enum(0, 1)), "fitting_calls": enum(0, 1), "convergence_warnings": enum(0)}
BLOCK = {"block": enum(0, 1, 2), "fitting_questions": enum(6), "held_questions": enum(3),
         "fitting_n": I, "held_n": I, "correct_n": I, "incorrect_n": I,
         "selected_hyperparameters": old.HYPER, "fits": FITS}
DEVELOPMENT = {"variant": old.VARIANT, "fold": FOLD, "reference_development": old.DEVELOPMENT,
               "crossfit": {"role_sha256": HASH, "blocks": listing(BLOCK)}, "router": ROUTER,
               "final_classifier_fits": FITS, "policies": {r: listing(old.POLICY) for r in RULES}}
HEAD = {"n": I, "correct_n": I, "incorrect_n": I, "mean_predicted_correctness": NN,
        "binary_brier": NN, "binary_ece": NN, "ineligible_reasons": REASONS}
HEAD_GROUPS = {s: HEAD for s in STRATA}
HEAD_EVAL = {"groups": HEAD_GROUPS, "questions": listing({"QuestionId": I, "groups": HEAD_GROUPS})}
RECORD = {**old.RECORD, "rule": RULE, "reliability": nullable(HEAD_EVAL)}
AUC = {"n": I, "correct_n": I, "incorrect_n": I, "auroc": NN, "ineligible_reasons": REASONS}
RANK = {"variant": old.VARIANT, "fold": FOLD, "rule": RULE, "all": AUC,
        "questions": listing({"QuestionId": I, **AUC})}
SUMMARY = {**old.SUMMARY, "rule": RULE, "groups": {s: {m: STAT for m in METRICS} for s in STRATA},
           "reliability": nullable({s: {m: STAT for m in HEAD_METRICS} for s in STRATA})}
PAIRED = {**old.PAIRED, "left": enum("learned_reliability"), "right": enum("confidence_only", "raw_confidence", "support_aware", "frequency"),
          "coverage_difference": STAT, "risk_difference": STAT}
RANK_STAT = {"variant": old.VARIANT, "rule": RULE, **STAT}
RANK_PAIR = {"variant": old.VARIANT, "left": enum("learned_reliability"),
             "right": enum("confidence_only", "raw_confidence", "support_aware"), **STAT}
PROV = {k: v for k, v in old.PROVENANCE.items() if k not in ("model_fitting_calls", "reproduction_checks_passed")}
PROV.update({"e007_result_sha256": HASH, "e008_result_sha256": HASH, "classifier_fits": FITS,
             "router_fitting_calls": I, "router_fallbacks": I, "development_policies_reproduced": enum(90), "evaluation_records_reproduced": enum(120)})
DEV_CHECK = {"variant": old.VARIANT, "fold": FOLD, "temperature_absolute_difference": N,
             "inner_mean_map_at_3_absolute_difference": N, "exact_fields_match": enum(True), "policy_records_matched": enum(9)}
SCHEMA = {"experiment_id": enum("E009"), "status": enum("COMPLETED"), "provenance": PROV,
          "development": listing(DEVELOPMENT), "reproduction": {"development": listing(DEV_CHECK),
            "evaluation": listing({"variant": old.VARIANT, "fold": FOLD, "matched_records": enum(12)})},
          "records": listing(RECORD), "ranking": listing(RANK), "aggregate": {"summaries": listing(SUMMARY),
            "paired": listing(PAIRED), "ranking": listing(RANK_STAT), "ranking_paired": listing(RANK_PAIR)}}


def _check_binary(group, original, metric_names):
    if (group["n"], group["correct_n"], group["incorrect_n"]) != (original["retained_n"], original["correct_n"], original["incorrect_n"]):
        raise ValueError("Binary diagnostic count mismatch.")
    reasons = original["calibration_ineligible_reasons"]
    if group["ineligible_reasons"] != reasons:
        raise ValueError("Binary eligibility mismatch.")
    for key in metric_names:
        value = group[key]
        if (value is None) != bool(reasons) or (value is not None and not 0 <= value <= 1):
            raise ValueError("Invalid binary metric/null.")


def _validate_policy(p):
    if [q["role_index"] for q in p["development"]] != [0, 1] or p["candidate_count"] < 1:
        raise ValueError("Policy grid mismatch.")
    selected = p["status"] == "SELECTED"
    if selected != (p["threshold"] is not None) or selected != (p["admissible_candidate_count"] > 0):
        raise ValueError("Policy status mismatch.")
    if p["admissible_candidate_count"] > p["candidate_count"] or (selected and not 0 <= p["threshold"] <= 1):
        raise ValueError("Policy bounds mismatch.")
    for q in p["development"]:
        n, e, original = q["retained_n"], q["incorrect_n"], q["original_n"]
        if original <= 0 or not 0 <= e <= n <= original:
            raise ValueError("Development count mismatch.")
        old._same(q["coverage"], n / original)
        old._same(q["risk"], e / n if n else None)
        if selected and not (n >= 100 and 10 * n >= original and 100 * e <= p["target_percent"] * n):
            raise ValueError("Selected policy is inadmissible.")
        if not selected and n != 0:
            raise ValueError("Absent policy retained data.")


def validate_public_payload(p):
    old.validate_schema(p, SCHEMA)
    contexts = {(v, f) for v in VARIANTS for f in range(5)}
    development = {(d["variant"], d["fold"]): d for d in p["development"]}
    if len(p["development"]) != 10 or set(development) != contexts:
        raise ValueError("Development grid incomplete.")
    fits = []
    for d in development.values():
        reference, router = d["reference_development"], d["router"]
        if (reference["variant"], reference["fold"]) != (d["variant"], d["fold"]) or reference["role_counts"] != [9, 1, 2, 3]:
            raise ValueError("Historical role mismatch.")
        old._same(reference["temperature_supported_fraction"], reference["temperature_supported_n"] / reference["temperature_n"])
        if reference["temperature"] <= 0 or reference["temperature_fallback"] != (reference["temperature_supported_n"] == 0):
            raise ValueError("Temperature mismatch.")
        for rule, policies in d["policies"].items():
            if [x["target_percent"] for x in policies] != list(TARGETS):
                raise ValueError("Target grid mismatch.")
            for policy in policies: _validate_policy(policy)
            if rule in reference["policies"] and policies != reference["policies"][rule]:
                raise ValueError("Historical development policy mismatch.")
        blocks = d["crossfit"]["blocks"]
        if [b["block"] for b in blocks] != [0, 1, 2] or sum(b["held_n"] for b in blocks) != router["n"]:
            raise ValueError("Cross-fit partition mismatch.")
        if sum(b["correct_n"] for b in blocks) != router["correct_n"] or router["correct_n"] + router["incorrect_n"] != router["n"]:
            raise ValueError("Cross-fit correctness mismatch.")
        if abs(router["weight_sum"] - router["n"]) > 1e-8:
            raise ValueError("Question weights not normalized.")
        for b in blocks:
            if b["fitting_n"] + b["held_n"] != router["n"] or b["correct_n"] + b["incorrect_n"] != b["held_n"]:
                raise ValueError("Cross-fit row counts mismatch.")
            fits.append(b["fits"])
        fits.append(d["final_classifier_fits"])
        fallback = router["status"] == "CONSTANT_CORRECTNESS_FALLBACK"
        if fallback != (router["constant"] is not None) or router["fitting_calls"] != int(not fallback):
            raise ValueError("Router fallback mismatch.")
        if fallback and router["correct_n"] != router["constant"] * router["n"]:
            raise ValueError("Constant target mismatch.")
    for c in fits:
        if c["attempted"] != 10 or c["successful"] + c["failed"] != 10 or c["convergence_warnings"] > c["warnings"]:
            raise ValueError("Classifier fitting counts mismatch.")
    if p["provenance"]["classifier_fits"] != {k: sum(f[k] for f in fits) for k in FITS}:
        raise ValueError("Total fitting counts mismatch.")
    for key, value in (("router_fitting_calls", sum(d["router"]["fitting_calls"] for d in development.values())),
                       ("router_fallbacks", sum(d["router"]["constant"] is not None for d in development.values()))):
        if p["provenance"][key] != value: raise ValueError("Router total mismatch.")
    for phase, checks in p["reproduction"].items():
        if len(checks) != 10 or {(c["variant"], c["fold"]) for c in checks} != contexts:
            raise ValueError("Reproduction grid incomplete.")
        if phase == "development":
            for c in checks:
                if any(not 0 <= c[k] <= 1e-10 for k in ("temperature_absolute_difference", "inner_mean_map_at_3_absolute_difference")):
                    raise ValueError("Failed reproduction.")
    lookup = {}
    for row in p["records"]:
        d, target, policy = development[row["variant"], row["fold"]], row["target_percent"], row["policy"]
        expected = None if target is None else next(x for x in d["policies"][row["rule"]] if x["target_percent"] == target)
        if policy != expected:
            raise ValueError("Evaluation uses a different policy.")
        ev = row["evaluation"]
        old.validate_groups(ev["groups"], target)
        if len(ev["questions"]) != 3 or len({q["QuestionId"] for q in ev["questions"]}) != 3:
            raise ValueError("Evaluation question grid mismatch.")
        for q in ev["questions"]:
            old.validate_groups(q["groups"], target)
            risk = q["groups"]["all"]["risk"]
            devrisk = sum(x["risk"] for x in policy["development"]) / 2 if policy and policy["status"] == "SELECTED" else None
            old._same(q["risk_minus_development"], risk - devrisk if risk is not None and devrisk is not None else None)
        for s in STRATA:
            for key in ("original_n", "retained_n", "correct_n", "incorrect_n"):
                if sum(q["groups"][s][key] for q in ev["questions"]) != ev["groups"][s][key]:
                    raise ValueError("Question/fold count partition mismatch.")
        if policy is None and ev["groups"]["all"]["coverage"] != 1:
            raise ValueError("Unfiltered reference retained fewer rows.")
        if policy and policy["status"] == "NO_ADMISSIBLE_THRESHOLD" and ev["groups"]["all"]["retained_n"]:
            raise ValueError("Absent policy retained rows.")
        head = row["reliability"]
        if (head is not None) != (row["rule"] == "learned_reliability"):
            raise ValueError("Head diagnostics on wrong rule.")
        if head is not None:
            if [q["QuestionId"] for q in head["questions"]] != [q["QuestionId"] for q in ev["questions"]]:
                raise ValueError("Head question alignment mismatch.")
            for h, g in [(head["groups"], ev["groups"]), *[(a["groups"], b["groups"]) for a, b in zip(head["questions"], ev["questions"])]]:
                for s in STRATA: _check_binary(h[s], g[s], ("mean_predicted_correctness", "binary_brier", "binary_ece"))
        if target is None: lookup[row["variant"], row["fold"], row["rule"]] = ev
    for rank in p["ranking"]:
        ev = lookup[rank["variant"], rank["fold"], rank["rule"]]
        _check_binary(rank["all"], ev["groups"]["all"], ("auroc",))
        if [q["QuestionId"] for q in rank["questions"]] != [q["QuestionId"] for q in ev["questions"]]:
            raise ValueError("Ranking question alignment mismatch.")
        for a, b in zip(rank["questions"], ev["questions"]): _check_binary(a, b["groups"]["all"], ("auroc",))
        if rank["rule"] == "frequency":
            for a in [rank["all"], *rank["questions"]]:
                if a["auroc"] is not None and a["auroc"] != .5: raise ValueError("Constant frequency AUROC differs.")
    if aggregate(p["records"], p["ranking"]) != p["aggregate"]:
        raise ValueError("Aggregate arithmetic mismatch.")


def report(p):
    validate_public_payload(p)
    def n(x): return "null" if x is None else format(x, ".8g")
    def stat(v): return f"{n(v['mean'])} ± {n(v['sd'])} [{v['defined_folds']}]"
    lines = ["# E009 — learned-reliability results", "", "Status: **COMPLETED**. Numerical results only; interpretation and any next experiment await user review.", "",
        "Fixed classifier, nested question-held-out reliability training, and unchanged E007 outer folds/temperature/threshold criteria. Primary target 20%; secondary 10% and 30%. All uncertainty is descriptive on a repeatedly examined 15-question benchmark, not independent confirmation or a deployment guarantee.", "",
        "Equal-fold means ± sample SD [defined folds]. Null retained risk is undefined, not zero. Frequency repeats the same reference across arms. Comparisons at a common target may retain different populations/coverage.", "",
        "[Complete aggregate/fold/question/stratum JSON](../results/E009_aggregates.json) includes all five values for numeric fold summaries, original classifier calibration, separate reliability calibration, eligibility reasons, inner-block audit counts and reproduction checks.", "",
        "## Registered transfer criteria", "", "| Target | Arm | Rule | Admissible / 5 | Nonempty / 15 | Count floor / 15 | Coverage floor / 15 | Both floors / 15 | Risk met / 15 | Risk exceeded / nonempty | Max question risk | Criterion met |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for target in (20, 10, 30):
        for s in p["aggregate"]["summaries"]:
            if s["target_percent"] != target: continue
            lines.append(f"| {target}% | {s['variant']} | {s['rule']} | {s['admissible_folds']} | {s['nonempty_questions']} | {s['count_floor_questions']} | {s['coverage_floor_questions']} | {s['both_floors_questions']} | {s['risk_met_questions']} | {s['risk_exceeded_questions']} / {s['nonempty_questions']} | {n(s['maximum_question_risk'])} | {s['useful_transfer']} |")
    lines += ["", "## Aggregate all-case results", "", "| Arm | Rule | Target | Coverage | Accuracy | MAP@3 | Risk | Classifier ECE | Multiclass Brier |", "|---|---|---|---|---|---|---|---|---|"]
    for s in p["aggregate"]["summaries"]:
        g = s["groups"]["all"]
        lines.append(f"| {s['variant']} | {s['rule']} | {s['target_percent'] if s['target_percent'] is not None else 'Unfiltered'} | " + " | ".join(stat(g[k]) for k in ("coverage", "top1_accuracy", "map_at_3", "risk", "ece", "brier")) + " |")
    lines += ["", "## All fold-level results", "", "| Arm | Fold | Rule | Target | Cutoff | Retained / original | Coverage | Accuracy | MAP@3 | Risk | Classifier ECE | Multiclass Brier |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in p["records"]:
        g, policy = r["evaluation"]["groups"]["all"], r["policy"]
        cutoff = 'Unfiltered' if policy is None else 'NONE' if policy['threshold'] is None else format(policy['threshold'], '.17g')
        lines.append(f"| {r['variant']} | {r['fold']} | {r['rule']} | {r['target_percent'] if policy else 'Unfiltered'} | {cutoff} | {g['retained_n']} / {g['original_n']} | " + " | ".join(n(g[k]) for k in ("coverage", "top1_accuracy", "map_at_3", "risk", "ece", "brier")) + " |")
    lines += ["", "## All evaluation-question results", "", "| Arm | Fold | Question | Rule | Target | Retained / original | Coverage | Accuracy | MAP@3 | Risk | Risk minus target | Risk minus development | ECE | Brier |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in p["records"]:
        for q in r["evaluation"]["questions"]:
            g = q["groups"]["all"]
            values = [g[k] for k in ("coverage", "top1_accuracy", "map_at_3", "risk", "error_minus_target")] + [q['risk_minus_development'], g['ece'], g['brier']]
            lines.append(f"| {r['variant']} | {r['fold']} | {q['QuestionId']} | {r['rule']} | {r['target_percent'] if r['target_percent'] is not None else 'Unfiltered'} | {g['retained_n']} / {g['original_n']} | " + " | ".join(n(x) for x in values) + " |")
    lines += ["", "## Correctness discrimination — complete fold and question results", "", "Eligibility: n>=200, correct>=20, incorrect>=20. Frequency predicts a different correctness target and is contextual only.", "", "| Arm | Fold | Scope | Rule | n | Correct | Incorrect | AUROC | Ineligible reasons |", "|---|---|---|---|---|---|---|---|---|"]
    for r in p["ranking"]:
        for scope, g in [("All", r["all"]), *[(q["QuestionId"], q) for q in r["questions"]]]:
            lines.append(f"| {r['variant']} | {r['fold']} | {scope} | {r['rule']} | {g['n']} | {g['correct_n']} | {g['incorrect_n']} | {n(g['auroc'])} | {', '.join(g['ineligible_reasons']) or 'none'} |")
    lines += ["", "## AUROC fold summaries and paired differences", "", "| Arm | Rule / learned-minus-control | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |", "|---|---|---|---|---|---|---|---|"]
    for s in [*p["aggregate"]["ranking"], *p["aggregate"]["ranking_paired"]]:
        label = s['rule'] if 'rule' in s else 'learned minus ' + s['right']
        lines.append(f"| {s['variant']} | {label} | " + " | ".join(n(x) for x in s['fold_values']) + f" | {stat(s)} |")
    lines += ["", "## Paired policy differences at the same target", "", "| Arm | Target | Control | Fold | Learned coverage | Control coverage | Coverage difference | Risk difference |", "|---|---|---|---|---|---|---|---|"]
    for s in p["aggregate"]["paired"]:
        for f in s['folds']:
            lines.append(f"| {s['variant']} | {s['target_percent']}% | {s['right']} | {f['fold']} | " + " | ".join(n(f[k]) for k in ('left_coverage','right_coverage','coverage_difference','risk_difference')) + " |")
        lines.append(f"| {s['variant']} | {s['target_percent']}% | {s['right']} | Summary | — | — | {stat(s['coverage_difference'])} | {stat(s['risk_difference'])} |")
    lines += ["", "## Learned reliability calibration — all-case fold and question results", "", "These are correctness-probability diagnostics, not multiclass classifier calibration. All three statistics require the fixed eligibility counts. Full stratum values and reasons are in the JSON.", "", "| Arm | Fold | Scope | Target | n | Correct | Incorrect | Mean predicted correctness | Binary Brier | Binary ECE | Ineligible reasons |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in p['records']:
        h = r['reliability']
        if h is None: continue
        for scope, groups in [('All',h['groups']), *[(q['QuestionId'],q['groups']) for q in h['questions']]]:
            g=groups['all']
            lines.append(f"| {r['variant']} | {r['fold']} | {scope} | {r['target_percent'] if r['target_percent'] is not None else 'Unfiltered'} | {g['n']} | {g['correct_n']} | {g['incorrect_n']} | " + " | ".join(n(g[k]) for k in ('mean_predicted_correctness','binary_brier','binary_ece')) + f" | {', '.join(g['ineligible_reasons']) or 'none'} |")
    lines += ["", "## Complete numeric fold summaries (all registered strata)", "", "Five fold values, equal-fold mean, sample SD and eligible/defined count; undefined values are not imputed. These include support-stratum results even when no policy is admitted."]
    for s in p['aggregate']['summaries']:
        lines += ["", f"### {s['variant']} / {s['rule']} / {s['target_percent'] if s['target_percent'] is not None else 'Unfiltered'}", "", "| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |", "|---|---|---|---|---|---|---|"]
        for label, groups in [('classifier',s['groups']), ('reliability',s['reliability'])]:
            if groups is None: continue
            for group, metrics in groups.items():
                for metric,v in metrics.items():
                    lines.append(f"| {label}.{group}.{metric} | " + " | ".join(n(x) for x in v['fold_values']) + f" | {stat(v)} |")
    v=p['provenance']
    lines += ["", "## Execution", "", f"Runtime: {v['wall_seconds']:.3f} seconds. Pre-run revision: `{v['git_revision']}`. Historical development policies reproduced: 90/90; evaluation records reproduced: 120/120. Preserved files: {v['preserved_files']}. Classifier fits: {v['classifier_fits']['attempted']} attempted, {v['classifier_fits']['successful']} successful, {v['classifier_fits']['failed']} failed; warnings: {v['classifier_fits']['warnings']}, including {v['classifier_fits']['convergence_warnings']} convergence warnings. Reliability fits: {v['router_fitting_calls']}; constant fallbacks: {v['router_fallbacks']}.", "", "No raw responses, row-level features/predictions/scores, neighbor identifiers, candidate arrays, fitted coefficients or scaler statistics are serialized. No experiment interpretation is added to this numerical report.", ""]
    return '\n'.join(lines)


def publish(root):
    p = json.loads((root / 'artifacts/e009/results.json').read_text(encoding='utf-8'))
    validate_public_payload(p)
    contents = {root / 'results/E009_aggregates.json': json.dumps(p, indent=2, allow_nan=False) + '\n',
                root / 'docs/E009_RESULTS.md': report(p)}
    for path, content in contents.items():
        if path.exists() and path.read_text(encoding='utf-8') != content:
            raise ValueError('Refusing to overwrite different published results.')
    for path, content in contents.items():
        if not path.exists():
            with path.open('x', encoding='utf-8', newline='\n') as stream: stream.write(content)


if __name__ == '__main__':
    publish(Path(__file__).resolve().parents[2])
