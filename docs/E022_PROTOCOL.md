# E022: transfer of review cutoffs for correctness-conditioned predictions

## Review status and scope

Prepared **2026-10-29**, against completed E021 commit `cfbec27c49114f15edddc92df4c2b3c6e578d3e0`. **Proposed preregistration for user review; execution is NOT approved.** The user's agreement to proceed authorizes this protocol and an append-only experiment-log entry. It does not authorize implementation, an attempt directory, real-data fitting, calibration, cutoff search, scoring or monitoring yet. No E022 result is known.

Preserve E001–E021, all prior protocols/code/results/locks, failed and recovered attempts, README and frozen folds unchanged. E018 remains blocked. After approval, use only additive E022 files and a new exclusive attempt. Historical scientific helpers may be imported read-only, never patched. No external model calls, downloads, annotations, human reviewers, new classifier or ensemble-weight selection are included.

Research question: **Can a confidence cutoff selected on development questions identify a useful subset of correctness-conditioned exact-label predictions that meets a prespecified empirical error target on every held-out question?**

E021 reported L7 MAP@3=0.580689 and fixed C50=0.579796 versus frequency=0.539215. At its retrospective 50% review budget, C50 retained accuracy was 0.686455, with substantial remaining errors. That analysis ranked each evaluation batch to allocate a budget; it did not transfer a cutoff selected without evaluation outcomes. E022 explicitly revisits E007's threshold-transfer question using the stronger fixed prediction pipelines. It does not introduce a new selective-classification algorithm or independently confirm generalization after repeated use of the same 15 questions.

## Questions, hypotheses and decision priority

There are **two separately reported primary-arm decisions** at the historical 20% error target:

- **H1-L7:** L7 has a development-admissible cutoff in every fold, and every one of the 15 evaluation questions meets error <=20%, retained count >=100 and coverage >=10%.
- **H1-C50:** the identical criterion, evaluated separately for fixed C50.

Report both results, including a failure of either. Do not choose the successful arm after inspection, combine them into an unspecified overall success, or replace either with the tuned T ensemble. There is no formal familywise inference; these are descriptive, prespecified benchmark decisions. The frequency arm receives the same decision calculation as a contextual negative control, not a third learned primary hypothesis.

**Secondary:** apply the identical rules at the previously registered 10% and 30% error targets, separately for each arm. Also characterize calibration, true-label support, coverage and development-to-evaluation risk gaps. Secondary targets do not rescue a failed 20% decision. E021's +0.020 MAP@3 margin is not a criterion for this different risk-transfer experiment.

The 10%, 20% and 30% targets are inherited research stress tests, not educational safety standards or permission to automate student decisions. A result with zero retained predictions is not success. No additional meaningful-effect threshold is introduced.

## Frozen population and input identities

Use all 36,696 original rows in source order, the exact `Category:Misconception` label including literal `NA`, the same 15 QuestionIds, five outer folds 0–4, and seed 20260831. Each outer fold keeps nine training, three original calibration and three evaluation questions. Every row belongs to exactly one outer evaluation role. No row exclusions, label changes, split regeneration, question rotation or favorable subset selection are permitted.

| Evidence | Required SHA-256 |
|---|---|
| Training CSV | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen split manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen fold assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |
| E007 protocol, canonical LF bytes | `699a3e5691a2bf41bd27311e11f94f548aaff5466e497167ed702196ea21676e` |
| Completed E020 G7 cache, 60 pairs | `00830d9a7a64735682fce41655b55adf6c088105c339913eac4e604b4275bb13` |
| E021 aggregate JSON | `7dee7d0d8772744524630b9358b14a685aec3ac5cb2bef7ca01c396c022dde3c` |
| E021 frozen development receipt | `92d843364bdb95cf044260fc665adffbd46b618fe50178d76b7b0545474dd0cf` |
| E021 additive lock, byte hash | `6a64122304e4c1b1b9bd6d5c368afd13ad436b13f97f4b5c5c5200689b3c6a46` |

