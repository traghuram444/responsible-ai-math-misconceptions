# E016 direct Category learning with frequency-based misconception ranking

## Review status and motivation

Prepared 2026-10-19 for user review against revision `7a3144990783eb3976641fa67c3dfaf93675fb8f`. **This is a proposed preregistration, not authorization to implement or run.** No E016 fitting, selection, evaluation, pilot, or monitor has started. Approval of this exact specification is required.

Preserve E001–E015, their scientific files, protocols, approvals, locks, results and attempts, and all frozen assignments. Add E016 in new files; the experiment log is append-only.

The research question remains generalization of mathematical-misconception detection to unseen K–12 math questions, with uncertainty-aware human review. E016 asks whether directly learning the six shared Categories transfers better than learning the full Category:Misconception target, when within-Category misconception ordering is deliberately left to training frequency.

There has been measurable improvement over a learned control, but no meaningful frequency-baseline win: E014's selected frequency/logistic mixture reached mean MAP@3 0.537231, versus E011 0.511887 and frequency 0.539215. E015's primary notation-retaining arm scored 0.491902. These results motivate separating transferable Category evidence from more question-dependent exact-label distinctions, rather than assuming another representation or ensemble will help.

Earlier Category summaries marginalize predictions from exact-label classifiers. They do not test direct Category training. E016 is a structured hybrid of a learned Category distribution and empirical within-Category frequencies. It is not another weighted average of full-label classifiers. No new ensemble, mixture weight, class weighting, tokenizer, annotation, label regrouping, or enlarged parameter search is included.

The same 15 questions have informed multiple research decisions. Prospective specification constrains E016's execution, but does not make this reused benchmark an independent confirmatory sample. No novel-algorithm or deployment-readiness claim is planned.

## Hypotheses and analysis roles

**H1, sole confirmatory outcome:** the factorized model achieves a meaningful all-row exact-label MAP@3 improvement over the unchanged frequency baseline under frozen question-held-out evaluation. The precise magnitude and fold-consistency rule is below.

**H2, prespecified secondary mechanism comparison:** direct Category learning improves raw six-way Category accuracy relative to Category probabilities marginalized from the raw E011 exact-label classifier. Report the signed equal-fold mean difference and every fold. Raw six-way macro-F1 is a companion metric, not an alternative chosen after seeing results. Also report both metrics against frequency. There is no separate binary success threshold or significance claim.

**H3, prespecified secondary utility comparison:** factorization improves final exact-label MAP@3 over E011, and changes the balance of gains and losses relative to frequency. Report signed comparisons, win/tie/loss counts and contributions, including the fixed support strata. This cannot replace H1.

**H4, prespecified secondary reliance diagnostic:** the factorized model's predictions depend usefully on the recipient explanation within a fixed question and selected answer, measured by the unchanged explanation-shuffle diagnostic below. This measures fitted-model reliance, not mathematical reasoning or causal student cognition.

Final marginalized Category performance, calibration and fixed-review-budget results are exploratory diagnostics with fixed reporting rules. They cannot rescue a negative H1. No new post-hoc subgroup, threshold, best arm, best budget, or metric will be selected.

## Three fixed reporting arms

| Arm | Learned target | Exact-label prediction |
|---|---|---|
| Factorized Category model, primary | Existing six-way Category | Learned Category probability times training-only within-Category exact-label frequency |
| E011 full-context control | Existing exact Category:Misconception | Original TF–IDF/logistic pipeline, reproduced unchanged |
| Frequency | None | Original exact-label training prevalence, unscaled |

Both learned arms use exactly the E011 full-context construction and missing-to-empty conversion:

```text
[QUESTION] {QuestionText} [ANSWER] {MC_Answer} [EXPLANATION] {StudentExplanation}
```

Use the original default word tokenizer `r"(?u)\b\w\w+\b"`, not E015's alternative tokenizers. No QuestionId, source position, correctness flag, target, label-derived answer key, or evaluation label enters the predictor. No generated solution, numerical evaluator, new semantic model, external API or data is added.

The fixed Category order is:

```text
False_Correct
False_Misconception
False_Neither
True_Correct
True_Misconception
True_Neither
```

