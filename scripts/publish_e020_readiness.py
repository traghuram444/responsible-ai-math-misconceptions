"""Verify the one-attempt gate and publish only strict aggregate receipts."""
import json
from pathlib import Path
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e020_integrity import preserve_e020,verify_readiness
from map_misconceptions.e020_readiness_publication import validate


def main():
    root=Path(__file__).resolve().parents[1]; out=root/'artifacts/e020_attempt01'
    if list(out.glob('*failure.json')): raise ValueError('Technical failure; no completed gate publication.')
    verify_readiness(root); preserve_e020(root)
    p=json.loads((out/'readiness.json').read_text()); validate(p)
    attempt=json.loads((out/'attempt.json').read_text())
    if attempt['lock_sha256']!=sha(root/'experiments/e020_readiness_lock.json'): raise ValueError('Attempt lock changed.')
    for r in p['model_receipts']:
        key=r['model']
        if r!=json.loads((out/(key+'_receipt.json')).read_text()): raise ValueError('Model receipt mismatch.')
        expected={'readiness_lock_sha256':sha(root/'experiments/e020_readiness_lock.json'),
            'environment_lock_sha256':sha(root/'experiments/e020_environment_lock.json'),
            'model_manifest_sha256':sha(root/('experiments/e019_model_manifest.json' if key=='G15' else 'experiments/e020_model7_manifest.json'))}
        if any(r[k]!=v for k,v in expected.items()): raise ValueError('Receipt provenance mismatch.')
    destination=root/'results/E020_readiness.json'
    write_new(destination,p)
    lines=['# E020 synthetic readiness results','',
        'These are the fixed synthetic gate results, not MAP evaluation results. No MAP inference or classifier fit has started.',
        '',f"Status: `{p['status']}`. Automatic retry: false.",'',
        '| Checkpoint | Readouts | Binary correct | Insufficient correct | Gate | Tokens/s | Projected MAP hours |',
        '|---|---:|---:|---:|---|---:|---:|']
    for r in p['model_receipts']:
        rate='null' if r['tokens_per_second'] is None else f"{r['tokens_per_second']:.6f}"
        hours='null' if r['projected_map_seconds'] is None else f"{r['projected_map_seconds']/3600:.6f}"
        lines.append(f"| {r['model']} | {r['completed_readouts']}/12 | {r['binary_correct']}/10 | {r['insufficient_correct']}/2 | {r['gate_passed']} | {rate} | {hours} |")
    lines.extend(['','The smaller checkpoint has only a technical completion gate; its semantic accuracy is not a stopping criterion.',
        'The 7B gate requires 12/12 completed readouts, at least 8/10 binary fixtures and 2/2 insufficient-information fixtures.',
        'Timings are synthetic-suite projections, not a deadline. No fixture-level decisions or generated text are published.',
        '', '[Full-precision aggregate receipt](../results/E020_readiness.json)',
        '',f'Aggregate SHA-256: `{sha(destination)}`.',''])
    with (root/'docs/E020_READINESS.md').open('x',encoding='utf-8',newline='\n') as stream: stream.write('\n'.join(lines))
    print('Validated readiness aggregates published; no MAP results or private fields.')


if __name__=='__main__': main()
