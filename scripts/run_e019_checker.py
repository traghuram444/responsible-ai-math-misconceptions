"""Stage 1: input-only fixed model generation; no raw MAP data mount or scoring."""
import json
import os
from pathlib import Path
import time
from collections import Counter
from map_misconceptions import e019_checker as c
from map_misconceptions.e019_integrity import model_files
from map_misconceptions.resilient_status import ResilientStatus


def main():
    root=Path('/workspace'); out=Path('/attempt')
    lock=json.loads((root/'experiments/e019_lock.json').read_text())
    if os.getuid()!=10001 or os.getgid()!=10001: raise ValueError('Non-root identity required.')
    catalogue=Path('/inputs/catalogue.json')
    if c.sha(catalogue)!=lock['catalogue_sha256']: raise ValueError('Catalogue changed.')
    pairs=c.load_catalogue(catalogue)
    if len(pairs)!=lock['pairs']: raise ValueError('Pair count changed.')
    c.write_new(out/'checker_started.json',{'pairs':len(pairs),'lock_sha256':c.sha(root/'experiments/e019_lock.json')})
    started=time.monotonic()
    live=ResilientStatus(out/'solver_status.json',experiment_id='E019',total=len(pairs))
    try:
        with live:
            live.update('Checker: verifying model and loading CPU float32; no scores available')
            model_files('/model',json.loads((root/'experiments/e019_model_manifest.json').read_text()))
            tokenizer,config,metadata=c.inspect_configuration('/model')
            if metadata!=json.loads((root/'experiments/e019_environment_lock.json').read_text())['pins']:
                raise ValueError('Locked configuration changed.')
            c.configure(); model=c.load_model('/model')
            outputs=[]
            for i,(question,answer) in enumerate(pairs):
                live.update(f'Checker pair {i+1}/{len(pairs)}; no scores before global freeze',completed=i)
                result=c.check_pair(question,answer,model,tokenizer,config)
                c.write_new(out/f'pair_{i:04d}_private.json',result)
                outputs.append(result)
                live.update(f'Checker pairs completed {i+1}/{len(pairs)}',completed=i+1)
            c.write_new(out/'checker_cache_private.json',outputs)
            counts=Counter(x['reason'] for x in outputs)
            c.write_new(out/'checker_completion.json',{'status':'COMPLETED','pairs':len(pairs),
                'cache_sha256':c.sha(out/'checker_cache_private.json'),'catalogue_sha256':c.sha(catalogue),
                'reason_counts':{r:counts[r] for r in c.REASONS},'wall_seconds':time.monotonic()-started,
                'generated_tokens':[x['generated_tokens'] for x in outputs],
                'input_tokens':[x['input_tokens'] for x in outputs],
                'per_pair_counts_private':True})
            # Only aggregate receipt is eligible for eventual publication.
            c.write_new(out/'checker_aggregate_receipt.json',{'status':'COMPLETED','pairs':len(pairs),
                'cache_sha256':c.sha(out/'checker_cache_private.json'),
                'reason_counts':{r:counts[r] for r in c.REASONS},
                'generated_tokens_total':sum(x['generated_tokens'] for x in outputs),
                'wall_seconds':time.monotonic()-started})
            print('E019 complete label-free cache frozen. No agreement or model results scored.',flush=True)
    except BaseException as exc:
        c.write_new(out/'checker_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,
            'automatic_retry':False,'results_available':False})
        raise


if __name__=='__main__': main()
