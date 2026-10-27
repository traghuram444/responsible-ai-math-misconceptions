# E021: correctness-conditioned fusion under question shift

## Review status, scope and provenance

Prepared 2026-10-27 against `bb7a4ec12eda409b248c187dbc1f3bad27f18a1b`. **Exact proposed preregistration for user review; execution is NOT approved.** Only this document and an append-only experiment-log entry are authorized now. No E021 implementation, data analysis, permutation construction, fitting, calibration, scoring, attempt directory or monitor is started at review time.

Preserve E001–E020, their protocols, implementations, results, locks, successful/failed attempts and recovery evidence, all frozen assignments and README unchanged. E018 remains blocked. After approval, E021 uses new files and an exclusive new attempt; old source functions are imported read-only, never edited to implement E021. E020 remains a primary negative result for H under its own registered rule, alongside its positive secondary comparisons.

Research question: **Does applying the same mathematical correctness signal to both predictors improve held-question exact-label ranking relative to mixing conditioned and unconditioned predictions, and does a training-selected conditioned ensemble add value over both of its components?**

E020 reported F 0.539215, G7 0.565704, L7 0.580689 and H 0.557104 equal-fold MAP@3. H mixed F, unconditioned L and G7; it could not select L7. E021 is motivated by these observed outcomes. Its comparisons are prospectively specified, but the repeatedly examined 15-question benchmark is not a fresh confirmatory sample. "Primary" and "secondary" identify design priority, not formal inferential validity. No new architecture, causal effect of model size, independent replication or safe-automation claim is implied.

| Existing input/evidence | SHA-256 |
|---|---|
| Training CSV | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen split manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen fold assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |
| E020 aggregate JSON | `8a5fcfd894c4dd6b24607b330376ba4afbe0dff0f207ee1622365e6e855a8e2c` |
| E020 recovery receipt | `c8c1a1a9198e92df150fb67ab98cb05dd7d91d22cb50432c3ec91c36e4fc959d` |
| Original E020 MAP lock | `8fa454b8428548423c097221db2144402af2400c99572e320573d338eb112e11` |
| Additive E020 recovery lock | `c87ea0fdea69036a63905e05a22e05e4968030b6449610e2f8ce1fc200cbec89` |
| Completed G7 cache, 60 pairs | `00830d9a7a64735682fce41655b55adf6c088105c339913eac4e604b4275bb13` |

The G7 cache is the original Qwen/Qwen2.5-Math-7B-Instruct checkpoint `ef9926d75ab1d54532f6a30dd5e760355eb9aa4d`, with the exact E020 prompt/readout, CPU BF16 settings and input-only provenance. Validate it with the original E020 completion/catalogue/cache checks. **Zero new LLM calls, prompt changes, model loading or downloads are permitted.** No human reviewers or new correctness annotations are introduced.

## Population, roles and target

Use the unchanged 36,696 rows, original source order, 15 QuestionIds, five outer folds and seed 20260831. Each fold retains nine training, three calibration and three evaluation questions; every row is evaluated exactly once. Verify source hashes, role alignment, disjointness and row accounting before preparation and after scoring. Do not regenerate splits.

The target remains exact `Category:Misconception`, including literal `NA`. Only applicable training labels define sorted candidate columns and prefix inventories. Unsupported recipient truths contribute zero exact accuracy and MAP@3, and remain in union-label Brier. Calibration/evaluation labels never expand the candidate inventory.

The text model L is the unchanged historical full-context TF-IDF/logistic model, with QuestionText, MC_Answer and StudentExplanation in the original tagged format. Missing-to-empty conversion, tokenization, preprocessing and class ordering stay unchanged. No labels, correctness references, QuestionId, source position or checker outputs enter its predictive features. QuestionId is used only for roles/grouping; position only for alignment and fixed ties.

## Exact prediction construction and seven arms

Let F be applicable-training empirical exact-label frequencies, L the applicable-training learned raw distribution, and s=(s_false,s_true,s_unknown) the unchanged cached checker scores. For prefix b in {False,True}, let P_b be P restricted to candidates with prefix b and normalized within that prefix. If the inventory contains no such candidate, set P_b=P and record that fallback. If a nonempty prefix has zero/nonfinite probability mass, stop; do not smooth or drop it.

Use the unchanged E020 soft projection:

`S(P,s) = s_unknown * P + s_false * P_false + s_true * P_true`.

Exactly one-hot unknown returns P by the historical explicit branch. A valid C readout retains its entire soft vector; it is not converted to technical fallback. No binary renormalization, confidence threshold, new parsing or calibration of the three checker scores is introduced.

