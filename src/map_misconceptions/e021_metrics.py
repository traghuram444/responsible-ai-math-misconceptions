"""E021 registered original-input panels; no training or selection."""
import numpy as np
from . import e019_metrics as old
from .e021_selection import ARMS
PAIRS=(('C50','U50'),('C50','F'),('C50','G7'),('C50','L7'),('T','C50'),('T','U50'),('T','F'),
       ('T','G7'),('T','L7'),('L7','G7'),('G7','F'),('L','F'),('L7','F'))
GAIN_PAIRS=(('C50','U50'),('T','L7'),('T','G7'),('C50','F'),('T','F'))
REVIEW_PAIRS=(('C50','U50'),('T','G7'),('T','L7'),('T','F'))
SCALES=('raw','final'); STRATA=old.core.STRATA; BUDGETS=old.BUDGETS


def score_fold(fold,memory,truth,plans):
    classes=memory['classes']; domains=old.prior.scopes(memory,truth)
    scores={(a,s):old.row_scores(truth,plans[a][s],classes) for a in ARMS for s in SCALES}
    unsupported=~np.isin(truth,classes)
    if any(np.any(v[unsupported]!=0) for row in scores.values() for v in row.values()): raise ValueError('Unsupported truth scored.')
    exact=[]; cal=[]; gains=[]; review=[]; ranks=[]
    for q,t,mask in domains:
        n=int(mask.sum()); scope={'fold':fold,'question':q,'stratum':t,'n':n}
        for a in ARMS:
            for s in SCALES:
                exact.append({'arm':a,**scope,'scale':s,'metrics':{k:float(v[mask].mean()) if n else None for k,v in scores[a,s].items()}})
                cal.append({'arm':a,**scope,'scale':s,**old.calibration(truth,plans[a][s],classes,mask)})
            raw,final=plans[a]['raw'],plans[a]['final']
            n1=int(np.sum((raw['predicted']!=final['predicted'])&mask)); n3=int(np.sum(np.any(raw['top']!=final['top'],axis=1)&mask))
            ranks.append({'arm':a,**scope,'top1_changed_n':n1,'top3_changed_n':n3,
                'metrics':{'top1_changed_share':n1/n if n else None,'top3_changed_share':n3/n if n else None}})
        for a,b in GAIN_PAIRS:
            d=scores[a,'final']['map_at_3'][mask]-scores[b,'final']['map_at_3'][mask]
            gains.append({'left':a,'right':b,**scope,'wins':int((d>0).sum()),'ties':int((d==0).sum()),'losses':int((d<0).sum()),
                'metrics':{'gain':float(np.maximum(d,0).mean()) if n else None,'loss':float(np.minimum(d,0).mean()) if n else None,'delta':float(d.mean()) if n else None}})
    for a in ARMS:
        for budget in BUDGETS:
            keep=np.zeros(len(truth),dtype=bool); keep[plans[a]['order'][:len(truth)-len(truth)*budget//100]]=True
            r=old.calibration(truth,plans[a]['final'],classes,keep); acc=r['metrics'].pop('accuracy')
            review.append({'arm':a,'fold':fold,'question':None,'stratum':'all','review_percent':budget,**r,
                'metrics':{**r['metrics'],'top1_accuracy':acc,'risk':1-acc,
                    'map_at_3':float(scores[a,'final']['map_at_3'][keep].mean()),'coverage':int(keep.sum())/len(truth)}})
    return exact,cal,gains,review,ranks


def decisions(paired):
    rows=[]
    for a,b,s in (('C50','U50','final'),('C50','U50','raw'),('T','G7','final'),('T','L7','final')):
        ds=[next(r['metrics']['map_at_3'] for r in paired if (r['left'],r['right'],r['scale'],r['fold'],r['question'],r['stratum'])==(a,b,s,f,None,'all')) for f in range(5)]
        rows.append({'left':a,'right':b,'scale':s,**old.core.meaningful(ds)})
    flags=[r['criterion_met'] for r in rows]
    return {'comparisons':rows,'H1_fixed_primary':flags[0],'raw_attribution_check':flags[1],
        'conditioning_attribution_supported':flags[0] and flags[1],'H2_tuned_secondary':flags[2] and flags[3]}


def build_panels(exact,cal,gains,review,ranks):
    paired=old.contrasts(exact,PAIRS,('scale',))
    small=[{k:v for k,v in r.items() if k not in ('correct_n','incorrect_n','ineligible_reasons','metrics')} |
        {'metrics':{k:r['metrics'][k] for k in ('ece','brier')}} for r in cal]
    cp=old.contrasts(small,PAIRS,('scale',)); changes=[]
    idx={(r['arm'],r['fold'],r['question'],r['stratum'],r['scale']):r for r in small}
    for r in small:
        if r['scale']!='final': continue
        raw=idx[r['arm'],r['fold'],r['question'],r['stratum'],'raw']
        changes.append({k:v for k,v in r.items() if k not in ('scale','metrics')} | {'metrics':{
            k:r['metrics'][k]-raw['metrics'][k] if r['metrics'][k] is not None and raw['metrics'][k] is not None else None for k in ('ece','brier')}})
    rp=old.contrasts(review,REVIEW_PAIRS,('review_percent',))
    for rows in (cp,changes,rp):
        for r in rows: r['jointly_eligible_n']=r['n'] if r['metrics']['ece'] is not None else 0
    heterogeneity=[]
    for a,b in PAIRS:
        ds=[r['metrics']['map_at_3'] for r in paired if r['left']==a and r['right']==b and r['scale']=='final' and r['question'] is not None and r['stratum']=='all']
        if len(ds)!=15: raise ValueError('Fifteen-question grid required.')
        heterogeneity.append({'left':a,'right':b,'questions':15,'positive':sum(v>0 for v in ds),'zero':sum(v==0 for v in ds),
            'negative':sum(v<0 for v in ds),'min_delta':min(ds),'max_delta':max(ds)})
    def panel(rows,dims): return {'records':rows,'aggregate':old.summarize(rows,dims)}
    return {'exact':panel(exact,('arm','scale','stratum')),
        'comparisons':{**panel(paired,('left','right','scale','stratum')),'decisions':decisions(paired),'question_heterogeneity':heterogeneity},
        'calibration':{**panel(cal,('arm','scale','stratum')),'contrasts':cp,'contrast_aggregate':old.summarize(cp,('left','right','scale','stratum')),
            'final_minus_raw':changes,'change_aggregate':old.summarize(changes,('arm','stratum'))},
        'gain_loss':panel(gains,('left','right','stratum')),'rank_changes':panel(ranks,('arm','stratum')),
        'review':{**panel(review,('arm','review_percent','stratum')),'contrasts':rp,'contrast_aggregate':old.summarize(rp,('left','right','review_percent','stratum'))}}
