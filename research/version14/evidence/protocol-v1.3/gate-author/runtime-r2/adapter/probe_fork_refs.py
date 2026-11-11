"""Fixed, bounded read-only fork-ref shape probe. No candidate code execution."""
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
        for number in (5,6):
            pr,_=client.get(root+'/pulls/'+str(number));head=pr['head']['sha']
            g.need(g.oid(head),'invalid fork head')
            row={'number':number,'head_sha':head,'head_repository_id':pr['head']['repo']['id'],
                'head_repository':pr['head']['repo']['full_name'],'base_sha':pr['base']['sha'],
                'merge_commit_sha':pr.get('merge_commit_sha'),'observed_at':datetime.now(timezone.utc).isoformat()}
            for label,path in [('head_ref','/git/ref/pull/'+str(number)+'/head'),
                               ('merge_ref','/git/ref/pull/'+str(number)+'/merge'),
                               ('head_commit_in_base','/git/commits/'+head)]:
                try:
                    value,_=client.get(root+path)
                    row[label]={'response_sha256':g.core.digest(value),
                                **({k:value.get(k) for k in ('ref','object')} if label.endswith('_ref') else
                                   {k:value.get(k) for k in ('sha','tree','parents')})}
                except g.core.Invalid:
                    row[label]={'available':False}
            rows.append(row)
    except Exception:
        print('Fork-ref read-only probe failed without credential output.');return 2
    result={'schema':'fork-ref-shape-probe/v1','probe_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'rows':rows,'complete_gate_evaluation':False,'merge_authorized':False}
    path=Path(__file__).resolve().parent/'live-probe-20261107/fork-refs.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(path),'refs':[{'number':r['number'],'head_ref':r['head_ref'].get('ref'),
                       'merge_ref':r['merge_ref'].get('ref'),'head_commit':r['head_commit_in_base'].get('sha')} for r in rows]}))
    return 0

if __name__=='__main__':raise SystemExit(main())
