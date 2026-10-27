"""Publish strictly validated E020 recovery aggregates with explicit failure history."""
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e020_recovery_integrity import verify,SOURCE,OUT,LOCK
from map_misconceptions.e020_map_integrity import verify_caches,no_failures
from map_misconceptions.e020_map_publication import validate,render
from map_misconceptions.e011_publication import same
from map_misconceptions import e007_publication as s

SCHEMA={'experiment_id':s.enum('E020'),'status':s.enum('COMPLETED'),'phase':s.enum('reporting_recovery'),
    'results_sha256':s.HASH,'original_git_revision':s.pattern('[0-9a-f]{40}'),
    'recovery_git_revision':s.pattern('[0-9a-f]{40}'),'recovery_lock_sha256':s.HASH,
    'original_map_lock_sha256':s.HASH,'failed_attempt_inventory_sha256':s.HASH,'failed_attempt_files':s.I,
    'frozen_development_sha256':s.HASH,'source_failure_types':s.listing(s.enum('KeyError','CalledProcessError')),
    'failed_attempt_preserved':s.enum(True),'category_view_reconstructed':s.enum(True),
    'new_model_calls':s.enum(0),'new_classifier_fits':s.enum(0),
    'original_statistical_seconds':s.N,'recovery_seconds':s.N,
    'finished_utc':s.pattern(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:.]+\+00:00')}


def validate_receipt(receipt):
    s.validate_schema(receipt,SCHEMA)
    if receipt['source_failure_types']!=['KeyError','CalledProcessError']:
        raise ValueError('Failure history differs.')
    if min(receipt['original_statistical_seconds'],receipt['recovery_seconds'])<0:
        raise ValueError('Negative elapsed time.')
    return receipt


def main():
    out=ROOT/OUT; source=ROOT/SOURCE
    no_failures(out); original,frozen,lock=verify(ROOT)
    receipt=validate_receipt(json.loads((out/'execution.json').read_text()))
    path=out/'aggregate_results.json'; p=json.loads(path.read_text()); validate(p)
    start=json.loads((out/'started.json').read_text())
    if receipt['results_sha256']!=sha(path) or receipt['recovery_git_revision']!=start['git_revision']:
        raise ValueError('Recovery completion mismatch.')
    if receipt['recovery_lock_sha256']!=sha(ROOT/LOCK) or start['lock_sha256']!=sha(ROOT/LOCK):
        raise ValueError('Recovery lock changed.')
    if receipt['original_git_revision']!=json.loads((source/'started.json').read_text())['git_revision']:
        raise ValueError('Original provenance changed.')
    for key in ('failed_attempt_inventory_sha256','failed_attempt_files','frozen_development_sha256','original_map_lock_sha256'):
        same(receipt[key],lock[key])
    same(p['integrity']['git_revision'],receipt['original_git_revision'])
    same(p['integrity']['lock_sha256'],receipt['original_map_lock_sha256'])
    same(p['integrity']['frozen_development_sha256'],receipt['frozen_development_sha256'])
    same(receipt['original_statistical_seconds'],json.loads((source/'statistics_status.json').read_text())['elapsed_seconds'])
    same(p['resource_summary']['statistical_seconds'],receipt['original_statistical_seconds']+receipt['recovery_seconds'])
    _,_,caches=verify_caches(ROOT,source,original)
    same(p['integrity']['cache_sha256'],{k:r['cache_sha256'] for k,r in caches.items()})
    same(p['development'],frozen['development']); same(p['ensemble_development'],frozen['ensemble_development'])
    text=render(p)
    disclosure=('> Execution disclosure: the original attempt failed during historical validation. '
        'These tables were recovered from its unchanged, globally frozen predictions, with zero additional model calls or fits. '
        'See [recovery method](E020_RECOVERY.md) and [verified recovery receipt](../results/E020_recovery.json).\n\n')
    first,rest=text.split('\n',1); text=first+'\n\n'+disclosure+rest
    for destination in ('results/E020_aggregates.json','results/E020_recovery.json','docs/E020_RESULTS.md'):
        if (ROOT/destination).exists(): raise ValueError('Publication already exists.')
    write_new(ROOT/'results/E020_aggregates.json',p)
    write_new(ROOT/'results/E020_recovery.json',receipt)
    with (ROOT/'docs/E020_RESULTS.md').open('x',encoding='utf-8',newline='\n') as stream: stream.write(text)
    if sha(ROOT/'results/E020_aggregates.json')!=sha(path): raise ValueError('Public aggregate byte mismatch.')
    if sha(ROOT/'results/E020_recovery.json')!=sha(out/'execution.json'): raise ValueError('Recovery receipt byte mismatch.')
    verify(ROOT); no_failures(out)
    print('All registered E020 tables published with verified recovery provenance; interpretation withheld.')


if __name__=='__main__': main()
