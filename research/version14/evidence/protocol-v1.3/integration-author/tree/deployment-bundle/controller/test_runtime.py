"""Full signed-ledger/live-evaluator/publisher/CAS composition; fake HTTP only."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import runtime as r
from test_git_state import FakeGitHub
from test_live_protocol_context import LiveFixture
from test_live_integration import FixtureApp
import test_github_read_context as gh
from test_github_fork_context import forkify


class ControlAPI(FakeGitHub):
    main = 'a' * 40

    def request(self, method, path, data=None):
        if path == '/repos/owner/controller/git/ref/heads/main':
            return {'ref': 'refs/heads/main', 'object': {'type': 'commit', 'sha': self.main}}
        return super().request(method, path, data)


class ReadWriteFixtureApp(FixtureApp):
    root = gh.ROOT
    def get(self, path):
        return self.fixture.transport.get(path)


class RuntimeTests(LiveFixture):
    def setup_remote(self):
        self.transport.root = gh.ROOT
        forkify(self.p, self.transport)
        self.reader = r.github_fork_context.ForkReadContext(self.policy, self.transport)
        self.reader.api = r.CachingAPI(self.transport)
        self.recorder.github_reader = r.AuditObservationSource(self.reader)
        self.capture()
        self.control = ControlAPI()
        self.git = r.GitState(self.control, 'owner/controller', 42)
        self.environment = {'GITHUB_REPOSITORY': 'owner/controller', 'GITHUB_REPOSITORY_ID': '42',
            'GITHUB_REF': 'refs/heads/main', 'GITHUB_SHA': 'a'*40, 'GITHUB_EVENT_NAME': 'workflow_dispatch'}
        self.guard = r.RevisionGuard(self.control, 'owner/controller', 42, 'a'*40, self.environment)
        self.keys = {'operator': self.store.keys, 'intake': self.audit.keys,
                     'collector': {'collector': self.collector_key}}
        entries = {}
        checkpoints = {}
        for kind, store in (('operator', self.store), ('intake', self.audit)):
            log, cp, _ = store.read_verified()
            checkpoints[kind] = cp
            for e in log:
                entries[f"state/entries/{kind}/{e['sequence']:010d}.json"] = r.canonical(e)
        wrapper = {'schema': 'protocol-controller-generation/v1', 'controller_sha': None,
            'state': {'schema': 'protocol-publisher-state/v1', 'generations': [], 'targets': []},
            'publication': None}
        raw = r.canonical(wrapper)
        sha = r.digest(raw)
        entries['state/snapshots/'+sha+'.json'] = raw
        checkpoints['publisher'] = {'snapshot_sha256': sha}
        self.git.append(self.git.load(), entries, checkpoints)
        self.remote = r.RemoteState(self.git, self.guard)
        self.app = ReadWriteFixtureApp(self)
        self.config = r.publisher.Config('fixture/repo', 1, 42, 43, 'main', 'head')

    def key_environment(self):
        environment = {}
        for kind in ('operator', 'intake'):
            environment['PROTOCOL_' + kind.upper() + '_KEYS'] = json.dumps({
                key_id: {'operator_id': entry['operator_id'], 'secret_hex': entry['secret'].hex()}
                for key_id, entry in self.keys[kind].items()})
        environment['PROTOCOL_COLLECTOR_KEYS'] = json.dumps({
            key_id: secret.hex() for key_id, secret in self.keys['collector'].items()})
        return environment

    def test_real_secret_environment_to_signed_codecs_and_fork_publication(self):
        self.setup_remote()
        self.keys = r.load_keys(self.key_environment())
        # No fixtures bypass the production loader on this route. Both ledger
        # restore codecs and collector signature verification consume its output.
        result = self.execute()
        self.assertTrue(result['published_success'], result)
        self.assertTrue(all(path.startswith(gh.ROOT) for path in self.transport.calls))

    def test_real_publication_cache_hits_but_live_comments_reobserved(self):
        self.setup_remote()
        caches = []
        original = r.CachingAPI
        def cache(transport):
            value = original(transport)
            caches.append(value)
            return value
        with patch.object(r, 'CachingAPI', side_effect=cache):
            result = self.execute()
        self.assertTrue(result['published_success'], result)
        self.assertEqual(len(caches), 1)
        self.assertGreater(caches[0].statistics()['hits'], 0)
        comments = gh.ROOT+'/issues/7/comments?per_page=100&page=1'
        self.assertGreater(self.transport.calls.count(comments), 2)

    def test_warmed_cache_does_not_hide_comment_at_success_barrier(self):
        self.setup_remote()
        original = r.RemoteGenerationAuthority.before_success
        def changed(authority, *args):
            original(authority, *args)
            self.transport.routes[gh.ROOT+'/issues/7/comments?per_page=100&page=1'][0].append(
                {'id': 91235, 'body': 'new after cache warmed'})
        with patch.object(r.RemoteGenerationAuthority, 'before_success', changed):
            result = self.execute()
        self.assertFalse(result['published_success'])
        self.assertFalse(any(c.conclusion == 'success' for c in self.app.checks.values()))

    def test_key_attribution_change_fails_real_codec(self):
        self.setup_remote()
        environment = self.key_environment()
        registry = json.loads(environment['PROTOCOL_OPERATOR_KEYS'])
        for entry in registry.values():
            entry['operator_id'] = 'different-operator'
        environment['PROTOCOL_OPERATOR_KEYS'] = json.dumps(registry)
        self.keys = r.load_keys(environment)
        with self.assertRaises(r.operator_ledger.Invalid):
            self.execute()
        self.assertFalse(self.app.checks)

    def test_secret_schema_rejects_bare_hex_operator_or_intake(self):
        self.setup_remote()
        environment = self.key_environment()
        for kind in ('operator', 'intake'):
            malformed = dict(environment)
            malformed['PROTOCOL_' + kind.upper() + '_KEYS'] = json.dumps({'fixture': 'aa'*32})
            with self.subTest(kind=kind), self.assertRaises(r.Invalid):
                r.load_keys(malformed)

    def test_changed_pull_ref_blocks_fork_runtime(self):
        self.setup_remote()
        self.transport.routes[gh.ROOT+'/git/ref/pull/7/head'][0]['object']['sha'] = '9'*40
        result = self.execute()
        self.assertFalse(result['published_success'])
        self.assertFalse(any(c.conclusion == 'success' for c in self.app.checks.values()))

    def execute(self, suffix='first'):
        location = self.root / suffix
        location.mkdir()
        return r.evaluate(self.remote, location, (self.root/'candidate',), self.keys,
            self.config, self.app, self.p, self.selected, self.policy, self.collector_sha)

    def test_real_full_composition_and_ephemeral_restart(self):
        self.setup_remote()
        with patch('http.client.HTTPSConnection', side_effect=AssertionError('no network')):
            first = self.execute()
            self.assertTrue(first['published_success'], first)
            restored = r.RemoteState(self.git, self.guard)
            saved = restored.generation_snapshot()
            self.assertEqual(saved['generations'][0]['phase'], 'success')
            self.assertTrue(saved['targets'])
            self.remote = restored
            second = self.execute('second')
            self.assertTrue(second['published_success'], second)
            self.assertEqual(second['generation'], 2)
        wrappers = [r.decode_json(v) for k,v in self.git.load().entries.items() if k.startswith('state/snapshots/')]
        pending = [w for w in wrappers if w['publication'] is not None]
        self.assertEqual(len(pending), 2)
        self.assertTrue(all(w['state']['generations'][0]['phase'] == 'mutation_intent' for w in pending))
        self.assertTrue(all(w['publication']['target_sha'] == self.p['head']['commit'] for w in pending))

    def test_missing_selected_receipt_cannot_publish(self):
        self.setup_remote()
        self.selected.pop('assembly:complete')
        result = self.execute()
        self.assertFalse(result['published_success'], result)
        self.assertFalse(any(c.conclusion == 'success' for c in self.app.checks.values()))

    def test_signed_log_tamper_is_rejected_before_publisher(self):
        self.setup_remote()
        snapshot = self.git.load()
        path = 'state/entries/operator/0000000001.json'
        value = r.decode_json(snapshot.entries[path])
        value['signature'] = 'bad'
        # Simulate malicious but structurally valid state bootstrap, not append.
        raw = r.canonical(value)
        blob = self.control.add_blob(raw)
        files = dict(self.control.trees[snapshot.tree]); files[path] = blob
        index = copy.deepcopy(snapshot.index)
        index['files'][path] = {'blob': blob, 'sha256': r.digest(raw), 'size': len(raw)}
        index['parent'] = snapshot.commit
        files['state/index.json'] = self.control.add_blob(r.canonical(index))
        self.control.ref = self.control.add_commit(self.control.add_tree(files), [snapshot.commit])
        self.remote = r.RemoteState(self.git, self.guard)
        with self.assertRaises((r.Invalid, r.operator_ledger.Invalid)):
            self.execute()
        self.assertFalse(self.app.checks)

    def test_current_main_change_blocks_restoration(self):
        self.setup_remote()
        self.control.main = 'b'*40
        with self.assertRaisesRegex(r.Invalid, 'main ref changed'):
            self.execute()
        self.assertFalse(self.app.checks)

    def test_wrong_dispatch_ref_rejected(self):
        self.setup_remote()
        for field, value in [('GITHUB_REF','refs/heads/unreviewed'), ('GITHUB_SHA','b'*40),
                             ('GITHUB_EVENT_NAME','pull_request_target')]:
            env = dict(self.environment, **{field: value})
            with self.subTest(field=field), self.assertRaises(r.Invalid):
                r.RevisionGuard(self.control, 'owner/controller', 42, 'a'*40, env)

    def test_remote_advance_during_evaluation_blocks_success(self):
        self.setup_remote()
        original = self.app.get
        done = False
        def changed(path):
            nonlocal done
            if not done and '/git/blobs/' in path:
                done = True
                snap = self.git.load()
                self.git.append(snap, {}, snap.index['checkpoints'])
            return original(path)
        self.app.get = changed
        with self.assertRaisesRegex(r.Invalid, 'remote protocol state advanced'):
            self.execute()
        self.assertFalse(any(c.conclusion == 'success' for c in self.app.checks.values()))

    def test_new_live_comment_blocks_success(self):
        self.setup_remote()
        self.transport.routes[gh.ROOT+'/issues/7/comments?per_page=100&page=1'][0].append(
            {'id': 91234, 'body': 'new unresolved review'})
        result = self.execute()
        self.assertFalse(result['published_success'])
        self.assertFalse(any(c.conclusion == 'success' for c in self.app.checks.values()))


class BoundaryTests(unittest.TestCase):
    def test_control_token_never_targets_math_or_arbitrary_host(self):
        api = r.ControllerHTTPS('owner/controller', 'test-not-a-secret')
        for method, path in [('GET','/repos/owner/math'), ('POST','/repos/owner/controller/check-runs'),
                             ('GET','https://evil.invalid'), ('PATCH','/repos/owner/controller/git/refs/heads/main')]:
            with self.subTest(path=path), self.assertRaises(r.Invalid):
                api.request(method, path, None if method == 'GET' else {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