Derive Category as the prefix before the first colon in the unchanged exact-label construction. Validate its agreement with the original Category field in each truth-bearing partition. This is an existing target, never an input feature.

### Exact factorization

For the applicable training partition S, let Y_S be its sorted observed exact labels, c(y) the Category of label y, n_S(y) its count, and n_S(c) the total count for that Category. Train logistic regression directly on c(y), and reconstruct:

```text
q_S(y | c(y)) = n_S(y) / n_S(c(y))
p_raw(y | x) = p_Category(c(y) | x) * q_S(y | c(y)), for y in Y_S
```

Use all training examples with their original weights. No smoothing, question/answer-conditioned counts, balance correction, mixture weight, or label-name embedding is used. There is no hard Category gate: rank exact labels globally across all observed Categories using the reconstructed probabilities. Within a Category, ordering is fixed by its training counts.

The classifier's Category columns must be explicitly aligned by their names, not assumed to share exact-label column positions. A Category absent from training has probability zero in fixed-six reporting and no exact-label columns; no division by zero is performed. Fewer than two observed training Categories, an unknown Category, an empty vocabulary, a fit warning or an invalid/nonfinite probability vector stops the attempt. There is no silent fallback or retry.

Do not use held-out labels to construct Y_S or add exact-label probability columns. Unsupported evaluation truths receive zero exact-label accuracy and MAP@3, including when their Category is supported. They remain in the primary population.

Test two identities before fitting MAP: summing reconstructed raw probabilities within Category recovers the direct Category probabilities; substituting training Category prevalence for the learned Category probabilities recovers global exact-label frequency within absolute tolerance 1e-12. The reported baseline still uses the unchanged frequency routine, preserving its numerical and tie behavior.

## Frozen evaluation and nested selection

Use the original five outer QuestionId folds: nine training, three calibration and three evaluation questions per fold. Each response is evaluated once. Preserve source order, roles, target construction and seed `20260831`.

| Input | SHA-256 |
|---|---|
| Training data | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |

Select each learned arm independently using the identical GroupKFold(3) assignments within the nine training questions, with QuestionId.astype(str), and exactly this ordered coupled grid:

1. Unigram; min_df=2; C=0.5.
2. Unigram+bigram; min_df=2; C=1.
3. Unigram+bigram; min_df=5; C=2.

For both arms, maximize unweighted mean inner-validation **raw exact-label MAP@3**, not Category accuracy. Exact ties select the first grid entry. For the factorized arm, reconstruct each inner-validation prediction using only that inner training partition's Category model, vocabulary, IDF, exact-label inventory and conditional frequencies. Outer-training counts must not leak into an inner-validation prediction. Unsupported inner-validation exact truths score zero.

Publish all candidate inner scores and selected settings. Refit each selected arm on all nine outer-training questions, recomputing its training-only quantities. The controlled comparison holds representation, classifier family and selection procedure fixed; fitted hyperparameters and coefficient dimensions can differ because the target changes.

Keep lowercasing, no accent stripping, no stop words, word analyzer, `sublinear_tf=True`, L2 normalization, smooth IDF, no feature cap, and unchanged scikit-learn 1.5.2 defaults. Logistic regression keeps `max_iter=2000`, `class_weight=None`, `random_state=20260831`, `n_jobs=1` and other E011 defaults. No additional solver, regularization, calibration or feature-choice search is allowed.

There are nine inner fits plus one refit per learned arm/fold: **100 classifier fits total**. Frequency requires no classifier fits. No random-split rerun or E014/E015 candidate selection is included.

## Calibration and prediction semantics

After refitting, calibrate each learned arm separately using only the original three calibration questions. Apply the unchanged E001 temperature fitter to **exact-label probabilities**: reconstructed probabilities for the factorized arm, original exact probabilities for E011.

Use supported exact calibration truths only, NLL minimization, bounded log-temperature [-3, 3], clipping at 1e-12, and T=1 with supported count zero when no calibration exact truth is supported. A supported Category alone does not make an unsupported exact calibration truth eligible. Calibration labels cannot choose model settings or conditional frequencies. Frequency stays unscaled.

