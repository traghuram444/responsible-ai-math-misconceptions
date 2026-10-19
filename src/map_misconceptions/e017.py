"""E017 approved component-information diagnostics; never a new predictive model."""
from __future__ import annotations
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import time
from types import MappingProxyType
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from . import e016 as previous
from . import e013 as prior
from .e011_publication import same
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import write_new
from .e012_retry import sanitized_exception
from .resilient_status import ResilientStatus

ROOT = Path(__file__).resolve().parents[2]
core = previous.core
ATTEMPT = 'e017_attempt01'
REAL = ('F', 'E011', 'E016')
ORACLES = ('O_C', 'O_S', 'O_CS')
METRICS = ('map_at_3', 'top1_accuracy')
COMPONENTS = {'correctness': ('False', 'True'), 'status': ('Correct', 'Misconception', 'Neither'),
              'category': tuple(core.CATEGORIES)}
SUPPLIED = {'F': None, 'O_C': 'correctness', 'O_S': 'status', 'O_CS': 'category'}
REAL_PAIRS = (('E016', 'F'), ('E011', 'F'), ('E016', 'E011'))
ORACLE_PAIRS = (('O_C', 'F'), ('O_S', 'F'), ('O_CS', 'F'), ('O_CS', 'O_C'),
                ('O_CS', 'O_S'), ('O_C', 'O_S'), ('O_CS', 'E016'), ('O_CS', 'E011'))
JOINT = ('both_correct', 'correctness_only', 'status_only', 'neither_correct')
BANDS = ('unsupported', 'rank1', 'rank2', 'rank3', 'rank_gt3')


def components(labels):
    cats = np.asarray([str(y).split(':', 1)[0] for y in labels])
    if not set(cats).issubset(COMPONENTS['category']):
        raise ValueError('Unknown Category; no regrouping allowed.')
    return {'category': cats, 'correctness': np.asarray([x.split('_', 1)[0] for x in cats]),
            'status': np.asarray([x.split('_', 1)[1] for x in cats])}


def oracle_bank(classes, frequency):
    """Training-only API: precompute every compatible list, without evaluation inputs."""
    classes, frequency = np.asarray(classes), np.asarray(frequency)
    if classes.ndim != 1 or frequency.shape != classes.shape or not len(classes):
        raise ValueError('Invalid training inventory.')
    if classes.tolist() != sorted(set(classes.tolist())):
        raise ValueError('Original sorted distinct inventory required.')
    previous.valid_probabilities(frequency[None, :], len(classes))
    if (frequency <= 0).any(): raise ValueError('Only observed training labels allowed.')
    parts = components(classes)
    ranking = np.argsort(-frequency)
    bank = {}
    for arm, component in SUPPLIED.items():
        bank[arm] = {}
        for value in (COMPONENTS[component] if component else (None,)):
            mask = parts[component] == value if component else np.ones(len(classes), dtype=bool)
            indices = np.flatnonzero(mask)
            ordered = tuple(classes[ranking[mask[ranking]]].tolist())
            prediction = str(classes[indices[np.argmax(frequency[indices])]]) if len(indices) else None
            bank[arm][value] = (ordered, prediction)
        bank[arm] = MappingProxyType(bank[arm])
    return MappingProxyType(bank)


def oracle_scores(truth, bank):
    """Truth-bearing diagnostic only. No output can enter model preparation."""
    parts = components(truth)
    scores, ranks = {}, {}
    for arm, component in SUPPLIED.items():
        rr = np.zeros(len(truth)); acc = np.zeros(len(truth)); rank = np.zeros(len(truth), dtype=int)
        for i, y in enumerate(truth):
            ordering, prediction = bank[arm][parts[component][i] if component else None]
            if y in ordering:
                rank[i] = ordering.index(y) + 1
                if rank[i] <= 3: rr[i] = 1. / rank[i]
            acc[i] = float(y == prediction)
        scores[arm] = {'map_at_3': rr, 'top1_accuracy': acc}
        ranks[arm] = rank
    for high, low in (('O_C', 'F'), ('O_S', 'F'), ('O_CS', 'O_C'), ('O_CS', 'O_S')):
        for metric in METRICS:
            if np.any(scores[high][metric] < scores[low][metric]):
                raise ValueError('Oracle filtering monotonicity failed.')
    supported = np.isin(truth, bank['F'][None][0])
    for arm in SUPPLIED:
        for metric in METRICS:
            if np.any(scores[arm][metric][~supported] != 0): raise ValueError('Unsupported truth scored.')
    return scores, ranks


