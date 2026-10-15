"""Allowlisted E014 aggregates, independent arithmetic checks, complete numerical tables."""
from __future__ import annotations
import argparse
from copy import deepcopy
import json
from pathlib import Path
import numpy as np
from . import e007_publication as s
from . import e013_publication as previous
from . import e014 as c
from .e011_publication import payload_schema, same, STAT, GROUP, check_group
from .e013_publication import check_repetition, check_cal, table, fmt
from .data_contract import file_sha256
from .e006 import write_new

N, I, NN, B = s.N, s.I, s.NN, s.B
L, E = s.listing, s.enum
MODEL = E(*c.MODELS)
RECORD = deepcopy(previous.RECORD)
RECORD['model'] = MODEL
RECORD['shuffled'] = {'explanation_shuffle': RECORD['shuffled']['explanation_shuffle']}
AGG = deepcopy(previous.AGG)
AGG['model'] = MODEL
AGG['shuffled'] = {'explanation_shuffle': AGG['shuffled']['explanation_shuffle']}
OPPORTUNITY = {**previous.OPPORTUNITY, 'condition':E('explanation_shuffle')}
DIAGNOSTIC = {**previous.DIAGNOSTIC, 'model':MODEL}
WEIGHT_SELECTION = {'selected_index':I,'selected_weight':E(*c.WEIGHTS),
    'candidates':L({'weight':E(*c.WEIGHTS),'inner_fold_map_at_3':L(N),'inner_mean_map_at_3':N})}
DEVELOPMENT = {'E011':payload_schema('E011')['development'][1],'weight_selection':WEIGHT_SELECTION,
    'mixture_temperature':N,'mixture_calibration_supported_n':I,
    'mixture_calibration_method':E('unscaled_frequency','e011_temperature','mixture_temperature')}
CONTRAST = {'fold':E(0,1,2,3,4),'question':s.nullable(I),'stratum':E(*c.core.STRATA),'n':I,
    'deltas':{m:{k:NN for k in c.METRICS} for m in ('E011','frequency')},
    'contribution_change_from_E011':{k:NN for k in ('gain','loss','net')}}
ROUTE = {'model':MODEL,'fold':E(0,1,2,3,4),
    'budgets':L({'review_percent':E(0,10,20,30,40,50),'all':GROUP})}
ROUTE_AGG = {'model':MODEL,'review_percent':E(0,10,20,30,40,50),
    'metrics':{m:STAT for m in ('original_n','retained_n','top1_accuracy','map_at_3','risk','mean_confidence','ece','brier')}}
SCHEMA = {'experiment_id':E('E014'),'status':E('COMPLETED'),'development':L(DEVELOPMENT),
    'records':L(RECORD),'aggregate':L(AGG),'opportunity':L(OPPORTUNITY),'probability_diagnostics':L(DIAGNOSTIC),
    'contrasts':L(CONTRAST),'routing':L(ROUTE),'routing_aggregate':L(ROUTE_AGG),
    'contrast_aggregate':L({'stratum':E(*c.core.STRATA),
        'deltas':{m:{k:STAT for k in c.METRICS} for m in ('frequency','E011')},
        'contribution_change_from_E011':{k:STAT for k in ('gain','loss','net')}}),
    'primary':{'frequency':{**STAT,'positive_folds':I,'criterion_met':B},'E011':{**STAT,'positive_folds':I}},
    'provenance':{**previous.SCHEMA['provenance'],'model_fits':E(50),'reproduction_model_folds':E(5)}}


