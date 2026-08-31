# Publication audit

**Audit date:** 2026-08-31
**Repository purpose:** public, active research record for leakage-safe evaluation of mathematical-misconception detection.

## Publication allowlist

The initial public baseline may contain only:

- original Python source, tests, experiment configuration, and pinned Docker setup;
- protocol, limitations, literature/provenance notes, experiment log, and aggregate results expressed in reviewed documentation; and
- repository metadata and this audit.

It may not contain MAP files, student text, row-level data or predictions, frozen row-level split assignments, trained weights, archives, credentials, local absolute paths, caches, or private/restricted competition artifacts.

## Controls inspected

| Control | Result |
|---|---|
| Data and generated-output exclusion | `data/` and `artifacts/` are ignored in full; common tabular, archive, model, and row-level formats are also ignored. |
| Candidate source review | Documentation reports aggregate counts, hashes, schema names, metrics, and QuestionId-level aggregates only. It includes no response text or per-row output. |
| Credential scan | Source candidates were scanned for common key, token, password, authorization, and private-key markers. No credential material was found. |
| Local-path scan | Source candidates were scanned for Windows absolute paths and local data mount paths. No local absolute path is published. Docker's internal `/workspace` mount is configuration, not host data. |
| License and terms | The author-published dataset is not included. Its provenance and displayed MIT license are documented separately, with the former competition-terms conflict recorded. |
| Results policy | E001 is published as aggregate Markdown tables. The local JSON output and frozen row-level split assignment remain ignored. |

## Release gate

Before each push, run the tests, inspect `git status --ignored --short`, scan tracked candidates for secrets and absolute paths, and inspect `git diff --cached`. Reject any file outside the allowlist. Public commits must contain no raw data or row-level derivatives.

This audit records a technical publication review, not legal advice.
