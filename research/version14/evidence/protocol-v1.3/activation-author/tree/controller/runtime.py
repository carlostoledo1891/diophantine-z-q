"""Isolated controller composition. Candidate trees are read as data only.

The remote protocol-state ref is authoritative. Local SQLite files are disposable
verified mirrors, never rollback anchors. No candidate command is executed.
"""
from __future__ import annotations

import base64
from collections import OrderedDict
import copy
import hashlib
import http.client
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
for name in ('adapter', 'publisher', 'immutable-cache'):
    sys.path.insert(0, str(ROOT / name))

from git_state import GitState, Invalid, Conflict, canonical, decode_json, oid, object_id
import app_publisher as publisher
from generation_state import SQLiteGenerationState, StaleGeneration
from protected_ledger_store import ProtectedPath
from restore_verified_stores import restore_operator_store, restore_audit_store
from durable_intake import IntakeRecorder, AuditObservationSource
import github_read_context as github
import github_fork_context
import live_protocol_context_forks
import operator_ledger
import audit_intake
import coverage_gate
from immutable_git_cache import CachingAPI

MAX_INPUT = 40 * 1024 * 1024
MAX_ENTRIES = 20_000
MAX_JOBS = 100
MAX_CONTROLLER_CACHE_BYTES = 64 * 1024 * 1024
MAX_CONTROLLER_CACHE_ENTRIES = 4096


