"""Fork-capable read-only profile, preserving accepted reader methods otherwise.
All API requests stay in the protected base repository. No fork code is executed.
"""
import re
from dataclasses import asdict
from datetime import datetime, timezone
from urllib.parse import quote
import github_read_context as parent
from github_read_context import need,same_id,integer,oid,core

# This reviewed evidence profile is controller policy, never candidate input.
# The source-map digests prevent dropping an input pin while retaining the YAML.
SOURCE_BOUND_WORKFLOW = '.github/workflows/research-checks.yml'
SOURCE_BOUND_WORKFLOW_SHA256 = '6488391dc379a68e855234fccc933f6d71300dba67004112376bc2c15a1d5b23'
SOURCE_BOUND_PROFILES = {
    ('elliotglazer/diophantine-z-q', 1446122118, 407358539):
        'a5f6a33320b3b266e2ebd826a2f984506538fd6c7ba9fc763c6bb9e3b6ce2fe4',
    ('elliotglazer/private-diophantine', 1447509909, 408660600):
        'afd92925c4a26132e5d764a8a208f986488d7f50d920aee3a6b492221d8a934c',
}
SOURCE_BOUND_JOB_LABELS = {
    'Accepted Lean helpers and axiom audit': 'ubuntu-24.04',
    'Construction regeneration and finite checks': 'ubuntu-24.04',
    'Paper build': 'ubuntu-24.04',
    'Reconstructed quartic and Version 5 inventory': 'ubuntu-24.04',
    'Version 6 quartic reproduction and inventory': 'ubuntu-24.04',
    **{f'{name} ({os})': os
       for name in ('Version 9 odd-product replay', 'Version 12 source and quartic replay',
                    'Version 13 source and quartic replay')
       for os in ('ubuntu-24.04', 'windows-2022')},
}


def utc_time(value):
    need(type(value) is str and re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z', value),
         'source-bound CI requires UTC execution times')
    try:
        parsed = datetime.fromisoformat(value[:-1] + '+00:00')
    except ValueError:
        raise core.Invalid('source-bound CI requires valid execution times') from None
    need(parsed > datetime(1970, 1, 1, tzinfo=timezone.utc), 'source-bound CI requires positive execution times')
    return parsed