Primary exact-label metrics use these final probabilities. The raw factorization above is not an assertion that the final distribution preserves the original conditional-frequency probabilities: exact-level temperature scaling can change Category sums and within-Category probability magnitudes. It does not add an explanation-dependent within-Category ranker.

Distinguish two Category outputs explicitly:

- **Raw:** direct Category probabilities for the factorized arm; raw exact-probability marginalization for E011; marginalization for frequency. This is H2's designated pipeline.
- **Final:** sum each arm's final exact-label probabilities by Category. This is the final system's Category output, not a separately calibrated Category classifier.

Do not fit a separate Category temperature, compare calibration orderings, or report whichever pipeline performs better as the primary output.

Use sorted original exact-label strings, `np.argsort(-probabilities, axis=1)[:, :3]` for exact MAP@3, and `np.argmax` for top-1. For Category argmax ties use the fixed six-name order above. Fixed-six macro-F1 uses all six labels and zero_division=0. Record raw-to-final top-1 and ordered-top-three change counts/rates, temperatures, supported calibration counts and proximity to a log-temperature bound (distance <=1e-5).

## Global freeze, integrity and historical controls

Before any new outer scoring, prepare all ten fitted arm/fold pipelines, selections, conditional frequencies, temperatures, raw/final predictions, confidence-routing orders and label-blind shuffle mappings. Seal in-memory arrays and save an aggregate-only development receipt. Evaluation features may be used for prediction; evaluation targets are unavailable to the development layer. Truth-bearing scoring begins only after the global freeze.

First reproduce E011 and frequency: development selections, temperatures, supported calibration counts, and the original fold/question/support/Category/review records against the pinned E011 artifacts. Reproduce applicable raw/scaled and explanation-shuffle records against E013. Require identical counts/null patterns and absolute tolerance 1e-10, relative tolerance zero. A mismatch stops the attempt before releasing factorized-arm results; do not tune to recover a desired outer score.

Verify data/fold hashes, source/target alignment, group-disjoint roles and the full protected historical inventory before and after execution. Import historical scientific functions without editing them. Test factorized class alignment, normalization, frequency identity, absent Categories, unsupported truths and nested count isolation on synthetic fixtures. An ambiguity or scientific amendment requires review before computation proceeds.

## Primary estimand and decision

For fold f, define D_f as factorized final exact-label MAP@3 minus frequency MAP@3 on **all evaluation rows**. H1 is met only if both conditions hold:

- The unrounded equal-fold mean of five D values is **at least +0.020**.
- D_f is **strictly positive in at least four of five folds**.

Use full-precision paired results with no decision tolerance. With the historical baseline this corresponds to approximately 0.559215 mean MAP@3, but the paired comparison determines the decision. The threshold is a practical improvement criterion, not a significance test or safe-automation standard.

Report every fold's arm scores and deltas, equal-fold means, sample SDs (ddof=1), positive-fold count and criterion Boolean. A valid completed run missing either condition is negative for H1. A smaller positive difference is reported honestly as a sub-threshold gain. Improved Category performance, E011-relative performance, calibration or a subgroup cannot substitute for H1. Technical/integrity failure is incomplete execution, not a scientific negative.

## Prespecified secondary tables

For all three arms publish final exact-label MAP@3, accuracy and counts for each fold, each of the 15 questions, and the complete fixed support grid:

- All rows.
- Unsupported: zero outer-training examples of the exact truth.
- Rare: 1–19 examples.
- Frequent: at least 20 examples.
- Well-supported: at least 20 examples across at least two outer-training questions; nested within frequent.

Support is defined by the recipient truth for evaluation only; it never enters prediction or routing. Empty groups are null. Report factorized-minus-frequency, factorized-minus-E011 and E011-minus-frequency, with equal-fold summaries over defined folds and explicit denominators. No per-label, per-answer or newly selected question subgroup is introduced.

For every fold and question, report raw and final six-way Category accuracy and macro-F1 for all arms, and their paired contrasts. Preserve the designated raw H2 comparison even if final results differ. Report accuracy/F1 disagreement without selecting the favorable metric.

