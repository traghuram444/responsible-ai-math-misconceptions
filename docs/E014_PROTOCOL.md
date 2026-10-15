# E014 controlled shrinkage toward training label frequency

## Review status and scope

Prepared 2026-10-15 for user review. **Protocol preparation only; execution awaits approval of this specification.** No E014 model fitting, mixture selection, or held-out scoring has occurred. Reference revision: `c286731335eea8466c531b2f736a69920870573d`.

E014 tests whether a training-selected mixture can retain E011's useful response evidence while reducing its harmful departures from common-label rankings on unseen questions. Preserve E001–E013, both E012 attempts, all existing scientific code/results/locks, and frozen assignments. This is one bounded experiment, not an ensemble search or authorization for E015.

The design is informed by previously observed results: E011 full-context MAP@3 was 0.511887 versus frequency 0.539215. E013 found an explanation-shuffle decrement of 0.026683 for E011, positive in all five folds, while its gain/loss contributions against frequency were 0.063926 and 0.091253. These observations motivate a shrinkage hypothesis; they do not establish its remedy or cause. The same 15 questions have been repeatedly examined. Prospective rules below prevent within-run selection on evaluation outcomes, but cannot turn this reused benchmark into independent confirmation.

## Research questions and hypotheses

**H1, sole confirmatory outcome:** a mixture weight selected entirely within each outer training fold yields meaningfully better all-row exact Category:Misconception MAP@3 than training-label frequency on the unchanged held-question evaluation folds.

**H2, prespecified secondary:** the selected mixture reduces the MAP@3 loss contribution relative to unmodified E011 without eliminating all of its gain contribution. Report each contribution and change; no secondary success rule substitutes for H1.

**H3, prespecified secondary:** recipient explanations still improve the selected mixture's ranking over explanations shuffled within the same question and selected answer. Report original-minus-shuffled MAP@3 without a new binary threshold. A utility gain and an explanation-dependence effect are different findings; neither implies mathematical reasoning.

Exploratory questions concern probability calibration and confidence-based review. This experiment does not train a new representation, repair E012 calibration, infer the correct answer, introduce expert annotations, or expand the label space.

## Fixed predictor and endpoints

For each training partition, let `p_F` be its empirical exact-label prevalence and `p_L(x)` the unchanged E011 full-context logistic model's **raw** probabilities. Define:

`p_mix(x; lambda) = (1 - lambda) * p_F + lambda * p_L(x)`.

The ordered candidate weights are exactly **[0, 0.10, 0.25, 0.50, 0.75, 1]**. One scalar is selected per outer fold and applies to every evaluation response in that fold. No class-, question-, answer-, support-, confidence-, or row-specific weights are fitted. No smoothing, log-probability mixing, prior correction, grid expansion, or additional ensemble is allowed.

Align columns by training-only class strings in the original sorted order. Frequency and logistic classes must match within each fitted partition; mismatch is an integrity failure. Inner validation labels absent from inner training receive no probability column and contribute zero MAP@3. Do not pad inner predictions using the outer or global label inventory, which could also change tie handling. No evaluation/calibration labels determine the training classes.

Use explicit endpoint branches: lambda=0 returns the original frequency probabilities unchanged; lambda=1 returns the original logistic probabilities unchanged. This avoids endpoint roundoff and preserves historical behavior. Use the existing MAP@3 implementation (`np.argsort(-probabilities, axis=1)[:, :3]`) and top-1 argmax, with unchanged NumPy version and class order. No new tie-breaking policy is introduced.

Exactly three reporting arms: **selected mixture**, **E011 full context**, and **frequency**. Do not score every fixed weight on outer evaluation labels or select an outer winner. The selected mixture remains the primary arm even if either control wins.

## Frozen data and model settings

Use the existing five outer QuestionId folds with nine training, three calibration, and three evaluation questions per fold. Every response has exactly one outer evaluation assignment. Keep seed `20260831`, source order, target construction, and all role assignments unchanged.

| Input | SHA-256 |
|---|---|
| Training data | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |

Reuse E011's exact `[QUESTION] ... [ANSWER] ... [EXPLANATION] ...` input from QuestionText, MC_Answer, and StudentExplanation, with missing strings converted to empty strings. No numeric normalization, tokenizer repair, label-derived answer keys, or extra features. The word tokenizer still omits single-character tokens.

