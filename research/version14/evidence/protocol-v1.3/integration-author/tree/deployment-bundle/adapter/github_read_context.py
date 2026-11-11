"""Read-only GitHub observations. No receipt authority or merge authorization.

Configuration and this process belong outside candidate write/execution access.
Returned dictionaries are captured data, NOT authenticated portable exports.
"""
from dataclasses import dataclass
import base64
import copy
import hashlib
import http.client
import json
import re
from urllib.parse import quote, urlencode, urlsplit, parse_qs

import offline_manifest_gate as core

HOST = 'api.github.com'
MAX_RESPONSE = 16 * 1024 * 1024
MAX_PAGES = 100
MAX_REQUESTS = 5000

def need(ok, message):
    if not ok:
        raise core.Invalid(message)

def integer(n):
    return type(n) is int and n > 0

def same_id(value, expected):
    return integer(value) and integer(expected) and value == expected

def oid(s):
    return type(s) is str and re.fullmatch('[0-9a-f]{40}', s) is not None

def strict_json(raw):
    def pairs(items):
        d = {}
        for k, v in items:
            need(k not in d, 'duplicate API JSON key')
            d[k] = v
        return d
    try:
        return json.loads(raw, object_pairs_hook=pairs,
                          parse_constant=lambda x: (_ for _ in ()).throw(ValueError()))
    except (ValueError, UnicodeError, RecursionError):
        raise core.Invalid('invalid API JSON') from None

class GitHubHTTPS:
    """Fixed TLS origin, GET only, no redirects/proxies or response logging."""
    def __init__(self, token=None):
        need(token is None or (type(token) is str and token and
             all(32 < ord(c) < 127 for c in token)), 'invalid credential format')
        self._token = token

    def get(self, path):
        need(type(path) is str and path.startswith('/repos/') and
             not any(c in path for c in ('\r', '\n', '#', '\\')), 'invalid API path')
        headers = {'Accept': 'application/vnd.github+json',
                   'X-GitHub-Api-Version': '2022-11-28',
                   'User-Agent': 'research-review-read-context/1'}
        if self._token:
            headers['Authorization'] = 'Bearer ' + self._token
        connection = http.client.HTTPSConnection(HOST, timeout=30)
        try:
            connection.request('GET', path, headers=headers)
            response = connection.getresponse()
            need(response.status == 200, 'GitHub GET did not return 200')
            need(response.getheader('Content-Encoding', 'identity') == 'identity', 'encoded API response unsupported')
            need('application/json' in response.getheader('Content-Type', ''), 'non-JSON API response')
            raw = response.read(MAX_RESPONSE + 1)
            need(len(raw) <= MAX_RESPONSE, 'API response limit')
            return strict_json(raw), {'link': response.getheader('Link', '')}
        except core.Invalid:
            raise
        except Exception:
            # Never include a response body, credential, request header or URL.
            raise core.Invalid('GitHub transport failed') from None
        finally:
            connection.close()

class API:
    def __init__(self, transport):
        self.transport = transport
        self.requests = 0

    def get(self, path):
        self.requests += 1
        need(self.requests <= MAX_REQUESTS, 'API request budget')
        value, headers = self.transport.get(path)
        return copy.deepcopy(value), headers

    def one(self, path):
        value, headers = self.get(path)
        need(not headers.get('link'), 'unexpected pagination')
        need(type(value) is dict, 'API object required')
        return value

    def pages(self, path, key=None, query=None, search_cap=None):
        query = dict(query or {})
        need('page' not in query and 'per_page' not in query, 'reserved page parameters')
        result = []; ids = set(); expected_total = None; known_last = None
        for page in range(1, MAX_PAGES + 1):
            params = dict(query, per_page=100, page=page)
            value, headers = self.get(path + '?' + urlencode(params))
            if key is not None:
                need(type(value) is dict and type(value.get('total_count')) is int and value['total_count'] >= 0, 'missing API total count')
                total = value['total_count']
                need(search_cap is None or total < search_cap, 'filtered API search cap')
                need(expected_total is None or total == expected_total, 'pagination total changed')
                expected_total = total
                rows = value.get(key)
            else:
                rows = value
            need(type(rows) is list and len(rows) <= 100, 'invalid API page')
            for row in rows:
                need(type(row) is dict and integer(row.get('id')) and row['id'] not in ids, 'duplicate or invalid API record ID')
                ids.add(row['id']); result.append(row)
            link = headers.get('link', '')
            links = {}
            if link:
                for part in link.split(','):
                    match = re.fullmatch(r'\s*<([^>]+)>;\s*rel="(next|prev|first|last)"\s*', part)
                    need(match is not None, 'unsupported pagination link')
                    url, relation = match.groups(); need(relation not in links, 'duplicate pagination relation')
                    parsed = urlsplit(url)
                    need(parsed.scheme == 'https' and parsed.netloc == HOST and parsed.path == path and not parsed.fragment, 'pagination origin or endpoint changed')
                    args = parse_qs(parsed.query, strict_parsing=True)
                    wanted = {k:[str(v)] for k,v in dict(query, per_page=100).items()}
                    need(set(args) == set(wanted) | {'page'} and all(args[k] == v for k,v in wanted.items()), 'pagination query changed')
                    need(len(args['page']) == 1 and re.fullmatch('[1-9][0-9]*', args['page'][0]), 'invalid pagination page')
                    links[relation] = int(args['page'][0])
                need('next' not in links or links['next'] == page + 1, 'nonsequential pagination')
                need('last' not in links or links['last'] >= page, 'invalid last page')
                need('last' not in links or links['last'] == page or 'next' in links, 'missing pagination continuation')
                if 'last' in links:
                    need(known_last is None or known_last == links['last'], 'pagination last page changed')
                    known_last = links['last']
            if known_last is not None:
                need(page <= known_last and ('next' not in links or links['next'] <= known_last), 'pagination exceeds known last page')
            if 'next' not in links:
                need(known_last is None or page == known_last, 'pagination ended before known last page')
                need(expected_total is None or len(result) == expected_total, 'incomplete API pagination')
                return result
            need(rows, 'empty nonfinal API page')
        raise core.Invalid('API page budget')

