# E020 reporting recovery

On 2026-10-27, the user explicitly authorized fixing the technical failure and continuing E020. This authorizes one reporting-only recovery in a separate `artifacts/e020_recovery01` directory. The failed attempt remains unchanged, including both failure receipts and its status. No historical file, scientific protocol, fold, threshold, prompt, model, selection, calibration or prediction is changed.

## Failure and mechanical repair

The initial run completed 120 checker assessments and 50 classifier fits. All five folds' probabilities, predictions, rankings, review orders and development records were serialized and hash-frozen before evaluation truth access. The failure occurred in historical-control reproduction: the E016 Category audit expected `memory['category_raw']`, omitted by the new E020 preparation wrapper. Its exact historical definition is `e016.marginalize(memory['raw'], memory['classes'])` for E011.

The recovery loads the hash-verified frozen arrays and reconstructs only this derived Category view with the unchanged historical function. No truth enters this reconstruction. No probabilities, rankings, thresholds or fitted parameters are recalculated or changed. The Category view is used only to run the already-required historical reproduction checks; it adds no analysis. This is a disclosed execution repair after a failed attempt, not an uninterrupted successful run.

## Gates and execution

An additive lock captures this implementation, synthetic regression tests, full failed-attempt private inventory and append-only documentation prefixes before recovery scoring. The private inventory covers the complete original attempt, including readiness, inputs, cached outputs, freezes, logs and failure receipts; only its count and aggregate digest are public. The original readiness and MAP locks remain enforced. The historical 664-file preservation gate and E018 blocked status remain enforced.

The source must contain exactly the two known failure receipts, with the original exception types. Their existence is explicitly acknowledged, never removed or suppressed. Any additional failure, mutation, missing freeze, mismatched cache or failed control reproduction stops recovery. Recovery itself must have no failure receipts for publication. Frozen NumPy archives contain local object arrays; loading permits pickle only after the original freeze digest and the newly locked complete-attempt inventory both verify. No untrusted archive is accepted.

Run in the same pinned statistical Docker image, offline, non-root, read-only project/source mounts, with only the new recovery directory writable. The seed and single-thread environment remain unchanged. Use the frozen scoring functions, strict schema, interpretation rules and Markdown renderer. Reproduce every registered F/L/F_M control before displaying metrics. There are zero new model calls, fits, tuning steps or calibration fits. Verify all five folds' population/role alignment and unchanged prediction hashes before and after scoring.

The aggregate JSON retains the original scientific provenance fields and schema. A separate strict recovery receipt identifies original and recovery commits, locks, frozen-input hashes, source failure types, original statistical elapsed time, recovery elapsed time and zero additional compute calls/fits. `statistical_seconds` in the aggregate is the original failed statistical phase plus this reporting recovery; neither replaces the original timing receipt. The public report explicitly links the recovery receipt and this disclosure. Results remain descriptive and are shown before interpretation.

## Verification and monitoring

Regression tests reproduce the missing Category field on invented frozen arrays, verify equality to historical marginalization and unchanged input arrays, exercise all-fold freeze reload and reject changed hashes/missing folds. Run the complete suite and publication/secret/local-path/private-response scans. Commit the repair and additive lock before recovery; publish verified aggregate results in a separate commit afterward. No raw response, generated rationale, individual decision, prediction, mapping or per-file private inventory is public.

A read-only terminal viewer displays recovery phase, elapsed time and completed scoring folds out of five while the run is active. No idle monitoring is enabled. This recovery is expected to take minutes, so hourly scheduled monitoring is unnecessary unless it remains active that long. No E021 or changed analysis is authorized.
