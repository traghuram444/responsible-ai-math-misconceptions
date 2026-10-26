"""E020 training-only ensemble selection and fixed calibration; no evaluator."""
import numpy as np
from sklearn.model_selection import GroupKFold
from . import e011_context as core,e020_fusion as fusion,e019_metrics as old
from .e014 import FEATURES
from .data_contract import combined_label
from .e016 import valid_probabilities
from .selective import _routing_order


def select(train,signal7,completed_fit):
    valid_probabilities(signal7,3)
    if len(signal7)!=len(train): raise ValueError('Training signal alignment.')
    splits=list(GroupKFold(3).split(train,combined_label(train),train.QuestionId.astype(str)))
    candidates=[]; memories=[]
    for params in core.e001.GRID:
        scores=[]; parts=[]
        for left,right in splits:
            inner=train.iloc[left]; validation=train.iloc[right]
            fitted=core.fit_model(inner,'full_context','logistic',params)
            prob,classes=core.predict(fitted,validation[FEATURES],'full_context')
            fp,fc=core.e001.frequency_probabilities(inner,validation[FEATURES])
            if not np.array_equal(classes,fc): raise ValueError('Inner training columns changed.')
            g=fusion.soft_project(fp,classes,signal7[right]); truth=combined_label(validation).to_numpy()
            scores.append(core.map_at_3(truth,prob,classes)); parts.append((fp,prob,g,classes,truth))
            completed_fit()
        candidates.append({'params':{**params,'ngram_range':list(params['ngram_range'])},
            'inner_fold_map_at_3':scores,'inner_mean_map_at_3':float(np.mean(scores))})
        memories.append(parts)
    winner=int(np.argmax([v['inner_mean_map_at_3'] for v in candidates]))
    hybrid=[]
    for weights in fusion.WEIGHTS:
        values=[core.map_at_3(y,fusion.mix(fp,p,g,weights),classes) for fp,p,g,classes,y in memories[winner]]
        hybrid.append({'weights':list(weights),'inner_fold_map_at_3':values,'inner_mean_map_at_3':float(np.mean(values))})
    plain=[r for r in hybrid if r['weights'][2]==0]
    hi=fusion.choose([r['inner_fold_map_at_3'] for r in hybrid])
    bi=fusion.choose([r['inner_fold_map_at_3'] for r in plain])
    return {'selected_index':winner,'candidates':candidates}, {
        'B':{'selected_index':bi,'selected_weights':plain[bi]['weights'],'candidates':plain},
        'H':{'selected_index':hi,'selected_weights':hybrid[hi]['weights'],'candidates':hybrid}}


def raw_arms(frequency,learned,classes,s15,s7,majority,weights):
    unknown=np.full(len(frequency),-1); decision=np.argmax(s7,axis=1); decision=np.where(decision==2,-1,decision)
    g15=fusion.soft_project(frequency,classes,s15); g7=fusion.soft_project(frequency,classes,s7)
    probabilities={'F':frequency,'L':learned,'G15':g15,'G7':g7,
        'L7':fusion.soft_project(learned,classes,s7),
        'B':fusion.mix(frequency,learned,g7,tuple(weights['B']['selected_weights'])),
        'H':fusion.mix(frequency,learned,g7,tuple(weights['H']['selected_weights']))}
    plans={a:old.filter_output(p,classes,unknown) for a,p in probabilities.items()}
    plans['F_M']=old.filter_output(frequency,classes,np.full(len(frequency),majority))
    plans['G7_hard']=old.filter_output(frequency,classes,decision)
    return {a:plans[a] for a in fusion.ARMS}


