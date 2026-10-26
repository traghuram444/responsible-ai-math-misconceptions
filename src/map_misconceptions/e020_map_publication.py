"""Strict aggregate-only E020 MAP schema, consistency checks and full tables."""
import json
from pathlib import Path
import numpy as np
from . import e007_publication as s,e019_publication as prior,e020_map_metrics as m
from .e020_checker import REASONS
from .e020_fusion import WEIGHTS
from .e011_publication import same,payload_schema

E,L,I,N,NN=s.enum,s.listing,s.I,s.N,s.NN
ARM=E(*m.ARMS); MODEL=E('G15','G7'); FOLD=E(0,1,2,3,4)
def lift(value):
    if isinstance(value,dict): return {k:lift(v) for k,v in value.items()}
    if isinstance(value,tuple): return ARM if value==prior.ARM else tuple(lift(v) for v in value)
    return value
RECORD=lift(prior.RECORD); CAL=lift(prior.CAL); REVIEW=lift(prior.REVIEW); GAIN=lift(prior.GAIN)
PAIR={'left':ARM,'right':ARM}; SCOPE=prior.SCOPE; STRATUM=prior.STRATUM; SCALE=prior.SCALE
RANK={'arm':E('L','B','G15','G7','L7','H'),**SCOPE,'top1_changed_n':I,'top3_changed_n':I,
    'metrics':{'top1_changed_share':NN,'top3_changed_share':NN}}
AUDIT={'model':MODEL,**prior.AUDIT}
DIST={'n':I,'total':N,'min':NN,'median':NN,'mean':NN,'max':NN}
WEIGHT_CANDIDATE={'weights':L(N),'inner_fold_map_at_3':L(N),'inner_mean_map_at_3':N}
WEIGHT_CHOICE={'selected_index':I,'selected_weights':L(N),'candidates':L(WEIGHT_CANDIDATE)}
ENSEMBLE={'fold':FOLD,'weights':{k:WEIGHT_CHOICE for k in ('B','H')},
    'calibration':{a:{'temperature':N,'supported_n':I,'method':E('unscaled','own_temperature','all_unknown_frequency','component_endpoint')} for a in m.ARMS},
    'majority_correctness':s.B,'training_counts':{'false':I,'true':I}}
