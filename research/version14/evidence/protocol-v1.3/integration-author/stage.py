"""Curate the integrated source without inventing protected job inputs."""
from pathlib import Path
import importlib.util
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[2]
TREE = ROOT / 'tree'
SOURCE = WORKSPACE / 'work/protocol-ruleset-20261107'
V13 = ROOT.parent
if hashlib.sha256((SOURCE/'controller/stage_bundle.py').read_bytes()).hexdigest() != '191cd76f17740153c958fb41d87a05a1a670a6d67dbfa8a383b72bc0d3e01a9b':
    raise ValueError('baseline staging-tool digest changed')
spec = importlib.util.spec_from_file_location('staging', SOURCE/'controller/stage_bundle.py')
staging = importlib.util.module_from_spec(spec)
spec.loader.exec_module(staging)
staging.SOURCE = TREE
staging.TESTS = tuple(dict.fromkeys((*staging.TESTS, 'adapter/test_coverage_gate.py', 'controller/test_runtime_coverage.py')))
extra_documents = ['adapter/COVERAGE-V1.3.md', 'adapter/PROTOCOL-V1.3.md', 'RUNTIME-INTEGRATION.md']
for name in ('GATE-REVIEW.md', 'RUNTIME-REVIEW.md'):
    destination = TREE/'integration-evidence'/name
    destination.parent.mkdir(exist_ok=True)
    shutil.copyfile(V13/'independent-review'/name, destination)
    extra_documents.append('integration-evidence/'+name)
staging.DOCUMENTS = tuple(dict.fromkeys((*staging.DOCUMENTS, *extra_documents)))
# The deployed quota workflow is stored only at its actual workflow path.
# Materialize the exact baseline bytes at the existing curator's source name.
quota_source = TREE/'.github/workflows/protocol-quota-probe.yml'
quota_template = TREE/'controller/quota.workflow.template.yml'
if quota_template.exists() and quota_template.read_bytes() != quota_source.read_bytes():
    raise ValueError('quota template differs from frozen baseline workflow')
quota_template.write_bytes(quota_source.read_bytes())
staging.stage(TREE/'deployment-bundle')
manifest = json.loads((TREE/'deployment-bundle/BUNDLE-MANIFEST.json').read_text())
integration = json.loads((ROOT/'INTEGRATION.json').read_text())
assert manifest['production_edges'] == integration['production_edges']
assert manifest['test_edges'] == integration['test_edges']
for path, record in integration['accepted_overlays'].items():
    assert manifest['files'][path]['sha256'] == record['sha256'], path
assert not manifest['protected_config_present']
print('All ten accepted gate/runtime files and supporting note are present; actual protected input overlay is absent.')
