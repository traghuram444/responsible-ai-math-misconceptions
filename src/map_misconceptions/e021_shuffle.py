"""Only the registered E013 explanation permutation; no pair-shuffle construction."""
import numpy as np
from . import e019_metrics as old
from .e013 import repetition
from .e011_publication import same
ARMS=('L','L7','G7'); SCALES=('raw','final'); REPLICATES=100


def prepare(metadata,positions,fold,signals):
    if set(metadata)!={'QuestionId','QuestionText','MC_Answer','StudentExplanation'}: raise ValueError('Label-free shuffle metadata required.')
    if fold not in range(5): raise ValueError('Invalid fold.')
    positions=np.asarray(positions)
    if len(positions)!=len(metadata) or len(np.unique(positions))!=len(positions): raise ValueError('Unique positions required.')
    q=metadata.QuestionId.to_numpy(); text=metadata.QuestionText.fillna('').astype(str).to_numpy()
    answer=metadata.MC_Answer.fillna('').astype(str).to_numpy()
    for question in set(q):
        if len(set(text[q==question]))!=1: raise ValueError('Question text varies inside QuestionId.')
    keys=[(int(q[i]),answer[i]) for i in range(len(q))]; cells=[]
    for key in sorted(set(keys)):
        idx=np.asarray([i for i,k in enumerate(keys) if k==key],dtype=int)
        idx=idx[np.argsort(positions[idx],kind='stable')]
        if not np.all(signals[idx]==signals[idx[0]]): raise ValueError('Checker varies in shuffle cell.')
        idx.setflags(write=False); cells.append(idx)
    donors=np.empty((100,len(q)),dtype=np.int64)
    for r in range(100):
        for j,idx in enumerate(cells):
            rng=np.random.Generator(np.random.PCG64(np.random.SeedSequence([20261014,1,fold,r,j])))
            donors[r,idx]=rng.permutation(idx)
    donors.setflags(write=False)
    inputs=old.core.input_text(metadata,'full_context').to_numpy(); opportunities=[]
    for question in [None,*sorted(set(q.tolist()))]:
        mask=np.ones(len(q),dtype=bool) if question is None else q==question
        local=[c for c in cells if mask[c[0]]]
        opportunities.append({'fold':fold,'question':question,'n':int(mask.sum()),'cells':len(local),
            'singleton_rows':sum(len(c) for c in local if len(c)==1),'movable_rows':sum(len(c) for c in local if len(c)>1),
            'donor_changed_n':repetition([int((positions[d][mask]!=positions[mask]).sum()) for d in donors]),
            'input_changed_n':repetition([int((inputs[d][mask]!=inputs[mask]).sum()) for d in donors])})
    return {'donors':donors,'cells':cells,'opportunities':opportunities}


def verify_invariance(plans,shuffle):
    for s in SCALES:
        for d in shuffle['donors']:
            for key in ('prob','top','predicted','confidence'):
                p=plans['G7'][s][key]
                if not np.array_equal(p,p[d]): raise ValueError('G7 shuffle invariance failed.')


def score_fold(fold,memory,truth,plans,shuffle,completed):
    verify_invariance(plans,shuffle)
    domains=old.prior.scopes(memory,truth); rows=[]
    for arm in ARMS:
        for scale in SCALES:
            scores=old.row_scores(truth,plans[arm][scale],memory['classes'])
            for q,t,mask in domains:
                n=int(mask.sum())
                rows.append({'arm':arm,'scale':scale,'fold':fold,'question':q,'stratum':t,'n':n,
                    'original':{k:float(v[mask].mean()) if n else None for k,v in scores.items()},
                    'shuffled':{k:[] for k in old.METRICS}})
    for replicate,d in enumerate(shuffle['donors']):
        idx=0
        for arm in ARMS:
            for scale in SCALES:
                source=plans[arm][scale]
                scores=old.row_scores(truth,{k:v[d] for k,v in source.items() if k in ('top','predicted')},memory['classes'])
                for _,_,mask in domains:
                    row=rows[idx]; idx+=1
                    for k,v in scores.items():
                        if row['n']:
                            value=float(v[mask].mean())
                            if arm=='G7': same(value,row['original'][k])
                            row['shuffled'][k].append(value)
        completed()
    for row in rows:
        row['shuffled']={k:{'score':repetition(values),'original_minus_shuffled':
            repetition([row['original'][k]-v for v in values])} for k,values in row['shuffled'].items()}
    opportunities=[]
    for row in shuffle['opportunities']:
        q=row['question']; cells=[c for c in shuffle['cells'] if q is None or memory['questions'][c[0]]==q]
        mixed=sum(len(c) for c in cells if len(set(truth[c]))>1)
        opportunities.append({**row,'label_mixed_rows':mixed,'label_mixed_share':mixed/row['n']})
    return rows,opportunities


def summarize(rows):
    result=[]
    for a in ARMS:
        for scale in SCALES:
            for t in old.core.STRATA:
                parts=sorted([r for r in rows if (r['arm'],r['scale'],r['stratum'],r['question'])==(a,scale,t,None)],key=lambda r:r['fold'])
                if [r['fold'] for r in parts]!=list(range(5)): raise ValueError('Shuffle fold grid.')
                item={'arm':a,'scale':scale,'stratum':t,'n_total':sum(r['n'] for r in parts),
                    'original':{k:old.core.stat([r['original'][k] for r in parts]) for k in old.METRICS},'shuffled':{}}
                for k in old.METRICS:
                    item['shuffled'][k]={}
                    for kind in ('score','original_minus_shuffled'):
                        reps=[r['shuffled'][k][kind] for r in parts]; values=[r['values'] for r in reps if r['values']]
                        item['shuffled'][k][kind]={'fold_stat':old.core.stat([r['mean'] for r in reps]),
                            'paired_replicates':repetition(np.asarray(values).mean(axis=0) if values else [])}
                result.append(item)
    return result
