"""Freeze the explicitly authorized reporting repair without altering the attempt."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from map_misconceptions.e019_checker import sha, write_new
from map_misconceptions.e019_integrity import canonical
from map_misconceptions.e020_recovery_integrity import SOURCE, LOCK, FILES, source_gate, inventory


def main():
    source_gate(ROOT)
    folder = ROOT/'artifacts/e020_recovery_setup'
    folder.mkdir(exist_ok=False)
    records = inventory(ROOT/'artifacts/e020_attempt01')
    private = folder/'failed_attempt_inventory_private.json'
    write_new(private, records)
    prefixes = {}
    for name in ('docs/E020_EXECUTION.md', 'docs/EXPERIMENT_LOG.md'):
        raw = (ROOT/name).read_bytes()
        prefixes[name] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    write_new(ROOT/LOCK, {
        'experiment_id': 'E020', 'phase': 'authorized_reporting_recovery',
        'source_commit': subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'original_map_lock_sha256': sha(ROOT/'experiments/e020_map_lock.json'),
        'failed_attempt_inventory_sha256': sha(private), 'failed_attempt_files': len(records),
        'frozen_development_sha256': sha(ROOT/SOURCE/'frozen_development_private.json'),
        'files': {name: canonical(ROOT/name) for name in FILES},
        'append_only_prefixes': prefixes, 'new_model_calls': 0, 'new_classifier_fits': 0})
    print(f'Reporting recovery locked; {len(records)} failed-attempt files preserved; no scoring performed.')


if __name__ == '__main__': main()
