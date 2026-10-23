# E018 independently verified answer correctness with a matched frequency baseline

## Review status and research setting

Prepared 2026-10-20 against revision `496c5332b8b2201ea89abeb3cd51ede7ecd0187f`. **Proposed preregistration for review, not approval to implement, acquire keys, fit, or run.** No E018 key preparation, verification, pilot, fitting, scoring, attempt or monitor has started. No independently verified answer-key manifest is currently established. Execution requires approval of this specification and completion of the verification gate below.

Preserve E001–E017, their scientific code, protocols, approvals, locks, results, completed and failed attempts, and all frozen folds. Add E018 in new files and append to the experiment log without rewriting history.

The project studies generalization of mathematical-misconception detection to unseen K–12 math questions, with uncertainty-aware human review. E018 tests whether independently verified selected-answer correctness makes an existing explanation/context model more useful than a frequency baseline supplied with exactly the same information. It introduces neither a new classifier nor a new misconception annotation framework.

This is an **enriched-information, answer-key-available setting**. Question-held-out means the question supplies no training responses to that fold's classifier; it does not mean the assessment administrator lacks a verified mathematical solution. Human key preparation is part of the system's cost and input assumptions, not model reasoning or cost-free automation. Results must appear separately from original-input predictive results.

E017 found mean MAP@3 0.539215 for frequency, 0.511887 for E011, 0.653644 for frequency with true answer correctness, and 0.733311 with full true Category. Its truth-bearing oracle gains motivate this intervention but are not deployable results, promised scores, or thresholds to optimize toward. See [E017 results](E017_RESULTS.md). No E017 oracle output or answer-key reconstruction from MAP labels is an allowed E018 input.

## Hypotheses and analysis roles

**H1, sole primary predictive hypothesis:** on all held-question evaluation rows, correctness-grounded E011 improves exact-label MAP@3 meaningfully over correctness-grounded frequency. The same independently verified correctness signal, candidate rule and fallback apply to both. The practical criterion is an equal-fold mean paired gain of at least **+0.020**, strictly positive in at least **four of five folds**.

**H2, prespecified secondary information comparison:** correctness-grounded frequency improves over ordinary frequency. Report the magnitude and fold consistency, but do not substitute this result for H1 or call it a learned-model improvement.

**H3, prespecified secondary comparisons:** measure the effect of grounding E011, the grounded model's difference from ordinary frequency, and whether grounding changes the learned-versus-frequency gap. These are signed descriptive comparisons, not additional primary opportunities.

**H4, prespecified secondary signal audit:** quantify verified-signal availability, actual filtering coverage, and agreement with the existing MAP correctness component after freezing predictions. A disagreement measures a discrepancy between independent verification and existing labels; neither source is automatically declared wrong.

Fixed support/question analyses, verification-status groups, raw/final calibration and review-budget diagnostics are exploratory. They cannot replace H1. No explanation-shuffle experiment, new subgroup search, recalibration study, new classifier, ensemble search, unsupported-label generator, random-split rerun or E019 is included.

“Primary” and “secondary” identify prospective commitments, not independent statistical confirmation. The same 15 questions have repeatedly informed experiment design.

## Frozen data and evaluation

Keep the original `Category:Misconception` target, including literal `NA`, all 36,696 rows, source order and seed `20260831`. Keep five outer QuestionId folds, with nine training, three calibration and three evaluation questions per fold. Every row is evaluated once.

| Input | SHA-256 |
|---|---|
| Author-release training data | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |

The exact-label inventory and frequency counts come only from the nine outer training questions. Calibration rows never contribute counts, vocabulary or label columns. Supplying correctness never adds an exact label absent from training.

Use the fixed Categories `False_Correct`, `False_Misconception`, `False_Neither`, `True_Correct`, `True_Misconception`, `True_Neither`. The prefix denotes selected-answer correctness. Grounding supplies only this binary component; it never supplies explanation status, full Category or a misconception identity.

## Independent verification and the go or no go gate

### Allowed inputs and separation

Prepare a private, label-free catalogue of unique question text and selected-answer strings from the existing release. Retain QuestionId only for alignment, not as a learned feature. Do not expose student explanations, Category, Misconception, row identifiers, answer frequencies, response counts, fold assignments, per-question performance, model predictions or oracle records to verifiers. Question text must be consistent within each QuestionId; inconsistency stops preparation for review.

