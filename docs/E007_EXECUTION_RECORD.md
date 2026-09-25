# E007 approval and execution record

## Authorization — 2026-09-25

The user approved the proposed calibration split and risk/coverage criteria after reviewing the E007 proposal. The original draft text/status is preserved; the separate [approval registry](../experiments/e007_approval.yaml) supersedes its authorization status without changing its scientific content.

- Protocol canonical UTF-8/LF SHA-256: `699a3e5691a2bf41bd27311e11f94f548aaff5466e497167ed702196ea21676e`.
- Configuration canonical UTF-8/LF SHA-256: `815142c1b25fb6edd0859f971bdda3e955f56b91b9998420606146a165b5d630`.
- All E001–E006 history remains preserved. E007 changes only the approved subdivision of the existing calibration role and the abstention policy/evaluation.

Implementation uses two phases: fit models and select every development cutoff, write aggregate-only frozen policies, then begin evaluation metrics. Development selection includes unsupported true labels as errors. No row-level predictions, responses, fitted weights, or rankings are saved.

## Execution commands

After pre-run synthetic tests and a clean committed implementation:

```powershell
./scripts/run_e007_docker.ps1
./scripts/watch_e007_docker.ps1
```

The launcher requires the existing audited image, non-root UID/GID 10001, no network, a read-only project mount, and only `artifacts/e007/` writable. It does not build/pull images, install software, or change host settings. It refuses existing attempts. The read-only monitor exits at completion/failure/stale state; it does not interrupt fitting.

This entry records approval and implementation only. Test and execution evidence will be appended separately; it is not a result claim.

## Pre-run verification — 2026-09-25

The full suite passed **176 tests in 14.11 seconds** in the existing audited Docker image, with networking disabled, UID/GID 10001, read-only project/root filesystem, bytecode and pytest cache disabled, and ephemeral temporary storage. This includes 61 E007-specific synthetic tests; no MAP classifier was fitted by these tests.

Checks include an independent exhaustive cutoff-search oracle over tied/nonmonotone synthetic scores; exact rational error boundaries; per-question count/coverage floors; deterministic question-role assignment; separate temperature/selection questions; unsupported-label errors; unchanged decisions under evaluation-label/batch changes; all-deferral null metrics; complete fold/question reporting; historical rank/hyperparameter gates; approved-document hash validation; and rejection of private-field injection or altered aggregate values. A source-order check additionally confirms that the all-fold policy serialization barrier precedes evaluation calls.

Pre-run file-extension, credential-pattern and machine-path scans found no prohibited candidates; `git diff --check` and PowerShell launcher parsing passed. These pattern checks supplement, not replace, the strict aggregate export schema. The protocol and configuration hashes remain exactly those approved above. The existing image identity was verified; no environment installation or configuration changes were made.

## Completed run — 2026-09-25

- Execution revision: `b3a0a59f9c2e2226fd1a454eb438cf50c767b92f`, verified publicly on the personal repository before launch.
- Start: 18:35:40 UTC. Completion heartbeat: 18:44:51 UTC. Artifact runtime: **550.641 seconds**; final status runtime: **550.914 seconds**.
- Runtime inspection confirmed UID/GID 10001, no networking, read-only root/project, and only the new E007 output mount writable. The image identity matched the approved configuration. No unrelated containers or host configuration were modified.
- Exactly 100 classifier fitting calls completed. Every development cutoff was serialized before evaluation scoring. All 40 historical top-1/MAP@3 checks passed, and selected hyperparameters matched. No protocol adjustment or rerun occurred.
- Frozen policy SHA-256: `4dce8d85cf66330cc5a131788555b51516b414cccb6ece9c6fd4c275da81950a`.
- Original local and sanitized public result JSON SHA-256: `a0184aba0ac0649569efa56b42d248ebec466a40a6c44c615d2369587c9d3ff7`. They are byte-identical because the original artifact already satisfies the strict aggregate-only schema.
- Generated report SHA-256: `b8b5080beb2e8e79a88d4e0c35fe199634f06503f96feb6d73949351fe361d08`.

All 90 fold/arm/rule/target policy-selection records (including the frequency baseline duplicated across input arms) have `NO_ADMISSIBLE_THRESHOLD`. Consequently every selected set is empty at every target; risk, accuracy, MAP@3, ECE and Brier are null, never zero-valued performance. The unfiltered references and full question/support grid are retained. These are recorded numerical outcomes, not an interpretation or next-experiment proposal.

An independent read-only verifier, using count identities and standard-library statistics rather than the experiment's aggregation function, checked **2,400 metric groups**, **1,680 aggregate summaries**, calibration eligibility/ranges, support partitions, paired-summary denominators, frozen policy hash, and **42 preserved historical-file hashes**, with zero discrepancies. The strict publication validator additionally checked the full registered grid, question/fold totals, calibration nulls, development policy consistency, reproduction checks and aggregate recomputation.

### Monitor incident and post-run repair

The live terminal viewer exited after a missing-status-file read; its last displayed running snapshot was around 6 minutes 24 seconds. The precise cause of that read failure was not established. The independent experiment heartbeat continued through completion, and fitting was unaffected. It would be inaccurate to claim uninterrupted terminal monitoring for this run.

After completion, an E007-specific viewer was added with three bounded read attempts and 0.2-second delays for transient missing/invalid reads. It still exits on terminal/stale state and does not create idle monitoring or control the experiment. The historical E006 viewer/heartbeat module and all scientific E007 code remain unchanged. Six additional synthetic tests cover transient errors, persistent absence and terminal state. **182 tests passed in 13.95 seconds** in the same isolated Docker environment after this viewer-only change.

During execution, a read-only privacy audit checked 28,587 distinct case-folded, whitespace-normalized response prefixes (40–80 characters) against 89 publication files and found zero matches. This is not a guarantee against short or paraphrased disclosures; strict schema export and manual scope review are the primary safeguards. Final publication checks are recorded below when complete.

## Final publication verification

The final privacy scan included **94 public files**, including the generated E007 JSON/report and post-run viewer repair: **zero response-prefix matches** across the same 28,587 prefixes, and **zero credential-token or machine-path findings**. An inefficient first audit invocation was stopped and replaced with an equivalent read-only scan that normalizes each file once; no experiment was stopped or rerun and no artifact changed.

The publication exporter was rerun with the entire project read-only and reproduced both generated files exactly. `git diff --check` passed. All E007 scientific code, tests, protocol, configuration and approval files are unchanged from execution revision `b3a0a59`; only the separate monitor-viewer repair changed after the run, committed as `94f243d`. The completed monitor snapshot was read once and exited; no E007 container or idle monitor remains. Only sanitized documentation and aggregate results are included in the result commit.
