# Responsible AI for Mathematical Misconceptions

> **Active research — not a finished system or deployment recommendation.**

Reproducible research code and documentation for the question: **can mathematical-misconception detection generalize to unseen K–12 math questions, with uncertainty-aware human review?**

The current evidence is limited to a 15-question middle-school benchmark; it is not a claim of K–12-wide validity.

## Research scope

This project uses the author-published MIT-licensed MAP (Misconception Annotation Project) training release recorded in `docs/DATA_AND_LICENSES.md`. It is not a Kaggle leaderboard replication: the primary evaluation holds out entire `QuestionId` groups. The available MAP corpus is a middle-school benchmark, not evidence for K–12-wide performance.

The primary evaluation withholds entire `QuestionId` groups, rather than randomly splitting individual responses. This asks whether a model transfers to a never-before-seen math problem, while measuring calibration and a simulated option to defer uncertain predictions for human review.

## Status

**September 2026 checkpoint:** E001–E005 historical runs are preserved. **E006 is complete** under the approved protocol: all 60 E001 reproduction checks passed with zero difference, and the full run took about nine minutes. No experiment or monitor is currently active. See the [raw result tables](docs/E006_RESULTS.md), [complete aggregate/fold JSON](results/E006_aggregates.json), and [approval/execution record](docs/E006_EXECUTION_RECORD.md). Interpretation and any subsequent experiment await review.

Start with the [research review](docs/RESEARCH_REVIEW_2026_09.md), [reproducibility audit](docs/REPRODUCIBILITY_AUDIT_2026_09.md), and [reviewable E006 addendum](docs/E006_REVIEW_ADDENDUM.md).

E001 established the negative baseline:

| Evaluation | MAP@3 |
|---|---:|
| Random row split, TF–IDF + logistic regression | 0.785 |
| Question-held-out split, same model | 0.520 |
| Question-held-out frequency baseline | 0.539 |

Random validation was substantially optimistic, and the stronger lexical baseline did **not** exceed the frequency baseline under unseen-question evaluation. See [the original E001 report](docs/E001_RESULTS.md). E004 subsequently evaluated a frozen pretrained encoder; no transformer was fine-tuned.

| Subsequent evidence | Result | Record |
|---|---|---|
| E002: true-label support | 21.1% of grouped evaluation rows have an exact label absent from training | [E002](docs/E002_RESULTS.md) |
| E003: supported-label MAP@3 | TF–IDF question+explanation 0.668 vs frequency 0.689 | [E003](docs/E003_RESULTS.md) |
| E004: frozen MiniLM MAP@3 | 0.476 explanation-only / 0.464 question+explanation vs frequency 0.539 | [Recovered E004 tables](docs/E004_RESULTS_ARCHIVE.md) |
| E005: transfer decomposition | 7,755 unsupported, 0 rare, 28,941 frequent; 28,187 well-supported (nested) | [Recovered E005 tables](docs/E005_RESULTS_ARCHIVE.md) |

**Metric erratum:** the legacy Brier implementation understated scores for unsupported true labels. MAP@3, accuracy, and ECE are unaffected. Proper all-outcome-space grouped frequency Brier is **0.795057**, versus the historical **0.581666**. The [append-only correction](docs/METRIC_ERRATUM_2026_09.md) provides fold tables and tested replacement code without overwriting E001–E005. E004/E005 also have incomplete secondary reporting, disclosed in the audit.

E004/E005 files were committed retrospectively during this recovery, not publicly preregistered in Git before execution. Their original protocol status text is preserved as historical evidence; the archives and experiment-log addendum describe their actual status. Negative results remain visible.

### E006: registered results at 50% human review

Equal-weight five-fold means; Brier is union-label-corrected. These are retained-prediction results at a fixed review budget, not the original all-row classifier scores.

| Input / routing | Retained accuracy | MAP@3 | Risk | ECE | Brier |
|---|---:|---:|---:|---:|---:|
| Frequency reference | 0.4017 | 0.5387 | 0.5983 | 0.0569 | 0.7954 |
| Explanation / confidence | 0.4205 | 0.5430 | 0.5795 | 0.1616 | 0.8140 |
| Explanation / support-aware | 0.4374 | 0.5541 | 0.5626 | 0.1538 | 0.8035 |
| Question + explanation / confidence | 0.4469 | 0.5653 | 0.5531 | 0.1470 | 0.7799 |
| Question + explanation / support-aware | 0.4581 | 0.5710 | 0.5419 | 0.1459 | 0.7757 |

