# E001 results — frozen baseline experiment

**Status:** completed 2026-08-31. No transformers were trained.

## Reproducibility record

- Data: author-published MAP training release, SHA-256 `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c`.
- Split manifest: SHA-256 `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94`.
- Seed: `20260831`; five outer `QuestionId` folds; group-disjoint calibration subsets.
- Tuning: three TF–IDF/logistic configurations selected only with inner folds of each outer training portion. The question-held-out evaluation fold was never used for selection or calibration.
- Runtime: approximately 26 minutes in the UID 10001 Docker container; CPU baseline only.

## Aggregate results (mean across five outer folds)

| Split / input | Model | Top-1 accuracy | Macro-F1 | MAP@3 | ECE | Brier |
|---|---:|---:|---:|---:|---:|---:|
| Question-held-out / explanation | Frequency | 0.402 | 0.036 | 0.539 | 0.056 | 0.582 |
| Question-held-out / explanation | TF–IDF + LR | 0.354 | 0.049 | 0.497 | 0.120 | 0.605 |
| Question-held-out / question + explanation | Frequency | 0.402 | 0.036 | 0.539 | 0.056 | 0.582 |
| Question-held-out / question + explanation | TF–IDF + LR | 0.376 | 0.055 | 0.520 | 0.109 | 0.592 |
| Random-reference / explanation | TF–IDF + LR | 0.644 | 0.306 | 0.764 | 0.023 | 0.477 |
| Random-reference / question + explanation | TF–IDF + LR | 0.668 | 0.330 | 0.785 | 0.015 | 0.453 |

The random reference is intentionally optimistic: it permits responses from the same questions in both train and evaluation sets. It is not a generalization estimate.

## Question-held-out per-question performance

Results below use the stronger question-plus-explanation TF–IDF variant.

| QuestionId | n | Top-1 accuracy | MAP@3 | ECE |
|---|---:|---:|---:|---:|
| 31772 | 4,857 | 0.357 | 0.486 | 0.345 |
| 32829 | 2,156 | 0.556 | 0.677 | 0.073 |
| 104665 | 673 | 0.123 | 0.281 | 0.315 |
| 31778 | 3,640 | 0.337 | 0.453 | 0.145 |
| 32835 | 2,332 | 0.188 | 0.444 | 0.235 |
| 109465 | 1,051 | 0.422 | 0.594 | 0.041 |
| 31774 | 3,115 | 0.434 | 0.566 | 0.029 |
| 33474 | 1,766 | 0.227 | 0.388 | 0.080 |
| 91695 | 2,610 | 0.334 | 0.520 | 0.062 |
| 32833 | 3,105 | 0.390 | 0.493 | 0.192 |
| 33472 | 2,800 | 0.454 | 0.570 | 0.038 |
| 76870 | 1,186 | 0.331 | 0.484 | 0.104 |
| 31777 | 2,809 | 0.588 | 0.708 | 0.091 |
| 33471 | 1,542 | 0.375 | 0.519 | 0.172 |
| 89443 | 3,054 | 0.321 | 0.484 | 0.080 |

## Simulated human-review results

For question-held-out question-plus-explanation TF–IDF + LR, mean retained-case top-1 accuracy was:

| Human-review rate | AI coverage | Accuracy on AI-handled cases |
|---:|---:|---:|
| 0% | 100% | 0.376 |
| 10% | ~90% | 0.392 |
| 20% | ~80% | 0.402 |
| 30% | ~70% | 0.415 |
| 40% | ~60% | 0.430 |
| 50% | ~50% | 0.447 |

This is a weak reliability/coverage trade-off: deferral improves retained accuracy, but nowhere near a level that supports autonomous high-stakes use. It is a simulated routing analysis, not evidence of teacher time savings or educational impact.

## Decision and research implication

**Stop the TF–IDF branch; do not train a transformer yet.** Its question-held-out MAP@3 (0.520) is lower than the frequency baseline (0.539), despite modest macro-F1 gains. The result is valuable, not a failure to conceal: random validation overstated MAP@3 by 0.265 for the stronger baseline, and confidence calibration degraded markedly under unseen-problem transfer.

The next justified work is diagnostic analysis—not scale-up: quantify duplicate/paraphrase and synthetic-family overlap, characterize label support by held-out item, implement a sentence-embedding baseline with the same frozen folds, and pre-register any model change. The project remains technically meaningful as a reproducible audit of generalization and selective prediction, even if related academic work exists.
