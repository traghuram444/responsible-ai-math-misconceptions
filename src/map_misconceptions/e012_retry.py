"""Approved infrastructure-only adapter; the locked scientific main is reused."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import sys

from . import e011_context as core
from .data_contract import file_sha256
from .e006 import write_new
from .resilient_status import ResilientStatus

ROOT = Path(__file__).resolve().parents[2]
ATTEMPT = 'e012_attempt02'
OLD_NAMES = {'attempt': 'attempt.json', 'failure': 'failure.json', 'terminal_status': 'live_status.json'}


def verify_amendment(root=ROOT, *, local_failed=None):
    lock = json.loads((root / 'experiments/e012_attempt02_lock.json').read_text(encoding='utf-8'))
    if lock['attempt_id'] != ATTEMPT or lock['scientific_settings_changed'] is not False:
        raise ValueError('Unexpected amendment.')
    core.checked_lock(root, lock['docker_image_id'])
    for group in ('files', 'preserved'):
        for name, sha in lock[group].items():
            path = (root / name).resolve()
            if not path.is_relative_to(root.resolve()) or core.canonical_sha(path) != sha:
                raise ValueError('Amendment or history changed.')
    if local_failed is not None:
        record = json.loads((root / 'results/E012_execution_failure.json').read_text(encoding='utf-8'))
        for key, name in OLD_NAMES.items():
            if file_sha256(local_failed / name) != record['source_sha256'][key]:
                raise ValueError('Failed attempt changed.')
    return lock


def invoke_unchanged_main(revision, image_id, reference_sha):
    saved_status, saved_argv = core.LiveStatus, sys.argv
    try:
        core.LiveStatus = ResilientStatus
        sys.argv = ['run_e012_attempt02', '--experiment', 'E012', '--git-revision', revision,
                    '--image-id', image_id, '--e011-sha', reference_sha]
        core.main()
    finally:
        core.LiveStatus, sys.argv = saved_status, saved_argv


def sanitized_exception(exc):
    # Retain operation/function identifiers only, never traceback source lines,
    # exception messages, filenames or frame locals.
    while exc.__cause__ is not None or exc.__context__ is not None:
        exc = exc.__cause__ if exc.__cause__ is not None else exc.__context__
    functions = []
    tb = exc.__traceback__
    while tb is not None:
        name = tb.tb_frame.f_code.co_name
        functions.append(name if re.fullmatch('[A-Za-z_][A-Za-z0-9_]{0,99}', name) else 'redacted')
        tb = tb.tb_next
    return {'error_type': type(exc).__name__, 'errno': getattr(exc, 'errno', None), 'function_chain': functions[-8:]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-revision', required=True)
    parser.add_argument('--image-id', required=True)
    args = parser.parse_args()
    if not re.fullmatch('[0-9a-f]{40}', args.git_revision) or os.getuid() != 10001 or os.getgid() != 10001:
        raise ValueError('Exact revision and non-root identity required.')
    old = ROOT / 'artifacts/e012_failed_attempt01'
    lock = verify_amendment(local_failed=old)
    if args.image_id != lock['docker_image_id']:
        raise ValueError('Image changed.')
    output = ROOT / 'artifacts/e012'  # Bound to NEW host attempt directory by the launcher.
    if not output.is_dir() or any(output.iterdir()):
        raise ValueError('Empty new attempt directory required; no retry overwrite.')
    metadata = {'attempt_id': ATTEMPT, 'git_revision': args.git_revision,
                'amendment_lock_sha256': file_sha256(ROOT / 'experiments/e012_attempt02_lock.json'),
                'scientific_lock_sha256': file_sha256(ROOT / 'experiments/e011_e012_lock.json'),
                'failed_attempt_preserved': True, 'scientific_settings_changed': False}
    write_new(output / 'retry_authorization.json', metadata)
    try:
        invoke_unchanged_main(args.git_revision, args.image_id, file_sha256(ROOT / 'results/E011_aggregates.json'))
        verify_amendment(local_failed=old)
        receipt = {**metadata, 'status': 'COMPLETED', 'monitor': ResilientStatus.last_instance.diagnostics(),
                   'results_sha256': file_sha256(output / 'results.json')}
        write_new(output / 'retry_execution.json', receipt)
        print(json.dumps(receipt), flush=True)
    except BaseException as exc:
        diagnostic = {**metadata, 'status': 'FAILED', 'exception': sanitized_exception(exc),
                      'monitor': ResilientStatus.last_instance.diagnostics() if ResilientStatus.last_instance else None}
        try:
            write_new(output / 'retry_diagnostics.json', diagnostic)
        except OSError:
            pass
        try:
            print(json.dumps(diagnostic), flush=True)
        except OSError:
            pass
        raise RuntimeError('Attempt stopped; sanitized diagnostics only; no automatic retry.') from None


if __name__ == '__main__': main()
