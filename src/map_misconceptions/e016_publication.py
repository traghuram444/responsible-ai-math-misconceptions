"""Strict aggregate-only E016 publication and independent arithmetic verification."""
from __future__ import annotations
import argparse
from copy import deepcopy
import json
from pathlib import Path
import numpy as np
from . import e007_publication as s
from . import e013_publication as previous
from . import e016 as c
from .e011_publication import payload_schema, same, STAT, GROUP, CATEGORY, check_group
from .e013_publication import check_repetition, check_cal, table, fmt
from .e014_publication import check_selection
from .data_contract import file_sha256
from .e006 import write_new

N,I,NN,B=s.N,s.I,s.NN,s.B
L,E=s.listing,s.enum
MODEL=E(*c.MODELS)
RECORD=deepcopy(previous.RECORD)
RECORD['model']=MODEL
RECORD['shuffled']={'explanation_shuffle':RECORD['shuffled']['explanation_shuffle']}
AGG=deepcopy(previous.AGG)
AGG['model']=MODEL
AGG['shuffled']={'explanation_shuffle':AGG['shuffled']['explanation_shuffle']}
OPPORTUNITY={**previous.OPPORTUNITY,'condition':E('explanation_shuffle')}
DIAGNOSTIC={**previous.DIAGNOSTIC,'model':MODEL,'n':I,'top1_change_n':I,'ordered_top3_change_n':I}
DEVELOPMENT={**payload_schema('E011')['development'][1],'learning_arm':E(*c.ARMS)}
SCOPE={'fold':E(0,1,2,3,4),'question':s.nullable(I),'stratum':E(*c.core.STRATA),'n':I}
CONTRAST={**SCOPE,'left':MODEL,'right':MODEL,'deltas':{m:NN for m in c.METRICS},
    'calibration_deltas':{k:{m:NN for m in ('ece','brier')} for k in ('raw','scaled')}}
CONTRAST_AGG={'left':MODEL,'right':MODEL,'stratum':E(*c.core.STRATA),'deltas':{m:STAT for m in c.METRICS},
    'calibration_deltas':{k:{m:STAT for m in ('ece','brier')} for k in ('raw','scaled')}}
ROUTE={'model':MODEL,'fold':E(0,1,2,3,4),'budgets':L({'review_percent':E(0,10,20,30,40,50),'all':GROUP})}
ROUTE_AGG={'model':MODEL,'review_percent':E(0,10,20,30,40,50),
    'metrics':{m:STAT for m in ('original_n','retained_n','top1_accuracy','map_at_3','risk','mean_confidence','ece','brier')}}
CAT={'model':MODEL,'fold':E(0,1,2,3,4),'question':s.nullable(I),'scale':E(*c.SCALES),**CATEGORY}
CAT_AGG={'model':MODEL,'scale':E(*c.SCALES),'accuracy':STAT,'macro_f1_six':STAT}
CAT_CONTRAST={'left':MODEL,'right':MODEL,'fold':E(0,1,2,3,4),'question':s.nullable(I),'scale':E(*c.SCALES),
              'n':I,'deltas':{'accuracy':N,'macro_f1_six':N}}
CAT_CONTRAST_AGG={'left':MODEL,'right':MODEL,'scale':E(*c.SCALES),'accuracy':STAT,'macro_f1_six':STAT}
SCHEMA={'experiment_id':E('E016'),'status':E('COMPLETED'),'development':L(DEVELOPMENT),
    'records':L(RECORD),'aggregate':L(AGG),'primary':{**STAT,'positive_folds':I,'criterion_met':B},
    'contrasts':L(CONTRAST),'contrast_aggregate':L(CONTRAST_AGG),'opportunity':L(OPPORTUNITY),
    'probability_diagnostics':L(DIAGNOSTIC),'routing':L(ROUTE),'routing_aggregate':L(ROUTE_AGG),
    'category':L(CAT),'category_aggregate':L(CAT_AGG),'category_contrasts':L(CAT_CONTRAST),
    'category_contrast_aggregate':L(CAT_CONTRAST_AGG),
    'provenance':{**previous.SCHEMA['provenance'],'model_fits':E(100),'reproduction_model_folds':E(5)}}


