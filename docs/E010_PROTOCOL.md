# E010 review prioritization at fixed budgets

## Authorization and scope

Preregistered 2026-10-13 before E010 computation. The user authorized proceeding and starting the proposed fixed-budget review-prioritization experiment. The operational choices below are agent-specified before execution under that authorization, not a claim that the user separately reviewed every numerical choice. Commit and hash-lock this protocol and the tested implementation before a single Docker run. Preserve E001–E009 unchanged.

E010 asks whether E009's learned reliability score sends more actual classifier errors to a fixed-capacity review queue than simpler scores. It does not revise E009's negative automation result, relax its thresholds, replace the classifier, or assume human reviewers correct deferred errors. This is retrospective batch routing on the repeatedly examined 15-question MAP benchmark, not independent confirmation or an online risk guarantee.

## Hypotheses and fixed decision

H1, separately for each input arm: at **20% review**, learned reliability reduces remaining classifier errors by at least **2.0 per 100 original evaluation responses**, averaged equally over the five folds, compared with **support-aware routing**, and has strictly fewer remaining errors in at least **four of five folds**. Both requirements must hold. This margin is a pragmatic preregistered research criterion, not an educational safety standard. No tolerance or rounding enters the comparison. Neither arm is selected as the winner; report both Boolean results and all differences.

H2, secondary: quantify review prioritization at all registered budgets against calibrated confidence, raw confidence, support-aware routing, and a deterministic no-information reference applied to the same classifier. H3, secondary: characterize per-question and true-label-support variation and retained calibration. The frequency classifier is separate context, not a same-prediction routing comparison or a second independent arm.

An unmet H1 remains an unmet primary criterion even if AUROC, another budget, a subgroup or one arm looks favorable. A met H1 indicates descriptive error concentration in a simulated review queue, not corrected errors, human benefit or reliable automation. Retained risks can remain high. Report question-level reversals without attributing their cause.

## Frozen reconstruction and leakage safeguards

Reuse E009's code unchanged: both explanation-only and question-plus-explanation arms; the frozen five QuestionId folds and seed 20260831; nine classifier-training questions, one temperature question, two threshold-selection questions and three evaluation questions. Preserve its 3/3/3 reliability cross-fitting, independent E001 grouped tuning inside each six-question training subset, five features, weighted scaler/logistic router, final nine-question classifier and original temperature fit. No feature search, router tuning, extra calibration or new model.

The two threshold-selection questions remain reserved: their E009 policies are reproduced for verification, but they do not select E010 budgets, score functions or model settings. Do not transfer them into training. Keep E009's literal inner hash namespaces and seeds, not E010 substitutions.

E009 did not retain row-level scores or models. Reconstruct them once in memory; expected 400 classifier fitting attempts and up to 10 router fits, not an extra tuning experiment. Reproduce all ten development records before accepting new routing masks, then all 200 E009 evaluation records and all 50 ranking records after masks are frozen. Use exact structural/discrete comparisons and absolute 1e-10, relative zero for floats. Stop on any mismatch; no tolerance changes or silent retries.

Reference SHA-256 values:

| Input | SHA-256 |
|---|---|
| Author-release training CSV | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignments | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |
| E009 aggregate reference | `f0aecdff883f9a26facb8a9678a1079a54814c793353e9b52d8c00b38fb75a5b` |

Also verify unchanged E007–E009 approval/configuration hashes and referenced fingerprints through the existing gates. Hash preserved scientific files before and after execution.

## Batch routing rules and budgets

Six rules per arm: learned reliability, calibrated confidence, raw confidence, support-aware, hash-only no-information, and frequency. The first five share identical final classifier predictions. Hash-only uses a constant zero score, not a learned or random-seed-searched score. Frequency uses its original constant maximum probability and its own classifier predictions.

For each fold, pool all responses from its three evaluation questions as one batch. Do not allocate separate question or label quotas. Review budgets are **0%, 10%, 20%, 30%, 40%, 50%**; zero is the unfiltered reference. For N responses and integer percentage b, review exactly `floor(N*b/100)` and retain the other responses. This integer definition avoids floating-point boundary effects.

Sort by descending unrounded score; ties by ascending SHA-256 of UTF-8 `fold={fold};source_row={row};seed=20260831` (no newline), then ascending source position for hash collisions. This is E006's existing tie serialization. Retain the first N-floor(N*b/100); review the remainder. Scores, source positions and batch size enter routing; correctness, true-label support and QuestionId do not. Source positions are alignment/tie metadata, never model features or public row identifiers. No cutoff search, risk optimization or selection of the best observed budget.

