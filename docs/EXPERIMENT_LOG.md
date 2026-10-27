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

## E012 second attempt explicitly authorized

The user approved fixing the monitor and rerunning E012 in a new attempt directory, with all scientific settings unchanged and the failed attempt preserved. The [infrastructure amendment](E012_ATTEMPT02_AMENDMENT.md) records exactly one authorized retry. It adds a best-effort monitor adapter, operation-level sanitized I/O diagnostics, a dedicated viewer, a launcher that mounts the failed attempt read-only and writes to `artifacts/e012_attempt02`, and a new hash lock. The original scientific runner, protocols, grids, thresholds, folds, calibration, metrics and all prior result/failure records remain unchanged. No partial model from the first attempt is reused.

Synthetic tests cover each monitor write operation, transient recovery, persistent failure through finalization, propagation of real model/programming errors, stale snapshots, sanitized diagnostics, unchanged delegation and identical synthetic model probabilities under monitor failure. Writing guidance keeps the amendment explicit about authorization, preservation and scientific invariants. The tested amendment is committed and pushed before starting the one new attempt; any further operational failure stops for review.

Pre-run offline/non-root verification passed **372 tests with one expected unpublished-E012-result skip**, all historical aggregate validators and five deterministic figure artifacts. All 16 new infrastructure tests passed, including exact synthetic model-output equality under persistent monitor replacement failure. The amendment locks eight new files and preserves 179 prior public files. All 190 proposed public files passed path/secret/local-path checks, and all 11 changed/new files had zero matches against 28,587 private response prefixes. The original failed attempt's three evidence hashes were verified unchanged before publication; the second-attempt directory was absent.

## E012 second attempt completed — 2026-10-14 UTC

The approved second attempt used public pre-run revision `99ff908b8489c15701d71915e731a5f990b9e45f`; its independent GitHub workflow passed and all 190 public Git blob hashes matched locally. A container mount preflight failed before Python started because an empty alias mountpoint was missing. No attempt record or computation existed then. Creating the empty mountpoint and reissuing the identical Docker arguments allowed the one scientific retry to start; the original failed attempt and locked code remained unchanged. The [execution record](E012_ATTEMPT02_EXECUTION.md) documents this setup requirement and the initial viewer timeout.

E012 completed 95 fits with zero warnings in 415.699 seconds through result construction (415.849 seconds through monitor finalization), with all five development records frozen before held-out metrics. All 15 original frequency reference checks passed; the complete frequency fold/question summaries matched E011. Both locks, all 179 prior public files, source data/fold hashes and the first failed attempt's three evidence hashes remained unchanged. The new monitor reported zero I/O failures in this actual run, reached COMPLETED and exited normally. Its error-isolation behavior is covered separately by synthetic fault tests, not inferred from this error-free execution.

| Model | MAP@3 | Accuracy | ECE | Corrected Brier |
|---|---:|---:|---:|---:|
| Frequency | 0.539215 | 0.402009 | 0.056271 | 0.795057 |
| E011 full context | 0.511887 | 0.368558 | 0.149626 | 0.838084 |
| E012 full context | 0.537228 | 0.402374 | 0.377470 | 0.985662 |

E012's primary MAP@3 delta versus frequency is −0.001987 ± 0.003825, positive in 2/5 folds; versus E011 full context it is +0.025341 ± 0.057834, positive in 3/5 folds. Neither comparison meets both fixed requirements; the overall primary outcome is negative. Complete aggregate and fold-level results were shown before interpretation. All registered questions, support strata, Category, calibration and review-budget results remain in the [full tables](E012_RESULTS.md) and [aggregate-only JSON](../results/E012_aggregates.json). Mean/SD are descriptive only. No post-hoc scientific change, new subgroup analysis, further model or idle monitoring was added.

The completed retry receipt, result/revision/lock hashes, failed-attempt preservation and complete frequency comparisons passed a separate post-run check. Ninety independent weighted question-to-fold MAP@3, confidence and Category-accuracy identities matched with zero discrepancies. The first failure report remains unchanged; only the second attempt has evaluated results.

Final offline/non-root Docker verification passed **373 tests with no skips**, all historical aggregate checks and deterministic figures. All 193 public files passed path/secret/local-path checks; the five changed/new publication files had zero matches against 28,587 private response prefixes. Original failed-attempt evidence remained unchanged in the final scan. The completed E012 aggregate, tables, execution record and README/log update receive a separate descriptive result commit; no raw data, row-level output or fitted model is published.

## E013 protocol prepared for review — 2026-10-14

