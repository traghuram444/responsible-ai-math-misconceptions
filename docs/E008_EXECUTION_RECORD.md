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
