# E016 execution and preservation record

E016 completed its single approved attempt on 2026-10-19 with the reviewed protocol, scientific settings and frozen QuestionId roles unchanged. [Complete numerical tables](E016_RESULTS.md) precede interpretation.

## Approval and preflight

The [approval record](../experiments/e016_approval.json) pins the unchanged [protocol](E016_PROTOCOL.md). The tested implementation and [execution lock](../experiments/e016_lock.json) were published before fitting in commit `ababb48100e969ba8b1fa18b17e5fbc8f3aec6b2`. All 246 public blob hashes matched that revision; its [public verification job](https://github.com/traghuram444/responsible-ai-math-misconceptions/actions/runs/39258129156) passed.

The full preflight in the pinned offline/non-root Docker image passed **488 tests with one expected unpublished-result skip**, historical aggregate checks and five deterministic figure checks. The publication audit found no matching secret/local-path patterns and zero matches against 28,587 normalized student-response prefixes. The execution lock protects 233 prior public files, 52 private evidence files and the prior experiment-log prefix. Data and both frozen split hashes matched the protocol.

## Execution

| Item | Recorded value |
|---|---|
| Attempt | `e016_attempt01` |
| Image | `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0` |
| Identity | UID/GID 10001 |
| Isolation | Network disabled; root/project/data read-only; only the new attempt directory writable; ephemeral scratch |
| Numerical execution | CPU; OPENBLAS, OMP and MKL thread limits all 1; seed 20260831 |
| Start | 2026-10-19 13:12:41.549 UTC / 09:12:41.549 EDT |
| Result construction finished | 2026-10-19 13:19:48.661 UTC / 09:19:48.661 EDT |
| Result-construction runtime | 427.136 seconds |
| Monitor completion | 2026-10-19 13:19:49.400 UTC; 427.870 seconds, approximately 7 minutes 8 seconds |
| Classifier fits | 100 |
| Fit warnings | 0 |
| Reproduced historical model folds | 5 |
| Monitor final state | COMPLETED; 1601/1601 work units |
| Monitor I/O failures | One transient replace_snapshot PermissionError, errno 13; subsequent publication recovered |
| Terminal viewer exit code | 0 |

Live container inspection confirmed the pinned image, non-root identity, disabled network, read-only root/project mount, writable E016 attempt mount and dropped capabilities. Monitor work units count fits and scoring operations; they are not equal-duration units or elapsed-time estimates. The resilient monitor isolated the transient snapshot-write failure from computation. The experiment did not retry or change settings. The viewer exited normally, and no idle monitor or scheduled wakeup remains.

All ten arm/fold pipelines, selected settings, conditional frequencies, temperatures, raw/final predictions, routing orders and label-blind shuffle mappings were prepared before the global freeze. Evaluation targets were used for scoring only after that barrier. E011/frequency full-record reproduction and the applicable E013 raw/scaled and explanation-shuffle checks passed before factorized-model scoring. Data/fold hashes and historical preservation checks passed again after scoring.

The locked publisher verified the strict aggregate schema, recomputed summaries and contrasts, selection rules, calibration eligibility, Category grids, rank-change counts, metric identities and completion receipt before creating the public result files. No raw responses, answer strings, row-level predictions/probabilities, donor mappings, vocabularies, coefficients or fitted models were serialized.

## Artifact identities

| Artifact | SHA-256 |
|---|---|
| Approved protocol, LF-normalized | `bddb359a9869f7e0a5069f7544d4d3ff192422dc5fbf10033e695ded8bb91eab` |
| Execution lock | `6df217e5874acee5037e5db235542bb6a0a108c6b701daf62d67dfb4a0fd98a2` |
| Frozen development receipt | `61293cc920d014ab66a816a5cfedefa986d06eec0cf444106ab149a614d9847e` |
| Private and public aggregate | `de3fbdbf8a6e62ce5cb04b58dd9458574b3aa7dc6980c3a1be355128252e932d` |
| Completion receipt | `4a0b3802070343439327a4315d735232f46ff2c449e78dcfefb77d822d82d645` |

The public [aggregate artifact](../results/E016_aggregates.json) retains full-precision fold/question/support results, paired contrasts, raw/direct and final/marginalized Category metrics, explanation-shuffle summaries, calibration and fixed-review-budget results. The public aggregate is byte-identical to the private aggregate source. [The report](E016_RESULTS.md) renders the registered numerical tables. These records contain no interpretation or next-experiment proposal.