The user authorized preparing and showing the [E013 preregistration](E013_PROTOCOL.md), not running it. The proposal tests response-specific evidence in unchanged E011/E012 full-context models using label-blind explanation permutations within question/selected-answer cells and intact answer–explanation permutations within questions. It fixes 100 replicates, deterministic mappings shared across models, two separately reported explanation-evidence criteria, unchanged support strata, frequency agreement/win-loss summaries, and an exploratory raw-versus-registered-calibration audit. No recalibration, model change, new labels, or fold changes are proposed.

All historical files and E001–E012 outcomes remain unchanged; this log addition is append-only. The numerical choices are pending review, not represented as approved. No E013 implementation, model fit, permutation analysis, result artifact, monitor, or scheduled wakeup has been started. After explicit protocol approval, tested code and a preservation lock must be committed before execution. This protocol-only entry is not a claim of an executed or publicly registered experiment.

## E013 approved for execution — 2026-10-15

The user approved E013 exactly as preregistered, preserving E001–E012 and the frozen folds, with the live monitor active during computation and aggregate/fold results shown before interpretation. [The approval record](../experiments/e013_approval.json) pins the reviewed protocol bytes; its original review-status text remains historical rather than being silently rewritten. No scientific choices changed.

New implementation files reuse the original scientific preparation functions, retain raw/scaled predictions and shared label-blind permutations only in memory, and gate new summaries on complete reproduction of both historical full-context arms and frequency. A strict aggregate-only publisher checks reporting grids, counts, recipient support, permutation summaries, frequency invariance, gain/loss identities, question-to-fold arithmetic, calibration eligibility and both primary criteria. The monitor reuses the tested resilient adapter. Execution is limited to one new attempt, with all prior public scientific files and private E011/E012 attempt evidence pinned read-only. No automatic retry or E014 is authorized.

The E013 synthetic suite passed 19 tests with one expected not-yet-published-result skip before locking; this includes full five-fold synthetic reconstruction/scoring/reporting and deliberate aggregate corruption/private-field rejection. Writing review keeps approval history, numerical reporting and interpretation separate. The approved plan and tested implementation are committed before MAP reconstruction; results receive a separate commit after verification and aggregate-only publication checks.

## E013 completed numerical results — 2026-10-15

The approved run used public pre-run revision `a0874e9220d4d8e289d81fb70a59f475921280e2` and the unchanged pinned offline/non-root Docker image. Pre-run verification passed 392 tests with one expected unpublished-result skip; public CI and all 204 public blob hashes matched. The privacy audit found zero matches against 28,587 response prefixes. The execution lock preserves 191 previous public scientific files and 13 private E011/E012 attempt-evidence files.

E013 completed 145 fits with zero warnings, froze all ten model-fold preparations and shared label-blind mappings before new held-out metrics, and passed all historical full-record reproduction gates. Runtime was 751.993 seconds through result construction and 753.062 seconds through monitor finalization. One transient snapshot replacement PermissionError was caught by the pre-existing resilient monitor; computation continued unchanged, the final monitor state was COMPLETED and the viewer exited. No scientific or operational retry occurred.

| Model | Original MAP@3 | Explanation shuffled MAP@3 | Pair shuffled MAP@3 | Explanation delta mean | Fold SD | Positive folds | Registered explanation criterion |
|---|---:|---:|---:|---:|---:|---:|---|
| E011 | 0.511887 | 0.485204 | 0.465728 | 0.026683 | 0.006820 | 5/5 | Met |
| E012 | 0.537228 | 0.536613 | 0.536338 | 0.000616 | 0.000797 | 4/5 | Unmet |
| Frequency | 0.539215 | 0.539215 | 0.539215 | 0.000000 | 0.000000 | 0/5 | Not applicable |

Aggregate and fold-level numerical results were shown before interpretation. The [complete tables](E013_RESULTS.md), [aggregate-only artifact](../results/E013_aggregates.json) and [execution record](E013_EXECUTION.md) retain all registered question/support, frequency agreement/win-loss, calibration and opportunity summaries. Uncertainty remains descriptive. E001–E012, both E012 attempts, all scientific settings and frozen assignments remain unchanged. Interpretation is deferred for user review; no E014 or idle monitoring is active.

## E014 protocol prepared for review — 2026-10-15

Following discussion of E013, the user authorized proceeding with protocol preparation. The [E014 proposed preregistration](E014_PROTOCOL.md) tests a single fold-specific mixture of unchanged E011 raw probabilities and training-label frequency. Its six-weight grid is selected only inside the existing outer training questions, followed by the registered calibration stage. Proposed primary success requires at least +0.020 equal-fold mean MAP@3 over frequency and positive gains in at least four folds. Explanation-shuffle, gain/loss, support, calibration, and review diagnostics have fixed reporting rules.

