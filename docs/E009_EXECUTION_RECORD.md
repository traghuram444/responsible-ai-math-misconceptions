# E009 approval and execution record

## Approval — 2026-09-28

The user explicitly approved the complete E009 specification. The historical [protocol proposal](E009_PROTOCOL.md) remains unchanged; `experiments/e009_approval.yaml` records its approval and canonical LF protocol/configuration hashes. This record supersedes the proposal's historical pending-review status without rewriting it.

E009 adds only the registered nested question-held-out reliability learner and raw-confidence control. The final misconception classifier, frozen outer folds, original temperature/threshold roles, targets, count/coverage floors and all-question criterion remain unchanged. No feature/hyperparameter search or router calibration is authorized.

Synthetic verification, privacy scans and a clean implementation commit/push precede MAP execution. A single approved run uses the audited non-root/offline Docker image with read-only source/data and only `artifacts/e009/` writable. Existing attempts cannot be overwritten or silently repeated. All policies are serialized before evaluation correctness is read.

Commands, from the project root:

```powershell
./scripts/run_e009_docker.ps1
./scripts/watch_e009_docker.ps1
```

The read-only terminal viewer uses bounded status-read retries and stops when the run completes, fails or becomes stale. Progress counts completed fitting/feature/policy/evaluation work, not a time estimate. At-most-hourly notifications while active, plus completion/failure or required intervention; no idle recurring monitor.

After completion, results require full-grid, historical reproduction, arithmetic, preservation and publication checks. Only approved aggregate artifacts are published, in a separate result commit. Full numerical tables precede interpretation or any next-experiment proposal.

## Pre-run verification

The offline, non-root Docker regression suite passed **256 tests** in 23.14 seconds. E009 tests use invented examples only and cover nested tuning/vectorizer exclusions, exact cross-fit assignment, feature boundaries and training-only similarity, weighted scaler/model equivalence, constant fallbacks, convergence failure, evaluation-label and query-batch invariance, unsupported errors, eligibility/null behavior, complete 200-record/600-question export, private-field rejection, tamper detection, reproduction tolerances and the freeze-before-correctness barrier.

Preflight verified the locked E009 documents, unchanged E007/E008 approvals and reference fingerprints, all frozen input fingerprints, 120 historical evaluation-reference records and a 114-file preservation inventory. No E009 MAP model fit or feature computation occurred during these checks. The existing audited Docker image is available; no package/model download or host configuration change was needed.

The pre-run publication scan covered 126 public files and 28,587 unique normalized student-response prefixes (40–80 characters), finding zero response matches and zero secret/local-path matches. Only E009 files and append-only/shared status documentation are included in the implementation commit.

## Completed run — 2026-09-28

The single approved run used pre-run revision `c2dd478d3a857287ba8fcc6563fc2b64ad1cb496`, verified publicly before launch. It completed in 1,547.299 seconds through result construction (1,547.745 seconds through final heartbeat), with exit code 0. Runtime isolation was checked: UID/GID 10001, network disabled, read-only root/source/data, and only the new E009 artifact directory writable. The image was `sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c`; no dependency download or host configuration change occurred.

All 400 classifier fits succeeded with zero warnings, including zero convergence warnings. All 10 reliability fits succeeded without constant fallbacks. All policies were frozen before evaluation correctness was read. All 90 historical development policies and 120 E007 evaluation records reproduced under the original exact-discrete/absolute-1e-10 numerical gates. All 114 preservation fingerprints matched after execution.

The terminal viewer received live heartbeats, reached COMPLETED and exited normally with code 0. No monitor read interruption was observed. No experiment or idle monitor remains active.

At each target (10%, 20%, 30%), every arm/rule has zero admissible development cutoffs, zero retained evaluation rows and undefined retained metrics. The registered primary criterion is unmet. Complete secondary ranking and calibration values appear in the [numerical report](E009_RESULTS.md) and [JSON](../results/E009_aggregates.json). Interpretation remains deferred until user review.

## Post-run verification

An independent read-only Docker audit recomputed count/risk/coverage partitions, metric eligibility, fold means/sample SDs, paired differences and registered criteria from the serialized records. It checked 4,000 classifier groups, 800 reliability groups and 3,104 numerical fold summaries, independently reproduced all 120 historical evaluation records and rechecked all 114 preserved-file hashes: **zero discrepancies**. This checks aggregate arithmetic and historical reproduction, not a second experimental run.

The full offline/non-root Docker regression suite passed **256 tests in 23.07 seconds**. The strict exporter validated the full grid and generated 200 fold/policy records, 600 evaluation-question records and the separate ranking/calibration tables. It rejects unregistered fields and does not export response text, prediction arrays, candidate arrays or fitted parameters.

Published numerical artifact fingerprints (SHA-256):

| Artifact | SHA-256 |
|---|---|
| `results/E009_aggregates.json` | `f0aecdff883f9a26facb8a9678a1079a54814c793353e9b52d8c00b38fb75a5b` |
| `docs/E009_RESULTS.md` | `becd378ae9b86cb3660d48b49a3c7a683edccccbc2c4ae3f46d4aa1cdc1690ee` |
| Local frozen policies | `d6ce9cc3e5ab059cfdd65721ef85e49cbc7dcefc410906cc46661fab7ae0f5bf` |

No protocol amendment, retry, classifier change, threshold relaxation or unregistered analysis occurred. Results are reported before interpretation or another experiment.

Publication checks covered 128 public files against 28,587 unique normalized student-response prefixes (40–80 characters): zero response matches and zero secret/local-path pattern matches. The tracked-path audit found no raw data, private artifacts, model weights or caches. The generated report and JSON reproduced exactly with all Docker mounts read-only. E009's approved protocol and configuration hashes remain unchanged. Only the aggregate report/JSON and shared status/execution documentation are included in the separate results commit.
