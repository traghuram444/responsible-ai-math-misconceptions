# E014 execution and preservation record

E014 completed its single approved attempt on 2026-10-15, with the reviewed protocol and scientific settings unchanged. This record reports execution facts; [complete numerical tables](E014_RESULTS.md) precede interpretation.

## Approval and preflight

The [approval record](../experiments/e014_approval.json) pins the reviewed [protocol](E014_PROTOCOL.md). The tested implementation and [execution lock](../experiments/e014_lock.json) were published before fitting in commit `2ba6d2907f3586dde9a6dcf34b6b88881b5a968c`. All 218 public blob hashes were verified against that revision. Its [public CI run](https://github.com/traghuram444/responsible-ai-math-misconceptions/actions/runs/38774304025) passed.

Pre-run offline/non-root Docker verification passed **420 tests with one expected unpublished-result skip**, historical aggregate checks, and five deterministic figures. The publication audit checked 218 files, found no matching secret/local-path patterns, and found zero matches against 28,587 normalized student-response prefixes. The execution lock preserves 205 previous public files and 18 private evidence files. Existing experiment-log text remains append-only.

## Execution

| Item | Recorded value |
|---|---|
| Attempt | `e014_attempt01` |
| Docker image | `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0` |
| Identity | UID/GID 10001 |
| Isolation | Network disabled; root, project and data read-only; only the new attempt directory writable; ephemeral scratch |
| Numerical execution | CPU, one numerical thread, original seed 20260831 |
| Start | 2026-10-15 17:05:21.615 UTC / 13:05:21.615 EDT |
| Result construction finished | 2026-10-15 17:10:47.557 UTC |
| Result-construction runtime | 325.963 seconds |
| Monitor completion runtime | 326.673 seconds, approximately 5 minutes 27 seconds |
| Classifier fits | 50 |
| Fit warnings | 0 |
| Historical model folds reproduced | 5 |
| Final monitor status | COMPLETED; 1551/1551 work units |
| Monitor I/O failures | 0 |

All five model settings, weight selections, temperatures, prediction arrays, routing orders and explanation-shuffle mappings were frozen before evaluation scoring. Original E011/frequency development and fold/question/support/Category/review records reproduced within the registered absolute tolerance of 1e-10. E011 raw/scaled and explanation-shuffle diagnostics also reproduced E013 before selected-mixture scoring. Input hashes and prior-evidence preservation passed again after evaluation.

The selected weights by fold 0–4 were **0.25, 0.50, 0.25, 0.75, 0.00**. No outer weight sweep was evaluated. No scientific setting, grid, threshold, calibration rule, support stratum, or fold was changed during execution. No retry occurred. The separate read-only monitor exited normally after completion; no experiment or idle monitor remains active.

## Integrity receipts

| Object | SHA-256 |
|---|---|
| Approved protocol, LF-normalized | `4d375aab9f21c0d7d77dd4ffcaf3d49acea74b6c807215ccdfa9440044e08094` |
| Execution lock | `5de79c6064f42f2b449f115b9f04c507cc8defa78695edab297f238522b51951` |
| Frozen development receipt | `a905adb8b7630e34089a7e5d125089b2a46739504b15287b0195cd3ec423b8f6` |
| Private source and identical public aggregate JSON | `7d746c11cbb9add80571e3f9e411499c35cd9f775b556093669fbe473a92bfc7` |
| Private completion receipt | `5f7b9291a6306ed5e4217406b986996157a3bac9973e28d4a65201d7c805f7c6` |

The publisher verified the strict aggregate schema, numerical identities, fixed reporting grids, endpoint identities, and completion-receipt hashes before creating [the public artifact](../results/E014_aggregates.json) and deterministic report. No row probabilities, predictions, donor mappings, fitted models, vocabularies, or student text were serialized. The artifact contains repeated aggregate scores for the 100 diagnostic assignments, not individual prediction records.

## Numerical outcome

Mean exact-label MAP@3 is **0.537231** for the selected mixture, **0.511887** for E011, and **0.539215** for frequency. The paired mixture-minus-frequency mean is **-0.001984**, sample fold SD **0.033505**, positive in **3/5** folds; the registered primary criterion is **unmet**. Against E011 the mean delta is **+0.025343**, sample fold SD **0.028171**, positive in **4/5** folds.

All registered secondary and exploratory outcomes, null groups, and fold-level values remain in the artifact and numerical tables. No interpretation or E015 proposal is included. E001–E013 and all frozen assignments are preserved.
