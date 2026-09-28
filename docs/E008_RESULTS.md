# E008 — development feasibility diagnostics

Status: **COMPLETED**. Results only; interpretation and the next experiment await user review.

Prespecified exploratory diagnostic, not independent confirmatory evidence. No outer-evaluation predictions were made. Diagnostic witnesses are optimized on development correctness, not deployable policies or unbiased estimates. Frequency is the same reference across input arms and is not independent replicated evidence.

[Complete scalar/count JSON](../results/E008_aggregates.json). All five fold values, equal-fold mean, sample SD and defined-fold count are included below. No confidence intervals or hypothesis tests. Anonymous role slots may repeat questions across folds.

## Outcome counts (out of five folds)

| Target | Arm | Rule | FIXED_PREDICTION_LIMIT | SCORE_SELECTION_LIMIT | COMMON_CUTOFF_INCOMPATIBILITY |
|---|---|---|---|---|---|
| 20% | explanation_only | confidence_only | 0 | 5 | 0 |
| 20% | explanation_only | support_aware | 0 | 5 | 0 |
| 20% | explanation_only | frequency | 0 | 5 | 0 |
| 20% | question_plus_explanation | confidence_only | 0 | 5 | 0 |
| 20% | question_plus_explanation | support_aware | 0 | 5 | 0 |
| 20% | question_plus_explanation | frequency | 0 | 5 | 0 |
| 10% | explanation_only | confidence_only | 0 | 5 | 0 |
| 10% | explanation_only | support_aware | 0 | 5 | 0 |
| 10% | explanation_only | frequency | 0 | 5 | 0 |
| 10% | question_plus_explanation | confidence_only | 0 | 5 | 0 |
| 10% | question_plus_explanation | support_aware | 0 | 5 | 0 |
| 10% | question_plus_explanation | frequency | 0 | 5 | 0 |
| 30% | explanation_only | confidence_only | 0 | 5 | 0 |
| 30% | explanation_only | support_aware | 0 | 5 | 0 |
| 30% | explanation_only | frequency | 0 | 5 | 0 |
| 30% | question_plus_explanation | confidence_only | 0 | 4 | 1 |
| 30% | question_plus_explanation | support_aware | 0 | 4 | 1 |
| 30% | question_plus_explanation | frequency | 0 | 5 | 0 |

## All fold-level constraint and feasibility records

Histogram order is C/V/R bits: 000, 001, 010, 011, 100, 101, 110, 111. C=count, V=coverage, R=risk; joint bits require each condition on both questions. Single-condition failures are cells 011/101/110. Counts are grid properties, not comparable performance scores.

| Arm | Fold | Rule | Target | Candidates | Joint histogram | A0 size | A1 size | Intersection | Outcome | Minimax risk | Risk minus target | Witness cutoff |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| explanation_only | 0 | confidence_only | 10% | 4024 | 236, 0, 0, 0, 190, 0, 3598, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.60339943 | 0.50339943 | 0.74528599 |
| explanation_only | 0 | confidence_only | 20% | 4024 | 236, 0, 0, 0, 190, 0, 3598, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.60339943 | 0.40339943 | 0.74528599 |
| explanation_only | 0 | confidence_only | 30% | 4024 | 236, 0, 0, 0, 190, 0, 3598, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.60339943 | 0.30339943 | 0.74528599 |
| explanation_only | 0 | support_aware | 10% | 4024 | 259, 0, 0, 0, 148, 0, 3617, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.57006369 | 0.47006369 | 0.72561415 |
| explanation_only | 0 | support_aware | 20% | 4024 | 259, 0, 0, 0, 148, 0, 3617, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.57006369 | 0.37006369 | 0.72561415 |
| explanation_only | 0 | support_aware | 30% | 4024 | 259, 0, 0, 0, 148, 0, 3617, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.57006369 | 0.27006369 | 0.72561415 |
| explanation_only | 0 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.59139966 | 0 |
| explanation_only | 0 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.49139966 | 0 |
| explanation_only | 0 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.39139966 | 0 |
| explanation_only | 1 | confidence_only | 10% | 4014 | 350, 0, 0, 0, 77, 0, 3587, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.68124118 | 0.58124118 | 0.59941219 |
| explanation_only | 1 | confidence_only | 20% | 4014 | 350, 0, 0, 0, 77, 0, 3587, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.68124118 | 0.48124118 | 0.59941219 |
| explanation_only | 1 | confidence_only | 30% | 4014 | 350, 0, 0, 0, 77, 0, 3587, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.68124118 | 0.38124118 | 0.59941219 |
| explanation_only | 1 | support_aware | 10% | 4014 | 478, 0, 0, 0, 48, 0, 3488, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.66262976 | 0.56262976 | 0.60407405 |
| explanation_only | 1 | support_aware | 20% | 4014 | 478, 0, 0, 0, 48, 0, 3488, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.66262976 | 0.46262976 | 0.60407405 |
| explanation_only | 1 | support_aware | 30% | 4014 | 478, 0, 0, 0, 48, 0, 3488, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.66262976 | 0.36262976 | 0.60407405 |
| explanation_only | 1 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.59139966 | 0 |
| explanation_only | 1 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.49139966 | 0 |
| explanation_only | 1 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.39139966 | 0 |
| explanation_only | 2 | confidence_only | 10% | 4411 | 479, 6, 0, 0, 101, 0, 3825, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.35452794 | 0.25452794 | 0.50444153 |
| explanation_only | 2 | confidence_only | 20% | 4411 | 421, 64, 0, 0, 101, 0, 3825, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.35452794 | 0.15452794 | 0.50444153 |
| explanation_only | 2 | confidence_only | 30% | 4411 | 289, 196, 0, 0, 101, 0, 3825, 0 | 850 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.35452794 | 0.054527938 | 0.50444153 |
| explanation_only | 2 | support_aware | 10% | 4411 | 401, 69, 0, 0, 113, 0, 3828, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.33531746 | 0.23531746 | 0.49292577 |
| explanation_only | 2 | support_aware | 20% | 4411 | 325, 145, 0, 0, 113, 0, 3828, 0 | 136 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.33531746 | 0.13531746 | 0.49292577 |
| explanation_only | 2 | support_aware | 30% | 4411 | 89, 381, 0, 0, 113, 0, 3828, 0 | 1072 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.33531746 | 0.03531746 | 0.49292577 |
| explanation_only | 2 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.59139966 | 0 |
| explanation_only | 2 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.49139966 | 0 |
| explanation_only | 2 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.39139966 | 0 |
| explanation_only | 3 | confidence_only | 10% | 5237 | 251, 0, 0, 0, 388, 0, 4598, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.65737052 | 0.55737052 | 0.70564 |
| explanation_only | 3 | confidence_only | 20% | 5237 | 251, 0, 0, 0, 388, 0, 4598, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.65737052 | 0.45737052 | 0.70564 |
| explanation_only | 3 | confidence_only | 30% | 5237 | 251, 0, 0, 0, 388, 0, 4598, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.65737052 | 0.35737052 | 0.70564 |
| explanation_only | 3 | support_aware | 10% | 5237 | 352, 0, 0, 0, 240, 0, 4645, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.62 | 0.52 | 0.64106635 |
| explanation_only | 3 | support_aware | 20% | 5237 | 325, 27, 0, 0, 240, 0, 4645, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.62 | 0.42 | 0.64106635 |
| explanation_only | 3 | support_aware | 30% | 5237 | 307, 45, 0, 0, 240, 0, 4645, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.62 | 0.32 | 0.64106635 |
| explanation_only | 3 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.64607783 | 0.54607783 | 0 |
| explanation_only | 3 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.64607783 | 0.44607783 | 0 |
| explanation_only | 3 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.64607783 | 0.34607783 | 0 |
| explanation_only | 4 | confidence_only | 10% | 5602 | 732, 0, 0, 0, 474, 0, 4396, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.83006797 | 0.73006797 | 0.33674146 |
| explanation_only | 4 | confidence_only | 20% | 5602 | 732, 0, 0, 0, 474, 0, 4396, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.83006797 | 0.63006797 | 0.33674146 |
| explanation_only | 4 | confidence_only | 30% | 5602 | 732, 0, 0, 0, 474, 0, 4396, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.83006797 | 0.53006797 | 0.33674146 |
| explanation_only | 4 | support_aware | 10% | 5602 | 1276, 0, 0, 0, 383, 0, 3943, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.71104816 | 0.61104816 | 0.56131972 |
| explanation_only | 4 | support_aware | 20% | 5602 | 1276, 0, 0, 0, 383, 0, 3943, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.71104816 | 0.51104816 | 0.56131972 |
| explanation_only | 4 | support_aware | 30% | 5602 | 1276, 0, 0, 0, 383, 0, 3943, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.71104816 | 0.41104816 | 0.56131972 |
| explanation_only | 4 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.63785714 | 0.53785714 | 0 |
| explanation_only | 4 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.63785714 | 0.43785714 | 0 |
| explanation_only | 4 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.63785714 | 0.33785714 | 0 |
| question_plus_explanation | 0 | confidence_only | 10% | 4017 | 216, 0, 0, 0, 330, 0, 3471, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.67615658 | 0.57615658 | 0.80273934 |
| question_plus_explanation | 0 | confidence_only | 20% | 4017 | 216, 0, 0, 0, 330, 0, 3471, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.67615658 | 0.47615658 | 0.80273934 |
| question_plus_explanation | 0 | confidence_only | 30% | 4017 | 216, 0, 0, 0, 330, 0, 3471, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.67615658 | 0.37615658 | 0.80273934 |
| question_plus_explanation | 0 | support_aware | 10% | 4017 | 362, 0, 0, 0, 42, 0, 3613, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.58823529 | 0.48823529 | 0.79356981 |
| question_plus_explanation | 0 | support_aware | 20% | 4017 | 362, 0, 0, 0, 42, 0, 3613, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.58823529 | 0.38823529 | 0.79356981 |
| question_plus_explanation | 0 | support_aware | 30% | 4017 | 362, 0, 0, 0, 42, 0, 3613, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.58823529 | 0.28823529 | 0.79356981 |
| question_plus_explanation | 0 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.59139966 | 0 |
| question_plus_explanation | 0 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.49139966 | 0 |
| question_plus_explanation | 0 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.39139966 | 0 |
| question_plus_explanation | 1 | confidence_only | 10% | 4017 | 944, 0, 0, 0, 49, 0, 3024, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.72970195 | 0.62970195 | 0.31608431 |
| question_plus_explanation | 1 | confidence_only | 20% | 4017 | 944, 0, 0, 0, 49, 0, 3024, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.72970195 | 0.52970195 | 0.31608431 |
| question_plus_explanation | 1 | confidence_only | 30% | 4017 | 944, 0, 0, 0, 49, 0, 3024, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.72970195 | 0.42970195 | 0.31608431 |
| question_plus_explanation | 1 | support_aware | 10% | 4017 | 1123, 0, 0, 0, 55, 0, 2839, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.7257085 | 0.6257085 | 0.28922476 |
| question_plus_explanation | 1 | support_aware | 20% | 4017 | 1123, 0, 0, 0, 55, 0, 2839, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.7257085 | 0.5257085 | 0.28922476 |
| question_plus_explanation | 1 | support_aware | 30% | 4017 | 1123, 0, 0, 0, 55, 0, 2839, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.7257085 | 0.4257085 | 0.28922476 |
| question_plus_explanation | 1 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.59139966 | 0 |
| question_plus_explanation | 1 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.49139966 | 0 |
| question_plus_explanation | 1 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.39139966 | 0 |
| question_plus_explanation | 2 | confidence_only | 10% | 4404 | 1010, 10, 0, 0, 92, 0, 3292, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.43339254 | 0.33339254 | 0.51018362 |
| question_plus_explanation | 2 | confidence_only | 20% | 4404 | 937, 83, 0, 0, 92, 0, 3292, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.43339254 | 0.23339254 | 0.51018362 |
| question_plus_explanation | 2 | confidence_only | 30% | 4404 | 698, 322, 0, 0, 92, 0, 3292, 0 | 523 | 21 | 0 | COMMON_CUTOFF_INCOMPATIBILITY | 0.43339254 | 0.13339254 | 0.51018362 |
| question_plus_explanation | 2 | support_aware | 10% | 4404 | 1033, 15, 0, 0, 107, 0, 3249, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.43455497 | 0.33455497 | 0.49106915 |
| question_plus_explanation | 2 | support_aware | 20% | 4404 | 950, 98, 0, 0, 107, 0, 3249, 0 | 258 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.43455497 | 0.23455497 | 0.49106915 |
| question_plus_explanation | 2 | support_aware | 30% | 4404 | 719, 329, 0, 0, 107, 0, 3249, 0 | 762 | 23 | 0 | COMMON_CUTOFF_INCOMPATIBILITY | 0.43455497 | 0.13455497 | 0.49106915 |
| question_plus_explanation | 2 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.59139966 | 0 |
| question_plus_explanation | 2 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.49139966 | 0 |
| question_plus_explanation | 2 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.69139966 | 0.39139966 | 0 |
| question_plus_explanation | 3 | confidence_only | 10% | 5244 | 2985, 0, 0, 0, 70, 0, 2189, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.58716418 | 0.48716418 | 0.70757791 |
| question_plus_explanation | 3 | confidence_only | 20% | 5244 | 2985, 0, 0, 0, 70, 0, 2189, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.58716418 | 0.38716418 | 0.70757791 |
| question_plus_explanation | 3 | confidence_only | 30% | 5244 | 2985, 0, 0, 0, 70, 0, 2189, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.58716418 | 0.28716418 | 0.70757791 |
| question_plus_explanation | 3 | support_aware | 10% | 5244 | 3432, 0, 0, 0, 56, 0, 1756, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.61225541 | 0.51225541 | 0.66701611 |
| question_plus_explanation | 3 | support_aware | 20% | 5244 | 3432, 0, 0, 0, 56, 0, 1756, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.61225541 | 0.41225541 | 0.66701611 |
| question_plus_explanation | 3 | support_aware | 30% | 5244 | 3432, 0, 0, 0, 56, 0, 1756, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.61225541 | 0.31225541 | 0.66701611 |
| question_plus_explanation | 3 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.64607783 | 0.54607783 | 0 |
| question_plus_explanation | 3 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.64607783 | 0.44607783 | 0 |
| question_plus_explanation | 3 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.64607783 | 0.34607783 | 0 |
| question_plus_explanation | 4 | confidence_only | 10% | 5617 | 994, 0, 0, 0, 511, 0, 4112, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.79642857 | 0.69642857 | 0.71641053 |
| question_plus_explanation | 4 | confidence_only | 20% | 5617 | 994, 0, 0, 0, 511, 0, 4112, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.79642857 | 0.59642857 | 0.71641053 |
| question_plus_explanation | 4 | confidence_only | 30% | 5617 | 994, 0, 0, 0, 511, 0, 4112, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.79642857 | 0.49642857 | 0.71641053 |
| question_plus_explanation | 4 | support_aware | 10% | 5617 | 1236, 0, 0, 0, 492, 0, 3889, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.71266968 | 0.61266968 | 0.56315943 |
| question_plus_explanation | 4 | support_aware | 20% | 5617 | 1236, 0, 0, 0, 492, 0, 3889, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.71266968 | 0.51266968 | 0.56315943 |
| question_plus_explanation | 4 | support_aware | 30% | 5617 | 1236, 0, 0, 0, 492, 0, 3889, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.71266968 | 0.41266968 | 0.56315943 |
| question_plus_explanation | 4 | frequency | 10% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.63785714 | 0.53785714 | 0 |
| question_plus_explanation | 4 | frequency | 20% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.63785714 | 0.43785714 | 0 |
| question_plus_explanation | 4 | frequency | 30% | 2 | 0, 0, 0, 0, 0, 0, 2, 0 | 0 | 0 | 0 | SCORE_SELECTION_LIMIT | 0.63785714 | 0.33785714 | 0 |

## All development-question score diagnostics

F=fixed-prediction-limit flag; S=oracle-feasible but score-infeasible flag. Minima use the fixed count/coverage floors; null means NO_FEASIBLE_FLOOR. Cutoffs are scalar diagnostic witnesses only. Signed error differences are absolute risk minus target.

