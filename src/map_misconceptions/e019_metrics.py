"""Registered E019 filtering and aggregate scoring, separate from the checker."""
from __future__ import annotations
import numpy as np
from . import e016 as historical
from . import e017 as reporting
from . import e013 as prior
from .e011_publication import same
from .metrics import expected_calibration_error
from .metrics_v2 import union_label_brier_score
from .selective import _routing_order

core = historical.core
ARMS = ('F','L','F_M','F_A','L_A')
PAIRS = (('F_A','F'),('F_A','F_M'),('L_A','F_A'),('L_A','L'),('L','F'),('L_A','F'),('F_M','F'))
GAIN_PAIRS = (('F_A','F'),('F_A','F_M'),('L_A','L'),('L_A','F_A'))
REVIEW_PAIRS = PAIRS[:3]
STATES = ('filtered','fallback_unknown','fallback_no_candidate')
METRICS = ('map_at_3','top1_accuracy')
BUDGETS = (0,10,20,30,40,50)


def prefixes(classes):
    result = np.asarray([str(y).split('_',1)[0] for y in classes])
    if not set(result).issubset({'False','True'}): raise ValueError('Invalid correctness prefix.')
    return result == 'True'


def majority(train_labels):
    true_n = int(prefixes(train_labels).sum()); false_n = len(train_labels)-true_n
    return int(true_n > false_n), {'false':false_n, 'true':true_n}


def filter_output(prob, classes, signals):
    """No evaluation truth accepted. -1 is unknown; 0/1 are predicted false/true."""
    classes = np.asarray(classes); signals = np.asarray(signals)
    historical.valid_probabilities(prob,len(classes))
    if classes.tolist() != sorted(set(classes.tolist())): raise ValueError('Inventory changed.')
    if signals.shape != (len(prob),) or not set(signals).issubset({-1,0,1}):
        raise ValueError('Invalid supplied signal.')
    binary = prefixes(classes)
    q = prob.copy(); top = np.full((len(prob),3),-1,dtype=np.int64)
    predicted = np.empty(len(prob),dtype=np.int64); state = []
    orders = np.argsort(-prob,axis=1)
    for i, signal in enumerate(signals):
        mask = binary == signal
        status = 'fallback_unknown' if signal == -1 else 'fallback_no_candidate' if not mask.any() else 'filtered'
        state.append(status)
        if status == 'filtered':
            mass = prob[i,mask].sum()
            if not np.isfinite(mass) or mass <= 0: raise ValueError('Nonpositive compatible mass.')
            q[i] *= mask; q[i] /= mass
            indices = np.flatnonzero(mask)
            predicted[i] = indices[np.argmax(prob[i,indices])]
            ranking = orders[i,mask[orders[i]]]
        else:
            predicted[i] = np.argmax(prob[i]); ranking = orders[i]
        top[i,:min(3,len(ranking))] = ranking[:3]
    historical.valid_probabilities(q,len(classes))
    result = {'prob':q, 'top':top, 'predicted':predicted, 'state':np.asarray(state), 'confidence':q.max(axis=1)}
    for value in result.values(): value.setflags(write=False)
    return result


def prepare_arms(memory, signals, fold):
    constant, counts = majority(memory['train_labels'])
    plans = {}
    for arm in ARMS:
        signal = np.full(len(signals),-1) if arm in ('F','L') else np.full(len(signals),constant) if arm=='F_M' else signals
        scales = {}
        for scale in ('raw','final'):
            p = memory['frequency_prob'] if arm in ('F','F_A','F_M') else memory['raw' if scale=='raw' else 'prob']
            scales[scale] = filter_output(p,memory['classes'],signal)
        if arm == 'F_M' and not np.all(scales['final']['state']=='filtered'):
            raise ValueError('Majority signal has no training candidates.')
        order = _routing_order(scales['final']['confidence'],memory['positions'].tolist(),fold,core.SEED)
        order.setflags(write=False); plans[arm] = {**scales,'order':order}
    if not np.array_equal(plans['F_A']['final']['state'],plans['L_A']['final']['state']):
        raise ValueError('Matched-arm processing states differ.')
    return plans, {'fold':fold, 'majority_correctness':bool(constant), 'training_counts':counts}


def row_scores(truth, prediction, classes):
    rr = np.zeros(len(truth))
    for rank in range(3):
        idx = prediction['top'][:,rank]; valid = idx>=0
        rr[valid] += (truth[valid]==classes[idx[valid]])/(rank+1)
    return {'map_at_3':rr, 'top1_accuracy':(truth==classes[prediction['predicted']]).astype(float)}


