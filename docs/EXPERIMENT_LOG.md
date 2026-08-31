# Experiment log

This log is append-only in spirit: completed negative results remain visible. E001 was completed before the repository's first public Git commit; that fact is recorded rather than retroactively assigning it a revision.

| ID | Date | Hypothesis | Split/data fingerprint | Model | Result | Decision |
|---|---|---|---|---|---|---|
| E001 | 2026-08-31 | TF–IDF + logistic regression exceeds frequency baseline under grouped evaluation. | MAP author release `0a5e…686c`; grouped manifest `93a2…7b94`; seed 20260831 | Frequency; TF–IDF + multinomial LR | Grouped MAP@3: 0.539 frequency vs 0.497 explanation-only / 0.520 question+explanation LR. Random reference: 0.764 / 0.785. | Stop TF–IDF branch; no transformer. Preserve as negative result. |

For each completed run add: command/config path, Git revision, seed, runtime/hardware, train/calibration/evaluation group IDs or hashes, all metrics, artifacts, and an honest decision.
