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
