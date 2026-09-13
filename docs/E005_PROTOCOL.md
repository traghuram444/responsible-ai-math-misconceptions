# E005 preregistration — question-held-out transferability decomposition

**Status:** proposed; awaiting review. E005 will not train a new model or alter E001–E004.

## Purpose and research questions

E005 diagnoses where transfer fails under the existing frozen five-fold `QuestionId` protocol. It asks:

1. Does the six-way `Category` target transfer to unseen questions better than the exact combined `Category:Misconception` target?
2. How do frequency and learned models behave when the exact target is frequent, rare, or absent in the fold-local training role?
3. Does per-question performance covary with train-label support?
4. After restricting evaluation to well-supported exact labels, how much of the random-versus-question-held-out collapse remains?
5. Is confidence/calibration useful within the predeclared support strata?

## Fixed data, models, and splits

- Reuse the E001 frozen manifest, outer folds, train/calibration/evaluation roles, seed, and data fingerprint exactly.
- Reproduce the E001 frequency and TF–IDF + logistic-regression baselines in both registered input arms. No E004 embedding rerun is required for the confirmatory analysis; it remains a preserved negative result.
- Keep E001 inner-only hyperparameter selection and group-disjoint temperature scaling unchanged.
- The primary all-row exact-target scores remain unchanged reference results; no E005 subset becomes a replacement primary score.

## Predeclared decomposition groups

For each outer fold, define exact-target support using only the fold's **train** role:

| Stratum | Definition |
|---|---|
| Unsupported | Exact `Category:Misconception` label occurs 0 times in train. |
| Rare | Label occurs 1–19 times in train. |
| Frequent | Label occurs at least 20 times in train. |
| Well-supported | Label occurs at least 20 times **and** at least two distinct training `QuestionId` groups. |

The 20-count threshold and two-question requirement are fixed before E005 execution. Every evaluation row belongs to exactly one support-count stratum; well-supported is a nested diagnostic subset of frequent labels.

## Confirmatory analyses

1. **Exact target:** frequency versus TF–IDF MAP@3, top-1 accuracy, macro-F1, ECE, and Brier overall and in Unsupported/Rare/Frequent strata where metrics are mathematically defined.
2. **Category target:** collapse model probabilities from exact labels to the six `Category` values by summing class probabilities, then report category top-1, macro-F1, ECE, and Brier. No model is retrained for category.
3. **Transfer collapse:** report random-reference versus question-held-out MAP@3 for all rows and the Well-supported subset; report absolute deltas, not ratios.
4. **Per-question relation:** report each held-out question's metrics, support-stratum composition, and a Spearman correlation across the 15 questions between supported-row share and performance. Treat the 15 questions—not rows—as the independent units.

## Statistical and uncertainty reporting

- Report all five outer-fold values, mean, standard deviation, and paired fold-level difference (learned minus frequency).
- Use a nonparametric bootstrap over the five outer folds only to give an interval for mean differences; label it descriptive because five groups provide low precision.
- For per-question association, report Spearman rho and an exact/permutation two-sided p-value over the 15 questions, with a strong low-power caveat.
- Calibration is reported only for strata with at least 200 evaluation rows pooled across folds and at least 20 correct and 20 incorrect predictions; otherwise report sample size and mark calibration not estimable.

## Safeguards against post-hoc subgroup selection

- All thresholds, strata, metrics, folds, models, and aggregation rules above are fixed before execution.
- No analysis may add, merge, remove, or relabel a stratum after results are observed.
- No E005 result may alter E001–E004 hyperparameters, folds, calibration, or target.
- Aggregate tables only: no student text, row-level probabilities, predictions, or error examples are retained or published.

## Interpretation map

| Outcome | Meaning |
|---|---|
| Category transfers materially better than exact target | The main barrier is fine-grained misconception taxonomy transfer, not necessarily broad correctness/category reasoning. |
| Category also fails | The problem likely requires question-conditioned mathematical reasoning or has broader distribution shift. |
| Well-supported restriction closes most of the random/grouped gap | Label support is a major source of the apparent generalization failure. |
| Large gap remains among well-supported labels | The failure is not primarily an open-label problem; item-conditioned reasoning or semantic heterogeneity remains central. |
| Frequency wins across strata | Learned models are not extracting transferable signal beyond stable prevalence. |
| Learned model wins only frequent/well-supported strata | Closed-set representation works only under strong label support; report this as a constrained diagnostic, not general transfer. |
| Calibration fails within supported strata | Deferral confidence is unreliable even after removing unsupported-label cases. |

## Confirmatory versus exploratory boundary

The listed strata, exact/category decomposition, collapse comparison, per-question correlation, and calibration eligibility rule are **confirmatory**. Any additional threshold, label regrouping, confusion narrative, model comparison, or text-based error audit is **exploratory** and must be separately preregistered before publication or model decisions.
