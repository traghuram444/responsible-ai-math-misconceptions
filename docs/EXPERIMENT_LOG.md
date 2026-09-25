# Experiment log

This log is append-only in spirit: completed negative results remain visible. E001 was completed before the repository's first public Git commit; that fact is recorded rather than retroactively assigning it a revision.

| ID | Date | Hypothesis | Split/data fingerprint | Model | Result | Decision |
|---|---|---|---|---|---|---|
| E001 | 2026-08-31 | TF–IDF + logistic regression exceeds frequency baseline under grouped evaluation. | MAP author release `0a5e…686c`; grouped manifest `93a2…7b94`; seed 20260831 | Frequency; TF–IDF + multinomial LR | Grouped MAP@3: 0.539 frequency vs 0.497 explanation-only / 0.520 question+explanation LR. Random reference: 0.764 / 0.785. | Stop TF–IDF branch; no transformer. Preserve as negative result. |
| E002 | 2026-08-31 | Fold-local label support is non-zero, while cross-question exact/near text overlap is low enough that E001's gap cannot be dismissed as response reuse. | Same frozen MAP grouped manifest as E001; train role only compared to evaluation role. | Aggregate support + exact-match + fixed character-TF–IDF nearest-neighbor diagnostic; no classifier. | 21.1% of held-out rows had a label absent from fold-local train; exact overlap 0.59%; mean rate with similarity ≥0.95 was 0.88%. | Preserve E001. E003 must decompose supported versus unsupported-label results without changing the primary all-row score. |
| E003 | 2026-08-31 | Scores improve on fold-supported labels, but the original all-row lexical-baseline decision remains unchanged. | Same frozen grouped manifest, E001 roles, variants, grid, and calibration. | E001 frequency and TF–IDF + LR reproduced; primary all-row plus secondary fold-supported-label subset. | Supported question+explanation MAP@3: 0.668 TF–IDF vs 0.689 frequency; all-row E001 reproduced. | Preserve negative result; preregister a small semantic baseline only after license/literature review. |
| E005 | 2026-08-31 | Proposed diagnostic: separate category transfer, label-support effects, and remaining random-to-grouped collapse without altering the target or model. | Frozen E001 grouped/random protocol; no execution until approved. | Frequency and E001 TF–IDF baselines decomposed by predeclared support strata; category probabilities collapsed without retraining. | Awaiting review. | Do not run, tune, or alter E001–E004. |
| E006 | 2026-09-01 | Proposed diagnostic: calibrated confidence or a prediction-time support-aware confidence rule identifies a reliable held-question subset for automated routing. | Frozen E001 grouped folds, roles, tuning, and calibration; no execution until approved. | Frequency and both E001 TF–IDF arms; fixed 0–50% review budgets and aggregate-only risk–coverage reporting. | Awaiting review. | Do not run or adjust thresholds/rules after results. |

For each completed run add: command/config path, Git revision, seed, runtime/hardware, train/calibration/evaluation group IDs or hashes, all metrics, artifacts, and an honest decision.

## Recovery and audit addendum — 2026-09-13

The original rows above are preserved. The E005 awaiting-review row is stale: the conversation subsequently approved and completed E005. The local Git history stopped at E003 when this audit began. E004/E005 records below are retrospective recovery entries, not claims of pre-run public registration. Exact run timestamps and source revisions were not reliably recorded; they are not invented here.

| Record | Status and result | Evidence | Next action |
|---|---|---|---|
| E004 recovery | Completed primary negative result. MAP@3 0.475984 explanation-only / 0.463698 question+explanation; frequency 0.539215. Preregistered per-question/support outputs were not serialized. | [Aggregate and fold archive](E004_RESULTS_ARCHIVE.md); original script/protocol preserved. | Preserve; no rerun. |
| E005 recovery | Existing final artifact preserved. Exact/category/support tables, per-question results, and stored descriptive summaries archived. Some promised uncertainty comparisons were not serialized; eligibility used per-fold rather than pooled checks. | [Aggregate and fold archive](E005_RESULTS_ARCHIVE.md); [audit](REPRODUCIBILITY_AUDIT_2026_09.md). | Preserve; no new E005 analyses or replacement artifact. |
| Brier erratum | Arithmetic correction only: historical scorer omitted the unit loss for unsupported truths. MAP@3/accuracy/ECE unchanged; original artifacts untouched. | [Correction tables](METRIC_ERRATUM_2026_09.md), separate metric implementation and synthetic tests. | Use corrected metric for approved future work; keep legacy fields identifiable. |
| Research review | Direct conceptual predecessor found in EDM 2019; unseen-question transfer is not a first-of-kind claim. Contribution is a reproducible MAP-specific diagnostic and negative-result record. | [Primary-source review](RESEARCH_REVIEW_2026_09.md). | No classifier/model swap. |
| E006 review | Not run. Original draft has ambiguous failure logic and an undefined calibration gate. | [Proposed clarifying addendum](E006_REVIEW_ADDENDUM.md). | Await user review; no thresholds or models selected from new evaluation results. |

