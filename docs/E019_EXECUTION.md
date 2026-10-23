# E019 execution record

## Authorization and immutable specification

The user approved [E019](E019_PROTOCOL.md) on 2026-10-23. The separate [approval](../experiments/e019_approval.json) pins the unchanged protocol. E018 remains blocked; its protocol, approval and verification record are preserved. E001–E017 and their folds are not amended.

This record initially describes preparation, not completed MAP results. Completion, failure and publication entries will be appended. No follow-on experiment or automatic retry is authorized.

## Prepared environment

- Docker reported 33,489,608,704 bytes available; the solver is limited to 17,179,869,184 bytes (16 GiB), with no additional swap allowance and no host settings changed.
- The separate solver image is `sha256:08b0187445e3a72b9b1215968c69e536872705660a1b2fd4a6bd8694af40ddc6`.
- Historical reconstruction/scoring uses unchanged image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`.
- All 24 wheels are version- and SHA-256-pinned in [the complete closure](../repro/e019/requirements.lock), with [wheel provenance](../repro/e019/wheel_manifest.json). The separate image was installed offline with required hashes and passed `pip check`.
- The official revision's nine allowlisted files were downloaded into ignored project-local storage. The 3,087,467,144-byte weight file matches the preregistered SHA-256. The [model manifest](../experiments/e019_model_manifest.json) records all files; weights and notices remain private.
- The [environment lock](../experiments/e019_environment_lock.json) records image identities, full resolved generation configuration, template/prompt hashes, non-root identity and resource budget.

No GPU, remote inference service, host package installation, external account change or other project's configuration is involved. Solver and statistical containers are sequential, offline, non-root, read-only, capability-dropped and constrained to the new attempt for persistent writes.

## Exactly one synthetic plumbing check

The fixed `What is 1 + 1?` / `2` prompt was executed once, with the registered model, system prompt, generation configuration and parser. It used 177 input tokens and generated 272 tokens in 143.126690316014 seconds. Loading and generation completed; parsing returned **`unknown_invalid_output`**. The generated text remains private. The outcome was not used to change settings or add a retry.

Label-free input preparation read only QuestionText and MC_Answer, preserving the specified string normalization. All 36,696 rows reduce to **60 distinct pairs**. No correctness labels or student explanations entered this preparation. The private catalogue hash will be included in the execution lock, not individual pair digests or mappings.

At the synthetic check's approximately 1.90 output tokens/second, similar-length outputs across 60 pairs project about 2.4 hours; 1,024 tokens per pair project about 9 hours. These are rough extrapolations, not deadlines or guarantees: input lengths, output lengths, token-step cost and loading overhead differ. Every eligible pair remains required. The statistical stage adds 50 historical fits and registered reporting. No runtime-driven subset or early stopping is permitted.

## Execution and monitoring

The isolated dependency resolver is [resolve.py](../repro/e019/resolve.py), the official-file downloader is [download_model.py](../repro/e019/download_model.py), and the offline image definition is [Dockerfile](../repro/e019/Dockerfile). Building requires a context containing only the resolved `wheels/` and `requirements.lock`; do not include private inputs or weights in an image build context.

The [freeze script](../scripts/freeze_e019.py) refuses to replace a lock. The [one-attempt launcher](../scripts/run_e019_docker.py) requires a clean committed tree, exact images, the resource gate and preservation checks; it refuses an existing `artifacts/e019_attempt01`. Run from the repository root with its dependencies already prepared:

```powershell
python -B scripts/run_e019_docker.py
```

The launcher streams a read-only terminal monitor while its two Docker stages execute. A second terminal can observe the same state without affecting computation:

```powershell
$env:PYTHONPATH = 'src'
python -B scripts/monitor_e019.py
```

The viewer refuses to start when there is no attempt and exits on terminal/stale status. Heartbeats are not proof of numerical progress. Progress is pair count, classifier fit count and scoring work, never percent of predicted runtime. No metric is shown before global prediction/routing freeze. Routine chat notifications are at most hourly during the run; completion or technical failure is reported promptly. No idle scheduled monitor is created.

The solver container receives only source/scripts/experiment metadata, the pinned model and the two-field catalogue; **raw MAP data is not mounted into it**. Its full private cache is frozen before the statistical stage. All five folds' predictions, both scales, candidate filtering and review orders are frozen before accessing evaluation truth for scoring. Historical F/L reproduction and all preservation gates must pass before new results are released.

## Publication safeguards

The [preservation inventory](../experiments/e019_preservation_start.json) captures 513 pre-existing files and the prior experiment-log byte prefix. It includes the frozen inputs, earlier experiment artifacts and E018 records. Code and results are separate commits. Strict aggregate schemas reject unexpected keys/text and require complete reporting grids and consistency checks. Only code, tests, public metadata, protocols, aggregate tables and append-only history are publishable. All pair inputs, responses, completions, model weights, row predictions, class inventories and fitted model objects remain private.

Final results must precede interpretation. All negative outcomes, including unknown outputs and fallback behavior, remain in the registered denominators. An incomplete technical failure is not a scientific negative result and must not be silently resumed.

## Pre-launch verification — 2026-10-23

The unchanged historical Docker image passed the complete suite: **566 tests**. After the final E019 publication-integrity and alignment refinements, the E019-specific suite passed again: **38 tests**. Synthetic tests cover input normalization, parser precedence/EOS, unknown/no-candidate fallbacks, ranking/argmax ties, correct-filter monotonicity and wrong-filter harm, unsupported-label Brier, eligibility, fixed routing, full report grids, corrupted-publication rejection, the global truth boundary, frozen configuration and monitor I/O isolation.

The initial full publication scan found no secret/local-path patterns and zero matches against 28,587 unique private response prefixes. The final pre-commit audit is repeated after lock serialization. Preservation verification passed for all 513 captured files and the original experiment-log prefix. GitHub authentication and origin were verified as the personal public repository `traghuram444/responsible-ai-math-misconceptions`.

The execution preservation gate deliberately requires this existing local experiment history, including ignored private evidence, and refuses to invent missing prior artifacts on a fresh checkout. Public hashes are verification records, not a redistribution of that evidence. Reconstructing the scientific controls from lawfully acquired data and rebuilding the pinned environment are distinct from reproducing historical timestamps or private log bytes.

## Completed attempt — 2026-10-23

Attempt `e019_attempt01` completed at 21:49:45 UTC from pre-run commit `6f0fb14c4a1978f1d56451f2b6b80c3beebc36d3`. The execution lock SHA-256 remains `3369f0bb48694bce56fd1f386b04d658b31c7c6ac517a6929cf74c1c327895f6`. No failure receipt exists. No retry, resume, parser adjustment, model replacement or scientific-setting change occurred.

All 60 distinct pairs completed; 58 were recorded as `unknown_invalid_output` and two as `unknown_generation_limit`. There were zero accepted true/false decisions. All 36,696 evaluation rows therefore used the registered unknown fallback. Generated tokens totaled 19,770. The aggregate artifact records 10,205.431395421736 checker seconds and 316.3596602892503 statistical seconds. Terminal status spans, which include different bookkeeping boundaries, were 10,205.446 and 317.034 seconds respectively. The resilient solver monitor recorded three isolated I/O failures; final status was completed. The statistical monitor recorded zero I/O failures. Neither changed computation or settings.

All 50 historical classifier fits completed with zero fit warnings. All five folds' raw/final predictions and review orders were globally frozen before scoring. Historical F/L reproduction passed for ten model-fold combinations. Post-run verification checked the complete private cache and five frozen prediction-file hashes without publishing their contents, the development-freeze hash, all locked scientific files, the preparation-log prefix, and all 513 protected pre-existing files. E001–E017, frozen folds, README and E018's blocked verification records remain unchanged.

The completed aggregate SHA-256 is `4ed2fb5e01eb7bf0a8546d94f28c6c3db544374fbde3112a756dd758b312ebb4`, matching the execution receipt. The frozen publisher validated the strict aggregate schema, arithmetic and complete registered grids, then generated [all numerical tables](E019_RESULTS.md) and [full-precision aggregates](../results/E019_aggregates.json). No private inputs, generated text, pair mappings or row-level outputs are included.

| Arm | Equal-fold MAP@3 | Sample SD | Equal-fold exact accuracy |
|---|---|---|---|
| F | 0.539215 | 0.039204 | 0.402009 |
| L | 0.511887 | 0.070731 | 0.368558 |
| F_M | 0.474187 | 0.036689 | 0.402009 |
| F_A | 0.539215 | 0.039204 | 0.402009 |
| L_A | 0.511887 | 0.070731 | 0.368558 |

Registered MAP@3 comparisons: F_A−F = 0.000000 (0/5 positive folds; criterion false); F_A−F_M = +0.065028 (5/5; criterion true); L_A−F_A = −0.027328 (2/5; criterion false). The primary H1 conjunction and secondary H2 flags are both false. These are numerical decision-rule records, not an interpretation. All registered question/support, correctness, fallback, gain/loss, raw/final calibration and fixed-review panels are retained, including null and zero results. Interpretation and any next experiment await user review.

## Post-run publication verification — 2026-10-23

The complete unchanged test suite passed again in the pinned offline, non-root historical Docker image: **566 passed in 177.65 seconds**. The public JSON is byte-identical to the completed aggregate artifact, and the Markdown exactly matches the frozen renderer; its SHA-256 is `893b82cd081f01b6f63e0df27903e8a743580370a8c1c033581644d33d82caca`. Post-publication preservation checks passed for all 513 files, all locked E019 files, and both complete pre-run documentation prefixes.

The publication audit covered 293 public/proposed files, found no matching secret or local-path patterns, and verified the older 144-file public-history inventory and log prefix. The private-response scan checked 28,587 unique prefixes and found **zero matches**. Only the two generated aggregate files and append-only changes to this execution record and the experiment log are included in the results commit. The hourly E019 follow-up was removed after completion; no experiment or idle monitor remains active. Interpretation remains deferred.
