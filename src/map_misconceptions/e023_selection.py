"""Locked E023 matched reliability ablation; no evaluation outcomes here."""
import hashlib
import json
import warnings
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from . import e022_selection as old, e009_reliability as prior
from .e014 import FEATURES
from .data_contract import combined_label
from .selective import _routing_order

core,tt=old.core,old.tt
ARMS=('L7','C50')
RULES=('R5','R8','confidence','raw_confidence','support_aware','hash_only')
REVIEW=tuple((a,r) for a in ARMS for r in RULES)+(('F','frequency'),)
AUTO=tuple((a,r) for a,r in REVIEW if r!='hash_only')
BUDGETS=(0,10,20,30,40,50)
TARGETS=tt.TARGETS


def checker_features(raw_l,classes,signals):
    old.valid_probabilities(raw_l,len(classes)); old.valid_probabilities(signals,3)
    false=np.array([str(v).startswith('False_') for v in classes])
    true=np.array([str(v).startswith('True_') for v in classes])
    if not np.all(false|true) or len(raw_l)!=len(signals): raise ValueError('Checker feature inventory/alignment.')
    b=np.column_stack((raw_l[:,false].sum(axis=1),raw_l[:,true].sum(axis=1),np.zeros(len(raw_l))))
    log=np.zeros_like(signals); np.log(signals,out=log,where=signals>0)
    return np.column_stack((.5*np.abs(signals-b).sum(axis=1),-(signals*log).sum(axis=1)/np.log(3),signals[:,2]))


def similarity(model,train,query):
    vectorizer,_=model
    reference=vectorizer.transform(core.input_text(train,'full_context'))
    matrix=vectorizer.transform(core.input_text(query,'full_context'))
    if not len(train): raise ValueError('Empty similarity reference.')
    values=np.empty(len(query))
    for start in range(0,len(query),128): values[start:start+128]=(matrix[start:start+128]@reference.T).max(axis=1).toarray().ravel()
    if not np.isfinite(values).all(): raise ValueError('Nonfinite similarity.')
    return np.clip(values,0,1)


def query(model,train,features,signals):
    if set(features)!=set(FEATURES): raise ValueError('Label-free query required.')
    l,classes=core.predict(model,features,'full_context'); f,fc=core.e001.frequency_probabilities(train,features)
    if not np.array_equal(classes,fc): raise ValueError('Class alignment.')
    raw=old.raw_predictions(f,l,classes,signals)
    sim=similarity(model,train,features); extra=checker_features(l,classes,signals)
    xs={a:np.column_stack((prior.numeric_features(raw[a],classes,combined_label(train).to_numpy(),sim),extra)) for a in ARMS}
    return raw,classes,xs


class Router:
    def __init__(self,scaler,model,constant,width): self.scaler,self.model,self.constant,self.width=scaler,model,constant,width
    def score(self,x):
        if x.ndim!=2 or x.shape[1]!=self.width or not np.isfinite(x).all(): raise ValueError('Router query.')
        z=self.scaler.transform(x)
        p=np.full(len(x),self.constant,dtype=float) if self.constant is not None else self.model.predict_proba(z)[:,list(self.model.classes_).index(1)]
        if not np.isfinite(p).all() or np.any((p<0)|(p>1)): raise ValueError('Router score.')
        return p


def fit_router(x,y,questions):
    if x.ndim!=2 or x.shape[1] not in (5,8) or x.shape[0]!=len(y) or y.dtype!=bool or not np.isfinite(x).all(): raise ValueError('Router inputs.')
    w=prior.equal_question_weights(questions)
    scaler=StandardScaler(with_mean=True,with_std=True).fit(x,sample_weight=w)
    if not np.isfinite(scaler.mean_).all() or not np.isfinite(scaler.scale_).all(): raise ValueError('Router scaler.')
    constant=int(y[0]) if len(np.unique(y))==1 else None; model=None
    if constant is None:
        model=LogisticRegression(**prior.ROUTER_PARAMS)
        with warnings.catch_warnings():
            warnings.simplefilter('error'); model.fit(scaler.transform(x),y.astype(int),sample_weight=w)
        if not np.isfinite(model.coef_).all() or not np.isfinite(model.intercept_).all(): raise ValueError('Router coefficients.')
    meta={'n':len(y),'correct_n':int(y.sum()),'incorrect_n':int((~y).sum()),'question_count':9,'feature_count':x.shape[1],
        'weight_sum':float(w.sum()),'status':'FITTED' if constant is None else 'CONSTANT_CORRECTNESS_FALLBACK',
        'constant':constant,'fitting_calls':int(constant is None),'convergence_warnings':0}
    return Router(scaler,model,constant,x.shape[1]),meta


