"""Dataset schema checks kept deliberately separate from modeling."""

from __future__ import annotations

from pathlib import Path
import hashlib

import pandas as pd

REQUIRED_TRAIN_COLUMNS = frozenset(
    {
        "QuestionId",
        "QuestionText",
        "MC_Answer",
        "StudentExplanation",
        "Category",
        "Misconception",
    }
)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_training_frame(frame: pd.DataFrame) -> None:
    """Fail early for a schema that cannot support leakage-safe evaluation."""
    missing = REQUIRED_TRAIN_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing required training columns: {sorted(missing)}")
    if frame["QuestionId"].isna().any():
        raise ValueError("QuestionId contains missing values; groups cannot be assigned safely.")
    labels = frame[["Category", "Misconception"]]
    if labels.isna().any().any() or labels.astype(str).apply(lambda column: column.str.strip().eq("")).any().any():
        raise ValueError("Labels contain missing values; resolve before creating folds.")


def load_training_data(path: str | Path) -> pd.DataFrame:
    source = Path(path)
    # The documented non-misconception label is the literal token "NA". Pandas'
    # default parser would silently turn it into NaN and corrupt the target space.
    frame = pd.read_csv(source, keep_default_na=False)
    validate_training_frame(frame)
    return frame


def combined_label(frame: pd.DataFrame) -> pd.Series:
    """The official competition target representation, without changing labels."""
    return frame["Category"].astype(str) + ":" + frame["Misconception"].astype(str)
