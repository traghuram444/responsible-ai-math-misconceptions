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
