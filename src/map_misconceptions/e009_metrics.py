"""E009 registered metrics; original classifier evaluation remains unchanged."""
from __future__ import annotations

import numpy as np
from sklearn.metrics import roc_auc_score

from .e009_reliability import RULES, VARIANTS
from .metrics import expected_calibration_error
from .threshold_transfer import (METRICS, STRATA, TARGETS, apply_cutoff, canonical_question,
                                 evaluate_policy, mean_sd, support_masks)

HEAD_METRICS = ("n", "correct_n", "incorrect_n", "mean_predicted_correctness", "binary_brier", "binary_ece")


def eligibility(correct):
    n, c = len(correct), int(np.asarray(correct).sum())
    return (["n_below_200"] if n < 200 else []) + (["correct_below_20"] if c < 20 else []) + (["incorrect_below_20"] if n - c < 20 else [])


def correctness_auc(score, correct):
    score, correct = np.asarray(score), np.asarray(correct)
    reasons = eligibility(correct)
    return {"n": len(correct), "correct_n": int(correct.sum()), "incorrect_n": int((~correct).sum()),
            "auroc": float(roc_auc_score(correct, score)) if not reasons else None,
            "ineligible_reasons": reasons}


def head_summary(score, correct):
    reasons = eligibility(correct)
    return {"n": len(correct), "correct_n": int(correct.sum()), "incorrect_n": int((~correct).sum()),
            "mean_predicted_correctness": float(np.mean(score)) if not reasons else None,
            "binary_brier": float(np.mean((score - correct.astype(float)) ** 2)) if not reasons else None,
            "binary_ece": expected_calibration_error(score, correct, 10) if not reasons else None,
            "ineligible_reasons": reasons}


def evaluate_head(truth, prob, classes, train_labels, train_questions, questions, score, policy):
    retained = np.ones(len(truth), bool) if policy is None else apply_cutoff(score, policy)
    correct = classes[np.argmax(prob, axis=1)] == truth
    masks = support_masks(truth, train_labels, train_questions)
    def scoped(scope):
        return {name: head_summary(score[retained & scope & mask], correct[retained & scope & mask]) for name, mask in masks.items()}
    return {"groups": scoped(np.ones(len(truth), bool)), "questions": [
        {"QuestionId": canonical_question(q), "groups": scoped(questions == q)} for q in sorted(set(questions.tolist()))]}


def evaluate_fold(description, memory, truth):
    records, ranking = [], []
    for rule in RULES:
        p, c = ((memory["frequency_prob"], memory["frequency_classes"]) if rule == "frequency"
                else (memory["learned_prob"], memory["classes"]))
        score, questions = memory["scores"][rule], memory["evaluation_questions"]
        correct = c[p.argmax(axis=1)] == truth
        ranking.append({"variant": description["variant"], "fold": description["fold"], "rule": rule,
                        "all": correctness_auc(score, correct), "questions": [
                            {"QuestionId": canonical_question(q), **correctness_auc(score[questions == q], correct[questions == q])}
                            for q in sorted(set(questions.tolist()))]})
        for policy in (None, *description["policies"][rule]):
            evaluation = evaluate_policy(truth, p, c, memory["train_labels"], memory["train_questions"], questions, score, policy)
            head = (evaluate_head(truth, p, c, memory["train_labels"], memory["train_questions"], questions, score, policy)
                    if rule == "learned_reliability" else None)
            records.append({"variant": description["variant"], "fold": description["fold"], "rule": rule,
                            "target_percent": None if policy is None else policy["target_percent"],
                            "policy": policy, "evaluation": evaluation, "reliability": head})
    return records, ranking


def stat(values):
    return {**mean_sd(values), "fold_values": values}


