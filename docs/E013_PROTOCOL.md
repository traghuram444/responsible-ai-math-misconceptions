# E013 response evidence under question held out evaluation

## Review status and scope

Prepared 2026-10-14 for user review. **Protocol preparation is authorized; execution is not.** This is the proposed preregistration, not a completed experiment or execution approval. Numerical choices below are proposed for approval before implementation and any E013 computation on MAP data.

E013 asks whether the unchanged E011 and E012 full-context models use student-response information that transfers to held-out questions, beyond question context and common-label rankings. It is a diagnostic experiment, not a new classifier, calibration repair, or attempt to improve MAP@3. Preserve E001–E012, both E012 attempts, their protocols/code/results/locks, and all frozen assignments. The reference revision is `59aeaa1b556033b176fc039bbc88d2f0a9a17c6c`.

This design was motivated by already observed E001–E012 outcomes. Its new comparisons are prespecified prospectively, but the repeatedly examined 15-question benchmark is not an independent confirmatory sample. No statistical significance, deployment safety, or novel architecture claim follows from this experiment.

## Research questions and hypotheses

1. **Explanation evidence:** within an unseen question and the same selected answer, does supplying the recipient student's own explanation improve exact-label ranking over a randomly assigned explanation from that cell?
2. **Total response evidence:** within an unseen question, does the recipient's own answer–explanation pair improve ranking over a randomly assigned intact pair from that question?
3. **Frequency comparison:** where do learned rankings improve on frequency, where do they harm it, and how often do predictions agree? Similar aggregate scores alone do not establish identical predictions.
4. **Probability scale:** how do raw and historically calibrated probabilities differ in confidence and calibration, and is the registered temperature boundary binding? This audit does not change calibration settings.

There are two separately adjudicated co-primary hypotheses, one for E011 full-context logistic regression and one for E012 full-context ComplementNB: the original explanation provides a practically meaningful MAP@3 advantage over within-question-and-answer shuffled explanations. Both are reported, including disagreement; neither may be selected as the sole headline after inspection. The paired-response intervention, frequency comparisons, support analyses, and accuracy are prespecified secondary analyses. The probability-scale audit is exploratory.

## Unchanged models and frozen evaluation

Use exactly the inputs, grids, selection rules, defaults, and calibration in [E011](E011_PROTOCOL.md) and [E012](E012_PROTOCOL.md). Reconstruct only their full-context arms, using the original scientific functions without modifying them. Historical fitted models were not serialized; reconstruction is necessary, not permission to choose new settings.

- Five original outer QuestionId folds; each has nine training, three calibration, and three evaluation questions. Training seed remains `20260831`.
- Original three-setting word TF–IDF/logistic grid and six-setting character TF–IDF/ComplementNB grid; GroupKFold(3) selection entirely inside the nine training questions; equal-inner-fold MAP@3; first grid entry on an exact tie.
- Refit each selected setting on its nine training questions: 50 logistic fits plus 95 ComplementNB fits, **145 fits total**. No extra fit for an intervention.
- Original temperature fit on supported calibration truths only, bounded log-temperature `[-3, 3]`, clipping probabilities at `1e-12`. Apply the same fitted temperature to original and perturbed predictions. Frequency remains unscaled training-label prevalence.
- Exact full-context input and missing-to-empty string conversion remain unchanged. Labels, correctness flags, row IDs, and QuestionId are not predictive features. QuestionId is used only for frozen roles and diagnostic grouping.

The existing data contract remains:

| Input | SHA-256 |
|---|---|
| Training data | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |

Validate hashes, source order, target alignment, role disjointness, and exactly one outer evaluation assignment per response before reconstruction and after evaluation. Never regenerate assignments to pass a check.

## Three fixed evaluation conditions

The evaluation target always remains the **recipient's original exact Category:Misconception label**. Training and calibration inputs are never shuffled. No labels or support strata determine donor assignments.

| Condition | Donor assignment | Preserved information |
|---|---|---|
| `original` | Recipient retains own response | All original fields |
| `explanation_shuffle` | Permute explanations within each `(QuestionId, MC_Answer)` cell | Recipient question and selected answer |
| `pair_shuffle` | Permute intact `(MC_Answer, StudentExplanation)` pairs within each QuestionId | Recipient question; donor answer–explanation consistency |

Use the exact selected-answer string after the existing missing-to-empty conversion, without trimming, case folding, or semantic grouping. Converted QuestionText must be identical within each QuestionId; otherwise stop before evaluation and request an amendment rather than silently changing grouping.

Each intervention has **100 independent permutation replicates** per fold. Use NumPy `Generator(PCG64(SeedSequence([20261014, condition_id, fold, replicate, cell_index])))`, where explanation shuffle is condition 1, pair shuffle is condition 2, fold is 0–4, and replicate is 0–99. Sort cells by numeric QuestionId and, for explanation shuffle, Python Unicode ordering of the converted answer. Number cells from zero within each fold/condition. Sort members by original source position, then call the generator's `permutation` once on that position array. Recipient positions map to returned donor positions in that order.

