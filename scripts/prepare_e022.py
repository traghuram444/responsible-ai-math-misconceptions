"""Capture historical state and lock tested E022 code without MAP computation."""
import hashlib
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e019_integrity import canonical
from map_misconceptions.e021_integrity import preserve
from map_misconceptions.e022_integrity import IMAGE,PROTOCOL


def main():
    preserve(ROOT)
    if canonical(ROOT/'docs/E022_PROTOCOL.md')!=PROTOCOL: raise ValueError('Approved protocol changed.')
    if (ROOT/'artifacts/e022_attempt01').exists(): raise ValueError('E022 attempt exists.')
    folder=ROOT/'artifacts/e022_setup'; folder.mkdir(exist_ok=False)
    historical=subprocess.check_output(['git','ls-tree','-r','--name-only','e5e6708b9c745496e51bc909342e8c5880c22f49'],cwd=ROOT,text=True).splitlines()
    historical+=sorted(p.relative_to(ROOT).as_posix() for d in (ROOT/'artifacts').glob('e021*') for p in d.rglob('*') if p.is_file())
    records={}
    for name in sorted(set(historical)):
        path=ROOT/name; prefix=name=='docs/EXPERIMENT_LOG.md'; raw=path.read_bytes() if prefix else None
        records[name]={'prefix':prefix,'bytes':len(raw) if prefix else path.stat().st_size,
            'sha256':hashlib.sha256(raw).hexdigest() if prefix else sha(path)}
    private=folder/'preservation_private.json'; write_new(private,records)
    names=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
    files=sorted(set(n for n in names if 'e022' in n.lower() and n not in ('experiments/e022_lock.json','docs/E022_EXECUTION.md')))
    prefixes={}
    for name in ('docs/E022_EXECUTION.md','docs/EXPERIMENT_LOG.md'):
        raw=(ROOT/name).read_bytes(); prefixes[name]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    write_new(ROOT/'experiments/e022_lock.json',{'experiment_id':'E022','protocol_sha256':PROTOCOL,'image_id':IMAGE,
        'reference_commit':'cfbec27c49114f15edddc92df4c2b3c6e578d3e0','protocol_commit':'e5e6708b9c745496e51bc909342e8c5880c22f49',
        'preserved_files':len(records),'preservation_inventory_sha256':sha(private),
        'files':{n:canonical(ROOT/n) for n in files},'append_only_prefixes':prefixes})
    print(f'E022 additive lock created: {len(records)} historical files/prefixes; no MAP computation.')


if __name__=='__main__': main()
