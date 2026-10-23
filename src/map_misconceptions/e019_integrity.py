"""Project-scoped, byte-preserving E019 integrity gates; standard library only."""
import hashlib
import json
from pathlib import Path
from .e019_checker import sha

PROTOCOL_SHA = 'c16bdaddb55250e91422ec7ef0d1782d1af60df1191fcc8d134401045b4b0ad3'


def canonical(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b'\r\n',b'\n')).hexdigest()


def preserve(root):
    root=Path(root)
    baseline=json.loads((root/'experiments/e019_preservation_start.json').read_text())
    for name,expected in baseline['files'].items():
        path=(root/name).resolve()
        if not path.is_relative_to(root.resolve()): raise ValueError('Path escaped project.')
        if name=='docs/EXPERIMENT_LOG.md':
            actual=hashlib.sha256(path.read_bytes()[:baseline['log_bytes']]).hexdigest()
        else: actual=sha(path)
        if actual!=expected: raise ValueError('An existing file changed: '+name)
    if canonical(root/'docs/E019_PROTOCOL.md')!=PROTOCOL_SHA: raise ValueError('Approved protocol changed.')
    if json.loads((root/'experiments/e018_verification_gate.json').read_text())['gate_passed']:
        raise ValueError('E018 status changed.')
    return len(baseline['files'])


def verify_files(root,lock):
    for name,digest in lock['files'].items():
        if canonical(Path(root)/name)!=digest: raise ValueError('E019 locked file changed.')
    prefix=lock['execution_log_prefix']
    raw=(Path(root)/'docs/E019_EXECUTION.md').read_bytes()[:prefix['bytes']]
    if hashlib.sha256(raw).hexdigest()!=prefix['sha256']: raise ValueError('Preparation record changed.')


def model_files(model,manifest):
    for name,record in manifest['files'].items():
        path=Path(model)/name
        if path.stat().st_size!=record['bytes'] or sha(path)!=record['sha256']:
            raise ValueError('Model identity mismatch.')
