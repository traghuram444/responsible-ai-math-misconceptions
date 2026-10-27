"""One-shot reporting-only Docker recovery, with an independent read-only viewer."""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
import time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e020_recovery_integrity import verify,OUT,LOCK
from map_misconceptions.live_status import render_status


def output(*args): return subprocess.check_output(args,cwd=ROOT,text=True).strip()


def monitor():
    path=ROOT/OUT/'status.json'
    while True:
        if path.exists():
            try:
                state=json.loads(path.read_text()); print(render_status(state),flush=True)
                if state['status'] in ('COMPLETED','FAILED'): return
            except (OSError,ValueError,KeyError): pass
        if list((ROOT/OUT).glob('*failure.json')): return
        if not output('docker','ps','--filter','name=responsible-ai-math-e020-recovery','--format','{{.Names}}'): return
        time.sleep(10)


def main():
    if output('git','status','--porcelain=v1','--untracked-files=all'): raise ValueError('Clean committed recovery required.')
    lock,_,_=verify(ROOT)
    if output('docker','ps','--filter','name=responsible-ai-math-e020','--format','{{.Names}}'): raise ValueError('E020 already active.')
    image=lock['statistical_image_id']
    if output('docker','image','inspect',image,'--format','{{.Id}}')!=image: raise ValueError('Image changed.')
    out=ROOT/OUT; out.mkdir(exist_ok=False)
    revision=output('git','rev-parse','HEAD')
    write_new(out/'started.json',{'git_revision':revision,'lock_sha256':sha(ROOT/LOCK),'started_utc':datetime.now(timezone.utc).isoformat()})
    args=['docker','run','--rm','--pull','never','--name','responsible-ai-math-e020-recovery',
        '--network','none','--read-only','--user','10001:10001','--cap-drop','ALL','--security-opt','no-new-privileges',
        '--tmpfs','/tmp:rw,nosuid,nodev','-e','PYTHONHASHSEED=20260831',
        '--mount',f'type=bind,source={ROOT},target=/workspace,readonly',
        '--mount',f'type=bind,source={out},target=/workspace/{OUT}',
        '--workdir','/workspace',image,'python','-m','map_misconceptions.e020_recovery',
        '--git-revision',revision,'--image-id',image]
    try:
        with (out/'recovery_private.log').open('xb') as stream:
            subprocess.run(args,cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT,check=True)
        verify(ROOT)
        if json.loads((out/'execution.json').read_text())['status']!='COMPLETED': raise ValueError('No completion receipt.')
        print('E020 reporting recovery complete. No additional model calls or fits.')
    except BaseException as exc:
        write_new(out/'launcher_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False}); raise


if __name__=='__main__':
    if '--monitor' in sys.argv: monitor()
    else: main()
