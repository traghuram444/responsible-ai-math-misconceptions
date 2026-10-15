"""Strict E013 aggregate schema, numerical verification and complete result tables."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from . import e007_publication as s
from .e011_publication import payload_schema, same, STAT
from . import e013 as c
from .data_contract import file_sha256
from .e006 import write_new

N, I, NN, B = s.N, s.I, s.NN, s.B
L, E = s.listing, s.enum
MODEL = E(*c.MODELS)
STRATUM = E(*c.core.STRATA)
REPETITION = {'values':L(N), 'mean':NN, 'sd':NN, 'p025':NN, 'p975':NN}
CAL = {'n':I,'correct_n':I,'incorrect_n':I,'accuracy':NN,'mean_confidence':NN,
       'confidence_minus_accuracy':NN,'ece':NN,'brier':NN,
       'ineligible_reasons':L(E('n_below_200','correct_below_20','incorrect_below_20'))}
WIN = {'wins':I,'ties':I,'losses':I,'gain':NN,'loss':NN,'net':NN}
AGREE = {'n':I,'top1_agreement':NN,'ordered_top3_agreement':NN, **{m:WIN for m in c.METRICS}}
RECORD = {'model':MODEL,'fold':E(0,1,2,3,4),'question':s.nullable(I),'stratum':STRATUM,'n':I,
          'original':{m:NN for m in c.METRICS}, 'agreement':AGREE,
          'calibration':{k:CAL for k in ('raw','scaled')},
          'shuffled':{k:{m:{v:REPETITION for v in ('score','original_minus_shuffled')} for m in c.METRICS} for k in c.CONDITIONS}}
AGG = {'model':MODEL,'stratum':STRATUM,'original':{m:STAT for m in c.METRICS},
       'shuffled':{k:{m:{v:{'fold_stat':STAT,'paired_replicates':REPETITION} for v in ('score','original_minus_shuffled')}
                        for m in c.METRICS} for k in c.CONDITIONS},
       'calibration':{m:{v:STAT for v in ('raw','scaled','raw_minus_scaled')}
                      for m in ('accuracy','mean_confidence','confidence_minus_accuracy','ece','brier')},
       'agreement':{'top1_agreement':STAT,'ordered_top3_agreement':STAT,
                    **{m:{k:STAT for k in WIN} for m in c.METRICS}}}
OPPORTUNITY = {'fold':E(0,1,2,3,4),'question':s.nullable(I),'condition':E(*c.CONDITIONS),
               **{k:I for k in ('n','cells','singleton_rows','movable_rows','label_mixed_rows')},
               'label_mixed_share':N,'donor_changed_n':REPETITION,'input_changed_n':REPETITION}
DIAGNOSTIC = {'model':E('E011','E012'),'fold':E(0,1,2,3,4),'temperature':N,'calibration_supported_n':I,
              'lower_boundary':B,'upper_boundary':B,'raw_at_clip_floor_fraction':N,
              'top1_change_fraction':N,'ordered_top3_change_fraction':N}
SCHEMA = {'experiment_id':E('E013'),'status':E('COMPLETED'),
    'development':{m:payload_schema(m)['development'] for m in ('E011','E012')},
    'records':L(RECORD),'aggregate':L(AGG),'opportunity':L(OPPORTUNITY),'probability_diagnostics':L(DIAGNOSTIC),
    'primary':{'models':L({'model':E('E011','E012'),**STAT,'positive_folds':I,'criterion_met':B}),'concordant':B},
    'provenance':{'git_revision':s.pattern('[0-9a-f]{40}'),'image_id':s.pattern('sha256:[0-9a-f]{64}'),
        'lock_sha256':s.HASH,'frozen_development_sha256':s.HASH,
        'started_utc':s.pattern('[0-9T:+.Z-]+'),'finished_utc':s.pattern('[0-9T:+.Z-]+'),'wall_seconds':N,
        'model_fits':E(145),'fit_warnings':E(0),'reproduction_model_folds':E(10),
        'global_freeze_verified':E(True),'preservation_verified':E(True),'uid':E(10001),'gid':E(10001),
        'replicates':E(100),'permutation_seed':E(20261014),'row_level_outputs':E(False),'preserved_files':I}}


def check_repetition(rep, n):
    if len(rep['values']) != n: raise ValueError('Replicate count changed.')
    same(rep, c.repetition(rep['values']))


def check_cal(g):
    n, correct, errors = g['n'], g['correct_n'], g['incorrect_n']
    if not 0 <= correct <= n or correct + errors != n: raise ValueError('Calibration counts.')
    same(g['accuracy'], correct/n if n else None)
    same(g['confidence_minus_accuracy'], g['mean_confidence']-g['accuracy'] if n else None)
    reasons = (['n_below_200'] if n < 200 else []) + (['correct_below_20'] if correct < 20 else []) + (['incorrect_below_20'] if errors < 20 else [])
    same(g['ineligible_reasons'], reasons)
    for metric, upper in (('mean_confidence',1),('ece',1),('brier',2)):
        value = g[metric]
        if value is not None and not 0 <= value <= upper: raise ValueError('Calibration metric range.')
    for metric in ('ece','brier'):
        if (g[metric] is None) != bool(reasons): raise ValueError('Calibration eligibility.')


def validate(p):
    s.validate_schema(p, SCHEMA)
    rows = p['records']
    keys = [(r['model'],r['fold'],r['question'],r['stratum']) for r in rows]
    if len(set(keys)) != len(keys) or len(rows) != 300: raise ValueError('Incomplete reporting grid.')
    for model in c.MODELS:
        seen = []
        for fold in range(5):
            parts = [r for r in rows if r['model'] == model and r['fold'] == fold]
            questions = sorted({r['question'] for r in parts if r['question'] is not None})
            if len(questions) != 3: raise ValueError('Question grid.')
            seen.extend(questions)
            if {(r['question'],r['stratum']) for r in parts} != {(q,t) for q in [None,*questions] for t in c.core.STRATA}:
                raise ValueError('Stratum grid.')
            for stratum in c.core.STRATA:
                full = next(r for r in parts if r['question'] is None and r['stratum'] == stratum)
                sub = [r for r in parts if r['question'] is not None and r['stratum'] == stratum]
                if sum(r['n'] for r in sub) != full['n']: raise ValueError('Question counts do not sum.')
                if full['n']:
                    for m in c.METRICS:
                        same(full['original'][m], sum(r['n']*r['original'][m] for r in sub if r['n'])/full['n'])
                        for condition in c.CONDITIONS:
                            actual = full['shuffled'][condition][m]['score']['values']
                            expected = np.sum([r['n']*np.asarray(r['shuffled'][condition][m]['score']['values']) for r in sub if r['n']],axis=0)/full['n']
                            same(actual, expected.tolist())
        if len(set(seen)) != 15: raise ValueError('Question coverage.')
    for row in rows:
        n = row['n']
        same(row['agreement']['n'], n)
        for g in row['calibration'].values():
            same(g['n'],n); check_cal(g)
        same(row['calibration']['scaled']['accuracy'],row['original']['top1_accuracy'])
        for metric in c.METRICS:
            original = row['original'][metric]
            if (original is None) != (n == 0) or (original is not None and not 0 <= original <= 1): raise ValueError('Original metric.')
            w = row['agreement'][metric]
            if w['wins']+w['ties']+w['losses'] != n: raise ValueError('Win loss count identity.')
            same(w['net'],w['gain']-w['loss'] if n else None)
            baseline = next(r for r in rows if r['model']=='frequency' and all(r[k]==row[k] for k in ('fold','question','stratum')))
            same(w['net'],original-baseline['original'][metric] if n else None)
            for condition in c.CONDITIONS:
                item = row['shuffled'][condition][metric]
                for rep in item.values(): check_repetition(rep,100 if n else 0)
                if any(not 0 <= x <= 1 for x in item['score']['values']): raise ValueError('Shuffle score range.')
                same(item['original_minus_shuffled']['values'],[original-v for v in item['score']['values']])
                if row['model']=='frequency': same(item['score']['values'],[original]*100 if n else [])
    same(p['aggregate'],c.summarize(rows)); same(p['primary'],c.primary(rows))
    if len(p['opportunity']) != 40 or len(p['probability_diagnostics']) != 10: raise ValueError('Diagnostic grid.')
    for r in p['opportunity']:
        if r['singleton_rows']+r['movable_rows'] != r['n'] or not 0 <= r['label_mixed_rows'] <= r['movable_rows']: raise ValueError('Opportunity counts.')
        same(r['label_mixed_share'],r['label_mixed_rows']/r['n'])
        for k in ('donor_changed_n','input_changed_n'):
            check_repetition(r[k],100)
            if any(not 0 <= v <= r['movable_rows'] for v in r[k]['values']): raise ValueError('Movement counts.')
        if any(a>b for a,b in zip(r['input_changed_n']['values'],r['donor_changed_n']['values'])): raise ValueError('Changed-input count exceeds donors.')
    for model in ('E011','E012'):
        if [d['fold'] for d in p['development'][model]] != list(range(5)): raise ValueError('Development grid.')
    for r in p['probability_diagnostics']:
        d = p['development'][r['model']][r['fold']]
        same(r['temperature'],d['temperature']); same(r['calibration_supported_n'],d['calibration_supported_n'])
        same(r['lower_boundary'],bool(abs(np.log(r['temperature'])+3)<=1e-5))
        same(r['upper_boundary'],bool(abs(np.log(r['temperature'])-3)<=1e-5))


def fmt(x):
    if x is None: return 'null'
    if isinstance(x,bool): return str(x)
    if isinstance(x,int): return str(x)
    return f'{x:.6f}'


def table(lines,headers,rows):
    lines.extend(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|'])
    for row in rows: lines.append('| '+' | '.join(fmt(v) if not isinstance(v,str) else v for v in row)+' |')
    lines.append('')


def render(p):
    validate(p)
    lines=['# E013 numerical results','',
        'Equal-fold summaries and shuffle dispersion are descriptive only. No interpretation or next-experiment proposal is included.',
        '', '## Aggregate exact label performance','']
    data=[]
    for a in p['aggregate']:
        if a['stratum']!='all': continue
        data.append([a['model'],a['original']['map_at_3']['mean'],
            *[a['shuffled'][k]['map_at_3']['score']['fold_stat']['mean'] for k in c.CONDITIONS],
            a['original']['top1_accuracy']['mean']])
    table(lines,['Model','Original MAP@3','Explanation shuffle MAP@3','Pair shuffle MAP@3','Original accuracy'],data)
    lines.extend(['## Registered explanation criteria',''])
    table(lines,['Model','Delta mean','Fold SD','Positive folds','Criterion met'],
        [[r['model'],r['mean'],r['sd'],str(r['positive_folds'])+'/5',r['criterion_met']] for r in p['primary']['models']])
    lines.extend(['## Complete fold performance and paired differences',''])
    table(lines,['Model','Fold','Original MAP@3','Explanation MAP@3','Explanation delta','Pair MAP@3','Pair delta','Original accuracy','Explanation accuracy','Pair accuracy'],
        [[r['model'],r['fold'],r['original']['map_at_3'],
          r['shuffled']['explanation_shuffle']['map_at_3']['score']['mean'],r['shuffled']['explanation_shuffle']['map_at_3']['original_minus_shuffled']['mean'],
          r['shuffled']['pair_shuffle']['map_at_3']['score']['mean'],r['shuffled']['pair_shuffle']['map_at_3']['original_minus_shuffled']['mean'],
          r['original']['top1_accuracy'],*[r['shuffled'][k]['top1_accuracy']['score']['mean'] for k in c.CONDITIONS]]
         for r in p['records'] if r['question'] is None and r['stratum']=='all'])
    lines.extend(['## All aggregate support and shuffle dispersion summaries','',
        'Percentiles describe the 100 label-blind assignments, not population confidence intervals. Fold SD is across the five replicate-mean effects.',''])
    table(lines,['Model','Stratum','Metric','Condition','Original mean','Shuffled mean','Delta mean','Delta fold SD','Defined folds','Delta shuffle SD','Delta p2.5','Delta p97.5'],
        [[a['model'],a['stratum'],m,k,a['original'][m]['mean'],a['shuffled'][k][m]['score']['fold_stat']['mean'],
          a['shuffled'][k][m]['original_minus_shuffled']['fold_stat']['mean'],a['shuffled'][k][m]['original_minus_shuffled']['fold_stat']['sd'],
          a['shuffled'][k][m]['original_minus_shuffled']['fold_stat']['defined_folds'],
          *[a['shuffled'][k][m]['original_minus_shuffled']['paired_replicates'][v] for v in ('sd','p025','p975')]]
         for a in p['aggregate'] for m in c.METRICS for k in c.CONDITIONS])
    lines.extend(['## All fold and question support results',''])
    table(lines,['Model','Fold','Question','Stratum','n','Metric','Original','Explanation mean','Explanation delta','Pair mean','Pair delta'],
        [[r['model'],r['fold'],'all' if r['question'] is None else r['question'],r['stratum'],r['n'],m,r['original'][m],
          *[r['shuffled'][k][m][v]['mean'] for k in c.CONDITIONS for v in ('score','original_minus_shuffled')]]
         for r in p['records'] for m in c.METRICS])
    lines.extend(['## Original predictions versus frequency',''])
    table(lines,['Model','Fold','Question','Stratum','n','Top1 agreement','Ordered top3 agreement','RR wins','RR ties','RR losses','RR gain','RR loss','RR net','Accuracy wins','Accuracy ties','Accuracy losses'],
        [[r['model'],r['fold'],'all' if r['question'] is None else r['question'],r['stratum'],r['n'],
          r['agreement']['top1_agreement'],r['agreement']['ordered_top3_agreement'],
          *[r['agreement']['map_at_3'][k] for k in ('wins','ties','losses','gain','loss','net')],
          *[r['agreement']['top1_accuracy'][k] for k in ('wins','ties','losses')]] for r in p['records']])
    lines.extend(['## Calibration aggregates',''])
    table(lines,['Model','Stratum','Metric','Raw mean','Scaled mean','Paired raw minus scaled','Paired fold SD','Eligible paired folds'],
        [[a['model'],a['stratum'],m,v['raw']['mean'],v['scaled']['mean'],v['raw_minus_scaled']['mean'],v['raw_minus_scaled']['sd'],v['raw_minus_scaled']['defined_folds']]
         for a in p['aggregate'] for m,v in a['calibration'].items()])
    lines.extend(['## Complete original input calibration diagnostics',''])
    table(lines,['Model','Fold','Question','Stratum','Scale','n','Correct','Accuracy','Confidence','Confidence minus accuracy','ECE','Brier','Exclusions'],
        [[r['model'],r['fold'],'all' if r['question'] is None else r['question'],r['stratum'],k,g['n'],g['correct_n'],g['accuracy'],g['mean_confidence'],g['confidence_minus_accuracy'],g['ece'],g['brier'],', '.join(g['ineligible_reasons']) or 'eligible']
         for r in p['records'] for k,g in r['calibration'].items()])
    lines.extend(['## Probability scale diagnostics',''])
    table(lines,['Model','Fold','Temperature','Supported calibration n','Lower boundary','Upper boundary','Raw floor fraction','Top1 changes','Top3 changes'],
        [[r[k] for k in ('model','fold','temperature','calibration_supported_n','lower_boundary','upper_boundary','raw_at_clip_floor_fraction','top1_change_fraction','ordered_top3_change_fraction')] for r in p['probability_diagnostics']])
    lines.extend(['## Permutation opportunity',''])
    table(lines,['Fold','Question','Condition','n','Cells','Singleton rows','Movable rows','Label mixed rows','Label mixed share','Donor changes mean','Donor changes SD','Input changes mean','Input changes SD'],
        [[r['fold'],'all' if r['question'] is None else r['question'],r['condition'],*[r[k] for k in ('n','cells','singleton_rows','movable_rows','label_mixed_rows','label_mixed_share')],
          *[r[k][v] for k in ('donor_changed_n','input_changed_n') for v in ('mean','sd')]] for r in p['opportunity']])
    lines.extend(['Full replicate-level aggregates and all descriptive dispersion values are retained in [the aggregate artifact](../results/E013_aggregates.json). No row-level predictions or donor assignments are included.',''])
    return '\n'.join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output-json',type=Path,required=True); parser.add_argument('--output-markdown',type=Path,required=True)
    args=parser.parse_args()
    p=json.loads(args.source.read_text()); validate(p)
    receipt=json.loads((args.source.parent/'execution.json').read_text())
    if receipt['status']!='COMPLETED' or receipt['results_sha256']!=file_sha256(args.source): raise ValueError('Completion receipt mismatch.')
    same(receipt['git_revision'],p['provenance']['git_revision']); same(receipt['lock_sha256'],p['provenance']['lock_sha256'])
    if args.output_json.exists() or args.output_markdown.exists(): raise ValueError('Never overwrite published results.')
    write_new(args.output_json,p)
    with args.output_markdown.open('x',encoding='utf-8',newline='\n') as stream: stream.write(render(p))
    print('E013 aggregate schema, arithmetic and completion receipt verified; numerical report published.')


if __name__=='__main__': main()
