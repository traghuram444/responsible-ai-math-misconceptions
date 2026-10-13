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

## E007 completed — 2026-09-25

| Field | Recorded outcome |
|---|---|
| Pre-run revision | `b3a0a59f9c2e2226fd1a454eb438cf50c767b92f`, committed and pushed before launch |
| Runtime | 550.641 seconds through result construction; 550.914 seconds including final serialization/status |
| Execution | Existing audited non-root Docker image; network disabled; only new E007 artifact mount writable; 100 fitting calls |
| Reproduction | All 40 top-1/MAP@3 checks passed; inner-selected hyperparameters matched the historical reference |
| Primary 20% target | 0/5 admissible development folds for every arm/rule; all evaluation coverage 0%; retained metrics null |
| Secondary 10% and 30% targets | Same all-deferral outcome; no thresholds selected |
| Registered criterion | Unmet for all four learned pairs at all three targets; frequency also has no admissible cutoff |
| Fold/question reporting | All 5 folds and 15 questions retained in the tables/JSON, including unfiltered references and empty selected sets |
| Verification | Zero discrepancies in independent checks of 2,400 metric groups and 1,680 aggregate summaries; 42 preserved-file hashes verified |
| Outputs | [Numerical tables](E007_RESULTS.md), [full aggregate-only JSON](../results/E007_aggregates.json) |
| Monitor incident | Terminal viewer exited early after a missing-status-file read. Experiment and heartbeat continued. Viewer-only retries added/tested after completion, without rerunning or changing scientific code. |
| Stop condition | Present raw aggregate/fold/question results for user review; no interpretation or next experiment |

E001–E006 and E007's approved thresholds, folds, calibration subdivision and evaluation rules remain unchanged. No raw data, row-level predictions or fitted models were serialized or published. No active experiment or monitor remains.

## E008 diagnostic proposal — 2026-09-25

After reviewing E007, the user agreed to proceed with an infeasibility-diagnostic direction. The [E008 preregistration proposal](E008_PROTOCOL.md) specifies a development-only constraint decomposition, individual-versus-common cutoff feasibility, and correctness-informed oracle bounds for existing predictions. It preserves E007's targets, count/coverage floors, scores and question roles. This is prespecified exploratory analysis motivated by observed E007 outcomes, not independent confirmation or a classifier improvement.

**Status: detailed protocol awaiting review; not implemented or run.** No E008 MAP analysis or outer evaluation scoring was performed. E001–E007 remain unchanged. No experiment or monitor was started, and no learned error predictor is authorized by this proposal.

## E008 detailed protocol approved — 2026-09-28

The user approved the complete E008 preregistration. The historical proposal above is preserved. Approval/configuration hashes are locked in `experiments/e008_approval.yaml`; [execution record](E008_EXECUTION_RECORD.md). E008-only code implements development reconstruction with E007 reproduction gates, exact rational feasibility diagnostics, deduplicated oracle bounds, strict aggregate publication and an active-run terminal viewer. Synthetic testing and a pre-run commit/push precede any MAP diagnostics. No outer-evaluation prediction or further experiment is authorized. Full numerical results will be presented before interpretation.

## E008 completed — 2026-09-28

| Field | Recorded outcome |
|---|---|
| Pre-run revision | `ec4ed262bb8d63a0ad8bd38e6142ca8b28cbcf33`, committed/pushed and public revision verified before launch |
| Runtime | 535.172 seconds through result construction; 535.364 seconds through final heartbeat |
| Execution | One attempt; audited non-root/offline Docker image; only E008 artifacts writable; 100 model fitting calls |
| Reproduction | All 10 development records and 90 rule/target policy records matched E007 under the locked gate |
| Focal 20% target | Each arm/rule: fixed-prediction / score-selection / common-cutoff counts = 0 / 5 / 0 |
| Secondary 10% target | Each arm/rule: 0 / 5 / 0 |
| Secondary 30% target | Both learned question-plus-explanation rules: 0 / 4 / 1, with common-cutoff record at fold 2; other arm/rule combinations: 0 / 5 / 0 |
| Complete outputs | 90 fold/arm/rule/target records, 180 anonymous development-role records, 30 deduplicated model oracles; all five numeric fold values, means, sample SDs and defined counts |
| Independent verification | 270 count partitions and 1,782 numerical fold summaries checked with zero discrepancies; all 95 preserved-file hashes verified |
| Outer evaluation | Zero prediction calls; no witness cutoff applied to evaluation rows |
| Monitor | Active terminal viewer reached COMPLETED and exited normally; no observed read interruption and no idle monitor |
| Outputs | [Full numerical tables](E008_RESULTS.md), [aggregate-only JSON](../results/E008_aggregates.json) |
| Stop condition | Await user review of numerical results before interpretation or any new experiment |

