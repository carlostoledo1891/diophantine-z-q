import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

# Resolve from the project work directory, independent of the caller's cwd.
SOURCE = Path(__file__).resolve().parents[2] / 'quartic-v14-release' / 'preview-repository' / 'scripts' / 'build_paper.py'
spec = importlib.util.spec_from_file_location('candidate_build_paper', SOURCE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def http(code):
    return urllib.error.HTTPError('https://example.invalid/asset', code, 'mock failure', {}, None)

class RetryChecks(unittest.TestCase):
    def test_504_then_success(self):
        with patch.object(m.urllib.request, 'urlopen', side_effect=[http(504), io.BytesIO(b'pinned bytes')]) as op, patch.object(m.time, 'sleep') as sleep:
            self.assertEqual(m.download_archive('request'), b'pinned bytes')
            self.assertEqual(op.call_count, 2)
            self.assertEqual(op.call_args_list[1].kwargs, {'timeout': 60})
            sleep.assert_called_once_with(1)

    def test_404_is_not_retried(self):
        with patch.object(m.urllib.request, 'urlopen', side_effect=http(404)) as op, patch.object(m.time, 'sleep') as sleep:
            with self.assertRaises(urllib.error.HTTPError): m.download_archive('request')
            self.assertEqual(op.call_count, 1)
            sleep.assert_not_called()

    def test_exhaustion_is_bounded(self):
        with patch.object(m.urllib.request, 'urlopen', side_effect=http(503)) as op, patch.object(m.time, 'sleep') as sleep:
            with self.assertRaises(urllib.error.HTTPError): m.download_archive('request')
            self.assertEqual(op.call_count, 4)
            self.assertEqual([x.args for x in sleep.call_args_list], [(1,), (2,), (4,)])

    def test_url_error_and_timeout_recover(self):
        for error in [urllib.error.URLError('mock connection interruption'), TimeoutError('mock timeout')]:
            with self.subTest(error=type(error).__name__), patch.object(m.urllib.request, 'urlopen', side_effect=[error, io.BytesIO(b'ok')]) as op, patch.object(m.time, 'sleep'):
                self.assertEqual(m.download_archive('request'), b'ok')
                self.assertEqual(op.call_count, 2)

    def test_wrong_download_hash_is_never_cached(self):
        with tempfile.TemporaryDirectory() as td, patch.object(m, 'ROOT', Path(td)), patch.object(m.platform, 'system', return_value='Windows'), patch.object(m.platform, 'machine', return_value='amd64'), patch.object(m, 'download_archive', return_value=b'wrong archive'):
            with self.assertRaisesRegex(RuntimeError, '^Tectonic archive checksum mismatch$'): m.install()
            self.assertEqual(list(Path(td).rglob('*.zip')), [])
            self.assertEqual(list(Path(td).rglob('*.exe')), [])

    def test_wrong_cached_hash_is_rejected_without_download(self):
        with tempfile.TemporaryDirectory() as td, patch.object(m, 'ROOT', Path(td)), patch.object(m.platform, 'system', return_value='Windows'), patch.object(m.platform, 'machine', return_value='amd64'), patch.object(m, 'download_archive') as download:
            suffix = m.ASSETS[('Windows', 'amd64')][0]
            archive = Path(td) / '.tools' / ('tectonic-' + m.VERSION) / ('tectonic-' + m.VERSION + '-' + suffix)
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b'wrong cached archive')
            with self.assertRaisesRegex(RuntimeError, '^Cached Tectonic archive checksum mismatch$'): m.install()
            download.assert_not_called()
            self.assertEqual(list(Path(td).rglob('*.exe')), [])

if __name__ == '__main__': unittest.main(verbosity=2)
