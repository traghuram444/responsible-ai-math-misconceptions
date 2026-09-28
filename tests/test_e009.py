"""Invented E009 examples only; no real-data modeling in tests."""
from copy import deepcopy
import hashlib
import inspect
import json
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
import pytest
from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from map_misconceptions import e001, e008, e009
from map_misconceptions import e009_reliability as rel
from map_misconceptions.e009_metrics import aggregate, correctness_auc, evaluate_fold, head_summary, stat
from map_misconceptions.e009_publication import validate_public_payload, report
from map_misconceptions.threshold_transfer import TARGETS, calibration_roles, select_cutoff, apply_cutoff

PARAM = {"params": {"ngram_range": [1, 1], "min_df": 2, "C": .5}, "inner_mean_map_at_3": .5}
FITS = dict(attempted=10, successful=10, failed=0, warnings=0, convergence_warnings=0)


class Live:
    def update(self, *args, **kwargs): pass


def test_blocks_are_exact_deterministic_and_label_blind():
    expected = sorted(range(9), key=lambda q: (hashlib.sha256(f"E009|fold=2|QuestionId={q}|seed=20260831".encode()).hexdigest(), q))
    actual = rel.crossfit_blocks(list(range(9)) * 4, 2)
    assert actual == tuple(tuple(expected[i:i+3]) for i in (0,3,6))
    assert actual == rel.crossfit_blocks(list(reversed(range(9))), 2)
    assert len(set(q for block in actual for q in block)) == 9
    with pytest.raises(ValueError): rel.crossfit_blocks(range(8), 2)


def test_five_numeric_features_and_zero_entropy_boundaries():
    p = np.array([[.8,.2],[.5,.5],[1.,0.]])
    x = rel.numeric_features(p, np.array(['a','b']), ['a']*3+['b'], np.array([0., .2,1.]))
    assert x.shape == (3,5)
    np.testing.assert_allclose(x[:,0], [.8,.5,1.])
    np.testing.assert_allclose(x[:,1], [.6,0.,1.])
    np.testing.assert_allclose(x[:,2], [-sum(v*np.log(v) for v in [.8,.2])/np.log(2),1.,0.])
    np.testing.assert_allclose(x[:,3], 1.)
    np.testing.assert_allclose(x[:,4], [0.,.2,1.])
    single = rel.numeric_features(np.ones((2,1)), np.array(['a']), ['a'], np.zeros(2))
    np.testing.assert_allclose(single, [[1.,1.,0.,1.,0.]]*2)


@pytest.mark.parametrize('bad', ['nan','negative','sum','similarity','vocabulary'])
def test_invalid_features_stop(bad):
    p, c, s = np.array([[.8,.2]]), np.array(['a','b']), np.array([.5])
    if bad=='nan': p[0,0]=np.nan
    if bad=='negative': p[0]=[-.1,1.1]
    if bad=='sum': p[0]=[.1,.1]
    if bad=='similarity': s[0]=np.nan
    if bad=='vocabulary': c[0]='unknown'
    with pytest.raises(ValueError): rel.numeric_features(p,c,['a','b'],s)


def test_similarity_all_training_rows_zero_queries_and_batch_independence(monkeypatch):
    train = pd.DataFrame({'StudentExplanation':['alpha beta','gamma delta'], 'Category':['A','B'], 'Misconception':'NA'})
    query = pd.DataFrame({'StudentExplanation':['alpha beta','unknownword','gamma']*90, 'Category':'secret', 'QuestionId':999})
    vectorizer = TfidfVectorizer().fit(train.StudentExplanation)
    def no_fit(*args, **kwargs): raise AssertionError('Refitting vectorizer is prohibited')
    monkeypatch.setattr(vectorizer,'fit',no_fit)
    monkeypatch.setattr(vectorizer,'fit_transform',no_fit)
    actual=rel.maximum_similarity((vectorizer,None),train,query,'explanation_only')
    expected=(vectorizer.transform(query.StudentExplanation) @ vectorizer.transform(train.StudentExplanation).T).toarray().max(axis=1)
    np.testing.assert_allclose(actual,np.clip(expected,0,1))
    assert actual[1]==0
    changed=query.iloc[[0]].copy()
    changed['Category']='different'; changed['QuestionId']=42
    assert rel.maximum_similarity((vectorizer,None),train,changed,'explanation_only')[0]==actual[0]
    assert set(rel.text_view(query).columns)=={'StudentExplanation'}


