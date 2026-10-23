"""Strict aggregate-only allowlist, arithmetic validation and complete E019 tables."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from . import e019_metrics as c
from . import e007_publication as s
from .e011_publication import same,payload_schema
from .e019_checker import REASONS,sha,write_new

E,L,NN,I,N=s.enum,s.listing,s.NN,s.I,s.N
ARM=E(*c.ARMS); STRATUM=E(*c.core.STRATA)
SCOPE={'fold':E(0,1,2,3,4),'question':s.nullable(I),'stratum':STRATUM,'n':I}
STAT={'fold_values':L(NN),'mean':NN,'sd':NN,'defined_folds':I}
EXACT={k:NN for k in c.METRICS}
CALMETRICS={k:NN for k in ('accuracy','mean_confidence','confidence_minus_accuracy','ece','brier')}
REVIEWMETRICS={k:NN for k in ('mean_confidence','confidence_minus_accuracy','ece','brier','top1_accuracy','risk','map_at_3','coverage')}
GAINMETRICS={k:NN for k in ('gain','loss','delta')}
AUDITMETRICS={k:NN for k in ('answered_share','unknown_share','predicted_false_share','predicted_true_share',
    'covered_agreement','all_row_agreement','covered_balanced_accuracy','all_row_balanced_accuracy')}
CONTROL_METRICS={k:NN for k in ('all_row_agreement','all_row_balanced_accuracy')}
REASONS_SCHEMA={k:I for k in REASONS}
ELIGIBLE={'correct_n':I,'incorrect_n':I,'ineligible_reasons':L(E('n_below_200','correct_below_20','incorrect_below_20'))}
PAIR={'left':ARM,'right':ARM}
SCALE={'scale':E('raw','final')}
RECORD={'arm':ARM,**SCOPE,'metrics':EXACT}
CAL={'arm':ARM,**SCOPE,**SCALE,**ELIGIBLE,'metrics':CALMETRICS}
REVIEW={'arm':ARM,**SCOPE,'review_percent':E(*c.BUDGETS),**ELIGIBLE,'metrics':REVIEWMETRICS}
GAIN={**PAIR,**SCOPE,'wins':I,'ties':I,'losses':I,'metrics':GAINMETRICS}
FALLBACK={'arm':E('F_A','L_A'),**SCOPE,'state':E(*c.STATES),'metrics':EXACT}
CONFUSION={'confusion_counts':L(L(I)),'confusion_row_normalized':L(L(NN))}
AUDIT={**SCOPE,**CONFUSION,'answered_n':I,'unknown_n':I,'metrics':AUDITMETRICS}
CONTROL={**SCOPE,**CONFUSION,'metrics':CONTROL_METRICS}
DIST={'n':I,'total':I,'min':s.nullable(I),'median':NN,'max':s.nullable(I)}


def summary(dimensions,metrics):
    return {**dimensions,'n_total':I,'metrics':{k:STAT for k in metrics}}


def panel():
    return {'records':L(RECORD),'aggregate':L(summary({'arm':ARM,'stratum':STRATUM},EXACT))}


SCHEMA={'experiment_id':E('E019'),'status':E('COMPLETED'),
    'development':payload_schema('E011')['development'],
    'constant_development':L({'fold':E(0,1,2,3,4),'majority_correctness':s.B,'training_counts':{'false':I,'true':I}}),
    'original_input_controls':panel(),'constant_filter_control':panel(),'automated_correctness_predictions':panel(),
    'comparisons':{'records':L({**PAIR,**SCOPE,'metrics':EXACT}),
        'aggregate':L(summary({**PAIR,'stratum':STRATUM},EXACT)),
        'decisions':{'comparisons':L({**PAIR,**STAT,'positive_folds':I,'criterion_met':s.B}),
                     'H1_conjunction_met':s.B,'H2_secondary_met':s.B}},
    'calibration':{'records':L(CAL),'aggregate':L(summary({'arm':ARM,**SCALE,'stratum':STRATUM},CALMETRICS)),
        'contrasts':L({**PAIR,**SCOPE,**SCALE,'jointly_eligible_n':I,'metrics':{'ece':NN,'brier':NN}}),
        'contrast_aggregate':L(summary({**PAIR,**SCALE,'stratum':STRATUM},('ece','brier'))),
        'final_minus_raw':L({'arm':ARM,**SCOPE,'jointly_eligible_n':I,'metrics':{'ece':NN,'brier':NN}}),
        'change_aggregate':L(summary({'arm':ARM,'stratum':STRATUM},('ece','brier')))},
    'gain_loss':{'records':L(GAIN),'aggregate':L(summary({**PAIR,'stratum':STRATUM},GAINMETRICS))},
    'fallback':{'records':L(FALLBACK),'aggregate':L(summary({'arm':ARM,'state':E(*c.STATES),'stratum':STRATUM},EXACT))},
    'review':{'records':L(REVIEW),'aggregate':L(summary({'arm':ARM,'review_percent':E(*c.BUDGETS),'stratum':STRATUM},REVIEWMETRICS)),
        'contrasts':L({**PAIR,**SCOPE,'review_percent':E(*c.BUDGETS),'jointly_eligible_n':I,'metrics':REVIEWMETRICS}),
        'contrast_aggregate':L(summary({**PAIR,'review_percent':E(*c.BUDGETS),'stratum':STRATUM},REVIEWMETRICS))},
    'correctness_audit':{'records':L(AUDIT),'aggregate':L(summary({'stratum':STRATUM},AUDITMETRICS)),
        'majority_records':L(CONTROL),'majority_aggregate':L(summary({'stratum':STRATUM},CONTROL_METRICS)),
        'pair_counts':L({'fold':E(0,1,2,3,4),'question':s.nullable(I),'distinct_pairs':I,'predicted_false':I,'predicted_true':I,'unknown':I}),
        'row_reason_counts':L({'fold':E(0,1,2,3,4),'question':s.nullable(I),'n':I,'reason_counts':REASONS_SCHEMA}),
        'pooled_confusion_counts':L(L(I)),'pooled_confusion_row_normalized':L(L(NN))},
    'resource_summary':{'pairs':I,'reason_counts':REASONS_SCHEMA,'input_tokens':DIST,'generated_tokens':DIST,
        'checker_seconds':N,'statistical_seconds':N,'solver_image_id':s.pattern('sha256:[0-9a-f]{64}'),
        'statistical_image_id':s.pattern('sha256:[0-9a-f]{64}'),'model_manifest_sha256':s.HASH,'environment_lock_sha256':s.HASH,
        'cpu_count':I,'architecture':E('x86_64'),'solver_memory_limit_bytes':E(17179869184)},
    'integrity':{'git_revision':s.pattern('[0-9a-f]{40}'),'lock_sha256':s.HASH,'cache_sha256':s.HASH,
        'frozen_development_sha256':s.HASH,'preserved_files':I,'preservation_verified':E(True),'global_freeze_verified':E(True),
        'e018_remains_blocked':E(True),'fit_warnings':E(0),'model_fits':E(50),'reproduction_model_folds':E(10),
        'row_level_outputs':E(False),'uid':E(10001),'gid':E(10001)}}


def unique(rows,keys):
    index={tuple(r[k] for k in keys):r for r in rows}
    if len(index)!=len(rows): raise ValueError('Duplicate report rows.')
    return index


def exact_rows(p):
    return sum([p[name]['records'] for name in ('original_input_controls','constant_filter_control','automated_correctness_predictions')],[])


def validate(p):
    s.validate_schema(p,SCHEMA)
    rows=exact_rows(p); index=unique(rows,('arm','fold','question','stratum'))
    qs={f:sorted({r['question'] for r in rows if r['fold']==f and r['question'] is not None}) for f in range(5)}
    if any(len(x)!=3 for x in qs.values()) or len(set(sum(qs.values(),[])))!=15: raise ValueError('Question grid changed.')
    scopes=[(f,q,t) for f in range(5) for q in [None,*qs[f]] for t in c.core.STRATA]
    if set(index)!={(a,*d) for a in c.ARMS for d in scopes}: raise ValueError('Incomplete exact grid.')
    for r in rows:
        key=(r['fold'],r['question'],r['stratum']); same(r['n'],index['F',*key]['n'])
        for k,v in r['metrics'].items():
            if (v is None)!=(r['n']==0) or v is not None and not 0<=v<=1: raise ValueError('Invalid metric.')
            if r['stratum']=='unsupported' and r['n'] and v!=0: raise ValueError('Unsupported labels scored.')
        if r['question'] is None:
            parts=[index[r['arm'],r['fold'],q,r['stratum']] for q in qs[r['fold']]]
        elif r['stratum']=='all':
            parts=[index[r['arm'],r['fold'],r['question'],t] for t in ('unsupported','rare','frequent')]
        else: continue
        same(r['n'],sum(x['n'] for x in parts))
        for k in c.METRICS:
            same(r['metrics'][k],sum(x['n']*x['metrics'][k] for x in parts if x['n'])/r['n'] if r['n'] else None)
    if sum(index['F',f,None,'all']['n'] for f in range(5))!=36696: raise ValueError('Population changed.')
    calindex=unique(p['calibration']['records'],('arm','fold','question','stratum','scale'))
    if set(calindex)!={(a,*d,scale) for a in c.ARMS for d in scopes for scale in ('raw','final')}: raise ValueError('Calibration grid.')
    for r in [*p['calibration']['records'],*p['review']['records']]:
        n=r['n']; correct=r['correct_n']; errors=r['incorrect_n']; same(n,correct+errors)
        if correct>n or errors>n: raise ValueError('Correctness counts.')
        reasons=[]
        if n<200: reasons.append('n_below_200')
        if correct<20: reasons.append('correct_below_20')
        if errors<20: reasons.append('incorrect_below_20')
        same(reasons,r['ineligible_reasons'])
        for metric in ('ece','brier'):
            if (r['metrics'][metric] is None)!=bool(reasons): raise ValueError('Eligibility changed.')
        acc=r['metrics'].get('accuracy',r['metrics'].get('top1_accuracy'))
        same(acc,correct/n if n else None)
        same(r['metrics']['confidence_minus_accuracy'],r['metrics']['mean_confidence']-acc if n else None)
        if r.get('scale')=='final': same(acc,index[r['arm'],r['fold'],r['question'],r['stratum']]['metrics']['top1_accuracy'])
    routing=unique(p['review']['records'],('arm','fold','review_percent'))
    if set(routing)!={(a,f,b) for a in c.ARMS for f in range(5) for b in c.BUDGETS}: raise ValueError('Review grid.')
    for (a,f,b),r in routing.items():
        n=index[a,f,None,'all']['n']; same(r['n'],n-n*b//100); same(r['metrics']['coverage'],r['n']/n)
        same(r['metrics']['risk'],1-r['metrics']['top1_accuracy'])
        if b==0:
            for k in c.METRICS: same(r['metrics'][k],index[a,f,None,'all']['metrics'][k])
    paired=unique(p['comparisons']['records'],('left','right','fold','question','stratum'))
    gainindex=unique(p['gain_loss']['records'],('left','right','fold','question','stratum'))
    if set(gainindex)!={(a,b,*d) for a,b in c.GAIN_PAIRS for d in scopes}: raise ValueError('Gain grid.')
    for key,r in gainindex.items():
        same(r['n'],r['wins']+r['ties']+r['losses'])
        if r['n']:
            same(r['metrics']['gain']+r['metrics']['loss'],r['metrics']['delta'])
            same(r['metrics']['delta'],paired[key]['metrics']['map_at_3'])
            if r['metrics']['gain']<0 or r['metrics']['loss']>0: raise ValueError('Signed gain/loss convention.')
    fall=unique(p['fallback']['records'],('arm','fold','question','state'))
    if set(fall)!={(a,f,q,st) for a in ('F_A','L_A') for f in range(5) for q in [None,*qs[f]] for st in c.STATES}: raise ValueError('Fallback grid.')
    for a in ('F_A','L_A'):
        for f in range(5):
            for q in [None,*qs[f]]:
                parts=[fall[a,f,q,st] for st in c.STATES]; n=index[a,f,q,'all']['n']
                same(sum(x['n'] for x in parts),n)
                for st in c.STATES: same(fall['F_A',f,q,st]['n'],fall['L_A',f,q,st]['n'])
                for metric in c.METRICS: same(index[a,f,q,'all']['metrics'][metric],sum(x['n']*x['metrics'][metric] for x in parts if x['n'])/n)
    rebuilt=c.build_panels(rows,p['calibration']['records'],p['gain_loss']['records'],p['fallback']['records'],p['review']['records'])
    for key,value in rebuilt.items(): same(p[key],value)
    audit=p['correctness_audit']; ai=unique(audit['records'],('fold','question'))
    if set(ai)!={(f,q) for f in range(5) for q in [None,*qs[f]]}: raise ValueError('Correctness grid.')
    for (f,q),r in ai.items():
        cm=np.asarray(r['confusion_counts'])
        if cm.shape!=(2,3) or int(cm.sum())!=r['n']: raise ValueError('Correctness confusion shape/count.')
        same(r['n'],index['F',f,q,'all']['n'])
        truth=np.repeat([False,True],cm.sum(axis=1))
        signal=np.concatenate([np.repeat([0,1,-1],row) for row in cm])
        same(r,c.audit_record(f,q,truth,signal))
        if q is None: same(cm.tolist(),np.sum([ai[f,x]['confusion_counts'] for x in qs[f]],axis=0).tolist())
    same(audit['aggregate'],c.summarize(audit['records'],('stratum',)))
    same(audit['majority_aggregate'],c.summarize(audit['majority_records'],('stratum',)))
    same(audit['pooled_confusion_counts'],np.sum([ai[f,None]['confusion_counts'] for f in range(5)],axis=0).tolist())
    pooled=np.asarray(audit['pooled_confusion_counts'])
    same(audit['pooled_confusion_row_normalized'],[[float(x/row.sum()) if row.sum() else None for x in row] for row in pooled])
    majority=unique(audit['majority_records'],('fold','question'))
    pair_counts=unique(audit['pair_counts'],('fold','question'))
    reason_counts=unique(audit['row_reason_counts'],('fold','question'))
    if any(set(x)!=set(ai) for x in (majority,pair_counts,reason_counts)): raise ValueError('Incomplete correctness audit.')
    constants=unique(p['constant_development'],('fold',))
    if set(constants)!={(f,) for f in range(5)}: raise ValueError('Constant development grid.')
    for (f,q),row in majority.items():
        cm=np.asarray(row['confusion_counts']); base=np.asarray(ai[f,q]['confusion_counts'])
        if cm.shape!=(2,2): raise ValueError('Constant confusion shape.')
        same(cm.sum(axis=1).tolist(),base.sum(axis=1).tolist())
        same(row['n'],int(cm.sum()))
        const=int(constants[f,]['majority_correctness'])
        if np.any(cm[:,1-const]): raise ValueError('Nonconstant control audit.')
        same(row['metrics']['all_row_agreement'],float(np.trace(cm)/row['n']))
        den=cm.sum(axis=1)
        same(row['metrics']['all_row_balanced_accuracy'],float(np.mean(np.diag(cm)/den)) if np.all(den>0) else None)
        same(row['confusion_row_normalized'],[[float(v/r.sum()) if r.sum() else None for v in r] for r in cm])
    for (f,q),row in pair_counts.items():
        same(row['distinct_pairs'],row['predicted_false']+row['predicted_true']+row['unknown'])
        if row['distinct_pairs']>ai[f,q]['n']: raise ValueError('Pair counts exceed rows.')
    for (f,q),row in reason_counts.items():
        same(row['n'],sum(row['reason_counts'].values())); same(row['n'],ai[f,q]['n'])
        same(row['reason_counts']['false']+row['reason_counts']['true'],ai[f,q]['answered_n'])
        if q is None:
            for reason in REASONS: same(row['reason_counts'][reason],sum(reason_counts[f,x]['reason_counts'][reason] for x in qs[f]))
    same(p['resource_summary']['pairs'],sum(p['resource_summary']['reason_counts'].values()))
    for r in p['constant_development']:
        same(r['majority_correctness'],r['training_counts']['true']>r['training_counts']['false'])
    return p


def value(x):
    if x is None: return 'null'
    if isinstance(x,float): return f'{x:.6f}'
    if isinstance(x,(dict,list)): return json.dumps(x,separators=(',',':'))
    return str(x)


def table(lines,rows):
    if not rows: return
    flattened=[]
    def flatten(obj,prefix=''):
        result={}
        for key,x in obj.items():
            name=prefix+key
            if isinstance(x,dict): result.update(flatten(x,name+'.'))
            else: result[name]=x
        return result
    flattened=[flatten(r) for r in rows]; columns=list(flattened[0])
    if any(list(r)!=columns for r in flattened): raise ValueError('Table column inconsistency.')
    lines.extend(['| '+' | '.join(columns)+' |','|'+'|'.join(['---']*len(columns))+'|'])
    for row in flattened: lines.append('| '+' | '.join(value(row[k]).replace('|','\\|') for k in columns)+' |')
    lines.append('')


def render(p):
    validate(p)
    lines=['# E019 numerical results','',
        'Results only; interpretation awaits user review. F: ordinary frequency; L: historical E011; F_M: training-majority correctness filter; F_A and L_A: automated correctness filter. The checker is fallible, not independently verified. All five-fold summaries are descriptive; E018 remains blocked.','']
    panels=('original_input_controls','constant_filter_control','automated_correctness_predictions')
    rows=exact_rows(p)
    lines.extend(['## Aggregate results (equal five-fold means)',''])
    table(lines,[r for name in panels for r in p[name]['aggregate'] if r['stratum']=='all'])
    lines.extend(['## Fold-level results',''])
    table(lines,[r for r in rows if r['question'] is None and r['stratum']=='all'])
    lines.extend(['## Registered paired results and Boolean criteria',''])
    table(lines,[r for r in p['comparisons']['aggregate'] if r['stratum']=='all'])
    table(lines,[r for r in p['comparisons']['records'] if r['question'] is None and r['stratum']=='all'])
    table(lines,p['comparisons']['decisions']['comparisons'])
    lines.extend([f"H1 conjunction: {p['comparisons']['decisions']['H1_conjunction_met']}; H2 secondary: {p['comparisons']['decisions']['H2_secondary_met']}.",''])
    # Every registered record and summary, not favorable examples.
    for name in (*panels,'comparisons','calibration','gain_loss','fallback','review','correctness_audit'):
        lines.extend(['## '+name.replace('_',' ').title(),''])
        for key,content in p[name].items():
            if isinstance(content,list) and content and isinstance(content[0],dict):
                lines.extend(['### '+key.replace('_',' ').title(),'']); table(lines,content)
            elif key.startswith('pooled_'):
                lines.extend([key+': `'+json.dumps(content)+'`',''])
    lines.extend(['## Historical development selections','']); table(lines,p['development'])
    lines.extend(['## Training-majority controls','']); table(lines,p['constant_development'])
    for key in ('resource_summary','integrity'):
        lines.extend(['## '+key.replace('_',' ').title(),'']); table(lines,[p[key]])
    lines.extend(['Full precision: [aggregate JSON](../results/E019_aggregates.json). All assessment inputs, completions, pair mappings and row predictions remain private.',''])
    return '\n'.join(lines)


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--json',type=Path,required=True); parser.add_argument('--markdown',type=Path,required=True)
    args=parser.parse_args(); p=json.loads(args.source.read_text()); validate(p)
    receipt=json.loads((args.source.parent/'execution.json').read_text())
    if receipt['status']!='COMPLETED' or receipt['results_sha256']!=sha(args.source): raise ValueError('Completion receipt mismatch.')
    if args.json.exists() or args.markdown.exists(): raise ValueError('Do not overwrite results.')
    rendered=render(p); write_new(args.json,p)
    with args.markdown.open('x',encoding='utf-8',newline='\n') as f: f.write(rendered)
    print('E019 complete aggregate-only schema and arithmetic verified; all tables published.')


if __name__=='__main__': main()