def require(ok, message):
    if not ok:
        raise Invalid(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def exact(value, fields, message):
    require(type(value) is dict and set(value) == set(fields.split()), message)


class ControllerHTTPS:
    """GITHUB_TOKEN transport restricted to one private controller Git store."""
    def __init__(self, repository, token):
        require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) is not None,
                'invalid controller repository')
        require(type(token) is str and token and all(32 < ord(c) < 127 for c in token),
                'invalid controller credential')
        self.root = '/repos/' + repository
        self._token = token
        self.requests = 0
        self.blob_cache = OrderedDict()
        self.blob_cache_bytes = 0
        self.blob_cache_hits = 0
        self.rate_limit = None
        self.rate_remaining = None
        self.rate_reset = None

    def diagnostics(self):
        # Emit only nonsecret counters and the server's numeric quota headers.
        print(json.dumps({'controller_requests': self.requests,
            'controller_blob_cache_hits': self.blob_cache_hits,
            'controller_rate_limit': self.rate_limit,
            'controller_rate_remaining': self.rate_remaining,
            'controller_rate_reset': self.rate_reset}, sort_keys=True), file=sys.stderr)

    @staticmethod
    def blob_response(sha, raw):
        return {'sha': sha, 'size': len(raw), 'encoding': 'base64',
                'content': base64.b64encode(raw).decode('ascii')}

    def cache_blob(self, sha, value):
        require(value.get('sha') == sha and value.get('encoding') == 'base64' and
                type(value.get('size')) is int and 0 <= value['size'] <= MAX_INPUT,
                'invalid controller blob response')
        content = value.get('content')
        require(type(content) is str and len(content) <= 2 * MAX_INPUT,
                'invalid controller blob content')
        raw = base64.b64decode(''.join(content.split()), validate=True)
        require(len(raw) == value['size'] and object_id('blob', raw) == sha,
                'controller blob identity mismatch')
        if len(raw) <= MAX_CONTROLLER_CACHE_BYTES:
            while self.blob_cache and (self.blob_cache_bytes + len(raw) > MAX_CONTROLLER_CACHE_BYTES or
                                      len(self.blob_cache) >= MAX_CONTROLLER_CACHE_ENTRIES):
                _, evicted = self.blob_cache.popitem(last=False)
                self.blob_cache_bytes -= len(evicted)
            self.blob_cache[sha] = raw
            self.blob_cache_bytes += len(raw)
        return self.blob_response(sha, raw)

    def request(self, method, path, data=None):
        allowed = {
            'GET': r'(?:|/git/ref/heads/(?:main|protocol-state)|/git/(?:commits|blobs)/[0-9a-f]{40}|/git/trees/[0-9a-f]{40}\?recursive=1)',
            'POST': r'/git/(?:blobs|trees|commits)',
            'PATCH': r'/git/refs/heads/protocol-state',
        }
        require(method in allowed and type(path) is str and path.startswith(self.root) and
                re.fullmatch(allowed[method], path[len(self.root):]) is not None,
                'controller endpoint outside allowed Git operations')
        require((method == 'GET') == (data is None), 'invalid request body')
        blob_sha = path.rsplit('/', 1)[-1] if method == 'GET' and path.startswith(self.root + '/git/blobs/') else None
        if blob_sha in self.blob_cache:
            raw_blob = self.blob_cache.pop(blob_sha)
            self.blob_cache[blob_sha] = raw_blob
            self.blob_cache_hits += 1
            return self.blob_response(blob_sha, raw_blob)
        self.requests += 1
        require(self.requests <= 100_000, 'controller request budget exceeded')
        raw = None if data is None else canonical(data)
        require(raw is None or len(raw) <= 2 * MAX_INPUT, 'controller request too large')
        headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28',
                   'User-Agent': 'research-review-controller/1',
                   'Authorization': 'Bearer ' + self._token}
        if raw is not None:
            headers['Content-Type'] = 'application/json'
        connection = http.client.HTTPSConnection('api.github.com', timeout=30)
        try:
            connection.request(method, path, body=raw, headers=headers)
            response = connection.getresponse()
            for header, attribute in (('X-RateLimit-Limit', 'rate_limit'),
                                      ('X-RateLimit-Remaining', 'rate_remaining'),
                                      ('X-RateLimit-Reset', 'rate_reset')):
                value = response.getheader(header)
                setattr(self, attribute, int(value) if type(value) is str and
                        re.fullmatch(r'[0-9]{1,19}', value) else None)
            require(response.status == (201 if method == 'POST' else 200),
                    'controller Git request failed')
            require(response.getheader('Content-Encoding', 'identity') == 'identity' and
                    'application/json' in response.getheader('Content-Type', '') and
                    not response.getheader('Link'), 'invalid controller response')
            body = response.read(2 * MAX_INPUT + 1)
            require(len(body) <= 2 * MAX_INPUT, 'controller response too large')
            result = decode_json(body)
            require(type(result) is dict, 'controller API object required')
            return self.cache_blob(blob_sha, result) if blob_sha is not None else result
        except Invalid:
            raise
        except Exception:
            raise Invalid('controller transport failed') from None
        finally:
            connection.close()


class RevisionGuard:
    def __init__(self, api, repository, repository_id, approved_sha, environment):
        require(oid(approved_sha), 'explicit approved controller SHA required')
        require(environment.get('GITHUB_REPOSITORY') == repository and
                environment.get('GITHUB_REPOSITORY_ID') == str(repository_id) and
                environment.get('GITHUB_REF') == 'refs/heads/main' and
                environment.get('GITHUB_SHA') == approved_sha and
                environment.get('GITHUB_EVENT_NAME') in ('workflow_dispatch', 'schedule'),
                'run is not the approved controller main revision')
        self.api = api
        self.repository = repository
        self.repository_id = repository_id
        self.approved_sha = approved_sha

    def check(self):
        root = '/repos/' + self.repository
        repo = self.api.request('GET', root)
        require(type(repo.get('id')) is int and repo['id'] == self.repository_id and
                repo.get('full_name') == self.repository and repo.get('private') is True,
                'controller identity or privacy changed')
        ref = self.api.request('GET', root + '/git/ref/heads/main')
        require(ref.get('ref') == 'refs/heads/main' and
                ref.get('object', {}).get('type') == 'commit' and
                ref.get('object', {}).get('sha') == self.approved_sha,
                'approved controller main ref changed')


