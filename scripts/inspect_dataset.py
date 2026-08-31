"""Create an auditable, non-textual inspection report from approved MAP training data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from map_misconceptions.data_contract import combined_label, file_sha256, load_training_data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("artifacts/data_inspection.json"))
    args = parser.parse_args()

    frame = load_training_data(args.input)
    report = {
        "input_file": args.input.name,
        "input_sha256": file_sha256(args.input),
        "rows": len(frame),
        "columns": list(frame.columns),
        "question_groups": int(frame["QuestionId"].nunique()),
        "category_counts": frame["Category"].value_counts(dropna=False).to_dict(),
        "combined_label_counts": combined_label(frame).value_counts(dropna=False).to_dict(),
        "missing_values": frame.isna().sum().to_dict(),
        "explanation_length_chars": frame["StudentExplanation"].fillna("").str.len().describe().to_dict(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"Wrote {args.output}; no student explanations were emitted.")


if __name__ == "__main__":
    main()