| Arm | Fold | Rule | Target | Role | Histogram | Feasible | F | S | Min cutoff | Retained | Errors | Coverage | Min risk | Risk minus target | Oracle gap | Shared retained | Shared errors | Shared coverage | Shared risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| explanation_only | 0 | confidence_only | 10% | 0 | 219, 17, 0, 0, 48, 0, 3740, 0 | False | False | True | 0.79779847 | 121 | 44 | 0.10202361 | 0.36363636 | 0.26363636 | 0.36363636 | 179 | 77 | 0.15092749 | 0.4301676 |
| explanation_only | 0 | confidence_only | 10% | 1 | 161, 0, 0, 0, 265, 0, 3598, 0 | False | False | True | 0.74528599 | 353 | 213 | 0.11332263 | 0.60339943 | 0.50339943 | 0.60339943 | 353 | 213 | 0.11332263 | 0.60339943 |
| explanation_only | 0 | confidence_only | 20% | 0 | 163, 73, 0, 0, 48, 0, 3740, 0 | False | False | True | 0.79779847 | 121 | 44 | 0.10202361 | 0.36363636 | 0.16363636 | 0.36363636 | 179 | 77 | 0.15092749 | 0.4301676 |
| explanation_only | 0 | confidence_only | 20% | 1 | 161, 0, 0, 0, 265, 0, 3598, 0 | False | False | True | 0.74528599 | 353 | 213 | 0.11332263 | 0.60339943 | 0.40339943 | 0.60339943 | 353 | 213 | 0.11332263 | 0.60339943 |
| explanation_only | 0 | confidence_only | 30% | 0 | 64, 172, 0, 0, 48, 0, 3740, 0 | False | False | True | 0.79779847 | 121 | 44 | 0.10202361 | 0.36363636 | 0.063636364 | 0.36363636 | 179 | 77 | 0.15092749 | 0.4301676 |
| explanation_only | 0 | confidence_only | 30% | 1 | 161, 0, 0, 0, 265, 0, 3598, 0 | False | False | True | 0.74528599 | 353 | 213 | 0.11332263 | 0.60339943 | 0.30339943 | 0.60339943 | 353 | 213 | 0.11332263 | 0.60339943 |
| explanation_only | 0 | support_aware | 10% | 0 | 202, 57, 0, 0, 66, 0, 3699, 0 | False | False | True | 0.74565926 | 124 | 40 | 0.10455312 | 0.32258065 | 0.22258065 | 0.32258065 | 142 | 49 | 0.11973019 | 0.34507042 |
| explanation_only | 0 | support_aware | 10% | 1 | 155, 0, 0, 0, 252, 0, 3617, 0 | False | False | True | 0.72561415 | 314 | 179 | 0.10080257 | 0.57006369 | 0.47006369 | 0.57006369 | 314 | 179 | 0.10080257 | 0.57006369 |
| explanation_only | 0 | support_aware | 20% | 0 | 169, 90, 0, 0, 66, 0, 3699, 0 | False | False | True | 0.74565926 | 124 | 40 | 0.10455312 | 0.32258065 | 0.12258065 | 0.32258065 | 142 | 49 | 0.11973019 | 0.34507042 |
| explanation_only | 0 | support_aware | 20% | 1 | 155, 0, 0, 0, 252, 0, 3617, 0 | False | False | True | 0.72561415 | 314 | 179 | 0.10080257 | 0.57006369 | 0.37006369 | 0.57006369 | 314 | 179 | 0.10080257 | 0.57006369 |
| explanation_only | 0 | support_aware | 30% | 0 | 7, 252, 0, 0, 66, 0, 3699, 0 | False | False | True | 0.74565926 | 124 | 40 | 0.10455312 | 0.32258065 | 0.022580645 | 0.32258065 | 142 | 49 | 0.11973019 | 0.34507042 |
| explanation_only | 0 | support_aware | 30% | 1 | 155, 0, 0, 0, 252, 0, 3617, 0 | False | False | True | 0.72561415 | 314 | 179 | 0.10080257 | 0.57006369 | 0.27006369 | 0.57006369 | 314 | 179 | 0.10080257 | 0.57006369 |
| explanation_only | 0 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.59139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 0 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.44895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| explanation_only | 0 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.49139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 0 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.34895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| explanation_only | 0 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.39139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 0 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.24895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| explanation_only | 1 | confidence_only | 10% | 0 | 335, 15, 0, 0, 77, 0, 3587, 0 | False | False | True | 0.69796232 | 120 | 76 | 0.10118044 | 0.63333333 | 0.53333333 | 0.63333333 | 298 | 203 | 0.25126476 | 0.68120805 |
| explanation_only | 1 | confidence_only | 10% | 1 | 125, 0, 0, 0, 268, 0, 3621, 0 | False | False | True | 0.60407405 | 686 | 466 | 0.22093398 | 0.67930029 | 0.57930029 | 0.67930029 | 709 | 483 | 0.22834138 | 0.68124118 |
| explanation_only | 1 | confidence_only | 20% | 0 | 335, 15, 0, 0, 77, 0, 3587, 0 | False | False | True | 0.69796232 | 120 | 76 | 0.10118044 | 0.63333333 | 0.43333333 | 0.63333333 | 298 | 203 | 0.25126476 | 0.68120805 |
| explanation_only | 1 | confidence_only | 20% | 1 | 125, 0, 0, 0, 268, 0, 3621, 0 | False | False | True | 0.60407405 | 686 | 466 | 0.22093398 | 0.67930029 | 0.47930029 | 0.67930029 | 709 | 483 | 0.22834138 | 0.68124118 |
| explanation_only | 1 | confidence_only | 30% | 0 | 335, 15, 0, 0, 77, 0, 3587, 0 | False | False | True | 0.69796232 | 120 | 76 | 0.10118044 | 0.63333333 | 0.33333333 | 0.63333333 | 298 | 203 | 0.25126476 | 0.68120805 |
| explanation_only | 1 | confidence_only | 30% | 1 | 125, 0, 0, 0, 268, 0, 3621, 0 | False | False | True | 0.60407405 | 686 | 466 | 0.22093398 | 0.67930029 | 0.37930029 | 0.67930029 | 709 | 483 | 0.22834138 | 0.68124118 |
| explanation_only | 1 | support_aware | 10% | 0 | 459, 19, 0, 0, 48, 0, 3488, 0 | False | False | True | 0.64232547 | 120 | 73 | 0.10118044 | 0.60833333 | 0.50833333 | 0.60833333 | 187 | 120 | 0.15767285 | 0.64171123 |
| explanation_only | 1 | support_aware | 10% | 1 | 105, 0, 0, 0, 245, 0, 3664, 0 | False | False | True | 0.60407405 | 578 | 383 | 0.18615137 | 0.66262976 | 0.56262976 | 0.66262976 | 578 | 383 | 0.18615137 | 0.66262976 |
| explanation_only | 1 | support_aware | 20% | 0 | 459, 19, 0, 0, 48, 0, 3488, 0 | False | False | True | 0.64232547 | 120 | 73 | 0.10118044 | 0.60833333 | 0.40833333 | 0.60833333 | 187 | 120 | 0.15767285 | 0.64171123 |
| explanation_only | 1 | support_aware | 20% | 1 | 105, 0, 0, 0, 245, 0, 3664, 0 | False | False | True | 0.60407405 | 578 | 383 | 0.18615137 | 0.66262976 | 0.46262976 | 0.66262976 | 578 | 383 | 0.18615137 | 0.66262976 |
| explanation_only | 1 | support_aware | 30% | 0 | 459, 19, 0, 0, 48, 0, 3488, 0 | False | False | True | 0.64232547 | 120 | 73 | 0.10118044 | 0.60833333 | 0.30833333 | 0.60833333 | 187 | 120 | 0.15767285 | 0.64171123 |
| explanation_only | 1 | support_aware | 30% | 1 | 105, 0, 0, 0, 245, 0, 3664, 0 | False | False | True | 0.60407405 | 578 | 383 | 0.18615137 | 0.66262976 | 0.36262976 | 0.66262976 | 578 | 383 | 0.18615137 | 0.66262976 |
| explanation_only | 1 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.59139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 1 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3105 | 1870 | 1 | 0.60225443 | 0.50225443 | 0.60225443 | 3105 | 1870 | 1 | 0.60225443 |
| explanation_only | 1 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.49139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 1 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3105 | 1870 | 1 | 0.60225443 | 0.40225443 | 0.60225443 | 3105 | 1870 | 1 | 0.60225443 |
| explanation_only | 1 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.39139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 1 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3105 | 1870 | 1 | 0.60225443 | 0.30225443 | 0.60225443 | 3105 | 1870 | 1 | 0.60225443 |
| explanation_only | 2 | confidence_only | 10% | 0 | 360, 125, 0, 0, 101, 0, 3825, 0 | False | False | True | 0.50546572 | 119 | 24 | 0.10033727 | 0.20168067 | 0.10168067 | 0.20168067 | 123 | 25 | 0.10370995 | 0.20325203 |
| explanation_only | 2 | confidence_only | 10% | 1 | 103, 7, 0, 0, 309, 0, 3992, 0 | False | False | True | 0.54230437 | 366 | 120 | 0.10054945 | 0.32786885 | 0.22786885 | 0.32786885 | 519 | 184 | 0.14258242 | 0.35452794 |
| explanation_only | 2 | confidence_only | 20% | 0 | 35, 450, 0, 0, 64, 37, 3825, 0 | False | False | True | 0.50546572 | 119 | 24 | 0.10033727 | 0.20168067 | 0.0016806723 | 0.20168067 | 123 | 25 | 0.10370995 | 0.20325203 |
| explanation_only | 2 | confidence_only | 20% | 1 | 45, 65, 0, 0, 309, 0, 3992, 0 | False | False | True | 0.54230437 | 366 | 120 | 0.10054945 | 0.32786885 | 0.12786885 | 0.32786885 | 519 | 184 | 0.14258242 | 0.35452794 |
| explanation_only | 2 | confidence_only | 30% | 0 | 2, 483, 0, 0, 0, 101, 2975, 850 | True | False | False | 0.50546572 | 119 | 24 | 0.10033727 | 0.20168067 | -0.098319328 | 0.20168067 | 123 | 25 | 0.10370995 | 0.20325203 |
| explanation_only | 2 | confidence_only | 30% | 1 | 4, 106, 0, 0, 218, 91, 3992, 0 | False | False | True | 0.54230437 | 366 | 120 | 0.10054945 | 0.32786885 | 0.027868852 | 0.32786885 | 519 | 184 | 0.14258242 | 0.35452794 |
| explanation_only | 2 | support_aware | 10% | 0 | 177, 293, 0, 0, 113, 0, 3828, 0 | False | False | True | 0.49287166 | 120 | 18 | 0.10118044 | 0.15 | 0.05 | 0.15 | 119 | 18 | 0.10033727 | 0.1512605 |
| explanation_only | 2 | support_aware | 10% | 1 | 43, 70, 0, 0, 319, 0, 3979, 0 | False | False | True | 0.52543932 | 365 | 113 | 0.10027473 | 0.30958904 | 0.20958904 | 0.30958904 | 504 | 169 | 0.13846154 | 0.33531746 |
| explanation_only | 2 | support_aware | 20% | 0 | 1, 469, 0, 0, 0, 113, 3692, 136 | True | False | False | 0.49287166 | 120 | 18 | 0.10118044 | 0.15 | -0.05 | 0.15 | 119 | 18 | 0.10033727 | 0.1512605 |
| explanation_only | 2 | support_aware | 20% | 1 | 0, 113, 0, 0, 286, 33, 3979, 0 | False | False | True | 0.52543932 | 365 | 113 | 0.10027473 | 0.30958904 | 0.10958904 | 0.30958904 | 504 | 169 | 0.13846154 | 0.33531746 |
| explanation_only | 2 | support_aware | 30% | 0 | 1, 469, 0, 0, 0, 113, 2756, 1072 | True | False | False | 0.49287166 | 120 | 18 | 0.10118044 | 0.15 | -0.15 | 0.15 | 119 | 18 | 0.10033727 | 0.1512605 |
| explanation_only | 2 | support_aware | 30% | 1 | 0, 113, 0, 0, 50, 269, 3979, 0 | False | False | True | 0.52543932 | 365 | 113 | 0.10027473 | 0.30958904 | 0.0095890411 | 0.30958904 | 504 | 169 | 0.13846154 | 0.33531746 |
| explanation_only | 2 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.59139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 2 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3640 | 2500 | 1 | 0.68681319 | 0.58681319 | 0.68681319 | 3640 | 2500 | 1 | 0.68681319 |
| explanation_only | 2 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.49139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 2 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3640 | 2500 | 1 | 0.68681319 | 0.48681319 | 0.68681319 | 3640 | 2500 | 1 | 0.68681319 |
| explanation_only | 2 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.39139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| explanation_only | 2 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3640 | 2500 | 1 | 0.68681319 | 0.38681319 | 0.68681319 | 3640 | 2500 | 1 | 0.68681319 |
| explanation_only | 3 | confidence_only | 10% | 0 | 129, 34, 0, 0, 476, 0, 4598, 0 | False | False | True | 0.72209528 | 502 | 282 | 0.10335598 | 0.56175299 | 0.46175299 | 0.56175299 | 590 | 340 | 0.12147416 | 0.57627119 |
| explanation_only | 3 | confidence_only | 10% | 1 | 251, 0, 0, 0, 19, 0, 4967, 0 | False | False | True | 0.78649209 | 127 | 80 | 0.1208373 | 0.62992126 | 0.52992126 | 0.62992126 | 251 | 165 | 0.23882017 | 0.65737052 |
| explanation_only | 3 | confidence_only | 20% | 0 | 109, 54, 0, 0, 476, 0, 4598, 0 | False | False | True | 0.72209528 | 502 | 282 | 0.10335598 | 0.56175299 | 0.36175299 | 0.56175299 | 590 | 340 | 0.12147416 | 0.57627119 |
| explanation_only | 3 | confidence_only | 20% | 1 | 251, 0, 0, 0, 19, 0, 4967, 0 | False | False | True | 0.78649209 | 127 | 80 | 0.1208373 | 0.62992126 | 0.42992126 | 0.62992126 | 251 | 165 | 0.23882017 | 0.65737052 |
| explanation_only | 3 | confidence_only | 30% | 0 | 74, 89, 0, 0, 476, 0, 4598, 0 | False | False | True | 0.72209528 | 502 | 282 | 0.10335598 | 0.56175299 | 0.26175299 | 0.56175299 | 590 | 340 | 0.12147416 | 0.57627119 |
| explanation_only | 3 | confidence_only | 30% | 1 | 251, 0, 0, 0, 19, 0, 4967, 0 | False | False | True | 0.78649209 | 127 | 80 | 0.1208373 | 0.62992126 | 0.32992126 | 0.62992126 | 251 | 165 | 0.23882017 | 0.65737052 |
| explanation_only | 3 | support_aware | 10% | 0 | 105, 9, 0, 0, 478, 0, 4645, 0 | False | False | True | 0.67427963 | 521 | 261 | 0.10726786 | 0.50095969 | 0.40095969 | 0.50095969 | 711 | 385 | 0.14638666 | 0.54149086 |
| explanation_only | 3 | support_aware | 10% | 1 | 318, 34, 0, 0, 11, 0, 4874, 0 | False | False | True | 0.64106635 | 250 | 155 | 0.2378687 | 0.62 | 0.52 | 0.62 | 250 | 155 | 0.2378687 | 0.62 |
| explanation_only | 3 | support_aware | 20% | 0 | 72, 42, 0, 0, 478, 0, 4645, 0 | False | False | True | 0.67427963 | 521 | 261 | 0.10726786 | 0.50095969 | 0.30095969 | 0.50095969 | 711 | 385 | 0.14638666 | 0.54149086 |
| explanation_only | 3 | support_aware | 20% | 1 | 317, 35, 0, 0, 11, 0, 4874, 0 | False | False | True | 0.64106635 | 250 | 155 | 0.2378687 | 0.62 | 0.42 | 0.62 | 250 | 155 | 0.2378687 | 0.62 |
| explanation_only | 3 | support_aware | 30% | 0 | 29, 85, 0, 0, 478, 0, 4645, 0 | False | False | True | 0.67427963 | 521 | 261 | 0.10726786 | 0.50095969 | 0.20095969 | 0.50095969 | 711 | 385 | 0.14638666 | 0.54149086 |
| explanation_only | 3 | support_aware | 30% | 1 | 307, 45, 0, 0, 11, 0, 4874, 0 | False | False | True | 0.64106635 | 250 | 155 | 0.2378687 | 0.62 | 0.32 | 0.62 | 250 | 155 | 0.2378687 | 0.62 |
| explanation_only | 3 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 4857 | 3138 | 1 | 0.64607783 | 0.54607783 | 0.64607783 | 4857 | 3138 | 1 | 0.64607783 |
| explanation_only | 3 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1051 | 624 | 1 | 0.59372027 | 0.49372027 | 0.59372027 | 1051 | 624 | 1 | 0.59372027 |
| explanation_only | 3 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 4857 | 3138 | 1 | 0.64607783 | 0.44607783 | 0.64607783 | 4857 | 3138 | 1 | 0.64607783 |
| explanation_only | 3 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1051 | 624 | 1 | 0.59372027 | 0.39372027 | 0.59372027 | 1051 | 624 | 1 | 0.59372027 |
| explanation_only | 3 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 4857 | 3138 | 1 | 0.64607783 | 0.34607783 | 0.64607783 | 4857 | 3138 | 1 | 0.64607783 |
| explanation_only | 3 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1051 | 624 | 1 | 0.59372027 | 0.29372027 | 0.59372027 | 1051 | 624 | 1 | 0.59372027 |
| explanation_only | 4 | confidence_only | 10% | 0 | 732, 0, 0, 0, 474, 0, 4396, 0 | False | False | True | 0.33674146 | 2501 | 2076 | 0.89321429 | 0.83006797 | 0.73006797 | 0.83006797 | 2501 | 2076 | 0.89321429 | 0.83006797 |
| explanation_only | 4 | confidence_only | 10% | 1 | 90, 5, 0, 0, 215, 0, 5292, 0 | False | False | True | 0.91455405 | 321 | 100 | 0.10304976 | 0.31152648 | 0.21152648 | 0.31152648 | 2892 | 1581 | 0.92841091 | 0.5466805 |
| explanation_only | 4 | confidence_only | 20% | 0 | 732, 0, 0, 0, 474, 0, 4396, 0 | False | False | True | 0.33674146 | 2501 | 2076 | 0.89321429 | 0.83006797 | 0.63006797 | 0.83006797 | 2501 | 2076 | 0.89321429 | 0.83006797 |
| explanation_only | 4 | confidence_only | 20% | 1 | 8, 87, 0, 0, 215, 0, 5292, 0 | False | False | True | 0.91455405 | 321 | 100 | 0.10304976 | 0.31152648 | 0.11152648 | 0.31152648 | 2892 | 1581 | 0.92841091 | 0.5466805 |
| explanation_only | 4 | confidence_only | 30% | 0 | 732, 0, 0, 0, 474, 0, 4396, 0 | False | False | True | 0.33674146 | 2501 | 2076 | 0.89321429 | 0.83006797 | 0.53006797 | 0.83006797 | 2501 | 2076 | 0.89321429 | 0.83006797 |
| explanation_only | 4 | confidence_only | 30% | 1 | 0, 95, 0, 0, 73, 142, 5292, 0 | False | False | True | 0.91455405 | 321 | 100 | 0.10304976 | 0.31152648 | 0.01152648 | 0.31152648 | 2892 | 1581 | 0.92841091 | 0.5466805 |
| explanation_only | 4 | support_aware | 10% | 0 | 1276, 0, 0, 0, 383, 0, 3943, 0 | False | False | True | 0.56131972 | 353 | 251 | 0.12607143 | 0.71104816 | 0.61104816 | 0.71104816 | 353 | 251 | 0.12607143 | 0.71104816 |
| explanation_only | 4 | support_aware | 10% | 1 | 89, 5, 0, 0, 203, 0, 5305, 0 | False | False | True | 0.91455405 | 318 | 97 | 0.10208668 | 0.30503145 | 0.20503145 | 0.30503145 | 1555 | 691 | 0.49919743 | 0.44437299 |
| explanation_only | 4 | support_aware | 20% | 0 | 1276, 0, 0, 0, 383, 0, 3943, 0 | False | False | True | 0.56131972 | 353 | 251 | 0.12607143 | 0.71104816 | 0.51104816 | 0.71104816 | 353 | 251 | 0.12607143 | 0.71104816 |
| explanation_only | 4 | support_aware | 20% | 1 | 8, 86, 0, 0, 203, 0, 5305, 0 | False | False | True | 0.91455405 | 318 | 97 | 0.10208668 | 0.30503145 | 0.10503145 | 0.30503145 | 1555 | 691 | 0.49919743 | 0.44437299 |
| explanation_only | 4 | support_aware | 30% | 0 | 1276, 0, 0, 0, 383, 0, 3943, 0 | False | False | True | 0.56131972 | 353 | 251 | 0.12607143 | 0.71104816 | 0.41104816 | 0.71104816 | 353 | 251 | 0.12607143 | 0.71104816 |
| explanation_only | 4 | support_aware | 30% | 1 | 0, 94, 0, 0, 46, 157, 5305, 0 | False | False | True | 0.91455405 | 318 | 97 | 0.10208668 | 0.30503145 | 0.0050314465 | 0.30503145 | 1555 | 691 | 0.49919743 | 0.44437299 |
| explanation_only | 4 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 2800 | 1786 | 1 | 0.63785714 | 0.53785714 | 0.63785714 | 2800 | 1786 | 1 | 0.63785714 |
| explanation_only | 4 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.44895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| explanation_only | 4 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 2800 | 1786 | 1 | 0.63785714 | 0.43785714 | 0.63785714 | 2800 | 1786 | 1 | 0.63785714 |
| explanation_only | 4 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.34895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| explanation_only | 4 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 2800 | 1786 | 1 | 0.63785714 | 0.33785714 | 0.63785714 | 2800 | 1786 | 1 | 0.63785714 |
| explanation_only | 4 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.24895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| question_plus_explanation | 0 | confidence_only | 10% | 0 | 200, 16, 0, 0, 41, 0, 3760, 0 | False | False | True | 0.85469628 | 119 | 70 | 0.10033727 | 0.58823529 | 0.48823529 | 0.58823529 | 281 | 190 | 0.23693086 | 0.67615658 |
| question_plus_explanation | 0 | confidence_only | 10% | 1 | 166, 0, 0, 0, 380, 0, 3471, 0 | False | False | True | 0.76266934 | 437 | 235 | 0.14028892 | 0.53775744 | 0.43775744 | 0.53775744 | 315 | 176 | 0.1011236 | 0.55873016 |
| question_plus_explanation | 0 | confidence_only | 20% | 0 | 195, 21, 0, 0, 41, 0, 3760, 0 | False | False | True | 0.85469628 | 119 | 70 | 0.10033727 | 0.58823529 | 0.38823529 | 0.58823529 | 281 | 190 | 0.23693086 | 0.67615658 |
| question_plus_explanation | 0 | confidence_only | 20% | 1 | 166, 0, 0, 0, 380, 0, 3471, 0 | False | False | True | 0.76266934 | 437 | 235 | 0.14028892 | 0.53775744 | 0.33775744 | 0.53775744 | 315 | 176 | 0.1011236 | 0.55873016 |
| question_plus_explanation | 0 | confidence_only | 30% | 0 | 180, 36, 0, 0, 41, 0, 3760, 0 | False | False | True | 0.85469628 | 119 | 70 | 0.10033727 | 0.58823529 | 0.28823529 | 0.58823529 | 281 | 190 | 0.23693086 | 0.67615658 |
| question_plus_explanation | 0 | confidence_only | 30% | 1 | 166, 0, 0, 0, 380, 0, 3471, 0 | False | False | True | 0.76266934 | 437 | 235 | 0.14028892 | 0.53775744 | 0.23775744 | 0.53775744 | 315 | 176 | 0.1011236 | 0.55873016 |
| question_plus_explanation | 0 | support_aware | 10% | 0 | 307, 55, 0, 0, 42, 0, 3613, 0 | False | False | True | 0.79356981 | 119 | 70 | 0.10033727 | 0.58823529 | 0.48823529 | 0.58823529 | 119 | 70 | 0.10033727 | 0.58823529 |
| question_plus_explanation | 0 | support_aware | 10% | 1 | 101, 0, 0, 0, 298, 0, 3618, 0 | False | False | True | 0.76266145 | 400 | 211 | 0.12841091 | 0.5275 | 0.4275 | 0.5275 | 318 | 178 | 0.10208668 | 0.55974843 |
| question_plus_explanation | 0 | support_aware | 20% | 0 | 307, 55, 0, 0, 42, 0, 3613, 0 | False | False | True | 0.79356981 | 119 | 70 | 0.10033727 | 0.58823529 | 0.38823529 | 0.58823529 | 119 | 70 | 0.10033727 | 0.58823529 |
| question_plus_explanation | 0 | support_aware | 20% | 1 | 101, 0, 0, 0, 298, 0, 3618, 0 | False | False | True | 0.76266145 | 400 | 211 | 0.12841091 | 0.5275 | 0.3275 | 0.5275 | 318 | 178 | 0.10208668 | 0.55974843 |
| question_plus_explanation | 0 | support_aware | 30% | 0 | 261, 101, 0, 0, 42, 0, 3613, 0 | False | False | True | 0.79356981 | 119 | 70 | 0.10033727 | 0.58823529 | 0.28823529 | 0.58823529 | 119 | 70 | 0.10033727 | 0.58823529 |
| question_plus_explanation | 0 | support_aware | 30% | 1 | 101, 0, 0, 0, 298, 0, 3618, 0 | False | False | True | 0.76266145 | 400 | 211 | 0.12841091 | 0.5275 | 0.2275 | 0.5275 | 318 | 178 | 0.10208668 | 0.55974843 |
| question_plus_explanation | 0 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.59139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 0 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.44895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| question_plus_explanation | 0 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.49139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 0 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.34895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| question_plus_explanation | 0 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.39139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 0 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.24895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| question_plus_explanation | 1 | confidence_only | 10% | 0 | 799, 145, 0, 0, 49, 0, 3024, 0 | False | False | True | 0.4942384 | 119 | 71 | 0.10033727 | 0.59663866 | 0.49663866 | 0.59663866 | 973 | 710 | 0.82040472 | 0.72970195 |
| question_plus_explanation | 1 | confidence_only | 10% | 1 | 92, 0, 0, 0, 203, 0, 3722, 0 | False | False | True | 0.19473508 | 3103 | 2180 | 0.99935588 | 0.70254592 | 0.60254592 | 0.70254592 | 2422 | 1761 | 0.78003221 | 0.72708505 |
| question_plus_explanation | 1 | confidence_only | 20% | 0 | 775, 169, 0, 0, 49, 0, 3024, 0 | False | False | True | 0.4942384 | 119 | 71 | 0.10033727 | 0.59663866 | 0.39663866 | 0.59663866 | 973 | 710 | 0.82040472 | 0.72970195 |
| question_plus_explanation | 1 | confidence_only | 20% | 1 | 92, 0, 0, 0, 203, 0, 3722, 0 | False | False | True | 0.19473508 | 3103 | 2180 | 0.99935588 | 0.70254592 | 0.50254592 | 0.70254592 | 2422 | 1761 | 0.78003221 | 0.72708505 |
| question_plus_explanation | 1 | confidence_only | 30% | 0 | 525, 419, 0, 0, 49, 0, 3024, 0 | False | False | True | 0.4942384 | 119 | 71 | 0.10033727 | 0.59663866 | 0.29663866 | 0.59663866 | 973 | 710 | 0.82040472 | 0.72970195 |
| question_plus_explanation | 1 | confidence_only | 30% | 1 | 92, 0, 0, 0, 203, 0, 3722, 0 | False | False | True | 0.19473508 | 3103 | 2180 | 0.99935588 | 0.70254592 | 0.40254592 | 0.70254592 | 2422 | 1761 | 0.78003221 | 0.72708505 |
| question_plus_explanation | 1 | support_aware | 10% | 0 | 1030, 93, 0, 0, 55, 0, 2839, 0 | False | False | True | 0.45224005 | 119 | 71 | 0.10033727 | 0.59663866 | 0.49663866 | 0.59663866 | 988 | 717 | 0.83305228 | 0.7257085 |
| question_plus_explanation | 1 | support_aware | 10% | 1 | 92, 0, 0, 0, 200, 0, 3725, 0 | False | False | True | 0.23245091 | 2982 | 2080 | 0.96038647 | 0.69751844 | 0.59751844 | 0.69751844 | 2538 | 1799 | 0.8173913 | 0.70882585 |
| question_plus_explanation | 1 | support_aware | 20% | 0 | 951, 172, 0, 0, 55, 0, 2839, 0 | False | False | True | 0.45224005 | 119 | 71 | 0.10033727 | 0.59663866 | 0.39663866 | 0.59663866 | 988 | 717 | 0.83305228 | 0.7257085 |
| question_plus_explanation | 1 | support_aware | 20% | 1 | 92, 0, 0, 0, 200, 0, 3725, 0 | False | False | True | 0.23245091 | 2982 | 2080 | 0.96038647 | 0.69751844 | 0.49751844 | 0.69751844 | 2538 | 1799 | 0.8173913 | 0.70882585 |
| question_plus_explanation | 1 | support_aware | 30% | 0 | 843, 280, 0, 0, 55, 0, 2839, 0 | False | False | True | 0.45224005 | 119 | 71 | 0.10033727 | 0.59663866 | 0.29663866 | 0.59663866 | 988 | 717 | 0.83305228 | 0.7257085 |
| question_plus_explanation | 1 | support_aware | 30% | 1 | 92, 0, 0, 0, 200, 0, 3725, 0 | False | False | True | 0.23245091 | 2982 | 2080 | 0.96038647 | 0.69751844 | 0.39751844 | 0.69751844 | 2538 | 1799 | 0.8173913 | 0.70882585 |
| question_plus_explanation | 1 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.59139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 1 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3105 | 1870 | 1 | 0.60225443 | 0.50225443 | 0.60225443 | 3105 | 1870 | 1 | 0.60225443 |
| question_plus_explanation | 1 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.49139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 1 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3105 | 1870 | 1 | 0.60225443 | 0.40225443 | 0.60225443 | 3105 | 1870 | 1 | 0.60225443 |
| question_plus_explanation | 1 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.39139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 1 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3105 | 1870 | 1 | 0.60225443 | 0.30225443 | 0.60225443 | 3105 | 1870 | 1 | 0.60225443 |
| question_plus_explanation | 2 | confidence_only | 10% | 0 | 461, 559, 0, 0, 92, 0, 3292, 0 | False | False | True | 0.49926063 | 145 | 34 | 0.1222597 | 0.23448276 | 0.13448276 | 0.23448276 | 128 | 33 | 0.1079258 | 0.2578125 |
| question_plus_explanation | 2 | confidence_only | 10% | 1 | 45, 53, 0, 0, 253, 0, 4053, 0 | False | False | True | 0.65312033 | 364 | 103 | 0.1 | 0.28296703 | 0.18296703 | 0.28296703 | 1126 | 488 | 0.30934066 | 0.43339254 |
| question_plus_explanation | 2 | confidence_only | 20% | 0 | 168, 852, 0, 0, 92, 0, 3292, 0 | False | False | True | 0.49926063 | 145 | 34 | 0.1222597 | 0.23448276 | 0.034482759 | 0.23448276 | 128 | 33 | 0.1079258 | 0.2578125 |
| question_plus_explanation | 2 | confidence_only | 20% | 1 | 0, 98, 0, 0, 218, 35, 4053, 0 | False | False | True | 0.65312033 | 364 | 103 | 0.1 | 0.28296703 | 0.082967033 | 0.28296703 | 1126 | 488 | 0.30934066 | 0.43339254 |
| question_plus_explanation | 2 | confidence_only | 30% | 0 | 50, 970, 0, 0, 0, 92, 2769, 523 | True | False | False | 0.49926063 | 145 | 34 | 0.1222597 | 0.23448276 | -0.065517241 | 0.23448276 | 128 | 33 | 0.1079258 | 0.2578125 |
| question_plus_explanation | 2 | confidence_only | 30% | 1 | 0, 98, 0, 0, 0, 253, 4032, 21 | True | False | False | 0.65312033 | 364 | 103 | 0.1 | 0.28296703 | -0.017032967 | 0.28296703 | 1126 | 488 | 0.30934066 | 0.43339254 |
| question_plus_explanation | 2 | support_aware | 10% | 0 | 526, 522, 0, 0, 107, 0, 3249, 0 | False | False | True | 0.4872385 | 133 | 19 | 0.11214165 | 0.14285714 | 0.042857143 | 0.14285714 | 123 | 19 | 0.10370995 | 0.15447154 |
| question_plus_explanation | 2 | support_aware | 10% | 1 | 39, 59, 0, 0, 257, 0, 4049, 0 | False | False | True | 0.64947725 | 365 | 106 | 0.10027473 | 0.29041096 | 0.19041096 | 0.29041096 | 1146 | 498 | 0.31483516 | 0.43455497 |
| question_plus_explanation | 2 | support_aware | 20% | 0 | 49, 999, 0, 0, 0, 107, 2991, 258 | True | False | False | 0.4872385 | 133 | 19 | 0.11214165 | 0.14285714 | -0.057142857 | 0.14285714 | 123 | 19 | 0.10370995 | 0.15447154 |
| question_plus_explanation | 2 | support_aware | 20% | 1 | 0, 98, 0, 0, 208, 49, 4049, 0 | False | False | True | 0.64947725 | 365 | 106 | 0.10027473 | 0.29041096 | 0.090410959 | 0.29041096 | 1146 | 498 | 0.31483516 | 0.43455497 |
| question_plus_explanation | 2 | support_aware | 30% | 0 | 49, 999, 0, 0, 0, 107, 2487, 762 | True | False | False | 0.4872385 | 133 | 19 | 0.11214165 | 0.14285714 | -0.15714286 | 0.14285714 | 123 | 19 | 0.10370995 | 0.15447154 |
| question_plus_explanation | 2 | support_aware | 30% | 1 | 0, 98, 0, 0, 0, 257, 4026, 23 | True | False | False | 0.64947725 | 365 | 106 | 0.10027473 | 0.29041096 | -0.0095890411 | 0.29041096 | 1146 | 498 | 0.31483516 | 0.43455497 |
| question_plus_explanation | 2 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.59139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 2 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3640 | 2500 | 1 | 0.68681319 | 0.58681319 | 0.68681319 | 3640 | 2500 | 1 | 0.68681319 |
| question_plus_explanation | 2 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.49139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 2 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3640 | 2500 | 1 | 0.68681319 | 0.48681319 | 0.68681319 | 3640 | 2500 | 1 | 0.68681319 |
| question_plus_explanation | 2 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1186 | 820 | 1 | 0.69139966 | 0.39139966 | 0.69139966 | 1186 | 820 | 1 | 0.69139966 |
| question_plus_explanation | 2 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3640 | 2500 | 1 | 0.68681319 | 0.38681319 | 0.68681319 | 3640 | 2500 | 1 | 0.68681319 |
| question_plus_explanation | 3 | confidence_only | 10% | 0 | 81, 6, 0, 0, 351, 0, 4806, 0 | False | False | True | 0.87029749 | 651 | 241 | 0.13403335 | 0.37019969 | 0.27019969 | 0.37019969 | 3350 | 1967 | 0.68972617 | 0.58716418 |
| question_plus_explanation | 3 | confidence_only | 10% | 1 | 2552, 433, 0, 0, 70, 0, 2189, 0 | False | False | True | 0.69546774 | 121 | 56 | 0.11512845 | 0.46280992 | 0.36280992 | 0.46280992 | 106 | 50 | 0.10085633 | 0.47169811 |
| question_plus_explanation | 3 | confidence_only | 20% | 0 | 76, 11, 0, 0, 351, 0, 4806, 0 | False | False | True | 0.87029749 | 651 | 241 | 0.13403335 | 0.37019969 | 0.17019969 | 0.37019969 | 3350 | 1967 | 0.68972617 | 0.58716418 |
| question_plus_explanation | 3 | confidence_only | 20% | 1 | 2323, 662, 0, 0, 70, 0, 2189, 0 | False | False | True | 0.69546774 | 121 | 56 | 0.11512845 | 0.46280992 | 0.26280992 | 0.46280992 | 106 | 50 | 0.10085633 | 0.47169811 |
| question_plus_explanation | 3 | confidence_only | 30% | 0 | 65, 22, 0, 0, 351, 0, 4806, 0 | False | False | True | 0.87029749 | 651 | 241 | 0.13403335 | 0.37019969 | 0.070199693 | 0.37019969 | 3350 | 1967 | 0.68972617 | 0.58716418 |
| question_plus_explanation | 3 | confidence_only | 30% | 1 | 2251, 734, 0, 0, 70, 0, 2189, 0 | False | False | True | 0.69546774 | 121 | 56 | 0.11512845 | 0.46280992 | 0.16280992 | 0.46280992 | 106 | 50 | 0.10085633 | 0.47169811 |
| question_plus_explanation | 3 | support_aware | 10% | 0 | 81, 6, 0, 0, 350, 0, 4807, 0 | False | False | True | 0.87029749 | 651 | 241 | 0.13403335 | 0.37019969 | 0.27019969 | 0.37019969 | 3884 | 2378 | 0.79967058 | 0.61225541 |
| question_plus_explanation | 3 | support_aware | 10% | 1 | 1639, 1793, 0, 0, 56, 0, 1756, 0 | False | False | True | 0.66482054 | 107 | 43 | 0.1018078 | 0.40186916 | 0.30186916 | 0.40186916 | 106 | 43 | 0.10085633 | 0.40566038 |
| question_plus_explanation | 3 | support_aware | 20% | 0 | 76, 11, 0, 0, 350, 0, 4807, 0 | False | False | True | 0.87029749 | 651 | 241 | 0.13403335 | 0.37019969 | 0.17019969 | 0.37019969 | 3884 | 2378 | 0.79967058 | 0.61225541 |
| question_plus_explanation | 3 | support_aware | 20% | 1 | 1442, 1990, 0, 0, 56, 0, 1756, 0 | False | False | True | 0.66482054 | 107 | 43 | 0.1018078 | 0.40186916 | 0.20186916 | 0.40186916 | 106 | 43 | 0.10085633 | 0.40566038 |
| question_plus_explanation | 3 | support_aware | 30% | 0 | 65, 22, 0, 0, 350, 0, 4807, 0 | False | False | True | 0.87029749 | 651 | 241 | 0.13403335 | 0.37019969 | 0.070199693 | 0.37019969 | 3884 | 2378 | 0.79967058 | 0.61225541 |
| question_plus_explanation | 3 | support_aware | 30% | 1 | 1105, 2327, 0, 0, 56, 0, 1756, 0 | False | False | True | 0.66482054 | 107 | 43 | 0.1018078 | 0.40186916 | 0.10186916 | 0.40186916 | 106 | 43 | 0.10085633 | 0.40566038 |
| question_plus_explanation | 3 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 4857 | 3138 | 1 | 0.64607783 | 0.54607783 | 0.64607783 | 4857 | 3138 | 1 | 0.64607783 |
| question_plus_explanation | 3 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1051 | 624 | 1 | 0.59372027 | 0.49372027 | 0.59372027 | 1051 | 624 | 1 | 0.59372027 |
| question_plus_explanation | 3 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 4857 | 3138 | 1 | 0.64607783 | 0.44607783 | 0.64607783 | 4857 | 3138 | 1 | 0.64607783 |
| question_plus_explanation | 3 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1051 | 624 | 1 | 0.59372027 | 0.39372027 | 0.59372027 | 1051 | 624 | 1 | 0.59372027 |
| question_plus_explanation | 3 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 4857 | 3138 | 1 | 0.64607783 | 0.34607783 | 0.64607783 | 4857 | 3138 | 1 | 0.64607783 |
| question_plus_explanation | 3 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 1051 | 624 | 1 | 0.59372027 | 0.29372027 | 0.59372027 | 1051 | 624 | 1 | 0.59372027 |
| question_plus_explanation | 4 | confidence_only | 10% | 0 | 994, 0, 0, 0, 511, 0, 4112, 0 | False | False | True | 0.71641053 | 280 | 223 | 0.1 | 0.79642857 | 0.69642857 | 0.79642857 | 280 | 223 | 0.1 | 0.79642857 |
| question_plus_explanation | 4 | confidence_only | 10% | 1 | 91, 6, 0, 0, 204, 0, 5316, 0 | False | False | True | 0.94533647 | 336 | 101 | 0.10786517 | 0.30059524 | 0.20059524 | 0.30059524 | 1294 | 539 | 0.41540931 | 0.41653787 |
| question_plus_explanation | 4 | confidence_only | 20% | 0 | 994, 0, 0, 0, 511, 0, 4112, 0 | False | False | True | 0.71641053 | 280 | 223 | 0.1 | 0.79642857 | 0.59642857 | 0.79642857 | 280 | 223 | 0.1 | 0.79642857 |
| question_plus_explanation | 4 | confidence_only | 20% | 1 | 28, 69, 0, 0, 204, 0, 5316, 0 | False | False | True | 0.94533647 | 336 | 101 | 0.10786517 | 0.30059524 | 0.10059524 | 0.30059524 | 1294 | 539 | 0.41540931 | 0.41653787 |
| question_plus_explanation | 4 | confidence_only | 30% | 0 | 994, 0, 0, 0, 511, 0, 4112, 0 | False | False | True | 0.71641053 | 280 | 223 | 0.1 | 0.79642857 | 0.49642857 | 0.79642857 | 280 | 223 | 0.1 | 0.79642857 |
| question_plus_explanation | 4 | confidence_only | 30% | 1 | 0, 97, 0, 0, 6, 198, 5316, 0 | False | False | True | 0.94533647 | 336 | 101 | 0.10786517 | 0.30059524 | 0.0005952381 | 0.30059524 | 1294 | 539 | 0.41540931 | 0.41653787 |
| question_plus_explanation | 4 | support_aware | 10% | 0 | 1236, 0, 0, 0, 492, 0, 3889, 0 | False | False | True | 0.56315943 | 442 | 315 | 0.15785714 | 0.71266968 | 0.61266968 | 0.71266968 | 442 | 315 | 0.15785714 | 0.71266968 |
| question_plus_explanation | 4 | support_aware | 10% | 1 | 91, 6, 0, 0, 204, 0, 5316, 0 | False | False | True | 0.94533647 | 336 | 101 | 0.10786517 | 0.30059524 | 0.20059524 | 0.30059524 | 1759 | 776 | 0.564687 | 0.44115975 |
| question_plus_explanation | 4 | support_aware | 20% | 0 | 1236, 0, 0, 0, 492, 0, 3889, 0 | False | False | True | 0.56315943 | 442 | 315 | 0.15785714 | 0.71266968 | 0.51266968 | 0.71266968 | 442 | 315 | 0.15785714 | 0.71266968 |
| question_plus_explanation | 4 | support_aware | 20% | 1 | 28, 69, 0, 0, 204, 0, 5316, 0 | False | False | True | 0.94533647 | 336 | 101 | 0.10786517 | 0.30059524 | 0.10059524 | 0.30059524 | 1759 | 776 | 0.564687 | 0.44115975 |
| question_plus_explanation | 4 | support_aware | 30% | 0 | 1236, 0, 0, 0, 492, 0, 3889, 0 | False | False | True | 0.56315943 | 442 | 315 | 0.15785714 | 0.71266968 | 0.41266968 | 0.71266968 | 442 | 315 | 0.15785714 | 0.71266968 |
| question_plus_explanation | 4 | support_aware | 30% | 1 | 0, 97, 0, 0, 6, 198, 5316, 0 | False | False | True | 0.94533647 | 336 | 101 | 0.10786517 | 0.30059524 | 0.0005952381 | 0.30059524 | 1759 | 776 | 0.564687 | 0.44115975 |
| question_plus_explanation | 4 | frequency | 10% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 2800 | 1786 | 1 | 0.63785714 | 0.53785714 | 0.63785714 | 2800 | 1786 | 1 | 0.63785714 |
| question_plus_explanation | 4 | frequency | 10% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.44895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| question_plus_explanation | 4 | frequency | 20% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 2800 | 1786 | 1 | 0.63785714 | 0.43785714 | 0.63785714 | 2800 | 1786 | 1 | 0.63785714 |
| question_plus_explanation | 4 | frequency | 20% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.34895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |
| question_plus_explanation | 4 | frequency | 30% | 0 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 2800 | 1786 | 1 | 0.63785714 | 0.33785714 | 0.63785714 | 2800 | 1786 | 1 | 0.63785714 |
| question_plus_explanation | 4 | frequency | 30% | 1 | 0, 0, 0, 0, 0, 0, 2, 0 | False | False | True | 0 | 3115 | 1710 | 1 | 0.54895666 | 0.24895666 | 0.54895666 | 3115 | 1710 | 1 | 0.54895666 |

