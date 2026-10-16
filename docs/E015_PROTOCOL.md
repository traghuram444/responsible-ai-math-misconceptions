# E015 controlled mathematical-token retention ablation

## Review status and scope

Prepared 2026-10-16 for user review. **Protocol only: implementation and execution require approval of this exact specification.** No E015 fitting, token audit on MAP, hyperparameter selection, or evaluation has occurred. Reference revision: `16f55596de8b871d89820e31e75ddf28e4c2f150`.

Preserve E001–E014, all prior attempts, scientific modules, results, locks, and frozen assignments. E015 tests a representation failure mechanism, not another classifier family or a search for a favorable outer score. No E014 mixture, generated solution, label-derived answer key, new annotation, external model, or new data is introduced.

The motivation is recorded evidence, not a demonstrated cause. E011 full-context MAP@3 was 0.511887 versus frequency 0.539215. Its standalone answer-token audit found zero default word tokens for 9,502 of 36,696 selected answers (25.894%); this does **not** mean the full model input was empty. E014 improved over E011 to 0.537231 but still missed its baseline-improvement criterion. E012 changed both representation and classifier, so its result cannot isolate the effect of retaining mathematical notation.

The benchmark's 15 questions have been repeatedly examined. This is a prospectively specified test on a reused benchmark, not independent confirmation on new questions.

## Research questions and hypotheses

**H1, sole confirmatory outcome:** explicitly retaining single-character words/digits and the bounded notation tokens below, under the unchanged classifier family and nested selection procedure, produces a meaningful all-row exact Category:Misconception MAP@3 improvement over training-label frequency on held-out questions.

**H2, prespecified secondary:** relaxing only the two-character minimum improves performance relative to E011. Estimate B minus A without a separate binary success threshold.

**H3, prespecified secondary:** retaining notation in addition to single-character words/digits improves performance over single-character retention alone. Estimate C minus B without a separate binary success threshold.

**H4, prespecified secondary diagnostic:** any useful ranking signal still depends on the recipient explanation within a fixed question and selected answer. Reuse the registered explanation-shuffle diagnostic for every arm; this is a model-reliance measurement, not proof of mathematical reasoning.

Token/vocabulary coverage, calibration, Category summaries, and review-budget analyses are exploratory diagnostics with fixed reporting definitions. They cannot substitute for H1.

## Arms and exact input

Report exactly A, B, C, and frequency. C remains the primary arm regardless of which arm scores best.

All learned arms use E011's identical missing-to-empty string conversion and concatenation:

```text
[QUESTION] {QuestionText} [ANSWER] {MC_Answer} [EXPLANATION] {StudentExplanation}
```

No QuestionId, source position, correctness flag, target, or label-derived feature enters the predictor. Keep the existing lowercasing, no accent stripping, no stop words, word analyzer, and n-gram construction. Do not add Unicode normalization, stemming, spelling correction, numerical equivalence, expression evaluation, or question-specific rules.

| Arm | Tokenizer | Purpose |
|---|---|---|
| A: original E011 | Original `token_pattern=r"(?u)\b\w\w+\b"`, no custom tokenizer | Historical reproduction control |
| B: single-character retention | `token_pattern=r"(?u)\b\w+\b"`, no custom tokenizer | Changes only minimum word-token length |
| C: notation retention | Exact callable tokenizer below; `token_pattern=None`, `analyzer="word"` | Adds a fixed bounded notation vocabulary to B-style word tokens |
| Frequency | Exact-label prevalence in the applicable training partition, unscaled | Unchanged non-text reference |

### C lexical specification

Use Python `re` Unicode matching. The vectorizer performs its unchanged preprocessing first; the callable receives lowercased text. Scan left to right with the following **ordered** alternatives:

```python
r"\[(?:question|answer|explanation)\]|\b\w+\b|<=|>=|!=|==|\*\*|//|[+\-*/=<>^%×÷−≤≥≠±√∞≈:.,()\[\]{}|!\\]"
```

Emit each full match literally, except that the exact marker matches `[question]`, `[answer]`, and `[explanation]` emit `question`, `answer`, and `explanation` respectively. Thus the inserted markers do not create new bracket features. This same literal marker rule also applies if such a string occurs inside a field. Every unmatched character is a separator and emits nothing. There are no capturing groups, implicit symbol aliases, extra tokens, or hidden fallbacks.

