# E009 — learned-reliability results

Status: **COMPLETED**. Numerical results only; interpretation and any next experiment await user review.

Fixed classifier, nested question-held-out reliability training, and unchanged E007 outer folds/temperature/threshold criteria. Primary target 20%; secondary 10% and 30%. All uncertainty is descriptive on a repeatedly examined 15-question benchmark, not independent confirmation or a deployment guarantee.

Equal-fold means ± sample SD [defined folds]. Null retained risk is undefined, not zero. Frequency repeats the same reference across arms. Comparisons at a common target may retain different populations/coverage.

[Complete aggregate/fold/question/stratum JSON](../results/E009_aggregates.json) includes all five values for numeric fold summaries, original classifier calibration, separate reliability calibration, eligibility reasons, inner-block audit counts and reproduction checks.

## Registered transfer criteria

| Target | Arm | Rule | Admissible / 5 | Nonempty / 15 | Count floor / 15 | Coverage floor / 15 | Both floors / 15 | Risk met / 15 | Risk exceeded / nonempty | Max question risk | Criterion met |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 20% | explanation_only | learned_reliability | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | explanation_only | confidence_only | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | explanation_only | support_aware | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | explanation_only | raw_confidence | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | explanation_only | frequency | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | question_plus_explanation | learned_reliability | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | question_plus_explanation | confidence_only | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | question_plus_explanation | support_aware | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | question_plus_explanation | raw_confidence | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 20% | question_plus_explanation | frequency | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | explanation_only | learned_reliability | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | explanation_only | confidence_only | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | explanation_only | support_aware | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | explanation_only | raw_confidence | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | explanation_only | frequency | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | question_plus_explanation | learned_reliability | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | question_plus_explanation | confidence_only | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | question_plus_explanation | support_aware | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | question_plus_explanation | raw_confidence | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 10% | question_plus_explanation | frequency | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | explanation_only | learned_reliability | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | explanation_only | confidence_only | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | explanation_only | support_aware | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | explanation_only | raw_confidence | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | explanation_only | frequency | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | question_plus_explanation | learned_reliability | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | question_plus_explanation | confidence_only | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | question_plus_explanation | support_aware | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | question_plus_explanation | raw_confidence | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |
| 30% | question_plus_explanation | frequency | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | null | False |

## Aggregate all-case results

| Arm | Rule | Target | Coverage | Accuracy | MAP@3 | Risk | Classifier ECE | Multiclass Brier |
|---|---|---|---|---|---|---|---|---|
| explanation_only | learned_reliability | Unfiltered | 1 ± 0 [5] | 0.35370258 ± 0.052241491 [5] | 0.49685335 ± 0.03388943 [5] | 0.64629742 ± 0.052241491 [5] | 0.16834121 ± 0.085155604 [5] | 0.848443 ± 0.042847589 [5] |
| explanation_only | learned_reliability | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | learned_reliability | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | learned_reliability | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | confidence_only | Unfiltered | 1 ± 0 [5] | 0.35370258 ± 0.052241491 [5] | 0.49685335 ± 0.03388943 [5] | 0.64629742 ± 0.052241491 [5] | 0.16834121 ± 0.085155604 [5] | 0.848443 ± 0.042847589 [5] |
| explanation_only | confidence_only | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | confidence_only | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | confidence_only | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | support_aware | Unfiltered | 1 ± 0 [5] | 0.35370258 ± 0.052241491 [5] | 0.49685335 ± 0.03388943 [5] | 0.64629742 ± 0.052241491 [5] | 0.16834121 ± 0.085155604 [5] | 0.848443 ± 0.042847589 [5] |
| explanation_only | support_aware | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | support_aware | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | support_aware | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | raw_confidence | Unfiltered | 1 ± 0 [5] | 0.35370258 ± 0.052241491 [5] | 0.49685335 ± 0.03388943 [5] | 0.64629742 ± 0.052241491 [5] | 0.16834121 ± 0.085155604 [5] | 0.848443 ± 0.042847589 [5] |
| explanation_only | raw_confidence | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | raw_confidence | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | raw_confidence | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | frequency | Unfiltered | 1 ± 0 [5] | 0.40200945 ± 0.050064249 [5] | 0.53921498 ± 0.039203937 [5] | 0.59799055 ± 0.050064249 [5] | 0.056271279 ± 0.034632786 [5] | 0.79505714 ± 0.028763396 [5] |
| explanation_only | frequency | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | frequency | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| explanation_only | frequency | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | learned_reliability | Unfiltered | 1 ± 0 [5] | 0.3763057 ± 0.052035768 [5] | 0.51997115 ± 0.037798614 [5] | 0.6236943 ± 0.052035768 [5] | 0.16319539 ± 0.12155265 [5] | 0.82716724 ± 0.058119044 [5] |
| question_plus_explanation | learned_reliability | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | learned_reliability | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | learned_reliability | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | confidence_only | Unfiltered | 1 ± 0 [5] | 0.3763057 ± 0.052035768 [5] | 0.51997115 ± 0.037798614 [5] | 0.6236943 ± 0.052035768 [5] | 0.16319539 ± 0.12155265 [5] | 0.82716724 ± 0.058119044 [5] |
| question_plus_explanation | confidence_only | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | confidence_only | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | confidence_only | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | support_aware | Unfiltered | 1 ± 0 [5] | 0.3763057 ± 0.052035768 [5] | 0.51997115 ± 0.037798614 [5] | 0.6236943 ± 0.052035768 [5] | 0.16319539 ± 0.12155265 [5] | 0.82716724 ± 0.058119044 [5] |
| question_plus_explanation | support_aware | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | support_aware | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | support_aware | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | raw_confidence | Unfiltered | 1 ± 0 [5] | 0.3763057 ± 0.052035768 [5] | 0.51997115 ± 0.037798614 [5] | 0.6236943 ± 0.052035768 [5] | 0.16319539 ± 0.12155265 [5] | 0.82716724 ± 0.058119044 [5] |
| question_plus_explanation | raw_confidence | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | raw_confidence | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | raw_confidence | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | frequency | Unfiltered | 1 ± 0 [5] | 0.40200945 ± 0.050064249 [5] | 0.53921498 ± 0.039203937 [5] | 0.59799055 ± 0.050064249 [5] | 0.056271279 ± 0.034632786 [5] | 0.79505714 ± 0.028763396 [5] |
| question_plus_explanation | frequency | 10 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | frequency | 20 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |
| question_plus_explanation | frequency | 30 | 0 ± 0 [5] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] | null ± null [0] |

## All fold-level results

| Arm | Fold | Rule | Target | Cutoff | Retained / original | Coverage | Accuracy | MAP@3 | Risk | Classifier ECE | Multiclass Brier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| explanation_only | 0 | learned_reliability | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.33216237 | 0.47519299 | 0.66783763 | 0.21574408 | 0.88779982 |
| explanation_only | 0 | learned_reliability | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | learned_reliability | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | learned_reliability | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | confidence_only | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.33216237 | 0.47519299 | 0.66783763 | 0.21574408 | 0.88779982 |
| explanation_only | 0 | confidence_only | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | confidence_only | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | confidence_only | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | support_aware | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.33216237 | 0.47519299 | 0.66783763 | 0.21574408 | 0.88779982 |
| explanation_only | 0 | support_aware | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | support_aware | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | support_aware | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | raw_confidence | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.33216237 | 0.47519299 | 0.66783763 | 0.21574408 | 0.88779982 |
| explanation_only | 0 | raw_confidence | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | raw_confidence | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | raw_confidence | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | frequency | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.48581837 | 0.59181195 | 0.51418163 | 0.11264674 | 0.75585416 |
| explanation_only | 0 | frequency | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | frequency | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 0 | frequency | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| explanation_only | 1 | learned_reliability | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.2819308 | 0.45332004 | 0.7180692 | 0.2186875 | 0.89451124 |
| explanation_only | 1 | learned_reliability | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | learned_reliability | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | learned_reliability | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | confidence_only | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.2819308 | 0.45332004 | 0.7180692 | 0.2186875 | 0.89451124 |
| explanation_only | 1 | confidence_only | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | confidence_only | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | confidence_only | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | support_aware | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.2819308 | 0.45332004 | 0.7180692 | 0.2186875 | 0.89451124 |
| explanation_only | 1 | support_aware | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | support_aware | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | support_aware | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | raw_confidence | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.2819308 | 0.45332004 | 0.7180692 | 0.2186875 | 0.89451124 |
| explanation_only | 1 | raw_confidence | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | raw_confidence | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | raw_confidence | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | frequency | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.35896341 | 0.5018036 | 0.64103659 | 0.055844253 | 0.82352498 |
| explanation_only | 1 | frequency | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | frequency | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 1 | frequency | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| explanation_only | 2 | learned_reliability | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.34481378 | 0.49933253 | 0.65518622 | 0.020030233 | 0.80368179 |
| explanation_only | 2 | learned_reliability | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | learned_reliability | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | learned_reliability | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | confidence_only | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.34481378 | 0.49933253 | 0.65518622 | 0.020030233 | 0.80368179 |
| explanation_only | 2 | confidence_only | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | confidence_only | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | confidence_only | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | support_aware | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.34481378 | 0.49933253 | 0.65518622 | 0.020030233 | 0.80368179 |
| explanation_only | 2 | support_aware | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | support_aware | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | support_aware | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | raw_confidence | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.34481378 | 0.49933253 | 0.65518622 | 0.020030233 | 0.80368179 |
| explanation_only | 2 | raw_confidence | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | raw_confidence | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | raw_confidence | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | frequency | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.39540782 | 0.53882437 | 0.60459218 | 0.045889176 | 0.79378899 |
| explanation_only | 2 | frequency | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | frequency | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 2 | frequency | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| explanation_only | 3 | learned_reliability | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.40487942 | 0.51687585 | 0.59512058 | 0.21541354 | 0.84863038 |
| explanation_only | 3 | learned_reliability | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | learned_reliability | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | learned_reliability | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | confidence_only | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.40487942 | 0.51687585 | 0.59512058 | 0.21541354 | 0.84863038 |
| explanation_only | 3 | confidence_only | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | confidence_only | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | confidence_only | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | support_aware | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.40487942 | 0.51687585 | 0.59512058 | 0.21541354 | 0.84863038 |
| explanation_only | 3 | support_aware | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | support_aware | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | support_aware | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | raw_confidence | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.40487942 | 0.51687585 | 0.59512058 | 0.21541354 | 0.84863038 |
| explanation_only | 3 | raw_confidence | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | raw_confidence | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | raw_confidence | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | frequency | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.36877732 | 0.50122221 | 0.63122268 | 0.048873362 | 0.82213474 |
| explanation_only | 3 | frequency | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | frequency | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 3 | frequency | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| explanation_only | 4 | learned_reliability | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.40472654 | 0.53954535 | 0.59527346 | 0.17183069 | 0.8075918 |
| explanation_only | 4 | learned_reliability | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | learned_reliability | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | learned_reliability | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | confidence_only | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.40472654 | 0.53954535 | 0.59527346 | 0.17183069 | 0.8075918 |
| explanation_only | 4 | confidence_only | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | confidence_only | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | confidence_only | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | support_aware | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.40472654 | 0.53954535 | 0.59527346 | 0.17183069 | 0.8075918 |
| explanation_only | 4 | support_aware | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | support_aware | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | support_aware | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | raw_confidence | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.40472654 | 0.53954535 | 0.59527346 | 0.17183069 | 0.8075918 |
| explanation_only | 4 | raw_confidence | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | raw_confidence | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | raw_confidence | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | frequency | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.40108035 | 0.56241278 | 0.59891965 | 0.018102867 | 0.77998281 |
| explanation_only | 4 | frequency | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | frequency | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| explanation_only | 4 | frequency | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | learned_reliability | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.39214156 | 0.52159771 | 0.60785844 | 0.2354524 | 0.84782063 |
| question_plus_explanation | 0 | learned_reliability | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | learned_reliability | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | learned_reliability | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | confidence_only | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.39214156 | 0.52159771 | 0.60785844 | 0.2354524 | 0.84782063 |
| question_plus_explanation | 0 | confidence_only | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | confidence_only | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | confidence_only | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | support_aware | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.39214156 | 0.52159771 | 0.60785844 | 0.2354524 | 0.84782063 |
| question_plus_explanation | 0 | support_aware | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | support_aware | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | support_aware | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | raw_confidence | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.39214156 | 0.52159771 | 0.60785844 | 0.2354524 | 0.84782063 |
| question_plus_explanation | 0 | raw_confidence | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | raw_confidence | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | raw_confidence | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | frequency | Unfiltered | Unfiltered | 7686 / 7686 | 1 | 0.48581837 | 0.59181195 | 0.51418163 | 0.11264674 | 0.75585416 |
| question_plus_explanation | 0 | frequency | 10 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | frequency | 20 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 0 | frequency | 30 | NONE | 0 / 7686 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | learned_reliability | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.30029902 | 0.47135602 | 0.69970098 | 0.085969181 | 0.83256243 |
| question_plus_explanation | 1 | learned_reliability | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | learned_reliability | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | learned_reliability | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | confidence_only | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.30029902 | 0.47135602 | 0.69970098 | 0.085969181 | 0.83256243 |
| question_plus_explanation | 1 | confidence_only | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | confidence_only | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | confidence_only | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | support_aware | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.30029902 | 0.47135602 | 0.69970098 | 0.085969181 | 0.83256243 |
| question_plus_explanation | 1 | support_aware | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | support_aware | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | support_aware | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | raw_confidence | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.30029902 | 0.47135602 | 0.69970098 | 0.085969181 | 0.83256243 |
| question_plus_explanation | 1 | raw_confidence | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | raw_confidence | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | raw_confidence | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | frequency | Unfiltered | Unfiltered | 7023 / 7023 | 1 | 0.35896341 | 0.5018036 | 0.64103659 | 0.055844253 | 0.82352498 |
| question_plus_explanation | 1 | frequency | 10 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | frequency | 20 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 1 | frequency | 30 | NONE | 0 / 7023 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | learned_reliability | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.35015352 | 0.50812086 | 0.64984648 | 0.024472018 | 0.79055821 |
| question_plus_explanation | 2 | learned_reliability | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | learned_reliability | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | learned_reliability | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | confidence_only | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.35015352 | 0.50812086 | 0.64984648 | 0.024472018 | 0.79055821 |
| question_plus_explanation | 2 | confidence_only | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | confidence_only | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | confidence_only | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | support_aware | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.35015352 | 0.50812086 | 0.64984648 | 0.024472018 | 0.79055821 |
| question_plus_explanation | 2 | support_aware | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | support_aware | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | support_aware | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | raw_confidence | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.35015352 | 0.50812086 | 0.64984648 | 0.024472018 | 0.79055821 |
| question_plus_explanation | 2 | raw_confidence | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | raw_confidence | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | raw_confidence | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | frequency | Unfiltered | Unfiltered | 7491 / 7491 | 1 | 0.39540782 | 0.53882437 | 0.60459218 | 0.045889176 | 0.79378899 |
| question_plus_explanation | 2 | frequency | 10 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | frequency | 20 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 2 | frequency | 30 | NONE | 0 / 7491 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | learned_reliability | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.40544352 | 0.52221125 | 0.59455648 | 0.33082077 | 0.90880073 |
| question_plus_explanation | 3 | learned_reliability | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | learned_reliability | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | learned_reliability | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | confidence_only | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.40544352 | 0.52221125 | 0.59455648 | 0.33082077 | 0.90880073 |
| question_plus_explanation | 3 | confidence_only | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | confidence_only | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | confidence_only | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | support_aware | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.40544352 | 0.52221125 | 0.59455648 | 0.33082077 | 0.90880073 |
| question_plus_explanation | 3 | support_aware | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | support_aware | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | support_aware | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | raw_confidence | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.40544352 | 0.52221125 | 0.59455648 | 0.33082077 | 0.90880073 |
| question_plus_explanation | 3 | raw_confidence | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | raw_confidence | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | raw_confidence | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | frequency | Unfiltered | Unfiltered | 7091 / 7091 | 1 | 0.36877732 | 0.50122221 | 0.63122268 | 0.048873362 | 0.82213474 |
| question_plus_explanation | 3 | frequency | 10 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | frequency | 20 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 3 | frequency | 30 | NONE | 0 / 7091 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | learned_reliability | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.43349088 | 0.57656989 | 0.56650912 | 0.13926257 | 0.75609422 |
| question_plus_explanation | 4 | learned_reliability | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | learned_reliability | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | learned_reliability | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | confidence_only | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.43349088 | 0.57656989 | 0.56650912 | 0.13926257 | 0.75609422 |
| question_plus_explanation | 4 | confidence_only | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | confidence_only | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | confidence_only | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | support_aware | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.43349088 | 0.57656989 | 0.56650912 | 0.13926257 | 0.75609422 |
| question_plus_explanation | 4 | support_aware | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | support_aware | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | support_aware | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | raw_confidence | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.43349088 | 0.57656989 | 0.56650912 | 0.13926257 | 0.75609422 |
| question_plus_explanation | 4 | raw_confidence | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | raw_confidence | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | raw_confidence | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | frequency | Unfiltered | Unfiltered | 7405 / 7405 | 1 | 0.40108035 | 0.56241278 | 0.59891965 | 0.018102867 | 0.77998281 |
| question_plus_explanation | 4 | frequency | 10 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | frequency | 20 | NONE | 0 / 7405 | 0 | null | null | null | null | null |
| question_plus_explanation | 4 | frequency | 30 | NONE | 0 / 7405 | 0 | null | null | null | null | null |

## All evaluation-question results

