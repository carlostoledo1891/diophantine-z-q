"""Bounded independent tests for the Version 13 path adapter.

No historical source is edited, no network is used, and child commands are
mocked here. The complete unchanged replay remains a separate CI requirement.
"""
from pathlib import Path
from types import SimpleNamespace
from unittest import mock
import builtins
import hashlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


bootstrap = load('quartic394_path_bootstrap')
launcher = load('check_quartic394_portable')


class PortabilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='quartic394-path-test-')
        self.addCleanup(self.temp.cleanup)
        # Match the mapper's canonical paths even when TEMP uses an alias.
        self.packet = (Path(self.temp.name) / 'packet').resolve()
        self.sources = self.packet / 'sources'
        self.target = self.sources / 'work' / 'nested' / 'input.json'
        self.target.parent.mkdir(parents=True)
        self.target.write_bytes(b'{"value":42}')
        self.relative = 'work/nested/input.json'
        self.prefix = r'C:\Historical\workspace'
        self.manifest = {self.relative: {'bytes': self.target.stat().st_size}}
        self.map = bootstrap.make_mapper(self.packet, self.prefix, self.manifest)

    def test_historical_separator_forms(self):
        path = self.prefix + '\\' + self.relative.replace('/', '\\')
        for value in [path, path.replace('\\', '/'), path.encode(), Path(path)]:
            with self.subTest(value=value):
                self.assertEqual(self.map(value), self.target.resolve())

    def test_nonhistorical_paths_and_file_descriptors_are_unchanged(self):
        for value in [3, self.target, str(self.target), 'relative/file',
                      self.prefix + '-sibling/file', 'C:/Other/work/input.json']:
            with self.subTest(value=value):
                self.assertIs(self.map(value), value)

    def test_current_packet_under_historical_root_is_not_remapped(self):
        remap = bootstrap.make_mapper(self.packet, str(self.packet.parent), self.manifest)
        current = str(self.target.resolve())
        self.assertIs(remap(current), current)

    def test_unsafe_or_unlisted_descendants_rejected(self):
        (self.sources / 'unlisted.json').write_bytes(b'{}')
        for suffix in ['', '/work/../nested/input.json', '/work/./nested/input.json',
                       '//work/nested/input.json', '/work//nested/input.json',
                       '/work/nested/input.json:stream', '/work/nested/\x00input',
                       '/unlisted.json', '/missing.json']:
            with self.subTest(suffix=suffix):
                with self.assertRaises(ValueError):
                    self.map(self.prefix + suffix)

    def test_missing_manifest_member_rejected(self):
        remap = bootstrap.make_mapper(self.packet, self.prefix, {'missing.json': {}})
        with self.assertRaises(ValueError):
            remap(self.prefix + '/missing.json')

    def test_child_symbolic_link_rejected(self):
        original = Path.is_symlink
        def linked(path):
            return path == self.sources / 'work' or original(path)
        with mock.patch.object(Path, 'is_symlink', linked):
            with self.assertRaises(ValueError):
                self.map(self.prefix + '/' + self.relative)

    def test_sources_root_symbolic_link_rejected(self):
        original = Path.is_symlink
        def linked(path):
            return path == self.sources or original(path)
        with mock.patch.object(Path, 'is_symlink', linked):
            with self.assertRaises(ValueError):
                remap = bootstrap.make_mapper(self.packet, self.prefix, self.manifest)
                remap(self.prefix + '/' + self.relative)

    def test_bootstrap_uses_driver_and_restores_hooks_on_failure(self):
        (self.packet / 'VERIFICATION-PLAN.json').write_text(json.dumps({'originalRoot': self.prefix}))
        (self.packet / 'SOURCE-MANIFEST.json').write_text(json.dumps(self.manifest))
        before = builtins.open, io.open, sys.argv
        class Stop(Exception):
            pass
        def driver(path, run_name):
            self.assertEqual(path, str(self.packet / 'verify_lineage.py'))
            self.assertEqual(run_name, '__main__')
            self.assertEqual(sys.argv, [path])
            historical = self.prefix + '/' + self.relative
            with builtins.open(historical, 'rb') as stream:
                self.assertEqual(stream.read(), b'{"value":42}')
            with io.open(historical, 'rb') as stream:
                self.assertEqual(stream.read(), b'{"value":42}')
            raise Stop()
        with mock.patch.object(bootstrap, 'PACKET', self.packet), mock.patch.object(bootstrap.runpy, 'run_path', driver):
            with self.assertRaises(Stop):
                bootstrap.main()
        self.assertIs(builtins.open, before[0])
        self.assertIs(io.open, before[1])
        self.assertIs(sys.argv, before[2])

    def test_subprocess_command_and_options_preserved(self):
        expected = [sys.executable, '-X', 'utf8', '-B', str(launcher.PACKET / 'verify_lineage.py')]
        adapted = [sys.executable, '-X', 'utf8', '-B', str(ROOT / 'scripts/quartic394_path_bootstrap.py')]
        marker = object()
        with mock.patch.object(launcher.subprocess, 'run', return_value=marker) as run:
            self.assertIs(launcher.portable_run(expected, cwd=launcher.PACKET, check=True), marker)
            run.assert_called_once_with(adapted, cwd=launcher.PACKET, check=True)
        invalid = [(expected + ['extra'], {'cwd': launcher.PACKET, 'check': True}),
                   (expected, {'cwd': launcher.PACKET, 'check': False}),
                   (expected, {'cwd': launcher.PACKET.parent, 'check': True}),
                   (expected, {'cwd': launcher.PACKET, 'check': True, 'shell': True}),
                   (expected, {'check': True})]
        for command, kwargs in invalid:
            with self.subTest(command=command, kwargs=kwargs):
                with mock.patch.object(launcher.subprocess, 'run') as run:
                    with self.assertRaises(ValueError):
                        launcher.portable_run(command, **kwargs)
                    run.assert_not_called()

    def test_original_main_is_called_and_binding_restored(self):
        original_process = object()
        original = SimpleNamespace(subprocess=original_process)
        class Stop(Exception):
            pass
        def main():
            self.assertIs(original.subprocess.run, launcher.portable_run)
            raise Stop()
        original.main = main
        spec = SimpleNamespace(loader=SimpleNamespace(exec_module=lambda module: None))
        with mock.patch.object(launcher.importlib.util, 'spec_from_file_location', return_value=spec), \
             mock.patch.object(launcher.importlib.util, 'module_from_spec', return_value=original):
            with self.assertRaises(Stop):
                launcher.main()
        self.assertIs(original.subprocess, original_process)

    def test_changed_original_wrapper_rejected_before_import(self):
        with mock.patch.object(Path, 'read_bytes', return_value=b'changed wrapper'), \
             mock.patch.object(launcher.importlib.util, 'spec_from_file_location') as loader:
            with self.assertRaises(ValueError):
                launcher.main()
            loader.assert_not_called()

    def test_frozen_wrapper_and_packet_unchanged(self):
        sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
        self.assertEqual(sha(ROOT / 'scripts/check_quartic394.py'),
                         'faa43aab6431a9cb7ae14f92a47f649c494825ea5f3d56e798d73ad41e59ebd0')
        packet = ROOT / 'quartics/quartic-394-411'
        self.assertEqual(sha(packet / 'PACKAGE-MANIFEST.json'),
                         'b3bc37df3fcb06d622808d3a23741d602b27c0ff0b2179ad28ef313a8489fe22')
        manifest = json.loads((packet / 'PACKAGE-MANIFEST.json').read_bytes())
        self.assertEqual(len(manifest), 400)
        for name, entry in manifest.items():
            with self.subTest(file=name):
                path = packet / name
                self.assertEqual(path.stat().st_size, entry['bytes'])
                self.assertEqual(sha(path), entry['sha256'])
        sources = json.loads((packet / 'SOURCE-MANIFEST.json').read_bytes())
        self.assertEqual(len(sources), 382)


if __name__ == '__main__':
    unittest.main(verbosity=2)