| Arm | Raw exact-label distribution | Role |
|---|---|---|
| F | F | Historical frequency control |
| L | L | Historical unconditioned text control |
| G7 | S(F,s) | Historical conditioned frequency endpoint |
| L7 | S(L,s) | Historical conditioned text endpoint |
| U50 | 0.5*G7 + 0.5*L | Fixed matched unconditioned-text mixture |
| C50 | 0.5*G7 + 0.5*L7 | Fixed matched conditioned-text mixture |
| T | (1-alpha)*G7 + alpha*L7 | Separately training-selected conditioned ensemble |

All mixtures combine **raw** distributions first and are then calibrated as specified below. They never mix independently calibrated component distributions. Use float64 and the unchanged `np.argsort(-p)[:3]` and argmax conventions on sorted training columns. Explicit endpoints alpha=0 and alpha=1 return G7 and L7 exactly. When alpha=0.5, T reuses C50's raw/final predictions and temperature exactly.

This tests **conditioning each component before averaging**. It does not test conditioning the average `S((1-alpha)*F+alpha*L,s)`, which is generally a different operation. No such extra arm, hard checker arm, G15 arm, confidence-dependent router or expanded ensemble is included. Historical H may be displayed as an explicitly labeled E020 reference in the discussion; it is not reconstructed, tuned, or substituted for U50 in E021's primary comparison.

## Primary fixed comparison and distinct secondary tuned comparison

For original-input final exact-label predictions, let D_f(A,B) be fold f MAP@3(A) minus MAP@3(B). Define meaningful(A,B) as the **unrounded equal-five-fold mean D >= +0.020 and D strictly positive in at least 4/5 folds**. The threshold measures a descriptive practical margin, not significance or an educational safety standard.

**H1, sole primary: meaningful(C50,U50).** Both mixture coefficients are fixed at 0.5 before computation, with no candidate search. The only changed mixture component is L versus L7. Base L fitting/selection is shared; a positive H1 does not establish independence of the component errors or improvement over frequency.

**Raw attribution check:** also compute the same C50−U50 difference and meaningful rule on raw distributions. A claim that the conditioning construction itself improves ranking requires both the final H1 rule and this raw check. If only final H1 passes, describe a benefit of the complete calibrated pipeline; do not attribute it solely to conditioning. This check is a required mechanism diagnostic, not a replacement primary outcome. Publish raw-to-final top-1 and ordered-top-three changes.

**H2, secondary incremental ensemble utility: meaningful(T,G7) AND meaningful(T,L7).** Both are necessary. Beating frequency alone or beating only one endpoint does not establish incremental ensemble value. T is never substituted for C50 as primary. Choosing an endpoint is a valid selection outcome, but fails the claim of meaningful gain over both endpoints.

Report all other contrasts descriptively without additional success flags. No arm, support subgroup, metric, calibration scale, question subset, permutation replicate or review budget replaces H1/H2 after results. Do not round a value below +0.020 upward to a pass.

## Shared nested learning and secondary weight selection

Reconstruct L with the original three-setting word TF-IDF/logistic grid in its original order:

1. ngram_range=(1,1), min_df=2, C=0.5;
2. ngram_range=(1,2), min_df=2, C=1.0;
3. ngram_range=(1,2), min_df=5, C=2.0.

Retain sublinear TF, L2 norm, smooth IDF, historical lowercase/default word pattern, no stop words/accent stripping/feature cap, logistic L2/lbfgs defaults in pinned scikit-learn 1.5.2, max_iter=2000, class_weight=None, random_state=20260831 and n_jobs=1. Use original scientific functions read-only. Any convergence/fit warning is a technical stop, not permission to increase iterations or change settings.

Within each nine-question training role, GroupKFold(3) groups by QuestionId.astype(str). Fit each grid setting on each inner training subset and choose maximum equal-inner-fold **raw L MAP@3**, exact ties first grid entry. Refit that selected L on all nine training questions. This is 10 classifier fits per outer fold, **50 total**. Do not retune L for L7 or for any mixture. Historical inner predictions were not saved for reuse; reconstruction is authorized only after protocol approval.

Retain the selected L setting's inner validation predictions. For each inner split, independently compute F and sorted columns from that inner training subset, then G7 and L7 using the already frozen input-only checker cache. Use no outer-training counts, calibration rows or evaluation labels in these inner predictions.

