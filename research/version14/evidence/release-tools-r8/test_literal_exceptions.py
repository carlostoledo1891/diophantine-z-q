from pathlib import Path
import json
import unittest
from unittest.mock import patch
import package_v14

ROOT = Path(__file__).resolve().parents[2]
MARKER = b'-----BEGIN ' + b'PRIVATE KEY-----'

class LiteralExceptionTests(unittest.TestCase):
    def source_rows(self):
        rows = json.loads((ROOT / 'work/quartic-v14-prep/direct-history-install/INSTALLATION.json').read_bytes())['files']
        allowed = json.loads(Path(__file__).with_name('reviewed-literal-files.json').read_bytes())
        return [(row['path'], (ROOT / row['source_workspace_path']).read_bytes())
                for row in rows if row['path'] in allowed]

    def test_five_exact_reviewed_sources_pass(self):
        rows = self.source_rows()
        self.assertEqual(len(rows), 5)
        for name, raw in rows:
            package_v14.check_private_key_markers(name, raw)

    def test_changed_byte_fails(self):
        for name, raw in self.source_rows():
            with self.assertRaises(ValueError):
                package_v14.check_private_key_markers(name, raw + b' ')

    def test_appended_key_fails(self):
        sample = MARKER + b'\nQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB\n' + b'-----END PRIVATE KEY-----\n'
        for name, raw in self.source_rows():
            with self.assertRaises(ValueError):
                package_v14.check_private_key_markers(name, raw + sample)

    def test_renamed_source_fails(self):
        for name, raw in self.source_rows():
            with self.assertRaises(ValueError):
                package_v14.check_private_key_markers(name + '.other', raw)

    def test_unlisted_marker_source_fails(self):
        with self.assertRaises(ValueError):
            package_v14.check_private_key_markers('other.py', b'x = ' + repr(MARKER).encode())

    def test_key_at_reviewed_path_fails(self):
        name, _ = self.source_rows()[0]
        with self.assertRaises(ValueError):
            package_v14.check_private_key_markers(name, MARKER + b'\nQUFBQUFBQUFBQUFB\n')

    def test_changed_allowlist_fails(self):
        name, raw = self.source_rows()[0]
        with patch.object(package_v14.Path, 'read_bytes', return_value=b'{}'):
            with self.assertRaises(ValueError):
                package_v14.check_private_key_markers(name, raw)

    def test_ordinary_bytes_pass(self):
        package_v14.check_private_key_markers('proof.py', b'assert 2 + 2 == 4\n')

if __name__ == '__main__':
    unittest.main()