def test_weighted_scaler_and_logistic_match_explicit_reference():
    questions=np.repeat(np.arange(9),np.arange(3,12))
    rng=np.random.default_rng(9)
    x=rng.random((len(questions),5)); x[:,4]=1
    correct=rng.random(len(questions))<.5
    weights=rel.equal_question_weights(questions)
    assert weights.sum()==pytest.approx(len(questions))
    for q in range(9): assert weights[questions==q].sum()==pytest.approx(len(questions)/9)
    model, meta=rel.fit_router(x,correct,questions)
    scale=StandardScaler().fit(x,sample_weight=weights)
    clf=LogisticRegression(**rel.ROUTER_PARAMS).fit(scale.transform(x),correct.astype(int),sample_weight=weights)
    np.testing.assert_allclose(model.score(x),clf.predict_proba(scale.transform(x))[:,1])
    assert model.scaler.scale_[4]==1 and meta['fitting_calls']==1
    # A response's score is independent of unrelated query rows and order.
    np.testing.assert_allclose(model.score(x[:1]),model.score(x)[0:1])
    np.testing.assert_allclose(model.score(x[::-1])[::-1],model.score(x))


@pytest.mark.parametrize('constant',[False,True])
def test_single_correctness_fallback(constant):
    model, meta=rel.fit_router(np.ones((18,5)),np.full(18,constant,bool),np.repeat(np.arange(9),2))
    assert meta['status']=='CONSTANT_CORRECTNESS_FALLBACK' and meta['fitting_calls']==0
    np.testing.assert_array_equal(model.score(np.zeros((4,5))),int(constant))


def test_router_convergence_warning_and_nonfinite_stop(monkeypatch):
    def warn(*args,**kwargs): warnings.warn('invented',ConvergenceWarning)
    monkeypatch.setattr(rel.LogisticRegression,'fit',warn)
    with pytest.raises(ConvergenceWarning): rel.fit_router(np.ones((18,5)),np.tile([True,False],9),np.repeat(np.arange(9),2))
    with pytest.raises(ValueError): rel.fit_router(np.full((18,5),np.nan),np.tile([True,False],9),np.repeat(np.arange(9),2))


def test_crossfit_tuning_and_vectorizer_exclude_held_questions(monkeypatch):
    train=pd.DataFrame({'QuestionId':np.repeat(np.arange(9),6),'StudentExplanation':[f'question{q} alpha beta' for q in np.repeat(np.arange(9),6)],
                        'Category':np.tile(['A','A','A','B','B','UNSUPPORTED'],9),'Misconception':'NA'})
    blocks=rel.crossfit_blocks(train.QuestionId,0)
    held_by_call=[]
    current={}
    def tune(rows,variant,splitter,groups):
        block=len(held_by_call)
        held_by_call.append(set(blocks[block]))
        assert set(rows.QuestionId).isdisjoint(blocks[block]) and rows.QuestionId.nunique()==6
        assert splitter.n_splits==3 and groups.equals(rows.QuestionId.astype(str))
        # Model the unchanged 3x3 tuning fit calls with the actual wrapper active.
        for _ in range(9): e001.fit_tfidf_lr(rows,variant,PARAM['params'])
        current['held']=set(blocks[block])
        return deepcopy(PARAM)
    def fit(rows,variant,params):
        assert rows.QuestionId.nunique()==6
        vec=TfidfVectorizer().fit(rows.StudentExplanation)
        return vec,None
    def predict(fitted,rows,variant):
        assert set(rows.columns)=={'StudentExplanation'}
        for q in current['held']: assert f'question{q}' not in fitted[0].vocabulary_
        return np.tile([.8,.2,0.],(len(rows),1)),np.array(['A:NA','B:NA','UNSUPPORTED:NA'])
    monkeypatch.setattr(e001,'score_params',tune)
    monkeypatch.setattr(e001,'fit_tfidf_lr',fit)
    monkeypatch.setattr(e001,'predict',predict)
    x,y,summary=rel.crossfit_training(train,'explanation_only',0,Live(),0)
    assert x.shape==(54,5)
    np.testing.assert_array_equal(y,train.Category.to_numpy()=='A')
    assert sum(b['held_n'] for b in summary['blocks'])==54
    assert all(b['fits']['attempted']==10 for b in summary['blocks'])
    assert set(q for qs in held_by_call for q in qs)==set(range(9))


