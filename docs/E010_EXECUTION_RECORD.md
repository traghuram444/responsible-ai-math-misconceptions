# E010 authorization and execution record

## Authorization on 2026-10-13

The user authorized proceeding and starting the proposed review-prioritization experiment. The [protocol](E010_PROTOCOL.md) and `experiments/e010_review.yaml` fix the concrete evaluation choices before execution. `experiments/e010_approval.yaml` records this scope and canonical LF hashes without claiming separate user review of every new numerical choice.

E010 reuses E009 fitting/features/calibration unchanged and adds only the registered fixed-budget evaluation and hash-only control. E001–E009 scientific records remain immutable. A clean tested implementation is committed/pushed before one run in the existing audited offline/non-root Docker image. Only `artifacts/e010/` is writable during the run. No silent rerun is permitted.

Commands from the repository root:

```powershell
./scripts/run_e010_docker.ps1
./scripts/watch_e010_docker.ps1
```

The terminal viewer updates during execution and stops on completion/failure/staleness. No idle monitor or recurring automation is created. The provisional compute estimate is 25–45 minutes; reconstruction is required because E009 deliberately did not persist row-level scores or fitted models.

Full numerical results, including all folds, questions, support strata and calibration eligibility, precede interpretation. Only sanitized aggregate outputs are published in a separate results commit.

## Pre-run verification

The full offline/non-root Docker suite passed **294 tests in 50.41 seconds**, including 38 new E010 synthetic tests. These check quota arithmetic, deterministic ties/collisions, nested immutable masks, permutation invariance, label exclusion, perfect/reversed rankings, empty/error-free denominators, calibration eligibility, primary-margin boundaries, complete 360-record/1,080-question reporting, strict private-field rejection, corruption detection, historical mismatch failure and the freeze-before-correctness barrier. Existing E009 leakage and nested-training tests also passed.

Read-only preflight verified the locked protocol/configuration, original input/split fingerprints, the complete 200-record E009 reference and a 135-file preservation inventory. The audited Docker image was available without a pull/build or host change. No E010 MAP fit, timing pilot or budget evaluation occurred in these checks.

The pre-run publication scan covered 141 public files and 28,587 unique normalized student-response prefixes (40–80 characters), with zero response matches and zero secret/local-path pattern matches. Only E010 files and append-only/shared status documentation enter the pre-run commit.
