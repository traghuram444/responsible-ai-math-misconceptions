# E012 operational failure — not an evaluated model result

The preregistered conditional run started after E011's valid negative result was published. It stopped before held-out evaluation. **There is no E012 MAP@3, calibration comparison or primary scientific outcome.** Missing results must not be interpreted as zero scores or as evidence against Complement Naive Bayes.

| Field | Recorded value |
|---|---|
| Pre-run revision | `37bfd9e9d318a4964d6426cc9df137d67319d0f1` |
| Start / failure (UTC) | 2026-10-13 23:13:46 / 23:17:30 |
| Monotonic elapsed time | 223.968 seconds |
| Execution | One offline, non-root Docker attempt; only E012 artifacts writable |
| Completed classifier fits | 49 of 95 planned |
| Fully prepared outer folds | 2 of 5; stopped during fold 3 preparation |
| Recorded exception type | `PermissionError` |
| Global development freeze / evaluation | Not reached / not started |
| Research metrics | Unavailable, not zero |
| Retry / next experiment | None; protocol stopping rule applied |
| Monitor | Reported FAILED and exited; no active or idle monitor remains |

The [aggregate-only failure record](../results/E012_execution_failure.json) pins the pre-run revision, image, E011 result, protocol lock and local attempt/failure/status evidence hashes. Private artifact files are not published. E011 remains unchanged and valid; all 178 public E011 Git blob hashes were independently matched to the local commit, and its [GitHub verification workflow](https://github.com/traghuram444/responsible-ai-math-misconceptions/actions/runs/38482899383) passed.

## Diagnosis and uncertainty

Source inspection found that `LiveStatus._heartbeat` catches status-write `OSError`, but the main-thread `LiveStatus.update` path does not. Consequently an error in a progress update can abort fitting even though the progress monitor is intended to be observational. A synthetic Docker fault-injection check, using only temporary synthetic status data and no MAP fitting, confirmed that a `PermissionError` from the status publisher propagates through `update`.

The last recorded progress was 49 completed fits during fold 3 preparation. The failure is consistent with transient status-file write/replace contention on the Windows-mounted output directory. **That exact root cause is not confirmed**: the original exception traceback was suppressed by the locked runner and only the exception type was retained. The diagnostic demonstration establishes a software failure path, not the specific filesystem operation or actor responsible for this occurrence. No permissions were relaxed and no other PC project or service was changed.

## Required next decision

E012's preregistered operational-failure stopping rule applies. The locked implementation, thresholds, folds, calibration, model grid and preserved E001–E011 results have not been modified. The failed attempt remains on disk and is not overwritten.

Before any retry, propose and approve a transparent infrastructure-only amendment: isolate best-effort monitor I/O from research computation, retain sanitized operation-level failure diagnostics, test transient write/replace failures synthetically, and use a new attempt directory. Such an amendment must preserve every scientific choice and the failed-attempt record. It has **not** been implemented or authorized by this failure report. No E013 or replacement model has been started.