class RemoteState:
    """Single run's CAS cursor. Unexpected remote advances invalidate the run."""
    def __init__(self, store, guard):
        self.store = store
        self.guard = guard
        guard.check()
        self.current = store.load()
        exact(self.current.index['checkpoints'], 'operator intake publisher', 'invalid remote checkpoint set')

    def check(self):
        self.guard.check()
        require(self.store.tip() == self.current.commit, 'remote protocol state advanced')

    def advance(self, additions, checkpoints):
        self.check()
        commit = self.store.append(self.current, additions, checkpoints)
        self.current = self.store.load()
        require(self.current.commit == commit, 'remote state advanced after CAS')
        self.check()

    def generation_snapshot(self):
        pointer = self.current.index['checkpoints']['publisher']
        exact(pointer, 'snapshot_sha256', 'invalid publisher pointer')
        sha = pointer['snapshot_sha256']
        require(type(sha) is str and re.fullmatch('[0-9a-f]{64}', sha), 'invalid snapshot digest')
        path = 'state/snapshots/' + sha + '.json'
        require(path in self.current.entries, 'publisher snapshot missing')
        raw = self.current.entries[path]
        require(digest(raw) == sha, 'publisher snapshot digest mismatch')
        value = decode_json(raw)
        require(canonical(value) == raw, 'noncanonical publisher snapshot')
        exact(value, 'schema controller_sha state publication', 'invalid publisher snapshot wrapper')
        require(value['schema'] == 'protocol-controller-generation/v1' and
                (value['controller_sha'] is None or oid(value['controller_sha'])) and
                (value['publication'] is None or type(value['publication']) is dict),
                'invalid publisher snapshot wrapper fields')
        return value['state']

    def entries(self, kind, codec, keys):
        checkpoint = self.current.index['checkpoints'][kind]
        codec.check_checkpoint(checkpoint)
        count = checkpoint['sequence']
        require(count <= MAX_ENTRIES, 'ledger entry count exceeds limit')
        prefix = 'state/entries/' + kind + '/'
        expected = [prefix + f'{n:010d}.json' for n in range(1, count + 1)]
        require(set(expected) == {p for p in self.current.entries if p.startswith(prefix)},
                'remote ledger inventory differs from checkpoint')
        entries = []
        for path in expected:
            raw = self.current.entries[path]
            entry = decode_json(raw)
            require(canonical(entry) == raw, 'noncanonical ledger entry')
            entries.append(entry)
        codec.verify(entries, keys, checkpoint)
        self.check()
        return entries, copy.deepcopy(checkpoint)


class ReadOnlyRemoteAnchor:
    def __init__(self, remote, kind):
        self.remote, self.kind = remote, kind

    def read(self):
        self.remote.check()
        return copy.deepcopy(self.remote.current.index['checkpoints'][self.kind])

    def compare_and_swap(self, expected, replacement):
        raise Invalid('evaluation cannot append operator or intake observations')


