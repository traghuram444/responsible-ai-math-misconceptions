# E017 component information and fixed frequency ranking limits

## Review status and purpose

Prepared 2026-10-19 against revision `fc78f08b833d75faf1cdd0076d0a089be68456e1`. **Proposed preregistration for review, not approval to implement or run.** No E017 fitting, component scoring, oracle scoring, pilot, attempt or monitor has started. Approval of this exact specification is required before execution.

Preserve E001–E016, all scientific files, protocols, approvals, locks, results, failed and completed attempts, and frozen assignments. Add E017 in new files; append to the experiment log without rewriting history.

The project studies generalization of mathematical-misconception detection to unseen K–12 math questions, with uncertainty-aware human review. E017 is a bounded diagnostic experiment, not a new classifier or a search for an improved headline score. It asks how much perfect information about existing Category components would help a fixed training-frequency ranker, which components existing models predict poorly, and how much exact-label error remains after supplying the full Category.

E016's direct Category/frequency system scored mean MAP@3 0.481557, versus E011 0.511887 and frequency 0.539215. E016's raw Category macro-F1 increased relative to E011, but its raw Category accuracy decreased. Those existing results motivate component decomposition, without establishing the cause of the failures. See [E016 results](E016_RESULTS.md).

## Research questions and analysis roles

**H1, sole primary diagnostic hypothesis:** supplying the true full Category yields substantial all-row exact-label MAP@3 headroom over the unchanged training-frequency baseline, under the fixed frequency ordering defined below. The magnitude and fold-consistency criterion is specified below. Meeting it is an oracle-information finding, never a predictive success.

**H2, prespecified secondary diagnostic questions:** how much headroom is obtained from answer correctness alone, from explanation status alone, and from adding the second component after the first? There is no preregistered expectation that one component dominates. Report all six fixed oracle contrasts; do not choose the largest as a new primary outcome.

**H3, prespecified secondary real-prediction questions:** for unchanged E016, E011 and frequency outputs, what are binary correctness, three-way explanation-status and six-way Category performance? Report both accuracy and fixed-class macro-F1, their full confusion matrices and paired contrasts. No positive-direction hypothesis or binary pass criterion is imposed on these decomposition metrics.

**H4, prespecified secondary diagnostic question:** how much residual full-Category-oracle error is attributable arithmetically to unsupported exact truths versus imperfect within-Category frequency rank among supported truths? This is a decomposition of this scoring procedure, not a causal attribution of all learned-model errors.

Support and per-question heterogeneity, joint component error counts, and raw-versus-final differences are fixed exploratory analyses. They cannot replace H1. “Primary” and “secondary” designate prospective reporting commitments, not formal statistical confirmation: the same 15 questions have informed earlier research decisions.

## Existing targets and partitions

Keep the original exact `Category:Misconception` target, including literal `NA`. Parse Category before the first colon and verify agreement with the original Category field. Parse the two components only from these six allowed Categories:

```text
False_Correct
False_Misconception
False_Neither
True_Correct
True_Misconception
True_Neither
```

The first component is selected-answer correctness, with fixed order `[False, True]`. The second is explanation status, with fixed order `[Correct, Misconception, Neither]`. “Correct” here is an existing label, not a new expert judgment. No relabeling, grouping of misconception identities, annotation framework or inferred answer key is introduced.

Use the unchanged five outer QuestionId folds: nine training, three calibration and three evaluation questions per fold; each of the 36,696 rows is evaluated once. Preserve source order and seed `20260831`. Calibration rows never contribute to frequency counts, vocabulary, label inventory or conditional ranking.

| Input | SHA-256 |
|---|---|
| Training data | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |

No random-split rerun, new split, external data, answer-key acquisition or model download is included.

## Two strictly separate result panels

### Real prediction controls

| Identifier | Output | Evaluation truth as input |
|---|---|---|
| F | Unchanged training exact-label frequency | No |
| E011 | Unchanged full-context exact-label TF–IDF/logistic system | No |
| E016 | Unchanged direct Category/frequency system | No |

These are historical prediction systems reconstructed for new diagnostics, not new E017 predictive candidates. Report their original exact-label results and historical reproduction status in the real-prediction panel. Do not rename an oracle as a model, include it in a predictive leaderboard, or update the project's best predictive score with an oracle value.