Use the same mappings for both models and frequency. Sampling is without replacement within each cell and replicate. Allow ordinary permutation fixed points; do not redraw to force movement. Singleton cells remain unchanged. Duplicate text is retained. Do not remove cells for label homogeneity, identical explanations, low movement, or unfavorable results.

Each shuffled input is exactly another observed input in the same question, so its predictions can be obtained by indexing the corresponding donor's original probability row. For explanation shuffle, identical selected answers also guarantee this equivalence. Verify these identities with synthetic tests; do not approximate them. No retraining or vocabulary fitting occurs. Prediction vectors and donor mappings remain in memory, not on disk.

For each condition, fold, and question, report row counts, cell counts, singleton-row counts, rows in cells of size at least two, and replicate mean/SD of donor-position changes and actual input-string changes. After the evaluation barrier, report the number/share of rows in label-mixed cells as a descriptive opportunity check only. Do not publish cell identifiers, answer strings, or label-by-answer tables. Limited within-cell variation limits what a null effect establishes.

## Freeze barrier and reproduction gates

Prepare all ten fitted models, selected settings, temperatures, original raw/scaled probabilities, and both conditions' mappings for all folds before computing any E013 held-out metric. The permutation constructor receives question/answer metadata and source positions, never targets. Save an aggregate-only development receipt with settings, fit counts, seed specification, hashes, and completion status; seal in-memory prediction/mapping arrays against mutation.

Only after this global barrier may the scoring layer access evaluation truths. First reproduce the published E011/E012 original full-context and frequency records: development selections and supported calibration counts must match; numerical settings/temperatures and all available original fold/question/support metrics must match their respective artifacts with absolute tolerance `1e-10`, relative tolerance zero, and identical null patterns/counts. Reference artifacts are hash-pinned before execution. A mismatch blocks new E013 summaries and stops the attempt. Never patch a discrepancy using held-out scores.

Frequency predictions are constant within each fold. Its original and shuffled scores must agree to the same tolerance for every replicate and reporting stratum. Failure is an implementation error, not a scientific finding.

## Co-primary estimands and decision rules

Use the unchanged exact-label MAP@3 implementation, class order, and tie handling. An unsupported recipient truth contributes zero. For model `m` and fold `f`, define:

`D[m,f] = MAP3(original[m,f]) - mean_r MAP3(explanation_shuffle[m,f,r])`.

The primary estimate is the **unweighted mean of the five fold differences**. A model meets its explanation-evidence criterion only if the unrounded mean is at least **0.020** and its difference is strictly positive in at least **4/5 folds**. This proposed two-point margin measures useful explanation dependence under this intervention; it is not E012's baseline-improvement criterion or a safety standard.

Report each model's Boolean separately. Call the finding concordant across both models only if both meet the rule. Neither meeting it means neither demonstrates the registered magnitude/consistency of explanation evidence, not statistical equivalence or absence of information. Smaller positive effects are reported as below the registered meaningful margin. Negative differences mean shuffled assignment performs better under this diagnostic, not that explanations should be discarded in practice.

No support-restricted, question-selected, accuracy, or calibration finding replaces either all-row primary result. No success decision is based on outperforming frequency in this experiment.

## Prespecified secondary summaries

For both models, frequency, every condition, all five folds, all 15 questions, and every existing support stratum, report exact-label MAP@3 and top-1 accuracy. Summarize shuffled conditions over 100 replicates and report original-minus-shuffled deltas. Report pair-shuffle effects in the same units without an additional pass/fail threshold. Original scores are computed once, not treated as 100 independent observations.

Support is determined from the recipient's true label and the outer training set, never the donor's label:

- unsupported: zero training examples;
- rare: 1–19 training examples;
- frequent: at least 20 training examples;
- well-supported: at least 20 examples spanning at least two training questions;
- all: all recipients.

Well-supported is nested within frequent, not a disjoint fifth group. Membership is fixed across conditions and replicates. Empty groups remain null with counts; no search for a populated rare threshold. Shuffle across full registered cells first, then score recipient strata; never shuffle within outcome-defined strata.

For **original predictions only**, report model-versus-frequency top-1 agreement and exact ordered-top-three agreement. Also report paired win/tie/loss counts for per-row reciprocal-rank-at-three scores, mean gain contribution `mean(max(model_score - frequency_score, 0))`, mean loss contribution `mean(max(frequency_score - model_score, 0))`, and their difference. Report analogous accuracy win/tie/loss counts. Use the same fold/question/support grid, without exposing labels or individual predictions. Gain minus loss must reproduce the MAP@3 delta.

## Exploratory probability and calibration audit

This prespecified exploratory audit does not select a calibration method, probability transformation, temperature bound, or confidence cutoff. Use **original inputs only**. Compare each model's raw `predict_proba` with the unchanged temperature-scaled probabilities; frequency supplies one unchanged reference.

For every fold, question, and support stratum report counts, accuracy, mean maximum probability, signed confidence-minus-accuracy gap, 10-equal-width-bin ECE, and corrected union-label Brier. Preserve historical eligibility for ECE/Brier: `n >= 200`, at least 20 correct and at least 20 incorrect predictions in that condition/group. Otherwise report null and reasons, not zero. Paired raw-minus-scaled ECE/Brier summaries use only groups eligible in both; report the eligible-fold denominator. Do not silently average over missing groups.

