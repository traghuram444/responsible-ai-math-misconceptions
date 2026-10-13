"""Publication checks; never print matched text, tokens, or response prefixes."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
HISTORY = ROOT / 'repro/history.json'
BASE = '7bd41443e8a88024f05144d49902c69f9da76a08'
PRIVATE_DIRS = {'data', 'artifacts', '.venv', '__pycache__', '.pytest_cache', '.cache', '.docker', '.aws'}
PRIVATE_SUFFIXES = {'.csv', '.tsv', '.jsonl', '.zip', '.tar', '.gz', '.parquet', '.feather', '.arrow',
                    '.npy', '.npz', '.pkl', '.pickle', '.joblib', '.pt', '.bin', '.ckpt', '.safetensors',
                    '.pem', '.key', '.p12', '.pfx', '.pyc'}
TEXT_SUFFIXES = {'.md', '.py', '.ps1', '.json', '.yaml', '.yml', '.toml', '.txt', '.lock', '.cff', '.svg'}
SECRET = re.compile(r'C:\\Users\\|/' r'Users/|/' r'home/|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[A-Z0-9]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def canonical(data):
    # Git text checkout may use CRLF on Windows; preserve all other bytes.
    return data.replace(b'\r\n', b'\n')


def digest(data):
    return hashlib.sha256(canonical(data)).hexdigest()


def path_allowed(name):
    p = PurePosixPath(name)
    return (not p.is_absolute() and '..' not in p.parts and '\\' not in name
            and not PRIVATE_DIRS.intersection(p.parts)
            and not any(part.endswith('.egg-info') for part in p.parts)
            and not any(part.startswith('.env') for part in p.parts)
            and p.name != 'credentials.json' and p.suffix.lower() not in PRIVATE_SUFFIXES
            and (p.suffix.lower() in TEXT_SUFFIXES or p.name in {'Dockerfile', 'LICENSE', '.gitignore', '.gitattributes', '.dockerignore'}))


def freeze_history():
    if HISTORY.exists():
        raise ValueError('History inventory already exists; do not overwrite it.')
    files = git('ls-tree', '-r', '--name-only', BASE).decode().splitlines()
    protected = {p: digest(git('show', f'{BASE}:{p}')) for p in files
                 if p not in {'README.md', 'docs/EXPERIMENT_LOG.md'}}
    log = canonical(git('show', f'{BASE}:docs/EXPERIMENT_LOG.md'))
    payload = {'baseline_commit': BASE, 'hash_convention': 'sha256; CRLF normalized to LF only',
               'protected': protected, 'append_only_log': {'bytes': len(log), 'sha256': digest(log)}}
    HISTORY.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(f'Captured {len(protected)} protected public files and append-only log prefix.')


def check_history(root=ROOT):
    history = json.loads((root / 'repro/history.json').read_text(encoding='utf-8'))
    for name, expected in history['protected'].items():
        if not path_allowed(name) or digest((root / name).read_bytes()) != expected:
            raise ValueError(f'Historical file changed: {name}')
    log = canonical((root / 'docs/EXPERIMENT_LOG.md').read_bytes())
    prefix = history['append_only_log']
    if digest(log[:prefix['bytes']]) != prefix['sha256']:
        raise ValueError('Historical experiment-log prefix changed.')
    return len(history['protected'])


def audit(private_prefixes=False):
    # Include new, nonignored files so a pre-commit scan covers proposed additions.
    names = sorted(set(git('ls-files', '-z', '--cached', '--others', '--exclude-standard').decode().split('\0')) - {''})
    texts = []
    for name in names:
        if not path_allowed(name):
            raise ValueError(f'Disallowed publication path: {name}')
        path = ROOT / name
        if path.is_symlink():
            raise ValueError(f'Symlink not permitted: {name}')
        text = path.read_text(encoding='utf-8')
        if SECRET.search(text):
            raise ValueError(f'Secret or local-path pattern in: {name}')
        if name.endswith('.svg') and re.search(r'<script|<foreignObject|(?:href|onload)\s*=', text, re.I):
            raise ValueError(f'Active or externally linked SVG: {name}')
        texts.append(' '.join(text.casefold().split()))
    print(f'Publication path/text checks passed: {len(names)} files; no matching secret/local-path patterns.')
    print(f'Historical preservation passed: {check_history()} protected files plus log prefix.')
    if private_prefixes:
        # Local audit only. CI never downloads or requires MAP data.
        with (ROOT / 'data/raw/train.csv').open(encoding='utf-8', newline='') as stream:
            prefixes = {' '.join(r['StudentExplanation'].casefold().split())[:80] for r in csv.DictReader(stream)}
        prefixes = {p for p in prefixes if len(p) >= 40}
        haystack = '\n'.join(texts)
        hits = sum(p in haystack for p in prefixes)
        print(f'Private response-prefix check: {len(prefixes)} unique prefixes; {hits} matches.')
        if hits:
            raise ValueError('Possible response text detected; publication blocked (content suppressed).')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--freeze-history', action='store_true')
    parser.add_argument('--private-prefixes', action='store_true')
    args = parser.parse_args()
    if args.freeze_history:
        freeze_history()
    else:
        audit(args.private_prefixes)
