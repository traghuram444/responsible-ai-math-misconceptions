# E023: checker signals for error prediction and review prioritization

## Authorization and scope

Prepared 2026-11-20 after the user authorized both preregistration and execution: "okay proceed with the E023 preregistration. Keep E001–E022 and the folds unchanged, clearly separate review prioritization from automation criteria, and proceed running it". Lock and publicly commit this specification before any E023 real-data fitting, feature computation, calibration, selection or scoring. Complete synthetic tests, implementation lock and publication scans before execution. No further approval checkpoint is imposed by this document.

Preserve E001–E022, their protocols, code, results, locks, completed/failed attempts, README and frozen folds. E018 stays blocked. Add only E023 files and append-only experiment-log records. The baseline is commit `f2b130ddb4befe65d2d13a007ae956b205359177`. No model download, new checker call, external dataset acquisition, expert annotation, label change or experiment beyond E023 is included.

E022 reproduced L7 MAP@3 0.580689 and fixed C50 0.579796 versus frequency 0.539215, but neither learned arm met its separate 20% all-question cutoff-transfer criterion. L7 had no admissible development cutoff; C50 had two admissible folds and one jointly passing evaluation question. Empty policies do not demonstrate evaluation-risk failure. E023 asks whether observable checker signals add error-prediction information after the same basic reliability features are controlled.

This is a controlled extension of E009/E010 to the stronger E022 pipelines, not an invention of reliability learning, a causal explanation of errors or independent confirmation on fresh questions. The 15 questions have repeatedly informed design. All uncertainty and decisions are descriptive.

## Separate hypotheses and decision rules

**Review prioritization, primary R-L7 and R-C50, reported separately:** at the fixed 20% review budget, the eight-feature reliability estimator R8 reduces remaining exact-label errors by at least **2.0 per 100 original evaluation responses**, averaged equally over all five folds, relative to its matched five-feature estimator R5, with strictly positive benefit in at least four of five folds. Benefit = R5 remaining errors per100 minus R8 remaining errors per100. Both conditions are required, without rounding/tolerance. The 2.0/four-of-five criterion is carried from E010; only the prespecified ablation comparator changes. Neither model arm is selected as an overall winner. Report R8-versus-confidence, raw confidence, support-aware and hash-only controls even if R5 is weak. Passing the R8-versus-R5 criterion alone does not establish superiority to every simple control.

**Automation stress test, separate A-L7 and A-C50:** R8 must have an admissible development cutoff in all five folds and meet exact-label error <=20%, retained n>=100 and coverage>=10% on **every one of the 15 evaluation questions**. Apply/report the identical decision separately for R5 and the simple cutoff controls, with frequency context. These preserve E022's requirements. The 10%/30% targets are secondary and cannot rescue failure at20%. These research targets are not educational safety standards. No retained cases means zero coverage and undefined risk, never successful automation.

There is no combined study-success Boolean or trade-off between the R and A families. Better review prioritization does not reverse E022, certify automation or establish that human reviewers correct deferred cases. Primary review gains at another budget or in a selected question/stratum cannot replace R-L7/R-C50.

## Fixed data, roles and prediction pipelines

Use all36,696 original rows, 15 QuestionIds, exact `Category:Misconception` including literalNA, source ordering, seed20260831, and five outer folds0–4. Each fold remains nine training, three calibration and three evaluation questions. Split calibration using E007's original SHA-256 ordering and namespace into one temperature question and two cutoff questions; verify its historical role hash. No rotation, excluded question or split regeneration.

| Input | SHA-256 |
|---|---|
| Training CSV | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Split manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |
| E022 aggregate | `9578d9fc08c278751112fa1aadc52c0b1d6276e2a0b309d4ff54c455c2e6164f` |
| E022 prediction/development freeze | `f742b17fc43d553d5a8a6de95b79837ef58d1eab66db59d1f56df32072705964` |
| E022 lock | `0dd2d4706e797cdcbae5340aadc3b63a511018a4e573dacea6bbdcd6871152f2` |
| E020 G7 cache | `00830d9a7a64735682fce41655b55adf6c088105c339913eac4e604b4275bb13` |

Reuse the completed Qwen/Qwen2.5-Math-7B-Instruct revision `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d` cache and original provenance validators. Its soft scores s=(false,true,unknown) come from question/selected-answer pairs, not explanations or labels. They are model estimates, not independently verified mathematical correctness. No cache recalibration, prompt/parsing change, new LLM generation or checker fit is allowed.

