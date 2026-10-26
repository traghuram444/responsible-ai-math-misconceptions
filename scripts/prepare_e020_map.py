"""Label-blind E020 input catalogue and additive MAP-phase scientific lock."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from map_misconceptions.e019_checker import sha,write_new,normalize,load_catalogue
from map_misconceptions.e019_integrity import canonical
from map_misconceptions.e020_integrity import verify_readiness,preserve_e020
from map_misconceptions.e020_map_integrity import no_failures


def catalogue():
    no_failures(ROOT/'artifacts/e020_attempt01'); verify_readiness(ROOT); preserve_e020(ROOT)
    ready=json.loads((ROOT/'results/E020_readiness.json').read_text())
    if ready['status']!='READY_FOR_MAP_IMPLEMENTATION_CHECK': raise ValueError('Readiness unmet.')
    if sha(ROOT/'data/raw/train.csv')!='0a5e4523ec9b1656b979002a58e7cb743d02c9ac2697cc154008f971d413686c': raise ValueError('Data changed.')
    folder=ROOT/'artifacts/e020_attempt01/map_inputs'; folder.mkdir(exist_ok=False)
    try:
        with (ROOT/'data/raw/train.csv').open(encoding='utf-8',newline='') as stream:
            # Read exactly the two authorized columns; never consult labels, IDs or explanations.
            reader=csv.reader(stream); header=next(reader); qi=header.index('QuestionText'); ai=header.index('MC_Answer')
            pairs=set(); n=0
            for fields in reader:
                pairs.add((normalize(fields[qi]),normalize(fields[ai]))); n+=1
        if n!=36696 or len(pairs)!=60: raise ValueError('Input population changed.')
        path=folder/'catalogue.json'
        write_new(path,[{'question':q,'proposed_answer':a} for q,a in sorted(pairs)])
        load_catalogue(path)
        write_new(folder/'receipt.json',{'rows':n,'pairs':len(pairs),'catalogue_sha256':sha(path),'label_blind':True})
        print('Label-blind catalogue frozen: 60 pairs across 36,696 rows; no model calls or scoring.')
    except BaseException as exc:
        write_new(folder/'preparation_failure.json',{'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False}); raise


def freeze():
    verify_readiness(ROOT); n=preserve_e020(ROOT); no_failures(ROOT/'artifacts/e020_attempt01')
    names=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
    files=sorted(set(x for x in names if 'e020_map' in x.lower() and x!='experiments/e020_map_lock.json'))
    files+=['results/E020_readiness.json','docs/E020_READINESS.md']
    env=json.loads((ROOT/'experiments/e020_environment_lock.json').read_text())
    receipt=json.loads((ROOT/'artifacts/e020_attempt01/map_inputs/receipt.json').read_text())
    attempt=ROOT/'artifacts/e020_attempt01'
    inventory=attempt/'map_inputs/readiness_preservation_private.json'
    write_new(inventory,{p.relative_to(attempt).as_posix():sha(p) for p in sorted(attempt.iterdir()) if p.is_file()})
    prefixes={}
    for name in ('docs/E020_EXECUTION.md','docs/EXPERIMENT_LOG.md'):
        raw=(ROOT/name).read_bytes(); prefixes[name]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    write_new(ROOT/'experiments/e020_map_lock.json',{'experiment_id':'E020','phase':'MAP_only','pairs_per_model':60,
        'readiness_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'readiness_lock_sha256':sha(ROOT/'experiments/e020_readiness_lock.json'),
        'readiness_result_sha256':sha(ROOT/'results/E020_readiness.json'),'preserved_files':n,
        'readiness_private_inventory_sha256':sha(inventory),
        'catalogue_sha256':receipt['catalogue_sha256'],'files':{p:canonical(ROOT/p) for p in files},
        'append_only_prefixes':prefixes,'solver_image_id':env['solver_image_id'],'statistical_image_id':env['statistical_image_id']})
    print('Additional MAP lock frozen; readiness lock and all scientific settings unchanged.')


if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('mode',choices=['catalogue','freeze']); args=p.parse_args()
    {'catalogue':catalogue,'freeze':freeze}[args.mode]()
