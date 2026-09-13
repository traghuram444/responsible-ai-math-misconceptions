# E006 preregistration — selective prediction under unseen-question transfer

**Status:** proposed; awaiting review. No E006 run has started.

## Research question

Under held-question transfer, can a model identify a subset of predictions sufficiently reliable for automated routing while deferring uncertain, unsupported, or distribution-shifted cases for human review?

E006 is a diagnostic of routing reliability. It does not claim that abstention works, and it does not introduce a new representation or classifier.

## Fixed framework and models

- Reuse the E001 frozen five-fold `QuestionId` assignments, data fingerprint, seed, train/calibration/evaluation roles, inner-only hyperparameter selection, and group-disjoint temperature scaling exactly.
- Reproduce both registered E001 TF–IDF + logistic-regression input arms: explanation-only and question-plus-explanation.
- Reproduce the fold-local frequency baseline for every fold.
- Recompute fold-local probabilities only in memory. Write aggregate curves/tables only—never student text, row-level probabilities, rankings, or predictions.

## Confirmatory routing rules

Each rule ranks evaluation cases before applying the fixed review budgets below. Higher score means retain for automation; lower score means defer.

1. **Confidence-only:** calibrated maximum predicted probability.
2. **Support-aware confidence:** calibrated maximum probability multiplied by normalized `log(1 + n)` for the *predicted* exact label, where `n` is that label's count in the fold-local training role and normalization divides by the maximum such log count among model classes. This is available at prediction time; it never uses the true evaluation label.
3. **Frequency baseline:** frequency model maximum probability. Ties are resolved by a fixed SHA-256 hash of `(fold, source_row, seed)`, used only to make a deterministic ordering and never as a feature.

The support-aware rule is a predeclared diagnostic, not an oracle for actual unsupported labels. Actual support strata are reporting strata only and are never used for routing.

## Fixed review budgets and outcomes

At 0%, 10%, 20%, 30%, 40%, and 50% review, defer the lowest-ranked cases and report:

- retained coverage and count;
- retained top-1 accuracy, MAP@3, and risk (`1 − accuracy`);
- absolute risk reduction from 0% review;
- ECE and Brier on retained predictions only when the preregistered eligibility rule is met: at least 200 retained rows and at least 20 correct and 20 incorrect top-1 predictions;
- the same quantities within actual Unsupported, Frequent, and Well-supported exact-label strata, where counts meet eligibility. Rare is reported if non-empty; otherwise explicitly reported as zero.

## Confidence-separation analysis

For each learned arm, report fold-level AUROC of confidence for distinguishing correct versus incorrect top-1 predictions, and a descriptive five-fold mean/SD. AUROC is reported only when both outcomes occur in a fold. This tests separation, not calibration.

## Frequency comparison

All routing curves and fixed-budget tables include frequency. Frequency's confidence is normally constant; its deterministic tie rule makes this an explicit no-information routing reference rather than an implied selective system.

## Threshold safeguards

- Review budgets are fixed before execution. No retained-accuracy target, risk target, or held-out-derived score threshold may be selected.
- Temperature scaling remains fitted only on the group-disjoint calibration role.
- The support-aware training-count factor is fixed above; no exponent, cutoff, reweighting, or learned combination may be adjusted after results.
- No true evaluation label, actual support stratum, per-question result, or E005 outcome is available to any routing score.

## Confirmatory analyses

1. Full held-question risk–coverage curves for all three routing rules and both TF–IDF input arms.
2. Fixed-budget retained metrics and risk reduction versus 0% review.
3. Confidence AUROC for correct-versus-incorrect separation.
4. Fixed actual-support-stratum reporting, including unsupported, frequent, well-supported, and rare-if-nonempty groups.
5. Retained calibration under the stated eligibility rule.

## Exploratory analyses

Any alternative uncertainty score (entropy, margin, nearest-neighbor distance), question-specific threshold, different review budget, hybrid rule, or qualitative error review is exploratory and cannot be used for a confirmatory claim without a new preregistration.

## Failure conditions and informative outcomes

E006 fails as a selective-prediction method if, for either learned arm, 50% review does not reduce mean held-question risk by at least 0.05 absolute from 0% review **and** does not outperform the frequency routing reference at the same coverage. It also fails if retained ECE/Brier is materially worse than frequency in eligible strata. A negative result would show that model confidence does not separate reliable from unreliable unseen-question predictions sufficiently for automated routing.

Even if retained accuracy improves, E006 must not claim deployment readiness: results remain a simulated routing analysis on 15 middle-school questions.
