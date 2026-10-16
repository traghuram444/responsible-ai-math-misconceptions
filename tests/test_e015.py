"""Synthetic E015 verification only; never reads MAP training data."""
from copy import deepcopy
import inspect
import json
from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import pytest
from map_misconceptions import e015 as c, e015_publication as p, e011_context as core
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


@pytest.mark.parametrize('text,a,b,expected',[
    ('I got -3.5',['got'],['i','got','3','5'],['i','got','-','3','.','5']),
    ('12/34',['12','34'],['12','34'],['12','/','34']),
    ('x<=2',[],['x','2'],['x','<=','2']),
    ('[ANSWER] 1/2',['answer'],['answer','1','2'],['answer','1','/','2']),
    (r'\frac{1}{2}',['frac'],['frac','1','2'],['\\','frac','{','1','}','{','2','}']),
    ('a−b',[],['a','b'],['a','−','b'])])
def test_exact_registered_examples(text,a,b,expected):
    for arm,result in zip(c.ARMS,(a,b,expected)):
        v=c.make_vectorizer(arm,core.e001.GRID[0])
        assert v.build_tokenizer()(v.build_preprocessor()(text))==result


def test_unicode_operators_markers_no_semantic_normalization():
    assert c.notation_tokens('[question] [answer] [explanation]')==['question','answer','explanation']
    assert c.notation_tokens('a_b α ≤ ≥ != == ** // − - × ÷ √ ∞ ≈')==['a_b','α','≤','≥','!=','==','**','//','−','-','×','÷','√','∞','≈']
    assert c.notation_tokens('1/2 0.5')==['1','/','2','0','.','5']
    assert c.notation_tokens('hello? €')==['hello']
    v=c.make_vectorizer('C',core.e001.GRID[1])
    assert v.build_analyzer()('x+1')==['x','+','1','x +','+ 1']
    assert v.token_pattern is None and v.analyzer=='word'
    with pytest.raises(ValueError): c.make_vectorizer('D',core.e001.GRID[0])


def test_training_only_vocabulary_and_warning_fatal(monkeypatch):
    f=synthetic(); fitted=c.fit_model(f[f.QuestionId<9],'C',core.e001.GRID[0])
    assert 'unseenevaluationword' not in fitted[0].vocabulary_
    features=f[f.QuestionId>=12][c.FEATURES].copy()
    features.StudentExplanation='unseenevaluationword'
    before=dict(fitted[0].vocabulary_); c.predict(fitted,features)
    assert fitted[0].vocabulary_==before
    original=c.LogisticRegression.fit
    def noisy(self,*args,**kwargs):
        warnings.warn('synthetic warning'); return original(self,*args,**kwargs)
    monkeypatch.setattr(c.LogisticRegression,'fit',noisy)
    with pytest.raises(RuntimeError): c.fit_model(f,'C',core.e001.GRID[0])


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
    d,m,_=c.prepare(f,a,0,'A',lambda:calls.append(1))
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
                        f[f.QuestionId>=12],np.arange(24),0,'A',lambda:None)


def test_calibration_receives_only_reserved_truths(monkeypatch):
    f=synthetic(); a=assignments(f,0); original=core.e001.temperature_scale; calls=[]
    def scaling(truth,prob,classes):
        np.testing.assert_array_equal(truth,combined_label(f[a.fold_0=='calibration']).to_numpy())
        calls.append(1); return original(truth,prob,classes)
    monkeypatch.setattr(core.e001,'temperature_scale',scaling)
    c.prepare(f,a,0,'C',lambda:None)
    assert len(calls)==1