def calibration(truth, prediction, classes, mask):
    n = int(mask.sum()); correct = truth==classes[prediction['predicted']]
    c = int(correct[mask].sum()); incorrect = n-c
    confidence = prediction['confidence']; reasons=[]
    if n<200: reasons.append('n_below_200')
    if c<20: reasons.append('correct_below_20')
    if incorrect<20: reasons.append('incorrect_below_20')
    accuracy = c/n if n else None
    conf = float(confidence[mask].mean()) if n else None
    return {'n':n, 'correct_n':c, 'incorrect_n':incorrect,
        'ineligible_reasons':reasons, 'metrics':{'accuracy':accuracy,'mean_confidence':conf,
        'confidence_minus_accuracy':conf-accuracy if n else None,
        'ece':expected_calibration_error(confidence[mask],correct[mask],10) if not reasons else None,
        'brier':union_label_brier_score(truth[mask],prediction['prob'][mask],classes) if not reasons else None}}


def summarize(rows, dimensions):
    return reporting.summarize(rows,dimensions)


def contrasts(rows,pairs,extra=(),paired_n=True):
    keys=('fold','question','stratum',*extra)
    index={(r['arm'],*(r[k] for k in keys)):r for r in rows}
    output=[]
    for left,right in pairs:
        for r in rows:
            if r['arm']!=left: continue
            other=index[right,*(r[k] for k in keys)]
            if paired_n and r['n']!=other['n']: raise ValueError('Paired n differs.')
            output.append({'left':left,'right':right,**{k:r[k] for k in keys},'n':r['n'],
                'metrics':{k:r['metrics'][k]-other['metrics'][k]
                    if r['metrics'][k] is not None and other['metrics'][k] is not None else None for k in r['metrics']}})
    return output


def decisions(exact_contrasts):
    flags=[]
    for left,right in REVIEW_PAIRS:
        values=[next(r['metrics']['map_at_3'] for r in exact_contrasts if r['left']==left and r['right']==right
                     and r['fold']==f and r['question'] is None and r['stratum']=='all') for f in range(5)]
        flags.append({'left':left,'right':right,**core.meaningful(values)})
    return {'comparisons':flags,'H1_conjunction_met':all(x['criterion_met'] for x in flags[:2]),
            'H2_secondary_met':flags[2]['criterion_met']}


