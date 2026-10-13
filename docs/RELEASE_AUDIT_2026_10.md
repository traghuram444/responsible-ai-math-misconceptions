# Research checkpoint audit

Date: 13 October 2026. Scope: documentation, aggregate figures and public-checkout verification after E010. No new research experiment, model fitting, threshold selection or data acquisition.

## Historical preservation

The inventory in [repro/history.json](../repro/history.json) records 144 existing public files at commit `7bd41443e8a88024f05144d49902c69f9da76a08`. Every historical scientific source file, test, result, protocol, configuration and environment file is protected. Only README changes and append-only additions to the existing experiment log are allowed outside new release files.

Hashes normalize CRLF to LF so the same protected content can be checked on Windows and Linux. The E001–E010 scientific record is unchanged; this convention is not an assertion that platform checkout line endings are identical. Private experiment artifacts are neither rewritten nor included in the inventory. The figure generator reads only the published E001 report and E010 JSON.

## Fresh environment verification

The separate verification image was built with `--pull --no-cache` from a digest-pinned Python 3.11.11 Linux amd64 image. All 15 added runtime packages have exact versions and wheel SHA-256 hashes; pip's dependency check passed. The image does not install the project through an editable build or include encoder dependencies. The original modeling image/tag is unchanged.

Locally observed verification image identity:

```text
sha256:82e688f599ba9cb92a5eef906670de8e12ac12f87d0ba056189ba29428cc4bd8
```

Image metadata/attestations may differ between rebuilds; identical image IDs are not promised. The immutable base and package hashes pin the tested inputs. This fresh build verifies the core test/report environment, **not** end-to-end historical MAP modeling or the full encoder dependency closure.

The initial complete check passed 312 tests in 55.13 seconds, all E007–E010 schema/arithmetic checks and all five deterministic figure artifacts. The final verification additionally checks E006 through its original sanitizer/reaggregation and adds citation, secret-pattern and documentation-link tests. Final check outcomes are recorded in the append-only release entry in the [experiment log](EXPERIMENT_LOG.md) and the public CI run.

Runtime controls: UID/GID 10001, no networking, read-only image and checkout, temporary writable `/tmp`, all Linux capabilities dropped, and no-new-privileges. Synthetic test fitting is not a MAP research experiment. CI receives no MAP data, student responses, models or credentials from this project.

## Publication checks and figure review

The publication checker covers tracked and proposed nonignored files, rejects data/artifact/cache paths and unapproved formats, and scans common secret and local-user-path patterns. All public aggregate files remain covered by preservation checks; E006–E010 also have content validation. SVG exports have no scripts, external links or embedded response content.

Four figures were rendered locally and visually inspected for legibility, clipping, units and signs. E001 is explicitly plotted at its published rounded precision. E010 includes both arms, all six rules, all registered review budgets, all five primary fold differences and all 15 questions per arm. The source fingerprints and plotted values are in [figure_data.json](figures/figure_data.json). Question-level benefits use the actual pooled-fold review allocations, not equal question budgets; no favorable questions are selected out.

Before publication, a separate data-owning-checkout audit checks public text against normalized 40–80-character response prefixes, printing only counts. Its final result is recorded in the experiment-log release entry. This is a bounded disclosure check, not a guarantee against short excerpts, paraphrases or every credential format. CI performs only the public static checks and never downloads MAP.

## Remaining limitations

- The historical full modeling dependency closure is still incompletely hash-locked. The original local image is not distributed. A passing fresh verification build must not be described as fresh reproduction of E001–E010 predictions.
- Historical E004/E005 publication timing, incomplete secondary reporting, E005 calibration eligibility/seed discrepancies and legacy Brier defects remain documented. No historical file is silently corrected by this checkpoint.
- Five overlapping folds and 15 repeatedly examined questions support descriptive evidence, not broad educational effectiveness or deployment guarantees.
- License provenance is retained from the documented author release. This checkpoint does not reinterpret the separate competition license or claim a legal chain-of-title opinion.

The release is a **research prerelease**, with original negative results and active-research status prominent. It contains no E011 experiment or deployment recommendation.