For T only, evaluate alpha in **[0,0.25,0.50,0.75,1]** on the same three selected-setting inner validation splits. Choose the maximum equal-inner-fold raw exact MAP@3; exact ties choose the smaller alpha (more G7). One alpha per outer fold is applied to every calibration/evaluation row. Publish all five candidates' three inner scores, means and selected index. Do not jointly search text parameters and alpha, use extra weights, choose different weights by question, or select on outer results. Reusing inner folds for L and alpha selection is disclosed development selection, not an independent validation estimate.

C50/U50 receive no mixture search. Their performance must never influence T selection, text hyperparameters, calibration choices or the fixed-comparison interpretation rule.

## Calibration and global freeze

Keep the existing three calibration questions per outer fold; no subdivision or role change. Frequency stays unscaled. Reproduce L, G7 and L7 exactly as E020, including its technical-fallback-aware G7 identity rule: only technical unknown fallback on every calibration AND evaluation row permits unchanged F; a valid C readout does not qualify.

U50 and C50 each fit one separate scalar temperature on their own complete raw exact-label distributions using the original supported-calibration-row NLL fitter: bounded log-temperature [-3,3], probability clipping at 1e-12, T=1 when no calibration truths are supported. Interior selected T values alpha=0.25/0.75 fit their own temperature in the same way. Endpoints reuse G7/L7, and alpha=0.5 reuses C50. Do not calibrate unselected mixture candidates or choose a temperature by MAP@3, ECE, Brier, review results or outer evaluation. Unsupported calibration rows remain excluded only from the original temperature objective, never from evaluation.

Prepare all five folds' models, selected text settings, alpha choices, temperatures, original raw/final distributions, rankings, review orders and exploratory permutation mappings before any E021 evaluation-truth access or scoring. Record a private global freeze with hashes and read-only arrays; no partial-fold results can influence later preparation. Calibration labels are used only for temperatures, training labels only in their prescribed learning/selection roles. The shuffle constructor accepts no targets.

First reproduce F/L/G7/L7 against the pinned E020 aggregate and frozen private prediction evidence: exact counts/nulls/roles/class order/selected settings/rankings/review orders; numerical probabilities, temperatures and all applicable original fold/question/support/calibration/review metrics with absolute tolerance 1e-10 and relative tolerance zero. Include the original historical L reproduction checks and the derived Category view used by the disclosed E020 recovery. Verify the original G7 provenance, frozen data and preservation inventories before and after. A failed reproduction stops before publication of new results; do not fix a mismatch by adjusting scientific settings.

## Registered original-input reporting

For all seven arms, report the complete five-fold and 15-question grid crossed with these unchanged recipient-truth support strata, based only on each outer training role:

- all;
- unsupported: zero examples;
- rare: 1–19 examples;
- frequent: at least 20 examples;
- well-supported: at least 20 examples spanning at least two training questions, nested inside frequent.

Empty cells remain n=0/null. Do not change thresholds to populate a group. True-label support is an evaluation stratum only; it is unavailable to prediction/routing.

Report n, MAP@3 and top-1 accuracy at **both raw and final scales**, along with mean maximum confidence, confidence-minus-accuracy, ten-equal-width-bin ECE and corrected union-label Brier. ECE/Brier require n>=200, correct>=20 and incorrect>=20 separately for the relevant arm/scale/cell; report all ineligibility reasons and jointly eligible denominators. Unsupported truths remain in Brier. No extra Category classifier or Category performance panel is introduced.

Fixed paired contrasts on that grid, at both scales: **C50−U50, C50−F, C50−G7, C50−L7, T−C50, T−U50, T−F, T−G7, T−L7, L7−G7, G7−F, L−F, L7−F**. Include MAP@3/accuracy and jointly eligible ECE/Brier differences. For each arm, report final-minus-raw calibration and ranking changes. At final scale, report exact reciprocal-rank wins/ties/losses and signed mean gain/loss contributions for C50−U50, T−L7, T−G7, C50−F and T−F. Gains plus signed losses must reproduce the paired MAP@3 delta. No oracle or post-hoc best-arm control.

Report every question, including harms. For each registered final all-row contrast, count positive/zero/negative question deltas using unrounded values and report their minimum/maximum. These are descriptive heterogeneity summaries; no per-question threshold, selected subset, new success flag or formal test follows.