Catalogue access exposes the assessment content to key preparation, not response-label evidence. It is permitted only in this explicitly enriched-information setting. The resulting lookup does not claim to solve arbitrary future questions: an unseen question without a verified entry yields `unknown`.

Normalize lookup text using Unicode NFC, CRLF/CR to LF, and removal of leading/trailing whitespace only. Preserve case, internal whitespace, punctuation, units and mathematical notation. Freeze the exact implementation. Do not use fuzzy matching or infer correctness from answer popularity, labels, a model's preferences or numerical string inequality. Each distinct normalized selected answer needs its own semantic verification; a nonmatching string is not automatically incorrect.

### Exactly two admissible evidence routes

Choose the evidence route before any comparison with MAP correctness or prediction results:

1. **Primary key plus independent mathematical verification.** An exact-version answer key from the original question owner or dataset authors, obtained through a lawful documented source, plus a separate mathematical derivation and answer-equivalence check signed by a human reviewer with documented relevant mathematical competence. A merely matching topic or similar question is insufficient. The reviewer first records a solution without seeing the source key, then compares them. Both must agree.
2. **Two independent mathematical verifications when no admissible primary key exists.** Two distinct human reviewers with documented relevant mathematical competence independently solve the exact question and assess each selected answer, without seeing each other's decisions. Both must agree. Any calculation checks and relevant unit/domain assumptions are retained privately.

The source route depends on provenance availability, not which route agrees with MAP or yields better scores. Reviewer competence, source identity/rights, exact-version match, evidence, timestamps and independence attestations must be recorded. No reviewer may use the prohibited inputs above or a remembered MAP answer-label mapping. The current research agent cannot certify itself as two independent reviewers; two runs of one model are not independent human verification. Automated arithmetic checks may supplement human work but cannot replace a required sign-off. No fabricated reviewer, qualification, signature or blinding claim is permitted.

If the source key and derivation disagree, the reviewers disagree, a diagram or condition is missing, equivalence is ambiguous, rights/provenance are inadequate, or evidence/sign-off is absent, mark the affected answer `unknown`. Do not adjudicate against MAP labels, search for a preferred answer, or resolve it based on downstream scores. Source-wide uncertainty marks all affected entries unknown. This protocol does not authorize external messages, paid services, account changes or uploading assessment/student content to an external AI service.

### Private manifest and freeze

For every catalogue entry record exactly one of `verified_true`, `verified_false`, or `unknown`, with a reason and evidence references. Retain question/answer text, keys, derivations and reviewer identity evidence only in ignored private storage. The public receipt contains the manifest SHA-256, preparation code/version hashes, source-route counts, reviewer count and independence/competence attestation status, timing/cost summaries and aggregate coverage; it contains no key mappings, answer text or per-entry digests that would facilitate dictionary recovery. Aggregate QuestionId counts are allowed.

Freeze the manifest for all 15 questions in one step before any E018 fitting, historical reconstruction or MAP-label agreement check. Do not prepare a key selectively for a high-performing question, revise entries fold by fold, or add answers after seeing scores. Use the same entry wherever that question/answer is encountered; MAP training/calibration labels cannot create or repair entries.

Gate requirements are approved protocol, complete catalogue accounting including unknown entries, required evidence for every verified entry, lawful local use, no prohibited-input exposure, a hash-locked manifest and at least one verified evaluation-row decision. This is a feasibility gate, not a minimum-accuracy or selected-coverage rule. There is no performance-based gate. If all entries are unknown, record blocked feasibility and stop without fitting; do not silently substitute oracle labels or a different solver.

Missing reviewers or source access may therefore block execution. Approval of this design is not evidence that independent verification has occurred. After approval, source-specific provenance and receipts supplement the lock; they do not change the evidence rules. A need for different verification methods or scientific settings requires a revised protocol and approval before execution.

## Four fixed predictive arms

| Identifier | Base predictions | Correctness information |
|---|---|---|
| F | Original exact-label training frequency | None |
| L | Original E011 full-context TF–IDF/logistic system | None |
| F_G | F with the fixed grounding transformation below | Frozen independent manifest |
| L_G | L with the identical grounding transformation | The same frozen manifest |

