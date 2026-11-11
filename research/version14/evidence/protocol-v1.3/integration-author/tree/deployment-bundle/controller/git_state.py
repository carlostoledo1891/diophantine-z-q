"""Bounded controller state on an owner-only GitHub repository ref.

The remote ref, not a second file in the same commit, is the current authority.
Administrative rollback is outside this store's threat model. The caller must
authenticate the fixed GitHub origin and supply the controller's own token.
"""
from __future__ import annotations

import base64
import hashlib
import json
import re
from dataclasses import dataclass

MAX_BLOB = 40 * 1024 * 1024
MAX_TOTAL = 512 * 1024 * 1024
MAX_FILES = 25_000
INDEX_PATH = 'state/index.json'


class Invalid(ValueError):
    pass


class Conflict(Invalid):
    pass


def require(ok, message):
    if not ok:
        raise Invalid(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, allow_nan=False).encode()


def object_id(kind, raw):
    return hashlib.sha1(kind.encode() + b' ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def oid(value):
    return type(value) is str and re.fullmatch('[0-9a-f]{40}', value) is not None


def path_ok(path):
    return (type(path) is str and
            re.fullmatch(r'state/(?:entries/(?:operator|intake)/[0-9]{10}|snapshots/[0-9a-f]{64})\.json', path) is not None)


def decode_json(raw):
    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, 'duplicate JSON key')
            out[key] = value
        return out
    def constant(_):
        raise Invalid('nonfinite JSON')
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=constant)


@dataclass(frozen=True)
class Snapshot:
    commit: str
    tree: str
    index: dict
    entries: dict


