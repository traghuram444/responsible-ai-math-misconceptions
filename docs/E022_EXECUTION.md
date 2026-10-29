# E022 execution record

## Approval and immutable protocol — 2026-10-29

The user approved execution of the exact E022 preregistration published at `e5e6708b9c745496e51bc909342e8c5880c22f49`. Its canonical LF SHA-256 is `cc635bb0f83407a0c2652bd0c717ecad5d9430a0a5c1168e9231abee737baef2`. The protocol document remains unchanged as the historical proposal; this append-only record establishes subsequent execution approval.

E022 evaluates L7 and fixed C50 with separate primary decisions at 20% error, alongside frequency context and secondary 10%/30% targets. The E007 one-temperature-question/two-cutoff-question allocation, exact distinct-score search, inclusive ties, 100-retained/10%-coverage floors and all-15-question rule are unchanged. There is no tuned ensemble, new classifier, new confidence score, new LLM call, human annotation or scientific-settings change. E001–E021, README, all prior failed/completed/recovered evidence and frozen folds remain unchanged; E018 stays blocked.

## Additive implementation and evaluation barriers

New E022 modules implement shared historical L reconstruction, fixed raw projection/fusion, separate temperatures, reporting, strict validation, preservation and one-shot orchestration. Historical scientific modules are imported read-only. Selection directly calls the existing E007 role, cutoff and mask helpers. The E001 temperature objective, clipping, bounds and optimizer defaults are reproduced exactly in an additive helper that also rejects optimizer failure; synthetic tests compare the returned values to E001. No historical helper is modified or monkeypatched in the actual run.

Each fold reconstructs exactly nine inner fits and one refit. L7 and C50 share L; no extra fitting for separate arms. Their temperatures use only the single assigned question. All nine policies for a fold are sealed before evaluation features are predicted/routed. After all five folds, private read-only arrays and hashed receipts freeze all forty-five policies, predictions and masks. Only then are evaluation labels passed to the reporting path. Existing G7 cache/completion/catalogue/input provenance is verified, with no new checker inference.

Before scoring, E021 raw F/L7/C50 probabilities, rankings, class/row/question alignment and base-model selection are reproduced; E007's derived calibration-role hashes must match. After the global freeze, all original fold/question/support exact-label metrics must reproduce. E021 final probabilities, temperatures and calibration/review metrics are deliberately not reused because the registered allocation changed. No new metric enters the live monitor before reproduction passes.

The strict public schema allows only registered numeric, Boolean, enumerated and hash fields. It checks all 600 unfiltered records, 900 retained records, 225 paired records, 135 gap records, 15 development records, 45 policies and nine decisions, including all empty cells. It verifies counts, support partitions, calibration eligibility and nulls, raw/final rank-metric identities, frequency all-or-none behavior, cutoff admissibility and all-question primary rules. Aggregate summaries, comparisons, gaps and decisions are rebuilt from their constituent records for verification. Public output contains no row-level predictions or private labels/text.

## Synthetic verification before any MAP computation

The E022-specific pinned Docker test suite passed **21 tests in 13.21 seconds**. Tests cover the complete invented reporting population; unknown/private fields and arithmetic corruption; exact historical temperature objective and optimizer failure; soft projection and fixed-mixture construction; rank preservation; rational cutoff boundaries and inclusive ties; nonmonotone selective risk; separate all-question primary conjunctions and empty-policy denominators; disjoint temperature/cutoff data; inner-only training and first-tie choice; all-fold freeze/hash corruption; historical raw/role reproduction; evaluation-label barriers; and independent phase-specific monitoring.

An initial synthetic test attempted to change a defined-fold count to its existing value and therefore did not exercise rejection. The test was corrected to change the value; no scientific implementation or setting was changed in response to MAP results. All testing used invented inputs; no E022 MAP fitting, calibration, cutoff search or scoring occurred before the implementation lock.

## Preservation, Docker and monitor

The additive lock captures the approved protocol, all new E022 implementation/launcher/publisher/tests and append-only documentation prefixes. Its private inventory captures all files committed at protocol approval and the complete existing E021 artifact set. Earlier nested gates preserve E001–E020, their original failures/recoveries, checker weights/caches and historical inventories. Public records include only inventory counts and digests. No inventory is overwritten.

Use pinned statistical image `sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0`, UID/GID10001, fixed seed20260831 and single numerical threads, no network, read-only root/project/history/data, dropped capabilities, no-new-privileges and tmpfs scratch. The sole persistent experiment write mount is the exclusive new `artifacts/e022_attempt01`. No system settings or files outside this project change.

The one-shot launcher is `python -B scripts/run_e022.py`, invoked only after complete tests/scans, the preparation commit and public verification. The independent viewer is `python -B scripts/run_e022.py --monitor`; it shows elapsed time and real progress in fits/50, policies/45 and scored folds/5. Viewer reads cannot launch, resume or retry computation. The viewer exits on completion/failure or absent execution; no idle follow-up is created. Scientific failures preserve the attempt and stop for review without an automatic retry.

## Completion and publication requirements

