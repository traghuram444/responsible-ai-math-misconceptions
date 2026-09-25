# E007 proposal: transfer of fixed abstention thresholds to unseen questions

**Status: DRAFT FOR USER REVIEW — NOT APPROVED, NOT IMPLEMENTED, NOT RUN.**

Prepared 2026-09-25 after discussion of E006. This document is the proposed scientific specification, not an execution authorization. E001–E006, their protocols, source, folds, and results remain unchanged. A reviewed protocol and matching implementation must be locked and committed before any E007 MAP analysis. Any changes during review must precede execution and remain visible in version history.

## 1. Question, motivation, and hypotheses

Can an abstention cutoff selected on development questions retain a useful fraction of predictions on different, unseen questions while meeting a prespecified empirical exact-label error target?

E006 ranked each unlabeled evaluation batch to meet fixed review budgets. That is a valid batch-allocation experiment, but does not test transfer of a previously selected cutoff. Its question-plus-explanation/support-aware result at 50% review had mean exact accuracy 0.458105, risk 0.541895, and MAP@3 0.571026. ECE increased from 0.108524 at full coverage to 0.145861; corrected Brier decreased from 0.805728 to 0.775702. These metrics measure different properties. Relative routing success is not reliable automation. See the preserved [E006 tables](E006_RESULTS.md).

