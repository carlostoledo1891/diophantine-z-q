"""Manifest-input offline record consistency checks, schema 2. No merge authority.

An EvidenceVerifier adapter must authenticate all supplied runs, receipts, authorship,
audit intake and Git commit/tree bindings independently of the candidate. None is
implemented here. check_records() checks *unverified* data only; it never authenticates.
"""
from __future__ import annotations
from approval_policy import approval_allowed
import argparse
import contextlib
import os
import subprocess
from pathlib import Path
import git_manifest as transport
import base64
import hashlib
import json
import io
import re
import unicodedata
from typing import Protocol

OBLIGATIONS = frozenset(('source_hypotheses', 'constructed_objects', 'index_domain_coverage',
    'transition_maps', 'consumed_object_identity', 'coefficient_conventions',
    'local_conditions', 'exceptional_cases', 'downstream_consumption'))
KINDS = frozenset(('argument', 'source', 'computation', 'editorial', 'policy'))

class Invalid(ValueError):
    pass

class IntegrationMissing(Invalid):
    pass

def require(ok, code):
    if not ok:
        raise Invalid(code)

def fields(value, names, where):
    require(type(value) is dict and set(value) == set(names.split()), 'schema:' + where)

def text(value):
    return type(value) is str and bool(value.strip())

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode('utf-8')

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def hexhash(value, length=64):
    return type(value) is str and re.fullmatch('[0-9a-f]{%d}' % length, value) is not None

def path_ok(path):
    return (type(path) is str and path and unicodedata.normalize('NFC', path) == path
        and not any(ord(c) < 32 or c in '\\:' for c in path)
        and all(p not in ('', '.', '..') and p.casefold() != '.git' for p in path.split('/')))

def unique(rows, key, where):
    require(type(rows) is list, 'list:' + where)
    out = {}
    for row in rows:
        require(type(row) is dict and text(row.get(key)), 'identity:' + where)
        require(row[key] not in out, 'duplicate:' + where)
        out[row[key]] = row
    return out

def string_set(values, where, nonempty=False):
    require(type(values) is list and all(text(x) for x in values), 'list:' + where)
    require(len(set(values)) == len(values) and (values or not nonempty), 'duplicate-or-empty:' + where)
    return set(values)