The registered targets, floors, score functions, candidate grids, folds, question roles, calibration and classification rules were not changed. Frequency input-arm duplication is the same reference, not additional evidence. This is exploratory diagnosis of an observed E007 result; no inferential intervals or new classifier-performance claim are added. E001–E007 remain unchanged.

## E009 learned-reliability proposal — 2026-09-28

After reviewing the E008 interpretation, the user agreed to proceed with the learned-reliability direction. The [E009 protocol proposal](E009_PROTOCOL.md) fixes the proposed inner question cross-fitting, independent nested classifier tuning, five prediction-time features, weighted binary logistic estimator, raw-confidence control, metrics and failure criteria for review. The final classifier, outer folds, temperature/threshold roles and original risk/count/coverage criteria remain unchanged. Prior work on correctness calibrators and selective prediction is cited; no algorithmic novelty or independent-confirmation claim is made.

**Status: detailed specification awaiting review; not implemented, not run.** No E009 MAP feature extraction, prediction, model fit, timing pilot or monitor was started. E001–E008 scientific artifacts remain unchanged. A separately approved, hash-locked and tested implementation must precede execution.

Draft publication checks: the unchanged offline/non-root Docker regression suite passed 219 tests in 17.58 seconds. The three changed documentation files were checked against 28,587 normalized student-response prefixes, with zero response matches and zero secret/local-path matches. E007/E008 result fingerprints remained unchanged; no E009 artifact directory exists. This verifies documentation hygiene, not an E009 implementation or result.

## E009 detailed protocol approved — 2026-09-28

The user explicitly approved the complete E009 protocol. Approval is recorded in `experiments/e009_approval.yaml`; the historical draft text remains unchanged. E009-only implementation and synthetic tests cover independently nested classifier tuning, fixed reliability features/weights, label-blind scoring, a global policy-freezing barrier, historical E007 reproduction, strict aggregate export and an active-run terminal viewer. Code/configuration will be committed and pushed before the single MAP run. No protocol change, E001–E008 modification or further experiment is authorized. See the [execution record](E009_EXECUTION_RECORD.md).

## E009 completed — 2026-09-28

| Field | Recorded outcome |
|---|---|
| Pre-run revision | `c2dd478d3a857287ba8fcc6563fc2b64ad1cb496`, committed/pushed and public revision verified before launch |
| Runtime | 1,547.299 seconds through result construction; 1,547.745 seconds through final heartbeat |
| Execution | One attempt; audited non-root/offline Docker image; only E009 artifacts writable |
| Fitting | 400/400 classifier fits successful, zero warnings/failures; 10 reliability fits, zero constant fallbacks |
| Reproduction | 90/90 E007 development policies and 120/120 evaluation records matched; all policies frozen before evaluation correctness |
| Primary 20% target | Every arm/rule: 0/5 admissible cutoffs, 0/15 nonempty evaluation questions, 0% coverage, retained metrics null, criterion unmet |
| Secondary 10% / 30% | Same all-deferral outcome for every arm/rule; no requirements relaxed |
| Learned correctness AUROC | Explanation-only: 0.694529 ± 0.057753; question-plus-explanation: 0.633822 ± 0.036207; five defined folds each |
| Complete outputs | 200 fold/arm/rule/target records, 600 evaluation-question records, 50 fold-level ranking records with 150 question-level counterparts; all support/calibration strata retained |
| Independent verification | 4,000 classifier groups, 800 reliability groups and 3,104 numerical fold summaries checked; zero discrepancies; 114 preserved-file hashes verified |
| Regression tests | 256 passed in 23.07 seconds in the fixed offline/non-root image |
| Monitor | Active viewer reached COMPLETED and exited normally; no observed read interruption and no idle monitor |
| Outputs | [Full numerical tables](E009_RESULTS.md), [aggregate-only JSON](../results/E009_aggregates.json) |
| Stop condition | Await user review of complete numerical results before interpretation or another experiment |

