"""Strict E021 aggregate schemas, arithmetic checks and full numerical tables."""
import numpy as np
from . import e007_publication as s,e019_publication as prior
from . import e021_metrics as m,e021_shuffle as sh
from .e021_selection import ALPHAS,CONTROLS
from .e011_publication import same,payload_schema
E,L,I,N,NN=s.enum,s.listing,s.I,s.N,s.NN
ARM=E(*m.ARMS); SCALE={'scale':E(*m.SCALES)}; PAIR={'left':ARM,'right':ARM}
SCOPE=prior.SCOPE; STRATUM=prior.STRATUM; FOLD=E(0,1,2,3,4)
EXACT={'arm':ARM,**SCOPE,**SCALE,'metrics':prior.EXACT}
CAL={'arm':ARM,**SCOPE,**SCALE,**prior.ELIGIBLE,'metrics':prior.CALMETRICS}
GAIN={**PAIR,**SCOPE,'wins':I,'ties':I,'losses':I,'metrics':prior.GAINMETRICS}
REVIEW={'arm':ARM,**SCOPE,'review_percent':E(*m.BUDGETS),**prior.ELIGIBLE,'metrics':prior.REVIEWMETRICS}
RANK={'arm':ARM,**SCOPE,'top1_changed_n':I,'top3_changed_n':I,'metrics':{'top1_changed_share':NN,'top3_changed_share':NN}}
REPETITION={'values':L(N),'mean':NN,'sd':NN,'p025':NN,'p975':NN}
SHUFFLE={'arm':E(*sh.ARMS),**SCALE,**SCOPE,'original':prior.EXACT,
    'shuffled':{k:{kind:REPETITION for kind in ('score','original_minus_shuffled')} for k in prior.EXACT}}
SHUFFLE_AGG={'arm':E(*sh.ARMS),**SCALE,'stratum':STRATUM,'n_total':I,'original':{k:prior.STAT for k in prior.EXACT},
    'shuffled':{k:{kind:{'fold_stat':prior.STAT,'paired_replicates':REPETITION} for kind in ('score','original_minus_shuffled')} for k in prior.EXACT}}
OPPORTUNITY={'fold':FOLD,'question':s.nullable(I),'n':I,'cells':I,'singleton_rows':I,'movable_rows':I,
    'label_mixed_rows':I,'label_mixed_share':N,'donor_changed_n':REPETITION,'input_changed_n':REPETITION}
SELECTION={'selected_index':I,'selected_alpha':E(*ALPHAS),'candidates':L({'alpha':E(*ALPHAS),'inner_fold_map_at_3':L(N),'inner_mean_map_at_3':N})}
ENSEMBLE={'fold':FOLD,'alpha_selection':SELECTION,
    'calibration':{a:{'temperature':N,'supported_n':I,'method':E('unscaled','own_temperature','all_unknown_frequency','component_reuse')} for a in m.ARMS},
    'projection_fallback':{'fold':FOLD,'missing_false_inventory':s.B,'missing_true_inventory':s.B,
        'false_projection_fallback_n':I,'true_projection_fallback_n':I}}


def panel(record,dims):
    return {'records':L(record),'aggregate':L(prior.summary(dims,record['metrics']))}