Reconstruct unchanged E022 predictions. F is the training exact-label frequency. L is historical full-context tagged QuestionText/MC_Answer/StudentExplanation word TF-IDF/logistic. S(P,s) is unchanged E020 soft projection, including missing-prefix and exact-unknown behavior. L7=S(L,s); C50=0.5*S(F,s)+0.5*S(L,s). Raw distributions are mixed before temperature; no weight search. Candidate labels and support derive only from the applicable classifier fitting set.

Use E011's ordered grid ((1,1),min_df2,C0.5), ((1,2),2,1.0), ((1,2),5,2.0); three-fold GroupKFold with string QuestionIds, maximize equal-inner raw L MAP@3, first exact tie, then refit. Use unchanged vectorizer and logistic defaults, sublinear_tf=True, max_iter2000, no class weighting, seed20260831, n_jobs1. Any fitting warning is a technical failure. L is shared between the two arms; it is not retuned for R5/R8.

Final L7/C50 temperatures use E022's same single temperature question, supported-truth NLL, clipping1e-12, log-temperature bounds[-3,3], original optimizer defaults and T=1 zero-support fallback. F stays unscaled. Temperature cannot change top1/ordered-top3. Unsupported truths remain errors in router training, cutoff selection and evaluation. Only the historical temperature objective excludes them.

## Router training without question leakage

Reuse E009's exact `crossfit_blocks` function and `E009|fold={fold}|QuestionId={qid}|seed=20260831` namespace to divide each outer training role into three blocks of three questions. The historical helper's ordering is authoritative; record its role hash. No outer calibration or evaluation row enters router training.

For each held block, independently tune L with GroupKFold3 on the other six questions, refit those six, then produce raw F/L/L7/C50 predictions for the three held questions. Their labels may only define router correctness targets after predictions/features exist. The final nine-question model's selected settings are not reused inside cross-fitting. Fit vectorizers, frequency/support inventories and similarity references on the six fitting questions only. No cross-outer-fold pooling, in-sample errors or calibration-label borrowing.

Concatenate the three held blocks in original row order, exactly one record per training response. Fit separate R5/R8 models for L7 and C50; each arm's target is whether its own raw top1 prediction matches the existing exact label. The identical out-of-question examples, targets, weights and estimator settings are used for the R5/R8 ablation. Six-question cross-fit training versus nine-question deployment remains a documented distribution difference.

## Exact features and estimator

For each arm, let p be its raw L7 or C50 probability vector, K the training class count and yhat its original argmax. R5 uses E009's five numeric definitions in this fixed order:

1. max(p).
2. Largest minus second-largest p; second=0 when K=1.
3. -sum(p log p)/log(K), with zero terms0 and K=1 entropy0.
4. log1p(training count of yhat)/log1p(max training class count).
5. Maximum cosine similarity of the query's **full-context L TF-IDF** vector to all classifier-fitting vectors. Use chunks128, zero vector similarity0, clip roundoff to[0,1]. No neighbor label or identifier is a feature.

R8 appends exactly three signals, identical across arms for the same fitting model/query:

6. Checker/text disagreement: total variation `0.5*sum(abs(s-b))`, where b=(sum of raw **L** probabilities for classes starting `False_`, sum for `True_`,0). All candidate classes must have one of these prefixes; otherwise stop. This uses L before checker projection, not agreement of an already-projected model with its own checker.
7. Checker normalized entropy `-sum(s log s)/log(3)`, zero terms0.
8. Checker unknown mass s_unknown. This distinguishes concentrated unknown from confidently false/true; entropy alone cannot do so.

Validate all probability vectors, finite features and class alignment. No true recipient label, true-label support, QuestionId, source position, generated text, label identity, polynomial interaction or selected feature subset enters the router. Predicted-label support does not identify actual unsupported truths. No features are added/dropped after results.

R5/R8 each use StandardScaler with_mean=True,with_std=True followed by L2 LogisticRegression C=1.0,solver=lbfgs,fit_intercept=True,tol1e-4,max_iter2000,class_weight=None,seed20260831,n_jobs1. Weight each training question equally: row weight N/(9*N_q), applied to both scaler and logistic fit. No router tuning or post-hoc score calibration. If all correctness targets agree, use the E009 constant-correctness fallback and record it; no extra fits. Any convergence warning/nonfinite parameter stops execution. Score=predicted probability of being correct, higher means retain. These scores are not risk guarantees.

## Registered controls and routing families

For each learned arm use six review scores: R5, R8, confidence (maximum E022-calibrated probability), raw_confidence (maximum raw arm probability), support_aware (confidence multiplied by feature4), and hash_only (constant0). Frequency is a single contextual arm with its constant unscaled maximum probability. Thus there are13 arm/score combinations for review. Frequency has different label predictions and is not an isolated routing ablation. No R5/R8 model changes the underlying label predictions.