The protocol awaits review; no E014 implementation, selection, fitting, scoring, or monitor has started. E001–E013 and frozen splits remain unchanged. This entry is an append-only status update, not an alteration of E013's recorded results or interpretation rules.

## E014 approved and implementation prepared — 2026-10-15

The user approved the displayed E014 specification. Approval is recorded separately with the reviewed protocol's SHA-256; the protocol text is unchanged. New E014 code reuses historical fitting, calibration, ranking, support, and routing functions without editing those modules. It preserves the exact frequency/logistic endpoints, uses inner-training-only frequency for weight selection, and runs only the explanation-shuffle diagnostic. All development choices are frozen globally before new evaluation scores; historical full-record and E013 diagnostic reproduction gates precede selected-mixture scoring.

Synthetic tests cover nested selection, endpoint identity, calibration order, label-free evaluation inputs, deterministic donor mappings, recipient support, null eligibility, primary decision boundaries, aggregate-only schemas, and monitor-I/O isolation. Verification and the hashed execution lock precede the run. No E015 or automatic operational retry is authorized.

## E014 completed numerical results — 2026-10-15

The approved single attempt used pre-run revision `2ba6d2907f3586dde9a6dcf34b6b88881b5a968c` and the unchanged pinned offline/non-root Docker image. Preflight verification passed 420 tests with one expected unpublished-result skip; all 218 public blob hashes matched and public CI passed. The privacy scan found zero matches against 28,587 response prefixes. The execution lock preserved 205 prior public files and 18 private evidence files.

E014 completed 50 fits with zero warnings. All development choices and mappings were frozen before evaluation; all historical E011/frequency full-record and E013 diagnostic gates passed before selected-mixture scoring. Result construction took 325.963 seconds; the monitor completed at 326.673 seconds with zero I/O failures and exited normally. There was no retry or scientific modification.

| Arm | Mean MAP@3 | Fold SD | Accuracy | Final ECE | Final Brier |
|---|---:|---:|---:|---:|---:|
| Selected mixture | 0.537231 | 0.054967 | 0.393572 | 0.144342 | 0.812655 |
| E011 | 0.511887 | 0.070731 | 0.368558 | 0.149626 | 0.838084 |
| Frequency | 0.539215 | 0.039204 | 0.402009 | 0.056271 | 0.795057 |

The mixture-minus-frequency paired mean is -0.001984, sample SD 0.033505, positive in 3/5 folds; the fixed primary criterion is unmet. The mixture-minus-E011 paired mean is +0.025343, sample SD 0.028171, positive in 4/5 folds. Weights for folds 0–4 were 0.25, 0.50, 0.25, 0.75, and 0.00. The mixture's explanation-shuffle decrement is 0.007261. These are numerical summaries, not a new interpretation or experiment proposal.

The [complete tables](E014_RESULTS.md), [aggregate artifact](../results/E014_aggregates.json), and [execution record](E014_EXECUTION.md) retain all fixed fold/question/support, contribution, calibration, review-budget, and permutation summaries. E001–E013 and frozen assignments remain unchanged. No E015 or idle monitoring is active.

## E015 protocol prepared — 2026-10-16

Prepared [E015: controlled mathematical-token retention ablation](E015_PROTOCOL.md) for review against reference revision `16f55596de8b871d89820e31e75ddf28e4c2f150`. Three fixed full-context TF–IDF/logistic pipelines compare the original E011 tokenizer, single-character word/digit retention, and a precisely bounded notation tokenizer, with unchanged nested selection, calibration, frozen QuestionId roles, and frequency reference. The sole primary outcome is notation-retaining C versus frequency: mean MAP@3 gain >=0.020 and a strictly positive gain in at least four of five folds. Fixed secondary comparisons and explanation reliance distinguish tokenization effects from baseline utility; coverage, Category, calibration and review diagnostics remain exploratory.

**Awaiting approval of the exact protocol.** No E015 implementation, MAP token audit, fitting, evaluation, monitor, or execution attempt has started. E001–E014 and all existing folds/attempts remain unchanged. This entry records preparation, not a result or authorization to execute.

## E015 approved and prepared for execution — 2026-10-16

The user explicitly approved the exact E015 protocol, unchanged folds and E001–E014, an active run monitor, and numerical aggregate/fold results before interpretation. The separate approval record pins the unchanged protocol. New E015 code reuses the historical scoring, calibration, permutation, and monitoring routines without editing them. The execution lock protects 219 previous public files and 23 private evidence files. Three arms require 150 fits; no E014 mixture, new model family, or automatic retry is authorized. Synthetic tests and publication checks precede the committed, offline/non-root Docker attempt. No MAP fitting has occurred at the time of this entry.