def frequency_memory(memory):
    fp, fc = memory['frequency_prob'], memory['frequency_classes']
    cat = previous.marginalize(fp, fc); cat.setflags(write=False)
    return {**memory, 'raw': fp, 'prob': fp, 'classes': fc, 'category_raw': cat,
            'order': memory['frequency_order']}


def original_records(model, fold, memory, truth):
    """Exactly the historical non-perturbation record fields, without shuffle work."""
    top, prediction = prior.rank_labels(memory['prob'], memory['classes'])
    ft, fp = prior.rank_labels(memory['frequency_prob'], memory['frequency_classes'])
    scores, baseline = prior.row_scores(truth, top, prediction), prior.row_scores(truth, ft, fp)
    return [{'model': model, 'fold': fold, 'question': q, 'stratum': s, 'n': int(mask.sum()),
             'original': {k: float(scores[k][mask].mean()) if mask.any() else None for k in METRICS},
             'agreement': prior.agreement(scores, baseline, top, prediction, ft, fp, mask),
             'calibration': {kind: prior.calibration(truth, p, memory['classes'], mask)
                 for kind, p in (('raw', memory['raw']), ('scaled', memory['prob']))}}
            for q, s, mask in prior.scopes(memory, truth)]


def reproduce(prepared, truths, ref16, ref11, completed):
    for fold in range(5):
        d, m, _ = prepared['E011', fold]
        prior.check_reproduction(d, m, truths[fold], ref11)
        for arm in previous.ARMS:
            expected = next(x for x in ref16['development'] if x['learning_arm'] == arm and x['fold'] == fold)
            same({'learning_arm': arm, **prepared[arm, fold][0]}, expected)
        for model in ('frequency', 'E011', 'factorized'):
            d, m, _ = prepared['E011' if model == 'frequency' else model, fold]
            if model == 'frequency': m = frequency_memory(m); d = {**d, 'temperature': 1.}
            expected = [{k: v for k, v in r.items() if k != 'shuffled'} for r in ref16['records']
                        if r['model'] == model and r['fold'] == fold]
            same(original_records(model, fold, m, truths[fold]), expected)
            same(previous.category_records(model, fold, m, truths[fold]),
                 [r for r in ref16['category'] if r['model'] == model and r['fold'] == fold])
            same(core.evaluate(d, m, truths[fold])['risk_coverage'],
                 next(r['budgets'] for r in ref16['routing'] if r['model'] == model and r['fold'] == fold))
            completed(model, fold)


def exact_records(arm, fold, domains, scores, oracle=False):
    return [{'arm': arm, **({'supplied_component': SUPPLIED[arm]} if oracle else {}),
             'fold': fold, 'question': q, 'stratum': s, 'n': int(mask.sum()),
             'metrics': {k: float(scores[k][mask].mean()) if mask.any() else None for k in METRICS}}
            for q, s, mask in domains]


def matrix_metrics(matrix):
    cm = np.asarray(matrix, dtype=int)
    if cm.ndim != 2 or cm.shape[0] != cm.shape[1] or (cm < 0).any():
        raise ValueError('Invalid confusion matrix.')
    n = int(cm.sum()); diag = np.diag(cm); den = cm.sum(axis=0) + cm.sum(axis=1)
    f1 = np.divide(2. * diag, den, out=np.zeros(len(cm)), where=den != 0)
    return {'accuracy': float(diag.sum() / n) if n else None,
            'macro_f1': float(f1.mean()) if n else None}, [
        [float(x / row.sum()) if row.sum() else None for x in row] for row in cm]


def component_predictions(category_prob):
    previous.valid_probabilities(category_prob, 6)
    source = components(np.asarray(core.CATEGORIES))
    return {name: np.asarray(order)[np.column_stack([
        category_prob[:, source[name] == value].sum(axis=1) for value in order]).argmax(axis=1)]
        for name, order in COMPONENTS.items()}


def component_records(arm, fold, memory, truth, domains):
    true = components(truth); records, joint = [], []
    for scale, prob in (('raw', memory['category_raw']),
                        ('final', previous.marginalize(memory['prob'], memory['classes']))):
        predictions = component_predictions(prob)
        c = predictions['correctness'] == true['correctness']; s = predictions['status'] == true['status']
        states = (c & s, c & ~s, ~c & s, ~c & ~s)
        for q, stratum, mask in domains:
            base = {'arm': arm, 'fold': fold, 'question': q, 'stratum': stratum,
                    'scale': scale, 'n': int(mask.sum())}
            for name, order in COMPONENTS.items():
                cm = confusion_matrix(true[name][mask], predictions[name][mask], labels=list(order))
                metrics, normalized = matrix_metrics(cm)
                records.append({**base, 'component': name, 'metrics': metrics,
                                'confusion_counts': cm.tolist(), 'confusion_row_normalized': normalized})
            counts = {name: int((state & mask).sum()) for name, state in zip(JOINT, states)}
            joint.append({**base, 'counts': counts,
                          'metrics': {k: v / base['n'] if base['n'] else None for k, v in counts.items()}})
    return records, joint


