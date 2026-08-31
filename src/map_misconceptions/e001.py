"""Leakage-safe E001 baseline experiment.

Hyperparameters are selected using only inner folds of each outer training role.
The group-disjoint calibration role is reserved for temperature scaling.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold, StratifiedKFold, StratifiedShuffleSplit

from .data_contract import combined_label, file_sha256, load_training_data
from .metrics import classification_summary, risk_coverage

SEED = 20260831
GRID = (
    {"ngram_range": (1, 1), "min_df": 2, "C": 0.5},
    {"ngram_range": (1, 2), "min_df": 2, "C": 1.0},
    {"ngram_range": (1, 2), "min_df": 5, "C": 2.0},
)


def text_input(frame: pd.DataFrame, variant: str) -> pd.Series:
    explanation = frame["StudentExplanation"].fillna("").astype(str)
    if variant == "explanation_only":
        return explanation
    if variant == "question_plus_explanation":
        return "[QUESTION] " + frame["QuestionText"].fillna("").astype(str) + " [EXPLANATION] " + explanation
    raise ValueError(f"Unknown variant: {variant}")


def fit_tfidf_lr(train: pd.DataFrame, variant: str, params: dict) -> tuple[TfidfVectorizer, LogisticRegression]:
    vectorizer = TfidfVectorizer(ngram_range=params["ngram_range"], min_df=params["min_df"], sublinear_tf=True)
    matrix = vectorizer.fit_transform(text_input(train, variant))
    model = LogisticRegression(C=params["C"], max_iter=2000, class_weight=None, random_state=SEED, n_jobs=1)
    model.fit(matrix, combined_label(train))
    return vectorizer, model


def predict(model_pair: tuple[TfidfVectorizer, LogisticRegression], frame: pd.DataFrame, variant: str) -> tuple[np.ndarray, np.ndarray]:
    vectorizer, model = model_pair
    return model.predict_proba(vectorizer.transform(text_input(frame, variant))), model.classes_


def score_params(
    train: pd.DataFrame,
    variant: str,
    splitter,
    groups: pd.Series | None = None,
    split_labels: pd.Series | None = None,
) -> dict:
    y = combined_label(train)
    scores: list[tuple[float, dict]] = []
    labels_for_split = y if split_labels is None else split_labels
    split_iter = splitter.split(train, labels_for_split, groups) if groups is not None else splitter.split(train, labels_for_split)
    splits = list(split_iter)
    for params in GRID:
        fold_scores = []
        for inner_train, inner_val in splits:
            try:
                fitted = fit_tfidf_lr(train.iloc[inner_train], variant, params)
                probabilities, classes = predict(fitted, train.iloc[inner_val], variant)
                fold_scores.append(classification_summary(combined_label(train.iloc[inner_val]).to_numpy(), probabilities, classes)["map_at_3"])
            except ValueError:
                fold_scores.append(float("-inf"))
        scores.append((float(np.mean(fold_scores)), params))
    best_score, best_params = max(scores, key=lambda item: item[0])
    if not np.isfinite(best_score):
        raise ValueError("All inner-fold configurations failed; inspect class/group support.")
    return {"params": {**best_params, "ngram_range": list(best_params["ngram_range"])}, "inner_mean_map_at_3": best_score}


def temperature_scale(calibration_y: np.ndarray, calibration_probabilities: np.ndarray, classes: np.ndarray) -> tuple[float, int]:
    class_to_index = {value: i for i, value in enumerate(classes)}
    valid = np.array([value in class_to_index for value in calibration_y])
    if valid.sum() == 0:
        return 1.0, 0
    truth_idx = np.array([class_to_index[value] for value in calibration_y[valid]])
    logits = np.log(np.clip(calibration_probabilities[valid], 1e-12, 1.0))

    def nll(log_temperature: float) -> float:
        temperature = np.exp(log_temperature)
        scaled = logits / temperature
        scaled -= scaled.max(axis=1, keepdims=True)
        probs = np.exp(scaled)
        probs /= probs.sum(axis=1, keepdims=True)
        return float(-np.log(probs[np.arange(len(truth_idx)), truth_idx]).mean())

    optimum = minimize_scalar(nll, bounds=(-3.0, 3.0), method="bounded")
    return float(np.exp(optimum.x)), int(valid.sum())


def apply_temperature(probabilities: np.ndarray, temperature: float) -> np.ndarray:
    logits = np.log(np.clip(probabilities, 1e-12, 1.0)) / temperature
    logits -= logits.max(axis=1, keepdims=True)
    scaled = np.exp(logits)
    return scaled / scaled.sum(axis=1, keepdims=True)


def frequency_probabilities(train: pd.DataFrame, evaluation: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    prevalence = combined_label(train).value_counts(normalize=True).sort_index()
    classes = prevalence.index.to_numpy()
    return np.tile(prevalence.to_numpy(), (len(evaluation), 1)), classes


def run_grouped(frame: pd.DataFrame, assignments: pd.DataFrame, variant: str) -> dict:
    fold_results = []
    for fold in range(sum(column.startswith("fold_") for column in assignments.columns)):
        role = assignments[f"fold_{fold}"].to_numpy()
        train = frame.iloc[np.where(role == "train")[0]]
        calibration = frame.iloc[np.where(role == "calibration")[0]]
        evaluation = frame.iloc[np.where(role == "evaluation")[0]]
        inner_groups = train["QuestionId"].astype(str)
        inner = GroupKFold(n_splits=min(3, inner_groups.nunique()))
        selected = score_params(train, variant, inner, groups=inner_groups)
        fitted = fit_tfidf_lr(train, variant, {**selected["params"], "ngram_range": tuple(selected["params"]["ngram_range"])})
        calibration_probs, classes = predict(fitted, calibration, variant)
        temperature, calibration_supported_n = temperature_scale(combined_label(calibration).to_numpy(), calibration_probs, classes)
        evaluation_probs, _ = predict(fitted, evaluation, variant)
        evaluation_probs = apply_temperature(evaluation_probs, temperature)
        y_eval = combined_label(evaluation).to_numpy()
        metrics = classification_summary(y_eval, evaluation_probs, classes)
        per_question = []
        for question_id, subset in evaluation.groupby("QuestionId", sort=True):
            positions = subset.index.to_numpy()
            relative = np.isin(evaluation.index.to_numpy(), positions)
            per_question.append({"QuestionId": str(question_id), **classification_summary(y_eval[relative], evaluation_probs[relative], classes)})
        freq_probs, freq_classes = frequency_probabilities(train, evaluation)
        train_classes = set(classes)
        fold_results.append(
            {
                "fold": fold,
                "n_train": len(train),
                "n_calibration": len(calibration),
                "n_evaluation": len(evaluation),
                "evaluation_question_ids": sorted(map(str, evaluation["QuestionId"].unique())),
                "unsupported_evaluation_label_rate": float((~pd.Series(y_eval).isin(train_classes)).mean()),
                "selected_hyperparameters": selected,
                "temperature": temperature,
                "calibration_supported_n": calibration_supported_n,
                "frequency_baseline": classification_summary(y_eval, freq_probs, freq_classes),
                "tfidf_logreg": metrics,
                "risk_coverage": risk_coverage(y_eval, evaluation_probs, classes),
                "per_question": per_question,
            }
        )
    return {"split": "QuestionId-grouped", "variant": variant, "folds": fold_results}


def run_random_reference(frame: pd.DataFrame, variant: str) -> dict:
    # Several combined labels occur fewer than five times.  Stratifying by the
    # documented six-way Category avoids an invalid split while retaining a
    # deliberately optimistic response-level reference comparison.
    strata = frame["Category"].astype(str)
    outer = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    folds = []
    for fold, (train_pool_idx, evaluation_idx) in enumerate(outer.split(frame, strata)):
        pool = frame.iloc[train_pool_idx]
        pool_strata = pool["Category"].astype(str)
        calibration_split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=SEED + fold)
        train_rel, calibration_rel = next(calibration_split.split(pool, pool_strata))
        train, calibration, evaluation = pool.iloc[train_rel], pool.iloc[calibration_rel], frame.iloc[evaluation_idx]
        inner = StratifiedKFold(n_splits=3, shuffle=True, random_state=SEED + fold)
        selected = score_params(train, variant, inner, split_labels=train["Category"].astype(str))
        fitted = fit_tfidf_lr(train, variant, {**selected["params"], "ngram_range": tuple(selected["params"]["ngram_range"])})
        calibration_probs, classes = predict(fitted, calibration, variant)
        temperature, calibration_supported_n = temperature_scale(combined_label(calibration).to_numpy(), calibration_probs, classes)
        evaluation_probs, _ = predict(fitted, evaluation, variant)
        evaluation_probs = apply_temperature(evaluation_probs, temperature)
        y_eval = combined_label(evaluation).to_numpy()
        freq_probs, freq_classes = frequency_probabilities(train, evaluation)
        folds.append({"fold": fold, "n_evaluation": len(evaluation), "selected_hyperparameters": selected, "temperature": temperature, "calibration_supported_n": calibration_supported_n, "frequency_baseline": classification_summary(y_eval, freq_probs, freq_classes), "tfidf_logreg": classification_summary(y_eval, evaluation_probs, classes), "risk_coverage": risk_coverage(y_eval, evaluation_probs, classes)})
    return {"split": "stratified-random-reference-only", "variant": variant, "folds": folds}


def aggregate(result: dict) -> dict:
    metric_names = ("top1_accuracy", "macro_f1_all_eval_labels", "map_at_3", "ece_10_equal_width", "multiclass_brier")
    output = {}
    for model in ("frequency_baseline", "tfidf_logreg"):
        output[model] = {}
        for metric in metric_names:
            values = np.array([fold[model][metric] for fold in result["folds"]])
            output[model][metric] = {"mean": float(values.mean()), "std": float(values.std(ddof=1))}
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Run E001 without outer-fold tuning leakage.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--splits", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("artifacts/e001_results.json"))
    args = parser.parse_args()
    frame = load_training_data(args.input)
    assignments = pd.read_csv(args.splits / "grouped_fold_assignments.csv")
    if len(frame) != len(assignments):
        raise ValueError("Split assignments do not match input row count.")
    manifest = json.loads((args.splits / "manifest.json").read_text(encoding="utf-8"))
    if manifest["input_sha256"] != file_sha256(args.input):
        raise ValueError("Input SHA-256 differs from frozen split manifest.")
    all_results = []
    for variant in ("explanation_only", "question_plus_explanation"):
        grouped = run_grouped(frame, assignments, variant)
        random = run_random_reference(frame, variant)
        all_results.extend(({**grouped, "aggregate": aggregate(grouped)}, {**random, "aggregate": aggregate(random)}))
    payload = {"experiment_id": "E001", "seed": SEED, "input_sha256": file_sha256(args.input), "split_manifest_sha256": hashlib.sha256((args.splits / "manifest.json").read_bytes()).hexdigest(), "results": all_results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote aggregate-only E001 results to {args.output}")


if __name__ == "__main__":
    main()