@dataclass(frozen=True)
class WorkflowPolicy:
    workflow_id: int
    path: str
    jobs: tuple
    # Complete approved local execution inputs, including workflow and scripts.
    source_sha256: dict
    # Exact API referenced_workflows rows required by the approved workflow.
    referenced_workflows: tuple = ()

@dataclass(frozen=True)
class TrustedPolicy:
    repository: str
    repository_id: int
    base_ref: str
    policy_path: str
    policy_sha256: str
    policy_paths: tuple
    workflows: tuple

# Repository-wide activity does not identify a reviewed revision. These fields
# can change when someone stars the repository or pushes an unrelated branch.
# Identity, visibility, permissions, configuration and unknown fields remain.
REPOSITORY_ACTIVITY_FIELDS = (
    'size', 'open_issues', 'open_issues_count',
    'stargazers_count', 'watchers', 'watchers_count',
    'forks', 'forks_count', 'network_count', 'subscribers_count',
    'updated_at', 'pushed_at',
)
PR_DERIVED_FIELDS = ('mergeable', 'mergeable_state', 'rebaseable')


def project_repository(repository):
    value = copy.deepcopy(repository)
    if type(value) is dict:
        for name in REPOSITORY_ACTIVITY_FIELDS:
            value.pop(name, None)
    return value


def project_pr(pr):
    value = copy.deepcopy(pr)
    for name in PR_DERIVED_FIELDS:
        value.pop(name, None)
    for side in ('base', 'head'):
        if type(value.get(side)) is dict and 'repo' in value[side]:
            value[side]['repo'] = project_repository(value[side]['repo'])
    return value


def project_ci_run(run):
    value = copy.deepcopy(run)
    for name in ('repository', 'head_repository'):
        if name in value:
            value[name] = project_repository(value[name])
    if type(value.get('pull_requests')) is list:
        for pr in value['pull_requests']:
            for side in ('base', 'head'):
                if type(pr.get(side)) is dict and 'repo' in pr[side]:
                    pr[side]['repo'] = project_repository(pr[side]['repo'])
    return value


