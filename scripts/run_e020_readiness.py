"""One-attempt hidden host launcher; synthetic gate only, never launches MAP."""
from datetime import datetime,timezone
import json
from pathlib import Path
import shutil
import subprocess
import sys
import threading

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e020_integrity import preserve_e020,verify_readiness
from map_misconceptions.live_status import render_status


def output(*args): return subprocess.check_output(args,cwd=ROOT,text=True).strip()


def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8',errors='replace')
    if output('git','status','--porcelain=v1','--untracked-files=all'): raise ValueError('Clean committed readiness plan required.')
    revision=output('git','rev-parse','HEAD'); lock=verify_readiness(ROOT)
    preserve_e020(ROOT)
    image=lock['solver_image_id']
    if output('docker','image','inspect',image,'--format','{{.Id}}')!=image: raise ValueError('Image mismatch.')
    if int(output('docker','info','--format','{{.MemTotal}}'))<24*1024**3: raise ValueError('Docker memory gate.')
    if shutil.disk_usage(ROOT).free<40*1024**3: raise ValueError('Disk gate.')
    out=ROOT/'artifacts/e020_attempt01'
    if out.exists(): raise ValueError('Attempt already exists; no retry.')
    out.mkdir()
    write_new(out/'attempt.json',{'experiment_id':'E020','phase':'synthetic_readiness','git_revision':revision,
        'lock_sha256':sha(ROOT/'experiments/e020_readiness_lock.json'),'started_utc':datetime.now(timezone.utc).isoformat()})
    stop=threading.Event()
    def display():
        while not stop.wait(60):
            try:
                for key in ('G7','G15'):
                    p=out/(key+'_status.json')
                    if p.exists(): print(render_status(json.loads(p.read_text())),flush=True); break
            except (OSError,ValueError,KeyError): pass
    thread=threading.Thread(target=display,daemon=True); thread.start()
    receipts=[]
    try:
        for key,model in (('G15',ROOT/'artifacts/e019_setup/model'),('G7',ROOT/'artifacts/e020_setup/model7')):
            args=['docker','run','--rm','--pull','never','--name','responsible-ai-math-e020-readiness-'+key.lower(),
                  '--network','none','--read-only','--user','10001:10001','--cap-drop','ALL',
                  '--security-opt','no-new-privileges','--tmpfs','/tmp:rw,nosuid,nodev',
                  '--memory','24g','--memory-swap','24g','-e','PYTHONHASHSEED=20261026']
            for directory in ('src','scripts','experiments','docs','tests','repro'):
                args+=['--mount',f'type=bind,source={ROOT/directory},target=/workspace/{directory},readonly']
            args+=['--mount',f'type=bind,source={model},target=/model,readonly',
                   '--mount',f'type=bind,source={out},target=/attempt',image,'python','scripts/e020_readiness.py','synthetic','--model',key]
            with (out/(key+'_private.log')).open('xb') as log:
                subprocess.run(args,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,check=True)
            r=json.loads((out/(key+'_receipt.json')).read_text()); receipts.append(r)
            if not r['gate_passed']:
                write_new(out/'readiness.json',{'status':'GATE_FAILED','failed_model':key,'model_receipts':receipts,
                    'map_started':False,'automatic_retry':False}); return
        projection=sum(r['projected_map_seconds'] for r in receipts)
        status='RUNTIME_REVIEW_REQUIRED' if projection>48*3600 else 'READY_FOR_MAP_IMPLEMENTATION_CHECK'
        verify_readiness(ROOT); preserve_e020(ROOT)
        write_new(out/'readiness.json',{'status':status,'model_receipts':receipts,'projected_map_seconds':projection,
            'map_started':False,'automatic_retry':False})
        print('Readiness complete; no MAP launch from this staged launcher.',flush=True)
    except BaseException as exc:
        write_new(out/'orchestration_failure.json',{'status':'FAILED','phase':'synthetic_readiness',
            'exception_type':type(exc).__name__,'automatic_retry':False,'map_started':False})
        raise
    finally:
        stop.set(); thread.join(timeout=3)


if __name__=='__main__': main()
