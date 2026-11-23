"""Invented E023 inputs only; no MAP pilot or outcome-dependent settings."""
import copy
import ast
import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from map_misconceptions import e023_selection as s,e023_metrics as m,e023_publication as pub,e023_run as run
from map_misconceptions import e022_run as oldrun,e009_reliability as prior
from map_misconceptions.e019_checker import sha,write_new


def load_test():
    spec=importlib.util.spec_from_file_location('e022_test_fixture',Path(__file__).with_name('test_e022.py'))
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module


@pytest.fixture(scope='module')
def experiment():
    old,original,truths=load_test().experiment.__wrapped__()
    policies=[]; routers=[]; cross=[]; counts=[]; memories={}; review=[]; automation=[]; ranking=[]
    for fold,orig in original.items():
        memory={k:v.copy() for k,v in orig.items()}; n=len(memory['positions']); scores={}
        for a,r in s.REVIEW:
            scores[a,r]=(memory[a+'_final'].max(axis=1) if r in ('confidence','frequency','raw_confidence') else
                np.zeros(n) if r=='hash_only' else np.linspace(.01,.99,n) if r=='R5' else np.linspace(.99,.01,n))
            memory[f'score_{a}_{r}']=scores[a,r]
            for b,keep in s.review_masks(scores[a,r],memory['positions'],fold).items():
                memory[f'review_{a}_{r}_{b}']=keep
                counts.append({'arm':a,'rule':r,'fold':fold,'review_percent':b,'original_n':n,'retained_n':int(keep.sum())})
        for a,r in s.AUTO:
            for t in s.TARGETS:
                policy=copy.deepcopy(next(p['policy'] for p in old['policies'] if p['fold']==fold and p['arm']==a and p['policy']['target_percent']==t))
                policies.append({'arm':a,'rule':r,'fold':fold,'policy':policy})
                memory[f'auto_{a}_{r}_{t}']=s.tt.apply_cutoff(scores[a,r],policy)
        train_n=next(d['n_train'] for d in old['development'] if d['fold']==fold)
        ns=[len(x) for x in np.array_split(np.arange(train_n),3)]; cs=[x//2 for x in ns]
        choice=next(d['selection'] for d in old['development'] if d['fold']==fold and d['arm']=='L7')
        cross.append({'fold':fold,'role_sha256':f'{fold:064x}','blocks':[{'block':b,'fitting_questions':6,'held_questions':3,
            'fitting_n':train_n-ns[b],'held_n':ns[b],'selection':choice,'correct_n':{a:cs[b] for a in s.ARMS},'classifier_fits':10} for b in range(3)]})
        for a in s.ARMS:
            for r,width in [('R5',5),('R8',8)]: routers.append({'arm':a,'rule':r,'fold':fold,'n':train_n,'correct_n':sum(cs),'incorrect_n':train_n-sum(cs),
                'question_count':9,'feature_count':width,'weight_sum':float(train_n),'status':'FITTED','constant':None,'fitting_calls':1,'convergence_warnings':0})
        for v in memory.values(): v.flags.writeable=False
        memories[fold]=memory
        rr,aa,kk=m.evaluate(fold,memory,truths[fold]); review.extend(rr); automation.extend(aa); ranking.extend(kk)
    payload={'experiment_id':'E023','status':'COMPLETED','development':old['development'],'policies':policies,'routers':routers,'crossfit':cross,
        **m.panels(review,automation,ranking,policies),'resources':{'image_id':'sha256:'+'a'*64,'wall_seconds':1.},
        'integrity':{'git_revision':'a'*40,'lock_sha256':'b'*64,'protocol_sha256':'c'*64,'reference_sha256':'d'*64,'g7_cache_sha256':'e'*64,
            'freeze_sha256':'f'*64,'preserved_files':500,'preservation_verified':True,'global_freeze_verified':True,'e018_remains_blocked':True,
            'model_fits':200,'router_preparations':20,'router_fits':20,'new_model_calls':0,'fit_warnings':0,'reproduced_model_folds':15,
            'reproduced_unfiltered_records':600,'reproduced_cutoff_records':900,'reproduced_policies':45,'policies':165,'review_masks':390,
            'seed':20260831,'uid':10001,'gid':10001,'row_level_public_outputs':False}}
    return payload,memories,counts,old,original,truths


def test_complete_numeric_schema_grids_and_render(experiment):
    p,*_=experiment; pub.validate(p); text=pub.render(p)
    assert [len(p[k]['records']) for k in ('review','automation','ranking')]==[7800,3300,1300]
    assert len(p['review']['comparisons']['records'])==1500 and len(p['automation']['comparisons']['records'])==750
    assert len(p['ranking']['comparisons']['records'])==250
    assert len(p['automation']['gaps'])==495 and len(p['automation']['decisions'])==33
    assert text.index('Primary review decisions')<text.index('Separate automation decisions')
    assert 'UNSUPPORTED_SYNTHETIC' not in text and 'False_Correct:NA' not in text


@pytest.mark.parametrize('case',range(9))
def test_strict_schema_and_arithmetic_reject_corruption(experiment,case):
    p=copy.deepcopy(experiment[0])
    if case==0: p['review']['records'][0]['private_response']='not allowed'
    elif case==1: p['review']['records'].pop()
    elif case==2: p['automation']['records'][0]['group']['incorrect_n']+=1
    elif case==3: p['review']['decisions'][0]['criterion_met']=not p['review']['decisions'][0]['criterion_met']
    elif case==4: p['routers'][0]['feature_count']=8
    elif case==5: p['ranking']['records'][0]['group']['auroc']=float('nan')
    elif case==6: p['review']['aggregate'][0]['metrics']['risk']['defined_folds']+=1
    elif case==7: p['crossfit'][0]['blocks'][0]['held_n']+=1
    elif case==8: p['policies'][0]['policy']['threshold']=1.01
    with pytest.raises(ValueError): pub.validate(p)


def test_checker_disagreement_entropy_and_unknown():
    classes=np.array(['False_Correct:NA','True_Correct:NA']); l=np.tile([.25,.75],(4,1))
    signals=np.array([[.25,.75,0],[1,0,0],[0,0,1],[1/3]*3])
    x=s.checker_features(l,classes,signals)
    np.testing.assert_allclose(x[:,0],[0,.75,1,.4166666666666667]); assert x[2,1]==0 and x[2,2]==1
    np.testing.assert_allclose(x[3,1],1)
    with pytest.raises(ValueError): s.checker_features(l,np.array(['OTHER','True_Correct:NA']),signals)


def test_router_exact_E009_match_and_extra_width():
    rng=np.random.default_rng(112); x=rng.uniform(size=(450,8)); y=(x[:,0]+x[:,6]>.9); qs=np.arange(450)%9
    actual,meta=s.fit_router(x[:,:5],y,qs); expected,oldmeta=prior.fit_router(x[:,:5],y,qs)
    np.testing.assert_allclose(actual.score(x[:,:5]),expected.score(x[:,:5]),atol=0,rtol=0); assert meta==oldmeta
    enhanced,metadata=s.fit_router(x,y,qs); assert metadata['feature_count']==8 and np.isfinite(enhanced.score(x)).all()
    constant,metadata=s.fit_router(x,np.ones(450,bool),qs); assert metadata['fitting_calls']==0
    assert np.all(constant.score(x)==1)
    with pytest.raises(ValueError): enhanced.score(x[:,:5])
    with pytest.raises(ValueError): s.fit_router(np.full((450,8),np.nan),y,qs)


def test_review_ties_quota_nesting_and_permutation():
    n=103; score=np.ones(n)*.5; ids=np.arange(n); masks=s.review_masks(score,ids,2)
    perm=np.arange(n)[::-1]; changed=s.review_masks(score[perm],ids[perm],2)
    for b in s.BUDGETS:
        assert masks[b].sum()==n-n*b//100 and not masks[b].flags.writeable
        np.testing.assert_array_equal(masks[b][perm],changed[b])
        if b: assert np.all(~masks[b]|masks[b-10])
    with pytest.raises(ValueError): s.review_masks(score,np.zeros(n,int),2)


def test_primary_review_boundary_and_automation_separate(experiment):
    assert m.primary_decision([2.]*5)['criterion_met']
    assert not m.primary_decision([1.999]*5)['criterion_met']
    assert not m.primary_decision([4.,4.,4.,0.,0.])['criterion_met']
    p=experiment[0]
    assert len(p['review']['decisions'])==2
    assert sum(r['primary'] for r in p['automation']['decisions'])==2
    assert all(r['target_percent']==20 for r in p['automation']['decisions'] if r['primary'])


def test_freeze_reproduction_and_tamper(experiment,tmp_path,monkeypatch):
    p,memories,counts,old,original,_=experiment; out=tmp_path/'new'; out.mkdir()
    digest=run.freeze(out,p['development'],p['policies'],p['routers'],p['crossfit'],counts,memories,200)
    assert len(run.verify_freeze(out,digest)['review_counts'])==390
    with pytest.raises(FileExistsError): run.freeze(out,p['development'],p['policies'],p['routers'],p['crossfit'],counts,memories,200)
    oldout=tmp_path/'artifacts/e022_attempt01'; oldout.mkdir(parents=True); (tmp_path/'results').mkdir()
    olddigest=oldrun.freeze(oldout,old['development'],old['policies'],original,50)
    write_new(tmp_path/'results/E022_aggregates.json',old)
    monkeypatch.setattr(run,'FROZEN',olddigest); monkeypatch.setattr(run,'REFERENCE',sha(tmp_path/'results/E022_aggregates.json'))
    run.reproduce_private(tmp_path,p['development'],p['policies'],memories)
    run.reproduce_metrics(tmp_path,old['unfiltered']['records'],old['retained']['records'])
    with (out/'fold_0_frozen_private.npz').open('ab') as f:f.write(b'changed')
    with pytest.raises(ValueError): run.verify_freeze(out,digest)


def test_prepare_nested_isolation_and_sealed_policies(monkeypatch):
    classes=np.array(['False_Correct:NA','True_Correct:NA']); counts={'fits':0,'routers':0,'policies':0}; calls=[]
    def frame(qs,n):
        q=np.repeat(qs,n); i=np.arange(len(q)); return pd.DataFrame({'QuestionId':q,'QuestionText':['invented question']*len(q),
            'MC_Answer':['invented answer']*len(q),'StudentExplanation':['invented explanation']*len(q),
            'Category':np.where(i%2,'True_Correct','False_Correct'),'Misconception':['NA']*len(q)})
    train,cal,ev=frame(np.arange(9),25),frame(np.arange(9,12),250),frame(np.arange(12,15),10)
    def select(f,arm,model,callback):
        calls.append(set(f.QuestionId)); assert len(calls[-1]) in (6,9)
        for _ in range(9):callback()
        return {'selected_index':0,'candidates':[{'params':{**p,'ngram_range':list(p['ngram_range'])},'inner_fold_map_at_3':[.5]*3,'inner_mean_map_at_3':.5} for p in s.core.e001.GRID]}
    monkeypatch.setattr(s.core,'select_params',select)
    monkeypatch.setattr(s.core,'fit_model',lambda f,*args:set(f.QuestionId))
    def query(model,fit,features,signals):
        assert set(features)==set(s.FEATURES) and not model&set(features.QuestionId)
        if set(features.QuestionId)==set(ev.QuestionId): assert counts=={'fits':40,'routers':4,'policies':33}
        n=len(features); i=np.arange(n); l=np.column_stack((.1+.8*(i%2),.9-.8*(i%2))); freq=np.tile([.5,.5],(n,1))
        raw=s.old.raw_predictions(freq,l,classes,signals)
        xs={a:np.column_stack((prior.numeric_features(raw[a],classes,s.combined_label(fit).to_numpy(),np.full(n,.5)),s.checker_features(l,classes,signals))) for a in s.ARMS}
        return raw,classes,xs
    monkeypatch.setattr(s,'query',query)
    def tick(key): counts[key]+=1
    sig=lambda f:np.tile([.3,.6,.1],(len(f),1))
    d,p,r,x,review,memory=s.prepare(train,cal,ev[s.FEATURES],np.arange(len(ev)),0,sig(train),sig(cal),sig(ev),lambda:tick('fits'),lambda:tick('routers'),lambda:tick('policies'))
    assert [len(c) for c in calls]==[6,6,6,9]
    assert len(d)==3 and len(p)==33 and len(r)==4 and len(review)==78
    assert all(not v.flags.writeable for v in memory.values())
    assert counts=={'fits':40,'routers':4,'policies':33}
    assert all(sum(q in c for c in calls[:3])==2 for q in range(9))
    with pytest.raises(ValueError): s.prepare(train,cal,ev,np.arange(len(ev)),0,sig(train),sig(cal),sig(ev),lambda:None,lambda:None,lambda:None)


def test_global_truth_barrier_and_viewer():
    source=Path(run.__file__).read_text()
    tree=ast.parse(source); body=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='run')
    calls={}
    for n in ast.walk(body):
        if isinstance(n,ast.Call): calls.setdefault(ast.unparse(n.func),[]).append(n.lineno)
    truth_line=next(n.lineno for n in ast.walk(body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='truths' for t in n.targets))
    assert calls['freeze'][0]<calls['reproduce_private'][0]<truth_line<calls['old_metrics.evaluate'][0]<calls['reproduce_metrics'][0]<calls['metrics.evaluate'][0]
    assert 'new_model_calls\':0' in source
    path=Path(__file__).resolve().parents[1]/'scripts/run_e023.py'
    spec=importlib.util.spec_from_file_location('viewer',path); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    for stage,n,total in [('Training: classifier fits 37/200; fold 1/5',37,200),('Routers: preparations 4/20; fold 1/5',4,20),('Development: policies 33/165; fold 1/5',33,165)]:
        assert module.view({'stage':stage,'status':'RUNNING'})['progress']=={'completed':n,'total':total,'percent':round(n/total*100,1)}