Verify the complete E020 cache catalogue/completion/input provenance using the original validators, alongside all nested preservation locks. The fixed checker is the E020 Qwen/Qwen2.5-Math-7B-Instruct checkpoint revision `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`. Reuse its existing question/selected-answer soft scores with the original normalization and mapping. Zero new LLM calls, model loading, prompts, score calibration, parsing changes or model-size comparisons are allowed. Cached signals use no student explanation or target label; do not reinterpret them as independently human-verified correctness.

## Fixed prediction pipelines and reconstruction

Let F be exact-label frequencies in the applicable outer training role, L the unchanged historical full-context word TF-IDF/logistic raw distribution, and s=(s_false,s_true,s_unknown) the frozen G7 signal. Use the E020 soft projection unchanged:

`S(P,s) = s_unknown * P + s_false * P_false + s_true * P_true`.

Here P_b is P normalized within the training candidate inventory whose Category has correctness prefix b. A missing prefix inventory falls back to P and is counted; zero/nonfinite mass inside a nonempty prefix is a technical failure. Exact one-hot unknown returns P by the existing explicit branch. A valid C readout retains its complete soft vector; technical unknown and valid C are not conflated. No hard checker, smoothing or new fallback policy is added.

| Public arm | Raw prediction construction | Selection score |
|---|---|---|
| F | Training empirical frequency | Maximum unscaled probability |
| L7 | S(L,s) | Maximum probability after its E022 temperature |
| C50 | 0.5*S(F,s) + 0.5*S(L,s) | Maximum probability after its E022 temperature |

G7 and L are intermediate components, not additional routed result arms. Mix raw distributions before temperature fitting. C50's weights are exactly 0.5/0.5; there is no T arm or weight search. F remains unscaled. No support-aware score, learned reliability model, entropy/margin score, special unknown deferral, predicted-correctness cutoff, per-question policy or score ensemble is evaluated.

Reconstruct the same L once per fold, shared by L7 and C50. Use E011/E021's exact tagged QuestionText, MC_Answer and StudentExplanation input, historical missing-to-empty conversion and vectorizer/classifier defaults. No QuestionId, source position, target-derived field or checker score enters L's features. Sorted candidate labels and support inventories use only the applicable training rows; neither calibration nor evaluation labels expand them.

Repeat exactly the historical three-fold GroupKFold search within nine training questions, grouped by QuestionId converted to strings. The ordered grid is (ngram_range=(1,1), min_df=2, C=0.5), ((1,2),2,1.0), ((1,2),5,2.0). Select highest equal-inner-fold raw L MAP@3; first grid entry wins an exact tie. Use sublinear_tf=True, max_iter=2000, class_weight=None, random_state=20260831, n_jobs=1 and the unchanged pinned defaults. Refit on all nine training questions. Exactly nine inner fits plus one refit per fold gives **50 classifier fits total**, not 50 per arm. No extra reliability fits or joint calibration/hyperparameter selection. Any fit warning stops the attempt.

Reconstruction is needed to obtain probabilities for the disjoint temperature and cutoff questions, which E021's evaluation prediction archive alone does not supply. It is not permission to select different text settings. Reproduce all historical grid scores, chosen settings and raw evaluation distributions; any mismatch stops the attempt.

## Explicit calibration subdivision

Reuse E007's exact deterministic allocation inside each existing three-question calibration role:

| Role | Question count | Allowed use |
|---|---:|---|
| Original training | 9 | Vocabulary, classifier tuning/fitting, frequencies, support counts |
| Temperature fitting | 1 | Separate scalar temperatures for L7 and C50 |
| Cutoff selection | 2 | Select each arm/target cutoff from development errors |
| Original evaluation | 3 | Apply frozen predictions/cutoffs; score only after global freeze |

Canonicalize QuestionId as a nonnegative integer base-10 string without leading zeros; reject booleans, nonintegral, negative or nonfinite identifiers. For each fold, sort its three calibration questions by the SHA-256 hexadecimal digest of UTF-8 `E007|fold={fold}|QuestionId={qid}|seed=20260831`, with no newline; break digest ties by numeric QuestionId. The first question fits temperatures; the remaining two, in this same order, have anonymous cutoff-role indices 0 and 1. **Keep the E007 namespace; do not replace it with E022.** Reuse the historical calibration_roles helper and verify the derived role hashes against E007 development receipts. No allocation search or rotations.