Keep the original ordered coupled grid: unigram/min_df=2/C=0.5; unigram+bigram/min_df=2/C=1; unigram+bigram/min_df=5/C=2. TF–IDF uses sublinear_tf=True. Logistic regression uses max_iter=2000, class_weight=None, random_state=20260831, n_jobs=1, and unchanged scikit-learn 1.5.2 defaults. Every vocabulary, IDF, classifier, and frequency estimate fits only its applicable training partition.

## Nested selection and calibration order

For each outer fold:

1. Recreate E011's GroupKFold(3) splits within the nine training questions, using QuestionId.astype(str). Fit all three logistic settings on each inner training split. Choose the setting with the largest equal-inner-fold raw MAP@3; exact ties choose the first setting. This is the unchanged E011 selector, not joint tuning of model settings and mixture weights.
2. Retain the inner validation raw probabilities for that selected setting in memory from those same fits. For each of the six weights, mix them with frequency computed from the corresponding **inner training** labels, not all nine outer training questions. Compute three inner MAP@3 values and maximize their unweighted mean. Exact ties choose the first weight in the ordered list, favoring smaller lambda. Publish the complete aggregate inner selection table, not row probabilities.
3. Refit the selected E011 setting on all nine training questions. Compute outer training frequency. This requires nine inner fits plus one refit per outer fold: **50 classifier fits total**. Reusing the inner selection predictions avoids extra fits; no historical fitted model exists to load.
4. Freeze lambda before calibration. Fit the original E011 temperature on its raw probabilities for the three calibration questions. For a selected interior weight, fit a separate temperature on the **raw mixture** probabilities for those same calibration questions. Both use the unchanged E001 fitter: supported calibration truths only, bounded log-temperature [-3, 3], clipping at 1e-12, and its existing T=1 fallback if no calibration truth is supported. Record temperature and supported count. Do not reuse the logistic temperature for an interior mixture.
5. For lambda=0, bypass temperature scaling entirely and return the unscaled frequency control, including calibration and routing outputs. For lambda=1, reuse the E011 control's fitted temperature and probabilities exactly. These endpoint rules are fixed in advance, not chosen by calibration quality.
6. Produce original raw and final probabilities for the three evaluation questions, with no evaluation metrics yet. All reported primary scores use the final probability pipeline. Weight selection uses raw ranking, not calibrated inner scores. Report raw-to-final top-1/top-three changes to expose clipping/tie effects rather than assuming perfect rank preservation.

The same inner folds select the E011 setting and then lambda. Their selected scores are development scores, not unbiased performance estimates; no claim of independence between the two selection stages is made. Outer evaluation remains separate. Calibration labels never select lambda, the model setting, a review threshold, or a subgroup.

## Global freeze and historical reproduction

Before any new outer scoring, prepare all five folds' settings, selection tables, lambdas, temperatures, predictions, confidence-routing orders, and explanation-shuffle mappings. Write an aggregate-only development receipt and seal arrays in memory. The fitting/selection layer receives no evaluation targets; label-bearing evaluation access is restricted to scoring after the global barrier.

First reproduce E011 full-context and frequency development and original fold/question/support/Category/risk-coverage records against the pinned published artifacts. Use absolute tolerance 1e-10, relative tolerance zero, and exact counts/null patterns. The E011 raw/scaled and explanation-shuffle diagnostics used here must also reproduce their corresponding E013 summaries. Only then release new selected-mixture summaries. A mismatch stops the attempt; never tune to match a held-out score.

Check data/manifest/assignment hashes, source/target alignment, group-disjoint roles, and preservation hashes before and after the run. Changes to an approved scientific rule require an amendment and renewed approval before execution, not a silent repair after viewing results.

## Primary estimand and decision rule

For fold f, define `D_f = MAP3(selected mixture, f) - MAP3(frequency, f)` on **all** evaluation rows, including unsupported truths. H1 is met only when the unrounded unweighted mean of all five D values is **at least 0.020** and D is **strictly positive in at least four of five folds**. No numerical tolerance or rounding applies to the decision. Relative to the reproduced baseline this corresponds to mean MAP@3 of at least approximately 0.559215, but the paired rule uses full-precision fold results, not that rounded target.