def residual_records(fold, domains, scores, ranks):
    rows = []
    for q, s, mask in domains:
        if s != 'all': continue
        n = int(mask.sum()); r = ranks[mask]
        counts = dict(zip(BANDS, [int((r == i).sum()) for i in range(4)] + [int((r > 3).sum())]))
        metrics = {'unsupported_loss': counts['unsupported'] / n}
        for k in METRICS:
            metrics['supported_ranking_loss_' + k] = float(np.where(r > 0, 1. - scores[k][mask], 0.).mean())
            metrics['total_loss_' + k] = 1. - float(scores[k][mask].mean())
            same(metrics['total_loss_' + k], metrics['unsupported_loss'] + metrics['supported_ranking_loss_' + k])
        same(sum(counts[k] / i for i, k in enumerate(('rank1', 'rank2', 'rank3'), 1)) / n,
             float(scores['map_at_3'][mask].mean()))
        rows.append({'arm': 'O_CS', 'supplied_component': 'category', 'fold': fold, 'question': q,
                     'stratum': 'all', 'n': n, 'counts': counts,
                     'shares': {k: v / n for k, v in counts.items()}, 'metrics': metrics})
    return rows


def summarize(rows, dimensions):
    groups = defaultdict(list)
    for r in rows:
        if r['question'] is None: groups[tuple(r[k] for k in dimensions)].append(r)
    output = []
    for key, parts in groups.items():
        parts = sorted(parts, key=lambda x: x['fold'])
        if [r['fold'] for r in parts] != list(range(5)): raise ValueError('Missing five-fold grid.')
        output.append({**dict(zip(dimensions, key)), 'n_total': sum(r['n'] for r in parts),
                       'metrics': {m: core.stat([r['metrics'][m] for r in parts]) for m in parts[0]['metrics']}})
    return output


def contrasts(rows, pairs, extra=()):
    keys = ('fold', 'question', 'stratum', *extra)
    lookup = {(r['arm'], *(r[k] for k in keys)): r for r in rows}
    output = []
    for left, right in pairs:
        for r in rows:
            if r['arm'] != left: continue
            ref = lookup[right, *(r[k] for k in keys)]
            if r['n'] != ref['n']: raise ValueError('Paired population mismatch.')
            output.append({'left': left, 'right': right, **{k: r[k] for k in keys}, 'n': r['n'],
                'metrics': {m: r['metrics'][m] - ref['metrics'][m]
                            if r['metrics'][m] is not None and ref['metrics'][m] is not None else None
                            for m in r['metrics']}})
    return output


def headroom(rows):
    return [{'arm': arm, 'supplied_component': SUPPLIED[arm], 'primary': arm == 'O_CS',
             **core.meaningful([next(r['metrics']['map_at_3'] for r in rows if r['left'] == arm and
                r['right'] == 'F' and r['question'] is None and r['stratum'] == 'all' and r['fold'] == f)
                for f in range(5)])} for arm in ORACLES]


def pooled_confusions(rows):
    groups = defaultdict(list)
    keys = ('arm', 'scale', 'component', 'stratum')
    for r in rows:
        if r['question'] is None: groups[tuple(r[k] for k in keys)].append(r)
    result = []
    for key, parts in groups.items():
        cm = np.sum([r['confusion_counts'] for r in parts], axis=0)
        _, normalized = matrix_metrics(cm)
        result.append({**dict(zip(keys, key)), 'n_total': int(cm.sum()), 'confusion_counts': cm.tolist(),
                       'confusion_row_normalized': normalized})
    return result


