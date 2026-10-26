"""Entire E020 reporting grid tested with invented arrays, never MAP records/models."""
import copy
import importlib.util
import json
from pathlib import Path
import numpy as np
import pytest
from map_misconceptions import e020_map_metrics as m,e020_map_publication as pub,e020_selection as select
from map_misconceptions.e020_fusion import WEIGHTS
from map_misconceptions.selective import _routing_order


def module_script(name):
    path=Path(__file__).resolve().parents[1]/'scripts'/name
    spec=importlib.util.spec_from_file_location(name[:-3],path)
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module


@pytest.fixture(scope='module')
def experiment():
    caches={k:[{'scores':([.7,.2,.1] if i%2 else [.1,.7,.2]) if k=='G7' else [.4,.3,.3],
                'decision':(0 if i%2 else 1) if k=='G7' else 0,'reason':'readout_completed'} for i in range(60)] for k in ('G15','G7')}
    prepared={}; plans={}; truths={}; ids={}; development=[]; ensembles=[]; collected=[[],[],[],[],[]]
    classes=np.array(['False_Correct:NA','True_Correct:NA']); offset=0
    for fold,n in enumerate([7339,7339,7339,7339,7340]):
        q=np.empty(n,dtype=int)
        for j,positions in enumerate(np.array_split(np.arange(n),3)): q[positions]=fold*3+j
        ids[fold]=q*4+np.arange(n)%4; ids[fold].setflags(write=False)
        f=np.tile([.6,.4],(n,1)); l=np.tile([.3,.7],(n,1))
        signals={k:np.asarray([rows[i]['scores'] for i in ids[fold]]) for k,rows in caches.items()}
        candidates=[{'weights':list(w),'inner_fold_map_at_3':[.6 if i==1 else .5]*3,
            'inner_mean_map_at_3':.6 if i==1 else .5} for i,w in enumerate(WEIGHTS)]
        weights={'H':{'selected_index':1,'selected_weights':list(WEIGHTS[1]),'candidates':candidates},
            'B':{'selected_index':1,'selected_weights':list(WEIGHTS[1]),'candidates':[r for r in candidates if r['weights'][2]==0]}}
        raw=select.raw_arms(f,l,classes,signals['G15'],signals['G7'],0,weights)
        positions=np.arange(offset,offset+n); offset+=n
        plans[fold]={a:{'raw':raw[a],'final':raw[a],'order':_routing_order(raw[a]['confidence'],positions.tolist(),fold,m.old.core.SEED)} for a in m.ARMS}
        for plan in plans[fold].values(): plan['order'].setflags(write=False)
        train=np.array([classes[0]]*600+[classes[1]]*400)
        mem={'classes':classes,'positions':positions,'questions':q,'train_labels':train,'train_questions':np.arange(1000)%9,
             'raw':l,'prob':l,'frequency_prob':f,'frequency_classes':classes,'order':plans[fold]['L']['order'],'frequency_order':plans[fold]['F']['order']}
        for x in mem.values(): x.setflags(write=False)
        grid=[{'params':{**r,'ngram_range':list(r['ngram_range'])},'inner_fold_map_at_3':[.5]*3,'inner_mean_map_at_3':.5} for r in m.old.core.e001.GRID]
        d={'arm':'full_context','model':'logistic','fold':fold,'n_train':1000,'n_calibration':300,'n_evaluation':n,
            'role_question_counts':[9,3,3],'selection':{'selected_index':0,'candidates':grid},'temperature':1.,'calibration_supported_n':300,'fits':10}
        prepared[fold]=(d,mem,None); development.append(d)
        ensembles.append({'fold':fold,'weights':weights,'calibration':{a:{'temperature':1.,'supported_n':300,
            'method':'unscaled' if a in ('F','F_M','G7_hard') else 'own_temperature'} for a in m.ARMS},
            'majority_correctness':False,'training_counts':{'false':600,'true':400}})
        truth=np.resize(classes,n).astype(object); truth[::7]='False_Misconception:UNSUPPORTED_SYNTHETIC_LABEL'; truths[fold]=truth
        for dest,rows in zip(collected,m.score_fold(fold,mem,truth,plans[fold])): dest.extend(rows)
    p={'experiment_id':'E020','status':'COMPLETED','development':development,'ensemble_development':ensembles,
       **m.build_panels(*collected),'correctness_audit':m.correctness(prepared,truths,ids,caches,ensembles)}
    checkers=[]
    for k in ('G15','G7'):
        checkers.append({'model':k,'pairs':60,'reason_counts':{r:60 if r=='readout_completed' else 0 for r in pub.REASONS},
            'truncated_rationales':0,**{key:m.distribution([.5 if key=='candidate_mass' else 3]*60)
                for key in ('input_tokens','generated_tokens','readout_tokens','candidate_mass')},
            'generation_seconds':1.,'readout_seconds':1.,'checker_seconds':2.,'peak_rss_bytes':100,'container_peak_bytes':100})
    p['resource_summary']={'checkers':checkers,'statistical_seconds':1.,'solver_image_id':'sha256:'+'a'*64,
        'statistical_image_id':'sha256:'+'b'*64,'environment_lock_sha256':'c'*64,'solver_memory_limit_bytes':24*1024**3}
    p['integrity']={'git_revision':'a'*40,'lock_sha256':'b'*64,'readiness_result_sha256':'c'*64,'cache_sha256':{'G15':'d'*64,'G7':'e'*64},
        'frozen_development_sha256':'f'*64,'preserved_files':664,'preservation_verified':True,'global_freeze_verified':True,
        'e018_remains_blocked':True,'fit_warnings':0,'model_fits':50,'reproduction_model_folds':15,'row_level_outputs':False,'uid':10001,'gid':10001}
    return p,prepared,plans,ids,truths