def score_fold(fold,memory,truth,plans,signals):
    classes=memory['classes']; domains=prior.scopes(memory,truth)
    scores={arm:row_scores(truth,plans[arm]['final'],classes) for arm in ARMS}
    supported=np.isin(truth,classes); binary=prefixes(truth)
    for arm in ARMS:
        for metric in METRICS:
            if np.any(scores[arm][metric][~supported]!=0): raise ValueError('Unsupported truth scored.')
    for high,low in (('F_A','F'),('L_A','L')):
        agree=signals==binary
        for metric in METRICS:
            if np.any(scores[high][metric][agree]<scores[low][metric][agree]):
                raise ValueError('Correct-signal monotonicity failed.')
    exact=[]; cal=[]; gains=[]; fallback=[]; review=[]
    for q,s,mask in domains:
        n=int(mask.sum()); scope={'fold':fold,'question':q,'stratum':s,'n':n}
        for arm in ARMS:
            exact.append({'arm':arm,**scope,'metrics':{k:float(v[mask].mean()) if n else None for k,v in scores[arm].items()}})
            for scale in ('raw','final'):
                cal.append({'arm':arm,**scope,'scale':scale,**calibration(truth,plans[arm][scale],classes,mask)})
        for left,right in GAIN_PAIRS:
            d=scores[left]['map_at_3'][mask]-scores[right]['map_at_3'][mask]
            gains.append({'left':left,'right':right,**scope,
                'wins':int((d>0).sum()),'ties':int((d==0).sum()),'losses':int((d<0).sum()),
                'metrics':{'gain':float(np.maximum(d,0).mean()) if n else None,
                           'loss':float(np.minimum(d,0).mean()) if n else None,
                           'delta':float(d.mean()) if n else None}})
        if s=='all':
            for arm in ('F_A','L_A'):
                for state in STATES:
                    keep=mask & (plans[arm]['final']['state']==state); size=int(keep.sum())
                    fallback.append({'arm':arm,**scope,'n':size,'state':state,
                        'metrics':{k:float(v[keep].mean()) if size else None for k,v in scores[arm].items()}})
    for arm in ARMS:
        for budget in BUDGETS:
            keep=np.zeros(len(truth),dtype=bool)
            keep[plans[arm]['order'][:len(truth)-len(truth)*budget//100]]=True
            result=calibration(truth,plans[arm]['final'],classes,keep)
            acc=result['metrics'].pop('accuracy')
            review.append({'arm':arm,'fold':fold,'question':None,'stratum':'all','review_percent':budget,
                **result, 'metrics':{**result['metrics'],'top1_accuracy':acc,'risk':1-acc,
                    'map_at_3':float(scores[arm]['map_at_3'][keep].mean()),'coverage':int(keep.sum())/len(truth)}})
    return exact,cal,gains,fallback,review


def audit_record(fold,question,truth_binary,signals):
    n=len(signals); answered=signals!=-1
    matrix=np.zeros((2,3),dtype=int)
    for y,p in zip(truth_binary,signals): matrix[int(y),int(p) if p!=-1 else 2]+=1
    covered=matrix[:,:2].sum(axis=1); total=matrix.sum(axis=1); diag=np.diag(matrix[:,:2])
    return {'fold':fold,'question':question,'stratum':'all','n':n,
        'answered_n':int(answered.sum()),'unknown_n':int((~answered).sum()),
        'confusion_counts':matrix.tolist(),
        'confusion_row_normalized':[[float(v/row.sum()) if row.sum() else None for v in row] for row in matrix],
        'metrics':{'answered_share':float(answered.mean()) if n else None,
            'unknown_share':float((~answered).mean()) if n else None,
            'predicted_false_share':float((signals==0).mean()) if n else None,
            'predicted_true_share':float((signals==1).mean()) if n else None,
            'covered_agreement':float(diag.sum()/covered.sum()) if covered.sum() else None,
            'all_row_agreement':float(diag.sum()/n) if n else None,
            'covered_balanced_accuracy':float(np.mean(diag/covered)) if np.all(covered>0) else None,
            'all_row_balanced_accuracy':float(np.mean(diag/total)) if np.all(total>0) else None}}


def build_panels(exact,cal,gains,fallback,review):
    paired=contrasts(exact,PAIRS)
    cal_small=[{k:v for k,v in r.items() if k not in ('correct_n','incorrect_n','ineligible_reasons')} for r in cal]
    for r in cal_small: r['metrics']={k:r['metrics'][k] for k in ('ece','brier')}
    calpaired=contrasts(cal_small,PAIRS,('scale',))
    for r in calpaired: r['jointly_eligible_n']=r['n'] if r['metrics']['ece'] is not None else 0
    changes=[]
    lookup={(r['arm'],r['fold'],r['question'],r['stratum'],r['scale']):r for r in cal_small}
    for r in cal_small:
        if r['scale']!='final': continue
        raw=lookup[r['arm'],r['fold'],r['question'],r['stratum'],'raw']
        changes.append({k:v for k,v in r.items() if k not in ('scale','metrics')} | {'metrics':{
            k:r['metrics'][k]-raw['metrics'][k] if r['metrics'][k] is not None and raw['metrics'][k] is not None else None for k in ('ece','brier')}})
    for r in changes: r['jointly_eligible_n']=r['n'] if r['metrics']['ece'] is not None else 0
    rp=contrasts(review,REVIEW_PAIRS,('review_percent',))
    for r in rp: r['jointly_eligible_n']=r['n'] if r['metrics']['ece'] is not None else 0
    result={}
    for name,arms in (('original_input_controls',('F','L')),('constant_filter_control',('F_M',)),
                      ('automated_correctness_predictions',('F_A','L_A'))):
        records=[r for r in exact if r['arm'] in arms]
        result[name]={'records':records,'aggregate':summarize(records,('arm','stratum'))}
    result.update(comparisons={'records':paired,'aggregate':summarize(paired,('left','right','stratum')),'decisions':decisions(paired)},
        calibration={'records':cal,'aggregate':summarize(cal,('arm','scale','stratum')),
            'contrasts':calpaired,'contrast_aggregate':summarize(calpaired,('left','right','scale','stratum')),
            'final_minus_raw':changes,'change_aggregate':summarize(changes,('arm','stratum'))},
        gain_loss={'records':gains,'aggregate':summarize(gains,('left','right','stratum'))},
        fallback={'records':fallback,'aggregate':summarize(fallback,('arm','state','stratum'))},
        review={'records':review,'aggregate':summarize(review,('arm','review_percent','stratum')),
            'contrasts':rp,'contrast_aggregate':summarize(rp,('left','right','review_percent','stratum'))})
    return result
