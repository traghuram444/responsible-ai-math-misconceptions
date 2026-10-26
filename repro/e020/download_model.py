"""Download only pinned publisher files in a container without private-data mounts."""
import hashlib
import json
from pathlib import Path
import urllib.request

REV='ef9926d75ab1d54532f6a30dd5e760355eb9aa4d'
SHARDS={
 'model-00001-of-00004.safetensors':(3945441440,'11f73294487dca1614bd7495e2c4e50372f5794f4cd175ce62d9ec2a8e97873a'),
 'model-00002-of-00004.safetensors':(3864726352,'2b992a00b09340ac3f8e54db70509b709e2eef9f601e679682e3a50b496a7b08'),
 'model-00003-of-00004.safetensors':(3864726424,'2460a589b1d606998574e0d84162e94307a15e2eea2aac6f4ea35f0361657660'),
 'model-00004-of-00004.safetensors':(3556377672,'9e7925045deba3bb6ac461f1c2e7eabbe2a189549156dff1ec08b6c750a82bc5')}
FILES=('LICENSE','README.md','config.json','generation_config.json','merges.txt','tokenizer.json','tokenizer_config.json','vocab.json','model.safetensors.index.json',*SHARDS)


def main():
    root=Path('/setup'); destination=root/'model7'; destination.mkdir(exist_ok=False)
    records={}
    try:
        for name in FILES:
            url=f'https://huggingface.co/Qwen/Qwen2.5-Math-7B-Instruct/resolve/{REV}/{name}'
            h=hashlib.sha256(); size=0; last=0
            with urllib.request.urlopen(url,timeout=60) as response,(destination/name).open('xb') as out:
                while chunk:=response.read(4*1024*1024):
                    out.write(chunk); h.update(chunk); size+=len(chunk)
                    if size-last>=256*1024*1024:
                        print(json.dumps({'file':name,'bytes_downloaded':size}),flush=True); last=size
            if name in SHARDS and (size,h.hexdigest())!=SHARDS[name]: raise ValueError('Pinned weight mismatch.')
            records[name]={'sha256':h.hexdigest(),'bytes':size}
            print(json.dumps({'verified_file':name,**records[name]}),flush=True)
        with (root/'model7_manifest.json').open('x',encoding='utf-8',newline='\n') as f:
            json.dump({'repository':'Qwen/Qwen2.5-Math-7B-Instruct','revision':REV,'files':records},f,indent=2); f.write('\n')
    except BaseException as exc:
        with (root/'download_failure.json').open('x',encoding='utf-8') as f:
            json.dump({'status':'FAILED','exception_type':type(exc).__name__,'automatic_retry':False},f)
        raise


if __name__=='__main__': main()
