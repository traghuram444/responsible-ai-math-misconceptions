"""Deterministic static SVG figures from public aggregates only; no new analyses."""
from __future__ import annotations

import argparse
import hashlib
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/figures'
VARIANTS = ('explanation_only', 'question_plus_explanation')
TITLES = ('Explanation only', 'Question + explanation')
COLORS = ('#007c91', '#c15d16', '#7956a5', '#627d24', '#777777', '#243746')
RULES = ('learned_reliability', 'confidence_only', 'support_aware', 'raw_confidence', 'hash_only', 'frequency')
LABELS = ('Learned reliability', 'Calibrated confidence', 'Support-aware', 'Raw confidence', 'Hash-only', 'Frequency classifier')


def extract(root=ROOT):
    source = 'results/E010_aggregates.json'
    p = json.loads((root / source).read_text(encoding='utf-8'))
    summaries = p['aggregate']['summaries']
    curves = [{k: s[k] for k in ('variant', 'rule', 'review_percent')} |
              {'remaining_errors_per_100': s['groups']['all']['remaining_errors_per_100']}
              for s in summaries]
    lookup = {(r['variant'], r['fold'], r['rule'], r['review_percent']): r for r in p['records']}
    questions = []
    for variant in VARIANTS:
        for fold in range(5):
            left = lookup[variant, fold, 'learned_reliability', 20]['evaluation']['questions']
            right = {q['QuestionId']: q for q in lookup[variant, fold, 'support_aware', 20]['evaluation']['questions']}
            for q in left:
                g, c = q['groups']['all'], right[q['QuestionId']]['groups']['all']
                questions.append({'variant': variant, 'fold': fold, 'QuestionId': q['QuestionId'],
                    'original_n': g['original_n'],
                    'benefit_per_100': c['remaining_errors_per_100'] - g['remaining_errors_per_100'],
                    'learned_review_fraction': g['review_fraction'], 'support_review_fraction': c['review_fraction']})
    # Extract the published rounded E001 values, not untracked private artifacts.
    rows = [line.split('|')[1:-1] for line in (root / 'docs/E001_RESULTS.md').read_text(encoding='utf-8').splitlines()
            if line.startswith('| Random-reference / question + explanation |')
            or line.startswith('| Question-held-out / question + explanation |')]
    baseline = {(row[0].strip(), row[1].strip()): float(row[4]) for row in rows}
    generalization = [
        {'label': 'Random response split / TF-IDF', 'map_at_3': baseline['Random-reference / question + explanation', 'TF–IDF + LR']},
        {'label': 'Held-out question / TF-IDF', 'map_at_3': baseline['Question-held-out / question + explanation', 'TF–IDF + LR']},
        {'label': 'Held-out question / frequency', 'map_at_3': baseline['Question-held-out / question + explanation', 'Frequency']}]
    sources = {name: hashlib.sha256((root / name).read_bytes().replace(b'\r\n', b'\n')).hexdigest()
               for name in (source, 'docs/E001_RESULTS.md')}
    return {'source_sha256_lf': sources, 'aggregation': 'equal-fold means; sample SD; descriptive only',
            'generalization': generalization, 'routing': curves, 'primary': p['aggregate']['primary'],
            'questions': questions, 'question_scope': 'all 15 questions per arm; 20% pooled fold review budget, not question quotas'}


class SVG:
    def __init__(self, title, subtitle, height=540):
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="{height}" viewBox="0 0 1100 {height}" role="img">',
                      f'<title>{escape(title)}</title><desc>{escape(subtitle)}</desc>',
                      f'<rect width="1100" height="{height}" fill="#ffffff"/>']
        self.text(32, 38, title, 24, weight='bold')
        self.text(32, 66, subtitle, 14)

    def text(self, x, y, value, size=13, color='#243746', anchor='start', weight='normal'):
        self.parts.append(f'<text x="{x:.2f}" y="{y:.2f}" fill="{color}" font-family="Arial, sans-serif" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{escape(str(value))}</text>')

    def line(self, x1, y1, x2, y2, color='#dce3e8', width=1, dash=''):
        self.parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>')

    def dot(self, x, y, color, radius=5):
        self.parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{radius}" fill="{color}"/>')

    def finish(self):
        return '\n'.join(self.parts + ['</svg>']) + '\n'


