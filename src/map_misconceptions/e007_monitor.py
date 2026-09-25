"""Read-only E007 viewer with bounded retries for transient status-file reads.

Added after the completed E007 run; not part of its scientific execution.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import time

from .live_status import monitor_state, render_status


def read_status(path, *, reader=None, pause=time.sleep):
    read = reader if reader is not None else lambda: path.read_text(encoding="utf-8")
    for attempt in range(3):
        try:
            status = json.loads(read())
            if not isinstance(status, dict):
                raise ValueError("Invalid status object.")
            return status
        except (OSError, ValueError):
            if attempt == 2:
                raise
            pause(.2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status-file", type=Path, default=Path("artifacts/e007/live_status.json"))
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    try:
        while True:
            try:
                status = read_status(args.status_file)
                output = render_status(status)
                state = monitor_state(status)
            except (OSError, ValueError, TypeError, AttributeError):
                print("E007 status unavailable after bounded retries; monitor stopped. Experiment unaffected.")
                return 1
            if sys.stdout.isatty() and not args.once:
                print("\033[2J\033[H", end="")
            print(output, flush=True)
            if args.once or state in {"COMPLETED", "FAILED", "STALE"}:
                return 1 if state == "FAILED" else 0
            time.sleep(2)
    except KeyboardInterrupt:
        print("Monitor closed; experiment unaffected.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
