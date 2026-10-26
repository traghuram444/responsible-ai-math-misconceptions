"""Additional E020 MAP-phase lock; never replaces readiness evidence."""
import hashlib
import json
from pathlib import Path
from .e019_checker import sha
from .e019_integrity import canonical
from .e020_integrity import verify_readiness


def verify_map(root):
    root=Path(root); verify_readiness(root)
    lock=json.loads((root/'experiments/e020_map_lock.json').read_text())
    if lock['readiness_lock_sha256']!=sha(root/'experiments/e020_readiness_lock.json'): raise ValueError('Readiness lock changed.')
    for name,digest in lock['files'].items():
        p=(root/name).resolve()
        if not p.is_relative_to(root.resolve()) or canonical(p)!=digest: raise ValueError('MAP code/report file changed.')
    for name,record in lock['append_only_prefixes'].items():
        if hashlib.sha256((root/name).read_bytes()[:record['bytes']]).hexdigest()!=record['sha256']:
            raise ValueError('MAP documentation prefix changed.')
    ready=json.loads((root/'results/E020_readiness.json').read_text())
    if sha(root/'results/E020_readiness.json')!=lock['readiness_result_sha256'] or ready['status']!='READY_FOR_MAP_IMPLEMENTATION_CHECK':
        raise ValueError('MAP readiness gate unmet.')
    if ready['projected_map_seconds']>48*3600 or not all(r['gate_passed'] for r in ready['model_receipts']):
        raise ValueError('Runtime or readiness gate unmet.')
    return lock


def no_failures(attempt):
    if any(Path(attempt).rglob('*failure.json')): raise ValueError('Failure receipt exists; no retry or continuation.')


def verify_readiness_evidence(root,lock):
    root=Path(root); folder=root/'artifacts/e020_attempt01'
    inventory=folder/'map_inputs/readiness_preservation_private.json'
    if sha(inventory)!=lock['readiness_private_inventory_sha256']: raise ValueError('Readiness evidence inventory changed.')
    for name,digest in json.loads(inventory.read_text()).items():
        p=(folder/name).resolve()
        if not p.is_relative_to(folder.resolve()) or sha(p)!=digest: raise ValueError('Readiness evidence changed.')


def verify_caches(root,out,lock):
    """Reads private caches in memory; returns no values to terminal/publication."""
    from .e019_checker import load_catalogue
    from .e020_checker import REASONS
    import numpy as np
    path=Path(root)/'artifacts/e020_attempt01/map_inputs/catalogue.json'
    if sha(path)!=lock['catalogue_sha256']: raise ValueError('Catalogue changed.')
    pairs=load_catalogue(path); caches={}; receipts={}
    if len(pairs)!=60: raise ValueError('Pair population changed.')
    for key in ('G15','G7'):
        folder=Path(out)/key; receipt=json.loads((folder/'completion_private.json').read_text())
        cachepath=folder/'cache_private.json'
        if receipt['status']!='COMPLETED' or receipt['model']!=key or receipt['pairs']!=60 or receipt['cache_sha256']!=sha(cachepath):
            raise ValueError('Incomplete or changed cache.')
        if receipt['catalogue_sha256']!=lock['catalogue_sha256'] or receipt['lock_sha256']!=sha(Path(root)/'experiments/e020_map_lock.json'):
            raise ValueError('Checker provenance changed.')
        rows=json.loads(cachepath.read_text())
        if len(rows)!=60: raise ValueError('Cache length changed.')
        for i,r in enumerate(rows):
            if r!=json.loads((folder/f'pair_{i:04d}_private.json').read_text()): raise ValueError('Pair/cache mismatch.')
            if r['reason'] not in REASONS: raise ValueError('Unknown checker reason.')
            scores=np.asarray(r['scores'],dtype=np.float64)
            if scores.shape!=(3,) or not np.isfinite(scores).all() or (scores<0).any() or not np.isclose(scores.sum(),1,atol=1e-12,rtol=0):
                raise ValueError('Malformed checker scores.')
            if r['decision']!=int(np.argmax(scores)): raise ValueError('Decision mismatch.')
            if r['reason']!='readout_completed' and r['scores']!=[0,0,1]: raise ValueError('Fallback vector changed.')
        caches[key]=rows; receipts[key]=receipt
    return pairs,caches,receipts
