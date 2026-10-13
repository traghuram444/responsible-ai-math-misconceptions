# Experiment index

E001–E010 are complete. This index describes historical status; proposal text in frozen files is not silently rewritten. Read the [current synthesis](RESEARCH_REPORT.md) alongside the [append-only log](EXPERIMENT_LOG.md).

| ID | Purpose | Main outcome | Protocol / approval | Results / execution |
|---|---|---|---|---|
| E001 | Random versus held-question lexical baseline | 0.785 random versus 0.520 grouped MAP@3; frequency 0.539 | [Configuration](../experiments/baseline_tfidf_logreg.yaml) | [Results](E001_RESULTS.md) |
| E002 | Label support and exact overlap | 21.1% unsupported; 0.59% cross-question exact overlap | [Protocol](E002_PROTOCOL.md) | [Results](E002_RESULTS.md) |
| E003 | Supported-label diagnostic | Grouped TF–IDF 0.668 versus frequency 0.689 on supported labels | [Protocol](E003_PROTOCOL.md) | [Results](E003_RESULTS.md) |
| E004 | Frozen semantic embedding baseline | MiniLM 0.476 / 0.464 versus frequency 0.539; negative | [Historical protocol](E004_PROTOCOL.md) | [Retrospective archive](E004_RESULTS_ARCHIVE.md) |
| E005 | Transfer decomposition, Category and support | Support restriction does not eliminate collapse; rare stratum empty | [Historical protocol](E005_PROTOCOL.md) | [Retrospective archive](E005_RESULTS_ARCHIVE.md) |
| E006 | Confidence/support-aware selective prediction | Relative criterion met at 50% review; high retained risk remains | [Protocol](E006_PROTOCOL.md), [addendum](E006_REVIEW_ADDENDUM.md), [approval](../experiments/e006_approval.yaml) | [Results](E006_RESULTS.md), [JSON](../results/E006_aggregates.json), [execution](E006_EXECUTION_RECORD.md) |
| E007 | Development-selected fixed cutoffs | No admissible cutoff; all deferred; null risk is not zero | [Protocol](E007_PROTOCOL.md), [approval](../experiments/e007_approval.yaml) | [Results](E007_RESULTS.md), [JSON](../results/E007_aggregates.json), [execution](E007_EXECUTION_RECORD.md) |
| E008 | Development-only feasibility diagnosis | Primary cases show score-selection limitation; oracle unavailable in practice | [Protocol](E008_PROTOCOL.md), [approval](../experiments/e008_approval.yaml) | [Results](E008_RESULTS.md), [JSON](../results/E008_aggregates.json), [execution](E008_EXECUTION_RECORD.md) |
| E009 | Cross-fitted learned reliability | Ranking improvement; primary automation criterion still unmet | [Protocol](E009_PROTOCOL.md), [approval](../experiments/e009_approval.yaml) | [Results](E009_RESULTS.md), [JSON](../results/E009_aggregates.json), [execution](E009_EXECUTION_RECORD.md) |
| E010 | Fixed-budget review prioritization | Neither arm reaches primary meaningful-gain criterion | [Protocol](E010_PROTOCOL.md), [authorization](../experiments/e010_approval.yaml) | [Results](E010_RESULTS.md), [JSON](../results/E010_aggregates.json), [execution](E010_EXECUTION_RECORD.md) |

## Read before comparing experiments

- Frequency input arms duplicate one reference. Support subsets do not replace all-row primary scores.
- E004/E005 were committed retrospectively; historical Git preregistration is not claimed. Missing outputs and E005 discrepancies are documented in the [audit](REPRODUCIBILITY_AUDIT_2026_09.md).
- Legacy Brier needs the [erratum](METRIC_ERRATUM_2026_09.md). Do not compare uncorrected scores with E006 onward.
- E006 uses three temperature questions; E007 onward splits those into one temperature and two threshold-development questions. E008 is development-only.
- E009's fixed-cutoff and E010's meaningful-gain criteria answer different questions. A favorable secondary ranking metric replaces neither.
- E010 operational choices were agent-specified and committed before fitting under user authorization, not separately user-reviewed numerical choices.
- All uncertainty is descriptive on a repeatedly examined 15-question benchmark. No plot supplies independent replication.