## E015 completed numerical record — 2026-10-16

The single approved attempt ran at pre-run commit `1f8d759e095112a1c60392432c766ef842b9d440` with the protocol, scientific settings, and frozen folds unchanged. All 150 fits completed with zero warnings. Global freezing and all historical reproduction gates passed before new B/C scoring. Result construction took 1011.218 seconds; the monitor completed at 1012.276 seconds and exited normally with zero I/O failures. No retry occurred.

| Arm | Mean MAP@3 | Fold SD | Accuracy | Final ECE | Final Brier |
|---|---:|---:|---:|---:|---:|
| A: original E011 | 0.511887 | 0.070731 | 0.368558 | 0.149626 | 0.838084 |
| B: single-character retention | 0.509537 | 0.066174 | 0.357535 | 0.168244 | 0.866803 |
| C: notation retention | 0.491902 | 0.057333 | 0.315591 | 0.208000 | 0.901172 |
| Frequency | 0.539215 | 0.039204 | 0.402009 | 0.056271 | 0.795057 |

The primary C-minus-frequency mean is −0.047313, fold sample SD 0.031903, positive in 0/5 folds; the fixed criterion is unmet. B-minus-A is −0.002350 (SD 0.053273); C-minus-B is −0.017635 (SD 0.013791). These are descriptive numerical records, without interpretation or a next-experiment proposal.

The [complete tables](E015_RESULTS.md), [aggregate artifact](../results/E015_aggregates.json), and [execution record](E015_EXECUTION.md) preserve all registered results, including null/ineligible strata. E001–E014 and all frozen assignments remain unchanged. No experiment or monitor remains active.

## E016 protocol prepared — 2026-10-19

Prepared [E016: direct Category learning with frequency-based misconception ranking](E016_PROTOCOL.md) for review against revision `7a3144990783eb3976641fa67c3dfaf93675fb8f`. The proposed primary arm learns the existing six Categories using the original E011 full-context TF–IDF/logistic representation, then reconstructs exact-label probabilities using training-only within-Category frequencies. E011 and unchanged frequency are reproduction controls. Frozen QuestionId roles, the original nested three-setting grid and exact-label temperature calibration remain fixed. The sole primary criterion is all-row mean MAP@3 gain >=0.020 over frequency, strictly positive in at least four of five folds. Direct raw Category accuracy, exact-label gain/loss decomposition and explanation reliance are prespecified secondary comparisons; final Category, calibration and review-budget diagnostics cannot replace the primary outcome.

**Awaiting approval of the exact E016 specification.** No implementation, MAP fitting, pilot, selection, evaluation, monitor or execution attempt has started. E001–E015 and all frozen folds/attempts remain unchanged. No new ensemble, expanded parameter search, scientific fallback or E017 is authorized.

## E016 approved and prepared for execution — 2026-10-19

The user explicitly approved E016 exactly as preregistered, preserving E001–E015 and frozen folds, with a live monitor during the run and numerical results before interpretation. The separate approval record pins the unchanged protocol. New E016 code implements direct six-way Category learning and training-only within-Category exact-label frequencies; historical fitting, selection, calibration, scoring, support and routing routines remain unchanged. E011 and frequency reproduction gates precede new model scoring.

Synthetic verification covers nested count isolation, factorization and frequency identities, absent Categories and unsupported exact truths, raw/direct versus final/marginalized Category semantics, frozen evaluation predictions, calibration isolation, historical reproduction, strict aggregate schemas, arithmetic and monitor-I/O isolation. The approved single attempt requires 100 classifier fits. The tested implementation and historical public/private preservation inventory are hash-locked and committed before fitting. No MAP fitting has occurred at the time of this entry. No retry, scientific amendment or subsequent experiment is authorized.

## E016 completed numerical record — 2026-10-19

The single approved attempt ran at pre-run revision `ababb48100e969ba8b1fa18b17e5fbc8f3aec6b2` with all scientific settings and frozen folds unchanged. All 100 fits completed with zero warnings. Global freezing, historical reproduction and post-scoring preservation checks passed. Result construction took 427.136 seconds; the monitor completed at 427.870 seconds and the viewer exited normally. One transient monitor snapshot-write PermissionError was isolated and recovered; there was no experiment retry or scientific amendment.

