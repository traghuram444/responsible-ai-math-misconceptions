import json
import numpy as np
import pytest
from map_misconceptions import e019_checker as c
from map_misconceptions import e019_metrics as m


def test_normalization_and_exact_json():
    assert c.normalize('  e\u0301\r\nx  y\r ') == 'é\nx  y'
    assert c.normalize(None)=='' and c.normalize('NA')=='NA'
    assert c.messages('x','é')[1]['content']=='{"question":"x","proposed_answer":"é"}'
    assert not c.SYSTEM.endswith('\n')


@pytest.mark.parametrize('text,expected',[
    ('reason\nFINAL: CORRECT','true'),(' FINAL: INCORRECT \r\n','false'),
    ('FINAL: UNKNOWN','unknown_model'),('FINAL: CORRECT\ntrailing','unknown_invalid_output'),
    ('FINAL: CORRECT\nFINAL: CORRECT','unknown_invalid_output'),
    ('final: CORRECT','unknown_invalid_output'),('FINAL: true','unknown_invalid_output'),
    ('{"FINAL":"CORRECT"}','unknown_invalid_output'),('', 'unknown_invalid_output'),
    ('FINAL: CORRECT <|im_end|>','unknown_invalid_output'),
    ('<|im_start|>\nFINAL: CORRECT','unknown_invalid_output')])
def test_parser(text,expected):
    assert c.parse_output(text,['<|im_end|>','<|im_start|>'])==expected


def test_input_precedence_and_boundaries():
    assert c.input_reason('', '<|im_end|>', ['<|im_end|>'],4000)=='unknown_missing_input'
    assert c.input_reason('q','<|im_end|>',['<|im_end|>'],4000)=='unknown_special_token_input'
    assert c.input_reason('q','a',[],3072) is None
    assert c.input_reason('q','a',[],3073)=='unknown_input_too_long'


def test_eos_precedence_and_decode_options():
    class Tokenizer:
        all_special_tokens=['<|im_end|>']
        def decode(self,tokens,**kwargs):
            assert tokens==[10]
            assert kwargs=={'skip_special_tokens':False,'clean_up_tokenization_spaces':False}
            return 'FINAL: CORRECT'
    assert c.parse_tokens([10],Tokenizer())==('unknown_generation_limit',None)
    assert c.parse_tokens([10,151645],Tokenizer())==('true','FINAL: CORRECT')


def test_catalogue_is_canonical_and_label_free(tmp_path):
    path=tmp_path/'catalogue.json'
    path.write_text(json.dumps([{'question':'q','proposed_answer':'a'}]))
    assert c.load_catalogue(path)==[('q','a')]
    for value in ([{'question':'q','proposed_answer':'a','Category':'True_Correct'}],
                  [{'question':' q','proposed_answer':'a'}],
                  [{'question':'q','proposed_answer':'a'}]*2):
        path.write_text(json.dumps(value))
        with pytest.raises(ValueError): c.load_catalogue(path)
    with pytest.raises(FileExistsError): c.write_new(path,{})


@pytest.fixture
def fixture():
    classes=np.array(['False_Correct:NA','False_Misconception:x','True_Correct:NA','True_Neither:NA'])
    return np.array([[.4,.1,.3,.2],[.25,.25,.25,.25]]),classes


def test_unknown_identity_and_readonly(fixture):
    p,classes=fixture; out=m.filter_output(p,classes,[-1,-1])
    np.testing.assert_array_equal(out['prob'],p)
    np.testing.assert_array_equal(out['top'],np.argsort(-p,axis=1)[:,:3])
    np.testing.assert_array_equal(out['predicted'],np.argmax(p,axis=1))
    assert not out['prob'].flags.writeable


def test_stable_subsequence_no_backfill_and_argmax(fixture):
    p,classes=fixture; out=m.filter_output(p,classes,[1,0])
    assert out['top'][0].tolist()==[2,3,-1]
    assert out['predicted'].tolist()==[2,0]
    np.testing.assert_array_equal(out['top'][1,:2],np.argsort(-p[1])[np.isin(np.argsort(-p[1]),[0,1])])
    np.testing.assert_allclose(out['prob'][0],[0,0,.6,.4])


def test_missing_candidates_and_zero_mass():
    p=np.array([[1.,0.]])
    classes=np.array(['False_Correct:NA','True_Correct:NA'])
    with pytest.raises(ValueError): m.filter_output(p,classes,[1])
    out=m.filter_output(np.ones((1,1)),classes[:1],[1])
    assert out['state'].tolist()==['fallback_no_candidate']
    assert out['top'].tolist()==[[0,-1,-1]]


def test_truth_cannot_repair_wrong_filter(fixture):
    p,classes=fixture
    truth=np.array([classes[0],'True_Misconception:unsupported'])
    base=m.row_scores(truth,m.filter_output(p,classes,[-1,-1]),classes)
    wrong=m.row_scores(truth,m.filter_output(p,classes,[1,1]),classes)
    assert base['map_at_3'][0]==1 and wrong['map_at_3'][0]==0
    assert wrong['map_at_3'][1]==wrong['top1_accuracy'][1]==0