class RemoteGenerationAuthority:
    """Publisher barriers commit full generation state to protocol-state."""
    def __init__(self, remote):
        self.remote = remote
        self.active = None

    def _save(self, snapshot, identity=None):
        wrapper = {'schema': 'protocol-controller-generation/v1',
                   'controller_sha': self.remote.guard.approved_sha,
                   'state': copy.deepcopy(snapshot), 'publication': copy.deepcopy(identity)}
        raw = canonical(wrapper)
        sha = digest(raw)
        checkpoints = copy.deepcopy(self.remote.current.index['checkpoints'])
        checkpoints['publisher'] = {'snapshot_sha256': sha}
        self.remote.advance({'state/snapshots/' + sha + '.json': raw}, checkpoints)

    @staticmethod
    def _row(snapshot, lease):
        rows = [r for r in snapshot['generations'] if r['key'] == lease.key]
        require(len(rows) == 1 and rows[0]['generation'] == lease.generation and
                rows[0]['token'] == lease.token, 'generation lease mismatch')
        return rows[0]

    def begin(self, lease, snapshot):
        self.remote.check()
        previous = self.remote.generation_snapshot()
        old = [r for r in previous['generations'] if r['key'] == lease.key]
        require(len(old) <= 1 and lease.generation == (old[0]['generation'] if old else 0) + 1,
                'remote publisher generation is stale')
        self._row(snapshot, lease)
        require([r for r in snapshot['generations'] if r['key'] != lease.key] ==
                [r for r in previous['generations'] if r['key'] != lease.key] and
                snapshot['targets'] == previous['targets'], 'unrelated generation changed')
        self._save(snapshot)
        self.active = lease

    def assert_current(self, lease):
        require(self.active == lease, 'inactive generation lease')
        self.remote.check()
        self._row(self.remote.generation_snapshot(), lease)

    def before_success(self, lease, snapshot, identity):
        self.assert_current(lease)
        require(type(identity) is dict and identity, 'publication identity missing')
        self._row(snapshot, lease)
        self._save(snapshot, identity)

    def finish(self, snapshot):
        require(self.active is not None, 'generation did not begin')
        self.assert_current(self.active)
        self._row(snapshot, self.active)
        self._save(snapshot)


class GitBlobReader:
    """Loads regular Git blobs through the App's bounded read-only transport."""
    def __init__(self, transport, repository):
        self.api = github.API(transport)
        self.root = '/repos/' + repository

    def open(self, side, path, entry):
        require(side in ('base', 'head'), 'invalid manifest side')
        sha = entry['blob']
        require(oid(sha), 'invalid blob ID')
        value = self.api.one(self.root + '/git/blobs/' + sha)
        require(value.get('sha') == sha and value.get('encoding') == 'base64' and
                type(value.get('size')) is int and 0 <= value['size'] <= MAX_INPUT,
                'invalid blob response')
        content = value.get('content')
        require(type(content) is str and len(content) <= 2 * MAX_INPUT, 'invalid blob content')
        raw = base64.b64decode(''.join(content.split()), validate=True)
        require(len(raw) == value['size'] and object_id('blob', raw) == sha,
                'blob content identity mismatch')
        return io.BytesIO(raw)


class ForkProtocolRunner:
    """Fixed approved fork profile; never chooses a module from packet data."""
    def __init__(self, input_provider, coverage_profile=None):
        self.input_provider = input_provider
        self.coverage_profile = copy.deepcopy(coverage_profile)

    def evaluate(self, context):
        inputs = self.input_provider(context)
        require(type(inputs) is publisher.EvaluationInputs, 'trusted evaluation inputs required')
        return live_protocol_context_forks.evaluate_session(copy.deepcopy(inputs.packet),
            inputs.recorder, inputs.live_reader, copy.deepcopy(inputs.selected_reports), inputs.blob_reader,
            copy.deepcopy(self.coverage_profile))

    def validate(self, session):
        require(type(session) is live_protocol_context_forks.LiveEvaluation,
                'fresh fork-profile session required, not result JSON')