E001–E008 scientific records and E009's approved models, thresholds, folds, features and evaluation rules are unchanged. Frequency's duplicated arms are one reference, not independent evidence. No raw responses, row-level artifacts, fitted models, router coefficients or scaler statistics were serialized or published. Uncertainty is descriptive; no new inferential analyses were added.

## E010 authorized and preregistered — 2026-10-13

The user authorized proceeding and starting the proposed fixed-budget review-prioritization experiment. The [E010 protocol](E010_PROTOCOL.md) records the exact operational choices before execution; these choices were agent-specified under that authorization, not separately user-reviewed. E010 reconstructs E009 unchanged, freezes all label-blind batch decisions, requires historical reproduction, and evaluates fixed 0–50% review budgets with all controls and both arms.

The primary comparison is learned versus support-aware routing at 20% review: at least two fewer remaining classifier errors per 100 original responses on an equal-fold mean, with positive benefit in at least four of five folds, separately per arm. This is simulated queue prioritization, not an automation-risk or human-benefit claim. The 15-question benchmark is repeatedly examined; all uncertainty is descriptive. E009's primary negative result is preserved.

Synthetic verification, privacy scans and a public clean pre-run commit precede the single Docker run. No new representation, rubric, model tuning, threshold relaxation, data acquisition or further experiment is included. [Execution record](E010_EXECUTION_RECORD.md).

## E010 completed — 2026-10-13

| Field | Recorded outcome |
|---|---|
| Pre-run revision | `af2efb703fd93cebd77ea17da45bea6147a30be4`, committed/pushed and public revision verified before launch |
| Runtime | 1,668.158 seconds through result construction; 1,669.264 seconds through final heartbeat |
| Execution | One attempt; audited offline/non-root Docker image; only E010 artifacts writable |
| Fitting | 400/400 classifier fits successful with zero warnings/failures; 10 reliability fits, zero constant fallbacks |
| Reproduction | All 10 E009 development records, 200 evaluation records and 50 ranking records matched under unchanged gates |
| Primary explanation-only benefit | 1.386828 ± 0.828494 fewer remaining errors per 100 responses versus support-aware at 20% review; positive in 5/5 folds; criterion unmet because mean <2.0 |
| Primary question-plus-explanation benefit | 0.278608 ± 1.097948; positive in 2/5 folds; both primary requirements unmet |
| Full reporting | 360 fold/arm/rule/budget records and 1,080 evaluation-question records, all support strata, classifier/reliability calibration and paired differences |
| Independent verification | 7,200 classifier groups, 1,200 reliability groups and 8,482 fold summaries checked; 60 unfiltered reference records verified; zero discrepancies; 135 preserved-file hashes matched |
| Monitor | Reached COMPLETED and exited normally with code 0; no observed read interruption; no idle monitor |
| Outputs | [Numerical tables](E010_RESULTS.md), [aggregate-only JSON](../results/E010_aggregates.json) |
| Stop condition | Present complete numerical results before interpretation or any subsequent experiment |

Both arms remain reported; no secondary budget or control replaces the preregistered primary comparison. Mean/SD uncertainty is descriptive on the reused benchmark. No human corrections are assumed. E001–E009 and E010's locked choices remain unchanged. No row-level output, fitted parameter, raw response or private artifact is published.

## E001–E010 research checkpoint consolidation — 2026-10-13

The user authorized a research report and reproducible public checkpoint after reviewing E010, not a new experiment. Added an evidence-linked synthesis, experiment index, concise README, citation metadata, four static aggregate-only figures and their source fingerprints, a separate hash-locked verification Docker environment, and public-checkout CI. Writing guidance shaped the report's evidence-linked structure and explicit interpretation boundaries; repository documentation remains the authoritative home.

