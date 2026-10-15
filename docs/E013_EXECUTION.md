# E013 execution and preservation record

E013 completed the approved response-evidence diagnostic without changing the reviewed protocol, models, calibration, thresholds, support definitions, or frozen folds. [Complete numerical results](E013_RESULTS.md) precede any interpretation; no interpretation or next experiment is proposed here.

## Prerun registration and verification

The [approval record](../experiments/e013_approval.json) pins the reviewed protocol SHA-256. Public pre-run commit `a0874e9220d4d8e289d81fb70a59f475921280e2` was pushed and matched local main before fitting. All 204 Git blob hashes matched the public repository, and its [independent GitHub workflow](https://github.com/traghuram444/responsible-ai-math-misconceptions/actions/runs/38753326329) passed.

Offline/non-root pre-run verification passed **392 tests with one expected unpublished-result skip**, historical aggregate checks, and five deterministic figure checks. Publication path/secret/local-path checks passed for 204 files; comparison against 28,587 normalized private response prefixes found zero matches. Synthetic tests include the complete five-fold diagnostic pipeline, unchanged scientific preparation, deterministic label-blind assignment, frequency invariance, recipient support, corruption rejection, and strict aggregate-only publication.

## Completed attempt

| Field | Value |
|---|---|
| Attempt | `e013_attempt01` |
| Local interval | 2026-10-15 10:39:53–10:52:26 America/New_York |
| UTC interval | 2026-10-15 14:39:53–14:52:26 |
| Runtime through result construction | 751.993 seconds |
| Runtime through monitor completion | 753.062 seconds |
| Classifier fits / warnings | 145 / 0 |
| Prepared model folds | 10 / 10 before new evaluation metrics |
| Historical reproduction | All ten model-fold development and full original model/frequency records matched at absolute tolerance 1e-10, relative tolerance zero |
| Intervention assignments | 100 per condition/fold, label-blind and shared across models |
| Reporting | 300 model/fold/question/support records; 15 aggregate support summaries; 40 opportunity records; 10 probability-scale records |
| Historical public files preserved | 191, plus unchanged historical execution locks and their checks |
| Private attempt evidence preserved | 13 files across E011, E012 failure and E012 retry |
| Frozen data and assignments | Hash, ordered alignment and question-role checks passed before/after computation |
| Row-level artifacts or models serialized | None |
| Monitor | COMPLETED, 3146/3146 work units; viewer exited normally |
| Monitor I/O incidents | One transient PermissionError replacing a snapshot; caught by the pre-existing resilient adapter |
| Retries / scientific changes | None |

Docker inspection confirmed network mode `none`, user `10001:10001`, read-only root/project, and only the new attempt output writable. The pinned image remained `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`. Numerical libraries used the existing single-thread environment. The monitor ran separately and could not alter scientific state. Its one snapshot incident did not interrupt the run; the final status and completion receipt were written successfully.

All historical model and frequency reproduction gates passed before new diagnostic scoring. Frequency invariance was checked for every registered replicate and nonempty reporting stratum. The strict publication validator recomputed primary/aggregate summaries, descriptive shuffle dispersion, gain/loss identities, calibration eligibility, and question-to-fold weighted original/permutation score identities. Empty and ineligible strata remain null with reasons. No new outcome-dependent analysis or selection was added.

## Artifact identities

| Artifact | SHA-256 |
|---|---|
| Approved protocol, LF-normalized | `14efc479adbee9debd03adffe35f7ab2ef52f7fdfcbb619b891b3b3c9d4d1bc9` |
| Execution lock | `ef06191ec7b04721a895f7cd261bd7dc267e0f4c3fe12b6c670395e6d38c02cd` |
| Frozen development receipt | `3448216766a1431d79591d5a6c53cc344d5e6fc6e06ebc22fd8aa4c958718510` |
| Private completed aggregate source | `0a4252502cbe7244a20050fff1fa94a8b48db221434e56ae812f32b0b97e2755` |
| Private completion receipt | `f81101656e2d2b751d29061a28e86f261cbc1cfd9b6ce6088267c452c7a77a07` |

The private completion receipt's source-result hash, pre-run revision, and execution-lock hash matched the aggregate before public report generation. No previous attempt or scientific record was overwritten. The terminal monitor stopped on completion; no idle automation or subsequent experiment was started.