def summary(dimensions,metrics): return prior.summary(dimensions,metrics)
def panel(record,dims): return {'records':L(record),'aggregate':L(summary(dims,record['metrics']))}
SCHEMA={'experiment_id':E('E020'),'status':E('COMPLETED'),
    'development':payload_schema('E011')['development'],'ensemble_development':L(ENSEMBLE),
    'exact':panel(RECORD,{'arm':ARM,'stratum':STRATUM}),
    'comparisons':{**panel({**PAIR,**SCOPE,'metrics':prior.EXACT},{**PAIR,'stratum':STRATUM}),
        'decisions':{'comparisons':L({**PAIR,**prior.STAT,'positive_folds':I,'criterion_met':s.B}),
            **{k:s.B for k in ('H1_primary','H2_secondary','H3_secondary','H4_secondary')}}},
    'calibration':{**panel(CAL,{'arm':ARM,**SCALE,'stratum':STRATUM}),
        'contrasts':L({**PAIR,**SCOPE,**SCALE,'jointly_eligible_n':I,'metrics':{'ece':NN,'brier':NN}}),
        'contrast_aggregate':L(summary({**PAIR,**SCALE,'stratum':STRATUM},('ece','brier'))),
        'final_minus_raw':L({'arm':ARM,**SCOPE,'jointly_eligible_n':I,'metrics':{'ece':NN,'brier':NN}}),
        'change_aggregate':L(summary({'arm':ARM,'stratum':STRATUM},('ece','brier')))},
    'gain_loss':panel(GAIN,{**PAIR,'stratum':STRATUM}),
    'rank_changes':panel(RANK,{'arm':RANK['arm'],'stratum':STRATUM}),
    'review':{**panel(REVIEW,{'arm':ARM,'review_percent':E(*m.BUDGETS),'stratum':STRATUM}),
        'contrasts':L({**PAIR,**SCOPE,'review_percent':E(*m.BUDGETS),'jointly_eligible_n':I,'metrics':prior.REVIEWMETRICS}),
        'contrast_aggregate':L(summary({**PAIR,'review_percent':E(*m.BUDGETS),'stratum':STRATUM},prior.REVIEWMETRICS))},
    'correctness_audit':{'records':L(AUDIT),'aggregate':L(summary({'model':MODEL,'stratum':STRATUM},prior.AUDITMETRICS)),
        'majority_records':L(prior.AUDIT),'majority_aggregate':L(summary({'stratum':STRATUM},prior.AUDITMETRICS)),
        'pair_counts':L({'model':MODEL,'fold':FOLD,'question':s.nullable(I),'distinct_pairs':I,'predicted_false':I,'predicted_true':I,'unknown':I}),
        'row_reason_counts':L({'model':MODEL,'fold':FOLD,'question':s.nullable(I),'n':I,'reason_counts':{r:I for r in REASONS}}),
        'projection_fallback':L({'model':MODEL,'fold':FOLD,'question':s.nullable(I),'n':I,
            'missing_false_inventory':s.B,'missing_true_inventory':s.B,'false_projection_fallback_n':I,'true_projection_fallback_n':I}),
        'pooled_confusion':L({'model':MODEL,**prior.CONFUSION})},
    'resource_summary':{'checkers':L({'model':MODEL,'pairs':E(60),'reason_counts':{r:I for r in REASONS},
        'truncated_rationales':I,'input_tokens':DIST,'generated_tokens':DIST,'readout_tokens':DIST,'candidate_mass':DIST,
        'generation_seconds':N,'readout_seconds':N,'checker_seconds':N,'peak_rss_bytes':I,'container_peak_bytes':s.nullable(I)}),
        'statistical_seconds':N,'solver_image_id':s.pattern('sha256:[0-9a-f]{64}'),'statistical_image_id':s.pattern('sha256:[0-9a-f]{64}'),
        'environment_lock_sha256':s.HASH,'solver_memory_limit_bytes':E(25769803776)},
    'integrity':{'git_revision':s.pattern('[0-9a-f]{40}'),'lock_sha256':s.HASH,'readiness_result_sha256':s.HASH,
        'cache_sha256':{key:s.HASH for key in ('G15','G7')},'frozen_development_sha256':s.HASH,
        'preserved_files':E(664),'preservation_verified':E(True),'global_freeze_verified':E(True),'e018_remains_blocked':E(True),
        'fit_warnings':E(0),'model_fits':E(50),'reproduction_model_folds':E(15),'row_level_outputs':E(False),'uid':E(10001),'gid':E(10001)}}