def test_correct_signal_monotonicity(fixture):
    p,classes=fixture
    for truth_label in classes:
        truth=np.array([truth_label]*2)
        signal=int(truth_label.startswith('True'))
        base=m.row_scores(truth,m.filter_output(p,classes,[-1,-1]),classes)
        filtered=m.row_scores(truth,m.filter_output(p,classes,[signal]*2),classes)
        for k in m.METRICS: assert np.all(filtered[k]>=base[k])


def test_majority_uses_binary_count_and_tie_false():
    assert m.majority(['False_Correct:NA','True_Correct:NA'])[0]==0
    assert m.majority(['False_Correct:NA','True_Correct:NA','True_Neither:NA'])[0]==1


def test_calibration_eligibility_union_and_registered_top1(fixture):
    p,classes=fixture
    prob=np.tile(p[0],(200,1)); out=m.filter_output(prob,classes,[-1]*200)
    truth=np.array([classes[0]]*100+['True_Misconception:unsupported']*100)
    result=m.calibration(truth,out,classes,np.ones(200,dtype=bool))
    assert not result['ineligible_reasons']
    assert result['metrics']['accuracy']==.5
    assert result['metrics']['brier']==pytest.approx(.9)
    small=m.calibration(truth,out,classes,np.arange(200)<10)
    assert small['ineligible_reasons']==['n_below_200','correct_below_20','incorrect_below_20']
    assert small['metrics']['ece'] is None and small['metrics']['brier'] is None


def test_primary_conjunction_and_exact_boundaries():
    rows=[]
    for left,right in m.REVIEW_PAIRS:
        for f in range(5): rows.append({'left':left,'right':right,'fold':f,'question':None,'stratum':'all','metrics':{'map_at_3':.02}})
    assert m.decisions(rows)['H1_conjunction_met']
    rows[5]['metrics']['map_at_3']=0
    assert not m.decisions(rows)['H1_conjunction_met']
    assert m.decisions(rows)['H2_secondary_met']


def test_confusion_unknown_denominators():
    r=m.audit_record(0,None,np.array([0,0,1,1]),np.array([0,-1,0,1]))
    assert r['confusion_counts']==[[1,0,1],[1,1,0]]
    assert r['metrics']['covered_agreement']==pytest.approx(2/3)
    assert r['metrics']['all_row_agreement']==.5
    assert r['metrics']['covered_balanced_accuracy']==.75
    assert r['metrics']['all_row_balanced_accuracy']==.5
    assert m.audit_record(0,None,np.array([0,1]),np.array([-1,-1]))['metrics']['covered_balanced_accuracy'] is None


def test_routing_is_pretruth_and_constant_unknown_not_forced_review(fixture):
    p,classes=fixture
    memory={'classes':classes,'frequency_prob':p,'raw':p,'prob':p,'positions':np.array([7,9]),'train_labels':classes}
    plans,_=m.prepare_arms(memory,np.array([-1,-1]),0)
    for a,b in (('F','F_A'),('L','L_A')):
        np.testing.assert_array_equal(plans[a]['order'],plans[b]['order'])


def test_five_fold_synthetic_reporting_grid(fixture):
    p,classes=fixture; truth=classes[[0,2]]
    collected=[[],[],[],[],[]]
    for fold in range(5):
        memory={'classes':classes,'frequency_prob':p,'raw':p,'prob':p,'positions':np.array([fold*2,fold*2+1]),
                'train_labels':np.tile(classes,20),'train_questions':np.tile([1,2,1,2],20),'questions':np.array([fold+10,fold+10])}
        signals=np.array([-1,-1]); plans,_=m.prepare_arms(memory,signals,fold)
        for dest,values in zip(collected,m.score_fold(fold,memory,truth,plans,signals)): dest.extend(values)
    result=m.build_panels(*collected)
    assert not result['comparisons']['decisions']['H1_conjunction_met']
    assert len(result['review']['records'])==150
    for r in result['gain_loss']['records']:
        if r['n']: assert r['metrics']['gain']+r['metrics']['loss']==pytest.approx(r['metrics']['delta'])