def figures(data):
    outputs = {}
    s = SVG('Random validation overstates unseen-question performance',
            'E001: question + explanation; five-fold mean MAP@3; published values rounded to three decimals.', 385)
    for i, row in enumerate(data['generalization']):
        y = 128 + i * 65
        s.text(32, y + 5, row['label'], 16)
        end = 385 + row['map_at_3'] * 620
        s.line(385, y, end, y, COLORS[0] if i == 0 else COLORS[i + 1], 25)
        s.text(end + 15, y + 5, f"{row['map_at_3']:.3f}", 17, weight='bold')
    for t in range(11):
        x = 385 + t / 10 * 620
        s.line(x, 290, x, 298)
        s.text(x, 318, f'{t / 10:.1f}', anchor='middle')
    s.text(695, 350, 'MAP@3 (higher is better)', anchor='middle')
    outputs['generalization.svg'] = s.finish()

    s = SVG('Fixed review budgets reduce remaining errors, but leave substantial risk',
            'E010: errors remaining outside the queue per 100 original responses; equal-fold means, all registered budgets.', 650)
    for arm, variant in enumerate(VARIANTS):
        x0, y0, w, h = 85 + 535 * arm, 120, 415, 330
        s.text(x0, 104, TITLES[arm], 18, weight='bold')
        for tick in range(0, 81, 20):
            y = y0 + h - tick / 80 * h
            s.line(x0, y, x0 + w, y)
            s.text(x0 - 10, y + 4, tick, anchor='end')
        for rule, color in zip(RULES, COLORS):
            rows = sorted([r for r in data['routing'] if r['variant'] == variant and r['rule'] == rule], key=lambda r: r['review_percent'])
            points = [(x0 + r['review_percent'] / 50 * w, y0 + h - r['remaining_errors_per_100']['mean'] / 80 * h) for r in rows]
            for a, b in zip(points, points[1:]): s.line(*a, *b, color, 2, '6 4' if rule in ('raw_confidence', 'frequency') else '')
            for x, y in points: s.dot(x, y, color, 3)
        for t in range(0, 51, 10): s.text(x0 + t / 50 * w, y0 + h + 25, t, anchor='middle')
        s.text(x0 + w / 2, y0 + h + 52, 'Review budget (%)', anchor='middle')
    for i, (label, color) in enumerate(zip(LABELS, COLORS)):
        x, y = 40 + (i % 3) * 350, 555 + (i // 3) * 27
        s.line(x, y - 4, x + 25, y - 4, color, 3)
        s.text(x + 34, y, label)
    s.text(32, 625, 'Deferred errors are not assumed corrected. Frequency is a different classifier; other rules share predictions.', 13)
    outputs['review_routing.svg'] = s.finish()

    s = SVG('Neither arm meets the E010 primary improvement criterion',
            '20% review: support-aware minus learned remaining errors per 100 original responses; positive favors learned.', 540)
    for arm, row in enumerate(data['primary']):
        x0, w = 100 + 535 * arm, 390
        s.text(x0, 108, TITLES[arm], 18, weight='bold')
        def xpos(v): return x0 + (v + 1) / 5 * w
        for t in (-1, 0, 1, 2, 3, 4):
            s.line(xpos(t), 130, xpos(t), 400, '#aab5bd' if t == 0 else '#e4e9ed')
            s.text(xpos(t), 424, t, anchor='middle')
        s.line(xpos(2), 130, xpos(2), 400, '#c15d16', 2, '6 4')
        for fold, value in enumerate(row['fold_values']):
            y = 154 + fold * 38
            s.text(x0 - 15, y + 4, f'Fold {fold}', anchor='end')
            s.dot(xpos(value), y, COLORS[0])
        y = 365
        s.line(xpos(row['mean'] - row['sd']), y, xpos(row['mean'] + row['sd']), y, COLORS[0], 3)
        s.dot(xpos(row['mean']), y, '#243746', 7)
        s.text(x0 - 15, y + 4, 'Mean / SD', anchor='end')
        s.text(x0, 465, f"Mean {row['mean']:.3f}; positive folds {row['positive_folds']}/5; criterion unmet", 14)
    s.text(32, 515, 'Criterion: mean benefit >= 2.0 AND positive in >= 4/5 folds. SD is descriptive, not a confidence interval.', 14)
    outputs['fold_variation.svg'] = s.finish()

    s = SVG('Review-prioritization benefit varies across questions',
            'E010: all 15 evaluation questions in numeric order; 20% pooled-fold budget; positive favors learned over support-aware.', 780)
    values = [q['benefit_per_100'] for q in data['questions']]
    limit = max(5, int(max(abs(v) for v in values)) + 1)
    for arm, variant in enumerate(VARIANTS):
        x0, w = 110 + 535 * arm, 390
        s.text(x0, 108, TITLES[arm], 18, weight='bold')
        def xpos(v): return x0 + (v + limit) / (2 * limit) * w
        for tick in (-limit, 0, limit):
            s.line(xpos(tick), 124, xpos(tick), 685, '#aab5bd' if tick == 0 else '#e4e9ed')
            s.text(xpos(tick), 713, tick, anchor='middle')
        rows = sorted([q for q in data['questions'] if q['variant'] == variant], key=lambda q: q['QuestionId'])
        for i, q in enumerate(rows):
            y = 145 + i * 37
            value = q['benefit_per_100']
            s.text(x0 - 12, y + 4, q['QuestionId'], anchor='end')
            s.line(xpos(0), y, xpos(value), y, COLORS[0] if value >= 0 else COLORS[1], 3)
            s.dot(xpos(value), y, COLORS[0] if value >= 0 else COLORS[1], 4)
    s.text(32, 756, 'Difference per 100 responses within each question; review shares may differ between rules. No question was selected out.', 13)
    outputs['per_question.svg'] = s.finish()
    outputs['figure_data.json'] = json.dumps(data, indent=2, sort_keys=True, allow_nan=False) + '\n'
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = figures(extract())
    if not args.check: OUT.mkdir(parents=True, exist_ok=True)
    for name, text in outputs.items():
        path = OUT / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != text:
                raise ValueError(f'Figure/source mismatch: {name}')
        else:
            path.write_text(text, encoding='utf-8', newline='\n')
    print(f'{len(outputs)} deterministic figure artifacts {"verified" if args.check else "generated"} from public aggregates only.')


if __name__ == '__main__': main()