Review profiles for all seven original-input arms at **0%,10%,20%,30%,40%,50%** use the unchanged E006 ordering/tie function, original source positions and seed20260831. Within each pooled evaluation fold, defer floor(N*b/100) lowest final-confidence cases. Freeze orders before truth access. Report retained count/coverage, accuracy, risk=1−accuracy, MAP@3, mean confidence, signed confidence gap, eligible ECE/Brier and reasons. Report C50−U50, T−G7, T−L7 and T−F at matched budgets. No threshold fitting, question-specific reranking, automatic unknown deferral or new routing rule. These are fixed-budget retrospective profiles, not deployable cutoff validation or measured human-review effectiveness.

## Exploratory explanation intervention, isolated from H1/H2

Question: does the recipient's own explanation improve L7 predictions beyond shared question/answer context? This reuses only E013's **within-question-and-answer explanation shuffle**. It does not repeat pair shuffling, add a model, or select an ensemble. It is explicitly exploratory and cannot rescue a failed H1/H2.

Apply 100 ordinary permutation replicates within each evaluation `(QuestionId, MC_Answer)` cell, using the exact selected-answer string after historical missing-to-empty conversion, without trimming/case folding/semantic grouping. Converted QuestionText must be identical within QuestionId; otherwise stop. Recipient target and support stratum remain unchanged. Never permute training or calibration inputs, or form donor groups using labels/support.

Use the **same fixed mapping rule and seed as E013**: NumPy Generator(PCG64(SeedSequence([20261014,1,fold,replicate,cell_index]))), folds0–4, replicates0–99. Sort cells by numeric QuestionId then Python Unicode answer order; index from zero within each fold. Sort members by original source position, call permutation once, and map recipients in that order to the returned donor positions. Ordinary fixed points, singleton cells and duplicate text remain; do not redraw or filter them.

Score **L and L7**, with G7 as an invariance control. Identical question/answer inputs imply identical checker vectors; shuffled predictions can therefore be obtained by donor-indexing the original raw/final predictions. Verify this identity synthetically and verify within-cell checker equality before evaluation. Reuse each original model/arm temperature; no recalibration or refitting. G7 must remain unchanged on every row and its scores must reproduce exactly within the numerical reproduction tolerance. Do not publish new shuffle panels for T/C50/U50 or use shuffled outcomes to select anything.

Report original and shuffled MAP@3/accuracy and original-minus-shuffle-mean effects, at raw/final scales, for all fold/question/support cells. For each fold/question report cell count, singleton-row count, rows in nonsingleton cells, and replicate mean/SD of changed donor positions and changed input strings. After the global truth barrier, report rows/share in label-mixed cells as an opportunity diagnostic only. No answer strings, cell IDs, label-by-answer tables or mappings are public. Do not interpret a small effect as absence of explanation information when cell variation is limited. No shuffled calibration or review-budget analyses and no additional meaningful-effect Boolean.

## Descriptive uncertainty and limits

For every original-input panel, publish all five fold values, unweighted mean, sample SD(ddof=1), defined-fold count and jointly defined paired count. SD is null below two defined folds. Primary/secondary decisions use complete all-row five-fold results. Do not substitute row-pooled means, weight questions by a favorable size rule or treat training-overlapping folds as independent experimental replications.

For shuffle quantities, publish replicate mean, sample SD and empirical 2.5th/97.5th percentiles with NumPy linear interpolation. For aggregate dispersion, first combine replicate r across the five folds with equal fold weighting, then summarize the 100 aggregate replicates. Never treat 500 fold-replicate values as independent observations. This is permutation-assignment dispersion, not a confidence interval for future questions or a randomization-test p-value.

No bootstrap, significance/equivalence tests, p-values, AURC, new correlations, unregistered subgroups or additional analyses are included. Repeated benchmark use, only 15 questions, possible model pretraining exposure, unsupported-label limitations and MAP correctness as an unverified reference remain explicit. No formal calibration/coverage guarantee under question shift is claimed.

## Interpretation rules fixed before execution

| Outcome | Permitted interpretation |
|---|---|
| Final H1 and raw attribution check pass | Conditioning the learned component provides a meaningful ranking advantage in the fixed matched comparison on this reused benchmark. |
| Final H1 passes, raw check fails | Registered calibrated-pipeline advantage; conditioning alone has not met the attribution criterion. |
| Raw check passes, final H1 fails | Raw construction benefits did not satisfy the primary calibrated outcome; primary remains negative. |
| H1 fails, H2 passes | Useful selected conditioned ensemble, without the required fixed-comparison mechanism evidence. H2 cannot replace H1. |
| H1 passes, H2 fails | Fixed conditioning benefit without demonstrated meaningful ensemble gain over both endpoints. |
| T selects G7 or L7 | Valid endpoint selection; no incremental ensemble success over that endpoint. |
| Average gains with question harms or poor calibration/review risk | Report the gains and limitations together; no reliable-automation claim. |
| L7 explanation-shuffle drop exceeds L's descriptively | Consistent with increased response-specific explanation dependence after conditioning, not proof of causal reasoning or a primary success. |
| Little shuffle effect | No demonstrated effect under this intervention; cell homogeneity/duplicates may limit its diagnostic power. |
| Both scientific criteria fail | Preserve a negative result; do not change the grid, arms, calibration or thresholds. |
| Missing cache, failed integrity/reproduction, fit warning or runtime error | Technical failure, preserved attempt and stop for review; not a negative scientific result or permission for automatic retry. |