**Review budgets:** 0,10,20,30,40,50 percent. Within each outer fold, pool its three evaluation questions; review exactly floor(N*budget/100) rows. Reuse E010/E006 descending-score order and hash tie rule `fold={fold};source_row={row};seed=20260831`, then source position for a hash collision. No per-question quotas. Freeze all390 fold/arm/rule/budget masks before evaluation correctness. Batch composition may affect these decisions; this is a finite review queue, not a transferable cutoff. Human outcomes are not measured.

**Automation cutoffs:** use R5,R8,confidence,raw_confidence,support_aware for each learned arm, plus frequency:11 combinations. For each fold and target10/20/30, reuse E007/E022 exact distinct-score candidate search (0 plus every distinct unrounded float64 score), inclusive ties, and both development questions separately satisfying n>=100,10*n>=N,100*errors<=target*n. Maximize total retained development n; lowest cutoff breaks ties. Search all candidates; risk need not be monotone. No admissible cutoff means null threshold and defer all. Freeze all165 policies before evaluation feature routing; apply without batch quantiles, quotas, normalization or subgroup adjustment. Freeze all resulting masks before evaluation truth access. Hash-only has no automation arm.

The one temperature question is not used to fit routers or choose cutoffs; the two cutoff questions cannot fit routers, choose features or hyperparameters. Review budgets never select a threshold. No outcome from an early evaluation fold influences later preparation.

## Complete aggregate reporting

Publish separate `review` and `automation` sections, their separate decision tables and all empty cells. Every metric record has arm/rule/fold, either review budget or error target, scope (pooled fold or each of its3 questions), and the unchanged five strata: all, unsupported0, rare1–19, frequent>=20, well_supported>=20 across>=2 training questions (nested in frequent). True-label strata are applied after routing, only for reporting.

- Review:13 combinations*6 budgets*5 folds*4 scopes*5 strata = **7,800 records**.
- Automation:11 combinations*3 targets*5 folds*4 scopes*5 strata = **3,300 records**, plus165 development policies,33 all-question decisions and495 development-to-question risk-gap records.
- Unfiltered score separation:13 combinations*5 folds*4 scopes*5 strata = **1,300 records**. Report correctness AUROC under E009 eligibility n>=200,correct>=20,incorrect>=20, else null with all reasons. Report R8-minus-R5/confidence/raw_confidence/support_aware/hash_only paired fold AUROC differences, separately by arm and stratum. Frequency is context, not a same-correctness-target contrast.
- Reproduction: all600 E022 unfiltered raw/final records, all900 E022 confidence-cutoff records and45 policies must reproduce; these can be referenced by digest/count in the public integrity receipt instead of duplicated in full. All13 zero-review combinations reproduce their applicable E022 unfiltered final metrics. The registered final predictions and calibration never depend on the router.

Each review/automation group reports original/retained/correct/incorrect counts, coverage/review fraction, accuracy, MAP@3, risk, mean classifier confidence, confidence-minus-accuracy, 10-bin ECE and union-label multiclass Brier. Calibration requires n>=200,correct>=20,incorrect>=20; otherwise null with all failed reasons. Empty retained metrics are null. Unsupported truth remains an error and contributes to union-label Brier. Automation additionally reports error-minus-target, count/coverage/risk flags. Review additionally reports original errors, reviewed n/errors/correct, remaining and captured errors per100 original rows, error capture fraction and review error precision, with nulls for zero denominators.

For R5/R8 records also report separate binary reliability metrics: n/correct/incorrect, mean predicted correctness, binary Brier and ten-bin binary ECE using E009's same eligibility rule. Do not substitute router scores for multiclass probabilities. All metrics refer to their own retained population.

Aggregate every numeric pooled-fold metric with all five values, equal-fold mean, sample SD(ddof1) and defined-fold count. Include zero coverage in means; retain null risk and eligibility denominators. No row-level intervals, bootstrap, p-values, formal certificates, causal claims or new correlation/curve summaries. These folds overlap in training and are not independent replications.

Review paired comparisons: within each learned arm, R8 versus R5/confidence/raw_confidence/support_aware/hash_only at each nonzero budget and every stratum, reporting remaining-errors-per100, error capture, review precision and retained-risk differences, both error counts and achieved review fractions. Also show R8 versus frequency as explicitly different-classifier context. Automation paired comparisons: R8 versus R5/confidence/raw_confidence/support_aware/frequency at each target and stratum, reporting both retained counts/coverages and jointly defined risk/accuracy/MAP@3/ECE/Brier differences. These are not matched-population risk comparisons. All paired summaries retain the five fold values and defined counts.