The multi-character operators `<= >= != == ** //` take priority over single symbols. The single-symbol set is exactly:

```text
+ - * / = < > ^ % × ÷ − ≤ ≥ ≠ ± √ ∞ ≈ : . , ( ) [ ] { } | ! \
```

Word tokens retain Python's Unicode `\w` semantics, including underscores; no special digit segmentation occurs inside words. ASCII hyphen and Unicode minus remain distinct. Decimal points and fraction slashes are separate tokens: `-3.5` becomes `- 3 . 5`; `1/2` becomes `1 / 2`. Fractions, decimals, and multi-symbol expressions are **not atomic numerical features**. Backslash commands retain the backslash and following word separately; this is not a LaTeX parser. Operators outside the enumerated set are not guaranteed to survive. Periods, commas, and other listed punctuation are retained even when used in prose; no outcome-informed mathematical/prose disambiguation is permitted.

Use a callable **tokenizer**, not a callable analyzer, so the existing selected unigram/bigram generation still applies. The fixed synthetic examples below are specification tests, not observations from MAP. Token lists show pre-ngram output after lowercasing; the backslash example uses JSON-style escaped token strings.

| Synthetic input | A | B | C |
|---|---|---|---|
| `I got -3.5` | `["got"]` | `["i","got","3","5"]` | `["i","got","-","3",".","5"]` |
| `12/34` | `["12","34"]` | `["12","34"]` | `["12","/","34"]` |
| `x<=2` | `[]` | `["x","2"]` | `["x","<=","2"]` |
| `[ANSWER] 1/2` | `["answer"]` | `["answer","1","2"]` | `["answer","1","/","2"]` |
| `\frac{1}{2}` | `["frac"]` | `["frac","1","2"]` | `["\\","frac","{","1","}","{","2","}"]` |
| `a−b` | `[]` | `["a","b"]` | `["a","−","b"]` |

This controls the classifier family and selection **procedure**, not identical fitted hyperparameters, feature dimensionality, n-gram adjacency, or TF–IDF normalization across arms. Adding tokens changes those quantities and retains some prose punctuation. Consequently C-minus-B tests this specified lexical pipeline, not a pure causal effect of mathematical meaning.

## Frozen evaluation, fitting, and calibration

Use the original five outer QuestionId folds, with nine training, three calibration, and three evaluation questions per fold; each response is evaluated once. Preserve source order, exact target construction, all roles, and seed `20260831`.

| Input | SHA-256 |
|---|---|
| Training data | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |

For each arm independently and each outer fold, use identical GroupKFold(3) inner assignments within the nine training questions, using QuestionId.astype(str). Select among exactly the original ordered coupled grid:

1. unigram; min_df=2; C=0.5.
2. unigram+bigram; min_df=2; C=1.
3. unigram+bigram; min_df=5; C=2.

Maximize unweighted mean inner-validation raw MAP@3. Exact ties choose the first grid entry. Publish all aggregate inner scores and selections. Never use outer results to select an arm, setting, tokenizer variant, or vocabulary rule. Each vocabulary, IDF, class inventory, and classifier is fitted on its applicable training partition only.

Keep `sublinear_tf=True`, L2 normalization, smooth IDF, no feature cap, and other unchanged scikit-learn 1.5.2 TF–IDF defaults. Logistic regression keeps `max_iter=2000`, `class_weight=None`, `random_state=20260831`, `n_jobs=1` and other unchanged defaults. No new class weighting, solver, regularization grid, or feature fusion. Every fit warning or error stops the attempt.

Refit each selected arm on all nine training questions. Fit a separate temperature for each arm using only the original three calibration questions and the unchanged E001 fitter: supported calibration truths only, NLL minimization, bounded log-temperature [-3, 3], clipping at 1e-12, and T=1 with count zero if no calibration truth is supported. Calibration labels cannot select model settings or tokenization. Frequency uses outer training prevalence with no temperature.

Use the original sorted training class order, `np.argsort(-probabilities, axis=1)[:, :3]` for MAP@3 and `np.argmax` for top-1, with pinned numerical versions. Unsupported evaluation truths receive zero MAP@3 and accuracy. Never pad prediction columns with held-out labels. Primary and performance comparisons use final calibrated predictions; report raw-to-final top-1 and ordered-top-three changes without choosing whichever pipeline looks better.

