"""Serialize preregistered descriptive uncertainty summaries from E005 aggregates."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
from scipy.stats import spearmanr

SEED=20260831; BOOTSTRAPS=100000; PERMUTATIONS=100000
def interval(values):
 rng=np.random.default_rng(SEED);v=np.asarray(values,float);draws=np.array([v[rng.integers(0,len(v),len(v))].mean() for _ in range(BOOTSTRAPS)])
 return {'mean':float(v.mean()),'fold_values':[float(x) for x in v],'descriptive_bootstrap_95_interval':[float(np.quantile(draws,.025)),float(np.quantile(draws,.975))],'bootstrap_replicates':BOOTSTRAPS,'note':'Descriptive resampling over five folds only; not formal inferential evidence.'}
def association(folds,model):
 q=[x for f in folds for x in f['per_question']];x=np.array([z['well_supported_row_share'] for z in q]);y=np.array([z[model]['map_at_3'] for z in q]);rho=float(spearmanr(x,y).statistic);rng=np.random.default_rng(SEED);null=np.array([spearmanr(x,rng.permutation(y)).statistic for _ in range(PERMUTATIONS)]);p=float((1+(np.abs(null)>=abs(rho)).sum())/(PERMUTATIONS+1));return {'n_questions':len(q),'spearman_rho':rho,'permutation_two_sided_p':p,'permutations':PERMUTATIONS,'note':'Descriptive permutation result across 15 questions; low power and not formal inferential evidence.'}
def main():
 a=argparse.ArgumentParser();a.add_argument('--input',type=Path,required=True);a.add_argument('--output',type=Path,required=True);z=a.parse_args();d=json.loads(z.input.read_text());out=[]
 for v in d['results']:
  item={'variant':v['variant'],'comparisons':{},'per_question_association':{}}
  for scope in ('grouped_folds','random_folds'):
   fs=v[scope];item['comparisons'][scope]={}
   for metric in ('map_at_3','ece_10_equal_width','multiclass_brier'):
    item['comparisons'][scope][metric]=interval([f['tfidf_logreg'][metric]-f['frequency_baseline'][metric] for f in fs])
  for model in ('frequency_baseline','tfidf_logreg'):item['per_question_association'][model]=association(v['grouped_folds'],model)
  out.append(item)
 d['preregistered_descriptive_summaries']={'seed':SEED,'results':out};z.output.write_text(json.dumps(d,indent=2));print('Wrote completed E005 aggregate-only artifact')
if __name__=='__main__':main()