Compute and freeze all 360 fold/arm/rule/budget masks in memory before reading evaluation correctness; mark arrays read-only and serialize only aggregate batch counts plus the full reconstructed development description as the freeze barrier. Do not persist masks, per-row scores or models. Masks are nested as review increases. Input ordering cannot change decisions when source positions remain attached. Changing batch composition may change fixed-budget decisions; this is explicitly not a streaming or batch-invariant policy.

## Metrics and denominators

For every fold/rule/budget, and each of its three questions and five registered support strata, report:

- Original count N, original errors E, retained count n and retained errors e; reviewed count d=N-n and reviewed errors c=E-e; reviewed correct count d-c.
- Coverage n/N and actual review fraction d/N; retained accuracy, MAP@3 and risk e/n.
- **Remaining errors per 100 original responses:** 100*e/N (primary metric). **Captured errors per 100:** 100*c/N; **error capture fraction:** c/E; **review error precision:** c/d. Null when the relevant denominator is zero; zero captured errors with a nonzero original-error denominator is zero, not null.
- Retained classifier mean confidence, ten-equal-width-bin ECE and union-label-corrected multiclass Brier. ECE/Brier require n>=200, correct>=20 and incorrect>=20; otherwise null with fixed eligibility reasons. These use original calibrated classifier probabilities, not router scores. Frequency remains unscaled.
- For learned reliability only, retained mean predicted correctness, binary Brier and binary ECE, with E009's same eligibility rule. Keep these distinct from classifier calibration.

True-label strata remain unsupported (training count 0), rare (1–19), frequent (>=20), and nested well-supported (>=20 across >=2 training questions), plus all. They are reporting masks after global routing, never routing inputs. Include empty strata. Unsupported truths remain errors; their calibration fails the correct-count eligibility rule by construction.

Within question/stratum summaries, original/error denominators refer to that question/stratum. Achieved review shares can differ from the fold-level budget; report this variation, do not restore quotas after seeing results. Question results are evaluation-only public identifiers; training/development groups use anonymous existing block/role indices.

## Aggregation and complete reporting

Publish the full **360 fold records and 1,080 evaluation-question records**, all five strata and separate reliability calibration. Frequency duplicates across arms are identical reference data, not additional evidence. All first-five-rule original errors agree within an arm/fold; all zero-review classifier metrics agree.

For each numeric fold metric report all five values, equal-fold mean, sample SD (ddof=1) and defined-fold count. No row-level intervals, bootstrap, permutation tests or p-values. Means are descriptive on a reused benchmark with overlapping training sets.

For each nonzero budget, pair learned-minus-control remaining-errors-per-100, error capture fraction, review error precision and retained risk against each of the other five rules. Include both original error counts and actual review fractions at fold level so frequency's different classifier and conditional denominators remain explicit. Positive primary **benefit** is support-aware minus learned remaining errors per 100. Publish its five fold values, mean/SD, positive-fold count and exact H1 Boolean for each arm. Show all question and stratum results; do not select favorable subgroups. No new curve sweep, oracle, ablation or significance analysis.

## Verification and publication

Synthetic tests cover exact budget arithmetic, hash ties and collisions, nested masks, permutation invariance, label exclusion, deferred/retained count identities, perfect/reversed/no-information orderings, empty/error-free strata, calibration eligibility, per-question partitions, frequency duplication, zero-review equality, exact primary margin boundary, full-grid completeness, strict schema/private-field rejection, reproduction mismatch and freeze-before-correctness ordering. Inherited E009 tests retain the nested fitting and feature-leakage coverage.

Use the existing audited image `sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c`, UID/GID 10001, network disabled, root/project/data read-only, single-thread numerical settings, and only new `artifacts/e010/` writable. Do not change host configuration or dependencies. Start the read-only terminal monitor only during execution; stop on completion/failure. At-most-hourly active-run notifications plus completion/failure/intervention, no idle automation.

Estimated compute 25–45 minutes, anchored to E009's 25m47s reconstruction; verification/implementation time is additional. No timing pilot or alternate seed run. Failures are preserved; no silent retry.

Strict aggregate allowlists reject raw responses, row identifiers, masks, scores/probability arrays, weights, coefficients, scaler statistics and neighbor information. Run full tests, preserved-file verification, independent aggregate arithmetic and response/secret/local-path scans before publishing. Commit/push implementation and preregistration first, results separately afterward, only to `traghuram444/responsible-ai-math-misconceptions`. Present full numerical results before interpretation; no further experiment or data acquisition is included.

## Literature boundary

E009's rationale and prior-art limits remain applicable: [Kamath et al., ACL 2020](https://aclanthology.org/2020.acl-main.503/) studies correctness calibration for selective QA under shift; [Varshney et al., Findings ACL 2022](https://aclanthology.org/2022.findings-acl.158/) finds no consistently superior selection method across tested settings. Neither establishes this MAP policy's effectiveness. The contribution is controlled, reproducible evaluation, not algorithmic priority.