F and L are historical reproduction controls. F_G is the matched enriched-information baseline; L_G is the sole primary candidate. Grounding does not change features, fit a component predictor, retune hyperparameters, reweight training observations or condition frequency counts on a held-out question. It is a fixed post-processing intervention.

## Historical fitting and calibration remain unchanged

Reconstruct L once per fold through unchanged historical preparation functions, importing rather than editing them. The five preparations require **50 classifier fits**: nine inner fits and one refit per fold. Reuse each preparation for L and L_G. F requires no classifier fitting; do not refit E016.

Input remains:

```text
[QUESTION] {QuestionText} [ANSWER] {MC_Answer} [EXPLANATION] {StudentExplanation}
```

Missing text becomes empty. Retain the default word tokenizer `r"(?u)\b\w\w+\b"`, lowercasing, no stop words/accent stripping, sublinear TF, L2 normalization, smooth IDF, no feature cap and pinned scikit-learn 1.5.2 defaults. Logistic regression uses `max_iter=2000`, `class_weight=None`, `random_state=20260831`, `n_jobs=1`.

Use the original GroupKFold(3) on QuestionId.astype(str) inside the nine training questions and ordered coupled grid:

1. Unigram, min_df=2, C=0.5.
2. Unigram+bigram, min_df=2, C=1.
3. Unigram+bigram, min_df=5, C=2.

Select by equal-inner-fold **ungrounded raw exact-label MAP@3**, with exact ties choosing the first entry. Recompute vocabulary, IDF and label inventory inside every inner training partition. Do not select using grounded scores, calibration-question performance or outer evaluation results. Refit the selected historical setting on all nine training questions.

Fit the original exact-label temperature on the three calibration questions, using supported exact truths only, NLL minimization, log-temperature in [-3,3], clipping at 1e-12 and T=1 if no calibration truth is supported. F remains unscaled. No grounding is used to fit a temperature. Apply grounding separately to the original raw and original final probability arrays, **after historical temperature scaling for the final pipeline**.

Consequently, final grounded probabilities inherit a temperature fitted for the ungrounded model; they are not claimed to be calibrated for the enriched setting. Measuring that limitation is part of E018. No after-grounding temperature refit, ordering search or smoothing is allowed.

## Exact grounding and ranking rules

Let Y be the unchanged sorted outer-training exact-label inventory. For row x, obtain g(x) in {true, false, unknown} from the frozen manifest using only its question and selected answer. Both grounded arms receive the identical g. Define compatibility by the correctness prefix of labels in Y, never by a held-out truth.

For each base arm A in {F,L} and scale in {raw,final}:

1. If g is unknown, copy A's probabilities, complete rank order and top-1 prediction unchanged. Mark `fallback_unknown`.
2. If g is verified but no label in Y has its correctness prefix, copy A unchanged and mark `fallback_no_candidate`. Do not invent an exact-label column or emit an empty probability distribution.
3. Otherwise mark `grounded`. Keep only compatible labels and normalize their original probability mass:

```text
p_A_G(y | x) = p_A(y | x) * 1[correctness(y) = g(x)]
              / sum_z(p_A(z | x) * 1[correctness(z) = g(x)])
```

A nonfinite vector or nonpositive compatible mass with a nonempty compatible inventory is an integrity failure, not a fallback or opportunity to add epsilon mass. Compatibility and fallback state must be identical for F_G and L_G. All rows, including fallback rows, remain in primary denominators.

For MAP@3, compute the complete original base ordering using the pinned `np.argsort(-p_A)` convention. For grounded rows use its compatible **stable subsequence**, preserving the original tie order. Do not re-sort renormalized values, backfill incompatible labels, duplicate entries, or pad a list shorter than three. Fallback rows use the original first three entries. Score reciprocal rank 1, 1/2 or 1/3 if the exact truth is present, otherwise zero.

For exact top-1 accuracy, separately select the highest original probability among compatible labels, with ties resolved by the first label in original sorted Y order, matching historical argmax semantics. On fallback rows use the historical argmax. Preserve the distinction between argmax and argsort tie rules.