Fit one temperature for each of L7 and C50 on the single temperature question, using the historical supported-truth NLL objective, probability clipping at 1e-12 and bounded log-temperature [-3,3]. The learned temperatures are then applied unchanged to the two cutoff questions and three evaluation questions. If no temperature-question truths are in the training inventory, use the existing T=1 fallback and record it. Nonfinite/invalid inputs, optimizer failure or nonpositive temperature are technical failures. No borrowing cutoff/evaluation labels or selecting calibration methods by observed performance.

Temperature fitting excludes unsupported truths only from that NLL objective. **Cutoff search and every evaluation risk include unsupported truths as errors.** Calibrated probability maxima, not support-weighted values, are the only learned routing scores. Use float64 and original argmax/argsort(-p) top-three conventions on sorted candidate labels. Require top-1 and ordered top-three ranks to remain unchanged after temperature application; a violation is a technical gate failure, not a reason to change tie handling.

This subdivision deliberately changes E021's three-question temperature-fitting sample. E022 is therefore **not a reproduction of E021's calibrated probabilities, ECE or review decisions**. Raw distributions and unfiltered rankings must reproduce; E022 calibration is separately reported. The report must preserve this distinction. Do not transplant E021's temperatures fitted on all three questions into the cutoff experiment.

## Exact cutoff selection and freezing

For each fold, each arm in [F,L7,C50], and each risk target in [10,20,30] percent, reuse E007's select_cutoff algorithm unchanged:

1. Candidates are 0 and every distinct unrounded float64 selection score across the two cutoff questions, sorted ascending. No quantile grid, bins, additional values or infinity.
2. Retain score >= cutoff, including the full tie group. No row-ID tie splitting or dependence on evaluation-batch composition.
3. A candidate is admissible only if **each** cutoff question has retained n>=100, retained n*10>=its original N, and errors*100<=target_percent*retained n. Use integer cross-products, without floating tolerance or rounded comparisons. This is a joint two-question constraint, not pooled development risk.
4. Search every candidate: observed risk need not be monotone. Choose greatest total retained count across the two questions; break ties by the lowest cutoff. Do not choose by MAP@3, ECE, held-out coverage or the other arm's results.
5. With no admissible candidate, record `NO_ADMISSIBLE_THRESHOLD`, null cutoff, and zero retention. Defer all evaluation responses for that fold/arm/target. Risk, accuracy and MAP@3 are null, not zero; review fraction is1. This is a scientific outcome, not a technical failure or authorization to relax requirements.
6. Freeze all **45 policies** (3 arms*3 targets*5 folds), both learned temperatures per fold, selected text settings, candidate inventories, row-aligned predictions and retain/defer masks across all five folds before any E022 evaluation truth access or scoring. Private hashed receipts/arrays may be saved only in the new ignored attempt. Freeze the policy before applying it to evaluation features; all masks must then also be frozen before evaluation truth access. No results from an early evaluation fold may influence later preparation.
7. Apply each cutoff unchanged to each corresponding evaluation response. No forced budget, test-batch quantile, cutoff clipping, adaptive score normalization, question-specific threshold, post-hoc union/intersection of arm masks or transfer of evaluation rows into development.

F uses the same algorithm with its constant maximum training probability, so it retains all or none. Do not give frequency a different target or quota to make it competitive. No G7-specific technical-fallback identity for calibration is needed: G7 is only an uncalibrated intermediate of C50, and both L7 and C50 always follow their own registered temperature rule.

## Reconstruction and leakage gates

