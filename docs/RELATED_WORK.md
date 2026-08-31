# Related-work audit

## Primary dataset work

Rittle-Johnson et al. introduce the MAP benchmark: 52,463 expert-coded explanations across 15 middle-school items, with an explicit warning that synthetic paraphrases may over-represent particular concepts. The paper reports 24% double-coding and Cohen's κ of .70–.90; it does not establish real-world educator workflow effects. [Paper](https://aclanthology.org/2025.aimecon-wip.3/)

## What the competition already established

The 2025 MAP competition evaluated ranking quality using MAP@3, had 1,858 teams in final standings, and the private leaderboard's first-place score was 0.94919. It is therefore not credible to present a generic fine-tuned classifier or standard random cross-validation as novel. [Competition](https://www.kaggle.com/competitions/map-charting-student-math-misunderstandings), [final leaderboard](https://www.kaggle.com/c/map-charting-student-math-misunderstandings/leaderboard).

Public solution accounts show why leaderboard performance is insufficient for this study:

- The first-place write-up reports deduplication to 35,960 samples, five-fold splits stratified by `Category`, and candidate sets conditioned on each `QuestionId`—a setting that exploits known-question structure. [Write-up](https://www.kaggle.com/competitions/map-charting-student-math-misunderstandings/writeups/1st-place-solution)
- A top-3% solution states the test questions were present in training and reduced the target space using a per-question true/false map; it also filtered labels by question and used exact train–test matches. These are inappropriate for an unseen-problem study. [Solution repository](https://github.com/tossowski/MAP)
- A silver-medal Qwen3 solution used question, chosen answer, a train-derived correctness indicator, LoRA, and probability ensembling. This is a useful competitive reference, but its prompt feature requires special leakage controls under grouped evaluation. [Solution repository](https://github.com/chenfeng-huang/Kaggle_Silver_Medal_Solution_MAP)

## Uncertainty and selective prediction

Selective prediction evaluates the decision to abstain or defer, rather than only classifying every response. Varshney, Mishra, and Baral show that naive maximum probability can be unreliable under distribution shift and test calibrated selective prediction in NLP. [Paper](https://arxiv.org/abs/2008.09371) The broader NLP uncertainty literature likewise treats calibration and out-of-distribution behavior as distinct evaluation questions. [Tutorial](https://research.google/pubs/uncertainty-estimation-for-natural-language-processing/)

## Precise contribution that remains defensible

This study should not claim a new misconception detector. Its contribution is an **evaluation protocol and evidence package**:

1. A frozen `QuestionId`-held-out test of generalization to unseen MAP problems, with an openly reported random-split comparison.
2. Leakage audits for question-conditioned answer keys, label candidate lists, exact duplicates, and synthetic-family overlap.
3. Post-hoc calibrated confidence and risk–coverage analysis on group-disjoint calibration data.
4. A simulated routing analysis: the model handles retained cases, and uncertain cases are referred for human review. This is not a study of teachers, time savings, learning outcomes, or real deployment.

## Remaining novelty risks

Only 15 items exist, so “unseen-problem” estimates have few independent groups and substantial variance. A group split alone cannot establish transfer to new curricula, grade bands, institutions, modalities, or authentic-only data. The paper must present this as a rigorous stress test of a small benchmark, not broad K–12 validation.