### Oracle information diagnostics

| Identifier | Deliberately supplied evaluation information | Ranking operation |
|---|---|---|
| O_C | True selected-answer correctness | Keep training labels with that correctness component |
| O_S | True explanation status | Keep training labels with that explanation-status component |
| O_CS | True full Category, both components | Keep training labels with that Category |

F is repeated as a clearly labeled shared reference in this panel. Every oracle table and artifact record must identify the arm as an **oracle diagnostic using evaluation truth**, not a real prediction result. The oracle is not a mathematical solver, expert annotation service, calibrated classifier or prediction-time support signal.

## Exact oracle ranking algorithm

For each fold let Y be the original sorted exact-label inventory observed in its nine training questions, and let p_F(y) be the unchanged training prevalence. Freeze these quantities and a complete baseline ranking before exposing evaluation truth.

1. Compute the full baseline ordering with the existing pinned NumPy convention `np.argsort(-p_F)`, without truncating to three. Its first three entries must exactly reproduce F's historical MAP@3 list.
2. For each possible correctness value, status value and full Category, precompute the compatible subsequence of that complete ordering. Filtering preserves the original relative order, including ties. Do not re-sort a filtered vector, change sort kind, add smoothing, or use held-out frequencies.
3. In the diagnostic scorer only, use the recipient row's true component to choose the corresponding precomputed list. Its first at most three labels define the oracle MAP@3 prediction. Do not backfill from incompatible Categories. An empty list scores zero; a list shorter than three uses only its available positions, without duplicates.
4. Preserve historical top-1 accuracy semantics separately: among compatible labels choose the maximum training prevalence, with ties resolved by the first label in the original sorted Y order, as with `np.argmax`. Empty candidate sets have no prediction and score zero. F uses its original unfiltered argmax. Do not silently equate argsort's first tied item with argmax's tied item; the historical MAP and accuracy conventions are distinct.
5. Score exact truth with reciprocal rank 1, 1/2 or 1/3 if present in the MAP list, otherwise zero. Exact accuracy uses the separate top-1 rule. An unsupported exact truth always scores zero for every arm; supplying its Category never creates a new exact-label column.

All compatibility masks and rankings come only from training labels and the fixed six-name taxonomy. Do not derive per-question or per-answer eligibility lists from evaluation labels. No renormalized oracle probabilities, temperature, confidence, ECE, Brier or review policy are defined. Those would condition on truth unavailable at prediction time and do not measure deployable uncertainty.

Check rowwise non-decrease of reciprocal rank and accuracy under nested filtering: O_C >= F, O_S >= F, O_CS >= O_C and O_CS >= O_S. Unsupported truths remain zero. There is no ordering constraint between O_C and O_S. Failures of these identities are implementation failures, not surprising scientific results.

O_CS is an information benchmark for this fixed within-Category frequency ordering and its exact tie convention. It is not a universal performance ceiling, a ceiling for all learned rankers, or an estimate of what a realistic correctness/status predictor can achieve. Do not assume it upper-bounds E011 or every tied ranking obtainable from E016.

## Reconstruct existing predictions without changing their science

Reconstruct E011 and E016 using the unchanged E016 preparation functions in new E017 orchestration; import historical modules without editing them. Run the original nested procedure, not a refit using settings chosen after inspecting E017. Both arms use:

```text
[QUESTION] {QuestionText} [ANSWER] {MC_Answer} [EXPLANATION] {StudentExplanation}
```

Missing input text becomes empty. Keep the default word tokenizer `r"(?u)\b\w\w+\b"`, lowercasing, no stop words or accent stripping, sublinear TF, L2 normalization, smooth IDF, no feature cap and pinned scikit-learn 1.5.2 defaults. Logistic regression keeps `max_iter=2000`, `class_weight=None`, `random_state=20260831` and `n_jobs=1`.

Keep GroupKFold(3) on QuestionId.astype(str) inside the nine training questions and exactly this ordered coupled grid: unigram/min_df=2/C=0.5; unigram+bigram/min_df=2/C=1; unigram+bigram/min_df=5/C=2. Maximize equal-inner-fold raw exact-label MAP@3, with exact ties choosing the first entry. Recompute vocabulary, IDF, label inventory and E016 conditional frequencies inside each inner training partition. E016 learns Category and reconstructs exact probabilities with training-only within-Category frequencies, exactly as before.

