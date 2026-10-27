"""Additive authorization and preservation gates for E020 reporting recovery."""
import hashlib
import json
from pathlib import Path
from .e019_checker import sha
from .e019_integrity import canonical
from .e020_integrity import preserve_e020
from .e020_map_integrity import verify_map, verify_readiness_evidence

SOURCE = 'artifacts/e020_attempt01/map'
OUT = 'artifacts/e020_recovery01'
LOCK = 'experiments/e020_recovery_lock.json'
FILES = ('src/map_misconceptions/e020_recovery_integrity.py',
         'src/map_misconceptions/e020_recovery.py',
         'scripts/prepare_e020_recovery.py', 'scripts/run_e020_recovery.py',
         'scripts/publish_e020_recovery.py', 'tests/test_e020_recovery.py',
         'docs/E020_RECOVERY.md')


def inventory(folder):
    return {p.relative_to(folder).as_posix(): sha(p)
            for p in sorted(folder.rglob('*')) if p.is_file()}


def source_gate(root):
    root = Path(root)
    lock = verify_map(root)
    preserve_e020(root)
    verify_readiness_evidence(root, lock)
    source = root / SOURCE
    expected = {'statistics_failure.json': 'KeyError',
                'orchestration_failure.json': 'CalledProcessError'}
    failures = {p.relative_to(source).as_posix() for p in source.rglob('*failure.json')}
    if failures != set(expected):
        raise ValueError('Unexpected source failure inventory.')
    for name, exception in expected.items():
        if json.loads((source / name).read_text()) != {
                'status': 'FAILED', 'exception_type': exception, 'automatic_retry': False}:
            raise ValueError('Source failure receipt changed.')
    if (source / 'execution.json').exists() or (source / 'aggregate_results.json').exists():
        raise ValueError('Recovery source must remain the failed attempt.')
    frozen = json.loads((source / 'frozen_development_private.json').read_text())
    if frozen['model_fits'] != 50 or frozen['all_predictions_and_review_orders_frozen'] is not True:
        raise ValueError('Global freeze incomplete.')
    expected_files = {f'fold_{f}_frozen_private.npz' for f in range(5)}
    if set(frozen['prediction_sha256']) != expected_files:
        raise ValueError('Incomplete frozen folds.')
    for name, digest in frozen['prediction_sha256'].items():
        if sha(source / name) != digest:
            raise ValueError('Frozen predictions changed.')
    return lock, frozen


def verify(root):
    root = Path(root)
    original, frozen = source_gate(root)
    lock = json.loads((root / LOCK).read_text())
    if lock['original_map_lock_sha256'] != sha(root / 'experiments/e020_map_lock.json'):
        raise ValueError('Original MAP lock changed.')
    if set(lock['files']) != set(FILES):
        raise ValueError('Recovery file coverage changed.')
    for name, digest in lock['files'].items():
        if canonical(root / name) != digest:
            raise ValueError('Recovery implementation changed.')
    private = root / 'artifacts/e020_recovery_setup/failed_attempt_inventory_private.json'
    if sha(private) != lock['failed_attempt_inventory_sha256']:
        raise ValueError('Failed-attempt inventory changed.')
    captured = json.loads(private.read_text())
    if len(captured) != lock['failed_attempt_files'] or inventory(root / 'artifacts/e020_attempt01') != captured:
        raise ValueError('Failed attempt changed.')
    for name, record in lock['append_only_prefixes'].items():
        if hashlib.sha256((root/name).read_bytes()[:record['bytes']]).hexdigest() != record['sha256']:
            raise ValueError('Recovery documentation prefix changed.')
    if sha(root/SOURCE/'frozen_development_private.json') != lock['frozen_development_sha256']:
        raise ValueError('Frozen development changed.')
    return original, frozen, lock