def evaluate(remote, workdir, candidate_roots, keys, config, app_transport, packet,
             selected_reports, read_policy, collector_sha, blob_reader=None, coverage_profile=None):
    """One real evaluation, with injected transports only for offline testing."""
    require(type(config) is publisher.Config, 'publisher configuration required')
    require(type(packet) is dict and packet.get('repository_id') == config.repository_id,
            'packet repository differs from configuration')
    packet = copy.deepcopy(packet)
    # Selection comes only from protected controller configuration. This early
    # check blocks missing/unknown governance before any publisher operation.
    coverage_profile = copy.deepcopy(coverage_gate.select_profile(packet, copy.deepcopy(coverage_profile)))
    workdir = Path(workdir).resolve()
    require(workdir.is_dir(), 'ephemeral directory missing')
    op_entries, op_cp = remote.entries('operator', operator_ledger, keys['operator'])
    in_entries, in_cp = remote.entries('intake', audit_intake, keys['intake'])
    op_store = restore_operator_store(ProtectedPath(workdir/'operator.sqlite', candidate_roots),
        ReadOnlyRemoteAnchor(remote, 'operator'), op_entries, keys['operator'], op_cp)
    in_store = restore_audit_store(ProtectedPath(workdir/'intake.sqlite', candidate_roots),
        ReadOnlyRemoteAnchor(remote, 'intake'), in_entries, keys['intake'], in_cp)
    state = SQLiteGenerationState(workdir/'publisher.sqlite', candidate_roots)
    state.initialize()
    state.restore_trusted(remote.generation_snapshot())
    reader = github_fork_context.ForkReadContext(read_policy, app_transport)
    reader.api = CachingAPI(app_transport)
    recorder = IntakeRecorder(in_store, op_store, AuditObservationSource(reader), collector_sha, keys['collector'])
    inputs = publisher.EvaluationInputs(packet, recorder, reader, selected_reports,
        blob_reader if blob_reader is not None else GitBlobReader(app_transport, config.repository))
    authority = RemoteGenerationAuthority(remote)
    pub = publisher.Publisher(config, state, app_transport,
        ForkProtocolRunner(lambda _: inputs, coverage_profile), authority)
    expected = state.read(pub.key(packet['head']['commit']))['generation']
    result = pub.run(packet['head']['commit'], expected)
    if authority.active is not None:
        authority.finish(state.snapshot())
    remote.check()
    return result


def read_protected_json(root, relative):
    require(type(relative) is str and re.fullmatch(r'[A-Za-z0-9_./-]+\.json', relative) and
            all(p not in ('', '.', '..') for p in relative.split('/')), 'invalid protected input path')
    path = root.joinpath(*relative.split('/'))
    require(path.resolve() == path and root in path.parents and path.is_file(), 'protected path escaped checkout')
    require(path.stat().st_size <= MAX_INPUT, 'protected JSON input too large')
    return decode_json(path.read_bytes())


def load_keys(environment):
    keys = {}
    for kind in ('operator', 'intake', 'collector'):
        value = decode_json(environment['PROTOCOL_' + kind.upper() + '_KEYS'])
        require(type(value) is dict and 0 < len(value) <= 32, 'invalid key registry')
        keys[kind] = {}
        for key_id, entry in value.items():
            require(type(key_id) is str and re.fullmatch('[A-Za-z0-9._-]{1,100}', key_id),
                    'invalid key identity')
            if kind == 'collector':
                secret_hex = entry
            else:
                exact(entry, 'operator_id secret_hex', 'operator/intake key needs attributed identity')
                require(type(entry['operator_id']) is str and entry['operator_id'].strip() and
                        len(entry['operator_id']) <= 200, 'invalid operator attribution')
                secret_hex = entry['secret_hex']
            require(type(secret_hex) is str and re.fullmatch('[0-9a-f]{64,256}', secret_hex)
                    and len(secret_hex) % 2 == 0, 'invalid key encoding')
            secret = bytes.fromhex(secret_hex)
            keys[kind][key_id] = secret if kind == 'collector' else {
                'operator_id': entry['operator_id'], 'secret': secret}
            if kind != 'collector':
                # Exercise the exact accepted-codec contract at the boundary.
                operator_ledger.trusted_key(keys[kind], key_id)
    return keys


