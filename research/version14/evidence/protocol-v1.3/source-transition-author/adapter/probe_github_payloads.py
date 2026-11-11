"""Opt-in, bounded authenticated GET probe. Never emits or stores credentials."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import github_read_context as g

REPOSITORIES=('elliotglazer/diophantine-z-q','elliotglazer/private-diophantine')

def probe(client, repository, event=None):
    g.need(repository in REPOSITORIES,'repository not permitted')
    g.need(event in (None,'pull_request'),'probe event unsupported')
    root='/repos/'+repository
    def get(path):
        value,_=client.get(root+path)
        return value
    repo=get('')
    g.need(g.integer(repo.get('id')) and repo.get('full_name')==repository,'probe repository mismatch')
    runs=get('/actions/runs?per_page=1&page=1'+('&event='+event if event else ''))
    g.need(type(runs.get('workflow_runs')) is list and len(runs['workflow_runs'])==1,'one run required for shape probe')
    candidate=runs['workflow_runs'][0]
    g.need(g.integer(candidate.get('id')),'invalid run ID')
    run=get('/actions/runs/'+str(candidate['id']))
    g.need(g.same_id(run.get('id'),candidate['id']) and g.integer(run.get('run_attempt')) and
           g.integer(run.get('workflow_id')),'missing run identity, workflow or attempt')
    g.need(event is None or run.get('event')==event,'probe run event mismatch')
    workflow=get('/actions/workflows/'+str(run['workflow_id']))
    jobs=get('/actions/runs/'+str(run['id'])+'/attempts/'+str(run['run_attempt'])+'/jobs?per_page=100&page=1')
    g.need(type(jobs.get('jobs')) is list and len(jobs['jobs'])<=100,'invalid jobs response')
    def digest(value):return hashlib.sha256(g.core.canonical(value)).hexdigest()
    return {'schema':'github-payload-shape-probe/v1','observed_at':datetime.now(timezone.utc).isoformat(),
        'probe_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'repository':repository,'repository_id':repo['id'],'run_id':run['id'],
        'workflow_path':workflow.get('path'),'run_path':run.get('path'),'event':run.get('event'),
        'run_attempt':run['run_attempt'],'head_sha':run.get('head_sha'),
        'run_pull_requests':run.get('pull_requests'),
        'jobs_total_count':jobs.get('total_count'),'jobs_page_count':len(jobs['jobs']),
        'jobs':[{'id':j.get('id'),'name':j.get('name'),'run_attempt_present':'run_attempt' in j,
                 'run_attempt':j.get('run_attempt'),'head_sha':j.get('head_sha'),
                 'step_conclusions':[s.get('conclusion') for s in j.get('steps',[])]} for j in jobs['jobs']],
        'response_sha256':{'repository':digest(repo),'run':digest(run),'workflow':digest(workflow),'jobs':digest(jobs)},
        'auth_basis':'existing operator Git credential via approved helper, fixed TLS API origin',
        'complete_ci_evaluation':False,'portable_authenticated_receipt':False,'merge_authorized':False}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--live-read',action='store_true')
    parser.add_argument('--helper',type=Path,required=True)
    parser.add_argument('--helper-sha256',required=True)
    parser.add_argument('--repository',choices=REPOSITORIES,required=True)
    parser.add_argument('--event',choices=('pull_request',))
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    g.need(args.live_read,'explicit live read required')
    raw=args.helper.read_bytes()
    g.need(hashlib.sha256(raw).hexdigest()==args.helper_sha256,'unapproved helper bytes')
    spec=importlib.util.spec_from_file_location('approved_credential_helper',args.helper)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    try:
        credential=helper.token()
        result=probe(g.GitHubHTTPS(credential),args.repository,args.event)
    except Exception:
        # Neither helper stderr nor response bodies are included in failures.
        print('Authenticated read-only probe failed; no compatibility conclusion.',file=sys.stderr)
        return 2
    finally:
        credential=None
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output),'run_id':result['run_id'],
        'run_path':result['run_path'],'workflow_path':result['workflow_path'],
        'job_attempt_fields':[j['run_attempt_present'] for j in result['jobs']],
        'merge_authorized':False}))
    return 0

if __name__=='__main__':raise SystemExit(main())