def calibrate(cal_plans,eval_plans,classes,cal_truth,weights,cal_signals,eval_signals):
    supported=int(np.isin(cal_truth,classes).sum()); final={}; records={}
    for arm in ('F','L','F_M','G15','G7','L7','B','H','G7_hard'):
        source=None; method='own_temperature'
        if arm in ('F','F_M','G7_hard'): source=arm; method='unscaled'
        elif arm in ('G15','G7'):
            if np.all(cal_signals[arm]==[0,0,1]) and np.all(eval_signals[arm]==[0,0,1]):
                if not np.array_equal(cal_plans[arm]['prob'],cal_plans['F']['prob']) or not np.array_equal(eval_plans[arm]['prob'],eval_plans['F']['prob']):
                    raise ValueError('All-unknown identity failed.')
                source='F'; method='all_unknown_frequency'
        elif arm in ('B','H'):
            selected=weights[arm]['selected_weights']
            if 1 in selected:
                source=('F','L','G7')[selected.index(1)]; method='component_endpoint'
        if source is not None:
            final[arm]=eval_plans[arm] if source==arm else final[source]
            temperature=1. if source==arm else records[source]['temperature']
        else:
            temperature,count=core.e001.temperature_scale(cal_truth,cal_plans[arm]['prob'],classes)
            if count!=supported: raise ValueError('Calibration support count.')
            p=core.e001.apply_temperature(eval_plans[arm]['prob'],temperature)
            final[arm]=old.filter_output(p,classes,np.full(len(p),-1))
        records[arm]={'temperature':temperature,'supported_n':supported,'method':method}
    return final,records


def prepare_parts(train,calibration,evaluation_features,positions,fold,train_s7,cal_signals,eval_signals,completed_fit):
    if set(evaluation_features)!=set(FEATURES): raise ValueError('Evaluation inputs must be label-free.')
    groups=[set(p.QuestionId) for p in (train,calibration,evaluation_features)]
    if list(map(len,groups))!=[9,3,3] or any(groups[i]&groups[j] for i in range(3) for j in range(i)):
        raise ValueError('Frozen question roles changed.')
    selection,weights=select(train,train_s7,completed_fit)
    fitted=core.fit_model(train,'full_context','logistic',selection['candidates'][selection['selected_index']]['params'])
    completed_fit()
    cal_p,classes=core.predict(fitted,calibration[FEATURES],'full_context')
    p,ec=core.predict(fitted,evaluation_features,'full_context')
    cf,cc=core.e001.frequency_probabilities(train,calibration[FEATURES]); ef,fc=core.e001.frequency_probabilities(train,evaluation_features)
    if not all(np.array_equal(classes,x) for x in (ec,cc,fc)): raise ValueError('Training class alignment.')
    maj,counts=old.majority(combined_label(train).to_numpy())
    calplans=raw_arms(cf,cal_p,classes,cal_signals['G15'],cal_signals['G7'],maj,weights)
    raw=raw_arms(ef,p,classes,eval_signals['G15'],eval_signals['G7'],maj,weights)
    final,calrecords=calibrate(calplans,raw,classes,combined_label(calibration).to_numpy(),weights,cal_signals,eval_signals)
    plans={a:{'raw':raw[a],'final':final[a],
        'order':_routing_order(final[a]['confidence'],positions.tolist(),fold,core.SEED)} for a in fusion.ARMS}
    memory={'raw':p,'prob':final['L']['prob'],'classes':classes,'frequency_prob':ef,'frequency_classes':fc,
        'positions':np.asarray(positions),'questions':evaluation_features.QuestionId.to_numpy(),
        'train_labels':combined_label(train).to_numpy(),'train_questions':train.QuestionId.to_numpy(),
        'order':plans['L']['order'],'frequency_order':plans['F']['order']}
    for value in memory.values():
        if isinstance(value,np.ndarray): value.setflags(write=False)
    for plan in plans.values(): plan['order'].setflags(write=False)
    description={'arm':'full_context','model':'logistic','fold':fold,'n_train':len(train),'n_calibration':len(calibration),
        'n_evaluation':len(evaluation_features),'role_question_counts':[9,3,3],'selection':selection,
        'temperature':calrecords['L']['temperature'],'calibration_supported_n':calrecords['L']['supported_n'],'fits':10}
    return description,memory,plans,{'fold':fold,'weights':weights,'calibration':calrecords,
        'majority_correctness':bool(maj),'training_counts':counts}
