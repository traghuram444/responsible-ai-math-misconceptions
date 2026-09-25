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