SCHEMA={'experiment_id':E('E021'),'status':E('COMPLETED'),
    'development':payload_schema('E011')['development'],'ensemble_development':L(ENSEMBLE),
    'exact':panel(EXACT,{'arm':ARM,**SCALE,'stratum':STRATUM}),
    'comparisons':{**panel({**PAIR,**SCOPE,**SCALE,'metrics':prior.EXACT},{**PAIR,**SCALE,'stratum':STRATUM}),
        'decisions':{'comparisons':L({**PAIR,**SCALE,**prior.STAT,'positive_folds':I,'criterion_met':s.B}),
            **{k:s.B for k in ('H1_fixed_primary','raw_attribution_check','conditioning_attribution_supported','H2_tuned_secondary')}},
        'question_heterogeneity':L({**PAIR,'questions':E(15),'positive':I,'zero':I,'negative':I,'min_delta':N,'max_delta':N})},
    'calibration':{**panel(CAL,{'arm':ARM,**SCALE,'stratum':STRATUM}),
        'contrasts':L({**PAIR,**SCOPE,**SCALE,'jointly_eligible_n':I,'metrics':{'ece':NN,'brier':NN}}),
        'contrast_aggregate':L(prior.summary({**PAIR,**SCALE,'stratum':STRATUM},('ece','brier'))),
        'final_minus_raw':L({'arm':ARM,**SCOPE,'jointly_eligible_n':I,'metrics':{'ece':NN,'brier':NN}}),
        'change_aggregate':L(prior.summary({'arm':ARM,'stratum':STRATUM},('ece','brier')))},
    'gain_loss':panel(GAIN,{**PAIR,'stratum':STRATUM}),'rank_changes':panel(RANK,{'arm':ARM,'stratum':STRATUM}),
    'review':{**panel(REVIEW,{'arm':ARM,'review_percent':E(*m.BUDGETS),'stratum':STRATUM}),
        'contrasts':L({**PAIR,**SCOPE,'review_percent':E(*m.BUDGETS),'jointly_eligible_n':I,'metrics':prior.REVIEWMETRICS}),
        'contrast_aggregate':L(prior.summary({**PAIR,'review_percent':E(*m.BUDGETS),'stratum':STRATUM},prior.REVIEWMETRICS))},
    'explanation_shuffle':{'records':L(SHUFFLE),'aggregate':L(SHUFFLE_AGG),'opportunity':L(OPPORTUNITY)},
    'integrity':{'git_revision':s.pattern('[0-9a-f]{40}'),'lock_sha256':s.HASH,'protocol_sha256':s.HASH,
        'e020_results_sha256':s.HASH,'g7_cache_sha256':s.HASH,'frozen_development_sha256':s.HASH,
        'preserved_files':I,'preservation_verified':E(True),'global_freeze_verified':E(True),'e018_remains_blocked':E(True),
        'model_fits':E(50),'new_model_calls':E(0),'fit_warnings':E(0),'reproduction_model_folds':E(20),
        'shuffle_replicates_per_fold':E(100),'shuffle_seed':E(20261014),'seed':E(20260831),'row_level_outputs':E(False),'uid':E(10001),'gid':E(10001)},
    'resources':{'image_id':s.pattern('sha256:[0-9a-f]{64}'),'wall_seconds':N}}