There are 9 inner fits and 1 refit per arm/fold: **150 classifier fits total**. No random-split rerun, E012 refit, or E014 mixture is included.

## Global freeze and reproduction gates

Before any new outer scoring, prepare all 15 fitted arm/fold pipelines, selections, temperatures, original raw/final predictions, confidence-routing orders, and label-blind explanation-shuffle mappings. Save an aggregate-only development receipt and seal in-memory arrays. The development layer receives evaluation features but no evaluation targets; truth-bearing scoring starts only after this global barrier.

First reproduce A and frequency against the pinned E011 artifacts: development selections, temperatures, supported calibration counts, original fold/question/support/Category/review records and historical answer-token counts. Reproduce the applicable A raw/scaled and explanation-shuffle records against E013. Use absolute tolerance `1e-10`, relative tolerance zero, identical counts and null patterns. A mismatch stops the attempt before releasing B/C results; never tune to match an outer score.

Verify data/fold hashes, row/target alignment, group-disjoint roles, and the complete protected history inventory before and after execution. Historical scientific files are imported, not edited. New E015 code handles the tokenizer alternatives. An approved scientific rule cannot be changed without a documented amendment and renewed approval before further computation.

## Primary estimand and success/failure

For each fold f, `D_f = MAP3(C, f) - MAP3(frequency, f)` on **all evaluation rows**. H1 is met only if:

- the unrounded equal-fold mean of the five D values is **at least +0.020**; and
- D is **strictly positive in at least four of five folds**.

Use no tolerance or rounded value for adjudication. With the reproduced baseline, the first condition corresponds to approximately 0.559215 mean MAP@3, but the actual test uses paired full-precision results. This is a practical margin, not statistical significance or a classroom safety threshold.

Report all five scores/deltas, equal-fold mean, sample SD (ddof=1), positive-fold count, and the criterion Boolean. Any valid completed run missing either condition is negative for H1. A B-arm success, support-restricted improvement, calibration gain, or favorable individual question cannot replace C's all-row result. Technical/integrity failure is incomplete execution, not a scientific negative.

## Prespecified secondary reporting

For A, B, C, and frequency, publish original-input exact-label MAP@3, top-1 accuracy, and counts for every fold, every one of the 15 questions, and all fixed recipient-truth support strata:

- unsupported: zero outer-training examples of the exact label;
- rare: 1–19 examples;
- frequent: at least 20 examples;
- well-supported: at least 20 examples across at least two training questions, nested within frequent;
- all rows.

Strata never use donor labels and never become prediction features or routing signals. Empty groups remain null. Report B-minus-A, C-minus-B, C-minus-A, and each learned arm minus frequency. Equal-fold summaries average only defined folds and state their denominator; no empty stratum is silently assigned zero.

Report original top-1 and ordered-top-three agreement with frequency and per-row reciprocal-rank-at-three win/tie/loss counts. Gain contribution is `mean(max(model_RR - frequency_RR, 0))`; loss contribution is `mean(max(frequency_RR - model_RR, 0))`. Verify gain minus loss equals the MAP@3 difference for the same reporting group. No per-answer or per-label performance search is added.

For explanation reliance, use **only** E013's `explanation_shuffle`: 100 ordinary permutations within exact missing-to-empty (QuestionId, MC_Answer) cells, with no trimming/case-folding of grouping keys. Converted QuestionText must be identical within QuestionId or the attempt stops. Use `Generator(PCG64(SeedSequence([20261014, 1, fold, replicate, cell_index])))`, folds 0–4 and replicates 0–99; cells sort by numeric QuestionId then Python Unicode answer order, members by source position, indices start at zero. Apply the same mappings to all arms and frequency. Retain fixed points, singletons, duplicate text, and label-homogeneous cells.

Recipient truths/support stay fixed. Donor-row indexing of original final probabilities is exactly equivalent to the perturbed input because question and answer context are unchanged; test that identity on synthetic data. No retraining, reselection, or recalibration. Report original-minus-shuffled MAP@3/accuracy for all fixed folds/questions/strata, with replicate mean, sample SD and linear 2.5th/97.5th percentiles. For across-fold summaries, pair replicate r across folds before averaging; do not treat 500 fold/replicate values as independent.

