# E012 second attempt infrastructure amendment

The user explicitly approved fixing the monitor and rerunning E012 in a new attempt directory, with all scientific settings unchanged and the failed attempt preserved. This amendment authorizes exactly one new attempt, `e012_attempt02`. It is committed and published before that attempt starts. A further operational failure stops; no automatic third attempt or replacement model is authorized.

## Scientific protocol unchanged

The [E012 protocol](E012_PROTOCOL.md), original execution lock, scientific runner, publisher, frozen data and QuestionId assignments, seeds, features, six-setting character TF–IDF/Complement Naive Bayes grid, inner group validation, temperature calibration, frequency comparison, support strata, metrics, primary margin/sign criterion and interpretation rules are unchanged. All 95 fits restart from scratch; no partial fit, score, vocabulary or model from the failed attempt is reused. The all-fold preparation barrier still precedes held-out metrics. The original scientific functions are called directly, not copied or rewritten.

The same image identity and non-root/offline/read-only/single-thread Docker controls apply. `experiments/e012_attempt02_lock.json` pins the amendment and all 179 prior public files other than the evolving README and append-only experiment log. The old E011/E012 lock remains valid and unchanged.

## Monitor failure isolation

The new `ResilientStatus` adapter replaces only the scientific runner's imported monitor class for this process. It preserves stage/progress/metric validation, in-memory state transitions and the independent heartbeat. An `OSError`, including `PermissionError`, while creating/opening/writing/replacing/cleaning up a monitor snapshot is best-effort: count it, report a sanitized operation identifier, and let computation continue. There is no immediate retry loop; the next heartbeat/update attempts publication. Diagnostic stdout failure is also nonfatal. Non-I/O programming errors remain visible.

Only monitoring I/O receives this treatment. Model exceptions, data/lock integrity failures, global-freeze writes, scientific result writes and execution-receipt writes remain strict failures. A final snapshot failure must not turn successful modeling into failure; the scientific result and execution receipt, not monitor availability, determine completion. If monitoring remains unavailable, the viewer reports unavailable/stale and stops without claiming that computation stopped or succeeded.

Diagnostics contain operation/function identifiers, exception type, numeric errno and counts, never exception messages, source lines, frame locals, student content or local paths. A synthetic test suite exercises all snapshot operations, transient recovery, persistent failure through finalization, model-error propagation, invalid metrics, diagnostic-output failure, stale rendering, and exact delegation to unchanged scientific functions.

## Attempt directories and preservation

The host directory `artifacts/e012` retains the failed first attempt unchanged. The launcher verifies its three evidence hashes against the [published failure record](../results/E012_execution_failure.json), mounts it read-only under an explicit failed-attempt alias, and verifies the hashes again after computation.

Only the new host directory `artifacts/e012_attempt02` is writable. Inside the modeling container it is mounted at the existing runner's fixed output location, `artifacts/e012`. This output-path mapping avoids modifying the locked scientific runner. The launcher refuses any pre-existing second-attempt directory. The old directory is never overwritten, moved, deleted or made writable in the container.

The new viewer reads only `artifacts/e012_attempt02/live_status.json`; it cannot accidentally display the failed first attempt. Monitoring operates only during the actual run. Use `python scripts/monitor_e012_attempt02.py` in the project environment. Periodic chat-monitoring notifications remain at most hourly; no idle automation is created.

## Publication and runtime

Launch with `scripts/run_e012_attempt02_docker.ps1` after synthetic tests, hash and privacy scans, and a clean public amendment commit. The original aggregate publisher can read the second attempt through the same read-only mount alias after execution. Publication additionally requires a completed `retry_execution.json` receipt, matching result/revision/amendment hashes and unchanged failed-attempt evidence. Publish the original strict E012 aggregate schema and complete tables, plus an explicit second-attempt execution record. Preserve the first failure report unchanged.

Expected modeling time remains approximately 5–20 minutes, CPU. Setup, testing and publication checks are additional. Report complete aggregate/fold results before interpretation, whether the fixed scientific criterion succeeds or fails. Stop after this E012 attempt; no E013.
