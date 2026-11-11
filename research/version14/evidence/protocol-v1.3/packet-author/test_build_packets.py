"""Synthetic local Git fixtures only. No real review or observation is created."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest

import build_packets as b


class PacketTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=b.HERE)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repository = self.root / 'repository'
        self.repository.mkdir()
        self.git('init', '-q')
        self.git('config', 'user.name', 'Synthetic fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('config', 'core.autocrlf', 'false')
        self.document_manifest = b.load(b.HERE.parent / 'docs-author/r2/MANIFEST.json')
        old_files = b.HERE.parents[1] / 'protocol-ruleset-20261107/protocol-v1.2/repo-files'
        for row in self.document_manifest['files']:
            if row['base_sha256'] is not None:
                if row['path'] == 'README.md':
                    raw = subprocess.check_output(['git', '-C', str(b.HERE.parents[1] / 'quartic-version6-release/repository'),
                        'show', '2125274b93314c9a9e51c7b47559025489565632:README.md'])
                else:
                    raw = (old_files / row['path']).read_bytes()
                self.put(row['path'], raw)
        self.put('proof.tex', b'Synthetic unchanged proof.\n')
        self.put('data/table.json', b'{"synthetic":true}\n')
        self.commit()
        base = self.git('rev-parse', 'HEAD').strip()
        for row in self.document_manifest['files']:
            self.put(row['path'], (b.HERE.parent / 'docs-author/r2/files' / row['path']).read_bytes())
        self.report_source = self.root / 'report.md'
        self.report_source.write_bytes(b'Synthetic report fixture, not an actual decision.\n')
        self.report_path = 'docs/research-review/V13-FIXTURE-REPORT.md'
        self.put(self.report_path, self.report_source.read_bytes())
        self.dossier_path = 'docs/research-review/coverage/v13-fixture.json'
        self.profile = {'schema': 'protocol-coverage-policy/v1', 'protocol_version': '1.3',
                        'governing_protocol': {'path': b.PROTOCOL, 'sha256': b.PROTOCOL_SHA256},
                        'runtime_policy_sha256': 'f' * 64, 'mode': 'non_substantive', 'claim_ids': [],
                        'proof_paths': ['proof.tex', 'data/table.json'],
                        'allowed_nonmath_paths': sorted(b.DOCUMENT_PATHS | {self.report_path, self.dossier_path})}
        self.dossier = {'schema': 'protocol-coverage/v1', 'profile_sha256': b.core.digest(self.profile),
                        'mode': 'non_substantive', 'scope': 'Synthetic policy-only scope. No proof completion claim.',
                        'sources': [{'side': 'head', 'path': path,
                                     'sha256': hashlib.sha256((self.repository / path).read_bytes()).hexdigest()}
                                    for path in self.profile['proof_paths']]}
        self.dossier_source = self.root / 'dossier.json'
        self.write_dossier()
        self.commit()
        self.context = {'repository': 'fixture/repository', 'repository_id': 123, 'pr': 99,
                        'base': base, 'head': self.git('rev-parse', 'HEAD').strip()}

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repository), *args],
                                       env=b.gm.git_environment()).decode().strip()

    def put(self, path, raw):
        destination = self.repository / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'synthetic fixture')

    def update_head(self):
        self.commit()
        self.context['head'] = self.git('rev-parse', 'HEAD')

    def write_dossier(self):
        self.dossier_source.write_bytes((json.dumps(self.dossier) + '\n').encode())
        self.put(self.dossier_path, self.dossier_source.read_bytes())

    def prepare(self, **changes):
        arguments = dict(repository=self.repository, context=self.context, policy_sha256='f' * 64,
                         document_manifest=self.document_manifest,
                         reports=[{'path': self.report_path, 'source': str(self.report_source),
                                   'author_run': 'synthetic-report-author'}],
                         dossier_path=self.dossier_path, dossier_source=self.dossier_source,
                         profile=self.profile, text_author_run='synthetic-text-author',
                         integrator_run='synthetic-integrator', coverage_author_runs=['synthetic-dossier-author'],
                         findings=[], finding_bodies={})
        arguments.update(changes)
        return b.prepare(**arguments)

    def test_complete_packet_and_separate_coverage_target(self):
        result = self.prepare()
        packet = result['packet.json']
        self.assertEqual(len(packet['changes']), 8)
        self.assertEqual(len(packet['applications']), 2)
        apps = {a['id']: a for a in packet['applications']}
        self.assertEqual(apps[b.COVERAGE_ID]['dependencies'], [b.POLICY_ID])
        self.assertEqual(apps[b.POLICY_ID]['dependencies'], [])
        self.assertIn(apps[b.COVERAGE_ID]['coverage_record'], apps[b.COVERAGE_ID]['files'])
        self.assertEqual(packet['base']['files']['proof.tex'], packet['head']['files']['proof.tex'])
        target = next(t for t in result['targets.json'] if t['target_id'] == b.COVERAGE_ID)
        self.assertEqual(target['target_kind'], 'application')
        self.assertTrue(target['status'].startswith('awaiting'))
        self.assertFalse(result['PREPARATION.json']['receipts_created'])
        self.assertFalse(result['PREPARATION.json']['observations_created'])
        b.write_outputs(self.root / 'unsigned', result)
        b.write_outputs(self.root / 'unsigned', result)
        with self.assertRaises(ValueError):
            b.write_outputs(self.root / 'unsigned', {'packet.json': {'changed': True}})

    def test_current_coverage_schema_accepts_the_unsigned_structure(self):
        path = b.HERE.parent / 'gate-author/adapter/coverage_gate.py'
        spec = importlib.util.spec_from_file_location('synthetic_coverage_schema', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        core_spec = importlib.util.spec_from_file_location('synthetic_coverage_core',
            b.HERE.parent / 'gate-author/adapter/offline_manifest_gate.py')
        coverage_core = importlib.util.module_from_spec(core_spec)
        core_spec.loader.exec_module(coverage_core)
        module.g = coverage_core
        result = self.prepare()
        profile = module.select_profile(result['packet.json'], self.profile)
        self.assertEqual(profile, self.profile)
        # Exercise only the post-authentication structural routine with explicit
        # synthetic in-memory evidence. This does not export a receipt.
        apps = {a['id']: a for a in result['packet.json']['applications']}
        def read_pin(pin):
            return (self.repository / pin['path']).read_bytes()
        status = module.validate(result['packet.json'], profile, apps,
                                 {b.POLICY_ID: {'synthetic-policy-author'}, b.COVERAGE_ID: {'synthetic-dossier-author'}},
                                 {'synthetic-reviewer': {'agent_id': 'synthetic-nonauthor'}},
                                 {('application', b.COVERAGE_ID): {'run_id': 'synthetic-reviewer'}}, read_pin)
        self.assertEqual(status['protocol_coverage'], '1.3-non-substantive-scope-only')

    def test_unlisted_change_is_rejected(self):
        self.put('unlisted.txt', b'Unexpected artifact.\n')
        self.update_head()
        with self.assertRaisesRegex(ValueError, 'unlisted'):
            self.prepare()

    def test_wrong_supplied_protocol_cannot_be_rehashed_away(self):
        changed = copy.deepcopy(self.document_manifest)
        next(r for r in changed['files'] if r['path'] == b.PROTOCOL)['candidate_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'supplied v1.3'):
            self.prepare(document_manifest=changed)

    def test_historical_v12_cannot_be_replaced(self):
        changed = copy.deepcopy(self.document_manifest)
        next(r for r in changed['files'] if r['path'] == b.HISTORY)['candidate_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'historical v1.2'):
            self.prepare(document_manifest=changed)

    def test_profile_cannot_claim_new_mathematics(self):
        changed = copy.deepcopy(self.profile)
        changed['claim_ids'] = ['new-theorem']
        with self.assertRaisesRegex(ValueError, 'cannot declare mathematical claims'):
            self.prepare(profile=changed)

    def test_runtime_policy_binding_required(self):
        changed = copy.deepcopy(self.profile)
        changed['runtime_policy_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'policy binding differs'):
            self.prepare(profile=changed)

    def test_actual_report_required(self):
        with self.assertRaisesRegex(ValueError, 'actual review report'):
            self.prepare(reports=[])

    def test_changed_proof_is_rejected(self):
        self.put('proof.tex', b'Changed proof.\n')
        self.update_head()
        with self.assertRaises(ValueError):
            self.prepare()

    def test_committed_report_must_match_actual_file(self):
        self.report_source.write_bytes(b'Different local report.\n')
        with self.assertRaisesRegex(ValueError, 'committed report'):
            self.prepare()

    def test_unreviewed_executable_mode_rejected(self):
        self.git('update-index', '--chmod=+x', 'README.md')
        self.git('commit', '-qm', 'synthetic mode change')
        self.context['head'] = self.git('rev-parse', 'HEAD')
        with self.assertRaisesRegex(ValueError, 'file mode differs'):
            self.prepare()

    def test_profile_and_dossier_cannot_disagree(self):
        changed = copy.deepcopy(self.profile)
        changed['proof_paths'].pop()
        with self.assertRaisesRegex(ValueError, 'profile binding'):
            self.prepare(profile=changed)

    def test_missing_dossier_proof_pin_is_rejected(self):
        self.dossier['sources'].pop()
        self.write_dossier()
        self.update_head()
        with self.assertRaisesRegex(ValueError, 'omits a protected'):
            self.prepare()

    def test_unresolved_finding_is_preserved(self):
        body = 'Synthetic unresolved review issue.'
        finding = {'id': 'SYNTHETIC-ISSUE', 'body_sha256': hashlib.sha256(body.encode()).hexdigest(),
                   'status': 'unresolved', 'reason': 'Synthetic pending investigation.',
                   'authors': ['synthetic-integrator'], 'applications': [b.POLICY_ID], 'duplicate_of': None}
        result = self.prepare(findings=[finding], finding_bodies={finding['id']: body})
        self.assertEqual(result['packet.json']['findings'], [finding])


if __name__ == '__main__':
    unittest.main(verbosity=2)
