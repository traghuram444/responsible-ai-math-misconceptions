"""E021 synthetic validation only; never read MAP examples or fit MAP models."""
import copy
import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from map_misconceptions import e021_selection as s,e021_metrics as m,e021_shuffle as sh,e021_publication as pub
from map_misconceptions.e019_checker import sha,write_new
from map_misconceptions.selective import _routing_order


def script(name):
    path=Path(__file__).resolve().parents[1]/'scripts'/name
    spec=importlib.util.spec_from_file_location(name,path); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module


@pytest.fixture(scope='module')
def experiment():
    prepared={}; plans={}; truths={}; shuffles={}; ensembles=[]; collected=[[],[],[],[],[]]; offset=0
    classes=np.array(['False_Correct:NA','True_Correct:NA'])
    for fold,n in enumerate([7339,7339,7339,7339,7340]):
        i=np.arange(n); q=np.empty(n,dtype=int)
        for j,part in enumerate(np.array_split(i,3)): q[part]=3*fold+j
        metadata=pd.DataFrame({'QuestionId':q,'QuestionText':['Synthetic question '+str(x) for x in q],
            'MC_Answer':(i%2).astype(str),'StudentExplanation':(i%3).astype(str)})
        signals=np.asarray([[.8,.1,.1] if x%2 else [.1,.7,.2] for x in i]); positions=np.arange(offset,offset+n); offset+=n
        f=np.tile([.6,.4],(n,1)); l=np.column_stack((.2+.3*(i%3),.8-.3*(i%3)))
        alpha=s.ALPHAS[fold]; raw=s.raw_arms(f,l,classes,signals,alpha)
        if alpha in (0.,.5,1.): raw['T']=raw[{0.:'G7',.5:'C50',1.:'L7'}[alpha]]
        plans[fold]={a:{'raw':raw[a],'final':raw[a],'order':_routing_order(raw[a]['confidence'],positions.tolist(),fold,s.core.SEED)} for a in s.ARMS}
        for plan in plans[fold].values(): plan['order'].setflags(write=False)
        memory={'raw':l,'prob':raw['L']['prob'],'category_raw':s.marginalize(l,classes),'classes':classes,'frequency_prob':f,'frequency_classes':classes,
            'positions':positions,'questions':q,'train_labels':np.array([classes[0]]*600+[classes[1]]*400),'train_questions':np.arange(1000)%9,
            'order':plans[fold]['L']['order'],'frequency_order':plans[fold]['F']['order']}
        for v in memory.values(): v.setflags(write=False)
        candidates=[{'params':{**r,'ngram_range':list(r['ngram_range'])},'inner_fold_map_at_3':[.5]*3,'inner_mean_map_at_3':.5} for r in s.core.e001.GRID]
        d={'arm':'full_context','model':'logistic','fold':fold,'n_train':1000,'n_calibration':300,'n_evaluation':n,'role_question_counts':[9,3,3],
            'selection':{'selected_index':0,'candidates':candidates},'temperature':1.,'calibration_supported_n':300,'fits':10}
        choice={'selected_index':fold,'selected_alpha':alpha,'candidates':[{'alpha':a,'inner_fold_map_at_3':[.6 if a==alpha else .5]*3,
            'inner_mean_map_at_3':.6 if a==alpha else .5} for a in s.ALPHAS]}
        ensembles.append({'fold':fold,'alpha_selection':choice,'calibration':{a:{'temperature':1.,'supported_n':300,
            'method':'unscaled' if a=='F' else 'component_reuse' if a=='T' and alpha in (0.,.5,1.) else 'own_temperature'} for a in s.ARMS},
            'projection_fallback':{'fold':fold,'missing_false_inventory':False,'missing_true_inventory':False,
                'false_projection_fallback_n':0,'true_projection_fallback_n':0}})
        prepared[fold]=(d,memory,None)
        truths[fold]=np.resize(classes,n).astype(object); truths[fold][::7]='False_Misconception:SYNTHETIC_UNSUPPORTED'
        shuffles[fold]=sh.prepare(metadata,positions,fold,signals)
        for dest,rows in zip(collected,m.score_fold(fold,memory,truths[fold],plans[fold])): dest.extend(rows)
    shuffled=[]; opportunities=[]; counter=[]
    for fold in range(5):
        rows,opp=sh.score_fold(fold,prepared[fold][1],truths[fold],plans[fold],shuffles[fold],lambda:counter.append(1))
        shuffled.extend(rows); opportunities.extend(opp)
    assert len(counter)==500
    p={'experiment_id':'E021','status':'COMPLETED','development':[prepared[f][0] for f in range(5)],'ensemble_development':ensembles,
        **m.build_panels(*collected),'explanation_shuffle':{'records':shuffled,'aggregate':sh.summarize(shuffled),'opportunity':opportunities},
        'resources':{'image_id':'sha256:'+'a'*64,'wall_seconds':1.},
        'integrity':{'git_revision':'a'*40,'lock_sha256':'b'*64,'protocol_sha256':'c'*64,'e020_results_sha256':'d'*64,
            'g7_cache_sha256':'e'*64,'frozen_development_sha256':'f'*64,'preserved_files':500,'preservation_verified':True,
            'global_freeze_verified':True,'e018_remains_blocked':True,'model_fits':50,'new_model_calls':0,'fit_warnings':0,
            'reproduction_model_folds':20,'shuffle_replicates_per_fold':100,'shuffle_seed':20261014,'seed':20260831,
            'row_level_outputs':False,'uid':10001,'gid':10001}}
    return p,prepared,plans,shuffles,truths


