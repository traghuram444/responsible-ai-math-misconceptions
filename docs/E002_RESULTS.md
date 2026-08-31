# E002 results — label support and cross-question overlap diagnostic

**Status:** completed 2026-08-31. No classifier was trained or selected.

## Reproducibility record

- Data: author-published MAP training release, SHA-256 `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c`.
- Frozen split manifest SHA-256: `93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94`.
- Local aggregate report SHA-256: `dbbc182ae04f9b3765ac5461942782c123c020dd1b07398c31cb4d17aed8af94` (the report is ignored because it contains fold-level derivatives).
- Implementation: character-boundary TF–IDF (3–5 grams, `min_df=1`) fitted only on each fold's train role, followed by one-nearest-neighbor cosine similarity for its held-out role.
- Output policy: no text, match pairs, row-level similarities, or identifiers were written or published.

## Results

| Fold | Held-out rows | Rows with label unsupported in train | Exact normalized train-text match | Nearest-train similarity p95 | Similarity ≥ 0.95 |
|---:|---:|---:|---:|---:|---:|
| 0 | 7,686 | 5.3% | 0.30% | 0.757 | 0.44% |
| 1 | 7,023 | 23.0% | 0.68% | 0.813 | 1.04% |
| 2 | 7,491 | 26.5% | 0.56% | 0.796 | 0.92% |
| 3 | 7,091 | 30.5% | 0.83% | 0.821 | 1.16% |
| 4 | 7,405 | 21.4% | 0.62% | 0.771 | 0.86% |
| **Pooled / mean** | **36,696** | **21.1% pooled** | **0.59% pooled** | **0.792 mean** | **0.88% mean** |

The median nearest-train character-TF–IDF cosine similarity averaged 0.505 across folds; the p90 averaged 0.716, p99 averaged 0.936, and the mean rates at or above 0.80 and 0.90 were 4.57% and 1.61%, respectively.

## Interpretation and decision

The preregistered hypothesis was partially supported. A material 21.1% of evaluation rows have a combined label absent from the fold-local training set. A standard closed-set classifier cannot assign such a label, so aggregate performance mixes two distinct challenges: transfer to a new question with a known label and transfer requiring a new label.

At the same time, cross-question **exact** response overlap is low (0.59%) and only 0.88% of held-out responses clear the deliberately strict 0.95 character-similarity threshold. These measures do not rule out semantic paraphrases, shared answer patterns, or other item-family effects; they do rule out explaining E001's broad random-versus-grouped gap through widespread exact or near-exact text reuse.

E003 must therefore report results separately for fold-supported and unsupported labels, while retaining the full primary target. It should not remove unsupported labels from the primary score or reinterpret the E001 negative result as a success.