Record each temperature and supported calibration count; flag proximity to either log-temperature bound when absolute distance is at most `1e-5`. Report aggregate fractions of raw probability entries at or below `1e-12`, raw-to-scaled top-1 changes, and ordered-top-three changes, exposing clipping/tie effects. No coefficients, individual scores, or class-specific vectors are published. Boundary contact describes the constrained fit, not its underlying cause. Calibration does not ordinarily change label rankings; no revised E012 result is issued.

## Descriptive uncertainty and reporting order

For each primary comparison publish all five `D` values, equal-fold mean, sample SD (`ddof=1`), and positive-fold count. Secondary comparisons use the same fold convention with defined-fold counts for null strata. For each shuffled score/delta publish replicate mean, sample SD, and empirical 2.5th/97.5th percentiles using NumPy's linear percentile method. Across-fold replicate summaries use replicate `r` jointly across all five folds before computing percentiles; never treat 500 fold-replicate values as independent observations.

Permutation dispersion measures variation in diagnostic assignments, **not** a confidence interval for future-question generalization. It is not a randomization test or p-value. No bootstrap, inferential/equivalence test, or post-hoc adjustment is added. Folds overlap in training data and cover only 15 already examined questions. Per-question heterogeneity and limited power remain explicit.

Show complete aggregate and fold-level tables first, then per-question/support summaries and calibration diagnostics, before interpretation. Publish all preregistered outcomes, including negative effects and null/ineligible groups. Additional analyses require a separately labeled later proposal and cannot alter E013's primary judgment.

## Interpretation fixed before execution

| Observed pattern | Permitted conclusion | Not established |
|---|---|---|
| Explanation criterion met, original model still below frequency | Useful response-specific ranking information coexists with net losses elsewhere | A deployable model or a particular remedy |
| Pair-shuffle drop positive, explanation criterion unmet | Evidence may depend more on answer choice or the joint pair than within-answer distinctions | No explanation signal; low cell variation can limit this test |
| Original MAP@3 does not exceed either shuffled mean | No positive mean response-specific benefit under these perturbations for that model | Equivalence, absence of mathematical information, or failure of all future models |
| Similar original and frequency scores, different predictions | Aggregate parity hides offsetting wins and losses | Identical behavior |
| High prediction agreement with frequency | Common rankings account for much observed behavior | Proof the learned algorithm explicitly uses the frequency baseline |
| Temperature boundary and poor calibration | The registered probability pipeline warrants a separate investigation | Permission to repair E012 or tune on E013 evaluation labels |
| Models disagree | Representation/classifier-dependent behavior on this benchmark | A universal claim about explanations |

The interventions break response-to-target alignment while preserving registered context; they are not causal manipulations of student understanding. Equal labels within cells, duplicate explanations, and shared reasoning can attenuate effects. Nothing here supplies expert annotations, diagnoses a child's cognition, or establishes safe automation.

## Execution and publication after approval

After approval, implement E013 in new files and test with synthetic data. Tests must cover deterministic label-blind mappings, fold/cell boundaries, singleton/duplicate/missing strings, donor-row prediction equivalence, recipient target/stratum preservation, frequency invariance, gain/loss arithmetic, null eligibility, reproduction failures, the global evaluation barrier, strict aggregate schemas, and monitor failure isolation. Commit/hash-lock the approved protocol and tested implementation before fitting. A scientific change requires an amendment and renewed approval before computation.

Use pinned CPU image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, UID/GID 10001, one numerical thread, no network, read-only project/data/root, and only a new `artifacts/e013_attempt01` directory writable, with ephemeral scratch as required. Refuse a pre-existing attempt directory. Pin prior public scientific files and both prior execution locks; verify private failed/completed attempt evidence read-only. Do not substitute an unavailable image without a reviewed environment amendment.

Expected compute is **approximately 15–45 minutes**, based on previous fit timings and 145 reconstruction fits plus aggregate scoring; this is an estimate, not an E013 pilot. Implementation, testing, privacy checks, and publication are additional. No GPU, downloads, external API, transformer, random-split rerun, new labels, or new dataset are required.

Use the resilient monitor: experiment ID, status, elapsed time, fit/permutation-scoring progress, stage, and latest completed metric. Before the evaluation barrier, metrics are unavailable, never invented or stale prior-experiment values. Monitor I/O failures cannot alter computations; scientific/integrity failures remain fatal. Terminal refreshes are local; periodic chat notifications are at most hourly while active, with completion/failure reported promptly. No monitor or scheduled wakeup is started for protocol-only review.

Publish only allowlisted aggregate JSON, tables, protocol/code/tests, and append-only experiment-log updates after privacy/secret/local-path checks. Never serialize responses, selected answers, donor mappings, row IDs, row probabilities/predictions, models, vocabularies, or per-cell answer summaries. Preserve failed attempts; operational failure stops for review, is not a negative scientific result, and does not trigger another model. Stop after E013 reporting. No E014 is authorized.