| Arm | Fold | Question | Rule | Target | Retained / original | Coverage | Accuracy | MAP@3 | Risk | Risk minus target | Risk minus development | ECE | Brier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| explanation_only | 0 | 31772 | learned_reliability | Unfiltered | 4857 / 4857 | 1 | 0.34403953 | 0.47347471 | 0.65596047 | null | null | 0.2031329 | 0.88024522 |
| explanation_only | 0 | 32829 | learned_reliability | Unfiltered | 2156 / 2156 | 1 | 0.35250464 | 0.52643785 | 0.64749536 | null | null | 0.19267021 | 0.83866896 |
| explanation_only | 0 | 104665 | learned_reliability | Unfiltered | 673 / 673 | 1 | 0.18127786 | 0.32342744 | 0.81872214 | null | null | 0.38067686 | 1.0997149 |
| explanation_only | 0 | 31772 | learned_reliability | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | learned_reliability | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | learned_reliability | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | learned_reliability | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | learned_reliability | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | learned_reliability | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | learned_reliability | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | learned_reliability | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | learned_reliability | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | confidence_only | Unfiltered | 4857 / 4857 | 1 | 0.34403953 | 0.47347471 | 0.65596047 | null | null | 0.2031329 | 0.88024522 |
| explanation_only | 0 | 32829 | confidence_only | Unfiltered | 2156 / 2156 | 1 | 0.35250464 | 0.52643785 | 0.64749536 | null | null | 0.19267021 | 0.83866896 |
| explanation_only | 0 | 104665 | confidence_only | Unfiltered | 673 / 673 | 1 | 0.18127786 | 0.32342744 | 0.81872214 | null | null | 0.38067686 | 1.0997149 |
| explanation_only | 0 | 31772 | confidence_only | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | confidence_only | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | confidence_only | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | confidence_only | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | confidence_only | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | confidence_only | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | confidence_only | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | confidence_only | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | confidence_only | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | support_aware | Unfiltered | 4857 / 4857 | 1 | 0.34403953 | 0.47347471 | 0.65596047 | null | null | 0.2031329 | 0.88024522 |
| explanation_only | 0 | 32829 | support_aware | Unfiltered | 2156 / 2156 | 1 | 0.35250464 | 0.52643785 | 0.64749536 | null | null | 0.19267021 | 0.83866896 |
| explanation_only | 0 | 104665 | support_aware | Unfiltered | 673 / 673 | 1 | 0.18127786 | 0.32342744 | 0.81872214 | null | null | 0.38067686 | 1.0997149 |
| explanation_only | 0 | 31772 | support_aware | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | support_aware | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | support_aware | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | support_aware | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | support_aware | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | support_aware | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | support_aware | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | support_aware | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | support_aware | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | raw_confidence | Unfiltered | 4857 / 4857 | 1 | 0.34403953 | 0.47347471 | 0.65596047 | null | null | 0.2031329 | 0.88024522 |
| explanation_only | 0 | 32829 | raw_confidence | Unfiltered | 2156 / 2156 | 1 | 0.35250464 | 0.52643785 | 0.64749536 | null | null | 0.19267021 | 0.83866896 |
| explanation_only | 0 | 104665 | raw_confidence | Unfiltered | 673 / 673 | 1 | 0.18127786 | 0.32342744 | 0.81872214 | null | null | 0.38067686 | 1.0997149 |
| explanation_only | 0 | 31772 | raw_confidence | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | raw_confidence | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | raw_confidence | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | raw_confidence | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | raw_confidence | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | raw_confidence | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | raw_confidence | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | raw_confidence | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | raw_confidence | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | frequency | Unfiltered | 4857 / 4857 | 1 | 0.35392217 | 0.48586233 | 0.64607783 | null | null | 0.019249461 | 0.83175074 |
| explanation_only | 0 | 32829 | frequency | Unfiltered | 2156 / 2156 | 1 | 0.73283859 | 0.79081633 | 0.26716141 | null | null | 0.35966696 | 0.61324346 |
| explanation_only | 0 | 104665 | frequency | Unfiltered | 673 / 673 | 1 | 0.64635958 | 0.71892026 | 0.35364042 | null | null | 0.27318795 | 0.66497603 |
| explanation_only | 0 | 31772 | frequency | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | frequency | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | frequency | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | frequency | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | frequency | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | frequency | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 31772 | frequency | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 32829 | frequency | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| explanation_only | 0 | 104665 | frequency | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | learned_reliability | Unfiltered | 3640 / 3640 | 1 | 0.31978022 | 0.43878205 | 0.68021978 | null | null | 0.18867852 | 0.88021149 |
| explanation_only | 1 | 32835 | learned_reliability | Unfiltered | 2332 / 2332 | 1 | 0.22298456 | 0.45833333 | 0.77701544 | null | null | 0.27983445 | 0.93935406 |
| explanation_only | 1 | 109465 | learned_reliability | Unfiltered | 1051 / 1051 | 1 | 0.28163654 | 0.49254678 | 0.71836346 | null | null | 0.18807734 | 0.84453752 |
| explanation_only | 1 | 31778 | learned_reliability | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | learned_reliability | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | learned_reliability | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | learned_reliability | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | learned_reliability | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | learned_reliability | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | learned_reliability | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | learned_reliability | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | learned_reliability | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | confidence_only | Unfiltered | 3640 / 3640 | 1 | 0.31978022 | 0.43878205 | 0.68021978 | null | null | 0.18867852 | 0.88021149 |
| explanation_only | 1 | 32835 | confidence_only | Unfiltered | 2332 / 2332 | 1 | 0.22298456 | 0.45833333 | 0.77701544 | null | null | 0.27983445 | 0.93935406 |
| explanation_only | 1 | 109465 | confidence_only | Unfiltered | 1051 / 1051 | 1 | 0.28163654 | 0.49254678 | 0.71836346 | null | null | 0.18807734 | 0.84453752 |
| explanation_only | 1 | 31778 | confidence_only | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | confidence_only | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | confidence_only | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | confidence_only | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | confidence_only | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | confidence_only | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | confidence_only | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | confidence_only | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | confidence_only | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | support_aware | Unfiltered | 3640 / 3640 | 1 | 0.31978022 | 0.43878205 | 0.68021978 | null | null | 0.18867852 | 0.88021149 |
| explanation_only | 1 | 32835 | support_aware | Unfiltered | 2332 / 2332 | 1 | 0.22298456 | 0.45833333 | 0.77701544 | null | null | 0.27983445 | 0.93935406 |
| explanation_only | 1 | 109465 | support_aware | Unfiltered | 1051 / 1051 | 1 | 0.28163654 | 0.49254678 | 0.71836346 | null | null | 0.18807734 | 0.84453752 |
| explanation_only | 1 | 31778 | support_aware | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | support_aware | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | support_aware | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | support_aware | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | support_aware | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | support_aware | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | support_aware | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | support_aware | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | support_aware | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | raw_confidence | Unfiltered | 3640 / 3640 | 1 | 0.31978022 | 0.43878205 | 0.68021978 | null | null | 0.18867852 | 0.88021149 |
| explanation_only | 1 | 32835 | raw_confidence | Unfiltered | 2332 / 2332 | 1 | 0.22298456 | 0.45833333 | 0.77701544 | null | null | 0.27983445 | 0.93935406 |
| explanation_only | 1 | 109465 | raw_confidence | Unfiltered | 1051 / 1051 | 1 | 0.28163654 | 0.49254678 | 0.71836346 | null | null | 0.18807734 | 0.84453752 |
| explanation_only | 1 | 31778 | raw_confidence | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | raw_confidence | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | raw_confidence | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | raw_confidence | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | raw_confidence | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | raw_confidence | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | raw_confidence | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | raw_confidence | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | raw_confidence | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | frequency | Unfiltered | 3640 / 3640 | 1 | 0.31318681 | 0.43598901 | 0.68681319 | null | null | 0.10162085 | 0.87769413 |
| explanation_only | 1 | 32835 | frequency | Unfiltered | 2332 / 2332 | 1 | 0.40909091 | 0.56546598 | 0.59090909 | null | null | 0.0057167494 | 0.76931696 |
| explanation_only | 1 | 109465 | frequency | Unfiltered | 1051 / 1051 | 1 | 0.40627973 | 0.58848716 | 0.59372027 | null | null | 0.0085279249 | 0.75619618 |
| explanation_only | 1 | 31778 | frequency | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | frequency | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | frequency | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | frequency | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | frequency | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | frequency | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 31778 | frequency | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 32835 | frequency | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| explanation_only | 1 | 109465 | frequency | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | learned_reliability | Unfiltered | 3115 / 3115 | 1 | 0.43756019 | 0.57153558 | 0.56243981 | null | null | 0.054037744 | 0.73508695 |
| explanation_only | 2 | 33474 | learned_reliability | Unfiltered | 1766 / 1766 | 1 | 0.24745187 | 0.3990185 | 0.75254813 | null | null | 0.069497621 | 0.89086307 |
| explanation_only | 2 | 91695 | learned_reliability | Unfiltered | 2610 / 2610 | 1 | 0.3 | 0.48103448 | 0.7 | null | null | 0.034316457 | 0.82655948 |
| explanation_only | 2 | 31774 | learned_reliability | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | learned_reliability | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | learned_reliability | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | learned_reliability | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | learned_reliability | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | learned_reliability | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | learned_reliability | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | learned_reliability | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | learned_reliability | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | confidence_only | Unfiltered | 3115 / 3115 | 1 | 0.43756019 | 0.57153558 | 0.56243981 | null | null | 0.054037744 | 0.73508695 |
| explanation_only | 2 | 33474 | confidence_only | Unfiltered | 1766 / 1766 | 1 | 0.24745187 | 0.3990185 | 0.75254813 | null | null | 0.069497621 | 0.89086307 |
| explanation_only | 2 | 91695 | confidence_only | Unfiltered | 2610 / 2610 | 1 | 0.3 | 0.48103448 | 0.7 | null | null | 0.034316457 | 0.82655948 |
| explanation_only | 2 | 31774 | confidence_only | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | confidence_only | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | confidence_only | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | confidence_only | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | confidence_only | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | confidence_only | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | confidence_only | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | confidence_only | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | confidence_only | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | support_aware | Unfiltered | 3115 / 3115 | 1 | 0.43756019 | 0.57153558 | 0.56243981 | null | null | 0.054037744 | 0.73508695 |
| explanation_only | 2 | 33474 | support_aware | Unfiltered | 1766 / 1766 | 1 | 0.24745187 | 0.3990185 | 0.75254813 | null | null | 0.069497621 | 0.89086307 |
| explanation_only | 2 | 91695 | support_aware | Unfiltered | 2610 / 2610 | 1 | 0.3 | 0.48103448 | 0.7 | null | null | 0.034316457 | 0.82655948 |
| explanation_only | 2 | 31774 | support_aware | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | support_aware | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | support_aware | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | support_aware | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | support_aware | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | support_aware | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | support_aware | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | support_aware | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | support_aware | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | raw_confidence | Unfiltered | 3115 / 3115 | 1 | 0.43756019 | 0.57153558 | 0.56243981 | null | null | 0.054037744 | 0.73508695 |
| explanation_only | 2 | 33474 | raw_confidence | Unfiltered | 1766 / 1766 | 1 | 0.24745187 | 0.3990185 | 0.75254813 | null | null | 0.069497621 | 0.89086307 |
| explanation_only | 2 | 91695 | raw_confidence | Unfiltered | 2610 / 2610 | 1 | 0.3 | 0.48103448 | 0.7 | null | null | 0.034316457 | 0.82655948 |
| explanation_only | 2 | 31774 | raw_confidence | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | raw_confidence | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | raw_confidence | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | raw_confidence | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | raw_confidence | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | raw_confidence | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | raw_confidence | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | raw_confidence | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | raw_confidence | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | frequency | Unfiltered | 3115 / 3115 | 1 | 0.45104334 | 0.59384698 | 0.54895666 | null | null | 0.0097463404 | 0.74418345 |
| explanation_only | 2 | 33474 | frequency | Unfiltered | 1766 / 1766 | 1 | 0.18289921 | 0.3689128 | 0.81710079 | null | null | 0.25839779 | 0.95008875 |
| explanation_only | 2 | 91695 | frequency | Unfiltered | 2610 / 2610 | 1 | 0.47279693 | 0.58812261 | 0.52720307 | null | null | 0.031499937 | 0.74723568 |
| explanation_only | 2 | 31774 | frequency | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | frequency | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | frequency | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | frequency | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | frequency | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | frequency | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 31774 | frequency | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 33474 | frequency | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| explanation_only | 2 | 91695 | frequency | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | learned_reliability | Unfiltered | 3105 / 3105 | 1 | 0.3610306 | 0.46763285 | 0.6389694 | null | null | 0.27665499 | 0.93698038 |
| explanation_only | 3 | 33472 | learned_reliability | Unfiltered | 2800 / 2800 | 1 | 0.4525 | 0.57130952 | 0.5475 | null | null | 0.16182289 | 0.7581397 |
| explanation_only | 3 | 76870 | learned_reliability | Unfiltered | 1186 / 1186 | 1 | 0.40725126 | 0.51728499 | 0.59274874 | null | null | 0.18160169 | 0.83096356 |
| explanation_only | 3 | 32833 | learned_reliability | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | learned_reliability | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | learned_reliability | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | learned_reliability | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | learned_reliability | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | learned_reliability | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | learned_reliability | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | learned_reliability | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | learned_reliability | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | confidence_only | Unfiltered | 3105 / 3105 | 1 | 0.3610306 | 0.46763285 | 0.6389694 | null | null | 0.27665499 | 0.93698038 |
| explanation_only | 3 | 33472 | confidence_only | Unfiltered | 2800 / 2800 | 1 | 0.4525 | 0.57130952 | 0.5475 | null | null | 0.16182289 | 0.7581397 |
| explanation_only | 3 | 76870 | confidence_only | Unfiltered | 1186 / 1186 | 1 | 0.40725126 | 0.51728499 | 0.59274874 | null | null | 0.18160169 | 0.83096356 |
| explanation_only | 3 | 32833 | confidence_only | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | confidence_only | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | confidence_only | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | confidence_only | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | confidence_only | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | confidence_only | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | confidence_only | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | confidence_only | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | confidence_only | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | support_aware | Unfiltered | 3105 / 3105 | 1 | 0.3610306 | 0.46763285 | 0.6389694 | null | null | 0.27665499 | 0.93698038 |
| explanation_only | 3 | 33472 | support_aware | Unfiltered | 2800 / 2800 | 1 | 0.4525 | 0.57130952 | 0.5475 | null | null | 0.16182289 | 0.7581397 |
| explanation_only | 3 | 76870 | support_aware | Unfiltered | 1186 / 1186 | 1 | 0.40725126 | 0.51728499 | 0.59274874 | null | null | 0.18160169 | 0.83096356 |
| explanation_only | 3 | 32833 | support_aware | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | support_aware | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | support_aware | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | support_aware | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | support_aware | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | support_aware | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | support_aware | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | support_aware | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | support_aware | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | raw_confidence | Unfiltered | 3105 / 3105 | 1 | 0.3610306 | 0.46763285 | 0.6389694 | null | null | 0.27665499 | 0.93698038 |
| explanation_only | 3 | 33472 | raw_confidence | Unfiltered | 2800 / 2800 | 1 | 0.4525 | 0.57130952 | 0.5475 | null | null | 0.16182289 | 0.7581397 |
| explanation_only | 3 | 76870 | raw_confidence | Unfiltered | 1186 / 1186 | 1 | 0.40725126 | 0.51728499 | 0.59274874 | null | null | 0.18160169 | 0.83096356 |
| explanation_only | 3 | 32833 | raw_confidence | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | raw_confidence | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | raw_confidence | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | raw_confidence | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | raw_confidence | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | raw_confidence | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | raw_confidence | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | raw_confidence | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | raw_confidence | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | frequency | Unfiltered | 3105 / 3105 | 1 | 0.39774557 | 0.49736983 | 0.60225443 | null | null | 0.019905114 | 0.82418948 |
| explanation_only | 3 | 33472 | frequency | Unfiltered | 2800 / 2800 | 1 | 0.36214286 | 0.51875 | 0.63785714 | null | null | 0.055507828 | 0.80652789 |
| explanation_only | 3 | 76870 | frequency | Unfiltered | 1186 / 1186 | 1 | 0.30860034 | 0.46992693 | 0.69139966 | null | null | 0.10905035 | 0.85360123 |
| explanation_only | 3 | 32833 | frequency | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | frequency | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | frequency | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | frequency | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | frequency | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | frequency | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 32833 | frequency | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 33472 | frequency | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| explanation_only | 3 | 76870 | frequency | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | learned_reliability | Unfiltered | 2809 / 2809 | 1 | 0.58205767 | 0.68547526 | 0.41794233 | null | null | 0.075846258 | 0.60351581 |
| explanation_only | 4 | 33471 | learned_reliability | Unfiltered | 1542 / 1542 | 1 | 0.30090791 | 0.42542153 | 0.69909209 | null | null | 0.28761316 | 1.0075504 |
| explanation_only | 4 | 89443 | learned_reliability | Unfiltered | 3054 / 3054 | 1 | 0.2940406 | 0.46294477 | 0.7059594 | null | null | 0.20165508 | 0.89433484 |
| explanation_only | 4 | 31777 | learned_reliability | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | learned_reliability | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | learned_reliability | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | learned_reliability | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | learned_reliability | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | learned_reliability | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | learned_reliability | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | learned_reliability | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | learned_reliability | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | confidence_only | Unfiltered | 2809 / 2809 | 1 | 0.58205767 | 0.68547526 | 0.41794233 | null | null | 0.075846258 | 0.60351581 |
| explanation_only | 4 | 33471 | confidence_only | Unfiltered | 1542 / 1542 | 1 | 0.30090791 | 0.42542153 | 0.69909209 | null | null | 0.28761316 | 1.0075504 |
| explanation_only | 4 | 89443 | confidence_only | Unfiltered | 3054 / 3054 | 1 | 0.2940406 | 0.46294477 | 0.7059594 | null | null | 0.20165508 | 0.89433484 |
| explanation_only | 4 | 31777 | confidence_only | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | confidence_only | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | confidence_only | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | confidence_only | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | confidence_only | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | confidence_only | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | confidence_only | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | confidence_only | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | confidence_only | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | support_aware | Unfiltered | 2809 / 2809 | 1 | 0.58205767 | 0.68547526 | 0.41794233 | null | null | 0.075846258 | 0.60351581 |
| explanation_only | 4 | 33471 | support_aware | Unfiltered | 1542 / 1542 | 1 | 0.30090791 | 0.42542153 | 0.69909209 | null | null | 0.28761316 | 1.0075504 |
| explanation_only | 4 | 89443 | support_aware | Unfiltered | 3054 / 3054 | 1 | 0.2940406 | 0.46294477 | 0.7059594 | null | null | 0.20165508 | 0.89433484 |
| explanation_only | 4 | 31777 | support_aware | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | support_aware | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | support_aware | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | support_aware | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | support_aware | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | support_aware | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | support_aware | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | support_aware | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | support_aware | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | raw_confidence | Unfiltered | 2809 / 2809 | 1 | 0.58205767 | 0.68547526 | 0.41794233 | null | null | 0.075846258 | 0.60351581 |
| explanation_only | 4 | 33471 | raw_confidence | Unfiltered | 1542 / 1542 | 1 | 0.30090791 | 0.42542153 | 0.69909209 | null | null | 0.28761316 | 1.0075504 |
| explanation_only | 4 | 89443 | raw_confidence | Unfiltered | 3054 / 3054 | 1 | 0.2940406 | 0.46294477 | 0.7059594 | null | null | 0.20165508 | 0.89433484 |
| explanation_only | 4 | 31777 | raw_confidence | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | raw_confidence | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | raw_confidence | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | raw_confidence | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | raw_confidence | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | raw_confidence | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | raw_confidence | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | raw_confidence | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | raw_confidence | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | frequency | Unfiltered | 2809 / 2809 | 1 | 0.57956568 | 0.70404652 | 0.42043432 | null | null | 0.16038246 | 0.65605906 |
| explanation_only | 4 | 33471 | frequency | Unfiltered | 1542 / 1542 | 1 | 0.45460441 | 0.56236489 | 0.54539559 | null | null | 0.035421191 | 0.77077747 |
| explanation_only | 4 | 89443 | frequency | Unfiltered | 3054 / 3054 | 1 | 0.20988867 | 0.43216547 | 0.79011133 | null | null | 0.20929455 | 0.89861294 |
| explanation_only | 4 | 31777 | frequency | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | frequency | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | frequency | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | frequency | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | frequency | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | frequency | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 31777 | frequency | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 33471 | frequency | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| explanation_only | 4 | 89443 | frequency | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | learned_reliability | Unfiltered | 4857 / 4857 | 1 | 0.35659872 | 0.48599959 | 0.64340128 | null | null | 0.3479657 | 0.92567817 |
| question_plus_explanation | 0 | 32829 | learned_reliability | Unfiltered | 2156 / 2156 | 1 | 0.55612245 | 0.67694805 | 0.44387755 | null | null | 0.072303468 | 0.62421225 |
| question_plus_explanation | 0 | 104665 | learned_reliability | Unfiltered | 673 / 673 | 1 | 0.12332838 | 0.2808321 | 0.87667162 | null | null | 0.31785893 | 1.0022718 |
| question_plus_explanation | 0 | 31772 | learned_reliability | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | learned_reliability | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | learned_reliability | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | learned_reliability | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | learned_reliability | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | learned_reliability | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | learned_reliability | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | learned_reliability | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | learned_reliability | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | confidence_only | Unfiltered | 4857 / 4857 | 1 | 0.35659872 | 0.48599959 | 0.64340128 | null | null | 0.3479657 | 0.92567817 |
| question_plus_explanation | 0 | 32829 | confidence_only | Unfiltered | 2156 / 2156 | 1 | 0.55612245 | 0.67694805 | 0.44387755 | null | null | 0.072303468 | 0.62421225 |
| question_plus_explanation | 0 | 104665 | confidence_only | Unfiltered | 673 / 673 | 1 | 0.12332838 | 0.2808321 | 0.87667162 | null | null | 0.31785893 | 1.0022718 |
| question_plus_explanation | 0 | 31772 | confidence_only | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | confidence_only | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | confidence_only | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | confidence_only | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | confidence_only | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | confidence_only | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | confidence_only | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | confidence_only | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | confidence_only | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | support_aware | Unfiltered | 4857 / 4857 | 1 | 0.35659872 | 0.48599959 | 0.64340128 | null | null | 0.3479657 | 0.92567817 |
| question_plus_explanation | 0 | 32829 | support_aware | Unfiltered | 2156 / 2156 | 1 | 0.55612245 | 0.67694805 | 0.44387755 | null | null | 0.072303468 | 0.62421225 |
| question_plus_explanation | 0 | 104665 | support_aware | Unfiltered | 673 / 673 | 1 | 0.12332838 | 0.2808321 | 0.87667162 | null | null | 0.31785893 | 1.0022718 |
| question_plus_explanation | 0 | 31772 | support_aware | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | support_aware | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | support_aware | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | support_aware | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | support_aware | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | support_aware | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | support_aware | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | support_aware | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | support_aware | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | raw_confidence | Unfiltered | 4857 / 4857 | 1 | 0.35659872 | 0.48599959 | 0.64340128 | null | null | 0.3479657 | 0.92567817 |
| question_plus_explanation | 0 | 32829 | raw_confidence | Unfiltered | 2156 / 2156 | 1 | 0.55612245 | 0.67694805 | 0.44387755 | null | null | 0.072303468 | 0.62421225 |
| question_plus_explanation | 0 | 104665 | raw_confidence | Unfiltered | 673 / 673 | 1 | 0.12332838 | 0.2808321 | 0.87667162 | null | null | 0.31785893 | 1.0022718 |
| question_plus_explanation | 0 | 31772 | raw_confidence | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | raw_confidence | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | raw_confidence | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | raw_confidence | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | raw_confidence | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | raw_confidence | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | raw_confidence | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | raw_confidence | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | raw_confidence | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | frequency | Unfiltered | 4857 / 4857 | 1 | 0.35392217 | 0.48586233 | 0.64607783 | null | null | 0.019249461 | 0.83175074 |
| question_plus_explanation | 0 | 32829 | frequency | Unfiltered | 2156 / 2156 | 1 | 0.73283859 | 0.79081633 | 0.26716141 | null | null | 0.35966696 | 0.61324346 |
| question_plus_explanation | 0 | 104665 | frequency | Unfiltered | 673 / 673 | 1 | 0.64635958 | 0.71892026 | 0.35364042 | null | null | 0.27318795 | 0.66497603 |
| question_plus_explanation | 0 | 31772 | frequency | 10 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | frequency | 10 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | frequency | 10 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | frequency | 20 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | frequency | 20 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | frequency | 20 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 31772 | frequency | 30 | 0 / 4857 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 32829 | frequency | 30 | 0 / 2156 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 0 | 104665 | frequency | 30 | 0 / 673 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | learned_reliability | Unfiltered | 3640 / 3640 | 1 | 0.33681319 | 0.45334249 | 0.66318681 | null | null | 0.089510555 | 0.83601744 |
| question_plus_explanation | 1 | 32835 | learned_reliability | Unfiltered | 2332 / 2332 | 1 | 0.18825043 | 0.44403945 | 0.81174957 | null | null | 0.16239985 | 0.86341574 |
| question_plus_explanation | 1 | 109465 | learned_reliability | Unfiltered | 1051 / 1051 | 1 | 0.4224548 | 0.59435458 | 0.5775452 | null | null | 0.091878159 | 0.75213794 |
| question_plus_explanation | 1 | 31778 | learned_reliability | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | learned_reliability | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | learned_reliability | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | learned_reliability | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | learned_reliability | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | learned_reliability | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | learned_reliability | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | learned_reliability | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | learned_reliability | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | confidence_only | Unfiltered | 3640 / 3640 | 1 | 0.33681319 | 0.45334249 | 0.66318681 | null | null | 0.089510555 | 0.83601744 |
| question_plus_explanation | 1 | 32835 | confidence_only | Unfiltered | 2332 / 2332 | 1 | 0.18825043 | 0.44403945 | 0.81174957 | null | null | 0.16239985 | 0.86341574 |
| question_plus_explanation | 1 | 109465 | confidence_only | Unfiltered | 1051 / 1051 | 1 | 0.4224548 | 0.59435458 | 0.5775452 | null | null | 0.091878159 | 0.75213794 |
| question_plus_explanation | 1 | 31778 | confidence_only | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | confidence_only | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | confidence_only | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | confidence_only | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | confidence_only | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | confidence_only | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | confidence_only | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | confidence_only | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | confidence_only | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | support_aware | Unfiltered | 3640 / 3640 | 1 | 0.33681319 | 0.45334249 | 0.66318681 | null | null | 0.089510555 | 0.83601744 |
| question_plus_explanation | 1 | 32835 | support_aware | Unfiltered | 2332 / 2332 | 1 | 0.18825043 | 0.44403945 | 0.81174957 | null | null | 0.16239985 | 0.86341574 |
| question_plus_explanation | 1 | 109465 | support_aware | Unfiltered | 1051 / 1051 | 1 | 0.4224548 | 0.59435458 | 0.5775452 | null | null | 0.091878159 | 0.75213794 |
| question_plus_explanation | 1 | 31778 | support_aware | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | support_aware | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | support_aware | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | support_aware | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | support_aware | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | support_aware | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | support_aware | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | support_aware | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | support_aware | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | raw_confidence | Unfiltered | 3640 / 3640 | 1 | 0.33681319 | 0.45334249 | 0.66318681 | null | null | 0.089510555 | 0.83601744 |
| question_plus_explanation | 1 | 32835 | raw_confidence | Unfiltered | 2332 / 2332 | 1 | 0.18825043 | 0.44403945 | 0.81174957 | null | null | 0.16239985 | 0.86341574 |
| question_plus_explanation | 1 | 109465 | raw_confidence | Unfiltered | 1051 / 1051 | 1 | 0.4224548 | 0.59435458 | 0.5775452 | null | null | 0.091878159 | 0.75213794 |
| question_plus_explanation | 1 | 31778 | raw_confidence | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | raw_confidence | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | raw_confidence | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | raw_confidence | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | raw_confidence | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | raw_confidence | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | raw_confidence | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | raw_confidence | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | raw_confidence | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | frequency | Unfiltered | 3640 / 3640 | 1 | 0.31318681 | 0.43598901 | 0.68681319 | null | null | 0.10162085 | 0.87769413 |
| question_plus_explanation | 1 | 32835 | frequency | Unfiltered | 2332 / 2332 | 1 | 0.40909091 | 0.56546598 | 0.59090909 | null | null | 0.0057167494 | 0.76931696 |
| question_plus_explanation | 1 | 109465 | frequency | Unfiltered | 1051 / 1051 | 1 | 0.40627973 | 0.58848716 | 0.59372027 | null | null | 0.0085279249 | 0.75619618 |
| question_plus_explanation | 1 | 31778 | frequency | 10 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | frequency | 10 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | frequency | 10 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | frequency | 20 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | frequency | 20 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | frequency | 20 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 31778 | frequency | 30 | 0 / 3640 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 32835 | frequency | 30 | 0 / 2332 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 1 | 109465 | frequency | 30 | 0 / 1051 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | learned_reliability | Unfiltered | 3115 / 3115 | 1 | 0.43370787 | 0.56645265 | 0.56629213 | null | null | 0.02698317 | 0.73841194 |
| question_plus_explanation | 2 | 33474 | learned_reliability | Unfiltered | 1766 / 1766 | 1 | 0.22706682 | 0.38807097 | 0.77293318 | null | null | 0.059759005 | 0.8839615 |
| question_plus_explanation | 2 | 91695 | learned_reliability | Unfiltered | 2610 / 2610 | 1 | 0.33371648 | 0.5197318 | 0.66628352 | null | null | 0.037883848 | 0.78959477 |
| question_plus_explanation | 2 | 31774 | learned_reliability | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | learned_reliability | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | learned_reliability | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | learned_reliability | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | learned_reliability | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | learned_reliability | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | learned_reliability | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | learned_reliability | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | learned_reliability | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | confidence_only | Unfiltered | 3115 / 3115 | 1 | 0.43370787 | 0.56645265 | 0.56629213 | null | null | 0.02698317 | 0.73841194 |
| question_plus_explanation | 2 | 33474 | confidence_only | Unfiltered | 1766 / 1766 | 1 | 0.22706682 | 0.38807097 | 0.77293318 | null | null | 0.059759005 | 0.8839615 |
| question_plus_explanation | 2 | 91695 | confidence_only | Unfiltered | 2610 / 2610 | 1 | 0.33371648 | 0.5197318 | 0.66628352 | null | null | 0.037883848 | 0.78959477 |
| question_plus_explanation | 2 | 31774 | confidence_only | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | confidence_only | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | confidence_only | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | confidence_only | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | confidence_only | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | confidence_only | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | confidence_only | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | confidence_only | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | confidence_only | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | support_aware | Unfiltered | 3115 / 3115 | 1 | 0.43370787 | 0.56645265 | 0.56629213 | null | null | 0.02698317 | 0.73841194 |
| question_plus_explanation | 2 | 33474 | support_aware | Unfiltered | 1766 / 1766 | 1 | 0.22706682 | 0.38807097 | 0.77293318 | null | null | 0.059759005 | 0.8839615 |
| question_plus_explanation | 2 | 91695 | support_aware | Unfiltered | 2610 / 2610 | 1 | 0.33371648 | 0.5197318 | 0.66628352 | null | null | 0.037883848 | 0.78959477 |
| question_plus_explanation | 2 | 31774 | support_aware | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | support_aware | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | support_aware | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | support_aware | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | support_aware | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | support_aware | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | support_aware | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | support_aware | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | support_aware | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | raw_confidence | Unfiltered | 3115 / 3115 | 1 | 0.43370787 | 0.56645265 | 0.56629213 | null | null | 0.02698317 | 0.73841194 |
| question_plus_explanation | 2 | 33474 | raw_confidence | Unfiltered | 1766 / 1766 | 1 | 0.22706682 | 0.38807097 | 0.77293318 | null | null | 0.059759005 | 0.8839615 |
| question_plus_explanation | 2 | 91695 | raw_confidence | Unfiltered | 2610 / 2610 | 1 | 0.33371648 | 0.5197318 | 0.66628352 | null | null | 0.037883848 | 0.78959477 |
| question_plus_explanation | 2 | 31774 | raw_confidence | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | raw_confidence | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | raw_confidence | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | raw_confidence | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | raw_confidence | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | raw_confidence | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | raw_confidence | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | raw_confidence | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | raw_confidence | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | frequency | Unfiltered | 3115 / 3115 | 1 | 0.45104334 | 0.59384698 | 0.54895666 | null | null | 0.0097463404 | 0.74418345 |
| question_plus_explanation | 2 | 33474 | frequency | Unfiltered | 1766 / 1766 | 1 | 0.18289921 | 0.3689128 | 0.81710079 | null | null | 0.25839779 | 0.95008875 |
| question_plus_explanation | 2 | 91695 | frequency | Unfiltered | 2610 / 2610 | 1 | 0.47279693 | 0.58812261 | 0.52720307 | null | null | 0.031499937 | 0.74723568 |
| question_plus_explanation | 2 | 31774 | frequency | 10 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | frequency | 10 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | frequency | 10 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | frequency | 20 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | frequency | 20 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | frequency | 20 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 31774 | frequency | 30 | 0 / 3115 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 33474 | frequency | 30 | 0 / 1766 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 2 | 91695 | frequency | 30 | 0 / 2610 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | learned_reliability | Unfiltered | 3105 / 3105 | 1 | 0.39033816 | 0.49323671 | 0.60966184 | null | null | 0.35677442 | 0.98397524 |
| question_plus_explanation | 3 | 33472 | learned_reliability | Unfiltered | 2800 / 2800 | 1 | 0.45392857 | 0.57035714 | 0.54607143 | null | null | 0.27611841 | 0.79253218 |
| question_plus_explanation | 3 | 76870 | learned_reliability | Unfiltered | 1186 / 1186 | 1 | 0.33052277 | 0.48440135 | 0.66947723 | null | null | 0.39201854 | 0.98648632 |
| question_plus_explanation | 3 | 32833 | learned_reliability | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | learned_reliability | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | learned_reliability | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | learned_reliability | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | learned_reliability | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | learned_reliability | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | learned_reliability | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | learned_reliability | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | learned_reliability | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | confidence_only | Unfiltered | 3105 / 3105 | 1 | 0.39033816 | 0.49323671 | 0.60966184 | null | null | 0.35677442 | 0.98397524 |
| question_plus_explanation | 3 | 33472 | confidence_only | Unfiltered | 2800 / 2800 | 1 | 0.45392857 | 0.57035714 | 0.54607143 | null | null | 0.27611841 | 0.79253218 |
| question_plus_explanation | 3 | 76870 | confidence_only | Unfiltered | 1186 / 1186 | 1 | 0.33052277 | 0.48440135 | 0.66947723 | null | null | 0.39201854 | 0.98648632 |
| question_plus_explanation | 3 | 32833 | confidence_only | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | confidence_only | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | confidence_only | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | confidence_only | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | confidence_only | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | confidence_only | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | confidence_only | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | confidence_only | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | confidence_only | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | support_aware | Unfiltered | 3105 / 3105 | 1 | 0.39033816 | 0.49323671 | 0.60966184 | null | null | 0.35677442 | 0.98397524 |
| question_plus_explanation | 3 | 33472 | support_aware | Unfiltered | 2800 / 2800 | 1 | 0.45392857 | 0.57035714 | 0.54607143 | null | null | 0.27611841 | 0.79253218 |
| question_plus_explanation | 3 | 76870 | support_aware | Unfiltered | 1186 / 1186 | 1 | 0.33052277 | 0.48440135 | 0.66947723 | null | null | 0.39201854 | 0.98648632 |
| question_plus_explanation | 3 | 32833 | support_aware | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | support_aware | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | support_aware | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | support_aware | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | support_aware | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | support_aware | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | support_aware | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | support_aware | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | support_aware | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | raw_confidence | Unfiltered | 3105 / 3105 | 1 | 0.39033816 | 0.49323671 | 0.60966184 | null | null | 0.35677442 | 0.98397524 |
| question_plus_explanation | 3 | 33472 | raw_confidence | Unfiltered | 2800 / 2800 | 1 | 0.45392857 | 0.57035714 | 0.54607143 | null | null | 0.27611841 | 0.79253218 |
| question_plus_explanation | 3 | 76870 | raw_confidence | Unfiltered | 1186 / 1186 | 1 | 0.33052277 | 0.48440135 | 0.66947723 | null | null | 0.39201854 | 0.98648632 |
| question_plus_explanation | 3 | 32833 | raw_confidence | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | raw_confidence | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | raw_confidence | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | raw_confidence | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | raw_confidence | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | raw_confidence | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | raw_confidence | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | raw_confidence | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | raw_confidence | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | frequency | Unfiltered | 3105 / 3105 | 1 | 0.39774557 | 0.49736983 | 0.60225443 | null | null | 0.019905114 | 0.82418948 |
| question_plus_explanation | 3 | 33472 | frequency | Unfiltered | 2800 / 2800 | 1 | 0.36214286 | 0.51875 | 0.63785714 | null | null | 0.055507828 | 0.80652789 |
| question_plus_explanation | 3 | 76870 | frequency | Unfiltered | 1186 / 1186 | 1 | 0.30860034 | 0.46992693 | 0.69139966 | null | null | 0.10905035 | 0.85360123 |
| question_plus_explanation | 3 | 32833 | frequency | 10 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | frequency | 10 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | frequency | 10 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | frequency | 20 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | frequency | 20 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | frequency | 20 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 32833 | frequency | 30 | 0 / 3105 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 33472 | frequency | 30 | 0 / 2800 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 3 | 76870 | frequency | 30 | 0 / 1186 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | learned_reliability | Unfiltered | 2809 / 2809 | 1 | 0.58810965 | 0.7084965 | 0.41189035 | null | null | 0.04474762 | 0.58511951 |
| question_plus_explanation | 4 | 33471 | learned_reliability | Unfiltered | 1542 / 1542 | 1 | 0.37483787 | 0.51934717 | 0.62516213 | null | null | 0.2431792 | 0.88864738 |
| question_plus_explanation | 4 | 89443 | learned_reliability | Unfiltered | 3054 / 3054 | 1 | 0.32089064 | 0.48411919 | 0.67910936 | null | null | 0.17681661 | 0.84642525 |
| question_plus_explanation | 4 | 31777 | learned_reliability | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | learned_reliability | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | learned_reliability | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | learned_reliability | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | learned_reliability | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | learned_reliability | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | learned_reliability | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | learned_reliability | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | learned_reliability | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | confidence_only | Unfiltered | 2809 / 2809 | 1 | 0.58810965 | 0.7084965 | 0.41189035 | null | null | 0.04474762 | 0.58511951 |
| question_plus_explanation | 4 | 33471 | confidence_only | Unfiltered | 1542 / 1542 | 1 | 0.37483787 | 0.51934717 | 0.62516213 | null | null | 0.2431792 | 0.88864738 |
| question_plus_explanation | 4 | 89443 | confidence_only | Unfiltered | 3054 / 3054 | 1 | 0.32089064 | 0.48411919 | 0.67910936 | null | null | 0.17681661 | 0.84642525 |
| question_plus_explanation | 4 | 31777 | confidence_only | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | confidence_only | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | confidence_only | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | confidence_only | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | confidence_only | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | confidence_only | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | confidence_only | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | confidence_only | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | confidence_only | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | support_aware | Unfiltered | 2809 / 2809 | 1 | 0.58810965 | 0.7084965 | 0.41189035 | null | null | 0.04474762 | 0.58511951 |
| question_plus_explanation | 4 | 33471 | support_aware | Unfiltered | 1542 / 1542 | 1 | 0.37483787 | 0.51934717 | 0.62516213 | null | null | 0.2431792 | 0.88864738 |
| question_plus_explanation | 4 | 89443 | support_aware | Unfiltered | 3054 / 3054 | 1 | 0.32089064 | 0.48411919 | 0.67910936 | null | null | 0.17681661 | 0.84642525 |
| question_plus_explanation | 4 | 31777 | support_aware | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | support_aware | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | support_aware | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | support_aware | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | support_aware | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | support_aware | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | support_aware | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | support_aware | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | support_aware | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | raw_confidence | Unfiltered | 2809 / 2809 | 1 | 0.58810965 | 0.7084965 | 0.41189035 | null | null | 0.04474762 | 0.58511951 |
| question_plus_explanation | 4 | 33471 | raw_confidence | Unfiltered | 1542 / 1542 | 1 | 0.37483787 | 0.51934717 | 0.62516213 | null | null | 0.2431792 | 0.88864738 |
| question_plus_explanation | 4 | 89443 | raw_confidence | Unfiltered | 3054 / 3054 | 1 | 0.32089064 | 0.48411919 | 0.67910936 | null | null | 0.17681661 | 0.84642525 |
| question_plus_explanation | 4 | 31777 | raw_confidence | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | raw_confidence | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | raw_confidence | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | raw_confidence | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | raw_confidence | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | raw_confidence | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | raw_confidence | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | raw_confidence | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | raw_confidence | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | frequency | Unfiltered | 2809 / 2809 | 1 | 0.57956568 | 0.70404652 | 0.42043432 | null | null | 0.16038246 | 0.65605906 |
| question_plus_explanation | 4 | 33471 | frequency | Unfiltered | 1542 / 1542 | 1 | 0.45460441 | 0.56236489 | 0.54539559 | null | null | 0.035421191 | 0.77077747 |
| question_plus_explanation | 4 | 89443 | frequency | Unfiltered | 3054 / 3054 | 1 | 0.20988867 | 0.43216547 | 0.79011133 | null | null | 0.20929455 | 0.89861294 |
| question_plus_explanation | 4 | 31777 | frequency | 10 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | frequency | 10 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | frequency | 10 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | frequency | 20 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | frequency | 20 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | frequency | 20 | 0 / 3054 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 31777 | frequency | 30 | 0 / 2809 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 33471 | frequency | 30 | 0 / 1542 | 0 | null | null | null | null | null | null | null |
| question_plus_explanation | 4 | 89443 | frequency | 30 | 0 / 3054 | 0 | null | null | null | null | null | null | null |

