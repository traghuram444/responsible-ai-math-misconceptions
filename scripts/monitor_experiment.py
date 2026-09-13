"""Render a lightweight terminal monitor from a local experiment-status JSON file."""

from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime
from pathlib import Path


def render(status: dict) -> str:
    now = datetime.now().strftime("%I:%M:%S %p")
    progress = status.get("progress", {})
    completed = progress.get("completed", "—")
    total = progress.get("total", "—")
    percent = progress.get("percent", "—")
    metrics = status.get("latest_metrics", {})
    lines = [
        "AI Misconception Experiments — LIVE",
        "─" * 36,
        f"Experiment: {status.get('experiment_id', '—')}",
        f"Status:     {status.get('status', '—')}",
        f"Elapsed:    {status.get('elapsed', '—')}",
        f"Progress:   {completed} / {total}  ({percent}%)",
        f"Stage:      {status.get('stage', '—')}",
        "",
        "Latest metrics",
    ]
    for name, value in metrics.items():
        lines.append(f"{name + ':':12}{value}")
    lines.extend(["", f"Last update: {status.get('updated_at', now)}", "─" * 36])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Monitor a local experiment without interrupting it.")
    parser.add_argument("--status-file", type=Path, default=Path("artifacts/live_status.json"))
    parser.add_argument("--refresh-seconds", type=float, default=2.0)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        if args.status_file.exists():
            status = json.loads(args.status_file.read_text(encoding="utf-8"))
            print(render(status))
        else:
            print("AI Misconception Experiments — LIVE\n\nWaiting for an experiment status file …")
        if args.once:
            return
        time.sleep(args.refresh_seconds)


if __name__ == "__main__":
    main()