def aggregate(records, ranking):
    if len(records) != 200 or len(ranking) != 50:
        raise ValueError("Incomplete E009 grid.")
    lookup = {(r["variant"], r["rule"], r["target_percent"], r["fold"]): r for r in records}
    ranks = {(r["variant"], r["rule"], r["fold"]): r for r in ranking}
    if len(lookup) != 200 or len(ranks) != 50:
        raise ValueError("Duplicate E009 records.")
    summaries, paired, auc, auc_paired = [], [], [], []
    for variant in VARIANTS:
        for rule in RULES:
            rr = [ranks[variant, rule, f] for f in range(5)]
            auc.append({"variant": variant, "rule": rule, **stat([r["all"]["auroc"] for r in rr])})
            for target in (None, *TARGETS):
                rows = [lookup[variant, rule, target, f] for f in range(5)]
                questions = [q for r in rows for q in r["evaluation"]["questions"]]
                if len(questions) != 15 or len({q["QuestionId"] for q in questions}) != 15:
                    raise ValueError("Question grid differs from frozen evaluation.")
                allq = [q["groups"]["all"] for q in questions]
                admitted = sum(r["policy"] is not None and r["policy"]["status"] == "SELECTED" for r in rows)
                both = sum(q["count_floor_met"] and q["coverage_floor_met"] for q in allq)
                risk_met = sum(q["risk_target_met"] is True for q in allq)
                head = ({s: {m: stat([r["reliability"]["groups"][s][m] for r in rows]) for m in HEAD_METRICS} for s in STRATA}
                        if rule == "learned_reliability" else None)
                summaries.append({"variant": variant, "rule": rule, "target_percent": target,
                    "groups": {s: {m: stat([r["evaluation"]["groups"][s][m] for r in rows]) for m in METRICS} for s in STRATA},
                    "reliability": head, "admissible_folds": admitted if target is not None else None,
                    "nonempty_questions": sum(q["retained_n"] > 0 for q in allq),
                    "count_floor_questions": sum(q["count_floor_met"] for q in allq),
                    "coverage_floor_questions": sum(q["coverage_floor_met"] for q in allq),
                    "both_floors_questions": both, "risk_met_questions": risk_met if target else None,
                    "risk_exceeded_questions": sum(q["target_exceeded"] is True for q in allq) if target else None,
                    "maximum_question_risk": max((q["risk"] for q in allq if q["risk"] is not None), default=None),
                    "useful_transfer": bool(admitted == 5 and both == 15 and risk_met == 15) if target else None})
        for right in ("confidence_only", "raw_confidence", "support_aware", "frequency"):
            for target in TARGETS:
                folds = []
                for fold in range(5):
                    leftg = lookup[variant, "learned_reliability", target, fold]["evaluation"]["groups"]["all"]
                    rightg = lookup[variant, right, target, fold]["evaluation"]["groups"]["all"]
                    folds.append({"fold": fold, "left_coverage": leftg["coverage"], "right_coverage": rightg["coverage"],
                                  "coverage_difference": leftg["coverage"] - rightg["coverage"],
                                  "risk_difference": leftg["risk"] - rightg["risk"] if leftg["risk"] is not None and rightg["risk"] is not None else None})
                paired.append({"variant": variant, "target_percent": target, "left": "learned_reliability", "right": right,
                               "folds": folds, "coverage_difference": stat([f["coverage_difference"] for f in folds]),
                               "risk_difference": stat([f["risk_difference"] for f in folds])})
            if right != "frequency":
                differences = []
                for fold in range(5):
                    lefta, righta = ranks[variant, "learned_reliability", fold]["all"]["auroc"], ranks[variant, right, fold]["all"]["auroc"]
                    differences.append(lefta - righta if lefta is not None and righta is not None else None)
                auc_paired.append({"variant": variant, "left": "learned_reliability", "right": right, **stat(differences)})
    # Duplicate frequency references must not create extra evidence.
    for fold in range(5):
        for target in (None, *TARGETS):
            a, b = (lookup[v, "frequency", target, fold] for v in VARIANTS)
            if {k: x for k, x in a.items() if k != "variant"} != {k: x for k, x in b.items() if k != "variant"}:
                raise ValueError("Frequency arms differ.")
    return {"summaries": summaries, "paired": paired, "ranking": auc, "ranking_paired": auc_paired}
