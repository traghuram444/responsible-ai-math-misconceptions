"""E021 fixed conditioning comparison and separate inner-only alpha selection."""
import numpy as np
from sklearn.model_selection import GroupKFold
from . import e020_selection as prior
from .e020_fusion import soft_project
from .e016 import marginalize
from .data_contract import combined_label

ARMS=('F','L','G7','L7','U50','C50','T')
ALPHAS=(0.,.25,.5,.75,1.)
CONTROLS=('F','L','G7','L7')
core=prior.core
FEATURES=prior.FEATURES


def blend(g,l,alpha):
    if alpha not in ALPHAS: raise ValueError('Unregistered alpha.')
    if alpha==0: return g.copy()
    if alpha==1: return l.copy()
    return (1-alpha)*g+alpha*l


def select(train,signals,completed):
    prior.valid_probabilities(signals,3)
    if len(signals)!=len(train): raise ValueError('Signal alignment.')
    splits=list(GroupKFold(3).split(train,combined_label(train),train.QuestionId.astype(str)))
    candidates=[]; memories=[]
    for params in core.e001.GRID:
        scores=[]; parts=[]
        for left,right in splits:
            inner=train.iloc[left]; validation=train.iloc[right]
            fitted=core.fit_model(inner,'full_context','logistic',params)
            p,classes=core.predict(fitted,validation[FEATURES],'full_context')
            f,fc=core.e001.frequency_probabilities(inner,validation[FEATURES])
            if not np.array_equal(classes,fc): raise ValueError('Inner inventory differs.')
            y=combined_label(validation).to_numpy()
            scores.append(core.map_at_3(y,p,classes))
            parts.append((soft_project(f,classes,signals[right]),soft_project(p,classes,signals[right]),classes,y))
            completed()
        candidates.append({'params':{**params,'ngram_range':list(params['ngram_range'])},
            'inner_fold_map_at_3':scores,'inner_mean_map_at_3':float(np.mean(scores))})
        memories.append(parts)
    winner=int(np.argmax([r['inner_mean_map_at_3'] for r in candidates])); choices=[]
    for alpha in ALPHAS:
        scores=[core.map_at_3(y,blend(g,l,alpha),classes) for g,l,classes,y in memories[winner]]
        choices.append({'alpha':alpha,'inner_fold_map_at_3':scores,'inner_mean_map_at_3':float(np.mean(scores))})
    selected=int(np.argmax([r['inner_mean_map_at_3'] for r in choices]))
    return {'selected_index':winner,'candidates':candidates},{'selected_index':selected,
        'selected_alpha':ALPHAS[selected],'candidates':choices}


def raw_arms(f,l,classes,signals,alpha):
    g=soft_project(f,classes,signals); l7=soft_project(l,classes,signals)
    probabilities={'F':f,'L':l,'G7':g,'L7':l7,'U50':.5*g+.5*l,'C50':.5*g+.5*l7,
        'T':blend(g,l7,alpha)}
    return {a:prior.old.filter_output(p,classes,np.full(len(p),-1)) for a,p in probabilities.items()}


def calibrate(cal,ev,classes,truth,alpha,cal_fallback,ev_fallback):
    supported=int(np.isin(truth,classes).sum()); final={}; records={}
    for arm in ARMS:
        source=None; method='own_temperature'
        if arm=='F': source='F'; method='unscaled'
        elif arm=='G7' and np.all(cal_fallback) and np.all(ev_fallback):
            if not np.array_equal(cal[arm]['prob'],cal['F']['prob']) or not np.array_equal(ev[arm]['prob'],ev['F']['prob']):
                raise ValueError('Technical fallback identity differs.')
            source='F'; method='all_unknown_frequency'
        elif arm=='T' and alpha in (0.,.5,1.):
            source={0.:'G7',.5:'C50',1.:'L7'}[alpha]; method='component_reuse'
        if source is not None:
            final[arm]=ev[arm] if source==arm else final[source]
            temperature=1. if source==arm else records[source]['temperature']
        else:
            temperature,n=core.e001.temperature_scale(truth,cal[arm]['prob'],classes)
            if n!=supported: raise ValueError('Calibration support differs.')
            final[arm]=prior.old.filter_output(core.e001.apply_temperature(ev[arm]['prob'],temperature),classes,np.full(len(ev[arm]['prob']),-1))
        records[arm]={'temperature':temperature,'supported_n':supported,'method':method}
    return final,records