## Fixed-prediction oracle bounds (deduplicated)

These are correctness-informed count bounds, not observed selector performance. Effective m=max(100,ceil(N/10)); stronger floor identifies the redundant weaker constraint. K=0 means no possible coverage, not an observed zero error. Each oracle is shared by both learned rules; frequency is shared by both arms.

| Model / arm | Fold | Role | N | Correct | Coverage floor n | m | Stronger floor | Oracle min risk at m | K10 | Max coverage10 | Feasible10 | K20 | Max coverage20 | Feasible20 | K30 | Max coverage30 | Feasible30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| tfidf_logreg / explanation_only | 0 | 0 | 1186 | 411 | 119 | 119 | coverage | 0 | 456 | 0.38448567 | True | 513 | 0.43254637 | True | 587 | 0.49494098 | True |
| tfidf_logreg / explanation_only | 0 | 1 | 3115 | 978 | 312 | 312 | coverage | 0 | 1086 | 0.34863563 | True | 1222 | 0.39229535 | True | 1397 | 0.44847512 | True |
| frequency_baseline / shared_frequency | 0 | 0 | 1186 | 366 | 119 | 119 | coverage | 0 | 406 | 0.34232715 | True | 457 | 0.38532884 | True | 522 | 0.44013491 | True |
| frequency_baseline / shared_frequency | 0 | 1 | 3115 | 1405 | 312 | 312 | coverage | 0 | 1561 | 0.5011236 | True | 1756 | 0.56372392 | True | 2007 | 0.64430177 | True |
| tfidf_logreg / explanation_only | 1 | 0 | 1186 | 328 | 119 | 119 | coverage | 0 | 364 | 0.306914 | True | 410 | 0.34569983 | True | 468 | 0.39460371 | True |
| tfidf_logreg / explanation_only | 1 | 1 | 3105 | 818 | 311 | 311 | coverage | 0 | 908 | 0.29243156 | True | 1022 | 0.32914654 | True | 1168 | 0.37616747 | True |
| frequency_baseline / shared_frequency | 1 | 0 | 1186 | 366 | 119 | 119 | coverage | 0 | 406 | 0.34232715 | True | 457 | 0.38532884 | True | 522 | 0.44013491 | True |
| frequency_baseline / shared_frequency | 1 | 1 | 3105 | 1235 | 311 | 311 | coverage | 0 | 1372 | 0.44186795 | True | 1543 | 0.49694042 | True | 1764 | 0.56811594 | True |
| tfidf_logreg / explanation_only | 2 | 0 | 1186 | 508 | 119 | 119 | coverage | 0 | 564 | 0.47554806 | True | 635 | 0.53541315 | True | 725 | 0.61129848 | True |
| tfidf_logreg / explanation_only | 2 | 1 | 3640 | 1287 | 364 | 364 | coverage | 0 | 1430 | 0.39285714 | True | 1608 | 0.44175824 | True | 1838 | 0.50494505 | True |
| frequency_baseline / shared_frequency | 2 | 0 | 1186 | 366 | 119 | 119 | coverage | 0 | 406 | 0.34232715 | True | 457 | 0.38532884 | True | 522 | 0.44013491 | True |
| frequency_baseline / shared_frequency | 2 | 1 | 3640 | 1140 | 364 | 364 | coverage | 0 | 1266 | 0.3478022 | True | 1425 | 0.39148352 | True | 1628 | 0.44725275 | True |
| tfidf_logreg / explanation_only | 3 | 0 | 4857 | 1426 | 486 | 486 | coverage | 0 | 1584 | 0.32612724 | True | 1782 | 0.36689314 | True | 2037 | 0.41939469 | True |
| tfidf_logreg / explanation_only | 3 | 1 | 1051 | 282 | 106 | 106 | coverage | 0 | 313 | 0.29781161 | True | 352 | 0.33491912 | True | 402 | 0.38249286 | True |
| frequency_baseline / shared_frequency | 3 | 0 | 4857 | 1719 | 486 | 486 | coverage | 0 | 1910 | 0.39324686 | True | 2148 | 0.4422483 | True | 2455 | 0.50545604 | True |
| frequency_baseline / shared_frequency | 3 | 1 | 1051 | 427 | 106 | 106 | coverage | 0 | 474 | 0.45099905 | True | 533 | 0.50713606 | True | 610 | 0.58039962 | True |
| tfidf_logreg / explanation_only | 4 | 0 | 2800 | 473 | 280 | 280 | coverage | 0 | 525 | 0.1875 | True | 591 | 0.21107143 | True | 675 | 0.24107143 | True |
| tfidf_logreg / explanation_only | 4 | 1 | 3115 | 1371 | 312 | 312 | coverage | 0 | 1523 | 0.48892456 | True | 1713 | 0.54991974 | True | 1958 | 0.62857143 | True |
| frequency_baseline / shared_frequency | 4 | 0 | 2800 | 1014 | 280 | 280 | coverage | 0 | 1126 | 0.40214286 | True | 1267 | 0.4525 | True | 1448 | 0.51714286 | True |
| frequency_baseline / shared_frequency | 4 | 1 | 3115 | 1405 | 312 | 312 | coverage | 0 | 1561 | 0.5011236 | True | 1756 | 0.56372392 | True | 2007 | 0.64430177 | True |
| tfidf_logreg / question_plus_explanation | 0 | 0 | 1186 | 323 | 119 | 119 | coverage | 0 | 358 | 0.30185497 | True | 403 | 0.33979764 | True | 461 | 0.38870152 | True |
| tfidf_logreg / question_plus_explanation | 0 | 1 | 3115 | 1134 | 312 | 312 | coverage | 0 | 1260 | 0.40449438 | True | 1417 | 0.45489567 | True | 1620 | 0.52006421 | True |
| tfidf_logreg / question_plus_explanation | 1 | 0 | 1186 | 307 | 119 | 119 | coverage | 0 | 341 | 0.28752108 | True | 383 | 0.32293423 | True | 438 | 0.3693086 | True |
| tfidf_logreg / question_plus_explanation | 1 | 1 | 3105 | 923 | 311 | 311 | coverage | 0 | 1025 | 0.33011272 | True | 1153 | 0.37133655 | True | 1318 | 0.42447665 | True |
| tfidf_logreg / question_plus_explanation | 2 | 0 | 1186 | 520 | 119 | 119 | coverage | 0 | 577 | 0.48650927 | True | 650 | 0.54806071 | True | 742 | 0.62563238 | True |
| tfidf_logreg / question_plus_explanation | 2 | 1 | 3640 | 1290 | 364 | 364 | coverage | 0 | 1433 | 0.39368132 | True | 1612 | 0.44285714 | True | 1842 | 0.50604396 | True |
| tfidf_logreg / question_plus_explanation | 3 | 0 | 4857 | 1720 | 486 | 486 | coverage | 0 | 1911 | 0.39345275 | True | 2150 | 0.44266008 | True | 2457 | 0.50586782 | True |
| tfidf_logreg / question_plus_explanation | 3 | 1 | 1051 | 417 | 106 | 106 | coverage | 0 | 463 | 0.44053283 | True | 521 | 0.49571836 | True | 595 | 0.5661275 | True |
| tfidf_logreg / question_plus_explanation | 4 | 0 | 2800 | 485 | 280 | 280 | coverage | 0 | 538 | 0.19214286 | True | 606 | 0.21642857 | True | 692 | 0.24714286 | True |
| tfidf_logreg / question_plus_explanation | 4 | 1 | 3115 | 1376 | 312 | 312 | coverage | 0 | 1528 | 0.4905297 | True | 1720 | 0.55216693 | True | 1965 | 0.63081862 | True |

## Complete numeric fold summaries

Values are folds 0–4. Question means weight the two development questions equally; an undefined component leaves that mean null. SD uses ddof=1 and is null with fewer than two defined folds.