## Implementation, runtime and publication after approval only

Create additive E021 code/tests and a preservation inventory for existing public/private historical evidence, including both E020 locks, original failed attempt, completed recovery, frozen caches/predictions and full prior documentation prefixes. Lock this reviewed protocol, implementation, dependency/input identities and reporting schema, and commit/push sanitized preparation to `traghuram444/responsible-ai-math-misconceptions` before any E021 fitting or scoring. Do not overwrite an E020 lock or receipt, remove its failures, or rerun its launcher/publisher.

Use the unchanged CPU statistical image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`: Python3.11.11, NumPy1.26.4, scikit-learn1.5.2 and its existing complete dependency lock. Set PYTHONHASHSEED=20260831, numerical threads one, UID/GID10001, network none, read-only root/project/data/historical artifacts, cap-dropALL, no-new-privileges and tmpfs scratch. Only a new `artifacts/e021_attempt01` is persistently writable; refuse an existing directory. No system/Docker configuration changes, GPU, model downloads, external API, raw-data redistribution or work outside this project.

Exactly 50 historical classifier reconstruction fits are allowed. Mixture selection and the 100 shuffle replicates reuse predictions; no extra fits or LLM calls. Planning allowance: **10–30 minutes for reconstruction, registered scoring and preservation checks**, excluding implementation, tests, privacy scans and publication. This is an estimate from earlier work, not an E021 pilot or runtime cutoff. If computation fails, preserve it and stop; never reduce replicates or change settings to meet the estimate.

Before execution, synthetic tests must cover projection/fallback identities, fixed comparison differing only in L versus L7, endpoint and alpha0.5 reuse, inner-only counts and selection/ties, supported calibration, sorted-class rankings, all-fold truth barrier, unsupported union Brier, fixed review ties, historical reproduction, strict aggregate field/grid rejection, shuffle mapping/donor equivalence/G7 invariance and monitor isolation. No real MAP pilot is permitted during implementation.

Keep a resilient independent read-only terminal viewer active during actual execution, showing experiment/status/elapsed time/stage, 50-fit progress, and then clearly labeled scoring/permutation progress. Metrics are unavailable before global freeze and historical reproduction; never display stale E020 metrics as E021 progress. Routine chat updates at most hourly while active, completion/failure promptly, no idle monitor and no schedule for protocol review.

On completion verify hashes, strict aggregate schema, historical preservation and reproduction; run full tests and publication/secret/local-path/private-response scans. Publish only sanitized code/docs, aggregate JSON/tables and receipts, with an append-only experiment-log/execution outcome and a separate descriptive result commit. No student text, model weights/vocabulary, generated reasoning, private row/pair/cell identifiers, predictions, mappings or per-file private inventories are public. Show full aggregate and fold-level results first, then all registered question/support/calibration/review/shuffle panels, before interpretation. Stop for user review; no E022 or automatic next experiment is authorized.

## Relationship to existing work

Probability mixtures and calibration under shift are established ideas. [Kumar et al. (UAI2022)](https://proceedings.mlr.press/v180/kumar22a.html) analyze conditions under which calibrated ensembles improve distribution-shift tradeoffs; their results do not guarantee E021 will work. [Park et al. (AISTATS2020)](https://proceedings.mlr.press/v108/park20b.html) show why calibration can fail under covariate shift; E021 does not adopt their adaptation method or assume question shift satisfies their conditions. The [MAP benchmark](https://aclanthology.org/2025.aimecon-wip.3/) defines the task context. E013 already supplies this project's explanation-shuffle intervention; E021 explicitly reuses it rather than claiming novelty.

The intended contribution is the controlled separation of fixed correctness conditioning, training-selected ensemble utility and response-specific evidence under the unchanged question-held-out framework, with complete calibration/heterogeneity reporting and preserved failures. This is a bounded literature/context check, not an exhaustive novelty certification.
