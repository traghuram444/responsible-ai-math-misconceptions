# Responsible AI for Mathematical Misconceptions

> **Active research — not a finished system or deployment recommendation.**

Reproducible research code and documentation for the question: **can mathematical-misconception detection generalize to unseen K–12 math questions, with uncertainty-aware human review?**

The current evidence is limited to a 15-question middle-school benchmark; it is not a claim of K–12-wide validity.

## Research scope

This project uses the author-published MIT-licensed MAP (Misconception Annotation Project) training release recorded in `docs/DATA_AND_LICENSES.md`. It is not a Kaggle leaderboard replication: the primary evaluation holds out entire `QuestionId` groups. The available MAP corpus is a middle-school benchmark, not evidence for K–12-wide performance.

The primary evaluation withholds entire `QuestionId` groups, rather than randomly splitting individual responses. This asks whether a model transfers to a never-before-seen math problem, while measuring calibration and a simulated option to defer uncertain predictions for human review.

## Status

E001 is complete and preserved as a negative result:

| Evaluation | MAP@3 |
|---|---:|
| Random row split, TF–IDF + logistic regression | 0.785 |
| Question-held-out split, same model | 0.520 |
| Question-held-out frequency baseline | 0.539 |

Random validation was substantially optimistic, and the stronger lexical baseline did **not** exceed the frequency baseline under unseen-question evaluation. This negative result motivates stronger, scientifically controlled generalization research—not performance claims. No transformer has been trained. See [the full E001 report](docs/E001_RESULTS.md).

## Quick start after data approval

1. Obtain the MIT-licensed author-published `train.csv` from the source recorded in `docs/DATA_AND_LICENSES.md`, and verify its SHA-256 before use.
2. Put it at `data/raw/train.csv` (the directory is gitignored).
3. Create the auditable inspection report and grouped split manifests:

```powershell
docker compose build
docker compose run --rm research python scripts/inspect_dataset.py --input data/raw/train.csv
docker compose run --rm research python scripts/make_grouped_folds.py --input data/raw/train.csv --output artifacts/splits --n-splits 5 --seed 20260831
docker compose run --rm research python -m pytest
docker compose run --rm research python scripts/run_e001.py --input data/raw/train.csv --splits artifacts/splits --output artifacts/e001_results.json
```

The fold manifest captures a SHA-256 fingerprint of the input. Do not publish that manifest or any row-level derivative: it is local-only by policy. Do not use competition test labels or derive question-level answer keys from held-out groups.

## Layout

- `docs/` — provenance, related work, protocol, limitations, and experiment log.
- `src/map_misconceptions/` — data-contract and split-generation utilities.
- `scripts/` — explicit, reproducible data inspection and split creation entry points.
- `experiments/` — experiment configurations (not result claims).
- `artifacts/` — generated local-only artifacts (never versioned).
- `tests/` — leakage and schema-contract tests.

## Research progression

E001 established that a lexical baseline is not adequate for the primary task. Future experiments will be preregistered in the experiment log, evaluated on the same frozen question-held-out protocol, and committed as distinct research milestones. The non-root Docker image has pinned dependencies and mounts `data/` and `artifacts/`; raw data stays out of the image. Full protocol: [docs/RESEARCH_PLAN.md](docs/RESEARCH_PLAN.md).

## Publication and data policy

This repository contains original code, Docker configuration, protocols, aggregate results, and documentation only. It does **not** contain MAP data, raw student responses, row-level predictions, trained weights, credentials, or competition/private artifacts. The repository's code is MIT-licensed; that license does not relicense MAP data. See [the data register](docs/DATA_AND_LICENSES.md) and [publication audit](docs/PUBLICATION_AUDIT.md).

## Citation

Please cite the MAP benchmark paper and competition source recorded in [docs/DATA_AND_LICENSES.md](docs/DATA_AND_LICENSES.md). This repository is not affiliated with Eedi, Vanderbilt University, The Learning Agency, or Kaggle.
