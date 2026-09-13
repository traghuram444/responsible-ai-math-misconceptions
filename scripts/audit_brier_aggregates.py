"""Append-only Brier erratum derived from stored aggregates, with no model run.

Outputs are new audit files. Historical experiment artifacts are never rewritten.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from statistics import mean, stdev


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new_or_identical(path, content):
    if path.exists() and path.read_text(encoding="utf-8") != content:
        raise FileExistsError("Audit output already exists with different contents.")
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main():
    root = Path(__file__).resolve().parents[1]
    artifacts = root / "artifacts"
    names = ["e001_results.json", "e004_results.json", "e005_results_final.json"]
    sources = {name: read(artifacts / name) for name in names}
    first = sources[names[0]]
    fourth = sources[names[1]]
    fifth = sources[names[2]]
    fifth_index = {v["variant"]: v for v in fifth["results"]}
    rows = []
    comparisons_checked = 0
    metrics = ["map_at_3", "top1_accuracy", "macro_f1_all_eval_labels",
               "ece_10_equal_width", "multiclass_brier"]

    def append(experiment, split, variant, fold, model, legacy, rate):
        rows.append({"experiment": experiment, "split": split, "variant": variant,
                     "fold": fold, "model": model, "legacy_multiclass_brier": legacy,
                     "unsupported_true_label_share": rate,
                     "union_label_brier": legacy + rate})

    for result in first["results"]:
        scope = "grouped_folds" if result["split"] == "QuestionId-grouped" else "random_folds"
        # Reject unexpected split names instead of silently mapping them.
        if result["split"] not in {"QuestionId-grouped", "stratified-random-reference-only"}:
            raise ValueError("Unexpected historical split name.")
        fifth_folds = {f["fold"]: f for f in fifth_index[result["variant"]][scope]}
        for f in result["folds"]:
            other = fifth_folds[f["fold"]]
            rate = other["strata"]["unsupported"]["n"] / other["n_evaluation"]
            if ("unsupported_evaluation_label_rate" in f
                    and abs(rate - f["unsupported_evaluation_label_rate"]) > 1e-12):
                raise ValueError("Unsupported fractions do not agree across historical artifacts.")
            for model in ("frequency_baseline", "tfidf_logreg"):
                for metric in metrics:
                    if abs(f[model][metric] - other[model][metric]) > 1e-12:
                        raise ValueError("E001/E005 overall metrics fail reproduction check.")
                    comparisons_checked += 1
                for experiment, item in (("E001", f), ("E005", other)):
                    append(experiment, result["split"], result["variant"], f["fold"], model,
                           item[model]["multiclass_brier"], rate)
    for result in fourth["results"]:
        fifth_folds = {f["fold"]: f for f in fifth_index[result["variant"]]["grouped_folds"]}
        for f in result["folds"]:
            other = fifth_folds[f["fold"]]
            rate = other["strata"]["unsupported"]["n"] / other["n_evaluation"]
            for metric in metrics:
                if abs(f["frequency_baseline"][metric] - other["frequency_baseline"][metric]) > 1e-12:
                    raise ValueError("E004 frequency does not reproduce the same fold.")
            for model in ("frequency_baseline", "embedding_logreg"):
                append("E004", "QuestionId-grouped", result["variant"], f["fold"], model,
                       f[model]["multiclass_brier"], rate)
    keys = sorted({(r["experiment"], r["split"], r["variant"], r["model"]) for r in rows})
    aggregates = []
    for key in keys:
        subset = [r for r in rows if tuple(r[k] for k in ("experiment", "split", "variant", "model")) == key]
        if len(subset) != 5:
            raise ValueError("Expected exactly five folds per aggregate.")
        record = dict(zip(("experiment", "split", "variant", "model"), key, strict=True))
        for metric in ("legacy_multiclass_brier", "unsupported_true_label_share", "union_label_brier"):
            record[metric] = {"mean": mean(r[metric] for r in subset), "sample_sd": stdev(r[metric] for r in subset)}
        aggregates.append(record)
    out = {"audit_id": "BRIER_ERRATUM_2026_09_13", "is_new_experiment": False,
           "source_sha256": {name: sha(artifacts / name) for name in names},
           "e001_e005_scalar_metrics_matching_1e_minus12": comparisons_checked,
           "formula": "union_label_brier = legacy_multiclass_brier + unsupported_true_label_share",
           "aggregation": "equal-weight five-fold mean and sample SD, not row-pooled",
           "folds": rows, "aggregates": aggregates}
    report = ["# Historical Brier metric erratum — 2026-09-13", "",
              "This is an **append-only arithmetic correction**, not a new experiment or a rerun. "
              "E001–E005 original files remain unchanged. Values below are equal-weight five-fold means.", "",
              "## Error and effect", "",
              "The original scorer omitted the one-hot true-label contribution when that label was absent "
              "from the model's class set. Proper multiclass Brier (sum over outcome labels, range 0–2) equals "
              "the legacy score **plus the unsupported true-label fraction**. See `metrics_v2.py` and its synthetic tests.", "",
              "MAP@3, top-1 accuracy and ECE are unaffected. Brier on supported-only subsets is unaffected. "
              "Same-fold learned-minus-frequency Brier differences cancel the correction when evaluated on "
              "the same population/class support. That cancellation need not hold for differently retained "
              "subsets in E006. Neither score is a pure measure of calibration alone.", "",
              "## All-row correction tables", "",
              "| Experiment | Split | Input | Model | Legacy Brier | Added unsupported share | Corrected Brier | Corrected SD |",
              "|---|---|---|---|---:|---:|---:|---:|"]
    for r in aggregates:
        report.append(f"| {r['experiment']} | {r['split']} | {r['variant']} | {r['model']} | "
                      f"{r['legacy_multiclass_brier']['mean']:.6f} | {r['unsupported_true_label_share']['mean']:.6f} | "
                      f"{r['union_label_brier']['mean']:.6f} | {r['union_label_brier']['sample_sd']:.6f} |")
    report += ["", "## Fold-level arithmetic", "",
               "E001 and E005 corresponding overall values agree within 1e-12 in all 200 checked scalar "
               "metrics. Their duplicated corrections are serialized locally; the E001 and E004 fold rows are shown here.", "",
               "| Experiment | Split | Input | Fold | Model | Legacy | Added share | Corrected |",
               "|---|---|---|---:|---|---:|---:|---:|"]
    for r in rows:
        if r["experiment"] != "E005":
            report.append(f"| {r['experiment']} | {r['split']} | {r['variant']} | {r['fold']} | {r['model']} | "
                          f"{r['legacy_multiclass_brier']:.6f} | {r['unsupported_true_label_share']:.6f} | {r['union_label_brier']:.6f} |")
    report += ["", "## Scope and provenance", "",
               "The mean-fold grouped correction is 0.213391; the pooled row fraction is 7755/36696 = "
               "0.211331. Using the latter to correct an equal-fold mean would be incorrect. E003's "
               "all-row references reproduce E001; its supported-only Brier needs no correction. "
               "E002 contains no classifier Brier. No correction is inferred for an unrecorded retained "
               "subset; that requires its own unsupported share.", "",
               "The historical E001 prose also reports explanation-only grouped Brier as 0.605; "
               "its serialized legacy value is 0.619925. The table above uses the artifact, not that prose typo.", "",
               "Reproduce with `python scripts/audit_brier_aggregates.py` from the existing local artifacts. "
               "The new ignored JSON is `artifacts/brier_erratum_2026_09.json`. No raw examples or row-level "
               "predictions are read or written. This table does not fill missing E004/E005 preregistered analyses. "
               "See [the full audit](REPRODUCIBILITY_AUDIT_2026_09.md).", ""]
    for name, digest in out["source_sha256"].items():
        report.append(f"- `{name}`: `{digest}`")
    report.append("")
    write_new_or_identical(artifacts / "brier_erratum_2026_09.json", json.dumps(out, indent=2) + "\n")
    write_new_or_identical(root / "docs" / "METRIC_ERRATUM_2026_09.md", "\n".join(report))
    print(json.dumps({"status": "audit_written", "matching_scalar_metrics": comparisons_checked,
                      "aggregate_records": len(aggregates), "model_runs": 0}))


if __name__ == "__main__":
    main()
