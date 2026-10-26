"""Single approved MAP phase, sequential checkpoints then frozen statistics."""
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
from map_misconceptions.e020_integrity import preserve_e020
from map_misconceptions.e020_map_integrity import verify_map,no_failures,verify_readiness_evidence
from map_misconceptions.live_status import render_status
from monitor_e020_map import snapshot


def output(*args): return subprocess.check_output(args,cwd=ROOT,text=True).strip()


def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8',errors='replace')
    if output('git','status','--porcelain=v1','--untracked-files=all'): raise ValueError('Clean committed MAP implementation required.')
    lock=verify_map(ROOT); no_failures(ROOT/'artifacts/e020_attempt01'); preserve_e020(ROOT); verify_readiness_evidence(ROOT,lock)
    if output('docker','ps','--filter','name=responsible-ai-math-e020','--format','{{.Names}}'): raise ValueError('E020 already active.')
    for key in ('solver_image_id','statistical_image_id'):
        if output('docker','image','inspect',lock[key],'--format','{{.Id}}')!=lock[key]: raise ValueError('Image identity changed.')
    if int(output('docker','info','--format','{{.MemTotal}}'))<24*1024**3 or shutil.disk_usage(ROOT).free<40*1024**3:
        raise ValueError('Resource gate failed.')
    out=ROOT/'artifacts/e020_attempt01/map'; out.mkdir(exist_ok=False)
    revision=output('git','rev-parse','HEAD')
    write_new(out/'started.json',{'experiment_id':'E020','phase':'MAP','git_revision':revision,
        'lock_sha256':sha(ROOT/'experiments/e020_map_lock.json'),'started_utc':datetime.now(timezone.utc).isoformat()})
    stop=threading.Event()
    def display():
        while not stop.wait(60):
            try:
                state=snapshot(out)
                if state: print(render_status(state),flush=True)
            except (OSError,ValueError,KeyError): pass
    thread=threading.Thread(target=display,daemon=True); thread.start()
    common=['docker','run','--rm','--pull','never','--network','none','--read-only','--user','10001:10001',
        '--cap-drop','ALL','--security-opt','no-new-privileges','--tmpfs','/tmp:rw,nosuid,nodev']
    def mount(source,target,readonly=True): return ['--mount',f'type=bind,source={source},target={target}'+(',readonly' if readonly else '')]
    try:
        for key,model in (('G15',ROOT/'artifacts/e019_setup/model'),('G7',ROOT/'artifacts/e020_setup/model7')):
            folder=out/key; folder.mkdir(exist_ok=False)
            args=common+['--name','responsible-ai-math-e020-map-'+key.lower(),'--memory','24g','--memory-swap','24g','-e','PYTHONHASHSEED=20261026']
            for name in ('src','scripts','experiments','docs','results','repro','tests'): args+=mount(ROOT/name,'/workspace/'+name)
            args+=mount(model,'/model')+mount(ROOT/'artifacts/e020_attempt01/map_inputs/catalogue.json','/inputs/catalogue.json')+mount(folder,'/attempt',False)
            args+=[lock['solver_image_id'],'python','scripts/e020_map_checker.py','--model',key]
            with (folder/'checker_private.log').open('xb') as stream:
                subprocess.run(args,cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT,check=True)
            no_failures(out.parent)
            if json.loads((folder/'completion_private.json').read_text())['status']!='COMPLETED': raise ValueError('Missing complete cache.')
        args=common+['--name','responsible-ai-math-e020-map-statistics','-e','PYTHONHASHSEED=20260831']
        args+=mount(ROOT,'/workspace')+mount(out,'/workspace/artifacts/e020_attempt01/map',False)
        args+=['--workdir','/workspace',lock['statistical_image_id'],'python','-m','map_misconceptions.e020_map_run',
            '--git-revision',revision,'--image-id',lock['statistical_image_id']]
        with (out/'statistics_private.log').open('xb') as stream:
            subprocess.run(args,cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT,check=True)
        no_failures(out.parent); verify_map(ROOT); preserve_e020(ROOT); verify_readiness_evidence(ROOT,lock)
        if json.loads((out/'execution.json').read_text())['status']!='COMPLETED': raise ValueError('No completion receipt.')
    except BaseException as exc:
        write_new(out/'orchestration_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False}); raise
    finally:
        stop.set(); thread.join(timeout=3)
        state=snapshot(out)
        if state: print(render_status(state),flush=True)


if __name__=='__main__': main()
