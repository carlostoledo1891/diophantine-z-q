"""Manifest-input core tests. Synthetic receipts are never provenance evidence."""
import base64,contextlib,copy,hashlib,importlib.util,io,json,subprocess,sys,tempfile,unittest
from unittest.mock import patch
from pathlib import Path
import offline_manifest_gate as g
import git_manifest as m
H=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('v1_fixture_module',H.parent/'gate/test_offline_gate.py')
# The fixture module imports its sibling core. It is the pinned accepted source.
sys.path.insert(0,str(H.parent/'gate'))
v1=importlib.util.module_from_spec(spec);spec.loader.exec_module(v1)
sys.path.pop(0)

class Blobs:
    def __init__(self,values):self.values=values;self.reads=[]
    def open(self,side,path,entry):
        self.reads.append((side,path,entry['sha256']))
        if entry['sha256'] not in self.values:raise FileNotFoundError('missing fixture blob')
        return io.BytesIO(self.values[entry['sha256']])

def manifest(files,tag):
    # Build the same full tree as the v1 fixture, then give it a real commit object.
    inline=v1.make_snapshot(files,'1');tree=inline['tree']
    raw=('tree '+tree+'\nauthor Fixture <f@example.invalid> 0 +0000\ncommitter Fixture <f@example.invalid> 0 +0000\n\n'+tag+'\n').encode()
    entries={};values={}
    for path,value in files.items():
        mode,body=value if isinstance(value,tuple) else ('100644',value)
        rawhash=hashlib.sha256(body).hexdigest();values[rawhash]=body
        entries[path]={'mode':mode,'blob':hashlib.sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest(),'size':len(body),'sha256':rawhash}
    unique={v['blob']:v['size'] for v in entries.values()}
    return {'schema':'research-git-manifest/v1','git_hash':'sha1','commit':hashlib.sha1(b'commit '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
        'commit_raw_base64':base64.b64encode(raw).decode(),'tree':tree,'files':entries,
        'stats':{'file_count':len(entries),'path_bytes':sum(v['size'] for v in entries.values()),'unique_blobs':len(unique),'unique_blob_bytes':sum(unique.values())}},values

def refresh(p,e):
    base,_=g.snapshot(p['base'],'sha1');head,_=g.snapshot(p['head'],'sha1');e['binding']=g.binding(p,base,head)
    apps={a['id']:a for a in p['applications']};closures={}
    def dep(a):
        if a not in closures:closures[a]=g.digest({'application':apps[a],'dependencies':{d:dep(d) for d in sorted(apps[a]['dependencies'])}})
        return closures[a]
    for a in apps:dep(a)
    findings={f['id']:f for f in p['findings']}
    def fdep(f):
        d=f['duplicate_of']
        return g.digest({'applications':{a:closures[a] for a in sorted(f['applications'])},'duplicate_target':None if d is None else {'finding':findings[d],'dependencies':fdep(findings[d])}})
    def r(kind,target,targethash,dephash,run='reviewer'):
        report={'side':'head','path':'reviews/report.md','sha256':p['head']['files']['reviews/report.md']['sha256']}
        return {'id':kind+':'+target,'kind':kind,'target':target,'target_sha256':targethash,'dependency_sha256':dephash,
            'run_id':run,'decision':'accepted','scope':'Synthetic fixture','binding':copy.deepcopy(e['binding']),'report':report}
    e['receipts']=[r('application',a,g.digest(apps[a]),closures[a]) for a in apps]
    e['receipts'] += [r('finding',f['id'],g.digest(f),fdep(f)) for f in p['findings']]
    e['receipts'].append(r('assembly','complete',g.digest(p),g.digest(closures),'assembler'))

def fixture():
    p,e=v1.fixture();p['schema']=2;blobs={}
    for side in ('base','head'):
        files={path:(f['mode'],base64.b64decode(f['content_base64'])) for path,f in p[side]['files'].items()}
        p[side],values=manifest(files,side);blobs.update(values)
    refresh(p,e);return p,e,Blobs(blobs)

class ManifestGateTests(unittest.TestCase):
    def setUp(self):self.p,self.e,self.blobs=fixture()
    def run_core(self):return g.check_records(self.p,self.e,self.blobs)
    def rejects(self,code):
        with self.assertRaisesRegex(g.Invalid,code):self.run_core()
    def test_valid_full_manifests_and_actual_blob_reads(self):
        r=self.run_core();self.assertTrue(r['records_consistent']);self.assertFalse(r['merge_authorized']);self.assertFalse(r['deployment_eligible'])
        self.assertEqual(r['verified_evidence_blobs'],4);self.assertEqual(len(self.blobs.reads),4)
    def test_schema1_cannot_be_mislabelled(self):self.p['schema']=1;self.rejects('schema-version')
    def test_schema1_binding_cannot_be_reused(self):del self.e['binding']['record_schema'];self.rejects('stale-or-wrong-candidate-binding')
    def test_no_blob_reader_fails_closed(self):
        with self.assertRaisesRegex(g.IntegrationMissing,'blob-reader'):g.check_records(self.p,self.e)
    def test_no_authentication_adapter_fails_closed(self):
        with self.assertRaisesRegex(g.IntegrationMissing,'authentication'):g.validate_offline(self.p,blob_reader=self.blobs)
    def test_verified_adapter_still_no_merge(self):
        evidence=self.e
        class FixtureVerifier:
            def verify(self,p):return evidence
        self.assertFalse(g.validate_offline(self.p,FixtureVerifier(),self.blobs)['merge_authorized'])
    def test_v1_content_manifest_hash_compatibility(self):
        old,_=v1.fixture()
        for side in ('base','head'):
            oldmap,_=v1.g.snapshot(old[side],'sha1');newmap,_=g.snapshot(self.p[side],'sha1')
            self.assertEqual(oldmap,newmap);self.assertEqual(v1.g.digest(oldmap),g.digest(newmap))
    def test_wrong_commit_link(self):self.p['head']['commit']='0'*40;self.rejects('commit object mismatch')
    def test_omitted_full_manifest_path(self):del self.p['head']['files']['sources/input.md'];self.rejects('tree mismatch')
    def test_wrong_manifest_algorithm(self):self.p['git_hash']='sha256';self.rejects('snapshot-hash-algorithm')
    def test_missing_changed_path(self):self.p['changes']=[];self.rejects('incomplete-changed-file')
    def test_extra_changed_path(self):self.p['changes'].append({'path':'not-present','kind':'argument','applications':['B']});self.rejects('incomplete-changed-file')
    def test_duplicate_changed_path(self):self.p['changes']*=2;self.rejects('duplicate:changes')
    def test_mode_change_not_covered(self):
        self.p['head']['files']['sources/input.md']['mode']='100755'
        self.rejects('tree mismatch')
    def test_missing_obligation(self):del self.p['applications'][1]['obligations']['index_domain_coverage'];self.rejects('missing-obligation')
    def test_open_obligation(self):self.p['applications'][1]['obligations']['exceptional_cases']['status']='open';self.rejects('unresolved-obligation')
    def test_missing_dependency(self):self.p['applications'][1]['dependencies']=['no-such-app'];self.rejects('missing-dependency')
    def test_dependency_cycle(self):self.p['applications'][0]['dependencies']=['B'];self.rejects('dependency-cycle')
    def test_dependency_change_invalidates_unchanged_consumer(self):
        old=copy.deepcopy(self.e['receipts'][1]);self.p['applications'][0]['obligations']['source_hypotheses']['justification']='Changed premise';refresh(self.p,self.e)
        self.e['receipts'][1]=old;self.rejects('stale-review-content-or-dependencies')
    def test_same_agent_second_run_rejected(self):self.e['runs'][2]['agent_id']='authorB-agent';self.rejects('self-acceptance')
    def test_invented_authorship_rejected(self):self.p['applications'][1]['authors']=['reviewer'];self.rejects('authorship-mismatch')
    def test_missing_receipt(self):self.e['receipts'].pop(0);self.rejects('missing-or-extra-acceptance')
    def test_pending_receipt(self):self.e['receipts'][0]['decision']='pending';self.rejects('invalid-review')
    def test_missing_assembly(self):self.e['receipts'].pop();self.rejects('missing-or-extra-acceptance')
    def test_assembly_author_rejected(self):self.e['receipts'][-1]['run_id']='authorA';self.rejects('self-acceptance')
    def test_missing_finding(self):self.p['findings']=[];self.rejects('missing-or-extra-finding')
    def test_changed_finding(self):self.p['findings'][0]['body_sha256']='0'*64;self.rejects('changed-finding')
    def test_open_finding(self):self.p['findings'][0]['status']='open';self.rejects('unresolved-finding')
    def test_unreviewed_disposition(self):self.e['receipts'].pop(2);self.rejects('missing-or-extra-acceptance')
    def test_malformed_policy_directory(self):self.e['policy_paths'].append('gate//');self.rejects('policy-path')
    def test_policy_directory_root_is_protected(self):self.e['policy_paths'].append('proof.md/');self.rejects('unreviewed-policy-change')
    def test_boolean_evidence_binding(self):
        self.p['repository_id']=1;refresh(self.p,self.e);self.e['binding']['repository_id']=True;self.rejects('stale-or-wrong-candidate')
    def test_float_receipt_binding(self):self.e['receipts'][0]['binding']['repository_id']=123.0;self.rejects('stale-review-binding')
    def test_stale_base_binding(self):self.e['binding']['base_commit']='0'*40;self.rejects('stale-or-wrong-candidate')
    def test_stale_head_receipt(self):self.e['receipts'][0]['binding']['head_commit']='0'*40;self.rejects('stale-review-binding')
    def test_missing_evidence_blob(self):
        del self.blobs.values[self.p['head']['files']['proof.md']['sha256']];self.rejects('evidence-blob')
    def test_wrong_evidence_blob(self):
        self.blobs.values[self.p['head']['files']['proof.md']['sha256']]=b'wrong';self.rejects('evidence-blob')
    def test_report_blob_verified(self):
        self.blobs.values[self.p['head']['files']['reviews/report.md']['sha256']]=b'wrong';self.rejects('evidence-blob')
    def test_missing_empty_git_blob_is_not_success(self):
        entry={'mode':'100644','blob':m.object_hash('blob',b'','sha1'),'size':0,'sha256':m.sha(b'')}
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(['git','init','--bare',d],check=True,capture_output=True,env=m.git_environment())
            reader=g.GitBlobReader({'head':d})
            with self.assertRaisesRegex(OSError,'Git blob reader failed'):
                with contextlib.closing(reader.open('head','empty',entry)) as stream:
                    m.verify_blob(stream,entry,'sha1')
            subprocess.run(['git','-C',d,'hash-object','-w','--stdin'],input=b'',check=True,capture_output=True,env=m.git_environment())
            with contextlib.closing(reader.open('head','empty',entry)) as stream:
                self.assertTrue(m.verify_blob(stream,entry,'sha1'))
    def test_git_blob_timeout_is_not_success(self):
        class Process:
            stdout=io.BytesIO(b'');returncode=None;killed=False
            def poll(self):return self.returncode
            def wait(self,timeout=None):
                if not self.killed:raise subprocess.TimeoutExpired('git',timeout)
                self.returncode=-9;return -9
            def kill(self):self.killed=True
        proc=Process()
        entry={'mode':'100644','blob':m.object_hash('blob',b'','sha1'),'size':0,'sha256':m.sha(b'')}
        with patch.object(g.subprocess,'Popen',return_value=proc):
            with self.assertRaisesRegex(OSError,'timed out'):
                with contextlib.closing(g.GitBlobReader({'head':H}).open('head','empty',entry)) as stream:
                    m.verify_blob(stream,entry,'sha1')
        self.assertTrue(proc.killed)
    def test_base_blob_verified(self):
        self.blobs.values[self.p['base']['files']['proof.md']['sha256']]=b'wrong';self.rejects('evidence-blob')
    def test_transported_size_tampering(self):
        self.p['head']['files']['proof.md']['size']+=1;self.p['head']['stats']['path_bytes']+=1;self.p['head']['stats']['unique_blob_bytes']+=1
        refresh(self.p,self.e);self.rejects('evidence-blob')
    def test_large_unconsumed_blob_stays_in_full_binding(self):
        raw=b'x'*(9*1024*1024)
        for side in ('base','head'):
            files={path:(entry['mode'],self.blobs.values[entry['sha256']]) for path,entry in self.p[side]['files'].items()}
            files['archive.bin']=raw;self.p[side],values=manifest(files,side);self.blobs.values.update(values)
        refresh(self.p,self.e);r=self.run_core();self.assertEqual(r['verified_evidence_blobs'],4)
        self.assertNotIn('archive.bin',[x[1] for x in self.blobs.reads])
        self.p['head']['files'].pop('archive.bin');self.rejects('tree mismatch')
    def test_cli_structural_preview_stays_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);p=root/'p.json';e=root/'e.json';store=root/'blobs';store.mkdir()
            p.write_text(json.dumps(self.p));e.write_text(json.dumps(self.e))
            for key,raw in self.blobs.values.items():(store/key).write_bytes(raw)
            r=subprocess.run([sys.executable,'-B',str(H/'offline_manifest_gate.py'),str(p),'--unverified-evidence',str(e),'--blob-directory',str(store)],capture_output=True,text=True)
            self.assertEqual(r.returncode,2);self.assertTrue(json.loads(r.stdout)['records_consistent']);self.assertFalse(json.loads(r.stdout)['merge_authorized'])

if __name__=='__main__':unittest.main(verbosity=2)