class GitState:
    def __init__(self, api, repository, repository_id, branch='protocol-state'):
        require(re.fullmatch('[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) is not None,
                'invalid controller repository')
        require(type(repository_id) is int and repository_id > 0, 'invalid repository ID')
        require(re.fullmatch('[a-z][a-z0-9-]{0,63}', branch) is not None, 'invalid state branch')
        self.api = api
        self.repository = repository
        self.repository_id = repository_id
        self.branch = branch
        self.root = '/repos/' + repository

    def identity(self):
        repo = self.api.request('GET', self.root)
        require(type(repo.get('id')) is int and repo['id'] == self.repository_id and
                repo.get('full_name') == self.repository,
                'controller repository identity changed')
        require(repo.get('private') is True, 'controller repository is not private')

    def tip(self):
        value = self.api.request('GET', self.root + '/git/ref/heads/' + self.branch)
        require(value.get('ref') == 'refs/heads/' + self.branch, 'wrong state ref')
        obj = value.get('object', {})
        require(obj.get('type') == 'commit' and oid(obj.get('sha')), 'invalid state tip')
        return obj['sha']

    def blob(self, sha, expected_size=None):
        require(oid(sha), 'invalid blob ID')
        value = self.api.request('GET', self.root + '/git/blobs/' + sha)
        require(value.get('sha') == sha and value.get('encoding') == 'base64', 'invalid blob response')
        require(type(value.get('size')) is int and 0 <= value['size'] <= MAX_BLOB, 'state blob too large')
        content = value.get('content')
        require(type(content) is str and len(content) <= 2*MAX_BLOB, 'invalid encoded blob')
        raw = base64.b64decode(''.join(content.split()), validate=True)
        require(len(raw) == value['size'] and object_id('blob', raw) == sha, 'state blob hash mismatch')
        require(expected_size is None or len(raw) == expected_size, 'state blob length mismatch')
        return raw

    def load(self):
        self.identity()
        commit = self.tip()
        body = self.api.request('GET', self.root + '/git/commits/' + commit)
        require(body.get('sha') == commit and oid(body.get('tree', {}).get('sha')), 'invalid state commit')
        tree = body['tree']['sha']
        listing = self.api.request('GET', self.root + '/git/trees/' + tree + '?recursive=1')
        require(listing.get('sha') == tree and listing.get('truncated') is False, 'incomplete state tree')
        files = {}
        for item in listing.get('tree', []):
            if item.get('type') == 'tree':
                continue
            path = item.get('path')
            require(path == INDEX_PATH or path_ok(path), 'unapproved controller state path')
            require(path not in files and item.get('type') == 'blob' and item.get('mode') == '100644',
                    'invalid state tree entry')
            require(oid(item.get('sha')), 'invalid state tree blob')
            files[path] = item['sha']
        require(INDEX_PATH in files and len(files) <= MAX_FILES, 'missing or oversized state inventory')
        index = decode_json(self.blob(files.pop(INDEX_PATH)))
        require(type(index) is dict and set(index) == {'schema', 'generation', 'parent', 'files', 'checkpoints'},
                'invalid state index schema')
        require(type(index['schema']) is int and index['schema'] == 1, 'invalid state index version')
        require(type(index['generation']) is int and index['generation'] >= 0, 'invalid generation')
        require(index['parent'] is None or oid(index['parent']), 'invalid indexed parent')
        parents = [x.get('sha') for x in body.get('parents', [])]
        require(parents == ([] if index['parent'] is None else [index['parent']]), 'state ancestry mismatch')
        require(type(index['files']) is dict and set(index['files']) == set(files), 'incomplete state index')
        require(type(index['checkpoints']) is dict, 'invalid checkpoint map')
        entries = {}
        total = 0
        for path, sha in files.items():
            item = index['files'][path]
            require(type(item) is dict and set(item) == {'blob', 'sha256', 'size'}, 'invalid entry metadata')
            require(item['blob'] == sha and type(item['size']) is int and 0 <= item['size'] <= MAX_BLOB,
                    'invalid indexed blob')
            total += item['size']
            require(total <= MAX_TOTAL, 'state inventory too large')
            raw = self.blob(sha, item['size'])
            require(hashlib.sha256(raw).hexdigest() == item['sha256'], 'state raw digest mismatch')
            entries[path] = raw
        require(self.tip() == commit, 'state changed while loading')
        return Snapshot(commit, tree, index, entries)

    def append(self, snapshot, additions, checkpoints):
        """Append immutable files and a fresh index using a fast-forward ref CAS.

        Callers verify all signed ledger/checkpoint transitions before this call.
        This layer checks transport, immutability and concurrent publication only.
        """
        require(type(snapshot) is Snapshot, 'expected a loaded state snapshot')
        # A dataclass frozen at its top level still contains mutable dictionaries.
        # Treat the supplied object only as the caller's expected commit token;
        # reload all content and ancestry through authenticated remote reads.
        authoritative = self.load()
        if authoritative.commit != snapshot.commit:
            raise Conflict('state advanced before update')
        snapshot = authoritative
        require(type(additions) is dict and type(checkpoints) is dict, 'invalid state update')
        metadata = dict(snapshot.index['files'])
        tree_items = []
        total = sum(item['size'] for item in metadata.values())
        for path, raw in additions.items():
            require(path_ok(path) and type(raw) is bytes and len(raw) <= MAX_BLOB, 'invalid new state entry')
            if path in snapshot.entries:
                require(snapshot.entries[path] == raw, 'attempt to replace immutable state entry')
                continue
            total += len(raw)
            require(total <= MAX_TOTAL and len(metadata) < MAX_FILES-1, 'state capacity exceeded')
            value = self.api.request('POST', self.root + '/git/blobs',
                                     {'content':base64.b64encode(raw).decode(), 'encoding':'base64'})
            sha = object_id('blob', raw)
            require(value.get('sha') == sha, 'created state blob mismatch')
            metadata[path] = {'blob':sha, 'sha256':hashlib.sha256(raw).hexdigest(), 'size':len(raw)}
            tree_items.append({'path':path, 'mode':'100644', 'type':'blob', 'sha':sha})
        index = {'schema':1, 'generation':snapshot.index['generation']+1,
                 'parent':snapshot.commit, 'files':metadata, 'checkpoints':checkpoints}
        raw = canonical(index)
        require(len(raw) <= MAX_BLOB, 'state index too large')
        value = self.api.request('POST', self.root + '/git/blobs',
                                 {'content':base64.b64encode(raw).decode(), 'encoding':'base64'})
        sha = object_id('blob', raw)
        require(value.get('sha') == sha, 'created index blob mismatch')
        tree_items.append({'path':INDEX_PATH, 'mode':'100644', 'type':'blob', 'sha':sha})
        tree = self.api.request('POST', self.root + '/git/trees',
                                {'base_tree':snapshot.tree, 'tree':tree_items})
        require(oid(tree.get('sha')), 'invalid created tree')
        commit = self.api.request('POST', self.root + '/git/commits',
            {'message':'Advance verified protocol state', 'tree':tree['sha'], 'parents':[snapshot.commit]})
        require(oid(commit.get('sha')) and commit.get('tree', {}).get('sha') == tree['sha'] and
                [x.get('sha') for x in commit.get('parents', [])] == [snapshot.commit],
                'created state commit mismatch')
        # No force and exactly the old tip as parent: a concurrent sibling commit
        # makes GitHub reject this update rather than silently losing its entries.
        updated = self.api.request('PATCH', self.root + '/git/refs/heads/' + self.branch,
                                   {'sha':commit['sha'], 'force':False})
        require(updated.get('object', {}).get('sha') == commit['sha'], 'state update not confirmed')
        if self.tip() != commit['sha']:
            raise Conflict('state advanced during confirmation')
        return commit['sha']