def check_selection(selection, grid, key):
    candidates = selection['candidates']
    if len(candidates)!=len(grid): raise ValueError('Selection grid size changed.')
    for row, setting in zip(candidates,grid):
        same(row[key],setting)
        scores = row['inner_fold_map_at_3']
        if len(scores)!=3 or any(not 0<=v<=1 for v in scores): raise ValueError('Inner score contract.')
        same(row['inner_mean_map_at_3'],float(np.mean(scores)))
    winner = max(range(len(grid)),key=lambda i:candidates[i]['inner_mean_map_at_3'])
    same(selection['selected_index'],winner)
    if key=='weight': same(selection['selected_weight'],grid[winner])


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
    if len(p['opportunity']) != 20 or len(p['probability_diagnostics']) != 15: raise ValueError('Diagnostic grid.')
    for r in p['opportunity']:
        if r['singleton_rows']+r['movable_rows'] != r['n'] or not 0 <= r['label_mixed_rows'] <= r['movable_rows']: raise ValueError('Opportunity counts.')
        same(r['label_mixed_share'],r['label_mixed_rows']/r['n'])
        for k in ('donor_changed_n','input_changed_n'):
            check_repetition(r[k],100)
            if any(not 0 <= v <= r['movable_rows'] for v in r[k]['values']): raise ValueError('Movement counts.')
        if any(a>b for a,b in zip(r['input_changed_n']['values'],r['donor_changed_n']['values'])): raise ValueError('Changed-input count exceeds donors.')

    if len(p['development'])!=5: raise ValueError('Development count.')
    for fold,d in enumerate(p['development']):
        old = d['E011']
        same(old['fold'],fold); same(old['arm'],'full_context'); same(old['role_question_counts'],[9,3,3])
        check_selection(old['selection'],[{**g,'ngram_range':list(g['ngram_range'])} for g in c.core.e001.GRID],'params')
        check_selection(d['weight_selection'],c.WEIGHTS,'weight')
        same(d['mixture_calibration_supported_n'],old['calibration_supported_n'])
        weight = d['weight_selection']['selected_weight']
        method = 'unscaled_frequency' if weight==0 else 'e011_temperature' if weight==1 else 'mixture_temperature'
        same(d['mixture_calibration_method'],method)
        if not np.exp(-3)<=d['mixture_temperature']<=np.exp(3): raise ValueError('Temperature bounds.')
        if weight==0: same(d['mixture_temperature'],1.)
        if weight==1: same(d['mixture_temperature'],old['temperature'])
        for model in c.MODELS:
            diag = next(x for x in p['probability_diagnostics'] if x['model']==model and x['fold']==fold)
            temperature = old['temperature'] if model=='E011' else d['mixture_temperature'] if model=='mixture' else 1.
            same(diag['temperature'],temperature); same(diag['calibration_supported_n'],old['calibration_supported_n'])
            same(diag['lower_boundary'],bool(abs(np.log(temperature)+3)<=1e-5))
            same(diag['upper_boundary'],bool(abs(np.log(temperature)-3)<=1e-5))
        if weight in (0,1):
            control = 'frequency' if weight==0 else 'E011'
            for r in rows:
                if r['model']=='mixture' and r['fold']==fold:
                    expected = next(x for x in rows if x['model']==control and all(x[k]==r[k] for k in ('fold','question','stratum')))
                    same({**r,'model':control},expected)
    same(p['contrasts'],c.contrasts(rows))
    same(p['contrast_aggregate'],c.contrast_summary(p['contrasts']))
    expected_route = {(m,f) for m in c.MODELS for f in range(5)}
    if len(p['routing'])!=15 or {(r['model'],r['fold']) for r in p['routing']}!=expected_route: raise ValueError('Routing grid.')
    for r in p['routing']:
        same([x['review_percent'] for x in r['budgets']],[0,10,20,30,40,50])
        original = next(x for x in rows if x['model']==r['model'] and x['fold']==r['fold'] and x['question'] is None and x['stratum']=='all')
        for b in r['budgets']:
            g = b['all']; check_group(g)
            same(g['original_n'],original['n'])
            same(g['retained_n'],original['n']-original['n']*b['review_percent']//100)
            if b['review_percent']==0:
                same(g['map_at_3'],original['original']['map_at_3'])
                same(g['top1_accuracy'],original['original']['top1_accuracy'])
                for metric in ('ece','brier'): same(g[metric],original['calibration']['scaled'][metric])
    same(p['routing_aggregate'],c.routing_summary(p['routing']))


def render(p):
    validate(p)
    lines=['# E014 numerical results','',
           'Equal-fold and permutation summaries are descriptive only. Numerical results precede interpretation.','',
           '## Aggregate exact label performance','']
    table(lines,['Model','MAP@3','Fold SD','Accuracy','Explanation shuffled MAP@3','Explanation decrement'],
        [[a['model'],a['original']['map_at_3']['mean'],a['original']['map_at_3']['sd'],
          a['original']['top1_accuracy']['mean'],a['shuffled']['explanation_shuffle']['map_at_3']['score']['fold_stat']['mean'],
          a['shuffled']['explanation_shuffle']['map_at_3']['original_minus_shuffled']['fold_stat']['mean']]
         for a in p['aggregate'] if a['stratum']=='all'])
    lines.extend(['## Primary comparison and complete fold results',''])
    h=p['primary']['frequency']
    table(lines,['Comparator','Mixture delta mean','Fold SD','Positive folds','Criterion met'],
        [['frequency',h['mean'],h['sd'],str(h['positive_folds'])+'/5',h['criterion_met']],
         ['E011',p['primary']['E011']['mean'],p['primary']['E011']['sd'],str(p['primary']['E011']['positive_folds'])+'/5','not applicable']])
    table(lines,['Fold','Selected weight','Mixture MAP@3','E011 MAP@3','Frequency MAP@3','Delta versus frequency','Delta versus E011'],
        [[f,p['development'][f]['weight_selection']['selected_weight'],
          *[next(r['original']['map_at_3'] for r in p['records'] if r['model']==m and r['fold']==f and r['question'] is None and r['stratum']=='all') for m in c.MODELS],
          p['primary']['frequency']['fold_values'][f],p['primary']['E011']['fold_values'][f]] for f in range(5)])
    lines.extend(['## Complete inner development selection',''])
    table(lines,['Fold','Stage','Candidate','Settings','Inner fold 0','Inner fold 1','Inner fold 2','Mean','Selected'],
        [[f,stage,i,json.dumps(x.get('params',x.get('weight')),sort_keys=True),
          *x['inner_fold_map_at_3'],x['inner_mean_map_at_3'],i==selection['selected_index']]
         for f,d in enumerate(p['development'])
         for stage,selection in [('logistic',d['E011']['selection']),('weight',d['weight_selection'])]
         for i,x in enumerate(selection['candidates'])])
    lines.extend(['## Aggregate support and explanation dispersion','',
        'Permutation percentiles describe assignments, not population confidence intervals.',''])
    table(lines,['Model','Stratum','Metric','Original','Original fold SD','Defined folds','Shuffled mean',
                 'Decrement mean','Decrement fold SD','Permutation SD','p2.5','p97.5'],
        [[a['model'],a['stratum'],m,a['original'][m]['mean'],a['original'][m]['sd'],a['original'][m]['defined_folds'],
          a['shuffled']['explanation_shuffle'][m]['score']['fold_stat']['mean'],
          *[a['shuffled']['explanation_shuffle'][m]['original_minus_shuffled']['fold_stat'][v] for v in ('mean','sd')],
          *[a['shuffled']['explanation_shuffle'][m]['original_minus_shuffled']['paired_replicates'][v] for v in ('sd','p025','p975')]]
         for a in p['aggregate'] for m in c.METRICS])
    lines.extend(['## All fold and question support results',''])
    table(lines,['Model','Fold','Question','Stratum','n','Metric','Original','Shuffled mean','Decrement','Permutation SD','p2.5','p97.5'],
        [[r['model'],r['fold'],'all' if r['question'] is None else r['question'],r['stratum'],r['n'],m,r['original'][m],
          r['shuffled']['explanation_shuffle'][m]['score']['mean'],
          *[r['shuffled']['explanation_shuffle'][m]['original_minus_shuffled'][v] for v in ('mean','sd','p025','p975')]]
         for r in p['records'] for m in c.METRICS])
    lines.extend(['## Paired contrasts and contribution changes',''])
    table(lines,['Stratum','Comparison','Metric','Mean delta','Fold SD','Defined folds'],
        [[r['stratum'],m,k,v['mean'],v['sd'],v['defined_folds']]
         for r in p['contrast_aggregate'] for m,metrics in r['deltas'].items() for k,v in metrics.items()]
        + [[r['stratum'],'contribution change versus E011',k,v['mean'],v['sd'],v['defined_folds']]
           for r in p['contrast_aggregate'] for k,v in r['contribution_change_from_E011'].items()])
    table(lines,['Fold','Question','Stratum','n','MAP delta versus frequency','MAP delta versus E011',
                 'Accuracy delta versus frequency','Accuracy delta versus E011','Gain change','Loss change','Net change'],
        [[r['fold'],'all' if r['question'] is None else r['question'],r['stratum'],r['n'],
          *[r['deltas'][m][k] for k in c.METRICS for m in ('frequency','E011')],
          *[r['contribution_change_from_E011'][k] for k in ('gain','loss','net')]] for r in p['contrasts']])
    lines.extend(['## Agreement and contributions versus frequency',''])
    table(lines,['Model','Fold','Question','Stratum','Top1 agreement','Top3 agreement','RR wins','RR ties','RR losses','RR gain','RR loss','RR net'],
        [[r['model'],r['fold'],'all' if r['question'] is None else r['question'],r['stratum'],
          r['agreement']['top1_agreement'],r['agreement']['ordered_top3_agreement'],
          *[r['agreement']['map_at_3'][k] for k in ('wins','ties','losses','gain','loss','net')]] for r in p['records']])
    lines.extend(['## Aggregate calibration',''])
    table(lines,['Model','Stratum','Metric','Raw mean','Final mean','Raw minus final','Paired fold SD','Eligible folds'],
        [[a['model'],a['stratum'],m,v['raw']['mean'],v['scaled']['mean'],v['raw_minus_scaled']['mean'],
          v['raw_minus_scaled']['sd'],v['raw_minus_scaled']['defined_folds']]
         for a in p['aggregate'] for m,v in a['calibration'].items()])
    lines.extend(['## Complete calibration diagnostics',''])
    table(lines,['Model','Fold','Question','Stratum','Scale','n','Correct','Accuracy','Confidence','Confidence minus accuracy','ECE','Brier','Exclusions'],
        [[r['model'],r['fold'],'all' if r['question'] is None else r['question'],r['stratum'],kind,
          *[g[k] for k in ('n','correct_n','accuracy','mean_confidence','confidence_minus_accuracy','ece','brier')],
          ', '.join(g['ineligible_reasons']) or 'eligible'] for r in p['records'] for kind,g in r['calibration'].items()])
    lines.extend(['## Probability scaling diagnostics',''])
    table(lines,['Model','Fold','Temperature','Supported calibration n','Lower boundary','Upper boundary','Raw floor fraction','Top1 changes','Top3 changes'],
        [[r[k] for k in ('model','fold','temperature','calibration_supported_n','lower_boundary','upper_boundary','raw_at_clip_floor_fraction','top1_change_fraction','ordered_top3_change_fraction')] for r in p['probability_diagnostics']])
    lines.extend(['## Review budget aggregates',''])
    table(lines,['Model','Review percent','Metric','Mean','Fold SD','Defined folds'],
        [[r['model'],r['review_percent'],m,v['mean'],v['sd'],v['defined_folds']] for r in p['routing_aggregate'] for m,v in r['metrics'].items()])
    lines.extend(['## Complete fold review results',''])
    table(lines,['Model','Fold','Review percent','Original n','Retained n','Accuracy','MAP@3','Risk','Confidence','ECE','Brier','Exclusions'],
        [[r['model'],r['fold'],b['review_percent'],*[b['all'][k] for k in ('original_n','retained_n','top1_accuracy','map_at_3','risk','mean_confidence','ece','brier')],
          ', '.join(b['all']['calibration_ineligible_reasons']) or 'eligible'] for r in p['routing'] for b in r['budgets']])
    lines.extend(['## Permutation opportunity',''])
    table(lines,['Fold','Question','n','Cells','Singleton rows','Movable rows','Label mixed rows','Label mixed share','Donor changes mean','Input changes mean'],
        [[r['fold'],'all' if r['question'] is None else r['question'],
          *[r[k] for k in ('n','cells','singleton_rows','movable_rows','label_mixed_rows','label_mixed_share')],
          r['donor_changed_n']['mean'],r['input_changed_n']['mean']] for r in p['opportunity']])
    lines.extend(['All replicate-level aggregates and full precision values are in [the aggregate artifact](../results/E014_aggregates.json). No row-level predictions are published.',''])
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
    print('E014 aggregate schema, arithmetic and completion receipt verified; numerical report published.')


if __name__=='__main__': main()


