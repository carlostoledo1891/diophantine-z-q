"""Offline record consistency checks. No GitHub API, code execution or merge authority.

An EvidenceVerifier adapter must authenticate all supplied runs, receipts, authorship,
audit intake and Git commit/tree bindings independently of the candidate. None is
implemented here. check_records() checks *unverified* data only; it never authenticates.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import re
import unicodedata
from typing import Protocol

OBLIGATIONS = frozenset(('source_hypotheses', 'constructed_objects', 'index_domain_coverage',
    'transition_maps', 'consumed_object_identity', 'coefficient_conventions',
    'local_conditions', 'exceptional_cases', 'downstream_consumption'))
KINDS = frozenset(('argument', 'source', 'computation', 'editorial', 'policy'))
MAX_FILE = 8 * 1024 * 1024
MAX_TOTAL = 64 * 1024 * 1024
MAX_FILES = 10000

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
    fields(snap, 'commit tree files', 'snapshot')
    length = 40 if algorithm == 'sha1' else 64
    require(hexhash(snap['commit'], length) and hexhash(snap['tree'], length), 'git-id')
    require(type(snap['files']) is dict and len(snap['files']) <= MAX_FILES, 'snapshot-files')
    tree, manifest, content, total, folded = {}, {}, {}, 0, {}
    for path, item in sorted(snap['files'].items()):
        require(path_ok(path), 'unsafe-path')
        fields(item, 'mode content_base64', 'file')
        require(item['mode'] in ('100644', '100755'), 'unsupported-file-mode')
        require(type(item['content_base64']) is str and len(item['content_base64']) <= 4 * ((MAX_FILE + 2)//3), 'file-size')
        try:
            raw = base64.b64decode(item['content_base64'], validate=True)
        except (ValueError, TypeError):
            raise Invalid('base64') from None
        require(base64.b64encode(raw).decode() == item['content_base64'], 'noncanonical-base64')
        total += len(raw)
        require(len(raw) <= MAX_FILE and total <= MAX_TOTAL, 'snapshot-size')
        parts = path.split('/')
        for i in range(1, len(parts)+1):
            prefix = '/'.join(parts[:i]); key = prefix.casefold()
            require(key not in folded or folded[key] == prefix, 'case-collision')
            folded[key] = prefix
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
            require(type(node) is dict, 'file-directory-collision')
        require(parts[-1] not in node, 'file-directory-collision')
        oid = git_object('blob', raw, algorithm)
        node[parts[-1]] = (item['mode'], oid)
        manifest[path] = {'mode':item['mode'], 'blob':oid, 'sha256':sha(raw)}
        content[path] = raw
    def tree_id(node):
        entries = []
        for name, value in node.items():
            directory = type(value) is dict
            mode, oid = ('40000', tree_id(value)) if directory else value
            name = name.encode('utf-8')
            entries.append((name + (b'/' if directory else b''), mode.encode()+b' '+name+b'\0'+bytes.fromhex(oid)))
        return git_object('tree', b''.join(v for _,v in sorted(entries)), algorithm)
    require(tree_id(tree) == snap['tree'], 'git-tree-mismatch')
    return manifest, content

def binding(packet, base_manifest, head_manifest):
    return {'repository_id':packet['repository_id'], 'pull_request':packet['pull_request'],
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

def validate_offline(packet, verifier: EvidenceVerifier | None = None):
    if verifier is None:
        raise IntegrationMissing('receipt-authentication-and-snapshot-adapter-not-implemented')
    evidence = verifier.verify(packet)
    result = check_records(packet, evidence)
    result['authentication'] = 'externally verified by caller adapter; not implemented in this package'
    return result

def check_records(packet, evidence):
    """Check structure against supplied evidence. Evidence is NOT authenticated here."""
    fields(packet, 'schema repository_id pull_request git_hash policy_sha256 base head changes applications findings', 'packet')
    require(type(packet['schema']) is int and packet['schema'] == 1, 'schema-version')
    require(type(packet['repository_id']) is int and packet['repository_id'] > 0, 'repository-id')
    require(type(packet['pull_request']) is int and packet['pull_request'] > 0, 'pull-request')
    require(packet['git_hash'] in ('sha1', 'sha256') and hexhash(packet['policy_sha256']), 'hash-algorithm-or-policy')
    fields(evidence, 'binding policy_paths runs authorship findings receipts', 'evidence')
    base, base_bytes = snapshot(packet['base'], packet['git_hash'])
    head, head_bytes = snapshot(packet['head'], packet['git_hash'])
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
    def pin(p):
        fields(p, 'side path sha256', 'file-pin')
        require(p['side'] in ('base', 'head') and path_ok(p['path']) and hexhash(p['sha256']), 'bad-file-pin')
        source = base if p['side']=='base' else head
        require(p['path'] in source and p['sha256'] == source[p['path']]['sha256'], 'stale-file-pin')
        return p['side'], p['path']
    app_agents, app_pins = {}, {}
    for aid, app in apps.items():
        fields(app, 'id kind authors dependencies files obligations', 'application')
        require(app['kind'] in KINDS, 'application-kind')
        app_agents[aid] = authors('application:'+aid, app['authors'])
        deps = string_set(app['dependencies'], 'dependencies')
        require(deps <= set(apps), 'missing-dependency')
        require(type(app['files']) is list and app['files'], 'application-files')
        pairs = [pin(p) for p in app['files']]
        require(len(pairs)==len(set(pairs)), 'duplicate-file-pin')
        app_pins[aid] = set(pairs)
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
    for aid, app in apps.items():
        decision('application',aid,digest(app),closure[aid],app_agents[aid])
    for fid, f in findings.items():
        deps=finding_closure[fid]
        forbidden=finding_agents[fid].union(*(app_agents[a] for a in f['applications']))
        decision('finding',fid,digest(f),deps,forbidden)
    decision('assembly','complete',digest(packet),digest(closure),set().union(*app_agents.values(),*finding_agents.values()))
    return {'records_consistent':True, 'applications':len(apps), 'changed_files':len(changes),
        'findings':len(findings), 'packet_sha256':digest(packet),
        'authentication':'NOT CHECKED: supplied evidence is unverified',
        'live_github_state':'NOT IMPLEMENTED', 'merge_authorized':False,
        'deployment_eligible':False,
        'limitation':'Structural consistency only; no proof of mathematical truth or complete semantic inventory.'}

def read_json(path):
    def pairs(items):
        out={}
        for k,v in items:
            require(k not in out, 'duplicate-json-key');out[k]=v
        return out
    def constant(_):raise Invalid('nonfinite-json')
    with open(path, encoding='utf-8-sig') as f:
        return json.load(f, object_pairs_hook=pairs, parse_constant=constant)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('packet')
    p.add_argument('--unverified-evidence', help='Structural preview only. This never authenticates receipts or authorizes merging.')
    args=p.parse_args()
    try:
        packet=read_json(args.packet)
        if args.unverified_evidence:
            result=check_records(packet,read_json(args.unverified_evidence))
        else:
            result=validate_offline(packet)
        print(json.dumps(result,indent=2))
        return 2  # Integration absent: never emit a deployment-success exit status.
    except (Invalid,KeyError,TypeError,ValueError) as e:
        print(json.dumps({'records_consistent':False,'error':str(e),'merge_authorized':False}))
        return 2

if __name__=='__main__':
    raise SystemExit(main())
