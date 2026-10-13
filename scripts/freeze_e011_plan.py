"""Create the execution lock once, before E011; never overwrite an existing lock."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = '7eaea0a584c03ed6d5d3821f286505995771a577'

def digest(raw): return hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--image-id', required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'sha256:[0-9a-f]{64}', args.image_id): raise ValueError('Image identity required.')
    destination = ROOT / 'experiments/e011_e012_lock.json'
    if destination.exists(): raise ValueError('Existing lock; refuse overwrite.')
    old = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE], cwd=ROOT).decode().splitlines()
    protected = {p: digest(subprocess.check_output(['git', 'show', f'{BASE}:{p}'], cwd=ROOT)) for p in old if p not in ('README.md', 'docs/EXPERIMENT_LOG.md')}
    files = ['docs/E011_PROTOCOL.md', 'docs/E012_PROTOCOL.md', 'src/map_misconceptions/e011_context.py',
             'src/map_misconceptions/e011_publication.py', 'scripts/run_e011_context.py', 'scripts/publish_e011_context.py',
             'scripts/run_e011_context_docker.ps1', 'scripts/monitor_e011_context.py', 'scripts/freeze_e011_plan.py',
             'tests/test_e011_context.py', 'repro/core.lock', 'repro/Dockerfile']
    payload = {'status': 'authorized_locked_before_execution', 'baseline_commit': BASE,
        'docker_image_id': args.image_id, 'hash_convention': 'sha256; CRLF normalized to LF only',
        'files': {p: digest((ROOT / p).read_bytes()) for p in files}, 'preserved': protected}
    with destination.open('x', encoding='utf-8', newline='\n') as stream: stream.write(json.dumps(payload, indent=2, sort_keys=True) + '\n')
    print(f'Locked {len(files)} execution files and {len(protected)} preserved historical files.')
