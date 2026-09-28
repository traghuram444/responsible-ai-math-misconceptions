# E008 preregistration proposal: why E007 cutoff selection was infeasible

**Status: FOR USER REVIEW — NOT APPROVED FOR EXECUTION, NOT IMPLEMENTED, NOT RUN.**

Prepared 2026-09-25 after the user agreed to proceed with the E008 diagnostic direction. This proposal fixes the detailed analyses before they are computed; execution awaits review. E001–E007, their scientific code, protocols, input fingerprints, folds and results remain unchanged.

## 1. Research question and evidence boundary

Why did E007 find no development-admissible cutoff: insufficient correct predictions at the required coverage/count, limitations of score-based selection, incompatibility of a common cutoff across two questions, or overlapping constraints?

[E007](E007_RESULTS.md) found no admissible cutoff at any registered target. That is a development-feasibility result, not an observed failure of a nonempty policy to transfer. E008 investigates this result using **only the two threshold-selection questions within each existing outer fold**, with the same trained models and one-question temperature-fitting role. It does not evaluate a new policy on outer evaluation questions, train an error predictor, change the target, or seek an improved MAP@3 result.

This is a **prespecified exploratory diagnostic motivated by observed E007 outcomes**, not independent confirmatory evidence. The questions have already been examined across earlier experiments. All interpretations are conditional on these fixed predictions, scores, question roles and constraints.

The competing explanations to distinguish are:

- **Prediction-supply limitation:** even a correctness-informed selector cannot retain enough existing correct predictions to satisfy the requirements on at least one development question.
- **Score-selection limitation:** an oracle could satisfy the requirements, but no allowed score cutoff does so on at least one question. This includes restrictions from tied scores; it is not necessarily a pure ranking defect.
- **Common-cutoff incompatibility:** each development question has at least one admissible cutoff individually, but their admissible cutoff sets have no intersection.

No explanation is assumed dominant. More than one limitation can occur across questions or folds. None identifies mathematical reasoning, label semantics, or representation quality as a unique causal explanation.

## 2. Fixed framework and exclusions

Retain all E007 settings:

- Five frozen outer folds (0–4), seed 20260831, existing dataset/manifest/assignment fingerprints, exact Category:Misconception target.
- Nine training questions per fold. E001's unchanged three-fold inner grouped tuning, three-setting TF–IDF/LR grid, grid tie handling, final fit, inputs and class ordering.
- E007's deterministic hashed calibration subdivision: one temperature-fitting question and two threshold-selection questions. No rotations, extra calibration questions or alternate seeds.
- The original temperature objective, supported-truth filtering, bounded optimizer, and T=1 fallback when no temperature-fitting truth is supported. Unsupported truths remain errors in every diagnostic below.
- Both input arms; confidence-only and support-aware rules; training-frequency reference. Reuse the exact E007 score implementation, including floating-point arithmetic and tie behavior.
- Error targets **10%, 20%, 30%**, with **20% the focal diagnostic** and 10%/30% secondary. Minimum retained count **100** and minimum coverage **10%**, separately for each development question.

The training-label vocabulary and predicted-label support come only from the training role. No expert annotation, new features, learned selector, model/representation replacement, parameter search, risk target, support threshold, or relaxed deployed policy is introduced.

For a particular outer fold, do not predict on, compute scores for, or analyze correctness on its evaluation-role rows. Loading/hashing the complete source file and verifying frozen assignments for integrity is allowed; those checks are not evaluation analyses. A question can have a different role in another frozen fold; do not pool cross-fold error labels to build a model or select a favorable analysis.

## 3. Reconstruction and pre-analysis gates

Published E007 artifacts contain aggregates, not reusable row probabilities or fitted models. E008 therefore needs an approved **development-only reconstruction**, not an E007 rerun. Use new entry points that reuse unchanged training, temperature and score primitives. Do not call E007's `prepare_fold`, because it also predicts on evaluation rows.

Before new diagnostic output for a fold/arm, reproduce the corresponding E007 development record:

- Selected hyperparameters exactly; inner mean MAP@3 within absolute tolerance 1e-10, relative tolerance zero.
- Temperature within absolute tolerance 1e-10, relative tolerance zero; temperature sample/support counts, fallback flag, and derived question-role hash exactly.
- For every rule/target: candidate count, admissible-candidate count, selection status, development-role counts, and selected threshold/null status exactly. E007's stored records have no selected threshold, but the gate must compare against the artifact rather than force a null result.

Verify E007 public result SHA-256 `a0184aba0ac0649569efa56b42d248ebec466a40a6c44c615d2369587c9d3ff7`, its frozen policy artifact SHA-256 `4dce8d85cf66330cc5a131788555b51516b414cccb6ece9c6fd4c275da81950a`, and its approved protocol/configuration hashes. Preserve hashes of E001–E007 scientific records before and after the run. A mismatch stops execution for investigation; it does not authorize new tolerances, refitting choices, or replacement history.

All row-level scores, correctness and labels stay in memory. Reproduction is based on development records only; do not reuse E007's evaluation-rank reproduction gate in this experiment.

