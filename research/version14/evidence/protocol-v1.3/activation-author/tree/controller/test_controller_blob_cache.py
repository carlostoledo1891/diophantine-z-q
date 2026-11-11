"""Immutable controller blob cache and safe quota diagnostics."""
import base64
import contextlib
import io
import json
import unittest
from unittest.mock import patch

import runtime as r
import quota_probe
from test_git_state import FakeGitHub


class Response:
    status = 200

    def __init__(self, value):
        self.body = r.canonical(value)
        self.headers = {'Content-Type': 'application/json', 'X-RateLimit-Limit': '1000',
                        'X-RateLimit-Remaining': '875', 'X-RateLimit-Reset': '1800000000'}

    def getheader(self, name, default=None):
        return self.headers.get(name, default)

    def read(self, limit):
        return self.body[:limit]


class BlobCacheTests(unittest.TestCase):
    def setUp(self):
        self.backend = FakeGitHub()
        self.api = r.ControllerHTTPS('owner/controller', 'never-print-this-token')
        self.calls = []
        self.response_transform = lambda response: response
        test = self

        class Connection:
            def __init__(self, *args, **kwargs):
                pass

            def request(self, method, path, body=None, headers=None):
                test.calls.append((method, path))
                value = test.backend.request(method, path, None if body is None else json.loads(body))
                response = Response(value)
                response.status = 201 if method == 'POST' else 200
                self.response = test.response_transform(response)

            def getresponse(self):
                return self.response

            def close(self):
                pass

        self.http = patch.object(r.http.client, 'HTTPSConnection', Connection)
        self.http.start()
        self.addCleanup(self.http.stop)

    def path(self, raw):
        return '/repos/owner/controller/git/blobs/' + self.backend.add_blob(raw)

    def test_two_stores_share_verified_blob_cache_and_keep_authoritative_reads(self):
        first = r.GitState(self.api, 'owner/controller', 42)
        second = r.GitState(self.api, 'owner/controller', 42)
        first.load()
        boundary = len(self.calls)
        second.load()
        later = self.calls[boundary:]
        self.assertFalse(any('/git/blobs/' in path for _, path in later))
        self.assertEqual(sum('/git/ref/' in path for _, path in later), 2)
        self.assertTrue(any('/git/commits/' in path for _, path in later))
        self.assertTrue(any('/git/trees/' in path for _, path in later))
        self.backend.private = False
        with self.assertRaises(r.Invalid):
            second.load()

    def test_six_state_reloads_fetch_each_of_101_blobs_once(self):
        seed = r.GitState(self.backend, 'owner/controller', 42)
        additions = {f'state/entries/operator/{n:010d}.json': r.canonical({'entry': n})
                     for n in range(1, 101)}
        seed.append(seed.load(), additions, {})
        stores = [r.GitState(self.api, 'owner/controller', 42) for _ in range(2)]
        for n in range(6):
            stores[n % 2].load()
        self.assertEqual(sum('/git/blobs/' in path for _, path in self.calls), 101)
        self.assertEqual(len(self.calls), 131)
        self.assertEqual(self.api.blob_cache_hits, 505)

    def test_returned_response_mutation_cannot_change_cached_bytes(self):
        path = self.path(b'original')
        first = self.api.request('GET', path)
        first['content'] = base64.b64encode(b'changed').decode()
        second = self.api.request('GET', path)
        self.assertEqual(base64.b64decode(second['content']), b'original')
        self.assertEqual(len(self.calls), 1)

    def test_malformed_blob_responses_never_enter_cache(self):
        path = self.path(b'original')
        for change in ({'sha': 'b' * 40}, {'size': True}, {'content': '!invalid!'},
                       {'content': base64.b64encode(b'changed').decode()}, {'encoding': 'utf8'}):
            with self.subTest(change=change):
                def transform(response):
                    body = json.loads(response.body)
                    body.update(change)
                    response.body = r.canonical(body)
                    return response
                self.response_transform = transform
                with self.assertRaises((r.Invalid, ValueError)):
                    self.api.request('GET', path)
                self.assertFalse(self.api.blob_cache)

    def test_strict_lru_byte_and_entry_limits(self):
        with patch.object(r, 'MAX_CONTROLLER_CACHE_BYTES', 6), \
             patch.object(r, 'MAX_CONTROLLER_CACHE_ENTRIES', 2):
            paths = [self.path(raw) for raw in (b'aaa', b'bbb', b'ccc', b'large!!')]
            self.api.request('GET', paths[0])
            self.api.request('GET', paths[1])
            self.api.request('GET', paths[0])
            self.api.request('GET', paths[2])
            self.assertEqual(list(self.api.blob_cache), [paths[0].rsplit('/', 1)[1], paths[2].rsplit('/', 1)[1]])
            self.assertEqual(self.api.blob_cache_bytes, 6)
            self.api.request('GET', paths[3])
            self.assertEqual(self.api.blob_cache_bytes, 6)
            for raw in (b'', b'x', b'y'):
                self.api.request('GET', self.path(raw))
            self.assertLessEqual(len(self.api.blob_cache), 2)
            self.assertEqual(self.api.blob_cache_bytes, sum(map(len, self.api.blob_cache.values())))

    def test_mutations_and_nonblob_paths_are_never_cached(self):
        for _ in range(2):
            self.api.request('POST', '/repos/owner/controller/git/blobs',
                             {'content': base64.b64encode(b'new').decode(), 'encoding': 'base64'})
            self.api.request('GET', '/repos/owner/controller/git/ref/heads/protocol-state')
        self.assertEqual(len(self.calls), 4)
        self.assertFalse(self.api.blob_cache)
        with self.assertRaises(r.Invalid):
            self.api.request('GET', self.path(b'x') + '?unsafe=1')
        with self.assertRaises(r.Invalid):
            self.api.request('GET', '/repos/other/controller/git/blobs/' + 'a' * 40)

    def test_quota_diagnostic_contains_only_numbers_and_counts(self):
        self.api.request('GET', self.path(b'x'))
        with contextlib.redirect_stderr(io.StringIO()) as stream:
            self.api.diagnostics()
        report = json.loads(stream.getvalue())
        self.assertEqual(report, {'controller_requests': 1, 'controller_blob_cache_hits': 0,
            'controller_rate_limit': 1000, 'controller_rate_remaining': 875,
            'controller_rate_reset': 1800000000})
        self.assertNotIn('never-print', stream.getvalue())

    def test_quota_probe_checks_owner_and_revision_with_two_fresh_reads(self):
        config = {'schema': 'protocol-controller/v1', 'controller_repository': 'owner/controller',
                  'controller_repository_id': 42, 'jobs': []}
        env = {'GITHUB_TOKEN': 'never-print-this-token', 'GITHUB_REPOSITORY': 'owner/controller',
               'GITHUB_REPOSITORY_ID': '42', 'GITHUB_REF': 'refs/heads/main',
               'GITHUB_SHA': 'a' * 40, 'PROTOCOL_APPROVED_SHA': 'a' * 40,
               'GITHUB_EVENT_NAME': 'workflow_dispatch'}
        original = self.backend.request
        def request(method, path, data=None):
            if path.endswith('/git/ref/heads/main'):
                return {'ref': 'refs/heads/main', 'object': {'type': 'commit', 'sha': 'a' * 40}}
            return original(method, path, data)
        with patch.object(r, 'read_protected_json', return_value=config), \
             patch.object(self.backend, 'request', side_effect=request), \
             patch.object(r, 'load_keys', side_effect=AssertionError('probe loaded keys')), \
             contextlib.redirect_stderr(io.StringIO()) as stream:
            self.assertEqual(quota_probe.main(env), 0)
        self.assertEqual(len(self.calls), 2)
        self.assertTrue(all(method == 'GET' for method, _ in self.calls))
        self.assertEqual(json.loads(stream.getvalue())['controller_rate_remaining'], 875)
        self.assertNotIn('never-print', stream.getvalue())
        env['GITHUB_SHA'] = 'b' * 40
        with patch.object(r, 'read_protected_json', return_value=config), \
             contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(r.Invalid):
                quota_probe.main(env)
        self.assertEqual(len(self.calls), 2)

    def test_main_failure_emits_sanitized_quota_diagnostic(self):
        config = {'schema': 'protocol-controller/v1', 'controller_repository': 'owner/controller',
                  'controller_repository_id': 42, 'jobs': [{'id': 'configured'}]}
        env = {'GITHUB_TOKEN': 'never-print-this-token'}
        with patch.object(r, 'read_protected_json', return_value=config), \
             contextlib.redirect_stderr(io.StringIO()) as stream:
            with self.assertRaises(KeyError):
                r.main(env)
        self.assertEqual(json.loads(stream.getvalue())['controller_requests'], 0)
        self.assertNotIn('never-print', stream.getvalue())


if __name__ == '__main__':
    unittest.main(verbosity=2)
