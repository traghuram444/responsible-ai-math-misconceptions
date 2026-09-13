# Research review: unseen-question transfer and selective prediction

**Review date:** 2026-09-13

**Status:** active research; literature and design review before E006 execution.

**Scope:** this review adds context to E001–E005. It does not revise their results or constitute an E006 run.

## Research question and evidence boundary

The project investigates the **generalization of mathematical-misconception detection to unseen K–12 math questions, with uncertainty-aware human review**. Its current evidence comes from a much narrower setting: the author-published MAP release containing 36,696 explanations across 15 middle-school questions. The K–12 wording describes the research motivation; it is not a claim that the experiments validate performance throughout K–12 education. Dataset provenance and the local release fingerprint are documented in [DATA_AND_LICENSES.md](DATA_AND_LICENSES.md).

The original MAP paper describes 52,463 explanations, comprising 38,095 original explanations and 14,368 synthetic paraphrases. It reports item-specific rubrics developed by mathematics experts, rather than one universal scoring rubric. It also warns that paraphrasing can overrepresent particular concepts and recommends examining prediction performance by misconception and explanation origin. No student demographics were available. These properties justify a question-level transfer evaluation, but do not establish why any particular model fails. The paper's full-dataset composition must not be attributed automatically to the smaller public release. [Rittle-Johnson et al., 2025](https://aclanthology.org/2025.aimecon-wip.3/)

E001–E005 provide evidence about the tested lexical and generic embedding systems under the frozen protocol. They do not isolate mathematical reasoning, annotation ambiguity, label semantics, or data provenance as causal explanations. Those remain competing explanations requiring appropriately designed evidence.

## Search strategy and novelty assessment

The review used primary papers and official proceedings, with searches for combinations of “MAP,” “Misconception Annotation Project,” “unseen questions,” “question-held-out,” “generalization,” “selective prediction,” “calibration,” and “distribution shift.” It also followed direct methodological predecessors surfaced by those searches. Source claims were checked against paper abstracts or full text. Searches were conducted on 2026-09-13; this is a bounded narrative review, not a systematic review with an exhaustive screening protocol.

A substantial predecessor is **Generalizing Expert Misconception Diagnoses Through Common Wrong Answer Embedding**. Kolb, Farrar, and Pardos learn question-answer embeddings from learner answer sequences and use multinomial logistic regression to predict words in expert misconception diagnoses. Their evaluation explicitly holds out raters, topics, and questions. This differs from classifying MAP's explanation-level exact labels, but directly precludes a broad claim that unseen-question misconception transfer or embeddings with logistic regression are new contributions. [Kolb, Farrar, and Pardos, EDM 2019](https://files.eric.ed.gov/fulltext/ED599212.pdf)

The search did not identify a primary study matching this project's exact combination of the public MAP subset, frozen question-held-out evaluation, label-support decomposition, and selective prediction. Absence from these search results is not proof that no such study exists. The defensible contribution is the reproducible evidence package and its carefully limited findings, rather than a priority claim or a new classifier architecture.

## What selective prediction research already establishes

Selective prediction asks which predictions to retain when a system may abstain. Its established research questions include the trade-off between retained error and coverage, whether confidence separates correct from incorrect predictions, and how that behavior changes outside the training distribution.