## 4. Candidate grid and exact definitions

For each fold, input arm and rule, let T be **0 plus all distinct unrounded float64 scores from the two threshold-selection questions**, sorted ascending, exactly as in E007. Retain every response with score >= t, including every tie. Do not split ties or substitute score quantiles. This same union grid is used for shared-cutoff and individual-question analyses.

For question q and candidate t define:

- N_q: total development responses; n_q(t): retained responses; e_q(t): retained errors.
- Count condition: n_q(t) >=100.
- Coverage condition: 10*n_q(t) >=N_q.
- Risk condition for target a percent: n_q(t)>0 and 100*e_q(t) <=a*n_q(t).

The positive-count requirement in the risk condition is explicit: retaining nobody never satisfies a risk target. Use integer cross-products for all comparisons and rational-risk ordering; no rounded-number or tolerance-based decisions. Empty risk is null.

### A. Constraint-failure decomposition

At every candidate, compute whether each of the three conditions holds on **both** development questions. Record the histogram of all eight Boolean combinations of joint count/coverage/risk satisfaction. Also record the corresponding eight-cell histogram separately for each question.

Report total candidates, candidates satisfying each condition, candidates satisfying both count and coverage, and candidates satisfying all three. The all-three count must equal E007's admissible-candidate count.

As fixed counterfactual diagnostics, report the count of candidates that fail exactly one condition while satisfying the other two: count-only, coverage-only, and risk-only failures. This documents the effect of removing that condition **without deploying, evaluating, or declaring a relaxed policy successful**. Keep all multiple-failure cells visible. If count and coverage requirements are redundant on a question, report that fact using N_q and the effective minimum below; do not invent separate causal attribution.

Counts describe this particular candidate grid. Distinct-score density and tied-score plateaus differ across rules, so candidate-count percentages are not comparable model-performance scores. Do not select a preferred method from these counts.

### B. Individual versus common cutoff feasibility

Define A_q(a) as the set of candidates satisfying all three conditions for question q. Report whether A_0 and A_1 are empty, their cardinalities, and the cardinality of A_0 intersection A_1. Do not publish the candidate arrays or infer feasibility between the minimum and maximum feasible scores: risk can be nonmonotonic and feasible sets disconnected.

Also report these **optimized development diagnostics**:

1. For each question, the minimum observed risk among candidates satisfying its count and coverage floors. Break equal-risk ties by larger retained count, then lower threshold. Report the diagnostic witness cutoff, retained count/coverage/error, and signed risk minus each registered target.
2. For the shared policy, the minimum of max(risk_0(t), risk_1(t)) over candidates satisfying count and coverage on both questions. Break equal-objective ties by larger total retained count, then lower threshold. Report the witness cutoff and both questions' counts, coverage and risks.

When no candidate meets the applicable count/coverage floors, report an explicit no-feasible-floor status and null optimized risk/witness. These witness cutoffs are selected using development correctness and are **not deployable policies or unbiased validation results**. Do not apply them to outer evaluation questions. Their computed risks do not replace E007 results.

### C. Correctness-informed oracle bound

For each model/fold/development question, let C_q be the number of correct existing top-1 predictions and define the effective minimum retained count:

`m_q = max(100, ceil(N_q / 10))`.

An oracle may select any responses using their known correctness, ignoring score ordering and ties. It does not change predictions, recover unsupported true labels, or fit a model. Compute it analytically from counts without constructing or saving a row-level oracle selection.

For a percent error target a, its maximum possible retained count is:

`K_q(a) = min(N_q, floor(100 * C_q / (100 - a)))`.

The oracle meets the count/coverage/error requirements exactly when K_q(a) >=m_q. Report N_q, C_q, m_q, K_q(a), oracle maximum coverage, and this feasibility flag. When m_q<=N_q, also report the oracle's minimum error at the required minimum count:

`max(0, m_q - C_q) / m_q`.

If m_q>N_q, that minimum-count subset is impossible and its risk is null. Use integer ceiling/floor arithmetic. A zero K_q means zero possible coverage, not zero observed retained risk.

The oracle is identical across the two learned routing rules for a given model/arm; report it once per model/arm/fold/question and reference it in comparisons. Frequency has its own fixed-prediction oracle; its duplicate input-arm records must be identical and must not double the apparent evidence.

Compare each question's floor-constrained minimum score-based risk with the oracle minimum risk at m_q, and report their absolute difference where both exist. This is a score-selection/tie-constrained diagnostic gap, not a generalization improvement. An oracle-feasibility failure is a limitation of **these fixed predictions under these requirements**, not proof that the task is impossible.

## 5. Fixed outcome classification and interpretation rules

For every fold/arm/rule/target, report all question-level flags first. Use this mutually exclusive summary classification, in order:

| Condition | Summary code | Permitted statement |
|---|---|---|
| At least one question has oracle K_q<m_q | FIXED_PREDICTION_LIMIT | Even correctness-informed selection cannot meet the requirements on that question with the existing predictions. |
| Both questions are oracle-feasible, but at least one A_q is empty | SCORE_SELECTION_LIMIT | Correct predictions exist in sufficient quantity, but the allowed score cutoffs cannot select an admissible subset on at least one question. |
| Both A_q are nonempty, but their intersection is empty | COMMON_CUTOFF_INCOMPATIBILITY | Individually admissible development cutoffs exist, but no single cutoff works for both questions. |
| The shared intersection is nonempty | REPRODUCTION_MISMATCH | This contradicts the preserved E007 record; stop, do not reinterpret it as an E008 improvement. |

The priority order makes fold counts exclusive; it does not erase mixed explanations. Independently report, for each question, whether the oracle is infeasible and whether the oracle is feasible but A_q is empty. Keep the joint constraint histograms visible. In particular, one question's fixed-prediction limit may coexist with another question's score-selection limit.

No binary classifier-performance success criterion is proposed. E008 is complete only when the registered diagnostic grid and reproduction checks are complete and verified. Finding no new remedy, or different explanations across folds, is a valid outcome. Do not choose a next model automatically based on one favorable subgroup; any intervention requires a separate reviewed protocol.

## 6. Reporting and uncertainty

The complete comparison grid has five folds, two input arms, three routing rules and three targets: 90 fold/arm/rule/target records, with two development-question role slots per record. Frequency is duplicated across arms only for alignment and identified as the same reference. Report development questions as anonymous within-fold role indices 0/1, not student IDs or raw text. These ten development-role slots per arm are not ten independent new questions; question identities can recur across folds.

Publish, in order:

1. At the focal 20% target, counts out of five folds for each outcome code, for each arm/rule separately.
2. The same complete summary for the 10% and 30% targets, without replacing the focal result.
3. All fold-level constraint histograms, individual/shared feasibility flags and optimized development-risk summaries.
4. Both role-index question records per fold, including oracle bounds and the score-selection diagnostic gap.

For numeric fold-level quantities, give all five values, equal-fold mean and sample SD (ddof=1), plus the defined-fold count. Within a fold, where a two-question mean is reported, weight the two questions equally; do not treat rows or repeated question-role slots as independent samples. Undefined values remain null; SD is null with fewer than two defined folds. Category counts are counts out of five, not hypothesis-test evidence. No bootstrap intervals, permutation tests, p-values or population guarantees are proposed.

All analyses A–C and the outcome classification are fixed in advance of E008 computation, but exploratory relative to the already observed E007 failure. Additional targets, minimum-count/coverage sweeps, alternate score functions, calibration-role rotations, learned routers, subgroup searches, outer-test oracle curves, new MAP@3 comparisons, and qualitative examples are outside scope. No new support-stratum or calibration analysis is added; the existing training support definition is used only where the unchanged score requires it.

## 7. Implementation, verification, and publication after review

- Create E008-only analysis, tests and configuration; do not edit E001–E007 scientific files or results. Lock the reviewed protocol/configuration and commit tested code before any new MAP analysis.
- Synthetic tests must cover exact risk boundaries, zero-retention risk, tied scores, disconnected feasible sets, overlapping constraint failures, independently feasible questions with no common cutoff, and all three diagnostic outcome classes.
- Verify oracle formulas against exhaustive enumeration on small invented examples, including zero correct, all correct, N<100, and nonintegral coverage/error boundaries. Compare optimized score/minimax witnesses against independent exhaustive candidate enumeration.
- Test that E008 never predicts on the current outer evaluation role, that development roles reproduce E007, and that the analysis/export cannot serialize response text, row identifiers, score arrays, predictions, fitted weights or oracle selections.
- Expect approximately 100 classifier fitting calls, as in E007, because saved aggregates are insufficient to reconstruct the needed score/correctness relationships. A provisional **10–20 minute compute estimate**, excluding implementation/testing, is anchored to E007's 550.6-second run, not guaranteed.
- Use the existing audited Docker image with UID/GID 10001, network disabled, read-only project/data and only a new `artifacts/e008/` output mount writable. Do not install packages, download models, change host settings, or touch unrelated projects.
- Use a read-only active-run terminal monitor with the repaired bounded-read behavior; at-most-hourly notifications while active, plus completion/failure. No idle monitor. Record actual runtime and any monitor interruption honestly.
- Export only aggregate counts, Boolean flags, scalar diagnostic witnesses/bounds, summary statistics, hashes and provenance through a strict allowlist. Never publish all candidate thresholds: distinct-score arrays can effectively disclose row-level scores.
- Validate grid completeness, reproduction, rational decisions, count partitions, oracle bounds and historical hashes. Run tests and privacy/secret/path scans, then publish the sanitized result with a separate descriptive commit. Preserve failures and prohibit silent retries.
- Present aggregate and all fold/development-question results before interpretation or proposing a new experiment. E008 does not authorize a learned error predictor or an outer-test policy evaluation.

## Review checkpoint

Review the eight-cell constraint decomposition, separate-versus-shared cutoff comparison, correctness-informed oracle definition, and fixed outcome classification above. The error targets, count/coverage floors, training/calibration roles, models and scores are unchanged from E007. No E008 diagnostic results have been computed.
