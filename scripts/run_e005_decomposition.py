"""Approved E005 aggregate-only transferability decomposition."""
from __future__ import annotations
import argparse, json, hashlib
from datetime import datetime
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.model_selection import GroupKFold, StratifiedKFold, StratifiedShuffleSplit
from map_misconceptions.data_contract import combined_label,file_sha256,load_training_data
from map_misconceptions.e001 import SEED,fit_tfidf_lr,predict,score_params,temperature_scale,apply_temperature,frequency_probabilities
from map_misconceptions.metrics import classification_summary

def status(p,start,stage,done=0,total=20,latest=None):
 p.write_text(json.dumps({'experiment_id':'E005','status':'RUNNING','elapsed':str(datetime.now()-start).split('.')[0],'progress':{'completed':done,'total':total,'percent':round(100*done/total)},'stage':stage,'latest_metrics':latest or {},'updated_at':datetime.now().strftime('%I:%M:%S %p')}))
def category_probs(prob,classes):
 cats=np.array([x.split(':',1)[0] for x in classes]); unique=np.unique(cats); out=np.column_stack([prob[:,cats==c].sum(1) for c in unique]);return out,unique
def summary(y,p,c): return classification_summary(y,p,c)
def strata(y,train_y,train_groups):
 counts=train_y.value_counts(); qcounts=pd.DataFrame({'y':train_y,'q':train_groups.astype(str)}).drop_duplicates().groupby('y').size();n=pd.Series(y).map(counts).fillna(0).astype(int);q=pd.Series(y).map(qcounts).fillna(0).astype(int)
 return {'unsupported':n.eq(0).to_numpy(),'rare':n.between(1,19).to_numpy(),'frequent':n.ge(20).to_numpy(),'well_supported':(n.ge(20)&q.ge(2)).to_numpy()}
def eligible(y,p,c):
 pred=c[p.argmax(1)];correct=pred==y
 if len(y)<200 or correct.sum()<20 or (~correct).sum()<20:return {'n':int(len(y)),'calibration':'not_estimable'}
 m=summary(y,p,c);return {'n':int(len(y)),'ece_10_equal_width':m['ece_10_equal_width'],'multiclass_brier':m['multiclass_brier']}
def fold_eval(frame,tr,ca,ev,variant,grouped):
 y=combined_label(frame); train=frame.iloc[tr];cal=frame.iloc[ca];evalf=frame.iloc[ev]
 splitter=GroupKFold(n_splits=3) if grouped else StratifiedKFold(n_splits=3,shuffle=True,random_state=SEED)
 selected=score_params(train,variant,splitter,groups=train.QuestionId.astype(str) if grouped else None,split_labels=None if grouped else train.Category.astype(str))
 m=fit_tfidf_lr(train,variant,{**selected['params'],'ngram_range':tuple(selected['params']['ngram_range'])});cp,cl=predict(m,cal,variant);t,_=temperature_scale(y.iloc[ca].to_numpy(),cp,cl);p=apply_temperature(predict(m,evalf,variant)[0],t);fp,fc=frequency_probabilities(train,evalf);truth=y.iloc[ev].to_numpy(); masks=strata(truth,y.iloc[tr],train.QuestionId)
 out={'n_evaluation':len(ev),'frequency_baseline':summary(truth,fp,fc),'tfidf_logreg':summary(truth,p,cl),'category':{'frequency_baseline':summary(pd.Series(truth).str.split(':').str[0].to_numpy(),*category_probs(fp,fc)),'tfidf_logreg':summary(pd.Series(truth).str.split(':').str[0].to_numpy(),*category_probs(p,cl))},'strata':{}}
 for name,mask in masks.items():
  out['strata'][name]={'n':int(mask.sum()),'frequency_baseline':summary(truth[mask],fp[mask],fc) if mask.any() else None,'tfidf_logreg':summary(truth[mask],p[mask],cl) if mask.any() else None,'calibration':{'frequency_baseline':eligible(truth[mask],fp[mask],fc) if mask.any() else {'n':0,'calibration':'not_estimable'},'tfidf_logreg':eligible(truth[mask],p[mask],cl) if mask.any() else {'n':0,'calibration':'not_estimable'}}}
 out['per_question']=[]
 for q in sorted(evalf.QuestionId.astype(str).unique()):
  mask=evalf.QuestionId.astype(str).to_numpy()==q
  out['per_question'].append({'QuestionId':q,'n':int(mask.sum()),'supported_row_share':float((masks['frequent'][mask]).mean()),'well_supported_row_share':float((masks['well_supported'][mask]).mean()),'frequency_baseline':summary(truth[mask],fp[mask],fc),'tfidf_logreg':summary(truth[mask],p[mask],cl)})
 return out
def main():
 a=argparse.ArgumentParser();a.add_argument('--input',type=Path,required=True);a.add_argument('--splits',type=Path,required=True);a.add_argument('--output',type=Path,required=True);a.add_argument('--status-file',type=Path,default=Path('artifacts/live_status.json'));z=a.parse_args();start=datetime.now();z.status_file.parent.mkdir(parents=True,exist_ok=True);status(z.status_file,start,'Loading frozen data')
 f=load_training_data(z.input);ass=pd.read_csv(z.splits/'grouped_fold_assignments.csv',keep_default_na=False);man=json.loads((z.splits/'manifest.json').read_text());
 if man['input_sha256']!=file_sha256(z.input):raise ValueError('input differs from frozen manifest')
 results=[];done=0
 for variant in ('explanation_only','question_plus_explanation'):
  grouped=[]
  for fold in range(5):
   role=ass[f'fold_{fold}'].to_numpy();grouped.append({'fold':fold,**fold_eval(f,np.where(role=='train')[0],np.where(role=='calibration')[0],np.where(role=='evaluation')[0],variant,True)});done+=1;status(z.status_file,start,f'Grouped fold {fold+1}/5: {variant}',done,20,{'MAP@3':f"{grouped[-1]['tfidf_logreg']['map_at_3']:.3f}",'Baseline':f"{grouped[-1]['frequency_baseline']['map_at_3']:.3f}"})
  outer=StratifiedKFold(n_splits=5,shuffle=True,random_state=SEED);random=[];strat=f.Category.astype(str)
  for fold,(pooli,evi) in enumerate(outer.split(f,strat)):
   pool=f.iloc[pooli];ss=StratifiedShuffleSplit(n_splits=1,test_size=.2,random_state=SEED+fold);tri,cai=next(ss.split(pool,pool.Category.astype(str)));random.append({'fold':fold,**fold_eval(f,pooli[tri],pooli[cai],evi,variant,False)});done+=1;status(z.status_file,start,f'Random-reference fold {fold+1}/5: {variant}',done,20)
  results.append({'variant':variant,'grouped_folds':grouped,'random_folds':random})
 z.output.write_text(json.dumps({'experiment_id':'E005','input_sha256':file_sha256(z.input),'split_manifest_sha256':hashlib.sha256((z.splits/'manifest.json').read_bytes()).hexdigest(),'results':results},indent=2));status(z.status_file,start,'Aggregate report written',20,20);print('Wrote aggregate-only E005 results')
if __name__=='__main__':main()