def validate(p):
    s.validate_schema(p,SCHEMA)
    rows=p['exact']['records']; index=prior.unique(rows,('arm','fold','question','stratum'))
    qs={f:sorted({r['question'] for r in rows if r['fold']==f and r['question'] is not None}) for f in range(5)}
    if any(len(x)!=3 for x in qs.values()) or len(set(sum(qs.values(),[])))!=15: raise ValueError('Question grid changed.')
    scopes=[(f,q,t) for f in range(5) for q in [None,*qs[f]] for t in m.STRATA]
    if set(index)!={(a,*d) for a in m.ARMS for d in scopes}: raise ValueError('Incomplete exact grid.')
    for r in rows:
        key=(r['fold'],r['question'],r['stratum']); same(r['n'],index['F',*key]['n'])
        for v in r['metrics'].values():
            if (v is None)!=(r['n']==0) or v is not None and not 0<=v<=1: raise ValueError('Invalid exact metric.')
            if r['stratum']=='unsupported' and r['n'] and v!=0: raise ValueError('Unsupported label scored.')
        if r['stratum']=='well_supported' and r['n']>index[r['arm'],r['fold'],r['question'],'frequent']['n']:
            raise ValueError('Support nesting changed.')
        if r['question'] is None: parts=[index[r['arm'],r['fold'],q,r['stratum']] for q in qs[r['fold']]]
        elif r['stratum']=='all': parts=[index[r['arm'],r['fold'],r['question'],t] for t in ('unsupported','rare','frequent')]
        else: continue
        same(r['n'],sum(x['n'] for x in parts))
        for k in m.old.METRICS: same(r['metrics'][k],sum(x['n']*x['metrics'][k] for x in parts if x['n'])/r['n'] if r['n'] else None)
    if sum(index['F',f,None,'all']['n'] for f in range(5))!=36696: raise ValueError('Population changed.')
    ci=prior.unique(p['calibration']['records'],('arm','fold','question','stratum','scale'))
    if set(ci)!={(a,*d,scale) for a in m.ARMS for d in scopes for scale in ('raw','final')}: raise ValueError('Calibration grid.')
    for r in [*p['calibration']['records'],*p['review']['records']]:
        n=r['n']; correct=r['correct_n']; errors=r['incorrect_n']; same(n,correct+errors)
        if 'scale' in r: same(n,index[r['arm'],r['fold'],r['question'],r['stratum']]['n'])
        reasons=[]
        if n<200: reasons.append('n_below_200')
        if correct<20: reasons.append('correct_below_20')
        if errors<20: reasons.append('incorrect_below_20')
        same(reasons,r['ineligible_reasons'])
        for key in ('ece','brier'):
            v=r['metrics'][key]
            if (v is None)!=bool(reasons) or v is not None and not -1e-12<=v<=(2 if key=='brier' else 1)+1e-12: raise ValueError('Calibration eligibility/range.')
        acc=r['metrics'].get('accuracy',r['metrics'].get('top1_accuracy'))
        same(acc,correct/n if n else None)
        confidence=r['metrics']['mean_confidence']
        if (confidence is None)!=(n==0) or confidence is not None and not 0<=confidence<=1+1e-12: raise ValueError('Confidence range.')
        same(r['metrics']['confidence_minus_accuracy'],r['metrics']['mean_confidence']-acc if n else None)
        if r.get('scale')=='final': same(acc,index[r['arm'],r['fold'],r['question'],r['stratum']]['metrics']['top1_accuracy'])
    routing=prior.unique(p['review']['records'],('arm','fold','review_percent'))
    if set(routing)!={(a,f,b) for a in m.ARMS for f in range(5) for b in m.BUDGETS}: raise ValueError('Review grid.')
    for (a,f,b),r in routing.items():
        n=index[a,f,None,'all']['n']; same(r['n'],n-n*b//100); same(r['metrics']['coverage'],r['n']/n)
        same(r['metrics']['risk'],1-r['metrics']['top1_accuracy'])
        if b==0:
            for k in m.old.METRICS: same(r['metrics'][k],index[a,f,None,'all']['metrics'][k])
    paired=prior.unique(p['comparisons']['records'],('left','right','fold','question','stratum'))
    gains=prior.unique(p['gain_loss']['records'],('left','right','fold','question','stratum'))
    if set(gains)!={(a,b,*d) for a,b in m.GAIN_PAIRS for d in scopes}: raise ValueError('Gain grid.')
    for key,r in gains.items():
        same(r['n'],r['wins']+r['ties']+r['losses'])
        same(r['n'],index[r['left'],r['fold'],r['question'],r['stratum']]['n'])
        if any((v is None)!=(r['n']==0) for v in r['metrics'].values()): raise ValueError('Empty gain/loss cell.')
        if r['n']:
            same(r['metrics']['gain']+r['metrics']['loss'],r['metrics']['delta']); same(r['metrics']['delta'],paired[key]['metrics']['map_at_3'])
            if r['metrics']['gain']<0 or r['metrics']['loss']>0: raise ValueError('Signed gain/loss changed.')
    ranks=prior.unique(p['rank_changes']['records'],('arm','fold','question','stratum'))
    if set(ranks)!={(a,*d) for a in ('L','B','G15','G7','L7','H') for d in scopes}: raise ValueError('Rank-change grid.')
    for r in ranks.values():
        same(r['n'],index[r['arm'],r['fold'],r['question'],r['stratum']]['n'])
        for key in ('top1','top3'):
            count=r[key+'_changed_n']
            if count>r['n']: raise ValueError('Rank-change count.')
            same(r['metrics'][key+'_changed_share'],count/r['n'] if r['n'] else None)
    rebuilt=m.build_panels(rows,p['calibration']['records'],p['gain_loss']['records'],p['review']['records'],p['rank_changes']['records'])
    for key,value in rebuilt.items(): same(p[key],value)
    validate_development(p)
    validate_audit(p,index,qs)
    for r in p['resource_summary']['checkers']:
        same(sum(r['reason_counts'].values()),60)
        if any(r[k]<0 for k in ('generation_seconds','readout_seconds','checker_seconds')): raise ValueError('Negative timing.')
        if r['truncated_rationales']>60 or r['container_peak_bytes'] is not None and r['container_peak_bytes']>24*1024**3: raise ValueError('Checker resource count/budget.')
        for key in ('input_tokens','generated_tokens','readout_tokens','candidate_mass'):
            d=r[key]; n=d['n']
            if n>60 or any((d[k] is None)!=(n==0) for k in ('min','median','mean','max')): raise ValueError('Distribution count.')
            same(d['total'],d['mean']*n if n else 0)
            if n and not 0<=d['min']<=d['median']<=d['max']: raise ValueError('Distribution range.')
            if n and not d['min']-1e-12<=d['mean']<=d['max']+1e-12: raise ValueError('Distribution mean.')
        if r['generated_tokens']['max'] is not None and r['generated_tokens']['max']>512: raise ValueError('Generation budget changed.')
        if r['candidate_mass']['n']!=r['reason_counts']['readout_completed']: raise ValueError('Candidate mass population.')
        if r['candidate_mass']['max'] is not None and r['candidate_mass']['max']>1: raise ValueError('Candidate mass range.')
    if [r['model'] for r in p['resource_summary']['checkers']]!=['G15','G7']: raise ValueError('Checker sequence.')
    return p


def validate_development(p):
    dev=prior.unique(p['development'],('fold',)); ens=prior.unique(p['ensemble_development'],('fold',))
    if set(dev)!=set(ens) or set(dev)!={(f,) for f in range(5)}: raise ValueError('Development grid.')
    for (fold,),r in ens.items():
        d=dev[fold,]; same(sum(r['training_counts'].values()),d['n_train'])
        same(r['majority_correctness'],r['training_counts']['true']>r['training_counts']['false'])
        for arm,weights in (('B',[w for w in WEIGHTS if w[2]==0]),('H',WEIGHTS)):
            choice=r['weights'][arm]; same([c['weights'] for c in choice['candidates']],[list(w) for w in weights])
            for c in choice['candidates']:
                if len(c['inner_fold_map_at_3'])!=3 or not all(0<=x<=1 for x in c['inner_fold_map_at_3']): raise ValueError('Inner score grid.')
                same(c['inner_mean_map_at_3'],float(np.mean(c['inner_fold_map_at_3'])))
            winner=int(np.argmax([c['inner_mean_map_at_3'] for c in choice['candidates']]))
            same(choice['selected_index'],winner); same(choice['selected_weights'],list(weights[winner]))
        same(r['weights']['B']['candidates'],[c for c in r['weights']['H']['candidates'] if c['weights'][2]==0])
        for arm,c in r['calibration'].items():
            if not np.exp(-3)<=c['temperature']<=np.exp(3): raise ValueError('Temperature bounds.')
            same(c['supported_n'],d['calibration_supported_n'])
            if arm in ('F','F_M','G7_hard'): same(c['method'],'unscaled'); same(c['temperature'],1.)
            if c['method']=='all_unknown_frequency':
                if arm not in ('G15','G7'): raise ValueError('Identity applied to unregistered arm.')
                same(c['temperature'],1.)
            if arm in ('B','H'):
                weights=r['weights'][arm]['selected_weights']
                if 1 in weights:
                    source=('F','L','G7')[weights.index(1)]
                    same(c['method'],'component_endpoint'); same(c['temperature'],r['calibration'][source]['temperature'])
                else: same(c['method'],'own_temperature')
        same(r['calibration']['L']['temperature'],d['temperature'])


def validate_audit(p,index,qs):
    audit=p['correctness_audit']; keys={(f,q) for f in range(5) for q in [None,*qs[f]]}
    ai=prior.unique(audit['records'],('model','fold','question'))
    if set(ai)!={(k,*x) for k in ('G15','G7') for x in keys}: raise ValueError('Correctness grid.')
    def check(r):
        cm=np.asarray(r['confusion_counts'])
        if cm.shape!=(2,3) or int(cm.sum())!=r['n']: raise ValueError('Confusion dimensions.')
        truth=np.repeat([False,True],cm.sum(axis=1)); signal=np.concatenate([np.repeat([0,1,-1],row) for row in cm])
        same({k:v for k,v in r.items() if k!='model'},m.old.audit_record(r['fold'],r['question'],truth,signal))
        same(r['n'],index['F',r['fold'],r['question'],'all']['n'])
    for r in audit['records']: check(r)
    for f,q in keys:
        same(np.asarray(ai['G15',f,q]['confusion_counts']).sum(axis=1).tolist(),np.asarray(ai['G7',f,q]['confusion_counts']).sum(axis=1).tolist())
    majority=prior.unique(audit['majority_records'],('fold','question'))
    if set(majority)!=keys: raise ValueError('Majority audit grid.')
    for (f,q),r in majority.items():
        check(r); cm=np.asarray(r['confusion_counts']); b=int(p['ensemble_development'][f]['majority_correctness'])
        if np.any(cm[:,2]) or np.any(cm[:,1-b]): raise ValueError('Nonconstant majority control.')
        same(cm.sum(axis=1).tolist(),np.asarray(ai['G15',f,q]['confusion_counts']).sum(axis=1).tolist())
    for key in ('pair_counts','row_reason_counts','projection_fallback'):
        idx=prior.unique(audit[key],('model','fold','question'))
        if set(idx)!=set(ai): raise ValueError('Auxiliary correctness grid.')
        for (k,f,q),r in idx.items():
            if key=='pair_counts':
                same(r['distinct_pairs'],r['predicted_false']+r['predicted_true']+r['unknown'])
                if not 0<r['distinct_pairs']<=ai[k,f,q]['n']: raise ValueError('Pair count.')
            elif key=='row_reason_counts': same(sum(r['reason_counts'].values()),ai[k,f,q]['n'])
            else:
                for name in ('false','true'):
                    count=r[name+'_projection_fallback_n']
                    if count>r['n'] or not r['missing_'+name+'_inventory'] and count: raise ValueError('Projection fallback count.')
            if key!='pair_counts': same(r['n'],ai[k,f,q]['n'])
            if q is None and key=='row_reason_counts':
                for name in REASONS: same(r['reason_counts'][name],sum(idx[k,f,x]['reason_counts'][name] for x in qs[f]))
    same(audit['aggregate'],m.old.summarize(audit['records'],('model','stratum')))
    same(audit['majority_aggregate'],m.old.summarize(audit['majority_records'],('stratum',)))
    if [r['model'] for r in audit['pooled_confusion']]!=['G15','G7']: raise ValueError('Pooled model grid.')
    for r in audit['pooled_confusion']:
        k=r['model']; cm=np.sum([ai[k,f,None]['confusion_counts'] for f in range(5)],axis=0)
        same(r['confusion_counts'],cm.tolist())
        same(r['confusion_row_normalized'],[[float(v/row.sum()) if row.sum() else None for v in row] for row in cm])
        for f in range(5): same(ai[k,f,None]['confusion_counts'],np.sum([ai[k,f,q]['confusion_counts'] for q in qs[f]],axis=0).tolist())


def render(p):
    validate(p); lines=['# E020 MAP numerical results','',
        'Results only; interpretation awaits review. All summaries are descriptive on the reused frozen question-held-out benchmark. E018 remains blocked. No oracle or independently verified answer key is used.','',
        '## Aggregate exact-label results (equal-fold means)','']
    prior.table(lines,[r for r in p['exact']['aggregate'] if r['stratum']=='all'])
    lines.extend(['## Fold-level exact-label results',''])
    prior.table(lines,[r for r in p['exact']['records'] if r['question'] is None and r['stratum']=='all'])
    lines.extend(['## Registered numerical decision rules','']); prior.table(lines,p['comparisons']['decisions']['comparisons'])
    lines.append('Flags: '+json.dumps({k:v for k,v in p['comparisons']['decisions'].items() if k!='comparisons'})+'\n')
    for name in ('exact','comparisons','calibration','gain_loss','rank_changes','review','correctness_audit'):
        for table,rows in p[name].items():
            if isinstance(rows,list): lines.extend(['## '+name+' / '+table,'']); prior.table(lines,rows)
    lines.extend(['## Historical development','']); prior.table(lines,p['development'])
    lines.extend(['## Training-selected weights and fixed calibration','']); prior.table(lines,p['ensemble_development'])
    lines.extend(['## Checker resource aggregates','']); prior.table(lines,p['resource_summary']['checkers'])
    lines.extend(['## Integrity','', '```json',json.dumps(p['integrity'],indent=2),'```',''])
    return '\n'.join(lines)
