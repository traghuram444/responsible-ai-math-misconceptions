"""Export allowlisted historical aggregate fields; never load data or fit models.

The two source filenames and two destination filenames are fixed. Existing
destinations are accepted only when byte-identical to the deterministic export.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
from statistics import fmean, stdev


VARIANTS = ("explanation_only", "question_plus_explanation")
SCOPES = ("grouped_folds", "random_folds")
STRATA = ("unsupported", "rare", "frequent", "well_supported")
METRICS = (
    "top1_accuracy", "macro_f1_all_eval_labels", "map_at_3",
    "ece_10_equal_width", "multiclass_brier",
)
CATEGORY_METRICS = tuple(m for m in METRICS if m != "map_at_3")
LABELS = {
    "top1_accuracy": "Accuracy", "macro_f1_all_eval_labels": "Macro-F1",
    "map_at_3": "MAP@3", "ece_10_equal_width": "ECE",
    "multiclass_brier": "Brier (LEGACY)",
}
SCOPE_LABELS = {"grouped_folds": "Question-held-out", "random_folds": "Random"}
MODEL_LABELS = {
    "frequency_baseline": "Frequency", "tfidf_logreg": "TF-IDF",
    "embedding_logreg": "Embedding + logistic",
}


def number(value: object) -> float:
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError("Expected a finite numeric aggregate")
    return float(value)


def count(value: object) -> int:
    result = number(value)
    if result < 0 or not result.is_integer():
        raise ValueError("Expected a nonnegative integer count")
    return int(result)


def scalar(value: object) -> str:
    return f"{number(value):.6f}"


def mean_sd(values: list[object]) -> str:
    numeric = [number(value) for value in values if value is not None]
    if not numeric:
        return "Not estimable"
    sd = f"{stdev(numeric):.6f}" if len(numeric) > 1 else "undefined"
    return f"{fmean(numeric):.6f} +/- {sd}"


def digest(value: object) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        raise ValueError("Expected a SHA-256 digest")
    return value


def question_id(value: object) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]+", value):
        raise ValueError("Expected an aggregate QuestionId")
    return value


def sorted_folds(folds: list[dict]) -> list[dict]:
    if len(folds) != 5 or sorted(count(f["fold"]) for f in folds) != list(range(5)):
        raise ValueError("Expected exactly frozen fold IDs 0 through 4")
    return sorted(folds, key=lambda f: f["fold"])


def variants(data: dict) -> list[dict]:
    indexed = {item["variant"]: item for item in data["results"]}
    if len(data["results"]) != 2 or set(indexed) != set(VARIANTS):
        raise ValueError("Unexpected input variants")
    return [indexed[name] for name in VARIANTS]


def table(headers: list[str], rows: list[list[object]]) -> str:
    # Callers supply constant labels, allowlisted IDs, or formatted numbers only.
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        if len(row) != len(headers):
            raise ValueError("Table width mismatch")
        lines.append("| " + " | ".join(map(str, row)) + " |")
    return "\n".join(lines) + "\n"


def intro(experiment: str, source_sha: str, data: dict) -> list[str]:
    return [
        f"# {experiment} historical aggregate results archive\n",
        "Archive prepared on 2026-09-13 from the preserved completed result artifact. "
        "This is a retrospective publication of existing results, not a prospectively "
        "preregistered Git record. No models, bootstrap resamples, or permutations were run "
        "to produce this archive. E001-E005 source artifacts remain unchanged.\n",
        f"Source artifact SHA-256: `{digest(source_sha)}`.\n"
        f"Source data SHA-256: `{digest(data['input_sha256'])}`.\n",
        "**Metric status:** every Brier value below is **LEGACY**, retained verbatim or "
        "summarized from the historical implementation. It must not be interpreted as a "
        "validated corrected Brier score; see [metric erratum](METRIC_ERRATUM_2026_09.md).\n",
        "Numerical summaries use equal-weight fold means and sample standard deviation "
        "(denominator k - 1), formatted to six decimal places. Counts are summed across "
        "the five disjoint evaluation folds. Paired differences use learned minus frequency "
        "within each fold. The five folds have overlapping training sets; their variation "
        "and any archived intervals are descriptive, not formal inferential evidence.\n",
    ]


def aggregate_rows(folds: list[dict], models: tuple[str, ...], metrics=METRICS) -> list[list[object]]:
    rows = []
    for model in models:
        rows.append([MODEL_LABELS[model], sum(count(f[model]["n"]) for f in folds)] +
                    [mean_sd([f[model][metric] for f in folds]) for metric in metrics])
    return rows


def e004_report(data: dict, source_sha: str) -> str:
    if data["experiment_id"] != "E004":
        raise ValueError("Wrong E004 artifact")
    chunks = intro("E004", source_sha, data)
    chunks += [
        "Model: frozen all-MiniLM-L6-v2 embeddings followed by fold-local logistic "
        "regression. Both stored input arms are reported. These tables preserve the "
        "negative result without selecting an arm after seeing its performance.\n",
        "The source artifact does not contain per-question metrics, exact-label support "
        "strata, or frequency-baseline risk-coverage curves. Those missing outputs are "
        "not reconstructed or inferred here.\n",
    ]
    for variant in variants(data):
        folds = sorted_folds(variant["folds"])
        chunks.append(f"## {variant['variant']}\n")
        chunks.append("### Aggregate metrics (mean +/- sample SD)\n")
        chunks.append(table(["Model", "Evaluation n"] + [LABELS[m] for m in METRICS],
                            aggregate_rows(folds, ("frequency_baseline", "embedding_logreg"))))
        chunks.append(table(["Paired comparison"] + [LABELS[m] for m in METRICS],
                            [["Embedding minus frequency"] + [mean_sd([
                                number(f["embedding_logreg"][m]) - number(f["frequency_baseline"][m])
                                for f in folds]) for m in METRICS]]))
        chunks.append("### All five fold values\n")
        rows = []
        for fold in folds:
            for model in ("frequency_baseline", "embedding_logreg"):
                delta = number(fold[model]["map_at_3"]) - number(fold["frequency_baseline"]["map_at_3"])
                rows.append([count(fold["fold"]), MODEL_LABELS[model], count(fold[model]["n"])] +
                            [scalar(fold[model][m]) for m in METRICS] + [scalar(delta)])
        chunks.append(table(["Fold", "Model", "n"] + [LABELS[m] for m in METRICS] + ["MAP@3 delta"], rows))
        chunks.append("### Stored selective-prediction summaries\n")
        chunks.append("These are the original E004 routing values, not an E006 result. "
                      "Mean coverage, accuracy, and risk are equal-weight fold summaries.\n")
        rows = []
        fold_rows = []
        for index, budget in enumerate((0, 0.1, 0.2, 0.3, 0.4, 0.5)):
            points = [f["risk_coverage"][index] for f in folds]
            if any(number(p["human_review_rate"]) != budget for p in points):
                raise ValueError("Unexpected historical review budget")
            rows.append([f"{budget:.0%}", sum(count(p["ai_handled_n"]) for p in points)] +
                        [mean_sd([p[m] for p in points]) for m in
                         ("ai_coverage", "ai_handled_accuracy", "ai_handled_risk")])
            for fold, point in zip(folds, points):
                fold_rows.append([count(fold["fold"]), f"{budget:.0%}", count(point["ai_handled_n"])] +
                                 [scalar(point[m]) for m in ("ai_coverage", "ai_handled_accuracy", "ai_handled_risk")])
        chunks.append(table(["Review", "Retained n", "Coverage", "Accuracy", "Risk"], rows))
        chunks.append(table(["Fold", "Review", "Retained n", "Coverage", "Accuracy", "Risk"], fold_rows))
    return "\n".join(chunks)


def e005_report(data: dict, source_sha: str) -> str:
    if data["experiment_id"] != "E005":
        raise ValueError("Wrong E005 artifact")
    chunks = intro("E005", source_sha, data)
    chunks += [
        f"Frozen split-manifest SHA-256: `{digest(data['split_manifest_sha256'])}`.\n",
        "Support definitions are unchanged: unsupported = zero training examples; rare = "
        "1-19; frequent = at least 20; well-supported = at least 20 across at least two "
        "training questions. Well-supported is nested inside frequent and must not be "
        "added to the three mutually exclusive count strata.\n",
        "Random and grouped support subsets are defined from their respective fold-local "
        "training roles and can contain different examples. Their score difference is a "
        "comparison of those subsets, not a matched-row causal decomposition. Category "
        "probabilities were formed by summing exact-label probabilities in the original run.\n",
        "**Calibration eligibility:** the source execution applied the rule separately "
        "within each fold (at least 200 examples, 20 correct, and 20 incorrect), although "
        "the protocol described pooled eligibility. This archive preserves the executed "
        "foldwise results and flags the discrepancy; it does not claim pooled calibration "
        "or silently repair the implementation. In stratum tables, ECE/Brier are averaged "
        "only across the source's eligible folds; eligibility counts are shown. Unsupported "
        "exact labels cannot yield correct closed-set predictions and are ineligible.\n",
    ]
    for variant in variants(data):
        chunks.append(f"## {variant['variant']}\n")
        for scope in SCOPES:
            folds = sorted_folds(variant[scope])
            chunks.append(f"### {SCOPE_LABELS[scope]}: all-row exact-label performance\n")
            chunks.append(table(["Model", "Evaluation n"] + [LABELS[m] for m in METRICS],
                                aggregate_rows(folds, ("frequency_baseline", "tfidf_logreg"))))
            chunks.append("### All-row fold values\n")
            rows = []
            for fold in folds:
                for model in ("frequency_baseline", "tfidf_logreg"):
                    rows.append([count(fold["fold"]), MODEL_LABELS[model], count(fold[model]["n"])] +
                                [scalar(fold[model][m]) for m in METRICS] + [scalar(
                                    number(fold[model]["map_at_3"]) - number(fold["frequency_baseline"]["map_at_3"]))])
            chunks.append(table(["Fold", "Model", "n"] + [LABELS[m] for m in METRICS] + ["MAP@3 delta"], rows))
            chunks.append("### Exact-label support strata\n")
            rows, fold_rows = [], []
            for stratum in STRATA:
                groups = [f["strata"][stratum] for f in folds]
                for model in ("frequency_baseline", "tfidf_logreg"):
                    present = [g[model] for g in groups if g[model] is not None]
                    eligible = [g["calibration"][model] for g in groups
                                if "ece_10_equal_width" in g["calibration"][model]]
                    rows.append([stratum, MODEL_LABELS[model], sum(count(g["n"]) for g in groups), len(present)] +
                                [mean_sd([p[m] for p in present]) for m in METRICS[:3]] +
                                [len(eligible), sum(count(p["n"]) for p in eligible)] +
                                [mean_sd([p[m] for p in eligible]) for m in METRICS[3:]])
                    for fold, group in zip(folds, groups):
                        metric_row = group[model]
                        cal = group["calibration"][model]
                        fold_rows.append([count(fold["fold"]), stratum, MODEL_LABELS[model], count(group["n"])] +
                                         [scalar(metric_row[m]) if metric_row else "Not estimable" for m in METRICS[:3]] +
                                         [scalar(cal[m]) if m in cal else "Not estimable" for m in METRICS[3:]])
            chunks.append(table(["Stratum", "Model", "n", "Nonempty folds"] + [LABELS[m] for m in METRICS[:3]] +
                                ["Eligible calibration folds", "Eligible calibration n"] + [LABELS[m] for m in METRICS[3:]], rows))
            chunks.append("### Support-stratum fold values\n")
            chunks.append(table(["Fold", "Stratum", "Model", "n"] + [LABELS[m] for m in METRICS], fold_rows))
            chunks.append("### Six-way Category: aggregate and fold values\n")
            cats = [f["category"] for f in folds]
            chunks.append(table(["Model", "n"] + [LABELS[m] for m in CATEGORY_METRICS],
                                aggregate_rows(cats, ("frequency_baseline", "tfidf_logreg"), CATEGORY_METRICS)))
            rows = []
            for fold in folds:
                for model in ("frequency_baseline", "tfidf_logreg"):
                    result = fold["category"][model]
                    rows.append([count(fold["fold"]), MODEL_LABELS[model], count(result["n"])] +
                                [scalar(result[m]) for m in CATEGORY_METRICS])
            chunks.append(table(["Fold", "Model", "n"] + [LABELS[m] for m in CATEGORY_METRICS], rows))
        chunks.append("### Random minus grouped MAP@3: all rows and well-supported subset\n")
        rows = []
        for subset in ("all", "well_supported"):
            for model in ("frequency_baseline", "tfidf_logreg"):
                metrics = {}
                counts = {}
                for scope in SCOPES:
                    fs = sorted_folds(variant[scope])
                    entries = [f[model] if subset == "all" else f["strata"][subset][model] for f in fs]
                    metrics[scope] = [number(e["map_at_3"]) for e in entries]
                    counts[scope] = sum(count(e["n"]) for e in entries)
                rows.append([subset, MODEL_LABELS[model], counts["random_folds"], counts["grouped_folds"],
                             mean_sd(metrics["random_folds"]), mean_sd(metrics["grouped_folds"]),
                             scalar(fmean(metrics["random_folds"]) - fmean(metrics["grouped_folds"]))])
        chunks.append(table(["Subset", "Model", "Random n", "Grouped n", "Random MAP@3", "Grouped MAP@3", "Random - grouped"], rows))
        chunks.append("### All 15 held-out questions: stored support and performance\n")
        questions = [(f["fold"], q) for f in sorted_folds(variant["grouped_folds"]) for q in f["per_question"]]
        if len(questions) != 15 or len({question_id(q["QuestionId"]) for _, q in questions}) != 15:
            raise ValueError("Expected 15 unique held-out aggregate questions")
        rows = []
        for fold, q in sorted(questions, key=lambda item: int(question_id(item[1]["QuestionId"]))):
            rows.append([question_id(q["QuestionId"]), count(fold), count(q["n"]),
                         scalar(q["supported_row_share"]), scalar(q["well_supported_row_share"]),
                         scalar(q["frequency_baseline"]["map_at_3"]), scalar(q["tfidf_logreg"]["map_at_3"])])
        chunks.append(table(["QuestionId", "Fold", "n", "Supported share", "Well-supported share", "Frequency MAP@3", "TF-IDF MAP@3"], rows))
    chunks.append("## Existing descriptive uncertainty summaries\n")
    chunks.append("The intervals and permutation results below are copied from the finalized "
                  "artifact, with no new random draws. Bootstrap intervals describe five-fold "
                  "resampling only. Question associations use 15 questions and have low power; "
                  "the stored two-sided permutation values are descriptive, not formal evidence.\n")
    summaries = data["preregistered_descriptive_summaries"]
    chunks.append(f"Stored seed: `{count(summaries['seed'])}`.\n")
    for item in variants(summaries):
        chunks.append(f"### {item['variant']}: TF-IDF minus frequency\n")
        rows = []
        for scope in SCOPES:
            for metric in ("map_at_3", "ece_10_equal_width", "multiclass_brier"):
                result = item["comparisons"][scope][metric]
                if len(result["fold_values"]) != 5 or len(result["descriptive_bootstrap_95_interval"]) != 2:
                    raise ValueError("Unexpected stored uncertainty dimensions")
                rows.append([SCOPE_LABELS[scope], LABELS[metric], scalar(result["mean"]),
                             "[" + ", ".join(scalar(x) for x in result["descriptive_bootstrap_95_interval"]) + "]",
                             count(result["bootstrap_replicates"])] + [scalar(x) for x in result["fold_values"]])
        chunks.append(table(["Split", "Metric", "Stored mean delta", "Stored 95% descriptive interval", "Resamples"] +
                            [f"Fold {i} delta" for i in range(5)], rows))
        rows = []
        for model in ("frequency_baseline", "tfidf_logreg"):
            result = item["per_question_association"][model]
            rows.append([MODEL_LABELS[model], count(result["n_questions"]), scalar(result["spearman_rho"]),
                         scalar(result["permutation_two_sided_p"]), count(result["permutations"])])
        chunks.append(table(["Model", "Questions", "Spearman rho", "Stored two-sided permutation value", "Permutations"], rows))
    chunks.append("The source serializes bootstrap intervals for all-row learned-minus-frequency "
                  "MAP@3, ECE, and LEGACY Brier only. It contains no bootstrap intervals for "
                  "stratum, Category, or random-minus-grouped comparisons; this archive does "
                  "not create or imply those missing intervals.\n")
    return "\n".join(chunks)


def publish_new_or_identical(destination: Path, payload: bytes, check: bool) -> None:
    if destination.exists():
        if destination.read_bytes() != payload:
            raise ValueError(f"Refusing to overwrite non-identical archive: {destination.name}")
        return
    if check:
        raise ValueError(f"Archive missing: {destination.name}")
    with destination.open("xb") as stream:
        stream.write(payload)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="Check identical exports without writing")
    args = parser.parse_args()
    root = args.project_root.resolve(strict=True)
    jobs = (
        ("e004_results.json", "E004_RESULTS_ARCHIVE.md", e004_report),
        ("e005_results_final.json", "E005_RESULTS_ARCHIVE.md", e005_report),
    )
    pending = []
    for source_name, destination_name, renderer in jobs:
        source = root / "artifacts" / source_name
        raw = source.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        payload = renderer(json.loads(raw), sha).encode("utf-8")
        destination = root / "docs" / destination_name
        # Validate both existing destinations before creating either output.
        if destination.exists() and destination.read_bytes() != payload:
            raise ValueError(f"Refusing non-identical archive: {destination.name}")
        pending.append((destination, payload, source, sha))
    for destination, payload, source, sha in pending:
        publish_new_or_identical(destination, payload, args.check)
        if hashlib.sha256(source.read_bytes()).hexdigest() != sha:
            raise ValueError("Source artifact changed during archive export")
        print(f"Verified {destination.name}: {len(payload)} bytes; SHA-256 {hashlib.sha256(payload).hexdigest()}")


if __name__ == "__main__":
    main()
