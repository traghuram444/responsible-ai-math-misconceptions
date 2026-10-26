# E020 execution record

## Approval and staged implementation — 2026-10-26

The user approved the exact [E020 protocol](E020_PROTOCOL.md) with “approved,proceed”. The protocol is preserved verbatim, including its historical proposed-status paragraph; [the separate approval record](../experiments/e020_approval.json) records the transition to approved execution. Its canonical SHA-256 is `1c018789dbcba1cbdd7d7096a7e2830c2a547304297154a76345bcde7941ede2`.

The first implementation stage is **synthetic readiness only**: twelve fixed fixtures per checkpoint, smaller checkpoint first, using the exact approved settings. This stage does not prepare MAP inputs, fit classifiers or report MAP performance. No extra model call, alternative prompt, automatic retry or settings substitution is allowed. The 7B semantic gate and both technical gates must pass. A combined projected MAP runtime over 48 hours requires explicit runtime approval before any MAP inference.

The readiness launcher deliberately stops after serializing the gate outcome. If the gate passes within the approved runtime allowance, the complete MAP orchestration, reporting schema, reproduction checks and publisher must be implemented, tested and separately committed before MAP execution. Initial fusion/selection helpers are present but are not a completed MAP runner. This staged implementation does not change scientific settings or grant permission to score partial MAP results.

## Historical preservation and private evidence

The [aggregate preservation receipt](../experiments/e020_preservation_start.json) captures 664 historical files against baseline commit `382e2de2011e2428f365e150ea29b718e82352c6`. The full per-file inventory remains private: only its count and whole-inventory hash are published. Original E001–E019 evidence, frozen folds and README remain unchanged; E018 remains blocked. The captured experiment-log bytes are checked as an immutable prefix so new outcomes can be appended without rewriting history.

Official model downloads use a separate non-root container with no private-data mounts. The smaller official checkpoint is reused read-only from the preserved E019 setup. The 7B checkpoint is acquired from the protocol's fixed official revision; all four weight hashes and the allowlisted small-file hashes are locked before inference. No weights, cached inputs, generated reasoning, individual decisions, row predictions or local paths are publishable.

## Reproducibility and gates

The solver and statistical images are the exact historical image IDs named in the protocol. No dependency, OS, Docker setting or driver is changed. Solver containers are offline, non-root, read-only, capability-dropped, no-new-privileges, with tmpfs scratch and a 24 GiB memory/swap limit. Models run sequentially on CPU BF16, with the approved deterministic seed, eager attention and single numerical threads.

Configuration-only inspection resolves the full generation configuration, tokenizer special tokens, chat-template hash and single-token A/B/C identities without loading model weights or invoking a model. The public environment/model manifests and readiness code lock must be committed before the first synthetic inference. The launch refuses a dirty tree, an existing attempt directory, changed hashes or failed resource gates.

Launch the one authorized readiness attempt from the repository root after its committed locks exist:

```powershell
python -B scripts/run_e020_readiness.py
```

Observe it in an independent, read-only terminal:

```powershell
$env:PYTHONPATH = 'src'
python -B scripts/monitor_e020.py
```

The independent viewer reports readiness progress out of 24 synthetic fixtures, not 120 MAP pairs or 50 classifier fits. It never launches or resumes computation and exits on completion/failure/stale status. Routine chat checks are hourly only while work is active; completion, failure or runtime approval is actionable. There is no idle monitor after the experiment stops.

The strict readiness publisher rejects arbitrary/private fields, validates gate arithmetic and model order, verifies receipt/model/environment/code provenance and historical preservation, and refuses publication as a completed gate if any technical-failure receipt exists. Synthetic results must not be described as MAP predictive evidence.

## Pre-launch tests — 2026-10-26

The complete suite passed **603 tests in 181.74 seconds** in the unchanged, offline, non-root statistical Docker image. The final E020-specific suite passed again: **37 tests in 2.32 seconds**. These are synthetic-array/fake-model tests, not real model calls. All eleven new Python implementation/launcher files also passed syntax compilation without writing caches.

The tests cover the exact prompt and fixtures, single-token candidates, input and rationale fallback precedence, token-limit boundaries, EOS/cap behavior, empty rationale and forced next-token readout, full-vocabulary candidate mass, nonfinite rejection, fixed gate and runtime boundaries, strict aggregate fields, model sequence, fusion identities, zero/absent prefix behavior, endpoint calibration identity, training-only inner counts/selection, held-out-label exclusion and read-only monitor behavior. No scientific result is inferred from these checks.

## Acquisition and publication checks — 2026-10-26

All thirteen allowlisted 7B files downloaded successfully from the pinned official revision. The four actual shard sizes and SHA-256 values match the preregistered publisher identities; no download-failure receipt exists. The [model manifest](../experiments/e020_model7_manifest.json) records actual small-file and weight hashes. The [environment lock](../experiments/e020_environment_lock.json) records both resolved generation/tokenizer configurations, the unchanged image identities and the 24 GiB memory limit. Configuration inspection made no model calls.

The initial publication audit passed for 309 public/proposed files with no matching secret or local-path patterns. Its scan of 28,587 unique private-response prefixes found zero matches. After adding the model/environment manifests, a current-E020-file scan covered nineteen files, including the appended experiment log, against the same 28,587 prefixes and found zero matches. The final locked tree receives another path/text audit and a current-E020 prefix scan before commit. Historical preservation was verified for all 664 captured files and the old log prefix.

The authenticated account, origin, main branch and public repository identity were verified as `traghuram444/responsible-ai-math-misconceptions`. No raw data, downloaded archive/weights, individual output, private inventory or cache is included in publication. Readiness execution begins only after the sanitized plan/code/configuration commit is pushed and verified.