def git_object(kind, raw, algorithm):
    return hashlib.new(algorithm, kind.encode() + b' ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()

def snapshot(snap, algorithm):
    # Preserve schema-1 manifest digest bytes: size and transport fields are not
    # added to this map. The outer schema-2 packet also binds the full transport.
    try:
        transport.verify_manifest(snap)
    except transport.Invalid as error:
        raise Invalid('manifest: ' + str(error)) from error
    require(snap['git_hash'] == algorithm, 'snapshot-hash-algorithm')
    manifest = {p:{k:item[k] for k in ('mode','blob','sha256')}
                for p,item in snap['files'].items()}
    return manifest, None

class DirectoryBlobReader:
    """Untrusted flat SHA-256 blob store; returned bytes are always verified."""
    def __init__(self, root):
        self.root = Path(root).resolve()
    def open(self, side, path, entry):
        require(hexhash(entry['sha256']), 'invalid-blob-name')
        target = self.root / entry['sha256']
        require(not target.is_symlink() and target.resolve().parent == self.root, 'unsafe-blob-store-path')
        return target.open('rb')

class GitBlobReader:
    """Read raw objects only. Never check out or execute the candidate."""
    def __init__(self, repositories):
        self.repositories = {side:Path(path).resolve().as_posix() for side,path in repositories.items()}
    def open(self, side, path, entry):
        require(side in self.repositories and re.fullmatch('[0-9a-f]{40}|[0-9a-f]{64}',entry['blob']) is not None, 'invalid-blob-source')
        repo = self.repositories[side]
        proc = subprocess.Popen(['git','--no-replace-objects','-c','safe.directory='+repo,'-C',repo,
            'cat-file','blob',entry['blob']], env=transport.git_environment(),
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        class Stream:
            def read(self, amount): return proc.stdout.read(amount)
            def close(self):
                proc.stdout.close()
                if proc.poll() is None:
                    try:
                        proc.wait(timeout=2)
                    except subprocess.TimeoutExpired:
                        proc.kill(); proc.wait()
                        raise OSError('Git blob reader timed out and was terminated') from None
                if proc.returncode != 0:
                    raise OSError('Git blob reader failed with exit code ' + str(proc.returncode))
        return Stream()

def binding(packet, base_manifest, head_manifest):
    return {'record_schema':packet['schema'], 'repository_id':packet['repository_id'], 'pull_request':packet['pull_request'],
        'git_hash':packet['git_hash'], 'policy_sha256':packet['policy_sha256'],
        'base_commit':packet['base']['commit'], 'base_tree':packet['base']['tree'],
        'head_commit':packet['head']['commit'], 'head_tree':packet['head']['tree'],
        'base_manifest_sha256':digest(base_manifest), 'head_manifest_sha256':digest(head_manifest)}

def same_binding(value, expected):
    # Python equality identifies True, 1 and 1.0; these are distinct records.
    return (type(value) is dict and set(value) == set(expected)
        and all(type(value[k]) is type(expected[k]) for k in expected)
        and canonical(value) == canonical(expected))

class EvidenceVerifier(Protocol):
    def verify(self, packet: dict) -> dict:
        """Return independently authenticated evidence, or raise Invalid.

        Must authenticate snapshot commit/tree links, complete audit intake,
        author contributions and immutable agent identities, reviewer receipts,
        report digests, old-policy identity/paths, and their exact binding.
        Candidate-supplied verified=true fields are not authentication.
        """
        ...

def validate_offline(packet, verifier: EvidenceVerifier | None = None, blob_reader=None, coverage_profile=None):
    if verifier is None:
        raise IntegrationMissing('receipt-authentication-and-snapshot-adapter-not-implemented')
    evidence = verifier.verify(packet)
    result = check_records(packet, evidence, blob_reader, coverage_profile)
    result['authentication'] = 'externally verified by caller adapter; not implemented in this package'
    return result

def check_records(packet, evidence, blob_reader=None, coverage_profile=None):
    """Check structure against supplied evidence. Evidence is NOT authenticated here."""
    if blob_reader is None:
        raise IntegrationMissing('evidence-blob-reader-not-implemented')
    fields(packet, 'schema repository_id pull_request git_hash policy_sha256 base head changes applications findings', 'packet')
    require(type(packet['schema']) is int and packet['schema'] == 2, 'schema-version')
    require(type(packet['repository_id']) is int and packet['repository_id'] > 0, 'repository-id')
    require(type(packet['pull_request']) is int and packet['pull_request'] > 0, 'pull-request')
    require(packet['git_hash'] in ('sha1', 'sha256') and hexhash(packet['policy_sha256']), 'hash-algorithm-or-policy')
    fields(evidence, 'binding policy_paths runs authorship findings receipts', 'evidence')
    base, _ = snapshot(packet['base'], packet['git_hash'])
    head, _ = snapshot(packet['head'], packet['git_hash'])
    expected_binding = binding(packet, base, head)
    require(same_binding(evidence['binding'], expected_binding), 'stale-or-wrong-candidate-binding')
    policy_paths = string_set(evidence['policy_paths'], 'policy-paths', nonempty=True)
    # Strip at most the one permitted directory marker. Never normalize an
    # invalid prefix differently from the path used by the matcher.
    require(all(path_ok(p[:-1] if p.endswith('/') else p) for p in policy_paths), 'policy-path')
    def is_policy(path):
        return any(path == p or (p.endswith('/') and (path == p[:-1] or path.startswith(p))) for p in policy_paths)
    changes = unique(packet['changes'], 'path', 'changes')
    changed_paths = {p for p in set(base)|set(head) if base.get(p) != head.get(p)}
    require(set(changes) == changed_paths, 'incomplete-changed-file-coverage')
    apps = unique(packet['applications'], 'id', 'applications')
    require(apps, 'empty-applications')
    import coverage_gate
    coverage_profile = coverage_gate.select_profile(packet, coverage_profile)
    runs = unique(evidence['runs'], 'id', 'runs')
    for run in runs.values():
        fields(run, 'id agent_id reviewer_type model tools', 'run')
        require(text(run['agent_id']) and run['reviewer_type'] in ('model', 'human'), 'run-identity')
        require(text(run['model']) if run['reviewer_type']=='model' else run['model'] is None, 'model-identity')
        string_set(run['tools'], 'run-tools')
    require(type(evidence['authorship']) is dict, 'authorship')
    def authors(entity, declared):
        ids = string_set(declared, 'authors', nonempty=True)
        require(ids <= set(runs), 'unknown-author-run')
        require(entity in evidence['authorship'] and ids == string_set(evidence['authorship'][entity], 'authenticated-authors', True), 'authorship-mismatch')
        return {runs[i]['agent_id'] for i in ids}
    verified_blobs = set()
    verified_blob_bytes = 0
    def pin(p):
        nonlocal verified_blob_bytes
        fields(p, 'side path sha256', 'file-pin')
        require(p['side'] in ('base', 'head') and path_ok(p['path']) and hexhash(p['sha256']), 'bad-file-pin')
        source = base if p['side']=='base' else head
        require(p['path'] in source and p['sha256'] == source[p['path']]['sha256'], 'stale-file-pin')
        entry = packet[p['side']]['files'][p['path']]
        cache_key = (packet['git_hash'], entry['blob'], entry['size'], entry['sha256'])
        if cache_key not in verified_blobs:
            try:
                with contextlib.closing(blob_reader.open(p['side'], p['path'], entry)) as stream:
                    transport.verify_blob(stream, entry, packet['git_hash'])
            except (transport.Invalid, OSError) as error:
                raise Invalid('evidence-blob: ' + str(error)) from error
            verified_blobs.add(cache_key)
            verified_blob_bytes += entry['size']
        return p['side'], p['path']
    def read_pin(p):
        pin(p)
        entry = packet[p['side']]['files'][p['path']]
        require(entry['size'] <= 16 * 1024 * 1024, 'coverage-blob-too-large')
        try:
            with contextlib.closing(blob_reader.open(p['side'], p['path'], entry)) as stream:
                raw = stream.read(16 * 1024 * 1024 + 1)
            # Revalidate the returned bytes: an untrusted reader may change between reads.
            transport.verify_blob(io.BytesIO(raw), entry, packet['git_hash'])
        except (transport.Invalid, OSError) as error:
            raise Invalid('coverage-evidence-blob: ' + str(error)) from error
        return raw
    app_agents, app_pins = {}, {}
    for aid, app in apps.items():
        is_coverage = app.get('kind') == 'coverage'
        fields(app, 'id kind authors dependencies files ' + ('coverage_record' if is_coverage else 'obligations'), 'application')
        require(app['kind'] in KINDS or (is_coverage and coverage_profile is not None and aid == coverage_gate.COVERAGE_ID), 'application-kind')
        app_agents[aid] = authors('application:'+aid, app['authors'])
        deps = string_set(app['dependencies'], 'dependencies')
        require(deps <= set(apps), 'missing-dependency')
        require(type(app['files']) is list and app['files'], 'application-files')
        pairs = [pin(p) for p in app['files']]
        require(len(pairs)==len(set(pairs)), 'duplicate-file-pin')
        app_pins[aid] = set(pairs)
        if is_coverage:
            continue
        require(type(app['obligations']) is dict and set(app['obligations']) == OBLIGATIONS, 'missing-obligation')
        for obligation in app['obligations'].values():
            fields(obligation, 'status required constructed justification evidence', 'obligation')
            require(obligation['status'] in ('checked','not_applicable'), 'unresolved-obligation')
            require(all(text(obligation[k]) for k in ('required','constructed','justification')), 'empty-obligation')
            require(type(obligation['evidence']) is list and obligation['evidence'], 'missing-obligation-evidence')
            require(all(pin(p) in app_pins[aid] for p in obligation['evidence']), 'unbound-obligation-evidence')
    for path, change in changes.items():
        fields(change, 'path kind applications', 'change')
        require(change['kind'] in KINDS, 'change-kind')
        aids = string_set(change['applications'], 'change-applications', True)
        require(aids <= set(apps), 'unreviewed-change')
        needed = {(side,path) for side,manifest in (('base',base),('head',head)) if path in manifest}
        require(all(needed <= app_pins[a] and apps[a]['kind']==change['kind'] for a in aids), 'unbound-change')
        require(not is_policy(path) or change['kind']=='policy', 'unreviewed-policy-change')
    closure, visiting = {}, set()
    def dependency_digest(aid):
        require(aid not in visiting, 'dependency-cycle')
        if aid not in closure:
            visiting.add(aid)
            deps = {d:dependency_digest(d) for d in sorted(apps[aid]['dependencies'])}
            closure[aid] = digest({'application':apps[aid], 'dependencies':deps})
            visiting.remove(aid)
        return closure[aid]
    for aid in apps: dependency_digest(aid)
    findings = unique(packet['findings'], 'id', 'findings')
    intake = unique(evidence['findings'], 'id', 'authenticated-findings')
    require(set(findings) == set(intake), 'missing-or-extra-finding')
    finding_agents = {}
    for fid, f in findings.items():
        fields(f, 'id body_sha256 status reason authors applications duplicate_of', 'finding')
        fields(intake[fid], 'id body_sha256', 'finding-intake')
        require(hexhash(f['body_sha256']) and f['body_sha256']==intake[fid]['body_sha256'], 'changed-finding')
        require(f['status'] in ('repaired','rebutted','duplicate','out_of_scope') and text(f['reason']), 'unresolved-finding')
        finding_agents[fid] = authors('finding:'+fid, f['authors'])
        related = string_set(f['applications'], 'finding-applications')
        require(related <= set(apps), 'unknown-finding-application')
        require(f['status'] not in ('repaired','rebutted') or related, 'missing-resolution-application')
        require((f['status']=='duplicate' and f['duplicate_of'] in findings and f['duplicate_of']!=fid) or (f['status']!='duplicate' and f['duplicate_of'] is None), 'invalid-duplicate-finding')
    finding_closure, finding_visiting = {}, set()
    def finding_dependency_digest(fid):
        require(fid not in finding_visiting, 'finding-cycle')
        if fid not in finding_closure:
            finding_visiting.add(fid)
            f = findings[fid]
            duplicate = f['duplicate_of']
            target = None if duplicate is None else {
                'finding':findings[duplicate], 'dependencies':finding_dependency_digest(duplicate)}
            finding_closure[fid] = digest({'applications':{a:closure[a] for a in sorted(f['applications'])},
                                           'duplicate_target':target})
            finding_visiting.remove(fid)
        return finding_closure[fid]
    for fid in findings: finding_dependency_digest(fid)
    expected_authorship = {'application:'+x for x in apps}|{'finding:'+x for x in findings}
    require(set(evidence['authorship']) == expected_authorship, 'authorship-inventory')
    receipts = unique(evidence['receipts'], 'id', 'receipts')
    by_target = {}
    for receipt in receipts.values():
        fields(receipt, 'id kind target target_sha256 dependency_sha256 run_id decision scope binding report', 'receipt')
        key = receipt['kind'], receipt['target']
        require(key not in by_target, 'duplicate-receipt-target')
        by_target[key] = receipt
        require(same_binding(receipt['binding'], expected_binding), 'stale-review-binding')
        require(receipt['run_id'] in runs and receipt['decision']=='accepted' and text(receipt['scope']), 'invalid-review-decision')
        require(pin(receipt['report'])[0]=='head', 'review-report-not-in-candidate')
    needed_targets={('application',a) for a in apps}|{('finding',f) for f in findings}|{('assembly','complete')}
    require(set(by_target)==needed_targets, 'missing-or-extra-acceptance')
    def decision(kind, target, target_hash, dependencies, forbidden_agents):
        r=by_target[kind,target]
        require(r['target_sha256']==target_hash and r['dependency_sha256']==dependencies, 'stale-review-content-or-dependencies')
        require(runs[r['run_id']]['agent_id'] not in forbidden_agents, 'self-acceptance')
        reviewer = runs[r['run_id']]
        require(approval_allowed(packet['repository_id'], reviewer['model'], reviewer['reviewer_type']),
                'public-required-approval-needs-exact-astra')
    for aid, app in apps.items():
        decision('application',aid,digest(app),closure[aid],app_agents[aid])
    for fid, f in findings.items():
        deps=finding_closure[fid]
        forbidden=finding_agents[fid].union(*(app_agents[a] for a in f['applications']))
        decision('finding',fid,digest(f),deps,forbidden)
    decision('assembly','complete',digest(packet),digest(closure),set().union(*app_agents.values(),*finding_agents.values()))
    coverage = coverage_gate.validate(packet, coverage_profile, apps, app_agents, runs, by_target, read_pin)
    return {**coverage, 'records_consistent':True, 'applications':len(apps), 'changed_files':len(changes),
        'findings':len(findings), 'packet_sha256':digest(packet),
        'verified_evidence_blobs':len(verified_blobs), 'verified_evidence_bytes':verified_blob_bytes,
        'authentication':'NOT CHECKED: supplied evidence is unverified',
        'live_github_state':'NOT IMPLEMENTED', 'merge_authorized':False,
        'deployment_eligible':False,
        'limitation':'Structural consistency only; no proof of mathematical truth or complete semantic inventory.'}

def parse_json_bytes(raw, where='json'):
    def pairs(items):
        out={}
        for k,v in items:
            require(k not in out, 'duplicate-json-key');out[k]=v
        return out
    def constant(_):raise Invalid('nonfinite-json')
    try:
        return json.loads(raw.decode('utf-8-sig'), object_pairs_hook=pairs, parse_constant=constant)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise Invalid('invalid-'+where) from error

def read_json(path):
    return parse_json_bytes(Path(path).read_bytes())

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('packet')
    p.add_argument('--blob-directory', help='Untrusted flat SHA-256 blob store; every consumed blob is verified.')
    p.add_argument('--unverified-evidence', help='Structural preview only. This never authenticates receipts or authorizes merging.')
    args=p.parse_args()
    try:
        packet=read_json(args.packet)
        if args.unverified_evidence:
            reader=DirectoryBlobReader(args.blob_directory) if args.blob_directory else None
            result=check_records(packet,read_json(args.unverified_evidence),reader)
        else:
            result=validate_offline(packet)
        print(json.dumps(result,indent=2))
        return 2  # Integration absent: never emit a deployment-success exit status.
    except (Invalid,KeyError,TypeError,ValueError) as e:
        print(json.dumps({'records_consistent':False,'error':str(e),'merge_authorized':False}))
        return 2

if __name__=='__main__':
    raise SystemExit(main())
