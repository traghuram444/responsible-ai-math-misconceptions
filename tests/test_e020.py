"""Synthetic arrays and fake model plumbing only; never load a checkpoint."""
from contextlib import nullcontext
import copy
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
import pytest
from map_misconceptions import e020_checker as c,e020_fusion as f


def test_exact_protocol_prompt_and_fixtures():
    root=Path(__file__).resolve().parents[1]
    protocol=(root/'docs/E020_PROTOCOL.md').read_text()
    assert '```text\n'+c.SYSTEM+'\n```' in protocol
    assert '```text\n'+c.READOUT+'\n```' in protocol
    assert len(c.FIXTURES)==12
    for q,a,ref in c.FIXTURES: assert f'| {q} | {a} | {"ABC"[ref]} |' in protocol
    assert c.OVERRIDES=={**c.OLD_OVERRIDES,'max_new_tokens':512}
    assert c.SEED==20261026


@pytest.mark.parametrize('q,a,length,expected',[
 ('','<X>',9999,'missing_input'),('q','<X>',9999,'special_token_input'),
 ('q','a',2048,None),('q','a',2049,'initial_too_long'),('NA','NA',1,None)])
def test_input_gates(q,a,length,expected):
    assert c.input_reason(q,a,['<X>'],length)==expected


def test_readout_label_only_and_unicode():
    m=c.messages('x','é')
    assert len(m)==2 and m[1]['content']=='{"question":"x","proposed_answer":"é"}'
    assert c.normalize(' e\u0301\r\n ')=='é'


class Tokenizer:
    all_special_tokens=['<X>']; all_special_ids=[99]
    def __init__(self,initial=3,readout=5,text='assessment'):
        self.initial=initial; self.readout=readout; self.text=text; self.histories=[]; self.decoded=None
    def encode(self,x,**kw): assert kw=={'add_special_tokens':False}; return [{'A':0,'B':1,'C':2}[x]]
    def decode(self,ids,**kw):
        assert kw=={'skip_special_tokens':False,'clean_up_tokenization_spaces':False}
        self.decoded=ids; return self.text
    def apply_chat_template(self,history,**kw):
        assert kw=={'tokenize':True,'add_generation_prompt':True,'return_tensors':'pt'}
        self.histories.append(copy.deepcopy(history))
        return np.zeros((1,self.initial if len(history)==2 else self.readout),dtype=int)


def test_single_token_gate():
    t=Tokenizer(); assert c.candidate_tokens(t)==[0,1,2]
    t.all_special_ids=[1]
    with pytest.raises(ValueError): c.candidate_tokens(t)
    t=Tokenizer(); t.encode=lambda x,**k:[0]
    with pytest.raises(ValueError): c.candidate_tokens(t)
    t.encode=lambda x,**k:[0,1]
    with pytest.raises(ValueError): c.candidate_tokens(t)


@pytest.mark.parametrize('tokens,truncated', [([4,151645],False),([4,151643],False),([4],True),([],True)])
def test_rationale_eos_and_cap(tokens,truncated):
    t=Tokenizer(); text,cap,reason=c.decode_rationale(tokens,t)
    assert (text,cap,reason)==('assessment',truncated,None)
    assert t.decoded==(tokens if truncated else tokens[:-1])


def test_rationale_special_rejected_not_repaired():
    assert c.decode_rationale([4,151645],Tokenizer(text='text<X>'))[2]=='rationale_special_token'


def test_readout_probabilities_mass_and_ties():
    p,mass=c.readout_scores([0,0,0,0],[0,1,2])
    np.testing.assert_allclose(p,[1/3]*3); assert mass==pytest.approx(.75)
    assert np.argmax(p)==0
    p,mass=c.readout_scores([1000,1001,999,1002],[0,1,2])
    assert np.argmax(p)==1 and 0<mass<1
    for values in ([0,np.nan,1],[0,np.inf,1],[[0,1,2]]):
        with pytest.raises(ValueError): c.readout_scores(values,[0,1,2])


class Tensor:
    def __init__(self,x): self.x=np.asarray(x)
    def __getitem__(self,key): return Tensor(self.x[key])
    def to(self,**kwargs): assert kwargs=={'dtype':'float64'}; return self
    def numpy(self): return self.x


