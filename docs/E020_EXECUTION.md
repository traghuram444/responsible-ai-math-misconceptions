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

## Synthetic readiness completed — 2026-10-26

The single attempt began at 15:09:26 UTC from committed, publicly verified preparation `bcf37d49835aa7405e53e46752c0ee1a91f1e78b`. The readiness lock SHA-256 is `15259599434374d3c9106de86c23f4b13d9a0c62f5e8700b943784b16ec59a98`. G15 completed at 15:40:29 UTC and G7 at 17:17:44 UTC. Both models completed exactly twelve fixed fixtures; no technical-failure receipt exists, no retry occurred, and both monitors recorded zero I/O failures.

| Checkpoint | Completed readouts | Binary correct | Insufficient-information correct | Semantic gate applies | Gate passed | Tokens/second | Projected MAP hours |
|---|---:|---:|---:|---|---|---:|---:|
| G15 | 12/12 | 5/10 | 0/2 | false | true | 2.778534 | 3.805376 |
| G7 | 12/12 | 10/10 | 2/2 | true | true | 0.716011 | 14.633404 |

G15 recorded two capped rationales; G7 recorded none. Both had zero technical input/content fallbacks. Recorded container peak memory was 4,532,477,952 bytes for G15 and 18,505,318,400 bytes for G7, within the unchanged 24 GiB limits. Model wall times were 1,859.430248 and 5,830.023526 seconds respectively. The combined registered projection is 66,379.606139 seconds (18.438779 hours), below the 48-hour runtime-approval boundary; it is an estimate, not a deadline.

These are synthetic readiness outcomes only. No MAP catalogue, MAP inference, classifier fit, outer-fold prediction or evaluation result was produced by this stage. The smaller model's semantic accuracy does not control inclusion under the registered rule. No MAP-generalization claim follows from either checkpoint's fixture performance.

The frozen publisher verified the strict aggregate schema, gate arithmetic, ordered model receipts, model/environment/readiness hashes and all 664 historical files. Both full model manifests were independently rehashed after execution. The 17-file readiness lock and both append-only prefixes remain intact. The unchanged complete test suite passed again: **603 tests in 164.76 seconds**. [Readiness tables](E020_READINESS.md) and the [full-precision aggregate receipt](../results/E020_readiness.json) are retained; aggregate SHA-256: `85a35a6c4ffdfe81323965aac4c4a52048a8b09424b438688c330a7aa3450c6b`.

Status is `READY_FOR_MAP_IMPLEMENTATION_CHECK`. The authorized next phase remains contingent on complete, tested, separately locked and committed MAP orchestration/reporting. Existing readiness code and evidence will not be edited.

The readiness-results publication audit passed for 314 public/proposed files, with no secret/local-path matches and zero matches against 28,587 unique private-response prefixes. The complete pre-run execution-document and experiment-log prefixes were independently compared against the pre-run commit. Only the two aggregate result files and append-only updates to these outcome records belong to the separate readiness-results commit; unfinished MAP implementation is excluded.

## MAP-phase implementation and preflight — 2026-10-26

Readiness results were committed separately as `1c9e3d54582a826aa535dbf1aeb77dbc639b359a`, pushed only to the personal repository and verified against public GitHub main. The subsequent implementation uses new MAP-phase files and an additional lock; none of the seventeen readiness-locked files is edited. The existing attempt receives new `map_inputs/` and `map/` subdirectories, each created exclusively. It is a phase transition within the same approved attempt, not a retry of either synthetic checkpoint.

The catalogue preparer verifies the frozen data hash and selects only the two authorized CSV columns, applying the original normalization and sorted-distinct ordering. It does not consult targets, IDs, explanations, model outputs or answer frequencies. The model containers receive only that catalogue plus read-only code/configuration/metadata and their respective official model files. No raw training CSV is mounted into either model container. Exactly sixty MAP assessments per checkpoint are permitted, G15 then G7, with unchanged two-stage settings and seed. All generated reasoning, scores, individual decisions, caches and mappings remain private.

The statistical phase validates and freezes both complete checker caches before selection or agreement scoring. It uses the unchanged nine-training/three-calibration/three-evaluation question roles, original nested E011 grid and fifty classifier fits. The fixed mixture grids reuse the selected inner predictions and training-only inventories. Calibration uses the original supported-calibration-row temperature fitter; all five folds' raw/final distributions, rankings, selected weights, temperatures and fixed review orders are serialized and hash-frozen before the evaluation-truth boundary.

The MAP calibration wrapper carries explicit technical-fallback provenance from the cache. This implements the existing protocol rule without editing the readiness helpers: valid C readouts, even if their numerical vector is exactly `(0,0,1)`, are not relabeled as technical fallback. Only deterministic technical fallback on every calibration and evaluation row enables the registered frequency identity for G15/G7. Pure mixture endpoints reuse their component outputs. Synthetic tests check both this distinction and exact agreement with the locked preparation helper for ordinary technical-fallback inputs; numerical zeros remain allowed.

