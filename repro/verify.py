"""Offline verification of synthetic tests and public aggregates; no MAP fitting."""
import importlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

from audit_release import check_history

ROOT = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    print(f'Preserved historical files: {check_history()}', flush=True)
    subprocess.run([sys.executable, '-m', 'pip', 'check'], check=True)
    subprocess.run([sys.executable, '-m', 'pytest', '-q', '-p', 'no:cacheprovider'], cwd=ROOT, check=True)
    spec = importlib.util.spec_from_file_location('publish_e006', ROOT / 'scripts/publish_e006_results.py')
    publication = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(publication)
    e006 = json.loads((ROOT / 'results/E006_aggregates.json').read_text(encoding='utf-8'))
    if publication.sanitize_payload(e006, e006['source_artifact_sha256']) != e006:
        raise ValueError('E006 public artifact differs from its sanitized/recomputed aggregate.')
    print('E006: public allowlist and recomputed aggregates verified.', flush=True)
    for experiment in ('e007', 'e008', 'e009', 'e010'):
        payload = json.loads((ROOT / f'results/{experiment.upper()}_aggregates.json').read_text(encoding='utf-8'))
        importlib.import_module(f'map_misconceptions.{experiment}_publication').validate_public_payload(payload)
        print(f'{experiment.upper()}: public schema and aggregate consistency verified.', flush=True)
    subprocess.run([sys.executable, 'repro/make_figures.py', '--check'], cwd=ROOT, check=True)
    print('Verification complete; no source dataset loaded and no research experiment run.', flush=True)