Report E013's applicable opportunity counts for each fold/question: rows, cells, singleton rows, rows in cells of size at least two, label-mixed-cell row counts/shares, and replicate mean/SD of donor-position and actual-input changes. Never publish cell identifiers or answer strings. Frequency invariance and A's historical shuffle effect are integrity gates. H4 has no new binary threshold and cannot rescue H1.

## Fixed exploratory diagnostics

### Token retention and training-vocabulary coverage

After the global barrier, audit original evaluation inputs only, reporting all arms, folds, and questions. Audit each raw field separately **without inserted markers**, plus the full constructed input. Use each arm's actual preprocessor/tokenizer and selected outer-trained vocabulary, never fit a diagnostic vocabulary on evaluation text.

For each field/input report row count, blank-string count (empty after the unchanged missing conversion, no trimming), zero-token rows, total emitted unigram occurrences, emitted one-character word-token occurrences, and emitted notation-token occurrences. Notation means membership in C's exact listed single/multi-character symbol set; word means a full Unicode `\w+` match. Markers contribute only to full-input counts.

Report unigram occurrence coverage = emitted unigram occurrences present in that arm's fitted vocabulary / all emitted unigram occurrences. Report the same coverage separately for the predefined one-character word tokens and notation tokens, so retention of the added token types is distinguishable from coverage of ordinary words. Also report selected-analyzer occurrence coverage = emitted unigram/bigram feature occurrences present in that vocabulary / all emitted feature occurrences under that arm's selected n-gram range. State numerator/denominator; a zero denominator yields null. For standalone fields, do not invent cross-field bigrams. Report rows with zero surviving feature occurrences. Coverage is occurrence-weighted within a reporting group, not an average of per-row ratios.

Publish vocabulary **size**, not vocabulary strings, and zero-token/zero-surviving-feature rates. Distinguish lexical retention from survival after training-only min_df and from predictive utility. No token-content dump, new subgroup based on coverage, coverage/performance correlation search, or post-audit lexer adjustment is allowed.

### Category, calibration, and human-review context

For original inputs, report six-way Category accuracy and fixed-six-label macro-F1 by fold/question, summing exact-label probabilities as in E011. Labels are `False_Correct`, `False_Misconception`, `False_Neither`, `True_Correct`, `True_Misconception`, `True_Neither`. This is marginalization, not a newly trained Category classifier.

For original exact-label predictions on the fixed fold/question/support grid, report raw and final mean confidence, accuracy, signed confidence-minus-accuracy, 10-equal-width-bin ECE, and corrected union-label Brier. ECE/Brier eligibility remains local: n>=200, correct>=20, incorrect>=20; otherwise null with reasons. Raw-to-final and between-arm calibration differences use only jointly eligible groups and state denominators. Frequency has one unchanged pipeline. Record temperatures, supported calibration counts, log-temperature distance <=1e-5 from a bound, and raw-to-final rank-change rates.

Use E011's final-confidence routing and E006's SHA-256/source-position tie rules at exactly 0/10/20/30/40/50% review. Within each outer fold pooled over its three evaluation questions, defer floor(N*b/100) lowest-confidence rows. Freeze ranks without truth. For the retained all-row subset report coverage/count, accuracy, MAP@3, top-1 risk, confidence, and eligible ECE/Brier for all four arms. No best budget, learned rejection threshold, or automation claim is selected.

## Uncertainty, interpretation, and reporting order

All uncertainty is **descriptive**: publish five fold values, equal-fold means, sample SDs, and defined/eligible-fold counts, plus all questions and strata. For fewer than two defined folds, sample SD is null. No bootstrap or inferential/significance/equivalence test is added. Shuffle percentiles describe perturbation dispersion, not a confidence interval for new questions. Overlapping training sets and only 15 reused questions limit the strength of any finding.