def validate(p):
    s.validate_schema(p,SCHEMA)
    rows=p['exact']['records']; idx=prior.unique(rows,('arm','fold','question','stratum','scale'))
    qs={f:sorted({r['question'] for r in rows if r['fold']==f and r['question'] is not None}) for f in range(5)}
    if any(len(q)!=3 for q in qs.values()) or len(set(sum(qs.values(),[])))!=15: raise ValueError('Question grid.')
    scopes=[(f,q,t) for f in range(5) for q in [None,*qs[f]] for t in m.STRATA]
    expected={(a,*scope,scale) for a in m.ARMS for scope in scopes for scale in m.SCALES}
    if set(idx)!=expected: raise ValueError('Exact grid.')
    for r in rows:
        a,f,q,t,scale=(r[k] for k in ('arm','fold','question','stratum','scale')); n=r['n']
        same(n,idx['F',f,q,t,'raw']['n'])
        for v in r['metrics'].values():
            if (v is None)!=(n==0) or v is not None and not 0<=v<=1: raise ValueError('Exact range/null.')
            if t=='unsupported' and n and v!=0: raise ValueError('Unsupported truth scored.')
        if t=='well_supported' and n>idx[a,f,q,'frequent',scale]['n']: raise ValueError('Support nesting.')
        parts=[idx[a,f,x,t,scale] for x in qs[f]] if q is None else [idx[a,f,q,x,scale] for x in ('unsupported','rare','frequent')] if t=='all' else None
        if parts is not None:
            same(n,sum(x['n'] for x in parts))
            for k in prior.EXACT: same(r['metrics'][k],sum(x['n']*x['metrics'][k] for x in parts if x['n'])/n if n else None)
    if sum(idx['F',f,None,'all','raw']['n'] for f in range(5))!=36696: raise ValueError('Population differs.')
    cal=prior.unique(p['calibration']['records'],('arm','fold','question','stratum','scale'))
    if set(cal)!=expected: raise ValueError('Calibration grid.')
    review=prior.unique(p['review']['records'],('arm','fold','review_percent'))
    if set(review)!={(a,f,b) for a in m.ARMS for f in range(5) for b in m.BUDGETS}: raise ValueError('Review grid.')
    for r in [*cal.values(),*review.values()]:
        n=r['n']; correct=r['correct_n']; errors=r['incorrect_n']; same(n,correct+errors)
        reasons=[]
        if n<200: reasons.append('n_below_200')
        if correct<20: reasons.append('correct_below_20')
        if errors<20: reasons.append('incorrect_below_20')
        same(reasons,r['ineligible_reasons']); v=r['metrics']
        acc=v.get('accuracy',v.get('top1_accuracy')); same(acc,correct/n if n else None)
        if (v['mean_confidence'] is None)!=(n==0) or n and not 0<=v['mean_confidence']<=1+1e-12: raise ValueError('Confidence range.')
        same(v['confidence_minus_accuracy'],v['mean_confidence']-acc if n else None)
        for k in ('ece','brier'):
            if (v[k] is None)!=bool(reasons) or v[k] is not None and not -1e-12<=v[k]<=(2 if k=='brier' else 1)+1e-12: raise ValueError('Calibration eligibility/range.')
        if 'scale' in r:
            source=idx[r['arm'],r['fold'],r['question'],r['stratum'],r['scale']]
            same(n,source['n']); same(acc,source['metrics']['top1_accuracy'])
        else:
            source=idx[r['arm'],r['fold'],None,'all','final']; total=source['n']; budget=r['review_percent']
            if r['question'] is not None or r['stratum']!='all': raise ValueError('Review scope.')
            same(n,total-total*budget//100); same(v['coverage'],n/total); same(v['risk'],1-acc)
            if budget==0:
                for k in prior.EXACT: same(v[k],source['metrics'][k])
    gains=prior.unique(p['gain_loss']['records'],('left','right','fold','question','stratum'))
    if set(gains)!={(a,b,*scope) for a,b in m.GAIN_PAIRS for scope in scopes}: raise ValueError('Gain grid.')
    for r in gains.values():
        f,q,t=(r[k] for k in ('fold','question','stratum')); n=r['n']
        same(n,idx[r['left'],f,q,t,'final']['n']); same(n,r['wins']+r['ties']+r['losses'])
        if any((v is None)!=(n==0) for v in r['metrics'].values()): raise ValueError('Gain null.')
        if n:
            v=r['metrics']; same(v['gain']+v['loss'],v['delta'])
            same(v['delta'],idx[r['left'],f,q,t,'final']['metrics']['map_at_3']-idx[r['right'],f,q,t,'final']['metrics']['map_at_3'])
            if v['gain']<0 or v['loss']>0: raise ValueError('Gain signs.')
    ranks=prior.unique(p['rank_changes']['records'],('arm','fold','question','stratum'))
    if set(ranks)!={(a,*scope) for a in m.ARMS for scope in scopes}: raise ValueError('Rank grid.')
    for r in ranks.values():
        same(r['n'],idx[r['arm'],r['fold'],r['question'],r['stratum'],'raw']['n'])
        for k in ('top1','top3'):
            if r[k+'_changed_n']>r['n']: raise ValueError('Rank count.')
            same(r['metrics'][k+'_changed_share'],r[k+'_changed_n']/r['n'] if r['n'] else None)
    rebuilt=m.build_panels(rows,list(cal.values()),list(gains.values()),list(review.values()),list(ranks.values()))
    for key,value in rebuilt.items(): same(p[key],value)
    validate_development(p)
    validate_shuffle(p,idx,scopes,qs)
    if p['resources']['wall_seconds']<0: raise ValueError('Negative elapsed time.')
    return p


def validate_development(p):
    ds=prior.unique(p['development'],('fold',)); es=prior.unique(p['ensemble_development'],('fold',))
    if set(ds)!=set(es) or set(ds)!={(f,) for f in range(5)}: raise ValueError('Development grid.')
    for key,e in es.items():
        d=ds[key]; choice=e['alpha_selection']
        same([x['alpha'] for x in choice['candidates']],list(ALPHAS))
        for selection in (choice,d['selection']):
            for c in selection['candidates']:
                if len(c['inner_fold_map_at_3'])!=3 or not all(0<=x<=1 for x in c['inner_fold_map_at_3']): raise ValueError('Inner scores.')
                same(c['inner_mean_map_at_3'],float(np.mean(c['inner_fold_map_at_3'])))
            same(selection['selected_index'],int(np.argmax([c['inner_mean_map_at_3'] for c in selection['candidates']])))
        same([r['params'] for r in d['selection']['candidates']],[{**r,'ngram_range':list(r['ngram_range'])} for r in m.old.core.e001.GRID])
        same(choice['selected_alpha'],ALPHAS[choice['selected_index']]); same(d['fits'],10); same(d['role_question_counts'],[9,3,3])
        for arm,c in e['calibration'].items():
            if not np.exp(-3)<=c['temperature']<=np.exp(3): raise ValueError('Temperature bound.')
            same(c['supported_n'],d['calibration_supported_n'])
            if arm=='F': same(c['method'],'unscaled'); same(c['temperature'],1.)
            elif arm=='G7' and c['method']=='all_unknown_frequency': same(c['temperature'],1.)
            elif arm=='T' and choice['selected_alpha'] in (0.,.5,1.):
                source={0.:'G7',.5:'C50',1.:'L7'}[choice['selected_alpha']]
                same(c['method'],'component_reuse'); same(c['temperature'],e['calibration'][source]['temperature'])
            else: same(c['method'],'own_temperature')
        same(e['calibration']['L']['temperature'],d['temperature'])
        fallback=e['projection_fallback']; same(fallback['fold'],d['fold'])
        for b in ('false','true'):
            n=fallback[b+'_projection_fallback_n']
            if n>d['n_evaluation'] or not fallback['missing_'+b+'_inventory'] and n: raise ValueError('Projection fallback.')


def validate_shuffle(p,exact,scopes,qs):
    rows=p['explanation_shuffle']['records']; idx=prior.unique(rows,('arm','fold','question','stratum','scale'))
    if set(idx)!={(a,*scope,scale) for a in sh.ARMS for scope in scopes for scale in sh.SCALES}: raise ValueError('Shuffle grid.')
    for key,r in idx.items():
        same(r['n'],exact[key]['n']); same(r['original'],exact[key]['metrics'])
        for k in prior.EXACT:
            for kind,rep in r['shuffled'][k].items():
                if len(rep['values'])!=(100 if r['n'] else 0): raise ValueError('Replicate count.')
                same(rep,sh.repetition(rep['values']))
                if any(not (-1 if kind=='original_minus_shuffled' else 0)<=v<=1 for v in rep['values']): raise ValueError('Shuffle range.')
            score=r['shuffled'][k]['score']['values']; delta=r['shuffled'][k]['original_minus_shuffled']['values']
            same(delta,[r['original'][k]-v for v in score])
            if r['arm']=='G7': same(delta,[0.]*len(delta))
    same(p['explanation_shuffle']['aggregate'],sh.summarize(rows))
    opp=prior.unique(p['explanation_shuffle']['opportunity'],('fold','question'))
    if set(opp)!={(f,q) for f in range(5) for q in [None,*qs[f]]}: raise ValueError('Opportunity grid.')
    for (f,q),r in opp.items():
        same(r['n'],exact['F',f,q,'all','raw']['n']); same(r['n'],r['singleton_rows']+r['movable_rows'])
        if not 0<r['cells']<=r['n'] or r['label_mixed_rows']>r['movable_rows']: raise ValueError('Opportunity counts.')
        same(r['label_mixed_share'],r['label_mixed_rows']/r['n'])
        for k in ('donor_changed_n','input_changed_n'):
            rep=r[k]
            if len(rep['values'])!=100 or any(v!=int(v) or not 0<=v<=r['movable_rows'] for v in rep['values']): raise ValueError('Opportunity replicates.')
            same(rep,sh.repetition(rep['values']))
        if any(a>b for a,b in zip(r['input_changed_n']['values'],r['donor_changed_n']['values'])): raise ValueError('Movement ordering.')
        if q is None:
            for k in ('n','cells','singleton_rows','movable_rows','label_mixed_rows'): same(r[k],sum(opp[f,x][k] for x in qs[f]))
            for k in ('donor_changed_n','input_changed_n'): same(r[k]['values'],np.sum([opp[f,x][k]['values'] for x in qs[f]],axis=0).tolist())


def render(p):
    validate(p); lines=['# E021 numerical results','',
        'Results before interpretation. Fixed primary comparison and tuned secondary ensemble remain separate. All uncertainty is descriptive on the reused frozen question-held-out benchmark.','',
        '## Fixed comparison: primary final and raw attribution','']
    prior.table(lines,p['comparisons']['decisions']['comparisons'][:2])
    lines+=['## Tuned ensemble: secondary comparisons with both endpoints','']
    prior.table(lines,p['comparisons']['decisions']['comparisons'][2:])
    lines+=['## Aggregate original-input results','']; prior.table(lines,p['exact']['aggregate'])
    lines+=['## Fold-level original-input results','']; prior.table(lines,[r for r in p['exact']['records'] if r['question'] is None and r['stratum']=='all'])
    for name in ('exact','comparisons','calibration','gain_loss','rank_changes','review','explanation_shuffle'):
        for title,rows in p[name].items():
            if isinstance(rows,list): lines+=['## '+name+' / '+title,'']; prior.table(lines,rows)
    lines+=['## Historical text development','']; prior.table(lines,p['development'])
    lines+=['## Secondary alpha selection and calibration','']; prior.table(lines,p['ensemble_development'])
    import json
    lines+=['## Decision flags and provenance','','```json',json.dumps({'decisions':p['comparisons']['decisions'],
        'integrity':p['integrity'],'resources':p['resources']},indent=2),'```','']
    return '\n'.join(lines)
