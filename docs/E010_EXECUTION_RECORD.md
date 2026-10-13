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

## Completed run on 2026-10-13

The single run used pre-run revision `af2efb703fd93cebd77ea17da45bea6147a30be4`, verified publicly before launch. It completed with code 0 in 1,668.158 seconds through result construction and 1,669.264 seconds through final heartbeat. Runtime inspection confirmed UID/GID 10001, no network, a read-only root/project/data mount, and only `artifacts/e010/` writable. No package/model download, host setting change or unrelated-project mutation occurred.

All 400 classifier fits and 10 reliability fits succeeded, with zero classifier warnings/failures and zero router constant fallbacks. All 360 batch masks were fixed before evaluation correctness. Complete E009 reproduction passed: 10 development records, 200 evaluation records and 50 ranking records, exact discrete matches and absolute 1e-10 numerical tolerance. All 135 preservation fingerprints matched.

At 20% review, the explanation-only mean primary benefit is 1.386828 ± 0.828494 remaining errors per 100 original responses, with positive benefit in 5/5 folds. The question-plus-explanation benefit is 0.278608 ± 1.097948, positive in 2/5 folds. Both preregistered primary criteria are unmet. The [complete numerical report](E010_RESULTS.md) and [JSON](../results/E010_aggregates.json) preserve every secondary result without changing that decision. Interpretation remains deferred.

The terminal viewer reached COMPLETED and exited normally with code 0. No read interruption was observed. No active experiment, idle monitor or recurring automation remains.

## Post-run verification

An independent read-only Docker audit recomputed review/retention/error count partitions, all ratio denominators, metric eligibility, per-question partitions, fold means/sample SDs, paired differences and primary decisions from the serialized records. It checked 7,200 classifier groups, 1,200 reliability groups and 8,482 fold summaries, independently matched 60 unfiltered references (including the hash-only duplicate), and verified all 135 preserved-file hashes: **zero discrepancies**. This is arithmetic/reference verification, not a second experiment.

The full post-run offline/non-root Docker suite passed **294 tests in 50.38 seconds**. The strict exporter validated the complete registered grid before creating the aggregate JSON and numerical report.

Published numerical artifact fingerprints (SHA-256):

| Artifact | SHA-256 |
|---|---|
| `results/E010_aggregates.json` | `a42b6640993d95030efa3df3cfc8c1250a462911c44cab4a87ab6e88c1f32e07` |
| `docs/E010_RESULTS.md` | `5c137a0b8754349d7218dad82661aa806207dede3f2a651f0dac6b3d3ee40917` |
| Local frozen plan | `4aa07c4d8eb4e0268b723acc9b04c5634a64ead595c230de1c7493a6ea8ca913` |

No retry, threshold/budget change, model substitution, revised primary margin or unregistered analysis occurred. Only aggregate outputs and shared status/execution documentation enter the separate results commit.

The final publication scan covered 143 public files and 28,587 unique normalized student-response prefixes (40–80 characters): zero response matches and zero secret/local-path pattern matches. The tracked-path check found no raw data, private artifacts, weights or caches. The report and JSON reproduced exactly with every Docker mount read-only; protocol/configuration hashes are unchanged. The experiment container and terminal viewer both stopped after completion.