def test_counted_legacy_fits_preserves_arguments_failures_and_warnings(monkeypatch):
    calls=[]
    def fit(value):
        calls.append(value)
        warnings.warn('invented',ConvergenceWarning)
        if value==2: raise ValueError('invented')
        return value
    monkeypatch.setattr(e001,'fit_tfidf_lr',fit)
    with rel.counted_fits(Live(),'synthetic',0) as counts:
        assert e001.fit_tfidf_lr(1)==1
        with pytest.raises(ValueError): e001.fit_tfidf_lr(2)
    assert e001.fit_tfidf_lr is fit and calls==[1,2]
    assert counts==dict(attempted=2,successful=1,failed=1,warnings=2,convergence_warnings=2)


def test_unsupported_truth_is_error_and_not_feature():
    raw=np.tile([.8,.2],(200,1)); classes=np.array(['a','b'])
    truth=np.full(200,'unseen')
    x=rel.numeric_features(raw,classes,['a']*9+['b'],np.ones(200))
    assert np.isfinite(x).all()
    correct=classes[raw.argmax(axis=1)]==truth
    assert not correct.any()
    policy=select_cutoff(x[:,0],correct,np.repeat([0,1],100),20)
    assert policy['status']=='NO_ADMISSIBLE_THRESHOLD'


def test_ranking_and_head_eligibility_are_exact():
    correct=np.r_[np.ones(180,bool),np.zeros(20,bool)]
    assert correctness_auc(np.ones(200)*.8,correct)['auroc']==.5
    assert correctness_auc(correct.astype(float),correct)['auroc']==1
    assert correctness_auc(np.ones(199),correct[:199])['auroc'] is None
    head=head_summary(np.full(200,.8),correct)
    assert head['binary_brier']==pytest.approx(.9*.04+.1*.64)
    assert head['binary_ece']==pytest.approx(.1)
    assert head_summary(np.ones(200),np.ones(200,bool))['mean_predicted_correctness'] is None
    assert stat([None]*5)['mean'] is None
    assert stat([1,None,None,None,None])['sd'] is None


def make_reference(frame,fold=0):
    calibration=frame.loc[frame.QuestionId.isin([9,10,11])]
    tq,sq=calibration_roles(calibration.QuestionId,fold)
    selection=calibration.loc[calibration.QuestionId.isin(sq)]
    roles=np.array([sq.index(int(q)) for q in selection.QuestionId])
    correct=selection.Category.to_numpy()=='A'
    serial=json.dumps({'fold':fold,'temperature':tq,'threshold':sq},sort_keys=True,separators=(',',':'))
    # Train A:B prevalence .8:.2, same as mocked probabilities.
    policies={r:[select_cutoff(np.full(len(selection),.8),correct,roles,t) for t in TARGETS] for r in ('confidence_only','support_aware','frequency')}
    return {'variant':'explanation_only','fold':fold,'temperature':1.,'temperature_n':250,
            'temperature_supported_n':250,'temperature_supported_fraction':1.,'temperature_fallback':False,
            'role_counts':[9,1,2,3],'derived_role_sha256':hashlib.sha256(serial.encode()).hexdigest(),
            'selected_hyperparameters':deepcopy(PARAM),'policies':policies}