Historical reproduction checks compare F, L and F_M exact/support/question/calibration/review records against E019 with absolute tolerance 1e-10 and exact counts/nulls, alongside original selection/temperature checks. No settings may be adjusted to pass reproduction. The strict public schema verifies the complete nine-arm grids, eleven exact/calibration contrasts, five gain/loss contrasts, six review budgets, four review contrasts, both correctness audits, training-majority controls, pair/reason/fallback counts, rank changes, resource distributions, five-fold summaries and registered decision rules. It rejects arbitrary/private text, missing cells and inconsistent arithmetic.

The additional private preservation inventory captures the completed readiness attempt files without publishing individual fixture filenames or digests. Both that inventory and the historical 664-file inventory are checked before/after MAP execution and before publication. The MAP lock captures the complete execution/log prefixes. The frozen publisher verifies aggregate/completion/cache/development/prediction hashes and emits only aggregate JSON and the full numerical tables; interpretation remains withheld until user review.

After all final tests, scans and the additional lock are committed, launch the one MAP phase from the repository root:

```powershell
python -B scripts/run_e020_map.py
```

The independent read-only terminal viewer is:

```powershell
python -B scripts/monitor_e020_map.py
```

Progress is completed MAP pairs out of 120, followed by classifier fits out of 50. No MAP metric appears before global prediction freeze and historical-control reproduction. The viewer preserves completed counts on failure and never starts/resumes computation. The hourly follow-up is updated for this phase only while computation is active; it stops after completion/failure. No E021, changed model/prompt, retry or new analysis is authorized.

Final pre-MAP verification passed **622 tests in 203.65 seconds** in the pinned offline, non-root statistical image; the targeted E020 suites passed **56 tests in 12.78 seconds** before the final full-suite run. These include a complete invented-data reporting grid, deliberate corruption/private-field rejection, all-fold freeze requirements, historical-control mismatch rejection, fixed review ties, unsupported-label union Brier, fallback provenance, pure endpoints and preparation equivalence. The checker entry point also passed a solver-image import/help check with no data/model mounts and no inference. No real MAP fit or model assessment was used as a test.

The label-blind catalogue reproduced **60 distinct pairs across 36,696 rows**. The full public/proposed-file audit passed for 324 files at its snapshot, with zero secret/local-path matches and zero matches against 28,587 private-response prefixes. After the final provenance wrapper and tests were added, a current-E020 scan covered 33 public files against the same prefixes and again found zero matches. Final path/text and current-E020 scans are repeated after serialization of the additive lock. All code/protocol thresholds, frozen roles, model settings and interpretation rules remain as approved.

## Technical failure and authorized reporting recovery — 2026-10-27

The original MAP phase began from `f55ea3e864b33fbc2bfa195c64473ad1dcf98358` at 18:50:44 UTC on 2026-10-26. G15 completed 60/60 assessments in 10,931.701 seconds and G7 completed 60/60 in 32,896.304 seconds. The statistical phase completed all 50 fits and serialized all five frozen prediction archives and development records, then failed after 306.842 seconds during historical-control reproduction. The statistical receipt records `KeyError`; the enclosing launcher records `CalledProcessError`. No completion receipt or public result was produced. Both failure receipts and the entire failed attempt remain preserved.

The failure was the missing `category_raw` derived memory field required by the historical E016 Category audit. The original E020 preparation wrapper stored the underlying raw exact-label probabilities and classes but omitted that view. The original frozen code and locks are retained unchanged. The user subsequently authorized fixing the failure and continuing the experiment.

The additive [recovery specification](E020_RECOVERY.md) reconstructs this view with the exact historical marginalization function and uses the original scoring, reproduction and publication schema/renderer. It loads authenticated frozen predictions without any new inference, fitting, selection or calibration. Recovery outputs have a separate directory and completion receipt; the original failed attempt is read-only and inventoried in full. The original scientific protocol, historical results, folds, README and E018 blocked status remain unchanged. Synthetic regression tests passed **4 tests in 11.28 seconds**, including the actual missing-field failure and exact frozen-array reload/tamper rejection. Full-suite and publication checks precede the separately committed recovery lock and execution.

The complete pre-recovery suite passed **626 tests in 189.25 seconds** in the unchanged offline, non-root statistical Docker image. The additive recovery lock captures seven new repair/specification/test files and all **180 files** in the original failed attempt through a private inventory. Original locks, frozen predictions, 664 historical files and documentation prefixes passed verification. Publication path/text checks passed for 334 proposed files with no secret/local-path matches; the private-response scan must also finish successfully before launch.

The full private-response scan completed successfully: **28,587 unique response prefixes, zero matches** across the public/proposed files at its snapshot. A final current-recovery scan covers the newly serialized lock and appended documentation before commit. The original failed statistical run remains a failure in its own receipts; recovery will not overwrite or relabel it.
