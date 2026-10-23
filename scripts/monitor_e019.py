"""Read-only terminal monitor; never changes or resumes an experiment."""
from datetime import datetime,timezone
import json
from pathlib import Path
import sys
import time
from map_misconceptions.live_status import render_status,monitor_state

OUT=Path(__file__).resolve().parents[1]/'artifacts/e019_attempt01'


def snapshot(out=OUT):
    if not (out/'attempt.json').exists(): return None
    attempt=json.loads((out/'attempt.json').read_text())
    for name in ('orchestration_failure.json','statistical_failure.json','checker_failure.json','execution.json'):
        if (out/name).exists():
            result=json.loads((out/name).read_text())
            return {'schema_version':1,'experiment_id':'E019','status':result['status'],
                'started_at':attempt['started_utc'],'updated_at':datetime.now(timezone.utc).isoformat(),
                'elapsed_seconds':(datetime.now(timezone.utc)-datetime.fromisoformat(attempt['started_utc'])).total_seconds(),
                'stage':'Complete; results await review' if result['status']=='COMPLETED' else 'Technical failure; no automatic retry',
                'progress':{'completed':1 if result['status']=='COMPLETED' else 0,'total':1,'percent':100 if result['status']=='COMPLETED' else 0},
                'latest_metrics':{}}
    for name in ('statistics_status.json','solver_status.json'):
        if (out/name).exists():
            status=json.loads((out/name).read_text())
            status['started_at']=attempt['started_utc']
            status['elapsed_seconds']=(datetime.now(timezone.utc)-datetime.fromisoformat(attempt['started_utc'])).total_seconds()
            if name=='solver_status.json' and status['status']=='COMPLETED':
                status['status']='RUNNING'; status['stage']='Checker complete; preparing statistical stage (no scores yet)'
            return status
    return None


def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8',errors='replace')
    if not (OUT/'attempt.json').exists():
        print('No E019 attempt is active. Monitor not started.'); return
    unavailable=time.monotonic()
    while True:
        try:
            status=snapshot()
            if status is not None:
                unavailable=time.monotonic()
                if sys.stdout.isatty(): print('\033[2J\033[H',end='')
                print('Attempt: e019_attempt01\n'+render_status(status),flush=True)
                if monitor_state(status)!='RUNNING': return
        except (OSError,ValueError,KeyError): pass
        if time.monotonic()-unavailable>60:
            print('Monitor unavailable; activity NOT confirmed. Computation unaffected.',flush=True); return
        time.sleep(2 if sys.stdout.isatty() else 60)


if __name__=='__main__': main()