def test_coverage_denominators_and_training_vocabulary():
    v=c.make_vectorizer('C',{'ngram_range':(1,2),'min_df':1,'C':1.})
    v.fit(['x+1','x+1'])
    g=c.token_coverage(v,['x+1','z',''])
    assert g['n']==3 and g['blank_n']==1 and g['zero_token_n']==1 and g['zero_surviving_feature_n']==2
    assert g['occurrences']['unigram']=={'covered':3,'total':4,'coverage':.75}
    assert g['occurrences']['short_word']=={'covered':2,'total':3,'coverage':2/3}
    assert g['occurrences']['notation']=={'covered':1,'total':1,'coverage':1.}
    assert g['occurrences']['selected_analyzer']=={'covered':5,'total':6,'coverage':5/6}
    empty=c.token_coverage(v,[''])
    assert all(x['coverage'] is None for x in empty['occurrences'].values())


def test_global_barrier_and_reproduction_before_new_scores():
    source=inspect.getsource(c.main)
    assert source.index("write_new(output/'frozen_development.json'")<source.index('truths=')<source.index('prior.check_reproduction(')<source.index('score_fold(')
    assert "for model in ('A','frequency','B','C')" in source
    assert "if model=='frequency' and fold==4:" in source
    assert 'reproduction_diagnostic(' in source and 'ResilientStatus(' in source
    assert "same(core.answer_diagnostics(frame),ref11['answer_diagnostics'])" in source


def test_primary_exact_margin_consistency_and_no_winner_switch():
    def rows(delta):
        return [{'model':m,'fold':f,'question':None,'stratum':'all','n':1,
            'original':{metric:delta[f] if m=='C' else 0. for metric in c.METRICS},
            'calibration':{kind:{k:None for k in ('ece','brier')} for kind in ('raw','scaled')}}
                for m in c.MODELS for f in range(5)]
    assert c.primary(rows([.020]*5))['criterion_met']
    assert not c.primary(rows([.019999]*5))['criterion_met']
    assert not c.primary(rows([.1,.1,.1,0,0]))['criterion_met']
    assert not c.primary(rows([0]*5))['criterion_met']


@pytest.fixture(scope='module')
def payload():
    f=synthetic(); dev=[]; rows=[]; opportunities=[]; diagnostics=[]; routes=[]; categories=[]; coverage=[]
    for fold in range(5):
        a=assignments(f,fold); parts={}
        for arm in c.ARMS:
            d,m,v=c.prepare(f,a,fold,arm,lambda:None); parts[arm]=(d,m,v)
            dev.append({'tokenizer_arm':arm,**d})
        d,m,v=parts['A']; meta=f.iloc[m['positions']][c.FEATURES]
        truth=combined_label(f.iloc[m['positions']]).to_numpy(); maps=c.mappings(meta,m['positions'],fold)
        opportunities.extend(c.opportunity(meta,m['positions'],fold,maps,truth))
        donor=maps['explanation_shuffle']['donors'][0]
        perturbed=meta.copy(); perturbed.StudentExplanation=meta.StudentExplanation.to_numpy()[donor]
        np.testing.assert_array_equal(core.input_text(perturbed,'full_context'),core.input_text(meta,'full_context').to_numpy()[donor])
        for model in c.MODELS:
            d,m,v=parts['A' if model=='frequency' else model]
            if model=='frequency':
                m={**m,'prob':m['frequency_prob'],'raw':m['frequency_prob'],'classes':m['frequency_classes'],'order':m['frequency_order']}
                d={**d,'temperature':1.}
            else:
                # Rowwise temperature scaling commutes with donor indexing.
                np.testing.assert_array_equal(core.e001.apply_temperature(m['raw'][donor],d['temperature']),m['prob'][donor])
                coverage.extend(c.coverage_records(v,meta,model,fold))
            diagnostics.append(c.probability_diagnostic(model,fold,d,m))
            rows.extend(c.score_fold(model,fold,m,truth,maps,lambda *_:None))
            evaluated=core.evaluate(d,m,truth)
            routes.append({'model':model,'fold':fold,'budgets':evaluated['risk_coverage']})
            categories.extend([{'model':model,'fold':fold,'question':q,**g} for q,g in
                [(None,evaluated['category']),*[(r['QuestionId'],r['category']) for r in evaluated['questions']]]])
    return {'experiment_id':'E015','status':'COMPLETED','development':dev,'records':rows,
        'aggregate':c.summarize(rows),'primary':c.primary(rows),'contrasts':c.contrasts(rows),
        'contrast_aggregate':c.contrast_summary(c.contrasts(rows)),'opportunity':opportunities,
        'probability_diagnostics':diagnostics,'routing':routes,'routing_aggregate':c.routing_summary(routes),
        'category':categories,'coverage':coverage,
        'provenance':{'git_revision':'a'*40,'image_id':'sha256:'+'a'*64,'lock_sha256':'a'*64,'frozen_development_sha256':'a'*64,
            'started_utc':'2026-10-16T00:00:00+00:00','finished_utc':'2026-10-16T00:00:01+00:00','wall_seconds':1.,
            'model_fits':150,'fit_warnings':0,'reproduction_model_folds':5,'global_freeze_verified':True,
            'preservation_verified':True,'uid':10001,'gid':10001,'replicates':100,'permutation_seed':20261014,
            'row_level_outputs':False,'preserved_files':219}}


