"""Strict aggregate-only readiness receipt validation; no MAP results."""
import math
from . import e007_publication as s
from .e020_checker import REASONS

E=s.enum; I=s.I; N=s.N; B=s.B; NN=s.NN
MODEL={'model':E('G15','G7'),'fixtures':E(12),'completed_readouts':I,'binary_correct':I,'binary_total':E(10),
    'insufficient_correct':I,'insufficient_total':E(2),'technical_pass':B,'semantic_gate_applicable':B,
    'gate_passed':B,'reason_counts':{r:I for r in REASONS},'truncated_rationales':I,
    'generated_tokens':I,'generation_seconds':N,'tokens_per_second':NN,'mean_readout_seconds':N,
    'projected_map_seconds':NN,'status':E('COMPLETED'),'wall_seconds':N,'peak_rss_bytes':I,
    'container_peak_bytes':s.nullable(I),'model_manifest_sha256':s.HASH,'environment_lock_sha256':s.HASH,
    'readiness_lock_sha256':s.HASH}


def close(a,b):
    if a is None or b is None:
        if a is not b: raise ValueError('Null mismatch.')
    elif not math.isclose(a,b,abs_tol=1e-10,rel_tol=1e-12): raise ValueError('Readiness arithmetic mismatch.')


def validate_model(p):
    s.validate_schema(p,MODEL)
    for key in ('generation_seconds','tokens_per_second','mean_readout_seconds','projected_map_seconds','wall_seconds'):
        if p[key] is not None and p[key]<0: raise ValueError('Negative timing.')
    if sum(p['reason_counts'].values())!=12 or p['completed_readouts']!=p['reason_counts']['readout_completed']:
        raise ValueError('Readiness fixture accounting.')
    if p['binary_correct']>10 or p['insufficient_correct']>2 or p['truncated_rationales']>12 or p['generated_tokens']>12*512:
        raise ValueError('Invalid readiness counts.')
    if p['semantic_gate_applicable']!=(p['model']=='G7') or p['technical_pass']!=(p['completed_readouts']==12):
        raise ValueError('Gate applicability changed.')
    expected=p['technical_pass'] and (p['model']=='G15' or p['binary_correct']>=8 and p['insufficient_correct']==2)
    if p['gate_passed']!=expected: raise ValueError('Gate decision changed.')
    rate=p['generated_tokens']/p['generation_seconds'] if p['generation_seconds']>0 else None
    close(p['tokens_per_second'],rate)
    projected=60*(512/rate+p['mean_readout_seconds']) if rate and p['technical_pass'] else None
    close(p['projected_map_seconds'],projected)
    if p['container_peak_bytes'] is not None and p['container_peak_bytes']>24*1024**3:
        raise ValueError('Memory budget exceeded.')
    return p


def validate(p):
    common={'map_started':E(False),'automatic_retry':E(False),'model_receipts':s.listing(MODEL)}
    if p.get('status')=='GATE_FAILED':
        schema={**common,'status':E('GATE_FAILED'),'failed_model':E('G15','G7')}
    else:
        schema={**common,'status':E('RUNTIME_REVIEW_REQUIRED','READY_FOR_MAP_IMPLEMENTATION_CHECK'),'projected_map_seconds':N}
    s.validate_schema(p,schema)
    rows=[validate_model(r) for r in p['model_receipts']]
    if not rows or [r['model'] for r in rows]!=['G15','G7'][:len(rows)]: raise ValueError('Model sequence changed.')
    if p['status']=='GATE_FAILED':
        if rows[-1]['model']!=p['failed_model'] or rows[-1]['gate_passed'] or any(not r['gate_passed'] for r in rows[:-1]):
            raise ValueError('Gate failure mismatch.')
    else:
        if len(rows)!=2 or not all(r['gate_passed'] for r in rows): raise ValueError('Unmet gate.')
        projection=sum(r['projected_map_seconds'] for r in rows); close(p['projected_map_seconds'],projection)
        if (p['status']=='RUNTIME_REVIEW_REQUIRED')!=(projection>48*3600): raise ValueError('Runtime rule changed.')
    return p
