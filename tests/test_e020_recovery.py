"""Invented-data regression for the actual missing historical Category view."""
import copy
import json
from pathlib import Path
import numpy as np
import pytest
from test_e020_map import experiment, module_script
from map_misconceptions import e016
from map_misconceptions.e020_map_run import freeze_predictions
from map_misconceptions.e020_recovery import restore_category,load_frozen


def test_missing_category_regression_and_exact_reconstruction(experiment):
    _,prepared,_,_,truths=experiment
    memory=prepared[0][1]
    before={k:v.copy() for k,v in memory.items()}
    with pytest.raises(KeyError,match='category_raw'):
        e016.category_records('E011',0,memory,truths[0])
    repaired=restore_category(memory)
    reference={**memory,'category_raw':e016.marginalize(memory['raw'],memory['classes'])}
    assert e016.category_records('E011',0,repaired,truths[0])==e016.category_records('E011',0,reference,truths[0])
    assert 'category_raw' not in memory and not repaired['category_raw'].flags.writeable
    for name,value in before.items():
        assert np.array_equal(memory[name],value)
        assert repaired[name] is memory[name]
    with pytest.raises(ValueError,match='documented missing field'): restore_category(repaired)


def test_complete_frozen_reload_and_tamper_rejection(experiment,tmp_path):
    p,prepared,plans,ids,_=experiment
    freeze_predictions(tmp_path,prepared,plans,p['development'],p['ensemble_development'],ids,50)
    frozen=json.loads((tmp_path/'frozen_development_private.json').read_text())
    restored,rplans,rids=load_frozen(tmp_path,frozen)
    for fold in range(5):
        assert restored[fold][0]==prepared[fold][0]
        assert np.array_equal(rids[fold],ids[fold])
        for name,value in prepared[fold][1].items(): assert np.array_equal(value,restored[fold][1][name])
        for arm,plan in plans[fold].items():
            assert np.array_equal(rplans[fold][arm]['order'],plan['order'])
            for scale in ('raw','final'):
                for name,value in plan[scale].items():
                    assert np.array_equal(rplans[fold][arm][scale][name],value)
                    assert not rplans[fold][arm][scale][name].flags.writeable
    bad=copy.deepcopy(frozen); bad['prediction_sha256'].pop('fold_4_frozen_private.npz')
    with pytest.raises(ValueError,match='Incomplete'): load_frozen(tmp_path,bad)
    bad=copy.deepcopy(frozen); bad['prediction_sha256']['fold_0_frozen_private.npz']='0'*64
    with pytest.raises(ValueError,match='changed'): load_frozen(tmp_path,bad)


def test_recovery_contains_no_training_or_calibration_calls():
    import ast
    root=Path(__file__).resolve().parents[1]
    tree=ast.parse((root/'src/map_misconceptions/e020_recovery.py').read_text())
    forbidden={'fit','fit_model','select','prepare','calibrate','temperature_scale','generate','raw_arms'}
    calls={n.func.attr if isinstance(n.func,ast.Attribute) else n.func.id for n in ast.walk(tree)
           if isinstance(n,ast.Call) and isinstance(n.func,(ast.Attribute,ast.Name))}
    assert not calls & forbidden
    text=(root/'scripts/run_e020_recovery.py').read_text()
    assert 'out.mkdir(exist_ok=False)' in text and '--read-only' in text and '--network' in text


def test_recovery_receipt_rejects_private_and_extra_compute():
    pub=module_script('publish_e020_recovery.py')
    p={'experiment_id':'E020','status':'COMPLETED','phase':'reporting_recovery','results_sha256':'a'*64,
       'original_git_revision':'b'*40,'recovery_git_revision':'c'*40,'recovery_lock_sha256':'d'*64,
       'original_map_lock_sha256':'e'*64,'failed_attempt_inventory_sha256':'f'*64,'failed_attempt_files':300,
       'frozen_development_sha256':'a'*64,'source_failure_types':['KeyError','CalledProcessError'],
       'failed_attempt_preserved':True,'category_view_reconstructed':True,'new_model_calls':0,'new_classifier_fits':0,
       'original_statistical_seconds':300.,'recovery_seconds':10.,'finished_utc':'2026-10-27T10:00:00.000+00:00'}
    assert pub.validate_receipt(p) is p
    for extra in ({'private_text':'reject'},{'new_model_calls':1},{'new_classifier_fits':50},
                  {'source_failure_types':[]},{'recovery_seconds':-1.}):
        with pytest.raises(ValueError): pub.validate_receipt(p|extra)