## Correctness discrimination — complete fold and question results

Eligibility: n>=200, correct>=20, incorrect>=20. Frequency predicts a different correctness target and is contextual only.

| Arm | Fold | Scope | Rule | n | Correct | Incorrect | AUROC | Ineligible reasons |
|---|---|---|---|---|---|---|---|---|
| explanation_only | 0 | All | learned_reliability | 7686 | 2553 | 5133 | 0.79090387 | none |
| explanation_only | 0 | 31772 | learned_reliability | 4857 | 1671 | 3186 | 0.73060288 | none |
| explanation_only | 0 | 32829 | learned_reliability | 2156 | 760 | 1396 | 0.87196313 | none |
| explanation_only | 0 | 104665 | learned_reliability | 673 | 122 | 551 | 0.84006724 | none |
| explanation_only | 0 | All | confidence_only | 7686 | 2553 | 5133 | 0.57542213 | none |
| explanation_only | 0 | 31772 | confidence_only | 4857 | 1671 | 3186 | 0.58500685 | none |
| explanation_only | 0 | 32829 | confidence_only | 2156 | 760 | 1396 | 0.57777956 | none |
| explanation_only | 0 | 104665 | confidence_only | 673 | 122 | 551 | 0.48873881 | none |
| explanation_only | 0 | All | support_aware | 7686 | 2553 | 5133 | 0.63576087 | none |
| explanation_only | 0 | 31772 | support_aware | 4857 | 1671 | 3186 | 0.61794682 | none |
| explanation_only | 0 | 32829 | support_aware | 2156 | 760 | 1396 | 0.67987389 | none |
| explanation_only | 0 | 104665 | support_aware | 673 | 122 | 551 | 0.59285651 | none |
| explanation_only | 0 | All | raw_confidence | 7686 | 2553 | 5133 | 0.57693039 | none |
| explanation_only | 0 | 31772 | raw_confidence | 4857 | 1671 | 3186 | 0.58859 | none |
| explanation_only | 0 | 32829 | raw_confidence | 2156 | 760 | 1396 | 0.57660798 | none |
| explanation_only | 0 | 104665 | raw_confidence | 673 | 122 | 551 | 0.48186606 | none |
| explanation_only | 0 | All | frequency | 7686 | 3734 | 3952 | 0.5 | none |
| explanation_only | 0 | 31772 | frequency | 4857 | 1719 | 3138 | 0.5 | none |
| explanation_only | 0 | 32829 | frequency | 2156 | 1580 | 576 | 0.5 | none |
| explanation_only | 0 | 104665 | frequency | 673 | 435 | 238 | 0.5 | none |
| explanation_only | 1 | All | learned_reliability | 7023 | 1980 | 5043 | 0.66520905 | none |
| explanation_only | 1 | 31778 | learned_reliability | 3640 | 1164 | 2476 | 0.7435201 | none |
| explanation_only | 1 | 32835 | learned_reliability | 2332 | 520 | 1812 | 0.45206954 | none |
| explanation_only | 1 | 109465 | learned_reliability | 1051 | 296 | 755 | 0.66799266 | none |
| explanation_only | 1 | All | confidence_only | 7023 | 1980 | 5043 | 0.61418683 | none |
| explanation_only | 1 | 31778 | confidence_only | 3640 | 1164 | 2476 | 0.69474082 | none |
| explanation_only | 1 | 32835 | confidence_only | 2332 | 520 | 1812 | 0.45025259 | none |
| explanation_only | 1 | 109465 | confidence_only | 1051 | 296 | 755 | 0.58224897 | none |
| explanation_only | 1 | All | support_aware | 7023 | 1980 | 5043 | 0.63225518 | none |
| explanation_only | 1 | 31778 | support_aware | 3640 | 1164 | 2476 | 0.71545791 | none |
| explanation_only | 1 | 32835 | support_aware | 2332 | 520 | 1812 | 0.44979623 | none |
| explanation_only | 1 | 109465 | support_aware | 1051 | 296 | 755 | 0.60481027 | none |
| explanation_only | 1 | All | raw_confidence | 7023 | 1980 | 5043 | 0.61624018 | none |
| explanation_only | 1 | 31778 | raw_confidence | 3640 | 1164 | 2476 | 0.69785213 | none |
| explanation_only | 1 | 32835 | raw_confidence | 2332 | 520 | 1812 | 0.45379946 | none |
| explanation_only | 1 | 109465 | raw_confidence | 1051 | 296 | 755 | 0.58162699 | none |
| explanation_only | 1 | All | frequency | 7023 | 2521 | 4502 | 0.5 | none |
| explanation_only | 1 | 31778 | frequency | 3640 | 1140 | 2500 | 0.5 | none |
| explanation_only | 1 | 32835 | frequency | 2332 | 954 | 1378 | 0.5 | none |
| explanation_only | 1 | 109465 | frequency | 1051 | 427 | 624 | 0.5 | none |
| explanation_only | 2 | All | learned_reliability | 7491 | 2583 | 4908 | 0.68314103 | none |
| explanation_only | 2 | 31774 | learned_reliability | 3115 | 1363 | 1752 | 0.63359933 | none |
| explanation_only | 2 | 33474 | learned_reliability | 1766 | 437 | 1329 | 0.57673738 | none |
| explanation_only | 2 | 91695 | learned_reliability | 2610 | 783 | 1827 | 0.7527051 | none |
| explanation_only | 2 | All | confidence_only | 7491 | 2583 | 4908 | 0.62852487 | none |
| explanation_only | 2 | 31774 | confidence_only | 3115 | 1363 | 1752 | 0.67837156 | none |
| explanation_only | 2 | 33474 | confidence_only | 1766 | 437 | 1329 | 0.53272191 | none |
| explanation_only | 2 | 91695 | confidence_only | 2610 | 783 | 1827 | 0.55182305 | none |
| explanation_only | 2 | All | support_aware | 7491 | 2583 | 4908 | 0.66221689 | none |
| explanation_only | 2 | 31774 | support_aware | 3115 | 1363 | 1752 | 0.70302088 | none |
| explanation_only | 2 | 33474 | support_aware | 1766 | 437 | 1329 | 0.55027438 | none |
| explanation_only | 2 | 91695 | support_aware | 2610 | 783 | 1827 | 0.60876235 | none |
| explanation_only | 2 | All | raw_confidence | 7491 | 2583 | 4908 | 0.63105094 | none |
| explanation_only | 2 | 31774 | raw_confidence | 3115 | 1363 | 1752 | 0.68101857 | none |
| explanation_only | 2 | 33474 | raw_confidence | 1766 | 437 | 1329 | 0.53308694 | none |
| explanation_only | 2 | 91695 | raw_confidence | 2610 | 783 | 1827 | 0.55377266 | none |
| explanation_only | 2 | All | frequency | 7491 | 2962 | 4529 | 0.5 | none |
| explanation_only | 2 | 31774 | frequency | 3115 | 1405 | 1710 | 0.5 | none |
| explanation_only | 2 | 33474 | frequency | 1766 | 323 | 1443 | 0.5 | none |
| explanation_only | 2 | 91695 | frequency | 2610 | 1234 | 1376 | 0.5 | none |
| explanation_only | 3 | All | learned_reliability | 7091 | 2871 | 4220 | 0.6391748 | none |
| explanation_only | 3 | 32833 | learned_reliability | 3105 | 1121 | 1984 | 0.60839526 | none |
| explanation_only | 3 | 33472 | learned_reliability | 2800 | 1267 | 1533 | 0.65249309 | none |
| explanation_only | 3 | 76870 | learned_reliability | 1186 | 483 | 703 | 0.71138628 | none |
| explanation_only | 3 | All | confidence_only | 7091 | 2871 | 4220 | 0.59730018 | none |
| explanation_only | 3 | 32833 | confidence_only | 3105 | 1121 | 1984 | 0.52863407 | none |
| explanation_only | 3 | 33472 | confidence_only | 2800 | 1267 | 1533 | 0.66325449 | none |
| explanation_only | 3 | 76870 | confidence_only | 1186 | 483 | 703 | 0.63547382 | none |
| explanation_only | 3 | All | support_aware | 7091 | 2871 | 4220 | 0.62047918 | none |
| explanation_only | 3 | 32833 | support_aware | 3105 | 1121 | 1984 | 0.55875415 | none |
| explanation_only | 3 | 33472 | support_aware | 2800 | 1267 | 1533 | 0.67673637 | none |
| explanation_only | 3 | 76870 | support_aware | 1186 | 483 | 703 | 0.66576105 | none |
| explanation_only | 3 | All | raw_confidence | 7091 | 2871 | 4220 | 0.59253856 | none |
| explanation_only | 3 | 32833 | raw_confidence | 3105 | 1121 | 1984 | 0.51072226 | none |
| explanation_only | 3 | 33472 | raw_confidence | 2800 | 1267 | 1533 | 0.67039393 | none |
| explanation_only | 3 | 76870 | raw_confidence | 1186 | 483 | 703 | 0.63460208 | none |
| explanation_only | 3 | All | frequency | 7091 | 2615 | 4476 | 0.5 | none |
| explanation_only | 3 | 32833 | frequency | 3105 | 1235 | 1870 | 0.5 | none |
| explanation_only | 3 | 33472 | frequency | 2800 | 1014 | 1786 | 0.5 | none |
| explanation_only | 3 | 76870 | frequency | 1186 | 366 | 820 | 0.5 | none |
| explanation_only | 4 | All | learned_reliability | 7405 | 2997 | 4408 | 0.69421645 | none |
| explanation_only | 4 | 31777 | learned_reliability | 2809 | 1635 | 1174 | 0.68934196 | none |
| explanation_only | 4 | 33471 | learned_reliability | 1542 | 464 | 1078 | 0.54254666 | none |
| explanation_only | 4 | 89443 | learned_reliability | 3054 | 898 | 2156 | 0.63680654 | none |
| explanation_only | 4 | All | confidence_only | 7405 | 2997 | 4408 | 0.61346184 | none |
| explanation_only | 4 | 31777 | confidence_only | 2809 | 1635 | 1174 | 0.6749819 | none |
| explanation_only | 4 | 33471 | confidence_only | 1542 | 464 | 1078 | 0.4283745 | none |
| explanation_only | 4 | 89443 | confidence_only | 3054 | 898 | 2156 | 0.53615151 | none |
| explanation_only | 4 | All | support_aware | 7405 | 2997 | 4408 | 0.64767853 | none |
| explanation_only | 4 | 31777 | support_aware | 2809 | 1635 | 1174 | 0.68484129 | none |
| explanation_only | 4 | 33471 | support_aware | 1542 | 464 | 1078 | 0.48195593 | none |
| explanation_only | 4 | 89443 | support_aware | 3054 | 898 | 2156 | 0.57041235 | none |
| explanation_only | 4 | All | raw_confidence | 7405 | 2997 | 4408 | 0.61202014 | none |
| explanation_only | 4 | 31777 | raw_confidence | 2809 | 1635 | 1174 | 0.67235828 | none |
| explanation_only | 4 | 33471 | raw_confidence | 1542 | 464 | 1078 | 0.42433206 | none |
| explanation_only | 4 | 89443 | raw_confidence | 3054 | 898 | 2156 | 0.53638703 | none |
| explanation_only | 4 | All | frequency | 7405 | 2970 | 4435 | 0.5 | none |
| explanation_only | 4 | 31777 | frequency | 2809 | 1628 | 1181 | 0.5 | none |
| explanation_only | 4 | 33471 | frequency | 1542 | 701 | 841 | 0.5 | none |
| explanation_only | 4 | 89443 | frequency | 3054 | 641 | 2413 | 0.5 | none |
| question_plus_explanation | 0 | All | learned_reliability | 7686 | 3014 | 4672 | 0.64118009 | none |
| question_plus_explanation | 0 | 31772 | learned_reliability | 4857 | 1732 | 3125 | 0.70946023 | none |
| question_plus_explanation | 0 | 32829 | learned_reliability | 2156 | 1199 | 957 | 0.80158579 | none |
| question_plus_explanation | 0 | 104665 | learned_reliability | 673 | 83 | 590 | 0.75568716 | none |
| question_plus_explanation | 0 | All | confidence_only | 7686 | 3014 | 4672 | 0.61818843 | none |
| question_plus_explanation | 0 | 31772 | confidence_only | 4857 | 1732 | 3125 | 0.70732961 | none |
| question_plus_explanation | 0 | 32829 | confidence_only | 2156 | 1199 | 957 | 0.66821358 | none |
| question_plus_explanation | 0 | 104665 | confidence_only | 673 | 83 | 590 | 0.55472738 | none |
| question_plus_explanation | 0 | All | support_aware | 7686 | 3014 | 4672 | 0.62568456 | none |
| question_plus_explanation | 0 | 31772 | support_aware | 4857 | 1732 | 3125 | 0.70727603 | none |
| question_plus_explanation | 0 | 32829 | support_aware | 2156 | 1199 | 957 | 0.71310209 | none |
| question_plus_explanation | 0 | 104665 | support_aware | 673 | 83 | 590 | 0.59642638 | none |
| question_plus_explanation | 0 | All | raw_confidence | 7686 | 3014 | 4672 | 0.61550241 | none |
| question_plus_explanation | 0 | 31772 | raw_confidence | 4857 | 1732 | 3125 | 0.70586208 | none |
| question_plus_explanation | 0 | 32829 | raw_confidence | 2156 | 1199 | 957 | 0.6654239 | none |
| question_plus_explanation | 0 | 104665 | raw_confidence | 673 | 83 | 590 | 0.55707576 | none |
| question_plus_explanation | 0 | All | frequency | 7686 | 3734 | 3952 | 0.5 | none |
| question_plus_explanation | 0 | 31772 | frequency | 4857 | 1719 | 3138 | 0.5 | none |
| question_plus_explanation | 0 | 32829 | frequency | 2156 | 1580 | 576 | 0.5 | none |
| question_plus_explanation | 0 | 104665 | frequency | 673 | 435 | 238 | 0.5 | none |
| question_plus_explanation | 1 | All | learned_reliability | 7023 | 2109 | 4914 | 0.63435254 | none |
| question_plus_explanation | 1 | 31778 | learned_reliability | 3640 | 1226 | 2414 | 0.68238143 | none |
| question_plus_explanation | 1 | 32835 | learned_reliability | 2332 | 439 | 1893 | 0.48217808 | none |
| question_plus_explanation | 1 | 109465 | learned_reliability | 1051 | 444 | 607 | 0.56500364 | none |
| question_plus_explanation | 1 | All | confidence_only | 7023 | 2109 | 4914 | 0.60317774 | none |
| question_plus_explanation | 1 | 31778 | confidence_only | 3640 | 1226 | 2414 | 0.70332404 | none |
| question_plus_explanation | 1 | 32835 | confidence_only | 2332 | 439 | 1893 | 0.43339145 | none |
| question_plus_explanation | 1 | 109465 | confidence_only | 1051 | 444 | 607 | 0.51650044 | none |
| question_plus_explanation | 1 | All | support_aware | 7023 | 2109 | 4914 | 0.62543935 | none |
| question_plus_explanation | 1 | 31778 | support_aware | 3640 | 1226 | 2414 | 0.72210248 | none |
| question_plus_explanation | 1 | 32835 | support_aware | 2332 | 439 | 1893 | 0.44291461 | none |
| question_plus_explanation | 1 | 109465 | support_aware | 1051 | 444 | 607 | 0.52559479 | none |
| question_plus_explanation | 1 | All | raw_confidence | 7023 | 2109 | 4914 | 0.60205728 | none |
| question_plus_explanation | 1 | 31778 | raw_confidence | 3640 | 1226 | 2414 | 0.7005368 | none |
| question_plus_explanation | 1 | 32835 | raw_confidence | 2332 | 439 | 1893 | 0.42795721 | none |
| question_plus_explanation | 1 | 109465 | raw_confidence | 1051 | 444 | 607 | 0.52905294 | none |
| question_plus_explanation | 1 | All | frequency | 7023 | 2521 | 4502 | 0.5 | none |
| question_plus_explanation | 1 | 31778 | frequency | 3640 | 1140 | 2500 | 0.5 | none |
| question_plus_explanation | 1 | 32835 | frequency | 2332 | 954 | 1378 | 0.5 | none |
| question_plus_explanation | 1 | 109465 | frequency | 1051 | 427 | 624 | 0.5 | none |
| question_plus_explanation | 2 | All | learned_reliability | 7491 | 2623 | 4868 | 0.66960169 | none |
| question_plus_explanation | 2 | 31774 | learned_reliability | 3115 | 1351 | 1764 | 0.64867546 | none |
| question_plus_explanation | 2 | 33474 | learned_reliability | 1766 | 401 | 1365 | 0.5333854 | none |
| question_plus_explanation | 2 | 91695 | learned_reliability | 2610 | 871 | 1739 | 0.72741074 | none |
| question_plus_explanation | 2 | All | confidence_only | 7491 | 2623 | 4868 | 0.62895297 | none |
| question_plus_explanation | 2 | 31774 | confidence_only | 3115 | 1351 | 1764 | 0.65295255 | none |
| question_plus_explanation | 2 | 33474 | confidence_only | 1766 | 401 | 1365 | 0.53258155 | none |
| question_plus_explanation | 2 | 91695 | confidence_only | 2610 | 871 | 1739 | 0.54579548 | none |
| question_plus_explanation | 2 | All | support_aware | 7491 | 2623 | 4868 | 0.66588622 | none |
| question_plus_explanation | 2 | 31774 | support_aware | 3115 | 1351 | 1764 | 0.68522519 | none |
| question_plus_explanation | 2 | 33474 | support_aware | 1766 | 401 | 1365 | 0.54872434 | none |
| question_plus_explanation | 2 | 91695 | support_aware | 2610 | 871 | 1739 | 0.61485744 | none |
| question_plus_explanation | 2 | All | raw_confidence | 7491 | 2623 | 4868 | 0.63464224 | none |
| question_plus_explanation | 2 | 31774 | raw_confidence | 3115 | 1351 | 1764 | 0.65789178 | none |
| question_plus_explanation | 2 | 33474 | raw_confidence | 1766 | 401 | 1365 | 0.52512583 | none |
| question_plus_explanation | 2 | 91695 | raw_confidence | 2610 | 871 | 1739 | 0.56644224 | none |
| question_plus_explanation | 2 | All | frequency | 7491 | 2962 | 4529 | 0.5 | none |
| question_plus_explanation | 2 | 31774 | frequency | 3115 | 1405 | 1710 | 0.5 | none |
| question_plus_explanation | 2 | 33474 | frequency | 1766 | 323 | 1443 | 0.5 | none |
| question_plus_explanation | 2 | 91695 | frequency | 2610 | 1234 | 1376 | 0.5 | none |
| question_plus_explanation | 3 | All | learned_reliability | 7091 | 2875 | 4216 | 0.57354422 | none |
| question_plus_explanation | 3 | 32833 | learned_reliability | 3105 | 1212 | 1893 | 0.45675835 | none |
| question_plus_explanation | 3 | 33472 | learned_reliability | 2800 | 1271 | 1529 | 0.71867138 | none |
| question_plus_explanation | 3 | 76870 | learned_reliability | 1186 | 392 | 794 | 0.52083548 | none |
| question_plus_explanation | 3 | All | confidence_only | 7091 | 2875 | 4216 | 0.57652937 | none |
| question_plus_explanation | 3 | 32833 | confidence_only | 3105 | 1212 | 1893 | 0.43749292 | none |
| question_plus_explanation | 3 | 33472 | confidence_only | 2800 | 1271 | 1529 | 0.73258955 | none |
| question_plus_explanation | 3 | 76870 | confidence_only | 1186 | 392 | 794 | 0.53399861 | none |
| question_plus_explanation | 3 | All | support_aware | 7091 | 2875 | 4216 | 0.58449596 | none |
| question_plus_explanation | 3 | 32833 | support_aware | 3105 | 1212 | 1893 | 0.44333998 | none |
| question_plus_explanation | 3 | 33472 | support_aware | 2800 | 1271 | 1529 | 0.72682994 | none |
| question_plus_explanation | 3 | 76870 | support_aware | 1186 | 392 | 794 | 0.56252249 | none |
| question_plus_explanation | 3 | All | raw_confidence | 7091 | 2875 | 4216 | 0.57322618 | none |
| question_plus_explanation | 3 | 32833 | raw_confidence | 3105 | 1212 | 1893 | 0.42830412 | none |
| question_plus_explanation | 3 | 33472 | raw_confidence | 2800 | 1271 | 1529 | 0.73290601 | none |
| question_plus_explanation | 3 | 76870 | raw_confidence | 1186 | 392 | 794 | 0.53102671 | none |
| question_plus_explanation | 3 | All | frequency | 7091 | 2615 | 4476 | 0.5 | none |
| question_plus_explanation | 3 | 32833 | frequency | 3105 | 1235 | 1870 | 0.5 | none |
| question_plus_explanation | 3 | 33472 | frequency | 2800 | 1014 | 1786 | 0.5 | none |
| question_plus_explanation | 3 | 76870 | frequency | 1186 | 366 | 820 | 0.5 | none |
| question_plus_explanation | 4 | All | learned_reliability | 7405 | 3210 | 4195 | 0.65043242 | none |
| question_plus_explanation | 4 | 31777 | learned_reliability | 2809 | 1652 | 1157 | 0.66188962 | none |
| question_plus_explanation | 4 | 33471 | learned_reliability | 1542 | 578 | 964 | 0.50336509 | none |
| question_plus_explanation | 4 | 89443 | learned_reliability | 3054 | 980 | 2074 | 0.57969442 | none |
| question_plus_explanation | 4 | All | confidence_only | 7405 | 3210 | 4195 | 0.62286192 | none |
| question_plus_explanation | 4 | 31777 | confidence_only | 2809 | 1652 | 1157 | 0.64521776 | none |
| question_plus_explanation | 4 | 33471 | confidence_only | 1542 | 578 | 964 | 0.43403531 | none |
| question_plus_explanation | 4 | 89443 | confidence_only | 3054 | 980 | 2074 | 0.61028452 | none |
| question_plus_explanation | 4 | All | support_aware | 7405 | 3210 | 4195 | 0.63671278 | none |
| question_plus_explanation | 4 | 31777 | support_aware | 2809 | 1652 | 1157 | 0.66112839 | none |
| question_plus_explanation | 4 | 33471 | support_aware | 1542 | 578 | 964 | 0.45384176 | none |
| question_plus_explanation | 4 | 89443 | support_aware | 3054 | 980 | 2074 | 0.6113748 | none |
| question_plus_explanation | 4 | All | raw_confidence | 7405 | 3210 | 4195 | 0.62122899 | none |
| question_plus_explanation | 4 | 31777 | raw_confidence | 2809 | 1652 | 1157 | 0.64799588 | none |
| question_plus_explanation | 4 | 33471 | raw_confidence | 1542 | 578 | 964 | 0.41958966 | none |
| question_plus_explanation | 4 | 89443 | raw_confidence | 3054 | 980 | 2074 | 0.61071552 | none |
| question_plus_explanation | 4 | All | frequency | 7405 | 2970 | 4435 | 0.5 | none |
| question_plus_explanation | 4 | 31777 | frequency | 2809 | 1628 | 1181 | 0.5 | none |
| question_plus_explanation | 4 | 33471 | frequency | 1542 | 701 | 841 | 0.5 | none |
| question_plus_explanation | 4 | 89443 | frequency | 3054 | 641 | 2413 | 0.5 | none |