Refit on all nine training questions. Keep original exact-label temperature calibration on the three calibration questions: supported exact truths only, NLL minimization, log-temperature bounded to [-3,3], clipping at 1e-12, and T=1 with count zero when no calibration truth is supported. Frequency stays unscaled. No component-specific calibration, tuning metric, feature, solver, class weight or extra grid entry is allowed.

This requires 100 classifier fits: nine inner fits plus one refit per arm/fold. No new model specification is introduced; these fits reconstruct the two approved historical pipelines. Do not rerun shuffle experiments or select between E014/E015/E016 candidates.

## Real component prediction definitions

For each of F, E011 and E016, form the fixed-six Category distribution at both stages:

- Raw: direct aligned Category probabilities for E016; raw exact-label probability sums by Category for E011 and F.
- Final: sums of final exact-label probabilities by Category for E016 and E011; unchanged sums for F.

Sum these Category probabilities over the other component to obtain a two-column correctness distribution and a three-column status distribution. Take argmax with the fixed component orders above. Use the fixed six-name order for six-way Category argmax. Absent training Categories contribute zero probability.

Component decisions come from marginalized probabilities, **not** from splitting the hard six-way prediction or the hard exact-label prediction. The pair of independently predicted components can differ from the hard six-way prediction; report them as distinct outputs. Raw component results are the designated secondary comparison; final results are mandatory companion diagnostics, not an alternative selected for a better score.

For each component and six-way Category report accuracy, macro-F1 using all 2/3/6 fixed classes with `zero_division=0`, raw count confusion matrices (rows truth, columns prediction), and row-normalized matrices. A zero-support truth row has null normalized entries, not inferred performance. Empty analysis groups have null metrics, not zero accuracy/F1. Count matrices always retain their fixed dimensions.

## Reporting populations and exact metrics

Use the existing support definitions based on the recipient's exact truth in the nine training questions, for evaluation only:

- All rows.
- Unsupported: zero training examples.
- Rare: 1–19 training examples.
- Frequent: at least 20 training examples.
- Well-supported: at least 20 examples across at least two training questions, nested within frequent.

No support definition enters any real predictor or oracle candidate list. Report every stratum, even if empty. Do not combine or drop rare/unsupported strata after seeing counts.

For all six arms F, E011, E016, O_C, O_S and O_CS, report n, exact accuracy and MAP@3 for each fold pooled over its three evaluation questions and for each of the 15 questions, crossed with all five support strata. Keep real and oracle panels separate. Aggregate fold metrics with equal fold weights; do not replace them with pooled-row or question-weighted performance.

Fixed oracle contrasts, for both exact metrics on that same grid, are O_C−F, O_S−F, O_CS−F, O_CS−O_C, O_CS−O_S and O_C−O_S. Fixed real-prediction contrasts are E016−F, E011−F and E016−E011. Also report O_CS−E016 and O_CS−E011 in the oracle panel only as information-benchmark gaps, not attainable model gains or error attribution. Signed differences can be negative for these last two comparisons.

Component and six-way tables use the three real controls, both raw/final stages, and the same complete fold/question/support grid. Report the three real-prediction pairwise contrasts for accuracy and macro-F1. For each group also report counts/shares of independently predicted component outcomes: both correct, correctness only correct, status only correct, neither correct. These four outcomes partition the group; they are exploratory diagnostics, not new training labels or selectable subgroups for a headline score.

For all-row full-Category oracle results, publish five mutually exclusive counts/shares for each fold and question: unsupported exact truth; supported truth at compatible-list rank 1, 2, 3, or greater than 3. These rank bands concern the frozen MAP list, not the separate top-1 tie rule. Verify that the shares sum to one and reproduce MAP@3 as share_rank1 + share_rank2/2 + share_rank3/3.

For both exact metrics m, decompose full-Category residual loss on all rows as:

```text
unsupported_loss = mean(1[exact truth unsupported])
supported_ranking_loss_m = mean(1[exact truth supported] * (1 - row_score_O_CS_m))
1 - score_O_CS_m = unsupported_loss + supported_ranking_loss_m
```

