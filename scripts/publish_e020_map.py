"""Publish only completed, verified aggregate E020 MAP results and full tables."""
import json
from pathlib import Path
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e020_integrity import preserve_e020
from map_misconceptions.e020_map_integrity import verify_map,no_failures,verify_readiness_evidence,verify_caches
from map_misconceptions.e020_map_publication import validate,render
from map_misconceptions.e011_publication import same


def main():
    root=Path(__file__).resolve().parents[1]; out=root/'artifacts/e020_attempt01/map'
    no_failures(out.parent); lock=verify_map(root); preserve_e020(root); verify_readiness_evidence(root,lock)
    execution=json.loads((out/'execution.json').read_text()); path=out/'aggregate_results.json'
    if execution['status']!='COMPLETED' or execution['results_sha256']!=sha(path): raise ValueError('Incomplete or changed aggregates.')
    p=json.loads(path.read_text()); validate(p)
    if p['integrity']['lock_sha256']!=sha(root/'experiments/e020_map_lock.json'): raise ValueError('MAP lock changed.')
    if p['integrity']['git_revision']!=execution['git_revision']: raise ValueError('Commit receipt mismatch.')
    start=json.loads((out/'started.json').read_text())
    if start['git_revision']!=execution['git_revision'] or start['lock_sha256']!=p['integrity']['lock_sha256']: raise ValueError('Start receipt mismatch.')
    _,_,receipts=verify_caches(root,out,lock)
    if {k:r['cache_sha256'] for k,r in receipts.items()}!=p['integrity']['cache_sha256']: raise ValueError('Cache receipt mismatch.')
    frozen=out/'frozen_development_private.json'
    if sha(frozen)!=p['integrity']['frozen_development_sha256']: raise ValueError('Development changed.')
    development=json.loads(frozen.read_text())
    same(p['development'],development['development']); same(p['ensemble_development'],development['ensemble_development'])
    for name,digest in development['prediction_sha256'].items():
        if sha(out/name)!=digest: raise ValueError('Frozen predictions changed.')
    text=render(p)
    write_new(root/'results/E020_aggregates.json',p)
    if sha(root/'results/E020_aggregates.json')!=sha(path): raise ValueError('Public aggregate byte mismatch.')
    with (root/'docs/E020_RESULTS.md').open('x',encoding='utf-8',newline='\n') as stream: stream.write(text)
    print('All registered E020 aggregate/fold/question/support/calibration/correctness/review tables published; no interpretation.')


if __name__=='__main__': main()