The release preserves 144 public files from revision `7bd41443e8a88024f05144d49902c69f9da76a08` and the existing log prefix. E001–E010 protocols, scientific code, original tests, results, configuration and historical Docker setup remain unchanged. No MAP modeling, threshold search, split regeneration, bootstrap/permutation draw, new subgroup analysis or E011 was run. No experiment monitor is active.

Fresh verification used a separately tagged Linux amd64 image built with `--pull --no-cache`, a digest-pinned interpreter, and a complete 15-package core wheel/hash lock. The final local offline/non-root check passed **317 tests in 53.19 seconds**, revalidated E006 through its original sanitizer/reaggregation and E007–E010 through strict public validators, and reproduced all five figure artifacts exactly. All four figures were also rendered and visually reviewed. The original modeling image identity is unchanged. This verifies tests and reporting, not a fresh reproduction of historical research predictions or the full encoder dependency closure.

Both E010 primary outcomes remain negative. The report separates improved correctness ranking, fixed-cutoff automation feasibility and fixed-budget review prioritization. Historical metric/reporting/provenance limitations remain prominent. See [research report](RESEARCH_REPORT.md), [release audit](RELEASE_AUDIT_2026_10.md), [reproduction guide](REPRODUCTION.md) and [release notes](RELEASE_NOTES.md). Publication and clean-public-checkout outcomes are recorded in the follow-up release entry.

## Research checkpoint publication checks — 2026-10-13

Checkpoint commit `097ca6745880e025cdea70ee778dbcea16e3672c` contains the synthesis and verification tooling, not new experimental results. A Git archive of that commit, with no raw data, private artifacts, Git metadata or model cache, passed **317 tests in 54.08 seconds**, E006–E010 public aggregate checks and deterministic figure checks in the offline/non-root verification image. The full proposed-public-file audit covered **165 files** and **28,587 unique normalized student-response prefixes**, with zero prefix, common-secret or local-path matches. The subsequently appended log text received its own prefix check, also zero matches.

