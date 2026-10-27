"""Capture historical state and freeze tested E021 code, without any MAP analysis."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e019_integrity import canonical
from map_misconceptions.e020_recovery_integrity import verify
from map_misconceptions.e021_integrity import IMAGE,PROTOCOL


def main():
    verify(ROOT)
    if canonical(ROOT/'docs/E021_PROTOCOL.md')!=PROTOCOL: raise ValueError('Approved protocol changed.')
    if (ROOT/'artifacts/e021_attempt01').exists(): raise ValueError('E021 attempt already exists.')
    folder=ROOT/'artifacts/e021_setup'; folder.mkdir(exist_ok=False)
    historical=subprocess.check_output(['git','ls-tree','-r','--name-only','587bc272b4a7abdb03ffc9bc9306b18f076a3b34'],cwd=ROOT,text=True).splitlines()
    # Full E020 artifact set includes the original failed attempt, model manifests,
    # weights, completed recovery, preparation evidence, and private receipts.
    historical+=sorted(p.relative_to(ROOT).as_posix() for d in (ROOT/'artifacts').glob('e020*') for p in d.rglob('*') if p.is_file())
    records={}
    for name in sorted(set(historical)):
        path=ROOT/name; prefix=name=='docs/EXPERIMENT_LOG.md'
        raw=path.read_bytes() if prefix else None
        records[name]={'prefix':prefix,'bytes':len(raw) if prefix else path.stat().st_size,'sha256':hashlib.sha256(raw).hexdigest() if prefix else sha(path)}
    private=folder/'preservation_private.json'; write_new(private,records)
    names=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
    files=sorted(set(p for p in names if 'e021' in p.lower() and p!='experiments/e021_lock.json' and p!='docs/E021_EXECUTION.md'))
    prefixes={}
    for name in ('docs/E021_EXECUTION.md','docs/EXPERIMENT_LOG.md'):
        raw=(ROOT/name).read_bytes(); prefixes[name]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    write_new(ROOT/'experiments/e021_lock.json',{'experiment_id':'E021','protocol_sha256':PROTOCOL,'image_id':IMAGE,
        'reference_commit':'bb7a4ec12eda409b248c187dbc1f3bad27f18a1b','protocol_commit':'587bc272b4a7abdb03ffc9bc9306b18f076a3b34',
        'preserved_files':len(records),'preservation_inventory_sha256':sha(private),
        'files':{p:canonical(ROOT/p) for p in files},'append_only_prefixes':prefixes})
    print(f'E021 code lock created; {len(records)} additional historical files/prefixes captured; no experiment computation.')


if __name__=='__main__': main()
