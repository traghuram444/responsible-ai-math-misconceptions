"""E023 numerical panels, computed only after the global freeze."""
import itertools
import numpy as np
from . import e023_selection as s, e022_metrics as old
from .e009_metrics import correctness_auc,head_summary,HEAD_METRICS
from .e010_metrics import review_group,EXTRA_METRICS,primary_decision
from .e011_context import stat

STRATA=s.tt.STRATA
AUTO_METRICS=old.NUMERIC
REVIEW_METRICS=(*AUTO_METRICS,*EXTRA_METRICS)
REVIEW_PAIRS=('remaining_errors_per_100','error_capture_fraction','review_error_precision','risk')
AUTO_PAIRS=('risk','top1_accuracy','map_at_3','ece','brier')
CONTROLS=('R5','confidence','raw_confidence','support_aware','hash_only','frequency')


def evaluate(fold,memory,truth):
    review=[]; automation=[]; ranking=[]; classes=memory['classes']; questions=memory['questions']
    strata=s.tt.support_masks(truth,memory['train_labels'],memory['train_questions'])
    for arm,rule in s.REVIEW:
        p=memory[arm+'_final']; score=memory[f'score_{arm}_{rule}']; correct=classes[p.argmax(axis=1)]==truth
        for question in [None,*sorted(set(questions.tolist()))]:
            scope=np.ones(len(truth),bool) if question is None else questions==question
            for name,mask in strata.items():
                member=mask&scope; base={'arm':arm,'rule':rule,'fold':fold,'question':question,'stratum':name}
                ranking.append({**base,'group':correctness_auc(score[member],correct[member])})
                for family,values in [('review',s.BUDGETS),('automation',s.TARGETS if (arm,rule) in s.AUTO else ())]:
                    for value in values:
                        keep=memory[f'{"review" if family=="review" else "auto"}_{arm}_{rule}_{value}']
                        if keep.dtype!=bool or keep.flags.writeable: raise ValueError('Frozen mask required.')
                        target=None if family=='review' else value
                        g=review_group(truth,p,classes,member,keep&scope) if target is None else s.tt.summarize_group(truth,p,classes,member,keep&scope,target)
                        g['confidence_minus_accuracy']=g['mean_confidence']-g['top1_accuracy'] if g['retained_n'] else None
                        h=head_summary(score[member&keep],correct[member&keep]) if rule in ('R5','R8') else None
                        row={**base,'review_percent' if family=='review' else 'target_percent':value,'group':g,'reliability':h}
                        (review if family=='review' else automation).append(row)
    return review,automation,ranking


def summarize_heads(records,value_key):
    result=[]
    for arm,rule,value,stratum in sorted({(r['arm'],r['rule'],r[value_key],r['stratum']) for r in records if r['reliability'] is not None}):
        rows=sorted((r for r in records if r['question'] is None and (r['arm'],r['rule'],r[value_key],r['stratum'])==(arm,rule,value,stratum)),key=lambda r:r['fold'])
        if [r['fold'] for r in rows]!=list(range(5)): raise ValueError('Head fold grid.')
        result.append({'arm':arm,'rule':rule,value_key:value,'stratum':stratum,'metrics':{k:stat([r['reliability'][k] for r in rows]) for k in HEAD_METRICS}})
    return result


def paired(records,value_key,values,controls,names):
    index={(r['arm'],r['rule'],r[value_key],r['fold'],r['stratum']):r['group'] for r in records if r['question'] is None}
    result=[]
    for arm,control,value,fold,stratum in itertools.product(s.ARMS,controls,values,range(5),STRATA):
        a=index[arm,'R8',value,fold,stratum]; b=index['F' if control=='frequency' else arm,control,value,fold,stratum]
        result.append({'arm':arm,'control':control,value_key:value,'fold':fold,'stratum':stratum,
            'left_original_n':a['original_n'],'right_original_n':b['original_n'],'left_retained_n':a['retained_n'],'right_retained_n':b['retained_n'],
            'left_coverage':a['coverage'],'right_coverage':b['coverage'],
            'left_original_error_n':a.get('original_error_n'),'right_original_error_n':b.get('original_error_n'),
            'metrics':{k:a[k]-b[k] if a[k] is not None and b[k] is not None else None for k in names}})
    return {'records':result,'aggregate':old.summarize(result,('arm','control',value_key,'stratum'),names,'metrics')}