class Model:
    def __init__(self,tokens=(8,151645),logits=(0,2,1,3)):
        self.tokens=tokens; self.logits=logits; self.generated=0; self.read=0
    def generate(self,**kwargs):
        self.generated+=1; assert kwargs['generation_config']=='config'
        np.testing.assert_array_equal(kwargs['attention_mask'],np.ones_like(kwargs['input_ids']))
        return np.concatenate([kwargs['input_ids'],np.asarray([self.tokens])],axis=1)
    def __call__(self,**kwargs):
        self.read+=1; assert set(kwargs)=={'input_ids','attention_mask'}
        return SimpleNamespace(logits=Tensor([[self.logits]]))


@pytest.fixture
def fake_torch(monkeypatch):
    monkeypatch.setitem(sys.modules,'torch',SimpleNamespace(inference_mode=nullcontext,ones_like=np.ones_like,float64='float64'))


def test_two_stage_forward_and_no_parser(fake_torch):
    t=Tokenizer(text='No FINAL marker here'); model=Model()
    r=c.check_pair('q','a',model,t,'config')
    assert r['reason']=='readout_completed' and r['decision']==1
    assert model.generated==model.read==1 and len(t.histories)==2
    assert t.histories[1][2:]==[{'role':'assistant','content':'No FINAL marker here'},{'role':'user','content':c.READOUT}]


@pytest.mark.parametrize('q,a,t,reason,generations,reads',[
 ('','a',Tokenizer(),'missing_input',0,0),('q','<X>',Tokenizer(),'special_token_input',0,0),
 ('q','a',Tokenizer(initial=2049),'initial_too_long',0,0),
 ('q','a',Tokenizer(text='<X>'),'rationale_special_token',1,0),
 ('q','a',Tokenizer(readout=3073),'readout_too_long',1,0)])
def test_complete_fallback_paths(fake_torch,q,a,t,reason,generations,reads):
    m=Model(); r=c.check_pair(q,a,m,t,'config')
    assert r['reason']==reason and r['scores']==[0,0,1] and r['decision']==2
    assert (m.generated,m.read)==(generations,reads)


def test_cap_still_readout_boundary_and_empty_rationale(fake_torch):
    r=c.check_pair('q','a',Model(tokens=(8,)),Tokenizer(initial=2048,readout=3072,text=''),'config')
    assert r['truncated_rationale'] and r['reason']=='readout_completed' and r['completion']==''


def synthetic_results(fake_torch):
    rows=[]
    for q,a,expected in c.FIXTURES:
        logits=[0.,0.,0.,0.]; logits[expected]=3
        rows.append(c.check_pair(q,a,Model(logits=logits),Tokenizer(),'config'))
    return rows


def test_readiness_semantic_thresholds(fake_torch):
    rows=synthetic_results(fake_torch)
    assert c.gate_summary(rows,'G7')['gate_passed']
    for i in range(2): rows[i].update(scores=[0,0,1],decision=2)
    assert c.gate_summary(rows,'G7')['gate_passed']
    rows[2].update(scores=[0,0,1],decision=2)
    assert not c.gate_summary(rows,'G7')['gate_passed']
    assert c.gate_summary(rows,'G15')['gate_passed']
    rows=synthetic_results(fake_torch); rows[10].update(scores=[1,0,0],decision=0)
    assert not c.gate_summary(rows,'G7')['gate_passed']
    rows[0]['reason']='missing_input'
    assert not c.gate_summary(rows,'G15')['gate_passed']


def test_readiness_summary_has_no_private_fields(fake_torch):
    summary=c.gate_summary(synthetic_results(fake_torch),'G7')
    assert not {'completion','scores','question','answer','decision'}&set(summary)
    assert summary['projected_map_seconds']>0
    with pytest.raises(ValueError): c.gate_summary([], 'G7')


@pytest.fixture
def base():
    return np.array([[.4,.1,.3,.2],[.25,.25,.25,.25]]),np.array(['False_Correct:NA','False_Neither:NA','True_Correct:NA','True_Neither:NA'])


def test_fusion_unknown_and_binary_marginal_identity(base):
    p,y=base
    np.testing.assert_array_equal(f.soft_project(p,y,np.array([[0.,0.,1.]]*2)),p)
    scores=np.column_stack([p[:,:2].sum(axis=1),p[:,2:].sum(axis=1),np.zeros(2)])
    np.testing.assert_allclose(f.soft_project(p,y,scores),p,atol=1e-12,rtol=0)