def test_full_synthetic_pipeline_and_report(payload):
    p.validate(payload); report=p.render(payload)
    assert 'Complete inner development' in report and 'Complete fold review' in report
    assert 'synthetic explanation' not in json.dumps(payload) and 'SyntheticError' not in json.dumps(payload)
    assert len(payload['records'])==400 and len(payload['coverage'])==240 and len(payload['category'])==80


@pytest.mark.parametrize('damage',['aggregate','primary','replicate','count','private','setting','route','temperature','contrast','coverage','category','calibration_delta'])
def test_reject_corrupt_artifact(payload,damage):
    x=deepcopy(payload)
    if damage=='aggregate': x['aggregate'][0]['original']['map_at_3']['mean']+=.1
    if damage=='primary': x['primary']['criterion_met']=not x['primary']['criterion_met']
    if damage=='replicate': x['records'][0]['shuffled']['explanation_shuffle']['map_at_3']['score']['values'][0]+=.1
    if damage=='count': x['records'][0]['n']+=1
    if damage=='private': x['coverage'][0]['vocabulary']=['private']
    if damage=='setting': x['development'][0]['selection']['selected_index']=7
    if damage=='route': x['routing'][0]['budgets'][1]['all']['retained_n']+=1
    if damage=='temperature': x['development'][0]['temperature']=1000.
    if damage=='contrast': x['contrasts'][0]['deltas']['map_at_3']+=.1
    if damage=='coverage': x['coverage'][0]['occurrences']['unigram']['covered']+=1
    if damage=='category': x['category'][0]['n']+=1
    if damage=='calibration_delta': x['contrasts'][0]['calibration_deltas']['scaled']['ece']=.1
    with pytest.raises((ValueError,IndexError)): p.validate(x)


def test_approved_protocol_and_preservation():
    root=Path(__file__).resolve().parents[1]
    approval=json.loads((root/'experiments/e015_approval.json').read_text())
    assert core.canonical_sha(root/'docs/E015_PROTOCOL.md')==approval['protocol_sha256_lf']
    if (root/'experiments/e015_lock.json').exists():
        lock=json.loads((root/'experiments/e015_lock.json').read_text())
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
    rows=c.score_fold('C',0,memory,truth,maps,lambda *_:None)
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
    with c.ResilientStatus(tmp_path/'status.json',experiment_id='E015',total=1) as live:
        value=core.meaningful([.02]*5); live.update('Synthetic work complete',completed=1)
    assert value['criterion_met'] and live.diagnostics()['status']=='COMPLETED'
    assert live.diagnostics()['io_failures']>=1


def test_published_result_if_present():
    path=Path(__file__).resolve().parents[1]/'results/E015_aggregates.json'
    if not path.exists(): pytest.skip('E015 not yet run or published.')
    x=json.loads(path.read_text()); p.validate(x)
    same((path.parents[1]/'docs/E015_RESULTS.md').read_text(),p.render(x))