Before evaluation, verify original data/assignments/cache hashes, 9/1/2/3 disjoint role counts, row alignment, model selection, derived E007 role hashes and all historical preservation inventories. Verify E021's frozen receipt and each prediction archive hash before loading any comparison arrays. Compare all five folds' raw F/L7/C50 probability arrays, exact class/source/question alignment, predicted labels and ordered top-three indices with E021: probabilities use absolute tolerance1e-10, relative tolerance0; discrete objects match exactly. Reproduce base L's historical selection scores/params separately. Evaluation labels are not necessary for these checks.

After the all-fold global freeze, compute unfiltered exact-label metrics and reproduce E021's raw F/L7/C50 fold/question/support MAP@3 and accuracy, counts and nulls at the same tolerance. E022 final ranks must match its raw ranks. E021 final probabilities/temperatures/ECE/Brier/review orders are not a reproduction target. The label-free preparation path must not receive evaluation Category/Misconception fields. Do not read other outer folds' stored labels or scores to choose the current fold's policy; overlapping outer roles do not authorize cross-fold pooling.

No new evaluation metrics are displayed until freeze and reproduction pass. Prior observations on this benchmark informed the proposal, so these implementation barriers prevent additional leakage during E022; they do not erase the project's adaptive benchmark reuse.

## Complete reporting grid and metrics

Publish the full grids, including empty cells. Original evaluation QuestionIds may appear as public aggregate identifiers; cutoff-selection questions use anonymous role indices. Never publish answers, explanation text, class-by-answer tables, individual decisions, row IDs or private mappings.

- **Development:** 15 arm/fold records with temperature/provenance, role counts/hashes and selected model settings; 45 cutoff-policy records with target, status, cutoff, candidate/admissible counts and both selection-question original/retained/error counts, coverage and risk. The frequency temperature is1 with method unscaled and no claimed fitting sample. For each learned arm report temperature-question total, supported count/fraction, fitted temperature and zero-support fallback flag.
- **Unfiltered reference:** all three arms, raw and E022-calibrated scales, five folds, each pooled fold plus its three questions, crossed with all five support groups: **600 metric records**. These identify the calibration change separately from selection.
- **Retained policies:** all three arms, three targets, five folds, each pooled fold plus its three questions, crossed with all five support groups: **900 metric records** using E022-calibrated probabilities (unscaled for F). Cutoff selection occurs globally before intersecting any true-label stratum. No secondary raw-confidence cutoff search.
- **Decisions:** nine arm/target records, preserving the separate 20% learned-arm primaries and frequency context. Report five fold admissibility statuses, 15 per-question count/coverage/risk flags, complete denominators and the all-question conjunction. Zero retention gives false count/coverage flags and null risk-compliance, never a risk pass. Count questions meeting each requirement and all requirements; report nonempty denominators for risk exceedances.

The unchanged strata use the nine-question training inventory only: all; unsupported (0 examples); rare (1–19); frequent (>=20); well-supported (>=20 over >=2 distinct training questions, nested in frequent). Unknown recipient labels stay unsupported. No threshold is allowed to use the recipient's true-label stratum. Unsupported truth always has zero exact accuracy/MAP@3 and remains in union-label Brier. Retaining an unsupported truth counts as an error even if the correctness prefix is predicted correctly.

For each metric record report original n, retained n, correct/incorrect n, coverage, review fraction, share of retained cases, top-1 accuracy, MAP@3, risk=1−accuracy, mean maximum probability, signed confidence-minus-accuracy, ten-equal-width-bin ECE and corrected union-label multiclass Brier. For targeted policies also report signed risk-minus-target and target-exceeded status. Coverage/review fraction use original n in that stratum and scope; share-of-retained uses all retained rows in that fold/question scope. Empty original strata have null coverage; empty retained groups have null prediction/calibration metrics. Unfiltered groups retain their entire original population.

ECE/Brier require retained n>=200, correct>=20 and incorrect>=20, separately per arm/scale/scope/stratum. Record all failed eligibility reasons; null is not good calibration. Mean confidence needs only nonempty retention. Do not use the selection score as a substitute probability distribution in Brier.

