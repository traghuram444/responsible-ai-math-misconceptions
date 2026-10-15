"""Synthetic E013 tests; never fit or inspect MAP research data."""
from copy import deepcopy
import inspect
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from map_misconceptions import e013 as c, e013_publication as p
from map_misconceptions import e011_context as core
from map_misconceptions.e011_publication import same
from map_misconceptions.data_contract import combined_label


def synthetic():
    return pd.DataFrame([{'QuestionId':q,'QuestionText':f'synthetic exercise {q}','MC_Answer':str(i%2),
        'StudentExplanation':f'synthetic explanation variant {i%3}',
        'Category':'True_Correct' if i%2 else 'False_Misconception',
        'Misconception':'NA' if i%2 else 'SyntheticError'} for q in range(15) for i in range(8)])


def metadata(f): return f[['QuestionId','QuestionText','MC_Answer','StudentExplanation']].copy()


def test_deterministic_mappings_exact_rng_and_cell_boundaries():
    f=synthetic().iloc[:24]; positions=np.arange(len(f))*2
    maps=c.mappings(metadata(f),positions,2)
    other=c.mappings(metadata(f),positions,2)
    for condition in c.CONDITIONS:
        d=maps[condition]['donors']
        np.testing.assert_array_equal(d,other[condition]['donors'])
        assert not d.flags.writeable and d.shape==(100,len(f))
        for r in range(100):
            assert sorted(d[r].tolist())==list(range(len(f)))
            np.testing.assert_array_equal(f.QuestionId.to_numpy()[d[r]],f.QuestionId.to_numpy())
            if condition=='explanation_shuffle': np.testing.assert_array_equal(f.MC_Answer.to_numpy()[d[r]],f.MC_Answer.to_numpy())
    first=maps['explanation_shuffle']['cells'][0]
    rng=np.random.Generator(np.random.PCG64(np.random.SeedSequence([20261014,1,2,0,0])))
    np.testing.assert_array_equal(maps['explanation_shuffle']['donors'][0,first],rng.permutation(first))


def test_singleton_duplicate_missing_strings_and_unordered_positions():
    f=synthetic().iloc[:4].copy(); f.MC_Answer=['a','b',None,'']; f.StudentExplanation=['x','x',None,'']
    maps=c.mappings(metadata(f),np.array([8,2,6,4]),0)
    d=maps['explanation_shuffle']['donors']
    assert np.all(d[:,0]==0) and np.all(d[:,1]==1)
    assert any(np.array_equal(d[r,2:],[2,3]) for r in range(100)) # Fixed points are allowed.
    assert any(np.array_equal(d[r,2:],[3,2]) for r in range(100))
    assert len(maps['explanation_shuffle']['cells'])==3


def test_target_columns_and_question_text_variation_rejected():
    f=synthetic().iloc[:8].copy()
    with pytest.raises(ValueError): c.mappings(f,np.arange(len(f)),0)
    f.loc[0,'QuestionText']='different'
    with pytest.raises(ValueError): c.mappings(metadata(f),np.arange(len(f)),0)


@pytest.mark.parametrize('model',['E011','E012'])
def test_unchanged_prepare_and_label_blind_global_inputs(model):
    f=synthetic(); assignments=pd.DataFrame({'fold_0':np.where(f.QuestionId<9,'train',np.where(f.QuestionId<12,'calibration','evaluation'))})
    calls=[]; d,m=c.prepare(f,assignments,model,0,lambda:calls.append(1))
    old_d,old_m=core.prepare(f,assignments,'full_context','logistic' if model=='E011' else 'complement_nb',0,lambda:None)
    same(d,old_d); np.testing.assert_array_equal(m['prob'],old_m['prob'])
    assert len(calls)==(10 if model=='E011' else 19)
    raw,classes=core.predict(m['fitted'],f.iloc[m['positions']],'full_context')
    np.testing.assert_array_equal(raw,m['raw'])
    changed=f.copy(); changed.loc[changed.QuestionId>=12,['Category','Misconception']]=['HIDDEN','TARGET']
    d2,m2=c.prepare(changed,assignments,model,0,lambda:None)
    same(d,d2); np.testing.assert_array_equal(m['prob'],m2['prob'])
    evaluation=f.iloc[m['positions']].reset_index(drop=True)
    maps=c.mappings(metadata(evaluation),m['positions'],0)
    for condition in c.CONDITIONS:
        donor=maps[condition]['donors'][0]
        perturbed=evaluation.copy()
        perturbed.StudentExplanation=evaluation.StudentExplanation.to_numpy()[donor]
        if condition=='pair_shuffle': perturbed.MC_Answer=evaluation.MC_Answer.to_numpy()[donor]
        actual,_=core.predict(m['fitted'],perturbed,'full_context')
        np.testing.assert_allclose(actual,m['raw'][donor],rtol=0,atol=1e-14)