def load_job(root, job):
    extra = ' coverage_profile' if type(job) is dict and 'coverage_profile' in job else ''
    exact(job, 'id publisher policy packet selected_reports collector_sha256' + extra, 'invalid job configuration')
    require(not extra or type(job['coverage_profile']) is dict, 'coverage profile must be an inline protected object')
    require(type(job['id']) is str and re.fullmatch('[a-z0-9-]{1,80}', job['id']), 'invalid job ID')
    c = copy.deepcopy(job['publisher'])
    exact(c, 'repository repository_id app_id installation_id base_ref target_mode required_merge_ci', 'invalid publisher fields')
    c['required_merge_ci'] = tuple(publisher.RequiredCheck(**r) for r in c['required_merge_ci'])
    config = publisher.Config(**c)
    config.validate()
    p = copy.deepcopy(job['policy'])
    exact(p, 'repository repository_id base_ref policy_path policy_sha256 policy_paths workflows', 'invalid policy fields')
    p['policy_paths'] = tuple(p['policy_paths'])
    p['workflows'] = tuple(github.WorkflowPolicy(**dict(w, jobs=tuple(w['jobs']),
        referenced_workflows=tuple(w.get('referenced_workflows', ())))) for w in p['workflows'])
    policy = github.TrustedPolicy(**p)
    require((policy.repository, policy.repository_id, policy.base_ref) ==
            (config.repository, config.repository_id, config.base_ref), 'policy/publisher origin differs')
    require(type(job['collector_sha256']) is str and re.fullmatch('[0-9a-f]{64}', job['collector_sha256']), 'invalid collector pin')
    packet = read_protected_json(root, job['packet'])
    coverage_gate.select_profile(packet, copy.deepcopy(job.get('coverage_profile')))
    return config, policy, packet, read_protected_json(root, job['selected_reports'])


def main(environment=None):
    env = os.environ if environment is None else environment
    checkout = ROOT.resolve()
    config = read_protected_json(checkout, 'controller/config.json')
    exact(config, 'schema controller_repository controller_repository_id jobs', 'invalid controller config')
    require(config['schema'] == 'protocol-controller/v1' and type(config['controller_repository_id']) is int and
            config['controller_repository_id'] > 0, 'invalid controller identity')
    require(type(config['jobs']) is list and len(config['jobs']) <= MAX_JOBS and
            len({j['id'] for j in config['jobs']}) == len(config['jobs']), 'invalid configured jobs')
    api = ControllerHTTPS(config['controller_repository'], env['GITHUB_TOKEN'])
    try:
        guard = RevisionGuard(api, config['controller_repository'], config['controller_repository_id'],
                              env['PROTOCOL_APPROVED_SHA'], env)
        guard.check()
        if not config['jobs']:
            print(json.dumps([]))
            return 0
        keys = load_keys(env)
        # Import App credential handling only after the independent controller guard.
        from github_app_transport import GitHubAppTransport, TransportConfig, RS256Signer
        signer = RS256Signer.from_pem(env['PROTOCOL_APP_PRIVATE_KEY'].encode())
        results = []
        for job in config['jobs']:
            guard.check()
            pub_config, policy, packet, selected = load_job(checkout, job)
            transport = GitHubAppTransport(TransportConfig(installation_id=pub_config.installation_id,
                repository_id=pub_config.repository_id), signer)
            remote = RemoteState(GitState(api, config['controller_repository'], config['controller_repository_id']), guard)
            with tempfile.TemporaryDirectory(prefix='protocol-private-') as temporary:
                workdir = Path(temporary).resolve()
                # This path is never created or used for checkout. It explicitly marks
                # the separate, forbidden candidate execution area for store APIs.
                candidate_roots = (workdir/'candidate-forbidden',)
                result = evaluate(remote, workdir, candidate_roots, keys, pub_config, transport,
                    packet, selected, policy, job['collector_sha256'],
                    coverage_profile=copy.deepcopy(job.get('coverage_profile')))
                results.append({'job': job['id'], **result})
        print(json.dumps(results, sort_keys=True))
        return 0 if all(r['published_success'] for r in results) else 1
    finally:
        api.diagnostics()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        # Do not print credentials, bodies or potentially sensitive exception text.
        print('Controller stopped: trusted configuration, state, or transport check failed.', file=sys.stderr)
        sys.exit(2)