| Arm | Mean MAP@3 | Fold SD | Exact accuracy | Final ECE | Final Brier |
|---|---:|---:|---:|---:|---:|
| Factorized Category/frequency | 0.481557 | 0.084770 | 0.347878 | 0.133588 | 0.839697 |
| E011 | 0.511887 | 0.070731 | 0.368558 | 0.149626 | 0.838084 |
| Frequency | 0.539215 | 0.039204 | 0.402009 | 0.056271 | 0.795057 |

Factorized-minus-frequency mean MAP@3 is −0.057658, sample fold SD 0.074549, positive in 1/5 folds; the registered criterion is unmet. Factorized-minus-E011 is −0.030330, sample fold SD 0.026433. Raw six-way Category accuracy is 0.356099 / 0.368513 / 0.402009 and macro-F1 is 0.189978 / 0.168469 / 0.095344 for factorized / E011 / frequency. Final marginalized Category accuracy is 0.340863 / 0.369042 / 0.402009; macro-F1 is 0.176700 / 0.182615 / 0.095344. The factorized explanation-shuffle MAP@3 decrement is 0.023696. These are numerical records only.

The [complete tables](E016_RESULTS.md), [aggregate artifact](../results/E016_aggregates.json) and [execution record](E016_EXECUTION.md) preserve every registered reporting group, including null/ineligible groups. E001–E015 and the frozen folds remain unchanged. No experiment or monitor remains active; interpretation awaits user review, and no E017 is authorized.

## E017 protocol prepared for review — 2026-10-19

Following the E016 interpretation, the user requested [E017 component information and fixed frequency ranking limits](E017_PROTOCOL.md), preserving E001–E016 and the frozen folds. The proposed diagnostic compares unchanged training frequency with oracle filtering using true answer correctness, true explanation status, or both. Oracle information is supplied only inside the post-freeze diagnostic scorer and is explicitly separated from real E011/E016/frequency predictions. No oracle result can count as a predictive baseline win.

The sole primary diagnostic criterion is full-Category oracle minus frequency all-row mean MAP@3 >=0.020, with strictly positive differences in at least four of five folds. Fixed secondary component headroom comparisons, real component predictions, complete support/question tables and residual unsupported-versus-ranking loss decomposition distinguish information value from attainable model performance. Historical reconstruction uses unchanged nested selection and calibration; no new model, answer key, threshold or fold is introduced.

**Awaiting review and approval of the exact E017 protocol.** No E017 implementation, fitting, new component/oracle scoring, pilot, attempt, monitor or execution has started. E001–E016 records remain unchanged; this entry is append-only. No E018 or automatic fallback is authorized.

## E017 approved and prepared for execution — 2026-10-19

The user approved E017 exactly as preregistered, preserving E001–E016 and frozen folds, with an active execution monitor and aggregate/fold-level numerical results before interpretation. The separate approval record pins the unchanged reviewed protocol. New E017 orchestration reconstructs unchanged E011/E016 pipelines, freezes training-only compatible candidate lists before evaluation truth is accessed, and runs historical reproduction gates before new component/oracle scoring. Oracle diagnostics are isolated from real predictions in code, publication schemas, reports and monitor labels.

Synthetic tests cover frequency endpoints and tied-subsequence behavior, absent Categories, short/empty candidate lists, unsupported exact truths, monotonicity, component marginalization, confusion/F1 arithmetic, null groups, residual identities, headroom decision boundaries, truth isolation, publication corruption rejection and monitor-I/O isolation. The single approved attempt requires 100 historical classifier reconstruction fits. Full verification, privacy scanning and the committed execution lock precede fitting. No new model specification, calibration procedure, fold, support stratum or scientific fallback is authorized. No E017 MAP fitting or new scoring has occurred at the time of this entry.

## E017 completed numerical record — 2026-10-19

The approved single attempt ran at public pre-run revision `2dd8ae24d25ea311852de5a8f4fb75c4c089aad2` with the protocol and scientific settings unchanged. Preflight verification passed 527 tests with one expected unpublished-result skip; public CI passed and all 260 public blobs matched the committed tree. The privacy scan found zero matches against 28,587 private response prefixes. The execution lock protected 247 prior public files and 57 private evidence files.

All 100 historical reconstruction fits completed with zero warnings. All real predictions and training-only oracle candidate lists were frozen before evaluation truth access; all 15 model/fold reproduction gates passed before new diagnostic scoring. Preservation checks passed before and after execution. Result construction took 434.180 seconds; the monitor completed at 434.752 seconds and exited normally with zero I/O failures. No retry or scientific amendment occurred.

### Real prediction controls