def build_panels(real, oracle, cats, joint, residual):
    rc = contrasts(real, REAL_PAIRS)
    oc = contrasts([*real, *[r for r in oracle if r['arm'] != 'F']], ORACLE_PAIRS)
    cc = contrasts(cats, REAL_PAIRS, ('scale', 'component'))
    return {'real_prediction': {'records': real, 'aggregate': summarize(real, ('arm', 'stratum')),
        'contrasts': rc, 'contrast_aggregate': summarize(rc, ('left', 'right', 'stratum')),
        'component_records': cats, 'component_aggregate': summarize(cats, ('arm', 'scale', 'component', 'stratum')),
        'component_contrasts': cc, 'component_contrast_aggregate': summarize(cc, ('left', 'right', 'scale', 'component', 'stratum')),
        'joint_records': joint, 'joint_aggregate': summarize(joint, ('arm', 'scale', 'stratum')),
        'pooled_confusions': pooled_confusions(cats)},
        'oracle_diagnostic': {'uses_evaluation_truth': True, 'records': oracle,
        'aggregate': summarize(oracle, ('arm', 'supplied_component', 'stratum')),
        'contrasts': oc, 'contrast_aggregate': summarize(oc, ('left', 'right', 'stratum')),
        'headroom': headroom(oc), 'residual_records': residual,
        'residual_aggregate': summarize(residual, ('arm', 'supplied_component', 'stratum'))}}


