"""Additive E023 preservation gates; historical checks stay read-only."""
import hashlib
import json
from pathlib import Path
from .e019_checker import sha
from .e019_integrity import canonical
from .e022_integrity import preserve as preserve_e022,IMAGE,CACHE

PROTOCOL='a7aabfb30dd5a8960af161f25f8237247ee571e21a7e6225fb201b971d7574ac'
REFERENCE='9578d9fc08c278751112fa1aadc52c0b1d6276e2a0b309d4ff54c455c2e6164f'
FROZEN='f742b17fc43d553d5a8a6de95b79837ef58d1eab66db59d1f56df32072705964'
OUT='artifacts/e023_attempt01'


def preserve(root):
    root=Path(root); preserve_e022(root)
    for name,digest in (('results/E022_aggregates.json',REFERENCE),('artifacts/e022_attempt01/frozen_development_private.json',FROZEN)):
        if sha(root/name)!=digest: raise ValueError('E022 evidence changed.')
    if canonical(root/'docs/E023_PROTOCOL.md')!=PROTOCOL: raise ValueError('Approved E023 protocol changed.')
    lock=json.loads((root/'experiments/e023_lock.json').read_text())
    private=root/'artifacts/e023_setup/preservation_private.json'
    if sha(private)!=lock['preservation_inventory_sha256']: raise ValueError('Preservation inventory changed.')
    records=json.loads(private.read_text())
    if len(records)!=lock['preserved_files']: raise ValueError('Preservation count differs.')
    for name,r in records.items():
        path=(root/name).resolve()
        if not path.is_relative_to(root.resolve()): raise ValueError('Preservation path escaped.')
        actual=hashlib.sha256(path.read_bytes()[:r['bytes']]).hexdigest() if r['prefix'] else sha(path)
        if actual!=r['sha256']: raise ValueError('Historical preservation failed.')
    for name,digest in lock['files'].items():
        if canonical(root/name)!=digest: raise ValueError('E023 code lock changed.')
    for name,r in lock['append_only_prefixes'].items():
        if hashlib.sha256((root/name).read_bytes()[:r['bytes']]).hexdigest()!=r['sha256']: raise ValueError('Documentation prefix changed.')
    if lock['image_id']!=IMAGE or lock['protocol_sha256']!=PROTOCOL: raise ValueError('Lock identity differs.')
    return lock


def no_failures(out):
    if any(Path(out).rglob('*failure.json')): raise ValueError('E023 failure receipt exists; stop for review.')
