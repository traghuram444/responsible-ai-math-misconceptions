# E004 preregistration — semantic embedding baseline

**Status:** approved 2026-08-31; implementation pending. No E004 run has started.

## 1. Exact hypothesis

A compact pretrained semantic sentence encoder followed by fold-local multinomial logistic regression will improve mean question-held-out MAP@3 over the E003 frequency baseline (0.539), while retaining comparable or better calibration after fold-local temperature scaling.

## 2. Model and embedding approach

- Encoder: `sentence-transformers/all-MiniLM-L6-v2`, frozen (no fine-tuning), recorded by exact revision and license before execution.
- Input arms: `StudentExplanation` and `QuestionText + StudentExplanation`, matching E001/E003.
- Pooling: the encoder's standard sentence embedding; L2-normalize embeddings.
- Classifier: multinomial logistic regression, fit only on each fold's training role. This adds semantic representation capacity without a large supervised language model.

## 3. Train/validation methodology

Unchanged from E003: frozen five-fold outer `QuestionId` split; group-disjoint calibration role; all vector/embedding preprocessing and classifier hyperparameter selection fit inside each outer training role. A fixed small logistic-regression grid is selected only by three inner `GroupKFold` splits. Temperature scaling uses only the calibration role. The outer evaluation role is never used for tuning, calibration, or encoder fitting.

## 4. Metrics

- **Primary:** mean all-row question-held-out MAP@3, compared with the fold-local frequency baseline.
- **Secondary:** top-1 accuracy, macro-F1, ECE (10 equal-width bins), multiclass Brier, risk–coverage at 0–50% review, per-question aggregates, and the E003 supported-label subset as a diagnostic only.
- **Reference only:** the existing random-split comparison may be reproduced only if it does not change the primary grouped protocol.

## 5. Success and failure criteria

Success requires a **practically meaningful** mean grouped all-row MAP@3 gain over the 0.539 frequency baseline: an absolute delta of at least 0.02, with fold-level scores and their standard deviation reported, and no material ECE or Brier degradation relative to frequency. A failure includes a smaller gain, no improvement, a gain confined to the supported-label subset, or unreliable confidence/risk–coverage. In either case, publish the aggregate result and retain E001–E003 unchanged.

## 6. Expected runtime

Estimated 25–60 minutes on the current single-CPU Docker setup, depending on one-time model download and embedding throughput. The live terminal monitor will report fold/stage progress and most recent completed-fold metrics without reading or writing raw responses.

## Live monitor

Run this in a second terminal while an experiment is active:

```powershell
docker compose run --rm research python scripts/monitor_experiment.py --status-file artifacts/live_status.json
```

The experiment process will atomically refresh the ignored status file after meaningful milestones. The monitor is read-only and does not interrupt it.
