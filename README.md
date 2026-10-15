# Responsible AI for Mathematical Misconceptions

**Active research · E013 complete · Prior experiments preserved · Not deployment-ready**

**Research question:** Can mathematical-misconception detection generalize to unseen K–12 math questions, with uncertainty-aware human review?

This independent project tests that question on **36,696 responses to 15 middle-school math questions** from the author-published MAP release. It is a reproducible generalization and selective-prediction study, not a leaderboard solution or evidence of K–12-wide validity.

[Research report](docs/RESEARCH_REPORT.md) · [Experiment index](docs/EXPERIMENT_INDEX.md) · [Reproduce the checks](docs/REPRODUCTION.md) · [Release audit](docs/RELEASE_AUDIT_2026_10.md)

## Main findings

![E001 MAP@3: random response split 0.785, held-question TF-IDF 0.520, held-question frequency 0.539.](docs/figures/generalization.svg)

- **Random validation is optimistic.** TF–IDF + logistic regression reaches MAP@3 **0.785** on random response splits but **0.520** on held-out questions, below the **0.539** frequency baseline. Frozen MiniLM embeddings also fail to beat frequency.
- **Unavailable labels explain only part of the difficulty.** 21.1% of held-question responses have an exact label absent from training. Even among supported labels, TF–IDF MAP@3 is **0.668**, versus **0.689** for frequency.
- **Better ranking does not establish reliable automation.** E009's learned reliability score improves explanation-only correctness AUROC to **0.695**, but no admissible development cutoff meets the registered per-question requirements. All cases are deferred.
- **Review prioritization remains a negative primary result.** At E010's 20% review budget, learned routing improves on support-aware routing by **1.387 ± 0.828** fewer remaining errors per 100 responses for explanation-only and **0.279 ± 1.098** for question + explanation. Neither meets the preregistered criterion. Retained error rates remain **59.3%** and **58.8%**.

Means and sample SDs describe five folds, not independent inferential evidence. Deferred errors are **not** assumed corrected by a human. Both input arms, all registered budgets, all questions and negative results remain published.

## What this repository contributes

Frozen question-held-out evaluation; nested model selection; group-disjoint calibration; exact-label support diagnostics; comparison of confidence, support-aware and cross-fitted reliability routing; simulated fixed-budget review; and an auditable history of negative results. It does **not** introduce a new classifier architecture or claim priority for unseen-question diagnosis or selective prediction. See the [literature and interpretation review](docs/RESEARCH_REVIEW_2026_09.md).

## Verify without student data

Requires Git and Docker with Linux containers. The verification environment is CPU-only, Linux amd64, non-root and hash-locked. Run from a checkout root:

```powershell
docker build --platform linux/amd64 --pull --no-cache -t map-research-verify:2026-10 -f repro/Dockerfile repro
docker run --rm --network none --read-only --tmpfs /tmp:rw,nosuid,nodev --user 10001:10001 --cap-drop ALL --security-opt no-new-privileges --mount "type=bind,source=$($PWD.Path),target=/workspace,readonly" map-research-verify:2026-10
```

This runs synthetic regression tests, historical-preservation checks, public aggregate validators and deterministic figure checks. It does **not** download MAP, fit research models or reproduce their predictions. [Detailed commands and modeling-reproduction limits](docs/REPRODUCTION.md).

CI applies publication checks to the public checkout and runs the same offline verification. The original modeling Dockerfile, dependencies and experiment launchers remain unchanged; they are not a fully hash-locked fresh reproduction of every historical model.

## Research history and limitations

Start with the [experiment index](docs/EXPERIMENT_INDEX.md), then follow each protocol, execution record and complete result table. The [experiment log](docs/EXPERIMENT_LOG.md) is append-only. E001–E010 scientific records are preserved by a [checksum inventory](repro/history.json).

Only 15 questions underpin this repeatedly examined benchmark. Calibration-question roles differ between E006 and E007 onward. E004/E005 were archived retrospectively, not publicly preregistered in Git before execution, and have incomplete secondary reporting. A [Brier-score erratum](docs/METRIC_ERRATUM_2026_09.md) corrects a legacy unseen-label bug without rewriting the old results. These limits are part of the findings, not hidden exceptions.