Publish all five scores/deltas, equal-fold mean, sample SD (ddof=1), positive-fold count, and criterion Boolean. Also report the selected mixture versus E011 comparison with the same summaries, but no second success gate. This pragmatic margin is not a statistical significance threshold, classroom safety standard, or proof of generalization to new populations.

Any unmet H1 in a valid completed run is a negative result for this registered approach. A positive mean below 0.020, or sufficient mean gain with fewer than four positive folds, is below the criterion. Choosing lambda=0 in every fold reproduces frequency and fails H1; it is not a successful learned model. No fallback arm replaces the mixture as the headline result.

## Prespecified secondary analyses

For all three original-input arms, all five folds, all 15 questions, and all existing strata, report exact-label MAP@3, top-1 accuracy, sample counts, and paired deltas against frequency and E011. Use the unchanged recipient-truth support definitions from outer training data: unsupported=0, rare=1–19, frequent>=20, and nested well-supported>=20 across at least two training questions, plus all rows. Empty strata remain null. These labels are reporting strata, never prediction-time routing information.

Report top-1 and ordered-top-three agreement with frequency, plus reciprocal-rank-at-three win/tie/loss counts, gain `mean(max(model RR - frequency RR, 0))`, loss `mean(max(frequency RR - model RR, 0))`, and net gain minus loss. Report the selected mixture's change in each contribution relative to E011. Use the same fold/question/stratum grid and verify that gain minus loss equals the MAP@3 delta. No per-label or per-answer performance table is added.

For the explanation diagnostic, reuse **only E013's explanation_shuffle condition**, exactly as specified in its protocol: 100 ordinary permutations within converted (QuestionId, MC_Answer) cells, seed construction [20261014, 1, fold, replicate, cell_index], PCG64, fixed cell/member ordering, fixed points/singletons/duplicates retained. No pair-shuffle condition is added. Targets and support remain the recipient's. Freeze mappings without targets; apply the already selected lambda and already fitted temperature, with no refitting or reselection.

Because question/answer context is identical within a cell and frequency is constant per fold, donor-row indexing of the original probability matrix exactly supplies the perturbed input prediction. Test this identity. Score original-minus-shuffled MAP@3 and accuracy for every registered fold/question/stratum, reporting replicate mean, sample SD, and linear 2.5th/97.5th percentiles. Across-fold replicate summaries pair replicate r across folds before averaging. Report E013's applicable opportunity counts and input-change summaries; reproduce E011's registered shuffle effect and frequency invariance as controls. No 0.020 explanation-effect threshold is imposed on a deliberately attenuated mixture.

## Exploratory calibration and review diagnostics

For original inputs only, report raw and final mean confidence, accuracy, signed confidence-minus-accuracy, 10-equal-width-bin ECE, and corrected union-label Brier for all arms on the fold/question/stratum grid. ECE/Brier eligibility remains local: n>=200, correct>=20, and incorrect>=20. Otherwise return null with reasons. Paired calibration changes use groups eligible in both pipelines and state denominators. Frequency has one unchanged pipeline. Record temperature-bound proximity at distance <=1e-5 in log space, supported calibration counts, and raw-to-final top-1/ordered-top-three change rates.

Use the existing E011 confidence-routing procedure at exactly 0/10/20/30/40/50% review, separately within each outer fold pooled over its three evaluation questions. Defer floor(N*b/100), using final maximum probability and the existing E006 SHA-256/source-position tie rules. Freeze orders before scoring. For retained all-row predictions report counts, accuracy, MAP@3, risk, confidence, and eligible ECE/Brier, with frequency and E011 alongside the mixture. No budget is optimized or converted into an automation recommendation; no new rejection threshold or support-aware gate is trained.

## Uncertainty and safeguards against selective reporting

Uncertainty is descriptive only: show all five folds, equal-fold means, sample SDs, and defined/eligible-fold denominators; show all questions and all fixed strata. Shuffle percentiles describe assignment dispersion, not confidence intervals for future questions or inferential p-values. Do not add bootstrap tests, significance/equivalence tests, a favorable subset of folds, an outer weight-response curve, or unregistered analyses after results.

No post-hoc change to model grid, weight grid, tie rules, scaling sequence, support thresholds, fold assignments, review budgets, or interpretation rules. No random-split rerun. No selection of the better raw/calibrated pipeline for the primary outcome. Unsupported exact labels remain unrepresentable by this closed-set approach; support-restricted success cannot replace all-row H1.