Confidence is the maximum transformed probability. Retain all original training-label columns, with zero mass assigned to incompatible labels. Unsupported exact truths always score zero and remain in union-label Brier denominators. Hard filtering can be confidently wrong if verified correctness disagrees with the target; do not restore mass using that target.

No oracle truth enters this transformation. After freezing, synthetic and truth-bearing checks must establish: identity on fallback; compatible-only ranks; probability normalization; unchanged within-compatible ordering; and zero exact credit for unsupported truths. For rows whose verified g agrees with MAP correctness, grounding cannot decrease that row's reciprocal rank or exact accuracy. Rows with disagreement are not subject to that monotonicity expectation and must not trigger label correction.

## Primary estimand and fixed contrasts

For fold f, use all its evaluation rows and define:

```text
D_f = MAP@3(L_G)_f - MAP@3(F_G)_f
```

H1 is met only if the unrounded equal-five-fold mean D >= +0.020 and D_f > 0 in at least four folds. Use no decision tolerance. Report all five paired differences, their mean, sample SD (ddof=1), positive-fold count and the Boolean criterion. A positive but smaller/inconsistent gain is not a meaningful-baseline-win claim.

Report these five contrasts for exact MAP@3 and accuracy on the fixed reporting grid: L_G−F_G (primary), F_G−F, L_G−L, L_G−F, and L−F (historical control). Also report the difference-in-differences `(L_G−F_G)−(L−F)` descriptively. This is an arithmetic interaction summary, not causal identification. For F_G−F alone, report the same +0.020/four-positive-fold flag as a **secondary information-benefit descriptor**, never a substitute for H1. No other contrast receives a binary success flag.

## Complete reporting populations and metrics

All four arms must report n, exact accuracy and MAP@3 for every outer fold, every one of the 15 held-out questions, and these unchanged support strata:

- All rows.
- Unsupported: zero outer-training examples of the exact truth.
- Rare: 1–19 examples.
- Frequent: at least 20 examples.
- Well-supported: at least 20 examples across at least two outer-training questions, nested within frequent.

Support is computed from the original nine training questions and used only for evaluation. Do not recompute it within correctness-compatible candidates, use it for gating, omit unsupported rows, or merge empty strata. Empty groups have null metrics with n=0.

In a separate exploratory panel, report all-row fold/question results partitioned by the three shared processing states `grounded`, `fallback_unknown`, `fallback_no_candidate`. Do not cross these with support or add further outcome-selected subgroups. These states sum to the original population; no grounded-only headline replaces the all-row primary outcome.

For H4 report by fold/question: total rows; verified-decision count/share; grounded count/share; each fallback count/share; and a two-by-two confusion matrix comparing verified g with MAP correctness only among verified rows. Matrix rows use MAP correctness and columns use independent g, both ordered [false,true]. Report agreement and disagreement rates with their verified-row denominator, plus unknown counts. If no row is verified, rates are null. The correctness agreement audit occurs only after prediction freeze and does not assert that MAP is an infallible answer key.

Publish aggregate verification workload separately: questions and distinct question/answer entries considered, verified/unknown counts, source-route counts, unresolved-reason counts, reviewer count, recorded human minutes, preparation wall time and actual monetary cost if any. Unrecorded duration/cost is null, never assumed zero. Do not publish answer-level keys, mappings or evidence text.

## Calibration and human review diagnostics

For every arm, both raw and final scales, and the fixed fold/question/support grid, report exact accuracy, mean maximum exact-label confidence, signed confidence-minus-accuracy, 10-equal-width-bin ECE and corrected union-label Brier. Accuracy and mean confidence are defined for nonempty groups. ECE/Brier eligibility remains local: n>=200, correct>=20 and incorrect>=20; otherwise null with all applicable reasons. Paired changes use only jointly eligible groups and report eligible counts.

Use the unchanged union-label Brier convention, including zero predicted mass for exact truths absent from training. Do not substitute supported-only Brier, remove hard-filter mistakes, or clip grounded zeros to hide errors. Report paired final-minus-raw changes per arm and each of the five fixed arm contrasts at each scale for calibration measures. They are exploratory diagnostics, not selection criteria.

