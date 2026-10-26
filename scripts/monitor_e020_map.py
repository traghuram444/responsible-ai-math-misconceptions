"""Independent read-only E020 MAP monitor; no model start/resume capability."""
from datetime import datetime,timezone
import json
from pathlib import Path
import sys
import time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.live_status import render_status,monitor_state
OUT=ROOT/'artifacts/e020_attempt01/map'


def snapshot(out=OUT):
    if not (out/'started.json').exists(): return None
    attempt=json.loads((out/'started.json').read_text()); failures=list(out.rglob('*failure.json'))
    if failures or (out/'execution.json').exists():
        terminal=json.loads((failures[0] if failures else out/'execution.json').read_text())
        done,total=(50,50) if not failures else (0,120)
        if failures:
            for path,offset,size in ((out/'statistics_status.json',0,50),(out/'G7/status.json',60,120),(out/'G15/status.json',0,120)):
                if path.exists():
                    done=offset+json.loads(path.read_text())['progress']['completed']; total=size; break
        return {'schema_version':1,'experiment_id':'E020','status':terminal['status'],
            'started_at':attempt['started_utc'],'updated_at':datetime.now(timezone.utc).isoformat(),
            'elapsed_seconds':(datetime.now(timezone.utc)-datetime.fromisoformat(attempt['started_utc'])).total_seconds(),
            'stage':'MAP completed; aggregate validation/publication pending' if not failures else 'Technical failure; no automatic retry',
            'progress':{'completed':done,'total':total,'percent':100*done/total},'latest_metrics':{}}
    for path,offset,total in ((out/'statistics_status.json',0,50),(out/'G7/status.json',60,120),(out/'G15/status.json',0,120)):
        if path.exists():
            state=json.loads(path.read_text()); n=state['progress']['completed']+offset
            state['progress']={'completed':n,'total':total,'percent':100*n/total}
            state['started_at']=attempt['started_utc']
            state['elapsed_seconds']=(datetime.now(timezone.utc)-datetime.fromisoformat(attempt['started_utc'])).total_seconds()
            if state['status']=='COMPLETED': state.update(status='RUNNING',stage='Completed stage; validating receipts and next-phase handoff')
            return state
    return None


def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8',errors='replace')
    if not (OUT/'started.json').exists(): print('No E020 MAP attempt active.'); return
    unavailable=time.monotonic()
    while True:
        try:
            state=snapshot()
            if state:
                unavailable=time.monotonic()
                if sys.stdout.isatty(): print('\033[2J\033[H',end='')
                print(render_status(state),flush=True)
                if monitor_state(state)!='RUNNING': return
        except (OSError,ValueError,KeyError): pass
        if time.monotonic()-unavailable>60: print('Status unavailable; active computation not confirmed.'); return
        time.sleep(2 if sys.stdout.isatty() else 60)


if __name__=='__main__': main()
