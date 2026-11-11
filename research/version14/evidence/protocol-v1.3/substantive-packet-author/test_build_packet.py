"""Synthetic local Git objects only. No real reviewer decisions are created."""
import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import build_packet as b


class BuilderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Synthetic fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.write(b.coverage.PROTOCOL_PATH, b'old synthetic protocol\n')
        self.write('proof.txt', b'Old synthetic argument.\n')
        self.base = self.commit('base fixture')
        self.write(b.coverage.PROTOCOL_PATH, (b.ADAPTER / 'PROTOCOL-V1.3.md').read_bytes())
        proof = b'New synthetic argument.\nAn explicit elementary step.\n'
        self.write('proof.txt', proof)
        source = {'side': 'head', 'path': 'proof.txt', 'sha256': b.core.sha(proof)}
        self.profile = {'schema': 'protocol-coverage-policy/v1', 'protocol_version': '1.3',
            'governing_protocol': {'path': b.coverage.PROTOCOL_PATH, 'sha256': b.coverage.PROTOCOL_SHA256},
            'runtime_policy_sha256': 'a' * 64, 'mode': 'substantive', 'claim_ids': ['math'],
            'proof_paths': ['proof.txt'], 'allowed_nonmath_paths': []}
        initial = {'schema': 'protocol-source-first/v1', 'sources': [source], 'uses': []}
        self.initial_path = 'docs/research-review/initial.json'
        self.dossier_path = 'docs/research-review/dossier.json'
        self.report_path = 'docs/research-review/report.md'
        initial_raw = b.core.canonical(initial)
        self.write(self.initial_path, initial_raw)
        dossier = {'schema': 'protocol-coverage/v1', 'profile_sha256': b.core.digest(self.profile),
            'mode': 'substantive', 'sources': [source], 'scope': 'Synthetic two-line proof fixture.',
            'coverage_index': [{'id': 'p1', 'claim_ids': ['math'], 'location': {'pin': source,
                'start_line': 1, 'end_line': 2, 'excerpt_sha256': b.core.sha(proof)},
                'status': 'reviewed', 'reason': 'Synthetic coverage record.', 'use_ids': [],
                'no_imports_reason': 'Synthetic proof has no imported assertion.'}],
            'initial': {'side': 'head', 'path': self.initial_path, 'sha256': b.core.sha(initial_raw)},
            'reconstruction': {'run_id': 'independent-fixture', 'method': 'Read fixture first.',
                'prior_exposure': 'None in this synthetic record.', 'limitations': 'Synthetic fixture only.',
                'frozen_at': '2026-11-01T00:00:00Z', 'compared_at': '2026-11-01T01:00:00Z'},
            'reconciled_uses': [], 'declared_edges_before': [], 'declared_edges': [], 'reconciliation': []}
        self.write(self.dossier_path, b.core.canonical(dossier))
        self.write(self.report_path, b'Synthetic report body. Not an actual review.\n')
        head = self.commit('head fixture')
        self.context = {'repository': 'fixture/repo', 'repository_id': 1, 'pr': 2, 'base': self.base, 'head': head}
        self.base_manifest = b.gm.collect(str(self.repo), self.base)
        self.head_manifest = b.gm.collect(str(self.repo), head)
        changed = sorted(p for p in set(self.base_manifest['files']) | set(self.head_manifest['files'])
                         if self.base_manifest['files'].get(p) != self.head_manifest['files'].get(p))
        def pin(side, path):
            manifest = self.base_manifest if side == 'base' else self.head_manifest
            return {'side': side, 'path': path, 'sha256': manifest['files'][path]['sha256']}
        apps = []
        changes = []
        for aid, kind, author, paths in [('math', 'argument', 'math-author', ['proof.txt']),
                                         ('policy', 'policy', 'policy-author', [p for p in changed if p != 'proof.txt'])]:
            pins = [pin(s, p) for s, m in [('base', self.base_manifest), ('head', self.head_manifest)]
                    for p in paths if p in m['files']]
            obligations = {key: {'status': 'checked', 'required': 'Synthetic requirement.',
                'constructed': 'Synthetic constructed item.', 'justification': 'Fixture authored claim only.',
                'evidence': [p for p in pins if p['side'] == 'head']} for key in b.core.OBLIGATIONS}
            apps.append({'id': aid, 'kind': kind, 'authors': [author], 'dependencies': [], 'files': pins, 'obligations': obligations})
            changes.extend({'path': p, 'kind': kind, 'applications': [aid],
                'base': self.base_manifest['files'].get(p), 'head': self.head_manifest['files'].get(p)} for p in paths)
        self.contract = {'schema': 'unsigned-research-release/v1', 'policy_sha256': 'a' * 64,
            'policy_paths': ['docs/research-review/'], 'changes': changes, 'applications': apps,
            'coverage_record': pin('head', self.dossier_path), 'coverage_author_runs': ['integrator'],
            'assembly_author_runs': ['math-author', 'policy-author', 'integrator', 'report-author']}
        report_entry = self.head_manifest['files'][self.report_path]
        self.reports = [{'path': self.report_path, 'sha256': report_entry['sha256'], 'bytes': report_entry['size'],
                         'author_runs': ['report-author'], 'scope': 'Actual bytes, synthetic report.'}]
        self.findings = []
        self.bodies = {}

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.repo), *args], env=b.gm.git_environment(), stderr=subprocess.DEVNULL)

    def write(self, path, raw):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)

    def commit(self, message):
        self.git('add', '.')
        self.git('-c', 'core.hooksPath=NUL', 'commit', '-qm', message)
        return self.git('rev-parse', 'HEAD').decode().strip()

    def build(self):
        return b.prepare(self.repo, self.context, self.contract, self.reports, self.findings, self.bodies, self.profile)

    def amend_json(self, path, change):
        value = json.loads((self.repo / path).read_bytes())
        change(value)
        self.write(path, b.core.canonical(value))
        self.context['head'] = self.commit('modified fixture')
        head = b.gm.collect(str(self.repo), self.context['head'])
        def refresh(value):
            if isinstance(value, dict):
                if set(value) == {'side', 'path', 'sha256'} and value['side'] == 'head':
                    value['sha256'] = head['files'][value['path']]['sha256']
                for child in value.values():
                    refresh(child)
            elif isinstance(value, list):
                for child in value:
                    refresh(child)
        refresh(self.contract)
        for row in self.contract['changes']:
            row['head'] = head['files'].get(row['path'])

    def test_unsigned_success_and_reserved_dependency_direction(self):
        out = self.build()
        apps = out['packet.json']['applications']
        self.assertEqual(apps[-1]['dependencies'], ['math', 'policy'])
        self.assertTrue(all(b.coverage.COVERAGE_ID not in a['dependencies'] for a in apps[:-1]))
        self.assertEqual(len(out['targets.json']), 4)
        self.assertTrue(all('decision' not in t and t['status'].startswith('awaiting') for t in out['targets.json']))
        self.assertFalse(out['PREPARATION.json']['receipts_created'])

    def test_missing_change_rejected(self):
        self.contract['changes'].pop()
        with self.assertRaisesRegex(b.core.Invalid, 'unlisted-or-missing-change'):
            self.build()

    def test_stale_reviewed_entry_rejected(self):
        self.contract['changes'][0]['head'] = dict(self.contract['changes'][0]['head'], sha256='0' * 64)
        with self.assertRaisesRegex(b.core.Invalid, 'reviewed-file-entry-changed'):
            self.build()

    def test_unknown_dependency_rejected(self):
        self.contract['applications'][0]['dependencies'] = ['absent']
        with self.assertRaisesRegex(b.core.Invalid, 'missing-ordinary-dependency'):
            self.build()

    def test_cycle_rejected(self):
        self.contract['applications'][0]['dependencies'] = ['policy']
        self.contract['applications'][1]['dependencies'] = ['math']
        with self.assertRaisesRegex(b.core.Invalid, 'cyclic'):
            self.build()

    def test_unindexed_source_line_rejected(self):
        def change(d):
            d['coverage_index'][0]['location']['end_line'] = 1
            d['coverage_index'][0]['location']['excerpt_sha256'] = b.core.sha(b'New synthetic argument.\n')
        self.amend_json(self.dossier_path, change)
        with self.assertRaisesRegex(b.core.Invalid, 'unindexed-proof-lines'):
            self.build()

    def test_stale_location_excerpt_rejected(self):
        self.amend_json(self.dossier_path, lambda d: d['coverage_index'][0]['location'].update(excerpt_sha256='0' * 64))
        with self.assertRaisesRegex(b.core.Invalid, 'stale-location-excerpt'):
            self.build()

    def test_reconstruction_wrong_chronology_rejected(self):
        self.amend_json(self.dossier_path, lambda d: d['reconstruction'].update(compared_at=d['reconstruction']['frozen_at']))
        with self.assertRaisesRegex(b.core.Invalid, 'reconstruction-chronology'):
            self.build()

    def test_missing_reconciliation_for_new_use_rejected(self):
        self.amend_json(self.dossier_path, lambda d: d['reconciled_uses'].append({'id': 'new-use'}))
        with self.assertRaisesRegex(b.core.Invalid, 'missing-reconciliation-row'):
            self.build()

    def test_missing_obligation_rejected(self):
        self.contract['applications'][0]['obligations'].pop('transition_maps')
        with self.assertRaisesRegex(b.core.Invalid, 'missing-obligation'):
            self.build()

    def test_stale_evidence_pin_rejected(self):
        self.contract['applications'][0]['files'][0]['sha256'] = '0' * 64
        with self.assertRaisesRegex(b.core.Invalid, 'stale-file-pin'):
            self.build()

    def test_no_reports_rejected(self):
        self.reports = []
        with self.assertRaisesRegex(b.core.Invalid, 'actual-report-manifest-required'):
            self.build()

    def test_stale_report_bytes_rejected(self):
        self.reports[0]['bytes'] += 1
        with self.assertRaisesRegex(b.core.Invalid, 'report-bytes-or-mode'):
            self.build()

    def test_missing_or_changed_profile_rejected(self):
        self.profile['governing_protocol']['sha256'] = '0' * 64
        with self.assertRaisesRegex(b.core.Invalid, 'unapproved-governing-protocol'):
            self.build()

    def test_incomplete_assembly_authors_rejected(self):
        self.contract['assembly_author_runs'].remove('report-author')
        with self.assertRaisesRegex(b.core.Invalid, 'incomplete-assembly-authors'):
            self.build()

    def test_reconstruction_author_conflict_rejected(self):
        self.contract['coverage_author_runs'] = ['independent-fixture']
        with self.assertRaisesRegex(b.core.Invalid, 'declared-coverage-reviewer-is-author'):
            self.build()

    def test_original_findings_and_unresolved_obligations_preserved(self):
        self.contract['applications'][0]['obligations']['transition_maps']['status'] = 'unresolved'
        body = 'An actual supplied unresolved fixture finding.'
        self.bodies = {'F': body}
        self.findings = [{'id': 'F', 'body_sha256': b.core.sha(body.encode()), 'status': 'unresolved',
            'reason': 'Still awaits disposition.', 'authors': ['math-author'], 'applications': ['math'], 'duplicate_of': None}]
        out = self.build()
        self.assertEqual(out['packet.json']['findings'], self.findings)
        self.assertEqual(out['packet.json']['applications'][0]['obligations']['transition_maps']['status'], 'unresolved')
        self.assertEqual(out['finding-bodies.json'], self.bodies)

    def test_changed_finding_body_rejected(self):
        self.bodies = {'F': 'wrong'}
        self.findings = [{'id': 'F', 'body_sha256': '0' * 64, 'status': 'unresolved', 'reason': 'Unresolved.',
            'authors': ['math-author'], 'applications': ['math'], 'duplicate_of': None}]
        with self.assertRaisesRegex(b.core.Invalid, 'changed-finding-body'):
            self.build()

    def test_output_escape_rejected(self):
        with self.assertRaisesRegex(b.core.Invalid, 'output-must-be-isolated'):
            b.write_outputs(self.repo, self.build())

    def test_cyclic_duplicate_findings_rejected(self):
        self.bodies = {'F1': 'First original finding.', 'F2': 'Second original finding.'}
        self.findings = [{'id': fid, 'body_sha256': b.core.sha(body.encode()), 'status': 'duplicate',
            'reason': 'Synthetic cycle.', 'authors': ['math-author'], 'applications': ['math'],
            'duplicate_of': 'F2' if fid == 'F1' else 'F1'} for fid, body in self.bodies.items()]
        with self.assertRaisesRegex(b.core.Invalid, 'cyclic'):
            self.build()

    def test_changed_application_requires_new_coverage_target(self):
        first = self.build()
        self.contract['applications'][0]['obligations']['transition_maps']['justification'] = 'Changed authored contract.'
        second = self.build()
        a = next(t for t in first['targets.json'] if t['target_id'] == b.coverage.COVERAGE_ID)
        c = next(t for t in second['targets.json'] if t['target_id'] == b.coverage.COVERAGE_ID)
        self.assertEqual(a['target_sha256'], c['target_sha256'])
        self.assertNotEqual(a['dependency_sha256'], c['dependency_sha256'])
        self.assertTrue(c['status'].startswith('awaiting'))

    def test_frozen_output_cannot_be_replaced(self):
        first = self.build()
        with tempfile.TemporaryDirectory(prefix='synthetic-output-', dir=b.HERE) as directory:
            output = Path(directory)
            b.write_outputs(output, first)
            raw = (output / 'packet.json').read_bytes()
            changed = copy.deepcopy(first)
            changed['packet.json']['pull_request'] += 1
            with self.assertRaisesRegex(b.core.Invalid, 'frozen-output-differs'):
                b.write_outputs(output, changed)
            self.assertEqual((output / 'packet.json').read_bytes(), raw)


if __name__ == '__main__':
    unittest.main(verbosity=2)