## AUROC fold summaries and paired differences

| Arm | Rule / learned-minus-control | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|---|
| explanation_only | learned_reliability | 0.79090387 | 0.66520905 | 0.68314103 | 0.6391748 | 0.69421645 | 0.69452904 ± 0.057753021 [5] |
| explanation_only | confidence_only | 0.57542213 | 0.61418683 | 0.62852487 | 0.59730018 | 0.61346184 | 0.60577917 ± 0.020251679 [5] |
| explanation_only | support_aware | 0.63576087 | 0.63225518 | 0.66221689 | 0.62047918 | 0.64767853 | 0.63967813 ± 0.015898479 [5] |
| explanation_only | raw_confidence | 0.57693039 | 0.61624018 | 0.63105094 | 0.59253856 | 0.61202014 | 0.60575604 ± 0.02118141 [5] |
| explanation_only | frequency | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 ± 0 [5] |
| question_plus_explanation | learned_reliability | 0.64118009 | 0.63435254 | 0.66960169 | 0.57354422 | 0.65043242 | 0.63382219 ± 0.03620748 [5] |
| question_plus_explanation | confidence_only | 0.61818843 | 0.60317774 | 0.62895297 | 0.57652937 | 0.62286192 | 0.60994209 ± 0.020967259 [5] |
| question_plus_explanation | support_aware | 0.62568456 | 0.62543935 | 0.66588622 | 0.58449596 | 0.63671278 | 0.62764377 ± 0.029219701 [5] |
| question_plus_explanation | raw_confidence | 0.61550241 | 0.60205728 | 0.63464224 | 0.57322618 | 0.62122899 | 0.60933142 ± 0.023327947 [5] |
| question_plus_explanation | frequency | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 ± 0 [5] |
| explanation_only | learned minus confidence_only | 0.21548174 | 0.051022219 | 0.054616165 | 0.041874621 | 0.080754605 | 0.08874987 ± 0.072302602 [5] |
| explanation_only | learned minus raw_confidence | 0.21397348 | 0.048968868 | 0.052090087 | 0.046636243 | 0.082196307 | 0.088772998 ± 0.07145615 [5] |
| explanation_only | learned minus support_aware | 0.155143 | 0.032953869 | 0.020924145 | 0.018695618 | 0.046537917 | 0.054850909 ± 0.057151814 [5] |
| question_plus_explanation | learned minus confidence_only | 0.022991664 | 0.031174803 | 0.040648727 | -0.0029851497 | 0.027570502 | 0.023880109 ± 0.016359627 [5] |
| question_plus_explanation | learned minus raw_confidence | 0.025677688 | 0.03229526 | 0.034959453 | 0.00031804307 | 0.029203435 | 0.024490776 ± 0.013950288 [5] |
| question_plus_explanation | learned minus support_aware | 0.015495539 | 0.0089131931 | 0.0037154732 | -0.010951737 | 0.013719641 | 0.0061784218 ± 0.010614449 [5] |