def test_prepare_evaluation_labels_do_not_enter_training_or_policy(monkeypatch):
    frame=pd.DataFrame({'QuestionId':np.repeat(np.arange(15),250), 'Category':np.tile(['A']*200+['B']*50,15),
                        'Misconception':'NA','StudentExplanation':'alpha beta','QuestionText':'invented question'})
    assign=pd.DataFrame({'fold_0':np.repeat(['train']*9+['calibration']*3+['evaluation']*3,250)})
    def crossfit(train,*args):
        assert set(train.QuestionId)==set(range(9))
        return np.tile([.8,.6,.7,1.,1.],(len(train),1)),train.Category.to_numpy()=='A',{}
    def fit(train,*args):
        assert set(train.QuestionId)==set(range(9))
        return (TfidfVectorizer().fit(train.StudentExplanation),None),deepcopy(PARAM),deepcopy(FITS)
    def predict(model,rows,*args):
        assert set(rows.columns)=={'StudentExplanation','QuestionText'}
        return np.tile([.8,.2],(len(rows),1)),np.array(['A:NA','B:NA'])
    monkeypatch.setattr(e009,'crossfit_training',crossfit)
    monkeypatch.setattr(e009,'tuned_fit',fit)
    monkeypatch.setattr(e001,'predict',predict)
    monkeypatch.setattr(e001,'temperature_scale',lambda *a:(1.,250))
    reference=make_reference(frame)
    first,memory,gate=e009.prepare_fold(frame,assign,'explanation_only',0,Live(),0,reference)
    changed=frame.copy(); changed.loc[changed.QuestionId>=12,'Category']='UNSUPPORTED'
    second,changed_memory,_=e009.prepare_fold(changed,assign,'explanation_only',0,Live(),0,reference)
    assert first==second and 'truth' not in memory
    for r in rel.RULES: np.testing.assert_array_equal(memory['scores'][r],changed_memory['scores'][r])
    assert gate['policy_records_matched']==9


def synthetic_payload():
    development,records,ranking,dev_checks,eval_checks=[],[],[],[],[]
    for variant in rel.VARIANTS:
        for fold in range(5):
            old={'variant':variant,'fold':fold,'temperature':1.,'temperature_n':200,'temperature_supported_n':200,
                 'temperature_supported_fraction':1.,'temperature_fallback':False,'role_counts':[9,1,2,3],
                 'derived_role_sha256':'a'*64,'selected_hyperparameters':deepcopy(PARAM),
                 'policies':{r:[select_cutoff(np.full(400,.8),np.tile(np.arange(200)>=20,2),np.repeat([0,1],200),t) for t in TARGETS] for r in ('confidence_only','support_aware','frequency')}}
            policies={r:deepcopy(old['policies']['confidence_only']) for r in rel.RULES}
            d={'variant':variant,'fold':fold,'reference_development':old,'crossfit':{'role_sha256':'b'*64,
                'blocks':[{'block':b,'fitting_questions':6,'held_questions':3,'fitting_n':600,'held_n':300,'correct_n':240,'incorrect_n':60,'selected_hyperparameters':deepcopy(PARAM),'fits':deepcopy(FITS)} for b in range(3)]},
                'router':{'n':900,'correct_n':720,'incorrect_n':180,'question_count':9,'feature_count':5,'weight_sum':900.,'status':'FITTED','constant':None,'fitting_calls':1,'convergence_warnings':0},
                'final_classifier_fits':deepcopy(FITS),'policies':policies}
            truth=np.tile(['a']*240+['b']*30+['unsupported']*30,3)
            memory={'learned_prob':np.tile([.8,.2],(900,1)),'frequency_prob':np.tile([.8,.2],(900,1)),
                    'classes':np.array(['a','b']),'frequency_classes':np.array(['a','b']),
                    'train_labels':np.tile(['a']*80+['b']*20,9),'train_questions':np.repeat(np.arange(9),100),
                    'evaluation_questions':np.repeat(np.arange(fold*3,fold*3+3),300),
                    'scores':{r:np.full(900,.8) for r in rel.RULES}}
            memory['scores']['learned_reliability']=np.where(truth=='a',.9,.2)
            rows,ranks=evaluate_fold(d,memory,truth)
            development.append(d); records.extend(rows); ranking.extend(ranks)
            dev_checks.append(e008.reproduction_gate(old,old))
            eval_checks.append({'variant':variant,'fold':fold,'matched_records':12})
    prov={'started_utc':'2026-09-28T00:00:00+00:00','finished_utc':'2026-09-28T00:01:00+00:00','wall_seconds':60.,
          'git_revision':'a'*40,'docker_image_id':'sha256:'+'a'*64,'uid':10001,'gid':10001,'seed':20260831,
          'preserved_files':100,'preservation_verified':True,'all_cutoffs_frozen_before_evaluation':True,
          'classifier_fits':{k:v*40 for k,v in FITS.items()},'router_fitting_calls':10,'router_fallbacks':0,
          'development_policies_reproduced':90,'evaluation_records_reproduced':120,'row_level_artifacts_serialized':False,
          'packages':{name:'1.0.0' for name in ('numpy','pandas','scipy','scikit-learn','PyYAML')}}
    for key in ('protocol_sha256','configuration_sha256','frozen_policies_sha256','e007_result_sha256','e008_result_sha256','data_sha256','manifest_sha256','assignments_sha256'): prov[key]='b'*64
    return {'experiment_id':'E009','status':'COMPLETED','provenance':prov,'development':development,
            'reproduction':{'development':dev_checks,'evaluation':eval_checks},'records':records,'ranking':ranking,'aggregate':aggregate(records,ranking)}