def test_complete_strict_report(experiment):
    p,*_=experiment
    assert pub.validate(p) is p
    assert len(p['exact']['records'])==1400
    assert len(p['comparisons']['records'])==2600
    assert len(p['explanation_shuffle']['records'])==600
    assert len(p['review']['records'])==210
    assert all(r['n']==0 for r in p['exact']['records'] if r['stratum']=='rare')
    text=pub.render(p)
    assert 'Fixed comparison: primary' in text and 'Tuned ensemble: secondary' in text
    assert 'SYNTHETIC_UNSUPPORTED' not in text


@pytest.mark.parametrize('change',[
    lambda p:p.update(private_response='reject'),
    lambda p:p['exact']['records'].pop(),
    lambda p:p['comparisons']['decisions'].update(H1_fixed_primary=not p['comparisons']['decisions']['H1_fixed_primary']),
    lambda p:p['calibration']['records'][0]['ineligible_reasons'].append('n_below_200'),
    lambda p:p['review']['records'][0]['metrics'].update(coverage=.1),
    lambda p:p['ensemble_development'][0]['alpha_selection'].update(selected_index=4),
    lambda p:p['explanation_shuffle']['records'][0]['shuffled']['map_at_3']['score']['values'].pop(),
    lambda p:p['explanation_shuffle']['opportunity'][0].update(label_mixed_rows=999999),
    lambda p:p['gain_loss']['records'][0].update(wins=999999),
    lambda p:p['rank_changes']['records'][0].update(top3_changed_n=999999),
])
def test_corrupt_or_private_report_rejected(experiment,change):
    p=copy.deepcopy(experiment[0]); change(p)
    with pytest.raises(ValueError): pub.validate(p)


def test_fixed_contrast_and_raw_endpoints():
    classes=np.array(['False_Correct:NA','True_Correct:NA']); f=np.array([[.6,.4]]); l=np.array([[.2,.8]])
    scores=np.array([[.8,.1,.1]])
    for alpha in s.ALPHAS:
        arms=s.raw_arms(f,l,classes,scores,alpha)
        np.testing.assert_allclose(arms['C50']['prob']-arms['U50']['prob'],.5*(arms['L7']['prob']-arms['L']['prob']),atol=1e-15)
        if alpha in (0.,.5,1.): np.testing.assert_array_equal(arms['T']['prob'],arms[{0.:'G7',.5:'C50',1.:'L7'}[alpha]]['prob'])


@pytest.mark.parametrize('alpha',s.ALPHAS)
def test_calibration_support_reuse_and_fallback(alpha,monkeypatch):
    classes=np.array(['False_Correct:NA','True_Correct:NA']); f=np.tile([.6,.4],(3,1)); l=np.tile([.2,.8],(3,1))
    signals=np.tile([0.,0.,1.],(3,1)); raw=s.raw_arms(f,l,classes,signals,alpha); calls=[]
    def temperature(truth,p,cols):
        calls.append(p); assert np.isin(truth,cols).sum()==2; return 1.,2
    monkeypatch.setattr(s.core.e001,'temperature_scale',temperature)
    truth=np.array([classes[0],classes[1],'False_Misconception:UNSUPPORTED'])
    final,records=s.calibrate(raw,raw,classes,truth,alpha,np.ones(3,dtype=bool),np.ones(3,dtype=bool))
    assert records['G7']['method']=='all_unknown_frequency' and final['G7'] is final['F']
    if alpha in (0.,.5,1.): assert final['T'] is final[{0.:'G7',.5:'C50',1.:'L7'}[alpha]]
    assert len(calls)==(4 if alpha in (0.,.5,1.) else 5)
    calls.clear()
    _,records=s.calibrate(raw,raw,classes,truth,alpha,np.zeros(3,dtype=bool),np.zeros(3,dtype=bool))
    assert records['G7']['method']=='own_temperature'