def validate(p):
    s.validate_schema(p,SCHEMA)
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


    if len(p['development'])!=10 or {(d['learning_arm'],d['fold']) for d in p['development']}!={(a,f) for a in c.ARMS for f in range(5)}:
        raise ValueError('Development grid.')
    for d in p['development']:
        same(d['arm'],'full_context'); same(d['model'],'logistic'); same(d['role_question_counts'],[9,3,3])
        check_selection(d['selection'],[{**g,'ngram_range':list(g['ngram_range'])} for g in c.core.e001.GRID],'params')
        if not np.exp(-3)<=d['temperature']<=np.exp(3) or not 0<=d['calibration_supported_n']<=d['n_calibration']:
            raise ValueError('Temperature/support contract.')
        for model in ([d['learning_arm'],'frequency'] if d['learning_arm']=='E011' else [d['learning_arm']]):
            diag=next(x for x in p['probability_diagnostics'] if x['model']==model and x['fold']==d['fold'])
            t=1. if model=='frequency' else d['temperature']
            same(diag['temperature'],t); same(diag['calibration_supported_n'],d['calibration_supported_n'])
            same(diag['lower_boundary'],bool(abs(np.log(t)+3)<=1e-5))
            same(diag['upper_boundary'],bool(abs(np.log(t)-3)<=1e-5))
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

    reference={(r['model'],r['fold'],r['question']):r for r in rows if r['stratum']=='all'}
    catkeys=[(r['model'],r['fold'],r['question'],r['scale']) for r in p['category']]
    expected={(m,f,q,scale) for m,f,q in reference for scale in c.SCALES}
    if len(catkeys)!=120 or set(catkeys)!=expected: raise ValueError('Category grid.')
    for row in p['category']:
        same(row['n'],reference[row['model'],row['fold'],row['question']]['n'])
        if not all(0<=row[k]<=1 for k in ('accuracy','macro_f1_six')): raise ValueError('Category range.')
        if row['question'] is None:
            parts=[r for r in p['category'] if r['model']==row['model'] and r['fold']==row['fold']
                   and r['scale']==row['scale'] and r['question'] is not None]
            same(row['accuracy'],sum(r['n']*r['accuracy'] for r in parts)/row['n'])
    same(p['category_aggregate'],c.category_summary(p['category']))
    same(p['category_contrasts'],c.category_contrasts(p['category']))
    same(p['category_contrast_aggregate'],c.category_contrast_summary(p['category_contrasts']))
    diagnostic_keys=[(r['model'],r['fold']) for r in p['probability_diagnostics']]
    if set(diagnostic_keys)!={(m,f) for m in c.MODELS for f in range(5)}: raise ValueError('Probability grid.')
    for row in p['probability_diagnostics']:
        same(row['n'],reference[row['model'],row['fold'],None]['n'])
        for name in ('top1','ordered_top3'):
            count=row[name+'_change_n']
            if not 0<=count<=row['n']: raise ValueError('Rank change counts.')
            same(row[name+'_change_fraction'],count/row['n'])



