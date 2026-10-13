"""Terminal-only active-run viewer; no data access, edits or recurring automation."""
import argparse
from pathlib import Path
import sys
import time

from map_misconceptions.e010_monitor import read_status
from map_misconceptions.live_status import monitor_state, render_status

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiment', choices=('E011', 'E012'), required=True)
    parser.add_argument('--once', action='store_true')
    args = parser.parse_args()
    path = Path('artifacts') / args.experiment.lower() / 'live_status.json'
    try:
        while True:
            try:
                status = read_status(path)
            except (OSError, ValueError):
                print('Status unavailable; viewer stopped. Experiment unaffected.', flush=True)
                return 1
            if sys.stdout.isatty() and not args.once: print('\033[2J\033[H', end='')
            print(render_status(status), flush=True)
            state = monitor_state(status)
            if args.once or state != 'RUNNING': return int(state == 'FAILED')
            time.sleep(2 if sys.stdout.isatty() else 60)
    except KeyboardInterrupt:
        print('Viewer closed; experiment unaffected.')
        return 0

if __name__ == '__main__': raise SystemExit(main())