Prespecified paired **fold/stratum** comparisons at each common risk target are L7−F, C50−F and C50−L7: coverage, actual review fraction, risk, accuracy, MAP@3, mean confidence, confidence gap, eligible ECE/Brier, with both arms' original/retained counts and both achieved coverages. Differences use jointly defined values only; show the defined-fold count. These are **225 paired records** (3 contrasts*3 targets*5 folds*5 strata), not comparisons on identical retained responses or at matched coverage. Do not add a test-batch matched-budget policy. Full per-question values remain available in the 900 retained records; no selected-question comparison panel.

For every selected policy, report each of its three evaluation questions' all-row retained risk minus the equal-question mean of the two selected development risks. If either quantity is undefined, report null. This yields **135 gap records**, including nulls for absent policies. Development risk is optimized by cutoff search and is not an unbiased validation estimate.

## Aggregation and descriptive uncertainty

Within each fold, pooled metrics combine its three evaluation questions. Report every fold and every question, then equal-fold means, sample SD(ddof=1), all five fold values and defined-fold count for each arm/target/stratum (or arm/scale/stratum for unfiltered results). SD is null below two defined folds. Include zero-coverage deferral-only folds in coverage averages; average risk/accuracy/MAP@3/calibration only over defined/eligible folds and label these conditional means explicitly. A favorable conditional mean cannot establish all-question success.

Show selected-policy counts out of 5, nonempty questions out of 15, per-question count and coverage passes out of 15, risk exceedances with nonempty denominator, joint passes out of 15, and maximum nonempty question risk for every arm/target. No imputation for undefined risk and no rounding a near miss into a pass. For paired summaries use only jointly defined fold values and disclose counts; separately show both arms' five-fold coverage summaries.

These five overlapping folds and 15 repeatedly examined questions are not independent experimental replications. No bootstrap, response-level confidence intervals, significance tests, p-values, conformal/risk certificates, causal claims, new correlations or role-permutation analyses. MAP correctness remains the existing annotation reference. Potential pretraining exposure and accumulated benchmark adaptation remain limitations. Human-review outcomes are not observed; deferred cases are not assumed to be corrected.

## Confirmatory-style versus secondary boundary

H1-L7 and H1-C50 are the two prespecified primary-arm empirical transfer decisions at 20%. Report them separately with no study-level winner. The 10%/30% decisions, frequency context, calibration/support tables, unfiltered reproduction, paired summaries and development-to-evaluation gaps are prespecified secondary/descriptive analyses. Their results cannot replace the primary outcomes. There are **no exploratory analyses in E022**. Alternative uncertainty scores, calibration methods, cutoffs, mixture weights, risk targets, relaxed floors, handpicked questions and extra ablations require a later reviewed proposal.

## Fixed interpretation rules

| Observed outcome | Permitted interpretation |
|---|---|
| No admissible cutoff in one or more folds | No policy found under the registered development requirements for those folds; transfer is unassessed there. Do not claim evaluation-risk failure for an empty policy or impossibility for every method. |
| Admissible cutoff, evaluation count/coverage fails | The selected policy did not retain the registered useful amount of data on new questions, even if its nonempty risk is low. |
| Admissible cutoff, any nonempty evaluation question exceeds target | Observed risk transfer failed on that question; show magnitude even below the count floor. A favorable mean does not override the all-question criterion. |
| All five policies admissible and all 15 questions meet all three conditions | That named arm/target achieves descriptive benchmark success; no distribution-free guarantee, educational safety claim or human-benefit claim. |
| One learned primary passes, the other fails | Report the two distinct outcomes. Do not retrospectively designate the passing arm as the sole primary or claim both worked. |
| Only a secondary target passes | Secondary trade-off result; the 20% primary decision remains unchanged. |
| Ranking reproduces but calibration/retained risk is poor | Improved exact-label ranking has not established calibrated or reliable selective prediction under this allocation. No claim that calibration alone caused failure. |
| Both learned primaries fail | Preserve both outcomes; do not change targets, scores, role allocation, thresholds or model weights. |
| Integrity, reproduction, warning, schema or runtime gate fails | Technical failure; preserve the attempt and stop for review, without retry, repair-in-place or scientific conclusions. |

## Execution and publication after explicit protocol approval