| Observed pattern | Registered interpretation |
|---|---|
| C meets H1 | The specified notation-retaining lexical pipeline meets the useful-improvement criterion on this reused benchmark; not proof of mathematical reasoning or independent replication |
| B improves A, C does not improve B | Single-character retention helps in this comparison; the additional specified notation treatment has no demonstrated incremental mean benefit |
| C improves B and A but misses H1 | This tokenization change contributes, but is insufficient to beat frequency by the registered magnitude/consistency |
| C meets H1 but has little/no explanation-shuffle decrement | Better ranking without demonstrated explanation reliance under this diagnostic; do not attribute the gain to reasoning from explanations |
| Retention/coverage increases without performance improvement | Preserving these lexical tokens is not an adequate remedy within this classifier/selection procedure; mathematical information or stronger reasoning methods are not ruled out |
| Low coverage of retained short-word/notation tokens | Report the exact coverage: the specified lexical vocabulary cannot use the out-of-vocabulary occurrences on held-out questions; do not silently lower min_df or introduce a post-hoc coverage cutoff |
| Better MAP@3 but worse calibration or retained risk | Ranking and uncertainty quality diverge; no safe-automation conclusion |
| Any scientific comparison is mixed across questions/folds | Report the heterogeneity without excluding questions or redefining the target |
| Technical/reproduction/integrity failure | Preserve the incomplete attempt and stop for review; do not call it model failure or trigger another model |

Secondary positive/negative descriptions refer to the reported signed mean, not significance. No B-versus-A or C-versus-B threshold will be invented after results. None of these outcomes identifies a student's cognition or licenses deployment. Stronger generalization claims require genuinely new questions.

Show the full aggregate and fold-level numerical results first, followed by all registered question/support, coverage, shuffle, calibration, and review tables. Defer interpretation until the user reviews the results. Publish negative results unchanged. Stop after E015; no E016 is authorized.

## Execution and publication only after approval

After explicit approval, implement in new E015 files and record approval separately. Before any MAP computation, test the exact synthetic token examples, Unicode/operator/marker edge cases, selected n-gram generation, training-only vocabulary/class fitting, inner split identity, selector/tie rules, calibration isolation, global scoring barrier, historical reproduction failures, coverage denominators, recipient support, permutation identity/invariance, metric arithmetic, null eligibility, strict aggregate schema, and monitor-failure isolation. Run the existing test suite. Hash-lock and commit the approved protocol, tested code, image, reference artifacts, and historical public/private preservation inventory before fitting. A scientific ambiguity requires review, not an unrecorded implementation choice.

Use the pinned CPU image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, UID/GID 10001, one numerical thread, network disabled, read-only root/project/data, and only new `artifacts/e015_attempt01` writable plus ephemeral scratch. Refuse an existing attempt directory. Do not replace an unavailable image or change dependencies without approval. No automatic retry, increased iterations, data download, external API, GPU, or next-model fallback.

Expected run time is **20–45 minutes for 150 classifier fits and aggregate reporting**, excluding implementation/testing/privacy review. This is an estimate from E014's approximately 5.5-minute 50-fit run with allowance for larger feature spaces and diagnostics, not an E015 pilot or a guarantee. Slower execution alone does not authorize changing scientific settings.

Keep the resilient terminal monitor active only during execution: experiment ID, status, elapsed time, completed fits/scoring work, stage, and latest completed metric. Before scoring, display metrics as unavailable. Terminal refresh does not imply chat notifications every few minutes; periodic chat updates are at most hourly while running, with completion/failure reported promptly. No monitor or scheduled wakeup is started for this protocol review.

Publish only allowlisted aggregate JSON, complete tables, code/tests, protocol and append-only log updates after secret/data/local-path scans and artifact checks. Never serialize student responses, answer strings, row identifiers, probability/prediction arrays, donor mappings, vocabularies, coefficients, or fitted models. Preserve every earlier experiment and attempt. Publish the approved plan and verified results as separate descriptive commits only to the existing personal repository. This review draft is not approval to execute.

## Prior art and contribution limits

The [official scikit-learn 1.5 documentation](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) specifies the default two-character token rule and custom-tokenizer interface. Retaining short words and mathematical symbols is not a novel learning algorithm. E015's contribution is the controlled, leakage-safe comparison and complete failure/uncertainty reporting for this question-shift setting; no priority claim is made.

The explanation permutation is a bounded fitted-model reliance diagnostic, consistent with the distinction between predictive reliance and causal reasoning discussed by [Fisher, Rudin and Dominici](https://jmlr.org/papers/v20/18-760.html). E015 does not implement their full model-class analysis or inferential guarantees. Neither source predicts that this tokenizer will improve MAP.