def tuned(train,fitted):
    choice=core.select_params(train,'full_context','logistic',fitted)
    model=core.fit_model(train,'full_context','logistic',choice['candidates'][choice['selected_index']]['params']); fitted()
    return model,choice


def crossfit(train,signals,fold,fitted,router_ready):
    blocks=prior.crossfit_blocks(train.QuestionId,fold); canonical=train.QuestionId.map(tt.canonical_question).to_numpy()
    xs={a:np.empty((len(train),8)) for a in ARMS}; ys={a:np.empty(len(train),bool) for a in ARMS}; visits=np.zeros(len(train),int); records=[]
    for block,held_q in enumerate(blocks):
        held=np.isin(canonical,held_q); fit=train.iloc[np.flatnonzero(~held)]; query_frame=train.iloc[np.flatnonzero(held)]
        if fit.QuestionId.nunique()!=6 or query_frame.QuestionId.nunique()!=3: raise ValueError('Crossfit question roles.')
        model,choice=tuned(fit,fitted)
        raw,classes,x=query(model,fit,query_frame[FEATURES],signals[held])
        correct={a:classes[raw[a].argmax(axis=1)]==combined_label(query_frame).to_numpy() for a in ARMS}
        for a in ARMS: xs[a][held]=x[a]; ys[a][held]=correct[a]
        visits[held]+=1
        records.append({'block':block,'fitting_questions':6,'held_questions':3,'fitting_n':len(fit),'held_n':len(query_frame),
            'selection':choice,'correct_n':{a:int(correct[a].sum()) for a in ARMS},'classifier_fits':10})
    if not np.all(visits==1): raise ValueError('Crossfit coverage.')
    routers={}; metadata=[]
    for a in ARMS:
        for rule,width in [('R5',5),('R8',8)]:
            routers[a,rule],meta=fit_router(xs[a][:,:width],ys[a],train.QuestionId.to_numpy())
            metadata.append({'arm':a,'rule':rule,'fold':fold,**meta}); router_ready()
    serial=json.dumps({'fold':fold,'blocks':blocks},sort_keys=True,separators=(',',':'))
    return routers,metadata,{'fold':fold,'role_sha256':hashlib.sha256(serial.encode()).hexdigest(),'blocks':records}


def scores(raw,final,xs,routers):
    result={('F','frequency'):final['F'].max(axis=1)}
    for a in ARMS:
        for rule in RULES:
            result[a,rule]=(routers[a,rule].score(xs[a][:,:5 if rule=='R5' else 8]) if rule in ('R5','R8') else
                final[a].max(axis=1) if rule=='confidence' else raw[a].max(axis=1) if rule=='raw_confidence' else
                final[a].max(axis=1)*xs[a][:,3] if rule=='support_aware' else np.zeros(len(final[a])))
    return result


