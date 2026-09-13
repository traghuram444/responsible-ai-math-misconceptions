# Recovery verification — 2026-09-13

This verifies project maintenance, not a new scientific experiment. E006 is not running. Changes are confined to this repository and its personal GitHub remote; no global packages, host settings, other projects, or recurring automations were changed.

## Docker and tests

Checks used the existing project image `map-misconceptions:e001`:

`sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c`

Measured runtime: Python 3.11.11; UID/GID **10001/10001**. Core packages: NumPy 1.26.4, pandas 2.2.3, SciPy 1.14.1, scikit-learn 1.5.2, pytest 8.3.4, sentence-transformers 3.3.1, transformers 4.46.3, torch 2.5.1. No encoder or new classifier was run. Torch's installed dependencies include CUDA packages despite the historical E004 runner selecting CPU.

The test environment had networking disabled, a read-only root filesystem and project mount, an ephemeral `/tmp`, and bytecode/cache writing disabled. PowerShell command from the project root:

```powershell
docker run --rm --network none --read-only --tmpfs /tmp:rw,nosuid,nodev --user 10001:10001 -e PYTHONDONTWRITEBYTECODE=1 -v "${PWD}:/workspace:ro" -w /workspace map-misconceptions:e001 python -m pytest -q -p no:cacheprovider
```

The final full suite passed **27 tests in 2.87 seconds**. Tests cover the original synthetic E001 pipeline; union-label Brier's missing-unit regression, probability validation and cancellation limits; frozen-assignment validation against reordering, mismatched questions/targets, invalid roles, group leakage, and repeated evaluation; and seven E006 proposal-contract checks for its unapproved status, fixed values, explicit decision rule, correction fields, reproduction gate, and absence of automatic execution. Test duration is not an E006 runtime estimate.

This does **not** claim a fresh image build or a bitwise-reproducible environment. Current dependencies are only partially locked; build/transitive dependencies remain a documented limitation. Do not substitute a package upgrade during an experiment to improve results. Historical Docker files and dependency declarations were preserved in this recovery.

## Data and split integrity

`python scripts/verify_frozen_inputs.py` passed inside the same network-disabled, read-only container:

- The data and manifest SHA-256 values match the registered study.
- 36,696 rows and 15 questions match the manifest.
- Ordered source positions, QuestionId values and target labels match the input.
- Every question belongs to exactly one role per fold; every row is evaluated once.
- In-memory deterministic reconstruction matches all existing assignment columns. No split or manifest was written.

The current assignment SHA-256 is `b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd`. This audit-time lock cannot independently prove the original file's historical identity. Raw data and assignments remain ignored and unpublished.

## Aggregate recovery and correction

`scripts/archive_completed_results.py` deterministically exports allowlisted aggregate fields from the original E004 and final E005 artifacts. Byte-identical archive reproduction passed with a read-only mount. The exporter rejects nonnumeric metric values, unknown variants/IDs, inconsistent counts, and attempts to overwrite differing outputs. Injected unrelated private-string fields were excluded by its allowlist. No new model, bootstrap draw, or permutation was computed.

`scripts/audit_brier_aggregates.py` checked all **200** comparable E001/E005 overall scalar metrics to absolute tolerance `1e-12` and checked the E004 frequency reference. It generated a separately named arithmetic erratum containing 20 five-fold aggregate records; historical artifacts were not replaced. This is a bug correction, not a new hypothesis test.

The historical source/artifact fingerprints were recorded before maintenance and rechecked before publication. E001–E005 data, folds, source metrics, runners, protocols and original result artifacts remain unchanged. Existing E004/E005 files entered Git after execution, disclosed as retrospective records.

## Publication checks

Publication review covers the prospective tracked files, not ignored data/caches. Automated checks look for forbidden data/model/archive extensions and directories, private-key blocks, common GitHub/API/cloud token patterns, credential assignments, and user-specific machine paths. Existing history is separately checked for forbidden data/artifact paths. All generated tables are allowlisted numeric aggregates plus aggregate QuestionId values and hashes.

A local exact-text check compared whitespace-normalized, case-folded prefixes of **29,427** student explanations (those at least 40 characters; up to 80 characters checked) against the proposed public text. It found **zero matches**. This test does not cover every short explanation, arbitrary paraphrases, or every possible secret format; it complements source review and strict export allowlists, not a proof of universal detection. Student text and matched substrings are never printed or written by the check.

The initial publication scan found zero token/path findings, zero forbidden candidate files, and zero forbidden historical paths. `git diff --check` passed. Final staged verification and commit identifiers are reported with the publication handoff; Git timestamps are not backdated.

## Outstanding research gates

- The E006 addendum remains proposed and must be reviewed before execution.
- No historical E004/E005 missing secondary analyses were filled or relabeled complete.
- No positive result, automation readiness, or first-of-kind novelty is claimed.
- No experiment is active. Do not launch a monitor from the stale legacy status file. Future approved active runs should show terminal status and hourly progress, ending on completion/failure.