def render(p):
    validate(p)
    lines=['# E016 numerical results','',
        'Equal-fold and permutation summaries are descriptive only. Numerical results precede interpretation.','',
        'Factorized: direct Category learning with within-Category frequency (primary); E011: unchanged flat classifier; frequency: unchanged baseline.','',
        '## Aggregate exact label performance','']
    table(lines,['Model','MAP@3','Fold SD','Accuracy','Explanation shuffled MAP@3','Explanation decrement'],
        [[a['model'],a['original']['map_at_3']['mean'],a['original']['map_at_3']['sd'],
          a['original']['top1_accuracy']['mean'],a['shuffled']['explanation_shuffle']['map_at_3']['score']['fold_stat']['mean'],
          a['shuffled']['explanation_shuffle']['map_at_3']['original_minus_shuffled']['fold_stat']['mean']]
         for a in p['aggregate'] if a['stratum']=='all'])
    lines.extend(['## Primary comparison and complete fold results',''])
    h=p['primary']
    table(lines,['Comparison','Delta mean','Fold SD','Positive folds','Criterion met'],
        [['Factorized minus frequency',h['mean'],h['sd'],str(h['positive_folds'])+'/5',h['criterion_met']]])
    table(lines,['Fold','Factorized MAP@3','E011 MAP@3','Frequency MAP@3','Factorized minus frequency'],
        [[f,*[next(r['original']['map_at_3'] for r in p['records'] if r['model']==m and r['fold']==f
                  and r['question'] is None and r['stratum']=='all') for m in c.MODELS],h['fold_values'][f]] for f in range(5)])
    lines.extend(['## Complete inner development selection',''])
    table(lines,['Arm','Fold','Candidate','Settings','Inner 0','Inner 1','Inner 2','Mean','Selected'],
        [[d['learning_arm'],d['fold'],i,json.dumps(x['params'],sort_keys=True),*x['inner_fold_map_at_3'],
          x['inner_mean_map_at_3'],i==d['selection']['selected_index']]
         for d in p['development'] for i,x in enumerate(d['selection']['candidates'])])
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

    lines.extend(['## Fixed paired contrasts',''])
    table(lines,['Left','Right','Stratum','Metric','Mean delta','Fold SD','Defined folds'],
        [[r['left'],r['right'],r['stratum'],m,v['mean'],v['sd'],v['defined_folds']]
         for r in p['contrast_aggregate'] for m,v in r['deltas'].items()])
    table(lines,['Left','Right','Fold','Question','Stratum','n','MAP delta','Accuracy delta'],
        [[r['left'],r['right'],r['fold'],r['question'],r['stratum'],r['n'],
          r['deltas']['map_at_3'],r['deltas']['top1_accuracy']] for r in p['contrasts']])
    lines.extend(['## Jointly eligible between arm calibration differences',''])
    table(lines,['Left','Right','Stratum','Scale','Metric','Mean delta','Fold SD','Eligible folds'],
        [[r['left'],r['right'],r['stratum'],kind,m,v['mean'],v['sd'],v['defined_folds']]
         for r in p['contrast_aggregate'] for kind,items in r['calibration_deltas'].items() for m,v in items.items()])
    table(lines,['Left','Right','Fold','Question','Stratum','Scale','ECE delta','Brier delta'],
        [[r['left'],r['right'],r['fold'],r['question'],r['stratum'],kind,v['ece'],v['brier']]
         for r in p['contrasts'] for kind,v in r['calibration_deltas'].items()])
    lines.extend(['## Category aggregates and paired comparisons','',
        'Raw direct Category accuracy is the designated H2 comparison; final Category probabilities are marginalized after exact-label calibration.',''])
    table(lines,['Model','Scale','Metric','Mean','Fold SD','Defined folds'],
        [[r['model'],r['scale'],metric,r[metric]['mean'],r[metric]['sd'],r[metric]['defined_folds']]
         for r in p['category_aggregate'] for metric in ('accuracy','macro_f1_six')])
    table(lines,['Left','Right','Scale','Metric','Mean delta','Fold SD','Defined folds'],
        [[r['left'],r['right'],r['scale'],metric,r[metric]['mean'],r[metric]['sd'],r[metric]['defined_folds']]
         for r in p['category_contrast_aggregate'] for metric in ('accuracy','macro_f1_six')])
    lines.extend(['## Complete Category results',''])
    table(lines,['Model','Fold','Question','Scale','n','Accuracy','Fixed six label macro F1'],
        [[r[k] for k in ('model','fold','question','scale','n','accuracy','macro_f1_six')] for r in p['category']])
    table(lines,['Left','Right','Fold','Question','Scale','n','Accuracy delta','Macro F1 delta'],
        [[*[r[k] for k in ('left','right','fold','question','scale','n')],r['deltas']['accuracy'],r['deltas']['macro_f1_six']]
         for r in p['category_contrasts']])
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
    table(lines,['Model','Fold','Temperature','Supported calibration n','Lower boundary','Upper boundary','Raw floor fraction','n','Top1 change count','Top3 change count','Top1 change rate','Top3 change rate'],
        [[r[k] for k in ('model','fold','temperature','calibration_supported_n','lower_boundary','upper_boundary','raw_at_clip_floor_fraction','n','top1_change_n','ordered_top3_change_n','top1_change_fraction','ordered_top3_change_fraction')] for r in p['probability_diagnostics']])
    lines.extend(['## Review budget aggregates',''])
    table(lines,['Model','Review percent','Metric','Mean','Fold SD','Defined folds'],
        [[r['model'],r['review_percent'],m,v['mean'],v['sd'],v['defined_folds']] for r in p['routing_aggregate'] for m,v in r['metrics'].items()])
    lines.extend(['## Complete fold review results',''])
    table(lines,['Model','Fold','Review percent','Original n','Retained n','Accuracy','MAP@3','Risk','Confidence','ECE','Brier','Exclusions'],
        [[r['model'],r['fold'],b['review_percent'],*[b['all'][k] for k in ('original_n','retained_n','top1_accuracy','map_at_3','risk','mean_confidence','ece','brier')],
          ', '.join(b['all']['calibration_ineligible_reasons']) or 'eligible'] for r in p['routing'] for b in r['budgets']])
    lines.extend(['## Permutation opportunity',''])
    table(lines,['Fold','Question','n','Cells','Singleton rows','Movable rows','Label mixed rows','Label mixed share','Donor changes mean','Donor changes SD','Input changes mean','Input changes SD'],
        [[r['fold'],'all' if r['question'] is None else r['question'],
          *[r[k] for k in ('n','cells','singleton_rows','movable_rows','label_mixed_rows','label_mixed_share')],
          r['donor_changed_n']['mean'],r['donor_changed_n']['sd'],r['input_changed_n']['mean'],r['input_changed_n']['sd']] for r in p['opportunity']])
    lines.extend(['All replicate-level aggregates and full precision values are in [the aggregate artifact](../results/E016_aggregates.json). No row-level predictions are published.',''])
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
    print('E016 aggregate schema, arithmetic and completion receipt verified; numerical report published.')


if __name__=='__main__': main()