| Arm | Mean MAP@3 | Fold SD | Exact accuracy |
|---|---:|---:|---:|
| Frequency | 0.539215 | 0.039204 | 0.402009 |
| E011 | 0.511887 | 0.070731 | 0.368558 |
| E016 | 0.481557 | 0.084770 | 0.347878 |

### Oracle diagnostics using evaluation truth

These are information diagnostics, not real predictions or new predictive baseline wins.

| Supplied true component | Mean MAP@3 | Fold SD | Exact accuracy | MAP@3 delta versus frequency | Paired fold SD | Positive folds |
|---|---:|---:|---:|---:|---:|---:|
| Answer correctness | 0.653644 | 0.043628 | 0.580184 | 0.114429 | 0.021381 | 5/5 |
| Explanation status | 0.658031 | 0.045635 | 0.582750 | 0.118816 | 0.024065 | 5/5 |
| Full Category | 0.733311 | 0.034067 | 0.733311 | 0.194096 | 0.029165 | 5/5 |

The registered primary full-Category oracle headroom flag is true; both prespecified secondary component-headroom flags are true. These flags use the unchanged +0.020 mean and four-positive-fold rule and do not describe predictive success. Full-Category oracle all-row residual MAP@3 loss is 0.266689: 0.213391 unsupported-label loss plus 0.053298 supported-ranking loss, using equal-fold means and full-group denominators.

The [complete numerical tables](E017_RESULTS.md), [aggregate artifact](../results/E017_aggregates.json), and [execution record](E017_EXECUTION.md) retain every registered real/oracle fold/question/support result, raw/final component metric and confusion matrix, joint component count, contrast and residual decomposition. Empty rare strata remain null. E001–E016 and frozen folds remain unchanged. No interpretation or next-experiment proposal is included; no experiment or monitor remains active.

## E018 protocol prepared for review — 2026-10-20

Following E017 interpretation, the user requested [E018 independently verified answer correctness with a matched frequency baseline](E018_PROTOCOL.md), preserving E001–E017 and frozen folds. The proposed enriched-information experiment compares correctness-grounded E011 with frequency supplied with the identical independently verified correctness signal. Original E011 and frequency remain reproduction controls. No oracle truth, label-derived answer key, new classifier, expanded tuning or post-grounding recalibration is allowed.

The sole primary criterion is grounded-E011 minus grounded-frequency all-row mean MAP@3 >=0.020, strictly positive in at least four of five folds. Grounded-frequency versus ordinary-frequency improvement is a secondary information-benefit comparison and cannot substitute for learned-model success. Existing support groups, calibration eligibility and fixed review budgets remain unchanged. Unknown or unavailable-compatible-candidate cases retain original predictions and stay in primary denominators.

**Awaiting approval of the exact E018 specification.** Execution additionally requires documented label-blind mathematical verification, source/rights checks where applicable, and a frozen private correctness manifest. Required human reviewers and verified keys are not yet established. Missing verification blocks execution; it does not permit substitution of E017 oracle information. No E018 key preparation, verification, implementation, fitting, pilot, scoring, attempt or monitor has started. E001–E017 records and frozen folds remain unchanged; this entry is append-only.

## E018 approved but stopped at the independent verification gate — 2026-10-20

The user approved E018 exactly as preregistered and explicitly required stopping if independent correctness verification could not be established. The [separate approval record](../experiments/e018_approval.json) pins the unchanged protocol SHA-256. The [verification feasibility record](../experiments/e018_verification_gate.json) records an unmet prerequisite, not experimental results.

Both permitted evidence routes require genuine documented human mathematical verification. No designated qualified reviewer or signed label-blind verification was provided, and no E018 verification package was found in the checked project locations. No authoritative exact-version key has been established; no external source search was performed and no claim is made that such a key is unavailable. Even finding a primary key would not replace the required independent human check.

**Stopped before key preparation, implementation or fitting.** No private catalogue/manifest or attempt directory was created; no MAP-label agreement, model scoring, oracle substitution or monitoring occurred. This is a verification feasibility blocker, not a negative predictive result or a completed all-unknown catalogue. Resumption requires the documented reviewers and evidence specified in the approved protocol. E001–E017, the E018 protocol, and frozen folds remain unchanged. No protocol relaxation, retry, alternative model or next experiment is authorized.

## E019 protocol prepared for review — 2026-10-20

The user requested a separate [E019 preregistration for automated correctness prediction](E019_PROTOCOL.md), preserving E018's blocked status, E001–E017 and frozen folds. The proposed checker is the official `Qwen/Qwen2.5-Math-1.5B-Instruct` at revision `aafeb0fc6f22cbf0eaeed126eff8be45b0360a35`, with a fixed zero-shot prompt, greedy CPU float32 generation, 3072 input/1024 output token limits, and explicit unknown/fallback rules. These are fallible model predictions, not independently verified keys. Only public metadata/configuration and license information have been inspected; no weights were downloaded.

