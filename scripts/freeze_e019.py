"""Lock tested E019 files and references before the single MAP attempt."""
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e019_integrity import canonical,preserve,PROTOCOL_SHA

if __name__=='__main__':
    preserved=preserve(ROOT)
    approval=json.loads((ROOT/'experiments/e019_approval.json').read_text())
    if approval['protocol_sha256_lf']!=PROTOCOL_SHA: raise ValueError('Approval identity mismatch.')
    paths=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
    files=[p for p in paths if ('e019' in p.lower()) and p not in ('experiments/e019_lock.json','docs/E019_EXECUTION.md')]
    if any((ROOT/p).is_dir() for p in files): raise ValueError('Unexpected directory.')
    catalogue=json.loads((ROOT/'artifacts/e019_setup/catalogue_receipt.json').read_text())
    synthetic=json.loads((ROOT/'artifacts/e019_setup/synthetic_receipt.json').read_text())
    env=json.loads((ROOT/'experiments/e019_environment_lock.json').read_text())
    execution_prefix=(ROOT/'docs/E019_EXECUTION.md').read_bytes()
    import hashlib
    lock={'experiment_id':'E019','attempt_id':'e019_attempt01','baseline_commit':'496c5332b8b2201ea89abeb3cd51ede7ecd0187f',
        'solver_image_id':env['solver_image_id'],'statistical_image_id':env['statistical_image_id'],
        'files':{p:canonical(ROOT/p) for p in files},'preserved_files':preserved,
        'catalogue_sha256':catalogue['catalogue_sha256'],'pairs':catalogue['pairs'],
        'synthetic_receipt':synthetic,'references':{p:sha(ROOT/p) for p in ('results/E011_aggregates.json','results/E016_aggregates.json','results/E017_aggregates.json')},
        'execution_log_prefix':{'bytes':len(execution_prefix),'sha256':hashlib.sha256(execution_prefix).hexdigest()},
        'all_scientific_settings_unchanged':True}
    write_new(ROOT/'experiments/e019_lock.json',lock)
    print(f'Locked {len(files)} new E019 files; preservation gate passed for {preserved} existing files.')