## Paired policy differences at the same target

| Arm | Target | Control | Fold | Learned coverage | Control coverage | Coverage difference | Risk difference |
|---|---|---|---|---|---|---|---|
| explanation_only | 10% | confidence_only | 0 | 0 | 0 | 0 | null |
| explanation_only | 10% | confidence_only | 1 | 0 | 0 | 0 | null |
| explanation_only | 10% | confidence_only | 2 | 0 | 0 | 0 | null |
| explanation_only | 10% | confidence_only | 3 | 0 | 0 | 0 | null |
| explanation_only | 10% | confidence_only | 4 | 0 | 0 | 0 | null |
| explanation_only | 10% | confidence_only | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 20% | confidence_only | 0 | 0 | 0 | 0 | null |
| explanation_only | 20% | confidence_only | 1 | 0 | 0 | 0 | null |
| explanation_only | 20% | confidence_only | 2 | 0 | 0 | 0 | null |
| explanation_only | 20% | confidence_only | 3 | 0 | 0 | 0 | null |
| explanation_only | 20% | confidence_only | 4 | 0 | 0 | 0 | null |
| explanation_only | 20% | confidence_only | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 30% | confidence_only | 0 | 0 | 0 | 0 | null |
| explanation_only | 30% | confidence_only | 1 | 0 | 0 | 0 | null |
| explanation_only | 30% | confidence_only | 2 | 0 | 0 | 0 | null |
| explanation_only | 30% | confidence_only | 3 | 0 | 0 | 0 | null |
| explanation_only | 30% | confidence_only | 4 | 0 | 0 | 0 | null |
| explanation_only | 30% | confidence_only | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 10% | raw_confidence | 0 | 0 | 0 | 0 | null |
| explanation_only | 10% | raw_confidence | 1 | 0 | 0 | 0 | null |
| explanation_only | 10% | raw_confidence | 2 | 0 | 0 | 0 | null |
| explanation_only | 10% | raw_confidence | 3 | 0 | 0 | 0 | null |
| explanation_only | 10% | raw_confidence | 4 | 0 | 0 | 0 | null |
| explanation_only | 10% | raw_confidence | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 20% | raw_confidence | 0 | 0 | 0 | 0 | null |
| explanation_only | 20% | raw_confidence | 1 | 0 | 0 | 0 | null |
| explanation_only | 20% | raw_confidence | 2 | 0 | 0 | 0 | null |
| explanation_only | 20% | raw_confidence | 3 | 0 | 0 | 0 | null |
| explanation_only | 20% | raw_confidence | 4 | 0 | 0 | 0 | null |
| explanation_only | 20% | raw_confidence | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 30% | raw_confidence | 0 | 0 | 0 | 0 | null |
| explanation_only | 30% | raw_confidence | 1 | 0 | 0 | 0 | null |
| explanation_only | 30% | raw_confidence | 2 | 0 | 0 | 0 | null |
| explanation_only | 30% | raw_confidence | 3 | 0 | 0 | 0 | null |
| explanation_only | 30% | raw_confidence | 4 | 0 | 0 | 0 | null |
| explanation_only | 30% | raw_confidence | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 10% | support_aware | 0 | 0 | 0 | 0 | null |
| explanation_only | 10% | support_aware | 1 | 0 | 0 | 0 | null |
| explanation_only | 10% | support_aware | 2 | 0 | 0 | 0 | null |
| explanation_only | 10% | support_aware | 3 | 0 | 0 | 0 | null |
| explanation_only | 10% | support_aware | 4 | 0 | 0 | 0 | null |
| explanation_only | 10% | support_aware | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 20% | support_aware | 0 | 0 | 0 | 0 | null |
| explanation_only | 20% | support_aware | 1 | 0 | 0 | 0 | null |
| explanation_only | 20% | support_aware | 2 | 0 | 0 | 0 | null |
| explanation_only | 20% | support_aware | 3 | 0 | 0 | 0 | null |
| explanation_only | 20% | support_aware | 4 | 0 | 0 | 0 | null |
| explanation_only | 20% | support_aware | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 30% | support_aware | 0 | 0 | 0 | 0 | null |
| explanation_only | 30% | support_aware | 1 | 0 | 0 | 0 | null |
| explanation_only | 30% | support_aware | 2 | 0 | 0 | 0 | null |
| explanation_only | 30% | support_aware | 3 | 0 | 0 | 0 | null |
| explanation_only | 30% | support_aware | 4 | 0 | 0 | 0 | null |
| explanation_only | 30% | support_aware | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 10% | frequency | 0 | 0 | 0 | 0 | null |
| explanation_only | 10% | frequency | 1 | 0 | 0 | 0 | null |
| explanation_only | 10% | frequency | 2 | 0 | 0 | 0 | null |
| explanation_only | 10% | frequency | 3 | 0 | 0 | 0 | null |
| explanation_only | 10% | frequency | 4 | 0 | 0 | 0 | null |
| explanation_only | 10% | frequency | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 20% | frequency | 0 | 0 | 0 | 0 | null |
| explanation_only | 20% | frequency | 1 | 0 | 0 | 0 | null |
| explanation_only | 20% | frequency | 2 | 0 | 0 | 0 | null |
| explanation_only | 20% | frequency | 3 | 0 | 0 | 0 | null |
| explanation_only | 20% | frequency | 4 | 0 | 0 | 0 | null |
| explanation_only | 20% | frequency | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| explanation_only | 30% | frequency | 0 | 0 | 0 | 0 | null |
| explanation_only | 30% | frequency | 1 | 0 | 0 | 0 | null |
| explanation_only | 30% | frequency | 2 | 0 | 0 | 0 | null |
| explanation_only | 30% | frequency | 3 | 0 | 0 | 0 | null |
| explanation_only | 30% | frequency | 4 | 0 | 0 | 0 | null |
| explanation_only | 30% | frequency | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 10% | confidence_only | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | confidence_only | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | confidence_only | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | confidence_only | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | confidence_only | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | confidence_only | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 20% | confidence_only | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | confidence_only | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | confidence_only | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | confidence_only | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | confidence_only | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | confidence_only | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 30% | confidence_only | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | confidence_only | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | confidence_only | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | confidence_only | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | confidence_only | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | confidence_only | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 10% | raw_confidence | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | raw_confidence | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | raw_confidence | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | raw_confidence | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | raw_confidence | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | raw_confidence | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 20% | raw_confidence | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | raw_confidence | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | raw_confidence | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | raw_confidence | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | raw_confidence | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | raw_confidence | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 30% | raw_confidence | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | raw_confidence | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | raw_confidence | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | raw_confidence | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | raw_confidence | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | raw_confidence | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 10% | support_aware | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | support_aware | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | support_aware | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | support_aware | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | support_aware | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | support_aware | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 20% | support_aware | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | support_aware | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | support_aware | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | support_aware | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | support_aware | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | support_aware | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 30% | support_aware | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | support_aware | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | support_aware | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | support_aware | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | support_aware | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | support_aware | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 10% | frequency | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | frequency | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | frequency | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | frequency | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | frequency | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 10% | frequency | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 20% | frequency | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | frequency | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | frequency | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | frequency | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | frequency | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 20% | frequency | Summary | — | — | 0 ± 0 [5] | null ± null [0] |
| question_plus_explanation | 30% | frequency | 0 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | frequency | 1 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | frequency | 2 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | frequency | 3 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | frequency | 4 | 0 | 0 | 0 | null |
| question_plus_explanation | 30% | frequency | Summary | — | — | 0 ± 0 [5] | null ± null [0] |

