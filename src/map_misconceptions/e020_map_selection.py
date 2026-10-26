"""MAP phase carries fallback provenance into the registered calibration identity.

The initial readiness helpers remain byte-locked. Reuse their selection/fusion;
distinguish technical fallback from a valid C readout, including numerical zeros.
"""
import numpy as np
from . import e020_selection as base
from .data_contract import combined_label


def calibrate(calplans,evalplans,classes,truth,weights,cal_fallback,eval_fallback):
    supported=int(np.isin(truth,classes).sum()); final={}; records={}
    for arm in ('F','L','F_M','G15','G7','L7','B','H','G7_hard'):
        source=None; method='own_temperature'
        if arm in ('F','F_M','G7_hard'): source=arm; method='unscaled'
        elif arm in ('G15','G7') and np.all(cal_fallback[arm]) and np.all(eval_fallback[arm]):
            if not np.array_equal(calplans[arm]['prob'],calplans['F']['prob']) or not np.array_equal(evalplans[arm]['prob'],evalplans['F']['prob']):
                raise ValueError('Technical all-unknown identity failed.')
            source='F'; method='all_unknown_frequency'
        elif arm in ('B','H'):
            chosen=weights[arm]['selected_weights']
            if 1 in chosen: source=('F','L','G7')[chosen.index(1)]; method='component_endpoint'
        if source is not None:
            final[arm]=evalplans[arm] if source==arm else final[source]
            temperature=1. if source==arm else records[source]['temperature']
        else:
            temperature,count=base.core.e001.temperature_scale(truth,calplans[arm]['prob'],classes)
            if count!=supported: raise ValueError('Calibration support count.')
            p=base.core.e001.apply_temperature(evalplans[arm]['prob'],temperature)
            final[arm]=base.old.filter_output(p,classes,np.full(len(p),-1))
        records[arm]={'temperature':temperature,'supported_n':supported,'method':method}
    return final,records


def prepare(train,calibration,evaluation_features,positions,fold,train_s7,cal_signals,eval_signals,cal_fallback,eval_fallback,completed_fit):
    if set(evaluation_features)!=set(base.FEATURES): raise ValueError('Evaluation inputs must be label-free.')
    groups=[set(p.QuestionId) for p in (train,calibration,evaluation_features)]
    if list(map(len,groups))!=[9,3,3] or any(groups[i]&groups[j] for i in range(3) for j in range(i)): raise ValueError('Frozen question roles changed.')
    for signals,flags,n in ((cal_signals,cal_fallback,len(calibration)),(eval_signals,eval_fallback,len(evaluation_features))):
        for key in ('G15','G7'):
            if flags[key].shape!=(n,) or flags[key].dtype!=bool: raise ValueError('Fallback provenance alignment.')
            if np.any(flags[key] & ~np.all(signals[key]==[0,0,1],axis=1)): raise ValueError('Fallback vector mismatch.')
    selection,weights=base.select(train,train_s7,completed_fit)
    fitted=base.core.fit_model(train,'full_context','logistic',selection['candidates'][selection['selected_index']]['params']); completed_fit()
    cp,classes=base.core.predict(fitted,calibration[base.FEATURES],'full_context')
    ep,ec=base.core.predict(fitted,evaluation_features,'full_context')
    cf,cc=base.core.e001.frequency_probabilities(train,calibration[base.FEATURES]); ef,fc=base.core.e001.frequency_probabilities(train,evaluation_features)
    if not all(np.array_equal(classes,x) for x in (ec,cc,fc)): raise ValueError('Training columns changed.')
    majority,counts=base.old.majority(combined_label(train).to_numpy())
    calplans=base.raw_arms(cf,cp,classes,cal_signals['G15'],cal_signals['G7'],majority,weights)
    raw=base.raw_arms(ef,ep,classes,eval_signals['G15'],eval_signals['G7'],majority,weights)
    final,records=calibrate(calplans,raw,classes,combined_label(calibration).to_numpy(),weights,cal_fallback,eval_fallback)
    plans={a:{'raw':raw[a],'final':final[a],'order':base._routing_order(final[a]['confidence'],positions.tolist(),fold,base.core.SEED)} for a in base.fusion.ARMS}
    memory={'raw':ep,'prob':final['L']['prob'],'classes':classes,'frequency_prob':ef,'frequency_classes':fc,
        'positions':np.asarray(positions),'questions':evaluation_features.QuestionId.to_numpy(),'train_labels':combined_label(train).to_numpy(),
        'train_questions':train.QuestionId.to_numpy(),'order':plans['L']['order'],'frequency_order':plans['F']['order']}
    for value in memory.values():
        if isinstance(value,np.ndarray): value.setflags(write=False)
    for plan in plans.values(): plan['order'].setflags(write=False)
    description={'arm':'full_context','model':'logistic','fold':fold,'n_train':len(train),'n_calibration':len(calibration),'n_evaluation':len(evaluation_features),
        'role_question_counts':[9,3,3],'selection':selection,'temperature':records['L']['temperature'],
        'calibration_supported_n':records['L']['supported_n'],'fits':10}
    return description,memory,plans,{'fold':fold,'weights':weights,'calibration':records,'majority_correctness':bool(majority),'training_counts':counts}
