"""Aggregate-only experiment heartbeats, independent of the model fitting thread."""

from __future__ import annotations

import json
import math
import os
import re
import tempfile
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def _safe_stage(stage: str) -> str:
    if not isinstance(stage, str) or not stage.strip() or len(stage) > 300:
        raise ValueError("Stage must be a nonempty short aggregate description.")
    return " ".join(stage.split())


def _safe_metrics(metrics: Mapping) -> dict:
    result = {}
    for key, value in metrics.items():
        if not isinstance(key, str) or not re.fullmatch(r"[A-Za-z0-9_@./() +%-]{1,64}", key):
            raise ValueError("Metric names must be short aggregate labels.")
        if value is not None and (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or not math.isfinite(value)
        ):
            raise ValueError("Metrics must be finite numbers or null, never row text.")
        result[key] = value
    return result


class LiveStatus:
    """Write atomic status snapshots while the main thread performs long fits.

    ``with LiveStatus(path) as live: live.update('Outer fold 1/5', completed=0)``
    starts automatically and publishes COMPLETED on normal context exit, FAILED
    otherwise. Exception details are deliberately not written to the status file.
    The progress counter represents caller-defined completed work, not elapsed
    time. Only actual caller updates advance it; heartbeats never invent progress.
    """

    def __init__(
        self,
        path: str | Path,
        experiment_id: str = "E006",
        total: int = 100,
        heartbeat_seconds: float = 10.0,
    ) -> None:
        if not isinstance(total, int) or isinstance(total, bool) or total <= 0:
            raise ValueError("Total must be a positive integer.")
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,32}", experiment_id):
            raise ValueError("Invalid experiment identifier.")
        if not math.isfinite(heartbeat_seconds) or heartbeat_seconds <= 0:
            raise ValueError("Heartbeat interval must be positive and finite.")
        self.path = Path(path)
        self.experiment_id = experiment_id
        self.total = total
        self.heartbeat_seconds = heartbeat_seconds
        self._lock = threading.RLock()
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._started = False
        self._start_monotonic = 0.0
        self._payload: dict = {}

    def start(self) -> "LiveStatus":
        with self._lock:
            if self._started:
                raise RuntimeError("A status publisher cannot be restarted.")
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._start_monotonic = time.monotonic()
            self._payload = {
                "schema_version": 1,
                "experiment_id": self.experiment_id,
                "status": "RUNNING",
                "started_at": _utc_now(),
                "updated_at": _utc_now(),
                "finished_at": None,
                "elapsed_seconds": 0.0,
                "stage": "Starting experiment",
                "progress": {"completed": 0, "total": self.total, "percent": 0.0},
                "latest_metrics": {},
                "heartbeat_seconds": self.heartbeat_seconds,
                "error_reason": None,
            }
            self._publish_locked()
            self._started = True
            self._thread = threading.Thread(
                target=self._heartbeat, name=f"{self.experiment_id}-status", daemon=True
            )
            self._thread.start()
        return self

    def _publish_locked(self) -> None:
        self._payload["updated_at"] = _utc_now()
        self._payload["elapsed_seconds"] = round(time.monotonic() - self._start_monotonic, 3)
        # Same-directory replace ensures readers see a complete old or new JSON.
        fd, temporary = tempfile.mkstemp(prefix=f".{self.path.name}.", dir=self.path.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
                json.dump(self._payload, stream, indent=2, allow_nan=False)
                stream.write("\n")
            os.replace(temporary, self.path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)

    def _heartbeat(self) -> None:
        while not self._stop.wait(self.heartbeat_seconds):
            with self._lock:
                if self._payload.get("status") != "RUNNING":
                    return
                try:
                    self._publish_locked()
                except OSError:
                    # A blocked write must not interrupt a model fit. Readers
                    # mark the last successful snapshot stale after 60 seconds.
                    continue

    def update(
        self,
        stage: str,
        completed: int | None = None,
        latest_metrics: Mapping | None = None,
    ) -> None:
        stage = _safe_stage(stage)
        metrics = _safe_metrics(latest_metrics) if latest_metrics is not None else None
        with self._lock:
            if self._payload.get("status") != "RUNNING":
                raise RuntimeError("Status updates require a running experiment.")
            if completed is not None:
                previous = self._payload["progress"]["completed"]
                if (
                    not isinstance(completed, int)
                    or isinstance(completed, bool)
                    or not previous <= completed <= self.total
                ):
                    raise ValueError("Completed work must be monotonic and within total.")
                self._payload["progress"] = {
                    "completed": completed,
                    "total": self.total,
                    "percent": round(100 * completed / self.total, 1),
                }
            self._payload["stage"] = stage
            if metrics is not None:
                self._payload["latest_metrics"] = metrics
            self._publish_locked()

    def finish(self, status: str = "COMPLETED", stage: str = "Experiment complete") -> None:
        if status not in {"COMPLETED", "FAILED"}:
            raise ValueError("Final status must be COMPLETED or FAILED.")
        stage = _safe_stage(stage)
        with self._lock:
            if not self._started:
                raise RuntimeError("Start the status publisher before finishing.")
            if self._payload["status"] != "RUNNING":
                return
            self._stop.set()
            self._payload["status"] = status
            self._payload["stage"] = stage
            self._payload["finished_at"] = _utc_now()
            self._payload["error_reason"] = (
                "Experiment failed; inspect the private run log locally."
                if status == "FAILED" else None
            )
            if status == "COMPLETED":
                self._payload["progress"] = {
                    "completed": self.total, "total": self.total, "percent": 100.0
                }
            self._publish_locked()
        if self._thread is not None:
            self._thread.join(timeout=min(self.heartbeat_seconds + 1, 2))

    def __enter__(self) -> "LiveStatus":
        return self.start()

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.finish(
            status="FAILED" if exc_type is not None else "COMPLETED",
            stage="Experiment failed" if exc_type is not None else "Experiment complete",
        )
        return False


def _timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("UTC-aware timestamp required.")
    return parsed.astimezone(timezone.utc)


def monitor_state(status: dict, now: datetime | None = None, stale_seconds: float = 60) -> str:
    """Terminal snapshots remain terminal; a heartbeat is not proof of progress."""
    now = now or datetime.now(timezone.utc)
    state = status.get("status")
    if state in {"COMPLETED", "FAILED"}:
        return state
    if state != "RUNNING":
        return "STALE"
    try:
        age = (now - _timestamp(status["updated_at"])).total_seconds()
        _timestamp(status["started_at"])
    except (KeyError, TypeError, ValueError, AttributeError):
        return "STALE"
    return "RUNNING" if -5 <= age <= stale_seconds else "STALE"


def render_status(status: dict, now: datetime | None = None) -> str:
    """Render dynamic elapsed time only for a recent running snapshot."""
    now = now or datetime.now(timezone.utc)
    state = monitor_state(status, now)
    elapsed = max(0, float(status.get("elapsed_seconds", 0)))
    if state == "RUNNING":
        elapsed = max(elapsed, (now - _timestamp(status["started_at"])).total_seconds())
    seconds = int(elapsed)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    elapsed_text = f"{hours}h {minutes:02}m {seconds:02}s" if hours else f"{minutes}m {seconds:02}s"
    progress = status.get("progress", {})
    lines = [
        "AI Misconception Experiments — LIVE",
        "─" * 48,
        f"Experiment: {status.get('experiment_id', 'unknown')}",
        f"Status:     {state}",
        f"Elapsed:    {elapsed_text}",
        f"Progress:   {progress.get('completed', 0)} / {progress.get('total', '?')}"
        f"  ({progress.get('percent', 0)}%)",
        f"Stage:      {status.get('stage', 'unknown')}",
        "",
        "Latest metrics (completed work only)",
    ]
    metrics = status.get("latest_metrics", {})
    if not metrics:
        lines.append("No completed evaluation yet.")
    for name, value in metrics.items():
        display = f"{value:.6f}" if isinstance(value, float) else str(value)
        lines.append(f"{name + ':':20}{display}")
    lines.extend(["", f"Last heartbeat: {status.get('updated_at', 'unknown')}"])
    if state == "STALE":
        lines.append("Heartbeat missing/stale; run activity is NOT confirmed. Monitor stopped.")
    elif state == "FAILED":
        lines.append("Run failed; inspect the private run log locally.")
    else:
        lines.append("Heartbeat tracks process liveness; progress advances only on completed work.")
    lines.append("─" * 48)
    return "\n".join(lines)