Development records include final selection/temperatures/E007 role hashes, three inner block selections and row counts/anonymous block indices/E009 role hash per fold, and20 router metadata records (feature count5/8, fitting status, target counts and weight sum only). No coefficients, scalers, raw features, training-question mappings or row-level decisions are public.

## Outcomes and interpretation boundary

R8 passing review but failing automation means improved review prioritization under the registered criterion only. R8 beating R5 but losing confidence must be reported explicitly; it does not justify preferring R8 operationally. AUC improvement without the primary review margin is secondary. R5/R8 no-cutoff outcomes leave nonempty transfer unassessed for that fold. A nonempty held question exceeding target is a risk-transfer failure; insufficient retention is a separate usefulness failure. Report coexisting failures and all questions, not a favorable subset.

If R8 does not improve on R5, the result concerns these three signals and this fixed learner. It does not prove mathematical verification or reliability learning impossible. Checker information is already present in L7/C50; additional signals can be redundant. Positive results do not establish correct mathematical reasoning, human-review benefit or generalization outside this repeatedly used middle-school sample.

There are no exploratory analyses in E023. Alternative features, models, thresholds, budgets, seeds, calibrations, shuffled signals, oracle routing or further data require a later proposal. Primary review and automation results are both published even if negative. Present numerical aggregate/fold/question results before interpretation; no E024 is authorized.

## Reproducibility, gates and execution

Use pinned image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, Python3.11.11, NumPy1.26.4, sklearn1.5.2, UID/GID10001, seed20260831, single numerical threads, networknone, read-only root/project/data/history, dropped capabilities and no-new-privileges. Only new exclusive `artifacts/e023_attempt01` is writable; tmpfs scratch. All inputs/old locks remain read-only. Private predictions, scores and masks may be exclusively serialized inside the ignored attempt for hashed global-freeze verification; never publish them or raw responses.

Exactly200 classifier fits: per fold30 inner cross-fit fits plus10 final reconstruction fits, shared between both arms. Up to20 tiny router fits (constant fallbacks recorded). Zero new LLM calls. Estimate25–60 minutes compute, with similarity/reporting costs uncertain; implementation/tests/integrity/publication scans are additional. No real-data timing pilot. The terminal viewer reports actual phase, elapsed time, fits/200, router preparations/20 and policies/165; scored metrics only after global freeze and historical reproduction. At-most-hourly routine updates during long execution, plus completion/failure/intervention; no idle monitor.

Before execution test nested fitting isolation, features/unknown/disagreement, exact estimator weighting, boundary/tie arithmetic, label-blind routing, freeze barriers, inherited predictions/temperatures/policies, full grids/nulls and strict aggregate schema. Lock all new scientific code/tests/publisher and append-only record prefixes; capture E022 private inventory and all current historical public files, with nested earlier preservation gates. Commit/push preparation only to the authorized personal repository before launching.

Before scoring reproduce E022 raw/final probabilities, classes/source/question alignment, selected parameters, temperatures and confidence policies; verify data/fold/cache/freeze hashes. Globally freeze all folds' router descriptions,165 policies,390 review masks and165 automation masks before evaluation labels. After freeze reproduce all registered E022 metric records, then score E023. On any mismatch, required gate failure, warning, invalid/nonfinite value or stopped execution, preserve a technical failure and stop; no automatic retry or scientific-setting change.

On completion verify no failure receipts, locks, private freeze/completion/aggregate hashes, strict allowlists and independent count/metric/grid checks. Frozen publisher runs once. Run full tests and publication/secret/local-path/private-response scans. Append execution/outcome logs without rewriting historical prefixes, commit/push only sanitized aggregate results and documentation, verify public commit and file hashes. Keep README unchanged.

## Literature and novelty boundary

[Kamath, Jia and Liang (ACL2020)](https://aclanthology.org/2020.acl-main.503/) study learned correctness calibration under domain shift. [Varshney, Mishra and Baral (FindingsACL2022)](https://aclanthology.org/2022.findings-acl.158/) show that selective methods do not consistently outperform maximum probability across their tested settings. These official records were checked2026-11-20. Neither establishes benefit on MAP. E009/E010 supply this project's existing error-learning and review-budget designs; E023's contribution is the preregistered incremental checker-signal ablation with stronger fixed predictions and separate negative/positive review and automation outcomes. Independent new questions remain necessary for external confirmation.
