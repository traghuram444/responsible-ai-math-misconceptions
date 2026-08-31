# Frozen research plan (v1.0)

## Research question

On MAP student explanations, how do straightforward models and a supervised language model perform when all responses to an evaluation `QuestionId` are withheld, and can calibrated confidence define a useful simulated human-review tradeoff?

## Unit of generalization and leakage rules

The primary unit is `QuestionId`, not a response row. For each outer fold, train, calibration, and evaluation roles are mutually exclusive at the `QuestionId` level. The implementation writes a data fingerprint and assignments before fitting.

Forbidden features for primary evaluation include:

- any test/evaluation response or label;
- mappings from held-out question to correct answer, category prefix, candidate label list, error rate, or exact/near-duplicate response;
- model selection using leaderboard feedback;
- preprocessing fit on the evaluation fold;
- calibration fit on evaluation responses.

Permitted at inference are the target response's own `QuestionText`, `MC_Answer`, and `StudentExplanation`. Whether an independently supplied answer key is permitted is an explicit ablation; it cannot be reconstructed from held-out examples.

## Evaluation design

| Purpose | Split | Role |
|---|---|---|
| Primary | 5 outer `GroupKFold` folds by `QuestionId`; group-disjoint 20% inner calibration split | Generalization to unseen problems |
| Reference only | 5-fold random row split stratified by the six-way `Category` field, same seed | Quantifies optimistic leakage bias; sparse combined labels make full-target stratification invalid |
| Optional stress test | Semantic/item-family grouping preregistered before results | Stronger but lower-power transfer test |

With 15 known item groups, each outer evaluation fold will contain roughly three items. Report each outer-fold score, mean, standard deviation, and bootstrap confidence intervals over responses **and** a caveat that response-level resampling does not create new items. Report the number/rate of evaluation labels absent from that outer training fold.

## Outcomes

The main target is the combined competition target `Category:Misconception`; the competition's MAP@3 is retained for comparability. Report top-1 accuracy, macro-F1 (clearly stating whether labels unsupported in training are included), MAP@3, per-question metrics, and confusion summaries.

For uncertainty, fit temperature scaling only on the group-disjoint calibration part of each outer fold. Compare maximum probability, top-two margin, and predictive entropy. Report ECE (bin scheme stated), multiclass Brier score, reliability plots, risk–coverage/AURC, and retained-case performance at 0%, 10%, 20%, 30%, 40%, and 50% review. Thresholds must be chosen without evaluation labels.

## Model sequence and stop rules

1. Frequency baseline: predict training-fold label prevalence.
2. TF–IDF + multinomial logistic regression: explanation-only; then question-plus-explanation.
3. Sentence embedding + logistic regression, using a permissively licensed encoder recorded by revision and license.
4. Add a lightweight tree model only if it introduces distinct non-text features without question leakage.
5. One supervised transformer chosen after baselines based on license, runtime, grouped performance, and calibration—not size.

Stop a branch if it does not exceed the frequency baseline on mean grouped MAP@3, has materially worse calibration without a recoverable calibrated variant, or relies on prohibited question-specific information.

## Ablations

Hold model, folds, seed, and calibration procedure constant while comparing: explanation-only; question + explanation; selected answer + question + explanation; and independent answer-key availability if legally/source-supported. Never include a feature only in the stronger arm without declaring it.

## Reproducibility record

Every run receives an experiment ID and records the hypothesis, data SHA-256, split-manifest hash, seed, code revision, model/revision/license, parameters, runtime/hardware, metrics, and decision in [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md). Negative outcomes stay logged.