Before real-data work, add tested E022-only orchestration, strict aggregate schema/publisher and configuration. Capture an additive preservation inventory covering all existing public scientific files and private historical evidence, including the E021 frozen arrays, prior failures/recoveries, old locks and full documentation prefixes. Lock this approved protocol, implementation, inputs, dependencies and reporting specification; commit and publicly verify sanitized preparation before running. Do not overwrite old locks or infer runtime approval from this drafting request.

Use the same E021 CPU statistical Docker image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, Python 3.11.11, NumPy 1.26.4, scikit-learn 1.5.2 and its full dependency lock. Use UID/GID 10001, PYTHONHASHSEED=20260831, numerical threads 1, network none, read-only root/project/data/history, cap-drop ALL, no-new-privileges and tmpfs scratch. Only exclusive new `artifacts/e022_attempt01` may be persistently writable. No host settings, external project files or model downloads change. Refuse an existing attempt; any failure is preserved for review with no automatic restart/resume/retry.

Synthetic tests must verify exact E007 role/hash and cutoff equivalence, rational risk boundaries, inclusive ties, nonmonotone candidate search, two-question joint requirements, absent-policy nulls, F all-or-none behavior, unsupported truths as errors, nested support groups, historical projection identities, fixed mixture order, one-question temperature exclusion, sorted-class rankings, original E021 raw prediction reproduction, complete freeze before truth, schema/grid rejection and safe publication. Changing evaluation labels, order or batch composition must not change a cutoff or an individual response's selection decision after alignment. Test corrupted hashes/failure receipts, no accidental E021 three-question temperature reuse, and monitor isolation. No MAP pilot, exploratory cutoff search or partial real-data fit during implementation.

After approval, the independent read-only terminal monitor is active only during execution. Show actual fits/50, complete policies/45 and scored folds/5, with elapsed time and clearly named phases. No new scored metric before global freeze and reproduction; no stale historical metrics as E022 progress. Routine chat progress at most hourly, immediate meaningful failure/completion, no idle automation. The computational planning estimate is **10–30 minutes**, based on E021's measured approximately 13.6-minute execution; implementation, tests, publication and privacy scans are additional. This estimate is not a pilot or scientific stopping rule.

On completion validate all input/lock/freeze/completion hashes, preservation, historical reproduction, strict aggregate schema and complete grids. Run the full tests and publication/secret/local-path/private-response scans. Publish only sanitized aggregate JSON/tables, configuration/code, provenance and append-only execution/log records in a separate descriptive commit to `traghuram444/responsible-ai-math-misconceptions`. Keep README and all earlier experiment files unchanged. Private frozen probabilities/masks and per-file inventories stay ignored and local. No raw responses, generated reasoning, model weights, individual predictions or row-level identifiers are public. Verify the public commit and show all aggregate/fold/question results before interpretation. No E023 is authorized.

## Prior work and intended contribution

The original [E007 protocol](E007_PROTOCOL.md) and [E008](E008_PROTOCOL.md)/[E009](E009_PROTOCOL.md) already studied this project's cutoff feasibility and reliability limits. E022 deliberately reuses the earlier criterion and role allocation; its changed ingredient is the fixed correctness-conditioned prediction pipeline. It must not be presented as an invention of abstention or a fresh independent replication.

[Liang, Peng and Sun (TMLR 2024)](https://arxiv.org/abs/2405.05160) study selective classification with distribution shifts and non-training confidence scores; E022 does not adopt their proposed margin scores. [Park et al. (AISTATS 2020)](https://proceedings.mlr.press/v108/park20b.html) address calibration under covariate shift; E022 does not adopt their adaptation method or assume that MAP question shift meets that setting's assumptions. These primary-source records were checked on 2026-10-29. This is a bounded context check, not an exhaustive novelty certification.

The proposed contribution is a controlled follow-up asking whether an observed ranking improvement changes the feasibility and transfer of the project's existing review policy, while keeping negative outcomes, unsupported labels and question-level harms visible. New independent questions would still be needed for stronger external-validation claims.