[E011: selected-answer-context ablation](docs/E011_PROTOCOL.md) is complete under the original frozen E001 question roles. Full-context word TF–IDF/logistic MAP@3 is **0.511887**, versus **0.519971** for question + explanation and **0.539215** for frequency. Its mean delta versus frequency is **−0.027328 ± 0.056586**, positive in 2/5 folds; its fixed primary criterion is unmet. Mean ECE is **0.149626**, versus **0.108524** and **0.056271** respectively (lower is better). [Complete E011 results](docs/E011_RESULTS.md).

This valid negative triggered the previously registered [E012](docs/E012_PROTOCOL.md): character TF–IDF + Complement Naive Bayes on full context, without changing folds or calibration. **The first E012 attempt stopped with a PermissionError after 49/95 fits, before evaluation.** Its [failure record and diagnosis](docs/E012_EXECUTION_FAILURE.md) remain unchanged. The approved [infrastructure-only second attempt](docs/E012_ATTEMPT02_AMENDMENT.md) completed with the original scientific runner byte-for-byte unchanged and a separate output directory.

E012 MAP@3 is **0.537228**, versus frequency **0.539215**: delta **−0.001987 ± 0.003825**, positive in **2/5 folds**. Versus E011 full context, the delta is **+0.025341 ± 0.057834**, positive in **3/5 folds**. The fixed primary criterion is unmet. Mean ECE is **0.377470** (frequency **0.056271**), and corrected Brier is **0.985662** (frequency **0.795057**); both are worse. [Full E012 results](docs/E012_RESULTS.md) · [Second-attempt execution and preservation record](docs/E012_ATTEMPT02_EXECUTION.md).

[E013: response-evidence diagnostic](docs/E013_PROTOCOL.md) reconstructed the unchanged E011/E012 full-context models with the frozen folds and 100 label-blind shuffles per intervention. Original / explanation-shuffled / answer–explanation-pair-shuffled MAP@3 is **0.511887 / 0.485204 / 0.465728** for E011, **0.537228 / 0.536613 / 0.536338** for E012, and **0.539215 / 0.539215 / 0.539215** for frequency. The registered explanation delta is **0.026683 ± 0.006820** for E011 (5/5 positive; criterion met) and **0.000616 ± 0.000797** for E012 (4/5 positive; criterion unmet). These are original-minus-shuffled differences, not improvements over frequency. [Complete numerical tables](docs/E013_RESULTS.md) · [Aggregate-only artifact](results/E013_aggregates.json) · [Execution record](docs/E013_EXECUTION.md). Interpretation is deferred for review.

No experiment or monitor remains active. These are descriptive follow-up studies on repeatedly examined questions, not independent confirmation. E001–E012, their failed/completed attempts, and the frozen folds remain unchanged. No E014 has been started.

Terminal monitoring is used only during active runs, with at-most-hourly scheduled progress updates; no idle monitor is scheduled. E013 uses `python scripts/monitor_e013.py` in the project environment to view status, elapsed time, completed work and the latest available aggregate metric. Its viewer exits on completion/failure or stale status. E012's retry viewer remains `scripts/monitor_e012_attempt02.py`; the legacy E012 viewer points to the preserved failed attempt. E013 held-out scoring starts only after all models and shuffle mappings are frozen and historical reproduction passes.

## Data, privacy and citation

Data provenance and the author-release license are recorded in [DATA_AND_LICENSES.md](docs/DATA_AND_LICENSES.md). Obtain data only from that author-published source; the closed competition and unrelated reuploads are not substitutes. The repository includes **no raw student responses, dataset archives, row-level predictions, fitted models or credentials**. Raw data and local artifacts stay ignored. The repository's MIT code license does not relicense third-party data.

Repository citation metadata is in [CITATION.cff](CITATION.cff). Also cite [Rittle-Johnson et al., *Detecting Math Misconceptions: An AI Benchmark Dataset* (2025)](https://aclanthology.org/2025.aimecon-wip.3/) and the author-published release when using MAP. This project is not affiliated with Eedi, Vanderbilt University, The Learning Agency or Kaggle.
