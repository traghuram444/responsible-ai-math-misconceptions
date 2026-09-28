"""E009 fixed five-feature correctness learner and nested question cross-fitting."""
from __future__ import annotations

from collections import Counter
from contextlib import contextmanager
import hashlib
import json
import warnings

import numpy as np
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler

from . import e001
from .data_contract import combined_label
from .threshold_transfer import canonical_question

RULES = ("learned_reliability", "confidence_only", "support_aware", "raw_confidence", "frequency")
VARIANTS = ("explanation_only", "question_plus_explanation")
FEATURES = ("raw_confidence", "raw_margin", "normalized_entropy", "predicted_label_support", "maximum_training_cosine")
ROUTER_PARAMS = dict(penalty="l2", C=1.0, solver="lbfgs", fit_intercept=True, tol=1e-4,
                     max_iter=2000, class_weight=None, random_state=20260831, n_jobs=1)


def crossfit_blocks(question_ids, fold):
    questions = {canonical_question(q) for q in question_ids}
    if len(questions) != 9 or fold not in range(5):
        raise ValueError("E009 requires nine training questions and a frozen fold.")
    ordered = sorted(questions, key=lambda q: (hashlib.sha256(
        f"E009|fold={fold}|QuestionId={q}|seed=20260831".encode()).hexdigest(), q))
    return tuple(tuple(ordered[start:start + 3]) for start in (0, 3, 6))


def text_view(frame):
    # Do not pass evaluation labels/identifiers into any prediction-time feature.
    return frame.loc[:, [c for c in ("StudentExplanation", "QuestionText") if c in frame.columns]]


def maximum_similarity(fitted, train, query, variant):
    vectorizer, _ = fitted
    reference = vectorizer.transform(e001.text_input(text_view(train), variant))
    matrix = vectorizer.transform(e001.text_input(text_view(query), variant))
    if reference.shape[0] == 0:
        raise ValueError("Empty training similarity reference.")
    maxima = np.empty(len(query), dtype=np.float64)
    for start in range(0, len(query), 128):
        product = matrix[start:start + 128] @ reference.T
        maxima[start:start + 128] = product.max(axis=1).toarray().ravel()
    if not np.isfinite(maxima).all():
        raise ValueError("Nonfinite similarity.")
    return np.clip(maxima, 0., 1.)


def numeric_features(probabilities, classes, training_labels, similarity):
    p, classes, similarity = np.asarray(probabilities, dtype=np.float64), np.asarray(classes), np.asarray(similarity)
    counts = Counter(training_labels)
    if (p.ndim != 2 or p.shape[1] != len(classes) or not len(p) or len(classes) == 0
            or similarity.shape != (len(p),) or set(classes) != set(counts)
            or not np.isfinite(p).all() or (p < 0).any() or (p > 1).any()
            or not np.allclose(p.sum(axis=1), 1., atol=1e-8, rtol=0)
            or not np.isfinite(similarity).all() or (similarity < 0).any() or (similarity > 1).any()):
        raise ValueError("Invalid reliability features.")
    first = p.max(axis=1)
    second = np.partition(p, -2, axis=1)[:, -2] if len(classes) > 1 else np.zeros(len(p))
    logp = np.zeros_like(p)
    np.log(p, out=logp, where=p > 0)
    entropy = -(p * logp).sum(axis=1) / np.log(len(classes)) if len(classes) > 1 else np.zeros(len(p))
    predicted = classes[p.argmax(axis=1)]
    support = np.log1p([counts[label] for label in predicted]) / np.log1p(max(counts.values()))
    result = np.column_stack((first, first - second, entropy, support, similarity))
    if not np.isfinite(result).all():
        raise ValueError("Nonfinite feature matrix.")
    return result


def features(fitted, train, query, variant, raw=None, classes=None):
    if raw is None:
        raw, classes = e001.predict(fitted, text_view(query), variant)
    return numeric_features(raw, classes, combined_label(train).to_numpy(),
                            maximum_similarity(fitted, train, query, variant))


def equal_question_weights(questions):
    canonical = [canonical_question(q) for q in questions]
    counts = Counter(canonical)
    if len(counts) != 9:
        raise ValueError("Router weighting requires nine questions.")
    return np.asarray([len(canonical) / (9 * counts[q]) for q in canonical], dtype=np.float64)


class ReliabilityModel:
    """Memory-only scaler/weights; public records contain status and counts only."""
    def __init__(self, scaler, model=None, constant=None):
        self.scaler, self.model, self.constant = scaler, model, constant

    def score(self, x):
        x = np.asarray(x, dtype=np.float64)
        if x.ndim != 2 or x.shape[1] != 5 or not np.isfinite(x).all():
            raise ValueError("Invalid router query.")
        transformed = self.scaler.transform(x)
        p = (np.full(len(x), self.constant, dtype=np.float64) if self.constant is not None else
             self.model.predict_proba(transformed)[:, list(self.model.classes_).index(1)])
        if not np.isfinite(p).all() or (p < 0).any() or (p > 1).any():
            raise ValueError("Invalid router probability.")
        return p


