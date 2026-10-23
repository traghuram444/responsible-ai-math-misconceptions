"""Resolve the approved CPU wheel closure, without any data/model mount."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile
from email.parser import BytesParser

DEST = Path('/output')
WHEELS = DEST / 'wheels'
DIRECT = ['transformers==4.46.3', 'tokenizers==0.20.3',
          'huggingface-hub==0.26.2', 'safetensors==0.4.5',
          'numpy==1.26.4', 'PyYAML==6.0.2']


def pip(*args):
    subprocess.run([sys.executable, '-m', 'pip', *args], check=True)


def main():
    if WHEELS.exists():
        raise ValueError('Preserve previous resolver output; do not overwrite.')
    WHEELS.mkdir()
    pip('download', '--only-binary=:all:', '--no-deps', '-d', str(WHEELS), 'pip==24.3.1')
    pip('install', '--no-index', '--find-links', str(WHEELS), '--target', '/tmp/pinned-pip', 'pip==24.3.1')
    sys.path.insert(0, '/tmp/pinned-pip')
    # Make subprocesses use this exact installer; never install into the host.
    import os
    os.environ['PYTHONPATH'] = '/tmp/pinned-pip'
    pip('--version')
    pip('download', '--only-binary=:all:', '--no-deps', '--index-url',
        'https://download.pytorch.org/whl/cpu', '-d', str(WHEELS), 'torch==2.5.1+cpu')
    torch = next(WHEELS.glob('torch-*.whl'))
    pip('download', '--only-binary=:all:', '-d', str(WHEELS), str(torch), *DIRECT)
    records = []
    for path in sorted(WHEELS.glob('*.whl')):
        with zipfile.ZipFile(path) as archive:
            metadata = [x for x in archive.namelist() if x.endswith('.dist-info/METADATA')]
            if len(metadata) != 1: raise ValueError('Wheel metadata ambiguity.')
            parsed = BytesParser().parsebytes(archive.read(metadata[0]))
        records.append({'name': parsed['Name'], 'version': parsed['Version'],
                        'file': path.name, 'sha256': hashlib.file_digest(path.open('rb'), 'sha256').hexdigest()})
    if len({x['name'].lower().replace('_','-') for x in records}) != len(records):
        raise ValueError('Duplicate packages.')
    with (DEST / 'requirements.lock').open('x') as f:
        f.write(''.join(f"{r['name']}=={r['version']} --hash=sha256:{r['sha256']}\n" for r in records))
    with (DEST / 'wheel_manifest.json').open('x') as f:
        json.dump(records, f, indent=2); f.write('\n')
    print(json.dumps({'resolved_wheels': len(records), 'private_data_access': False}))


if __name__ == '__main__': main()
