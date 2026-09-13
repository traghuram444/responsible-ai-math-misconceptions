"""Verify the registered study without exposing rows, text, labels, or local paths."""
import json
from pathlib import Path

from map_misconceptions.frozen_validation import verify_frozen_inputs


if __name__ == "__main__":
    print(json.dumps(verify_frozen_inputs(
        Path("data/raw/train.csv"), Path("artifacts/splits"),
        expected_data_sha="0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c",
        expected_manifest_sha="93a25f33389b68487c09c5e9b34cfd10ca0d03b9b6438a53e2c385b2e87a7b94",
        expected_assignments_sha="b0211bafc055aedcd334877782d8db818a7c0a05873f1826ad32f0c17a61c9dd",
    ), indent=2))
