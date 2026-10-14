"""Infrastructure-only regression tests; no source data or research fitting."""
import json
from pathlib import Path
import sys
import time
from unittest.mock import patch

import pytest
from map_misconceptions import e011_context as core
from map_misconceptions import resilient_status as monitor
from map_misconceptions.e012_retry import invoke_unchanged_main, sanitized_exception, verify_amendment
from map_misconceptions.live_status import monitor_state

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize('operation,target', [
    ('create_temporary', 'tempfile.mkstemp'), ('open_temporary', 'os.fdopen'),
    ('write_temporary', 'json.dump'), ('replace_snapshot', 'os.replace'),
    ('cleanup_temporary', 'os.unlink'),
])
def test_all_snapshot_io_errors_are_nonfatal_and_redacted(tmp_path, capsys, operation, target):
    live = monitor.ResilientStatus(tmp_path / 'status.json', total=2)
    with patch('map_misconceptions.resilient_status.' + target, side_effect=PermissionError(13, 'PRIVATE_ERROR_TEXT')):
        with live:
            live.update('Synthetic fit finished', completed=1)
    assert live.diagnostics()['status'] == 'COMPLETED'
    assert live.io_failures >= 3
    assert live.last_io_error == {'operation': operation, 'error_type': 'PermissionError', 'errno': 13}
    assert not live._thread.is_alive()
    assert 'PRIVATE_ERROR_TEXT' not in capsys.readouterr().out


def test_recovery_publishes_real_progress_and_keeps_metrics(tmp_path):
    path = tmp_path / 'status.json'
    with monitor.ResilientStatus(path, total=4, heartbeat_seconds=.01) as live:
        live.update('First fit', completed=1)
        first = json.loads(path.read_text())
        with patch('map_misconceptions.resilient_status.os.replace', side_effect=PermissionError()):
            live.update('Second fit', completed=2, latest_metrics={'Synthetic metric': .5})
            assert json.loads(path.read_text()) == first
        deadline = time.monotonic() + 2
        while json.loads(path.read_text())['progress']['completed'] != 2 and time.monotonic() < deadline:
            time.sleep(.01)
        recovered = json.loads(path.read_text())
        assert recovered['progress']['completed'] == 2
        assert recovered['latest_metrics'] == {'Synthetic metric': .5}
        assert recovered['monitor_io_failures'] >= 1
    assert json.loads(path.read_text())['status'] == 'COMPLETED'


def test_missing_monitor_directory_and_final_write_failure_do_not_abort(tmp_path):
    live = monitor.ResilientStatus(tmp_path / 'absent' / 'status.json', total=3)
    with live:
        for i in range(1, 4): live.update('Synthetic work', completed=i)
    assert live.diagnostics()['completed'] == 3
    assert live.diagnostics()['status'] == 'COMPLETED'
    assert live.io_failures == 5
    assert not live._thread.is_alive()


def test_monitor_error_does_not_mask_model_exception(tmp_path):
    live = monitor.ResilientStatus(tmp_path / 'status.json', total=3)
    with pytest.raises(ValueError, match='synthetic model failure'):
        with patch('map_misconceptions.resilient_status.os.replace', side_effect=PermissionError()):
            with live:
                live.update('Synthetic fit', completed=1)
                raise ValueError('synthetic model failure')
    assert live.diagnostics()['status'] == 'FAILED'
    assert live.diagnostics()['completed'] == 1
    assert not live._thread.is_alive()


def test_non_io_programming_errors_and_bad_metrics_remain_fatal(tmp_path):
    with monitor.ResilientStatus(tmp_path / 'status.json', total=3) as live:
        with pytest.raises(ValueError): live.update('Synthetic fit', completed=4)
        with pytest.raises(ValueError): live.update('Synthetic fit', latest_metrics={'bad': float('nan')})
        with patch('map_misconceptions.resilient_status.json.dump', side_effect=TypeError('synthetic bug')):
            with pytest.raises(TypeError): live.update('Synthetic fit', completed=1)


def test_faulty_diagnostic_stdout_does_not_abort(tmp_path):
    with patch('map_misconceptions.resilient_status.os.replace', side_effect=PermissionError()), \
         patch('builtins.print', side_effect=BrokenPipeError()):
        with monitor.ResilientStatus(tmp_path / 'status.json', total=1) as live:
            live.update('Synthetic fit', completed=1)
    assert live.diagnostics()['status'] == 'COMPLETED'


def test_stale_snapshot_not_reported_as_current(tmp_path):
    path = tmp_path / 'status.json'
    with monitor.ResilientStatus(path) as live:
        old = json.loads(path.read_text())
    old['updated_at'] = old['started_at'] = '2020-01-01T00:00:00+00:00'
    assert monitor_state(old) == 'STALE'


@pytest.mark.parametrize('raises', [False, True])
def test_only_monitor_binding_and_fixed_cli_are_injected(monkeypatch, raises):
    original_status, original_argv = core.LiveStatus, sys.argv
    scientific = [core.fit_model, core.select_params, core.prepare, core.evaluate, core.primary]
    def fake_main():
        assert core.LiveStatus is monitor.ResilientStatus
        assert sys.argv == ['run_e012_attempt02', '--experiment', 'E012', '--git-revision', 'a'*40,
                            '--image-id', 'sha256:'+'b'*64, '--e011-sha', 'c'*64]
        assert scientific == [core.fit_model, core.select_params, core.prepare, core.evaluate, core.primary]
        if raises: raise ValueError('synthetic failure')
    monkeypatch.setattr(core, 'main', fake_main)
    if raises:
        with pytest.raises(ValueError): invoke_unchanged_main('a'*40, 'sha256:'+'b'*64, 'c'*64)
    else: invoke_unchanged_main('a'*40, 'sha256:'+'b'*64, 'c'*64)
    assert core.LiveStatus is original_status and sys.argv is original_argv


def test_sanitized_failure_contains_no_message_or_path():
    try:
        try: raise PermissionError(13, 'PRIVATE_ERROR_TEXT')
        except PermissionError: raise RuntimeError('outer private text') from None
    except RuntimeError as exc:
        result = sanitized_exception(exc)
    assert result['error_type'] == 'PermissionError' and result['errno'] == 13
    assert 'PRIVATE' not in json.dumps(result) and 'outer private' not in json.dumps(result)
    assert set(result) == {'error_type', 'errno', 'function_chain'}


def test_amendment_and_historical_hashes_when_lock_exists():
    if (ROOT / 'experiments/e012_attempt02_lock.json').exists():
        assert verify_amendment()['attempt_id'] == 'e012_attempt02'


def test_synthetic_model_outputs_identical_under_persistent_monitor_failure(tmp_path):
    import numpy as np
    from test_e011_context import frame, assignments
    data = frame()
    baseline, memory = core.prepare(data, assignments(data), 'full_context', 'complement_nb', 0, lambda: None)
    with patch('map_misconceptions.resilient_status.os.replace', side_effect=PermissionError()):
        with monitor.ResilientStatus(tmp_path/'status.json', total=19) as live:
            count = 0
            def completed():
                nonlocal count
                count += 1
                live.update('Synthetic classifier fit complete', completed=count)
            result, after = core.prepare(data, assignments(data), 'full_context', 'complement_nb', 0, completed)
    assert count == 19 and result == baseline
    for key in memory:
        np.testing.assert_array_equal(memory[key], after[key])