def toy_memory():
    truth=np.array(['a','b','unsupported','a','b','a'])
    prob=np.array([[.8,.2],[.1,.9],[.7,.3],[.4,.6],[.9,.1],[.5,.5]])
    fp=np.tile([.6,.4],(6,1)); classes=np.array(['a','b'])
    memory={'prob':prob,'raw':prob.copy(),'classes':classes,'frequency_prob':fp,'frequency_classes':classes,
        'positions':np.arange(6),'questions':np.array([1,1,1,2,2,2]),
        'train_labels':np.array(['a']*40+['b']*40),'train_questions':np.tile([10,11],40)}
    f=pd.DataFrame({'QuestionId':memory['questions'],'QuestionText':['one']*3+['two']*3,
                    'MC_Answer':['choice']*6,'StudentExplanation':[f'synthetic {i}' for i in range(6)]})
    return truth,memory,f


def test_scores_recipient_support_frequency_invariance_and_gain_loss():
    truth,m,f=toy_memory(); maps=c.mappings(f,m['positions'],0); calls=[]
    rows=c.score_fold('E011',0,m,truth,maps,lambda condition,r:calls.append((condition,r)))
    assert len(calls)==200
    unsupported=next(r for r in rows if r['question'] is None and r['stratum']=='unsupported')
    assert unsupported['n']==1 and unsupported['original']['map_at_3']==0
    assert unsupported['shuffled']['pair_shuffle']['map_at_3']['score']['values']==[0]*100
    rare=next(r for r in rows if r['question'] is None and r['stratum']=='rare')
    assert rare['n']==0 and rare['original']['map_at_3'] is None
    for row in rows:
        for g in row['calibration'].values(): p.check_cal(g)
        for metric in c.METRICS:
            w=row['agreement'][metric]
            assert w['wins']+w['ties']+w['losses']==row['n']
            if row['n']: assert w['net']==pytest.approx(w['gain']-w['loss'])
    m.update(prob=m['frequency_prob'],raw=m['frequency_prob'],classes=m['frequency_classes'])
    baseline=c.score_fold('frequency',0,m,truth,maps,lambda *_:None)
    for row in baseline:
        for condition in c.CONDITIONS:
            assert row['shuffled'][condition]['map_at_3']['original_minus_shuffled']['values']==([0]*100 if row['n'] else [])


def test_map_rank_ties_match_historical_function():
    truth,m,_=toy_memory()
    top,prediction=c.rank_labels(m['prob'],m['classes'])
    assert c.row_scores(truth,top,prediction)['map_at_3'].mean()==core.map_at_3(truth,m['prob'],m['classes'])


def test_replicates_and_calibration_eligibility():
    values=np.arange(100)/100
    stat=c.repetition(values); p.check_repetition(stat,100)
    assert stat['p025']==np.percentile(values,2.5,method='linear')
    n=200; truth=np.array(['a']*100+['b']*100); prob=np.tile([.6,.4],(n,1))
    g=c.calibration(truth,prob,np.array(['a','b']),np.ones(n,dtype=bool))
    assert g['ineligible_reasons']==[] and g['ece']==pytest.approx(.1)
    short=c.calibration(truth,prob,np.array(['a','b']),np.arange(n)<199)
    assert short['ece'] is None and 'n_below_200' in short['ineligible_reasons']


def test_reproduction_failure_stops(monkeypatch):
    d={'arm':'full_context','fold':0}; reference={'development':[deepcopy(d)],'records':[{'arm':'full_context','fold':0},{'arm':'frequency','fold':0}]}
    monkeypatch.setattr(core,'evaluate',lambda *args,**kwargs:{'arm':'frequency' if kwargs['frequency'] else 'full_context','fold':0})
    c.check_reproduction(d,{},np.array([]),reference)
    reference['development'][0]['fold']=1
    with pytest.raises((ValueError,StopIteration)): c.check_reproduction(d,{},np.array([]),reference)


def test_global_barrier_and_all_reference_gates_precede_scoring():
    source=inspect.getsource(c.main)
    assert source.index("write_new(output / 'frozen_development.json'")<source.index('truths =')<source.index('check_reproduction(')<source.index('score_fold(')
    assert 'ResilientStatus(' in source
    assert 'temperature_scale' not in source


def test_strict_schemas_reject_private_fields():
    truth,m,f=toy_memory(); maps=c.mappings(f,m['positions'],0)
    row=c.score_fold('E011',0,m,truth,maps,lambda *_:None)[0]
    p.s.validate_schema(row,p.RECORD)
    row['StudentExplanation']='synthetic forbidden'
    with pytest.raises(ValueError): p.s.validate_schema(row,p.RECORD)