def test_complete_registered_report(experiment):
    p,*_=experiment
    assert pub.validate(p) is p
    assert len(p['exact']['records'])==9*5*4*5
    assert len(p['calibration']['records'])==9*5*4*5*2
    assert len(p['comparisons']['records'])==11*5*4*5
    assert len(p['gain_loss']['records'])==5*5*4*5
    assert len(p['review']['records'])==9*5*6
    assert len(p['correctness_audit']['records'])==2*5*4
    assert all(r['n']==0 for r in p['exact']['records'] if r['stratum']=='rare')
    assert all(r['metrics']['map_at_3']==0 for r in p['exact']['records'] if r['stratum']=='unsupported')
    text=pub.render(p)
    assert 'Aggregate exact-label results' in text and 'Fold-level exact-label results' in text
    assert 'correctness_audit / projection_fallback' in text
    assert 'UNSUPPORTED_SYNTHETIC_LABEL' not in text


@pytest.mark.parametrize('mutation',[
    lambda p:p.update(private_text='must reject'),
    lambda p:p['exact']['records'].pop(),
    lambda p:p['calibration']['records'][0]['ineligible_reasons'].append('n_below_200'),
    lambda p:p['review']['records'][0]['metrics'].update(coverage=.9),
    lambda p:p['comparisons']['decisions'].update(H1_primary=not p['comparisons']['decisions']['H1_primary']),
    lambda p:p['ensemble_development'][0]['weights']['H'].update(selected_index=0),
    lambda p:p['correctness_audit']['records'][0]['confusion_counts'][0].__setitem__(0,0),
    lambda p:p['resource_summary']['checkers'][0]['reason_counts'].update(readout_completed=59),
    lambda p:p['rank_changes']['records'][0].update(top1_changed_n=999999),
])
def test_corrupt_or_private_report_rejected(experiment,mutation):
    p=copy.deepcopy(experiment[0]); mutation(p)
    with pytest.raises(ValueError): pub.validate(p)


def test_global_freeze_requires_all_folds_and_fits(experiment,tmp_path):
    from map_misconceptions.e020_map_run import freeze_predictions
    p,prepared,plans,ids,_=experiment
    with pytest.raises(ValueError): freeze_predictions(tmp_path,prepared,plans,p['development'],p['ensemble_development'],ids,49)
    assert not list(tmp_path.iterdir())
    digest,files=freeze_predictions(tmp_path,prepared,plans,p['development'],p['ensemble_development'],ids,50)
    assert len(digest)==64 and len(files)==5
    receipt=json.loads((tmp_path/'frozen_development_private.json').read_text())
    assert receipt['all_predictions_and_review_orders_frozen'] and receipt['model_fits']==50


