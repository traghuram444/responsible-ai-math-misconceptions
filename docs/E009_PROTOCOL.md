# E009 proposal: learning reliability from question-held-out errors

**Status: DRAFT FOR USER REVIEW — NOT LOCKED, NOT IMPLEMENTED, NOT RUN.**

Prepared 2026-09-28 after the user agreed to proceed with the learned-reliability direction. That agreement authorizes preparing this specification; the new choices below require review before execution. E001–E008 scientific files, results, folds and protocols remain unchanged. No E009 MAP predictions, features, timing pilot or model fits have been computed.

## 1. Research question, evidence and hypotheses

Can a small reliability estimator, trained on errors made on questions excluded from classifier training and tuning, select useful low-error subsets on unseen questions when the misconception classifier remains fixed?

E008 found sufficient correct predictions for a correctness-informed selector to satisfy the minimum retained count with zero error in all 30 development model/question-role records. However, at the focal 20% error target, every arm/rule had a score-selection limitation in all five folds. That oracle uses unavailable correctness; it does not establish that an observable or learnable selector exists. E008's optimized development risks are not held-out performance. Its diagnostic evidence motivates this proposal, not a claim that E009 will succeed.

The scientific intervention is **learning a selection score**, not changing the exact-label classifier, its representation, the labels, or the evaluation requirements.

- **H1, primary, separately for each input arm:** a development-selected learned-reliability cutoff targeting 20% error meets the unchanged count, coverage and risk requirements on all 15 outer evaluation questions.
- **H2, prespecified secondary:** learned reliability separates correct from incorrect held-question predictions differently from the fixed calibrated-confidence, raw-confidence and support-aware scores. Report paired correctness-AUROC differences, including negative differences; no secondary ranking result substitutes for H1.
- **H3, prespecified secondary:** the unchanged 10% and 30% targets characterize feasibility and transfer without replacing the 20% result.

This is a prospective specification of a new experiment, but **not independent confirmatory evidence**: these 15 questions and earlier results have repeatedly informed project decisions. H1 is a fixed confirmatory-style decision rule within a reused benchmark. All uncertainty remains descriptive. No claim of a novel reliability-learning algorithm, educational safety, reviewer benefit or K–12-wide generalization is proposed.

## 2. Literature basis and novelty boundary