## Learned reliability calibration — all-case fold and question results

These are correctness-probability diagnostics, not multiclass classifier calibration. All three statistics require the fixed eligibility counts. Full stratum values and reasons are in the JSON.

| Arm | Fold | Scope | Target | n | Correct | Incorrect | Mean predicted correctness | Binary Brier | Binary ECE | Ineligible reasons |
|---|---|---|---|---|---|---|---|---|---|---|
| explanation_only | 0 | All | Unfiltered | 7686 | 2553 | 5133 | 0.29973423 | 0.18104044 | 0.09608601 | none |
| explanation_only | 0 | 31772 | Unfiltered | 4857 | 1671 | 3186 | 0.32245175 | 0.19612738 | 0.071139354 | none |
| explanation_only | 0 | 32829 | Unfiltered | 2156 | 760 | 1396 | 0.27603224 | 0.1666776 | 0.16343898 | none |
| explanation_only | 0 | 104665 | Unfiltered | 673 | 122 | 551 | 0.21171418 | 0.11817128 | 0.062962732 | none |
| explanation_only | 0 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 31772 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 32829 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 104665 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 31772 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 32829 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 104665 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 31772 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 32829 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 0 | 104665 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | All | Unfiltered | 7023 | 1980 | 5043 | 0.34107378 | 0.18900813 | 0.066458009 | none |
| explanation_only | 1 | 31778 | Unfiltered | 3640 | 1164 | 2476 | 0.37030531 | 0.18531412 | 0.064726951 | none |
| explanation_only | 1 | 32835 | Unfiltered | 2332 | 520 | 1812 | 0.31304486 | 0.19458396 | 0.12345919 | none |
| explanation_only | 1 | 109465 | Unfiltered | 1051 | 296 | 755 | 0.30202593 | 0.18942993 | 0.030097648 | none |
| explanation_only | 1 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 31778 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 32835 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 109465 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 31778 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 32835 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 109465 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 31778 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 32835 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 1 | 109465 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | All | Unfiltered | 7491 | 2583 | 4908 | 0.34921116 | 0.20508507 | 0.039119957 | none |
| explanation_only | 2 | 31774 | Unfiltered | 3115 | 1363 | 1752 | 0.39129099 | 0.23060555 | 0.08089668 | none |
| explanation_only | 2 | 33474 | Unfiltered | 1766 | 437 | 1329 | 0.34467048 | 0.21302656 | 0.11828448 | none |
| explanation_only | 2 | 91695 | Unfiltered | 2610 | 783 | 1827 | 0.3020618 | 0.16925327 | 0.056289037 | none |
| explanation_only | 2 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 31774 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 33474 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 91695 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 31774 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 33474 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 91695 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 31774 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 33474 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 2 | 91695 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | All | Unfiltered | 7091 | 2871 | 4220 | 0.40496717 | 0.22732023 | 0.046939797 | none |
| explanation_only | 3 | 32833 | Unfiltered | 3105 | 1121 | 1984 | 0.42520452 | 0.22733745 | 0.081668009 | none |
| explanation_only | 3 | 33472 | Unfiltered | 2800 | 1267 | 1533 | 0.40351857 | 0.23311585 | 0.056302621 | none |
| explanation_only | 3 | 76870 | Unfiltered | 1186 | 483 | 703 | 0.3554049 | 0.21359241 | 0.054295212 | none |
| explanation_only | 3 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 32833 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 33472 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 76870 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 32833 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 33472 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 76870 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 32833 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 33472 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 3 | 76870 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | All | Unfiltered | 7405 | 2997 | 4408 | 0.34700562 | 0.21817016 | 0.061047501 | none |
| explanation_only | 4 | 31777 | Unfiltered | 2809 | 1635 | 1174 | 0.44612021 | 0.23283251 | 0.13593746 | none |
| explanation_only | 4 | 33471 | Unfiltered | 1542 | 464 | 1078 | 0.35930019 | 0.22344304 | 0.19075741 | none |
| explanation_only | 4 | 89443 | Unfiltered | 3054 | 898 | 2156 | 0.2496346 | 0.20202174 | 0.083811539 | none |
| explanation_only | 4 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 31777 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 33471 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 89443 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 31777 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 33471 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 89443 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 31777 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 33471 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| explanation_only | 4 | 89443 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | All | Unfiltered | 7686 | 3014 | 4672 | 0.52112164 | 0.24310864 | 0.15837364 | none |
| question_plus_explanation | 0 | 31772 | Unfiltered | 4857 | 1732 | 3125 | 0.60647708 | 0.27422351 | 0.25010855 | none |
| question_plus_explanation | 0 | 32829 | Unfiltered | 2156 | 1199 | 957 | 0.41500544 | 0.21296836 | 0.2162983 | none |
| question_plus_explanation | 0 | 104665 | Unfiltered | 673 | 83 | 590 | 0.24506692 | 0.11511089 | 0.12173854 | none |
| question_plus_explanation | 0 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 31772 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 32829 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 104665 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 31772 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 32829 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 104665 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 31772 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 32829 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 0 | 104665 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | All | Unfiltered | 7023 | 2109 | 4914 | 0.37578668 | 0.20380481 | 0.09013899 | none |
| question_plus_explanation | 1 | 31778 | Unfiltered | 3640 | 1226 | 2414 | 0.37379773 | 0.20205469 | 0.059390774 | none |
| question_plus_explanation | 1 | 32835 | Unfiltered | 2332 | 439 | 1893 | 0.35617152 | 0.18937202 | 0.17523648 | none |
| question_plus_explanation | 1 | 109465 | Unfiltered | 1051 | 444 | 607 | 0.42619801 | 0.24189014 | 0.045566099 | none |
| question_plus_explanation | 1 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 31778 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 32835 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 109465 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 31778 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 32835 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 109465 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 31778 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 32835 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 1 | 109465 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | All | Unfiltered | 7491 | 2623 | 4868 | 0.31791066 | 0.20975715 | 0.033471754 | none |
| question_plus_explanation | 2 | 31774 | Unfiltered | 3115 | 1351 | 1764 | 0.32292472 | 0.23961792 | 0.11254658 | none |
| question_plus_explanation | 2 | 33474 | Unfiltered | 1766 | 401 | 1365 | 0.28386895 | 0.19808676 | 0.11146393 | none |
| question_plus_explanation | 2 | 91695 | Unfiltered | 2610 | 871 | 1739 | 0.33496003 | 0.18201524 | 0.098712729 | none |
| question_plus_explanation | 2 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 31774 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 33474 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 91695 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 31774 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 33474 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 91695 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 31774 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 33474 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 2 | 91695 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | All | Unfiltered | 7091 | 2875 | 4216 | 0.44033052 | 0.24739884 | 0.085503636 | none |
| question_plus_explanation | 3 | 32833 | Unfiltered | 3105 | 1212 | 1893 | 0.43198509 | 0.2753031 | 0.17168615 | none |
| question_plus_explanation | 3 | 33472 | Unfiltered | 2800 | 1271 | 1529 | 0.4445231 | 0.21443933 | 0.048336097 | none |
| question_plus_explanation | 3 | 76870 | Unfiltered | 1186 | 392 | 794 | 0.45228106 | 0.25215759 | 0.16418502 | none |
| question_plus_explanation | 3 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 32833 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 33472 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 76870 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 32833 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 33472 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 76870 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 32833 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 33472 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 3 | 76870 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | All | Unfiltered | 7405 | 3210 | 4195 | 0.35340843 | 0.2354141 | 0.080082455 | none |
| question_plus_explanation | 4 | 31777 | Unfiltered | 2809 | 1652 | 1157 | 0.42078092 | 0.24971965 | 0.16739812 | none |
| question_plus_explanation | 4 | 33471 | Unfiltered | 1542 | 578 | 964 | 0.39529245 | 0.24446437 | 0.099563305 | none |
| question_plus_explanation | 4 | 89443 | Unfiltered | 3054 | 980 | 2074 | 0.27029301 | 0.21768659 | 0.058707128 | none |
| question_plus_explanation | 4 | All | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 31777 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 33471 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 89443 | 10 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | All | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 31777 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 33471 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 89443 | 20 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | All | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 31777 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 33471 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |
| question_plus_explanation | 4 | 89443 | 30 | 0 | 0 | 0 | null | null | null | n_below_200, correct_below_20, incorrect_below_20 |

## Complete numeric fold summaries (all registered strata)

Five fold values, equal-fold mean, sample SD and eligible/defined count; undefined values are not imputed. These include support-stratum results even when no policy is admitted.

### explanation_only / learned_reliability / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.all.incorrect_n | 5133 | 5043 | 4908 | 4220 | 4408 | 4742.4 ± 404.6842 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.33216237 | 0.2819308 | 0.34481378 | 0.40487942 | 0.40472654 | 0.35370258 ± 0.052241491 [5] |
| classifier.all.map_at_3 | 0.47519299 | 0.45332004 | 0.49933253 | 0.51687585 | 0.53954535 | 0.49685335 ± 0.03388943 [5] |
| classifier.all.risk | 0.66783763 | 0.7180692 | 0.65518622 | 0.59512058 | 0.59527346 | 0.64629742 ± 0.052241491 [5] |
| classifier.all.mean_confidence | 0.54790645 | 0.5006183 | 0.34374157 | 0.62029297 | 0.57510411 | 0.51753268 ± 0.10640272 [5] |
| classifier.all.ece | 0.21574408 | 0.2186875 | 0.020030233 | 0.21541354 | 0.17183069 | 0.16834121 ± 0.085155604 [5] |
| classifier.all.brier | 0.88779982 | 0.89451124 | 0.80368179 | 0.84863038 | 0.8075918 | 0.848443 ± 0.042847589 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.5588242 | 0.46740816 | 0.31615669 | 0.61815543 | 0.58689641 | 0.50948818 ± 0.12184256 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.frequent.incorrect_n | 4726 | 3430 | 2923 | 2058 | 2820 | 3191.4 ± 988.24329 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.35073499 | 0.36598891 | 0.46912459 | 0.58247109 | 0.51521403 | 0.45670672 ± 0.098556727 [5] |
| classifier.frequent.map_at_3 | 0.50176306 | 0.58847813 | 0.6793498 | 0.74359234 | 0.68683743 | 0.64000415 ± 0.095180722 [5] |
| classifier.frequent.risk | 0.64926501 | 0.63401109 | 0.53087541 | 0.41752891 | 0.48478597 | 0.54329328 ± 0.098556727 [5] |
| classifier.frequent.mean_confidence | 0.54729599 | 0.51051996 | 0.35368635 | 0.62123055 | 0.57188489 | 0.52092355 ± 0.10177251 [5] |
| classifier.frequent.ece | 0.196561 | 0.14453105 | 0.11926662 | 0.055633989 | 0.062437156 | 0.11568596 ± 0.058794785 [5] |
| classifier.frequent.brier | 0.85785762 | 0.76538237 | 0.67038713 | 0.56878811 | 0.63112556 | 0.69870816 ± 0.11404244 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.well_supported.incorrect_n | 4472 | 3025 | 2923 | 2058 | 2725 | 3040.6 ± 884.31968 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.36341637 | 0.3956044 | 0.46912459 | 0.58247109 | 0.52376791 | 0.46687687 ± 0.089982647 [5] |
| classifier.well_supported.map_at_3 | 0.5199051 | 0.63583084 | 0.6793498 | 0.74359234 | 0.69824071 | 0.65538376 ± 0.085042089 [5] |
| classifier.well_supported.risk | 0.63658363 | 0.6043956 | 0.53087541 | 0.41752891 | 0.47623209 | 0.53312313 ± 0.089982647 [5] |
| classifier.well_supported.mean_confidence | 0.54648205 | 0.5148185 | 0.35368635 | 0.62123055 | 0.56871203 | 0.5209859 ± 0.10124723 [5] |
| classifier.well_supported.ece | 0.18306568 | 0.11921411 | 0.11926662 | 0.055633989 | 0.051519224 | 0.10573992 ± 0.054300752 [5] |
| classifier.well_supported.brier | 0.8376648 | 0.72182497 | 0.67038713 | 0.56878811 | 0.61449237 | 0.68263147 ± 0.10407285 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |
| reliability.all.n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| reliability.all.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| reliability.all.incorrect_n | 5133 | 5043 | 4908 | 4220 | 4408 | 4742.4 ± 404.6842 [5] |
| reliability.all.mean_predicted_correctness | 0.29973423 | 0.34107378 | 0.34921116 | 0.40496717 | 0.34700562 | 0.34839839 ± 0.037498261 [5] |
| reliability.all.binary_brier | 0.18104044 | 0.18900813 | 0.20508507 | 0.22732023 | 0.21817016 | 0.20412481 ± 0.019349572 [5] |
| reliability.all.binary_ece | 0.09608601 | 0.066458009 | 0.039119957 | 0.046939797 | 0.061047501 | 0.061930255 ± 0.021982487 [5] |
| reliability.unsupported.n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| reliability.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| reliability.unsupported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.rare.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.frequent.n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| reliability.frequent.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| reliability.frequent.incorrect_n | 4726 | 3430 | 2923 | 2058 | 2820 | 3191.4 ± 988.24329 [5] |
| reliability.frequent.mean_predicted_correctness | 0.29895058 | 0.34961158 | 0.35145984 | 0.40866725 | 0.34127435 | 0.34999272 ± 0.03913537 [5] |
| reliability.frequent.binary_brier | 0.18418781 | 0.21134752 | 0.22548507 | 0.24501125 | 0.23197706 | 0.21960174 ± 0.023214672 [5] |
| reliability.frequent.binary_ece | 0.10978854 | 0.039638207 | 0.11770124 | 0.17576557 | 0.17741537 | 0.12406179 ± 0.05677017 [5] |
| reliability.well_supported.n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| reliability.well_supported.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| reliability.well_supported.incorrect_n | 4472 | 3025 | 2923 | 2058 | 2725 | 3040.6 ± 884.31968 [5] |
| reliability.well_supported.mean_predicted_correctness | 0.29899012 | 0.35140766 | 0.35145984 | 0.40866725 | 0.33836338 | 0.34977765 ± 0.039316443 [5] |
| reliability.well_supported.binary_brier | 0.18746189 | 0.217778 | 0.22548507 | 0.24501125 | 0.2311845 | 0.22138414 ± 0.021417448 [5] |
| reliability.well_supported.binary_ece | 0.11226734 | 0.050566047 | 0.11770124 | 0.17576557 | 0.18893793 | 0.12904763 ± 0.055540734 [5] |

### explanation_only / learned_reliability / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |
| reliability.all.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.rare.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.frequent.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_ece | null | null | null | null | null | null ± null [0] |

### explanation_only / learned_reliability / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |
| reliability.all.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.rare.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.frequent.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_ece | null | null | null | null | null | null ± null [0] |

### explanation_only / learned_reliability / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |
| reliability.all.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.rare.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.frequent.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_ece | null | null | null | null | null | null ± null [0] |

