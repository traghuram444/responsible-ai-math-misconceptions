"""Best-effort monitor I/O; computation and argument errors remain strict."""
from __future__ import annotations

import json
import os
import tempfile
import threading
import time

from .live_status import LiveStatus, _utc_now


class ResilientStatus(LiveStatus):
    last_instance = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.io_failures = 0
        self.last_io_error = None
        type(self).last_instance = self

    def _io_error(self, operation, exc):
        self.io_failures += 1
        self.last_io_error = {'operation': operation, 'error_type': type(exc).__name__,
                              'errno': exc.errno if isinstance(exc.errno, int) else None}
        # Bounded diagnostics, no exception messages, paths or student content.
        if self.io_failures <= 3 or self.io_failures & (self.io_failures - 1) == 0:
            try:
                print(json.dumps({'monitor_io_failures': self.io_failures, **self.last_io_error}), flush=True)
            except OSError:
                pass

    def start(self):
        # The scientific runner owns/creates the output directory. Monitoring
        # never creates it or treats its availability as a modeling prerequisite.
        with self._lock:
            if self._started:
                raise RuntimeError('A status publisher cannot be restarted.')
            self._start_monotonic = time.monotonic()
            self._payload = {
                'schema_version': 1, 'experiment_id': self.experiment_id, 'status': 'RUNNING',
                'started_at': _utc_now(), 'updated_at': _utc_now(), 'finished_at': None,
                'elapsed_seconds': 0., 'stage': 'Starting experiment',
                'progress': {'completed': 0, 'total': self.total, 'percent': 0.},
                'latest_metrics': {}, 'heartbeat_seconds': self.heartbeat_seconds, 'error_reason': None,
            }
            self._publish_locked()
            self._started = True
            self._thread = threading.Thread(target=self._heartbeat, name=f'{self.experiment_id}-status', daemon=True)
            self._thread.start()
        return self

    def _publish_locked(self):
        self._payload['updated_at'] = _utc_now()
        self._payload['elapsed_seconds'] = round(time.monotonic() - self._start_monotonic, 3)
        self._payload['monitor_io_failures'] = self.io_failures
        temporary, fd, operation = None, None, 'create_temporary'
        try:
            fd, temporary = tempfile.mkstemp(prefix=f'.{self.path.name}.', dir=self.path.parent)
            operation = 'open_temporary'
            stream = os.fdopen(fd, 'w', encoding='utf-8', newline='\n')
            fd = None  # Stream now owns the descriptor.
            operation = 'write_temporary'
            with stream:
                json.dump(self._payload, stream, indent=2, allow_nan=False)
                stream.write('\n')
            operation = 'replace_snapshot'
            os.replace(temporary, self.path)
        except OSError as exc:
            self._io_error(operation, exc)
        finally:
            if fd is not None:
                try:
                    os.close(fd)
                except OSError as exc:
                    self._io_error('close_temporary', exc)
            if temporary is not None:
                try:
                    os.unlink(temporary)
                except FileNotFoundError:
                    pass
                except OSError as exc:
                    self._io_error('cleanup_temporary', exc)

    def diagnostics(self):
        with self._lock:
            return {'status': self._payload.get('status'), 'completed': self._payload.get('progress', {}).get('completed', 0),
                    'total': self.total, 'io_failures': self.io_failures, 'last_io_error': self.last_io_error,
                    'elapsed_seconds': self._payload.get('elapsed_seconds', 0.)}
