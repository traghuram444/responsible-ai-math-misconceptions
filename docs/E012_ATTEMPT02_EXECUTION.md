# E012 second attempt execution record

The approved monitor-only amendment completed E012 without changing its scientific settings. The fixed primary criterion was not met. The first attempt's operational failure remains preserved separately; this record concerns `e012_attempt02` only.

## Execution and preservation

| Field | Verified value |
|---|---|
| Public pre-run revision | `99ff908b8489c15701d71915e731a5f990b9e45f` |
| Modeling interval UTC | 2026-10-14 01:38:06–01:45:02 |
| Runtime through result construction | 415.699 seconds |
| Runtime through final monitor state | 415.849 seconds |
| Classifier fits / warnings | 95 / 0 |
| Prepared outer folds before evaluation | 5 / 5 |
| Original frequency reference checks | 15 / 15 passed |
| Complete frequency fold/question records | Matched E011 at the unchanged tolerance |
| Original scientific lock | Unchanged; 163 historical files preserved by original gate |
| Infrastructure amendment lock | Unchanged; all 179 prior public files preserved |
| First failed attempt | Three evidence hashes unchanged before and after modeling |
| Execution | Same image, offline, non-root, read-only root/project/data, only new attempt output writable |
| Monitor | COMPLETED, 101/101 work units, zero I/O failures in this actual run; viewer exited normally |
| Stop condition | E012 completed; no further experiment or idle monitor |

The pre-run [GitHub workflow](https://github.com/traghuram444/responsible-ai-math-misconceptions/actions/runs/38496606718) passed. All 190 pre-run public Git blob hashes matched the local commit. The original scientific runner, original monitor source, protocols, model grid, support thresholds, data/fold hashes, calibration, evaluation, primary criterion and publisher were not edited. The adapter replaced only the runner's monitor-class binding in its process.

The local execution receipt records `failed_attempt_preserved=true`, `scientific_settings_changed=false`, a completed monitor, and the scientific result hash. A separate post-run check matched the receipt to the result, pre-run revision, both locks, the preserved failed attempt and all complete E011 frequency records. Another independent arithmetic check verified 90 weighted question-to-fold MAP@3, confidence and Category-accuracy identities with zero discrepancies. Public outputs remain aggregate-only.

| Pinned item | SHA-256 |
|---|---|
| Original scientific lock | `05a203f9fe979213820ceed3a1e9723bf98cc159c74d8d21a6c9f0656235c094` |
| Infrastructure amendment lock | `5318f88f1ebe5041b55f0d390884bef03180f06d516ec80a39b7b89ac7ac31ed` |
| Second-attempt source result | `48f4b8b79218f7ed7530d5ac72c75b7536c6b15f493b45c5f4dd8c0edfda23f6` |
| Local second-attempt execution receipt | `cd3a1e50d585f7f08859b0b1229e2874687fc40cb8fbd7540b70b9ebb9865d7c` |
| E011 comparator artifact | `98d48fb1b9143d3f9a9c461d7b28eb89b8a9d873722b0cd622b1cf18ddb20c87` |

## Container mount preflight

One container initialization request failed before Python started because the read-only project mount lacked the empty directory used for the failed-attempt alias. No second-attempt metadata, fits or metrics existed at that point. An empty `artifacts/e012_failed_attempt01` mountpoint was created, and the identical Docker argument list was reissued against the still-empty `artifacts/e012_attempt02` directory. No scientific parameter or locked file changed, no prior attempt was removed, and no running research computation was restarted. The viewer initially timed out waiting for a nonexistent status file; it was reopened after the successful container start.

For a fresh authorized reproduction environment, prepare the empty alias mountpoint before the first launcher invocation:

```powershell
if (-not (Test-Path -LiteralPath 'artifacts/e012_failed_attempt01')) {
    New-Item -ItemType Directory -Path 'artifacts/e012_failed_attempt01' | Out-Null
}
.\scripts\run_e012_attempt02_docker.ps1
```

This attempt-preservation launcher requires the original failed-attempt evidence, authorized MAP data and frozen split artifacts locally. It refuses a pre-existing second-attempt output directory; never delete a completed or failed attempt to bypass that guard. The adapter, scientific code and hashes remained unchanged during this run.

## Complete result and interpretation boundary

[Complete numerical tables](E012_RESULTS.md) and the [aggregate artifact](../results/E012_aggregates.json) contain all registered outputs. Equal-fold full-context MAP@3 is 0.537228, versus 0.539215 for frequency and 0.511887 for E011 full context. The delta versus frequency is −0.001987 ± 0.003825, positive in 2/5 folds; versus E011 it is +0.025341 ± 0.057834, positive in 3/5 folds. The fixed requirement is mean improvement at least 0.020 with positive gains in at least 4/5 folds against both comparators; it is unmet.

Mean ECE is 0.377470, versus 0.056271 for frequency and 0.149626 for E011. Corrected Brier is 0.985662, versus 0.795057 and 0.838084 respectively. Near-baseline MAP@3 does not establish useful calibration or reliable automation. These are descriptive results on repeatedly examined questions, not formal equivalence or independent inferential evidence. No calibration change, alternative threshold, favorable subgroup or secondary metric replaces the registered outcome.

The actual retry encountered no monitor I/O error, so its success alone does not demonstrate handling of a recurring filesystem failure. The 16 synthetic infrastructure tests, including persistent replacement failure with identical model outputs, establish the tested isolation behavior. The precise cause of the first attempt's PermissionError remains unconfirmed.

## Final publication checks

Offline/non-root Docker verification passed 373 tests with no skips, historical aggregate validators and all five deterministic figure artifacts. All 193 proposed public files passed path/secret/local-path checks. The five changed/new publication files were checked against 28,587 unique normalized student-response prefixes with zero matches; unchanged prior files remain covered by the earlier audit and preservation hashes. No raw response, dataset archive, row-level prediction, model parameter or private attempt file is published.
