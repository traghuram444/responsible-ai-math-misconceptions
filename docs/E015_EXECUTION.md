# E015 execution and preservation record

E015 completed its single approved attempt on 2026-10-16. The reviewed protocol, all scientific settings, and frozen QuestionId roles were unchanged. [Complete numerical tables](E015_RESULTS.md) precede interpretation.

## Approval and preflight

The [approval record](../experiments/e015_approval.json) pins the unchanged [protocol](E015_PROTOCOL.md). The tested implementation and [execution lock](../experiments/e015_lock.json) were published before fitting in commit `1f8d759e095112a1c60392432c766ef842b9d440`. All 232 public blob hashes matched that revision. Its [public verification run](https://github.com/traghuram444/responsible-ai-math-misconceptions/actions/runs/38935659222) passed.

Preflight in the pinned offline/non-root Docker image passed **455 tests with one expected unpublished-result skip**, historical aggregate checks, and five deterministic figure checks. The publication audit found no matching secret/local-path patterns and zero matches against 28,587 normalized student-response prefixes. The E015 execution lock preserves 219 previous public files and 23 private evidence files. The existing experiment-log prefix is retained.

## Execution

| Item | Recorded value |
|---|---|
| Attempt | `e015_attempt01` |
| Image | `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0` |
| Identity | UID/GID 10001 |
| Isolation | Network disabled; root/project/data read-only; only the new attempt directory writable; ephemeral scratch |
| Numerical execution | CPU; OPENBLAS, OMP and MKL thread limits all 1; seed 20260831 |
| Start | 2026-10-16 16:55:55.315 UTC / 12:55:55.315 EDT |
| Result construction finished | 2026-10-16 17:12:46.440 UTC / 13:12:46.440 EDT |
| Result-construction runtime | 1011.218 seconds |
| Monitor completion | 2026-10-16 17:12:47.502 UTC; 1012.276 seconds, approximately 16 minutes 52 seconds |
| Classifier fits | 150 |
| Fit warnings | 0 |
| Reproduced historical model folds | 5 |
| Monitor final state | COMPLETED; 2151/2151 work units; 0 I/O failures |

Live container inspection confirmed the pinned image, non-root identity, network isolation, read-only root/project mount, writable E015 attempt mount, dropped capabilities, and one-thread environment. Monitor work units count completed fits and scoring operations; they are not equal-duration units or elapsed-time estimates. The separate read-only terminal viewer exited normally at completion. No idle monitor or scheduled wakeup remains.

All 15 arm/fold pipelines, selected settings, temperatures, predictions, routing orders, and shuffle mappings were frozen before evaluation targets were used for scoring. E011/frequency full-record reproduction and historical answer-token counts passed; the applicable E013 raw/scaled and explanation-shuffle checks passed before B/C scoring. Input hashes and historical preservation checks passed again after scoring. There was no retry or scientific amendment.

The locked publisher verified the strict aggregate schema, recomputed summaries, selection rules, metric/count identities, token-coverage denominators, and completion receipt before creating the public result files. No raw student text, answer strings, row predictions/probabilities, vocabularies, donor mappings, or fitted models were serialized.

## Artifact identities

| Artifact | SHA-256 |
|---|---|
| Approved protocol, LF-normalized | `8760a8449228b50320c4fff8184b02d5e909f9457d3c6f4562ff87731153fe25` |
| Execution lock | `faf0f97b45be4c66e637b6499f295e20db0494548bdb04747e70c478292c9628` |
| Frozen development receipt | `f679c40f56cc86608aa5c20c5da97f624851409cea284dcab81cc8316de98bde` |
| Private aggregate source | `ddd818ee61dfc9fb70bd90baada6cf02c476a3058a22da4c1a7220b931a7c90d` |
| Completion receipt | `8c683094dfe62ae2ab410abb4ab6f2896bf20e0d53d2cadbb648007e115ae850` |

The public [aggregate artifact](../results/E015_aggregates.json) retains full-precision fold/question/support results, paired contrasts, Category metrics, token/vocabulary coverage, permutation summaries, calibration, and fixed-review-budget results. [The report](E015_RESULTS.md) renders the registered tables. These numerical records do not propose a next experiment or interpret the findings.

## Post-run verification

The full pinned Docker verification passed **456 tests with no skips**, including validation of the completed E015 artifact and exact regeneration of its numerical report. Historical aggregate checks and all five deterministic figure checks passed. The public aggregate file is byte-identical to the private aggregate source recorded above. All E001–E014 scientific files, private evidence, and frozen split inputs remain unchanged.

The final publication audit checked 235 public files, found no matching secret/local-path patterns, and found zero matches against 28,587 normalized student-response prefixes. Only aggregate results and factual documentation are included in the separate E015 results commit.
