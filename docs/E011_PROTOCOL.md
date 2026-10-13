# E011 selected answer context ablation

## Authorization and fixed decision

The user authorized E011 and, if it fails, another model. This protocol and the conditional [E012 protocol](E012_PROTOCOL.md) fix operational choices before new outcomes. These choices are agent-specified under that authorization, not separately user-approved numerical thresholds. Commit and publish the tested implementation and lock before fitting. Preserve E001–E010 and the research checkpoint.

H1: adding the student's selected answer to question plus explanation produces a meaningful improvement in held-question exact-label MAP@3. The full-context arm must beat **both** the unchanged question-plus-explanation arm and frequency by an equal-fold mean of at least **0.020**, and have a positive paired delta in at least **4/5 folds against each**. Both conditions against both comparators must hold without rounding or tolerance. This is a pragmatic research margin, not a safety standard.

H2, secondary: compare full context with question plus selected answer without explanation, to examine the incremental contribution of explanation text. Report the comparison regardless of its sign. No secondary metric, question or support subgroup substitutes for H1.

An unmet H1 after a valid completed run triggers the one preregistered E012 experiment. A runtime, reproduction, privacy or integrity failure is **not** scientific failure and stops the chain for investigation. A met H1 stops after E011. Stop after E012 regardless of outcome; no unlimited model search.

## Arms and leakage controls

Exactly three arms, all with TF–IDF and multinomial logistic regression:

1. `question_plus_explanation`: E001's exact `[QUESTION] ... [EXPLANATION] ...` input.
2. `full_context`: `[QUESTION] ... [ANSWER] ... [EXPLANATION] ...`, using only `QuestionText`, `MC_Answer`, and `StudentExplanation`.
3. `question_plus_answer`: `[QUESTION] ... [ANSWER] ...`, with no explanation.

Missing strings become empty; no rewriting, numeric normalization, external reasoning or generated annotations. Question identifiers, labels, row identifiers, answer-correctness flags, label-derived answer keys and question-specific label candidate lists are not features. `MC_Answer` is an observed student selection, not an oracle correct answer.

Use the **unchanged E001 word tokenizer and grid**, including its omission of single-character tokens. This isolates adding fields under that representation, not a test of all possible mathematical encodings. Record aggregate proportions of blank selected answers and selected answers producing zero tokens, per evaluation question and overall, without reporting answer text or vocabulary. An input benefit is not proof of mathematical reasoning; a failure may reflect representation limitations.

## Frozen training and calibration

Use the existing five outer QuestionId assignment folds and seed 20260831, with nine training, three calibration and three evaluation questions per fold. This returns to the E001/E006 classification roles, **not** E007's one-temperature/two-threshold subdivision. No assignments regenerated or altered.

Inner selection is GroupKFold(3), with `QuestionId.astype(str)` and the original coupled grid, in this order: unigram/min_df=2/C=0.5; unigram+bigram/min_df=2/C=1; unigram+bigram/min_df=5/C=2. TF–IDF sublinear_tf=True; logistic max_iter=2000, class_weight=None, random_state=20260831, n_jobs=1; all other scikit-learn 1.5.2 defaults unchanged. Each inner vocabulary/IDF/classifier fits only its inner training split. Maximize equal-inner-fold MAP@3; exact ties choose the first grid entry. No outer score selects settings. Any fit error or convergence warning stops; no silent fallback or added iterations.

Fit the selected setting on the nine training questions. Reuse E001's exact temperature fitter: supported calibration truths only, bounded log-temperature [-3,3], and probability clipping at 1e-12; no new calibration method. Record supported calibration counts and temperature. Frequency uses training-label prevalence and remains unscaled. Unsupported calibration rows are excluded as historically implemented, not claimed calibrated.

Prepare all 15 arm/fold models, temperatures and evaluation probabilities in memory before accessing evaluation labels for metrics. Freeze the development description to an aggregate-only file; serialize no model or row-level predictions. Evaluate only after that barrier. Reproduce all 30 E006/E001 reference checks for the unchanged arm and frequency: MAP@3, accuracy and ECE, five folds, absolute tolerance 1e-10 and relative tolerance zero. Mismatch stops publication and the conditional chain.

