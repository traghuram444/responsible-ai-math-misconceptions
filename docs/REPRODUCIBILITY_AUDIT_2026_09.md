# September 2026 reproducibility audit and metric erratum

Audit date: 2026-09-13. This is an append-only audit of the local E001–E005 record. It preserves the historical source, protocols, result artifacts, and negative results. The audit inspected code, aggregate artifacts, and split metadata; it did not rerun a scientific experiment or start E006. Tests for new corrective utilities are a separate verification step and were pending when this audit was written.

The findings below qualify the earlier completion and reproducibility claims. They do not change the historical MAP@3 results. Source line references identify the legacy files inspected during this audit.

## 1. Material metric error: Brier score for unsupported labels

**Severity: P1 — affects reported absolute Brier scores.**

The legacy `multiclass_brier` in `src/map_misconceptions/metrics.py:29–31` constructs one-hot targets only over the classifier's fitted classes. When the true exact label is absent from those classes, the target becomes all zero. A full-outcome-space Brier score must also include the unseen true class, whose predicted probability is zero and whose target is one.

For each prediction whose true label is unsupported:

```text
legacy Brier = sum over fitted classes of p(class)^2
full-outcome-space Brier = 1 + legacy Brier
```

Consequently, a group's corrected mean equals its legacy mean plus its unsupported-label fraction. This correction can be derived from existing aggregate counts; it does not require a model rerun or student text.

The distinction between aggregation schemes matters:

| Quantity | Value |
|---|---:|
| Unsupported grouped evaluation rows | 7,755 / 36,696 |
| Row-pooled unsupported fraction | 0.2113309353 |
| Unweighted mean of five fold unsupported fractions | 0.2133910443 |
| Historical frequency mean-fold Brier | 0.5816660930 |
| Corrected frequency mean-fold Brier | 0.7950571373 |

The historical experiment headline scores use unweighted fold means, so their Brier correction is **0.2133910443**, not the row-pooled fraction. Each per-fold or per-question correction must use that unit's own fraction.

MAP@3, top-1 accuracy, macro-F1, and ECE are unaffected by this bug. Supported-only exact-label Brier is also unaffected. For two models evaluated on the same rows with the same supported class set, the same Brier correction applies to each: their Brier difference and its descriptive bootstrap interval remain unchanged. This cancellation must not be assumed for E006 retained subsets, which can differ between routing rules.

Historical artifacts remain evidence of what was actually computed. Corrected scores must be published in a separately named, versioned erratum with source-artifact hashes, rather than replacing historical values in place. Future metric code must distinguish the legacy implementation from the corrected definition.

## 2. E005 random-reference inner-fold seed discrepancy

**Severity: P2 — protocol reproduction discrepancy without an observed overall metric difference.**

E001 uses `SEED + fold` for random-reference inner cross-validation (`src/map_misconceptions/e001.py:189`). E005 uses the same `SEED` in every random-reference inner split (`scripts/run_e005_decomposition.py:26`). Its outer random folds and train/calibration division still use the corresponding E001 rules (`run_e005_decomposition.py:46–48`).

The audit compared all **200** stored overall scalar metrics between E001 and final E005: five metrics, two models, five folds, two input arms, and two split regimes. Every compared value agreed within `1e-12`. Thus the seed discrepancy did not change these recorded outputs. E005 does not serialize selected hyperparameters, inner scores, temperature, or calibration support counts (`run_e005_decomposition.py:29–36`), so the artifact cannot establish that the intermediate fitting history was identical.

Record this discrepancy; do not silently edit E005 or regenerate its outputs and describe the replacement as the original run.

## 3. E005 calibration eligibility and incomplete reporting

**Severity: P2 — implementation and reporting do not fully match the written protocol.**

`docs/E005_PROTOCOL.md:47` defines calibration eligibility using at least 200 rows **pooled across folds**, with at least 20 correct and 20 incorrect predictions. The runner instead applies these checks separately inside each fold (`scripts/run_e005_decomposition.py:20–23,31`). It also serializes unconditionally computed ECE/Brier in each stratum's model summary, even when the adjacent eligibility object says `not_estimable`.

For the current grouped results, frequent and well-supported strata pass the checks in every fold; unsupported strata have zero correct predictions, and the rare stratum is empty. This limits the practical effect of the eligibility discrepancy on those particular reported tables. It does not make an average of fold ECE values a pooled ECE: ECE depends on bin-level counts and confidence/correctness totals that are absent from the artifact.

The finalizer serializes overall learned-minus-frequency MAP@3, ECE, and Brier bootstrap summaries (`scripts/finalize_e005_summaries.py:18–22`). It does not serialize comparable uncertainty summaries for Category, support strata, or the random-to-grouped comparisons. The original statistical reporting language is broader (`docs/E005_PROTOCOL.md:44–46`). E005's missing reporting is acknowledged here, rather than silently completed under a changed historical record. No additional E005 intervals or analyses were generated by this audit.

The 15-question Spearman/permutation summaries and the overall five-fold bootstrap summaries are present. They remain **descriptive**: five overlapping training-fold analyses and 15 questions do not support treating the resampling results as formal independent-sample inference.

## 4. E004 secondary outputs are incomplete

**Severity: P2 — primary negative result exists; not every preregistered secondary output exists.**