def synthetic_payload():
    from map_misconceptions import e019_run as runner
    from pathlib import Path
    root=Path(__file__).resolve().parents[1]
    prepared={}; truths={}; signals={}; pair_ids={}; constant=[]; collected=[[],[],[],[],[]]
    classes=np.array(['False_Correct:NA','False_Neither:NA','True_Correct:NA','True_Neither:NA'])
    for fold in range(5):
        questions=np.repeat(np.arange(fold*3,fold*3+3),[2447 if q<6 else 2446 for q in range(fold*3,fold*3+3)])
        n=len(questions); p=np.tile([.4,.1,.3,.2],(n,1))
        memory={'classes':classes,'frequency_prob':p,'raw':p,'prob':p,'positions':np.arange(n)+fold*8000,
            'train_labels':np.tile(classes,20),'train_questions':np.tile([1,2,1,2],20),'questions':questions}
        prepared[fold]=({},memory,None)
        truth=np.tile(classes,int(np.ceil(n/4)))[:n]; truths[fold]=truth
        sig=np.where(np.arange(n)%3==0,-1,np.arange(n)%2); signals[fold]=sig
        pair_ids[fold]=np.where(sig==-1,2,sig)
        plans,d=m.prepare_arms(memory,sig,fold); constant.append(d)
        for dest,rows in zip(collected,m.score_fold(fold,memory,truth,plans,sig)): dest.extend(rows)
    reference=json.loads((root/'results/E011_aggregates.json').read_text())
    return {'experiment_id':'E019','status':'COMPLETED',
        'development':[d for d in reference['development'] if d['arm']=='full_context'],
        'constant_development':constant,**m.build_panels(*collected),
        'correctness_audit':runner.correctness_audit(prepared,truths,signals,pair_ids,['false','true','unknown_model'],constant),
        'resource_summary':{'pairs':3,'reason_counts':{r:int(r in ('false','true','unknown_model')) for r in c.REASONS},
            'input_tokens':runner.distribution([177,177,177]),'generated_tokens':runner.distribution([20,20,20]),
            'checker_seconds':1.,'statistical_seconds':1.,'solver_image_id':'sha256:'+'0'*64,'statistical_image_id':'sha256:'+'0'*64,
            'model_manifest_sha256':'0'*64,'environment_lock_sha256':'0'*64,'cpu_count':1,'architecture':'x86_64','solver_memory_limit_bytes':17179869184},
        'integrity':{'git_revision':'0'*40,'lock_sha256':'0'*64,'cache_sha256':'0'*64,'frozen_development_sha256':'0'*64,
            'preserved_files':513,'preservation_verified':True,'global_freeze_verified':True,'e018_remains_blocked':True,
            'fit_warnings':0,'model_fits':50,'reproduction_model_folds':10,'row_level_outputs':False,'uid':10001,'gid':10001}}


@pytest.fixture(scope='module')
def publication_payload(): return synthetic_payload()


def test_complete_synthetic_publication(publication_payload):
    from map_misconceptions import e019_publication as publication
    assert publication.validate(publication_payload) is publication_payload
    report=publication.render(publication_payload)
    assert 'Fold-level results' in report and 'Row Reason Counts' in report


@pytest.mark.parametrize('kind',range(8))
def test_publication_rejects_corruption(publication_payload,kind):
    from copy import deepcopy
    from map_misconceptions import e019_publication as publication
    bad=deepcopy(publication_payload)
    if kind==0: bad['student_response']='not allowed'
    if kind==1: bad['original_input_controls']['records'].pop()
    if kind==2: bad['comparisons']['decisions']['H1_conjunction_met']=not bad['comparisons']['decisions']['H1_conjunction_met']
    if kind==3: bad['calibration']['records'][0]['ineligible_reasons']=['n_below_200']
    if kind==4: bad['fallback']['records'][0]['n']+=1
    if kind==5: bad['correctness_audit']['records'][0]['confusion_counts'][0][0]+=1
    if kind==6: bad['review']['records'][0]['metrics']['coverage']=.9
    if kind==7: bad['gain_loss']['records'][0]['metrics']['loss']=1.
    with pytest.raises(ValueError): publication.validate(bad)


def test_no_evaluation_scoring_before_freeze():
    import inspect
    from map_misconceptions import e019_run as runner
    source=inspect.getsource(runner.run)
    assert source.index('freeze_predictions(')<source.index('truths={')<source.index('reproduce(')<source.index('m.score_fold(')
    for required in ('check_reproduction','original_records','category_records','risk_coverage','real_prediction'):
        assert required in inspect.getsource(runner.reproduce)


def test_approved_protocol_and_environment():
    from pathlib import Path
    from map_misconceptions.e019_integrity import canonical,PROTOCOL_SHA
    root=Path(__file__).resolve().parents[1]
    assert canonical(root/'docs/E019_PROTOCOL.md')==PROTOCOL_SHA
    lock=json.loads((root/'experiments/e019_environment_lock.json').read_text())
    for k,v in c.OVERRIDES.items(): assert lock['pins']['generation_config'][k]==v
    assert 'torch==2.5.1+cpu' in (root/'repro/e019/requirements.lock').read_text()


def test_monitor_failure_does_not_interrupt_computation(tmp_path,monkeypatch):
    from map_misconceptions import resilient_status as rs
    def denied(*args): raise PermissionError(13,'synthetic failure')
    monkeypatch.setattr(rs.os,'replace',denied)
    with rs.ResilientStatus(tmp_path/'live.json',experiment_id='E019',total=1) as live:
        live.update('Synthetic checker phase',completed=1)
    assert live.diagnostics()['status']=='COMPLETED' and live.diagnostics()['io_failures']>0
