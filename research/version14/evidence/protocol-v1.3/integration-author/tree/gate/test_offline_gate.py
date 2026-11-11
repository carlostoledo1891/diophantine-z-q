"""Synthetic tests only. Fixture receipts are not authenticated research reviews."""
import base64
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import offline_gate as g

H=Path(__file__).resolve().parent

def make_snapshot(files, commit, algorithm='sha1'):
    nodes={}
    result={}
    for path,value in files.items():
        mode,raw=value if isinstance(value,tuple) else ('100644',value)
        result[path]={'mode':mode,'content_base64':base64.b64encode(raw).decode()}
        node=nodes
        parts=path.split('/')
        for part in parts[:-1]:node=node.setdefault(part,{})
        node[parts[-1]]=(mode,hashlib.new(algorithm,b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest())
    def tree(node):
        rows=[]
        for name,v in node.items():
            folder=isinstance(v,dict)
            mode,oid=('40000',tree(v)) if folder else v
            raw=mode.encode()+b' '+name.encode()+b'\0'+bytes.fromhex(oid)
            rows.append((name.encode()+(b'/' if folder else b''),raw))
        raw=b''.join(row for _,row in sorted(rows))
        return hashlib.new(algorithm,b'tree '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    return {'commit':commit*(40 if algorithm=='sha1' else 64),'tree':tree(nodes),'files':result}

def pin(packet,side,path):
    raw=base64.b64decode(packet[side]['files'][path]['content_base64'])
    return {'side':side,'path':path,'sha256':hashlib.sha256(raw).hexdigest()}

def refresh(packet,evidence):
    """Fixture-only new external receipts; never called by the validator."""
    bm,_=g.snapshot(packet['base'],'sha1');hm,_=g.snapshot(packet['head'],'sha1')
    evidence['binding']=g.binding(packet,bm,hm)
    apps={a['id']:a for a in packet['applications']}
    closures={}
    def closure(a):
        if a not in closures:
            closures[a]=g.digest({'application':apps[a],'dependencies':{d:closure(d) for d in sorted(apps[a]['dependencies'])}})
        return closures[a]
    for a in apps:closure(a)
    receipts=[]
    def receipt(kind,target,target_hash,deps,reviewer='reviewer'):
        receipts.append({'id':kind+':'+target,'kind':kind,'target':target,
            'target_sha256':target_hash,'dependency_sha256':deps,'run_id':reviewer,
            'decision':'accepted','scope':'Synthetic fixture scope only.',
            'binding':copy.deepcopy(evidence['binding']), 'report':pin(packet,'head','reviews/report.md')})
    for a in apps:receipt('application',a,g.digest(apps[a]),closures[a])
    findings={f['id']:f for f in packet['findings']}
    def fdeps(f):
        target=f['duplicate_of']
        return g.digest({'applications':{a:closures[a] for a in sorted(f['applications'])},
            'duplicate_target':None if target is None else {'finding':findings[target],'dependencies':fdeps(findings[target])}})
    for f in packet['findings']:
        receipt('finding',f['id'],g.digest(f),fdeps(f))
    receipt('assembly','complete',g.digest(packet),g.digest(closures),'assembler')
    evidence['receipts']=receipts

def fixture():
    files={'proof.md':b'Old argument\n','sources/input.md':b'Fixed source statement\n','reviews/report.md':b'Synthetic review report\n','policy.md':b'Policy fixture\n'}
    packet={'schema':1,'repository_id':123,'pull_request':7,'git_hash':'sha1','policy_sha256':g.sha(files['policy.md']),
        'base':make_snapshot(files,'1'),'head':make_snapshot(dict(files,**{'proof.md':b'New reviewed argument\n'}),'2'),
        'changes':[{'path':'proof.md','kind':'argument','applications':['B']}], 'applications':[],
        'findings':[{'id':'F1','body_sha256':g.sha(b'Original objection'), 'status':'repaired','reason':'The reviewed argument supplies the missing map.',
            'authors':['authorB'],'applications':['B'],'duplicate_of':None}]}
    for aid,path,author,deps,kind in [('A','sources/input.md','authorA',[],'source'),('B','proof.md','authorB',['A'],'argument')]:
        pins=[pin(packet,s,path) for s in ('base','head')]
        obligations={k:{'status':'checked','required':'Exact input','constructed':'Exact supplied input',
            'justification':'Synthetic derivation for fixture only.','evidence':[pins[1]]} for k in g.OBLIGATIONS}
        packet['applications'].append({'id':aid,'kind':kind,'authors':[author],'dependencies':deps,'files':pins,'obligations':obligations})
    evidence={'binding':{},'policy_paths':['policy.md','.github/','gate/'],
        'runs':[{'id':r,'agent_id':r+'-agent','reviewer_type':'model','model':'synthetic-test-model','tools':['read']} for r in ('authorA','authorB','reviewer','assembler')],
        'authorship':{'application:A':['authorA'],'application:B':['authorB'],'finding:F1':['authorB']},
        'findings':[{'id':'F1','body_sha256':packet['findings'][0]['body_sha256']}], 'receipts':[]}
    refresh(packet,evidence)
    return packet,evidence

class GateTests(unittest.TestCase):
    def setUp(self):self.p,self.e=fixture()
    def rejects(self,code):
        with self.assertRaisesRegex(g.Invalid,code):g.check_records(self.p,self.e)
    def test_valid_records_without_human_approval(self):
        r=g.check_records(self.p,self.e)
        self.assertTrue(r['records_consistent']);self.assertFalse(r['merge_authorized'])
        self.assertIn('NOT CHECKED',r['authentication'])
    def test_missing_authentication_adapter(self):
        with self.assertRaises(g.IntegrationMissing):g.validate_offline(self.p)
    def test_adapter_is_explicit_and_still_not_merge_authority(self):
        evidence=self.e
        class SyntheticVerifier:
            def verify(self,packet):return copy.deepcopy(evidence)
        r=g.validate_offline(self.p,SyntheticVerifier())
        self.assertFalse(r['merge_authorized']);self.assertEqual(r['live_github_state'],'NOT IMPLEMENTED')
    def test_bad_verifier_propagates_failure(self):
        class Bad:
            def verify(self,packet):raise g.Invalid('unauthenticated')
        with self.assertRaisesRegex(g.Invalid,'unauthenticated'):g.validate_offline(self.p,Bad())
    def test_known_git_blob_and_empty_tree(self):
        self.assertEqual(g.git_object('blob',b'hello\n','sha1'),'ce013625030ba8dba906f756967f9e9ca394464a')
        self.assertEqual(g.git_object('tree',b'','sha1'),'4b825dc642cb6eb9a060e54bf8d69288fbee4904')
    def test_tree_mismatch(self):self.p['head']['tree']='0'*40;self.rejects('git-tree-mismatch')
    def test_sha256_git_snapshot(self):
        snap=make_snapshot({'a/b':b'content'},'4','sha256')
        manifest,raw=g.snapshot(snap,'sha256')
        self.assertEqual(raw['a/b'],b'content');self.assertEqual(len(manifest['a/b']['blob']),64)
    def test_stale_head(self):self.p['head']['commit']='3'*40;self.rejects('stale-or-wrong-candidate')
    def test_stale_base(self):self.p['base']['commit']='3'*40;self.rejects('stale-or-wrong-candidate')
    def test_cross_repository_receipt(self):self.p['repository_id']=999;self.rejects('stale-or-wrong-candidate')
    def test_missing_changed_path(self):self.p['changes']=[];self.rejects('incomplete-changed-file')
    def test_duplicate_changed_path(self):self.p['changes']*=2;self.rejects('duplicate:changes')
    def test_deleted_path_requires_base_review(self):
        raw={'proof.md':b'Old argument\n','sources/input.md':b'Fixed source statement\n','reviews/report.md':b'Synthetic review report\n','policy.md':b'Policy fixture\n'}
        del raw['proof.md'];self.p['head']=make_snapshot(raw,'2')
        b=self.p['applications'][1];b['files']=[pin(self.p,'base','proof.md')]
        for v in b['obligations'].values():v['evidence']=copy.deepcopy(b['files'])
        refresh(self.p,self.e)
        self.assertTrue(g.check_records(self.p,self.e)['records_consistent'])
        b['files']=[pin(self.p,'head','reviews/report.md')]
        for v in b['obligations'].values():v['evidence']=copy.deepcopy(b['files'])
        self.rejects('unbound-change')
    def test_mode_only_change_is_in_inventory(self):
        self.p['head']['files']['sources/input.md']['mode']='100755'
        raw={p:(v['mode'],base64.b64decode(v['content_base64'])) for p,v in self.p['head']['files'].items()}
        self.p['head']=make_snapshot(raw,'2');refresh(self.p,self.e)
        self.rejects('incomplete-changed-file')
    def test_rename_requires_both_paths(self):
        raw={p:base64.b64decode(v['content_base64']) for p,v in self.p['head']['files'].items()}
        raw['moved/proof.md']=raw.pop('proof.md');self.p['head']=make_snapshot(raw,'2')
        refresh(self.p,self.e);self.rejects('incomplete-changed-file')
        self.p['changes'].append({'path':'moved/proof.md','kind':'argument','applications':['B']})
        app=self.p['applications'][1];app['files']=[pin(self.p,'base','proof.md'),pin(self.p,'head','moved/proof.md')]
        for obligation in app['obligations'].values():obligation['evidence']=[app['files'][1]]
        refresh(self.p,self.e);self.assertTrue(g.check_records(self.p,self.e)['records_consistent'])
    def test_symlink_rejected(self):self.p['head']['files']['proof.md']['mode']='120000';self.rejects('unsupported-file-mode')
    def test_unsafe_path_rejected(self):self.p['head']['files']['../outside']={'mode':'100644','content_base64':''};self.rejects('unsafe-path')
    def test_case_collision_rejected(self):self.p['head']['files']['PROOF.md']=self.p['head']['files']['proof.md'];self.rejects('case-collision')
    def test_missing_dependency(self):self.p['applications'][1]['dependencies']=['absent'];self.rejects('missing-dependency')
    def test_dependency_cycle(self):self.p['applications'][0]['dependencies']=['B'];self.rejects('dependency-cycle')
    def test_changed_dependency_invalidates_consumer(self):
        old=copy.deepcopy(self.e['receipts']);self.p['applications'][0]['obligations']['source_hypotheses']['justification']='Changed premise'
        refresh(self.p,self.e)
        self.e['receipts'][1]=old[1]
        self.rejects('stale-review-content-or-dependencies')
    def test_missing_obligation(self):del self.p['applications'][1]['obligations']['index_domain_coverage'];self.rejects('missing-obligation')
    def test_empty_reason_not_applicable(self):
        self.p['applications'][1]['obligations']['index_domain_coverage'].update(status='not_applicable',justification='')
        self.rejects('empty-obligation')
    def test_unknown_author_run(self):self.p['applications'][1]['authors']=['invented'];self.rejects('unknown-author-run')
    def test_mismatched_authorship(self):self.p['applications'][1]['authors']=['authorA'];self.rejects('authorship-mismatch')
    def test_same_agent_second_run_is_not_independent(self):
        self.e['runs'][2]['agent_id']='authorB-agent';self.rejects('self-acceptance')
    def test_missing_receipt(self):self.e['receipts'].pop(0);self.rejects('missing-or-extra-acceptance')
    def test_stale_receipt_binding(self):self.e['receipts'][0]['binding']['head_commit']='0'*40;self.rejects('stale-review-binding')
    def test_evidence_binding_rejects_boolean_integer_alias(self):
        self.p['repository_id']=1;refresh(self.p,self.e)
        self.e['binding']['repository_id']=True;self.rejects('stale-or-wrong-candidate-binding')
    def test_evidence_binding_rejects_float_integer_alias(self):
        self.e['binding']['pull_request']=7.0;self.rejects('stale-or-wrong-candidate-binding')
    def test_receipt_binding_rejects_boolean_integer_alias(self):
        self.p['pull_request']=1;refresh(self.p,self.e)
        self.e['receipts'][0]['binding']['pull_request']=True;self.rejects('stale-review-binding')
    def test_receipt_binding_rejects_float_integer_alias(self):
        self.e['receipts'][0]['binding']['repository_id']=123.0;self.rejects('stale-review-binding')
    def test_changed_report(self):self.e['receipts'][0]['report']['sha256']='0'*64;self.rejects('stale-file-pin')
    def test_unaccepted_decision(self):self.e['receipts'][0]['decision']='pending';self.rejects('invalid-review-decision')
    def test_missing_assembly(self):self.e['receipts'].pop();self.rejects('missing-or-extra-acceptance')
    def test_assembly_author_cannot_self_accept(self):self.e['receipts'][-1]['run_id']='authorA';self.rejects('self-acceptance')
    def test_omitted_finding(self):self.p['findings']=[];self.rejects('missing-or-extra-finding')
    def test_changed_finding(self):self.p['findings'][0]['body_sha256']='0'*64;self.rejects('changed-finding')
    def test_open_finding(self):self.p['findings'][0]['status']='open';self.rejects('unresolved-finding')
    def test_unreviewed_finding_disposition(self):self.e['receipts'].pop(2);self.rejects('missing-or-extra-acceptance')
    def test_duplicate_self_link(self):self.p['findings'][0].update(status='duplicate',duplicate_of='F1');self.rejects('invalid-duplicate-finding')
    def test_duplicate_finding_tracks_target_changes(self):
        f=copy.deepcopy(self.p['findings'][0]);f.update(id='F2',status='duplicate',duplicate_of='F1')
        self.p['findings'].append(f);self.e['findings'].append({'id':'F2','body_sha256':f['body_sha256']})
        self.e['authorship']['finding:F2']=['authorB'];refresh(self.p,self.e)
        self.assertTrue(g.check_records(self.p,self.e)['records_consistent'])
        old=next(copy.deepcopy(r) for r in self.e['receipts'] if r['kind']=='finding' and r['target']=='F2')
        self.p['findings'][0]['reason']='New rebuttal evidence changes the target disposition.'
        refresh(self.p,self.e)
        self.e['receipts']=[old if r['kind']=='finding' and r['target']=='F2' else r for r in self.e['receipts']]
        self.rejects('stale-review-content-or-dependencies')
    def test_cyclic_duplicate_findings(self):
        f=copy.deepcopy(self.p['findings'][0]);f.update(id='F2',status='duplicate',duplicate_of='F1')
        self.p['findings'].append(f);self.e['findings'].append({'id':'F2','body_sha256':f['body_sha256']})
        self.e['authorship']['finding:F2']=['authorB']
        self.p['findings'][0].update(status='duplicate',duplicate_of='F2');self.rejects('finding-cycle')
    def test_finding_without_repair_application(self):self.p['findings'][0]['applications']=[];self.rejects('missing-resolution-application')
    def test_explicit_reviewed_out_of_scope_disposition(self):
        self.p['findings'][0].update(status='out_of_scope',applications=[],reason='Does not concern any claimed result in this synthetic fixture.')
        refresh(self.p,self.e);self.assertTrue(g.check_records(self.p,self.e)['records_consistent'])
    def test_policy_file_cannot_be_classified_editorial(self):
        self.e['policy_paths'].append('proof.md');self.p['changes'][0]['kind']='editorial';self.p['applications'][1]['kind']='editorial'
        self.rejects('unreviewed-policy-change')
    def test_policy_directory_marker_cannot_repeat(self):
        self.e['policy_paths'].append('gate//');self.rejects('policy-path')
    def test_policy_directory_protects_root_file(self):
        self.e['policy_paths'].append('proof.md/');self.rejects('unreviewed-policy-change')
    def test_policy_directory_does_not_match_sibling_prefix(self):
        self.e['policy_paths'].append('proof/')
        self.assertTrue(g.check_records(self.p,self.e)['records_consistent'])
    def test_valid_old_policy_reviewed_transition(self):
        self.e['policy_paths'].append('proof.md');self.p['changes'][0]['kind']='policy';self.p['applications'][1]['kind']='policy'
        refresh(self.p,self.e);self.assertTrue(g.check_records(self.p,self.e)['records_consistent'])
    def test_unknown_verified_flag_is_not_authentication(self):self.e['verified']=True;self.rejects('schema:evidence')
    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'x.json';path.write_text('{"a":1,"a":2}')
            with self.assertRaisesRegex(g.Invalid,'duplicate-json-key'):g.read_json(path)
    def test_cli_never_authorizes_merge_or_exits_success(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'packet.json';e=Path(d)/'evidence.json';p.write_text(json.dumps(self.p));e.write_text(json.dumps(self.e))
            r=subprocess.run([sys.executable,'-B',str(H/'offline_gate.py'),str(p),'--unverified-evidence',str(e)],capture_output=True,text=True)
            self.assertEqual(r.returncode,2);self.assertFalse(json.loads(r.stdout)['merge_authorized'])
            r=subprocess.run([sys.executable,'-B',str(H/'offline_gate.py'),str(p)],capture_output=True,text=True)
            self.assertEqual(r.returncode,2);self.assertIn('adapter-not-implemented',r.stdout)

if __name__=='__main__':unittest.main(verbosity=2)
