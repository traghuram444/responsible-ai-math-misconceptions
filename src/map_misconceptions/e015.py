"""Approved E015 token-retention ablation; historical scientific modules stay unchanged."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import time
import warnings
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
from . import e011_context as core
from . import e013 as prior
from . import e014 as historical
from .e014 import mappings, score_fold, opportunity, reproduction_diagnostic
from .e013 import repetition, probability_diagnostic
from .data_contract import combined_label, file_sha256, load_training_data
from .e006 import write_new
from .e011_publication import same
from .e012_retry import sanitized_exception
from .resilient_status import ResilientStatus
from .selective import _routing_order

ROOT = Path(__file__).resolve().parents[2]
ARMS = ('A', 'B', 'C')
MODELS = (*ARMS, 'frequency')
CONDITIONS = ('explanation_shuffle',)
METRICS = prior.METRICS
REPLICATES = prior.REPLICATES
PERMUTATION_SEED = prior.PERMUTATION_SEED
ATTEMPT = 'e015_attempt01'
FEATURES = historical.FEATURES
FIELDS = ('QuestionText', 'MC_Answer', 'StudentExplanation', 'full_input')
PAIRS = (('B','A'), ('C','B'), ('C','A'), ('A','frequency'), ('B','frequency'), ('C','frequency'))
TOKEN_PATTERN = r"\[(?:question|answer|explanation)\]|\b\w+\b|<=|>=|!=|==|\*\*|//|[+\-*/=<>^%×÷−≤≥≠±√∞≈:.,()\[\]{}|!\\]"
TOKEN_RE = re.compile(TOKEN_PATTERN)
MARKERS = ('[question]', '[answer]', '[explanation]')
SYMBOLS = frozenset(list("+-*/=<>^%×÷−≤≥≠±√∞≈:.,()[]{}|!\\") + ['<=','>=','!=','==','**','//'])


def notation_tokens(text):
    return [t[1:-1] if t in MARKERS else t for t in TOKEN_RE.findall(text)]


def make_vectorizer(arm, params):
    options = {}
    if arm == 'B': options['token_pattern'] = r"(?u)\b\w+\b"
    elif arm == 'C': options.update(tokenizer=notation_tokens, token_pattern=None, analyzer='word')
    elif arm != 'A': raise ValueError('Unknown registered arm.')
    return TfidfVectorizer(ngram_range=tuple(params['ngram_range']), min_df=params['min_df'],
                          sublinear_tf=True, **options)


def fit_model(train, arm, params):
    vectorizer = make_vectorizer(arm, params)
    classifier = LogisticRegression(C=params['C'], max_iter=2000, class_weight=None,
                                    random_state=core.SEED, n_jobs=1)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        matrix = vectorizer.fit_transform(core.input_text(train, 'full_context'))
        classifier.fit(matrix, combined_label(train))
    if caught: raise RuntimeError('Fit warning; no automatic retry.')
    return vectorizer, classifier


def predict(fitted, features):
    if set(features) != set(FEATURES): raise ValueError('Label-free features required.')
    return core.predict(fitted, features, 'full_context')


def select(train, arm, completed_fit):
    splits = list(GroupKFold(3).split(train, combined_label(train), train.QuestionId.astype(str)))
    candidates = []
    for params in core.e001.GRID:
        scores = []
        for left, right in splits:
            fitted = fit_model(train.iloc[left], arm, params)
            prob, classes = predict(fitted, train.iloc[right][FEATURES])
            scores.append(core.map_at_3(combined_label(train.iloc[right]).to_numpy(), prob, classes))
            completed_fit()
        candidates.append({'params': {**params, 'ngram_range': list(params['ngram_range'])},
            'inner_fold_map_at_3': scores, 'inner_mean_map_at_3': float(np.mean(scores))})
    winner = max(range(len(candidates)), key=lambda i: candidates[i]['inner_mean_map_at_3'])
    return {'selected_index': winner, 'candidates': candidates}


def prepare_parts(train, calibration_frame, evaluation_features, positions, fold, arm, completed_fit):
    if set(evaluation_features) != set(FEATURES): raise ValueError('Evaluation features must be label-free.')
    parts = (train, calibration_frame, evaluation_features)
    if [p.QuestionId.nunique() for p in parts] != [9,3,3]: raise ValueError('Role counts changed.')
    questions = [set(p.QuestionId) for p in parts]
    if any(questions[i] & questions[j] for i in range(3) for j in range(i)):
        raise ValueError('Question roles overlap.')
    selection = select(train, arm, completed_fit)
    fitted = fit_model(train, arm, selection['candidates'][selection['selected_index']]['params'])
    completed_fit()
    cal_raw, classes = predict(fitted, calibration_frame[FEATURES])
    raw, eval_classes = predict(fitted, evaluation_features)
    if not np.array_equal(classes, eval_classes): raise ValueError('Class alignment.')
    fp, fc = core.e001.frequency_probabilities(train, evaluation_features)
    if not np.array_equal(classes, fc): raise ValueError('Frequency class alignment.')
    temperature, supported = core.e001.temperature_scale(combined_label(calibration_frame).to_numpy(), cal_raw, classes)
    prob = core.e001.apply_temperature(raw, temperature)
    description = {'arm':'full_context', 'model':'logistic', 'fold':fold,
        'n_train':len(train), 'n_calibration':len(calibration_frame), 'n_evaluation':len(evaluation_features),
        'role_question_counts':[9,3,3], 'selection':selection, 'temperature':temperature,
        'calibration_supported_n':supported, 'fits':10}
    memory = {'raw':raw, 'prob':prob, 'classes':classes, 'frequency_prob':fp, 'frequency_classes':fc,
        'positions':np.asarray(positions), 'questions':evaluation_features.QuestionId.to_numpy(),
        'train_labels':combined_label(train).to_numpy(), 'train_questions':train.QuestionId.to_numpy(),
        'order':_routing_order(prob.max(axis=1),positions.tolist(),fold,core.SEED),
        'frequency_order':_routing_order(fp.max(axis=1),positions.tolist(),fold,core.SEED)}
    for v in memory.values():
        if isinstance(v,np.ndarray): v.setflags(write=False)
    return description, memory, fitted[0]


def prepare(frame, assignments, fold, arm, completed_fit):
    roles = assignments[f'fold_{fold}'].to_numpy()
    positions = np.flatnonzero(roles == 'evaluation')
    return prepare_parts(frame.iloc[np.flatnonzero(roles=='train')],
        frame.iloc[np.flatnonzero(roles=='calibration')],frame.iloc[positions][FEATURES].copy(),
        positions,fold,arm,completed_fit)


def token_coverage(vectorizer, texts):
    preprocessor, tokenizer, analyzer = (vectorizer.build_preprocessor(),vectorizer.build_tokenizer(),vectorizer.build_analyzer())
    vocab = vectorizer.vocabulary_
    counts = dict(n=len(texts),blank_n=0,zero_token_n=0,zero_surviving_feature_n=0,
                  vocabulary_size=len(vocab))
    totals = {k:[0,0] for k in ('unigram','short_word','notation','selected_analyzer')}
    for text in texts:
        tokens = tokenizer(preprocessor(text))
        features = analyzer(text)
        counts['blank_n'] += int(text=='')
        counts['zero_token_n'] += int(not tokens)
        counts['zero_surviving_feature_n'] += int(not any(t in vocab for t in features))
        kinds = {'unigram':tokens, 'short_word':[t for t in tokens if len(t)==1 and re.fullmatch(r'\w+',t)],
                 'notation':[t for t in tokens if t in SYMBOLS], 'selected_analyzer':features}
        for key, seq in kinds.items():
            totals[key][0] += sum(t in vocab for t in seq)
            totals[key][1] += len(seq)
    counts['occurrences'] = {k:{'covered':v[0],'total':v[1],'coverage':v[0]/v[1] if v[1] else None} for k,v in totals.items()}
    counts['zero_token_rate'] = counts['zero_token_n']/counts['n'] if counts['n'] else None
    counts['zero_surviving_feature_rate'] = counts['zero_surviving_feature_n']/counts['n'] if counts['n'] else None
    return counts


def coverage_records(vectorizer, metadata, model, fold):
    result = []
    for question in [None,*sorted(metadata.QuestionId.unique().tolist())]:
        part = metadata if question is None else metadata[metadata.QuestionId==question]
        for field in FIELDS:
            text = core.input_text(part,'full_context') if field=='full_input' else part[field].fillna('').astype(str)
            result.append({'model':model,'fold':fold,'question':question,'field':field,**token_coverage(vectorizer,text.tolist())})
    return result


def summarize(rows):
    output = []
    for model in MODELS:
        for stratum in core.STRATA:
            parts = sorted([r for r in rows if r['model'] == model and r['stratum'] == stratum and r['question'] is None],
                           key=lambda r: r['fold'])
            if [r['fold'] for r in parts] != list(range(5)): raise ValueError('Missing fold grid.')
            item = {'model': model, 'stratum': stratum,
                'original': {m: core.stat([r['original'][m] for r in parts]) for m in METRICS}, 'shuffled': {},
                'calibration': {}, 'agreement': {}}
            for condition in CONDITIONS:
                item['shuffled'][condition] = {}
                for metric in METRICS:
                    item['shuffled'][condition][metric] = {}
                    for kind in ('score', 'original_minus_shuffled'):
                        reps = [r['shuffled'][condition][metric][kind] for r in parts]
                        values = [x['values'] for x in reps if x['values']]
                        item['shuffled'][condition][metric][kind] = {
                            'fold_stat': core.stat([x['mean'] for x in reps]),
                            'paired_replicates': repetition(np.asarray(values).mean(axis=0) if values else [])}
            for metric in ('accuracy', 'mean_confidence', 'confidence_minus_accuracy', 'ece', 'brier'):
                raw, scaled = ([r['calibration'][kind][metric] for r in parts] for kind in ('raw', 'scaled'))
                item['calibration'][metric] = {'raw': core.stat(raw), 'scaled': core.stat(scaled),
                    'raw_minus_scaled': core.stat([a - b if a is not None and b is not None else None for a, b in zip(raw, scaled)])}
            for metric in ('top1_agreement', 'ordered_top3_agreement'):
                item['agreement'][metric] = core.stat([r['agreement'][metric] for r in parts])
            for metric in METRICS:
                item['agreement'][metric] = {key: core.stat([r['agreement'][metric][key] for r in parts])
                                             for key in ('wins', 'ties', 'losses', 'gain', 'loss', 'net')}
            output.append(item)
    return output



def contrasts(rows):
    result = []
    for left,right in PAIRS:
        for row in rows:
            if row['model']!=left: continue
            ref=next(r for r in rows if r['model']==right and all(r[k]==row[k] for k in ('fold','question','stratum')))
            result.append({'left':left,'right':right,**{k:row[k] for k in ('fold','question','stratum','n')},
                'deltas':{m:row['original'][m]-ref['original'][m] if row['n'] else None for m in METRICS},
                'calibration_deltas':{kind:{m:row['calibration'][kind][m]-ref['calibration'][kind][m]
                    if row['calibration'][kind][m] is not None and ref['calibration'][kind][m] is not None else None
                    for m in ('ece','brier')} for kind in ('raw','scaled')}})
    return result


def contrast_summary(records):
    return [{'left':left,'right':right,'stratum':stratum,
        'deltas':{m:core.stat([r['deltas'][m] for r in parts]) for m in METRICS},
        'calibration_deltas':{kind:{m:core.stat([r['calibration_deltas'][kind][m] for r in parts])
            for m in ('ece','brier')} for kind in ('raw','scaled')}}
        for left,right in PAIRS for stratum in core.STRATA
        for parts in [sorted([r for r in records if r['left']==left and r['right']==right
                    and r['stratum']==stratum and r['question'] is None],key=lambda r:r['fold'])]]


def primary(rows):
    parts = sorted([r for r in contrasts(rows) if r['left']=='C' and r['right']=='frequency'
                    and r['question'] is None and r['stratum']=='all'], key=lambda r:r['fold'])
    return core.meaningful([r['deltas']['map_at_3'] for r in parts])


def routing_summary(records):
    return [{'model': model, 'review_percent': b, 'metrics': {
        metric: core.stat([next(x for x in next(r for r in records if r['model'] == model and r['fold'] == f)['budgets']
                                if x['review_percent'] == b)['all'][metric] for f in range(5)])
        for metric in ('original_n','retained_n','top1_accuracy','map_at_3','risk','mean_confidence','ece','brier')}}
        for model in MODELS for b in (0,10,20,30,40,50)]



def verify_lock(root, image_id, private=True):
    lock=json.loads((root/'experiments/e015_lock.json').read_text())
    if image_id!=lock['docker_image_id']: raise ValueError('Image changed.')
    historical.verify_lock(root,image_id,private=private)
    approval=json.loads((root/'experiments/e015_approval.json').read_text())
    if core.canonical_sha(root/'docs/E015_PROTOCOL.md')!=approval['protocol_sha256_lf']:
        raise ValueError('Approved protocol changed.')
    for group in ('files','preserved'):
        for name,sha in lock[group].items():
            path=(root/name).resolve()
            if not path.is_relative_to(root.resolve()) or core.canonical_sha(path)!=sha:
                raise ValueError('Locked file changed.')
    if private:
        for name,sha in lock['private_evidence'].items():
            if file_sha256(root/name)!=sha: raise ValueError('Historical evidence changed.')
    return lock


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-revision',required=True); parser.add_argument('--image-id',required=True)
    args=parser.parse_args()
    if not re.fullmatch('[0-9a-f]{40}',args.git_revision) or os.getuid()!=10001 or os.getgid()!=10001:
        raise ValueError('Exact revision and non-root identity required.')
    lock=verify_lock(ROOT,args.image_id)
    output=ROOT/'artifacts'/ATTEMPT
    if not output.is_dir() or any(output.iterdir()): raise ValueError('Empty new attempt required.')
    started,clock=datetime.now(timezone.utc).isoformat(),time.monotonic()
    write_new(output/'attempt.json',{'experiment_id':'E015','git_revision':args.git_revision,'started_utc':started})
    live=ResilientStatus(output/'live_status.json',experiment_id='E015',total=2151)
    try:
        with live:
            def frozen():
                return core.verify_frozen_inputs(ROOT/'data/raw/train.csv',ROOT/'artifacts/splits',
                    expected_data_sha=core.DATA_SHA,expected_manifest_sha=core.MANIFEST_SHA,
                    expected_assignments_sha=core.ASSIGN_SHA)
            frozen()
            frame=load_training_data(ROOT/'data/raw/train.csv')
            assignments=pd.read_csv(ROOT/'artifacts/splits/grouped_fold_assignments.csv',keep_default_na=False)
            ref11=json.loads((ROOT/'results/E011_aggregates.json').read_text())
            ref13=json.loads((ROOT/'results/E013_aggregates.json').read_text())
            prepared,maps,metadata={},{},{}
            fits=0
            for fold in range(5):
                for arm in ARMS:
                    def fitted():
                        nonlocal fits
                        fits+=1
                        live.update(f'{arm} fold {fold+1}/5; fits {fits}/150',completed=fits)
                    live.update(f'{arm} fold {fold+1}/5; nested training')
                    prepared[arm,fold]=prepare(frame,assignments,fold,arm,fitted)
                memory=prepared['A',fold][1]
                metadata[fold]=frame.iloc[memory['positions']][FEATURES].copy()
                maps[fold]=mappings(metadata[fold],memory['positions'],fold)
                print(json.dumps({'phase':'prepared','fold':fold,'fits':fits}),flush=True)
            if fits!=150: raise ValueError('Fit count changed.')
            development=[{'tokenizer_arm':arm,**prepared[arm,f][0]} for f in range(5) for arm in ARMS]
            write_new(output/'frozen_development.json',{'development':development,'model_fits':fits,
                'all_predictions_and_mappings_frozen':True,'lock_sha256':file_sha256(ROOT/'experiments/e015_lock.json')})
            freeze_sha=file_sha256(output/'frozen_development.json')
            # Global barrier. Evaluation targets are accessed only after all development is sealed.
            truths={f:combined_label(frame.iloc[prepared['A',f][1]['positions']]).to_numpy() for f in range(5)}
            live.update('All folds frozen; historical reproduction gates')
            for fold in range(5):
                d,m,_=prepared['A',fold]
                prior.check_reproduction(d,m,truths[fold],ref11)
            same(core.answer_diagnostics(frame),ref11['answer_diagnostics'])
            rows,opportunities,diagnostics,routes,coverage,categories=[],[],[],[],[],[]
            completed=fits
            for model in ('A','frequency','B','C'):
                for fold in range(5):
                    d,m,v=prepared['A' if model=='frequency' else model,fold]
                    if model=='frequency':
                        m={**m,'raw':m['frequency_prob'],'prob':m['frequency_prob'],'classes':m['frequency_classes'],
                           'order':m['frequency_order']}
                        d={**d,'temperature':1.}
                    diagnostics.append(probability_diagnostic(model,fold,d,m))
                    def scored(condition,replicate):
                        nonlocal completed
                        completed+=1
                        if replicate%10==9:
                            live.update(f'{model} fold {fold+1}/5; shuffle {replicate+1}/100',completed=completed)
                    part=score_fold(model,fold,m,truths[fold],maps[fold],scored)
                    rows.extend(part)
                    evaluated=core.evaluate(d,m,truths[fold])
                    routes.append({'model':model,'fold':fold,'budgets':evaluated['risk_coverage']})
                    for question,g in [(None,evaluated['category']),*[(r['QuestionId'],r['category']) for r in evaluated['questions']]]:
                        categories.append({'model':model,'fold':fold,'question':question,**g})
                    if model!='frequency': coverage.extend(coverage_records(v,metadata[fold],model,fold))
                    if model=='A':
                        opportunities.extend(opportunity(metadata[fold],m['positions'],fold,maps[fold],truths[fold]))
                    if model=='frequency' and fold==4:
                        reproduction_diagnostic([{**r,'model':'E011' if r['model']=='A' else r['model']} for r in rows],
                            opportunities,[{**r,'model':'E011'} for r in diagnostics if r['model']=='A'],ref13)
                        live.update('Historical gates passed; B/C scoring begins')
                    if model in ('B','C'):
                        item=next(r for r in part if r['question'] is None and r['stratum']=='all')
                        baseline=next(r for r in rows if r['model']=='frequency' and r['fold']==fold and r['question'] is None and r['stratum']=='all')
                        live.update(f'{model} fold {fold+1}/5 scored',completed=completed,latest_metrics={
                            'MAP@3 latest fold':item['original']['map_at_3'],
                            'Frequency latest fold':baseline['original']['map_at_3'],
                            'Delta latest fold':item['original']['map_at_3']-baseline['original']['map_at_3']})
            frozen(); verify_lock(ROOT,args.image_id)
            if freeze_sha!=file_sha256(output/'frozen_development.json'): raise ValueError('Freeze changed.')
            comparisons=contrasts(rows)
            payload={'experiment_id':'E015','status':'COMPLETED','development':development,'records':rows,
                'aggregate':summarize(rows),'primary':primary(rows),'contrasts':comparisons,
                'contrast_aggregate':contrast_summary(comparisons),'opportunity':opportunities,
                'probability_diagnostics':diagnostics,'routing':routes,'routing_aggregate':routing_summary(routes),
                'coverage':coverage,'category':categories,
                'provenance':{'git_revision':args.git_revision,'image_id':args.image_id,
                    'lock_sha256':file_sha256(ROOT/'experiments/e015_lock.json'),'frozen_development_sha256':freeze_sha,
                    'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'wall_seconds':time.monotonic()-clock,
                    'model_fits':fits,'fit_warnings':0,'reproduction_model_folds':5,'global_freeze_verified':True,
                    'preservation_verified':True,'uid':os.getuid(),'gid':os.getgid(),'replicates':REPLICATES,
                    'permutation_seed':PERMUTATION_SEED,'row_level_outputs':False,'preserved_files':len(lock['preserved'])}}
            from .e015_publication import validate
            validate(payload)
            write_new(output/'results.json',payload)
            live.update('Complete aggregate artifact serialized',completed=live.total)
        write_new(output/'execution.json',{'status':'COMPLETED','results_sha256':file_sha256(output/'results.json'),
            'monitor':live.diagnostics(),'git_revision':args.git_revision,'lock_sha256':file_sha256(ROOT/'experiments/e015_lock.json')})
        print(json.dumps({'experiment_id':'E015','status':'COMPLETED','primary':payload['primary']}),flush=True)
    except BaseException as exc:
        write_new(output/'failure.json',{'experiment_id':'E015','status':'FAILED','exception':sanitized_exception(exc)})
        raise RuntimeError('E015 stopped; no automatic retry; sanitized diagnostics only.') from None


if __name__=='__main__': main()