### explanation_only / confidence_only / 20%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 236 | 350 | 421 | 251 | 732 | 398 | 201.39638 | 5 |
| joint.histogram.001 | 0 | 0 | 64 | 0 | 0 | 12.8 | 28.62167 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 190 | 77 | 101 | 388 | 474 | 246 | 176.68475 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| joint.counts.count_pass | 3788 | 3664 | 3926 | 4986 | 4870 | 4246.8 | 630.05174 | 5 |
| joint.counts.coverage_pass | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.counts.risk_pass | 0 | 0 | 64 | 0 | 0 | 12.8 | 28.62167 | 5 |
| joint.counts.both_floors | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| shared.threshold | 0.74528599 | 0.59941219 | 0.50444153 | 0.70564 | 0.33674146 | 0.57830424 | 0.16458366 | 5 |
| shared.worst_risk | 0.60339943 | 0.68124118 | 0.35452794 | 0.65737052 | 0.83006797 | 0.62532141 | 0.17312207 | 5 |
| shared.error_minus_target | 0.40339943 | 0.48124118 | 0.15452794 | 0.45737052 | 0.63006797 | 0.42532141 | 0.17312207 | 5 |
| q0.histogram.000 | 163 | 335 | 35 | 109 | 732 | 274.8 | 278.45502 | 5 |
| q0.histogram.001 | 73 | 15 | 450 | 54 | 0 | 118.4 | 187.66806 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 48 | 77 | 64 | 476 | 474 | 227.8 | 225.89644 | 5 |
| q0.histogram.101 | 0 | 0 | 37 | 0 | 0 | 7.4 | 16.546903 | 5 |
| q0.histogram.110 | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q0.counts.count_pass | 3788 | 3664 | 3926 | 5074 | 4870 | 4264.4 | 656.53545 | 5 |
| q0.counts.coverage_pass | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.counts.risk_pass | 73 | 15 | 487 | 54 | 0 | 125.8 | 204.02867 | 5 |
| q0.counts.both_floors | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 37 | 0 | 0 | 7.4 | 16.546903 | 5 |
| q0.counts.risk_only_failure | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.minimum.threshold | 0.79779847 | 0.69796232 | 0.50546572 | 0.72209528 | 0.33674146 | 0.61201265 | 0.18784859 | 5 |
| q0.minimum.retained_n | 121 | 120 | 119 | 502 | 2501 | 672.6 | 1035.4049 | 5 |
| q0.minimum.incorrect_n | 44 | 76 | 24 | 282 | 2076 | 500.4 | 886.79017 | 5 |
| q0.minimum.coverage | 0.10202361 | 0.10118044 | 0.10033727 | 0.10335598 | 0.89321429 | 0.26002232 | 0.35396683 | 5 |
| q0.minimum.risk | 0.36363636 | 0.63333333 | 0.20168067 | 0.56175299 | 0.83006797 | 0.51809427 | 0.24315043 | 5 |
| q0.minimum.error_minus_target | 0.16363636 | 0.43333333 | 0.0016806723 | 0.36175299 | 0.63006797 | 0.31809427 | 0.24315043 | 5 |
| q0.minimum.oracle_risk_gap | 0.36363636 | 0.63333333 | 0.20168067 | 0.56175299 | 0.83006797 | 0.51809427 | 0.24315043 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 411 | 328 | 508 | 1426 | 473 | 629.2 | 450.64143 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 513 | 410 | 635 | 1782 | 591 | 786.2 | 563.19331 | 5 |
| q0.oracle.maximum_coverage | 0.43254637 | 0.34569983 | 0.53541315 | 0.36689314 | 0.21107143 | 0.37832479 | 0.11914853 | 5 |
| q0.shared.retained_n | 179 | 298 | 123 | 590 | 2501 | 738.2 | 1001.7957 | 5 |
| q0.shared.incorrect_n | 77 | 203 | 25 | 340 | 2076 | 544.2 | 864.92352 | 5 |
| q0.shared.coverage | 0.15092749 | 0.25126476 | 0.10370995 | 0.12147416 | 0.89321429 | 0.30411813 | 0.334222 | 5 |
| q0.shared.risk | 0.4301676 | 0.68120805 | 0.20325203 | 0.57627119 | 0.83006797 | 0.54419337 | 0.2401922 | 5 |
| q1.histogram.000 | 161 | 125 | 45 | 251 | 8 | 118 | 96.197713 | 5 |
| q1.histogram.001 | 0 | 0 | 65 | 0 | 87 | 30.4 | 42.347373 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 265 | 268 | 309 | 19 | 215 | 215.2 | 114.63071 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q1.counts.count_pass | 3863 | 3889 | 4301 | 4986 | 5507 | 4509.2 | 719.11626 | 5 |
| q1.counts.coverage_pass | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.counts.risk_pass | 0 | 0 | 65 | 0 | 87 | 30.4 | 42.347373 | 5 |
| q1.counts.both_floors | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.minimum.threshold | 0.74528599 | 0.60407405 | 0.54230437 | 0.78649209 | 0.91455405 | 0.71854211 | 0.14825299 | 5 |
| q1.minimum.retained_n | 353 | 686 | 366 | 127 | 321 | 370.6 | 201.00323 | 5 |
| q1.minimum.incorrect_n | 213 | 466 | 120 | 80 | 100 | 195.8 | 159.40263 | 5 |
| q1.minimum.coverage | 0.11332263 | 0.22093398 | 0.10054945 | 0.1208373 | 0.10304976 | 0.13173862 | 0.050521318 | 5 |
| q1.minimum.risk | 0.60339943 | 0.67930029 | 0.32786885 | 0.62992126 | 0.31152648 | 0.51040326 | 0.17630218 | 5 |
| q1.minimum.error_minus_target | 0.40339943 | 0.47930029 | 0.12786885 | 0.42992126 | 0.11152648 | 0.31040326 | 0.17630218 | 5 |
| q1.minimum.oracle_risk_gap | 0.60339943 | 0.67930029 | 0.32786885 | 0.62992126 | 0.31152648 | 0.51040326 | 0.17630218 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 978 | 818 | 1287 | 282 | 1371 | 947.2 | 434.51203 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1222 | 1022 | 1608 | 352 | 1713 | 1183.4 | 543.0302 | 5 |
| q1.oracle.maximum_coverage | 0.39229535 | 0.32914654 | 0.44175824 | 0.33491912 | 0.54991974 | 0.4096078 | 0.090930229 | 5 |
| q1.shared.retained_n | 353 | 709 | 519 | 251 | 2892 | 944.8 | 1102.2795 | 5 |
| q1.shared.incorrect_n | 213 | 483 | 184 | 165 | 1581 | 525.2 | 604.17812 | 5 |
| q1.shared.coverage | 0.11332263 | 0.22834138 | 0.14258242 | 0.23882017 | 0.92841091 | 0.3302955 | 0.33868047 | 5 |
| q1.shared.risk | 0.60339943 | 0.68124118 | 0.35452794 | 0.65737052 | 0.5466805 | 0.56864391 | 0.13046699 | 5 |
| question_mean.minimum.risk | 0.4835179 | 0.65631681 | 0.26477476 | 0.59583712 | 0.57079723 | 0.51424876 | 0.15265925 | 5 |
| question_mean.minimum.coverage | 0.10767312 | 0.16105721 | 0.10044336 | 0.11209664 | 0.49813202 | 0.19588047 | 0.17064376 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.4835179 | 0.65631681 | 0.26477476 | 0.59583712 | 0.57079723 | 0.51424876 | 0.15265925 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.41242086 | 0.33742318 | 0.4885857 | 0.35090613 | 0.38049559 | 0.39396629 | 0.060262267 | 5 |
| question_mean.shared.risk | 0.51678352 | 0.68122462 | 0.27888999 | 0.61682085 | 0.68837424 | 0.55641864 | 0.16972797 | 5 |
| question_mean.shared.coverage | 0.13212506 | 0.23980307 | 0.12314618 | 0.18014717 | 0.9108126 | 0.31720682 | 0.33505944 | 5 |

### explanation_only / confidence_only / 10%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 236 | 350 | 479 | 251 | 732 | 409.6 | 204.69563 | 5 |
| joint.histogram.001 | 0 | 0 | 6 | 0 | 0 | 1.2 | 2.6832816 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 190 | 77 | 101 | 388 | 474 | 246 | 176.68475 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| joint.counts.count_pass | 3788 | 3664 | 3926 | 4986 | 4870 | 4246.8 | 630.05174 | 5 |
| joint.counts.coverage_pass | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.counts.risk_pass | 0 | 0 | 6 | 0 | 0 | 1.2 | 2.6832816 | 5 |
| joint.counts.both_floors | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| shared.threshold | 0.74528599 | 0.59941219 | 0.50444153 | 0.70564 | 0.33674146 | 0.57830424 | 0.16458366 | 5 |
| shared.worst_risk | 0.60339943 | 0.68124118 | 0.35452794 | 0.65737052 | 0.83006797 | 0.62532141 | 0.17312207 | 5 |
| shared.error_minus_target | 0.50339943 | 0.58124118 | 0.25452794 | 0.55737052 | 0.73006797 | 0.52532141 | 0.17312207 | 5 |
| q0.histogram.000 | 219 | 335 | 360 | 129 | 732 | 355 | 230.28569 | 5 |
| q0.histogram.001 | 17 | 15 | 125 | 34 | 0 | 38.2 | 49.997 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 48 | 77 | 101 | 476 | 474 | 235.2 | 219.71049 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q0.counts.count_pass | 3788 | 3664 | 3926 | 5074 | 4870 | 4264.4 | 656.53545 | 5 |
| q0.counts.coverage_pass | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.counts.risk_pass | 17 | 15 | 125 | 34 | 0 | 38.2 | 49.997 | 5 |
| q0.counts.both_floors | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.minimum.threshold | 0.79779847 | 0.69796232 | 0.50546572 | 0.72209528 | 0.33674146 | 0.61201265 | 0.18784859 | 5 |
| q0.minimum.retained_n | 121 | 120 | 119 | 502 | 2501 | 672.6 | 1035.4049 | 5 |
| q0.minimum.incorrect_n | 44 | 76 | 24 | 282 | 2076 | 500.4 | 886.79017 | 5 |
| q0.minimum.coverage | 0.10202361 | 0.10118044 | 0.10033727 | 0.10335598 | 0.89321429 | 0.26002232 | 0.35396683 | 5 |
| q0.minimum.risk | 0.36363636 | 0.63333333 | 0.20168067 | 0.56175299 | 0.83006797 | 0.51809427 | 0.24315043 | 5 |
| q0.minimum.error_minus_target | 0.26363636 | 0.53333333 | 0.10168067 | 0.46175299 | 0.73006797 | 0.41809427 | 0.24315043 | 5 |
| q0.minimum.oracle_risk_gap | 0.36363636 | 0.63333333 | 0.20168067 | 0.56175299 | 0.83006797 | 0.51809427 | 0.24315043 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 411 | 328 | 508 | 1426 | 473 | 629.2 | 450.64143 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 456 | 364 | 564 | 1584 | 525 | 698.6 | 500.74924 | 5 |
| q0.oracle.maximum_coverage | 0.38448567 | 0.306914 | 0.47554806 | 0.32612724 | 0.1875 | 0.33611499 | 0.10585388 | 5 |
| q0.shared.retained_n | 179 | 298 | 123 | 590 | 2501 | 738.2 | 1001.7957 | 5 |
| q0.shared.incorrect_n | 77 | 203 | 25 | 340 | 2076 | 544.2 | 864.92352 | 5 |
| q0.shared.coverage | 0.15092749 | 0.25126476 | 0.10370995 | 0.12147416 | 0.89321429 | 0.30411813 | 0.334222 | 5 |
| q0.shared.risk | 0.4301676 | 0.68120805 | 0.20325203 | 0.57627119 | 0.83006797 | 0.54419337 | 0.2401922 | 5 |
| q1.histogram.000 | 161 | 125 | 103 | 251 | 90 | 146 | 64.567794 | 5 |
| q1.histogram.001 | 0 | 0 | 7 | 0 | 5 | 2.4 | 3.3615473 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 265 | 268 | 309 | 19 | 215 | 215.2 | 114.63071 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q1.counts.count_pass | 3863 | 3889 | 4301 | 4986 | 5507 | 4509.2 | 719.11626 | 5 |
| q1.counts.coverage_pass | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.counts.risk_pass | 0 | 0 | 7 | 0 | 5 | 2.4 | 3.3615473 | 5 |
| q1.counts.both_floors | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.minimum.threshold | 0.74528599 | 0.60407405 | 0.54230437 | 0.78649209 | 0.91455405 | 0.71854211 | 0.14825299 | 5 |
| q1.minimum.retained_n | 353 | 686 | 366 | 127 | 321 | 370.6 | 201.00323 | 5 |
| q1.minimum.incorrect_n | 213 | 466 | 120 | 80 | 100 | 195.8 | 159.40263 | 5 |
| q1.minimum.coverage | 0.11332263 | 0.22093398 | 0.10054945 | 0.1208373 | 0.10304976 | 0.13173862 | 0.050521318 | 5 |
| q1.minimum.risk | 0.60339943 | 0.67930029 | 0.32786885 | 0.62992126 | 0.31152648 | 0.51040326 | 0.17630218 | 5 |
| q1.minimum.error_minus_target | 0.50339943 | 0.57930029 | 0.22786885 | 0.52992126 | 0.21152648 | 0.41040326 | 0.17630218 | 5 |
| q1.minimum.oracle_risk_gap | 0.60339943 | 0.67930029 | 0.32786885 | 0.62992126 | 0.31152648 | 0.51040326 | 0.17630218 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 978 | 818 | 1287 | 282 | 1371 | 947.2 | 434.51203 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1086 | 908 | 1430 | 313 | 1523 | 1052 | 482.89181 | 5 |
| q1.oracle.maximum_coverage | 0.34863563 | 0.29243156 | 0.39285714 | 0.29781161 | 0.48892456 | 0.3641321 | 0.080897777 | 5 |
| q1.shared.retained_n | 353 | 709 | 519 | 251 | 2892 | 944.8 | 1102.2795 | 5 |
| q1.shared.incorrect_n | 213 | 483 | 184 | 165 | 1581 | 525.2 | 604.17812 | 5 |
| q1.shared.coverage | 0.11332263 | 0.22834138 | 0.14258242 | 0.23882017 | 0.92841091 | 0.3302955 | 0.33868047 | 5 |
| q1.shared.risk | 0.60339943 | 0.68124118 | 0.35452794 | 0.65737052 | 0.5466805 | 0.56864391 | 0.13046699 | 5 |
| question_mean.minimum.risk | 0.4835179 | 0.65631681 | 0.26477476 | 0.59583712 | 0.57079723 | 0.51424876 | 0.15265925 | 5 |
| question_mean.minimum.coverage | 0.10767312 | 0.16105721 | 0.10044336 | 0.11209664 | 0.49813202 | 0.19588047 | 0.17064376 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.4835179 | 0.65631681 | 0.26477476 | 0.59583712 | 0.57079723 | 0.51424876 | 0.15265925 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.36656065 | 0.29967278 | 0.4342026 | 0.31196942 | 0.33821228 | 0.35012355 | 0.05357789 | 5 |
| question_mean.shared.risk | 0.51678352 | 0.68122462 | 0.27888999 | 0.61682085 | 0.68837424 | 0.55641864 | 0.16972797 | 5 |
| question_mean.shared.coverage | 0.13212506 | 0.23980307 | 0.12314618 | 0.18014717 | 0.9108126 | 0.31720682 | 0.33505944 | 5 |

### explanation_only / confidence_only / 30%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 236 | 350 | 289 | 251 | 732 | 371.6 | 206.22148 | 5 |
| joint.histogram.001 | 0 | 0 | 196 | 0 | 0 | 39.2 | 87.653865 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 190 | 77 | 101 | 388 | 474 | 246 | 176.68475 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| joint.counts.count_pass | 3788 | 3664 | 3926 | 4986 | 4870 | 4246.8 | 630.05174 | 5 |
| joint.counts.coverage_pass | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.counts.risk_pass | 0 | 0 | 196 | 0 | 0 | 39.2 | 87.653865 | 5 |
| joint.counts.both_floors | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3598 | 3587 | 3825 | 4598 | 4396 | 4000.8 | 468.29873 | 5 |
| shared.threshold | 0.74528599 | 0.59941219 | 0.50444153 | 0.70564 | 0.33674146 | 0.57830424 | 0.16458366 | 5 |
| shared.worst_risk | 0.60339943 | 0.68124118 | 0.35452794 | 0.65737052 | 0.83006797 | 0.62532141 | 0.17312207 | 5 |
| shared.error_minus_target | 0.30339943 | 0.38124118 | 0.054527938 | 0.35737052 | 0.53006797 | 0.32532141 | 0.17312207 | 5 |
| q0.histogram.000 | 64 | 335 | 2 | 74 | 732 | 241.4 | 302.59511 | 5 |
| q0.histogram.001 | 172 | 15 | 483 | 89 | 0 | 151.8 | 197.35932 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 48 | 77 | 0 | 476 | 474 | 215 | 238.93514 | 5 |
| q0.histogram.101 | 0 | 0 | 101 | 0 | 0 | 20.2 | 45.168573 | 5 |
| q0.histogram.110 | 3740 | 3587 | 2975 | 4598 | 4396 | 3859.2 | 652.70414 | 5 |
| q0.histogram.111 | 0 | 0 | 850 | 0 | 0 | 170 | 380.13156 | 5 |
| q0.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q0.counts.count_pass | 3788 | 3664 | 3926 | 5074 | 4870 | 4264.4 | 656.53545 | 5 |
| q0.counts.coverage_pass | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.counts.risk_pass | 172 | 15 | 1434 | 89 | 0 | 342 | 614.26094 | 5 |
| q0.counts.both_floors | 3740 | 3587 | 3825 | 4598 | 4396 | 4029.2 | 441.29095 | 5 |
| q0.counts.all_three | 0 | 0 | 850 | 0 | 0 | 170 | 380.13156 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 101 | 0 | 0 | 20.2 | 45.168573 | 5 |
| q0.counts.risk_only_failure | 3740 | 3587 | 2975 | 4598 | 4396 | 3859.2 | 652.70414 | 5 |
| q0.minimum.threshold | 0.79779847 | 0.69796232 | 0.50546572 | 0.72209528 | 0.33674146 | 0.61201265 | 0.18784859 | 5 |
| q0.minimum.retained_n | 121 | 120 | 119 | 502 | 2501 | 672.6 | 1035.4049 | 5 |
| q0.minimum.incorrect_n | 44 | 76 | 24 | 282 | 2076 | 500.4 | 886.79017 | 5 |
| q0.minimum.coverage | 0.10202361 | 0.10118044 | 0.10033727 | 0.10335598 | 0.89321429 | 0.26002232 | 0.35396683 | 5 |
| q0.minimum.risk | 0.36363636 | 0.63333333 | 0.20168067 | 0.56175299 | 0.83006797 | 0.51809427 | 0.24315043 | 5 |
| q0.minimum.error_minus_target | 0.063636364 | 0.33333333 | -0.098319328 | 0.26175299 | 0.53006797 | 0.21809427 | 0.24315043 | 5 |
| q0.minimum.oracle_risk_gap | 0.36363636 | 0.63333333 | 0.20168067 | 0.56175299 | 0.83006797 | 0.51809427 | 0.24315043 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 411 | 328 | 508 | 1426 | 473 | 629.2 | 450.64143 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 587 | 468 | 725 | 2037 | 675 | 898.4 | 643.93307 | 5 |
| q0.oracle.maximum_coverage | 0.49494098 | 0.39460371 | 0.61129848 | 0.41939469 | 0.24107143 | 0.43226186 | 0.13612519 | 5 |
| q0.shared.retained_n | 179 | 298 | 123 | 590 | 2501 | 738.2 | 1001.7957 | 5 |
| q0.shared.incorrect_n | 77 | 203 | 25 | 340 | 2076 | 544.2 | 864.92352 | 5 |
| q0.shared.coverage | 0.15092749 | 0.25126476 | 0.10370995 | 0.12147416 | 0.89321429 | 0.30411813 | 0.334222 | 5 |
| q0.shared.risk | 0.4301676 | 0.68120805 | 0.20325203 | 0.57627119 | 0.83006797 | 0.54419337 | 0.2401922 | 5 |
| q1.histogram.000 | 161 | 125 | 4 | 251 | 0 | 108.2 | 107.26929 | 5 |
| q1.histogram.001 | 0 | 0 | 106 | 0 | 95 | 40.2 | 55.183331 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 265 | 268 | 218 | 19 | 73 | 168.6 | 115.2532 | 5 |
| q1.histogram.101 | 0 | 0 | 91 | 0 | 142 | 46.6 | 66.308371 | 5 |
| q1.histogram.110 | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q1.counts.count_pass | 3863 | 3889 | 4301 | 4986 | 5507 | 4509.2 | 719.11626 | 5 |
| q1.counts.coverage_pass | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.counts.risk_pass | 0 | 0 | 197 | 0 | 237 | 86.8 | 119.69419 | 5 |
| q1.counts.both_floors | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 91 | 0 | 142 | 46.6 | 66.308371 | 5 |
| q1.counts.risk_only_failure | 3598 | 3621 | 3992 | 4967 | 5292 | 4294 | 787.00095 | 5 |
| q1.minimum.threshold | 0.74528599 | 0.60407405 | 0.54230437 | 0.78649209 | 0.91455405 | 0.71854211 | 0.14825299 | 5 |
| q1.minimum.retained_n | 353 | 686 | 366 | 127 | 321 | 370.6 | 201.00323 | 5 |
| q1.minimum.incorrect_n | 213 | 466 | 120 | 80 | 100 | 195.8 | 159.40263 | 5 |
| q1.minimum.coverage | 0.11332263 | 0.22093398 | 0.10054945 | 0.1208373 | 0.10304976 | 0.13173862 | 0.050521318 | 5 |
| q1.minimum.risk | 0.60339943 | 0.67930029 | 0.32786885 | 0.62992126 | 0.31152648 | 0.51040326 | 0.17630218 | 5 |
| q1.minimum.error_minus_target | 0.30339943 | 0.37930029 | 0.027868852 | 0.32992126 | 0.01152648 | 0.21040326 | 0.17630218 | 5 |
| q1.minimum.oracle_risk_gap | 0.60339943 | 0.67930029 | 0.32786885 | 0.62992126 | 0.31152648 | 0.51040326 | 0.17630218 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 978 | 818 | 1287 | 282 | 1371 | 947.2 | 434.51203 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1397 | 1168 | 1838 | 402 | 1958 | 1352.6 | 620.84845 | 5 |
| q1.oracle.maximum_coverage | 0.44847512 | 0.37616747 | 0.50494505 | 0.38249286 | 0.62857143 | 0.46813039 | 0.10401195 | 5 |
| q1.shared.retained_n | 353 | 709 | 519 | 251 | 2892 | 944.8 | 1102.2795 | 5 |
| q1.shared.incorrect_n | 213 | 483 | 184 | 165 | 1581 | 525.2 | 604.17812 | 5 |
| q1.shared.coverage | 0.11332263 | 0.22834138 | 0.14258242 | 0.23882017 | 0.92841091 | 0.3302955 | 0.33868047 | 5 |
| q1.shared.risk | 0.60339943 | 0.68124118 | 0.35452794 | 0.65737052 | 0.5466805 | 0.56864391 | 0.13046699 | 5 |
| question_mean.minimum.risk | 0.4835179 | 0.65631681 | 0.26477476 | 0.59583712 | 0.57079723 | 0.51424876 | 0.15265925 | 5 |
| question_mean.minimum.coverage | 0.10767312 | 0.16105721 | 0.10044336 | 0.11209664 | 0.49813202 | 0.19588047 | 0.17064376 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.4835179 | 0.65631681 | 0.26477476 | 0.59583712 | 0.57079723 | 0.51424876 | 0.15265925 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.47170805 | 0.38538559 | 0.55812177 | 0.40094378 | 0.43482143 | 0.45019612 | 0.068871779 | 5 |
| question_mean.shared.risk | 0.51678352 | 0.68122462 | 0.27888999 | 0.61682085 | 0.68837424 | 0.55641864 | 0.16972797 | 5 |
| question_mean.shared.coverage | 0.13212506 | 0.23980307 | 0.12314618 | 0.18014717 | 0.9108126 | 0.31720682 | 0.33505944 | 5 |