@pytest.fixture(scope='module')
def payload(): return synthetic_payload()


def test_complete_grid_report_and_primary_criterion(payload):
    validate_public_payload(payload)
    assert len(payload['records'])==200 and sum(len(r['evaluation']['questions']) for r in payload['records'])==600
    assert 'All evaluation-question results' in report(payload)
    selected=[s for s in payload['aggregate']['summaries'] if s['target_percent']==20]
    assert all(s['useful_transfer'] for s in selected)
    assert all(s['mean']==1 for s in payload['aggregate']['ranking'] if s['rule']=='learned_reliability')
    json.dumps(payload,allow_nan=False)


@pytest.mark.parametrize('field',['StudentExplanation','row_id','features','probabilities','weights','scaler_statistics','neighbor_ids','candidate_thresholds'])
def test_export_rejects_private_fields(payload,field):
    p=deepcopy(payload); p['development'][0]['router'][field]=['private']
    with pytest.raises(ValueError): validate_public_payload(p)


@pytest.mark.parametrize('mutation',['grid','counts','head','auc','summary','weight','policy','eligibility','question'])
def test_export_rejects_tampering(payload,mutation):
    p=deepcopy(payload)
    if mutation=='grid': p['records'].pop()
    if mutation=='counts': p['provenance']['classifier_fits']['successful']-=1
    if mutation=='head': p['records'][0]['reliability']['groups']['all']['correct_n']-=1
    if mutation=='auc': p['ranking'][0]['all']['auroc']=2.
    if mutation=='summary': p['aggregate']['summaries'][0]['groups']['all']['risk']['mean']=.5
    if mutation=='weight': p['development'][0]['router']['weight_sum']=1.
    if mutation=='policy': p['records'][1]['policy']=deepcopy(p['records'][1]['policy']); p['records'][1]['policy']['threshold']=.99
    if mutation=='eligibility': p['records'][0]['reliability']['groups']['unsupported']['binary_brier']=0.
    if mutation=='question': p['ranking'][0]['questions'][0]['QuestionId']=99
    with pytest.raises((ValueError,KeyError)): validate_public_payload(p)


def test_reference_gate_exact_discrete_and_float_tolerance(payload):
    rows=payload['records'][:20]
    expected=[{k:v for k,v in r.items() if k!='reliability'} for r in rows if r['rule'] in ('confidence_only','support_aware','frequency')]
    assert e009.evaluation_gate(rows,expected)==12
    altered=deepcopy(expected); altered[0]['evaluation']['groups']['all']['map_at_3']+=2e-10
    with pytest.raises(ValueError): e009.evaluation_gate(rows,altered)
    with pytest.raises(ValueError): e009.compare_reference({'count':1.},{'count':1})
    e009.compare_reference({'value':.5+5e-11},{'value':.5})


def test_frozen_policy_barrier_and_hash_lock(tmp_path):
    source=inspect.getsource(e009.main)
    assert source.index('write_new(output / "frozen_policies.json"') < source.index('truth = combined_label(frame.iloc[memory["evaluation_positions"]])') < source.index('evaluate_fold(')
    root=Path(__file__).resolve().parents[1]
    config=e009.approved_config(root)
    assert config['router']==rel.ROUTER_PARAMS and tuple(config['features'])==rel.FEATURES
    for name in ('docs/E009_PROTOCOL.md','experiments/e009_reliability.yaml','experiments/e009_approval.yaml'):
        dest=tmp_path/name; dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text((root/name).read_text(encoding='utf-8'),encoding='utf-8')
    path=tmp_path/'experiments/e009_reliability.yaml'
    path.write_text(path.read_text()+'\n',encoding='utf-8')
    with pytest.raises(ValueError): e009.approved_config(tmp_path)
