"""Additive E022 preservation gates; historical checks stay read-only."""
import hashlib
import json
from pathlib import Path
from .e019_checker import sha
from .e019_integrity import canonical
from .e021_integrity import preserve as preserve_e021,IMAGE,CACHE

PROTOCOL='cc635bb0f83407a0c2652bd0c717ecad5d9430a0a5c1168e9231abee737baef2'
REFERENCE='7dee7d0d8772744524630b9358b14a685aec3ac5cb2bef7ca01c396c022dde3c'
FROZEN='92d843364bdb95cf044260fc665adffbd46b618fe50178d76b7b0545474dd0cf'
OUT='artifacts/e022_attempt01'


def preserve(root):
    root=Path(root); preserve_e021(root)
    for name,digest in (('results/E021_aggregates.json',REFERENCE),('artifacts/e021_attempt01/frozen_development_private.json',FROZEN)):
        if sha(root/name)!=digest: raise ValueError('E021 evidence changed.')
    if canonical(root/'docs/E022_PROTOCOL.md')!=PROTOCOL: raise ValueError('Approved E022 protocol changed.')
    lock=json.loads((root/'experiments/e022_lock.json').read_text())
    private=root/'artifacts/e022_setup/preservation_private.json'
    if sha(private)!=lock['preservation_inventory_sha256']: raise ValueError('Preservation inventory changed.')
    records=json.loads(private.read_text())
    if len(records)!=lock['preserved_files']: raise ValueError('Preservation count differs.')
    for name,r in records.items():
        path=(root/name).resolve()
        if not path.is_relative_to(root.resolve()): raise ValueError('Preservation path escaped.')
        actual=hashlib.sha256(path.read_bytes()[:r['bytes']]).hexdigest() if r['prefix'] else sha(path)
        if actual!=r['sha256']: raise ValueError('Historical preservation failed.')
    for name,digest in lock['files'].items():
        if canonical(root/name)!=digest: raise ValueError('E022 code lock changed.')
    for name,r in lock['append_only_prefixes'].items():
        if hashlib.sha256((root/name).read_bytes()[:r['bytes']]).hexdigest()!=r['sha256']: raise ValueError('Documentation prefix changed.')
    if lock['image_id']!=IMAGE or lock['protocol_sha256']!=PROTOCOL: raise ValueError('Lock identity differs.')
    return lock


def no_failures(out):
    if any(Path(out).rglob('*failure.json')): raise ValueError('E022 failure receipt exists; stop for review.')