def prepare(train,cal,ev,positions,fold,train_signals,cal_signals,ev_signals,cal_fallback,ev_fallback,completed):
    if set(ev)!=set(FEATURES): raise ValueError('Evaluation features must be label-free.')
    groups=[set(x.QuestionId) for x in (train,cal,ev)]
    if list(map(len,groups))!=[9,3,3] or any(groups[i]&groups[j] for i in range(3) for j in range(i)):
        raise ValueError('Frozen roles differ.')
    for signals,flags,n in ((cal_signals,cal_fallback,len(cal)),(ev_signals,ev_fallback,len(ev))):
        if flags.shape!=(n,) or flags.dtype!=bool or np.any(flags & ~np.all(signals==[0,0,1],axis=1)):
            raise ValueError('Fallback provenance differs.')
    selection,choice=select(train,train_signals,completed)
    fitted=core.fit_model(train,'full_context','logistic',selection['candidates'][selection['selected_index']]['params']); completed()
    cp,classes=core.predict(fitted,cal[FEATURES],'full_context'); ep,ec=core.predict(fitted,ev,'full_context')
    cf,cc=core.e001.frequency_probabilities(train,cal[FEATURES]); ef,fc=core.e001.frequency_probabilities(train,ev)
    if not all(np.array_equal(classes,x) for x in (ec,cc,fc)): raise ValueError('Outer inventory differs.')
    alpha=choice['selected_alpha']; calplans=raw_arms(cf,cp,classes,cal_signals,alpha)
    raw=raw_arms(ef,ep,classes,ev_signals,alpha)
    final,records=calibrate(calplans,raw,classes,combined_label(cal).to_numpy(),alpha,cal_fallback,ev_fallback)
    if alpha in (0.,.5,1.): raw['T']=raw[{0.:'G7',.5:'C50',1.:'L7'}[alpha]]
    plans={a:{'raw':raw[a],'final':final[a],
        'order':prior._routing_order(final[a]['confidence'],positions.tolist(),fold,core.SEED)} for a in ARMS}
    memory={'raw':ep,'prob':final['L']['prob'],'category_raw':marginalize(ep,classes),'classes':classes,
        'frequency_prob':ef,'frequency_classes':fc,'positions':np.asarray(positions),'questions':ev.QuestionId.to_numpy(),
        'train_labels':combined_label(train).to_numpy(),'train_questions':train.QuestionId.to_numpy(),
        'order':plans['L']['order'],'frequency_order':plans['F']['order']}
    for value in memory.values(): value.setflags(write=False)
    for plan in plans.values(): plan['order'].setflags(write=False)
    d={'arm':'full_context','model':'logistic','fold':fold,'n_train':len(train),'n_calibration':len(cal),'n_evaluation':len(ev),
        'role_question_counts':[9,3,3],'selection':selection,'temperature':records['L']['temperature'],
        'calibration_supported_n':records['L']['supported_n'],'fits':10}
    absent=[not np.any(prior.old.prefixes(classes)==b) for b in (False,True)]
    fallback={'fold':fold,'missing_false_inventory':absent[0],'missing_true_inventory':absent[1],
        'false_projection_fallback_n':int(np.sum(ev_signals[:,0]>0)) if absent[0] else 0,
        'true_projection_fallback_n':int(np.sum(ev_signals[:,1]>0)) if absent[1] else 0}
    return (d,memory,None),plans,{'fold':fold,'alpha_selection':choice,'calibration':records,'projection_fallback':fallback}
