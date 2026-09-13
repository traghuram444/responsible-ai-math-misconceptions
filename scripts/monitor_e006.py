"""Read-only terminal monitor; exits when no run, terminal state, or stale heartbeat."""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

from map_misconceptions.live_status import monitor_state, render_status


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status-file", type=Path, default=Path("artifacts/e006/live_status.json"))
    parser.add_argument("--refresh-seconds", type=float, default=2.0)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    if not math.isfinite(args.refresh_seconds) or args.refresh_seconds <= 0:
        parser.error("Refresh interval must be positive and finite.")
    try:
        while True:
            try:
                status = json.loads(args.status_file.read_text(encoding="utf-8"))
                if not isinstance(status, dict):
                    raise ValueError("Invalid status.")
                output = render_status(status)
                state = monitor_state(status)
            except FileNotFoundError:
                print("No E006 status file exists. No active run is confirmed; monitor stopped.")
                return 0
            except (OSError, ValueError, TypeError, AttributeError):
                print("Status unavailable or invalid. No active run is confirmed; monitor stopped.")
                return 1
            if sys.stdout.isatty() and not args.once:
                print("\033[2J\033[H", end="")
            print(output, flush=True)
            if args.once or state in {"COMPLETED", "FAILED", "STALE"}:
                return 1 if state == "FAILED" else 0
            time.sleep(args.refresh_seconds)
    except KeyboardInterrupt:
        print("\nMonitor closed; the experiment is unaffected.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
