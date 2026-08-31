# Data provenance and licensing register

## Decision: approved source is the author-published Kaggle release

The project uses **MAP (Misconception Annotation Project)**, the publicly downloadable Kaggle dataset published by `lburleigh`, rather than the now-closed competition download. This is not an unrelated re-upload: Kaggle identifies **L Burleigh** as the dataset owner and **Jules King** as its administrator; both are named in the competition citation and the original benchmark paper. The dataset page says the data were used in the MAP competition and displays an **MIT** license.

| Item | Verified finding | Source | Status |
|---|---|---|---|
| Dataset identity | MAP is Eedi's Misconception Annotation Project. The usable release is the author-published `lburleigh/math-misunderstandings-in-student-explanations` Kaggle dataset. | [author-published dataset](https://www.kaggle.com/datasets/lburleigh/math-misunderstandings-in-student-explanations), [benchmark paper](https://aclanthology.org/2025.aimecon-wip.3/) | Verified |
| Corpus construction | 52,463 labeled explanations across 15 middle-school math items; 38,095 authentic and 14,368 synthetic paraphrases. | [Rittle-Johnson et al., 2025, pp. 20–21](https://aclanthology.org/anthology-files/pdf/aimecon/2025.aimecon-wip.3.pdf) | Identified from primary paper |
| Labels | One human-assigned code per response; the project target is `Category:Misconception`. The literal string `NA` is a valid label, not a missing value. | [benchmark paper](https://aclanthology.org/anthology-files/pdf/aimecon/2025.aimecon-wip.3.pdf), [author-published dataset](https://www.kaggle.com/datasets/lburleigh/math-misunderstandings-in-student-explanations) | Verified locally |
| Privacy | The paper states explanations were screened for PII and that no demographics were available. This does not remove the need to protect raw responses. | [benchmark paper](https://aclanthology.org/anthology-files/pdf/aimecon/2025.aimecon-wip.3.pdf) | Documented |
| Author-release license | The author-published Kaggle dataset page displays MIT. MIT permits use, copying, modification, distribution, and private/commercial use subject to retaining the notice. This supports the planned independent research. | [author-published dataset](https://www.kaggle.com/datasets/lburleigh/math-misunderstandings-in-student-explanations), [MIT license text](https://opensource.org/license/mit) | Verified directly 2026-08-31 |
| Closed competition terms | The former competition Rules show CC BY-NC 4.0 and additional access restrictions. They conflict with the newer dataset-card MIT label; they do not govern this project’s data acquisition because the project downloads only the separate author-published release. | [competition rules](https://www.kaggle.com/competitions/map-charting-student-math-misunderstandings/rules) | Recorded conflict |

## Required provenance record before any modeling

This record is complete for the author release. Commit the record, not the dataset.

| Field | Required value |
|---|---|
| Authoritative source URL | `https://www.kaggle.com/datasets/lburleigh/math-misunderstandings-in-student-explanations` |
| Author identity evidence | Owner L Burleigh; admin Jules King. Both are competition-citation and benchmark-paper authors; Burleigh is a [Learning Agency data analyst](https://the-learning-agency.com/our-team/l-burleigh/). |
| Release evidence | Dataset says it was used in MAP competition, was last updated 10 months before inspection, and exposes only `train.csv`, not test data. This is strong evidence of an intentional author release, though not a substitute for an independent chain-of-title legal opinion. |
| Displayed data license / permitted uses | MIT; retain license/copyright notices. |
| Archive SHA-256 | `7412a9ce5b3c7e78dca12702d032acc85bad444c04e9be50b922985b078aa252` |
| Training CSV SHA-256 | `0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c` |
| Train CSV rows / columns / question count | 36,696 rows; 7 columns; 15 question groups. Inspection artifact: `artifacts/data_inspection.json`. |

## Expected training schema (to confirm from official `train.csv`)

The verified source contains `row_id`, `QuestionId`, `QuestionText`, `MC_Answer`, `StudentExplanation`, `Category`, and `Misconception`. The code requires the last six semantic fields; `row_id` is retained as source provenance. Any schema difference stops the pipeline rather than being silently coerced.

## Data handling

- Keep raw data in `data/raw/`; it is excluded from version control.
- Do not commit student text, per-row predictions, trained weights, competition test data, or any answer-key reconstruction derived from held-out questions, even though the author release is MIT-licensed.
- Do not use public/private leaderboard scores, competition test labels, or test-row matches as model-selection signals.
- Publish only aggregate statistics and carefully reviewed, permitted illustrative examples. If reuse terms do not explicitly permit examples, publish no raw text.
- Report authentic-versus-synthetic composition if the source exposes this field; otherwise state that it is unavailable at row level.

## Citation

Rittle-Johnson, B., Adler, R., Durkin, K., Burleigh, L., King, J., & Crossley, S. (2025). *Detecting Math Misconceptions: An AI Benchmark Dataset.* AIME-Con Works in Progress, 20–24. [ACL Anthology](https://aclanthology.org/2025.aimecon-wip.3/).

Also cite: King, J., Smith, K., Burleigh, L., Crossley, S., Demkin, M., & Reade, W. (2025). *MAP – Charting Student Math Misunderstandings.* Kaggle, and the author-published dataset URL above.
