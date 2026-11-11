import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from datetime import date

import prepare_manuscript as pm
import prepare_ci as ci
import release_common as common
import mirror_plan
import package_v14

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT / 'work/quartic-version6-release/repository'
BASE = '2125274b93314c9a9e51c7b47559025489565632'


class ReleaseTests(unittest.TestCase):
    def test_real_baseline_assembly_preserves_prior_body_and_register(self):
        raw = common.blob(REPO, BASE, common.V13_TEX)
        register = json.loads(common.blob(REPO, BASE, common.REGISTER))
        result, edits, new = pm.assemble_manuscript(raw, b'\\section{Synthetic fixture}\\label{sec:v14}\n', 'November 7, 2026', 264430, register)
        self.assertIn(b'264\\,430', result)
        self.assertIn(b'2^{6496}', result)
        self.assertIn(b'186624\\cdot3^{2^{26}}', result)
        self.assertEqual(edits[:len(register['edits'])], register['edits'])
        self.assertEqual(raw.count(b'\\label{sec:v13}'), result.count(b'\\label{sec:v13}'))
        self.assertEqual(len(new), 4)
        title = next(edit for edit in new if edit['id'] == 'v14-title')
        self.assertEqual(title, {'id': 'v14-title', 'old': r'\large Version 13',
                                'new': r'\large Version 14', 'kind': 'administrative'})
        self.assertNotIn('}', title['old'])
        replay = raw.decode('utf-8')
        for edit in new:
            self.assertEqual(replay.count(edit['old']), 1)
            replay = replay.replace(edit['old'], edit['new'], 1)
        self.assertEqual(replay.encode('utf-8'), result)

    def test_missing_addition_label_rejected(self):
        with self.assertRaises(ValueError):
            pm.assemble_manuscript(b'', b'no label', 'November 7, 2026', 1, {})

    def test_actual_canonical_table_and_missing_extra_terms(self):
        path = ROOT / 'work/quartic-v14-prep/quartic-299-314/quartic-314-ordinary-coefficients.txt'
        raw = path.read_bytes()
        pm.validate_decimal_table(raw, 6672)
        rows = raw.splitlines(keepends=True)
        with self.assertRaises(ValueError):
            pm.validate_decimal_table(b''.join(rows[:-1]), 6672)
        with self.assertRaises(ValueError):
            pm.validate_decimal_table(raw + rows[-1], 6672)

    def test_bad_coefficient_coordinate_or_power(self):
        for row in (b'0 | 0 | 1\n', b'1 | 1 | 1\n', b'1 | 0 | 315\n', b'1 | 0 | 2,1\n'):
            with self.assertRaises(ValueError):
                pm.validate_decimal_table(row, 1)

    def test_current_navigation_and_exact_protocol_bytes(self):
        get = lambda name: common.blob(REPO, BASE, name)
        files = pm.navigation(get, 'November 7, 2026', 264430)
        pm.add_protocol(files, ROOT/'work/protocol-v13-20261107/docs-author/r3', REPO, BASE)
        self.assertEqual(common.sha(files[pm.PROTOCOL_PATH]), 'd3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a')
        self.assertIn(b'Version 14', files['README.md'])
        self.assertIn(b'Protocol v1.3', files['README.md'])
        self.assertIn(b'264,430', files['README.md'])
        self.assertIn(b'| Version 13, decimal table | 411', files['README.md'])
        self.assertIn(b'Gabriel Conant with ChatGPT', files['README.md'])
        self.assertIn(b'| 13 | [PDF](quartic_v13.pdf)', files['manuscripts/README.md'])

    def test_ci_retains_required_job_names_and_old_replays(self):
        for path in ci.WORKFLOWS:
            raw = common.blob(REPO, BASE, path).decode()
            render = ('1,276-300', 308) if path.endswith('manuscript-integration.yml') else None
            result = ci.workflow(raw, render)
            self.assertIn('Version 13 source and quartic replay (${{ matrix.os }})', result)
            self.assertIn(ci.REPLAY, result)
            self.assertIn(ci.INVENTORY, result)
            self.assertIn('python -B scripts/check_quartic394_portable.py', result)

    def test_build_paper_pin_preservation(self):
        raw = common.blob(REPO, BASE, ci.PAPER).decode()
        result = ci.paper(raw, date(2026, 11, 7))
        self.assertIn('quartic_v14.pdf', result)
        for line in raw.splitlines():
            if 'DIGEST' in line or '0.17.0' in line:
                self.assertIn(line, result)

    def test_unsafe_paths_and_missing_selection_rejected(self):
        for path in ('../x', 'C:/x', 'a\\b', 'a//b', 'a/CON.txt', 'a./x'):
            with self.assertRaises(ValueError):
                common.safe(path)
        with self.assertRaises(ValueError):
            package_v14.collect(REPO, BASE, {})

    def test_mirror_exact_preimages_and_wrong_allowlist(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            def git(*args):
                return subprocess.check_output(['git', '-C', str(repo), *args]).decode().strip()
            git('init', '-q'); git('config', 'user.name', 'Synthetic test'); git('config', 'user.email', 'fixture@example.invalid')
            (repo/'file.txt').write_bytes(b'old\n'); git('add', '.'); git('commit', '-qm', 'fixture base')
            base = git('rev-parse', 'HEAD')
            (repo/'file.txt').write_bytes(b'new\n'); git('add', '.'); git('commit', '-qm', 'fixture head')
            head = git('rev-parse', 'HEAD')
            files = mirror_plan.plan(repo, repo, base, head, base, {'file.txt': common.sha(b'new\n')})
            self.assertEqual(files, {'file.txt': b'new\n'})
            (repo/'archive-receipt.txt').write_bytes(b'synthetic archive receipt\n')
            git('add', '.'); git('commit', '-qm', 'fixture archive commit')
            final_head = git('rev-parse', 'HEAD')
            allow = {'file.txt': common.sha(b'new\n'), 'archive-receipt.txt': common.sha(b'synthetic archive receipt\n')}
            final_files = mirror_plan.plan(repo, repo, base, final_head, base, allow)
            self.assertEqual(set(final_files), set(allow))
            with self.assertRaises(ValueError):
                mirror_plan.plan(repo, repo, final_head, head, base, allow)

            with self.assertRaises(ValueError):
                mirror_plan.plan(repo, repo, base, head, head, {'file.txt': common.sha(b'new\n')})
            with self.assertRaises(ValueError):
                mirror_plan.plan(repo, repo, base, head, base, {})


if __name__ == '__main__':
    unittest.main()

class HandoffTests(unittest.TestCase):
    def test_deterministic_archive_and_safe_restore(self):
        import io
        import zipfile
        import restore
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = {'old.txt': b'old'}
            files['MANIFEST.json'] = common.json_bytes({'files': {'old.txt': common.sha(b'old')}})
            base = root/'base.zip'
            package_v14.write_archive(base, files, date(2026, 11, 7))
            current = {'version13-base.zip': base.read_bytes(),
                'restore.py': Path(restore.__file__).read_bytes(), 'current/new.txt': b'new'}
            current['MANIFEST.json'] = common.json_bytes({'files': {k: common.sha(v) for k, v in current.items()}})
            a, b = root/'a.zip', root/'b.zip'
            package_v14.write_archive(a, current, date(2026, 11, 7))
            package_v14.write_archive(b, current, date(2026, 11, 7))
            self.assertEqual(a.read_bytes(), b.read_bytes())
            checked, manifest = restore.checked_zip(a.read_bytes())
            extracted = root/'extract'
            with checked:
                for name in checked.namelist():
                    common.put(extracted, name, checked.read(name))
            subprocess.run([__import__('sys').executable, '-B', str(extracted/'restore.py'), str(root/'restored')], check=True, capture_output=True)
            self.assertEqual((root/'restored/old.txt').read_bytes(), b'old')
            self.assertEqual((root/'restored/new.txt').read_bytes(), b'new')
            self.assertEqual((root/'restored'/common.V13_ARCHIVE).read_bytes(), base.read_bytes())

    def test_unsafe_zip_rejected(self):
        import io
        import zipfile
        import restore
        raw = io.BytesIO()
        with zipfile.ZipFile(raw, 'w') as archive:
            archive.writestr('../escape', b'x')
        with self.assertRaises(ValueError):
            restore.checked_zip(raw.getvalue())


class CoverageSelectionTests(unittest.TestCase):
    def test_all_protocol_docs_are_required(self):
        self.assertTrue(package_v14.PROTOCOL_DOCUMENTS <= package_v14.REQUIRED)
        self.assertEqual(len(package_v14.PROTOCOL_DOCUMENTS), 6)

    def test_actual_role_paths_are_required_and_included(self):
        roles = {'coverage': ['coverage.json'], 'profiles': ['profile.json'], 'evidence': ['review.md']}
        selected = {name: '0'*64 for names in roles.values() for name in names}
        self.assertEqual(package_v14.coverage_paths(roles, selected), set(selected))
        for broken in (None, {}, {**roles, 'profiles': []}, {**roles, 'evidence': ['missing.md']}):
            with self.assertRaises(ValueError):
                package_v14.coverage_paths(broken, selected)