### explanation_only / support_aware / 20%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 259 | 478 | 325 | 325 | 1276 | 532.6 | 423.28395 | 5 |
| joint.histogram.001 | 0 | 0 | 145 | 27 | 0 | 34.4 | 62.922969 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 148 | 48 | 113 | 240 | 383 | 186.4 | 129.94345 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| joint.counts.count_pass | 3765 | 3536 | 3941 | 4885 | 4326 | 4090.6 | 529.73135 | 5 |
| joint.counts.coverage_pass | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.counts.risk_pass | 0 | 0 | 145 | 27 | 0 | 34.4 | 62.922969 | 5 |
| joint.counts.both_floors | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| shared.threshold | 0.72561415 | 0.60407405 | 0.49292577 | 0.64106635 | 0.56131972 | 0.60500001 | 0.087060343 | 5 |
| shared.worst_risk | 0.57006369 | 0.66262976 | 0.33531746 | 0.62 | 0.71104816 | 0.57981181 | 0.14626123 | 5 |
| shared.error_minus_target | 0.37006369 | 0.46262976 | 0.13531746 | 0.42 | 0.51104816 | 0.37981181 | 0.14626123 | 5 |
| q0.histogram.000 | 169 | 459 | 1 | 72 | 1276 | 395.4 | 522.23012 | 5 |
| q0.histogram.001 | 90 | 19 | 469 | 42 | 0 | 124 | 195.77155 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 66 | 48 | 0 | 478 | 383 | 195 | 218.92236 | 5 |
| q0.histogram.101 | 0 | 0 | 113 | 0 | 0 | 22.6 | 50.535136 | 5 |
| q0.histogram.110 | 3699 | 3488 | 3692 | 4645 | 3943 | 3893.4 | 450.01811 | 5 |
| q0.histogram.111 | 0 | 0 | 136 | 0 | 0 | 27.2 | 60.821049 | 5 |
| q0.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q0.counts.count_pass | 3765 | 3536 | 3941 | 5123 | 4326 | 4138.2 | 621.67331 | 5 |
| q0.counts.coverage_pass | 3699 | 3488 | 3828 | 4645 | 3943 | 3920.6 | 438.77135 | 5 |
| q0.counts.risk_pass | 90 | 19 | 718 | 42 | 0 | 173.8 | 306.07058 | 5 |
| q0.counts.both_floors | 3699 | 3488 | 3828 | 4645 | 3943 | 3920.6 | 438.77135 | 5 |
| q0.counts.all_three | 0 | 0 | 136 | 0 | 0 | 27.2 | 60.821049 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 113 | 0 | 0 | 22.6 | 50.535136 | 5 |
| q0.counts.risk_only_failure | 3699 | 3488 | 3692 | 4645 | 3943 | 3893.4 | 450.01811 | 5 |
| q0.minimum.threshold | 0.74565926 | 0.64232547 | 0.49287166 | 0.67427963 | 0.56131972 | 0.62329115 | 0.098470536 | 5 |
| q0.minimum.retained_n | 124 | 120 | 120 | 521 | 353 | 247.6 | 182.82314 | 5 |
| q0.minimum.incorrect_n | 40 | 73 | 18 | 261 | 251 | 128.6 | 117.98856 | 5 |
| q0.minimum.coverage | 0.10455312 | 0.10118044 | 0.10118044 | 0.10726786 | 0.12607143 | 0.10805066 | 0.010392227 | 5 |
| q0.minimum.risk | 0.32258065 | 0.60833333 | 0.15 | 0.50095969 | 0.71104816 | 0.45858437 | 0.22454382 | 5 |
| q0.minimum.error_minus_target | 0.12258065 | 0.40833333 | -0.05 | 0.30095969 | 0.51104816 | 0.25858437 | 0.22454382 | 5 |
| q0.minimum.oracle_risk_gap | 0.32258065 | 0.60833333 | 0.15 | 0.50095969 | 0.71104816 | 0.45858437 | 0.22454382 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 411 | 328 | 508 | 1426 | 473 | 629.2 | 450.64143 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 513 | 410 | 635 | 1782 | 591 | 786.2 | 563.19331 | 5 |
| q0.oracle.maximum_coverage | 0.43254637 | 0.34569983 | 0.53541315 | 0.36689314 | 0.21107143 | 0.37832479 | 0.11914853 | 5 |
| q0.shared.retained_n | 142 | 187 | 119 | 711 | 353 | 302.4 | 246.06666 | 5 |
| q0.shared.incorrect_n | 49 | 120 | 18 | 385 | 251 | 164.6 | 152.38537 | 5 |
| q0.shared.coverage | 0.11973019 | 0.15767285 | 0.10033727 | 0.14638666 | 0.12607143 | 0.13003968 | 0.02255594 | 5 |
| q0.shared.risk | 0.34507042 | 0.64171123 | 0.1512605 | 0.54149086 | 0.71104816 | 0.47811623 | 0.22889561 | 5 |
| q1.histogram.000 | 155 | 105 | 0 | 317 | 8 | 117 | 129.5743 | 5 |
| q1.histogram.001 | 0 | 0 | 113 | 35 | 86 | 46.8 | 51.085223 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 252 | 245 | 286 | 11 | 203 | 199.4 | 109.37687 | 5 |
| q1.histogram.101 | 0 | 0 | 33 | 0 | 0 | 6.6 | 14.758049 | 5 |
| q1.histogram.110 | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q1.counts.count_pass | 3869 | 3909 | 4298 | 4885 | 5508 | 4493.8 | 698.6313 | 5 |
| q1.counts.coverage_pass | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.counts.risk_pass | 0 | 0 | 146 | 35 | 86 | 53.4 | 62.608306 | 5 |
| q1.counts.both_floors | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 33 | 0 | 0 | 6.6 | 14.758049 | 5 |
| q1.counts.risk_only_failure | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.minimum.threshold | 0.72561415 | 0.60407405 | 0.52543932 | 0.64106635 | 0.91455405 | 0.68214958 | 0.14852839 | 5 |
| q1.minimum.retained_n | 314 | 578 | 365 | 250 | 318 | 365 | 125.90075 | 5 |
| q1.minimum.incorrect_n | 179 | 383 | 113 | 155 | 97 | 185.4 | 115.1816 | 5 |
| q1.minimum.coverage | 0.10080257 | 0.18615137 | 0.10027473 | 0.2378687 | 0.10208668 | 0.14543681 | 0.063467299 | 5 |
| q1.minimum.risk | 0.57006369 | 0.66262976 | 0.30958904 | 0.62 | 0.30503145 | 0.49346279 | 0.17306989 | 5 |
| q1.minimum.error_minus_target | 0.37006369 | 0.46262976 | 0.10958904 | 0.42 | 0.10503145 | 0.29346279 | 0.17306989 | 5 |
| q1.minimum.oracle_risk_gap | 0.57006369 | 0.66262976 | 0.30958904 | 0.62 | 0.30503145 | 0.49346279 | 0.17306989 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 978 | 818 | 1287 | 282 | 1371 | 947.2 | 434.51203 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1222 | 1022 | 1608 | 352 | 1713 | 1183.4 | 543.0302 | 5 |
| q1.oracle.maximum_coverage | 0.39229535 | 0.32914654 | 0.44175824 | 0.33491912 | 0.54991974 | 0.4096078 | 0.090930229 | 5 |
| q1.shared.retained_n | 314 | 578 | 504 | 250 | 1555 | 640.2 | 528.6636 | 5 |
| q1.shared.incorrect_n | 179 | 383 | 169 | 155 | 691 | 315.4 | 229.89737 | 5 |
| q1.shared.coverage | 0.10080257 | 0.18615137 | 0.13846154 | 0.2378687 | 0.49919743 | 0.23249632 | 0.15771175 | 5 |
| q1.shared.risk | 0.57006369 | 0.66262976 | 0.33531746 | 0.62 | 0.44437299 | 0.52647678 | 0.13459844 | 5 |
| question_mean.minimum.risk | 0.44632217 | 0.63548155 | 0.22979452 | 0.56047985 | 0.5080398 | 0.47602358 | 0.15418793 | 5 |
| question_mean.minimum.coverage | 0.10267784 | 0.1436659 | 0.10072758 | 0.17256828 | 0.11407905 | 0.12674373 | 0.030832816 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.44632217 | 0.63548155 | 0.22979452 | 0.56047985 | 0.5080398 | 0.47602358 | 0.15418793 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.41242086 | 0.33742318 | 0.4885857 | 0.35090613 | 0.38049559 | 0.39396629 | 0.060262267 | 5 |
| question_mean.shared.risk | 0.45756706 | 0.65217049 | 0.24328898 | 0.58074543 | 0.57771057 | 0.50229651 | 0.16077107 | 5 |
| question_mean.shared.coverage | 0.11026638 | 0.17191211 | 0.1193994 | 0.19212768 | 0.31263443 | 0.181268 | 0.081135008 | 5 |

### explanation_only / support_aware / 10%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 259 | 478 | 401 | 352 | 1276 | 553.2 | 411.79327 | 5 |
| joint.histogram.001 | 0 | 0 | 69 | 0 | 0 | 13.8 | 30.857738 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 148 | 48 | 113 | 240 | 383 | 186.4 | 129.94345 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| joint.counts.count_pass | 3765 | 3536 | 3941 | 4885 | 4326 | 4090.6 | 529.73135 | 5 |
| joint.counts.coverage_pass | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.counts.risk_pass | 0 | 0 | 69 | 0 | 0 | 13.8 | 30.857738 | 5 |
| joint.counts.both_floors | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| shared.threshold | 0.72561415 | 0.60407405 | 0.49292577 | 0.64106635 | 0.56131972 | 0.60500001 | 0.087060343 | 5 |
| shared.worst_risk | 0.57006369 | 0.66262976 | 0.33531746 | 0.62 | 0.71104816 | 0.57981181 | 0.14626123 | 5 |
| shared.error_minus_target | 0.47006369 | 0.56262976 | 0.23531746 | 0.52 | 0.61104816 | 0.47981181 | 0.14626123 | 5 |
| q0.histogram.000 | 202 | 459 | 177 | 105 | 1276 | 443.8 | 484.05134 | 5 |
| q0.histogram.001 | 57 | 19 | 293 | 9 | 0 | 75.6 | 123.45364 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 66 | 48 | 113 | 478 | 383 | 217.6 | 198.65372 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 3699 | 3488 | 3828 | 4645 | 3943 | 3920.6 | 438.77135 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q0.counts.count_pass | 3765 | 3536 | 3941 | 5123 | 4326 | 4138.2 | 621.67331 | 5 |
| q0.counts.coverage_pass | 3699 | 3488 | 3828 | 4645 | 3943 | 3920.6 | 438.77135 | 5 |
| q0.counts.risk_pass | 57 | 19 | 293 | 9 | 0 | 75.6 | 123.45364 | 5 |
| q0.counts.both_floors | 3699 | 3488 | 3828 | 4645 | 3943 | 3920.6 | 438.77135 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 3699 | 3488 | 3828 | 4645 | 3943 | 3920.6 | 438.77135 | 5 |
| q0.minimum.threshold | 0.74565926 | 0.64232547 | 0.49287166 | 0.67427963 | 0.56131972 | 0.62329115 | 0.098470536 | 5 |
| q0.minimum.retained_n | 124 | 120 | 120 | 521 | 353 | 247.6 | 182.82314 | 5 |
| q0.minimum.incorrect_n | 40 | 73 | 18 | 261 | 251 | 128.6 | 117.98856 | 5 |
| q0.minimum.coverage | 0.10455312 | 0.10118044 | 0.10118044 | 0.10726786 | 0.12607143 | 0.10805066 | 0.010392227 | 5 |
| q0.minimum.risk | 0.32258065 | 0.60833333 | 0.15 | 0.50095969 | 0.71104816 | 0.45858437 | 0.22454382 | 5 |
| q0.minimum.error_minus_target | 0.22258065 | 0.50833333 | 0.05 | 0.40095969 | 0.61104816 | 0.35858437 | 0.22454382 | 5 |
| q0.minimum.oracle_risk_gap | 0.32258065 | 0.60833333 | 0.15 | 0.50095969 | 0.71104816 | 0.45858437 | 0.22454382 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 411 | 328 | 508 | 1426 | 473 | 629.2 | 450.64143 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 456 | 364 | 564 | 1584 | 525 | 698.6 | 500.74924 | 5 |
| q0.oracle.maximum_coverage | 0.38448567 | 0.306914 | 0.47554806 | 0.32612724 | 0.1875 | 0.33611499 | 0.10585388 | 5 |
| q0.shared.retained_n | 142 | 187 | 119 | 711 | 353 | 302.4 | 246.06666 | 5 |
| q0.shared.incorrect_n | 49 | 120 | 18 | 385 | 251 | 164.6 | 152.38537 | 5 |
| q0.shared.coverage | 0.11973019 | 0.15767285 | 0.10033727 | 0.14638666 | 0.12607143 | 0.13003968 | 0.02255594 | 5 |
| q0.shared.risk | 0.34507042 | 0.64171123 | 0.1512605 | 0.54149086 | 0.71104816 | 0.47811623 | 0.22889561 | 5 |
| q1.histogram.000 | 155 | 105 | 43 | 318 | 89 | 142 | 106.21205 | 5 |
| q1.histogram.001 | 0 | 0 | 70 | 34 | 5 | 21.8 | 30.433534 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 252 | 245 | 319 | 11 | 203 | 206 | 116.6619 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q1.counts.count_pass | 3869 | 3909 | 4298 | 4885 | 5508 | 4493.8 | 698.6313 | 5 |
| q1.counts.coverage_pass | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.counts.risk_pass | 0 | 0 | 70 | 34 | 5 | 21.8 | 30.433534 | 5 |
| q1.counts.both_floors | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.minimum.threshold | 0.72561415 | 0.60407405 | 0.52543932 | 0.64106635 | 0.91455405 | 0.68214958 | 0.14852839 | 5 |
| q1.minimum.retained_n | 314 | 578 | 365 | 250 | 318 | 365 | 125.90075 | 5 |
| q1.minimum.incorrect_n | 179 | 383 | 113 | 155 | 97 | 185.4 | 115.1816 | 5 |
| q1.minimum.coverage | 0.10080257 | 0.18615137 | 0.10027473 | 0.2378687 | 0.10208668 | 0.14543681 | 0.063467299 | 5 |
| q1.minimum.risk | 0.57006369 | 0.66262976 | 0.30958904 | 0.62 | 0.30503145 | 0.49346279 | 0.17306989 | 5 |
| q1.minimum.error_minus_target | 0.47006369 | 0.56262976 | 0.20958904 | 0.52 | 0.20503145 | 0.39346279 | 0.17306989 | 5 |
| q1.minimum.oracle_risk_gap | 0.57006369 | 0.66262976 | 0.30958904 | 0.62 | 0.30503145 | 0.49346279 | 0.17306989 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 978 | 818 | 1287 | 282 | 1371 | 947.2 | 434.51203 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1086 | 908 | 1430 | 313 | 1523 | 1052 | 482.89181 | 5 |
| q1.oracle.maximum_coverage | 0.34863563 | 0.29243156 | 0.39285714 | 0.29781161 | 0.48892456 | 0.3641321 | 0.080897777 | 5 |
| q1.shared.retained_n | 314 | 578 | 504 | 250 | 1555 | 640.2 | 528.6636 | 5 |
| q1.shared.incorrect_n | 179 | 383 | 169 | 155 | 691 | 315.4 | 229.89737 | 5 |
| q1.shared.coverage | 0.10080257 | 0.18615137 | 0.13846154 | 0.2378687 | 0.49919743 | 0.23249632 | 0.15771175 | 5 |
| q1.shared.risk | 0.57006369 | 0.66262976 | 0.33531746 | 0.62 | 0.44437299 | 0.52647678 | 0.13459844 | 5 |
| question_mean.minimum.risk | 0.44632217 | 0.63548155 | 0.22979452 | 0.56047985 | 0.5080398 | 0.47602358 | 0.15418793 | 5 |
| question_mean.minimum.coverage | 0.10267784 | 0.1436659 | 0.10072758 | 0.17256828 | 0.11407905 | 0.12674373 | 0.030832816 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.44632217 | 0.63548155 | 0.22979452 | 0.56047985 | 0.5080398 | 0.47602358 | 0.15418793 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.36656065 | 0.29967278 | 0.4342026 | 0.31196942 | 0.33821228 | 0.35012355 | 0.05357789 | 5 |
| question_mean.shared.risk | 0.45756706 | 0.65217049 | 0.24328898 | 0.58074543 | 0.57771057 | 0.50229651 | 0.16077107 | 5 |
| question_mean.shared.coverage | 0.11026638 | 0.17191211 | 0.1193994 | 0.19212768 | 0.31263443 | 0.181268 | 0.081135008 | 5 |

### explanation_only / support_aware / 30%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 259 | 478 | 89 | 307 | 1276 | 481.8 | 465.09537 | 5 |
| joint.histogram.001 | 0 | 0 | 381 | 45 | 0 | 85.2 | 166.50135 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 148 | 48 | 113 | 240 | 383 | 186.4 | 129.94345 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| joint.counts.count_pass | 3765 | 3536 | 3941 | 4885 | 4326 | 4090.6 | 529.73135 | 5 |
| joint.counts.coverage_pass | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.counts.risk_pass | 0 | 0 | 381 | 45 | 0 | 85.2 | 166.50135 | 5 |
| joint.counts.both_floors | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3617 | 3488 | 3828 | 4645 | 3943 | 3904.2 | 450.5005 | 5 |
| shared.threshold | 0.72561415 | 0.60407405 | 0.49292577 | 0.64106635 | 0.56131972 | 0.60500001 | 0.087060343 | 5 |
| shared.worst_risk | 0.57006369 | 0.66262976 | 0.33531746 | 0.62 | 0.71104816 | 0.57981181 | 0.14626123 | 5 |
| shared.error_minus_target | 0.27006369 | 0.36262976 | 0.03531746 | 0.32 | 0.41104816 | 0.27981181 | 0.14626123 | 5 |
| q0.histogram.000 | 7 | 459 | 1 | 29 | 1276 | 354.4 | 550.39786 | 5 |
| q0.histogram.001 | 252 | 19 | 469 | 85 | 0 | 165 | 196.8032 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 66 | 48 | 0 | 478 | 383 | 195 | 218.92236 | 5 |
| q0.histogram.101 | 0 | 0 | 113 | 0 | 0 | 22.6 | 50.535136 | 5 |
| q0.histogram.110 | 3699 | 3488 | 2756 | 4645 | 3943 | 3706.2 | 687.01579 | 5 |
| q0.histogram.111 | 0 | 0 | 1072 | 0 | 0 | 214.4 | 479.41297 | 5 |
| q0.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q0.counts.count_pass | 3765 | 3536 | 3941 | 5123 | 4326 | 4138.2 | 621.67331 | 5 |
| q0.counts.coverage_pass | 3699 | 3488 | 3828 | 4645 | 3943 | 3920.6 | 438.77135 | 5 |
| q0.counts.risk_pass | 252 | 19 | 1654 | 85 | 0 | 402 | 706.89214 | 5 |
| q0.counts.both_floors | 3699 | 3488 | 3828 | 4645 | 3943 | 3920.6 | 438.77135 | 5 |
| q0.counts.all_three | 0 | 0 | 1072 | 0 | 0 | 214.4 | 479.41297 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 113 | 0 | 0 | 22.6 | 50.535136 | 5 |
| q0.counts.risk_only_failure | 3699 | 3488 | 2756 | 4645 | 3943 | 3706.2 | 687.01579 | 5 |
| q0.minimum.threshold | 0.74565926 | 0.64232547 | 0.49287166 | 0.67427963 | 0.56131972 | 0.62329115 | 0.098470536 | 5 |
| q0.minimum.retained_n | 124 | 120 | 120 | 521 | 353 | 247.6 | 182.82314 | 5 |
| q0.minimum.incorrect_n | 40 | 73 | 18 | 261 | 251 | 128.6 | 117.98856 | 5 |
| q0.minimum.coverage | 0.10455312 | 0.10118044 | 0.10118044 | 0.10726786 | 0.12607143 | 0.10805066 | 0.010392227 | 5 |
| q0.minimum.risk | 0.32258065 | 0.60833333 | 0.15 | 0.50095969 | 0.71104816 | 0.45858437 | 0.22454382 | 5 |
| q0.minimum.error_minus_target | 0.022580645 | 0.30833333 | -0.15 | 0.20095969 | 0.41104816 | 0.15858437 | 0.22454382 | 5 |
| q0.minimum.oracle_risk_gap | 0.32258065 | 0.60833333 | 0.15 | 0.50095969 | 0.71104816 | 0.45858437 | 0.22454382 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 411 | 328 | 508 | 1426 | 473 | 629.2 | 450.64143 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 587 | 468 | 725 | 2037 | 675 | 898.4 | 643.93307 | 5 |
| q0.oracle.maximum_coverage | 0.49494098 | 0.39460371 | 0.61129848 | 0.41939469 | 0.24107143 | 0.43226186 | 0.13612519 | 5 |
| q0.shared.retained_n | 142 | 187 | 119 | 711 | 353 | 302.4 | 246.06666 | 5 |
| q0.shared.incorrect_n | 49 | 120 | 18 | 385 | 251 | 164.6 | 152.38537 | 5 |
| q0.shared.coverage | 0.11973019 | 0.15767285 | 0.10033727 | 0.14638666 | 0.12607143 | 0.13003968 | 0.02255594 | 5 |
| q0.shared.risk | 0.34507042 | 0.64171123 | 0.1512605 | 0.54149086 | 0.71104816 | 0.47811623 | 0.22889561 | 5 |
| q1.histogram.000 | 155 | 105 | 0 | 307 | 0 | 113.4 | 127.47666 | 5 |
| q1.histogram.001 | 0 | 0 | 113 | 45 | 94 | 50.4 | 52.271407 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 252 | 245 | 50 | 11 | 46 | 120.8 | 117.58274 | 5 |
| q1.histogram.101 | 0 | 0 | 269 | 0 | 157 | 85.2 | 123.20187 | 5 |
| q1.histogram.110 | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4024 | 4014 | 4411 | 5237 | 5602 | 4657.6 | 725.27188 | 5 |
| q1.counts.count_pass | 3869 | 3909 | 4298 | 4885 | 5508 | 4493.8 | 698.6313 | 5 |
| q1.counts.coverage_pass | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.counts.risk_pass | 0 | 0 | 382 | 45 | 251 | 135.6 | 172.49145 | 5 |
| q1.counts.both_floors | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 269 | 0 | 157 | 85.2 | 123.20187 | 5 |
| q1.counts.risk_only_failure | 3617 | 3664 | 3979 | 4874 | 5305 | 4287.8 | 760.39181 | 5 |
| q1.minimum.threshold | 0.72561415 | 0.60407405 | 0.52543932 | 0.64106635 | 0.91455405 | 0.68214958 | 0.14852839 | 5 |
| q1.minimum.retained_n | 314 | 578 | 365 | 250 | 318 | 365 | 125.90075 | 5 |
| q1.minimum.incorrect_n | 179 | 383 | 113 | 155 | 97 | 185.4 | 115.1816 | 5 |
| q1.minimum.coverage | 0.10080257 | 0.18615137 | 0.10027473 | 0.2378687 | 0.10208668 | 0.14543681 | 0.063467299 | 5 |
| q1.minimum.risk | 0.57006369 | 0.66262976 | 0.30958904 | 0.62 | 0.30503145 | 0.49346279 | 0.17306989 | 5 |
| q1.minimum.error_minus_target | 0.27006369 | 0.36262976 | 0.0095890411 | 0.32 | 0.0050314465 | 0.19346279 | 0.17306989 | 5 |
| q1.minimum.oracle_risk_gap | 0.57006369 | 0.66262976 | 0.30958904 | 0.62 | 0.30503145 | 0.49346279 | 0.17306989 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 978 | 818 | 1287 | 282 | 1371 | 947.2 | 434.51203 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1397 | 1168 | 1838 | 402 | 1958 | 1352.6 | 620.84845 | 5 |
| q1.oracle.maximum_coverage | 0.44847512 | 0.37616747 | 0.50494505 | 0.38249286 | 0.62857143 | 0.46813039 | 0.10401195 | 5 |
| q1.shared.retained_n | 314 | 578 | 504 | 250 | 1555 | 640.2 | 528.6636 | 5 |
| q1.shared.incorrect_n | 179 | 383 | 169 | 155 | 691 | 315.4 | 229.89737 | 5 |
| q1.shared.coverage | 0.10080257 | 0.18615137 | 0.13846154 | 0.2378687 | 0.49919743 | 0.23249632 | 0.15771175 | 5 |
| q1.shared.risk | 0.57006369 | 0.66262976 | 0.33531746 | 0.62 | 0.44437299 | 0.52647678 | 0.13459844 | 5 |
| question_mean.minimum.risk | 0.44632217 | 0.63548155 | 0.22979452 | 0.56047985 | 0.5080398 | 0.47602358 | 0.15418793 | 5 |
| question_mean.minimum.coverage | 0.10267784 | 0.1436659 | 0.10072758 | 0.17256828 | 0.11407905 | 0.12674373 | 0.030832816 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.44632217 | 0.63548155 | 0.22979452 | 0.56047985 | 0.5080398 | 0.47602358 | 0.15418793 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.47170805 | 0.38538559 | 0.55812177 | 0.40094378 | 0.43482143 | 0.45019612 | 0.068871779 | 5 |
| question_mean.shared.risk | 0.45756706 | 0.65217049 | 0.24328898 | 0.58074543 | 0.57771057 | 0.50229651 | 0.16077107 | 5 |
| question_mean.shared.coverage | 0.11026638 | 0.17191211 | 0.1193994 | 0.19212768 | 0.31263443 | 0.181268 | 0.081135008 | 5 |

