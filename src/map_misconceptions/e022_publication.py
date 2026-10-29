"""Strict aggregate-only E022 schema and independent arithmetic/grid checks."""
import itertools
import numpy as np
from . import e007_publication as s,e019_publication as prior,e022_metrics as m
from .e011_publication import same,payload_schema
from .e022_selection import ARMS,TARGETS,core

E,L,I,N,NN=s.enum,s.listing,s.I,s.N,s.NN
ARM=E(*ARMS); TARGET=E(*TARGETS); FOLD=E(0,1,2,3,4); Q=s.nullable(I); STRATUM=E(*m.STRATA)
GROUP={**s.GROUP,'confidence_minus_accuracy':NN}
BASE={'arm':ARM,'fold':FOLD,'question':Q,'stratum':STRATUM,'group':GROUP}
SELECTION=payload_schema('E011')['development'][1]['selection']
DEV={'arm':ARM,'fold':FOLD,'role_counts':L(I),'derived_role_sha256':s.HASH,'n_train':I,'n_calibration':I,'n_evaluation':I,
    'selection':s.nullable(SELECTION),'temperature':N,'temperature_n':I,'temperature_supported_n':I,
    'temperature_supported_fraction':NN,'temperature_fallback':s.B,'method':E('unscaled','own_temperature'),
    'projection_fallback':{'false_n':I,'true_n':I}}
POLICY={'arm':ARM,'fold':FOLD,'policy':s.POLICY}
STAT=prior.STAT
def summary(dims,names): return {**dims,'metrics':{k:STAT for k in names}}
PAIRED={'left':ARM,'right':ARM,'target_percent':TARGET,'fold':FOLD,'stratum':STRATUM,
    'left_original_n':I,'right_original_n':I,'left_retained_n':I,'right_retained_n':I,
    'left_coverage':NN,'right_coverage':NN,'metrics':{k:NN for k in m.PAIR_METRICS}}
DECISION={'arm':ARM,'target_percent':TARGET,'primary':s.B,'fold_admissible':L(s.B),'admissible_folds':I,
    'questions':L({'fold':FOLD,'question':I,'original_n':I,'retained_n':I,'risk':NN,'count_pass':s.B,
        'coverage_pass':s.B,'risk_pass':s.NB,'joint_pass':s.B}),
    **{k:I for k in ('question_count','nonempty_questions','count_pass_questions','coverage_pass_questions',
        'risk_pass_questions','risk_exceeded_questions','risk_denominator','joint_pass_questions')},
    'maximum_question_risk':NN,'criterion_met':s.B}
SCHEMA={'experiment_id':E('E022'),'status':E('COMPLETED'),'development':L(DEV),'policies':L(POLICY),
    'unfiltered':{'records':L({**BASE,'scale':E('raw','final')}),'aggregate':L(summary({'arm':ARM,'scale':E('raw','final'),'stratum':STRATUM},m.NUMERIC))},
    'retained':{'records':L({**BASE,'target_percent':TARGET}),'aggregate':L(summary({'arm':ARM,'target_percent':TARGET,'stratum':STRATUM},m.NUMERIC))},
    'comparisons':{'records':L(PAIRED),'aggregate':L(summary({'left':ARM,'right':ARM,'target_percent':TARGET,'stratum':STRATUM},m.PAIR_METRICS))},
    'decisions':L(DECISION),'gaps':L({'arm':ARM,'target_percent':TARGET,'fold':FOLD,'question':I,
        'development_risk':NN,'evaluation_risk':NN,'risk_minus_development':NN}),
    'integrity':{'git_revision':s.pattern('[0-9a-f]{40}'),'lock_sha256':s.HASH,'protocol_sha256':s.HASH,
        'reference_sha256':s.HASH,'g7_cache_sha256':s.HASH,'freeze_sha256':s.HASH,'preserved_files':I,
        'preservation_verified':E(True),'global_freeze_verified':E(True),'e018_remains_blocked':E(True),
        'model_fits':E(50),'new_model_calls':E(0),'fit_warnings':E(0),'reproduced_model_folds':E(15),
        'policies':E(45),'seed':E(20260831),'uid':E(10001),'gid':E(10001),'row_level_public_outputs':E(False)},
    'resources':{'image_id':s.pattern('sha256:[0-9a-f]{64}'),'wall_seconds':N}}


