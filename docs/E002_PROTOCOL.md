# E002 preregistration — label support and cross-question overlap diagnostic

**Status:** completed on 2026-08-31. Results: [E002_RESULTS.md](E002_RESULTS.md).

## Motivation and hypothesis

E001 found a large random-to-question-held-out MAP@3 gap (0.785 to 0.520) and did not beat the grouped frequency baseline (0.539). Before trying a stronger model, E002 tests two non-model explanations that could constrain or distort that result:

1. evaluation targets may be absent from the fold-local training label set; and
2. cross-question responses may contain exact or very-near text overlap.

The MAP benchmark paper reports synthetic paraphrases and warns about their distribution, making this diagnostic necessary. The hypothesis is that unsupported labels are non-zero, but cross-question exact/near overlap is low enough that E001's generalization gap cannot be reduced to obvious response reuse.

## Fixed protocol

- Reuse the frozen five-fold `QuestionId` assignments from E001; no fold, threshold, or model selection will use E002 results.
- For each outer fold, compare the evaluation role only with the fold-local **train** role. Calibration examples are excluded from the comparison corpus because they are not model-fitting examples.
- Count held-out combined `Category:Misconception` labels absent from the train role, by rows and unique labels.
- Normalize explanations with Unicode NFKC, case-folding, and whitespace collapse; count exact normalized matches between train and evaluation. Never write normalized text or match pairs.
- Fit a character-boundary TF–IDF vectorizer (3–5 grams; `min_df=1`) on train explanations only. For each evaluation explanation, calculate its cosine similarity to its single nearest train explanation. Report only quantiles and rates at fixed thresholds 0.80, 0.90, and 0.95.
- Write only per-fold and pooled numeric summaries. The output, all inputs, and the row-level fold assignment remain local-only and ignored by Git.

## Decision boundary

E002 does not select a model and cannot overturn E001. It will determine whether E003 must explicitly separate unsupported-label performance or introduce a stronger duplicate/family stress test. Any E003 model will be preregistered after these aggregate findings are documented.
