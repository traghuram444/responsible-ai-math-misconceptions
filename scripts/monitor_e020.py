"""Independent read-only E020 readiness monitor; never starts or resumes work."""
from datetime import datetime,timezone
import json
from pathlib import Path
import sys
import time
from map_misconceptions.live_status import render_status,monitor_state

OUT=Path(__file__).resolve().parents[1]/'artifacts/e020_attempt01'


def snapshot(out=OUT):
    if not (out/'attempt.json').exists(): return None
    attempt=json.loads((out/'attempt.json').read_text())
    receipts=sorted(out.glob('*failure.json'))
    terminal=receipts[0] if receipts else out/'readiness.json'
    if terminal.exists():
        r=json.loads(terminal.read_text()); complete=r['status'] in ('READY_FOR_MAP_IMPLEMENTATION_CHECK','RUNTIME_REVIEW_REQUIRED')
        done=0
        for key in ('G15','G7'):
            statuspath=out/(key+'_status.json')
            if statuspath.exists(): done+=json.loads(statuspath.read_text())['progress']['completed']
        return {'schema_version':1,'experiment_id':'E020','status':'COMPLETED' if complete else 'FAILED',
            'started_at':attempt['started_utc'],'updated_at':datetime.now(timezone.utc).isoformat(),
            'elapsed_seconds':(datetime.now(timezone.utc)-datetime.fromisoformat(attempt['started_utc'])).total_seconds(),
            'stage':r['status']+'; MAP not started','progress':{'completed':done,'total':24,'percent':100*done/24},'latest_metrics':{}}
    for key,offset in (('G7',12),('G15',0)):
        p=out/(key+'_status.json')
        if p.exists():
            state=json.loads(p.read_text()); done=offset+state['progress']['completed']
            state['progress']={'completed':done,'total':24,'percent':100*done/24}
            state['started_at']=attempt['started_utc']
            state['elapsed_seconds']=(datetime.now(timezone.utc)-datetime.fromisoformat(attempt['started_utc'])).total_seconds()
            if state['status']=='COMPLETED': state.update(status='RUNNING',stage=key+' synthetic stage complete; gate bookkeeping')
            return state
    return None


def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8',errors='replace')
    if not (OUT/'attempt.json').exists(): print('No E020 attempt active.'); return
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
        if time.monotonic()-unavailable>60: print('Status unavailable; activity not confirmed.'); return
        time.sleep(2 if sys.stdout.isatty() else 60)


if __name__=='__main__': main()
