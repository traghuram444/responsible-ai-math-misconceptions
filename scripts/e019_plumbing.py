"""One authorized synthetic generation only; never a MAP pilot or tuning loop."""
import argparse
from pathlib import Path
from map_misconceptions import e019_checker as c

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('mode', choices=['config','synthetic'])
    a = p.parse_args(); output = Path('/setup')
    tokenizer, config, metadata = c.inspect_configuration('/model')
    if a.mode == 'config':
        c.write_new(output / 'resolved_config.json', metadata)
    else:
        import json
        if metadata != json.loads((output / 'resolved_config.json').read_text()):
            raise ValueError('Configuration changed after lock.')
        c.write_new(output / 'synthetic_started.json', {'one_prompt_only': True})
        c.configure()
        model = c.load_model('/model')
        result = c.check_pair('What is 1 + 1?', '2', model, tokenizer, config)
        c.write_new(output / 'synthetic_private.json', result)
        public = {k:v for k,v in result.items() if k != 'completion'}
        c.write_new(output / 'synthetic_receipt.json', public)
        print(json.dumps(public), flush=True)
