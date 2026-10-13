"""Publication/figure regression tests: public and synthetic material only."""
import importlib.util
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f'repro/{name}.py')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


@pytest.mark.parametrize('name', ['data/raw/train.csv', 'artifacts/results.json', '.env', 'nested/.env.local',
    'model.pt', 'outputs/predictions.npz', 'credentials.json', '../escape.md', '/abs.md', 'unknown.exe'])
def test_private_paths_rejected(name):
    assert not module('audit_release').path_allowed(name)


@pytest.mark.parametrize('name', ['README.md', 'repro/Dockerfile', 'repro/core.lock', '.github/workflows/verify.yml',
                                  'docs/figures/generalization.svg', 'CITATION.cff'])
def test_public_paths_allowed(name):
    assert module('audit_release').path_allowed(name)


def test_all_historical_files_preserved():
    assert module('audit_release').check_history() == 144


@pytest.mark.parametrize('prefix,size', [('gh' + 'p_', 36), ('github_' + 'pat_', 40), ('AK' + 'IA', 16)])
def test_common_secret_shapes_detected(prefix, size):
    assert module('audit_release').SECRET.search(prefix + 'A' * size)


def test_release_document_links_exist_and_stay_in_checkout():
    names = ['README.md', 'docs/RESEARCH_REPORT.md', 'docs/EXPERIMENT_INDEX.md',
             'docs/REPRODUCTION.md', 'docs/RELEASE_NOTES.md', 'docs/RELEASE_AUDIT_2026_10.md']
    for name in names:
        path = ROOT / name
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if target.startswith(('https://', 'http://', '#')): continue
            resolved = (path.parent / target.split('#')[0]).resolve()
            assert resolved.is_relative_to(ROOT) and resolved.exists(), (name, target)


def test_citation_matches_repository_and_checkpoint():
    import yaml
    citation = yaml.safe_load((ROOT / 'CITATION.cff').read_text(encoding='utf-8'))
    assert citation['cff-version'] == '1.2.0'
    assert citation['version'] == '0.1.0-research'
    assert citation['repository-code'].endswith('/traghuram444/responsible-ai-math-misconceptions')
    assert citation['license'] == 'MIT'


def test_figures_use_complete_registered_grids():
    mod = module('make_figures')
    data = mod.extract()
    assert len(data['routing']) == 72
    assert len(data['questions']) == 30
    for arm in mod.VARIANTS:
        assert len({q['QuestionId'] for q in data['questions'] if q['variant'] == arm}) == 15
    assert [g['map_at_3'] for g in data['generalization']] == [.785, .520, .539]
    source = json.loads((ROOT / 'results/E010_aggregates.json').read_text(encoding='utf-8'))
    assert data['primary'] == source['aggregate']['primary']
    for name, text in mod.figures(data).items():
        assert (ROOT / 'docs/figures' / name).read_text(encoding='utf-8') == text
        if name.endswith('.svg'):
            root = ET.fromstring(text)
            assert root.attrib['role'] == 'img'
            assert root.find('{http://www.w3.org/2000/svg}title') is not None