On completion the frozen publisher validates locks, preservation, strict schema and start/global-freeze/completion/cache hashes, then creates the complete numerical report and aggregate JSON exactly once. Run the full tests and publication/secret/local-path/private-response scans. Append numerical outcomes and verification here and in the experiment log; create a separate sanitized results commit to the approved personal repository and verify its public revision. Keep README and all other historical files unchanged. Present aggregate and all fold/question results before interpretation. No next experiment is authorized.

## Verified preflight — 2026-10-29

The complete pinned Docker suite passed **669 tests in 220.86 seconds**. The additive gate verified **366 historical files/prefixes**, in addition to all earlier nested preservation inventories. Ten protocol/implementation/test files are locked, with append-only execution/log prefixes. Lock byte SHA-256: `0dd2d4706e797cdcbae5340aadc3b63a511018a4e573dacea6bbdcd6871152f2`. The focused scan of all thirteen E022/protocol/log publication files checked **28,587** unique private response prefixes and found **zero matches**. No E022 MAP computation occurred during these checks.

The repository-wide private-response-prefix scan also passed with **zero matches** across all 28,587 prefixes. Publication path/text and original historical-prefix checks passed. The approved personal repository and public visibility were verified before staging preparation. The one-shot start receipt will record the exact preparation commit and unchanged lock hash; execution starts only after its public revision is verified.


## Completed numerical outcome - 2026-10-29

The approved one-shot attempt completed at 13:07:22 UTC, from preparation commit `6f54a1a498aaacd0599595ea6451a5ae3db965cd`. Statistical wall time was 934.655451 seconds; the live status recorded 935.218 seconds. All 50 classifier fits, 45 policies and five scored folds completed, with zero new checker calls, zero fit warnings and zero monitor I/O errors. No failure receipts were present. Global freeze, historical raw-model reproduction for all 15 arm/fold combinations, data/fold hashes and nested preservation checks passed before completion. The independent viewer stops when execution completes; no idle monitor was scheduled.

Aggregate SHA-256: `9578d9fc08c278751112fa1aadc52c0b1d6276e2a0b309d4ff54c455c2e6164f`. Global freeze receipt SHA-256: `f742b17fc43d553d5a8a6de95b79837ef58d1eab66db59d1f56df32072705964`. The preparation lock and protocol hashes remain as recorded above.

At the primary 20% error target, L7 had 0/5 admissible development cutoffs, zero retained evaluation cases and 0/15 questions jointly passing; its separate primary criterion was not met. C50 had 2/5 admissible cutoffs, four questions with retained cases and 1/15 questions jointly passing; its separate primary criterion was not met. Frequency had 0/5 admissible cutoffs and zero retained cases. Empty retained groups have undefined risk, accuracy and MAP@3, not zero error.

C50's primary five-fold coverage mean was 0.141592 (SD 0.213485, all five folds). Among its two nonempty folds, mean risk was 0.208691 (SD 0.045770), accuracy 0.791309, MAP@3 0.891717, ECE 0.114119 and Brier 0.350499. These conditional metrics use two defined folds; they are not five-fold risk estimates or matched-population model comparisons. Fold 0 retained 3,692 cases (coverage 0.480354, risk 0.176327, MAP@3 0.909534); fold 2 retained 1,705 (coverage 0.227606, risk 0.241056, MAP@3 0.873900). Folds 1, 3 and 4 retained none.

At the secondary 10% target, all arms retained zero cases. At 30%, L7 had 3/5 admissible cutoffs and 3/15 jointly passing questions; coverage mean was 0.246886 over five folds, risk mean 0.251594 and MAP@3 mean 0.819021 over three nonempty folds. C50 had 4/5 admissible cutoffs and 6/15 jointly passing questions; coverage mean was 0.389894 over five folds, risk mean 0.266017 and MAP@3 mean 0.827537 over four nonempty folds. Frequency retained none at 30%. Neither secondary all-question criterion was met. Secondary targets do not replace the primary decisions.

The frozen publisher is responsible for the complete registered numerical tables in `docs/E022_RESULTS.md` and `results/E022_aggregates.json`. Interpretation remains withheld pending user review. E001-E021, README, frozen folds and E018's blocked status remain unchanged. No further experiment has been started.


Post-run verification: the complete pinned Docker suite passed **669 tests in 213.80 seconds**. The independent terminal viewer exited after completion. Publication integrity and privacy checks are recorded separately when complete.


Final publication verification - 2026-10-29: the frozen publisher completed successfully exactly once. The public aggregate bytes match completion SHA-256 `9578d9fc08c278751112fa1aadc52c0b1d6276e2a0b309d4ff54c455c2e6164f`; strict schema, global freeze, cache provenance, all 366 additive preservation entries and earlier nested gates passed. The repository-wide scan passed for 366 publication files, with no matching secret/local-path patterns and zero matches across 28,587 unique private response prefixes. The original 144 protected public files and experiment-log prefix also passed. Post-run tests passed 669/669. Only the two E022 numerical outputs and append-only execution/log updates belong in the separate results commit; no private artifacts are published. Interpretation awaits user review.