The E004 protocol lists per-question aggregates and the supported-label subset among its secondary metrics. `scripts/run_e004_embeddings.py:45,50` serializes fold/global metrics and risk–coverage points, but neither of those secondary decompositions. The existing aggregate artifact cannot recover them.

E004's primary negative result remains preserved. Earlier statements implying completion of every promised secondary analysis should be read with this qualification. This audit does not rerun E004 to fill the omissions.

## 5. Frozen split integrity is only partly authenticated

**Severity: P2 — current split checks pass, but historical identity is incompletely authenticated.**

The manifest stores the data hash and split-generation settings, but no assignment-file hash (`src/map_misconceptions/splits.py:78–90`). Runners consume positional assignment roles after checking the data hash; they do not authenticate the assignment CSV itself or validate its row/question mapping before fitting. Relevant examples are `src/map_misconceptions/e001.py:220–225` and `scripts/run_e005_decomposition.py:39–40`.

Read-only checks on the current assignment file found sequential `source_row` values and **zero QuestionId groups spanning multiple roles in every fold**. The current fingerprints are:

| Item | SHA-256 |
|---|---|
| Grouped assignment CSV | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |
| Grouped manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Final E005 aggregate artifact | `b69cda4fd8ce9d412da443d5d5728b16542fd3758ba195b34305b0e3069663e9` |

The assignment fingerprint records what is present at audit time. It is not an independently authenticated pre-run fingerprint of the original assignment file. Future checks can lock this preserved file and validate its roles without regenerating folds or claiming stronger historical evidence than exists.

The E005 grouped support counts were verified as 7,755 unsupported, zero rare, 28,941 frequent, and 28,187 well-supported rows. The code implements the specified 0 / 1–19 / at-least-20 support counts and the at-least-two-training-question condition (`run_e005_decomposition.py:17–19`).

## 6. Git and experiment-record provenance

**Severity: P2 — public history lagged local execution.**

At the start of this audit, the last local Git commit was E003 result commit `066cb28`. E004–E006 protocols and E004/E005 scripts were untracked; the local E005 protocol/config still said proposed, and the experiment log listed E005 as awaiting review while omitting E004. These are observations about the audit-start state, not a claim that they remain uncommitted after subsequent maintenance.

The conversation contains approvals and run reports. Existing local filesystem timestamps and the timestamps embedded in selected artifacts do not independently establish exact execution times or prospective Git registration. Future commits must truthfully describe these as recovered historical records and disclose that they were committed after execution. They must not backdate commits or imply an earlier public preregistration that the inspected Git history cannot establish.

## 7. Docker dependency pinning is partial

**Severity: P2 — reproducibility is useful but not fully hermetic.**

The Dockerfile pins its interpreter image digest (`Dockerfile:2`) and pip version (`Dockerfile:19`). It creates and runs as a non-root user. The listed dependencies use exact versions (`requirements.lock:2–22`). However, the lockfile does not constrain every transitive dependency or include package hashes. `pyproject.toml:2` allows any `setuptools>=68`; its runtime/dev declarations also use ranges (`pyproject.toml:10–16`). The editable install (`Dockerfile:21`) can resolve build dependencies independently of the pinned runtime list.

An existing local image was available during the audit:

```text
sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c
```

Availability of that image is not evidence of a successful fresh build from current package indexes. This audit makes no fresh-build or complete dependency-lock claim. A later environment verification should separately record resolved packages, build inputs, image identity, and its test results.

## 8. Limits on what the historical evidence can establish

- Temperature scaling excludes calibration rows whose exact label is absent from fitted classes (`src/map_misconceptions/e001.py:82–99`). Approximately 68.5%–89.7% of calibration rows participate across the five folds. Existing temperature calibration therefore cannot be assumed to guarantee calibration on unsupported evaluation labels.
- Neither registered text arm includes `MC_Answer` (`src/map_misconceptions/e001.py:32–37`; `scripts/run_e004_embeddings.py:17–19`). E004 also records no token-truncation diagnostics. The negative baselines do not isolate mathematical reasoning as the sole cause of transfer failure.
- Legacy `risk_coverage` uses `np.argsort(-confidence)` without the hashed tie rule proposed for E006 (`src/map_misconceptions/metrics.py:54`). Constant-confidence frequency predictions require an explicit reproducible tie rule for a useful no-information routing reference.
- The artifacts do not retain confidence/outcome pairs, ranking information, prediction/support joint counts, or calibration-bin sufficient statistics. They cannot support E006 confidence AUROC, new routing rules, retained support-stratum metrics, or retained calibration through aggregate postprocessing alone. Reproducing predictions in memory would be necessary for those analyses.
- Raw student text, row-level predictions, and the assignment CSV remain outside the publication output. This audit publishes only code references, aggregate counts, and fingerprints.

The historical field `macro_f1_all_eval_labels` invokes scikit-learn's default label union (observed truths and predictions), not an explicitly supplied evaluation-only label list. Category macro-F1 likewise was not passed an explicit six-label list. Preserve the field names in the archive, but do not interpret them as a differently specified estimand.

This document is a correction to the evidentiary record. E001–E005 remain intact; E006 has not been executed by this audit. The completed corrective-utility checks are recorded separately in [the verification record](VERIFICATION_2026_09.md), and the [metric erratum](METRIC_ERRATUM_2026_09.md) supplies the arithmetic correction tables.
