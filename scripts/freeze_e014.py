"""Create the approved E014 execution lock without modifying historical locks."""
import hashlib
import io
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
BASE='c286731335eea8466c531b2f736a69920870573d'
FILES=['docs/E014_PROTOCOL.md','experiments/e014_approval.json','src/map_misconceptions/e014.py',
       'src/map_misconceptions/e014_publication.py','scripts/run_e014.py','scripts/publish_e014.py',
       'scripts/monitor_e014.py','scripts/run_e014_docker.ps1','scripts/freeze_e014.py','tests/test_e014.py']
def digest(raw): return hashlib.sha256(raw.replace(b'\r\n',b'\n')).hexdigest()

if __name__=='__main__':
    destination=ROOT/'experiments/e014_lock.json'
    if destination.exists(): raise ValueError('Lock exists; never overwrite.')
    approval=json.loads((ROOT/'experiments/e014_approval.json').read_text())
    if digest((ROOT/'docs/E014_PROTOCOL.md').read_bytes())!=approval['protocol_sha256_lf']: raise ValueError('Approved protocol changed.')
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
    for folder in ('e011','e012','e012_attempt02','e013_attempt01'):
        for path in sorted((ROOT/'artifacts'/folder).rglob('*')):
            if path.is_file(): evidence[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
    lock={'experiment_id':'E014','attempt_id':'e014_attempt01','baseline_commit':BASE,
        'docker_image_id':json.loads((ROOT/'experiments/e011_e012_lock.json').read_text())['docker_image_id'],
        'hash_convention':'sha256; CRLF normalized to LF only except private evidence bytes',
        'files':{name:digest((ROOT/name).read_bytes()) for name in FILES},'preserved':preserved,'private_evidence':evidence}
    with destination.open('x',encoding='utf-8',newline='\n') as stream: stream.write(json.dumps(lock,indent=2,sort_keys=True)+'\n')
    print(f'Locked {len(FILES)} E014 files; preserved {len(preserved)} public and {len(evidence)} private evidence files.')