def fit_router(x, correct, questions):
    x, correct = np.asarray(x, dtype=np.float64), np.asarray(correct)
    if (x.shape != (len(correct), 5) or correct.dtype != bool or len(questions) != len(correct)
            or not len(correct) or not np.isfinite(x).all()):
        raise ValueError("Invalid router fitting inputs.")
    weights = equal_question_weights(questions)
    scaler = StandardScaler(with_mean=True, with_std=True).fit(x, sample_weight=weights)
    if not np.isfinite(scaler.mean_).all() or not np.isfinite(scaler.scale_).all():
        raise ValueError("Nonfinite scaler.")
    metadata = {"n": len(correct), "correct_n": int(correct.sum()), "incorrect_n": int((~correct).sum()),
                "question_count": 9, "feature_count": 5, "weight_sum": float(weights.sum()),
                "status": "FITTED", "constant": None, "fitting_calls": 1, "convergence_warnings": 0}
    if np.unique(correct).size == 1:
        constant = int(correct[0])
        metadata.update(status="CONSTANT_CORRECTNESS_FALLBACK", constant=constant, fitting_calls=0)
        return ReliabilityModel(scaler, constant=constant), metadata
    model = LogisticRegression(**ROUTER_PARAMS)
    with warnings.catch_warnings():
        warnings.simplefilter("error", ConvergenceWarning)
        model.fit(scaler.transform(x), correct.astype(int), sample_weight=weights)
    if not np.isfinite(model.coef_).all() or not np.isfinite(model.intercept_).all():
        raise ValueError("Nonfinite reliability fit.")
    return ReliabilityModel(scaler, model=model), metadata


@contextmanager
def counted_fits(live, label, prior_steps):
    """Wrap legacy fitting for honest counts/warnings, never alter its arguments."""
    original = e001.fit_tfidf_lr
    counts = dict(attempted=0, successful=0, failed=0, warnings=0, convergence_warnings=0)
    def wrapped(*args, **kwargs):
        counts["attempted"] += 1
        live.update(f"{label}: classifier fit {counts['attempted']}/10", completed=prior_steps + counts["attempted"] - 1)
        caught = []
        try:
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                result = original(*args, **kwargs)
            counts["successful"] += 1
            return result
        except Exception:
            counts["failed"] += 1
            raise
        finally:
            counts["warnings"] += len(caught)
            counts["convergence_warnings"] += sum(issubclass(w.category, ConvergenceWarning) for w in caught)
            live.update(f"{label}: classifier fit complete", completed=prior_steps + counts["attempted"])
    e001.fit_tfidf_lr = wrapped
    try:
        yield counts
    finally:
        e001.fit_tfidf_lr = original


def tuned_fit(train, variant, live, label, prior_steps):
    with counted_fits(live, label, prior_steps) as counts:
        selected = e001.score_params(train, variant, GroupKFold(3), groups=train.QuestionId.astype(str))
        fitted = e001.fit_tfidf_lr(train, variant, {**selected["params"], "ngram_range": tuple(selected["params"]["ngram_range"])})
    if counts["attempted"] != 10 or counts["successful"] + counts["failed"] != 10:
        raise ValueError("Unexpected classifier fit count.")
    return fitted, selected, counts


def crossfit_training(train, variant, fold, live, prior_steps):
    blocks = crossfit_blocks(train.QuestionId, fold)
    canonical = train.QuestionId.map(canonical_question).to_numpy()
    x, y, visits = np.empty((len(train), 5)), np.empty(len(train), bool), np.zeros(len(train), int)
    summaries = []
    for block, held_q in enumerate(blocks):
        held = np.isin(canonical, held_q)
        fit_rows, held_rows = train.iloc[np.flatnonzero(~held)], train.iloc[np.flatnonzero(held)]
        if fit_rows.QuestionId.nunique() != 6 or held_rows.QuestionId.nunique() != 3:
            raise ValueError("Cross-fit role mismatch.")
        fitted, selected, counts = tuned_fit(fit_rows, variant, live,
            f"{variant}, fold {fold + 1}/5, cross-fit {block + 1}/3", prior_steps + block * 10)
        live.update(f"{variant}, fold {fold + 1}/5: cross-fit {block + 1}/3 features")
        raw, classes = e001.predict(fitted, text_view(held_rows), variant)
        x[held] = features(fitted, fit_rows, held_rows, variant, raw, classes)
        correct = classes[raw.argmax(axis=1)] == combined_label(held_rows).to_numpy()
        y[held], visits[held] = correct, visits[held] + 1
        summaries.append({"block": block, "fitting_questions": 6, "held_questions": 3,
                          "fitting_n": len(fit_rows), "held_n": len(held_rows), "correct_n": int(correct.sum()),
                          "incorrect_n": int((~correct).sum()), "selected_hyperparameters": selected, "fits": counts})
    if not np.all(visits == 1):
        raise ValueError("Cross-fit rows are not held exactly once.")
    serial = json.dumps({"fold": fold, "blocks": blocks}, sort_keys=True, separators=(",", ":"))
    return x, y, {"role_sha256": hashlib.sha256(serial.encode()).hexdigest(), "blocks": summaries}
