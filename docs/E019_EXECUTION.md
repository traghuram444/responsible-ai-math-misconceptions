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
