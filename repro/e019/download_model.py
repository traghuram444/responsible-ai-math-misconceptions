"""Fetch only the approved publisher files; never reads assessment data."""
import hashlib
import json
from pathlib import Path
import urllib.request

REVISION = 'aafeb0fc6f22cbf0eaeed126eff8be45b0360a35'
FILES = ('LICENSE', 'README.md', 'config.json', 'generation_config.json', 'merges.txt',
         'model.safetensors', 'tokenizer.json', 'tokenizer_config.json', 'vocab.json')
WEIGHT_SHA = '08faf1e950173bb44c11d26df28c55da7237dc55c77dbc1cbae4a5d7584540d9'
ROOT = Path(__file__).resolve().parents[2]


def main():
    destination = ROOT / 'artifacts/e019_setup/model'
    destination.mkdir(exist_ok=False)
    records = {}
    for name in FILES:
        url = f'https://huggingface.co/Qwen/Qwen2.5-Math-1.5B-Instruct/resolve/{REVISION}/{name}'
        h = hashlib.sha256(); size = 0
        with urllib.request.urlopen(url, timeout=60) as response, (destination / name).open('xb') as out:
            while chunk := response.read(4 * 1024 * 1024):
                out.write(chunk); h.update(chunk); size += len(chunk)
        records[name] = {'sha256': h.hexdigest(), 'bytes': size}
        if name == 'model.safetensors' and (h.hexdigest() != WEIGHT_SHA or size != 3087467144):
            raise ValueError('Published weight identity mismatch; stop.')
        print(json.dumps({'downloaded': name, **records[name]}), flush=True)
    with (destination.parent / 'model_manifest.json').open('x', encoding='utf-8', newline='\n') as f:
        json.dump({'repository': 'Qwen/Qwen2.5-Math-1.5B-Instruct', 'revision': REVISION,
                   'files': records}, f, indent=2); f.write('\n')


if __name__ == '__main__': main()