The personal public GitHub `main` revision and all **165 Git blob hashes** were verified against the local checkpoint. The [public verification workflow](https://github.com/traghuram444/responsible-ai-math-misconceptions/actions/runs/38459350144) records the independent Linux checkout, fresh hash-locked build, synthetic tests and aggregate checks. No restricted files were published. The research prerelease uses the version `0.1.0-research`; its final tag/commit and workflow status are verifiable on GitHub. This entry records publication checks only and changes no experiment, result, protocol, threshold or fold.

## E011 and conditional E012 authorized and preregistered — 2026-10-13

The user authorized the next experiment and a different model if it fails. Before fitting, [E011](E011_PROTOCOL.md) fixes a selected-answer-context ablation under the original E001 nested word TF–IDF/logistic protocol, and [E012](E012_PROTOCOL.md) fixes one conditional character TF–IDF/Complement Naive Bayes alternative. Numerical choices are agent-specified under this authorization, not separately user-reviewed. E011 must improve equal-fold MAP@3 by at least 0.020 over both question + explanation and frequency, with positive paired gains in at least four of five folds against each. Only a valid completed negative triggers E012, which uses the same margin/sign rule against E011 full context and frequency. Operational failures stop the sequence; stop after E012 regardless of outcome.

All models, calibration temperatures and label-blind evaluation rankings are prepared before evaluation metrics. No folds, training/calibration roles, original support thresholds or historical files change. Reports retain all questions, support strata, calibration eligibility, exact-label and six-way Category metrics, fixed exploratory review budgets and input-token diagnostics. These follow-up results on 15 repeatedly examined questions are descriptive, not independent confirmation. No student responses, answer strings, row predictions or fitted models are serialized for publication.

A new CPU modeling image is built from the existing complete wheel/hash lock and digest-pinned Dockerfile, without changing the historical images. Synthetic tests cover leakage isolation, coupled grids/tie selection, support/calibration rules, both publication paths, baseline gates and strict aggregate schemas. The execution lock preserves all 163 checkpoint files except the README and append-only experiment log, and pins the new protocols/code/environment. Tested code and protocols are committed and pushed before the single E011 attempt. The read-only terminal viewer operates only during active experiments.

## E011 completed — 2026-10-13

Pre-run revision `97afd8414e33f8dec08f984577d139e5bb618081` was pushed and its public identity verified before fitting. Its public GitHub workflow passed. The fresh hash-locked modeling image is `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`. Pre-run Docker verification passed 354 tests with two expected not-yet-published-result skips, historical aggregate checks and deterministic figure checks. All 176 proposed public files passed path/secret/local-path scans; the response-prefix audit checked 28,587 unique prefixes with zero matches, including the newly completed hash lock separately.

E011 completed one offline/non-root attempt: 150 classifier fits, zero fit warnings, all 30 historical reference checks passed, and all 163 preserved-file hashes and frozen data/split identities verified. The monitor reached COMPLETED at 659.061 seconds and exited normally. No idle monitor remains. All 15 development records were frozen before evaluation metrics; no row-level predictions or models were serialized.

| Arm | MAP@3 | Accuracy | ECE | Corrected Brier |
|---|---:|---:|---:|---:|
| Frequency | 0.539215 | 0.402009 | 0.056271 | 0.795057 |
| Question + explanation | 0.519971 | 0.376306 | 0.108524 | 0.805728 |
| Full context | 0.511887 | 0.368558 | 0.149626 | 0.838084 |
| Question + answer | 0.433872 | 0.247739 | 0.122322 | 0.882256 |

The primary full-context MAP@3 delta is −0.027328 ± 0.056586 versus frequency (2/5 positive folds), and −0.008084 ± 0.055319 versus question + explanation (3/5 positive). Both fixed criteria fail. This valid negative is preserved and triggers only the already-preregistered E012 after publication checks. Full numerical results were presented before that decision; no threshold or comparison changed. [All fold/question/support/calibration/review-budget tables](E011_RESULTS.md) and [aggregate-only artifact](../results/E011_aggregates.json) retain every arm. Mean/SD are descriptive, not inferential.

Post-run offline Docker verification passed **355 tests, one expected E012-result skip**, E006–E010 historical aggregate checks and all deterministic figures. A separate arithmetic check verified 180 weighted question-to-fold MAP@3, confidence and Category-accuracy identities with zero discrepancies. Repository-wide path/secret/local-path checks passed for 178 public files; all four changed/new publication files were checked against 28,587 private response prefixes with zero matches. Existing unchanged public files remain covered by the pre-run audit and preservation checks. The aggregate-only E011 publication receives its own descriptive commit before E012 begins.

## E012 stopped before evaluation — 2026-10-13

E011 result commit `37bfd9e9d318a4964d6426cc9df137d67319d0f1` was public before launching the conditional E012 run. All 178 public Git blob hashes matched locally, and its GitHub verification workflow passed. E012 pinned E011's aggregate SHA-256 and used the unchanged preregistered image, protocol, model grid, folds and calibration. It completed 49/95 classifier fits and two full outer-fold preparations, then stopped with `PermissionError` during preparation of fold 3 after 223.968 seconds. The all-fold development freeze had not been reached; held-out evaluation never began. The primary criterion and metrics are unavailable, not failed scientific comparisons.

Source inspection and a no-data synthetic fault-injection check confirmed that the monitor's main-thread status-write path can propagate `PermissionError` into the research loop. Transient status-file write/replace contention is a suspected cause, not established: the original traceback was suppressed and only exception type persisted. No permissions, implementation, scientific choices or historical records were changed. The run and monitor both exited; there is no idle monitoring, retry or next-model run. The preregistered operational-failure stop was applied.

The failed local attempt is preserved. Its [sanitized failure record](../results/E012_execution_failure.json) and [diagnostic report](E012_EXECUTION_FAILURE.md) are published separately from completed-result artifacts. Any retry requires a documented infrastructure-only amendment and a new attempt directory; none is implemented here. E011 remains a valid negative result, while E012 remains unevaluated.

Failure-publication verification passed **356 tests with one expected unevaluated-E012-result skip**, all historical aggregate checks and deterministic figures in offline/non-root Docker. The strict failure-record test also pins the unchanged E011 aggregate and execution-lock hashes. All three local evidence hashes matched; no development-freeze or evaluation-result artifact exists. All 181 public files passed path/secret/local-path checks, and the five changed/new files had zero matches against 28,587 private student-response prefixes. No private attempt file is committed; only its sanitized operational metadata is published.
