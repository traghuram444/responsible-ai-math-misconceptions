"""Frozen E022 publisher: completed, preserved, strictly validated aggregates only."""
import json
from pathlib import Path
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e022_integrity import preserve,no_failures,OUT,PROTOCOL,REFERENCE,CACHE,IMAGE
from map_misconceptions.e022_run import verify_freeze
from map_misconceptions.e022_publication import validate,render
from map_misconceptions.e020_map_integrity import verify_map,verify_caches
from map_misconceptions.e011_publication import same


def main():
    root=Path(__file__).resolve().parents[1]; out=root/OUT
    lock=preserve(root); no_failures(out)
    completion=json.loads((out/'execution.json').read_text()); start=json.loads((out/'started.json').read_text())
    p=json.loads((out/'aggregate_results.json').read_text()); validate(p)
    if completion['status']!='COMPLETED' or completion['results_sha256']!=sha(out/'aggregate_results.json'): raise ValueError('Completion/hash differs.')
    for r in (completion,p['integrity']):
        same(r['git_revision'],start['git_revision']); same(r['lock_sha256'],sha(root/'experiments/e022_lock.json'))
    same(start['lock_sha256'],p['integrity']['lock_sha256'])
    for k,v in {'protocol_sha256':PROTOCOL,'reference_sha256':REFERENCE,'g7_cache_sha256':CACHE,'preserved_files':lock['preserved_files']}.items(): same(p['integrity'][k],v)
    same(p['resources']['image_id'],IMAGE)
    frozen=verify_freeze(out,p['integrity']['freeze_sha256'])
    same(p['development'],frozen['development']); same(p['policies'],frozen['policies'])
    verify_caches(root,root/'artifacts/e020_attempt01/map',verify_map(root))
    text=render(p)
    for name in ('results/E022_aggregates.json','docs/E022_RESULTS.md'):
        if (root/name).exists(): raise ValueError('Publication already exists.')
    write_new(root/'results/E022_aggregates.json',p)
    with (root/'docs/E022_RESULTS.md').open('x',encoding='utf-8',newline='\n') as stream: stream.write(text)
    if sha(root/'results/E022_aggregates.json')!=completion['results_sha256']: raise ValueError('Public byte mismatch.')
    preserve(root); no_failures(out)
    print('E022 complete aggregate, fold, question, support, calibration and cutoff tables published; no interpretation.')


if __name__=='__main__': main()
