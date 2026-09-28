# E008 approval and execution record

## Approval — 2026-09-28

The user explicitly approved the detailed E008 protocol. The historical proposal remains unchanged; `experiments/e008_approval.yaml` records the approval and canonical LF protocol/configuration hashes. This record supersedes the proposal's historical pending-review status without rewriting it.

Scope: development-only reconstruction of E007, fixed constraint diagnostics, individual/shared cutoff feasibility and count-based oracle bounds. No current-fold outer evaluation predictions, new classifier, changed floor/target, or new subgroup analysis is authorized. E001–E007 scientific history is preserved.

Implementation and synthetic verification precede a dedicated Git commit/push. The full run uses that clean revision in the existing audited Docker image, UID/GID 10001, no network, read-only source/data and only `artifacts/e008/` writable. The runner refuses to overwrite or silently retry a recorded attempt.

Execution commands (project root):

```powershell
./scripts/run_e008_docker.ps1
./scripts/watch_e008_docker.ps1
```

The terminal viewer reads only active-run status, uses bounded retries and stops at completion/failure/staleness. No idle recurring monitor; notifications at most hourly while active, plus completion/failure or required intervention. Diagnostic progress reports verified fold-arms and reproduced policies, not invented classifier metrics.

Results must pass the strict scalar/count allowlist, full-grid/count/oracle arithmetic checks, preserved-file hashes and publication privacy scan. A separate results commit follows verification. Results are presented before interpretation or another experiment proposal.

## Pre-run verification

The existing non-root, offline Docker image passed **219 tests** in 15.84 seconds, including synthetic E008 oracle enumeration, exact boundaries, disconnected feasible sets, exhaustive score/minimax comparisons, development-only prediction-role guards, reproduction gates, publication rejection and viewer retry tests. An initial synthetic assertion demanded bit-exact zero SD and was corrected for floating-point arithmetic noise; no experimental tolerance or decision rule changed. No E008 MAP computation occurred during testing.

Preflight verified all 10 E007 development records, frozen input fingerprints and a 95-file preservation inventory. A read-only publication scan covered 110 files against 28,587 unique normalized student-response prefixes (40–80 characters), with zero response matches and zero secret/local-path matches.

## Completed execution — 2026-09-28

- Pre-run public revision: `ec4ed262bb8d63a0ad8bd38e6142ca8b28cbcf33`, verified on personal repository `traghuram444/responsible-ai-math-misconceptions` before launch.
- One run completed in 535.172 seconds through result construction (535.364 seconds through final status), with 100 fitting calls and zero outer-evaluation prediction calls.
- All 10 development reconstruction gates passed, including all 90 rule/target policy records. No tolerances, targets, floors, question roles, score rules or analysis definitions changed during execution.
- Docker runtime inspection confirmed the locked image, UID/GID 10001, no network, read-only root/project and only the intended E008 artifact bind writable. No packages or models were downloaded.
- All 95 pre-run historical file fingerprints were unchanged. Independent verification checked 270 constraint partitions, 1,782 numerical fold summaries and all development references with zero discrepancies.
- The read-only terminal viewer remained active through completion and exited with code 0. The experiment also exited with code 0. No monitor read failure was observed; no recurring idle monitor remains.
- Full results are in [E008_RESULTS.md](E008_RESULTS.md) and [E008_aggregates.json](../results/E008_aggregates.json). Only counts, flags, scalar witnesses, descriptive summaries and provenance are exported. No fitted models, candidate arrays, source question identifiers, student text or row-level predictions are serialized.

The result is retained as computed. Outcome counts and full numerical tables are published before interpretation; the next research step is not authorized by this execution record.

## Final publication checks

The final Docker regression suite passed **219 tests** in 14.12 seconds. Read-only regeneration matched both published files exactly. The publication scan covered 112 files against 28,587 normalized student-response prefixes: zero response matches and zero secret/local-path matches. No restricted data, cache or model artifact is tracked. The E008 runtime container and terminal viewer have exited; no idle monitor remains.

SHA-256 of the aggregate artifact and its identical public JSON: `966e775a74f5d15fa0f2c253ee7a06f1bec9ab34cbf4812ae4d6a5f2180973ea`.

SHA-256 of the generated full report: `e0eb9a6da10b9e9a321abcd7f41bd150739caaa8b2055427140ca81e70590b8c`.