For each fixed fold/question/support group, report final top-1 and ordered-top-three agreement with frequency, and reciprocal-rank-at-three win/tie/loss counts. Gain contribution is mean(max(model_RR - frequency_RR, 0)); loss contribution is mean(max(frequency_RR - model_RR, 0)). Verify gain minus loss equals the group's MAP@3 difference. These diagnose whether useful corrections outweigh damage to the baseline's correct rankings.

### Explanation reliance

Reuse only E013's `explanation_shuffle`: 100 ordinary permutations within exact missing-to-empty (QuestionId, MC_Answer) cells, without trimming or case-folding grouping keys. Converted QuestionText must be identical within QuestionId or the attempt stops.

Use `Generator(PCG64(SeedSequence([20261014, 1, fold, replicate, cell_index])))`. Folds are 0–4, replicates 0–99, cells sort by numeric QuestionId then Python Unicode answer order, and members sort by source position; all indices start at zero. Use identical mappings for every arm. Retain fixed points, singletons, duplicate texts and label-homogeneous cells.

Recipient truths/support remain fixed. Indexing original final probabilities by donor position is equivalent to prediction on the shuffled explanation because question/answer context is unchanged; test this identity synthetically. Do not retrain, reselect, recalibrate or recompute conditional frequencies.

Report original-minus-shuffled exact MAP@3 and accuracy on the fixed fold/question/support grid, with replicate mean, sample SD and linear 2.5th/97.5th percentiles. For across-fold summaries pair replicate r across folds before averaging; do not treat 500 fold/replicate values as independent. No separate Category shuffle analysis is added.

Report applicable E013 opportunity summaries by fold/question: rows, cells, singleton rows, rows in cells of size at least two, label-mixed-cell rows/shares, and replicate mean/SD of donor-position and actual-input changes. Never publish cell identifiers or answer strings. Frequency invariance and E011's historical shuffle effect are integrity gates. H4 has no binary success threshold.

## Fixed exploratory uncertainty and review diagnostics

For original exact-label predictions on the fixed fold/question/support grid, report raw/final mean confidence, accuracy, signed confidence-minus-accuracy, 10-equal-width-bin ECE and corrected union-label Brier. ECE/Brier eligibility remains local: n>=200, correct>=20 and incorrect>=20; otherwise null with reasons. Paired calibration changes use only jointly eligible groups and state denominators. Frequency has one unchanged pipeline. Do not substitute supported-only Brier for the union-label score.

Use final maximum exact-label probability for confidence routing and the original E006 SHA-256/source-position tie rules. At exactly 0/10/20/30/40/50% review, within each outer fold pooled over its three evaluation questions, defer floor(N*b/100) lowest-confidence rows. Freeze routing without evaluation truth. Report retained counts/coverage, exact accuracy, MAP@3, top-1 risk, mean confidence and eligible ECE/Brier for every arm and budget. No new support-aware gate, fitted rejection threshold, selected budget or automation claim is included.

All uncertainty is **descriptive**: five fold values, equal-fold means, sample SDs and defined/eligible-fold counts, alongside all question results. Sample SD is null with fewer than two defined folds. No bootstrap, significance/equivalence test, p-value or new correlation analysis is added. Shuffle percentiles describe perturbation dispersion, not confidence intervals for new questions. Overlapping training sets and repeated research decisions on 15 questions limit generalization claims.

## Registered interpretation rules

| Outcome | Permitted interpretation |
|---|---|
| H1 met | The specified factorized system meets the practical ranking-gain criterion on this reused benchmark; independent new-question validation remains necessary |
| H1 missed, but positive exact delta | A quantified sub-threshold or inconsistent gain, not a meaningful-baseline-win claim |
| Raw Category accuracy improves over E011, exact MAP@3 does not | Category transfer and exact-label ranking diverge under this pipeline; fixed within-Category ranking and unsupported labels remain limitations, without claiming either is the sole cause |
| Exact MAP@3 improves but raw Category accuracy does not | Hard Category accuracy alone does not explain ranking changes; probability allocation may matter, but the mechanism is not established by this result |
| Neither raw Category accuracy nor exact MAP@3 improves over E011 | No demonstrated mean benefit of this specified direct-Category/frequency construction; not proof that every hierarchical or hybrid model must fail |
| Gains occur only in a support stratum or selected questions | Localized evidence, not a replacement for the all-row primary outcome |
| Accuracy and macro-F1, or raw and final Category results disagree | Report all designated comparisons; make no unqualified Category-improvement claim |
| Ranking improves but calibration or retained risk worsens | Ranking utility and uncertainty quality diverge; no safe-automation conclusion |
| Little/no explanation-shuffle decrement | No demonstrated explanation reliance under this diagnostic, regardless of a ranking improvement |
| Technical/reproduction/integrity failure | Preserve the incomplete attempt and stop for review; no automatic scientific fallback |

