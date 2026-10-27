"""E021 additive locks and historical preservation; no experiment computation."""
import hashlib
import json
from pathlib import Path
from .e019_checker import sha
from .e019_integrity import canonical
from .e020_recovery_integrity import verify as verify_e020
IMAGE='sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0'
PROTOCOL='1ab62b89f1bf8fe1e4845194b7a73d7c5233264b75babff239e29c2761887091'
REFERENCE='8a5fcfd894c4dd6b24607b330376ba4afbe0dff0f207ee1622365e6e855a8e2c'
CACHE='00830d9a7a64735682fce41655b55adf6c088105c339913eac4e604b4275bb13'
OUT='artifacts/e021_attempt01'


def preserve(root):
    root=Path(root); verify_e020(root)
    if canonical(root/'docs/E021_PROTOCOL.md')!=PROTOCOL or sha(root/'results/E020_aggregates.json')!=REFERENCE:
        raise ValueError('Approved protocol or reference changed.')
    lock=json.loads((root/'experiments/e021_lock.json').read_text())
    private=root/'artifacts/e021_setup/preservation_private.json'
    if sha(private)!=lock['preservation_inventory_sha256']: raise ValueError('Preservation inventory changed.')
    inventory=json.loads(private.read_text())
    if len(inventory)!=lock['preserved_files']: raise ValueError('Preservation count differs.')
    for name,r in inventory.items():
        path=(root/name).resolve()
        if not path.is_relative_to(root.resolve()): raise ValueError('Preservation path escaped.')
        actual=hashlib.sha256(path.read_bytes()[:r['bytes']]).hexdigest() if r['prefix'] else sha(path)
        if actual!=r['sha256']: raise ValueError('Historical preservation failed.')
    for name,digest in lock['files'].items():
        if canonical(root/name)!=digest: raise ValueError('E021 locked implementation changed.')
    for name,r in lock['append_only_prefixes'].items():
        if hashlib.sha256((root/name).read_bytes()[:r['bytes']]).hexdigest()!=r['sha256']: raise ValueError('E021 documentation prefix changed.')
    if lock['image_id']!=IMAGE: raise ValueError('Image differs.')
    return lock


def no_failures(folder):
    if any(Path(folder).rglob('*failure.json')): raise ValueError('E021 failure receipt exists; stop for review.')