def validate_development(development,policies):
    d=prior.unique(development,('arm','fold')); p={
        (r['arm'],r['fold'],r['policy']['target_percent']):r['policy'] for r in policies}
    if len(p)!=len(policies) or set(p)!=set(itertools.product(ARMS,range(5),TARGETS)):
        raise ValueError('Policy grid differs.')
    if set(d)!=set(itertools.product(ARMS,range(5))): raise ValueError('Development grid differs.')
    for (arm,fold),r in d.items():
        same(r['role_counts'],[9,1,2,3]); same(r['derived_role_sha256'],d['F',fold]['derived_role_sha256'])
        for k in ('n_train','n_calibration','n_evaluation'): same(r[k],d['F',fold][k])
        if not np.exp(-3)<=r['temperature']<=np.exp(3): raise ValueError('Temperature bounds.')
        if arm=='F':
            for k,v in {'temperature':1.,'temperature_n':0,'temperature_supported_n':0,'temperature_supported_fraction':None,
                        'temperature_fallback':False,'method':'unscaled','selection':None,'projection_fallback':{'false_n':0,'true_n':0}}.items(): same(r[k],v)
        else:
            n=r['temperature_n']; supported=r['temperature_supported_n']
            if not 0<n<r['n_calibration'] or not 0<=supported<=n: raise ValueError('Temperature support counts.')
            same(r['temperature_supported_fraction'],supported/n); same(r['temperature_fallback'],supported==0)
            if supported==0: same(r['temperature'],1.)
            same(r['method'],'own_temperature'); choice=r['selection']
            same([c['params'] for c in choice['candidates']],[{**v,'ngram_range':list(v['ngram_range'])} for v in core.e001.GRID])
            for c in choice['candidates']:
                if len(c['inner_fold_map_at_3'])!=3 or any(not 0<=v<=1 for v in c['inner_fold_map_at_3']): raise ValueError('Inner scores.')
                same(c['inner_mean_map_at_3'],float(np.mean(c['inner_fold_map_at_3'])))
            same(choice['selected_index'],int(np.argmax([c['inner_mean_map_at_3'] for c in choice['candidates']])))
            same(choice,d['L7',fold]['selection'])
            if any(v>r['n_evaluation'] for v in r['projection_fallback'].values()): raise ValueError('Projection fallback count.')
        for target in TARGETS:
            policy=p[arm,fold,target]; parts=policy['development']
            if [x['role_index'] for x in parts]!=[0,1] or any(x['original_n']==0 for x in parts): raise ValueError('Development questions.')
            if not 1<=policy['candidate_count'] or not 0<=policy['admissible_candidate_count']<=policy['candidate_count']: raise ValueError('Candidate accounting.')
            selected=policy['status']=='SELECTED'
            if selected!=(policy['admissible_candidate_count']>0) or selected!=(policy['threshold'] is not None): raise ValueError('Policy status.')
            if selected and not 0<=policy['threshold']<=1: raise ValueError('Cutoff range.')
            for x in parts:
                n=x['retained_n']; e=x['incorrect_n']; original=x['original_n']
                if not 0<=e<=n<=original: raise ValueError('Development counts.')
                same(x['coverage'],n/original); same(x['risk'],e/n if n else None)
                if selected and not (n>=100 and n*10>=original and e*100<=target*n): raise ValueError('Inadmissible selected policy.')
                if not selected and (n or e): raise ValueError('Absent policy retained cases.')
                if arm=='F' and selected: same(n,original)
            if arm!='F': same(sum(x['original_n'] for x in parts),r['n_calibration']-r['temperature_n'])
            same([x['original_n'] for x in parts],[x['original_n'] for x in p['F',fold,target]['development']])
    return d,p