## Interpretation rules

| Pattern | Permitted conclusion |
|---|---|
| H1 met and explanation decrement positive | This selected mixture improves ranking on the reused benchmark and retains measured explanation dependence; not proof that explanations alone caused the improvement |
| H1 met without a positive explanation decrement | A ranking improvement without demonstrated explanation dependence under this diagnostic; do not call it an explanation-based gain |
| H1 unmet but mixture beats E011 | Shrinkage mitigates some errors without meeting the useful-improvement criterion against frequency |
| All folds select lambda=0 | Inner grouped selection does not justify adding this logistic evidence under the registered procedure; baseline reproduction is not model success |
| Inner selection favors mixtures but outer results fail | The selected mixing policy does not transfer sufficiently to these held-out questions; it does not establish that every possible mixture must fail |
| MAP@3 improves while calibration or retained risk worsens | Ranking gain and uncertainty quality diverge; no safety or automation claim |
| Technical, reproduction, or integrity failure | Incomplete experiment, not scientific failure; preserve the attempt and stop for review |

A negative result would test the specific proposition that a single training-selected shrinkage weight is enough to make this E011 signal useful. It cannot rule out other representations, context-dependent weighting, or alternative tasks. Success still requires later evaluation on genuinely new questions before stronger generalization claims.

## Execution and publication after approval

Implement in new E014 files without editing historical scientific modules. Reuse their functions with tested orchestration. Before fitting, test inner-only frequency estimates, training-only class alignment, exact endpoint identities, sequential selector/tie rules, no evaluation-target access before the freeze, calibration ordering, fixed mappings, recipient strata, reproduction failures, contribution arithmetic, null eligibility, strict aggregate schemas, and monitor-failure isolation. Commit and hash-lock the approved protocol, implementation, dependency image, historical references, and preservation inventory before MAP computation. Approval is recorded separately; this review copy alone is not execution authorization.

Use pinned CPU image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, UID/GID 10001, one numerical thread, network disabled, read-only project/data/root, and only new `artifacts/e014_attempt01` writable with ephemeral scratch. Refuse an existing attempt directory. An unavailable image requires review, not silent substitution. Fit errors or warnings stop; no automatic retry, extra iterations, or next-model trigger.

Expected computation: **10–25 minutes for 50 classifier fits plus aggregate scoring**, estimated from E013's approximately 12.5-minute 145-fit run, allowing for the different fit mix and reporting work. This is not an E014 pilot. Implementation, synthetic tests, privacy audit, and publication add preparation time. No GPU, downloads, external API, or new dataset is needed.

Keep the resilient read-only terminal monitor active during execution, showing E014, status, elapsed time, completed fits/scoring work, stage, and latest completed metric. Metrics remain unavailable before the scoring barrier. Local terminal refreshes are independent of chat notifications, which are at most hourly while active, with prompt completion/failure notices. No idle monitor or scheduled wakeup is started for protocol review.

Publish allowlisted aggregate JSON and complete tables regardless of scientific outcome, after schema/arithmetic tests and secret/data/local-path scans. Never serialize student text, answers, row identifiers, probability/prediction arrays, donor mappings, fitted models, vocabularies, or coefficients. Preserve all failed attempts and earlier evidence. Append to the experiment log; publish approved plan and verified results as separate descriptive commits only to the existing personal repository. Show aggregate and fold-level numerical results before interpretation. Stop after E014 reporting.

## Prior art and contribution limits

Weighted probability averaging is established soft voting, not a new algorithm; see the [scikit-learn 1.5 weighted probability documentation](https://scikit-learn.org/1.5/modules/ensemble.html#weighted-average-probabilities-soft-voting). The intended contribution is a reproducible, bounded test of whether training-selected shrinkage makes observed explanation-dependent signal useful under question shift, with explicit negative-result and uncertainty reporting.

Permutation diagnostics concern a fitted model's reliance on inputs, not a causal explanation of student reasoning. This distinction is consistent with [Fisher, Rudin and Dominici's model-reliance framework](https://jmlr.org/papers/v20/18-760.html); E014 does not implement that paper's full model-class analysis or inferential guarantees. Neither source predicts an E014 gain or establishes novelty for this dataset-specific evaluation.