### explanation_only / frequency / 20%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| shared.worst_risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| shared.error_minus_target | 0.49139966 | 0.49139966 | 0.49139966 | 0.44607783 | 0.43785714 | 0.47162679 | 0.027230673 | 5 |
| q0.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.minimum.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.minimum.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.minimum.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.minimum.error_minus_target | 0.49139966 | 0.49139966 | 0.49139966 | 0.44607783 | 0.43785714 | 0.47162679 | 0.027230673 | 5 |
| q0.minimum.oracle_risk_gap | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 366 | 366 | 366 | 1719 | 1014 | 766.2 | 602.0201 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 457 | 457 | 457 | 2148 | 1267 | 957.2 | 752.42621 | 5 |
| q0.oracle.maximum_coverage | 0.38532884 | 0.38532884 | 0.38532884 | 0.4422483 | 0.4525 | 0.41014696 | 0.034176358 | 5 |
| q0.shared.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.shared.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.shared.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q1.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.minimum.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.minimum.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.minimum.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.minimum.error_minus_target | 0.34895666 | 0.40225443 | 0.48681319 | 0.39372027 | 0.34895666 | 0.39614024 | 0.056385732 | 5 |
| q1.minimum.oracle_risk_gap | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1405 | 1235 | 1140 | 427 | 1405 | 1122.4 | 405.06024 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1756 | 1543 | 1425 | 533 | 1756 | 1402.6 | 506.50795 | 5 |
| q1.oracle.maximum_coverage | 0.56372392 | 0.49694042 | 0.39148352 | 0.50713606 | 0.56372392 | 0.50460157 | 0.070448056 | 5 |
| q1.shared.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.shared.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.shared.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| question_mean.minimum.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.47452638 | 0.44113463 | 0.38840618 | 0.47469218 | 0.50811196 | 0.45737426 | 0.045245833 | 5 |
| question_mean.shared.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |

### explanation_only / frequency / 10%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| shared.worst_risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| shared.error_minus_target | 0.59139966 | 0.59139966 | 0.59139966 | 0.54607783 | 0.53785714 | 0.57162679 | 0.027230673 | 5 |
| q0.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.minimum.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.minimum.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.minimum.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.minimum.error_minus_target | 0.59139966 | 0.59139966 | 0.59139966 | 0.54607783 | 0.53785714 | 0.57162679 | 0.027230673 | 5 |
| q0.minimum.oracle_risk_gap | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 366 | 366 | 366 | 1719 | 1014 | 766.2 | 602.0201 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 406 | 406 | 406 | 1910 | 1126 | 850.8 | 669.17501 | 5 |
| q0.oracle.maximum_coverage | 0.34232715 | 0.34232715 | 0.34232715 | 0.39324686 | 0.40214286 | 0.36447423 | 0.030488806 | 5 |
| q0.shared.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.shared.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.shared.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q1.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.minimum.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.minimum.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.minimum.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.minimum.error_minus_target | 0.44895666 | 0.50225443 | 0.58681319 | 0.49372027 | 0.44895666 | 0.49614024 | 0.056385732 | 5 |
| q1.minimum.oracle_risk_gap | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1405 | 1235 | 1140 | 427 | 1405 | 1122.4 | 405.06024 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1561 | 1372 | 1266 | 474 | 1561 | 1246.8 | 450.19629 | 5 |
| q1.oracle.maximum_coverage | 0.5011236 | 0.44186795 | 0.3478022 | 0.45099905 | 0.5011236 | 0.44858328 | 0.062707112 | 5 |
| q1.shared.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.shared.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.shared.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| question_mean.minimum.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.42172537 | 0.39209755 | 0.34506467 | 0.42212295 | 0.45163323 | 0.40652876 | 0.04029461 | 5 |
| question_mean.shared.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |

### explanation_only / frequency / 30%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| shared.worst_risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| shared.error_minus_target | 0.39139966 | 0.39139966 | 0.39139966 | 0.34607783 | 0.33785714 | 0.37162679 | 0.027230673 | 5 |
| q0.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.minimum.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.minimum.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.minimum.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.minimum.error_minus_target | 0.39139966 | 0.39139966 | 0.39139966 | 0.34607783 | 0.33785714 | 0.37162679 | 0.027230673 | 5 |
| q0.minimum.oracle_risk_gap | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 366 | 366 | 366 | 1719 | 1014 | 766.2 | 602.0201 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 522 | 522 | 522 | 2455 | 1448 | 1093.8 | 860.11464 | 5 |
| q0.oracle.maximum_coverage | 0.44013491 | 0.44013491 | 0.44013491 | 0.50545604 | 0.51714286 | 0.46860072 | 0.039196816 | 5 |
| q0.shared.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.shared.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.shared.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q1.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.minimum.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.minimum.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.minimum.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.minimum.error_minus_target | 0.24895666 | 0.30225443 | 0.38681319 | 0.29372027 | 0.24895666 | 0.29614024 | 0.056385732 | 5 |
| q1.minimum.oracle_risk_gap | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1405 | 1235 | 1140 | 427 | 1405 | 1122.4 | 405.06024 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 2007 | 1764 | 1628 | 610 | 2007 | 1603.2 | 578.58163 | 5 |
| q1.oracle.maximum_coverage | 0.64430177 | 0.56811594 | 0.44725275 | 0.58039962 | 0.64430177 | 0.57687437 | 0.080597472 | 5 |
| q1.shared.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.shared.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.shared.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| question_mean.minimum.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.54221834 | 0.50412542 | 0.44369383 | 0.54292783 | 0.58072231 | 0.52273755 | 0.051825916 | 5 |
| question_mean.shared.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |

### question_plus_explanation / confidence_only / 20%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 216 | 944 | 937 | 2985 | 994 | 1215.2 | 1040.4887 | 5 |
| joint.histogram.001 | 0 | 0 | 83 | 0 | 0 | 16.6 | 37.118728 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 330 | 49 | 92 | 70 | 511 | 210.4 | 202.75922 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| joint.counts.count_pass | 3801 | 3073 | 3384 | 2259 | 4623 | 3428 | 874.88228 | 5 |
| joint.counts.coverage_pass | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.counts.risk_pass | 0 | 0 | 83 | 0 | 0 | 16.6 | 37.118728 | 5 |
| joint.counts.both_floors | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| shared.threshold | 0.80273934 | 0.31608431 | 0.51018362 | 0.70757791 | 0.71641053 | 0.61059914 | 0.19643132 | 5 |
| shared.worst_risk | 0.67615658 | 0.72970195 | 0.43339254 | 0.58716418 | 0.79642857 | 0.64456877 | 0.14071028 | 5 |
| shared.error_minus_target | 0.47615658 | 0.52970195 | 0.23339254 | 0.38716418 | 0.59642857 | 0.44456877 | 0.14071028 | 5 |
| q0.histogram.000 | 195 | 775 | 168 | 76 | 994 | 441.6 | 414.01485 | 5 |
| q0.histogram.001 | 21 | 169 | 852 | 11 | 0 | 210.6 | 365.12505 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 41 | 49 | 92 | 351 | 511 | 208.8 | 211.47151 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q0.counts.count_pass | 3801 | 3073 | 3384 | 5157 | 4623 | 4007.6 | 866.72879 | 5 |
| q0.counts.coverage_pass | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.counts.risk_pass | 21 | 169 | 852 | 11 | 0 | 210.6 | 365.12505 | 5 |
| q0.counts.both_floors | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.minimum.threshold | 0.85469628 | 0.4942384 | 0.49926063 | 0.87029749 | 0.71641053 | 0.68698067 | 0.18370363 | 5 |
| q0.minimum.retained_n | 119 | 119 | 145 | 651 | 280 | 262.8 | 227.06211 | 5 |
| q0.minimum.incorrect_n | 70 | 71 | 34 | 241 | 223 | 127.8 | 96.491969 | 5 |
| q0.minimum.coverage | 0.10033727 | 0.10033727 | 0.1222597 | 0.13403335 | 0.1 | 0.11139352 | 0.015850312 | 5 |
| q0.minimum.risk | 0.58823529 | 0.59663866 | 0.23448276 | 0.37019969 | 0.79642857 | 0.51719699 | 0.21843949 | 5 |
| q0.minimum.error_minus_target | 0.38823529 | 0.39663866 | 0.034482759 | 0.17019969 | 0.59642857 | 0.31719699 | 0.21843949 | 5 |
| q0.minimum.oracle_risk_gap | 0.58823529 | 0.59663866 | 0.23448276 | 0.37019969 | 0.79642857 | 0.51719699 | 0.21843949 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 323 | 307 | 520 | 1720 | 485 | 671 | 594.01136 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 403 | 383 | 650 | 2150 | 606 | 838.4 | 742.75857 | 5 |
| q0.oracle.maximum_coverage | 0.33979764 | 0.32293423 | 0.54806071 | 0.44266008 | 0.21642857 | 0.37397625 | 0.12611265 | 5 |
| q0.shared.retained_n | 281 | 973 | 128 | 3350 | 280 | 1002.4 | 1352.6775 | 5 |
| q0.shared.incorrect_n | 190 | 710 | 33 | 1967 | 223 | 624.6 | 792.06711 | 5 |
| q0.shared.coverage | 0.23693086 | 0.82040472 | 0.1079258 | 0.68972617 | 0.1 | 0.39099751 | 0.33991728 | 5 |
| q0.shared.risk | 0.67615658 | 0.72970195 | 0.2578125 | 0.58716418 | 0.79642857 | 0.60945276 | 0.21096023 | 5 |
| q1.histogram.000 | 166 | 92 | 0 | 2323 | 28 | 521.8 | 1008.9297 | 5 |
| q1.histogram.001 | 0 | 0 | 98 | 662 | 69 | 165.8 | 280.69592 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 380 | 203 | 218 | 70 | 204 | 215 | 110.14082 | 5 |
| q1.histogram.101 | 0 | 0 | 35 | 0 | 0 | 7 | 15.652476 | 5 |
| q1.histogram.110 | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q1.counts.count_pass | 3851 | 3925 | 4306 | 2259 | 5520 | 3972.2 | 1168.2336 | 5 |
| q1.counts.coverage_pass | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.counts.risk_pass | 0 | 0 | 133 | 662 | 69 | 172.8 | 279.0138 | 5 |
| q1.counts.both_floors | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 35 | 0 | 0 | 7 | 15.652476 | 5 |
| q1.counts.risk_only_failure | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.minimum.threshold | 0.76266934 | 0.19473508 | 0.65312033 | 0.69546774 | 0.94533647 | 0.65026579 | 0.27805613 | 5 |
| q1.minimum.retained_n | 437 | 3103 | 364 | 121 | 336 | 872.2 | 1252.592 | 5 |
| q1.minimum.incorrect_n | 235 | 2180 | 103 | 56 | 101 | 535 | 922.01491 | 5 |
| q1.minimum.coverage | 0.14028892 | 0.99935588 | 0.1 | 0.11512845 | 0.10786517 | 0.29252768 | 0.39541762 | 5 |
| q1.minimum.risk | 0.53775744 | 0.70254592 | 0.28296703 | 0.46280992 | 0.30059524 | 0.45733511 | 0.1743543 | 5 |
| q1.minimum.error_minus_target | 0.33775744 | 0.50254592 | 0.082967033 | 0.26280992 | 0.10059524 | 0.25733511 | 0.1743543 | 5 |
| q1.minimum.oracle_risk_gap | 0.53775744 | 0.70254592 | 0.28296703 | 0.46280992 | 0.30059524 | 0.45733511 | 0.1743543 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1134 | 923 | 1290 | 417 | 1376 | 1028 | 382.53431 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1417 | 1153 | 1612 | 521 | 1720 | 1284.6 | 478.19902 | 5 |
| q1.oracle.maximum_coverage | 0.45489567 | 0.37133655 | 0.44285714 | 0.49571836 | 0.55216693 | 0.46339493 | 0.066884333 | 5 |
| q1.shared.retained_n | 315 | 2422 | 1126 | 106 | 1294 | 1052.6 | 919.10598 | 5 |
| q1.shared.incorrect_n | 176 | 1761 | 488 | 50 | 539 | 602.8 | 679.4157 | 5 |
| q1.shared.coverage | 0.1011236 | 0.78003221 | 0.30934066 | 0.10085633 | 0.41540931 | 0.34135242 | 0.28040033 | 5 |
| q1.shared.risk | 0.55873016 | 0.72708505 | 0.43339254 | 0.47169811 | 0.41653787 | 0.52148875 | 0.12738868 | 5 |
| question_mean.minimum.risk | 0.56299637 | 0.64959229 | 0.2587249 | 0.41650481 | 0.5485119 | 0.48726605 | 0.15254029 | 5 |
| question_mean.minimum.coverage | 0.1203131 | 0.54984657 | 0.11112985 | 0.1245809 | 0.10393258 | 0.2019606 | 0.1946396 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.56299637 | 0.64959229 | 0.2587249 | 0.41650481 | 0.5485119 | 0.48726605 | 0.15254029 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.39734665 | 0.34713539 | 0.49545893 | 0.46918922 | 0.38429775 | 0.41868559 | 0.061648329 | 5 |
| question_mean.shared.risk | 0.61744337 | 0.7283935 | 0.34560252 | 0.52943115 | 0.60648322 | 0.56547075 | 0.14192242 | 5 |
| question_mean.shared.coverage | 0.16902723 | 0.80021846 | 0.20863323 | 0.39529125 | 0.25770465 | 0.36617496 | 0.25724208 | 5 |

### question_plus_explanation / confidence_only / 10%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 216 | 944 | 1010 | 2985 | 994 | 1229.8 | 1036.1121 | 5 |
| joint.histogram.001 | 0 | 0 | 10 | 0 | 0 | 2 | 4.472136 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 330 | 49 | 92 | 70 | 511 | 210.4 | 202.75922 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| joint.counts.count_pass | 3801 | 3073 | 3384 | 2259 | 4623 | 3428 | 874.88228 | 5 |
| joint.counts.coverage_pass | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.counts.risk_pass | 0 | 0 | 10 | 0 | 0 | 2 | 4.472136 | 5 |
| joint.counts.both_floors | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| shared.threshold | 0.80273934 | 0.31608431 | 0.51018362 | 0.70757791 | 0.71641053 | 0.61059914 | 0.19643132 | 5 |
| shared.worst_risk | 0.67615658 | 0.72970195 | 0.43339254 | 0.58716418 | 0.79642857 | 0.64456877 | 0.14071028 | 5 |
| shared.error_minus_target | 0.57615658 | 0.62970195 | 0.33339254 | 0.48716418 | 0.69642857 | 0.54456877 | 0.14071028 | 5 |
| q0.histogram.000 | 200 | 799 | 461 | 81 | 994 | 507 | 387.38676 | 5 |
| q0.histogram.001 | 16 | 145 | 559 | 6 | 0 | 145.2 | 238.94707 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 41 | 49 | 92 | 351 | 511 | 208.8 | 211.47151 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q0.counts.count_pass | 3801 | 3073 | 3384 | 5157 | 4623 | 4007.6 | 866.72879 | 5 |
| q0.counts.coverage_pass | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.counts.risk_pass | 16 | 145 | 559 | 6 | 0 | 145.2 | 238.94707 | 5 |
| q0.counts.both_floors | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.minimum.threshold | 0.85469628 | 0.4942384 | 0.49926063 | 0.87029749 | 0.71641053 | 0.68698067 | 0.18370363 | 5 |
| q0.minimum.retained_n | 119 | 119 | 145 | 651 | 280 | 262.8 | 227.06211 | 5 |
| q0.minimum.incorrect_n | 70 | 71 | 34 | 241 | 223 | 127.8 | 96.491969 | 5 |
| q0.minimum.coverage | 0.10033727 | 0.10033727 | 0.1222597 | 0.13403335 | 0.1 | 0.11139352 | 0.015850312 | 5 |
| q0.minimum.risk | 0.58823529 | 0.59663866 | 0.23448276 | 0.37019969 | 0.79642857 | 0.51719699 | 0.21843949 | 5 |
| q0.minimum.error_minus_target | 0.48823529 | 0.49663866 | 0.13448276 | 0.27019969 | 0.69642857 | 0.41719699 | 0.21843949 | 5 |
| q0.minimum.oracle_risk_gap | 0.58823529 | 0.59663866 | 0.23448276 | 0.37019969 | 0.79642857 | 0.51719699 | 0.21843949 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 323 | 307 | 520 | 1720 | 485 | 671 | 594.01136 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 358 | 341 | 577 | 1911 | 538 | 745 | 660.22988 | 5 |
| q0.oracle.maximum_coverage | 0.30185497 | 0.28752108 | 0.48650927 | 0.39345275 | 0.19214286 | 0.33229619 | 0.11191094 | 5 |
| q0.shared.retained_n | 281 | 973 | 128 | 3350 | 280 | 1002.4 | 1352.6775 | 5 |
| q0.shared.incorrect_n | 190 | 710 | 33 | 1967 | 223 | 624.6 | 792.06711 | 5 |
| q0.shared.coverage | 0.23693086 | 0.82040472 | 0.1079258 | 0.68972617 | 0.1 | 0.39099751 | 0.33991728 | 5 |
| q0.shared.risk | 0.67615658 | 0.72970195 | 0.2578125 | 0.58716418 | 0.79642857 | 0.60945276 | 0.21096023 | 5 |
| q1.histogram.000 | 166 | 92 | 45 | 2552 | 91 | 589.2 | 1098.0946 | 5 |
| q1.histogram.001 | 0 | 0 | 53 | 433 | 6 | 98.4 | 188.36215 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 380 | 203 | 253 | 70 | 204 | 222 | 111.48318 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q1.counts.count_pass | 3851 | 3925 | 4306 | 2259 | 5520 | 3972.2 | 1168.2336 | 5 |
| q1.counts.coverage_pass | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.counts.risk_pass | 0 | 0 | 53 | 433 | 6 | 98.4 | 188.36215 | 5 |
| q1.counts.both_floors | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.minimum.threshold | 0.76266934 | 0.19473508 | 0.65312033 | 0.69546774 | 0.94533647 | 0.65026579 | 0.27805613 | 5 |
| q1.minimum.retained_n | 437 | 3103 | 364 | 121 | 336 | 872.2 | 1252.592 | 5 |
| q1.minimum.incorrect_n | 235 | 2180 | 103 | 56 | 101 | 535 | 922.01491 | 5 |
| q1.minimum.coverage | 0.14028892 | 0.99935588 | 0.1 | 0.11512845 | 0.10786517 | 0.29252768 | 0.39541762 | 5 |
| q1.minimum.risk | 0.53775744 | 0.70254592 | 0.28296703 | 0.46280992 | 0.30059524 | 0.45733511 | 0.1743543 | 5 |
| q1.minimum.error_minus_target | 0.43775744 | 0.60254592 | 0.18296703 | 0.36280992 | 0.20059524 | 0.35733511 | 0.1743543 | 5 |
| q1.minimum.oracle_risk_gap | 0.53775744 | 0.70254592 | 0.28296703 | 0.46280992 | 0.30059524 | 0.45733511 | 0.1743543 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1134 | 923 | 1290 | 417 | 1376 | 1028 | 382.53431 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1260 | 1025 | 1433 | 463 | 1528 | 1141.8 | 424.95023 | 5 |
| q1.oracle.maximum_coverage | 0.40449438 | 0.33011272 | 0.39368132 | 0.44053283 | 0.4905297 | 0.41187019 | 0.059326187 | 5 |
| q1.shared.retained_n | 315 | 2422 | 1126 | 106 | 1294 | 1052.6 | 919.10598 | 5 |
| q1.shared.incorrect_n | 176 | 1761 | 488 | 50 | 539 | 602.8 | 679.4157 | 5 |
| q1.shared.coverage | 0.1011236 | 0.78003221 | 0.30934066 | 0.10085633 | 0.41540931 | 0.34135242 | 0.28040033 | 5 |
| q1.shared.risk | 0.55873016 | 0.72708505 | 0.43339254 | 0.47169811 | 0.41653787 | 0.52148875 | 0.12738868 | 5 |
| question_mean.minimum.risk | 0.56299637 | 0.64959229 | 0.2587249 | 0.41650481 | 0.5485119 | 0.48726605 | 0.15254029 | 5 |
| question_mean.minimum.coverage | 0.1203131 | 0.54984657 | 0.11112985 | 0.1245809 | 0.10393258 | 0.2019606 | 0.1946396 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.56299637 | 0.64959229 | 0.2587249 | 0.41650481 | 0.5485119 | 0.48726605 | 0.15254029 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.35317468 | 0.3088169 | 0.4400953 | 0.41699279 | 0.34133628 | 0.37208319 | 0.05465356 | 5 |
| question_mean.shared.risk | 0.61744337 | 0.7283935 | 0.34560252 | 0.52943115 | 0.60648322 | 0.56547075 | 0.14192242 | 5 |
| question_mean.shared.coverage | 0.16902723 | 0.80021846 | 0.20863323 | 0.39529125 | 0.25770465 | 0.36617496 | 0.25724208 | 5 |