def review_masks(score,positions,fold):
    score=np.asarray(score); positions=np.asarray(positions)
    if score.shape!=positions.shape or score.ndim!=1 or not len(score) or not np.isfinite(score).all() or np.any((score<0)|(score>1)):
        raise ValueError('Review scores.')
    if positions.dtype.kind not in 'iu' or np.any(positions<0) or len(np.unique(positions))!=len(positions) or fold not in range(5): raise ValueError('Review identifiers.')
    order=_routing_order(score,positions.tolist(),fold,20260831); result={}
    for b in BUDGETS:
        keep=np.zeros(len(score),bool); keep[order[:len(score)-len(score)*b//100]]=True; keep.flags.writeable=False; result[b]=keep
    return result


def prepare(train,cal,ev,positions,fold,train_signals,cal_signals,ev_signals,fitted,router_ready,selected):
    if set(ev)!=set(FEATURES): raise ValueError('Evaluation input must be label-free.')
    groups=[set(x.QuestionId) for x in (train,cal,ev)]
    if list(map(len,groups))!=[9,3,3] or any(groups[i]&groups[j] for i in range(3) for j in range(i)): raise ValueError('Outer roles changed.')
    routers,router_metadata,crossfit_record=crossfit(train,train_signals,fold,fitted,router_ready)
    model,choice=tuned(train,fitted)
    cal_raw,classes,cx=query(model,train,cal[FEATURES],cal_signals)
    temp_q,cutoff_q=tt.calibration_roles(cal.QuestionId,fold); cq=cal.QuestionId.map(tt.canonical_question).to_numpy(); temp=cq==temp_q; dev=~temp
    roles=np.array([cutoff_q.index(q) for q in cq[dev]])
    serial=json.dumps({'fold':fold,'temperature':temp_q,'threshold':cutoff_q},sort_keys=True,separators=(',',':'))
    role_hash=hashlib.sha256(serial.encode()).hexdigest(); cal_y=combined_label(cal).to_numpy(); development=[]; policies=[]; final={}
    prefix=np.array([str(v).startswith('True_') for v in classes])
    for a in old.ARMS:
        value,supported=(1.,0) if a=='F' else old.temperature(cal_y[temp],cal_raw[a][temp],classes)
        final[a]=old.apply_temperature(cal_raw[a],value,classes,a)
        development.append({'arm':a,'fold':fold,'role_counts':[9,1,2,3],'derived_role_sha256':role_hash,
            'n_train':len(train),'n_calibration':len(cal),'n_evaluation':len(ev),'selection':None if a=='F' else choice,'temperature':value,
            'temperature_n':0 if a=='F' else int(temp.sum()),'temperature_supported_n':supported,
            'temperature_supported_fraction':None if a=='F' else supported/int(temp.sum()),'temperature_fallback':bool(a!='F' and supported==0),
            'method':'unscaled' if a=='F' else 'own_temperature','projection_fallback':{str(b).lower()+'_n':int(np.sum(ev_signals[:,int(b)]>0))
                if a!='F' and not np.any(prefix==b) else 0 for b in (False,True)}})
    cs=scores(cal_raw,final,cx,routers)
    for a,r in AUTO:
        correct=classes[final[a][dev].argmax(axis=1)]==cal_y[dev]
        for target in TARGETS:
            policies.append({'arm':a,'rule':r,'fold':fold,'policy':tt.select_cutoff(cs[a,r][dev],correct,roles,target)}); selected()
    # Development and all cutoff policies are sealed before evaluation feature use.
    sealed=json.dumps([development,policies,router_metadata,crossfit_record],sort_keys=True)
    raw,ec,ex=query(model,train,ev,ev_signals)
    if not np.array_equal(ec,classes): raise ValueError('Evaluation inventory.')
    final={a:old.apply_temperature(raw[a],next(d['temperature'] for d in development if d['arm']==a),classes,a) for a in old.ARMS}
    es=scores(raw,final,ex,routers)
    memory={'classes':classes,'positions':np.asarray(positions),'questions':ev.QuestionId.to_numpy(),
        'train_labels':combined_label(train).to_numpy(),'train_questions':train.QuestionId.to_numpy()}
    for a in old.ARMS: memory[a+'_raw']=raw[a]; memory[a+'_final']=final[a]
    counts=[]
    for a,r in REVIEW:
        memory[f'score_{a}_{r}']=es[a,r]
        for b,keep in review_masks(es[a,r],positions,fold).items():
            memory[f'review_{a}_{r}_{b}']=keep
            counts.append({'arm':a,'rule':r,'fold':fold,'review_percent':b,'original_n':len(keep),'retained_n':int(keep.sum())})
    for p in policies:
        a,r,t=p['arm'],p['rule'],p['policy']['target_percent']; keep=tt.apply_cutoff(es[a,r],p['policy']); memory[f'auto_{a}_{r}_{t}']=keep
        if r in ('confidence','frequency'): memory[f'{a}_keep_{t}']=keep
    if sealed!=json.dumps([development,policies,router_metadata,crossfit_record],sort_keys=True): raise ValueError('Development mutation.')
    for v in memory.values(): v.flags.writeable=False
    return development,policies,router_metadata,crossfit_record,counts,memory