Kamath, Jia, and Liang study selective question answering under domain shift. They find that maximum prediction probability can be overconfident on unknown-domain examples. A correctness calibrator trained using source data and a separate known out-of-domain distribution improves selection in their experiments. Their setting motivates independent calibration questions, but their positive results do not imply that the same routing behavior transfers to MAP. [Kamath, Jia, and Liang, ACL 2020](https://aclanthology.org/2020.acl-main.503/)

Varshney, Mishra, and Baral compare selective prediction methods across 17 NLP datasets and in-domain, out-of-domain, and adversarial settings. None consistently and substantially outperforms maximum probability across all settings. Method rankings also vary by task. This supports retaining a simple confidence reference and recording failures of additional routing signals, rather than treating extra complexity as evidence of improvement. [Varshney, Mishra, and Baral, Findings ACL 2022](https://aclanthology.org/2022.findings-acl.158/)

E006 therefore tests the empirical usefulness of established selection ideas in a specific transfer setting. It should not be described as introducing abstention, selective classification, or uncertainty estimation.

## Calibration, discrimination, and shift are different questions

Calibration concerns agreement between predicted probabilities and observed outcome frequencies. Confidence discrimination concerns whether correct predictions receive higher scores than incorrect predictions. A constant confidence can match overall accuracy while offering no useful ranking. Conversely, a useful ranking can be numerically miscalibrated. ECE, Brier score, correctness AUROC, and risk–coverage curves therefore answer related but distinct questions.

Temperature scaling is a simple post-processing calibration method supported by Guo and colleagues' experiments. Its use here is a protocol choice, not a guarantee that calibrated probabilities remain valid on every unseen question. The original study does not establish MAP-specific performance. [Guo et al., ICML 2017](https://proceedings.mlr.press/v70/guo17a.html)

Ovadia and colleagues evaluate uncertainty under dataset shift and find that traditional post-hoc calibration can fall short as the distribution changes. Their evidence supports measuring retained calibration directly instead of assuming that successful source calibration survives transfer. It does not prove that every method or every shifted dataset must fail. [Ovadia et al., NeurIPS 2019](https://papers.neurips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html)

Formal guarantees require additional assumptions. Conformal Risk Control's main result uses exchangeable, bounded, monotone loss functions and treats extensions to shift separately. E006's fixed-budget empirical curves do not implement that procedure and are not risk certificates. Group-disjoint calibration alone does not establish exchangeability between calibration questions and future questions. [Angelopoulos et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html)

## Support-aware routing: available information and limitations

The E006 proposal multiplies calibrated maximum probability by a normalized logarithm of the training count of the predicted exact label. That count is available at prediction time. The true held-out label and its support are not.

For a closed-set classifier, every predicted class belongs to its training class set. Consequently, the predicted class has positive support even when the example's true label was never observed in training. An unsupported example can receive a high-confidence prediction of a common class and obtain a large support-aware score. This follows from the score definition; it is not an E006 finding.

The multiplier should therefore be described as a training-frequency weighting of the prediction, not an unsupported-label detector. It may favor common predicted classes without recognizing unfamiliar mathematics. Whether it improves routing must be measured. Its numerical value is a ranking score, not a new calibrated probability; retained ECE and Brier must use the underlying calibrated class probabilities.

Actual support strata remain valid reporting groups after predictions are frozen. They must never enter routing. Under a closed-set exact-label evaluation, unsupported examples cannot have correct predictions. A calibration eligibility rule requiring both correct and incorrect predictions will therefore exclude that stratum by construction; reports should explicitly state the reason rather than silently dropping it.

## Average gains can conceal uneven retention

Jones and colleagues show that selective classification can improve average accuracy while magnifying group disparities, and can even reduce accuracy in some groups as more predictions are deferred. Their findings support reporting support-stratum retention alongside overall risk. They do not imply a demographic fairness conclusion for MAP, where the necessary demographic observations are unavailable. [Jones et al., ICLR 2021](https://openreview.net/pdf?id=N0M_4BkQ05i)

Fixed-budget ranking of held-out scores is a label-free retrospective batch policy. It is different from selecting an operational score threshold on calibration data and applying it unchanged to future arrivals. The distinction should be explicit when describing results. Neither approach permits choosing a favorable test threshold after inspecting correctness.

A relative risk improvement also does not establish sufficient absolute reliability. For illustration, reducing an error rate of approximately 0.624 by 0.05 leaves approximately 0.574 error. Meeting a relative utility criterion at that level would not justify automation. The human-review component is a routing simulation; no reviewer accuracy, workload savings, or student benefit has been measured.

## Implications for E006 and the public repository

The E006 protocol should be concrete before execution: deterministic tie handling, aggregation conventions, eligible calibration denominators, and the exact Boolean meaning of its success/failure conditions must be auditable. Terms such as “materially worse calibration” require a fixed definition or an explicit statement that they are descriptive. Any clarification should be dated and preserved before results are inspected.

The project's contribution can be stated as a reproducible stress test of misconception classification and simulated human-review routing on a small benchmark: nested selection, frozen question splits, comparisons with prevalence and random-split references, explicit label-support limits, and sanitized aggregate outputs. Negative results strengthen this contribution when their scope is stated precisely and competing explanations remain open.

This review recommends neither a classifier replacement nor a change to E001–E005. It supplies the literature basis and interpretation boundaries for the proposed E006 analysis. No E006 experiment was executed as part of this review.