### question_plus_explanation / confidence_only / 30%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 216 | 944 | 698 | 2985 | 994 | 1167.4 | 1061.7372 | 5 |
| joint.histogram.001 | 0 | 0 | 322 | 0 | 0 | 64.4 | 144.00278 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 330 | 49 | 92 | 70 | 511 | 210.4 | 202.75922 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| joint.counts.count_pass | 3801 | 3073 | 3384 | 2259 | 4623 | 3428 | 874.88228 | 5 |
| joint.counts.coverage_pass | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.counts.risk_pass | 0 | 0 | 322 | 0 | 0 | 64.4 | 144.00278 | 5 |
| joint.counts.both_floors | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3471 | 3024 | 3292 | 2189 | 4112 | 3217.6 | 700.92746 | 5 |
| shared.threshold | 0.80273934 | 0.31608431 | 0.51018362 | 0.70757791 | 0.71641053 | 0.61059914 | 0.19643132 | 5 |
| shared.worst_risk | 0.67615658 | 0.72970195 | 0.43339254 | 0.58716418 | 0.79642857 | 0.64456877 | 0.14071028 | 5 |
| shared.error_minus_target | 0.37615658 | 0.42970195 | 0.13339254 | 0.28716418 | 0.49642857 | 0.34456877 | 0.14071028 | 5 |
| q0.histogram.000 | 180 | 525 | 50 | 65 | 994 | 362.8 | 401.45573 | 5 |
| q0.histogram.001 | 36 | 419 | 970 | 22 | 0 | 289.4 | 418.17437 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 41 | 49 | 0 | 351 | 511 | 190.4 | 227.56494 | 5 |
| q0.histogram.101 | 0 | 0 | 92 | 0 | 0 | 18.4 | 41.143651 | 5 |
| q0.histogram.110 | 3760 | 3024 | 2769 | 4806 | 4112 | 3694.2 | 824.64368 | 5 |
| q0.histogram.111 | 0 | 0 | 523 | 0 | 0 | 104.6 | 233.89271 | 5 |
| q0.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q0.counts.count_pass | 3801 | 3073 | 3384 | 5157 | 4623 | 4007.6 | 866.72879 | 5 |
| q0.counts.coverage_pass | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.counts.risk_pass | 36 | 419 | 1585 | 22 | 0 | 412.4 | 678.08502 | 5 |
| q0.counts.both_floors | 3760 | 3024 | 3292 | 4806 | 4112 | 3798.8 | 701.99943 | 5 |
| q0.counts.all_three | 0 | 0 | 523 | 0 | 0 | 104.6 | 233.89271 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 92 | 0 | 0 | 18.4 | 41.143651 | 5 |
| q0.counts.risk_only_failure | 3760 | 3024 | 2769 | 4806 | 4112 | 3694.2 | 824.64368 | 5 |
| q0.minimum.threshold | 0.85469628 | 0.4942384 | 0.49926063 | 0.87029749 | 0.71641053 | 0.68698067 | 0.18370363 | 5 |
| q0.minimum.retained_n | 119 | 119 | 145 | 651 | 280 | 262.8 | 227.06211 | 5 |
| q0.minimum.incorrect_n | 70 | 71 | 34 | 241 | 223 | 127.8 | 96.491969 | 5 |
| q0.minimum.coverage | 0.10033727 | 0.10033727 | 0.1222597 | 0.13403335 | 0.1 | 0.11139352 | 0.015850312 | 5 |
| q0.minimum.risk | 0.58823529 | 0.59663866 | 0.23448276 | 0.37019969 | 0.79642857 | 0.51719699 | 0.21843949 | 5 |
| q0.minimum.error_minus_target | 0.28823529 | 0.29663866 | -0.065517241 | 0.070199693 | 0.49642857 | 0.21719699 | 0.21843949 | 5 |
| q0.minimum.oracle_risk_gap | 0.58823529 | 0.59663866 | 0.23448276 | 0.37019969 | 0.79642857 | 0.51719699 | 0.21843949 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 323 | 307 | 520 | 1720 | 485 | 671 | 594.01136 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 461 | 438 | 742 | 2457 | 692 | 958 | 848.7965 | 5 |
| q0.oracle.maximum_coverage | 0.38870152 | 0.3693086 | 0.62563238 | 0.50586782 | 0.24714286 | 0.42733063 | 0.14389065 | 5 |
| q0.shared.retained_n | 281 | 973 | 128 | 3350 | 280 | 1002.4 | 1352.6775 | 5 |
| q0.shared.incorrect_n | 190 | 710 | 33 | 1967 | 223 | 624.6 | 792.06711 | 5 |
| q0.shared.coverage | 0.23693086 | 0.82040472 | 0.1079258 | 0.68972617 | 0.1 | 0.39099751 | 0.33991728 | 5 |
| q0.shared.risk | 0.67615658 | 0.72970195 | 0.2578125 | 0.58716418 | 0.79642857 | 0.60945276 | 0.21096023 | 5 |
| q1.histogram.000 | 166 | 92 | 0 | 2251 | 0 | 501.8 | 980.30669 | 5 |
| q1.histogram.001 | 0 | 0 | 98 | 734 | 97 | 185.8 | 310.30662 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 380 | 203 | 0 | 70 | 6 | 131.8 | 161.00373 | 5 |
| q1.histogram.101 | 0 | 0 | 253 | 0 | 198 | 90.2 | 125.0328 | 5 |
| q1.histogram.110 | 3471 | 3722 | 4032 | 2189 | 5316 | 3746 | 1123.2927 | 5 |
| q1.histogram.111 | 0 | 0 | 21 | 0 | 0 | 4.2 | 9.3914855 | 5 |
| q1.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q1.counts.count_pass | 3851 | 3925 | 4306 | 2259 | 5520 | 3972.2 | 1168.2336 | 5 |
| q1.counts.coverage_pass | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.counts.risk_pass | 0 | 0 | 372 | 734 | 295 | 280.2 | 304.79698 | 5 |
| q1.counts.both_floors | 3471 | 3722 | 4053 | 2189 | 5316 | 3750.2 | 1124.6678 | 5 |
| q1.counts.all_three | 0 | 0 | 21 | 0 | 0 | 4.2 | 9.3914855 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 253 | 0 | 198 | 90.2 | 125.0328 | 5 |
| q1.counts.risk_only_failure | 3471 | 3722 | 4032 | 2189 | 5316 | 3746 | 1123.2927 | 5 |
| q1.minimum.threshold | 0.76266934 | 0.19473508 | 0.65312033 | 0.69546774 | 0.94533647 | 0.65026579 | 0.27805613 | 5 |
| q1.minimum.retained_n | 437 | 3103 | 364 | 121 | 336 | 872.2 | 1252.592 | 5 |
| q1.minimum.incorrect_n | 235 | 2180 | 103 | 56 | 101 | 535 | 922.01491 | 5 |
| q1.minimum.coverage | 0.14028892 | 0.99935588 | 0.1 | 0.11512845 | 0.10786517 | 0.29252768 | 0.39541762 | 5 |
| q1.minimum.risk | 0.53775744 | 0.70254592 | 0.28296703 | 0.46280992 | 0.30059524 | 0.45733511 | 0.1743543 | 5 |
| q1.minimum.error_minus_target | 0.23775744 | 0.40254592 | -0.017032967 | 0.16280992 | 0.0005952381 | 0.15733511 | 0.1743543 | 5 |
| q1.minimum.oracle_risk_gap | 0.53775744 | 0.70254592 | 0.28296703 | 0.46280992 | 0.30059524 | 0.45733511 | 0.1743543 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1134 | 923 | 1290 | 417 | 1376 | 1028 | 382.53431 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1620 | 1318 | 1842 | 595 | 1965 | 1468 | 546.49291 | 5 |
| q1.oracle.maximum_coverage | 0.52006421 | 0.42447665 | 0.50604396 | 0.5661275 | 0.63081862 | 0.52950619 | 0.076282633 | 5 |
| q1.shared.retained_n | 315 | 2422 | 1126 | 106 | 1294 | 1052.6 | 919.10598 | 5 |
| q1.shared.incorrect_n | 176 | 1761 | 488 | 50 | 539 | 602.8 | 679.4157 | 5 |
| q1.shared.coverage | 0.1011236 | 0.78003221 | 0.30934066 | 0.10085633 | 0.41540931 | 0.34135242 | 0.28040033 | 5 |
| q1.shared.risk | 0.55873016 | 0.72708505 | 0.43339254 | 0.47169811 | 0.41653787 | 0.52148875 | 0.12738868 | 5 |
| question_mean.minimum.risk | 0.56299637 | 0.64959229 | 0.2587249 | 0.41650481 | 0.5485119 | 0.48726605 | 0.15254029 | 5 |
| question_mean.minimum.coverage | 0.1203131 | 0.54984657 | 0.11112985 | 0.1245809 | 0.10393258 | 0.2019606 | 0.1946396 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.56299637 | 0.64959229 | 0.2587249 | 0.41650481 | 0.5485119 | 0.48726605 | 0.15254029 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.45438286 | 0.39689263 | 0.56583817 | 0.53599766 | 0.43898074 | 0.47841841 | 0.07024435 | 5 |
| question_mean.shared.risk | 0.61744337 | 0.7283935 | 0.34560252 | 0.52943115 | 0.60648322 | 0.56547075 | 0.14192242 | 5 |
| question_mean.shared.coverage | 0.16902723 | 0.80021846 | 0.20863323 | 0.39529125 | 0.25770465 | 0.36617496 | 0.25724208 | 5 |

### question_plus_explanation / support_aware / 20%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 362 | 1123 | 950 | 3432 | 1236 | 1420.6 | 1173.7196 | 5 |
| joint.histogram.001 | 0 | 0 | 98 | 0 | 0 | 19.6 | 43.826932 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 42 | 55 | 107 | 56 | 492 | 150.4 | 192.57284 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| joint.counts.count_pass | 3655 | 2894 | 3356 | 1812 | 4381 | 3219.6 | 954.51312 | 5 |
| joint.counts.coverage_pass | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.counts.risk_pass | 0 | 0 | 98 | 0 | 0 | 19.6 | 43.826932 | 5 |
| joint.counts.both_floors | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| shared.threshold | 0.79356981 | 0.28922476 | 0.49106915 | 0.66701611 | 0.56315943 | 0.56080785 | 0.18979246 | 5 |
| shared.worst_risk | 0.58823529 | 0.7257085 | 0.43455497 | 0.61225541 | 0.71266968 | 0.61468477 | 0.11734515 | 5 |
| shared.error_minus_target | 0.38823529 | 0.5257085 | 0.23455497 | 0.41225541 | 0.51266968 | 0.41468477 | 0.11734515 | 5 |
| q0.histogram.000 | 307 | 951 | 49 | 76 | 1236 | 523.8 | 539.14071 | 5 |
| q0.histogram.001 | 55 | 172 | 999 | 11 | 0 | 247.4 | 425.64574 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 42 | 55 | 0 | 350 | 492 | 187.8 | 219.66383 | 5 |
| q0.histogram.101 | 0 | 0 | 107 | 0 | 0 | 21.4 | 47.851855 | 5 |
| q0.histogram.110 | 3613 | 2839 | 2991 | 4807 | 3889 | 3627.8 | 788.46002 | 5 |
| q0.histogram.111 | 0 | 0 | 258 | 0 | 0 | 51.6 | 115.38111 | 5 |
| q0.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q0.counts.count_pass | 3655 | 2894 | 3356 | 5157 | 4381 | 3888.6 | 891.45348 | 5 |
| q0.counts.coverage_pass | 3613 | 2839 | 3249 | 4807 | 3889 | 3679.4 | 743.52861 | 5 |
| q0.counts.risk_pass | 55 | 172 | 1364 | 11 | 0 | 320.4 | 587.35534 | 5 |
| q0.counts.both_floors | 3613 | 2839 | 3249 | 4807 | 3889 | 3679.4 | 743.52861 | 5 |
| q0.counts.all_three | 0 | 0 | 258 | 0 | 0 | 51.6 | 115.38111 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 107 | 0 | 0 | 21.4 | 47.851855 | 5 |
| q0.counts.risk_only_failure | 3613 | 2839 | 2991 | 4807 | 3889 | 3627.8 | 788.46002 | 5 |
| q0.minimum.threshold | 0.79356981 | 0.45224005 | 0.4872385 | 0.87029749 | 0.56315943 | 0.63330105 | 0.18767697 | 5 |
| q0.minimum.retained_n | 119 | 119 | 133 | 651 | 442 | 292.8 | 243.16496 | 5 |
| q0.minimum.incorrect_n | 70 | 71 | 19 | 241 | 315 | 143.2 | 127.55077 | 5 |
| q0.minimum.coverage | 0.10033727 | 0.10033727 | 0.11214165 | 0.13403335 | 0.15785714 | 0.12094134 | 0.024802557 | 5 |
| q0.minimum.risk | 0.58823529 | 0.59663866 | 0.14285714 | 0.37019969 | 0.71266968 | 0.48212009 | 0.22646941 | 5 |
| q0.minimum.error_minus_target | 0.38823529 | 0.39663866 | -0.057142857 | 0.17019969 | 0.51266968 | 0.28212009 | 0.22646941 | 5 |
| q0.minimum.oracle_risk_gap | 0.58823529 | 0.59663866 | 0.14285714 | 0.37019969 | 0.71266968 | 0.48212009 | 0.22646941 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 323 | 307 | 520 | 1720 | 485 | 671 | 594.01136 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 403 | 383 | 650 | 2150 | 606 | 838.4 | 742.75857 | 5 |
| q0.oracle.maximum_coverage | 0.33979764 | 0.32293423 | 0.54806071 | 0.44266008 | 0.21642857 | 0.37397625 | 0.12611265 | 5 |
| q0.shared.retained_n | 119 | 988 | 123 | 3884 | 442 | 1111.2 | 1590.0021 | 5 |
| q0.shared.incorrect_n | 70 | 717 | 19 | 2378 | 315 | 699.8 | 977.86231 | 5 |
| q0.shared.coverage | 0.10033727 | 0.83305228 | 0.10370995 | 0.79967058 | 0.15785714 | 0.39892544 | 0.38193055 | 5 |
| q0.shared.risk | 0.58823529 | 0.7257085 | 0.15447154 | 0.61225541 | 0.71266968 | 0.55866809 | 0.23384806 | 5 |
| q1.histogram.000 | 101 | 92 | 0 | 1442 | 28 | 332.6 | 621.63076 | 5 |
| q1.histogram.001 | 0 | 0 | 98 | 1990 | 69 | 431.4 | 872.34385 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 298 | 200 | 208 | 56 | 204 | 193.2 | 86.874622 | 5 |
| q1.histogram.101 | 0 | 0 | 49 | 0 | 0 | 9.8 | 21.913466 | 5 |
| q1.histogram.110 | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q1.counts.count_pass | 3916 | 3925 | 4306 | 1812 | 5520 | 3895.8 | 1336.953 | 5 |
| q1.counts.coverage_pass | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.counts.risk_pass | 0 | 0 | 147 | 1990 | 69 | 441.2 | 867.92609 | 5 |
| q1.counts.both_floors | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 49 | 0 | 0 | 9.8 | 21.913466 | 5 |
| q1.counts.risk_only_failure | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.minimum.threshold | 0.76266145 | 0.23245091 | 0.64947725 | 0.66482054 | 0.94533647 | 0.65094933 | 0.26195366 | 5 |
| q1.minimum.retained_n | 400 | 2982 | 365 | 107 | 336 | 838 | 1204.0218 | 5 |
| q1.minimum.incorrect_n | 211 | 2080 | 106 | 43 | 101 | 508.2 | 880.74837 | 5 |
| q1.minimum.coverage | 0.12841091 | 0.96038647 | 0.10027473 | 0.1018078 | 0.10786517 | 0.27974902 | 0.38065362 | 5 |
| q1.minimum.risk | 0.5275 | 0.69751844 | 0.29041096 | 0.40186916 | 0.30059524 | 0.44357876 | 0.17115234 | 5 |
| q1.minimum.error_minus_target | 0.3275 | 0.49751844 | 0.090410959 | 0.20186916 | 0.10059524 | 0.24357876 | 0.17115234 | 5 |
| q1.minimum.oracle_risk_gap | 0.5275 | 0.69751844 | 0.29041096 | 0.40186916 | 0.30059524 | 0.44357876 | 0.17115234 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1134 | 923 | 1290 | 417 | 1376 | 1028 | 382.53431 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1417 | 1153 | 1612 | 521 | 1720 | 1284.6 | 478.19902 | 5 |
| q1.oracle.maximum_coverage | 0.45489567 | 0.37133655 | 0.44285714 | 0.49571836 | 0.55216693 | 0.46339493 | 0.066884333 | 5 |
| q1.shared.retained_n | 318 | 2538 | 1146 | 106 | 1759 | 1173.4 | 1009.5622 | 5 |
| q1.shared.incorrect_n | 178 | 1799 | 498 | 43 | 776 | 658.8 | 698.2168 | 5 |
| q1.shared.coverage | 0.10208668 | 0.8173913 | 0.31483516 | 0.10085633 | 0.564687 | 0.37997129 | 0.31017088 | 5 |
| q1.shared.risk | 0.55974843 | 0.70882585 | 0.43455497 | 0.40566038 | 0.44115975 | 0.50998988 | 0.12582161 | 5 |
| question_mean.minimum.risk | 0.55786765 | 0.64707855 | 0.21663405 | 0.38603443 | 0.50663246 | 0.46284943 | 0.16688944 | 5 |
| question_mean.minimum.coverage | 0.11437409 | 0.53036187 | 0.10620819 | 0.11792058 | 0.13286116 | 0.20034518 | 0.18473747 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.55786765 | 0.64707855 | 0.21663405 | 0.38603443 | 0.50663246 | 0.46284943 | 0.16688944 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.39734665 | 0.34713539 | 0.49545893 | 0.46918922 | 0.38429775 | 0.41868559 | 0.061648329 | 5 |
| question_mean.shared.risk | 0.57399186 | 0.71726717 | 0.29451326 | 0.50895789 | 0.57691472 | 0.53432898 | 0.15411712 | 5 |
| question_mean.shared.coverage | 0.10121197 | 0.82522179 | 0.20927256 | 0.45026345 | 0.36127207 | 0.38944837 | 0.27835876 | 5 |

