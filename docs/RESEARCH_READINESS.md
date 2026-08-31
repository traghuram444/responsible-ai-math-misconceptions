# Research-readiness report

## Recommendation: data access and baseline readiness confirmed

The project has a defensible angle only if it treats leaderboard methods as prior art and evaluates **question-held-out transfer plus calibrated deferral**. The scaffold now fixes that direction. Do not train a large model yet.

## Evidence established

- The authoritative benchmark paper describes 52,463 explanations over 15 middle-school questions, including 14,368 synthetic paraphrases; this makes question grouping essential and leaves only a small number of independent evaluation groups. [Paper](https://aclanthology.org/2025.aimecon-wip.3/)
- MAP's competition task is ranking `Category:Misconception` predictions using MAP@3; the final leaderboard was highly competitive. [Competition](https://www.kaggle.com/competitions/map-charting-student-math-misunderstandings), [leaderboard](https://www.kaggle.com/c/map-charting-student-math-misunderstandings/leaderboard)
- Winning and medal solutions commonly exploit known-question signals (candidate labels, answer correctness, exact matches, or known test questions). Those mechanisms are disallowed in the project’s primary split. [First-place write-up](https://www.kaggle.com/competitions/map-charting-student-math-misunderstandings/writeups/1st-place-solution), [top-3% solution](https://github.com/tossowski/MAP)

## Blocker before model fitting

The closed competition rules are not the acquisition source. The author-published Kaggle dataset owned by L Burleigh and administered by Jules King is independently downloadable and displays MIT; both maintainers are named MAP authors. This provenance is sufficient for the planned independent research, but it does not prove every upstream rights agreement. The project retains a conservative raw-data handling policy and records the conflict with the closed competition’s CC BY-NC terms. Do **not** substitute unrelated reuploads.

## First experiment

Run E001: class-frequency baseline and TF–IDF + multinomial logistic regression, in explanation-only and question-plus-explanation forms, on the frozen five-fold `QuestionId` split. Use only fold-local preprocessing; fit temperature scaling on the inner group-disjoint calibration split. Report grouped versus random-split performance, label-support gaps, ECE/Brier, and the specified 0–50% review curve.

## Go/no-go criterion for expensive modeling

Proceed to a transformer only if E001 runs cleanly, shows a meaningful grouped-vs-random gap worth studying, and its risk–coverage curve can be reproduced across outer folds. Otherwise, refine the protocol or collect broader data rather than scaling the model.