Five fixed arms are ordinary frequency F, historical E011 L, training-majority correctness-filtered frequency F_M, automated-correctness frequency F_A and identically automated-correctness E011 L_A. Primary H1 requires F_A to beat both F and F_M, each by mean all-row MAP@3 >=0.020 and with strictly positive differences in at least four of five folds. Secondary L_A−F_A measures incremental learned-context value and cannot replace H1. Historical tuning/calibration and all rows remain unchanged; the protocol separately specifies agreement/coverage, gain/loss, calibration and fixed-review reporting.

**Awaiting approval of the exact E019 protocol.** No implementation, model execution, prompt catalogue, MAP pilot, fitting, scoring, attempt or monitor has started. E018 remains blocked and its protocol/approval/gate records are unchanged. No E001–E017 scientific files or frozen folds were changed; this log entry is append-only.

## E019 approved; isolated implementation and preparation — 2026-10-23

The user approved E019 exactly as preregistered, with E018 still blocked and earlier experiments/folds unchanged. The [approval record](../experiments/e019_approval.json) pins the original protocol. New implementation files preserve the fixed Qwen model, prompt, parser, CPU float32 settings, five matched arms, historical fitting/calibration, all-row denominators and complete registered reporting grid.

Docker's available memory passes the 16 GiB solver resource gate without host settings changes. The official weights match the registered size and SHA-256; the separate solver environment contains a complete 24-wheel hash-locked closure and passed its offline dependency check. The historical statistical image is unchanged. A preservation inventory records 513 existing files and the original log prefix.

The one authorized synthetic plumbing prompt completed: 177 input tokens, 272 generated tokens, 143.126690316014 seconds, parser status `unknown_invalid_output`. This status is retained without changing the prompt/parser or retrying. Label-free preparation found 60 distinct question/answer pairs across all 36,696 rows. No MAP model inference or correctness scoring occurred during preparation.

The complete suite passed 566 tests, including the initial 38 E019 tests. Final pre-launch checks, exact lock/commit identity and the subsequent run outcome are recorded append-only in [E019 execution](E019_EXECUTION.md). The single attempt may begin only after the tested implementation and lock are committed. Results will precede interpretation; no E020 is authorized.

## E019 completed; numerical results awaiting review — 2026-10-23

The approved attempt completed all 60 checker pairs and 50 historical classifier fits, without changing the locked protocol or retrying. Aggregate checker reasons were 58 invalid-output unknowns and two generation-limit unknowns; there were zero accepted binary decisions. All 36,696 rows remained in the registered denominators and used unknown fallback. No failure receipts exist. Global prediction/routing freeze and historical reproduction gates passed.

| Arm | Equal-fold MAP@3 | Sample SD | Equal-fold exact accuracy |
|---|---|---|---|
| F | 0.539215 | 0.039204 | 0.402009 |
| L | 0.511887 | 0.070731 | 0.368558 |
| F_M | 0.474187 | 0.036689 | 0.402009 |
| F_A | 0.539215 | 0.039204 | 0.402009 |
| L_A | 0.511887 | 0.070731 | 0.368558 |

F_A−F mean MAP@3 is 0.000000 with 0/5 positive folds; F_A−F_M is +0.065028 with 5/5; L_A−F_A is −0.027328 with 2/5. The registered H1 conjunction and secondary H2 flags are false. Fold summaries and sample SDs are descriptive only.

The [complete numerical tables](E019_RESULTS.md), [full-precision aggregate artifact](../results/E019_aggregates.json), and append-only [execution record](E019_EXECUTION.md) retain every registered panel, including question/support results, correctness confusion and coverage, fallback states, gain/loss, calibration and fixed-review budgets. The frozen publisher validated the schema and arithmetic. All 513 pre-existing protected files, E001–E017, frozen folds, README and E018's blocked status remain unchanged. No interpretation, parser repair, alternative model or E020 is included; results await user review.

## E020 larger-model/hybrid protocol prepared for review — 2026-10-26

After reviewing E019, the user requested a larger model and ensemble direction and authorized compute/source checks and protocol preparation, not execution. The [E020 preregistration](E020_PROTOCOL.md) proposes official revision-pinned Qwen2.5-Math-7B-Instruct, with the pinned 1.5B checkpoint under the same new BF16 reasoning/three-choice readout as a capacity control. No E019 output is repaired or rescored. A fixed synthetic readiness gate precedes any MAP inference.

