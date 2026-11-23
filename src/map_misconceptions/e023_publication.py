"""Strict E023 aggregate schema, arithmetic checks and numerical-only report."""
import itertools
import numpy as np
from . import e007_publication as v,e019_publication as tables,e022_publication as old,e023_metrics as m,e023_selection as s
from .e011_publication import same
from .e009_metrics import eligibility

E,L,I,N,NN=v.enum,v.listing,v.I,v.N,v.NN
ARM=E('F',*s.ARMS); RULE=E('frequency',*s.RULES); FOLD=E(0,1,2,3,4); STRATUM=E(*m.STRATA)
REASONS=L(E('n_below_200','correct_below_20','incorrect_below_20'))
HEAD={**{k:I for k in ('n','correct_n','incorrect_n')},**{k:NN for k in ('mean_predicted_correctness','binary_brier','binary_ece')},'ineligible_reasons':REASONS}
AUC={**{k:I for k in ('n','correct_n','incorrect_n')},'auroc':NN,'ineligible_reasons':REASONS}
BASE={'arm':ARM,'rule':RULE,'fold':FOLD,'question':v.nullable(I),'stratum':STRATUM}
RG={**old.GROUP,**{k:NN for k in m.EXTRA_METRICS}}
RG.update({k:I for k in ('original_error_n','reviewed_n','reviewed_error_n','reviewed_correct_n')})
def summary(dims,names): return {**dims,'metrics':{k:tables.STAT for k in names}}
def pair_schema(value_key,values,names):
    dims={'arm':E(*s.ARMS),'control':RULE,value_key:E(*values),'stratum':STRATUM}
    rec={**dims,'fold':FOLD,**{k:I for k in ('left_original_n','right_original_n','left_retained_n','right_retained_n')},
        **{k:NN for k in ('left_coverage','right_coverage')},**{k:v.nullable(I) for k in ('left_original_error_n','right_original_error_n')},'metrics':{k:NN for k in names}}
    return {'records':L(rec),'aggregate':L(summary(dims,names))}
def family_schema(key,values,group,names,pairnames):
    dims={'arm':ARM,'rule':RULE,key:E(*values),'stratum':STRATUM}
    return {'records':L({**BASE,key:E(*values),'group':group,'reliability':v.nullable(HEAD)}),
        'aggregate':L(summary(dims,names)),'reliability':L(summary(dims,m.HEAD_METRICS)),
        'comparisons':pair_schema(key,values,pairnames)}
REVIEW=family_schema('review_percent',s.BUDGETS,RG,m.REVIEW_METRICS,m.REVIEW_PAIRS)
REVIEW['decisions']=L({'arm':E(*s.ARMS),'review_percent':E(20),'control':E('R5'),**tables.STAT,'positive_folds':I,'criterion_met':v.B})
AUTO=family_schema('target_percent',s.TARGETS,old.GROUP,m.AUTO_METRICS,m.AUTO_PAIRS)
AUTO['decisions']=L({**old.DECISION,'arm':ARM,'rule':RULE})
AUTO['gaps']=L({'arm':ARM,'rule':RULE,'target_percent':E(*s.TARGETS),'fold':FOLD,'question':I,'development_risk':NN,'evaluation_risk':NN,'risk_minus_development':NN})
ROUTER={'arm':E(*s.ARMS),'rule':E('R5','R8'),'fold':FOLD,'n':I,'correct_n':I,'incorrect_n':I,'question_count':E(9),'feature_count':E(5,8),
    'weight_sum':N,'status':E('FITTED','CONSTANT_CORRECTNESS_FALLBACK'),'constant':v.nullable(E(0,1)),'fitting_calls':E(0,1),'convergence_warnings':E(0)}
CROSS={'fold':FOLD,'role_sha256':v.HASH,'blocks':L({'block':E(0,1,2),'fitting_questions':E(6),'held_questions':E(3),'fitting_n':I,'held_n':I,
    'selection':old.SELECTION,'correct_n':{a:I for a in s.ARMS},'classifier_fits':E(10)})}