def test_primary_margin_and_no_model_selection():
    rows=[]
    for model,deltas in [('E011',[.02]*5),('E012',[.019]*5)]:
        for fold,delta in enumerate(deltas):
            rows.append({'model':model,'fold':fold,'question':None,'stratum':'all',
                'shuffled':{'explanation_shuffle':{'map_at_3':{'original_minus_shuffled':{'mean':delta}}}}})
    decision=c.primary(rows)
    assert [x['criterion_met'] for x in decision['models']]==[True,False]
    assert not decision['concordant']


def test_approved_protocol_hash_and_prior_files_unchanged():
    root=Path(__file__).resolve().parents[1]
    approval=json.loads((root/'experiments/e013_approval.json').read_text())
    assert core.canonical_sha(root/'docs/E013_PROTOCOL.md')==approval['protocol_sha256_lf']
    if (root/'experiments/e013_lock.json').exists():
        lock=json.loads((root/'experiments/e013_lock.json').read_text())
        c.verify_lock(root,lock['docker_image_id'],private=False)


def test_published_result_if_present():
    path=Path(__file__).resolve().parents[1]/'results/E013_aggregates.json'
    if not path.exists(): pytest.skip('E013 not yet run or published.')
    payload=json.loads(path.read_text()); p.validate(payload)
    same((path.parents[1]/'docs/E013_RESULTS.md').read_text(),p.render(payload))


@pytest.fixture(scope='module')
def complete_synthetic_payload():
    f=synthetic(); descriptions={'E011':[],'E012':[]}; rows=[]; opportunities=[]; diagnostics=[]
    for fold in range(5):
        roles=np.where(f.QuestionId//3==fold,'evaluation',np.where(f.QuestionId//3==(fold+1)%5,'calibration','train'))
        assignments=pd.DataFrame({f'fold_{fold}':roles})
        memories={}
        for model in ('E011','E012'):
            description,memory=c.prepare(f,assignments,model,fold,lambda:None)
            descriptions[model].append(description); memories[model]=memory
            diagnostics.append(c.probability_diagnostic(model,fold,description,memory))
        memory=memories['E011']; eval_frame=f.iloc[memory['positions']]
        truth=combined_label(eval_frame).to_numpy(); maps=c.mappings(metadata(eval_frame),memory['positions'],fold)
        opportunities.extend(c.opportunity(metadata(eval_frame),memory['positions'],fold,maps,truth))
        freq=dict(memory); freq.update(prob=memory['frequency_prob'],raw=memory['frequency_prob'],classes=memory['frequency_classes'])
        memories['frequency']=freq
        for model in c.MODELS:
            rows.extend(c.score_fold(model,fold,memories[model],truth,maps,lambda *_:None))
    return {'experiment_id':'E013','status':'COMPLETED','development':descriptions,'records':rows,
        'aggregate':c.summarize(rows),'primary':c.primary(rows),'opportunity':opportunities,'probability_diagnostics':diagnostics,
        'provenance':{'git_revision':'a'*40,'image_id':'sha256:'+'a'*64,'lock_sha256':'a'*64,'frozen_development_sha256':'a'*64,
            'started_utc':'2026-10-15T00:00:00+00:00','finished_utc':'2026-10-15T00:00:01+00:00','wall_seconds':1.,
            'model_fits':145,'fit_warnings':0,'reproduction_model_folds':10,'global_freeze_verified':True,
            'preservation_verified':True,'uid':10001,'gid':10001,'replicates':100,'permutation_seed':20261014,
            'row_level_outputs':False,'preserved_files':191}}


def test_full_synthetic_pipeline_and_report(complete_synthetic_payload):
    payload=complete_synthetic_payload
    p.validate(payload)
    text=p.render(payload)
    assert 'Complete fold performance' in text and 'Permutation opportunity' in text
    assert 'synthetic explanation' not in json.dumps(payload)
    assert 'SyntheticError' not in json.dumps(payload)
    assert len(payload['records'])==300


@pytest.mark.parametrize('damage',['aggregate','primary','replicate','count','private'])
def test_reject_corrupted_synthetic_artifact(complete_synthetic_payload,damage):
    payload=deepcopy(complete_synthetic_payload)
    if damage=='aggregate': payload['aggregate'][0]['original']['map_at_3']['mean']+=.1
    if damage=='primary': payload['primary']['concordant']=not payload['primary']['concordant']
    if damage=='replicate': payload['records'][0]['shuffled']['pair_shuffle']['map_at_3']['score']['values'][0]+=.1
    if damage=='count': payload['records'][0]['n']+=1
    if damage=='private': payload['records'][0]['probabilities']=[.5,.5]
    with pytest.raises(ValueError): p.validate(payload)
