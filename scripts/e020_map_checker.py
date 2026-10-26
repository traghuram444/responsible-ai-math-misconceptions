"""One checkpoint's 60 fixed MAP assessments; raw data and labels never mounted."""
import argparse
import json
import os
from pathlib import Path
import resource
import time
from map_misconceptions import e020_checker as c
from map_misconceptions.e019_checker import load_catalogue
from map_misconceptions.e019_integrity import model_files
from map_misconceptions.e020_map_integrity import verify_map
from map_misconceptions.resilient_status import ResilientStatus


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--model',choices=['G15','G7'],required=True); key=parser.parse_args().model
    root=Path('/workspace'); out=Path('/attempt')
    try:
        lock=verify_map(root)
        if (os.getuid(),os.getgid())!=(10001,10001): raise ValueError('Non-root identity required.')
        catalogue=Path('/inputs/catalogue.json')
        if c.sha(catalogue)!=lock['catalogue_sha256']: raise ValueError('Catalogue changed.')
        pairs=load_catalogue(catalogue)
        if len(pairs)!=60: raise ValueError('Pair count changed.')
        c.write_new(out/'started.json',{'model':key,'pairs':60,'lock_sha256':c.sha(root/'experiments/e020_map_lock.json')})
        started=time.monotonic()
        with ResilientStatus(out/'status.json',experiment_id='E020',total=60) as live:
            live.update(key+' MAP: verifying model and loading; no evaluation metrics')
            manifest=json.loads((root/('experiments/e019_model_manifest.json' if key=='G15' else 'experiments/e020_model7_manifest.json')).read_text())
            model_files('/model',manifest)
            tokenizer,config,metadata=c.inspect_configuration('/model')
            if metadata!=json.loads((root/'experiments/e020_environment_lock.json').read_text())['models'][key]: raise ValueError('Configuration changed.')
            c.configure(); model=c.load_model('/model'); rows=[]
            for i,(q,a) in enumerate(pairs):
                live.update(f'{key} MAP pair {i+1}/60; no scores before global freeze',completed=i)
                r=c.check_pair(q,a,model,tokenizer,config)
                c.write_new(out/f'pair_{i:04d}_private.json',r); rows.append(r)
                live.update(f'{key} MAP pairs completed {i+1}/60',completed=i+1)
            c.write_new(out/'cache_private.json',rows)
            peak=Path('/sys/fs/cgroup/memory.peak')
            c.write_new(out/'completion_private.json',{'status':'COMPLETED','model':key,'pairs':60,
                'cache_sha256':c.sha(out/'cache_private.json'),'catalogue_sha256':c.sha(catalogue),
                'lock_sha256':c.sha(root/'experiments/e020_map_lock.json'),'wall_seconds':time.monotonic()-started,
                'peak_rss_bytes':int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024),
                'container_peak_bytes':int(peak.read_text()) if peak.exists() else None})
            print(key+' complete input-only cache frozen; no correctness or prediction results scored.',flush=True)
    except BaseException as exc:
        c.write_new(out/'checker_failure.json',{'status':'FAILED','model':key,'exception_type':type(exc).__name__,'automatic_retry':False}); raise


if __name__=='__main__': main()