def test_inner_only_counts_and_selection_ties(monkeypatch):
    n=36
    frame=pd.DataFrame({'QuestionId':np.repeat(np.arange(9),4),'QuestionText':['synthetic']*n,'MC_Answer':['answer']*n,
        'StudentExplanation':['explanation']*n,'Category':['False_Correct','True_Correct']*(n//2),'Misconception':['NA']*n})
    calls=[]; frequency_sizes=[]
    def fit(train,*args):
        assert len(set(train.QuestionId))==6; calls.append(set(train.QuestionId)); return set(train.QuestionId)
    def predict(trainqs,ev,*args):
        assert not trainqs & set(ev.QuestionId)
        return np.tile([.5,.5],(len(ev),1)),np.array(['False_Correct:NA','True_Correct:NA'])
    original=s.core.e001.frequency_probabilities
    def frequency(train,ev): frequency_sizes.append(len(train)); return original(train,ev)
    monkeypatch.setattr(s.core,'fit_model',fit); monkeypatch.setattr(s.core,'predict',predict)
    monkeypatch.setattr(s.core.e001,'frequency_probabilities',frequency)
    completed=[]; selection,choice=s.select(frame,np.tile([0,0,1],(n,1)),lambda:completed.append(1))
    assert len(calls)==len(completed)==9 and frequency_sizes==[24]*9
    assert selection['selected_index']==0 and choice['selected_alpha']==0


def test_preparation_matches_historical_controls_and_seals_state(monkeypatch):
    from map_misconceptions import e020_map_selection as historical
    classes=np.array(['False_Correct:NA','True_Correct:NA'])
    n=60; frame=pd.DataFrame({'QuestionId':np.repeat(np.arange(15),4),'QuestionText':['synthetic']*n,'MC_Answer':['a']*n,
        'StudentExplanation':['synthetic explanation']*n,'Category':['False_Correct','True_Correct']*(n//2),'Misconception':['NA']*n})
    train,cal,ev=frame.iloc[:36],frame.iloc[36:48],frame.iloc[48:][s.FEATURES]
    grid=[{'params':{**r,'ngram_range':list(r['ngram_range'])},'inner_fold_map_at_3':[.5]*3,'inner_mean_map_at_3':.5} for r in s.core.e001.GRID]
    chosen={'selected_index':0,'candidates':grid}
    alpha={'selected_index':2,'selected_alpha':.5,'candidates':[{'alpha':a,'inner_fold_map_at_3':[.6 if a==.5 else .5]*3,
        'inner_mean_map_at_3':.6 if a==.5 else .5} for a in s.ALPHAS]}
    def selected(train_,signals,completed):
        assert len(train_)==36 and signals.shape==(36,3)
        for _ in range(9): completed()
        return chosen,alpha
    def fit(train_,*args): assert set(train_.QuestionId)==set(range(9)); return None
    def predict(fitted,features,*args):
        assert set(features)==set(s.FEATURES)
        return np.tile([.6,.4],(len(features),1)),classes
    monkeypatch.setattr(s,'select',selected); monkeypatch.setattr(s.core,'fit_model',fit); monkeypatch.setattr(s.core,'predict',predict)
    signals=np.tile([.2,.6,.2],(n,1)); flag=np.zeros(12,dtype=bool); completed=[]
    prepared,plans,ens=s.prepare(train,cal,ev,np.arange(48,60),0,signals[:36],signals[36:48],signals[48:],flag,flag,lambda:completed.append(1))
    assert len(completed)==10 and 'category_raw' in prepared[1]
    assert all(not v.flags.writeable for v in prepared[1].values())
    assert plans['T']['raw'] is plans['C50']['raw'] and plans['T']['final'] is plans['C50']['final']
    weights={a:{'selected_weights':[.5,.5,0.]} for a in ('B','H')}
    monkeypatch.setattr(historical.base,'select',lambda *args:(chosen,weights))
    d,mem,oldplans,oldens=historical.prepare(train,cal,ev,np.arange(48,60),0,signals[:36],
        {a:signals[36:48] for a in ('G15','G7')},{a:signals[48:] for a in ('G15','G7')},
        {a:flag for a in ('G15','G7')},{a:flag for a in ('G15','G7')},lambda:None)
    assert d==prepared[0]
    for arm in s.CONTROLS:
        assert ens['calibration'][arm]==oldens['calibration'][arm]
        for scale in m.SCALES:
            for key in plans[arm][scale]: np.testing.assert_array_equal(plans[arm][scale][key],oldplans[arm][scale][key])
        np.testing.assert_array_equal(plans[arm]['order'],oldplans[arm]['order'])
    with pytest.raises(ValueError,match='label-free'):
        s.prepare(train,cal,ev.assign(Category='invalid'),np.arange(48,60),0,signals[:36],signals[36:48],signals[48:],flag,flag,lambda:None)


def test_shuffle_exact_legacy_mapping_label_boundary_and_donor_identity():
    from map_misconceptions.e013 import mappings
    meta=pd.DataFrame({'QuestionId':[1]*5+[2],'QuestionText':['q1']*5+['q2'],
        'MC_Answer':['a','a','a','b','b','a'],'StudentExplanation':['x','x','z','','w','only']})
    pos=np.array([10,7,9,3,1,2]); signals=np.tile([.3,.5,.2],(6,1))
    got=sh.prepare(meta,pos,2,signals); expected=mappings(meta,pos,2)['explanation_shuffle']
    np.testing.assert_array_equal(got['donors'],expected['donors'])
    assert np.all(got['donors'][:,5]==5) and not got['donors'].flags.writeable
    with pytest.raises(ValueError,match='Label-free'): sh.prepare(meta.assign(Category='bad'),pos,2,signals)
    changed=signals.copy(); changed[0]=[.1,.8,.1]
    with pytest.raises(ValueError,match='Checker varies'): sh.prepare(meta,pos,2,changed)
    # A synthetic deterministic text predictor: donor-indexing is exactly the
    # prediction on the recipient question/answer with the donor explanation.
    def predictor(data): return np.array([.1+.1*len(x) for x in data.StudentExplanation])
    original=predictor(meta)
    for d in got['donors']:
        perturbed=meta.copy(); perturbed['StudentExplanation']=meta.StudentExplanation.to_numpy()[d]
        np.testing.assert_array_equal(predictor(perturbed),original[d])


def test_freeze_and_historical_reproduction(experiment,tmp_path,monkeypatch):
    from map_misconceptions import e021_run as run
    p,prepared,plans,shuffles,truths=experiment
    out=tmp_path/'new'; out.mkdir()
    with pytest.raises(ValueError,match='Incomplete'): run.freeze(out,prepared,plans,p['ensemble_development'],shuffles,49)
    digest=run.freeze(out,prepared,plans,p['ensemble_development'],shuffles,50)
    assert run.verify_freeze(out,digest)['model_fits']==50
    source=tmp_path/'artifacts/e020_attempt01/map'; source.mkdir(parents=True)
    hashes={}
    for f in range(5):
        arrays={'memory_'+k:v for k,v in prepared[f][1].items()}
        for a in s.CONTROLS:
            for scale in m.SCALES: arrays.update({f'{a}_{scale}_{k}':v for k,v in plans[f][a][scale].items()})
            arrays[a+'_order']=plans[f][a]['order']
        path=source/f'fold_{f}_frozen_private.npz'; np.savez_compressed(path,**arrays); hashes[path.name]=sha(path)
    write_new(source/'frozen_development_private.json',{'prediction_sha256':hashes})
    (tmp_path/'results').mkdir()
    ref={'development':p['development'],'ensemble_development':p['ensemble_development'],
        'exact':{'records':[{k:v for k,v in r.items() if k!='scale'} for r in p['exact']['records'] if r['scale']=='final']},
        'calibration':p['calibration'],'review':p['review']}
    write_new(tmp_path/'results/E020_aggregates.json',ref)
    called=[]; monkeypatch.setattr(run,'historical_reproduction',lambda *args:called.append(1))
    run.reproduce(prepared,plans,p['ensemble_development'],truths,p,tmp_path)
    assert called==[1]
    wrong=copy.deepcopy(p); wrong['exact']['records'][1]['metrics']['map_at_3']+=.01
    with pytest.raises(ValueError): run.reproduce(prepared,plans,p['ensemble_development'],truths,wrong,tmp_path)
    (out/'fold_0_frozen_private.npz').write_bytes(b'corrupt')
    with pytest.raises(ValueError,match='changed'): run.verify_freeze(out,digest)


def test_global_barrier_no_model_calls_and_monitor():
    root=Path(__file__).resolve().parents[1]
    text=(root/'src/map_misconceptions/e021_run.py').read_text()
    assert text.index('frozen_sha=freeze(out')<text.index('truths={f:combined_label')
    assert text.index('reproduce(prepared,plans,ensembles,truths,panels,ROOT)')<text.index("latest_metrics={'Fixed")
    assert "frame.iloc[ev][selection.FEATURES]" in text and 'AutoModel' not in text
    launch=script('run_e021.py')
    for stage,n,total,expected in [('Training: fits',12,50,12),('Scoring original: fold',53,5,3),('Exploratory permutations',67,500,12)]:
        state={'status':'RUNNING','stage':stage,'progress':{'completed':n,'total':555}}
        result=launch.view(state); assert result['progress']['completed']==expected and result['progress']['total']==total
        assert state['progress']['total']==555
    assert 'out.mkdir(exist_ok=False)' in (root/'scripts/run_e021.py').read_text()