Kamath, Jia and Liang train a correctness calibrator for selective question answering under domain shift, including errors on a separate known shifted distribution. Their positive results motivate learning from held-question errors; they do not show that it will work for MAP. [ACL 2020](https://aclanthology.org/2020.acl-main.503/)

Varshney, Mishra and Baral compare selection methods across 17 NLP datasets and multiple distribution settings; no method consistently and substantially beats maximum probability across all settings. This motivates retaining simple score controls and negative results. [Findings ACL 2022](https://aclanthology.org/2022.findings-acl.158/)

This bounded source check extends the [existing literature review](RESEARCH_REVIEW_2026_09.md); it is not an exhaustive novelty search. The intended contribution is the MAP-specific, leakage-controlled evidence and reproducible failure/success analysis, not priority for abstention or correctness prediction.

## 3. Frozen outer framework

Retain the exact frozen five QuestionId folds, seed 20260831, both input arms (`explanation_only`, `question_plus_explanation`), exact `Category:Misconception` target, and the E007 roles:

| Role | Questions per outer fold | Permitted use |
|---|---:|---|
| Training | 9 | Classifier fitting/tuning, reliability-training cross-fitting, feature-reference data, scaler and reliability fit |
| Temperature | 1 | Original classifier temperature fit only |
| Threshold selection | 2 | Select scalar cutoffs, not features, router weights or hyperparameters |
| Evaluation | 3 | Apply frozen cutoffs and report results; no fitting or selection |

The one/two calibration subdivision uses the unchanged E007 SHA-256 ordering and role hashes. No alternate allocation, rotation, seed or new fold is allowed. Use the same author-release input and frozen fingerprints:

| Input | SHA-256 |
|---|---|
| Training CSV | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |
| E007 public reference | `a0184aba0ac0649569efa56b42d248ebec466a40a6c44c615d2369587c9d3ff7` |
| E007 frozen policies | `4dce8d85cf66330cc5a131788555b51516b414cccb6ece9c6fd4c275da81950a` |
| E008 public reference | `966e775a74f5d15fa0f2c253ee7a06f1bec9ab34cbf4812ae4d6a5f2180973ea` |

The final nine-question classifier retains unchanged E001 three-fold grouped tuning, three-setting TF–IDF/logistic grid, grid-order tie handling, final fitting, class order and text construction. Do not reuse historical fitted objects or evaluation results for fitting. Temperature uses the original objective, supported-truth filtering, bounds and T=1 fallback. Unsupported truths remain errors everywhere outside that historical temperature-fitting objective.

## 4. Leakage-safe reliability-training examples

Perform this construction independently for each outer fold and input arm, using only its nine training questions.

1. Canonicalize their QuestionIds with the unchanged E007 integer canonicalization. Sort by SHA-256 of UTF-8 `E009|fold={fold}|QuestionId={qid}|seed=20260831` (no newline), breaking digest ties by ascending numeric ID. The first three questions form reliability cross-fit block 0, the next three block 1, and the last three block 2. This new **inner** subdivision leaves every outer role unchanged. It fixes exactly six fitting and three held questions per block, without inspecting performance or labels. Both input arms use the same blocks.
2. For each block, set aside all responses from its three held questions. On the remaining six questions, independently rerun the unchanged E001 three-setting hyperparameter search using three-fold GroupKFold and refit the selected model on those six questions.
3. Compute the five features in section 5 and top-1 predictions only for the held block. Define the reliability target as 1 if that prediction equals the existing exact label, otherwise 0. A true label absent from those six fitting questions is necessarily an error and is retained in reliability training.
4. Concatenate the three held blocks in original source-position order, used only for deterministic alignment. Every training response has exactly one out-of-question feature/target record. Fit one scaler and one reliability estimator on this combined table.

**Critical exclusions:** do not use in-sample classifier errors; do not reuse the final nine-question classifier's selected parameters in a cross-fit block; do not fit a vectorizer, support count, similarity reference, scaler or selector on outer calibration/evaluation responses. Even unsupervised vocabulary fitting on held questions is excluded. No cross-outer-fold pooling of correctness records is allowed. Source positions and QuestionIds are never features.

Hyperparameter selection can otherwise leak a held question's labels into its purported out-of-fold prediction. Independently tuning within each six-question fitting set avoids that path. Inner-validation failures retain E001's existing handling; failure of every grid setting stops the experiment rather than changing the grid.

Cross-fit classifiers use six questions, whereas the final classifier uses nine. Feature distributions can therefore shift between reliability training and deployment. This is a prespecified limitation, not authorization to recalibrate or retune on evaluation questions.

## 5. Exactly five prediction-time features and one estimator

Let p be the classifier's **raw, un-temperature-scaled** probability vector over its K training classes; let p1 and p2 be its largest and second-largest probabilities, with p2=0 if K=1. Let yhat be the class chosen by the original class-order argmax. Counts and text references below come only from the fitting set of the classifier that produced p (six questions during cross-fitting; nine for final use).

| Feature, fixed order | Exact definition |
|---|---|
| Raw confidence | p1 |
| Raw margin | p1 - p2 |
| Normalized entropy | `-sum(p_k * log(p_k)) / log(K)`; zero-probability terms are zero; define 0 if K=1 |
| Predicted-label support | `log1p(count(yhat)) / log1p(max_class_count)` |
| Maximum training-text similarity | Maximum cosine similarity between the response's existing arm-specific TF–IDF vector and any fitting-response vector, using that classifier's fitted vectorizer and its L2 normalization |

Calculate similarity against **all** fitting rows, in fixed chunks of 128 query rows; retain only each maximum in memory. A zero query vector gives similarity 0. Clip numerical cosine roundoff to [0,1]; other nonfinite features stop execution. Do not retrieve neighbor labels or publish neighbor identities. No new vocabulary, encoder, text field, correctness rubric, feature interaction, polynomial expansion or feature-selection procedure is permitted.

These are label-blind signals at prediction time, not detectors of unsupported true labels. Question text may dominate similarity in the question-plus-explanation arm; both arms remain separately reported rather than selecting whichever looks favorable.

**Why raw probabilities:** raw features are available under the same construction during cross-fitting and final prediction, without fitting extra temperatures on the held blocks or using the outer temperature question to construct router-training examples. The historical temperature fit is unchanged and still supplies the original confidence/support-aware controls and retained classifier calibration metrics. A raw-confidence control below prevents improvements over calibrated confidence alone from being attributed automatically to reliability learning.

Reliability estimator specification:

- Target: correctness (1=correct, 0=incorrect); score is predicted probability of class 1, higher means retain.
- One StandardScaler (`with_mean=True`, `with_std=True`), followed by binary LogisticRegression: L2 penalty, C=1.0, solver=lbfgs, fit_intercept=True, tol=1e-4, max_iter=2000, class_weight=None, random_state=20260831, n_jobs=1.
- Give each of the nine training questions equal total weight: response weight `N / (9 * N_q)`, where N is the complete cross-fit table size and N_q is that question's row count. Weights sum to N. Apply the same weights to scaler fitting and logistic fitting. Do not reweight correctness classes or target deployment prevalence.
- StandardScaler's fixed implementation handles zero-variance columns with unit scale; no column dropping or alternative scaler.
- No router hyperparameter tuning, CV selection, feature search, alternative estimator or post-hoc calibration. C=1.0 is a fixed design choice, not a selected optimum.
- If all cross-fit correctness labels are identical, record `CONSTANT_CORRECTNESS_FALLBACK` and emit that constant (0 or 1). Do not sample extra questions or substitute a classifier. Record class counts and fallback status.
- A reliability-fit convergence warning, nonfinite coefficient/score or failed input contract stops execution. Do not increase iterations or change solvers during the run. Legacy classifier fitting retains its historical behavior; count its warnings transparently.

Standardization/sample-weight and estimator semantics use the installed scikit-learn 1.5.2 implementation: [StandardScaler](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.StandardScaler.html), [LogisticRegression](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegression.html). No dependency upgrade is authorized.

## 6. Fixed controls and cutoff selection

Five routing rules per arm:

1. `learned_reliability`: the new estimator's correctness score.
2. `confidence_only`: unchanged E007 maximum temperature-scaled probability.
3. `support_aware`: unchanged E007 confidence times predicted-label support factor.
4. `raw_confidence`: maximum raw classifier probability, with the same threshold policy as every other rule.
5. `frequency`: unchanged training-frequency classifier and its constant maximum probability.

Only the fifth rule changes the underlying classifier; its duplication across input arms is the same reference, not extra independent evidence. The other four route identical fixed top-1/top-three predictions. No control is removed if it outperforms learned reliability.

Use the exact E007 cutoff algorithm on the two threshold-selection questions, separately for targets 10%, **20% primary**, and 30%:

- Candidate grid: 0 plus distinct unrounded float64 scores, ascending; retain score>=cutoff with every tie.
- Each development question must have n>=100, 10*n>=N and 100*errors<=target_percent*n. Integer comparisons, no tolerance or rounding.
- Maximize total retained development count among admissible candidates, breaking ties by smallest cutoff; search every candidate, not a monotonic-risk approximation.
- If none is admissible, record null cutoff / `NO_ADMISSIBLE_THRESHOLD`, defer all evaluation rows, report zero coverage and null retained risk/accuracy/calibration.
- Freeze all rules' policies for all folds/arms in an aggregate-only artifact before reading evaluation correctness or computing evaluation metrics. Label-blind evaluation probabilities/features may be computed earlier and held in memory, but selection functions must not receive evaluation labels or batch statistics.
- Apply the frozen cutoff unchanged to each evaluation response. No test-batch quantiles, rank quotas, tie splitting, subgroup cutoffs or question-specific adjustments.

The learned score is not a risk certificate. Threshold selection on two questions is optimized development performance; it can fail to transfer even if it meets every development requirement.

## 7. Outcomes, metrics and fixed interpretation

### Primary decision

For each learned input arm separately, useful empirical transfer at 20% requires all five development policies to be admissible and **every one of the 15 evaluation questions** to meet retained n>=100, coverage>=10%, and exact-label error<=20%. Retain the same criterion for each control and the two secondary targets. Do not choose a winning arm or replace the primary target after inspection. These are research criteria, not acceptable-error standards for educational deployment.

| Observed pattern | Registered conclusion |
|---|---|
| No admissible development cutoff in any fold | The registered learner did not find an admissible policy for that fold; transfer of a nonempty policy is unassessed there |
| Development cutoff exists, but evaluation count/coverage fails | Registered useful-coverage criterion failed |
| Any nonempty evaluation question exceeds target | Registered risk-transfer criterion failed; report magnitude even if its retained count is below 100 |
| AUROC improves but H1 fails | Descriptive ranking improvement, not reliable automation or primary success |
| H1 passes for an arm | Descriptive benchmark success only; further independent questions are needed |
| No ranking or transfer improvement | Negative evidence about this fixed learner/features/protocol, not proof that reliability is unlearnable |

Report all coexisting failures. Do not attribute failure uniquely to mathematical reasoning, label semantics, calibration or training-size shift. Do not relax requirements or move to a more complex router within E009.

### Complete fixed-threshold outputs

The grid contains **200 fold/arm/rule/target records**: 5 folds x 2 arms x 5 rules x (unfiltered + 3 targets). Include each record's three evaluation-question records (600 total), including empty policies. Use existing public aggregate QuestionIds only for evaluation summaries; development and inner-training groups use anonymous role/block indices.

Reuse the E007 metrics/eligibility definitions: original and retained counts; errors; coverage/review fraction; accuracy; MAP@3; risk and signed risk-minus-target; maximum class confidence; 10-equal-width-bin ECE; union-label-corrected multiclass Brier. Calibration metrics always use the original temperature-scaled classifier probabilities, not the router score. Frequency remains unscaled.

Report the unchanged unsupported, rare (1–19), frequent (>=20), and nested well-supported (>=20 across >=2 training QuestionIds) true-label strata after global selection. True-label support is never a feature. Keep empty strata visible. ECE/Brier require n>=200, >=20 correct and >=20 incorrect; otherwise null with explicit eligibility reasons. This excludes unsupported exact labels by construction, not because they are safe.

Report E007-style development/evaluation risk gaps. Paired fold comparisons at the same target are learned minus each of calibrated confidence, raw confidence, support-aware and frequency. Show both coverage values alongside coverage/risk differences; risks condition on potentially different populations, not matched causal effects. Pair risk only where both are defined.

### Reliability diagnostics (prespecified secondary, not tuning objectives)

- On unfiltered evaluation data, report correctness AUROC for each rule at fold and question level, eligible only with n>=200 and >=20 correct and >=20 incorrect. Constant scores yield 0.5 when eligible. Report null and reasons otherwise.
- Report paired fold AUROC differences between learned reliability and calibrated confidence, raw confidence and support-aware. These four rules share the same correctness target. Frequency's AUROC has a different correctness target and is contextual only, not a paired discrimination comparison.
- For learned reliability only, report mean predicted correctness, binary Brier `mean((score-correct)^2)` and 10-bin binary ECE on unfiltered and each retained population, at fold/question/stratum levels under the same calibration eligibility rule. Distinguish these from classifier multiclass Brier/ECE. Equal-question training weighting does not guarantee row-weighted calibration on deployment questions.
- No new risk–coverage curve sweep, fixed-budget E006 rerun, oracle experiment, feature ablation, subgroup search or response examples. AUROC is not a substitute for fixed-cutoff risk/coverage.

### Aggregation and uncertainty

Within a fold, pool its evaluation rows as in E007; also report every question. For each numeric fold metric give all five values, equal-fold mean, sample SD (ddof=1), and defined-fold count. Null risks stay null; fewer than two eligible folds means null SD. Paired summaries use the eligible intersection and show its denominator. Report admissible folds/5, count/coverage successes/15, risk successes/15, nonempty questions, target exceedances and maximum observed question risk.

No response-level confidence intervals, bootstrap, permutation tests, p-values or independence assumptions. A pooled mean cannot override an individual-question primary failure. Results are exploratory in the broader research program; no unregistered exploratory analyses are added during the run.

## 8. Reproduction, leakage tests and publication gates

Before execution, lock the reviewed document and exact configuration hashes and commit the tested E009 implementation. Preserve E001–E008 hashes before/after. Verify original inputs, E007/E008 references and their approved protocol/configuration hashes. No silent reconstruction of mismatched inputs.

Before accepting new development policies, reproduce the final classifier's E007 selected hyperparameters, inner score, temperature, role hashes/counts and all original rules' development policies using the unchanged E008 gate (numeric tolerance absolute 1e-10, relative 0; exact discrete matches). New raw-confidence/learned policies are not expected to reproduce an old result.

After every policy is frozen, verify the unchanged unfiltered classifier/frequency accuracy and MAP@3, and all original rules' E007 evaluation records, against the historical reference with exact counts/status and absolute 1e-10 numeric tolerance (relative 0). A mismatch stops execution and publication as a completed experiment; no tolerance change or silent retry.

Synthetic tests must cover:

- deterministic 3/3/3 cross-fit allocation, disjoint roles and exactly one held-question prediction per training row;
- a spy showing both vectorizer fitting and hyperparameter selection exclude the held block;
- training-only support/similarity references, zero vectors, entropy/margin boundaries and fixed feature order;
- equal-question weights, scaler fit boundary, constant-correctness fallback, nonfinite/convergence failure handling;
- changing evaluation labels cannot change features, weights, selected policies or any response's retain/defer decision; changing evaluation batch composition cannot change another response's score or decision;
- unsupported truths remain reliability-training/selection/evaluation errors; no truth support enters routing;
- inclusive ties, exhaustive cutoff search, exact risk/count/coverage boundaries, empty policies and calibration eligibility;
- independent arithmetic checks, full-grid completeness, frequency duplication and strict aggregate export rejecting response text, row identifiers, features/scores/probability arrays, candidate arrays and fitted parameters.

Keep row-level features, errors, probabilities and fitted models in memory only. Publish aggregate fold/block counts, selected classifier settings, role hashes, temperatures, scalar cutoffs, convergence/fallback summaries, metrics and provenance through a strict allowlist. Do not serialize router coefficients, scaler statistics, neighbor identities or prediction arrays. Aggregate inner-block counts are audit information, not an additional model-selection analysis. Scan public changes for data excerpts, secrets and local paths; verify public file hashes after pushing only to the existing personal repository. Preserve failures and do not rerun without reviewed authorization.

## 9. Resources, execution and stopping point

Expected classifier-fitting calls: per outer fold/arm, 3 cross-fit blocks x (9 grid-CV fits + 1 six-question final fit), plus 9 original grid-CV fits + 1 nine-question final fit = **40**, or **400** over both arms and five folds. Up to **10** additional tiny binary reliability fits; constant fallbacks are counted separately. Feature construction adds sparse similarity computations but no embedding model or GPU work. Report actual attempted/successful fit counts and failures.

A provisional **30–60 minute compute estimate** excludes implementation/testing. It is anchored to E008's 535-second, 100-fit run, not a timing pilot; smaller cross-fit training sets may be faster and similarity computations may be slower. No runtime result is promised and no MAP timing run is authorized by this draft.

Use the existing audited image `sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c`, UID/GID 10001, disabled network, read-only project/data, fixed single-thread numerical settings, and only a new E009 artifact mount writable. No packages, models, host settings or unrelated files change. If resource limits prevent the locked plan, stop; do not reduce folds/features or silently substitute a method.

Run the repaired read-only terminal monitor during approved execution only. Report actual cross-fit/model/policy stages; notifications at most hourly while active plus completion/failure/required intervention. No idle monitor or invented time-based percentage.

After verification, publish the complete aggregate and fold/question tables in a separate results commit regardless of outcome. Present results before interpretation or proposing another experiment. No automatic escalation to larger models, expert annotation or new data acquisition is included.

## Review checkpoint

The newly proposed choices are the **3/3/3 inner question cross-fit with independent nested classifier tuning**, **five raw-probability/support/similarity features**, **fixed weighted logistic reliability estimator without tuning**, and **raw-confidence control**. The outer folds, final classifier, historical temperature procedure, risk targets, count/coverage floors and all-15-question success criterion remain unchanged. Review these choices before approving E009 implementation and execution.