Both loss terms use the full group denominator. Report them by fold and question and as equal-fold summaries. This explicitly distinguishes inability to emit an unseen label from residual fixed-frequency ranking errors; it does not diagnose annotation validity or mathematical reasoning.

## Primary diagnostic decision and descriptive uncertainty

For fold f let D_f = MAP@3(O_CS)_f − MAP@3(F)_f on all evaluation rows. H1's substantial-headroom criterion is met only when the unrounded equal-fold mean D is **at least +0.020** and D_f is **strictly positive in at least four of five folds**. Report the full five paired values, mean, sample SD (ddof=1), positive-fold count and Boolean decision. Use no decision tolerance. This reuses the project's practical magnitude convention but changes its meaning explicitly to **oracle information headroom**, not predictive improvement.

For the secondary O_C−F and O_S−F comparisons, report the same magnitude/consistency flags as secondary headroom descriptors; neither can replace H1. No other contrast receives a binary success label. Non-decrease alone is guaranteed by filtering and is not evidence of useful predictive learning. Report gains below the criterion as quantified sub-threshold or inconsistent headroom, not proof of no benefit.

All metrics and paired contrasts have equal-fold means, sample SDs and defined-fold counts. Empty groups remain null; SD is null with fewer than two defined folds. Use only jointly defined folds for a paired contrast. Publish every fold and every question, without selecting favorable cases. Count summaries may sum all evaluation rows, clearly labeled as counts; pooled confusion counts and their row normalization are descriptive and must not replace equal-fold accuracy/F1.

No bootstrap, permutation test, p-value, significance/equivalence claim, correlation search or independent-sample confidence interval is included. Overlapping training sets and adaptive reuse of 15 questions preclude treating five fold values as five independent validation studies. No claim of population safety, authentic-only performance, student-level independence or deployment readiness follows from this experiment.

## Truth isolation and integrity gates

Before scoring new outcomes, reconstruct and globally freeze all ten real arm/fold preparations, selections, temperatures, raw/final predictions, train-only counts, label inventory, complete frequency orderings and all possible component-compatible lists. Predictors receive label-free evaluation features only. Do not pass evaluation correctness, status, Category, exact truth or support to model preparation.

Write an aggregate-only freeze receipt. Only then may a separate truth-bearing diagnostic scorer select an oracle list using the recipient's true component and compute metrics. The new oracle outputs must never flow back into training, tuning, calibration, predictor inputs, routing or candidate construction. This is deliberate evaluation-truth use for a labeled diagnostic, not a leakage-safe deployable prediction arm.

Before releasing new component/oracle scores, reproduce E016's and E011's development selections, all candidate inner scores, temperatures, supported calibration counts and original non-perturbation records against pinned historical artifacts: exact fold/question/support metrics, raw/final calibration records, six-way Category records, frequency agreement and gain/loss records, and fixed-review records. Reproduce F in the same applicable records. Require identical categorical values, counts and null patterns, and absolute numerical tolerance 1e-10 with relative tolerance zero. Shuffle scores are outside this reproduction scope and remain preserved unchanged on disk.

Check training/data/fold identities, role disjointness, row alignment, Category parsing, label-free preparation, global freezing and complete historical public/private preservation inventories before and after execution. Hash-lock the approved protocol, new implementation, references, image identity and preservation inventory before fitting. A reproduction failure, fit warning, integrity violation, unknown Category, empty vocabulary or other scientific ambiguity stops the attempt for review. Do not adjust a setting to match an outer result, silently substitute an image or automatically retry.

## Registered interpretation rules