def test_truth_boundary_and_single_pass_execution():
    root=Path(__file__).resolve().parents[1]
    text=(root/'src/map_misconceptions/e020_map_run.py').read_text()
    assert text.index('freeze_sha,files=freeze_predictions')<text.index('truths={f:combined_label')
    assert "frame.iloc[ev][selection.FEATURES]" in text
    launch=(root/'scripts/run_e020_map.py').read_text()
    assert "for key,model in (('G15'" in launch and "out.mkdir(exist_ok=False)" in launch
    assert "PYTHONHASHSEED=20261026" in launch and "PYTHONHASHSEED=20260831" in launch
    checker=(root/'scripts/e020_map_checker.py').read_text()
    assert 'load_training_data' not in checker and 'StudentExplanation' not in checker


def test_control_reproduction_rejects_changed_record(experiment,tmp_path,monkeypatch):
    from map_misconceptions import e020_map_run as run
    p,prepared,_,_,truths=experiment
    monkeypatch.setattr(run,'historical_reproduction',lambda *args:None)
    ref={'development':p['development'],'constant_development':[{k:r[k] for k in ('fold','majority_correctness','training_counts')} for r in p['ensemble_development']],
         'original_input_controls':{'records':[r for r in p['exact']['records'] if r['arm'] in ('F','L')]},
         'constant_filter_control':{'records':[r for r in p['exact']['records'] if r['arm']=='F_M']},
         'calibration':p['calibration'],'review':p['review']}
    ref=copy.deepcopy(ref)
    (tmp_path/'results').mkdir(); path=tmp_path/'results/E019_aggregates.json'; path.write_text(json.dumps(ref))
    run.reproduce(prepared,truths,p,p['ensemble_development'],tmp_path)
    ref['constant_filter_control']['records'][0]['metrics']['map_at_3']+=.01
    path.write_text(json.dumps(ref))
    with pytest.raises(ValueError): run.reproduce(prepared,truths,p,p['ensemble_development'],tmp_path)


def test_monitor_idle_and_combined_pair_progress(tmp_path):
    from datetime import datetime,timezone
    monitor=module_script('monitor_e020_map.py')
    assert monitor.snapshot(tmp_path) is None
    (tmp_path/'started.json').write_text(json.dumps({'started_utc':datetime.now(timezone.utc).isoformat()}))
    (tmp_path/'G7').mkdir()
    state={'status':'RUNNING','progress':{'completed':11},'stage':'G7 MAP','latest_metrics':{}}
    (tmp_path/'G7/status.json').write_text(json.dumps(state))
    snapshot=monitor.snapshot(tmp_path)
    assert snapshot['progress']=={'completed':71,'total':120,'percent':100*71/120}
    assert snapshot['latest_metrics']=={}
    (tmp_path/'orchestration_failure.json').write_text(json.dumps({'status':'FAILED'}))
    failed=monitor.snapshot(tmp_path)
    assert failed['status']=='FAILED' and failed['progress']['completed']==71


def test_fixed_review_ties_and_union_brier(experiment):
    p,prepared,plans,_,truths=experiment
    for fold in range(5):
        mem=prepared[fold][1]; n=len(truths[fold])
        expected=_routing_order(plans[fold]['F']['final']['confidence'],mem['positions'].tolist(),fold,20260831)
        np.testing.assert_array_equal(plans[fold]['F']['order'],expected)
        for b in (0,10,20,30,40,50):
            row=next(r for r in p['review']['records'] if r['arm']=='F' and r['fold']==fold and r['review_percent']==b)
            assert row['n']==n-n*b//100
    truth=np.array(['absent','False_Correct:NA'])
    prob=np.array([[.6,.4],[.6,.4]])
    prediction=m.old.filter_output(prob,prepared[0][1]['classes'],np.array([-1,-1]))
    from map_misconceptions.metrics_v2 import union_label_brier_score
    assert union_label_brier_score(truth,prediction['prob'],prepared[0][1]['classes'])==pytest.approx((1+.36+.16+.16+.16)/2)


