"""E020 byte-preservation gates, including append-only history."""
import hashlib
import json
from pathlib import Path
from .e019_checker import sha
from .e019_integrity import canonical

PROTOCOL_SHA='1c018789dbcba1cbdd7d7096a7e2830c2a547304297154a76345bcde7941ede2'


def preserve_e020(root):
    root=Path(root).resolve()
    receipt=json.loads((root/'experiments/e020_preservation_start.json').read_text())
    private=root/'artifacts/e020_setup/preservation_private.json'
    if sha(private)!=receipt['private_inventory_sha256']: raise ValueError('Preservation inventory changed.')
    inventory=json.loads(private.read_text())
    if len(inventory['files'])!=receipt['preserved_files']: raise ValueError('Preservation count changed.')
    for name,record in inventory['files'].items():
        p=(root/name).resolve()
        if not p.is_relative_to(root): raise ValueError('Preservation path escaped project.')
        if record['prefix']:
            actual=hashlib.sha256(p.read_bytes()[:record['bytes']]).hexdigest()
        else: actual=sha(p)
        if actual!=record['sha256']: raise ValueError('Historical file changed: '+name)
    if canonical(root/'docs/E020_PROTOCOL.md')!=PROTOCOL_SHA: raise ValueError('Approved E020 protocol changed.')
    if json.loads((root/'experiments/e018_verification_gate.json').read_text())['gate_passed']:
        raise ValueError('E018 blocked status changed.')
    return len(inventory['files'])


def verify_readiness(root):
    root=Path(root); lock=json.loads((root/'experiments/e020_readiness_lock.json').read_text())
    for name,digest in lock['files'].items():
        if canonical(root/name)!=digest: raise ValueError('Readiness file changed.')
    prefix=lock['execution_prefix']
    if hashlib.sha256((root/'docs/E020_EXECUTION.md').read_bytes()[:prefix['bytes']]).hexdigest()!=prefix['sha256']:
        raise ValueError('Readiness execution prefix changed.')
    return lock
