"""Synthetic E014 tests only; no MAP training data is loaded."""
from copy import deepcopy
import inspect
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from map_misconceptions import e014 as c, e014_publication as p, e013 as prior
from map_misconceptions import e011_context as core
from map_misconceptions.data_contract import combined_label
from map_misconceptions.e011_publication import same


def synthetic():
    return pd.DataFrame([{'QuestionId':q,'QuestionText':f'synthetic exercise {q}','MC_Answer':str(i%2),
        'StudentExplanation':f'synthetic explanation variant {i%3}',
        'Category':'True_Correct' if i%2 else 'False_Misconception',
        'Misconception':'NA' if i%2 else 'SyntheticError'} for q in range(15) for i in range(8)])


def assignments(frame,fold):
    return pd.DataFrame({f'fold_{fold}':np.where(frame.QuestionId//3==fold,'evaluation',
        np.where(frame.QuestionId//3==(fold+1)%5,'calibration','train'))})


def test_endpoints_are_exact_objects_and_class_alignment():
    f=np.array([[.5,.5],[.6,.4]]); l=np.array([[.1,.9],[.8,.2]]); classes=np.array(['a','b'])
    assert c.mix(f,l,classes,classes,0) is f
    assert c.mix(f,l,classes,classes,1) is l
    np.testing.assert_array_equal(c.mix(f,l,classes,classes,.25),.75*f+.25*l)
    with pytest.raises(ValueError): c.mix(f,l,classes,classes[::-1],.25)
    with pytest.raises(ValueError): c.mix(f,l,classes,classes,.33)
    with pytest.raises(ValueError): c.mix(f[:1],l,classes,classes,.25)


def test_selection_reproduces_e011_and_only_inner_training_frequency(monkeypatch):
    f=synthetic(); train=f[f.QuestionId<9]; calls=[]; counts=[]
    historical=core.select_params(train,'full_context','logistic',lambda:None)
    original=core.e001.frequency_probabilities
    def frequency(part,validation):
        assert part.QuestionId.nunique()==6 and validation.QuestionId.nunique()==3
        assert not set(part.QuestionId)&set(validation.QuestionId)
        assert set(validation)==set(c.FEATURES)
        counts.append(len(part))
        return original(part,validation)
    monkeypatch.setattr(core.e001,'frequency_probabilities',frequency)
    selected,weight=c.select(train,lambda:calls.append(1))
    same(selected,historical)
    assert len(calls)==9 and len(counts)==9
    p.check_selection(weight,c.WEIGHTS,'weight')


def test_sequential_selection_ties_choose_first_and_no_heldout_classes(monkeypatch):
    f=synthetic(); train=f[f.QuestionId<9]
    monkeypatch.setattr(core,'map_at_3',lambda *args: .5)
    selected,weight=c.select(train,lambda:None)
    assert selected['selected_index']==0 and weight['selected_weight']==0
    # Every inner partition has its own class inventory; unknown truths score zero.
    prob=np.array([[.6,.4]]); classes=np.array(['a','b'])
    assert prior.row_scores(np.array(['never-trained']),*prior.rank_labels(prob,classes))['map_at_3'][0]==0


@pytest.mark.parametrize('weight',c.WEIGHTS)
def test_calibration_order_and_endpoint_identity(monkeypatch,weight):
    raw=np.array([[.8,.2],[.2,.8]]); freq=np.tile([.6,.4],(2,1)); classes=np.array(['a','b'])
    truth=np.array(['a','b']); scaled=core.e001.apply_temperature(raw,2.)
    calls=[]
    def fit(y,prob,cc):
        np.testing.assert_array_equal(prob,c.mix(freq,raw,classes,classes,weight))
        calls.append(1); return 3.,2
    monkeypatch.setattr(core.e001,'temperature_scale',fit)
    r,final,t,n,method=c.calibrate_mixture(weight,raw,raw,freq,freq,classes,classes,truth,2.,scaled)
    assert n==2
    if weight==0:
        assert r is freq and final is freq and t==1 and not calls and method=='unscaled_frequency'
    elif weight==1:
        assert r is raw and final is scaled and t==2 and not calls and method=='e011_temperature'
    else:
        assert len(calls)==1 and t==3 and method=='mixture_temperature'
        np.testing.assert_array_equal(final,core.e001.apply_temperature(r,3.))


def test_prepare_matches_control_and_ignores_evaluation_targets():
    f=synthetic(); a=assignments(f,0); calls=[]
    d,m=c.prepare(f,a,0,lambda:calls.append(1))
    original,om=core.prepare(f,a,'full_context','logistic',0,lambda:None)
    same(d['E011'],original)
    np.testing.assert_array_equal(m['E011']['prob'],om['prob'])
    assert len(calls)==10
    changed=f.copy(); changed.loc[a.fold_0=='evaluation',['Category','Misconception']]=['HIDDEN','TARGET']
    d2,m2=c.prepare(changed,a,0,lambda:None)
    same(d,d2)
    for model in c.MODELS:
        np.testing.assert_array_equal(m[model]['prob'],m2[model]['prob'])
        assert not m[model]['prob'].flags.writeable and not m[model]['order'].flags.writeable
    with pytest.raises(ValueError):
        c.prepare_parts(f[f.QuestionId<9],f[(f.QuestionId>=9)&(f.QuestionId<12)],f[f.QuestionId>=12],np.arange(24),0,lambda:None)


def test_mapping_exactly_e013_explanation_only_and_donor_equivalence():
    f=synthetic(); a=assignments(f,0); d,memories=c.prepare(f,a,0,lambda:None)
    m=memories['mixture']; meta=f.iloc[m['positions']][c.FEATURES]
    actual=c.mappings(meta,m['positions'],0); old=prior.mappings(meta,m['positions'],0)
    assert set(actual)=={'explanation_shuffle'}
    np.testing.assert_array_equal(actual['explanation_shuffle']['donors'],old['explanation_shuffle']['donors'])
    donor=actual['explanation_shuffle']['donors'][0]
    text=core.input_text(meta,'full_context').to_numpy()
    perturbed=meta.copy(); perturbed.StudentExplanation=meta.StudentExplanation.to_numpy()[donor]
    np.testing.assert_array_equal(core.input_text(perturbed,'full_context').to_numpy(),text[donor])
    # Frequency is invariant and temperature is rowwise, so indexing commutes with the mixture pipeline.
    weight=d['weight_selection']['selected_weight']; raw=memories['E011']['raw']; fp=m['frequency_prob']; cc=m['classes']
    np.testing.assert_array_equal(c.mix(fp,raw[donor],cc,cc,weight),c.mix(fp,raw,cc,cc,weight)[donor])


def test_global_freeze_and_reproduction_gates_before_new_scores():
    source=inspect.getsource(c.main)
    assert source.index("write_new(output/'frozen_development.json'")<source.index('truths =')<source.index('prior.check_reproduction(')<source.index('score_fold(')
    assert "for model in ('E011','frequency','mixture')" in source
    assert "if model == 'frequency' and fold == 4:" in source
    assert 'reproduction_diagnostic(' in source
    assert 'ResilientStatus(' in source
    assert 'core.prepare(' not in inspect.getsource(c.prepare_parts)


def test_primary_exact_margin_and_frequency_only_failure():
    def rows(deltas):
        return [{'model':m,'fold':f,'question':None,'stratum':'all','original':{'map_at_3':deltas[f] if m=='mixture' else 0.}}
                for m in c.MODELS for f in range(5)]
    assert c.primary(rows([.020]*5))['frequency']['criterion_met']
    assert not c.primary(rows([.019999]*5))['frequency']['criterion_met']
    assert not c.primary(rows([.1,.1,.1,0,0]))['frequency']['criterion_met']
    assert not c.primary(rows([0]*5))['frequency']['criterion_met']


@pytest.fixture(scope='module')
def payload():
    f=synthetic(); dev=[]; rows=[]; opportunities=[]; diagnostics=[]; routes=[]
    for fold in range(5):
        d,memories=c.prepare(f,assignments(f,fold),fold,lambda:None); dev.append(d)
        m=memories['E011']; meta=f.iloc[m['positions']][c.FEATURES]
        truth=combined_label(f.iloc[m['positions']]).to_numpy(); maps=c.mappings(meta,m['positions'],fold)
        opportunities.extend(c.opportunity(meta,m['positions'],fold,maps,truth))
        for model in c.MODELS:
            m=memories[model]; desc=dict(d['E011'])
            if model=='mixture': desc.update(temperature=d['mixture_temperature'],calibration_supported_n=d['mixture_calibration_supported_n'])
            if model=='frequency': desc['temperature']=1.
            diagnostics.append(c.probability_diagnostic(model,fold,desc,m))
            rows.extend(c.score_fold(model,fold,m,truth,maps,lambda *_:None))
            routes.append(c.routing(d['E011'],m,truth,model))
    return {'experiment_id':'E014','status':'COMPLETED','development':dev,'records':rows,
        'aggregate':c.summarize(rows),'primary':c.primary(rows),'contrasts':c.contrasts(rows),'opportunity':opportunities,
        'contrast_aggregate':c.contrast_summary(c.contrasts(rows)),
        'probability_diagnostics':diagnostics,'routing':routes,'routing_aggregate':c.routing_summary(routes),
        'provenance':{'git_revision':'a'*40,'image_id':'sha256:'+'a'*64,'lock_sha256':'a'*64,'frozen_development_sha256':'a'*64,
            'started_utc':'2026-10-15T00:00:00+00:00','finished_utc':'2026-10-15T00:00:01+00:00','wall_seconds':1.,
            'model_fits':50,'fit_warnings':0,'reproduction_model_folds':5,'global_freeze_verified':True,
            'preservation_verified':True,'uid':10001,'gid':10001,'replicates':100,'permutation_seed':20261014,
            'row_level_outputs':False,'preserved_files':205}}


def test_full_synthetic_pipeline_allowlist_and_report(payload):
    p.validate(payload); report=p.render(payload)
    assert 'Complete inner development' in report and 'Complete fold review' in report
    assert 'synthetic explanation' not in json.dumps(payload) and 'SyntheticError' not in json.dumps(payload)
    assert len(payload['records'])==300 and len(payload['opportunity'])==20
    assert len(payload['routing'])==15


@pytest.mark.parametrize('damage',['aggregate','primary','replicate','count','private','weight','route','temperature','contrast'])
def test_reject_corrupt_artifact(payload,damage):
    x=deepcopy(payload)
    if damage=='aggregate': x['aggregate'][0]['original']['map_at_3']['mean']+=.1
    if damage=='primary': x['primary']['frequency']['criterion_met']=not x['primary']['frequency']['criterion_met']
    if damage=='replicate': x['records'][0]['shuffled']['explanation_shuffle']['map_at_3']['score']['values'][0]+=.1
    if damage=='count': x['records'][0]['n']+=1
    if damage=='private': x['records'][0]['probabilities']=[.5,.5]
    if damage=='weight': x['development'][0]['weight_selection']['selected_weight']=.333
    if damage=='route': x['routing'][0]['budgets'][1]['all']['retained_n']+=1
    if damage=='temperature': x['development'][0]['mixture_temperature']=1000.
    if damage=='contrast': x['contrasts'][0]['contribution_change_from_E011']['gain']+=.1
    with pytest.raises(ValueError): p.validate(x)


def test_approved_protocol_and_historical_preservation():
    root=Path(__file__).resolve().parents[1]
    approval=json.loads((root/'experiments/e014_approval.json').read_text())
    assert core.canonical_sha(root/'docs/E014_PROTOCOL.md')==approval['protocol_sha256_lf']
    if (root/'experiments/e014_lock.json').exists():
        lock=json.loads((root/'experiments/e014_lock.json').read_text())
        c.verify_lock(root,lock['docker_image_id'],private=False)


def test_recipient_strata_frequency_and_null_eligibility():
    truth=np.array(['a','b','never','a','b','a'])
    prob=np.array([[.8,.2],[.1,.9],[.7,.3],[.4,.6],[.9,.1],[.5,.5]])
    fp=np.tile([.6,.4],(6,1)); classes=np.array(['a','b'])
    memory={'prob':prob,'raw':prob.copy(),'classes':classes,'frequency_prob':fp,'frequency_classes':classes,
        'positions':np.arange(6),'questions':np.array([1,1,1,2,2,2]),
        'train_labels':np.array(['a']*40+['b']*10),'train_questions':np.tile([10,11],25)}
    meta=pd.DataFrame({'QuestionId':memory['questions'],'QuestionText':['one']*3+['two']*3,
        'MC_Answer':['choice']*6,'StudentExplanation':['same']*6})
    maps=c.mappings(meta,memory['positions'],0); rows=c.score_fold('mixture',0,memory,truth,maps,lambda *_:None)
    for stratum,n in [('unsupported',1),('rare',2),('frequent',3),('well_supported',3)]:
        r=next(r for r in rows if r['question'] is None and r['stratum']==stratum)
        assert r['n']==n
        assert r['calibration']['scaled']['ece'] is None
        if stratum=='unsupported': assert r['shuffled']['explanation_shuffle']['map_at_3']['score']['values']==[0]*100
    freq={**memory,'prob':fp,'raw':fp}
    for row in c.score_fold('frequency',0,freq,truth,maps,lambda *_:None):
        assert row['shuffled']['explanation_shuffle']['map_at_3']['original_minus_shuffled']['values']==([0]*100 if row['n'] else [])


def test_reproduction_mismatch_is_fatal(payload):
    with pytest.raises((ValueError,StopIteration)):
        c.reproduction_diagnostic(payload['records'],payload['opportunity'],[],{'records':[]})


def test_monitor_permission_error_does_not_change_computation(tmp_path,monkeypatch):
    from map_misconceptions import resilient_status
    def fail(*args): raise PermissionError(13,'synthetic monitor failure')
    monkeypatch.setattr(resilient_status.os,'replace',fail)
    with c.ResilientStatus(tmp_path/'status.json',experiment_id='E014',total=1) as live:
        value=c.core.meaningful([.02]*5)
        live.update('Synthetic work complete',completed=1)
    assert value['criterion_met'] and live.diagnostics()['status']=='COMPLETED'
    assert live.diagnostics()['io_failures']>=1


def test_published_result_if_present():
    path=Path(__file__).resolve().parents[1]/'results/E014_aggregates.json'
    if not path.exists(): pytest.skip('E014 not yet run or published.')
    x=json.loads(path.read_text()); p.validate(x)
    same((path.parents[1]/'docs/E014_RESULTS.md').read_text(),p.render(x))