At fixed review budgets 0%, 10%, 20%, 30%, 40% and 50%, independently within each fold's three pooled evaluation questions, defer exactly floor(N*b/100) rows with lowest final confidence. Use unchanged E006 SHA-256/source-position tie rules and seed. Freeze routing before truth access. The same budgets and tie rules apply to all four arms, but retained subsets can differ.

Report retained n/coverage, exact accuracy, MAP@3, top-1 risk, mean confidence, confidence-minus-accuracy and eligible ECE/Brier at every budget. Publish all fold values and equal-fold summaries, plus L_G−F_G and F_G−F contrasts at every budget. The six points form a descriptive risk–coverage profile, not a threshold selected for deployment. No additional AURC, budget selection, support-aware routing, review policy for unknown entries or fitted rejection threshold is introduced. Unknown correctness invokes unchanged predictions, not automatic deferral; the confidence rule alone determines these diagnostic review sets.

No claim of safe automation follows from a ranking gain or lower observed retained risk. Key errors, unknown-key fallback, unsupported labels and calibration under shift remain visible.

## Descriptive uncertainty and interpretation

Report every fold and question. Metrics and contrasts use equal-fold means, sample SDs and defined-fold counts; a contrast uses only jointly defined folds. SD is null with fewer than two defined folds. Counts can be pooled with an explicit count label; pooled confusion counts and row-normalized rates do not replace equal-fold performance. Empty confusion rows have null normalized values. H1 always uses all five nonempty all-row folds.

No bootstrap, permutation test, p-value, significance/equivalence test, selected correlation, best-fold report or new subgroup is included. Training sets overlap and 15 questions have been reused adaptively. Neither fold dispersion nor this preregistration establishes performance on independent future questions. Authentic/synthetic identity is unavailable at row level; do not claim authentic-only or student-independent validation.

| Outcome | Registered interpretation |
|---|---|
| H1 met | The existing learned explanation/context system adds a meaningful ranking gain over a baseline given identical verified correctness on this reused benchmark; not proof of mathematical reasoning or future-question reliability |
| F_G−F meets its secondary flag but H1 fails | Verified correctness helps this system; no meaningful incremental learned-model benefit is demonstrated |
| L_G beats F but not F_G | Added information explains the apparent baseline win; do not credit it as learned-model success |
| H1 misses with a small positive difference | Quantified sub-threshold or inconsistent incremental benefit, not a meaningful win or proof of equivalence |
| Both grounding contrasts are nonpositive | This particular verification/filtering intervention does not improve mean performance; examine the registered availability/agreement and calibration summaries without changing keys |
| Gains appear only among grounded or well-supported rows | Localized descriptive benefit, not replacement of the all-row result |
| Verified decisions disagree with MAP correctness | Preserve the frozen evidence and labels, report discrepancy rates, and make no post-score key repair or relabeling in E018 |
| Accuracy improves while calibration or retained risk worsens | Ranking/accuracy utility and uncertainty quality diverge; no safety claim |
| No admissible verification or every entry unknown | Feasibility blocked, not a model failure and not permission to use oracle labels |
| Technical, integrity or historical reproduction failure | Preserve the incomplete attempt and stop for review; no automatic retry or scientific fallback |

F_G equaling the earlier correctness oracle would be expected if all rows have matching verified decisions and compatible candidates. That would be a control observation, not a discovery that the model acquired correctness. Do not rerun an oracle, calculate a new oracle-gap analysis, or combine oracle and predictive results in one leaderboard.

## Freeze order and integrity checks

After approval, complete the verification gate first. Before fitting, hash-lock the approved protocol, separate approval record, new tested implementation, private key manifest, source/evidence receipts, historical references, Docker identity and complete public/private preservation inventory. Commit only sanitized plan/code/aggregate receipts to the existing personal repository. Never commit private key material.

Reconstruct all five historical L preparations and freeze selections, candidate inner scores, temperatures, raw/final probabilities, F probabilities, training inventories/counts and source alignment. Apply the frozen grounding operation and freeze both grounded outputs and all review-routing orders globally. The model-preparation layer receives label-free evaluation features; the key lookup receives only assessment content. Only after this global freeze may a separate scorer read evaluation truths for historical reproduction, agreement checks, support and final results.

