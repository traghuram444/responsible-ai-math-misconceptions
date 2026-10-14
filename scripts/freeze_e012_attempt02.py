"""Freeze one approved infrastructure-only amendment, never replacing old locks."""
import hashlib
import io
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = 'da1364bc3bf7680ab94f591e3e9fa7802eabefa0'
FILES = ['src/map_misconceptions/resilient_status.py', 'src/map_misconceptions/e012_retry.py',
         'scripts/run_e012_attempt02.py', 'scripts/run_e012_attempt02_docker.ps1',
         'scripts/monitor_e012_attempt02.py', 'scripts/freeze_e012_attempt02.py',
         'tests/test_e012_retry.py', 'docs/E012_ATTEMPT02_AMENDMENT.md']

def digest(raw): return hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()

if __name__ == '__main__':
    destination = ROOT / 'experiments/e012_attempt02_lock.json'
    if destination.exists(): raise ValueError('Existing amendment lock; refuse overwrite.')
    entries = []
    for item in subprocess.check_output(['git','ls-tree','-r','-z',BASE],cwd=ROOT).split(b'\0'):
        if item:
            meta, name = item.split(b'\t',1)
            if name.decode() not in ('README.md','docs/EXPERIMENT_LOG.md'):
                entries.append((name.decode(), meta.decode().split()[2]))
    blobs = io.BytesIO(subprocess.check_output(['git','cat-file','--batch'],cwd=ROOT,
                       input=('\n'.join(sha for _,sha in entries)+'\n').encode()))
    preserved = {}
    for name, sha in entries:
        header = blobs.readline().decode().strip().split()
        if header[:2] != [sha,'blob']: raise ValueError('Unexpected Git object.')
        preserved[name] = digest(blobs.read(int(header[2])))
        if blobs.read(1) != b'\n': raise ValueError('Invalid batch framing.')
    previous = json.loads((ROOT/'experiments/e011_e012_lock.json').read_text(encoding='utf-8'))
    lock = {'attempt_id':'e012_attempt02','authorization':'user_approved_infrastructure_fix_and_one_new_attempt',
            'scientific_settings_changed':False,'baseline_commit':BASE,'docker_image_id':previous['docker_image_id'],
            'hash_convention':'sha256; CRLF normalized to LF only',
            'files':{name:digest((ROOT/name).read_bytes()) for name in FILES}, 'preserved':preserved}
    with destination.open('x',encoding='utf-8',newline='\n') as stream:
        stream.write(json.dumps(lock,indent=2,sort_keys=True)+'\n')
    print(f'Locked {len(FILES)} amendment files; preserved {len(preserved)} historical files.')