| Outcome | Permitted interpretation and next-step constraint |
|---|---|
| O_CS meets H1 | Perfect Category information creates substantial headroom for this fixed frequency ranker on the reused benchmark; no new predictive win has occurred |
| O_C meets its secondary headroom criterion | Correctness information is a promising component to obtain independently; any later answer key or correctness mechanism needs its own protocol and must not be derived from held-out labels |
| O_S meets its secondary headroom criterion | Reliable explanation-status information has diagnostic value; the result does not establish that current representations can acquire it |
| Both single-component gains are small but O_CS gain is substantial | Joint information is useful under this ranking rule; report the incremental contrasts without claiming statistical interaction or causal synergy |
| O_CS misses H1 | This fixed Category-filtered frequency rule does not meet the substantial-headroom criterion; report the actual gain, fold pattern and residual decomposition, without concluding all Category-aware methods fail |
| A component has oracle headroom but real component prediction is weak relative to F | Better independent component prediction is motivated, but realizability and attainable exact-label improvement remain untested |
| Real component accuracy and macro-F1 disagree, or raw/final results disagree | Retain both; no unqualified component-improvement claim and no replacement of the designated raw comparison |
| Supported ranking loss remains after full Category information | Fixed within-Category ordering leaves measurable residual error; improving that ranking is a possible later hypothesis, not a proven remedy |
| Unsupported loss is large | The training-only label inventory limits attainable exact-label recall; do not remove these rows or expand the inventory using held-out truths |
| Headroom is concentrated in particular questions or support strata | Report heterogeneity without choosing a favorable subgroup as the project's result |
| Integrity or reproduction fails | Incomplete technical attempt, not a scientific negative; preserve it and stop for review |

No automatic E018, ensemble, expert rubric, threshold search or model switch is authorized by any outcome. Report complete aggregate and fold-level numerical tables first, followed by the fixed question/support, component confusion and residual tables. Await user review before interpretation or a subsequent experiment proposal.

## Execution and publication after approval only

Implement new E017 code and tests only after approval, with a separate approval record pinning this unchanged protocol. Synthetic tests must cover compatible-subsequence filtering, exact tied-score conventions, fewer than three or zero candidates, absent Categories, unsupported truth, monotonicity, component marginalization, disagreement with hard-Category decomposition, fixed-class F1/confusions, empty strata, rank/loss identities, exact decision boundaries, historical reproduction, no oracle-to-predictor dataflow, strict aggregate schemas and monitor-I/O isolation. Run the existing full test suite. No MAP pilot is allowed before the protocol and tested implementation are locked and committed.

Use the existing CPU image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, UID/GID 10001, one numerical thread, network disabled, read-only root/project/data, and only new `artifacts/e017_attempt01` writable plus ephemeral scratch. Refuse an existing attempt directory. No GPU, paid service, external solver or new dependency is required. All scientific settings remain fixed after execution begins.

Expected execution time is **10–20 minutes for 100 historical reconstruction fits and diagnostic aggregation**, excluding implementation, tests and publication scans. E016 completed the same fit count plus shuffle reporting in about seven minutes; this is an estimate, not a new timing pilot or permission to change settings if slower.

Use the existing resilient terminal monitor only during execution: experiment ID, status, elapsed time, completed fits/scoring stages and latest completed metric. Metrics are unavailable before scoring; oracle metrics must include an ORACLE label and real metrics a REAL label. Progress units count work items, not estimated elapsed-time percentage. Periodic chat notifications are at most hourly while running, with completion/failure reported promptly. No idle monitor or scheduled wakeup is started for this review.

Publish only allowlisted aggregate JSON, complete tables, original code/tests, protocol and append-only documentation after verification and secret/data/local-path scans. Artifact schemas must separate `real_prediction` and `oracle_diagnostic` records and include the latter's supplied component. Never publish raw student text, answer strings, answer-key mappings, exact-label identities, row identifiers, individual ranks/predictions/probabilities, compatible label lists, vocabularies, coefficients, fitted models or donor mappings. Fixed six/two/three Category/component names and aggregate QuestionId results remain permitted.

Preserve the approved plan and verified results as separate descriptive commits only to the existing personal repository. This review draft does not authorize a run or publication of results. No historical predictive leaderboard or negative result will be replaced by an oracle score.

## Prior art and scope of contribution

The [Learning Agency's MAP description](https://the-learning-agency.com/datasets/misconceptions-preliminary/) distinguishes selected-answer correctness, explanation status and specific misconception identification, and discusses separating correctness evaluation from misconception detection. This decomposition is therefore not a new taxonomy or claimed novel algorithm. Its published evaluations use different conditions; their scores and suggested utility thresholds are not comparators or safety standards for this experiment.

E017's contribution is a reproducible information diagnostic under the project's unchanged question-shift framework, with train-only candidate inventories, honest real/oracle separation and complete negative-result reporting. Oracle information is assumed perfect and cost-free only for diagnosis. A later deployable system would have to obtain its signals independently, account for their errors and cost, and be tested under a new approved protocol and eventually independent questions.