def verify_lock(root, image_id, private=True):
    previous.verify_lock(root, image_id, private=private)
    lock = json.loads((root / 'experiments/e017_lock.json').read_text())
    approval = json.loads((root / 'experiments/e017_approval.json').read_text())
    if image_id != lock['docker_image_id']: raise ValueError('Image changed.')
    if core.canonical_sha(root / 'docs/E017_PROTOCOL.md') != approval['protocol_sha256_lf']:
        raise ValueError('Approved protocol changed.')
    for group in ('files', 'preserved'):
        for name, sha in lock[group].items():
            path = (root / name).resolve()
            if not path.is_relative_to(root.resolve()) or core.canonical_sha(path) != sha:
                raise ValueError('Locked file changed.')
    prefix = (root / 'docs/EXPERIMENT_LOG.md').read_bytes().replace(b'\r\n', b'\n')[:lock['append_only_log']['bytes']]
    if hashlib.sha256(prefix).hexdigest() != lock['append_only_log']['sha256']:
        raise ValueError('Historical log changed.')
    if private:
        for name, sha in lock['private_evidence'].items():
            if file_sha256(root / name) != sha: raise ValueError('Historical private evidence changed.')
    return lock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-revision', required=True); parser.add_argument('--image-id', required=True)
    args = parser.parse_args()
    if not re.fullmatch('[0-9a-f]{40}', args.git_revision) or os.getuid() != 10001 or os.getgid() != 10001:
        raise ValueError('Exact revision and non-root identity required.')
    lock = verify_lock(ROOT, args.image_id)
    output = ROOT / 'artifacts' / ATTEMPT
    if not output.is_dir() or any(output.iterdir()): raise ValueError('Empty new attempt required.')
    started, clock = datetime.now(timezone.utc).isoformat(), time.monotonic()
    write_new(output / 'attempt.json', {'experiment_id': 'E017', 'git_revision': args.git_revision, 'started_utc': started})
    live = ResilientStatus(output / 'live_status.json', experiment_id='E017', total=146)
    try:
        with live:
            def frozen():
                core.verify_frozen_inputs(ROOT / 'data/raw/train.csv', ROOT / 'artifacts/splits',
                    expected_data_sha=core.DATA_SHA, expected_manifest_sha=core.MANIFEST_SHA,
                    expected_assignments_sha=core.ASSIGN_SHA)
            frozen()
            frame = load_training_data(ROOT / 'data/raw/train.csv')
            assignments = pd.read_csv(ROOT / 'artifacts/splits/grouped_fold_assignments.csv', keep_default_na=False)
            ref16 = json.loads((ROOT / 'results/E016_aggregates.json').read_text())
            ref11 = json.loads((ROOT / 'results/E011_aggregates.json').read_text())
            prepared, banks = {}, {}
            fits = 0
            for fold in range(5):
                for arm in previous.ARMS:
                    def fitted():
                        nonlocal fits
                        fits += 1
                        live.update(f'REAL {arm} fold {fold+1}/5; fits {fits}/100', completed=fits)
                    live.update(f'REAL {arm} fold {fold+1}/5; historical nested reconstruction')
                    prepared[arm, fold] = previous.prepare(frame, assignments, fold, arm, fitted)
                m = prepared['E011', fold][1]
                banks[fold] = oracle_bank(m['frequency_classes'], m['frequency_prob'][0])
                if tuple(prior.rank_labels(m['frequency_prob'], m['frequency_classes'])[0][0]) != banks[fold]['F'][None][0][:3]:
                    raise ValueError('Historical frequency ordering changed.')
                print(json.dumps({'phase': 'prepared', 'fold': fold, 'fits': fits}), flush=True)
            if fits != 100: raise ValueError('Fit count changed.')
            development = [{'learning_arm': arm, **prepared[arm, f][0]} for f in range(5) for arm in previous.ARMS]
            write_new(output / 'frozen_development.json', {'development': development, 'model_fits': fits,
                'all_predictions_and_candidate_lists_frozen': True, 'lock_sha256': file_sha256(ROOT / 'experiments/e017_lock.json')})
            freeze_sha = file_sha256(output / 'frozen_development.json')
            # Truth boundary: all ten real preparations and all candidate banks already sealed.
            for f in range(5): previous.checked_categories(frame.iloc[prepared['E011', f][1]['positions']])
            truths = {f: combined_label(frame.iloc[prepared['E011', f][1]['positions']]).to_numpy() for f in range(5)}
            completed = fits
            def gate(model, fold):
                nonlocal completed
                completed += 1
                live.update(f'Historical gate passed: {model} fold {fold+1}/5', completed=completed)
            reproduce(prepared, truths, ref16, ref11, gate)
            real, oracle, cats, joint, residual = [], [], [], [], []
            for fold in range(5):
                base = prepared['E011', fold][1]
                domains = prior.scopes(base, truths[fold])
                for arm in REAL:
                    m = frequency_memory(base) if arm == 'F' else prepared['factorized' if arm == 'E016' else arm, fold][1]
                    top, pred = prior.rank_labels(m['prob'], m['classes'])
                    scores = prior.row_scores(truths[fold], top, pred)
                    records = exact_records(arm, fold, domains, scores)
                    real.extend(records)
                    cr, jr = component_records(arm, fold, m, truths[fold], domains)
                    cats.extend(cr); joint.extend(jr)
                    completed += 1
                    latest = next(r for r in records if r['question'] is None and r['stratum'] == 'all')
                    live.update(f'REAL {arm} fold {fold+1}/5 scored', completed=completed,
                                latest_metrics={f'REAL {arm} MAP@3 latest fold': latest['metrics']['map_at_3']})
                oscores, ranks = oracle_scores(truths[fold], banks[fold])
                oracle.extend(exact_records('F', fold, domains, oscores['F'], oracle=True))
                for arm in ORACLES:
                    records = exact_records(arm, fold, domains, oscores[arm], oracle=True)
                    oracle.extend(records); completed += 1
                    latest = next(r for r in records if r['question'] is None and r['stratum'] == 'all')
                    live.update(f'ORACLE {arm} fold {fold+1}/5 diagnostic scored', completed=completed,
                                latest_metrics={f'ORACLE {arm} MAP@3 latest fold': latest['metrics']['map_at_3']})
                residual.extend(residual_records(fold, domains, oscores['O_CS'], ranks['O_CS']))
            frozen(); verify_lock(ROOT, args.image_id)
            if freeze_sha != file_sha256(output / 'frozen_development.json'): raise ValueError('Freeze changed.')
            payload = {'experiment_id': 'E017', 'status': 'COMPLETED', 'development': development,
                **build_panels(real, oracle, cats, joint, residual),
                'provenance': {'git_revision': args.git_revision, 'image_id': args.image_id,
                    'lock_sha256': file_sha256(ROOT / 'experiments/e017_lock.json'), 'frozen_development_sha256': freeze_sha,
                    'started_utc': started, 'finished_utc': datetime.now(timezone.utc).isoformat(),
                    'wall_seconds': time.monotonic()-clock, 'model_fits': fits, 'fit_warnings': 0,
                    'reproduction_model_folds': 15, 'global_freeze_verified': True, 'preservation_verified': True,
                    'uid': os.getuid(), 'gid': os.getgid(), 'row_level_outputs': False, 'preserved_files': len(lock['preserved'])}}
            from .e017_publication import validate
            validate(payload)
            write_new(output / 'results.json', payload)
            live.update('Complete REAL and ORACLE aggregate artifact serialized', completed=146)
        write_new(output / 'execution.json', {'status': 'COMPLETED', 'results_sha256': file_sha256(output / 'results.json'),
            'monitor': live.diagnostics(), 'git_revision': args.git_revision, 'lock_sha256': file_sha256(ROOT / 'experiments/e017_lock.json')})
        print(json.dumps({'experiment_id': 'E017', 'status': 'COMPLETED', 'oracle_headroom': payload['oracle_diagnostic']['headroom']}), flush=True)
    except BaseException as exc:
        write_new(output / 'failure.json', {'experiment_id': 'E017', 'status': 'FAILED', 'exception': sanitized_exception(exc)})
        raise RuntimeError('E017 stopped; no automatic retry; sanitized diagnostics only.') from None


if __name__ == '__main__': main()
