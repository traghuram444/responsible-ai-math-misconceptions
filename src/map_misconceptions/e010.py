"""One authorized E010 reconstruction, mask freeze, reproduction and evaluation."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from importlib import metadata
import json
import os
from pathlib import Path
import re
import time

import numpy as np
import pandas as pd
import yaml

from . import e007, e009, e009_metrics
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import canonical_sha, write_new
from .e009_reliability import VARIANTS
from .e010_metrics import aggregate, evaluate_fold, freeze_counts, retention_masks
from .live_status import LiveStatus

PROTOCOL_SHA = '544ac65ad739ae10f70df92d4a73130d1cf46e0583d292cd679e40941db444c5'
CONFIG_SHA = '743a4537c22850e85f6768c0be66d43923195377d2dc7e764f517c4ba777f84b'


def approved_config(root):
    approval = yaml.safe_load((root / 'experiments/e010_approval.yaml').read_text(encoding='utf-8'))
    if approval['status'] != 'authorized_locked_for_execution':
        raise ValueError('Locked E010 authorization required.')
    for path, key, expected in [('docs/E010_PROTOCOL.md', 'protocol_sha256', PROTOCOL_SHA),
                               ('experiments/e010_review.yaml', 'configuration_sha256', CONFIG_SHA)]:
        if canonical_sha(root / path) != expected or approval[key] != expected:
            raise ValueError('Locked E010 documents changed.')
    return yaml.safe_load((root / 'experiments/e010_review.yaml').read_text(encoding='utf-8'))


def references(root, config):
    old_config = e009.approved_config(root)
    e009.references(root, old_config)
    path = root / 'results/E009_aggregates.json'
    if file_sha256(path) != config['e009_result_sha256']:
        raise ValueError('E009 reference changed.')
    ref = json.loads(path.read_text(encoding='utf-8'))
    from .e009_publication import validate_public_payload
    validate_public_payload(ref)
    return ref


def preservation_snapshot(root):
    paths = set()
    for directory in ('docs', 'experiments', 'results', 'artifacts'):
        base = root / directory
        for path in base.rglob('*'):
            if path.is_file() and re.search(r'(^|/)e00[1-9](?:[_./]|$)', path.relative_to(base).as_posix().lower()):
                paths.add(path)
    for directory in ('src', 'scripts', 'tests'):
        paths.update(p for p in (root / directory).rglob('*') if p.suffix in ('.py', '.ps1') and 'e010' not in p.name)
    return {p.relative_to(root).as_posix(): file_sha256(p) for p in sorted(paths)}


def reproduction_gate(description, memory, truth, reference):
    rows, rank = e009_metrics.evaluate_fold(description, memory, truth)
    expected_rows = [r for r in reference['records'] if (r['variant'], r['fold']) == (description['variant'], description['fold'])]
    expected_rank = [r for r in reference['ranking'] if (r['variant'], r['fold']) == (description['variant'], description['fold'])]
    if len(rows) != 20 or len(rank) != 5:
        raise ValueError('Incomplete E009 reproduction grid.')
    e009.compare_reference(rows, expected_rows)
    e009.compare_reference(rank, expected_rank)
    return {'variant': description['variant'], 'fold': description['fold'], 'evaluation_records': 20, 'ranking_records': 5}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-revision', required=True)
    parser.add_argument('--image-id', required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    config = approved_config(root)
    if (not re.fullmatch(r'[a-f0-9]{40}', args.git_revision) or args.image_id != config['docker_image_id']
            or os.getuid() != 10001 or os.getgid() != 10001):
        raise ValueError('Audited revision, image and non-root identity required.')
    output = root / 'artifacts/e010'
    output.mkdir(exist_ok=True)
    if any((output / n).exists() for n in ('attempt.json', 'results.json', 'failure.json')):
        raise ValueError('Existing E010 attempt; no silent retry.')
    started, clock = datetime.now(timezone.utc).isoformat(), time.monotonic()
    write_new(output / 'attempt.json', {'experiment_id': 'E010', 'git_revision': args.git_revision, 'started_utc': started})
    try:
        with LiveStatus(output / 'live_status.json', experiment_id='E010', total=431) as live:
            live.update('Verifying locked protocol, inputs and E009 reference')
            historical = e007.approved_config(root)
            frozen = e007.frozen_check(root, historical)
            reference, before = references(root, config), preservation_snapshot(root)
            write_new(output / 'preservation.json', before)
            frame = load_training_data(root / 'data/raw/train.csv')
            assignments = pd.read_csv(root / 'artifacts/splits/grouped_fold_assignments.csv', keep_default_na=False)
            prepared, plans = [], []
            for vi, variant in enumerate(VARIANTS):
                for fold in range(5):
                    index = vi * 5 + fold
                    prior = next(d for d in reference['development'] if d['variant'] == variant and d['fold'] == fold)
                    description, memory, _ = e009.prepare_fold(frame, assignments, variant, fold, live, index * 42, prior['reference_development'])
                    e009.compare_reference(description, prior)
                    masks = retention_masks(memory['scores'], memory['evaluation_positions'], fold)
                    prepared.append((description, memory, masks))
                    plans.extend(freeze_counts(variant, fold, masks))
                    live.update(f'Reconstructed {variant}, fold {fold + 1}/5; masks fixed', completed=(index + 1) * 42,
                                latest_metrics={'Reproduced fold-arms': index + 1, 'Frozen batch policies': 36 * (index + 1)})
                    print(json.dumps({'experiment_id': 'E010', 'phase': 'masks_prepared', 'variant': variant, 'fold': fold}), flush=True)
            development = [d for d, _, _ in prepared]
            write_new(output / 'frozen_plan.json', {'experiment_id': 'E010', 'development': development, 'batch_counts': plans})
            plan_sha = file_sha256(output / 'frozen_plan.json')
            live.update('ALL batch masks frozen; evaluation correctness now permitted', completed=420)
            records, checks = [], []
            for index, (description, memory, masks) in enumerate(prepared):
                truth = combined_label(frame.iloc[memory['evaluation_positions']]).to_numpy()
                checks.append(reproduction_gate(description, memory, truth, reference))
                records.extend(evaluate_fold(description, memory, truth, masks))
                latest = next(r for r in records[-36:] if r['rule'] == 'learned_reliability' and r['review_percent'] == 20)['evaluation']['groups']['all']
                live.update(f'Evaluation verified: {description["variant"]}, fold {description["fold"] + 1}/5', completed=421 + index,
                    latest_metrics={'Verified fold-arms': index + 1, '20% review residual errors/100 (latest fold)': round(latest['remaining_errors_per_100'], 4)})
            summaries = aggregate(records)
            e007.frozen_check(root, e007.approved_config(root))
            references(root, approved_config(root))
            if before != preservation_snapshot(root) or plan_sha != file_sha256(output / 'frozen_plan.json'):
                raise ValueError('Preserved history or frozen plan changed.')
            counts = [b['fits'] for d in development for b in d['crossfit']['blocks']] + [d['final_classifier_fits'] for d in development]
            total_counts = {k: sum(c[k] for c in counts) for k in counts[0]}
            if total_counts['attempted'] != 400:
                raise ValueError('Unexpected fitting count.')
            payload = {'experiment_id': 'E010', 'status': 'COMPLETED', 'provenance': {
                'started_utc': started, 'finished_utc': datetime.now(timezone.utc).isoformat(), 'wall_seconds': time.monotonic() - clock,
                'git_revision': args.git_revision, 'docker_image_id': args.image_id, 'uid': os.getuid(), 'gid': os.getgid(),
                'seed': 20260831, 'protocol_sha256': PROTOCOL_SHA, 'configuration_sha256': CONFIG_SHA,
                'e009_result_sha256': config['e009_result_sha256'], 'frozen_plan_sha256': plan_sha,
                'preserved_files': len(before), 'preservation_verified': True, 'all_masks_frozen_before_evaluation': True,
                'classifier_fits': total_counts, 'router_fitting_calls': sum(d['router']['fitting_calls'] for d in development),
                'router_fallbacks': sum(d['router']['status'] != 'FITTED' for d in development),
                'development_records_reproduced': 10, 'evaluation_records_reproduced': 200, 'ranking_records_reproduced': 50,
                'data_sha256': frozen['data_sha256'], 'manifest_sha256': historical['manifest_sha256'], 'assignments_sha256': historical['assignments_sha256'],
                'packages': {name: metadata.version(name) for name in ('numpy', 'pandas', 'scipy', 'scikit-learn', 'PyYAML')},
                'row_level_artifacts_serialized': False}, 'development': development, 'batch_counts': plans,
                'reproduction': checks, 'records': records, 'aggregate': summaries}
            from .e010_publication import validate_public_payload
            validate_public_payload(payload)
            write_new(output / 'results.json', payload)
            live.update('E010 complete: aggregate/fold/question results serialized', completed=431)
        print('E010 COMPLETED', flush=True)
        return 0
    except Exception as exc:
        write_new(output / 'failure.json', {'experiment_id': 'E010', 'status': 'FAILED', 'exception_type': type(exc).__name__})
        print(f'E010 FAILED ({type(exc).__name__}); no automatic retry.', flush=True)
        raise


if __name__ == '__main__':
    raise SystemExit(main())
