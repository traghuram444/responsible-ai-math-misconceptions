"""Synthetic E017 tests; no MAP training data or new research scores are accessed."""
from copy import deepcopy
import inspect
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from sklearn.metrics import f1_score
from map_misconceptions import e017 as c, e017_publication as p
from map_misconceptions.e011_publication import same
from map_misconceptions.data_contract import combined_label


def synthetic():
    frame=pd.DataFrame([{'QuestionId':q,'QuestionText':f'synthetic exercise {q}', 'MC_Answer':str(i%3),
        'StudentExplanation':f'synthetic explanation pattern {i%5}', 'Category':c.core.CATEGORIES[i%6],
        'Misconception':'Synthetic'+str(i%6)} for q in range(15) for i in range(24)])
    frame.loc[0,'Misconception']='SyntheticRare'
    assignments=pd.DataFrame({f'fold_{f}':np.where(frame.QuestionId//3==f,'evaluation',
        np.where(frame.QuestionId//3==(f+1)%5,'calibration','train')) for f in range(5)})
    return frame,assignments


@pytest.fixture(scope='module')
def payload():
    frame,assignments=synthetic(); prepared={}; development=[]
    for fold in range(5):
        for arm in c.previous.ARMS:
            prepared[arm,fold]=c.previous.prepare(frame,assignments,fold,arm,lambda:None)
            development.append({'learning_arm':arm,**prepared[arm,fold][0]})
    real,oracle,cats,joint,residual=[],[],[],[],[]
    for fold in range(5):
        base=prepared['E011',fold][1]
        truth=combined_label(frame.iloc[base['positions']]).to_numpy()
        truth[0]='False_Correct:UnsupportedSynthetic'
        domains=c.prior.scopes(base,truth)
        for arm in c.REAL:
            memory=c.frequency_memory(base) if arm=='F' else prepared['factorized' if arm=='E016' else arm,fold][1]
            top,pred=c.prior.rank_labels(memory['prob'],memory['classes'])
            real.extend(c.exact_records(arm,fold,domains,c.prior.row_scores(truth,top,pred)))
            cr,jr=c.component_records(arm,fold,memory,truth,domains); cats.extend(cr); joint.extend(jr)
        bank=c.oracle_bank(base['frequency_classes'],base['frequency_prob'][0])
        scores,ranks=c.oracle_scores(truth,bank)
        for arm in ('F',*c.ORACLES): oracle.extend(c.exact_records(arm,fold,domains,scores[arm],oracle=True))
        residual.extend(c.residual_records(fold,domains,scores['O_CS'],ranks['O_CS']))
    return {'experiment_id':'E017','status':'COMPLETED','development':development,
        **c.build_panels(real,oracle,cats,joint,residual),
        'provenance':{'git_revision':'a'*40,'image_id':'sha256:'+'b'*64,'lock_sha256':'c'*64,
            'frozen_development_sha256':'d'*64,'started_utc':'2026-10-19T00:00:00+00:00',
            'finished_utc':'2026-10-19T00:01:00+00:00','wall_seconds':60.,'model_fits':100,
            'fit_warnings':0,'reproduction_model_folds':15,'global_freeze_verified':True,
            'preservation_verified':True,'uid':10001,'gid':10001,'row_level_outputs':False,'preserved_files':247}}


def test_oracle_training_only_api_and_immutable_tied_subsequence():
    labels=np.asarray([f'{cat}:Synthetic{i:02}' for cat in c.core.CATEGORIES for i in range(9)])
    freq=np.ones(len(labels))/len(labels)
    bank=c.oracle_bank(labels,freq)
    order=tuple(labels[np.argsort(-freq)])
    assert bank['F'][None][0]==order and bank['F'][None][1]==labels[0]
    for arm,part in c.SUPPLIED.items():
        for value,(rank,pred) in bank[arm].items():
            allowed=[y for y in labels if part is None or c.components([y])[part][0]==value]
            assert rank==tuple(y for y in order if y in allowed)
            assert pred==(allowed[0] if allowed else None)
    with pytest.raises(TypeError): bank['O_C']['False']=((),None)
    with pytest.raises(TypeError): bank['F']={}
    assert list(inspect.signature(c.oracle_bank).parameters)==['classes','frequency']


def test_empty_short_absent_categories_and_unsupported_exact():
    labels=np.array(['False_Misconception:a','False_Misconception:b','True_Correct:NA'])
    bank=c.oracle_bank(labels,np.array([.5,.3,.2]))
    truth=np.array(['False_Misconception:b','True_Correct:NA','True_Correct:unseen','True_Neither:unseen'])
    scores,ranks=c.oracle_scores(truth,bank)
    np.testing.assert_array_equal(scores['O_CS']['map_at_3'],[.5,1,0,0])
    np.testing.assert_array_equal(scores['O_CS']['top1_accuracy'],[0,1,0,0])
    assert bank['O_CS']['True_Neither']==((),None)
    assert len(bank['O_CS']['False_Misconception'][0])==2
    assert ranks['O_CS'].tolist()==[2,1,0,0]


@pytest.mark.parametrize('seed',range(8))
def test_monotonicity_and_frequency_endpoint(seed):
    rng=np.random.default_rng(seed)
    labels=np.array([f'{cat}:Synthetic{i}' for cat in c.core.CATEGORIES for i in range(4)])
    counts=rng.integers(1,8,len(labels)); freq=counts/counts.sum()
    bank=c.oracle_bank(labels,freq)
    truth=np.concatenate([labels,['True_Correct:unsupported']])
    scores,_=c.oracle_scores(truth,bank)
    prob=np.tile(freq,(len(truth),1))
    top,pred=c.prior.rank_labels(prob,labels)
    baseline=c.prior.row_scores(truth,top,pred)
    for metric in c.METRICS: np.testing.assert_array_equal(scores['F'][metric],baseline[metric])


@pytest.mark.parametrize('labels,freq',[
    (['Unknown:a'],[1.]),(['True_Correct:b','False_Correct:a'],[.5,.5]),
    (['True_Correct:a','True_Correct:a'],[.5,.5]),(['True_Correct:a'],[0.]),
    (['True_Correct:a'],[float('nan')]),([],[])])
def test_invalid_inventory_stops(labels,freq):
    with pytest.raises(ValueError): c.oracle_bank(np.array(labels),np.array(freq))


def test_components_marginalization_not_hard_category_split():
    prob=np.array([[.05,.28,.20,.30,.10,.07]])
    pred=c.component_predictions(prob)
    assert pred['category'][0]=='True_Correct'
    assert pred['correctness'][0]=='False'
    assert pred['status'][0]=='Misconception'


def test_confusion_fixed_macro_f1_and_null_rows():
    cm=np.array([[3,1,0],[2,0,0],[0,0,0]])
    actual,normalized=c.matrix_metrics(cm)
    truth=[0]*4+[1]*2; prediction=[0]*3+[1]+[0]*2
    assert actual['macro_f1']==pytest.approx(f1_score(truth,prediction,labels=[0,1,2],average='macro',zero_division=0))
    assert actual['accuracy']==.5 and normalized[2]==[None]*3
    empty,norm=c.matrix_metrics(np.zeros((6,6),int))
    assert empty=={'accuracy':None,'macro_f1':None} and norm==[[None]*6]*6


def test_residual_loss_and_rank_bands():
    labels=np.array([f'False_Misconception:{i}' for i in range(4)])
    truth=np.concatenate([labels,['True_Correct:unseen']])
    scores,ranks=c.oracle_scores(truth,c.oracle_bank(labels,np.array([.4,.3,.2,.1])))
    rows=c.residual_records(0,[(None,'all',np.ones(5,bool))],scores['O_CS'],ranks['O_CS'])
    assert rows[0]['counts']==dict.fromkeys(c.BANDS,1)
    same(rows[0]['metrics']['total_loss_map_at_3'],1-(1+.5+1/3)/5)
    assert rows[0]['metrics']['unsupported_loss']==.2


def test_primary_exact_boundary_and_fold_consistency():
    def rows(values):
        return [{'left':a,'right':'F','question':None,'stratum':'all','fold':f,'metrics':{'map_at_3':v}}
                for a in c.ORACLES for f,v in enumerate(values)]
    for vals,expected in [([.02]*5,True),([.019999999]*5,False),([.04,.04,.04,0,0],False),([.025]*4+[0],True)]:
        result=c.headroom(rows(vals))
        assert all(x['criterion_met']==expected for x in result)
        assert [x['primary'] for x in result]==[False,False,True]


def test_global_truth_barrier_and_no_oracle_to_prediction_flow():
    source=inspect.getsource(c.main)
    assert source.index('previous.prepare(')<source.index('banks[fold] = oracle_bank(')<source.index("write_new(output / 'frozen_development.json'")<source.index('truths =')<source.index('reproduce(')<source.index('oracle_scores(')
    assert 'mappings(' not in source and 'score_fold(' not in source
    assert source.count('previous.prepare(')==1
    assert "latest_metrics={f'ORACLE" in source and "latest_metrics={f'REAL" in source
    assert 'ResilientStatus(' in source and 'completed=146' in source
    oracle_source=inspect.getsource(c.oracle_scores)
    assert 'fit(' not in oracle_source and 'prepare(' not in oracle_source and 'temperature' not in oracle_source


@pytest.mark.parametrize('arm',c.previous.ARMS)
def test_evaluation_truth_does_not_change_reconstruction(arm):
    frame,assignments=synthetic()
    before=c.previous.prepare(frame,assignments,0,arm,lambda:None)
    changed=frame.copy(); changed.loc[assignments.fold_0=='evaluation',['Category','Misconception']]=['HIDDEN','TARGET']
    after=c.previous.prepare(changed,assignments,0,arm,lambda:None)
    same(before[0],after[0]); np.testing.assert_array_equal(before[1]['prob'],after[1]['prob'])
    for array in after[1].values():
        if isinstance(array,np.ndarray): assert not array.flags.writeable


def test_synthetic_full_payload_and_deterministic_report(payload):
    p.validate(payload)
    text=p.render(payload)
    assert 'Real prediction controls' in text and 'Oracle diagnostics using evaluation truth' in text
    assert 'UnsupportedSynthetic' not in text
    assert text==p.render(deepcopy(payload))
    assert len(payload['real_prediction']['records'])==300
    assert len(payload['oracle_diagnostic']['records'])==400
    assert len(payload['real_prediction']['component_records'])==1800


@pytest.mark.parametrize('corruption',range(11))
def test_publication_rejects_corruption_and_private_fields(payload,corruption):
    bad=deepcopy(payload)
    if corruption==0: bad['raw_student_text']='forbidden synthetic'
    if corruption==1: bad['oracle_diagnostic']['records'][0]['supplied_component']='category'
    if corruption==2: bad['real_prediction']['records'][0]['arm']='O_CS'
    if corruption==3: bad['real_prediction']['aggregate'][0]['metrics']['map_at_3']['mean']=.987
    if corruption==4: bad['real_prediction']['component_records'][0]['confusion_counts'][0][0]+=1
    if corruption==5: bad['oracle_diagnostic']['headroom'][0]['primary']=True
    if corruption==6: bad['oracle_diagnostic']['residual_records'][0]['counts']['unsupported']+=1
    if corruption==7: bad['real_prediction']['component_records'].pop()
    if corruption==8: bad['real_prediction']['joint_records'][0]['counts']['both_correct']+=1
    if corruption==9: bad['oracle_diagnostic']['records'][0]['metrics']['map_at_3']=float('nan')
    if corruption==10: bad['development'][0]['selection']['selected_index']=99
    with pytest.raises(ValueError): p.validate(bad)


def test_historical_gate_detects_mismatch_before_new_scores(monkeypatch):
    # The production gate imports the unchanged comparison routine and is strict.
    source=inspect.getsource(c.reproduce)
    for required in ('prior.check_reproduction','original_records','category_records','risk_coverage','same('):
        assert required in source
    with pytest.raises(ValueError): same({'n':1},{'n':2})
    with pytest.raises(ValueError): same(None,0.)
    with pytest.raises(ValueError): same(.5,.500000001)


def test_monitor_io_failure_does_not_stop_work(tmp_path,monkeypatch):
    from map_misconceptions import resilient_status as rs
    def denied(*args): raise PermissionError(13,'synthetic failure')
    monkeypatch.setattr(rs.os,'replace',denied)
    with rs.ResilientStatus(tmp_path/'live_status.json',experiment_id='E017',total=1) as live:
        live.update('Synthetic isolated monitor check',completed=1,latest_metrics={'ORACLE synthetic':.5})
    assert live.diagnostics()['status']=='COMPLETED' and live.diagnostics()['io_failures']>0


def test_approved_protocol_unchanged():
    root=Path(__file__).resolve().parents[1]
    approval=json.loads((root/'experiments/e017_approval.json').read_text())
    assert approval['protocol_sha256_lf']==c.core.canonical_sha(root/'docs/E017_PROTOCOL.md')
    assert not approval['automatic_retry_authorized'] and not approval['next_experiment_authorized']


def test_published_artifact_when_available():
    root=Path(__file__).resolve().parents[1]; path=root/'results/E017_aggregates.json'
    if not path.exists(): pytest.skip('E017 not executed/published yet.')
    value=json.loads(path.read_text()); p.validate(value)
    assert p.render(value)==(root/'docs/E017_RESULTS.md').read_text()
    reference=json.loads((root/'results/E016_aggregates.json').read_text())
    same(value['development'],reference['development'])
    for r in value['real_prediction']['records']:
        old=next(x for x in reference['records'] if x['model']=={'F':'frequency','E011':'E011','E016':'factorized'}[r['arm']] and all(x[k]==r[k] for k in ('fold','question','stratum')))
        same(r['metrics'],old['original']); same(r['n'],old['n'])
