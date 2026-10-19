"""Synthetic E016 verification only; never reads MAP training data."""
from copy import deepcopy
import inspect
import json
from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import pytest
from map_misconceptions import e016 as c, e016_publication as p, e011_context as core
from map_misconceptions.data_contract import combined_label
from map_misconceptions.e011_publication import same


def synthetic():
    return pd.DataFrame([{'QuestionId':q,'QuestionText':f'synthetic exercise {q}',
        'MC_Answer':str(i%2),'StudentExplanation':f'synthetic explanation {i%3} x+1/2',
        'Category':'True_Correct' if i%2 else 'False_Misconception',
        'Misconception':'NA' if i%2 else 'SyntheticError'} for q in range(15) for i in range(8)])


def assignments(frame,fold):
    return pd.DataFrame({f'fold_{fold}':np.where(frame.QuestionId//3==fold,'evaluation',
        np.where(frame.QuestionId//3==(fold+1)%5,'calibration','train'))})


def test_training_only_vocabulary_and_warning_fatal(monkeypatch):
    f=synthetic(); fitted=c.fit_model(f[f.QuestionId<9],'factorized',core.e001.GRID[0])
    assert 'unseenevaluationword' not in fitted[0].vocabulary_
    features=f[f.QuestionId>=12][c.FEATURES].copy()
    features.StudentExplanation='unseenevaluationword'
    before=dict(fitted[0].vocabulary_); c.predict(fitted,features)
    assert fitted[0].vocabulary_==before
    original=c.LogisticRegression.fit
    def noisy(self,*args,**kwargs):
        warnings.warn('synthetic warning'); return original(self,*args,**kwargs)
    monkeypatch.setattr(c.LogisticRegression,'fit',noisy)
    with pytest.raises(RuntimeError): c.fit_model(f,'factorized',core.e001.GRID[0])


@pytest.mark.parametrize('arm',c.ARMS)
def test_inner_only_partitions_ties_and_calibration_isolation(monkeypatch,arm):
    f=synthetic(); train=f[f.QuestionId<9]; calls=[]
    original=c.fit_model
    def fitting(part,a,params):
        assert part.QuestionId.nunique()==6
        calls.append(set(part.QuestionId))
        return original(part,a,params)
    monkeypatch.setattr(c,'fit_model',fitting)
    monkeypatch.setattr(core,'map_at_3',lambda *args:.5)
    selected=c.select(train,arm,lambda:None)
    assert selected['selected_index']==0 and len(calls)==9
    assert all(s.issubset(set(train.QuestionId)) for s in calls)


def test_prepare_exact_A_reproduction_and_evaluation_target_independence():
    f=synthetic(); a=assignments(f,0); calls=[]
    d,m,_=c.prepare(f,a,0,'E011',lambda:calls.append(1))
    old,om=core.prepare(f,a,'full_context','logistic',0,lambda:None)
    same(d,old); np.testing.assert_array_equal(m['prob'],om['prob'])
    assert len(calls)==10
    changed=f.copy()
    changed.loc[a.fold_0=='evaluation',['Category','Misconception']]=['HIDDEN','TARGET']
    for arm in c.ARMS:
        d1,m1,_=c.prepare(f,a,0,arm,lambda:None)
        d2,m2,_=c.prepare(changed,a,0,arm,lambda:None)
        same(d1,d2); np.testing.assert_array_equal(m1['prob'],m2['prob'])
        assert not m1['prob'].flags.writeable and not m1['order'].flags.writeable
    with pytest.raises(ValueError):
        c.prepare_parts(f[f.QuestionId<9],f[(f.QuestionId>=9)&(f.QuestionId<12)],
                        f[f.QuestionId>=12],np.arange(24),0,'E011',lambda:None)


def test_calibration_receives_only_reserved_truths(monkeypatch):
    f=synthetic(); a=assignments(f,0); original=core.e001.temperature_scale; calls=[]
    def scaling(truth,prob,classes):
        np.testing.assert_array_equal(truth,combined_label(f[a.fold_0=='calibration']).to_numpy())
        calls.append(1); return original(truth,prob,classes)
    monkeypatch.setattr(core.e001,'temperature_scale',scaling)
    c.prepare(f,a,0,'factorized',lambda:None)
    assert len(calls)==1


def test_global_barrier_and_reproduction_before_new_scores():
    source=inspect.getsource(c.main)
    assert source.index("write_new(output/'frozen_development.json'")<source.index('truths=')<source.index('prior.check_reproduction(')<source.index('score_fold(')
    assert "for model in ('E011','frequency','factorized')" in source
    assert "if model=='frequency' and fold==4:" in source
    assert 'reproduction_diagnostic(' in source and 'ResilientStatus(' in source
    assert "same(core.answer_diagnostics(frame),ref11['answer_diagnostics'])" in source


def test_primary_exact_margin_consistency_and_no_winner_switch():
    def rows(delta):
        return [{'model':m,'fold':f,'question':None,'stratum':'all','n':1,
            'original':{metric:delta[f] if m=='factorized' else 0. for metric in c.METRICS},
            'calibration':{kind:{k:None for k in ('ece','brier')} for kind in ('raw','scaled')}}
                for m in c.MODELS for f in range(5)]
    assert c.primary(rows([.020]*5))['criterion_met']
    assert not c.primary(rows([.019999]*5))['criterion_met']
    assert not c.primary(rows([.1,.1,.1,0,0]))['criterion_met']
    assert not c.primary(rows([0]*5))['criterion_met']


@pytest.fixture(scope='module')
def payload():
    f=synthetic(); dev=[]; rows=[]; opportunities=[]; diagnostics=[]; routes=[]; categories=[]
    for fold in range(5):
        a=assignments(f,fold); parts={}
        for arm in c.ARMS:
            d,m,v=c.prepare(f,a,fold,arm,lambda:None); parts[arm]=(d,m,v)
            dev.append({'learning_arm':arm,**d})
        d,m,v=parts['E011']; meta=f.iloc[m['positions']][c.FEATURES]
        truth=combined_label(f.iloc[m['positions']]).to_numpy(); maps=c.mappings(meta,m['positions'],fold)
        opportunities.extend(c.opportunity(meta,m['positions'],fold,maps,truth))
        donor=maps['explanation_shuffle']['donors'][0]
        perturbed=meta.copy(); perturbed.StudentExplanation=meta.StudentExplanation.to_numpy()[donor]
        np.testing.assert_array_equal(core.input_text(perturbed,'full_context'),core.input_text(meta,'full_context').to_numpy()[donor])
        for model in c.MODELS:
            d,m,v=parts['E011' if model=='frequency' else model]
            if model=='frequency':
                m={**m,'prob':m['frequency_prob'],'raw':m['frequency_prob'],'classes':m['frequency_classes'],'order':m['frequency_order'],'category_raw':c.marginalize(m['frequency_prob'],m['frequency_classes'])}
                d={**d,'temperature':1.}
            else:
                # Rowwise temperature scaling commutes with donor indexing.
                np.testing.assert_array_equal(core.e001.apply_temperature(m['raw'][donor],d['temperature']),m['prob'][donor])
            diagnostics.append(c.probability_record(model,fold,d,m))
            rows.extend(c.score_fold(model,fold,m,truth,maps,lambda *_:None))
            evaluated=core.evaluate(d,m,truth)
            routes.append({'model':model,'fold':fold,'budgets':evaluated['risk_coverage']})
            categories.extend(c.category_records(model,fold,m,truth))
    return {'experiment_id':'E016','status':'COMPLETED','development':dev,'records':rows,
        'aggregate':c.summarize(rows),'primary':c.primary(rows),'contrasts':c.contrasts(rows),
        'contrast_aggregate':c.contrast_summary(c.contrasts(rows)),'opportunity':opportunities,
        'probability_diagnostics':diagnostics,'routing':routes,'routing_aggregate':c.routing_summary(routes),
        'category':categories,'category_aggregate':c.category_summary(categories),
        'category_contrasts':c.category_contrasts(categories),
        'category_contrast_aggregate':c.category_contrast_summary(c.category_contrasts(categories)),
        'provenance':{'git_revision':'a'*40,'image_id':'sha256:'+'a'*64,'lock_sha256':'a'*64,'frozen_development_sha256':'a'*64,
            'started_utc':'2026-10-19T00:00:00+00:00','finished_utc':'2026-10-19T00:00:01+00:00','wall_seconds':1.,
            'model_fits':100,'fit_warnings':0,'reproduction_model_folds':5,'global_freeze_verified':True,
            'preservation_verified':True,'uid':10001,'gid':10001,'replicates':100,'permutation_seed':20261014,
            'row_level_outputs':False,'preserved_files':219}}


def test_full_synthetic_pipeline_and_report(payload):
    p.validate(payload); report=p.render(payload)
    assert 'Complete inner development' in report and 'Complete fold review' in report
    assert 'synthetic explanation' not in json.dumps(payload) and 'SyntheticError' not in json.dumps(payload)
    assert len(payload['records'])==300 and len(payload['category'])==120


@pytest.mark.parametrize('damage',['aggregate','primary','replicate','count','private','setting','route','temperature','contrast','category_summary','category','calibration_delta'])
def test_reject_corrupt_artifact(payload,damage):
    x=deepcopy(payload)
    if damage=='aggregate': x['aggregate'][0]['original']['map_at_3']['mean']+=.1
    if damage=='primary': x['primary']['criterion_met']=not x['primary']['criterion_met']
    if damage=='replicate': x['records'][0]['shuffled']['explanation_shuffle']['map_at_3']['score']['values'][0]+=.1
    if damage=='count': x['records'][0]['n']+=1
    if damage=='private': x['records'][0]['row_predictions']=['private']
    if damage=='setting': x['development'][0]['selection']['selected_index']=7
    if damage=='route': x['routing'][0]['budgets'][1]['all']['retained_n']+=1
    if damage=='temperature': x['development'][0]['temperature']=1000.
    if damage=='contrast': x['contrasts'][0]['deltas']['map_at_3']+=.1
    if damage=='category_summary': x['category_aggregate'][0]['accuracy']['mean']+=.1
    if damage=='category': x['category'][0]['n']+=1
    if damage=='calibration_delta': x['contrasts'][0]['calibration_deltas']['scaled']['ece']=.1
    with pytest.raises((ValueError,IndexError)): p.validate(x)


def test_approved_protocol_and_preservation():
    root=Path(__file__).resolve().parents[1]
    approval=json.loads((root/'experiments/e016_approval.json').read_text())
    assert core.canonical_sha(root/'docs/E016_PROTOCOL.md')==approval['protocol_sha256_lf']
    if (root/'experiments/e016_lock.json').exists():
        lock=json.loads((root/'experiments/e016_lock.json').read_text())
        c.verify_lock(root,lock['docker_image_id'],private=False)


def test_reproduction_mismatch_fatal(payload):
    with pytest.raises((ValueError,StopIteration)):
        c.reproduction_diagnostic(payload['records'],[],[],{'records':[]})


def test_mapping_reproduces_E013_and_actual_donor_predictions():
    f=synthetic(); meta=f[f.QuestionId<3][c.FEATURES]; positions=np.arange(len(meta))
    maps=c.mappings(meta,positions,0)
    old=c.prior.mappings(meta,positions,0)
    donor=maps['explanation_shuffle']['donors'][0]
    np.testing.assert_array_equal(maps['explanation_shuffle']['donors'],old['explanation_shuffle']['donors'])
    perturbed=meta.copy(); perturbed.StudentExplanation=meta.StudentExplanation.to_numpy()[donor]
    for arm in c.ARMS:
        fitted=c.fit_model(f[f.QuestionId>=6],arm,core.e001.GRID[1])
        prob,classes=c.predict(fitted,meta)
        actual,other=c.predict(fitted,perturbed)
        np.testing.assert_array_equal(classes,other)
        np.testing.assert_array_equal(actual,prob[donor])


def test_recipient_support_and_empty_calibration_contract():
    truth=np.array(['a','b','never','a','b','a'])
    prob=np.array([[.8,.2],[.1,.9],[.7,.3],[.4,.6],[.9,.1],[.5,.5]])
    fp=np.tile([.6,.4],(6,1)); classes=np.array(['a','b'])
    memory={'prob':prob,'raw':prob.copy(),'classes':classes,'frequency_prob':fp,'frequency_classes':classes,
        'positions':np.arange(6),'questions':np.array([1,1,1,2,2,2]),
        'train_labels':np.array(['a']*40+['b']*10),'train_questions':np.tile([10,11],25)}
    meta=pd.DataFrame({'QuestionId':memory['questions'],'QuestionText':['one']*3+['two']*3,
        'MC_Answer':['choice']*6,'StudentExplanation':['same']*6})
    maps=c.mappings(meta,memory['positions'],0)
    rows=c.score_fold('factorized',0,memory,truth,maps,lambda *_:None)
    for stratum,n in [('unsupported',1),('rare',2),('frequent',3),('well_supported',3)]:
        row=next(r for r in rows if r['question'] is None and r['stratum']==stratum)
        assert row['n']==n and row['calibration']['scaled']['ece'] is None
        if stratum=='unsupported':
            assert row['original']['map_at_3']==0
            assert row['shuffled']['explanation_shuffle']['map_at_3']['score']['values']==[0]*100
    assert core.e001.temperature_scale(np.array(['never']*6),prob,classes)==(1.,0)


def test_monitor_io_failure_isolated(tmp_path,monkeypatch):
    from map_misconceptions import resilient_status
    def fail(*args): raise PermissionError(13,'synthetic monitor failure')
    monkeypatch.setattr(resilient_status.os,'replace',fail)
    with c.ResilientStatus(tmp_path/'status.json',experiment_id='E016',total=1) as live:
        value=core.meaningful([.02]*5); live.update('Synthetic work complete',completed=1)
    assert value['criterion_met'] and live.diagnostics()['status']=='COMPLETED'
    assert live.diagnostics()['io_failures']>=1


def test_published_result_if_present():
    path=Path(__file__).resolve().parents[1]/'results/E016_aggregates.json'
    if not path.exists(): pytest.skip('E016 not yet run or published.')
    x=json.loads(path.read_text()); p.validate(x)
    same((path.parents[1]/'docs/E016_RESULTS.md').read_text(),p.render(x))


def test_factorization_alignment_frequency_identity_absent_categories():
    f=synthetic().iloc[:8].copy()
    f.loc[f.index[:2],['Category','Misconception']]=['False_Misconception','SecondSynthetic']
    conditional=c.conditional_frequencies(f)
    categories=np.array(['True_Correct','False_Misconception'])  # Deliberately reverse sorted order.
    cats=c.checked_categories(f)
    prevalence=np.asarray([np.mean(cats==cat) for cat in categories])[None,:]
    prob,classes=c.reconstruct(prevalence,categories,conditional)
    expected,ec=core.e001.frequency_probabilities(f,f.iloc[:1])
    np.testing.assert_array_equal(classes,ec)
    np.testing.assert_allclose(prob,expected,atol=1e-12,rtol=0)
    direct=np.array([[.2,.8],[.9,.1]])
    reconstructed,_=c.reconstruct(direct,categories,conditional)
    marginal=c.marginalize(reconstructed,classes)
    for idx,cat in enumerate(categories):
        np.testing.assert_allclose(marginal[:,core.CATEGORIES.index(cat)],direct[:,idx],atol=1e-12,rtol=0)
    assert np.all(marginal[:,core.CATEGORIES.index('False_Neither')]==0)
    samecat=np.array([y.startswith('False_Misconception:') for y in classes])
    ratio=reconstructed[:,samecat][:,0]/reconstructed[:,samecat][:,1]
    np.testing.assert_allclose(ratio,ratio[0])
    # No hard gate: all observed Categories remain represented.
    assert (reconstructed>0).all()
    with pytest.raises(ValueError): c.reconstruct(direct,np.array(['True_Correct','False_Neither']),conditional)
    with pytest.raises(ValueError): c.reconstruct(np.array([[np.nan,0]]),categories,conditional)


def test_inner_counts_not_outer_counts_or_validation_labels(monkeypatch):
    f=synthetic(); train=f[f.QuestionId<9].copy()
    train['Misconception']=['Label'+str(q) for q in train.QuestionId]
    calls=[]; original=c.fit_model
    def fitting(part,arm,params):
        fitted=original(part,arm,params)
        classes,_,weights=fitted[2]
        assert set(classes)==set(combined_label(part))
        assert set(classes)!=set(combined_label(train))
        for cat in set(c.checked_categories(part)):
            cat_labels=[x for x in classes if x.startswith(cat+':')]
            for label in cat_labels:
                expected=(combined_label(part)==label).sum()/(part.Category==cat).sum()
                assert weights[list(classes).index(label)]==expected
        calls.append(set(part.QuestionId))
        return fitted
    monkeypatch.setattr(c,'fit_model',fitting)
    c.select(train,'factorized',lambda:None)
    expected=[set(train.iloc[left].QuestionId) for left,_ in c.GroupKFold(3).split(train,combined_label(train),train.QuestionId.astype(str))]
    assert calls==expected*3


def test_direct_category_fit_and_input_unchanged():
    f=synthetic()
    fitted=c.fit_model(f,'factorized',core.e001.GRID[1])
    vectorizer,classifier,_=fitted
    assert set(classifier.classes_)==set(f.Category)
    assert vectorizer.token_pattern==r'(?u)\b\w\w+\b'
    assert classifier.class_weight is None and classifier.max_iter==2000
    with pytest.raises(ValueError): c.fit_model(f[f.Category=='True_Correct'],'factorized',core.e001.GRID[0])
    bad=f.copy(); bad.Category='Unexpected'
    with pytest.raises(ValueError): c.fit_model(bad,'factorized',core.e001.GRID[0])


def test_exact_calibration_does_not_treat_category_support_as_label_support(monkeypatch):
    f=synthetic(); a=assignments(f,0); original=core.e001.temperature_scale; seen=[]
    f.loc[a.fold_0=='calibration','Misconception']='UnsupportedExact'
    def scale(truth,prob,classes):
        assert set(x.split(':',1)[0] for x in truth).issubset(core.CATEGORIES)
        assert not np.isin(truth,classes).any()
        seen.append(True)
        return original(truth,prob,classes)
    monkeypatch.setattr(core.e001,'temperature_scale',scale)
    d,m,_=c.prepare(f,a,0,'factorized',lambda:None)
    assert d['temperature']==1 and d['calibration_supported_n']==0 and seen==[True]


def test_raw_direct_vs_final_marginalized_category_semantics():
    classes=np.array(['False_Misconception:a','False_Misconception:b','True_Correct:NA'])
    raw=np.array([[.3,.3,.4]])
    direct=c.marginalize(raw,classes)
    final=core.e001.apply_temperature(raw,.25)
    memory={'raw':raw,'prob':final,'classes':classes,'category_raw':direct,'questions':np.array([1])}
    rows=c.category_records('factorized',0,memory,np.array(['False_Misconception:a']))
    assert next(r for r in rows if r['scale']=='raw' and r['question'] is None)['accuracy']==1.
    assert next(r for r in rows if r['scale']=='final' and r['question'] is None)['accuracy']==0.
    assert core.map_at_3(np.array(['True_Correct:unsupported']),final,classes)==0.


def test_no_exact_labels_or_category_inventory_from_evaluation():
    f=synthetic(); a=assignments(f,0)
    d,m,fitted=c.prepare(f,a,0,'factorized',lambda:None)
    evaluation=f[a.fold_0=='evaluation'][c.FEATURES].copy()
    before=[x.copy() for x in fitted[2]]
    evaluation.StudentExplanation='entirelyunseenevaluationword'
    c.predict(fitted,evaluation)
    for old,new in zip(before,fitted[2]): np.testing.assert_array_equal(old,new)
    assert 'entirelyunseenevaluationword' not in fitted[0].vocabulary_
    for value in m.values():
        if isinstance(value,np.ndarray): assert not value.flags.writeable


def test_six_category_multinomial_and_fixed_macro_f1():
    f=synthetic()
    f['Category']=[core.CATEGORIES[i%6] for i in range(len(f))]
    f['Misconception']=['Synthetic'+str(i%3) for i in range(len(f))]
    fitted=c.fit_model(f,'factorized',core.e001.GRID[0])
    assert set(fitted[1].classes_)==set(core.CATEGORIES)
    prob,classes=c.predict(fitted,f[c.FEATURES])
    raw,cc=c.category_predict(fitted,f[c.FEATURES])
    np.testing.assert_allclose(c.marginalize(prob,classes),raw,rtol=0,atol=1e-12)
    assert list(cc)==list(core.CATEGORIES)
    memory={'prob':prob,'classes':classes,'category_raw':raw,'questions':f.QuestionId.to_numpy()}
    rows=c.category_records('factorized',0,memory,combined_label(f).to_numpy())
    assert len(rows)==32
