"""Approved E022 development-only reconstruction, temperatures and fixed cutoffs."""
import hashlib
import json
import numpy as np
from scipy.optimize import minimize_scalar
from . import e011_context as core, threshold_transfer as tt
from .data_contract import combined_label
from .e014 import FEATURES
from .e016 import valid_probabilities
from .e020_fusion import soft_project

ARMS=('F','L7','C50')
TARGETS=tt.TARGETS


def temperature(truth, prob, classes):
    # Same E001 objective/bounds/default optimizer, with explicit failure checking.
    valid_probabilities(prob,len(classes))
    index={v:i for i,v in enumerate(classes)}
    keep=np.array([v in index for v in truth])
    if not keep.any(): return 1.,0
    y=np.array([index[v] for v in truth[keep]])
    logits=np.log(np.clip(prob[keep],1e-12,1.))
    def nll(log_t):
        scaled=logits/np.exp(log_t); scaled-=scaled.max(axis=1,keepdims=True)
        p=np.exp(scaled); p/=p.sum(axis=1,keepdims=True)
        return float(-np.log(p[np.arange(len(y)),y]).mean())
    result=minimize_scalar(nll,bounds=(-3.,3.),method='bounded')
    value=float(np.exp(result.x))
    if not result.success or not np.isfinite(result.fun) or not np.isfinite(value) or value<=0:
        raise ValueError('Temperature optimization failed.')
    return value,int(keep.sum())


def raw_predictions(f,l,classes,signals):
    g=soft_project(f,classes,signals); l7=soft_project(l,classes,signals)
    return {'F':f,'L7':l7,'C50':.5*g+.5*l7}


def ranks(prob):
    top=np.full((len(prob),3),-1,dtype=np.int64)
    top[:,:min(3,prob.shape[1])]=np.argsort(-prob,axis=1)[:,:3]
    return np.argmax(prob,axis=1),top


def apply_temperature(prob,value,classes,arm):
    final=prob.copy() if arm=='F' else core.e001.apply_temperature(prob,value)
    valid_probabilities(final,len(classes))
    if any(not np.array_equal(a,b) for a,b in zip(ranks(prob),ranks(final))):
        raise ValueError('Temperature changed prediction ranks.')
    return final


def prepare(train,cal,ev,positions,fold,cal_signals,ev_signals,fitted,selected):
    if set(ev)!=set(FEATURES): raise ValueError('Evaluation input must be label-free.')
    groups=[set(x.QuestionId) for x in (train,cal,ev)]
    if list(map(len,groups))!=[9,3,3] or any(groups[i]&groups[j] for i in range(3) for j in range(i)):
        raise ValueError('Frozen question roles differ.')
    temp_q,cutoff_q=tt.calibration_roles(cal.QuestionId,fold)
    cq=cal.QuestionId.map(tt.canonical_question).to_numpy()
    temp=cq==temp_q; dev=~temp
    roles=np.array([cutoff_q.index(q) for q in cq[dev]])
    serial=json.dumps({'fold':fold,'temperature':temp_q,'threshold':cutoff_q},sort_keys=True,separators=(',',':'))
    role_hash=hashlib.sha256(serial.encode()).hexdigest()
    choice=core.select_params(train,'full_context','logistic',fitted)
    model=core.fit_model(train,'full_context','logistic',choice['candidates'][choice['selected_index']]['params']); fitted()
    cp,classes=core.predict(model,cal[FEATURES],'full_context')
    cf,fc=core.e001.frequency_probabilities(train,cal[FEATURES])
    if not np.array_equal(classes,fc): raise ValueError('Training inventory differs.')
    cal_raw=raw_predictions(cf,cp,classes,cal_signals)
    cal_y=combined_label(cal).to_numpy(); development=[]; policies=[]
    prefix=np.array([str(v).startswith('True_') for v in classes])
    for arm in ARMS:
        value,supported=(1.,0) if arm=='F' else temperature(cal_y[temp],cal_raw[arm][temp],classes)
        scores=apply_temperature(cal_raw[arm][dev],value,classes,arm)
        confidence=scores.max(axis=1); correct=classes[np.argmax(scores,axis=1)]==cal_y[dev]
        for target in TARGETS:
            policies.append({'arm':arm,'fold':fold,'policy':tt.select_cutoff(confidence,correct,roles,target)}); selected()
        development.append({'arm':arm,'fold':fold,'role_counts':[9,1,2,3],'derived_role_sha256':role_hash,
            'n_train':len(train),'n_calibration':len(cal),'n_evaluation':len(ev),
            'selection':None if arm=='F' else choice,'temperature':value,
            'temperature_n':0 if arm=='F' else int(temp.sum()),'temperature_supported_n':supported,
            'temperature_supported_fraction':None if arm=='F' else supported/int(temp.sum()),
            'temperature_fallback':bool(arm!='F' and supported==0),'method':'unscaled' if arm=='F' else 'own_temperature',
            'projection_fallback':{str(b).lower()+'_n':int(np.sum(ev_signals[:,int(b)]>0))
                if arm!='F' and not np.any(prefix==b) else 0 for b in (False,True)}})
    # Seal policies before using evaluation features for prediction or routing.
    sealed=json.dumps({'development':development,'policies':policies},sort_keys=True)
    ep,ec=core.predict(model,ev,'full_context'); ef,fc=core.e001.frequency_probabilities(train,ev)
    if not all(np.array_equal(classes,c) for c in (ec,fc)): raise ValueError('Evaluation columns differ.')
    raw=raw_predictions(ef,ep,classes,ev_signals)
    memory={'classes':classes,'positions':np.asarray(positions),'questions':ev.QuestionId.to_numpy(),
        'train_labels':combined_label(train).to_numpy(),'train_questions':train.QuestionId.to_numpy()}
    for arm in ARMS:
        record=next(r for r in development if r['arm']==arm)
        memory[arm+'_raw']=raw[arm]
        memory[arm+'_final']=apply_temperature(raw[arm],record['temperature'],classes,arm)
        for p in policies:
            if p['arm']==arm:
                memory[f'{arm}_keep_{p["policy"]["target_percent"]}']=tt.apply_cutoff(memory[arm+'_final'].max(axis=1),p['policy'])
    if sealed!=json.dumps({'development':development,'policies':policies},sort_keys=True):
        raise ValueError('Frozen policy mutated.')
    for v in memory.values(): v.setflags(write=False)
    return development,policies,memory
