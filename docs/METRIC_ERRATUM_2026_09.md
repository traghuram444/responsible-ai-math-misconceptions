# Historical Brier metric erratum — 2026-09-13

This is an **append-only arithmetic correction**, not a new experiment or a rerun. E001–E005 original files remain unchanged. Values below are equal-weight five-fold means.

## Error and effect

The original scorer omitted the one-hot true-label contribution when that label was absent from the model's class set. Proper multiclass Brier (sum over outcome labels, range 0–2) equals the legacy score **plus the unsupported true-label fraction**. See `metrics_v2.py` and its synthetic tests.

MAP@3, top-1 accuracy and ECE are unaffected. Brier on supported-only subsets is unaffected. Same-fold learned-minus-frequency Brier differences cancel the correction when evaluated on the same population/class support. That cancellation need not hold for differently retained subsets in E006. Neither score is a pure measure of calibration alone.

## All-row correction tables

| Experiment | Split | Input | Model | Legacy Brier | Added unsupported share | Corrected Brier | Corrected SD |
|---|---|---|---|---:|---:|---:|---:|
| E001 | QuestionId-grouped | explanation_only | frequency_baseline | 0.581666 | 0.213391 | 0.795057 | 0.028763 |
| E001 | QuestionId-grouped | explanation_only | tfidf_logreg | 0.619925 | 0.213391 | 0.833316 | 0.052998 |
| E001 | QuestionId-grouped | question_plus_explanation | frequency_baseline | 0.581666 | 0.213391 | 0.795057 | 0.028763 |
| E001 | QuestionId-grouped | question_plus_explanation | tfidf_logreg | 0.592337 | 0.213391 | 0.805728 | 0.044888 |
| E001 | stratified-random-reference-only | explanation_only | frequency_baseline | 0.780231 | 0.000245 | 0.780476 | 0.000165 |
| E001 | stratified-random-reference-only | explanation_only | tfidf_logreg | 0.480070 | 0.000245 | 0.480315 | 0.004263 |
| E001 | stratified-random-reference-only | question_plus_explanation | frequency_baseline | 0.780231 | 0.000245 | 0.780476 | 0.000165 |
| E001 | stratified-random-reference-only | question_plus_explanation | tfidf_logreg | 0.453075 | 0.000245 | 0.453320 | 0.005008 |
| E004 | QuestionId-grouped | explanation_only | embedding_logreg | 0.636337 | 0.213391 | 0.849728 | 0.060761 |
| E004 | QuestionId-grouped | explanation_only | frequency_baseline | 0.581666 | 0.213391 | 0.795057 | 0.028763 |
| E004 | QuestionId-grouped | question_plus_explanation | embedding_logreg | 0.666088 | 0.213391 | 0.879479 | 0.049730 |
| E004 | QuestionId-grouped | question_plus_explanation | frequency_baseline | 0.581666 | 0.213391 | 0.795057 | 0.028763 |
| E005 | QuestionId-grouped | explanation_only | frequency_baseline | 0.581666 | 0.213391 | 0.795057 | 0.028763 |
| E005 | QuestionId-grouped | explanation_only | tfidf_logreg | 0.619925 | 0.213391 | 0.833316 | 0.052998 |
| E005 | QuestionId-grouped | question_plus_explanation | frequency_baseline | 0.581666 | 0.213391 | 0.795057 | 0.028763 |
| E005 | QuestionId-grouped | question_plus_explanation | tfidf_logreg | 0.592337 | 0.213391 | 0.805728 | 0.044888 |
| E005 | stratified-random-reference-only | explanation_only | frequency_baseline | 0.780231 | 0.000245 | 0.780476 | 0.000165 |
| E005 | stratified-random-reference-only | explanation_only | tfidf_logreg | 0.480070 | 0.000245 | 0.480315 | 0.004263 |
| E005 | stratified-random-reference-only | question_plus_explanation | frequency_baseline | 0.780231 | 0.000245 | 0.780476 | 0.000165 |
| E005 | stratified-random-reference-only | question_plus_explanation | tfidf_logreg | 0.453075 | 0.000245 | 0.453320 | 0.005008 |

## Fold-level arithmetic

E001 and E005 corresponding overall values agree within 1e-12 in all 200 checked scalar metrics. Their duplicated corrections are serialized locally; the E001 and E004 fold rows are shown here.