def test_no_failure_retry_and_path_safe_evidence(tmp_path):
    from map_misconceptions.e020_map_integrity import no_failures,verify_readiness_evidence
    from map_misconceptions.e019_checker import sha
    attempt=tmp_path/'artifacts/e020_attempt01'; (attempt/'map_inputs').mkdir(parents=True)
    no_failures(attempt)
    path=attempt/'map_inputs/readiness_preservation_private.json'
    path.write_text(json.dumps({'../../outside':'a'*64}))
    with pytest.raises(ValueError): verify_readiness_evidence(tmp_path,{'readiness_private_inventory_sha256':sha(path)})
    (attempt/'map_inputs/preparation_failure.json').write_text('{}')
    with pytest.raises(ValueError): no_failures(attempt)


def test_valid_c_is_not_technical_unknown_identity():
    from map_misconceptions.e020_map_selection import calibrate
    classes=np.array(['False_Correct:NA','True_Correct:NA'])
    p=np.tile([.7,.3],(4,1)); unknown=np.tile([0.,0.,1.],(4,1))
    weights={'B':{'selected_weights':[1.,0.,0.]},'H':{'selected_weights':[0.,0.,1.]}}
    raw=select.raw_arms(p,p,classes,unknown,unknown,0,weights)
    false={k:np.zeros(4,dtype=bool) for k in ('G15','G7')}; true={k:np.ones(4,dtype=bool) for k in ('G15','G7')}
    truth=np.array([classes[1]]*4)
    valid,vr=calibrate(raw,raw,classes,truth,weights,false,false)
    fallback,fr=calibrate(raw,raw,classes,truth,weights,true,true)
    assert vr['G7']['method']=='own_temperature' and fr['G7']['method']=='all_unknown_frequency'
    assert fallback['G7'] is fallback['F'] and fallback['H'] is fallback['F']
    assert valid['H'] is valid['G7'] and not np.array_equal(valid['G7']['prob'],valid['F']['prob'])


def test_map_prepare_rejects_truth_and_bad_roles_before_fit():
    import pandas as pd
    from map_misconceptions.e020_map_selection import prepare
    with pytest.raises(ValueError,match='label-free'):
        prepare(None,None,pd.DataFrame(columns=[*select.FEATURES,'Category']),None,0,None,None,None,None,None,None)


def test_map_preparation_matches_locked_helpers_for_technical_fallback(monkeypatch):
    import pandas as pd
    from map_misconceptions.e020_map_selection import prepare
    def frame(start,questions):
        return pd.DataFrame([{'QuestionId':q,'QuestionText':'synthetic question','MC_Answer':'synthetic answer',
            'StudentExplanation':'synthetic explanation','Category':'True_Correct' if i%2 else 'False_Correct','Misconception':'NA'}
            for q in range(start,start+questions) for i in range(4)])
    train,cal,ev=frame(0,9),frame(9,3),frame(12,3)
    monkeypatch.setattr(select.core,'fit_model',lambda part,*args:part.copy())
    monkeypatch.setattr(select.core,'predict',lambda fitted,features,*args:select.core.e001.frequency_probabilities(fitted,features))
    tr=np.tile([0.,0.,1.],(len(train),1)); cs={k:np.tile([0.,0.,1.],(len(cal),1)) for k in ('G15','G7')}
    es={k:np.tile([0.,0.,1.],(len(ev),1)) for k in ('G15','G7')}
    flags={k:np.ones(len(cal),dtype=bool) for k in ('G15','G7')}; counts=[]
    args=(train,cal,ev[select.FEATURES],np.arange(len(ev)),0,tr,cs,es)
    original=select.prepare_parts(*args,lambda:None)
    actual=prepare(*args,flags,flags,lambda:counts.append(1))
    assert len(counts)==10 and original[0]==actual[0] and original[3]==actual[3]
    for arm in m.ARMS:
        for scale in ('raw','final'):
            for key in original[2][arm][scale]: np.testing.assert_array_equal(original[2][arm][scale][key],actual[2][arm][scale][key])
        np.testing.assert_array_equal(original[2][arm]['order'],actual[2][arm]['order'])