def test_fusion_soft_no_truth_and_wrong_information(base):
    p,y=base; r=f.soft_project(p,y,np.array([[.2,.7,.1],[1.,0.,0.]]))
    np.testing.assert_allclose(r[0],[.2,.05,.45,.3]); np.testing.assert_array_equal(r[1],[.5,.5,0,0])
    assert r[0,0]<p[0,0]


def test_absent_prefix_and_zero_mass(base):
    p,y=base; np.testing.assert_allclose(f.soft_project(p[:,:2]*2,y[:2],np.array([[0,1,0]]*2)),p[:,:2]*2)
    with pytest.raises(ValueError): f.soft_project(np.array([[1.,0.]]),y[[0,2]],np.array([[0,1,0]]))
    with pytest.raises(ValueError): f.soft_project(p,y,np.ones((2,3)))


def test_grid_order_endpoints_and_edge(base):
    assert len(f.WEIGHTS)==len(set(f.WEIGHTS))==15 and f.WEIGHTS[0]==(1.,0.,0.)
    assert [x[1] for x in f.WEIGHTS if x[2]==0]==list(f.LAMBDAS)
    assert f.choose(np.zeros((15,3)))==0
    p,y=base; g=p[:,::-1]; learned=p*.8+.05
    for i in range(3):
        w=tuple(float(k==i) for k in range(3))
        np.testing.assert_array_equal(f.mix(p,learned,g,w),(p,learned,g)[i])
    for w in f.WEIGHTS: np.testing.assert_allclose(f.mix(p,learned,g,w).sum(axis=1),1)
    with pytest.raises(ValueError): f.mix(p,learned,g,(.2,.3,.5))
    with pytest.raises(ValueError): f.choose([[1,2]])


def test_meaningful_fixed_boundaries():
    assert f.meaningful([.025,.025,.025,.025,0])
    assert not f.meaningful([.019]*5)
    assert not f.meaningful([.1,.1,.1,0,0])
    with pytest.raises(ValueError): f.meaningful([.1]*4)


def test_no_map_entrypoint_in_readiness_launcher():
    text=(Path(__file__).resolve().parents[1]/'scripts/run_e020_readiness.py').read_text()
    assert "'synthetic','--model',key" in text
    assert 'READY_FOR_MAP_IMPLEMENTATION_CHECK' in text
    assert 'e019_run' not in text and 'data/raw' not in text


def test_calibration_endpoints_and_unknown_identity(base):
    from map_misconceptions import e020_selection as selection
    p,y=base; l=p*.8+.05; unknown=np.array([[0.,0.,1.]]*2)
    weights={'B':{'selected_weights':[0.,1.,0.]},'H':{'selected_weights':[0.,0.,1.]}}
    raw=selection.raw_arms(p,l,y,unknown,unknown,0,weights)
    final,records=selection.calibrate(raw,raw,y,np.array([y[0],y[2]]),weights,
        {'G15':unknown,'G7':unknown},{'G15':unknown,'G7':unknown})
    assert final['B'] is final['L'] and final['H'] is final['G7'] and final['G7'] is final['F']
    assert final['G15'] is final['F']
    assert records['G7']['method']=='all_unknown_frequency'
    np.testing.assert_array_equal(final['G7_hard']['prob'],p)


def test_inner_selection_training_only_counts_and_nine_fits(monkeypatch):
    import pandas as pd
    from map_misconceptions import e020_selection as selection
    train=pd.DataFrame({'QuestionId':list(range(9)),'QuestionText':['q']*9,'MC_Answer':['a']*9,
        'StudentExplanation':['x']*9,'Category':['False_Misconception']*9,'Misconception':[str(i) for i in range(9)]})
    fit_questions=[]; predictions=[]
    def fit(part,*args):
        fit_questions.append(set(part.QuestionId)); return part.copy()
    def predict(fitted,features,*args):
        assert set(features)==set(selection.FEATURES)
        assert not set(fitted.QuestionId)&set(features.QuestionId)
        prob,classes=selection.core.e001.frequency_probabilities(fitted,features)
        assert len(classes)==6
        predictions.append(len(features)); return prob,classes
    monkeypatch.setattr(selection.core,'fit_model',fit); monkeypatch.setattr(selection.core,'predict',predict)
    calls=[]
    sel,weights=selection.select(train,np.array([[0.,0.,1.]]*9),lambda:calls.append(1))
    assert len(calls)==len(fit_questions)==len(predictions)==9
    assert sel['selected_index']==0
    assert weights['B']['selected_weights']==weights['H']['selected_weights']==[1.,0.,0.]
    assert len(weights['B']['candidates'])==5 and len(weights['H']['candidates'])==15
    assert all(r['inner_mean_map_at_3']==0 for r in weights['H']['candidates'])


