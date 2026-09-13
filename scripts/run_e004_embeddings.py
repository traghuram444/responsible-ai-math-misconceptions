"""Locked E004 frozen semantic-embedding baseline with live aggregate status."""
from __future__ import annotations
import json, time
from datetime import datetime
from pathlib import Path
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import normalize
from map_misconceptions.data_contract import combined_label, file_sha256, load_training_data
from map_misconceptions.e001 import temperature_scale, apply_temperature, frequency_probabilities
from map_misconceptions.metrics import classification_summary, risk_coverage

SEED=20260831; MODEL="sentence-transformers/all-MiniLM-L6-v2"; GRID=(0.5,1.0,2.0)
def text(f,v):
 e=f.StudentExplanation.astype(str)
 return e if v=="explanation_only" else "[QUESTION] "+f.QuestionText.astype(str)+" [EXPLANATION] "+e
def live(p, started, status, stage, completed=0,total=5,latest=None):
 p.write_text(json.dumps({"experiment_id":"E004","status":status,"elapsed":str(datetime.now()-started).split('.')[0],"progress":{"completed":completed,"total":total,"percent":round(100*completed/total)},"stage":stage,"latest_metrics":latest or {},"updated_at":datetime.now().strftime("%I:%M:%S %p")},indent=2))
def fit(x,y,c):
 m=LogisticRegression(C=c,max_iter=2000,random_state=SEED,n_jobs=1);m.fit(x,y);return m
def main():
 import argparse
 a=argparse.ArgumentParser();a.add_argument('--input',type=Path,required=True);a.add_argument('--splits',type=Path,required=True);a.add_argument('--output',type=Path,required=True);a.add_argument('--status-file',type=Path,default=Path('artifacts/live_status.json'));z=a.parse_args()
 started=datetime.now();z.status_file.parent.mkdir(parents=True,exist_ok=True);live(z.status_file,started,'RUNNING','Loading frozen encoder')
 f=load_training_data(z.input); ass=pd.read_csv(z.splits/'grouped_fold_assignments.csv',keep_default_na=False); manifest=json.loads((z.splits/'manifest.json').read_text());
 if manifest['input_sha256']!=file_sha256(z.input): raise ValueError('input hash differs from frozen manifest')
 enc=SentenceTransformer(MODEL,revision='1110a243fdf4706b3f48f1d95db1a4f5529b4d41',device='cpu')
 results=[]
 for variant in ('explanation_only','question_plus_explanation'):
  live(z.status_file,started,'RUNNING',f'Encoding {variant}')
  X=normalize(enc.encode(text(f,variant).tolist(),batch_size=64,show_progress_bar=False,convert_to_numpy=True))
  folds=[]
  for fold in range(5):
   role=ass[f'fold_{fold}'].to_numpy();tr=np.where(role=='train')[0];ca=np.where(role=='calibration')[0];ev=np.where(role=='evaluation')[0]; y=combined_label(f); groups=f.iloc[tr].QuestionId.astype(str)
   inner=GroupKFold(n_splits=3); scores=[]
   for c in GRID:
    vals=[]
    for ii,jj in inner.split(X[tr],y.iloc[tr],groups):
     m=fit(X[tr][ii],y.iloc[tr].to_numpy()[ii],c); vals.append(classification_summary(y.iloc[tr].to_numpy()[jj],m.predict_proba(X[tr][jj]),m.classes_)['map_at_3'])
    scores.append((float(np.mean(vals)),c))
   _,c=max(scores);m=fit(X[tr],y.iloc[tr],c);cp=m.predict_proba(X[ca]);temp,n=temperature_scale(y.iloc[ca].to_numpy(),cp,m.classes_);prob=apply_temperature(m.predict_proba(X[ev]),temp); truth=y.iloc[ev].to_numpy(); fp,fc=frequency_probabilities(f.iloc[tr],f.iloc[ev]);
   folds.append({'fold':fold,'selected_C':c,'temperature':temp,'frequency_baseline':classification_summary(truth,fp,fc),'embedding_logreg':classification_summary(truth,prob,m.classes_),'risk_coverage':risk_coverage(truth,prob,m.classes_)})
   latest=folds[-1];live(z.status_file,started,'RUNNING',f'Cross-validation fold {fold+1}/5',fold+1,5,{'MAP@3':f"{latest['embedding_logreg']['map_at_3']:.3f}",'Baseline':f"{latest['frequency_baseline']['map_at_3']:.3f}",'Δ':f"{latest['embedding_logreg']['map_at_3']-latest['frequency_baseline']['map_at_3']:+.3f}"})
  def agg(key):
   return {k:{'mean':float(np.mean([q[key][k] for q in folds])),'std':float(np.std([q[key][k] for q in folds],ddof=1))} for k in folds[0][key] if k!='n'}
  results.append({'variant':variant,'folds':folds,'aggregate':{'frequency_baseline':agg('frequency_baseline'),'embedding_logreg':agg('embedding_logreg')}})
 out={'experiment_id':'E004','model':MODEL,'model_revision':'1110a243fdf4706b3f48f1d95db1a4f5529b4d41','input_sha256':file_sha256(z.input),'results':results};z.output.write_text(json.dumps(out,indent=2));live(z.status_file,started,'COMPLETED','Aggregate report written',5,5);print('Wrote aggregate-only E004 results')
if __name__=='__main__': main()
