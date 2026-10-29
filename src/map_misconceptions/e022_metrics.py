"""E022 registered reporting after global policy/prediction freeze."""
import itertools
import numpy as np
from . import threshold_transfer as tt
from .e011_context import stat
from .e022_selection import ARMS,TARGETS

STRATA=tt.STRATA
NUMERIC=(*tt.METRICS,'confidence_minus_accuracy')
PAIR_METRICS=('coverage','review_fraction','risk','top1_accuracy','map_at_3','mean_confidence','confidence_minus_accuracy','ece','brier')
PAIRS=(('L7','F'),('C50','F'),('C50','L7'))


def evaluate(fold,memory,truth):
    unfiltered=[]; retained=[]; classes=memory['classes']; q=memory['questions']
    masks=tt.support_masks(truth,memory['train_labels'],memory['train_questions'])
    for arm in ARMS:
        for scale,target in [('raw',None),('final',None),*[('final',t) for t in TARGETS]]:
            prob=memory[arm+'_'+scale]
            keep=np.ones(len(truth),dtype=bool) if target is None else memory[f'{arm}_keep_{target}']
            for question in [None,*sorted(set(q.tolist()))]:
                scope=np.ones(len(truth),dtype=bool) if question is None else q==question
                for name,mask in masks.items():
                    group=tt.summarize_group(truth,prob,classes,mask&scope,keep&scope,target)
                    group['confidence_minus_accuracy']=group['mean_confidence']-group['top1_accuracy'] if group['retained_n'] else None
                    row={'arm':arm,'fold':fold,'question':question,'stratum':name,'group':group}
                    if target is None: unfiltered.append({**row,'scale':scale})
                    else: retained.append({**row,'target_percent':target})
    return unfiltered,retained


def summarize(rows,dims,values,field):
    groups=sorted(set(tuple(r[k] for k in dims) for r in rows if r.get('question') is None))
    result=[]
    for group in groups:
        parts=sorted([r for r in rows if r.get('question') is None and tuple(r[k] for k in dims)==group],key=lambda r:r['fold'])
        if [r['fold'] for r in parts]!=list(range(5)): raise ValueError('Incomplete aggregate fold grid.')
        result.append({**dict(zip(dims,group)),'metrics':{k:stat([r[field][k] for r in parts]) for k in values}})
    return result


def panels(unfiltered,retained,policies):
    index={(r['arm'],r['target_percent'],r['fold'],r['question'],r['stratum']):r['group'] for r in retained}
    pindex={(r['arm'],r['policy']['target_percent'],r['fold']):r['policy'] for r in policies}
    comparisons=[]; gaps=[]; decisions=[]
    for a,b in PAIRS:
        for target,fold,stratum in itertools.product(TARGETS,range(5),STRATA):
            left=index[a,target,fold,None,stratum]; right=index[b,target,fold,None,stratum]
            comparisons.append({'left':a,'right':b,'target_percent':target,'fold':fold,'stratum':stratum,
                'left_original_n':left['original_n'],'right_original_n':right['original_n'],
                'left_retained_n':left['retained_n'],'right_retained_n':right['retained_n'],
                'left_coverage':left['coverage'],'right_coverage':right['coverage'],
                'metrics':{k:left[k]-right[k] if left[k] is not None and right[k] is not None else None for k in PAIR_METRICS}})
    for arm,target in itertools.product(ARMS,TARGETS):
        selected=[]; questions=[]
        for fold in range(5):
            policy=pindex[arm,target,fold]; selected.append(policy['status']=='SELECTED')
            devrisk=float(np.mean([r['risk'] for r in policy['development']])) if selected[-1] else None
            qs=sorted({r['question'] for r in retained if r['arm']==arm and r['target_percent']==target and r['fold']==fold and r['question'] is not None})
            for q in qs:
                g=index[arm,target,fold,q,'all']
                questions.append({'fold':fold,'question':q,'original_n':g['original_n'],'retained_n':g['retained_n'],
                    'risk':g['risk'],'count_pass':g['count_floor_met'],'coverage_pass':g['coverage_floor_met'],
                    'risk_pass':g['risk_target_met'],'joint_pass':bool(g['count_floor_met'] and g['coverage_floor_met'] and g['risk_target_met'] is True)})
                gaps.append({'arm':arm,'target_percent':target,'fold':fold,'question':q,'development_risk':devrisk,
                    'evaluation_risk':g['risk'],'risk_minus_development':g['risk']-devrisk if g['risk'] is not None and devrisk is not None else None})
        nonempty=sum(r['retained_n']>0 for r in questions)
        decisions.append({'arm':arm,'target_percent':target,'primary':arm!='F' and target==20,
            'fold_admissible':selected,'admissible_folds':sum(selected),'questions':questions,'question_count':len(questions),
            'nonempty_questions':nonempty,'count_pass_questions':sum(r['count_pass'] for r in questions),
            'coverage_pass_questions':sum(r['coverage_pass'] for r in questions),
            'risk_pass_questions':sum(r['risk_pass'] is True for r in questions),
            'risk_exceeded_questions':sum(r['risk_pass'] is False for r in questions),'risk_denominator':nonempty,
            'joint_pass_questions':sum(r['joint_pass'] for r in questions),
            'maximum_question_risk':max((r['risk'] for r in questions if r['risk'] is not None),default=None),
            'criterion_met':bool(all(selected) and len(questions)==15 and all(r['joint_pass'] for r in questions))})
    return {'unfiltered':{'records':unfiltered,'aggregate':summarize(unfiltered,('arm','scale','stratum'),NUMERIC,'group')},
        'retained':{'records':retained,'aggregate':summarize(retained,('arm','target_percent','stratum'),NUMERIC,'group')},
        'comparisons':{'records':comparisons,'aggregate':summarize(comparisons,('left','right','target_percent','stratum'),PAIR_METRICS,'metrics')},
        'gaps':gaps,'decisions':decisions}