| Experiment | Split | Input | Fold | Model | Legacy | Added share | Corrected |
|---|---|---|---:|---|---:|---:|---:|
| E001 | QuestionId-grouped | explanation_only | 0 | frequency_baseline | 0.702901 | 0.052953 | 0.755854 |
| E001 | QuestionId-grouped | explanation_only | 0 | tfidf_logreg | 0.823163 | 0.052953 | 0.876117 |
| E001 | QuestionId-grouped | explanation_only | 1 | frequency_baseline | 0.593851 | 0.229674 | 0.823525 |
| E001 | QuestionId-grouped | explanation_only | 1 | tfidf_logreg | 0.673575 | 0.229674 | 0.903249 |
| E001 | QuestionId-grouped | explanation_only | 2 | frequency_baseline | 0.528804 | 0.264985 | 0.793789 |
| E001 | QuestionId-grouped | explanation_only | 2 | tfidf_logreg | 0.539191 | 0.264985 | 0.804176 |
| E001 | QuestionId-grouped | explanation_only | 3 | frequency_baseline | 0.517241 | 0.304894 | 0.822135 |
| E001 | QuestionId-grouped | explanation_only | 3 | tfidf_logreg | 0.495832 | 0.304894 | 0.800726 |
| E001 | QuestionId-grouped | explanation_only | 4 | frequency_baseline | 0.565533 | 0.214450 | 0.779983 |
| E001 | QuestionId-grouped | explanation_only | 4 | tfidf_logreg | 0.567864 | 0.214450 | 0.782313 |
| E001 | stratified-random-reference-only | explanation_only | 0 | frequency_baseline | 0.780241 | 0.000136 | 0.780377 |
| E001 | stratified-random-reference-only | explanation_only | 0 | tfidf_logreg | 0.483048 | 0.000136 | 0.483184 |
| E001 | stratified-random-reference-only | explanation_only | 1 | frequency_baseline | 0.780290 | 0.000136 | 0.780426 |
| E001 | stratified-random-reference-only | explanation_only | 1 | tfidf_logreg | 0.482911 | 0.000136 | 0.483047 |
| E001 | stratified-random-reference-only | explanation_only | 2 | frequency_baseline | 0.780274 | 0.000409 | 0.780683 |
| E001 | stratified-random-reference-only | explanation_only | 2 | tfidf_logreg | 0.482277 | 0.000409 | 0.482686 |
| E001 | stratified-random-reference-only | explanation_only | 3 | frequency_baseline | 0.780063 | 0.000545 | 0.780608 |
| E001 | stratified-random-reference-only | explanation_only | 3 | tfidf_logreg | 0.478912 | 0.000545 | 0.479457 |
| E001 | stratified-random-reference-only | explanation_only | 4 | frequency_baseline | 0.780287 | 0.000000 | 0.780287 |
| E001 | stratified-random-reference-only | explanation_only | 4 | tfidf_logreg | 0.473199 | 0.000000 | 0.473199 |
| E001 | QuestionId-grouped | question_plus_explanation | 0 | frequency_baseline | 0.702901 | 0.052953 | 0.755854 |
| E001 | QuestionId-grouped | question_plus_explanation | 0 | tfidf_logreg | 0.793236 | 0.052953 | 0.846189 |
| E001 | QuestionId-grouped | question_plus_explanation | 1 | frequency_baseline | 0.593851 | 0.229674 | 0.823525 |
| E001 | QuestionId-grouped | question_plus_explanation | 1 | tfidf_logreg | 0.619092 | 0.229674 | 0.848766 |
| E001 | QuestionId-grouped | question_plus_explanation | 2 | frequency_baseline | 0.528804 | 0.264985 | 0.793789 |
| E001 | QuestionId-grouped | question_plus_explanation | 2 | tfidf_logreg | 0.525748 | 0.264985 | 0.790732 |
| E001 | QuestionId-grouped | question_plus_explanation | 3 | frequency_baseline | 0.517241 | 0.304894 | 0.822135 |
| E001 | QuestionId-grouped | question_plus_explanation | 3 | tfidf_logreg | 0.498197 | 0.304894 | 0.803090 |
| E001 | QuestionId-grouped | question_plus_explanation | 4 | frequency_baseline | 0.565533 | 0.214450 | 0.779983 |
| E001 | QuestionId-grouped | question_plus_explanation | 4 | tfidf_logreg | 0.525411 | 0.214450 | 0.739861 |
| E001 | stratified-random-reference-only | question_plus_explanation | 0 | frequency_baseline | 0.780241 | 0.000136 | 0.780377 |
| E001 | stratified-random-reference-only | question_plus_explanation | 0 | tfidf_logreg | 0.456000 | 0.000136 | 0.456136 |
| E001 | stratified-random-reference-only | question_plus_explanation | 1 | frequency_baseline | 0.780290 | 0.000136 | 0.780426 |
| E001 | stratified-random-reference-only | question_plus_explanation | 1 | tfidf_logreg | 0.455906 | 0.000136 | 0.456042 |
| E001 | stratified-random-reference-only | question_plus_explanation | 2 | frequency_baseline | 0.780274 | 0.000409 | 0.780683 |
| E001 | stratified-random-reference-only | question_plus_explanation | 2 | tfidf_logreg | 0.456858 | 0.000409 | 0.457267 |
| E001 | stratified-random-reference-only | question_plus_explanation | 3 | frequency_baseline | 0.780063 | 0.000545 | 0.780608 |
| E001 | stratified-random-reference-only | question_plus_explanation | 3 | tfidf_logreg | 0.451528 | 0.000545 | 0.452073 |
| E001 | stratified-random-reference-only | question_plus_explanation | 4 | frequency_baseline | 0.780287 | 0.000000 | 0.780287 |
| E001 | stratified-random-reference-only | question_plus_explanation | 4 | tfidf_logreg | 0.445083 | 0.000000 | 0.445083 |
| E004 | QuestionId-grouped | explanation_only | 0 | frequency_baseline | 0.702901 | 0.052953 | 0.755854 |
| E004 | QuestionId-grouped | explanation_only | 0 | embedding_logreg | 0.816306 | 0.052953 | 0.869260 |
| E004 | QuestionId-grouped | explanation_only | 1 | frequency_baseline | 0.593851 | 0.229674 | 0.823525 |
| E004 | QuestionId-grouped | explanation_only | 1 | embedding_logreg | 0.691599 | 0.229674 | 0.921273 |
| E004 | QuestionId-grouped | explanation_only | 2 | frequency_baseline | 0.528804 | 0.264985 | 0.793789 |
| E004 | QuestionId-grouped | explanation_only | 2 | embedding_logreg | 0.540990 | 0.264985 | 0.805975 |
| E004 | QuestionId-grouped | explanation_only | 3 | frequency_baseline | 0.517241 | 0.304894 | 0.822135 |
| E004 | QuestionId-grouped | explanation_only | 3 | embedding_logreg | 0.465346 | 0.304894 | 0.770240 |
| E004 | QuestionId-grouped | explanation_only | 4 | frequency_baseline | 0.565533 | 0.214450 | 0.779983 |
| E004 | QuestionId-grouped | explanation_only | 4 | embedding_logreg | 0.667444 | 0.214450 | 0.881894 |
| E004 | QuestionId-grouped | question_plus_explanation | 0 | frequency_baseline | 0.702901 | 0.052953 | 0.755854 |
| E004 | QuestionId-grouped | question_plus_explanation | 0 | embedding_logreg | 0.892747 | 0.052953 | 0.945700 |
| E004 | QuestionId-grouped | question_plus_explanation | 1 | frequency_baseline | 0.593851 | 0.229674 | 0.823525 |
| E004 | QuestionId-grouped | question_plus_explanation | 1 | embedding_logreg | 0.614691 | 0.229674 | 0.844365 |
| E004 | QuestionId-grouped | question_plus_explanation | 2 | frequency_baseline | 0.528804 | 0.264985 | 0.793789 |
| E004 | QuestionId-grouped | question_plus_explanation | 2 | embedding_logreg | 0.648972 | 0.264985 | 0.913956 |
| E004 | QuestionId-grouped | question_plus_explanation | 3 | frequency_baseline | 0.517241 | 0.304894 | 0.822135 |
| E004 | QuestionId-grouped | question_plus_explanation | 3 | embedding_logreg | 0.520173 | 0.304894 | 0.825066 |
| E004 | QuestionId-grouped | question_plus_explanation | 4 | frequency_baseline | 0.565533 | 0.214450 | 0.779983 |
| E004 | QuestionId-grouped | question_plus_explanation | 4 | embedding_logreg | 0.653861 | 0.214450 | 0.868310 |

## Scope and provenance

The mean-fold grouped correction is 0.213391; the pooled row fraction is 7755/36696 = 0.211331. Using the latter to correct an equal-fold mean would be incorrect. E003's all-row references reproduce E001; its supported-only Brier needs no correction. E002 contains no classifier Brier. No correction is inferred for an unrecorded retained subset; that requires its own unsupported share.

The historical E001 prose also reports explanation-only grouped Brier as 0.605; its serialized legacy value is 0.619925. The table above uses the artifact, not that prose typo.

Reproduce with `python scripts/audit_brier_aggregates.py` from the existing local artifacts. The new ignored JSON is `artifacts/brier_erratum_2026_09.json`. No raw examples or row-level predictions are read or written. This table does not fill missing E004/E005 preregistered analyses. See [the full audit](REPRODUCIBILITY_AUDIT_2026_09.md).

- `e001_results.json`: `dc06418b3120f3b4e4293b696c66d6f1b5cf00f59eba615640c97770f388df99`
- `e004_results.json`: `1a79ae7bc541ba4984e42831c8673328c774bd472a359b24374962efed37e8bd`
- `e005_results_final.json`: `b69cda4fd8ce9d412da443d5d5728b16542fd3758ba195b34305b0e3069663e9`