RP={'arm':E(*s.ARMS),'control':RULE,'fold':FOLD,'stratum':STRATUM,'metrics':{'auroc':NN}}
SCHEMA={'experiment_id':E('E023'),'status':E('COMPLETED'),'development':L(old.DEV),'policies':L({'arm':ARM,'rule':RULE,'fold':FOLD,'policy':v.POLICY}),
    'routers':L(ROUTER),'crossfit':L(CROSS),'review':REVIEW,'automation':AUTO,
    'ranking':{'records':L({**BASE,'group':AUC}),'aggregate':L(summary({'arm':ARM,'rule':RULE,'stratum':STRATUM},('n','correct_n','incorrect_n','auroc'))),
        'comparisons':{'records':L(RP),'aggregate':L(summary({'arm':E(*s.ARMS),'control':RULE,'stratum':STRATUM},('auroc',)))}},
    'integrity':{'git_revision':v.pattern('[0-9a-f]{40}'),'lock_sha256':v.HASH,'protocol_sha256':v.HASH,'reference_sha256':v.HASH,'g7_cache_sha256':v.HASH,
        'freeze_sha256':v.HASH,'preserved_files':I,'preservation_verified':E(True),'global_freeze_verified':E(True),'e018_remains_blocked':E(True),
        'model_fits':E(200),'router_preparations':E(20),'router_fits':I,'new_model_calls':E(0),'fit_warnings':E(0),
        'reproduced_model_folds':E(15),'reproduced_unfiltered_records':E(600),'reproduced_cutoff_records':E(900),'reproduced_policies':E(45),
        'policies':E(165),'review_masks':E(390),'seed':E(20260831),'uid':E(10001),'gid':E(10001),'row_level_public_outputs':E(False)},
    'resources':{'image_id':v.pattern('sha256:[0-9a-f]{64}'),'wall_seconds':N}}