No experiment is active and no idle monitor is scheduled. During future approved active runs, use the lightweight terminal monitor and hourly progress reporting. All public output remains sanitized code/documentation and aggregates only.

## E006 authorization — 2026-09-13

The user approved the clarified E006 addendum at published proposal revision `9c6962f8a3795342cd362f3201a1744c4fc39f3d`. The earlier proposed-status entries are historical. [The execution record](E006_EXECUTION_RECORD.md) and [approval registry](../experiments/e006_approval.yaml) now govern authorization without changing the scientific protocol. Implementation/tests are to be committed before the full Docker run. No E006 result is claimed by this entry; the final aggregate/fold results will precede interpretation or any next experiment.

## E006 completed — 2026-09-13

| Field | Recorded result |
|---|---|
| Pre-run implementation revision | `c5c0a987e409ef8aae99a19e1754b81de1662f7c` (committed and pushed before launch) |
| Execution | Non-root, network-disabled Docker; 100 fitting calls; ten outer-fold evaluations; approximately nine minutes |
| Reproduction gate | All 60 checks passed; maximum absolute difference from E001 = 0.0 |
| 50%-review frequency | Accuracy 0.401701; MAP@3 0.538735; risk 0.598299; ECE 0.056892; corrected Brier 0.795415 |
| 50%-review explanation/confidence | Accuracy 0.420454; MAP@3 0.543013; risk reduction 0.066751; ECE 0.161556; corrected Brier 0.813986 |
| 50%-review explanation/support-aware | Accuracy 0.437384; MAP@3 0.554111; risk reduction 0.083682; ECE 0.153821; corrected Brier 0.803498 |
| 50%-review question+explanation/confidence | Accuracy 0.446937; MAP@3 0.565317; risk reduction 0.070631; ECE 0.146974; corrected Brier 0.779865 |
| 50%-review question+explanation/support-aware | Accuracy 0.458105; MAP@3 0.571026; risk reduction 0.081800; ECE 0.145861; corrected Brier 0.775702 |
| Registered decisions | All four pairs pass the relative criterion; calibration descriptive only; no absolute acceptable automation risk was registered |
| Confidence AUROC | Explanation 0.603604 ± 0.021550; question+explanation 0.608135 ± 0.023960 (five-fold mean ± sample SD) |
| Output | [Full tables](E006_RESULTS.md), [complete aggregate/fold JSON](../results/E006_aggregates.json); no row-level artifacts |
| Stop condition | Numerical results presented for review. No interpretation, new analysis, or next experiment run. Monitor terminated on completion. |

All thresholds, folds, inputs, fitting/tuning, calibration and interpretation rules remained locked. E001–E005 artifacts were not overwritten. See [execution and verification details](E006_EXECUTION_RECORD.md).

## E007 proposal for review — 2026-09-25

The user resumed the project after discussion of E006's threshold-transfer gap. A [new E007 preregistration draft](E007_PROTOCOL.md) proposes frozen development-selected cutoffs with a primary 20% exact-label error target and secondary 10%/30% targets. It explicitly separates the three existing calibration questions into one temperature-fitting and two threshold-selection questions without changing frozen outer assignments. The proposed utility criterion requires at least 100 retained responses and 10% coverage, with error at or below target, on every evaluation question.

**Status: draft only; not approved, implemented, or run.** No new MAP results were computed. The previous E006 approval does not authorize E007. E001–E006 records remain unchanged; no monitor was started. Implementation, synthetic tests, hash locking, pre-run publication, and Docker execution await protocol review. There is no new result or success claim.

## E007 authorization — 2026-09-25

The user explicitly approved the proposed calibration split and error/coverage criteria. The [approval registry](../experiments/e007_approval.yaml) locks the original proposal and matching configuration by canonical hash; the historical draft status above is preserved. See the [execution record](E007_EXECUTION_RECORD.md). The implementation must pass synthetic tests and be committed before the Docker run. Results are not claimed by this entry.
