"""Read-only viewer; exits on terminal or stale state, never controls research."""
from pathlib import Path
import sys
import time
from map_misconceptions.e010_monitor import read_status
from map_misconceptions.live_status import render_status, monitor_state

def main():
    path = Path('artifacts/e016_attempt01/live_status.json')
    unavailable_since = None
    while True:
        try:
            status = read_status(path)
            unavailable_since = None
        except (OSError, ValueError):
            unavailable_since = unavailable_since or time.monotonic()
            if time.monotonic() - unavailable_since >= 60:
                print('E016 monitor unavailable; activity NOT confirmed. Computation unaffected.',flush=True)
                return 1
            time.sleep(2)
            continue
        if sys.stdout.isatty(): print('\033[2J\033[H',end='')
        print('Attempt: e016_attempt01\n'+render_status(status),flush=True)
        if monitor_state(status)!='RUNNING': return int(status.get('status')=='FAILED')
        time.sleep(2 if sys.stdout.isatty() else 60)

if __name__=='__main__':
    try: raise SystemExit(main())
    except KeyboardInterrupt: print('Viewer closed; computation unaffected.')