All four learned routing pairs meet the registered **relative** criterion at 50% review: at least 0.05 absolute risk reduction versus their own 0% result and lower retained risk than frequency. Calibration comparisons remain descriptive; no acceptable absolute deployment-risk threshold was defined. [The full report](docs/E006_RESULTS.md) includes every registered review budget, fold variation, calibration comparisons and confidence AUROC; the linked JSON includes the complete support-stratum grid. No deployment-readiness claim is made.

## Quick start after data approval

1. Obtain the MIT-licensed author-published `train.csv` from the source recorded in `docs/DATA_AND_LICENSES.md`, and verify its SHA-256 before use.
2. Put it at `data/raw/train.csv` (the directory is gitignored).
3. On a **new checkout only**, create the inspection report and grouped split manifests. Existing research checkouts must not regenerate frozen assignments. These are historical reproduction commands, not an instruction to start a new experiment:

```powershell
docker compose build
docker compose run --rm research python scripts/inspect_dataset.py --input data/raw/train.csv
docker compose run --rm research python scripts/make_grouped_folds.py --input data/raw/train.csv --output artifacts/splits --n-splits 5 --seed 20260831
docker compose run --rm research python -m pytest
docker compose run --rm research python scripts/run_e001.py --input data/raw/train.csv --splits artifacts/splits --output artifacts/e001_results.json
```

The fold manifest captures a SHA-256 fingerprint of the input. Do not publish that manifest or any row-level derivative: it is local-only by policy. Do not use competition test labels or derive question-level answer keys from held-out groups. The original scorer remains frozen and has a documented Brier defect; historical reproduction is not a recommendation to use it for new work.

For an existing research checkout, `python scripts/verify_frozen_inputs.py` performs read-only data/hash/order/group checks, including the assignment fingerprint recorded during this audit. See [the verification record](docs/VERIFICATION_2026_09.md) for Docker tests and environment limits. Listed dependencies are pinned, but transitive/build dependencies are not fully locked; a successful test in the existing image is **not** a fresh-build reproducibility claim.

## Layout

- `docs/` — provenance, related work, protocol, limitations, and experiment log.
- `src/map_misconceptions/` — data-contract and split-generation utilities.
- `scripts/` — explicit, reproducible data inspection and split creation entry points.
- `experiments/` — experiment configurations (not result claims).
- `artifacts/` — generated local-only artifacts (never versioned).
- `tests/` — leakage and schema-contract tests.

## Research progression

E001 established that the tested lexical baseline did not beat prevalence for the primary task. Future experiments will have their approved protocols committed before execution, use the frozen question-held-out framework, and receive distinct result commits. The non-root Docker environment mounts `data/` and `artifacts/`; raw data stays out of the image. Historical plan: [docs/RESEARCH_PLAN.md](docs/RESEARCH_PLAN.md).

E002 is complete: 21.1% of held-out rows have a label absent from their fold-local training set, while exact cross-question response overlap is only 0.59%. E003 and E005 subsequently decomposed support without replacing the primary all-row evaluation. Cross-question overlap alone does not exclude leakage within random-split questions. See [the E002 report](docs/E002_RESULTS.md).

E003 confirmed that unsupported labels are not the whole explanation: even on the supported-label subset, TF–IDF MAP@3 (0.668) remained below frequency (0.689). See [the E003 report](docs/E003_RESULTS.md).

## Live terminal monitor

During an active experiment, open a second terminal and run:

```powershell
docker compose run --rm research python scripts/monitor_experiment.py --status-file artifacts/live_status.json
```

It is read-only: it renders the active experiment ID, status, elapsed time, stage, progress, and latest aggregate metric from an ignored local status file. It never reads student responses or interrupts the run.

The legacy status file is not proof that a process is running; a completed E005 run left a stale `RUNNING` flag. Do not start a monitor when no experiment is active. Future approved runs will use a live terminal view plus at-most-hourly progress updates while active, stopping on completion/failure. No idle recurring monitor is scheduled.

## Publication and data policy

This repository contains original code, Docker configuration, protocols, aggregate results, and documentation only. It does **not** contain MAP data, raw student responses, row-level predictions, trained weights, credentials, or competition/private artifacts. The repository's code is MIT-licensed; that license does not relicense MAP data. See [the data register](docs/DATA_AND_LICENSES.md) and [publication audit](docs/PUBLICATION_AUDIT.md).

## Citation

Please cite the MAP benchmark paper and competition source recorded in [docs/DATA_AND_LICENSES.md](docs/DATA_AND_LICENSES.md). This repository is not affiliated with Eedi, Vanderbilt University, The Learning Agency, or Kaggle.
