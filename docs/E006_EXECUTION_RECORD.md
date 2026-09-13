# E006 approval and execution record

## Approval — 2026-09-13

The user explicitly approved the [clarified E006 protocol](E006_REVIEW_ADDENDUM.md) after its publication at commit `9c6962f8a3795342cd362f3201a1744c4fc39f3d`. The original proposal and addendum remain byte-preserved, including their historical proposed-status text. [The approval registry](../experiments/e006_approval.yaml) records current authorization and locks the exact approved Markdown/configuration using SHA-256 of UTF-8 text with CRLF normalized to LF. No scientific setting is changed by the approval registry.

Execution is limited to E006. Preserve E001–E005. No new representation, classifier, support cutoff, split, tuning/calibration rule, review budget, or interpretation rule is authorized. Report numerical aggregate and fold results before interpretation or any next-experiment proposal.

## Implementation plan locked before execution

- Reuse the original E001 fitting, inner selection and temperature functions unchanged. A progress-only wrapper may count fitting calls without altering their arguments or returned models.
- Reproduce all-row MAP@3, accuracy and ten-bin ECE within `1e-10` for every fold/model before evaluating its routing rules; any mismatch stops the run.
- Fit ten outer models (two input arms × five folds), each with nine original inner fitting calls and one final fitting call. The live monitor counts **100 fitting calls**, not student examples; routing/finalization are separately named stages.
- Store probabilities, true labels and rankings in process memory only. Serialize only aggregate counts/metrics, known protocol identifiers, reproducibility comparisons and environment/code fingerprints.
- Run in the existing non-root Docker image, with networking disabled and project/data/legacy artifacts read-only. Only the new `artifacts/e006/` output directory is writable; temporary process files use an ephemeral `/tmp`.
- Use a separate heartbeat status file `artifacts/e006/live_status.json`; terminal rendering is read-only. Finish/failure closes the monitor. No idle recurring monitor is created; progress notifications are hourly only if the actual run lasts that long, with immediate completion/failure reporting.
- No empirical runtime estimate exists yet. Record wall-clock runtime from the approved full run; do not tune the experiment to a runtime target.

The implementation and synthetic tests will be committed before any E006 scientific evaluation. Historical image/dependency limitations from the [audit](REPRODUCIBILITY_AUDIT_2026_09.md) still apply; this execution does not silently upgrade the environment or claim a fresh dependency-locked image build.

## Reproduction commands

From this project's root in PowerShell, the explicit full-run launcher is:

```powershell
./scripts/run_e006_docker.ps1
```

It requires a clean committed worktree and the exact previously inspected image. It neither builds nor pulls. An attempt marker, result, failure, or existing named E006 container prevents accidental duplicate execution. The marker and all outputs are confined to the new E006 directory.

While that process is active, a second terminal can display the read-only monitor:

```powershell
./scripts/watch_e006_docker.ps1
```

The monitor stops for absent, stale, completed, or failed state. Stopping the view does not terminate the experiment. Heartbeats refresh elapsed time but never invent completed work.

After completion, `python scripts/publish_e006_results.py` validates the complete registered grid and strictly allowlists aggregate values into `results/E006_aggregates.json` and `docs/E006_RESULTS.md`. It never copies arbitrary source fields or overwrites a different existing result. This publishing step does not fit a model or select a new analysis.

## Pre-run implementation verification — 2026-09-13

The complete suite passed **115 tests in 8.81 seconds** in the existing Docker image with networking disabled, non-root UID/GID 10001, the project read-only, pytest cache disabled and an ephemeral temporary directory. Both synthetic input arms reproduced the exact E001 selection/calibration functions, and tests verified that both baseline and learned reproduction gates precede routing. Tests also cover absolute-only tolerance, JSON-safe failures, hashed ties, support counts, fixed-budget selection, eligible-fold calibration pairing, AND-gated criteria, heartbeat behavior, and rejection/removal of injected private fields during publication.

No MAP model was fitted during these pre-run tests. Code and this record are committed before the full-run launcher. Git revision, input/code hashes, actual wall time and all 60 reproduction comparisons will be included in the completed artifact; a failed gate instead yields a clearly marked partial failure record.