def automation_decisions(records,policies):
    index={(r['arm'],r['rule'],r['target_percent'],r['fold'],r['question']):r['group'] for r in records if r['stratum']=='all' and r['question'] is not None}
    pi={(r['arm'],r['rule'],r['policy']['target_percent'],r['fold']):r['policy'] for r in policies}
    decisions=[]; gaps=[]
    for (arm,rule),target in itertools.product(s.AUTO,s.TARGETS):
        admissible=[]; qs=[]
        for fold in range(5):
            p=pi[arm,rule,target,fold]; selected=p['status']=='SELECTED'; admissible.append(selected)
            devrisk=float(np.mean([x['risk'] for x in p['development']])) if selected else None
            for key in sorted((k for k in index if k[:4]==(arm,rule,target,fold)),key=lambda k:k[4]):
                g=index[key]; q=key[4]
                qs.append({'fold':fold,'question':q,'original_n':g['original_n'],'retained_n':g['retained_n'],'risk':g['risk'],
                    'count_pass':g['count_floor_met'],'coverage_pass':g['coverage_floor_met'],'risk_pass':g['risk_target_met'],
                    'joint_pass':bool(g['count_floor_met'] and g['coverage_floor_met'] and g['risk_target_met'] is True)})
                gaps.append({'arm':arm,'rule':rule,'target_percent':target,'fold':fold,'question':q,'development_risk':devrisk,
                    'evaluation_risk':g['risk'],'risk_minus_development':g['risk']-devrisk if g['risk'] is not None and devrisk is not None else None})
        risks=[q['risk'] for q in qs if q['risk'] is not None]
        decisions.append({'arm':arm,'rule':rule,'target_percent':target,'primary':rule=='R8' and target==20,
            'fold_admissible':admissible,'admissible_folds':sum(admissible),'questions':qs,'question_count':len(qs),
            'nonempty_questions':len(risks),'count_pass_questions':sum(q['count_pass'] for q in qs),'coverage_pass_questions':sum(q['coverage_pass'] for q in qs),
            'risk_pass_questions':sum(q['risk_pass'] is True for q in qs),'risk_exceeded_questions':sum(q['risk_pass'] is False for q in qs),'risk_denominator':len(risks),
            'joint_pass_questions':sum(q['joint_pass'] for q in qs),'maximum_question_risk':max(risks,default=None),
            'criterion_met':bool(all(admissible) and len(qs)==15 and all(q['joint_pass'] for q in qs))})
    return decisions,gaps


def panels(review,automation,ranking,policies):
    rp=paired(review,'review_percent',s.BUDGETS[1:],CONTROLS,REVIEW_PAIRS)
    ap=paired(automation,'target_percent',s.TARGETS,tuple(c for c in CONTROLS if c!='hash_only'),AUTO_PAIRS)
    primary=[]
    for arm in s.ARMS:
        rows=sorted((r for r in rp['records'] if r['arm']==arm and r['control']=='R5' and r['review_percent']==20 and r['stratum']=='all'),key=lambda r:r['fold'])
        primary.append({'arm':arm,'review_percent':20,'control':'R5',**primary_decision([-r['metrics']['remaining_errors_per_100'] for r in rows])})
    decisions,gaps=automation_decisions(automation,policies)
    ri={(r['arm'],r['rule'],r['fold'],r['stratum']):r['group'] for r in ranking if r['question'] is None}
    ranking_pairs=[]
    for arm,control,fold,stratum in itertools.product(s.ARMS,CONTROLS[:-1],range(5),STRATA):
        a=ri[arm,'R8',fold,stratum]['auroc']; b=ri[arm,control,fold,stratum]['auroc']
        ranking_pairs.append({'arm':arm,'control':control,'fold':fold,'stratum':stratum,'metrics':{'auroc':a-b if a is not None and b is not None else None}})
    return {'review':{'records':review,'aggregate':old.summarize(review,('arm','rule','review_percent','stratum'),REVIEW_METRICS,'group'),
            'reliability':summarize_heads(review,'review_percent'),'comparisons':rp,'decisions':primary},
        'automation':{'records':automation,'aggregate':old.summarize(automation,('arm','rule','target_percent','stratum'),AUTO_METRICS,'group'),
            'reliability':summarize_heads(automation,'target_percent'),'comparisons':ap,'decisions':decisions,'gaps':gaps},
        'ranking':{'records':ranking,'aggregate':old.summarize(ranking,('arm','rule','stratum'),('n','correct_n','incorrect_n','auroc'),'group'),
            'comparisons':{'records':ranking_pairs,'aggregate':old.summarize(ranking_pairs,('arm','control','stratum'),('auroc',),'metrics')}}}
