"""Publication checks for the immutable, unevaluated E012 failed attempt."""
import hashlib
import json
from pathlib import Path

from map_misconceptions.e007_publication import validate_schema, enum, pattern

ROOT = Path(__file__).resolve().parents[1]


def test_e012_failure_is_strict_sanitized_operational_record():
    record = json.loads((ROOT / 'results/E012_execution_failure.json').read_text(encoding='utf-8'))
    digest = pattern('[0-9a-f]{64}')
    schema = {
        'experiment_id': enum('E012'), 'status': enum('FAILED'),
        'failure_class': enum('operational_not_scientific'), 'error_type': enum('PermissionError'),
        'git_revision': enum('37bfd9e9d318a4964d6426cc9df137d67319d0f1'),
        'docker_image_id': pattern('sha256:[0-9a-f]{64}'), 'lock_sha256': digest, 'e011_sha256': digest,
        'started_utc': enum('2026-10-13T23:13:46.587+00:00'),
        'finished_utc': enum('2026-10-13T23:17:30.537+00:00'), 'elapsed_seconds': enum(223.968),
        'completed_classifier_fits': enum(49), 'planned_classifier_fits': enum(95),
        'fully_prepared_outer_folds': enum(2), 'evaluation_started': enum(False),
        'primary_criterion_met': enum(None), 'held_out_metrics': enum(None),
        'automatic_retry': enum(False), 'row_level_outputs': enum(False),
        'monitor_stopped': enum(True), 'protocol_and_code_changed': enum(False),
        'source_sha256': {key: digest for key in ('attempt', 'failure', 'terminal_status')},
        'diagnosis': {
            'confirmed': enum('main_thread_status_permission_error_propagates_in_synthetic_test'),
            'suspected': enum('transient_status_file_write_or_replace_contention'),
            'root_cause_confirmed': enum(False), 'original_traceback_available': enum(False),
        },
    }
    validate_schema(record, schema)
    for name, key in [('experiments/e011_e012_lock.json', 'lock_sha256'), ('results/E011_aggregates.json', 'e011_sha256')]:
        content = (ROOT / name).read_bytes().replace(b'\r\n', b'\n')
        assert hashlib.sha256(content).hexdigest() == record[key]
