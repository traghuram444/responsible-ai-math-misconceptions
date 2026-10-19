"""Strict E017 aggregate publication, arithmetic checks and separate REAL/ORACLE tables."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from . import e017 as c
from . import e007_publication as s
from .e011_publication import same, STAT
from .e016_publication import DEVELOPMENT
from .e014_publication import check_selection
from .e013_publication import table
from .data_contract import file_sha256
from .e006 import write_new

E, L, NN, N, I = s.enum, s.listing, s.NN, s.N, s.I
REAL = E(*c.REAL)
ALL = E(*c.REAL, *c.ORACLES)
ORACLE = E('F', *c.ORACLES)
SUPPLIED = E(None, 'correctness', 'status', 'category')
SCOPE = {'fold': E(0,1,2,3,4), 'question': s.nullable(I), 'stratum': E(*c.core.STRATA), 'n': I}
EXACT = {k: NN for k in c.METRICS}
CMETRICS = {k: NN for k in ('accuracy', 'macro_f1')}
META = {'scale': E('raw','final'), 'component': E(*c.COMPONENTS)}
MATRIX = {'confusion_counts': L(L(I)), 'confusion_row_normalized': L(L(NN))}
R = {'arm': REAL, **SCOPE, 'metrics': EXACT}
O = {**R, 'arm': ORACLE, 'supplied_component': SUPPLIED}
C = {'arm': REAL, **SCOPE, **META, 'metrics': CMETRICS, **MATRIX}
J = {'arm': REAL, **SCOPE, 'scale': E('raw','final'), 'counts': {k:I for k in c.JOINT}, 'metrics': {k:NN for k in c.JOINT}}
RM = ('unsupported_loss', *[prefix+k for k in c.METRICS for prefix in ('supported_ranking_loss_', 'total_loss_')])
RESIDUAL = {'arm': E('O_CS'), 'supplied_component': E('category'), **SCOPE,
            'counts': {k:I for k in c.BANDS}, 'shares': {k:N for k in c.BANDS}, 'metrics': {k:N for k in RM}}


def summary_schema(dimensions, metrics):
    return {**dimensions, 'n_total': I, 'metrics': {k:STAT for k in metrics}}


RC = {'left':REAL, 'right':REAL, **SCOPE, 'metrics':EXACT}
OC = {**RC, 'left':E(*c.ORACLES), 'right':ALL}
CC = {'left':REAL, 'right':REAL, **SCOPE, **META, 'metrics':CMETRICS}
SCHEMA = {'experiment_id': E('E017'), 'status':E('COMPLETED'), 'development':L(DEVELOPMENT),
    'real_prediction': {'records':L(R), 'aggregate':L(summary_schema({'arm':REAL,'stratum':SCOPE['stratum']},EXACT)),
        'contrasts':L(RC), 'contrast_aggregate':L(summary_schema({'left':REAL,'right':REAL,'stratum':SCOPE['stratum']},EXACT)),
        'component_records':L(C), 'component_aggregate':L(summary_schema({'arm':REAL,**META,'stratum':SCOPE['stratum']},CMETRICS)),
        'component_contrasts':L(CC), 'component_contrast_aggregate':L(summary_schema({'left':REAL,'right':REAL,**META,'stratum':SCOPE['stratum']},CMETRICS)),
        'joint_records':L(J), 'joint_aggregate':L(summary_schema({'arm':REAL,'scale':META['scale'],'stratum':SCOPE['stratum']},c.JOINT)),
        'pooled_confusions':L({'arm':REAL,**META,'stratum':SCOPE['stratum'],'n_total':I,**MATRIX})},
    'oracle_diagnostic': {'uses_evaluation_truth':E(True), 'records':L(O),
        'aggregate':L(summary_schema({'arm':ORACLE,'supplied_component':SUPPLIED,'stratum':SCOPE['stratum']},EXACT)),
        'contrasts':L(OC), 'contrast_aggregate':L(summary_schema({'left':E(*c.ORACLES),'right':ALL,'stratum':SCOPE['stratum']},EXACT)),
        'headroom':L({'arm':E(*c.ORACLES),'supplied_component':SUPPLIED,'primary':s.B,**STAT,'positive_folds':I,'criterion_met':s.B}),
        'residual_records':L(RESIDUAL), 'residual_aggregate':L(summary_schema({'arm':E('O_CS'),'supplied_component':E('category'),'stratum':E('all')},RM))},
    'provenance': {'git_revision':s.pattern('[0-9a-f]{40}'), 'image_id':s.pattern('sha256:[0-9a-f]{64}'),
        'lock_sha256':s.HASH,'frozen_development_sha256':s.HASH,'started_utc':s.pattern('[0-9T:+.Z-]+'),
        'finished_utc':s.pattern('[0-9T:+.Z-]+'),'wall_seconds':N,'model_fits':E(100),'fit_warnings':E(0),
        'reproduction_model_folds':E(15),'global_freeze_verified':E(True),'preservation_verified':E(True),
        'uid':E(10001),'gid':E(10001),'row_level_outputs':E(False),'preserved_files':I}}


def unique(rows, keys):
    index = {tuple(r[k] for k in keys):r for r in rows}
    if len(index) != len(rows): raise ValueError('Duplicate aggregate records.')
    return index


def validate(p):
    s.validate_schema(p, SCHEMA)
    real, oracle = p['real_prediction'], p['oracle_diagnostic']
    rd = unique(real['records'], ('arm','fold','question','stratum'))
    od = unique(oracle['records'], ('arm','fold','question','stratum'))
    questions = {f: sorted({r['question'] for r in real['records'] if r['fold']==f and r['question'] is not None}) for f in range(5)}
    if any(len(v)!=3 for v in questions.values()) or len(set(sum(questions.values(),[])))!=15:
        raise ValueError('Question grid changed.')
    domains = [(f,q,t) for f in range(5) for q in [None,*questions[f]] for t in c.core.STRATA]
    if set(rd)!={(a,*d) for a in c.REAL for d in domains} or set(od)!={(a,*d) for a in ('F',*c.ORACLES) for d in domains}:
        raise ValueError('Incomplete real/oracle reporting grid.')
    for a in ('F',*c.ORACLES):
        for d in domains:
            if od[a,*d]['supplied_component']!=c.SUPPLIED[a]: raise ValueError('Oracle information tag changed.')
            if a=='F': same({k:v for k,v in od[a,*d].items() if k!='supplied_component'}, rd[a,*d])
    for rows, index, arms in ((real['records'],rd,c.REAL),(oracle['records'],od,('F',*c.ORACLES))):
        for r in rows:
            same(r['n'],rd['F',r['fold'],r['question'],r['stratum']]['n'])
            for metric,v in r['metrics'].items():
                if (v is None)!=(r['n']==0) or v is not None and not 0<=v<=1: raise ValueError('Invalid exact metric.')
                if r['stratum']=='unsupported' and r['n'] and v!=0: raise ValueError('Unsupported truth scored.')
            if r['question'] is None:
                parts = [index[r['arm'],r['fold'],q,r['stratum']] for q in questions[r['fold']]]
                same(r['n'],sum(x['n'] for x in parts))
                for m in c.METRICS:
                    same(r['metrics'][m],sum(x['n']*x['metrics'][m] for x in parts if x['n'])/r['n'] if r['n'] else None)
        for a in arms:
            for f in range(5):
                for q in [None,*questions[f]]:
                    all_r=index[a,f,q,'all']; parts=[index[a,f,q,s] for s in ('unsupported','rare','frequent')]
                    same(all_r['n'],sum(r['n'] for r in parts))
                    if index[a,f,q,'well_supported']['n']>index[a,f,q,'frequent']['n']: raise ValueError('Support nesting.')
                    for m in c.METRICS:
                        same(all_r['metrics'][m],sum(r['n']*r['metrics'][m] for r in parts if r['n'])/all_r['n'])
    for hi,lo in (('O_C','F'),('O_S','F'),('O_CS','O_C'),('O_CS','O_S')):
        for d in domains:
            if od[hi,*d]['n']:
                for m in c.METRICS:
                    if od[hi,*d]['metrics'][m]<od[lo,*d]['metrics'][m]-1e-12: raise ValueError('Oracle monotonicity.')
    cd = unique(real['component_records'],('arm','fold','question','stratum','scale','component'))
    expected = {(a,*d,scale,k) for a in c.REAL for d in domains for scale in ('raw','final') for k in c.COMPONENTS}
    if set(cd)!=expected: raise ValueError('Incomplete component grid.')
    for key,r in cd.items():
        cm=np.asarray(r['confusion_counts']); width=len(c.COMPONENTS[r['component']])
        if cm.shape!=(width,width): raise ValueError('Confusion dimensions changed.')
        same(int(cm.sum()),r['n']); same(r['n'],rd[key[:4]]['n'])
        metrics, normalized=c.matrix_metrics(cm)
        same(r['metrics'],metrics); same(r['confusion_row_normalized'],normalized)
        if r['question'] is None:
            expected_cm=sum(np.asarray(cd[r['arm'],r['fold'],q,r['stratum'],r['scale'],r['component']]['confusion_counts']) for q in questions[r['fold']])
            same(cm.tolist(),expected_cm.tolist())
        if r['stratum']=='all':
            expected_cm=sum(np.asarray(cd[r['arm'],r['fold'],r['question'],t,r['scale'],r['component']]['confusion_counts']) for t in ('unsupported','rare','frequent'))
            same(cm.tolist(),expected_cm.tolist())
        if r['stratum']=='well_supported':
            frequent=np.asarray(cd[r['arm'],r['fold'],r['question'],'frequent',r['scale'],r['component']]['confusion_counts'])
            if np.any(cm>frequent): raise ValueError('Nested support confusion mismatch.')
    jd=unique(real['joint_records'],('arm','fold','question','stratum','scale'))
    if set(jd)!={key[:-1] for key in expected}: raise ValueError('Incomplete joint grid.')
    for key,r in jd.items():
        same(r['n'],rd[key[:4]]['n']); same(sum(r['counts'].values()),r['n'])
        for k in c.JOINT: same(r['metrics'][k],r['counts'][k]/r['n'] if r['n'] else None)
        for comp,extra in (('correctness','correctness_only'),('status','status_only')):
            same(cd[*key,comp]['metrics']['accuracy'],(r['counts']['both_correct']+r['counts'][extra])/r['n'] if r['n'] else None)
        if r['question'] is None:
            for k in c.JOINT: same(r['counts'][k],sum(jd[r['arm'],r['fold'],q,r['stratum'],r['scale']]['counts'][k] for q in questions[r['fold']]))
    res=unique(oracle['residual_records'],('fold','question'))
    if set(res)!={(f,q) for f in range(5) for q in [None,*questions[f]]}: raise ValueError('Incomplete residual grid.')
    for (f,q),r in res.items():
        if r['stratum']!='all': raise ValueError('Residual population changed.')
        n=rd['F',f,q,'all']['n']; same(r['n'],n); same(sum(r['counts'].values()),n)
        same(r['counts']['unsupported'],rd['F',f,q,'unsupported']['n'])
        for k in c.BANDS: same(r['shares'][k],r['counts'][k]/n)
        same(od['O_CS',f,q,'all']['metrics']['map_at_3'],sum(r['shares'][k]/i for i,k in enumerate(('rank1','rank2','rank3'),1)))
        same(r['metrics']['unsupported_loss'],r['shares']['unsupported'])
        for m in c.METRICS:
            same(r['metrics']['total_loss_'+m],1-od['O_CS',f,q,'all']['metrics'][m])
            same(r['metrics']['supported_ranking_loss_'+m],r['metrics']['total_loss_'+m]-r['metrics']['unsupported_loss'])
            if r['metrics']['supported_ranking_loss_'+m]<-1e-12: raise ValueError('Negative residual loss.')
        if q is None:
            for k in c.BANDS: same(r['counts'][k],sum(res[f,x]['counts'][k] for x in questions[f]))
            for k in RM: same(r['metrics'][k],sum(res[f,x]['n']*res[f,x]['metrics'][k] for x in questions[f])/n)
    recomputed=c.build_panels(real['records'],oracle['records'],real['component_records'],real['joint_records'],oracle['residual_records'])
    same(real,recomputed['real_prediction']); same(oracle,recomputed['oracle_diagnostic'])
    dev=unique(p['development'],('learning_arm','fold'))
    if set(dev)!={(a,f) for a in c.previous.ARMS for f in range(5)}: raise ValueError('Development grid.')
    total=sum(rd['F',f,None,'all']['n'] for f in range(5))
    for (a,f),d in dev.items():
        check_selection(d['selection'], [{**x, 'ngram_range':list(x['ngram_range'])} for x in c.core.e001.GRID], 'params')
        if d['role_question_counts']!=[9,3,3] or d['n_train']+d['n_calibration']+d['n_evaluation']!=total:
            raise ValueError('Role counts changed.')
        same(d['n_evaluation'],rd['F',f,None,'all']['n'])
        if not np.exp(-3)<=d['temperature']<=np.exp(3) or not 0<=d['calibration_supported_n']<=d['n_calibration']:
            raise ValueError('Calibration metadata changed.')
    return p


def render(p):
    validate(p)
    r,o=p['real_prediction'],p['oracle_diagnostic']
    lines=['# E017 numerical results','',
        'Real historical predictions and oracle diagnostics are separate. Oracles use evaluation truth deliberately and are not deployable predictions or new baseline wins. All uncertainty is descriptive; results precede interpretation.','']
    for title,panel,arms in (('Real prediction controls',r,c.REAL),('Oracle diagnostics using evaluation truth',o,('F',*c.ORACLES))):
        lines.extend(['## '+title,''])
        if panel is o: lines.extend(['F is the unchanged real frequency reference. O_C supplies true correctness, O_S true explanation status, O_CS true full Category. No oracle confidence or calibration is reported.',''])
        table(lines,['Arm','MAP@3','Fold SD','Accuracy','Fold SD'],
            [[a['arm'],a['metrics']['map_at_3']['mean'],a['metrics']['map_at_3']['sd'],a['metrics']['top1_accuracy']['mean'],a['metrics']['top1_accuracy']['sd']] for a in panel['aggregate'] if a['stratum']=='all'])
        table(lines,['Arm','Fold','n','MAP@3','Accuracy'],[[x['arm'],x['fold'],x['n'],*[x['metrics'][m] for m in c.METRICS]] for x in panel['records'] if x['question'] is None and x['stratum']=='all'])
        table(lines,['Left','Right','MAP@3 delta','Fold SD','Accuracy delta','Fold SD'],
            [[x['left'],x['right'],x['metrics']['map_at_3']['mean'],x['metrics']['map_at_3']['sd'],x['metrics']['top1_accuracy']['mean'],x['metrics']['top1_accuracy']['sd']] for x in panel['contrast_aggregate'] if x['stratum']=='all'])
        table(lines,['Left','Right','Fold','MAP@3 delta','Accuracy delta'],
            [[x['left'],x['right'],x['fold'],*[x['metrics'][m] for m in c.METRICS]] for x in panel['contrasts'] if x['question'] is None and x['stratum']=='all'])
    lines.extend(['## Oracle headroom decisions only',''])
    table(lines,['Oracle','Primary','Delta mean','Fold SD','Positive folds','Headroom criterion'],
        [[x['arm'],x['primary'],x['mean'],x['sd'],x['positive_folds'],x['criterion_met']] for x in o['headroom']])
    lines.extend(['## Real component aggregate and fold results',''])
    table(lines,['Arm','Scale','Component','Accuracy','Fold SD','Macro F1','Fold SD'],
        [[x['arm'],x['scale'],x['component'],x['metrics']['accuracy']['mean'],x['metrics']['accuracy']['sd'],x['metrics']['macro_f1']['mean'],x['metrics']['macro_f1']['sd']] for x in r['component_aggregate'] if x['stratum']=='all'])
    table(lines,['Arm','Scale','Component','Fold','n','Accuracy','Macro F1'],
        [[x['arm'],x['scale'],x['component'],x['fold'],x['n'],x['metrics']['accuracy'],x['metrics']['macro_f1']] for x in r['component_records'] if x['question'] is None and x['stratum']=='all'])
    lines.extend(['## Oracle full Category residual decomposition',''])
    table(lines,['Fold','Question','n',*c.BANDS,*RM],
        [[x['fold'],'all' if x['question'] is None else x['question'],x['n'],*[x['counts'][k] for k in c.BANDS],*[x['metrics'][k] for k in RM]] for x in o['residual_records']])
    table(lines,['Metric','Mean','Fold SD','Defined folds'],[[k,v['mean'],v['sd'],v['defined_folds']] for x in o['residual_aggregate'] for k,v in x['metrics'].items()])
    for title,panel in (('Real prediction',r),('Oracle diagnostic using evaluation truth',o)):
        lines.extend(['## '+title+' complete exact label grid',''])
        table(lines,['Arm','Fold','Question','Stratum','n','MAP@3','Accuracy'],
            [[x['arm'],x['fold'],'all' if x['question'] is None else x['question'],x['stratum'],x['n'],*[x['metrics'][m] for m in c.METRICS]] for x in panel['records']])
        table(lines,['Arm','Stratum','Metric','Mean','Fold SD','Defined folds'],
            [[x['arm'],x['stratum'],k,v['mean'],v['sd'],v['defined_folds']] for x in panel['aggregate'] for k,v in x['metrics'].items()])
        table(lines,['Left','Right','Fold','Question','Stratum','n','MAP@3 delta','Accuracy delta'],
            [[x['left'],x['right'],x['fold'],'all' if x['question'] is None else x['question'],x['stratum'],x['n'],*[x['metrics'][m] for m in c.METRICS]] for x in panel['contrasts']])
        table(lines,['Left','Right','Stratum','Metric','Mean','Fold SD','Defined folds'],
            [[x['left'],x['right'],x['stratum'],k,v['mean'],v['sd'],v['defined_folds']] for x in panel['contrast_aggregate'] for k,v in x['metrics'].items()])
    lines.extend(['## Real component complete grid and confusion matrices','',
        'Rows are truth and columns predictions. Orders: correctness False, True; status Correct, Misconception, Neither; Category False_Correct, False_Misconception, False_Neither, True_Correct, True_Misconception, True_Neither. Matrices contain aggregate counts only. Null normalized rows have no truth support.',''])
    table(lines,['Arm','Fold','Question','Stratum','Scale','Component','n','Accuracy','Macro F1','Count matrix','Row normalized matrix'],
        [[x['arm'],x['fold'],'all' if x['question'] is None else x['question'],x['stratum'],x['scale'],x['component'],x['n'],
          x['metrics']['accuracy'],x['metrics']['macro_f1'],json.dumps(x['confusion_counts']),json.dumps(x['confusion_row_normalized'])] for x in r['component_records']])
    table(lines,['Arm','Scale','Component','Stratum','Metric','Mean','Fold SD','Defined folds'],
        [[x['arm'],x['scale'],x['component'],x['stratum'],k,v['mean'],v['sd'],v['defined_folds']] for x in r['component_aggregate'] for k,v in x['metrics'].items()])
    table(lines,['Left','Right','Fold','Question','Stratum','Scale','Component','n','Accuracy delta','Macro F1 delta'],
        [[x['left'],x['right'],x['fold'],'all' if x['question'] is None else x['question'],x['stratum'],x['scale'],x['component'],x['n'],x['metrics']['accuracy'],x['metrics']['macro_f1']] for x in r['component_contrasts']])
    table(lines,['Left','Right','Scale','Component','Stratum','Metric','Mean','Fold SD','Defined folds'],
        [[x['left'],x['right'],x['scale'],x['component'],x['stratum'],k,v['mean'],v['sd'],v['defined_folds']] for x in r['component_contrast_aggregate'] for k,v in x['metrics'].items()])
    lines.extend(['## Real pooled confusion counts only','', 'Pooled counts and row normalization do not replace equal-fold performance.',''])
    table(lines,['Arm','Scale','Component','Stratum','n','Count matrix','Row normalized matrix'],
        [[x['arm'],x['scale'],x['component'],x['stratum'],x['n_total'],json.dumps(x['confusion_counts']),json.dumps(x['confusion_row_normalized'])] for x in r['pooled_confusions']])
    lines.extend(['## Real joint component outcomes',''])
    table(lines,['Arm','Fold','Question','Stratum','Scale','n',*c.JOINT,*[k+' share' for k in c.JOINT]],
        [[x['arm'],x['fold'],'all' if x['question'] is None else x['question'],x['stratum'],x['scale'],x['n'],*[x['counts'][k] for k in c.JOINT],*[x['metrics'][k] for k in c.JOINT]] for x in r['joint_records']])
    table(lines,['Arm','Scale','Stratum','Outcome','Mean share','Fold SD','Defined folds'],
        [[x['arm'],x['scale'],x['stratum'],k,v['mean'],v['sd'],v['defined_folds']] for x in r['joint_aggregate'] for k,v in x['metrics'].items()])
    lines.extend(['## Historical reconstruction selections',''])
    table(lines,['Arm','Fold','Candidate','Settings','Inner 0','Inner 1','Inner 2','Mean','Selected','Temperature','Supported calibration n'],
        [[d['learning_arm'],d['fold'],i,json.dumps(v['params']),*v['inner_fold_map_at_3'],v['inner_mean_map_at_3'],i==d['selection']['selected_index'],d['temperature'],d['calibration_supported_n']] for d in p['development'] for i,v in enumerate(d['selection']['candidates'])])
    lines.extend(['Full precision, rank-band shares and all five-fold statistic vectors are in [the aggregate artifact](../results/E017_aggregates.json). No row-level outputs or answer keys are published.',''])
    return '\n'.join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output-json',type=Path,required=True); parser.add_argument('--output-markdown',type=Path,required=True)
    args=parser.parse_args()
    p=json.loads(args.source.read_text()); validate(p)
    receipt=json.loads((args.source.parent/'execution.json').read_text())
    if receipt['status']!='COMPLETED' or receipt['results_sha256']!=file_sha256(args.source): raise ValueError('Completion receipt mismatch.')
    same(receipt['git_revision'],p['provenance']['git_revision']); same(receipt['lock_sha256'],p['provenance']['lock_sha256'])
    if args.output_json.exists() or args.output_markdown.exists(): raise ValueError('Never overwrite published results.')
    write_new(args.output_json,p)
    with args.output_markdown.open('x',encoding='utf-8',newline='\n') as stream: stream.write(render(p))
    print('E017 separate real/oracle schema, arithmetic and completion receipt verified; numerical report published.')


if __name__=='__main__': main()
