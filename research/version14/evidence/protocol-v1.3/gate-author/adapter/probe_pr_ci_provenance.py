"""Bounded read-only sample of existing PR runs and check-suite provenance."""
from pathlib import Path
import hashlib,importlib.util,json
from datetime import datetime,timezone
import github_read_context as g

def main():
    helper_path=Path(__file__).resolve().parents[2]/'quartic-version7-release/github.py'
    g.need(hashlib.sha256(helper_path.read_bytes()).hexdigest()=='99e962826f9f88e2dadac40680b3aa9553e578bc9c28389e65abd7f742631844','helper changed')
    spec=importlib.util.spec_from_file_location('approved_helper',helper_path)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    rows=[]
    try:
        client=g.GitHubHTTPS(helper.token());root='/repos/elliotglazer/diophantine-z-q'
        listed,_=client.get(root+'/actions/runs?event=pull_request&per_page=10&page=1')
        runs=listed['workflow_runs'];g.need(type(runs) is list and len(runs)<=10,'invalid run sample')
        selected=[r for r in runs if r.get('conclusion')=='success'][:3] or runs[:3]
        def associated(items):
            return [{'number':r.get('number'),'base_sha':r.get('base',{}).get('sha'),
                     'head_sha':r.get('head',{}).get('sha'),
                     'head_repository_id':r.get('head',{}).get('repo',{}).get('id')} for r in items]
        for item in selected:
            g.need(g.integer(item.get('id')),'invalid run ID')
            run,_=client.get(root+'/actions/runs/'+str(item['id']))
            row={k:run.get(k) for k in ('id','head_sha','head_branch','run_attempt','status','conclusion','check_suite_id')}
            row['head_repository_id']=run.get('head_repository',{}).get('id')
            row['run_associations']=associated(run.get('pull_requests',[]))
            if g.integer(run.get('check_suite_id')):
                suite,_=client.get(root+'/check-suites/'+str(run['check_suite_id']))
                row['suite']={'head_sha':suite.get('head_sha'),'conclusion':suite.get('conclusion'),
                              'pull_requests':associated(suite.get('pull_requests',[]))}
            if g.integer(run.get('run_attempt')):
                jobs,_=client.get(root+'/actions/runs/'+str(run['id'])+'/attempts/'+str(run['run_attempt'])+'/jobs?per_page=100&page=1')
                row['jobs']=[{'head_sha':j.get('head_sha'),'run_attempt':j.get('run_attempt'),'conclusion':j.get('conclusion')} for j in jobs['jobs']]
            rows.append(row)
    except Exception:
        print('PR provenance read-only probe failed without credential output.');return 2
    result={'schema':'pr-provenance-sample/v1','observed_at':datetime.now(timezone.utc).isoformat(),
            'probe_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'listed_total':listed.get('total_count'),'sampled_count':len(runs),'rows':rows,
            'complete_inventory':False,'merge_authorized':False}
    out=Path(__file__).resolve().parent/'live-probe-20261107/pr-ci-provenance.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result));return 0

if __name__=='__main__':raise SystemExit(main())
