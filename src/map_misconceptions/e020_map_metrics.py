"""E020 registered aggregate scoring, used only after global prediction freeze."""
import numpy as np
from . import e019_metrics as old,e020_fusion as fusion

ARMS=fusion.ARMS
PAIRS=fusion.PAIRS
GAIN_PAIRS=(('H','F'),('H','B'),('H','G7'),('G7','F'),('G7','G7_hard'))
REVIEW_PAIRS=(('H','F'),('H','B'),('H','G7'),('G7','F'))
BUDGETS=old.BUDGETS
STRATA=old.core.STRATA


def score_fold(fold,memory,truth,plans):
    classes=memory['classes']; domains=old.prior.scopes(memory,truth)
    scores={a:old.row_scores(truth,plans[a]['final'],classes) for a in ARMS}
    unsupported=~np.isin(truth,classes)
    for a in ARMS:
        if any(np.any(x[unsupported]!=0) for x in scores[a].values()): raise ValueError('Unsupported truth scored.')
    exact=[]; cal=[]; gains=[]; review=[]; ranks=[]
    for q,s,mask in domains:
        n=int(mask.sum()); scope={'fold':fold,'question':q,'stratum':s,'n':n}
        for a in ARMS:
            exact.append({'arm':a,**scope,'metrics':{k:float(v[mask].mean()) if n else None for k,v in scores[a].items()}})
            for scale in ('raw','final'):
                cal.append({'arm':a,**scope,'scale':scale,**old.calibration(truth,plans[a][scale],classes,mask)})
            if a not in ('F','F_M','G7_hard'):
                raw,final=plans[a]['raw'],plans[a]['final']
                top1=int(np.sum((raw['predicted']!=final['predicted'])&mask))
                top3=int(np.sum(np.any(raw['top']!=final['top'],axis=1)&mask))
                ranks.append({'arm':a,**scope,'top1_changed_n':top1,'top3_changed_n':top3,
                    'metrics':{'top1_changed_share':top1/n if n else None,'top3_changed_share':top3/n if n else None}})
        for left,right in GAIN_PAIRS:
            d=scores[left]['map_at_3'][mask]-scores[right]['map_at_3'][mask]
            gains.append({'left':left,'right':right,**scope,'wins':int((d>0).sum()),'ties':int((d==0).sum()),'losses':int((d<0).sum()),
                'metrics':{'gain':float(np.maximum(d,0).mean()) if n else None,
                           'loss':float(np.minimum(d,0).mean()) if n else None,'delta':float(d.mean()) if n else None}})
    for a in ARMS:
        for budget in BUDGETS:
            keep=np.zeros(len(truth),dtype=bool); keep[plans[a]['order'][:len(truth)-len(truth)*budget//100]]=True
            row=old.calibration(truth,plans[a]['final'],classes,keep); acc=row['metrics'].pop('accuracy')
            review.append({'arm':a,'fold':fold,'question':None,'stratum':'all','review_percent':budget,**row,
                'metrics':{**row['metrics'],'top1_accuracy':acc,'risk':1-acc,
                    'map_at_3':float(scores[a]['map_at_3'][keep].mean()),'coverage':int(keep.sum())/len(truth)}})
    return exact,cal,gains,review,ranks


def decisions(paired):
    contrasts=[]
    for a,b in (('H','F'),('H','G7'),('H','B'),('G7','G15'),('G7','F'),('G7','F_M')):
        values=[next(r['metrics']['map_at_3'] for r in paired if r['left']==a and r['right']==b and
                     r['fold']==f and r['question'] is None and r['stratum']=='all') for f in range(5)]
        contrasts.append({'left':a,'right':b,**old.core.meaningful(values)})
    flags=[r['criterion_met'] for r in contrasts]
    return {'comparisons':contrasts,'H1_primary':flags[0],'H2_secondary':flags[1] and flags[2],
            'H3_secondary':flags[3],'H4_secondary':flags[4] and flags[5]}


def build_panels(exact,cal,gains,review,ranks):
    paired=old.contrasts(exact,PAIRS)
    small=[{k:v for k,v in r.items() if k not in ('correct_n','incorrect_n','ineligible_reasons','metrics')} |
           {'metrics':{k:r['metrics'][k] for k in ('ece','brier')}} for r in cal]
    cp=old.contrasts(small,PAIRS,('scale',)); changes=[]
    lookup={(r['arm'],r['fold'],r['question'],r['stratum'],r['scale']):r for r in small}
    for r in small:
        if r['scale']!='final': continue
        raw=lookup[r['arm'],r['fold'],r['question'],r['stratum'],'raw']
        changes.append({k:v for k,v in r.items() if k not in ('scale','metrics')} | {'metrics':{
            k:r['metrics'][k]-raw['metrics'][k] if r['metrics'][k] is not None and raw['metrics'][k] is not None else None for k in ('ece','brier')}})
    rp=old.contrasts(review,REVIEW_PAIRS,('review_percent',))
    for rows in (cp,changes,rp):
        for r in rows: r['jointly_eligible_n']=r['n'] if r['metrics']['ece'] is not None else 0
    def panel(rows,dims): return {'records':rows,'aggregate':old.summarize(rows,dims)}
    return {'exact':panel(exact,('arm','stratum')),
        'comparisons':{**panel(paired,('left','right','stratum')),'decisions':decisions(paired)},
        'calibration':{**panel(cal,('arm','scale','stratum')),'contrasts':cp,
            'contrast_aggregate':old.summarize(cp,('left','right','scale','stratum')),
            'final_minus_raw':changes,'change_aggregate':old.summarize(changes,('arm','stratum'))},
        'gain_loss':panel(gains,('left','right','stratum')),
        'review':{**panel(review,('arm','review_percent','stratum')),'contrasts':rp,
            'contrast_aggregate':old.summarize(rp,('left','right','review_percent','stratum'))},
        'rank_changes':panel(ranks,('arm','stratum'))}


def correctness(prepared,truths,pair_indices,caches,development):
    records=[]; majority=[]; pairs=[]; reasons=[]; missing=[]
    for fold in range(5):
        memory=prepared[fold][1]; binary=old.prefixes(truths[fold]); ids=pair_indices[fold]
        for q in [None,*sorted(set(memory['questions'].tolist()))]:
            mask=np.ones(len(binary),dtype=bool) if q is None else memory['questions']==q
            majority.append(old.audit_record(fold,q,binary[mask],np.full(int(mask.sum()),int(development[fold]['majority_correctness']))))
            for key in ('G15','G7'):
                cache=caches[key]; decision=np.array([r['decision'] for r in cache]); signal=np.where(decision==2,-1,decision)
                records.append({'model':key,**old.audit_record(fold,q,binary[mask],signal[ids[mask]])})
                distinct=np.unique(ids[mask]); counts=[int(np.sum(decision[distinct]==i)) for i in range(3)]
                pairs.append({'model':key,'fold':fold,'question':q,'distinct_pairs':len(distinct),
                    'predicted_false':counts[0],'predicted_true':counts[1],'unknown':counts[2]})
                from .e020_checker import REASONS
                reasons.append({'model':key,'fold':fold,'question':q,'n':int(mask.sum()),
                    'reason_counts':{r:sum(cache[i]['reason']==r for i in ids[mask]) for r in REASONS}})
                prefixes=old.prefixes(memory['classes'])
                scores=np.array([cache[i]['scores'] for i in ids[mask]])
                absent=[not np.any(prefixes==b) for b in (False,True)]
                missing.append({'model':key,'fold':fold,'question':q,'n':int(mask.sum()),
                    'missing_false_inventory':absent[0],'missing_true_inventory':absent[1],
                    'false_projection_fallback_n':int(np.sum(scores[:,0]>0)) if absent[0] else 0,
                    'true_projection_fallback_n':int(np.sum(scores[:,1]>0)) if absent[1] else 0})
    pooled=[]
    for key in ('G15','G7'):
        cm=np.sum([r['confusion_counts'] for r in records if r['model']==key and r['question'] is None],axis=0)
        pooled.append({'model':key,'confusion_counts':cm.tolist(),
            'confusion_row_normalized':[[float(v/row.sum()) if row.sum() else None for v in row] for row in cm]})
    return {'records':records,'aggregate':old.summarize(records,('model','stratum')),
        'majority_records':majority,'majority_aggregate':old.summarize(majority,('stratum',)),
        'pair_counts':pairs,'row_reason_counts':reasons,'projection_fallback':missing,'pooled_confusion':pooled}


def distribution(values):
    x=[v for v in values if v is not None]
    return {'n':len(x),'total':float(sum(x)),'min':float(min(x)) if x else None,
            'median':float(np.median(x)) if x else None,'mean':float(np.mean(x)) if x else None,'max':float(max(x)) if x else None}
