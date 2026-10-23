"""One-attempt sequential Docker orchestration; never changes host settings."""
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import threading
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import write_new,sha
from map_misconceptions.e019_integrity import preserve,verify_files
from map_misconceptions.live_status import render_status
from monitor_e019 import snapshot


def output(*args): return subprocess.check_output(args,cwd=ROOT,text=True).strip()


def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8',errors='replace')
    lock=json.loads((ROOT/'experiments/e019_lock.json').read_text())
    if output('git','status','--porcelain=v1','--untracked-files=all'): raise ValueError('Clean committed plan required.')
    revision=output('git','rev-parse','HEAD')
    for name in ('solver_image_id','statistical_image_id'):
        if output('docker','image','inspect',lock[name],'--format','{{.Id}}')!=lock[name]: raise ValueError('Image identity changed.')
    if int(output('docker','info','--format','{{.MemTotal}}'))<17179869184: raise ValueError('Docker memory gate failed.')
    preserve(ROOT); verify_files(ROOT,lock)
    out=ROOT/'artifacts/e019_attempt01'
    if out.exists(): raise ValueError('Attempt exists; never overwrite or retry.')
    if any(p.is_symlink() for p in (ROOT,ROOT/'artifacts')): raise ValueError('Real project directories required.')
    out.mkdir()
    write_new(out/'attempt.json',{'experiment_id':'E019','git_revision':revision,
        'lock_sha256':sha(ROOT/'experiments/e019_lock.json'),'started_utc':datetime.now(timezone.utc).isoformat()})
    stop=threading.Event()
    def display():
        while not stop.wait(2 if sys.stdout.isatty() else 60):
            try:
                state=snapshot(out)
                if state:
                    if sys.stdout.isatty(): print('\033[2J\033[H',end='')
                    print(render_status(state),flush=True)
            except (OSError,ValueError,KeyError): pass
    thread=threading.Thread(target=display,daemon=True); thread.start()
    common=['docker','run','--rm','--pull','never','--network','none','--read-only','--user','10001:10001',
        '--cap-drop','ALL','--security-opt','no-new-privileges','--tmpfs','/tmp:rw,nosuid,nodev']
    def mount(source,target,readonly=True):
        return ['--mount',f'type=bind,source={source},target={target}'+(',readonly' if readonly else '')]
    try:
        solver=common+['--name','responsible-ai-math-e019-checker-attempt01','--memory','16g','--memory-swap','16g']
        for directory in ('src','scripts','experiments'):
            solver+=mount(ROOT/directory,'/workspace/'+directory)
        solver+=mount(ROOT/'artifacts/e019_setup/model','/model')
        solver+=mount(ROOT/'artifacts/e019_setup/catalogue.json','/inputs/catalogue.json')
        solver+=mount(out,'/attempt',False)
        solver+=[lock['solver_image_id'],'python','scripts/run_e019_checker.py']
        with (out/'solver_private.log').open('xb') as log:
            subprocess.run(solver,stdout=log,stderr=subprocess.STDOUT,check=True,cwd=ROOT)
        if json.loads((out/'checker_completion.json').read_text())['status']!='COMPLETED': raise ValueError('No frozen cache.')
        statistics=common+['--name','responsible-ai-math-e019-statistics-attempt01','-e','PYTHONHASHSEED=20260831']
        statistics+=mount(ROOT,'/workspace')+mount(out,'/workspace/artifacts/e019_attempt01',False)
        statistics+=['--workdir','/workspace',lock['statistical_image_id'],'python','scripts/run_e019_statistics.py',
            '--git-revision',revision,'--image-id',lock['statistical_image_id']]
        with (out/'statistics_private.log').open('xb') as log:
            subprocess.run(statistics,stdout=log,stderr=subprocess.STDOUT,check=True,cwd=ROOT)
        preserve(ROOT); verify_files(ROOT,lock)
        if json.loads((out/'execution.json').read_text())['status']!='COMPLETED': raise ValueError('No completion receipt.')
    except BaseException as exc:
        write_new(out/'orchestration_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,
            'automatic_retry':False,'finished_utc':datetime.now(timezone.utc).isoformat()})
        raise
    finally:
        stop.set(); thread.join(timeout=3)
        state=snapshot(out)
        if state: print(render_status(state),flush=True)


if __name__=='__main__': main()
