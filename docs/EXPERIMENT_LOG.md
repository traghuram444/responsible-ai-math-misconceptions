# Experiment log

This log is append-only in spirit: completed negative results remain visible. E001 was completed before the repository's first public Git commit; that fact is recorded rather than retroactively assigning it a revision.

| ID | Date | Hypothesis | Split/data fingerprint | Model | Result | Decision |
|---|---|---|---|---|---|---|
| E001 | 2026-08-31 | TF–IDF + logistic regression exceeds frequency baseline under grouped evaluation. | MAP author release `0a5e…686c`; grouped manifest `93a2…7b94`; seed 20260831 | Frequency; TF–IDF + multinomial LR | Grouped MAP@3: 0.539 frequency vs 0.497 explanation-only / 0.520 question+explanation LR. Random reference: 0.764 / 0.785. | Stop TF–IDF branch; no transformer. Preserve as negative result. |
| E002 | 2026-08-31 | Fold-local label support is non-zero, while cross-question exact/near text overlap is low enough that E001's gap cannot be dismissed as response reuse. | Same frozen MAP grouped manifest as E001; train role only compared to evaluation role. | Aggregate support + exact-match + fixed character-TF–IDF nearest-neighbor diagnostic; no classifier. | 21.1% of held-out rows had a label absent from fold-local train; exact overlap 0.59%; mean rate with similarity ≥0.95 was 0.88%. | Preserve E001. E003 must decompose supported versus unsupported-label results without changing the primary all-row score. |
| E003 | 2026-08-31 | Scores improve on fold-supported labels, but the original all-row lexical-baseline decision remains unchanged. | Same frozen grouped manifest, E001 roles, variants, grid, and calibration. | E001 frequency and TF–IDF + LR reproduced; primary all-row plus secondary fold-supported-label subset. | Preregistered; not yet run. | Publish both views. Do not use the secondary subset to erase unsupported-label difficulty. |

For each completed run add: command/config path, Git revision, seed, runtime/hardware, train/calibration/evaluation group IDs or hashes, all metrics, artifacts, and an honest decision.