def test_evaluation_truth_rejected_before_fitting():
    import pandas as pd
    from map_misconceptions import e020_selection as selection
    evaluation=pd.DataFrame(columns=[*selection.FEATURES,'Category'])
    with pytest.raises(ValueError,match='label-free'):
        selection.prepare_parts(None,None,evaluation,None,0,None,None,None,None)


def public_readiness_model(fake_torch,key='G7'):
    p=c.gate_summary(synthetic_results(fake_torch),key)
    p.update(status='COMPLETED',wall_seconds=60.,peak_rss_bytes=1024,container_peak_bytes=2048,
        model_manifest_sha256='a'*64,environment_lock_sha256='b'*64,readiness_lock_sha256='c'*64)
    return p


def test_readiness_schema_private_fields_and_arithmetic(fake_torch):
    from map_misconceptions import e020_readiness_publication as pub
    p=public_readiness_model(fake_torch)
    assert pub.validate_model(p) is p
    for key,value in [('completion','private'),('binary_correct',11),('gate_passed',False),
                      ('projected_map_seconds',-1),('mean_readout_seconds',-1),('wall_seconds',-1),
                      ('container_peak_bytes',24*1024**3+1)]:
        bad=copy.deepcopy(p); bad[key]=value
        with pytest.raises((ValueError,TypeError)): pub.validate_model(bad)


@pytest.mark.parametrize('projection,status',[(48*3600,'READY_FOR_MAP_IMPLEMENTATION_CHECK'),
                                            (48*3600+1,'RUNTIME_REVIEW_REQUIRED')])
def test_readiness_runtime_rule(fake_torch,projection,status):
    from map_misconceptions import e020_readiness_publication as pub
    rows=[public_readiness_model(fake_torch,key) for key in ('G15','G7')]
    for r in rows:
        r['mean_readout_seconds']=1.
        r['tokens_per_second']=512/(projection/120-1)
        r['generation_seconds']=r['generated_tokens']/r['tokens_per_second']
        r['projected_map_seconds']=projection/2
    p={'map_started':False,'automatic_retry':False,'model_receipts':rows,
       'status':status,'projected_map_seconds':projection}
    assert pub.validate(p) is p
    p['map_started']=True
    with pytest.raises(ValueError): pub.validate(p)


def test_readiness_failure_gate_and_model_sequence(fake_torch):
    from map_misconceptions import e020_readiness_publication as pub
    rows=[public_readiness_model(fake_torch,key) for key in ('G15','G7')]
    rows[-1].update(binary_correct=7,gate_passed=False)
    p={'map_started':False,'automatic_retry':False,'model_receipts':rows,'status':'GATE_FAILED','failed_model':'G7'}
    assert pub.validate(p) is p
    p['model_receipts']=rows[::-1]
    with pytest.raises(ValueError): pub.validate(p)


def test_independent_monitor_never_starts_idle_work(tmp_path):
    import importlib.util
    from datetime import datetime,timezone
    path=Path(__file__).resolve().parents[1]/'scripts/monitor_e020.py'
    spec=importlib.util.spec_from_file_location('monitor_e020_test',path)
    monitor=importlib.util.module_from_spec(spec); spec.loader.exec_module(monitor)
    assert monitor.snapshot(tmp_path) is None
    (tmp_path/'attempt.json').write_text(json.dumps({'started_utc':datetime.now(timezone.utc).isoformat()}))
    (tmp_path/'G15_status.json').write_text(json.dumps({'progress':{'completed':12}}))
    (tmp_path/'G7_status.json').write_text(json.dumps({'progress':{'completed':7}}))
    (tmp_path/'orchestration_failure.json').write_text(json.dumps({'status':'FAILED'}))
    state=monitor.snapshot(tmp_path)
    assert state['status']=='FAILED' and state['progress']['completed']==19
    assert state['latest_metrics']=={} and state['progress']['total']==24
