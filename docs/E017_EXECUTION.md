# E017 execution and preservation record

## Approved single attempt

E017 executed the [approved protocol](E017_PROTOCOL.md) without scientific amendments or retries. The [approval record](../experiments/e017_approval.json) pins the unchanged reviewed document. Real historical predictions and truth-supplied oracle diagnostics remain separate throughout [the result tables](E017_RESULTS.md) and [aggregate artifact](../results/E017_aggregates.json).

| Item | Recorded value |
|---|---|
| Public pre-run commit | `2dd8ae24d25ea311852de5a8f4fb75c4c089aad2` |
| Attempt | `e017_attempt01` |
| Start UTC | `2026-10-19T13:53:55.012494+00:00` |
| Result construction finish UTC | `2026-10-19T14:01:09.145911+00:00` |
| Result construction elapsed | 434.179892 seconds |
| Monitor completion elapsed | 434.752 seconds |
| Classifier reconstruction fits | 100 |
| Fit warnings | 0 |
| Historical original-result model/fold gates | 15, all passed |
| Monitor completed work | 146/146 |
| Monitor I/O failures | 0 |
| Viewer exit | Normal, exit code 0 |
| Automatic retries | None |

## Isolation and preservation

The existing pinned CPU image was `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, with Python 3.11.11 and one OpenBLAS/OMP/MKL numerical thread. Execution used UID/GID 10001, no network, a read-only root filesystem and project/data mount, dropped capabilities and no-new-privileges. Only the new attempt directory and ephemeral temporary storage were writable.

The [execution lock](../experiments/e017_lock.json) protects 247 prior public files, 57 private evidence files, the historical experiment-log prefix, and ten E017 protocol/implementation files. Historical locks are chained unchanged. Frozen data and assignment hashes match the approved protocol. Preservation was checked before and after execution; E001–E016, their completed/failed attempts, and frozen folds were not modified.

All ten real arm/fold preparations and all training-only compatible candidate lists were frozen before accessing evaluation truth. Historical selections, temperatures, supported calibration counts and applicable original exact-label, Category, calibration, agreement and review records reproduced within the registered absolute tolerance of 1e-10, with identical counts and null patterns. No new oracle/component scoring preceded these gates. No shuffle experiment was rerun.

## Verification before execution

The pinned offline/non-root Docker verification passed **527 tests**, with one expected skip for the not-yet-published E017 artifact. Historical aggregate checks and all five deterministic figure checks passed. The public plan's [GitHub verification run](https://github.com/traghuram444/responsible-ai-math-misconceptions/actions/runs/39263962185) passed independently.

All 260 pre-run public blobs matched the pushed Git tree. The publication path/secret/local-path scan passed, and the private response-prefix scan found **zero matches among 28,587 unique prefixes**. No raw data or row-level predictions were pushed.

## Artifact identities and aggregate publication

| Artifact | SHA-256 |
|---|---|
| Reviewed protocol, LF normalized | `c364628187c24e060986ae25439f667104af4435d81b14a40c195ebaaf3df8f2` |
| Execution lock | `7fff5309aab0838c573411319b651a8158c1c18f505a814f4e18b400f313fd91` |
| Frozen development receipt | `880293aba0051416963318307bb1d705518c167799a77f2a6b8bcb31556332d5` |
| Aggregate result, private and public identical | `454efa9b367b999a7f99fb13d8def99be84bf0d4686173cf17313c87a97cd0d3` |
| Completion receipt | `ff439a036539c2aff81b7e0174caec75cf716d661e733aa5fa020efbf7d0fe7f` |

The publisher verified the strict aggregate schema, separate real/oracle records, complete reporting grids, confusion/count arithmetic, oracle monotonicity, residual identities, recomputed summaries and completion receipt before creating the public files. No existing result was overwritten. The full Category oracle is a diagnostic for fixed training-frequency ranking, not a universal performance ceiling or a predictive-model result.

The terminal monitor remained active during execution, labeled real and oracle metrics separately, and stopped on completion. No idle monitor, further model run or subsequent experiment was started. Numerical results are provided before interpretation.
