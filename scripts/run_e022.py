"""One-shot pinned Docker execution and independent read-only E022 monitor."""
from datetime import datetime,timezone
import json
import re
from pathlib import Path
import subprocess
import sys
import time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e022_integrity import preserve,no_failures,OUT,IMAGE
from map_misconceptions.live_status import render_status


def output(*args): return subprocess.check_output(args,cwd=ROOT,text=True).strip()


def view(state):
    state=json.loads(json.dumps(state))
    match=re.match(r'(?:Training: classifier fits|Development: policies|Scoring: evaluation folds) (\d+)/(\d+)',state['stage'])
    if state['status']=='RUNNING' and match:
        n,total=map(int,match.groups())
        state['progress']={'completed':n,'total':total,'percent':round(100*n/total,1)}
    return state


def monitor():
    while True:
        path=ROOT/OUT/'status.json'
        if path.exists():
            try:
                state=json.loads(path.read_text()); print(render_status(view(state)),flush=True)
                if state['status'] in ('COMPLETED','FAILED'): return
            except (OSError,ValueError,KeyError): pass
        if list((ROOT/OUT).glob('*failure.json')): return
        if not output('docker','ps','--filter','name=responsible-ai-math-e022','--format','{{.Names}}'): return
        time.sleep(10)


def main():
    if output('git','status','--porcelain=v1','--untracked-files=all'): raise ValueError('Clean committed implementation required.')
    preserve(ROOT)
    if output('docker','ps','--filter','name=responsible-ai-math-e022','--format','{{.Names}}'): raise ValueError('E022 already active.')
    if output('docker','image','inspect',IMAGE,'--format','{{.Id}}')!=IMAGE: raise ValueError('Pinned image differs.')
    out=ROOT/OUT; out.mkdir(exist_ok=False); revision=output('git','rev-parse','HEAD')
    write_new(out/'started.json',{'experiment_id':'E022','git_revision':revision,'lock_sha256':sha(ROOT/'experiments/e022_lock.json'),
        'started_utc':datetime.now(timezone.utc).isoformat()})
    args=['docker','run','--rm','--pull','never','--name','responsible-ai-math-e022','--network','none','--read-only',
        '--user','10001:10001','--cap-drop','ALL','--security-opt','no-new-privileges','--tmpfs','/tmp:rw,nosuid,nodev',
        '-e','PYTHONHASHSEED=20260831','--mount',f'type=bind,source={ROOT},target=/workspace,readonly',
        '--mount',f'type=bind,source={out},target=/workspace/{OUT}','--workdir','/workspace',IMAGE,
        'python','-m','map_misconceptions.e022_run','--git-revision',revision,'--image-id',IMAGE]
    try:
        with (out/'statistics_private.log').open('xb') as stream:
            subprocess.run(args,cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT,check=True)
        no_failures(out); preserve(ROOT)
        if json.loads((out/'execution.json').read_text())['status']!='COMPLETED': raise ValueError('No completion receipt.')
        print('E022 completed; all registered panels serialized, interpretation withheld.')
    except BaseException as exc:
        write_new(out/'launcher_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False}); raise


if __name__=='__main__':
    if '--monitor' in sys.argv: monitor()
    else: main()
