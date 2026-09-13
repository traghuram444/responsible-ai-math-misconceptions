"""Synthetic heartbeat/renderer tests; no student data or real model runs."""

import json
import threading
import time
from datetime import datetime, timedelta, timezone

import pytest

from map_misconceptions.live_status import LiveStatus, monitor_state, render_status


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_start_update_complete_and_frozen_elapsed(tmp_path):
    path = tmp_path / "status.json"
    with LiveStatus(path, total=4, heartbeat_seconds=0.01) as live:
        live.update("Fold 1/2: tuning", completed=1, latest_metrics={"MAP@3": 0.5})
        first = load(path)
        assert first["status"] == "RUNNING"
        assert first["progress"] == {"completed": 1, "total": 4, "percent": 25.0}
        time.sleep(0.04)
        active = load(path)
        assert active["elapsed_seconds"] > first["elapsed_seconds"]
        assert active["progress"] == first["progress"]
        assert active["latest_metrics"] == {"MAP@3": 0.5}
    final = load(path)
    assert final["status"] == "COMPLETED"
    assert final["progress"]["completed"] == 4
    assert final["finished_at"] is not None
    time.sleep(0.03)
    assert load(path) == final
    assert not live._thread.is_alive()
    future = datetime.now(timezone.utc) + timedelta(hours=1)
    assert render_status(final, future) == render_status(final)


def test_failure_redacts_exception_and_preserves_progress(tmp_path):
    path = tmp_path / "status.json"
    with pytest.raises(ValueError, match="sensitive-example"):
        with LiveStatus(path, total=10) as live:
            live.update("Fitting fold", completed=3)
            raise ValueError("sensitive-example must not reach status")
    status = load(path)
    assert status["status"] == "FAILED"
    assert status["progress"]["completed"] == 3
    assert "sensitive-example" not in path.read_text(encoding="utf-8")
    assert not live._thread.is_alive()


def test_explicit_finish_is_idempotent_and_cannot_restart(tmp_path):
    live = LiveStatus(tmp_path / "status.json").start()
    live.finish("COMPLETED", "Aggregate report written")
    final = load(live.path)
    live.finish("FAILED", "Ignored after terminal state")
    assert load(live.path) == final
    with pytest.raises(RuntimeError):
        live.update("Not running")
    with pytest.raises(RuntimeError):
        live.start()


def test_progress_and_metric_validation(tmp_path):
    with LiveStatus(tmp_path / "status.json", total=3) as live:
        live.update("Stage", completed=1)
        for invalid in [0, 4, 1.5, True]:
            with pytest.raises(ValueError):
                live.update("Stage", completed=invalid)
        for invalid in ["student text", float("nan"), float("inf"), True]:
            with pytest.raises(ValueError):
                live.update("Stage", latest_metrics={"MAP@3": invalid})
        with pytest.raises(ValueError):
            live.update("Stage", latest_metrics={"invalid\nname": 0.5})
        assert load(live.path)["progress"]["completed"] == 1


def test_readers_never_observe_partial_json(tmp_path):
    path = tmp_path / "status.json"
    reads = []
    stop = threading.Event()
    errors = []
    with LiveStatus(path, total=50, heartbeat_seconds=0.002) as live:
        def reader():
            while not stop.is_set():
                try:
                    reads.append(load(path)["status"])
                except Exception as exc:
                    errors.append(type(exc).__name__)
                time.sleep(0.001)

        thread = threading.Thread(target=reader)
        thread.start()
        try:
            for completed in range(1, 51):
                live.update("Synthetic work", completed=completed)
        finally:
            stop.set()
            thread.join(timeout=2)
    assert reads
    assert not errors


def test_stale_legacy_and_terminal_snapshots():
    now = datetime(2026, 9, 13, 12, 0, tzinfo=timezone.utc)
    status = {
        "experiment_id": "E006", "status": "RUNNING",
        "started_at": (now - timedelta(minutes=5)).isoformat(),
        "updated_at": (now - timedelta(seconds=20)).isoformat(),
        "elapsed_seconds": 280,
    }
    assert monitor_state(status, now) == "RUNNING"
    assert "5m 00s" in render_status(status, now)
    future = now + timedelta(seconds=41)
    assert monitor_state(status, future) == "STALE"
    assert "4m 40s" in render_status(status, future)
    assert "NOT confirmed" in render_status(status, future)
    assert monitor_state({"status": "RUNNING", "updated_at": "12:00:00"}, now) == "STALE"
    assert monitor_state({"status": "RUNNING"}, now) == "STALE"
    for terminal in ["COMPLETED", "FAILED"]:
        assert monitor_state({**status, "status": terminal}, future) == terminal


@pytest.mark.parametrize("kwargs", [{"total": 0}, {"total": True}, {"heartbeat_seconds": 0},
                                  {"heartbeat_seconds": float("nan")}, {"experiment_id": "bad\nname"}])
def test_rejects_invalid_constructor(tmp_path, kwargs):
    with pytest.raises(ValueError):
        LiveStatus(tmp_path / "status.json", **kwargs)
