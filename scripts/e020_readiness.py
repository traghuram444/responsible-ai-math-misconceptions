"""Configuration-only inspection or exactly one model's fixed synthetic suite."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import resource
import time
from map_misconceptions import e020_checker as c
from map_misconceptions.e019_integrity import model_files
from map_misconceptions.e020_integrity import verify_readiness
from map_misconceptions.resilient_status import ResilientStatus


def main():
    p=argparse.ArgumentParser(); p.add_argument('mode',choices=['config','synthetic']); p.add_argument('--model',choices=['G15','G7'],required=True)
    args=p.parse_args(); root=Path('/workspace'); out=Path('/attempt'); key=args.model
    tokenizer,config,metadata=c.inspect_configuration('/model')
    if args.mode=='config':
        c.write_new(Path('/setup')/(key+'_config.json'),metadata)
        print('Resolved tokenizer and generation configuration; no model loaded.',flush=True); return
    if os.getuid()!=10001 or os.getgid()!=10001: raise ValueError('Non-root identity required.')
    lock=verify_readiness(root)
    expected=json.loads((root/'experiments/e020_environment_lock.json').read_text())
    if metadata!=expected['models'][key]: raise ValueError('Resolved settings changed.')
    manifest=json.loads((root/('experiments/e019_model_manifest.json' if key=='G15' else 'experiments/e020_model7_manifest.json')).read_text())
    c.write_new(out/(key+'_started.json'),{'phase':'synthetic_readiness','model':key,'fixtures':12,
        'lock_sha256':c.sha(root/'experiments/e020_readiness_lock.json')})
    started=time.monotonic()
    try:
        with ResilientStatus(out/(key+'_status.json'),experiment_id='E020',total=12) as live:
            live.update(key+' readiness: verifying weights and loading; no MAP data')
            model_files('/model',manifest); c.configure(); model=c.load_model('/model')
            outputs=[]
            for i,(question,answer,reference) in enumerate(c.FIXTURES):
                live.update(f'{key} synthetic readiness fixture {i+1}/12; no MAP metrics',completed=i)
                result=c.check_pair(question,answer,model,tokenizer,config)
                c.write_new(out/f'{key}_fixture_{i:02d}_private.json',result); outputs.append(result)
                live.update(f'{key} readiness fixtures completed {i+1}/12',completed=i+1)
            summary=c.gate_summary(outputs,key)
            peak=Path('/sys/fs/cgroup/memory.peak')
            summary.update(status='COMPLETED',wall_seconds=time.monotonic()-started,
                peak_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024),
                container_peak_bytes=int(peak.read_text()) if peak.exists() else None,
                model_manifest_sha256=c.sha(root/('experiments/e019_model_manifest.json' if key=='G15' else 'experiments/e020_model7_manifest.json')),
                environment_lock_sha256=c.sha(root/'experiments/e020_environment_lock.json'),
                readiness_lock_sha256=c.sha(root/'experiments/e020_readiness_lock.json'))
            c.write_new(out/(key+'_receipt.json'),summary)
            print(json.dumps(summary),flush=True)
    except BaseException as exc:
        c.write_new(out/(key+'_failure.json'),{'status':'FAILED','phase':'synthetic_readiness','model':key,
            'exception_type':type(exc).__name__,'automatic_retry':False})
        raise


if __name__=='__main__': main()
