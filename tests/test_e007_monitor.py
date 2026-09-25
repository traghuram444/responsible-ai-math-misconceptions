"""Post-run viewer reliability tests; no experiment logic is changed."""
import json
from pathlib import Path

import pytest

from map_misconceptions.e007_monitor import read_status


@pytest.mark.parametrize("failure", [FileNotFoundError(), OSError(), "{", "[]"])
def test_transient_reads_retry_without_changing_status(failure):
    events = iter([failure, json.dumps({"experiment_id": "E007", "status": "RUNNING"})])
    pauses = []
    def read():
        item = next(events)
        if isinstance(item, Exception): raise item
        return item
    assert read_status(Path("unused"), reader=read, pause=pauses.append)["status"] == "RUNNING"
    assert pauses == [.2]


def test_persistent_missing_file_has_bounded_retry_and_does_not_idle_forever():
    calls, pauses = [], []
    def read():
        calls.append(True)
        raise FileNotFoundError()
    with pytest.raises(FileNotFoundError): read_status(Path("unused"), reader=read, pause=pauses.append)
    assert len(calls) == 3 and pauses == [.2, .2]


def test_terminal_state_is_returned_without_waiting_or_inventing_progress():
    payload = {"experiment_id": "E007", "status": "COMPLETED", "progress": {"completed": 111}}
    pauses = []
    assert read_status(Path("unused"), reader=lambda: json.dumps(payload), pause=pauses.append) == payload
    assert not pauses
