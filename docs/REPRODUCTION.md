# Reproduction and verification

## Three different claims

| Level | Inputs | What this release verifies |
|---|---|---|
| Public verification | Repository only | Synthetic regression tests, E006 publication/reaggregation and E007–E010 schema/arithmetic checks, protected history, deterministic figures |
| Aggregate regeneration | Public E001 report and E010 JSON | Four static SVG figures and their numerical/provenance artifact; no model fitting |
| Historical modeling reproduction | Separately obtained MAP release, authenticated frozen assignments, historical environment and approved configuration | Prior execution records; **not freshly rerun in this release** |

Passing synthetic tests does not reproduce scientific predictions. Regenerating a figure does not independently replicate its source experiment. E006 is rechecked through its original allowlist sanitizer and aggregate recomputation; E007–E010 use their strict publication validators.

## Public checkout verification

Use Git and Docker with Linux containers. The lock targets **CPython 3.11, Linux amd64**; another architecture is outside this lock's verified scope. No MAP account, dataset, GPU, API key or encoder download is required. Allow package-index access during the build; verification itself runs without networking.

From the checkout root, PowerShell:

```powershell
docker build --platform linux/amd64 --pull --no-cache -t map-research-verify:2026-10 -f repro/Dockerfile repro
docker run --rm --network none --read-only --tmpfs /tmp:rw,nosuid,nodev --user 10001:10001 --cap-drop ALL --security-opt no-new-privileges --mount "type=bind,source=$($PWD.Path),target=/workspace,readonly" map-research-verify:2026-10
```

POSIX shell:

```sh
docker build --platform linux/amd64 --pull --no-cache -t map-research-verify:2026-10 -f repro/Dockerfile repro
docker run --rm --network none --read-only --tmpfs /tmp:rw,nosuid,nodev --user 10001:10001 --cap-drop ALL --security-opt no-new-privileges --mount "type=bind,source=$PWD,target=/workspace,readonly" map-research-verify:2026-10
```

The build context is **only `repro/`** and the Dockerfile copies only `core.lock`. It cannot package data, project credentials or model artifacts. The image adds a complete 15-package core runtime closure with pinned versions and wheel SHA-256 values to a digest-pinned interpreter image. Bundled pip/build utilities come from that base image; no editable installation or build-isolation dependency resolution occurs. The project is imported directly from `src/`.

PyTorch, sentence-transformers and pretrained weights are intentionally absent. This is a verification environment, not a replacement E004 encoder environment. The original `Dockerfile`, `compose.yaml`, `requirements.lock` and `pyproject.toml` are unchanged. Do not retag this image as `map-misconceptions:e001`.

CI in [.github/workflows/verify.yml](../.github/workflows/verify.yml) runs the same workflow against a public checkout, with read-only repository permissions and an immutable checkout-action revision. It does not obtain MAP data or run an experiment. A host Python 3 interpreter is used only for the standard-library publication check:

```sh
python repro/audit_release.py
```

The scanner examines tracked plus nonignored proposed files, rejects prohibited paths and binary formats, checks common secret/local-path patterns, rejects active SVG content, and verifies the historical inventory. This is a bounded automated check, not proof that every possible secret or privacy issue is absent. Human review remains required.

## Regenerate figures without fitting

The generator uses Python's standard library, so a host Python 3.10+ interpreter is sufficient:

```sh
python repro/make_figures.py
python repro/make_figures.py --check
```

For an entirely containerized regeneration, mount the checkout read-only and **only** `docs/figures` writable:

```sh
docker run --rm --network none --read-only --tmpfs /tmp:rw,nosuid,nodev --user 10001:10001 --cap-drop ALL --security-opt no-new-privileges --mount "type=bind,source=$PWD,target=/workspace,readonly" --mount "type=bind,source=$PWD/docs/figures,target=/workspace/docs/figures" map-research-verify:2026-10 python repro/make_figures.py
```

On Linux, the output directory must already exist and be writable by UID 10001; do not solve permissions by running the research container as root. SVG files are text-only, deterministic and contain no scripts or external resources. `figure_data.json` stores all plotted aggregates and source SHA-256 values. Text hashes normalize CRLF to LF for cross-platform checkouts; they are not claims of identical checkout line endings. E001 values retain the published three-decimal precision. E010 uses the existing full-precision aggregates. No bootstrap, permutation or model is rerun.

## Historical modeling reproduction is a separate workflow

1. Review [data provenance and licensing](DATA_AND_LICENSES.md). Acquire only the named author release; retain its notices. Do not substitute a third-party upload or closed-competition archive.
2. Store raw inputs under ignored `data/` and generated outputs under ignored `artifacts/`. Never commit them. Verify the training CSV SHA-256 against `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c`.
3. Preserve existing frozen assignments. `scripts/verify_frozen_inputs.py` validates the current dataset, row order, roles and assignment fingerprint without rewriting them. The assignment hash was first independently recorded during recovery, not authenticated before the original E001 run.
4. On a new research checkout only, review `scripts/inspect_dataset.py` and `scripts/make_grouped_folds.py` with the original seed 20260831 and five groups, then compare generated artifacts against the recorded fingerprints **before fitting**. Do not regenerate an established research checkout's folds to make a run pass.
5. Use the experiment-specific protocol, configuration, approval and execution record linked in the [index](EXPERIMENT_INDEX.md). E006–E010 Docker launchers enforce the recorded historical image and frozen references. They are not plug-and-play with this new verification image. Missing image/inputs or reference mismatches must stop reproduction rather than trigger substitutions.

Historical modeling image identity:

```text
sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c
```

That local image is not distributed by this release. The original direct-version lock lacks a complete hashed transitive/build closure. Rebuilding it today is not guaranteed to recreate the image, and the launchers deliberately reject a different identity. This release closes the **public verification** dependency gap, not the full historical modeling reconstruction gap. Do not relax identity checks or silently substitute versions.

## Preservation, private checks and monitoring

`repro/history.json` freezes 144 public files from commit `7bd41443e8a88024f05144d49902c69f9da76a08` and the existing experiment-log prefix. README is intentionally editable; the log accepts only append-only additions. All historical scientific source, tests, configurations, results and environment files are protected. Do not regenerate that inventory to bless a changed experiment.

For the data-owning research checkout only, `python repro/audit_release.py --private-prefixes` also checks proposed public text against normalized 40–80-character student-response prefixes. It prints counts only. This check needs local MAP data and is **not** part of CI; it cannot detect every shorter, transformed or paraphrased disclosure.

No modeling or monitor is active for this release. Future approved experiments use their existing read-only terminal viewers and at-most-hourly status updates while active. Stale status files alone do not prove a process is running.