### question_plus_explanation / support_aware / 10%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 362 | 1123 | 1033 | 3432 | 1236 | 1437.2 | 1165.9613 | 5 |
| joint.histogram.001 | 0 | 0 | 15 | 0 | 0 | 3 | 6.7082039 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 42 | 55 | 107 | 56 | 492 | 150.4 | 192.57284 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| joint.counts.count_pass | 3655 | 2894 | 3356 | 1812 | 4381 | 3219.6 | 954.51312 | 5 |
| joint.counts.coverage_pass | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.counts.risk_pass | 0 | 0 | 15 | 0 | 0 | 3 | 6.7082039 | 5 |
| joint.counts.both_floors | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| shared.threshold | 0.79356981 | 0.28922476 | 0.49106915 | 0.66701611 | 0.56315943 | 0.56080785 | 0.18979246 | 5 |
| shared.worst_risk | 0.58823529 | 0.7257085 | 0.43455497 | 0.61225541 | 0.71266968 | 0.61468477 | 0.11734515 | 5 |
| shared.error_minus_target | 0.48823529 | 0.6257085 | 0.33455497 | 0.51225541 | 0.61266968 | 0.51468477 | 0.11734515 | 5 |
| q0.histogram.000 | 307 | 1030 | 526 | 81 | 1236 | 636 | 485.69589 | 5 |
| q0.histogram.001 | 55 | 93 | 522 | 6 | 0 | 135.2 | 219.5443 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 42 | 55 | 107 | 350 | 492 | 209.2 | 201.23295 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 3613 | 2839 | 3249 | 4807 | 3889 | 3679.4 | 743.52861 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q0.counts.count_pass | 3655 | 2894 | 3356 | 5157 | 4381 | 3888.6 | 891.45348 | 5 |
| q0.counts.coverage_pass | 3613 | 2839 | 3249 | 4807 | 3889 | 3679.4 | 743.52861 | 5 |
| q0.counts.risk_pass | 55 | 93 | 522 | 6 | 0 | 135.2 | 219.5443 | 5 |
| q0.counts.both_floors | 3613 | 2839 | 3249 | 4807 | 3889 | 3679.4 | 743.52861 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 3613 | 2839 | 3249 | 4807 | 3889 | 3679.4 | 743.52861 | 5 |
| q0.minimum.threshold | 0.79356981 | 0.45224005 | 0.4872385 | 0.87029749 | 0.56315943 | 0.63330105 | 0.18767697 | 5 |
| q0.minimum.retained_n | 119 | 119 | 133 | 651 | 442 | 292.8 | 243.16496 | 5 |
| q0.minimum.incorrect_n | 70 | 71 | 19 | 241 | 315 | 143.2 | 127.55077 | 5 |
| q0.minimum.coverage | 0.10033727 | 0.10033727 | 0.11214165 | 0.13403335 | 0.15785714 | 0.12094134 | 0.024802557 | 5 |
| q0.minimum.risk | 0.58823529 | 0.59663866 | 0.14285714 | 0.37019969 | 0.71266968 | 0.48212009 | 0.22646941 | 5 |
| q0.minimum.error_minus_target | 0.48823529 | 0.49663866 | 0.042857143 | 0.27019969 | 0.61266968 | 0.38212009 | 0.22646941 | 5 |
| q0.minimum.oracle_risk_gap | 0.58823529 | 0.59663866 | 0.14285714 | 0.37019969 | 0.71266968 | 0.48212009 | 0.22646941 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 323 | 307 | 520 | 1720 | 485 | 671 | 594.01136 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 358 | 341 | 577 | 1911 | 538 | 745 | 660.22988 | 5 |
| q0.oracle.maximum_coverage | 0.30185497 | 0.28752108 | 0.48650927 | 0.39345275 | 0.19214286 | 0.33229619 | 0.11191094 | 5 |
| q0.shared.retained_n | 119 | 988 | 123 | 3884 | 442 | 1111.2 | 1590.0021 | 5 |
| q0.shared.incorrect_n | 70 | 717 | 19 | 2378 | 315 | 699.8 | 977.86231 | 5 |
| q0.shared.coverage | 0.10033727 | 0.83305228 | 0.10370995 | 0.79967058 | 0.15785714 | 0.39892544 | 0.38193055 | 5 |
| q0.shared.risk | 0.58823529 | 0.7257085 | 0.15447154 | 0.61225541 | 0.71266968 | 0.55866809 | 0.23384806 | 5 |
| q1.histogram.000 | 101 | 92 | 39 | 1639 | 91 | 392.4 | 697.29821 | 5 |
| q1.histogram.001 | 0 | 0 | 59 | 1793 | 6 | 371.6 | 794.97377 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 298 | 200 | 257 | 56 | 204 | 203 | 91.596943 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q1.counts.count_pass | 3916 | 3925 | 4306 | 1812 | 5520 | 3895.8 | 1336.953 | 5 |
| q1.counts.coverage_pass | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.counts.risk_pass | 0 | 0 | 59 | 1793 | 6 | 371.6 | 794.97377 | 5 |
| q1.counts.both_floors | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.minimum.threshold | 0.76266145 | 0.23245091 | 0.64947725 | 0.66482054 | 0.94533647 | 0.65094933 | 0.26195366 | 5 |
| q1.minimum.retained_n | 400 | 2982 | 365 | 107 | 336 | 838 | 1204.0218 | 5 |
| q1.minimum.incorrect_n | 211 | 2080 | 106 | 43 | 101 | 508.2 | 880.74837 | 5 |
| q1.minimum.coverage | 0.12841091 | 0.96038647 | 0.10027473 | 0.1018078 | 0.10786517 | 0.27974902 | 0.38065362 | 5 |
| q1.minimum.risk | 0.5275 | 0.69751844 | 0.29041096 | 0.40186916 | 0.30059524 | 0.44357876 | 0.17115234 | 5 |
| q1.minimum.error_minus_target | 0.4275 | 0.59751844 | 0.19041096 | 0.30186916 | 0.20059524 | 0.34357876 | 0.17115234 | 5 |
| q1.minimum.oracle_risk_gap | 0.5275 | 0.69751844 | 0.29041096 | 0.40186916 | 0.30059524 | 0.44357876 | 0.17115234 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1134 | 923 | 1290 | 417 | 1376 | 1028 | 382.53431 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1260 | 1025 | 1433 | 463 | 1528 | 1141.8 | 424.95023 | 5 |
| q1.oracle.maximum_coverage | 0.40449438 | 0.33011272 | 0.39368132 | 0.44053283 | 0.4905297 | 0.41187019 | 0.059326187 | 5 |
| q1.shared.retained_n | 318 | 2538 | 1146 | 106 | 1759 | 1173.4 | 1009.5622 | 5 |
| q1.shared.incorrect_n | 178 | 1799 | 498 | 43 | 776 | 658.8 | 698.2168 | 5 |
| q1.shared.coverage | 0.10208668 | 0.8173913 | 0.31483516 | 0.10085633 | 0.564687 | 0.37997129 | 0.31017088 | 5 |
| q1.shared.risk | 0.55974843 | 0.70882585 | 0.43455497 | 0.40566038 | 0.44115975 | 0.50998988 | 0.12582161 | 5 |
| question_mean.minimum.risk | 0.55786765 | 0.64707855 | 0.21663405 | 0.38603443 | 0.50663246 | 0.46284943 | 0.16688944 | 5 |
| question_mean.minimum.coverage | 0.11437409 | 0.53036187 | 0.10620819 | 0.11792058 | 0.13286116 | 0.20034518 | 0.18473747 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.55786765 | 0.64707855 | 0.21663405 | 0.38603443 | 0.50663246 | 0.46284943 | 0.16688944 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.35317468 | 0.3088169 | 0.4400953 | 0.41699279 | 0.34133628 | 0.37208319 | 0.05465356 | 5 |
| question_mean.shared.risk | 0.57399186 | 0.71726717 | 0.29451326 | 0.50895789 | 0.57691472 | 0.53432898 | 0.15411712 | 5 |
| question_mean.shared.coverage | 0.10121197 | 0.82522179 | 0.20927256 | 0.45026345 | 0.36127207 | 0.38944837 | 0.27835876 | 5 |

### question_plus_explanation / support_aware / 30%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 362 | 1123 | 719 | 3432 | 1236 | 1374.4 | 1201.1013 | 5 |
| joint.histogram.001 | 0 | 0 | 329 | 0 | 0 | 65.8 | 147.13327 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 42 | 55 | 107 | 56 | 492 | 150.4 | 192.57284 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| joint.counts.count_pass | 3655 | 2894 | 3356 | 1812 | 4381 | 3219.6 | 954.51312 | 5 |
| joint.counts.coverage_pass | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.counts.risk_pass | 0 | 0 | 329 | 0 | 0 | 65.8 | 147.13327 | 5 |
| joint.counts.both_floors | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 3613 | 2839 | 3249 | 1756 | 3889 | 3069.2 | 833.30739 | 5 |
| shared.threshold | 0.79356981 | 0.28922476 | 0.49106915 | 0.66701611 | 0.56315943 | 0.56080785 | 0.18979246 | 5 |
| shared.worst_risk | 0.58823529 | 0.7257085 | 0.43455497 | 0.61225541 | 0.71266968 | 0.61468477 | 0.11734515 | 5 |
| shared.error_minus_target | 0.28823529 | 0.4257085 | 0.13455497 | 0.31225541 | 0.41266968 | 0.31468477 | 0.11734515 | 5 |
| q0.histogram.000 | 261 | 843 | 49 | 65 | 1236 | 490.8 | 526.46671 | 5 |
| q0.histogram.001 | 101 | 280 | 999 | 22 | 0 | 280.4 | 416.52287 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 42 | 55 | 0 | 350 | 492 | 187.8 | 219.66383 | 5 |
| q0.histogram.101 | 0 | 0 | 107 | 0 | 0 | 21.4 | 47.851855 | 5 |
| q0.histogram.110 | 3613 | 2839 | 2487 | 4807 | 3889 | 3527 | 912.65875 | 5 |
| q0.histogram.111 | 0 | 0 | 762 | 0 | 0 | 152.4 | 340.77676 | 5 |
| q0.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q0.counts.count_pass | 3655 | 2894 | 3356 | 5157 | 4381 | 3888.6 | 891.45348 | 5 |
| q0.counts.coverage_pass | 3613 | 2839 | 3249 | 4807 | 3889 | 3679.4 | 743.52861 | 5 |
| q0.counts.risk_pass | 101 | 280 | 1868 | 22 | 0 | 454.2 | 797.96942 | 5 |
| q0.counts.both_floors | 3613 | 2839 | 3249 | 4807 | 3889 | 3679.4 | 743.52861 | 5 |
| q0.counts.all_three | 0 | 0 | 762 | 0 | 0 | 152.4 | 340.77676 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 107 | 0 | 0 | 21.4 | 47.851855 | 5 |
| q0.counts.risk_only_failure | 3613 | 2839 | 2487 | 4807 | 3889 | 3527 | 912.65875 | 5 |
| q0.minimum.threshold | 0.79356981 | 0.45224005 | 0.4872385 | 0.87029749 | 0.56315943 | 0.63330105 | 0.18767697 | 5 |
| q0.minimum.retained_n | 119 | 119 | 133 | 651 | 442 | 292.8 | 243.16496 | 5 |
| q0.minimum.incorrect_n | 70 | 71 | 19 | 241 | 315 | 143.2 | 127.55077 | 5 |
| q0.minimum.coverage | 0.10033727 | 0.10033727 | 0.11214165 | 0.13403335 | 0.15785714 | 0.12094134 | 0.024802557 | 5 |
| q0.minimum.risk | 0.58823529 | 0.59663866 | 0.14285714 | 0.37019969 | 0.71266968 | 0.48212009 | 0.22646941 | 5 |
| q0.minimum.error_minus_target | 0.28823529 | 0.29663866 | -0.15714286 | 0.070199693 | 0.41266968 | 0.18212009 | 0.22646941 | 5 |
| q0.minimum.oracle_risk_gap | 0.58823529 | 0.59663866 | 0.14285714 | 0.37019969 | 0.71266968 | 0.48212009 | 0.22646941 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 323 | 307 | 520 | 1720 | 485 | 671 | 594.01136 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 461 | 438 | 742 | 2457 | 692 | 958 | 848.7965 | 5 |
| q0.oracle.maximum_coverage | 0.38870152 | 0.3693086 | 0.62563238 | 0.50586782 | 0.24714286 | 0.42733063 | 0.14389065 | 5 |
| q0.shared.retained_n | 119 | 988 | 123 | 3884 | 442 | 1111.2 | 1590.0021 | 5 |
| q0.shared.incorrect_n | 70 | 717 | 19 | 2378 | 315 | 699.8 | 977.86231 | 5 |
| q0.shared.coverage | 0.10033727 | 0.83305228 | 0.10370995 | 0.79967058 | 0.15785714 | 0.39892544 | 0.38193055 | 5 |
| q0.shared.risk | 0.58823529 | 0.7257085 | 0.15447154 | 0.61225541 | 0.71266968 | 0.55866809 | 0.23384806 | 5 |
| q1.histogram.000 | 101 | 92 | 0 | 1105 | 0 | 259.6 | 475.06031 | 5 |
| q1.histogram.001 | 0 | 0 | 98 | 2327 | 97 | 504.4 | 1020.03 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 298 | 200 | 0 | 56 | 6 | 112 | 131.58267 | 5 |
| q1.histogram.101 | 0 | 0 | 257 | 0 | 198 | 91 | 126.34081 | 5 |
| q1.histogram.110 | 3618 | 3725 | 4026 | 1756 | 5316 | 3688.2 | 1275.1001 | 5 |
| q1.histogram.111 | 0 | 0 | 23 | 0 | 0 | 4.6 | 10.285913 | 5 |
| q1.counts.total | 4017 | 4017 | 4404 | 5244 | 5617 | 4659.8 | 733.03117 | 5 |
| q1.counts.count_pass | 3916 | 3925 | 4306 | 1812 | 5520 | 3895.8 | 1336.953 | 5 |
| q1.counts.coverage_pass | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.counts.risk_pass | 0 | 0 | 378 | 2327 | 295 | 600 | 980.41292 | 5 |
| q1.counts.both_floors | 3618 | 3725 | 4049 | 1756 | 5316 | 3692.8 | 1276.6639 | 5 |
| q1.counts.all_three | 0 | 0 | 23 | 0 | 0 | 4.6 | 10.285913 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 257 | 0 | 198 | 91 | 126.34081 | 5 |
| q1.counts.risk_only_failure | 3618 | 3725 | 4026 | 1756 | 5316 | 3688.2 | 1275.1001 | 5 |
| q1.minimum.threshold | 0.76266145 | 0.23245091 | 0.64947725 | 0.66482054 | 0.94533647 | 0.65094933 | 0.26195366 | 5 |
| q1.minimum.retained_n | 400 | 2982 | 365 | 107 | 336 | 838 | 1204.0218 | 5 |
| q1.minimum.incorrect_n | 211 | 2080 | 106 | 43 | 101 | 508.2 | 880.74837 | 5 |
| q1.minimum.coverage | 0.12841091 | 0.96038647 | 0.10027473 | 0.1018078 | 0.10786517 | 0.27974902 | 0.38065362 | 5 |
| q1.minimum.risk | 0.5275 | 0.69751844 | 0.29041096 | 0.40186916 | 0.30059524 | 0.44357876 | 0.17115234 | 5 |
| q1.minimum.error_minus_target | 0.2275 | 0.39751844 | -0.0095890411 | 0.10186916 | 0.0005952381 | 0.14357876 | 0.17115234 | 5 |
| q1.minimum.oracle_risk_gap | 0.5275 | 0.69751844 | 0.29041096 | 0.40186916 | 0.30059524 | 0.44357876 | 0.17115234 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1134 | 923 | 1290 | 417 | 1376 | 1028 | 382.53431 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1620 | 1318 | 1842 | 595 | 1965 | 1468 | 546.49291 | 5 |
| q1.oracle.maximum_coverage | 0.52006421 | 0.42447665 | 0.50604396 | 0.5661275 | 0.63081862 | 0.52950619 | 0.076282633 | 5 |
| q1.shared.retained_n | 318 | 2538 | 1146 | 106 | 1759 | 1173.4 | 1009.5622 | 5 |
| q1.shared.incorrect_n | 178 | 1799 | 498 | 43 | 776 | 658.8 | 698.2168 | 5 |
| q1.shared.coverage | 0.10208668 | 0.8173913 | 0.31483516 | 0.10085633 | 0.564687 | 0.37997129 | 0.31017088 | 5 |
| q1.shared.risk | 0.55974843 | 0.70882585 | 0.43455497 | 0.40566038 | 0.44115975 | 0.50998988 | 0.12582161 | 5 |
| question_mean.minimum.risk | 0.55786765 | 0.64707855 | 0.21663405 | 0.38603443 | 0.50663246 | 0.46284943 | 0.16688944 | 5 |
| question_mean.minimum.coverage | 0.11437409 | 0.53036187 | 0.10620819 | 0.11792058 | 0.13286116 | 0.20034518 | 0.18473747 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.55786765 | 0.64707855 | 0.21663405 | 0.38603443 | 0.50663246 | 0.46284943 | 0.16688944 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.45438286 | 0.39689263 | 0.56583817 | 0.53599766 | 0.43898074 | 0.47841841 | 0.07024435 | 5 |
| question_mean.shared.risk | 0.57399186 | 0.71726717 | 0.29451326 | 0.50895789 | 0.57691472 | 0.53432898 | 0.15411712 | 5 |
| question_mean.shared.coverage | 0.10121197 | 0.82522179 | 0.20927256 | 0.45026345 | 0.36127207 | 0.38944837 | 0.27835876 | 5 |

### question_plus_explanation / frequency / 20%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| shared.worst_risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| shared.error_minus_target | 0.49139966 | 0.49139966 | 0.49139966 | 0.44607783 | 0.43785714 | 0.47162679 | 0.027230673 | 5 |
| q0.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.minimum.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.minimum.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.minimum.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.minimum.error_minus_target | 0.49139966 | 0.49139966 | 0.49139966 | 0.44607783 | 0.43785714 | 0.47162679 | 0.027230673 | 5 |
| q0.minimum.oracle_risk_gap | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 366 | 366 | 366 | 1719 | 1014 | 766.2 | 602.0201 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 457 | 457 | 457 | 2148 | 1267 | 957.2 | 752.42621 | 5 |
| q0.oracle.maximum_coverage | 0.38532884 | 0.38532884 | 0.38532884 | 0.4422483 | 0.4525 | 0.41014696 | 0.034176358 | 5 |
| q0.shared.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.shared.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.shared.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q1.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.minimum.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.minimum.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.minimum.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.minimum.error_minus_target | 0.34895666 | 0.40225443 | 0.48681319 | 0.39372027 | 0.34895666 | 0.39614024 | 0.056385732 | 5 |
| q1.minimum.oracle_risk_gap | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1405 | 1235 | 1140 | 427 | 1405 | 1122.4 | 405.06024 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1756 | 1543 | 1425 | 533 | 1756 | 1402.6 | 506.50795 | 5 |
| q1.oracle.maximum_coverage | 0.56372392 | 0.49694042 | 0.39148352 | 0.50713606 | 0.56372392 | 0.50460157 | 0.070448056 | 5 |
| q1.shared.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.shared.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.shared.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| question_mean.minimum.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.47452638 | 0.44113463 | 0.38840618 | 0.47469218 | 0.50811196 | 0.45737426 | 0.045245833 | 5 |
| question_mean.shared.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |

### question_plus_explanation / frequency / 10%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| shared.worst_risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| shared.error_minus_target | 0.59139966 | 0.59139966 | 0.59139966 | 0.54607783 | 0.53785714 | 0.57162679 | 0.027230673 | 5 |
| q0.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.minimum.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.minimum.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.minimum.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.minimum.error_minus_target | 0.59139966 | 0.59139966 | 0.59139966 | 0.54607783 | 0.53785714 | 0.57162679 | 0.027230673 | 5 |
| q0.minimum.oracle_risk_gap | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 366 | 366 | 366 | 1719 | 1014 | 766.2 | 602.0201 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 406 | 406 | 406 | 1910 | 1126 | 850.8 | 669.17501 | 5 |
| q0.oracle.maximum_coverage | 0.34232715 | 0.34232715 | 0.34232715 | 0.39324686 | 0.40214286 | 0.36447423 | 0.030488806 | 5 |
| q0.shared.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.shared.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.shared.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q1.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.minimum.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.minimum.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.minimum.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.minimum.error_minus_target | 0.44895666 | 0.50225443 | 0.58681319 | 0.49372027 | 0.44895666 | 0.49614024 | 0.056385732 | 5 |
| q1.minimum.oracle_risk_gap | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1405 | 1235 | 1140 | 427 | 1405 | 1122.4 | 405.06024 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 1561 | 1372 | 1266 | 474 | 1561 | 1246.8 | 450.19629 | 5 |
| q1.oracle.maximum_coverage | 0.5011236 | 0.44186795 | 0.3478022 | 0.45099905 | 0.5011236 | 0.44858328 | 0.062707112 | 5 |
| q1.shared.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.shared.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.shared.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| question_mean.minimum.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.42172537 | 0.39209755 | 0.34506467 | 0.42212295 | 0.45163323 | 0.40652876 | 0.04029461 | 5 |
| question_mean.shared.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |

### question_plus_explanation / frequency / 30%

| Metric | Fold 0 | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Mean | Sample SD | Defined folds |
|---|---|---|---|---|---|---|---|---|
| candidate_count | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared_feasible_count | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| joint.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| joint.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| shared.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| shared.worst_risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| shared.error_minus_target | 0.39139966 | 0.39139966 | 0.39139966 | 0.34607783 | 0.33785714 | 0.37162679 | 0.027230673 | 5 |
| q0.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q0.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.minimum.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.minimum.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.minimum.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.minimum.error_minus_target | 0.39139966 | 0.39139966 | 0.39139966 | 0.34607783 | 0.33785714 | 0.37162679 | 0.027230673 | 5 |
| q0.minimum.oracle_risk_gap | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q0.oracle.original_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.oracle.correct_n | 366 | 366 | 366 | 1719 | 1014 | 766.2 | 602.0201 | 5 |
| q0.oracle.coverage_minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_n | 119 | 119 | 119 | 486 | 280 | 224.6 | 161.90522 | 5 |
| q0.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q0.oracle.maximum_retained_n | 522 | 522 | 522 | 2455 | 1448 | 1093.8 | 860.11464 | 5 |
| q0.oracle.maximum_coverage | 0.44013491 | 0.44013491 | 0.44013491 | 0.50545604 | 0.51714286 | 0.46860072 | 0.039196816 | 5 |
| q0.shared.retained_n | 1186 | 1186 | 1186 | 4857 | 2800 | 2243 | 1619.7988 | 5 |
| q0.shared.incorrect_n | 820 | 820 | 820 | 3138 | 1786 | 1476.8 | 1018.4975 | 5 |
| q0.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q0.shared.risk | 0.69139966 | 0.69139966 | 0.69139966 | 0.64607783 | 0.63785714 | 0.67162679 | 0.027230673 | 5 |
| q1.histogram.000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.010 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.101 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.histogram.110 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.histogram.111 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.total | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.count_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.coverage_pass | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.risk_pass | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.both_floors | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.counts.all_three | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.count_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.coverage_only_failure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.counts.risk_only_failure | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 5 |
| q1.minimum.threshold | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.minimum.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.minimum.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.minimum.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.minimum.error_minus_target | 0.24895666 | 0.30225443 | 0.38681319 | 0.29372027 | 0.24895666 | 0.29614024 | 0.056385732 | 5 |
| q1.minimum.oracle_risk_gap | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| q1.oracle.original_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.oracle.correct_n | 1405 | 1235 | 1140 | 427 | 1405 | 1122.4 | 405.06024 | 5 |
| q1.oracle.coverage_minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_n | 312 | 311 | 364 | 106 | 312 | 281 | 100.41912 | 5 |
| q1.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| q1.oracle.maximum_retained_n | 2007 | 1764 | 1628 | 610 | 2007 | 1603.2 | 578.58163 | 5 |
| q1.oracle.maximum_coverage | 0.64430177 | 0.56811594 | 0.44725275 | 0.58039962 | 0.64430177 | 0.57687437 | 0.080597472 | 5 |
| q1.shared.retained_n | 3115 | 3105 | 3640 | 1051 | 3115 | 2805.2 | 1006.9683 | 5 |
| q1.shared.incorrect_n | 1710 | 1870 | 2500 | 624 | 1710 | 1682.8 | 675.53623 | 5 |
| q1.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| q1.shared.risk | 0.54895666 | 0.60225443 | 0.68681319 | 0.59372027 | 0.54895666 | 0.59614024 | 0.056385732 | 5 |
| question_mean.minimum.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.minimum.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| question_mean.minimum.oracle_risk_gap | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.oracle.minimum_risk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| question_mean.oracle.maximum_coverage | 0.54221834 | 0.50412542 | 0.44369383 | 0.54292783 | 0.58072231 | 0.52273755 | 0.051825916 | 5 |
| question_mean.shared.risk | 0.62017816 | 0.64682705 | 0.68910642 | 0.61989905 | 0.5934069 | 0.63388352 | 0.036189995 | 5 |
| question_mean.shared.coverage | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |

## Execution checks

Runtime: 535.172 seconds. Pre-run revision: `ec4ed262bb8d63a0ad8bd38e6142ca8b28cbcf33`. Reproduced development policies: 90/90. Preserved files: 95. Outer-evaluation prediction calls: 0. No response-level outputs or candidate arrays serialized.
