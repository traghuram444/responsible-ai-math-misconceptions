"""Capture historical state and lock tested E023 code without MAP computation."""
import hashlib
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e019_integrity import canonical
from map_misconceptions.e022_integrity import preserve
from map_misconceptions.e023_integrity import IMAGE,PROTOCOL


def main():
    preserve(ROOT)
    if canonical(ROOT/'docs/E023_PROTOCOL.md')!=PROTOCOL: raise ValueError('Approved protocol changed.')
    if (ROOT/'artifacts/e023_attempt01').exists(): raise ValueError('E023 attempt exists.')
    folder=ROOT/'artifacts/e023_setup'; folder.mkdir(exist_ok=False)
    historical=subprocess.check_output(['git','ls-tree','-r','--name-only','0dc68cde56c725a1c56dbe06ffe8363483450e93'],cwd=ROOT,text=True).splitlines()
    historical+=sorted(p.relative_to(ROOT).as_posix() for d in (ROOT/'artifacts').glob('e022*') for p in d.rglob('*') if p.is_file())
    records={}
    for name in sorted(set(historical)):
        path=ROOT/name; prefix=name=='docs/EXPERIMENT_LOG.md'; raw=path.read_bytes() if prefix else None
        records[name]={'prefix':prefix,'bytes':len(raw) if prefix else path.stat().st_size,
            'sha256':hashlib.sha256(raw).hexdigest() if prefix else sha(path)}
    private=folder/'preservation_private.json'; write_new(private,records)
    names=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
    files=sorted(set(n for n in names if 'e023' in n.lower() and n not in ('experiments/e023_lock.json','docs/E023_EXECUTION.md')))
    prefixes={}
    for name in ('docs/E023_EXECUTION.md','docs/EXPERIMENT_LOG.md'):
        raw=(ROOT/name).read_bytes(); prefixes[name]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    write_new(ROOT/'experiments/e023_lock.json',{'experiment_id':'E023','protocol_sha256':PROTOCOL,'image_id':IMAGE,
        'reference_commit':'f2b130ddb4befe65d2d13a007ae956b205359177','protocol_commit':'0dc68cde56c725a1c56dbe06ffe8363483450e93',
        'preserved_files':len(records),'preservation_inventory_sha256':sha(private),
        'files':{n:canonical(ROOT/n) for n in files},'append_only_prefixes':prefixes})
    print(f'E023 additive lock created: {len(records)} historical files/prefixes; no MAP computation.')


if __name__=='__main__': main()