“Improves” in secondary descriptions means the signed descriptive mean is positive, not statistically significant or practically sufficient. The primary criterion is unchanged by any secondary pattern. Factorization can alter Category mass, but cannot identify an unsupported exact label or learn explanation-dependent distinctions within a Category. A null result therefore tests a bounded architectural hypothesis, not all possible student-reasoning systems.

Present complete aggregate and fold-level numerical tables first, followed by the registered question/support, Category, contribution, shuffle, calibration and review tables. Await user review before interpretation. Preserve negative results. Stop after E016; no E017 or automatic alternative model is authorized.

## Execution and publication after approval only

Implement in new E016 files and record approval separately, without rewriting this reviewed protocol. Before MAP fitting, run synthetic tests for factorization identities, class ordering, missing Categories, training-only conditional counts in every inner fold, selector ties, exact-calibration eligibility/order, raw/final Category semantics, global freezing, historical reproduction, routing, permutations, metrics, null eligibility, primary decision boundaries, aggregate-only schema and monitor-I/O isolation, plus the existing test suite.

Hash-lock and commit the approved protocol, tested implementation, image identity, reference artifacts and complete historical public/private preservation inventory before the run. Do not modify E001–E015 modules to implement E016.

Use CPU image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, UID/GID 10001, one numerical thread, network disabled, read-only root/project/data, and only new `artifacts/e016_attempt01` writable plus ephemeral scratch. Refuse an existing attempt directory. Do not replace an unavailable image, change dependencies, increase iterations, retry automatically or start another model without approval.

Estimated execution time is **10–25 minutes for 100 classifier fits and aggregate reporting**, excluding implementation, testing and publication checks. This estimate uses E014/E015 timings; no E016 pilot has been run. Hardware load can change elapsed time and does not authorize scientific changes. No GPU, paid service or model download is needed.

Keep the resilient terminal monitor active only during execution, showing experiment ID, status, elapsed time, completed fits/scoring work, stage and latest completed metric. Before scoring, metrics are unavailable. Periodic chat notifications are at most hourly while running, with completion/failure reported promptly. No idle monitor or scheduled wakeup is started for this review.

Publish only allowlisted aggregate JSON, complete tables, original code/tests, protocol and append-only documentation after secret/data/local-path scans and artifact verification. Never publish raw responses, answer strings, row identifiers, probability/prediction arrays, shuffle mappings, vocabulary strings, coefficients or fitted models. Publish the approved plan and verified results as separate descriptive commits only to the existing personal repository. This draft is not approval to execute or push results.

## Prior art and limits

The classifier remains the existing implementation documented by [scikit-learn 1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegression.html). Factoring a joint label into a Category distribution and conditional label frequencies is an elementary probability construction, not a claimed novel algorithm. This experiment tests that constrained construction in the project's fixed question-shift setting.

[Soft voting](https://scikit-learn.org/1.5/modules/ensemble.html#weighted-average-probabilities-soft-voting) combines class probabilities; E014 already tested a bounded frequency/logistic mixture. E016 changes the learned target and factorization instead. A future multi-model ensemble would require a separate protocol, complementary-error rationale and training-only weight/selector learning; it is not included here.

[Guo et al.](https://proceedings.mlr.press/v70/guo17a.html) provide prior art for temperature scaling. Reusing this calibration method is not a guarantee of calibration under question shift. The contribution sought here is a reproducible, controlled comparison with complete negative-result and uncertainty reporting, not a promise of a positive score.