### explanation_only / confidence_only / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.all.incorrect_n | 5133 | 5043 | 4908 | 4220 | 4408 | 4742.4 ± 404.6842 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.33216237 | 0.2819308 | 0.34481378 | 0.40487942 | 0.40472654 | 0.35370258 ± 0.052241491 [5] |
| classifier.all.map_at_3 | 0.47519299 | 0.45332004 | 0.49933253 | 0.51687585 | 0.53954535 | 0.49685335 ± 0.03388943 [5] |
| classifier.all.risk | 0.66783763 | 0.7180692 | 0.65518622 | 0.59512058 | 0.59527346 | 0.64629742 ± 0.052241491 [5] |
| classifier.all.mean_confidence | 0.54790645 | 0.5006183 | 0.34374157 | 0.62029297 | 0.57510411 | 0.51753268 ± 0.10640272 [5] |
| classifier.all.ece | 0.21574408 | 0.2186875 | 0.020030233 | 0.21541354 | 0.17183069 | 0.16834121 ± 0.085155604 [5] |
| classifier.all.brier | 0.88779982 | 0.89451124 | 0.80368179 | 0.84863038 | 0.8075918 | 0.848443 ± 0.042847589 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.5588242 | 0.46740816 | 0.31615669 | 0.61815543 | 0.58689641 | 0.50948818 ± 0.12184256 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.frequent.incorrect_n | 4726 | 3430 | 2923 | 2058 | 2820 | 3191.4 ± 988.24329 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.35073499 | 0.36598891 | 0.46912459 | 0.58247109 | 0.51521403 | 0.45670672 ± 0.098556727 [5] |
| classifier.frequent.map_at_3 | 0.50176306 | 0.58847813 | 0.6793498 | 0.74359234 | 0.68683743 | 0.64000415 ± 0.095180722 [5] |
| classifier.frequent.risk | 0.64926501 | 0.63401109 | 0.53087541 | 0.41752891 | 0.48478597 | 0.54329328 ± 0.098556727 [5] |
| classifier.frequent.mean_confidence | 0.54729599 | 0.51051996 | 0.35368635 | 0.62123055 | 0.57188489 | 0.52092355 ± 0.10177251 [5] |
| classifier.frequent.ece | 0.196561 | 0.14453105 | 0.11926662 | 0.055633989 | 0.062437156 | 0.11568596 ± 0.058794785 [5] |
| classifier.frequent.brier | 0.85785762 | 0.76538237 | 0.67038713 | 0.56878811 | 0.63112556 | 0.69870816 ± 0.11404244 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.well_supported.incorrect_n | 4472 | 3025 | 2923 | 2058 | 2725 | 3040.6 ± 884.31968 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.36341637 | 0.3956044 | 0.46912459 | 0.58247109 | 0.52376791 | 0.46687687 ± 0.089982647 [5] |
| classifier.well_supported.map_at_3 | 0.5199051 | 0.63583084 | 0.6793498 | 0.74359234 | 0.69824071 | 0.65538376 ± 0.085042089 [5] |
| classifier.well_supported.risk | 0.63658363 | 0.6043956 | 0.53087541 | 0.41752891 | 0.47623209 | 0.53312313 ± 0.089982647 [5] |
| classifier.well_supported.mean_confidence | 0.54648205 | 0.5148185 | 0.35368635 | 0.62123055 | 0.56871203 | 0.5209859 ± 0.10124723 [5] |
| classifier.well_supported.ece | 0.18306568 | 0.11921411 | 0.11926662 | 0.055633989 | 0.051519224 | 0.10573992 ± 0.054300752 [5] |
| classifier.well_supported.brier | 0.8376648 | 0.72182497 | 0.67038713 | 0.56878811 | 0.61449237 | 0.68263147 ± 0.10407285 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / confidence_only / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / confidence_only / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / confidence_only / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / support_aware / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.all.incorrect_n | 5133 | 5043 | 4908 | 4220 | 4408 | 4742.4 ± 404.6842 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.33216237 | 0.2819308 | 0.34481378 | 0.40487942 | 0.40472654 | 0.35370258 ± 0.052241491 [5] |
| classifier.all.map_at_3 | 0.47519299 | 0.45332004 | 0.49933253 | 0.51687585 | 0.53954535 | 0.49685335 ± 0.03388943 [5] |
| classifier.all.risk | 0.66783763 | 0.7180692 | 0.65518622 | 0.59512058 | 0.59527346 | 0.64629742 ± 0.052241491 [5] |
| classifier.all.mean_confidence | 0.54790645 | 0.5006183 | 0.34374157 | 0.62029297 | 0.57510411 | 0.51753268 ± 0.10640272 [5] |
| classifier.all.ece | 0.21574408 | 0.2186875 | 0.020030233 | 0.21541354 | 0.17183069 | 0.16834121 ± 0.085155604 [5] |
| classifier.all.brier | 0.88779982 | 0.89451124 | 0.80368179 | 0.84863038 | 0.8075918 | 0.848443 ± 0.042847589 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.5588242 | 0.46740816 | 0.31615669 | 0.61815543 | 0.58689641 | 0.50948818 ± 0.12184256 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.frequent.incorrect_n | 4726 | 3430 | 2923 | 2058 | 2820 | 3191.4 ± 988.24329 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.35073499 | 0.36598891 | 0.46912459 | 0.58247109 | 0.51521403 | 0.45670672 ± 0.098556727 [5] |
| classifier.frequent.map_at_3 | 0.50176306 | 0.58847813 | 0.6793498 | 0.74359234 | 0.68683743 | 0.64000415 ± 0.095180722 [5] |
| classifier.frequent.risk | 0.64926501 | 0.63401109 | 0.53087541 | 0.41752891 | 0.48478597 | 0.54329328 ± 0.098556727 [5] |
| classifier.frequent.mean_confidence | 0.54729599 | 0.51051996 | 0.35368635 | 0.62123055 | 0.57188489 | 0.52092355 ± 0.10177251 [5] |
| classifier.frequent.ece | 0.196561 | 0.14453105 | 0.11926662 | 0.055633989 | 0.062437156 | 0.11568596 ± 0.058794785 [5] |
| classifier.frequent.brier | 0.85785762 | 0.76538237 | 0.67038713 | 0.56878811 | 0.63112556 | 0.69870816 ± 0.11404244 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.well_supported.incorrect_n | 4472 | 3025 | 2923 | 2058 | 2725 | 3040.6 ± 884.31968 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.36341637 | 0.3956044 | 0.46912459 | 0.58247109 | 0.52376791 | 0.46687687 ± 0.089982647 [5] |
| classifier.well_supported.map_at_3 | 0.5199051 | 0.63583084 | 0.6793498 | 0.74359234 | 0.69824071 | 0.65538376 ± 0.085042089 [5] |
| classifier.well_supported.risk | 0.63658363 | 0.6043956 | 0.53087541 | 0.41752891 | 0.47623209 | 0.53312313 ± 0.089982647 [5] |
| classifier.well_supported.mean_confidence | 0.54648205 | 0.5148185 | 0.35368635 | 0.62123055 | 0.56871203 | 0.5209859 ± 0.10124723 [5] |
| classifier.well_supported.ece | 0.18306568 | 0.11921411 | 0.11926662 | 0.055633989 | 0.051519224 | 0.10573992 ± 0.054300752 [5] |
| classifier.well_supported.brier | 0.8376648 | 0.72182497 | 0.67038713 | 0.56878811 | 0.61449237 | 0.68263147 ± 0.10407285 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / support_aware / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / support_aware / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / support_aware / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / raw_confidence / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.all.incorrect_n | 5133 | 5043 | 4908 | 4220 | 4408 | 4742.4 ± 404.6842 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.33216237 | 0.2819308 | 0.34481378 | 0.40487942 | 0.40472654 | 0.35370258 ± 0.052241491 [5] |
| classifier.all.map_at_3 | 0.47519299 | 0.45332004 | 0.49933253 | 0.51687585 | 0.53954535 | 0.49685335 ± 0.03388943 [5] |
| classifier.all.risk | 0.66783763 | 0.7180692 | 0.65518622 | 0.59512058 | 0.59527346 | 0.64629742 ± 0.052241491 [5] |
| classifier.all.mean_confidence | 0.54790645 | 0.5006183 | 0.34374157 | 0.62029297 | 0.57510411 | 0.51753268 ± 0.10640272 [5] |
| classifier.all.ece | 0.21574408 | 0.2186875 | 0.020030233 | 0.21541354 | 0.17183069 | 0.16834121 ± 0.085155604 [5] |
| classifier.all.brier | 0.88779982 | 0.89451124 | 0.80368179 | 0.84863038 | 0.8075918 | 0.848443 ± 0.042847589 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.5588242 | 0.46740816 | 0.31615669 | 0.61815543 | 0.58689641 | 0.50948818 ± 0.12184256 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.frequent.incorrect_n | 4726 | 3430 | 2923 | 2058 | 2820 | 3191.4 ± 988.24329 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.35073499 | 0.36598891 | 0.46912459 | 0.58247109 | 0.51521403 | 0.45670672 ± 0.098556727 [5] |
| classifier.frequent.map_at_3 | 0.50176306 | 0.58847813 | 0.6793498 | 0.74359234 | 0.68683743 | 0.64000415 ± 0.095180722 [5] |
| classifier.frequent.risk | 0.64926501 | 0.63401109 | 0.53087541 | 0.41752891 | 0.48478597 | 0.54329328 ± 0.098556727 [5] |
| classifier.frequent.mean_confidence | 0.54729599 | 0.51051996 | 0.35368635 | 0.62123055 | 0.57188489 | 0.52092355 ± 0.10177251 [5] |
| classifier.frequent.ece | 0.196561 | 0.14453105 | 0.11926662 | 0.055633989 | 0.062437156 | 0.11568596 ± 0.058794785 [5] |
| classifier.frequent.brier | 0.85785762 | 0.76538237 | 0.67038713 | 0.56878811 | 0.63112556 | 0.69870816 ± 0.11404244 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 2553 | 1980 | 2583 | 2871 | 2997 | 2596.8 ± 393.03206 [5] |
| classifier.well_supported.incorrect_n | 4472 | 3025 | 2923 | 2058 | 2725 | 3040.6 ± 884.31968 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.36341637 | 0.3956044 | 0.46912459 | 0.58247109 | 0.52376791 | 0.46687687 ± 0.089982647 [5] |
| classifier.well_supported.map_at_3 | 0.5199051 | 0.63583084 | 0.6793498 | 0.74359234 | 0.69824071 | 0.65538376 ± 0.085042089 [5] |
| classifier.well_supported.risk | 0.63658363 | 0.6043956 | 0.53087541 | 0.41752891 | 0.47623209 | 0.53312313 ± 0.089982647 [5] |
| classifier.well_supported.mean_confidence | 0.54648205 | 0.5148185 | 0.35368635 | 0.62123055 | 0.56871203 | 0.5209859 ± 0.10124723 [5] |
| classifier.well_supported.ece | 0.18306568 | 0.11921411 | 0.11926662 | 0.055633989 | 0.051519224 | 0.10573992 ± 0.054300752 [5] |
| classifier.well_supported.brier | 0.8376648 | 0.72182497 | 0.67038713 | 0.56878811 | 0.61449237 | 0.68263147 ± 0.10407285 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / raw_confidence / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / raw_confidence / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / raw_confidence / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / frequency / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 3734 | 2521 | 2962 | 2615 | 2970 | 2960.4 ± 477.21201 [5] |
| classifier.all.incorrect_n | 3952 | 4502 | 4529 | 4476 | 4435 | 4378.8 ± 241.09272 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.48581837 | 0.35896341 | 0.39540782 | 0.36877732 | 0.40108035 | 0.40200945 ± 0.050064249 [5] |
| classifier.all.map_at_3 | 0.59181195 | 0.5018036 | 0.53882437 | 0.50122221 | 0.56241278 | 0.53921498 ± 0.039203937 [5] |
| classifier.all.risk | 0.51418163 | 0.64103659 | 0.60459218 | 0.63122268 | 0.59891965 | 0.59799055 ± 0.050064249 [5] |
| classifier.all.mean_confidence | 0.37317163 | 0.41480766 | 0.441297 | 0.41765069 | 0.41918322 | 0.41322204 ± 0.024748237 [5] |
| classifier.all.ece | 0.11264674 | 0.055844253 | 0.045889176 | 0.048873362 | 0.018102867 | 0.056271279 ± 0.034632786 [5] |
| classifier.all.brier | 0.75585416 | 0.82352498 | 0.79378899 | 0.82213474 | 0.77998281 | 0.79505714 ± 0.028763396 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.37317163 | 0.41480766 | 0.441297 | 0.41765069 | 0.41918322 | 0.41322204 ± 0.024748237 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 3734 | 2521 | 2962 | 2615 | 2970 | 2960.4 ± 477.21201 [5] |
| classifier.frequent.incorrect_n | 3545 | 2889 | 2544 | 2314 | 2847 | 2827.8 ± 464.4951 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.51298255 | 0.46598891 | 0.53795859 | 0.53053358 | 0.51057246 | 0.51160722 ± 0.028002653 [5] |
| classifier.frequent.map_at_3 | 0.62490269 | 0.65141713 | 0.73307907 | 0.72107256 | 0.71594751 | 0.68928379 ± 0.048006032 [5] |
| classifier.frequent.risk | 0.48701745 | 0.53401109 | 0.46204141 | 0.46946642 | 0.48942754 | 0.48839278 ± 0.028002653 [5] |
| classifier.frequent.mean_confidence | 0.37317163 | 0.41480766 | 0.441297 | 0.41765069 | 0.41918322 | 0.41322204 ± 0.024748237 [5] |
| classifier.frequent.ece | 0.13981092 | 0.051181251 | 0.096661592 | 0.11288289 | 0.091389242 | 0.098385179 ± 0.032428383 [5] |
| classifier.frequent.brier | 0.73049733 | 0.70086877 | 0.62843511 | 0.64107891 | 0.65717317 | 0.67161066 ± 0.042803138 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 3734 | 2521 | 2962 | 2615 | 2970 | 2960.4 ± 477.21201 [5] |
| classifier.well_supported.incorrect_n | 3291 | 2484 | 2544 | 2314 | 2752 | 2677 ± 377.26913 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.53153025 | 0.5036963 | 0.53795859 | 0.53053358 | 0.51904928 | 0.5245536 ± 0.013504183 [5] |
| classifier.well_supported.map_at_3 | 0.64749703 | 0.7041292 | 0.73307907 | 0.72107256 | 0.72783409 | 0.70672239 ± 0.034859264 [5] |
| classifier.well_supported.risk | 0.46846975 | 0.4963037 | 0.46204141 | 0.46946642 | 0.48095072 | 0.4754464 ± 0.013504183 [5] |
| classifier.well_supported.mean_confidence | 0.37317163 | 0.41480766 | 0.441297 | 0.41765069 | 0.41918322 | 0.41322204 ± 0.024748237 [5] |
| classifier.well_supported.ece | 0.15835861 | 0.088888645 | 0.096661592 | 0.11288289 | 0.099866065 | 0.11133156 ± 0.027678062 [5] |
| classifier.well_supported.brier | 0.71330754 | 0.65808402 | 0.62843511 | 0.64107891 | 0.64993832 | 0.65816878 ± 0.032726844 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / frequency / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / frequency / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### explanation_only / frequency / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / learned_reliability / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.all.incorrect_n | 4672 | 4914 | 4868 | 4216 | 4195 | 4573 ± 347.64925 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.39214156 | 0.30029902 | 0.35015352 | 0.40544352 | 0.43349088 | 0.3763057 ± 0.052035768 [5] |
| classifier.all.map_at_3 | 0.52159771 | 0.47135602 | 0.50812086 | 0.52221125 | 0.57656989 | 0.51997115 ± 0.037798614 [5] |
| classifier.all.risk | 0.60785844 | 0.69970098 | 0.64984648 | 0.59455648 | 0.56650912 | 0.6236943 ± 0.052035768 [5] |
| classifier.all.mean_confidence | 0.62759395 | 0.38147442 | 0.36707686 | 0.73626429 | 0.57275345 | 0.5370326 ± 0.15988582 [5] |
| classifier.all.ece | 0.2354524 | 0.085969181 | 0.024472018 | 0.33082077 | 0.13926257 | 0.16319539 ± 0.12155265 [5] |
| classifier.all.brier | 0.84782063 | 0.83256243 | 0.79055821 | 0.90880073 | 0.75609422 | 0.82716724 ± 0.058119044 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.52378577 | 0.35742253 | 0.34307905 | 0.76509255 | 0.58928514 | 0.51573301 ± 0.17501896 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.frequent.incorrect_n | 4265 | 3301 | 2883 | 2054 | 2607 | 3022 ± 829.37627 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.41406787 | 0.38983364 | 0.47638939 | 0.58328261 | 0.55183084 | 0.48308087 ± 0.084067776 [5] |
| classifier.frequent.map_at_3 | 0.55076247 | 0.61189156 | 0.69130645 | 0.75126801 | 0.7339694 | 0.66783958 ± 0.084736918 [5] |
| classifier.frequent.risk | 0.58593213 | 0.61016636 | 0.52361061 | 0.41671739 | 0.44816916 | 0.51691913 ± 0.084067776 [5] |
| classifier.frequent.mean_confidence | 0.63339831 | 0.38864553 | 0.37572845 | 0.7236194 | 0.56824042 | 0.53792642 ± 0.15256856 [5] |
| classifier.frequent.ece | 0.22096024 | 0.030992432 | 0.10103658 | 0.14033678 | 0.017106222 | 0.10208645 ± 0.083473298 [5] |
| classifier.frequent.brier | 0.81879788 | 0.71866359 | 0.64484121 | 0.58087542 | 0.56623347 | 0.66588231 ± 0.10460381 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.well_supported.incorrect_n | 4011 | 2896 | 2883 | 2054 | 2512 | 2871.2 ± 724.00601 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.42903915 | 0.42137862 | 0.47638939 | 0.58328261 | 0.56099266 | 0.49421649 ± 0.074604085 [5] |
| classifier.well_supported.map_at_3 | 0.57067616 | 0.66140526 | 0.69130645 | 0.75126801 | 0.74615519 | 0.68416221 ± 0.073814498 [5] |
| classifier.well_supported.risk | 0.57096085 | 0.57862138 | 0.52361061 | 0.41671739 | 0.43900734 | 0.50578351 ± 0.074604085 [5] |
| classifier.well_supported.mean_confidence | 0.63134237 | 0.38797688 | 0.37572845 | 0.7236194 | 0.56666813 | 0.53706705 ± 0.15233504 [5] |
| classifier.well_supported.ece | 0.20419037 | 0.039333199 | 0.10103658 | 0.14033678 | 0.01414319 | 0.099808025 ± 0.07670631 [5] |
| classifier.well_supported.brier | 0.79339273 | 0.6753936 | 0.64484121 | 0.58087542 | 0.55072721 | 0.64904603 ± 0.094685884 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |
| reliability.all.n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| reliability.all.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| reliability.all.incorrect_n | 4672 | 4914 | 4868 | 4216 | 4195 | 4573 ± 347.64925 [5] |
| reliability.all.mean_predicted_correctness | 0.52112164 | 0.37578668 | 0.31791066 | 0.44033052 | 0.35340843 | 0.40171159 ± 0.08027776 [5] |
| reliability.all.binary_brier | 0.24310864 | 0.20380481 | 0.20975715 | 0.24739884 | 0.2354141 | 0.22789671 ± 0.0198602 [5] |
| reliability.all.binary_ece | 0.15837364 | 0.09013899 | 0.033471754 | 0.085503636 | 0.080082455 | 0.089514094 ± 0.044687276 [5] |
| reliability.unsupported.n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| reliability.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| reliability.unsupported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.rare.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.frequent.n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| reliability.frequent.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| reliability.frequent.incorrect_n | 4265 | 3301 | 2883 | 2054 | 2607 | 3022 ± 829.37627 [5] |
| reliability.frequent.mean_predicted_correctness | 0.52888153 | 0.37784984 | 0.31887793 | 0.42610013 | 0.35067575 | 0.40047704 ± 0.081845631 [5] |
| reliability.frequent.binary_brier | 0.24675658 | 0.22072989 | 0.24162419 | 0.24832367 | 0.25824621 | 0.24313611 ± 0.013898366 [5] |
| reliability.frequent.binary_ece | 0.16282788 | 0.036557306 | 0.15751147 | 0.15718248 | 0.20115509 | 0.14304684 ± 0.062283466 [5] |
| reliability.well_supported.n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| reliability.well_supported.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| reliability.well_supported.incorrect_n | 4011 | 2896 | 2883 | 2054 | 2512 | 2871.2 ± 724.00601 [5] |
| reliability.well_supported.mean_predicted_correctness | 0.52635622 | 0.38174917 | 0.31887793 | 0.42610013 | 0.34876106 | 0.4003689 ± 0.080910048 [5] |
| reliability.well_supported.binary_brier | 0.24255584 | 0.22853039 | 0.24162419 | 0.24832367 | 0.25876617 | 0.24396005 ± 0.010997327 [5] |
| reliability.well_supported.binary_ece | 0.14953053 | 0.045457471 | 0.15751147 | 0.15718248 | 0.2122316 | 0.14438271 ± 0.060729674 [5] |