def validate(p):
    v.validate_schema(p,SCHEMA)
    confidence=[{k:x[k] for k in ('arm','fold','policy')} for x in p['policies'] if x['rule'] in ('confidence','frequency')]
    dev,_=old.validate_development(p['development'],confidence)
    policies={(r['arm'],r['rule'],r['fold'],r['policy']['target_percent']):r['policy'] for r in p['policies']}
    if len(policies)!=len(p['policies']) or set(policies)!={(a,r,f,t) for a,r in s.AUTO for f in range(5) for t in s.TARGETS}: raise ValueError('Policy grid.')
    for (arm,rule,fold,target),policy in policies.items():
        selected=policy['status']=='SELECTED'; parts=policy['development']; d=dev[arm,fold]
        if [x['role_index'] for x in parts]!=[0,1] or not 0<=policy['admissible_candidate_count']<=policy['candidate_count'] or policy['candidate_count']<1: raise ValueError('Policy accounting.')
        if selected!=(policy['threshold'] is not None) or selected!=(policy['admissible_candidate_count']>0): raise ValueError('Policy status.')
        if selected and not 0<=policy['threshold']<=1: raise ValueError('Threshold range.')
        for x in parts:
            n,e,N=x['retained_n'],x['incorrect_n'],x['original_n']
            if not 0<=e<=n<=N or N==0: raise ValueError('Development counts.')
            same(x['risk'],e/n if n else None); same(x['coverage'],n/N)
            if selected and not (n>=100 and n*10>=N and e*100<=target*n): raise ValueError('Admissibility.')
            if not selected: same(n,0)
        same([x['original_n'] for x in parts],[x['original_n'] for x in policies['F','frequency',fold,target]['development']])
    routers=tables.unique(p['routers'],('arm','rule','fold')); cross=tables.unique(p['crossfit'],('fold',))
    if set(routers)!=set(itertools.product(s.ARMS,('R5','R8'),range(5))) or set(cross)!={(f,) for f in range(5)}: raise ValueError('Router/crossfit grid.')
    for (arm,rule,fold),r in routers.items():
        same(r['n'],dev[arm,fold]['n_train']); same(r['n'],r['correct_n']+r['incorrect_n']); same(r['weight_sum'],float(r['n']))
        same(r['feature_count'],5 if rule=='R5' else 8)
        for k in ('correct_n','incorrect_n'): same(r[k],routers[arm,'R5',fold][k])
        constant=r['correct_n'] in (0,r['n']); same(r['status']=='CONSTANT_CORRECTNESS_FALLBACK',constant)
        same(r['constant'],int(r['correct_n']>0) if constant else None); same(r['fitting_calls'],int(not constant))
    same(p['integrity']['router_fits'],sum(r['fitting_calls'] for r in routers.values()))
    for (fold,),r in cross.items():
        if [b['block'] for b in r['blocks']]!=[0,1,2]: raise ValueError('Crossfit blocks.')
        same(sum(b['held_n'] for b in r['blocks']),dev['L7',fold]['n_train'])
        for b in r['blocks']:
            same(b['held_n']+b['fitting_n'],dev['L7',fold]['n_train'])
            if b['held_n']==0 or any(not 0<=v<=b['held_n'] for v in b['correct_n'].values()): raise ValueError('Crossfit counts.')
            choice=b['selection']; same([c['params'] for c in choice['candidates']],[{**v,'ngram_range':list(v['ngram_range'])} for v in s.core.e001.GRID])
            for c in choice['candidates']:
                if len(c['inner_fold_map_at_3'])!=3 or any(not 0<=v<=1 for v in c['inner_fold_map_at_3']): raise ValueError('Inner metric.')
                same(c['inner_mean_map_at_3'],float(np.mean(c['inner_fold_map_at_3'])))
            same(choice['selected_index'],max(range(3),key=lambda i:choice['candidates'][i]['inner_mean_map_at_3']))
        for a in s.ARMS: same(sum(b['correct_n'][a] for b in r['blocks']),routers[a,'R5',fold]['correct_n'])
    review=p['review']['records']; qs={f:sorted({r['question'] for r in review if r['fold']==f and r['question'] is not None}) for f in range(5)}
    if any(len(q)!=3 for q in qs.values()) or len(set(sum(qs.values(),[])))!=15: raise ValueError('Question grid.')
    lookup={}
    for family,key,combos,values in [('review','review_percent',s.REVIEW,s.BUDGETS),('automation','target_percent',s.AUTO,s.TARGETS)]:
        records=p[family]['records']; index=tables.unique(records,('arm','rule','fold','question','stratum',key)); lookup[family]=index
        expected={(a,r,f,q,t,b) for a,r in combos for f in range(5) for q in [None,*qs[f]] for t in m.STRATA for b in values}
        if set(index)!=expected: raise ValueError('Reporting grid.')
        for (a,r,f,q,t,b),record in index.items():
            g=record['group']; n,N=g['retained_n'],g['original_n']; c=g['correct_n']; e=g['incorrect_n']
            same(g['confidence_minus_accuracy'],g['mean_confidence']-g['top1_accuracy'] if n else None)
            if t=='unsupported' and n: same(g['map_at_3'],0.); same(c,0)
            for metric,upper in [('ece',1),('brier',2),('mean_confidence',1),('map_at_3',1)]:
                if g[metric] is not None and not 0<=g[metric]<=upper: raise ValueError('Metric range.')
            if family=='review':
                E0=g['original_error_n']; reviewed=N-n; captured=E0-e
                if not 0<=e<=E0<=N or not 0<=captured<=reviewed: raise ValueError('Review error counts.')
                for k,val in {'reviewed_n':reviewed,'reviewed_error_n':captured,'reviewed_correct_n':reviewed-captured,
                    'remaining_errors_per_100':100*e/N if N else None,'captured_errors_per_100':100*captured/N if N else None,
                    'error_capture_fraction':captured/E0 if E0 else None,'review_error_precision':captured/reviewed if reviewed else None}.items(): same(g[k],val)
                zero=index[a,r,f,q,t,0]['group']; same(E0,zero['incorrect_n']); same(N,zero['original_n'])
                if q is None and t=='all': same(n,N-N*b//100)
                if b==0:
                    same(n,N)
                    for k in old.GROUP: same(g[k],index[a,'frequency' if a=='F' else 'confidence',f,q,t,0]['group'][k])
                if q is None and b>0:
                    previous=index[a,r,f,q,t,b-10]['group'];
                    if n>previous['retained_n'] or e>previous['incorrect_n']: raise ValueError('Nested review counts.')
            else:
                if policies[a,r,f,b]['status']=='NO_ADMISSIBLE_THRESHOLD': same(n,0)
                if a=='F' and policies[a,r,f,b]['status']=='SELECTED': same(n,N)
                same(N,lookup['review'][a,r,f,q,t,0]['group']['original_n'])
            h=record['reliability']
            if (h is not None)!=(r in ('R5','R8')): raise ValueError('Reliability reporting scope.')
            if h is not None:
                same(h['n'],n); same(h['correct_n'],c); same(h['incorrect_n'],e)
                reasons=(['n_below_200'] if n<200 else [])+(['correct_below_20'] if c<20 else [])+(['incorrect_below_20'] if e<20 else [])
                same(h['ineligible_reasons'],reasons)
                for k in ('mean_predicted_correctness','binary_brier','binary_ece'):
                    if reasons: same(h[k],None)
                    elif h[k] is None or not 0<=h[k]<=1: raise ValueError('Binary calibration range.')
            if t=='all': v.validate_groups({st:index[a,r,f,q,st,b]['group'] for st in m.STRATA},None if family=='review' else b)
            if q is None:
                parts=[index[a,r,f,x,t,b]['group'] for x in qs[f]]
                for k in ('original_n','retained_n','correct_n','incorrect_n'): same(g[k],sum(x[k] for x in parts))
                for k in ('map_at_3','mean_confidence'): same(g[k],sum(x['retained_n']*x[k] for x in parts if x['retained_n'])/n if n else None)
    same(sum(lookup['review']['F','frequency',f,None,'all',0]['group']['original_n'] for f in range(5)),36696)
    ranking=tables.unique(p['ranking']['records'],('arm','rule','fold','question','stratum'))
    if set(ranking)!={(a,r,f,q,t) for a,r in s.REVIEW for f in range(5) for q in [None,*qs[f]] for t in m.STRATA}: raise ValueError('Ranking grid.')
    for (a,r,f,q,t),row in ranking.items():
        g=row['group']; z=lookup['review'][a,r,f,q,t,0]['group']; n,c,e=g['n'],g['correct_n'],g['incorrect_n']
        same(n,z['original_n']); same(c,z['correct_n']); same(e,z['incorrect_n'])
        reasons=(['n_below_200'] if n<200 else [])+(['correct_below_20'] if c<20 else [])+(['incorrect_below_20'] if e<20 else [])
        same(g['ineligible_reasons'],reasons)
        if reasons: same(g['auroc'],None)
        elif g['auroc'] is None or not 0<=g['auroc']<=1: raise ValueError('AUROC range.')
    rebuilt=m.panels(review,p['automation']['records'],p['ranking']['records'],p['policies'])
    for key in rebuilt: same(p[key],rebuilt[key])


def table(lines,rows):
    # Nullable reliability objects and fitted/fallback metadata share one table.
    def flatten(obj,prefix=''):
        result={}
        for k,vv in obj.items():
            if isinstance(vv,dict): result.update(flatten(vv,prefix+k+'.'))
            else: result[prefix+k]=vv
        return result
    flat=[flatten(r) for r in rows]
    if not flat: return
    columns=list(dict.fromkeys(k for r in flat for k in r))
    lines.extend(['| '+' | '.join(columns)+' |','|'+'|'.join(['---']*len(columns))+'|'])
    for r in flat: lines.append('| '+' | '.join(tables.value(r.get(k)).replace('|','\\|') for k in columns)+' |')
    lines.append('')


def render(p):
    validate(p)
    lines=['# E023 numerical results','','Results before interpretation. Review prioritization and automation have separate criteria. Descriptive results on the repeatedly used 15-question benchmark; no human correction outcomes or risk guarantees.','',
        '## Primary review decisions at 20% review','']
    table(lines,p['review']['decisions'])
    lines+=['## Separate automation decisions at 20% error','']
    table(lines,[{k:v for k,v in r.items() if k not in ('questions','fold_admissible')} for r in p['automation']['decisions'] if r['target_percent']==20])
    for family,key in [('review','review_percent'),('automation','target_percent')]:
        lines+=['## '+family+' aggregate results','']; table(lines,[r for r in p[family]['aggregate'] if r['stratum']=='all'])
        lines+=['## '+family+' fold results','']; table(lines,[r for r in p[family]['records'] if r['question'] is None and r['stratum']=='all'])
    for arm in ('F',*s.ARMS):
        lines+=['## Development '+arm,'']; table(lines,[r for r in p['development'] if r['arm']==arm])
    for key in ('policies','routers','crossfit'):
        lines+=['## '+key,'']; table(lines,p[key])
    for family in ('review','automation','ranking'):
        for key,value in p[family].items():
            if isinstance(value,list): lines+=['## '+family+' / '+key,'']; table(lines,value)
            else:
                for name,rows in value.items(): lines+=['## '+family+' / '+key+' / '+name,'']; table(lines,rows)
    import json
    lines+=['## Provenance','','```json',json.dumps({'integrity':p['integrity'],'resources':p['resources']},indent=2),'```','']
    return '\n'.join(lines)
