"""E022 tests use invented inputs only; no MAP fitting, cutoff search or pilots."""
import copy
import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from map_misconceptions import e022_selection as s,e022_metrics as m,e022_publication as pub,e022_run as run
from map_misconceptions import threshold_transfer as tt
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.e019_metrics import filter_output


def script(name):
    path=Path(__file__).resolve().parents[1]/'scripts'/name
    spec=importlib.util.spec_from_file_location(name,path); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


@pytest.fixture(scope='module')
def experiment():
    memories={}; truths={}; development=[]; policies=[]; originals=[]; retained=[]; offset=0
    classes=np.array(['False_Correct:NA','False_Misconception:SYNTHETIC','True_Correct:NA'])
    for fold,n in enumerate([7339,7339,7339,7339,7340]):
        i=np.arange(n); questions=np.empty(n,dtype=int)
        for j,part in enumerate(np.array_split(i,3)): questions[part]=3*fold+j
        f=np.tile([.6,.01,.39],(n,1)); learned=np.full((n,3),.05); learned[i,i%3]=.9
        signals=np.tile([.05,.9,.05],(n,1)); signals[i%2==0]=[.9,.05,.05]
        raw=s.raw_predictions(f,learned,classes,signals)
        memory={'classes':classes,'positions':np.arange(offset,offset+n),'questions':questions,
            'train_labels':np.array([classes[0]]*600+[classes[1]]*10+[classes[2]]*390),'train_questions':np.arange(1000)%9+30}
        offset+=n
        candidates=[{'params':{**p,'ngram_range':list(p['ngram_range'])},'inner_fold_map_at_3':[.5]*3,'inner_mean_map_at_3':.5} for p in s.core.e001.GRID]
        choice={'selected_index':0,'candidates':candidates}
        for arm in s.ARMS:
            development.append({'arm':arm,'fold':fold,'role_counts':[9,1,2,3],'derived_role_sha256':f'{fold:064x}',
                'n_train':36696-n-1200,'n_calibration':1200,'n_evaluation':n,'selection':None if arm=='F' else choice,
                'temperature':1.,'temperature_n':0 if arm=='F' else 400,'temperature_supported_n':0 if arm=='F' else 350,
                'temperature_supported_fraction':None if arm=='F' else .875,'temperature_fallback':False,
                'method':'unscaled' if arm=='F' else 'own_temperature','projection_fallback':{'false_n':0,'true_n':0}})
            memory[arm+'_raw']=raw[arm]; memory[arm+'_final']=s.apply_temperature(raw[arm],1.,classes,arm)
            j=np.arange(800); roles=j//400
            score=np.full(800,.6) if arm=='F' else np.where(j%2==0,.9,.6)
            correct=j%5!=0 if arm=='F' else np.where(j%2==0,(j//2)%10!=0,(j//2)%2==0)
            for target in s.TARGETS:
                policy=tt.select_cutoff(score,correct,roles,target)
                policies.append({'arm':arm,'fold':fold,'policy':policy})
                memory[f'{arm}_keep_{target}']=tt.apply_cutoff(memory[arm+'_final'].max(axis=1),policy)
        for v in memory.values(): v.setflags(write=False)
        memories[fold]=memory
        truth=classes[i%3].astype(object); truth[::7]='False_Misconception:UNSUPPORTED_SYNTHETIC'; truths[fold]=truth
        u,r=m.evaluate(fold,memory,truth); originals.extend(u); retained.extend(r)
    payload={'experiment_id':'E022','status':'COMPLETED','development':development,'policies':policies,
        **m.panels(originals,retained,policies),'resources':{'image_id':'sha256:'+'a'*64,'wall_seconds':1.},
        'integrity':{'git_revision':'a'*40,'lock_sha256':'b'*64,'protocol_sha256':'c'*64,'reference_sha256':'d'*64,
            'g7_cache_sha256':'e'*64,'freeze_sha256':'f'*64,'preserved_files':500,'preservation_verified':True,
            'global_freeze_verified':True,'e018_remains_blocked':True,'model_fits':50,'new_model_calls':0,'fit_warnings':0,
            'reproduced_model_folds':15,'policies':45,'seed':20260831,'uid':10001,'gid':10001,'row_level_public_outputs':False}}
    return payload,memories,truths


def test_complete_report_and_registered_denominators(experiment):
    p,_,_=experiment; pub.validate(p); text=pub.render(p)
    assert [len(p[k]['records']) for k in ('unfiltered','retained','comparisons')]==[600,900,225]
    assert len(p['gaps'])==135 and len(p['policies'])==45 and len(p['development'])==15
    assert len(p['decisions'])==9 and sum(r['primary'] for r in p['decisions'])==2
    assert text.index('Primary decisions')<text.index('Aggregate retained')<text.index('Fold-level retained')
    assert 'UNSUPPORTED_SYNTHETIC' not in text and 'SYNTHETIC' not in text
    for row in p['retained']['records']:
        g=row['group']
        if row['arm']=='F' and row['target_percent']==10:
            assert g['retained_n']==0 and g['risk'] is None and g['risk_target_met'] is None
            if g['original_n']: assert g['coverage']==0 and g['review_fraction']==1


@pytest.mark.parametrize('damage',range(12))
def test_schema_arithmetic_privacy_and_selection_reject_corruption(experiment,damage):
    p=copy.deepcopy(experiment[0])
    if damage==0: p['private_response']='invented response'
    elif damage==1: p['retained']['records'].pop()
    elif damage==2: p['retained']['records'][0]['group']['risk']=0.
    elif damage==3: p['unfiltered']['records'][0]['group']['confidence_minus_accuracy']=.99
    elif damage==4: p['decisions'][0]['criterion_met']=True
    elif damage==5: p['policies'][0]['policy']['threshold']=.8
    elif damage==6: p['development'][1]['selection']['selected_index']=2
    elif damage==7: p['comparisons']['records'][0]['left_retained_n']+=1
    elif damage==8: p['gaps'][0]['development_risk']=.2
    elif damage==9: p['unfiltered']['records'][0]['question']=9999
    elif damage==10: p['development'][1]['temperature_supported_fraction']=0.
    else: p['retained']['aggregate'][0]['metrics']['risk']['defined_folds']+=1
    with pytest.raises(ValueError): pub.validate(p)


def test_temperature_exact_historical_objective_and_failure(monkeypatch):
    classes=np.array(['a','b','c']); prob=np.array([[.7,.2,.1],[.1,.3,.6],[.3,.6,.1],[.2,.5,.3]])
    truth=np.array(['a','b','absent','b'])
    assert s.temperature(truth,prob,classes)==s.core.e001.temperature_scale(truth,prob,classes)
    assert s.temperature(np.array(['absent']*4),prob,classes)==(1.,0)
    class Bad: success=False; x=0.; fun=1.
    monkeypatch.setattr(s,'minimize_scalar',lambda *a,**k:Bad())
    with pytest.raises(ValueError,match='optimization'): s.temperature(truth,prob,classes)


def test_projection_mixture_and_rank_checks():
    classes=np.array(['False_Correct:NA','False_Misconception:X','True_Correct:NA'])
    f=np.array([[.3,.3,.4],[.3,.3,.4]]); l=np.array([[.1,.3,.6],[.6,.3,.1]])
    signals=np.array([[.75,.25,0.],[0.,0.,1.]])
    plans=s.raw_predictions(f,l,classes,signals)
    assert np.allclose(plans['L7'][0],[.1875,.5625,.25])
    assert np.array_equal(plans['L7'][1],l[1])
    assert np.allclose(plans['C50'][0],[.28125,.46875,.25])
    old=filter_output(plans['L7'],classes,np.full(2,-1))
    predicted,top=s.ranks(plans['L7']); assert np.array_equal(predicted,old['predicted']) and np.array_equal(top,old['top'])
    with pytest.raises(ValueError,match='ranks'): s.apply_temperature(np.array([[1e-16,1e-15,1.]]),1.,classes,'L7')


def test_cutoffs_rational_bounds_ties_and_batch_invariance():
    scores=np.tile(np.r_[np.full(100,.9),np.full(100,.5)],2); roles=np.repeat([0,1],200)
    correct=np.ones(400,dtype=bool)
    for start in (0,200): correct[start:start+20]=False; correct[start+100:start+160]=False
    p=tt.select_cutoff(scores,correct,roles,20)
    assert p['threshold']==.9 and all(q['retained_n']==100 and q['incorrect_n']==20 for q in p['development'])
    assert tt.select_cutoff(scores,correct,roles,10)['status']=='NO_ADMISSIBLE_THRESHOLD'
    shifted=correct.copy(); shifted[20]=False
    assert tt.select_cutoff(scores,shifted,roles,20)['status']=='NO_ADMISSIBLE_THRESHOLD'
    sample=np.array([.8999999999,.9,.95,.3]); mask=tt.apply_cutoff(sample,p)
    assert mask.tolist()==[False,True,True,False]
    order=np.array([2,0,3,1]); assert np.array_equal(tt.apply_cutoff(sample[order],p),mask[order])
    assert np.array_equal(tt.apply_cutoff(np.r_[sample,.1,.99],p)[:4],mask)


def test_every_question_conjunction_and_separate_primary_flags(experiment):
    p=copy.deepcopy(experiment[0])
    # Isolated decision test: supply boundary-valued all-question summary records.
    for row in p['retained']['records']:
        if row['stratum']=='all' and row['target_percent']==20 and row['question'] is not None:
            g=row['group']; g.update(retained_n=1000,risk=.2,count_floor_met=True,coverage_floor_met=True,risk_target_met=True)
    decision=lambda: {r['arm']:r for r in m.panels(p['unfiltered']['records'],p['retained']['records'],p['policies'])['decisions'] if r['target_percent']==20}
    assert decision()['L7']['criterion_met'] and decision()['C50']['criterion_met']
    row=next(r for r in p['retained']['records'] if r['arm']=='L7' and r['target_percent']==20 and r['stratum']=='all' and r['question'] is not None)
    row['group'].update(risk=.201,risk_target_met=False)
    d=decision(); assert not d['L7']['criterion_met'] and d['C50']['criterion_met'] and d['L7']['risk_exceeded_questions']==1
    row['group'].update(retained_n=0,risk=None,count_floor_met=False,coverage_floor_met=False,risk_target_met=None)
    d=decision(); assert not d['L7']['criterion_met'] and d['L7']['risk_denominator']==14 and d['L7']['risk_exceeded_questions']==0


def test_nonmonotone_risk_search_and_unsupported_errors():
    score=np.tile(np.r_[np.full(100,.9),np.full(100,.8),np.full(100,.7)],2)
    correct=np.tile(np.r_[np.zeros(100,dtype=bool),np.ones(200,dtype=bool)],2)
    roles=np.repeat([0,1],300)
    assert tt.select_cutoff(score,correct,roles,30)['status']=='NO_ADMISSIBLE_THRESHOLD'
    # High-confidence unsupported labels are still incorrect; lower score tiers can improve risk.
    correct=np.tile(np.r_[np.r_[np.zeros(60,dtype=bool),np.ones(40,dtype=bool)],np.ones(200,dtype=bool)],2)
    policy=tt.select_cutoff(score,correct,roles,20)
    assert policy['status']=='SELECTED' and policy['threshold']==0. and all(r['risk']==.2 for r in policy['development'])


def test_preparation_disjoint_temperature_roles_and_frozen_policy(monkeypatch):
    classes=np.array(['False_Correct:NA','False_Misconception:SYNTHETIC','True_Correct:NA'])
    def frame(qs):
        ids=np.repeat(qs,250); i=np.arange(len(ids)); labels=classes[i%3]
        return pd.DataFrame({'QuestionId':ids,'QuestionText':['invented question '+str(q) for q in ids],
            'MC_Answer':(i%3).astype(str),'StudentExplanation':['invented explanation']*len(ids),
            'Category':[v.split(':')[0] for v in labels],'Misconception':[v.split(':')[1] for v in labels]})
    train,cal,ev=frame(range(9)),frame(range(9,12)),frame(range(12,15))
    fits=[]; choices=[]; temp_seen=[]; original_temp=s.temperature
    def fit(data,*args): fits.append(set(data.QuestionId)); return None
    def predict(model,data,*args):
        if set(data.QuestionId)==set(ev.QuestionId): assert len(choices)==9
        prob=np.full((len(data),3),.15); prob[np.arange(len(data)),data.MC_Answer.astype(int)]=.7
        return prob,classes
    def temp(y,p,c): temp_seen.append(len(y)); return original_temp(y,p,c)
    monkeypatch.setattr(s.core,'fit_model',fit); monkeypatch.setattr(s.core,'predict',predict); monkeypatch.setattr(s,'temperature',temp)
    calls=[]; signals=np.tile([.2,.6,.2],(750,1))
    d,p,memory=s.prepare(train,cal,ev[s.FEATURES],np.arange(750),0,signals,signals,lambda:calls.append(1),lambda:choices.append(1))
    assert len(fits)==len(calls)==10 and len(choices)==9 and temp_seen==[250,250]
    assert all(q<=set(range(9)) for q in fits) and fits[-1]==set(range(9))
    assert all(not v.flags.writeable for v in memory.values())
    assert d[1]['selection']['selected_index']==0 and d[1]['selection']==d[2]['selection']
    tq,cq=tt.calibration_roles(cal.QuestionId,0)
    serial=json.dumps({'fold':0,'temperature':tq,'threshold':cq},sort_keys=True,separators=(',',':'))
    import hashlib
    assert d[0]['derived_role_sha256']==hashlib.sha256(serial.encode()).hexdigest()
    with pytest.raises(ValueError,match='label-free'): s.prepare(train,cal,ev,np.arange(750),0,signals,signals,lambda:None,lambda:None)


def test_all_fold_freeze_historical_raw_reproduction_and_tamper(tmp_path,monkeypatch,experiment):
    p,memories,_=experiment; root=tmp_path; out=root/'new'; out.mkdir()
    digest=run.freeze(out,p['development'],p['policies'],memories,50)
    assert run.verify_freeze(out,digest)['policies']==p['policies']
    with pytest.raises(ValueError): run.freeze(root/'absent',p['development'],p['policies'][:-1],memories,50)
    previous=root/'artifacts/e021_attempt01'; previous.mkdir(parents=True); (root/'results').mkdir()
    files={}; historical=[]; roles=[]; exact=[]
    for fold,memory in memories.items():
        arrays={'memory_'+k:memory[k] for k in ('classes','positions','questions','train_labels','train_questions')}
        for arm in s.ARMS:
            prob=memory[arm+'_raw']; predicted,top=s.ranks(prob)
            arrays.update({arm+'_raw_prob':prob,arm+'_raw_predicted':predicted,arm+'_raw_top':top})
        path=previous/f'fold_{fold}_frozen_private.npz'
        with path.open('xb') as stream: np.savez_compressed(stream,**arrays)
        files[path.name]=sha(path)
        d=next(r for r in p['development'] if r['arm']=='L7' and r['fold']==fold)
        historical.append({k:d[k] for k in ('fold','selection','n_train','n_calibration','n_evaluation')})
        roles.append({'fold':fold,'derived_role_sha256':d['derived_role_sha256']})
    for r in p['unfiltered']['records']:
        if r['scale']=='raw': exact.append({k:r[k] for k in ('arm','fold','question','stratum','scale')}|
            {'n':r['group']['original_n'],'metrics':{k:r['group'][k] for k in ('map_at_3','top1_accuracy')}})
    write_new(previous/'frozen_development_private.json',{'prediction_sha256':files})
    write_new(root/'results/E021_aggregates.json',{'development':historical,'exact':{'records':exact}})
    write_new(root/'results/E007_aggregates.json',{'development':roles})
    monkeypatch.setattr(run,'FROZEN',sha(previous/'frozen_development_private.json')); monkeypatch.setattr(run,'REFERENCE',sha(root/'results/E021_aggregates.json'))
    run.reproduce_private(root,p['development'],memories); run.reproduce_scores(root,p['unfiltered']['records'])
    bad=copy.deepcopy(p['development']); bad[1]['derived_role_sha256']='f'*64
    with pytest.raises(ValueError): run.reproduce_private(root,bad,memories)
    damaged={**memories,0:{**memories[0],'L7_raw':memories[0]['L7_raw'][:,::-1]}}
    with pytest.raises(ValueError): run.reproduce_private(root,p['development'],damaged)
    with (out/'fold_0_frozen_private.npz').open('ab') as stream: stream.write(b'changed')
    with pytest.raises(ValueError): run.verify_freeze(out,digest)


def test_global_truth_boundary_and_read_only_monitor():
    import inspect
    source=inspect.getsource(run.run)
    assert source.index('freeze_sha=freeze(')<source.index('reproduce_private(')<source.index('truths=')<source.index('metrics.evaluate(')
    assert source.index('reproduce_scores(')<source.index('latest_metrics=')
    launcher=script('run_e022.py')
    for stage,n,total in [('Training: classifier fits 23/50; fold 3/5',23,50),('Development: policies 45/45; fold 5/5',45,45),('Scoring: evaluation folds 2/5; all policies frozen',2,5)]:
        state={'status':'RUNNING','stage':stage,'progress':{'completed':77,'total':100}}
        view=launcher.view(state); assert view['progress']['completed']==n and view['progress']['total']==total
        assert state['progress']['completed']==77
    assert 'subprocess.run' not in inspect.getsource(launcher.monitor)
    assert 'AutoModel' not in source and 'temperature_scale(' not in source