Data/manifest/assignment SHA-256 remain the values in the [reproduction guide](REPRODUCTION.md). Validate hashes, row order, target alignment, group-disjoint roles and exactly one outer evaluation per response before fitting and after evaluation. Reference JSON and all protocol/code/environment inputs are pinned in `experiments/e011_e012_lock.json`.

## Reporting and uncertainty

Confirmatory: all-row exact-label MAP@3 and the H1 Boolean/deltas. Report all five paired values, equal-fold mean, sample SD and positive-fold count for each comparator. No significance claims, bootstrap, permutation test or independent-confirmation claim: these 15 questions have already been repeatedly examined.

Prespecified secondary diagnostics for each arm and frequency, every fold and all 15 questions:

- Exact-label accuracy, MAP@3, top-1 risk, mean confidence, ECE (10 equal-width bins), union-label-corrected Brier and macro-F1 using the truth/prediction label union.
- Six-way Category accuracy and macro-F1 on the explicitly fixed labels `False_Correct`, `False_Misconception`, `False_Neither`, `True_Correct`, `True_Misconception`, `True_Neither`; Category probabilities sum exact-label probabilities. This explicit macro-F1 definition differs from E005's default union and must not be silently equated with it.
- Exact-label support strata: all, unsupported=0 training examples, rare=1–19, frequent>=20, nested well-supported>=20 across >=2 training questions. Empty groups stay null. These are after-the-fact reporting strata, never routing inputs.
- Calibration eligibility is fold/question/stratum local: n>=200, correct>=20, incorrect>=20; otherwise ECE/Brier null with reasons. Report denominator and eligible-fold counts. Unsupported truths cannot be correctly predicted by a closed-set model.

Also report all-row exact-label risk–coverage at fixed 0/10/20/30/40/50% review, for calibrated-confidence routing only, including the frequency reference. Pool each fold's three evaluation questions, defer floor(N*b/100), and resolve ties by the existing E006 SHA-256 serialization plus source position. Freeze ranks before truth. No threshold selection, best-budget claim or new support-aware learner. These are exploratory descriptive routing diagnostics, not automation certification. The input-token diagnostics are also exploratory. Do not add other analyses after seeing outcomes.

## Execution, publication and interpretation

The fully hashed CPU dependency closure is `repro/core.lock`, with its digest-pinned `repro/Dockerfile`; the separately built `map-modeling:e011` image is pinned in the execution lock. This environment contains every dependency required by these two models; it does not reconstruct historical encoder dependencies. Run as UID/GID 10001, single numerical thread, network disabled, root/project/data read-only, only the experiment's new artifact directory writable.

Expected E011 compute: roughly 15–40 minutes for 150 classifier fits plus reporting; an estimate, not a pilot result. Synthetic testing/build/publication checks add preparation time. Keep the read-only terminal monitor live while active, showing completed fits and latest completed metrics; stop it on completion/failure. At-most-hourly scheduled updates, never idle monitoring. Preserve failed attempts; no automatic retry.

Publish strict aggregate-only JSON and complete fold/question tables, checked against the locked schema and arithmetic. Never serialize student text, row IDs, answer strings, feature vocabularies, coefficients, neighbors, weights or probability arrays. Run synthetic tests, preservation checks and privacy/secret scans. Commit/push the plan first and each experiment's verified results separately, only to the personal repository. Show E011 numerical results before applying its preregistered E012 trigger.

A positive H1 supports additional input utility for this model on this reused benchmark, not mathematical reasoning or safe deployment. A negative H1 means this field addition fails the fixed useful-improvement criterion, not that selected answers contain no information. No post-hoc exclusion of questions or labels changes the outcome.

The MAP paper describes distractors designed around misconceptions and item-specific rubrics; it motivates examining selected-answer context, not an expected score gain. [Rittle-Johnson et al., 2025](https://aclanthology.org/2025.aimecon-wip.3.pdf)
