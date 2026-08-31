"""Aggregate-only diagnostics for unseen-question evaluation."""

from __future__ import annotations

from pathlib import Path
import hashlib
import unicodedata

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

from .data_contract import combined_label, file_sha256


def normalize_explanation(value: object) -> str:
    """Normalize locally for comparison only; never emit normalized text."""
    text = unicodedata.normalize("NFKC", str(value)).casefold()
    return " ".join(text.split())


def manifest_sha256(path: Path) -> str:
    return file_sha256(path)


def analyze_fold(frame: pd.DataFrame, roles: pd.Series) -> dict[str, object]:
    """Measure support and train-to-evaluation text proximity without saving text."""
    train = frame.loc[roles.eq("train")].copy()
    evaluation = frame.loc[roles.eq("evaluation")].copy()
    if train.empty or evaluation.empty:
        raise ValueError("Each diagnostic fold needs non-empty train and evaluation roles.")

    train_labels = set(combined_label(train))
    eval_labels = combined_label(evaluation)
    unsupported = ~eval_labels.isin(train_labels)

    train_normalized = train["StudentExplanation"].map(normalize_explanation)
    eval_normalized = evaluation["StudentExplanation"].map(normalize_explanation)
    exact_matches = eval_normalized.isin(set(train_normalized))

    # Fixed before execution: character 3–5 gram TF–IDF, fitted only on the
    # train role, then nearest-neighbor similarity for held-out responses.
    vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), min_df=1)
    train_matrix = vectorizer.fit_transform(train_normalized)
    evaluation_matrix = vectorizer.transform(eval_normalized)
    nearest = NearestNeighbors(n_neighbors=1, metric="cosine", algorithm="brute", n_jobs=1)
    nearest.fit(train_matrix)
    distances, _ = nearest.kneighbors(evaluation_matrix)
    similarity = 1.0 - distances[:, 0]

    return {
        "n_train_rows": int(len(train)),
        "n_evaluation_rows": int(len(evaluation)),
        "n_train_question_groups": int(train["QuestionId"].nunique()),
        "n_evaluation_question_groups": int(evaluation["QuestionId"].nunique()),
        "evaluation_rows_with_unsupported_label": int(unsupported.sum()),
        "evaluation_unsupported_label_rate": float(unsupported.mean()),
        "evaluation_unique_labels": int(eval_labels.nunique()),
        "evaluation_unique_labels_unsupported": int(eval_labels[unsupported].nunique()),
        "evaluation_rows_with_exact_train_explanation": int(exact_matches.sum()),
        "evaluation_exact_train_explanation_rate": float(exact_matches.mean()),
        "nearest_train_char_tfidf_cosine": {
            "p50": float(np.quantile(similarity, 0.50)),
            "p90": float(np.quantile(similarity, 0.90)),
            "p95": float(np.quantile(similarity, 0.95)),
            "p99": float(np.quantile(similarity, 0.99)),
            "max": float(np.max(similarity)),
            "rate_at_least_0_80": float(np.mean(similarity >= 0.80)),
            "rate_at_least_0_90": float(np.mean(similarity >= 0.90)),
            "rate_at_least_0_95": float(np.mean(similarity >= 0.95)),
        },
    }


def run_support_overlap_diagnostic(
    frame: pd.DataFrame, assignments: pd.DataFrame, n_splits: int
) -> dict[str, object]:
    """Run fixed-fold diagnostics and return aggregate/fold-level numeric summaries."""
    required = {"source_row", "QuestionId"}.union({f"fold_{fold}" for fold in range(n_splits)})
    missing = required.difference(assignments.columns)
    if missing:
        raise ValueError(f"Fold assignments are missing columns: {sorted(missing)}")
    if len(frame) != len(assignments) or not np.array_equal(
        frame.index.to_numpy(), assignments["source_row"].to_numpy()
    ):
        raise ValueError("Fold assignments do not align exactly with the supplied input rows.")
    if not np.array_equal(frame["QuestionId"].astype(str), assignments["QuestionId"].astype(str)):
        raise ValueError("Fold assignments do not align with input QuestionId values.")

    folds = []
    for fold in range(n_splits):
        summary = analyze_fold(frame, assignments[f"fold_{fold}"])
        summary["fold"] = fold
        folds.append(summary)

    total_eval = sum(item["n_evaluation_rows"] for item in folds)
    total_unsupported = sum(item["evaluation_rows_with_unsupported_label"] for item in folds)
    total_exact = sum(item["evaluation_rows_with_exact_train_explanation"] for item in folds)
    return {
        "folds": folds,
        "aggregate": {
            "fold_count": n_splits,
            "total_evaluation_rows": total_eval,
            "unsupported_label_rate_weighted": total_unsupported / total_eval,
            "exact_train_explanation_rate_weighted": total_exact / total_eval,
            "mean_nearest_train_char_tfidf_cosine_p50": float(
                np.mean([item["nearest_train_char_tfidf_cosine"]["p50"] for item in folds])
            ),
            "mean_nearest_train_char_tfidf_cosine_p90": float(
                np.mean([item["nearest_train_char_tfidf_cosine"]["p90"] for item in folds])
            ),
            "mean_nearest_train_char_tfidf_cosine_p95": float(
                np.mean([item["nearest_train_char_tfidf_cosine"]["p95"] for item in folds])
            ),
            "mean_nearest_train_char_tfidf_cosine_p99": float(
                np.mean([item["nearest_train_char_tfidf_cosine"]["p99"] for item in folds])
            ),
            "mean_nearest_train_char_tfidf_cosine_rate_at_least_0_80": float(
                np.mean([item["nearest_train_char_tfidf_cosine"]["rate_at_least_0_80"] for item in folds])
            ),
            "mean_nearest_train_char_tfidf_cosine_rate_at_least_0_90": float(
                np.mean([item["nearest_train_char_tfidf_cosine"]["rate_at_least_0_90"] for item in folds])
            ),
            "mean_nearest_train_char_tfidf_cosine_rate_at_least_0_95": float(
                np.mean([item["nearest_train_char_tfidf_cosine"]["rate_at_least_0_95"] for item in folds])
            ),
        },
    }