Selective classification under distribution shift is established research, not a new method introduced here. Holding the classifier fixed permits examination of the selection policy separately. This experiment contributes a MAP-specific, reproducible threshold-transfer diagnostic, not a general risk guarantee. [Liang, Peng, and Sun, TMLR 2024](https://arxiv.org/abs/2405.05160)

The fixed diagnostic hypotheses are:

- **H1, primary:** for each input-arm/routing-rule pair separately, a development-selected cutoff targeting at most 20% exact-label error transfers with at least 10% coverage, at least 100 retained responses, and error at most 20% on every outer evaluation question.
- **H2, secondary:** the same transfer criterion at the separately registered 10% and 30% error targets characterizes the reliability/coverage trade-off. Neither secondary target replaces H1 if H1 fails.
- **H3, secondary descriptive comparison:** predicted-label support weighting changes achieved coverage, error, and unsupported-case retention relative to confidence-only selection. There is no assumed benefit and no additional success threshold for this comparison.

The error targets are research stress-test levels, **not educational safety standards**. The coverage and count floors prevent one or two easy examples, or abstention on everything, from being called useful transfer. They are design choices fixed before E007 results, not quantities estimated from E007 outcomes.

## 2. Frozen framework and the explicit calibration change

Preserve the existing five outer QuestionId folds, seed 20260831, exact `Category:Misconception` target, and original input arms: explanation-only and question-plus-explanation. Do not add MC_Answer, new labels, question rubrics, encoders, classifiers, or correctness routers.

Each outer fold retains its existing nine training questions, three calibration questions, and three evaluation questions. **Only the existing calibration role is subdivided for E007**:

| Role | Questions per fold | Permitted use |
|---|---:|---|
| Original training | 9 | TF–IDF fitting, inner grouped tuning, final LR fit, frequency probabilities, and support counts |
| Temperature fitting | 1 of the original calibration questions | Fit the scalar temperature only |
| Threshold selection | Remaining 2 calibration questions | Select cutoffs using scores and correctness; no fitting of temperature or classifier |
| Original evaluation | 3 | Apply frozen cutoffs, then compute results |

Assign the three calibration questions without inspecting responses, labels, support, or performance. Canonicalize each QuestionId as its unsigned base-10 integer string without leading zeros; reject nonintegral or negative values. Sort ascending by the SHA-256 hexadecimal digest of UTF-8 `E007|fold={fold}|QuestionId={qid}|seed=20260831`, with no newline; break digest ties by ascending numeric QuestionId. The first is the temperature-fitting question and the remaining two are the threshold-selection questions. Fold IDs are 0–4. Record a hash of this derived question-role assignment locally and sanitized role counts publicly. Do not rotate or choose a favorable role allocation.

This **changes the temperature-fitting sample relative to E006**, which used all three calibration questions. It does not alter any frozen outer assignment. E007 is therefore not an exact replication of E006's calibrated scores. That distinction must appear in the report and README. One temperature question and two threshold questions provide weak development evidence; all findings remain descriptive.

Use unchanged E001 training code: three-fold GroupKFold within the nine training questions; select maximum mean inner MAP@3 from `(unigrams, min_df=2, C=0.5)`, `(unigrams+bigrams, min_df=2, C=1)`, and `(unigrams+bigrams, min_df=5, C=2)`, retaining the existing grid-order tie rule. TF–IDF uses sublinear term frequency; LR uses max_iter=2000, no class weights, seed 20260831, and n_jobs=1. Refit on the nine training questions only.

Temperature fitting reuses E001's clipped-log-probability objective, bounded log-temperature interval [-3, 3], and exclusion of calibration truths absent from training. Report the number and fraction used. If none are supported, preserve its deterministic T=1 fallback and flag it; do not borrow threshold-selection labels. Nonfinite probabilities/temperature are execution errors that stop the run. Crucially, **threshold selection and evaluation include unsupported truths as errors**: their exclusion from temperature fitting does not remove them from the risk calculation.

The frequency baseline uses training prevalence without temperature scaling. The training-label vocabulary and support counts never use either calibration subset or evaluation data.

## 3. Prediction-time scores and exact cutoff algorithm

Evaluate both existing learned rules for both input arms:

1. Confidence: maximum temperature-scaled class probability.
2. Support-aware: that maximum multiplied by `log1p(training_count_of_predicted_label) / max(log1p(training_class_counts))`.

The second score is not a probability or an unsupported-label detector. True-label support is unavailable to the routing policy. Keep historical class-order prediction and top-three tie handling unchanged.

For each fold, arm, rule, and target risk r in **[0.10, 0.20, 0.30]**, use the following procedure:

1. Form candidate thresholds from 0 and every distinct score observed on the two threshold-selection questions. Use unrounded float64 values, sorted ascending, with no binning or extra grid.
2. For a candidate t, retain every response with score >= t. Include all score ties; never use row identifiers to select a fraction of a tie group.
3. A candidate is admissible only if **each of the two selection questions** has retained count >=100, retained fraction >=0.10, and observed top-1 error <=r. Thus at least 200 selection responses must be retained overall. Compute risk from exact integer errors/counts; compare targets as rational fractions 1/10, 1/5, and 3/10 without rounding or a floating tolerance.
4. Among admissible candidates, choose the one retaining the largest total number of selection responses. Break ties by the lowest numeric threshold. Search all candidates; empirical selective risk need not be monotone in the threshold.
5. If none is admissible, set policy status `NO_ADMISSIBLE_THRESHOLD` and defer all evaluation responses. Serialize threshold as null with this status, not a JSON infinity. Report zero coverage and null accuracy/risk, **never zero risk**.
6. Freeze all selected cutoffs for all folds before examining E007 evaluation outcomes. Apply the same cutoff unchanged to each response on all three corresponding evaluation questions. No test-batch ranking, score-quantile adjustment, threshold clipping, target substitution, or forced review quota is allowed.

Apply this identical cutoff-selection algorithm to the frequency baseline's maximum training probability. Its constant score means it can retain all or none: this is an intentional negative control, not grounds to give it a different policy. Publish its unfiltered reference as well. E006's same-budget frequency results remain historical context, not an equal-coverage E007 comparator. Comparisons at a common target may have different achieved coverage and must show that difference.

Threshold-selection error is an optimized development statistic, not an unbiased validation estimate. Separating its questions from temperature fitting removes that particular reuse, but does not make the empirical threshold search a formal risk-control method.

## 4. Fixed outputs and metrics

For each arm/rule/target, retain all five fold entries and all 15 evaluation-question entries. Publish only aggregates. Record selection status, cutoff, temperature, development counts/coverage/error for each of its two questions (anonymous within-fold role indices), and actual evaluation counts/metrics. Evaluation questions may use existing public QuestionId aggregate identifiers; never publish student or source-row identifiers.

Primary outputs at r=0.20 are actual coverage, retained top-1 error, signed error minus target, target exceedance, retained count, and the criterion in section 5. Report every evaluation question, including zero-coverage cases. An observed error exceeding target is reported even if fewer than 100 predictions remain; the count floor concerns useful-transfer evidence, not whether an observed error is displayed.

For all three targets, report the following secondary quantities, plus an unfiltered reference under the E007 temperature:

- Top-1 accuracy, MAP@3, risk, retained fraction, and actual review fraction.
- Retained mean maximum probability and ten-equal-width-bin ECE, using original calibrated probabilities, never the support-weighted score as a probability.
- Union-label-corrected multiclass Brier; do not substitute the legacy Brier field.
- Original/retained counts, retention fractions, share of retained cases, accuracy, MAP@3, and risk within the unchanged support strata: unsupported (0 training instances), rare (1–19), frequent (>=20), and nested well-supported (>=20 over >=2 training QuestionIds).
- Fold-level paired confidence/support-aware differences in coverage and risk, and learned/frequency differences at the same target, always accompanied by both coverage values. Risk comparisons are conditional on different retained populations, not paired response-level treatment effects.

Select globally with the cutoff before intersecting true-label strata. Never choose stratum-specific cutoffs. Report empty rare strata explicitly. ECE and Brier at each fold/question/stratum require n>=200, >=20 correct, and >=20 incorrect retained predictions, as in E006. Otherwise they are null with the failed eligibility conditions recorded. This can exclude highly accurate small subsets as well as the unsupported stratum; null calibration is not evidence of good calibration. Mean confidence only requires a nonempty group.

For nonempty evaluation questions, report evaluation risk minus the equal-question mean risk on that policy's two threshold-selection questions. These development-to-evaluation gaps are descriptive and potentially optimistic because thresholds were selected on development correctness.

## 5. Fixed interpretation rules

Make a separate decision for each of the four learned arm/rule pairs at each target, and for the frequency reference. Do not select a winning arm/rule/target after inspection.

At a given target, an arm/rule demonstrates **useful empirical transfer on this benchmark** only if all five folds have an admissible development threshold and **all 15 evaluation questions** satisfy all three conditions: retained n>=100, coverage>=0.10, and observed error<=target. Check unrounded counts/ratios; no rounding-based passes. Report the number out of 15 meeting each condition separately. The 20% decision is primary; 10%/30% decisions are secondary.

| Outcome | Permitted interpretation |
|---|---|
| No admissible development threshold in one or more folds | No useful policy found under the registered development requirements; transfer cannot be assessed for those folds. This is not proof no reliable subset exists under other methods. |
| Threshold exists, but held-out coverage/count floors fail | The policy did not provide the registered useful coverage on new questions. Zero retained predictions is not a successful risk result. |
| Threshold exists, but any held-out question exceeds the error target | The policy failed the registered benchmark-wide risk-transfer criterion. Report its magnitude and count, not only its average. |
| All 15 questions meet risk and coverage/count requirements | Descriptive success on this benchmark; not a risk certificate, evidence of human benefit, or deployment authorization. |
| Coverage and risk failures coexist | Report both; do not force a single favorable explanation. |

Even uniformly negative results do not causally distinguish weak representation, label semantics, calibration-sample limitations, and distribution shift. Differences in these observed failure patterns guide subsequent hypotheses; they do not identify a sole cause.

## 6. Aggregation, uncertainty, and analysis boundary

Within a fold, all-case metrics pool its three evaluation questions, matching the earlier fold reporting convention. Report each fold and equal-fold mean/sample SD (ddof=1), plus all question values and maximum observed question risk. Coverage/count summaries include all five folds, including deferral-only folds. Risk, accuracy, MAP@3, and calibration means include only defined/eligible folds with the denominator prominently shown; an average over fewer than five is explicitly conditional and cannot establish useful transfer. SD is null with fewer than two defined folds. Paired summaries use the eligible-fold intersection and show its count. No imputation of empty risks.

Report the number of development-admissible folds, nonempty evaluation questions, count/coverage-eligible questions, and risk-target exceedances with their denominators. There are only 15 questions and overlapping training folds. Do not use response-level confidence intervals, formal significance tests, independence claims, or deployment guarantees. No bootstrap or permutation analysis is proposed for E007.

H1 and its predetermined all-question decision are the confirmatory-style diagnostic. H2, H3, calibration, support strata, and development-to-evaluation gaps are prespecified secondary/descriptive analyses. None is independent confirmation: E001–E006 and this proposal repeatedly use the same 15-question benchmark. There are no exploratory data analyses in this run. New scores, additional risk targets, role rotations, models, subsets, qualitative response examples, and post-hoc threshold searches require a separately reviewed proposal.

## 7. Execution, integrity, and publication plan — after approval only

- Verify the same training CSV, frozen manifest, assignment CSV, and E001 reference hashes recorded in the [E006 addendum](E006_REVIEW_ADDENDUM.md). Never regenerate files to fix a mismatch. Hash preserved E001–E006 records before and after execution.
- Reconstruct predictions in memory: published artifacts do not contain reusable row probabilities. Use the existing classifier fitting code and confirm its selected hyperparameters and unfiltered top-1/MAP@3 against the historical reference, absolute tolerance 1e-10 and relative tolerance zero. Positive temperature scaling should preserve those rankings. ECE/Brier reproduction is deliberately not a gate because temperature-fitting data changed. A mismatch stops the run; it does not authorize retuning.
- Before real-data execution, test deterministic question-role assignment, role disjointness, supported-only temperature fitting, inclusion of unsupported errors in threshold search, score ties, nonmonotone-risk search, rational target comparisons, frequency all-or-none behavior, empty policies, eligibility/null handling, fold summaries, strict aggregate export, and unchanged cutoff application. Synthetic tests must show that changing evaluation labels or batch composition cannot change the selected cutoff or an individual response's retain/defer decision.
- Approve and hash-lock this protocol; translate it into matching configuration; commit the tested implementation before execution. Do not infer approval from resuming the project. No E007 runner/configuration is authorized by this draft alone.
- Use the audited non-root Docker environment, no network, read-only project/data, and a new writable `artifacts/e007/` mount. No package installations, model downloads, host configuration changes, or unrelated project edits. If the audited image is unavailable, stop rather than silently substitute an environment.
- Reuse the live terminal monitor only during an active approved run, with at-most-hourly progress notifications and immediate completion/failure reporting. No idle monitoring. Implementation may report real fitting/threshold-search stages; do not invent percentage progress from elapsed time.
- Anticipate approximately 100 classifier fitting calls, as in E006. Its roughly nine-minute run is the only local timing anchor. A provisional **10–20 minute compute estimate** excludes implementation/tests and is not guaranteed; threshold-search cost and current resources may increase it. Report measured runtime. This drafting session performs no timing run or MAP analysis.
- Serialize aggregate outcomes, thresholds, counts, hashes, configuration, environment identity, seed, Git revision, and run status. Never serialize student text, source-row IDs, row probabilities/predictions/rankings, fitted weights, or caches. Publish through a strict allowlist after privacy/secret/path scans and verification. Preserve failure records and prevent silent reruns/overwrites.
- Present aggregate and all fold/question result tables first, before interpretation or any subsequent experiment proposal. Preserve E001–E006 unchanged. Any E007 result gets its own descriptive sanitized commit after verification, regardless of success.

## Review checkpoint

The choices requiring review are the **one-question temperature / two-question threshold** subdivision, **20% primary and 10%/30% secondary error targets**, **100 retained responses and 10% coverage per question**, and **all-15-question success criterion**. These are new E007 design choices, not retroactive changes to E006. No E007 result is known or claimed.
