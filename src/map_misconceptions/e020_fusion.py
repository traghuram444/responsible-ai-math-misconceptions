"""Pure E020 fixed fusion, inner-selection and preregistered decision rules."""
import numpy as np
from .e016 import valid_probabilities
from .e019_metrics import prefixes

LAMBDAS=(0.,.25,.5,.75,1.)
WEIGHTS=tuple((i/4,j/4,k/4) for k in range(5) for j in range(5-k) for i in [4-j-k])
ARMS=('F','L','F_M','B','G15','G7','L7','H','G7_hard')
PAIRS=(('H','F'),('H','B'),('H','G7'),('H','L'),('G7','F'),('G7','F_M'),('G7','G15'),('L7','G7'),('G7','G7_hard'),('B','F'),('L','F'))


def soft_project(prob,classes,scores):
    prob=np.asarray(prob,dtype=np.float64); scores=np.asarray(scores,dtype=np.float64)
    valid_probabilities(prob,len(classes)); valid_probabilities(scores,3)
    if len(prob)!=len(scores): raise ValueError('Row alignment.')
    if list(classes)!=sorted(set(classes)): raise ValueError('Sorted training inventory required.')
    binary=prefixes(classes); parts=[]
    for b in (False,True):
        mask=binary==b
        if not mask.any(): parts.append(prob.copy()); continue
        mass=prob[:,mask].sum(axis=1)
        if np.any(mass<=0) or not np.isfinite(mass).all(): raise ValueError('Nonpositive compatible mass.')
        parts.append(prob*mask/mass[:,None])
    result=scores[:,2,None]*prob+scores[:,0,None]*parts[0]+scores[:,1,None]*parts[1]
    unknown=np.all(scores==[0,0,1],axis=1); result[unknown]=prob[unknown]
    return valid_probabilities(result,len(classes))


def mix(frequency,learned,grounded,weights):
    if tuple(weights) not in WEIGHTS: raise ValueError('Unregistered weights.')
    for w,p in zip(weights,(frequency,learned,grounded)):
        if w==1: return p.copy()
    if weights[2]==0: return (1-weights[1])*frequency+weights[1]*learned
    return weights[0]*frequency+weights[1]*learned+weights[2]*grounded


def choose(candidate_fold_scores):
    a=np.asarray(candidate_fold_scores,dtype=np.float64)
    if a.ndim!=2 or a.shape[1]!=3 or not np.isfinite(a).all(): raise ValueError('Three inner folds required.')
    return int(np.argmax(a.mean(axis=1)))


def meaningful(differences):
    d=np.asarray(differences,dtype=np.float64)
    if d.shape!=(5,) or not np.isfinite(d).all(): raise ValueError('Five finite fold contrasts required.')
    return bool(d.mean()>=.020 and np.sum(d>0)>=4)
