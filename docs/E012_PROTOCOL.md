# E012 conditional character based Complement Naive Bayes

## Conditional authorization and hypothesis

Preregistered together with E011, before seeing either outcome, under the user's instruction to proceed to another model if E011 fails. Run exactly once **only if** E011 completes, its reproduction/preservation/publication checks pass, and its H1 criterion is false. Operational failures do not trigger E012. Publish E011 unchanged first. Stop after E012 regardless of score.

Hypothesis: a character-based complement classifier with full question/selected-answer/explanation context better transfers exact labels than word-based logistic regression under the same frozen outer evaluation. Character n-grams preserve short numeric and spelling fragments omitted by the E001 word tokenizer; complement statistics offer a different treatment of imbalanced text classes. This is a **joint representation/classifier alternative**, not an isolated causal test of either component or a mathematical reasoning model.

Primary criterion: E012's full-context MAP@3 must exceed both E011's full-context logistic arm and frequency by mean >=0.020, with positive deltas in >=4/5 folds against each. Exact unrounded decision; no secondary substitution. All fold variation remains descriptive, not inferential. Missing this criterion is a preserved negative result; it does not license E013.

## Fixed model and evaluation

Use only E011's `full_context` input. TfidfVectorizer with analyzer=`char_wb`, sublinear_tf=True, min_df=2, max_features=100000, other scikit-learn 1.5.2 defaults. Grid order: ngram_range (2,5) then (3,5), each with ComplementNB alpha 0.1, 1.0, 10.0 in that order. ComplementNB norm=True, fit_prior=False, force_alpha=True; no class or question identifiers as features. Maximum-feature selection, vocabulary and IDF fit only inner training text.

Select among these six settings with the same GroupKFold(3) and inner MAP@3 rule as E011, first grid entry on exact ties; refit on nine training questions. This gives 95 fits (six settings times three inner folds plus one final fit, times five outer folds). Calibration is the identical E001 temperature function on the same three calibration questions, not tuning on outer questions. ComplementNB probability quality may be poor; temperature fitting is not a guarantee that it repairs this. No architecture, alpha, tokenizer, feature-cap or calibration search beyond the fixed grid.

All frozen input, prediction-time feature, global preparation barrier, no-row-output, publication, monitor and integrity requirements in [E011](E011_PROTOCOL.md) apply. Use the same locked CPU image. Compare frequency reference metrics against the existing reference and require its complete new fold/question summaries to match E011. Pin the completed E011 aggregate artifact before launching; inspect its primary decision programmatically, not manually overriding the trigger.

Report exactly the same exact-label, Category, support, calibration, per-question and confidence risk–coverage outputs. The Category macro-F1 explicitly uses all six labels. No random-split rerun, fine-tuned transformer, generated rubric, threshold optimization or new dataset. Pair E012 with E011 full context for all-row accuracy/MAP@3/ECE/Brier and with frequency; publish full aggregate/fold/question tables before interpretation. No new resampling or significance test.

Expected compute: approximately 5–20 minutes, CPU, with uncertainty from character vocabulary and memory usage; no timing pilot. A resource failure is not scientific failure. Results cannot attribute a gain separately to character features versus the classifier. Even success would require fresh questions before stronger generalization claims.

## Prior art and limits

Complement Naive Bayes is established work on imbalanced text classification, not a novel architecture. It is included as a fixed, computationally bounded alternative rather than a claim that it will beat logistic regression on MAP. Its probability estimates require direct evaluation. [Rennie et al., ICML 2003](https://people.csail.mit.edu/jrennie/papers/icml03-nb.pdf), [scikit-learn 1.5 documentation](https://scikit-learn.org/1.5/modules/naive_bayes.html#complement-naive-bayes)