Nine fixed arms separate historical frequency/E011, constant filtering, a no-checker mixture, smaller/larger soft checker-assisted frequency, larger-checker-assisted E011, a selected three-component hybrid, and a hard-filter diagnostic. Only outer-training inner folds select the fixed ensemble weights; existing calibration questions fit final temperatures. H1 requires hybrid-minus-frequency mean MAP@3 >=0.020 and positive differences in at least four folds. Separate secondary rules test ensemble increment, checkpoint difference and mathematical-information benefit; none substitutes for H1.

Read-only hardware checks found about 63.7 GiB physical RAM, 31.2 GiB Docker memory and a roughly 4 GiB GPU. The proposed execution uses sequential CPU models with a 24 GiB memory gate, no host settings changes, and a broad 8–48-hour planning allowance subject to a synthetic timing gate. Only official public metadata/configuration/license and primary literature were fetched. The prior E019 public CI run is now confirmed successful.

**Awaiting approval of the exact E020 specification.** No model weights were downloaded, models loaded, synthetic prompts executed, MAP catalogue prepared, fitting/selection/scoring performed, or experiment/monitor started. E001–E019 scientific evidence, frozen folds, README and E018's blocked status remain unchanged. The protocol records related ensemble/verification work and makes no algorithmic-novelty claim. This entry is append-only.

## E020 approved; synthetic-readiness preparation — 2026-10-26

The user subsequently approved the exact specification with “approved,proceed”. The protocol bytes remain unchanged; approval is recorded separately. The [execution record](E020_EXECUTION.md) documents preparation of the single fixed synthetic gate, official model acquisition, exact configuration locks, preservation checks and aggregate-only publication safeguards. This stage is not MAP execution: it has no MAP input catalogue, predictions, classifier fits or scientific results.

The readiness launcher stops after the registered gate and runtime projection. A failed gate stops E020 before MAP; a projection over 48 hours requires runtime approval. Passing readiness does not authorize a changed model, prompt, threshold or evaluation design. Complete MAP orchestration/reporting must be tested and separately committed before that phase. The 664-file preservation inventory is retained privately, with only its aggregate receipt public. E001–E019, frozen folds, README and blocked E018 remain unchanged.

## E020 synthetic readiness completed; MAP not yet started — 2026-10-26

Both checkpoints completed 12/12 fixed synthetic readouts with zero technical fallbacks. G15 scored 5/10 binary and 0/2 insufficient-information fixtures; its registered gate is technical only. G7 scored 10/10 binary and 2/2 insufficient-information fixtures, passing its fixed semantic gate. No failure receipt, retry or settings change occurred. These are readiness outcomes, not MAP performance or evidence of unseen-question generalization.

The combined registered MAP projection is 18.438779 hours, below the 48-hour approval boundary. Complete numerical [readiness tables](E020_READINESS.md), [aggregate JSON](../results/E020_readiness.json) and [execution evidence](E020_EXECUTION.md) preserve this stage separately. The complete suite passed 603 tests, full model hashes and all 664 historical files were verified, and the 17-file readiness lock remains unchanged. The remaining approved MAP implementation must pass its own tests/lock/commit checks before inference. E001–E019, frozen folds, README and blocked E018 remain unchanged.

## E020 MAP-phase implementation after readiness — 2026-10-26

The readiness result is publicly preserved in commit `1c9e3d54582a826aa535dbf1aeb77dbc639b359a`. New phase-specific code implements the existing approved protocol without changing the readiness lock: sequential input-only checkpoint caches, training-only nested ensemble selection, original calibration, global five-fold prediction/routing freeze, matched historical reproduction and complete aggregate-only reporting. Valid C readouts remain distinct from technical fallback, as required by the preregistration. The [execution record](E020_EXECUTION.md) documents the additional lock, synthetic tests, private preservation and launch/monitor boundaries. No MAP score or scientific conclusion is available at this preparation stage; results will be reported before interpretation.

## E020 technical failure; reporting-only recovery authorized — 2026-10-27

All 120 checker assessments and 50 classifier fits completed, and all five folds' predictions were globally frozen. Historical validation then raised `KeyError` because E020 omitted the derived `category_raw` field used by the existing Category audit. This is a technical failure, not a scientific result. The failed attempt and both failure receipts remain unchanged.

The user authorized repair and continuation. The [additive recovery specification](E020_RECOVERY.md) reconstructs only the missing historical view from the unchanged frozen arrays, preserves all scientific settings and checks, and performs zero new model calls or fits. Separate recovery provenance and aggregate-only publication will disclose the interruption. No interpretation or subsequent experiment is authorized before review.