class ReadContext:
    def __init__(self, policy, transport=None):
        need(type(policy) is TrustedPolicy, 'protected configuration required')
        self.policy = copy.deepcopy(policy)
        p = self.policy
        need(re.fullmatch('[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', p.repository) is not None and integer(p.repository_id), 'invalid repository configuration')
        need(core.path_ok(p.base_ref) and core.path_ok(p.policy_path) and core.hexhash(p.policy_sha256), 'invalid policy configuration')
        need(p.policy_paths and all(core.path_ok(s[:-1] if s.endswith('/') else s) for s in p.policy_paths), 'invalid protected paths')
        need(p.workflows and len({w.workflow_id for w in p.workflows}) == len(p.workflows), 'missing or repeated required workflow')
        for w in p.workflows:
            need(type(w) is WorkflowPolicy and integer(w.workflow_id) and core.path_ok(w.path), 'invalid workflow configuration')
            need(w.jobs and len(set(w.jobs)) == len(w.jobs) and all(core.text(j) for j in w.jobs), 'invalid required jobs')
            need(type(w.source_sha256) is dict and w.path in w.source_sha256 and all(core.path_ok(k) and core.hexhash(v) for k,v in w.source_sha256.items()), 'missing workflow source closure')
        self.api = API(transport if transport is not None else GitHubHTTPS())
        self.root = '/repos/' + p.repository

    def state(self, number):
        p = self.policy
        repository = self.api.one(self.root)
        need(repository.get('id') == p.repository_id and type(repository.get('id')) is int and repository.get('full_name') == p.repository, 'repository origin mismatch')
        pr = self.api.one(self.root + '/pulls/' + str(number))
        need(type(pr.get('number')) is int and pr['number'] == number and pr.get('state') == 'open' and pr.get('draft') is False and pr.get('merged') is False, 'PR not open and ready')
        need(same_id(pr['base']['repo']['id'],p.repository_id) and same_id(pr['head']['repo']['id'],p.repository_id), 'foreign repository PR unsupported')
        need(pr['base']['ref'] == p.base_ref, 'base branch mismatch')
        base = pr['base']['sha']; head = pr['head']['sha']; merge = pr.get('merge_commit_sha')
        need(all(oid(x) for x in (base, head, merge)), 'missing exact commit identity')
        ref = self.api.one(self.root + '/git/ref/heads/' + quote(p.base_ref, safe='/'))
        need(ref['object']['type'] == 'commit' and ref['object']['sha'] == base, 'base ref moved')
        commits = {}
        for side, sha in (('base',base), ('head',head), ('merge',merge)):
            obj = self.api.one(self.root + '/git/commits/' + sha)
            need(obj.get('sha') == sha and oid(obj['tree']['sha']), 'commit origin mismatch')
            commits[side] = {'commit':sha, 'tree':obj['tree']['sha']}
            if side == 'merge':
                need([x['sha'] for x in obj['parents']] == [base,head], 'merge commit does not bind current base and head')
        # Preserve author-controlled and unknown fields; derived fields are checked separately.
        return {'projection_schema':'github-pr-state/v3', 'repository_id':p.repository_id, 'pr':project_pr(pr), 'commits':commits}

    def blob_at(self, tree, path):
        for index, part in enumerate(path.split('/')):
            obj = self.api.one(self.root + '/git/trees/' + tree)
            need(obj.get('sha') == tree and obj.get('truncated') is False and type(obj.get('tree')) is list, 'incomplete Git tree')
            rows = [v for v in obj['tree'] if v.get('path') == part]
            need(len(rows) == 1, 'missing source path')
            row = rows[0]; need(oid(row.get('sha')), 'invalid source object')
            if index < len(path.split('/')) - 1:
                need(row.get('type') == 'tree' and row.get('mode') == '040000', 'non-directory source parent')
                tree = row['sha']
            else:
                need(row.get('type') == 'blob' and row.get('mode') in ('100644','100755'), 'non-regular approved source')
        obj = self.api.one(self.root + '/git/blobs/' + row['sha'])
        need(obj.get('sha') == row['sha'] and obj.get('encoding') == 'base64', 'source blob identity')
        try:
            raw = base64.b64decode(''.join(obj['content'].split()), validate=True)
        except (ValueError, KeyError, TypeError):
            raise core.Invalid('invalid source blob encoding') from None
        need(type(obj.get('size')) is int and obj['size'] == len(raw), 'source blob size')
        need(core.git_object('blob',raw,'sha1') == row['sha'], 'source blob hash')
        return hashlib.sha256(raw).hexdigest()

    def sources(self, state, packet):
        p = self.policy
        need(packet['policy_sha256'] == p.policy_sha256, 'unregistered policy revision')
        required = {p.policy_path:p.policy_sha256}
        for w in p.workflows:
            for path, sha in w.source_sha256.items():
                need(path not in required or required[path] == sha, 'conflicting source pins')
                required[path] = sha
        for path, sha in required.items():
            # Pins are installed by an operator, never learned from this PR.
            for side in ('base','head','merge'):
                need(self.blob_at(state['commits'][side]['tree'],path) == sha, 'unapproved policy or workflow source')
            for side in ('base','head'):
                need(packet[side]['files'].get(path,{}).get('sha256') == sha, 'manifest source pin mismatch')

    def intake(self, number):
        return {kind:self.api.pages(self.root + path) for kind,path in (
            ('issue_comments','/issues/'+str(number)+'/comments'),
            ('reviews','/pulls/'+str(number)+'/reviews'),
            ('review_comments','/pulls/'+str(number)+'/comments'))}

    def ci(self, state, number):
        head = state['commits']['head']['commit']; base = state['commits']['base']['commit']
        result = []
        for w in self.policy.workflows:
            workflow = self.api.one(self.root+'/actions/workflows/'+str(w.workflow_id))
            need(same_id(workflow.get('id'),w.workflow_id) and workflow.get('path') == w.path and workflow.get('state') == 'active', 'workflow provenance mismatch')
            runs = self.api.pages(self.root+'/actions/workflows/'+str(w.workflow_id)+'/runs', 'workflow_runs', {'head_sha':head}, search_cap=1000)
            need(runs, 'missing required CI run')
            # Reject a newer failing/wrong-event run rather than select old green.
            newest = max(runs, key=lambda r:r['id'])
            run = self.api.one(self.root+'/actions/runs/'+str(newest['id']))
            need(same_id(run.get('id'),newest['id']) and same_id(run.get('workflow_id'),w.workflow_id) and run.get('path') == w.path and run.get('head_sha') == head, 'run provenance mismatch')
            need(same_id(run.get('repository',{}).get('id'),self.policy.repository_id) and same_id(run.get('head_repository',{}).get('id'),self.policy.repository_id), 'run repository mismatch')
            need(run.get('event') == 'pull_request', 'unsupported CI event')
            associations = run.get('pull_requests',[])
            need(any(same_id(r.get('number'),number) and r.get('base',{}).get('sha') == base and r.get('head',{}).get('sha') == head and same_id(r.get('base',{}).get('repo',{}).get('id'),self.policy.repository_id) and same_id(r.get('head',{}).get('repo',{}).get('id'),self.policy.repository_id) for r in associations), 'CI not bound to exact PR base and head')
            need(run.get('status') == 'completed' and run.get('conclusion') == 'success', 'required run not successful')
            need(integer(run.get('run_attempt')), 'missing run attempt')
            need(core.canonical(run.get('referenced_workflows',[])) == core.canonical(list(w.referenced_workflows)), 'unapproved reusable workflow provenance')
            attempt = run['run_attempt']
            jobs = self.api.pages(self.root+'/actions/runs/'+str(run['id'])+'/attempts/'+str(attempt)+'/jobs','jobs')
            names = [j.get('name') for j in jobs]
            need(set(names) == set(w.jobs) and len(names) == len(w.jobs), 'missing duplicate or unregistered CI job')
            for j in jobs:
                need(same_id(j.get('run_id'),run['id']) and same_id(j.get('run_attempt'),attempt) and j.get('head_sha') == head, 'job provenance mismatch')
                need(j.get('status') == 'completed' and j.get('conclusion') == 'success', 'required job not successful')
                need(j.get('steps') and all(s.get('status') == 'completed' and s.get('conclusion') == 'success' for s in j['steps']), 'CI step not actually successful')
            result.append({'workflow':workflow,'run':project_ci_run(run),'jobs':jobs,
                           'run_inventory':[project_ci_run(item) for item in runs]})
        return result

    def observe(self, packet):
        packet = copy.deepcopy(packet)
        need(packet.get('git_hash') == 'sha1' and type(packet.get('schema')) is int and packet['schema'] == 2, 'GitHub adapter requires schema2 SHA1')
        need(type(packet.get('repository_id')) is int and packet['repository_id'] == self.policy.repository_id and integer(packet.get('pull_request')), 'packet repository or PR identity')
        bm,_ = core.snapshot(packet['base'],'sha1'); hm,_ = core.snapshot(packet['head'],'sha1')
        number = packet['pull_request']; before = self.state(number)
        for side in ('base','head'):
            need(all(packet[side][k] == before['commits'][side][k] for k in ('commit','tree')), 'candidate origin mismatch')
        self.sources(before,packet)
        comments = self.intake(number); ci = self.ci(before,number)
        # Two complete reads detect changes during collection. Not an atomic
        # GitHub snapshot, and no guarantee after the final GET or while stopped.
        need(core.canonical(comments) == core.canonical(self.intake(number)), 'audit intake changed')
        need(core.canonical(ci) == core.canonical(self.ci(before,number)), 'CI changed during collection')
        need(core.canonical(before) == core.canonical(self.state(number)), 'PR or base changed during collection')
        return {'schema':'research-github-observation/v1',
            'binding':core.binding(packet,bm,hm), 'policy_paths':list(self.policy.policy_paths),
            'state':before, 'intake':comments, 'ci':ci,
            'merge_authorized':False, 'deployment_eligible':False,
            'durable_intake_registered':False}

    def verify_context(self, packet, checkpoint, report_inventory):
        # Deliberately cannot satisfy LedgerEvidenceBridge yet. Observation
        # persistence, all-report reconciliation and selection need a protected
        # registered-intake implementation, not caller assertions.
        raise core.IntegrationMissing('durable registered findings reconciliation and capture not implemented')
