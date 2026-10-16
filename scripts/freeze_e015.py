"""Create the approved E015 execution lock without modifying historical locks."""
import hashlib
import io
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
BASE='16f55596de8b871d89820e31e75ddf28e4c2f150'
FILES=['docs/E015_PROTOCOL.md','experiments/e015_approval.json','src/map_misconceptions/e015.py',
       'src/map_misconceptions/e015_publication.py','scripts/run_e015.py','scripts/publish_e015.py',
       'scripts/monitor_e015.py','scripts/run_e015_docker.ps1','scripts/freeze_e015.py','tests/test_e015.py']
def digest(raw): return hashlib.sha256(raw.replace(b'\r\n',b'\n')).hexdigest()

if __name__=='__main__':
    destination=ROOT/'experiments/e015_lock.json'
    if destination.exists(): raise ValueError('Lock exists; never overwrite.')
    approval=json.loads((ROOT/'experiments/e015_approval.json').read_text())
    if digest((ROOT/'docs/E015_PROTOCOL.md').read_bytes())!=approval['protocol_sha256_lf']: raise ValueError('Approved protocol changed.')
    entries=[]
    for item in subprocess.check_output(['git','ls-tree','-r','-z',BASE],cwd=ROOT).split(b'\0'):
        if item:
            meta,name=item.split(b'\t',1)
            if name.decode() not in ('README.md','docs/EXPERIMENT_LOG.md'):
                entries.append((name.decode(),meta.decode().split()[2]))
    blobs=io.BytesIO(subprocess.check_output(['git','cat-file','--batch'],cwd=ROOT,input=('\n'.join(sha for _,sha in entries)+'\n').encode()))
    preserved={}
    for name,sha in entries:
        header=blobs.readline().decode().strip().split()
        if header[:2]!=[sha,'blob']: raise ValueError('Unexpected Git object.')
        preserved[name]=digest(blobs.read(int(header[2])))
        if blobs.read(1)!=b'\n': raise ValueError('Invalid batch framing.')
        if digest((ROOT/name).read_bytes())!=preserved[name]: raise ValueError('Historical file changed.')
    evidence={}
    for folder in ('e011','e012','e012_attempt02','e013_attempt01','e014_attempt01'):
        for path in sorted((ROOT/'artifacts'/folder).rglob('*')):
            if path.is_file(): evidence[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
    lock={'experiment_id':'E015','attempt_id':'e015_attempt01','baseline_commit':BASE,
        'docker_image_id':json.loads((ROOT/'experiments/e011_e012_lock.json').read_text())['docker_image_id'],
        'hash_convention':'sha256; CRLF normalized to LF only except private evidence bytes',
        'files':{name:digest((ROOT/name).read_bytes()) for name in FILES},'preserved':preserved,'private_evidence':evidence}
    with destination.open('x',encoding='utf-8',newline='\n') as stream: stream.write(json.dumps(lock,indent=2,sort_keys=True)+'\n')
    print(f'Locked {len(FILES)} E015 files; preserved {len(preserved)} public and {len(evidence)} private evidence files.')
