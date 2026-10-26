"""Snapshot historical evidence or lock readiness files; never performs inference."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e019_integrity import canonical,preserve,verify_files


def snapshot():
    preserve(ROOT); verify_files(ROOT,json.loads((ROOT/'experiments/e019_lock.json').read_text()))
    names=set(subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines())
    for directory in ('artifacts','data'):
        for p in (ROOT/directory).rglob('*'):
            if p.is_file() and '__pycache__' not in p.parts and not any(x.startswith('e020') for x in p.parts):
                names.add(p.relative_to(ROOT).as_posix())
    records={}
    for name in sorted(names):
        p=ROOT/name
        if p.is_symlink(): raise ValueError('Historical symlink not allowed.')
        records[name]={'bytes':p.stat().st_size,'sha256':sha(p),'prefix':name=='docs/EXPERIMENT_LOG.md'}
    private=ROOT/'artifacts/e020_setup/preservation_private.json'
    write_new(private,{'baseline_commit':'382e2de2011e2428f365e150ea29b718e82352c6','files':records})
    write_new(ROOT/'experiments/e020_preservation_start.json',{'baseline_commit':'382e2de2011e2428f365e150ea29b718e82352c6',
        'preserved_files':len(records),'private_inventory_sha256':sha(private)})
    print('Captured historical files:',len(records),flush=True)


def freeze():
    from map_misconceptions.e020_integrity import preserve_e020
    n=preserve_e020(ROOT)
    paths=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
    files=sorted(set(p for p in paths if 'e020' in p.lower() and p not in ('experiments/e020_readiness_lock.json','docs/E020_EXECUTION.md')))
    prefix=(ROOT/'docs/E020_EXECUTION.md').read_bytes()
    write_new(ROOT/'experiments/e020_readiness_lock.json',{'experiment_id':'E020','phase':'synthetic_readiness_only',
        'files':{p:canonical(ROOT/p) for p in files},'preserved_files':n,
        'execution_prefix':{'bytes':len(prefix),'sha256':hashlib.sha256(prefix).hexdigest()},
        'solver_image_id':'sha256:08b0187445e3a72b9b1215968c69e536872705660a1b2fd4a6bd8694af40ddc6'})
    print('Frozen readiness files:',len(files),flush=True)


def metadata():
    setup=ROOT/'artifacts/e020_setup'
    if (setup/'download_failure.json').exists(): raise ValueError('Download failed; stop.')
    model=json.loads((setup/'model7_manifest.json').read_text())
    if model['repository']!='Qwen/Qwen2.5-Math-7B-Instruct' or model['revision']!='ef9926d75ab1d54532f6a30dd5e760355eb9aa4d':
        raise ValueError('Model source changed.')
    # Configuration and model metadata only, never private predictions or text.
    write_new(ROOT/'experiments/e020_model7_manifest.json',model)
    write_new(ROOT/'experiments/e020_environment_lock.json',{'experiment_id':'E020',
        'solver_image_id':'sha256:08b0187445e3a72b9b1215968c69e536872705660a1b2fd4a6bd8694af40ddc6',
        'statistical_image_id':'sha256:464fc81faf49a6355e4bd0f55956243cc0fee586f657937f495975c2268e6fe0',
        'memory_limit_bytes':24*1024**3,'models':{key:json.loads((setup/(key+'_config.json')).read_text()) for key in ('G15','G7')}})
    print('Public model/configuration manifests generated; no inference.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('mode',choices=['snapshot','freeze','metadata'])
    args=parser.parse_args()
    {'snapshot':snapshot,'freeze':freeze,'metadata':metadata}[args.mode]()