### question_plus_explanation / learned_reliability / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |
| reliability.all.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.rare.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.frequent.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_ece | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / learned_reliability / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |
| reliability.all.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.rare.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.frequent.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_ece | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / learned_reliability / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |
| reliability.all.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.all.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.all.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.unsupported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.unsupported.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.rare.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.rare.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.rare.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.frequent.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.frequent.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.frequent.binary_ece | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| reliability.well_supported.mean_predicted_correctness | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_brier | null | null | null | null | null | null ± null [0] |
| reliability.well_supported.binary_ece | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / confidence_only / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.all.incorrect_n | 4672 | 4914 | 4868 | 4216 | 4195 | 4573 ± 347.64925 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.39214156 | 0.30029902 | 0.35015352 | 0.40544352 | 0.43349088 | 0.3763057 ± 0.052035768 [5] |
| classifier.all.map_at_3 | 0.52159771 | 0.47135602 | 0.50812086 | 0.52221125 | 0.57656989 | 0.51997115 ± 0.037798614 [5] |
| classifier.all.risk | 0.60785844 | 0.69970098 | 0.64984648 | 0.59455648 | 0.56650912 | 0.6236943 ± 0.052035768 [5] |
| classifier.all.mean_confidence | 0.62759395 | 0.38147442 | 0.36707686 | 0.73626429 | 0.57275345 | 0.5370326 ± 0.15988582 [5] |
| classifier.all.ece | 0.2354524 | 0.085969181 | 0.024472018 | 0.33082077 | 0.13926257 | 0.16319539 ± 0.12155265 [5] |
| classifier.all.brier | 0.84782063 | 0.83256243 | 0.79055821 | 0.90880073 | 0.75609422 | 0.82716724 ± 0.058119044 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.52378577 | 0.35742253 | 0.34307905 | 0.76509255 | 0.58928514 | 0.51573301 ± 0.17501896 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.frequent.incorrect_n | 4265 | 3301 | 2883 | 2054 | 2607 | 3022 ± 829.37627 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.41406787 | 0.38983364 | 0.47638939 | 0.58328261 | 0.55183084 | 0.48308087 ± 0.084067776 [5] |
| classifier.frequent.map_at_3 | 0.55076247 | 0.61189156 | 0.69130645 | 0.75126801 | 0.7339694 | 0.66783958 ± 0.084736918 [5] |
| classifier.frequent.risk | 0.58593213 | 0.61016636 | 0.52361061 | 0.41671739 | 0.44816916 | 0.51691913 ± 0.084067776 [5] |
| classifier.frequent.mean_confidence | 0.63339831 | 0.38864553 | 0.37572845 | 0.7236194 | 0.56824042 | 0.53792642 ± 0.15256856 [5] |
| classifier.frequent.ece | 0.22096024 | 0.030992432 | 0.10103658 | 0.14033678 | 0.017106222 | 0.10208645 ± 0.083473298 [5] |
| classifier.frequent.brier | 0.81879788 | 0.71866359 | 0.64484121 | 0.58087542 | 0.56623347 | 0.66588231 ± 0.10460381 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.well_supported.incorrect_n | 4011 | 2896 | 2883 | 2054 | 2512 | 2871.2 ± 724.00601 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.42903915 | 0.42137862 | 0.47638939 | 0.58328261 | 0.56099266 | 0.49421649 ± 0.074604085 [5] |
| classifier.well_supported.map_at_3 | 0.57067616 | 0.66140526 | 0.69130645 | 0.75126801 | 0.74615519 | 0.68416221 ± 0.073814498 [5] |
| classifier.well_supported.risk | 0.57096085 | 0.57862138 | 0.52361061 | 0.41671739 | 0.43900734 | 0.50578351 ± 0.074604085 [5] |
| classifier.well_supported.mean_confidence | 0.63134237 | 0.38797688 | 0.37572845 | 0.7236194 | 0.56666813 | 0.53706705 ± 0.15233504 [5] |
| classifier.well_supported.ece | 0.20419037 | 0.039333199 | 0.10103658 | 0.14033678 | 0.01414319 | 0.099808025 ± 0.07670631 [5] |
| classifier.well_supported.brier | 0.79339273 | 0.6753936 | 0.64484121 | 0.58087542 | 0.55072721 | 0.64904603 ± 0.094685884 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / confidence_only / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / confidence_only / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / confidence_only / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / support_aware / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.all.incorrect_n | 4672 | 4914 | 4868 | 4216 | 4195 | 4573 ± 347.64925 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.39214156 | 0.30029902 | 0.35015352 | 0.40544352 | 0.43349088 | 0.3763057 ± 0.052035768 [5] |
| classifier.all.map_at_3 | 0.52159771 | 0.47135602 | 0.50812086 | 0.52221125 | 0.57656989 | 0.51997115 ± 0.037798614 [5] |
| classifier.all.risk | 0.60785844 | 0.69970098 | 0.64984648 | 0.59455648 | 0.56650912 | 0.6236943 ± 0.052035768 [5] |
| classifier.all.mean_confidence | 0.62759395 | 0.38147442 | 0.36707686 | 0.73626429 | 0.57275345 | 0.5370326 ± 0.15988582 [5] |
| classifier.all.ece | 0.2354524 | 0.085969181 | 0.024472018 | 0.33082077 | 0.13926257 | 0.16319539 ± 0.12155265 [5] |
| classifier.all.brier | 0.84782063 | 0.83256243 | 0.79055821 | 0.90880073 | 0.75609422 | 0.82716724 ± 0.058119044 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.52378577 | 0.35742253 | 0.34307905 | 0.76509255 | 0.58928514 | 0.51573301 ± 0.17501896 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.frequent.incorrect_n | 4265 | 3301 | 2883 | 2054 | 2607 | 3022 ± 829.37627 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.41406787 | 0.38983364 | 0.47638939 | 0.58328261 | 0.55183084 | 0.48308087 ± 0.084067776 [5] |
| classifier.frequent.map_at_3 | 0.55076247 | 0.61189156 | 0.69130645 | 0.75126801 | 0.7339694 | 0.66783958 ± 0.084736918 [5] |
| classifier.frequent.risk | 0.58593213 | 0.61016636 | 0.52361061 | 0.41671739 | 0.44816916 | 0.51691913 ± 0.084067776 [5] |
| classifier.frequent.mean_confidence | 0.63339831 | 0.38864553 | 0.37572845 | 0.7236194 | 0.56824042 | 0.53792642 ± 0.15256856 [5] |
| classifier.frequent.ece | 0.22096024 | 0.030992432 | 0.10103658 | 0.14033678 | 0.017106222 | 0.10208645 ± 0.083473298 [5] |
| classifier.frequent.brier | 0.81879788 | 0.71866359 | 0.64484121 | 0.58087542 | 0.56623347 | 0.66588231 ± 0.10460381 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.well_supported.incorrect_n | 4011 | 2896 | 2883 | 2054 | 2512 | 2871.2 ± 724.00601 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.42903915 | 0.42137862 | 0.47638939 | 0.58328261 | 0.56099266 | 0.49421649 ± 0.074604085 [5] |
| classifier.well_supported.map_at_3 | 0.57067616 | 0.66140526 | 0.69130645 | 0.75126801 | 0.74615519 | 0.68416221 ± 0.073814498 [5] |
| classifier.well_supported.risk | 0.57096085 | 0.57862138 | 0.52361061 | 0.41671739 | 0.43900734 | 0.50578351 ± 0.074604085 [5] |
| classifier.well_supported.mean_confidence | 0.63134237 | 0.38797688 | 0.37572845 | 0.7236194 | 0.56666813 | 0.53706705 ± 0.15233504 [5] |
| classifier.well_supported.ece | 0.20419037 | 0.039333199 | 0.10103658 | 0.14033678 | 0.01414319 | 0.099808025 ± 0.07670631 [5] |
| classifier.well_supported.brier | 0.79339273 | 0.6753936 | 0.64484121 | 0.58087542 | 0.55072721 | 0.64904603 ± 0.094685884 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / support_aware / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / support_aware / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / support_aware / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / raw_confidence / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.all.incorrect_n | 4672 | 4914 | 4868 | 4216 | 4195 | 4573 ± 347.64925 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.39214156 | 0.30029902 | 0.35015352 | 0.40544352 | 0.43349088 | 0.3763057 ± 0.052035768 [5] |
| classifier.all.map_at_3 | 0.52159771 | 0.47135602 | 0.50812086 | 0.52221125 | 0.57656989 | 0.51997115 ± 0.037798614 [5] |
| classifier.all.risk | 0.60785844 | 0.69970098 | 0.64984648 | 0.59455648 | 0.56650912 | 0.6236943 ± 0.052035768 [5] |
| classifier.all.mean_confidence | 0.62759395 | 0.38147442 | 0.36707686 | 0.73626429 | 0.57275345 | 0.5370326 ± 0.15988582 [5] |
| classifier.all.ece | 0.2354524 | 0.085969181 | 0.024472018 | 0.33082077 | 0.13926257 | 0.16319539 ± 0.12155265 [5] |
| classifier.all.brier | 0.84782063 | 0.83256243 | 0.79055821 | 0.90880073 | 0.75609422 | 0.82716724 ± 0.058119044 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.52378577 | 0.35742253 | 0.34307905 | 0.76509255 | 0.58928514 | 0.51573301 ± 0.17501896 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.frequent.incorrect_n | 4265 | 3301 | 2883 | 2054 | 2607 | 3022 ± 829.37627 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.41406787 | 0.38983364 | 0.47638939 | 0.58328261 | 0.55183084 | 0.48308087 ± 0.084067776 [5] |
| classifier.frequent.map_at_3 | 0.55076247 | 0.61189156 | 0.69130645 | 0.75126801 | 0.7339694 | 0.66783958 ± 0.084736918 [5] |
| classifier.frequent.risk | 0.58593213 | 0.61016636 | 0.52361061 | 0.41671739 | 0.44816916 | 0.51691913 ± 0.084067776 [5] |
| classifier.frequent.mean_confidence | 0.63339831 | 0.38864553 | 0.37572845 | 0.7236194 | 0.56824042 | 0.53792642 ± 0.15256856 [5] |
| classifier.frequent.ece | 0.22096024 | 0.030992432 | 0.10103658 | 0.14033678 | 0.017106222 | 0.10208645 ± 0.083473298 [5] |
| classifier.frequent.brier | 0.81879788 | 0.71866359 | 0.64484121 | 0.58087542 | 0.56623347 | 0.66588231 ± 0.10460381 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 3014 | 2109 | 2623 | 2875 | 3210 | 2766.2 ± 425.03494 [5] |
| classifier.well_supported.incorrect_n | 4011 | 2896 | 2883 | 2054 | 2512 | 2871.2 ± 724.00601 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.42903915 | 0.42137862 | 0.47638939 | 0.58328261 | 0.56099266 | 0.49421649 ± 0.074604085 [5] |
| classifier.well_supported.map_at_3 | 0.57067616 | 0.66140526 | 0.69130645 | 0.75126801 | 0.74615519 | 0.68416221 ± 0.073814498 [5] |
| classifier.well_supported.risk | 0.57096085 | 0.57862138 | 0.52361061 | 0.41671739 | 0.43900734 | 0.50578351 ± 0.074604085 [5] |
| classifier.well_supported.mean_confidence | 0.63134237 | 0.38797688 | 0.37572845 | 0.7236194 | 0.56666813 | 0.53706705 ± 0.15233504 [5] |
| classifier.well_supported.ece | 0.20419037 | 0.039333199 | 0.10103658 | 0.14033678 | 0.01414319 | 0.099808025 ± 0.07670631 [5] |
| classifier.well_supported.brier | 0.79339273 | 0.6753936 | 0.64484121 | 0.58087542 | 0.55072721 | 0.64904603 ± 0.094685884 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / raw_confidence / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / raw_confidence / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / raw_confidence / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / frequency / Unfiltered

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.correct_n | 3734 | 2521 | 2962 | 2615 | 2970 | 2960.4 ± 477.21201 [5] |
| classifier.all.incorrect_n | 3952 | 4502 | 4529 | 4476 | 4435 | 4378.8 ± 241.09272 [5] |
| classifier.all.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.share_of_retained | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.top1_accuracy | 0.48581837 | 0.35896341 | 0.39540782 | 0.36877732 | 0.40108035 | 0.40200945 ± 0.050064249 [5] |
| classifier.all.map_at_3 | 0.59181195 | 0.5018036 | 0.53882437 | 0.50122221 | 0.56241278 | 0.53921498 ± 0.039203937 [5] |
| classifier.all.risk | 0.51418163 | 0.64103659 | 0.60459218 | 0.63122268 | 0.59891965 | 0.59799055 ± 0.050064249 [5] |
| classifier.all.mean_confidence | 0.37317163 | 0.41480766 | 0.441297 | 0.41765069 | 0.41918322 | 0.41322204 ± 0.024748237 [5] |
| classifier.all.ece | 0.11264674 | 0.055844253 | 0.045889176 | 0.048873362 | 0.018102867 | 0.056271279 ± 0.034632786 [5] |
| classifier.all.brier | 0.75585416 | 0.82352498 | 0.79378899 | 0.82213474 | 0.77998281 | 0.79505714 ± 0.028763396 [5] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.share_of_retained | 0.052953422 | 0.22967393 | 0.26498465 | 0.30489353 | 0.2144497 | 0.21339104 ± 0.096230307 [5] |
| classifier.unsupported.top1_accuracy | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.map_at_3 | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.risk | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.mean_confidence | 0.37317163 | 0.41480766 | 0.441297 | 0.41765069 | 0.41918322 | 0.41322204 ± 0.024748237 [5] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.correct_n | 3734 | 2521 | 2962 | 2615 | 2970 | 2960.4 ± 477.21201 [5] |
| classifier.frequent.incorrect_n | 3545 | 2889 | 2544 | 2314 | 2847 | 2827.8 ± 464.4951 [5] |
| classifier.frequent.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.share_of_retained | 0.94704658 | 0.77032607 | 0.73501535 | 0.69510647 | 0.7855503 | 0.78660896 ± 0.096230307 [5] |
| classifier.frequent.top1_accuracy | 0.51298255 | 0.46598891 | 0.53795859 | 0.53053358 | 0.51057246 | 0.51160722 ± 0.028002653 [5] |
| classifier.frequent.map_at_3 | 0.62490269 | 0.65141713 | 0.73307907 | 0.72107256 | 0.71594751 | 0.68928379 ± 0.048006032 [5] |
| classifier.frequent.risk | 0.48701745 | 0.53401109 | 0.46204141 | 0.46946642 | 0.48942754 | 0.48839278 ± 0.028002653 [5] |
| classifier.frequent.mean_confidence | 0.37317163 | 0.41480766 | 0.441297 | 0.41765069 | 0.41918322 | 0.41322204 ± 0.024748237 [5] |
| classifier.frequent.ece | 0.13981092 | 0.051181251 | 0.096661592 | 0.11288289 | 0.091389242 | 0.098385179 ± 0.032428383 [5] |
| classifier.frequent.brier | 0.73049733 | 0.70086877 | 0.62843511 | 0.64107891 | 0.65717317 | 0.67161066 ± 0.042803138 [5] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.correct_n | 3734 | 2521 | 2962 | 2615 | 2970 | 2960.4 ± 477.21201 [5] |
| classifier.well_supported.incorrect_n | 3291 | 2484 | 2544 | 2314 | 2752 | 2677 ± 377.26913 [5] |
| classifier.well_supported.coverage | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.review_fraction | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.share_of_retained | 0.91399948 | 0.71265841 | 0.73501535 | 0.69510647 | 0.77272113 | 0.76590017 ± 0.087721485 [5] |
| classifier.well_supported.top1_accuracy | 0.53153025 | 0.5036963 | 0.53795859 | 0.53053358 | 0.51904928 | 0.5245536 ± 0.013504183 [5] |
| classifier.well_supported.map_at_3 | 0.64749703 | 0.7041292 | 0.73307907 | 0.72107256 | 0.72783409 | 0.70672239 ± 0.034859264 [5] |
| classifier.well_supported.risk | 0.46846975 | 0.4963037 | 0.46204141 | 0.46946642 | 0.48095072 | 0.4754464 ± 0.013504183 [5] |
| classifier.well_supported.mean_confidence | 0.37317163 | 0.41480766 | 0.441297 | 0.41765069 | 0.41918322 | 0.41322204 ± 0.024748237 [5] |
| classifier.well_supported.ece | 0.15835861 | 0.088888645 | 0.096661592 | 0.11288289 | 0.099866065 | 0.11133156 ± 0.027678062 [5] |
| classifier.well_supported.brier | 0.71330754 | 0.65808402 | 0.62843511 | 0.64107891 | 0.64993832 | 0.65816878 ± 0.032726844 [5] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / frequency / 10

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / frequency / 20

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

### question_plus_explanation / frequency / 30

| Group / metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean ± SD [defined] |
|---|---|---|---|---|---|---|
| classifier.all.original_n | 7686 | 7023 | 7491 | 7091 | 7405 | 7339.2 ± 278.04172 [5] |
| classifier.all.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.all.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.all.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.all.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.all.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.all.risk | null | null | null | null | null | null ± null [0] |
| classifier.all.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.all.ece | null | null | null | null | null | null ± null [0] |
| classifier.all.brier | null | null | null | null | null | null ± null [0] |
| classifier.all.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.original_n | 407 | 1613 | 1985 | 2162 | 1588 | 1551 ± 684.76748 [5] |
| classifier.unsupported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.unsupported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.unsupported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.risk | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.ece | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.brier | null | null | null | null | null | null ± null [0] |
| classifier.unsupported.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.rare.original_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.rare.coverage | null | null | null | null | null | null ± null [0] |
| classifier.rare.review_fraction | null | null | null | null | null | null ± null [0] |
| classifier.rare.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.rare.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.rare.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.rare.risk | null | null | null | null | null | null ± null [0] |
| classifier.rare.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.rare.ece | null | null | null | null | null | null ± null [0] |
| classifier.rare.brier | null | null | null | null | null | null ± null [0] |
| classifier.rare.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.frequent.original_n | 7279 | 5410 | 5506 | 4929 | 5817 | 5788.2 ± 892.21785 [5] |
| classifier.frequent.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.frequent.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.frequent.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.frequent.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.frequent.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.frequent.risk | null | null | null | null | null | null ± null [0] |
| classifier.frequent.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.frequent.ece | null | null | null | null | null | null ± null [0] |
| classifier.frequent.brier | null | null | null | null | null | null ± null [0] |
| classifier.frequent.error_minus_target | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.original_n | 7025 | 5005 | 5506 | 4929 | 5722 | 5637.4 ± 844.3366 [5] |
| classifier.well_supported.retained_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.correct_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.incorrect_n | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.coverage | 0 | 0 | 0 | 0 | 0 | 0 ± 0 [5] |
| classifier.well_supported.review_fraction | 1 | 1 | 1 | 1 | 1 | 1 ± 0 [5] |
| classifier.well_supported.share_of_retained | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.top1_accuracy | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.map_at_3 | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.risk | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.mean_confidence | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.ece | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.brier | null | null | null | null | null | null ± null [0] |
| classifier.well_supported.error_minus_target | null | null | null | null | null | null ± null [0] |

## Execution

Runtime: 1547.299 seconds. Pre-run revision: `c2dd478d3a857287ba8fcc6563fc2b64ad1cb496`. Historical development policies reproduced: 90/90; evaluation records reproduced: 120/120. Preserved files: 114. Classifier fits: 400 attempted, 400 successful, 0 failed; warnings: 0, including 0 convergence warnings. Reliability fits: 10; constant fallbacks: 0.

No raw responses, row-level features/predictions/scores, neighbor identifiers, candidate arrays, fitted coefficients or scaler statistics are serialized. No experiment interpretation is added to this numerical report.
