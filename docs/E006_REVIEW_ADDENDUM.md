# E006 review addendum — proposed clarifications and metric correction

**Status: proposed for user review; not approved and not run.** This addendum and its matching `experiments/e006_review_addendum.yaml` would govern E006 only after approval. The original E006 proposal and configuration remain preserved. E001–E005, their source metrics, and their artifacts remain unchanged.

## Scope and prior observation

The research question remains whether existing model confidence can allocate limited human review to less reliable predictions on unseen math questions. Reconstruct the two E001 TF–IDF/logistic input arms and their fold-local frequency baseline using the frozen five QuestionId folds, training/calibration roles, seed, inner tuning grid, temperature fitting, target, and inputs. There is no new classifier, representation, or routing score.

Existing artifacts contain aggregate results rather than row-level probabilities. Therefore E006 must reconstruct probabilities in memory using the existing fitting procedure. Those probabilities and all student data remain local and are never serialized. Runtime is currently unknown; measure it after approval rather than treating earlier experiment durations as a benchmark.

E001 already published confidence-based review results, including question-plus-explanation accuracy increasing from approximately 0.376 to 0.447 at 50% review. E006 extends and checks previously observed behavior; that curve and its proposed benefit threshold are not an independent discovery. Repeated examination of these 15 questions limits confirmatory inference even with frozen folds.

## Preflight and reproduction gate

Before computing selective results, verify the following SHA-256 fingerprints:

| Input | SHA-256 |
|---|---|
| Training CSV | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Frozen split manifest | `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94` |
| Frozen assignment CSV | `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd` |
| E001 aggregate reference | `dc06418b3120f3b4e4293b696c66d6f1b5cf00f59eba615640c97770f388df99` |

Also verify matching row counts; ordered, unique source-row positions; matching QuestionId and target values; exactly the five registered fold columns; valid train/calibration/evaluation roles; and disjoint QuestionId sets between roles. The assignment fingerprint records the existing file at this review; it does not imply that this additional hash was recorded at E001 preregistration.

For each grouped fold, input arm, and model, reproduce E001's all-row MAP@3, top-1 accuracy, and ten-bin ECE within absolute tolerance `1e-10`, with relative tolerance zero, before routing that fold. Record the comparisons. A mismatch stops execution for investigation; it cannot justify changing a split, parameter, calibration setting, tolerance, or historical artifact. A partial run is not a completed E006 result.

## Routing and review budgets

The three original rules remain: calibrated maximum probability; that probability multiplied by `log1p(training_count_of_predicted_label) / max(log1p(training_class_counts))`; and constant fold-local frequency confidence. Counts use only the training role. The support-weighted score is a ranking score, not a recalibrated probability. Actual target support never enters routing.

Within each outer evaluation fold, sort descending by routing score. For every rule, resolve equal scores by ascending SHA-256 hexadecimal digest of UTF-8 text `fold={fold};source_row={source_row};seed={seed}`. Integers use unsigned decimal notation without leading zeros, spaces, or a trailing newline. Use seed `20260831`; on a digest collision use ascending source-row position. Source-row identifiers remain in memory only.

The fixed review fractions are `0, 0.1, 0.2, 0.3, 0.4, 0.5`. Retain exactly `ceil(n * (1 - review_fraction))` cases per fold. Curves connect these six registered points over 50–100% coverage; there is no additional budget grid or full-domain area-under-curve metric.

This is a fixed-capacity batch simulation. Ranking an evaluation batch uses its unlabeled scores to allocate review; it does not establish a score threshold transferable to future questions. No accuracy target, risk target, or threshold is selected using evaluation outcomes. Temperature fitting remains unchanged, including its existing exclusion of unsupported calibration truths.

## Strata and reported quantities

True exact-label support is defined using the training role: unsupported means zero examples; rare means 1–19; frequent means at least 20; well-supported means at least 20 across at least two training questions. Well-supported is nested within frequent. Select the full fold's retained set first, then intersect it with each stratum; never allocate a separate review quota using true labels.

For all cases and each stratum at every budget, report original and retained counts, retention fraction relative to the original group, share of the retained set, top-1 accuracy, MAP@3, risk (`1 - accuracy`), and absolute risk reduction versus that rule's 0% review. Empty groups and undefined ratios or metrics are explicit nulls with counts, never zero-valued performance estimates.

Report ECE and Brier for a retained fold/stratum/model only when it has at least 200 cases, 20 correct predictions, and 20 incorrect predictions. Use original calibrated maximum probability for ten-equal-width-bin ECE, including for support-weighted routing. Unsupported cases cannot satisfy this eligibility rule; still report their counts, retention, accuracy, MAP@3, and risk. Report confidence AUROC for correct-versus-incorrect separation for each learned input arm on all evaluation cases, only where both outcomes exist.

## Brier correction and comparison

The historical Brier implementation omits the true-class squared-error term when the truth is outside the model's class set. Preserve it under the field `legacy_multiclass_brier`. E006 additionally reports `union_label_brier`, computed by the new `metrics_v2.union_label_brier_score` over the union of model and true labels, with probability zero assigned to absent classes. Equivalently:

`union_label_brier = legacy_multiclass_brier + unsupported_fraction_of_scored_cases`.

Keep the original metric implementation untouched. Both fields use the same eligibility rule. Use the corrected field for E006 calibration comparisons and distinguish it from historical values. This correction matters when routing methods retain different proportions of unsupported cases.

## Aggregation, uncertainty, and decision rule

Publish all five fold values, their equal-weight mean and sample standard deviation, and paired fold differences: learned routing minus frequency at the same budget, each rule's retained risk minus its own 0%-review risk, and support-weighted minus confidence-only routing within each input arm. Calibration means include eligible folds only; paired calibration comparisons use the intersection of eligible folds and report its size. Undefined folds stay visible. No significance claim or independent-fold interpretation follows from these summaries.

For each learned input-arm/routing-rule pair independently, the relative routing-benefit criterion at 50% review requires **both** mean risk reduction of at least `0.05` absolute versus its own 0% review **and** strictly lower mean retained risk than frequency at the same budget. Failure to meet either condition means that pair fails the criterion. Do not select a winning pair after inspection or collapse the four decisions into a general automation claim.

Calibration differences are descriptive, with no binary gate. This is an explicit proposed replacement of the original undefined phrase “materially worse” and requires review. Passing the relative criterion does not establish sufficiently low absolute risk for automation. No deployment threshold, educational benefit, or human-review accuracy is assumed.

The registered rules, budgets, support reporting, calibration, AUROC, and paired summaries form the fixed diagnostic analyses, subject to the prior-observation caveat. Alternative scores, budgets, thresholds, models, qualitative samples, and outcome-based subgroup choices remain exploratory and outside this run. Publish aggregate-only artifacts with hashes, provenance, and completion status; never publish student text, identifiers, probabilities, predictions, rankings, or model caches.