class ForkReadContext(parent.ReadContext):
    def source_stamp(self, state):
        return core.digest({'state': state, 'policy': asdict(self.policy)})

    def sources(self, state, packet):
        self._verified_source_stamp = None
        for side in ('base', 'head'):
            need(all(packet[side][key] == state['commits'][side][key] for key in ('commit', 'tree')),
                 'source verification context mismatch')
        # Retain the full existing base/head/merge blob checks and packet pins.
        super().sources(state, packet)
        self._verified_source_stamp = self.source_stamp(state)

    def empty_step_evidence(self, state, number, workflow, run, job):
        need(self.policy.source_transition is None,
             'source transitions require complete successful CI steps')
        need(getattr(self, '_verified_source_stamp', None) == self.source_stamp(state),
             'source-bound CI requires current source verification')
        need(same_id(state['pr'].get('number'), number), 'source-bound CI PR mismatch')
        profile = SOURCE_BOUND_PROFILES.get((self.policy.repository, self.policy.repository_id,
                                            workflow.workflow_id))
        need(profile is not None and workflow.path == SOURCE_BOUND_WORKFLOW and
             workflow.source_sha256.get(workflow.path) == SOURCE_BOUND_WORKFLOW_SHA256 and
             core.digest(workflow.source_sha256) == profile and not workflow.referenced_workflows,
             'CI step not actually successful: unapproved source-bound workflow profile')
        need(set(workflow.jobs) == set(SOURCE_BOUND_JOB_LABELS),
             'source-bound CI requires the complete reviewed job inventory')
        need(integer(job.get('id')) and integer(job.get('runner_id')) and
             core.text(job.get('runner_name')) and
             type(job.get('runner_group_id')) is int and job['runner_group_id'] >= 0 and
             core.text(job.get('runner_group_name')),
             'source-bound CI requires an assigned runner')
        need(job.get('labels') == [SOURCE_BOUND_JOB_LABELS[job['name']]],
             'source-bound CI runner labels mismatch')
        started = utc_time(job.get('started_at')); completed = utc_time(job.get('completed_at'))
        need(utc_time(run.get('run_started_at')) <= started < completed <= utc_time(run.get('updated_at')),
             'source-bound CI execution times are not ordered within the run')
        direct = self.api.one(self.root + '/actions/jobs/' + str(job['id']))
        need(core.canonical(direct) == core.canonical(job),
             'source-bound CI job detail disagrees with attempt listing')
        return {'job_id': job['id'], 'evidence_mode': 'source-bound-job-conclusion/v1',
                'steps_unavailable': True, 'workflow_sha256': SOURCE_BOUND_WORKFLOW_SHA256,
                'source_map_sha256': profile}

    def state(self, number):
        # A new state read cannot reuse a previous observation's source check.
        self._verified_source_stamp = None
        p = self.policy
        repository = self.api.one(self.root)
        need(repository.get('id') == p.repository_id and type(repository.get('id')) is int and repository.get('full_name') == p.repository, 'repository origin mismatch')
        pr = self.api.one(self.root + '/pulls/' + str(number))
        need(type(pr.get('number')) is int and pr['number'] == number and pr.get('state') == 'open' and pr.get('draft') is False and pr.get('merged') is False, 'PR not open and ready')
        need(same_id(pr['base']['repo']['id'],p.repository_id), 'PR base repository mismatch')
        head_repository=pr['head'].get('repo')
        need(type(head_repository) is dict and integer(head_repository.get('id')) and
             type(head_repository.get('full_name')) is str and re.fullmatch('[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',head_repository['full_name']) is not None,
             'missing authenticated fork repository identity')
        need(pr['base']['ref'] == p.base_ref, 'base branch mismatch')
        base = pr['base']['sha']; head = pr['head']['sha']; merge = pr.get('merge_commit_sha')
        need(all(oid(x) for x in (base, head, merge)), 'missing exact commit identity')
        pull_refs={}
        for label,sha in (('head',head),('merge',merge)):
            value=self.api.one(self.root+'/git/ref/pull/'+str(number)+'/'+label)
            need(value.get('ref')=='refs/pull/'+str(number)+'/'+label and value.get('object',{}).get('type')=='commit' and value['object'].get('sha')==sha,
                 'base repository pull ref mismatch')
            pull_refs[label]={'ref':value['ref'],'commit':sha}
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
        return self.bind_source_transition({'projection_schema':'github-pr-state/v3', 'repository_id':p.repository_id, 'pr':parent.project_pr(pr), 'commits':commits, 'pull_refs':pull_refs, 'head_repository':{'id':head_repository['id'],'full_name':head_repository['full_name']}})

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
            need(same_id(run.get('repository',{}).get('id'),self.policy.repository_id) and same_id(run.get('head_repository',{}).get('id'),state['head_repository']['id']), 'run repository mismatch')
            need(run.get('event') == 'pull_request', 'unsupported CI event')
            associations = run.get('pull_requests',[])
            need(any(same_id(r.get('number'),number) and r.get('base',{}).get('sha') == base and r.get('head',{}).get('sha') == head and same_id(r.get('base',{}).get('repo',{}).get('id'),self.policy.repository_id) and same_id(r.get('head',{}).get('repo',{}).get('id'),state['head_repository']['id']) for r in associations), 'CI not bound to exact PR base and head')
            need(run.get('status') == 'completed' and run.get('conclusion') == 'success', 'required run not successful')
            need(integer(run.get('run_attempt')), 'missing run attempt')
            need(core.canonical(run.get('referenced_workflows',[])) == core.canonical(list(w.referenced_workflows)), 'unapproved reusable workflow provenance')
            attempt = run['run_attempt']
            jobs = self.api.pages(self.root+'/actions/runs/'+str(run['id'])+'/attempts/'+str(attempt)+'/jobs','jobs')
            names = [j.get('name') for j in jobs]
            need(set(names) == set(w.jobs) and len(names) == len(w.jobs), 'missing duplicate or unregistered CI job')
            job_evidence = []
            for j in jobs:
                need(same_id(j.get('run_id'),run['id']) and same_id(j.get('run_attempt'),attempt) and j.get('head_sha') == head, 'job provenance mismatch')
                need(j.get('status') == 'completed' and j.get('conclusion') == 'success', 'required job not successful')
                steps = j.get('steps')
                need(type(steps) is list, 'CI step not actually successful: missing or malformed steps')
                if steps:
                    need(all(type(s) is dict and s.get('status') == 'completed' and
                             s.get('conclusion') == 'success' for s in steps),
                         'CI step not actually successful')
                    job_evidence.append({'job_id': j['id'], 'evidence_mode': 'api-step-conclusions',
                                         'steps_unavailable': False})
                else:
                    job_evidence.append(self.empty_step_evidence(state, number, w, run, j))
            result.append({'workflow':workflow,'run':parent.project_ci_run(run),'jobs':jobs,
                           'job_evidence':job_evidence,
                           'run_inventory':[parent.project_ci_run(item) for item in runs]})
        return result
