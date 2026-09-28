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