def validate(p):
    s.validate_schema(p,SCHEMA); dev,policies=validate_development(p['development'],p['policies'])
    u=prior.unique(p['unfiltered']['records'],('arm','fold','question','stratum','scale'))
    r=prior.unique(p['retained']['records'],('arm','fold','question','stratum','target_percent'))
    qs={f:sorted({v['question'] for v in p['unfiltered']['records'] if v['fold']==f and v['question'] is not None}) for f in range(5)}
    if any(len(v)!=3 for v in qs.values()) or len(set(sum(qs.values(),[])))!=15: raise ValueError('Question grid.')
    scopes=[(f,q,t) for f in range(5) for q in [None,*qs[f]] for t in m.STRATA]
    if set(u)!={(a,*scope,scale) for a in ARMS for scope in scopes for scale in ('raw','final')}: raise ValueError('Unfiltered grid.')
    if set(r)!={(a,*scope,target) for a in ARMS for scope in scopes for target in TARGETS}: raise ValueError('Retained grid.')
    for arm,fold,q in [(a,f,q) for a in ARMS for f in range(5) for q in [None,*qs[f]]]:
        for collection,values in ((u,('raw','final')),(r,TARGETS)):
            for value in values:
                groups={t:collection[arm,fold,q,t,value]['group'] for t in m.STRATA}
                target=value if collection is r else None
                s.validate_groups(groups,target)
                for t,g in groups.items():
                    n=g['retained_n']; original=g['original_n']
                    same(original,u['F',fold,q,t,'raw']['group']['original_n'])
                    same(g['confidence_minus_accuracy'],g['mean_confidence']-g['top1_accuracy'] if n else None)
                    if g['ece'] is not None and not 0<=g['ece']<=1 or g['brier'] is not None and not 0<=g['brier']<=2:
                        raise ValueError('Calibration range.')
                    if t=='unsupported' and n: same(g['map_at_3'],0.)
                    if collection is u:
                        same(n,original)
                        for k in ('correct_n','incorrect_n','map_at_3'): same(g[k],u[arm,fold,q,t,'raw']['group'][k])
                        if arm=='F': same(g,u['F',fold,q,t,'raw']['group'])
                    else:
                        policy=policies[arm,fold,target]
                        if policy['status']=='NO_ADMISSIBLE_THRESHOLD': same(n,0)
                        elif arm=='F': same(n,original)
                    if q is None:
                        parts=[collection[arm,fold,x,t,value]['group'] for x in qs[fold]]
                        for k in ('original_n','retained_n','correct_n','incorrect_n'): same(g[k],sum(x[k] for x in parts))
                        for k in ('map_at_3','mean_confidence'):
                            same(g[k],sum(x['retained_n']*x[k] for x in parts if x['retained_n'])/n if n else None)
                    if t=='all':
                        parts=[groups[x] for x in ('unsupported','rare','frequent')]
                        for k in ('map_at_3','mean_confidence'):
                            same(g[k],sum(x['retained_n']*x[k] for x in parts if x['retained_n'])/n if n else None)
    if sum(u['F',f,None,'all','raw']['group']['original_n'] for f in range(5))!=36696: raise ValueError('Population differs.')
    for (arm,fold),d in dev.items(): same(d['n_evaluation'],u[arm,fold,None,'all','raw']['group']['original_n'])
    rebuilt=m.panels(p['unfiltered']['records'],p['retained']['records'],p['policies'])
    for k,v in rebuilt.items(): same(p[k],v)


def render(p):
    validate(p)
    lines=['# E022 numerical results','',
        'Results before interpretation. L7 and fixed C50 have separate primary decisions at 20% error. Frequency is context. E022 uses one temperature question and two cutoff questions per fold; E021 used three temperature questions. All uncertainty is descriptive.','',
        '## Primary decisions at 20% error','']
    prior.table(lines,[{k:v for k,v in r.items() if k not in ('questions','fold_admissible')} for r in p['decisions'] if r['target_percent']==20])
    lines+=['## Aggregate retained results at all targets','']; prior.table(lines,[r for r in p['retained']['aggregate'] if r['stratum']=='all'])
    lines+=['## Fold-level retained results at all targets','']; prior.table(lines,[r for r in p['retained']['records'] if r['question'] is None and r['stratum']=='all'])
    for arm in ARMS:
        lines+=['## Development / '+arm,'']; prior.table(lines,[r for r in p['development'] if r['arm']==arm])
    for key in ('policies','decisions','gaps'):
        lines+=['## '+key,'']; prior.table(lines,p[key])
    for key in ('unfiltered','retained','comparisons'):
        for name,rows in p[key].items(): lines+=['## '+key+' / '+name,'']; prior.table(lines,rows)
    import json
    lines+=['## Provenance','','```json',json.dumps({'integrity':p['integrity'],'resources':p['resources']},indent=2),'```','']
    return '\n'.join(lines)
