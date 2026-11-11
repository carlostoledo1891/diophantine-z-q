"""Exercise generated renderer CLI against the frozen actual 309-page PDF."""
import ast
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import types
import unittest

import prepare_ci as ci
import release_common as common

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPO = ROOT / 'work/quartic-version6-release/repository'
BASE = '2125274b93314c9a9e51c7b47559025489565632'
PDF = ROOT / 'work/quartic-v14-release/preview-repository/build/paper/quartic_v14.pdf'
PDF_SHA = 'bebcfc92b11ee45c3302716859214b9feefab86480d941995b37eaa05d7a0ca5'

def module(text):
    result = types.ModuleType('renderer_fixture')
    result.__file__ = str(HERE / 'scripts/render_quartic_review.py')
    exec(compile(text, result.__file__, 'exec'), result.__dict__)
    return result

class RendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = common.blob(REPO, BASE, ci.RENDERER).decode()
        cls.new = ci.renderer(cls.old)
        cls.baseline = module(cls.old)
        cls.current = module(cls.new)

    def pages(self):
        pages = ['filler'] * 70
        for index, text in {
            12: 'This is the second final polynomial', 13: 'The finite checks do not replace',
            15: 'Arithmetic interfaces for the smaller quartic',
            17: 'The shared-point quartic in 962 variables',
            18: 'Why a single defining polynomial must have degree at least four',
            20: 'Dependency order in the arithmetic argument',
            25: 'Simultaneous primes with coprime adjacent norms',
            30: 'Gaussian ray weights and their progression main terms',
            45: 'A quartic presentation with 394 variables', 50: 'References',
            55: 'A quartic presentation with 299 variables', 60: 'References',
        }.items():
            pages[index] = text
        return pages

    def test_historical_automatic_routes_are_unchanged(self):
        for edition in ('v5', 'v6', 'v7', 'v8', 'v9', 'v12', 'v13'):
            with self.subTest(edition=edition):
                self.assertEqual(self.baseline.automatic_selection(self.pages(), edition),
                                 self.current.automatic_selection(self.pages(), edition))

    def test_v14_selects_299_heading_and_following_references(self):
        selected, groups = self.current.automatic_selection(self.pages(), 'v14')
        self.assertEqual(groups, {'front_matter': [0, 1, 2, 3], 'quartic_299': list(range(55, 61))})
        self.assertEqual(selected, [0, 1, 2, 3] + list(range(55, 61)))

    def test_missing_or_ambiguous_v14_heading_rejected(self):
        for where, text in [(55, 'missing'), (56, 'A quartic presentation with 299 variables')]:
            pages = self.pages()
            pages[where] = text
            with self.assertRaises(ValueError):
                self.current.automatic_selection(pages, 'v14')

    def test_v14_missing_following_references_rejected(self):
        pages = self.pages()
        pages[60] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Version 14 reference boundary'):
            self.current.automatic_selection(pages, 'v14')

    def test_changed_renderer_markers_are_rejected(self):
        with self.assertRaises(ValueError):
            ci.renderer(self.old.replace("default='v13'", "default='v12'"))

    def test_r3_paper_and_workflow_functions_preserved(self):
        def functions(text):
            return {n.name: ast.dump(n, include_attributes=False) for n in ast.parse(text).body if isinstance(n, ast.FunctionDef)}
        before = functions((HERE / 'history/r3/prepare_ci.py').read_text())
        after = functions(Path(ci.__file__).read_text())
        for name in ('paper', 'workflow'):
            self.assertEqual(before[name], after[name])

    def test_generated_cli_explicit_and_default_v14_on_final_pdf(self):
        self.assertEqual(hashlib.sha256(PDF.read_bytes()).hexdigest(), PDF_SHA)
        # Suppress optional-font warnings in this test process only. The real
        # script's parser/main and supported pypdf extraction still execute.
        wrapper = ('import logging,runpy,sys;logging.getLogger("pypdf").setLevel(logging.CRITICAL);'
                   'script=sys.argv.pop(1);sys.argv[0]=script;runpy.run_path(script,run_name="__main__")')
        with tempfile.TemporaryDirectory(prefix='renderer-regression-', dir=HERE) as temp:
            root = Path(temp)
            output = root / 'ci'
            subprocess.run([sys.executable, '-B', str(Path(ci.__file__)), '--repo', str(REPO),
                '--base', BASE, '--date', '2026-11-07', '--render-pages', '1,289-301',
                '--expected-pages', '309', '--output', str(output)], check=True, capture_output=True, text=True)
            manifest = json.loads((output / 'CI-PREPARATION.json').read_text())
            renderer = output / ci.RENDERER
            self.assertEqual(renderer.read_text(), self.new)
            self.assertEqual(manifest['files'][ci.RENDERER], hashlib.sha256(renderer.read_bytes()).hexdigest())
            self.assertIn('--edition v14 --pages 1,289-301 --expected-pages 309',
                          (output / ci.WORKFLOWS[1]).read_text())
            explicit = root / 'explicit'
            subprocess.run([sys.executable, '-B', '-c', wrapper, str(renderer), '--pdf', str(PDF), '--edition', 'v14',
                '--pages', '1,289-301', '--expected-pages', '309', '--select-only',
                '--pypdf', '--out', str(explicit)], check=True, capture_output=True, text=True)
            result = json.loads((explicit / 'rendered.json').read_text())
            self.assertEqual(result['pdf_sha256'], PDF_SHA)
            self.assertEqual(result['pages'], 309)
            self.assertEqual(result['selected_pages'], [1] + list(range(289, 302)))
            self.assertEqual(result['rendered_pages'], [])
            self.assertEqual(result['visual_inspection'], 'PENDING')
            # An omitted --pdf must resolve specifically to manuscripts/quartic_v14.pdf.
            target = output / 'manuscripts/quartic_v14.pdf'
            target.parent.mkdir()
            shutil.copyfile(PDF, target)
            automatic = root / 'automatic'
            subprocess.run([sys.executable, '-B', '-c', wrapper, str(renderer), '--edition', 'v14', '--expected-pages', '309',
                '--select-only', '--pypdf', '--out', str(automatic)],
                check=True, capture_output=True, text=True)
            auto = json.loads((automatic / 'rendered.json').read_text())
            self.assertEqual(auto['pdf_sha256'], PDF_SHA)
            self.assertEqual(auto['selection_method'], 'body headings')
            self.assertEqual(auto['section_pages']['front_matter'], [1, 2, 3, 4])
            self.assertTrue(auto['section_pages']['quartic_299'])
            self.assertGreater(auto['section_pages']['quartic_299'][0], 288)
            self.assertEqual(auto['rendered_pages'], [])
            print(json.dumps({'actual_pdf_regression': {'pdf_sha256': PDF_SHA, 'pages': 309,
                'explicit_pages': result['selected_pages'], 'automatic_sections': auto['section_pages'],
                'visual_inspection': 'PENDING; this test checks selection only'}}))

if __name__ == '__main__':
    unittest.main(verbosity=2)