Reproduce F/L historical development and applicable exact-label fold/question/support, raw/final calibration, Category and fixed-review records against the pinned E016/E017 and earlier reference artifacts. Require identical categorical values, counts and null patterns; numeric absolute tolerance 1e-10, relative tolerance zero. Historical-only Category reproduction is an integrity check, not a new E018 Category analysis. No shuffle rerun is required. Reproduction must pass before releasing grounded performance.

Synthetic tests cover lookup normalization/unknowns, forbidden-field isolation, manifest evidence requirements, stable tied ranking, argmax versus argsort, short compatible lists, absent correctness candidates, zero/nonfinite mass, shared fallback state, raw/final order, unsupported truths, union Brier, eligibility, fixed routing, decomposition counts, primary decision boundaries and aggregate privacy. Test monotonicity only when the supplied correctness agrees with truth; deliberate disagreement fixtures must permit degradation.

Run the existing full test suite and publication scans. Check data/fold hashes, all prior scientific files and attempts, private evidence, key manifest and append-only log preservation before/after execution. A fit warning, reproduction mismatch, unverified claimed entry, changed hash, leaked target input or scientific ambiguity stops the attempt. Do not fix an outcome by changing keys, rules, thresholds, folds, calibration, dependencies or model settings.

## Execution budget and publication

After all gates, use the existing CPU image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, UID/GID 10001, one numerical thread, network disabled, read-only root/project/data/key inputs, and only a new `artifacts/e018_attempt01` writable plus ephemeral scratch. Refuse an existing attempt directory. Preserve private verification materials in a separate new ignored E018 directory, read-only to the experiment. Do not modify old attempts. No GPU, model download, paid API or dependency change is part of this protocol.

Estimated Docker computation is **5–15 minutes for 50 historical fits and aggregate reporting**, excluding implementation, tests and publication checks. E017's 100 fits and diagnostics took about seven minutes; this estimate is not a pilot. Independent key preparation is a separate prerequisite with **no reliable completion-time estimate until sources and qualified reviewers are available**. Do not describe the entire experiment as a five-minute task.

Keep the resilient terminal monitor active during the Docker run only: E018, status, elapsed time, completed work units, stage and latest completed metric. Before scoring, metrics are unavailable. Show grounded and original-input results with explicit labels and use F_G as L_G's matched comparison. Progress counts work items, not estimated elapsed-time percentage. Periodic chat updates are at most hourly while active; completion/failure is reported promptly. No idle monitoring or wakeup is started for this review.

Serialize aggregate-only results with distinct `original_input_controls`, `enriched_information_predictions`, `verification_audit` and `integrity` sections. First show complete aggregate and fold-level numerical results, then the fixed question/support, availability/agreement, calibration and review tables. Await user review before interpretation or a subsequent experiment proposal.

Publish only allowlisted code/tests, protocol, aggregate provenance receipts, aggregate JSON/tables, execution documentation and append-only experiment history after secret/data/local-path scans. Never publish raw student/assessment text, selected answers, key mappings, derivations, row identifiers, exact-label identities, predictions/probability arrays, vocabularies, weights, models, credentials or private reviewer records. This preserves [existing data rules](DATA_AND_LICENSES.md); a new source's rights must be checked before use, with only a sanitized provenance supplement added in new E018 documentation.

Approved implementation and verified results receive separate descriptive commits only to the existing `traghuram444/responsible-ai-math-misconceptions` repository. Preserve negative results and all earlier history. This draft does not authorize a run, publication of results, E019 or an automatic alternative model.

## Prior art and scope of contribution

The [Learning Agency MAP description](https://the-learning-agency.com/datasets/misconceptions-preliminary/) separates answer correctness from explanation/misconception assessment and discusses rule-based correctness evaluation. E018 does not claim this decomposition as a novel algorithm, borrow the provider's performance thresholds, or compare its differently evaluated model scores with this project's held-question results.

[Guo et al.](https://proceedings.mlr.press/v70/guo17a.html) describe temperature scaling. Retaining the historical temperature method does not establish calibration after correctness filtering or under question shift.

The contribution sought is a controlled, reproducible test of externally verified correctness and incremental learned-model value under the frozen question-shift framework, with matched information, explicit verification cost/coverage, uncertainty reporting and preserved negative results.
