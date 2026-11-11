"""Local synthetic-only test of frozen candidate; no remote API is imported or called."""
import copy,hashlib,json,sys,unittest
from pathlib import Path
O=Path(__file__).resolve().parent
I=O.parent/'v15-controller-integration-author-001'
sys.dont_write_bytecode=True
sys.path[:0]=[str(I/'candidate'/p)for p in ('controller','adapter','publisher','gate','immutable-cache')]
import namespace_lifecycle as n,state_routing as s
from git_state import canonical,Invalid
T=json.loads((O/'CUTOVER-INPUTS.pending.json').read_text())

class BootstrapTests(unittest.TestCase):
 def setUp(self):
  self.old=copy.deepcopy(T['old_route']);self.old['owners']={}
  self.new=copy.deepcopy(T['new_route']);self.new['owners']={}
  self.controller=('synthetic/controller',999,'a'*40)
  self.ob={'schema':'protocol-bootstrap-ref-observation/v1','repository':self.controller[0],'repository_id':999,'approved_controller_sha':'a'*40,'refs':{'protocol-state':'b'*40}}
 def review(self,ob=None):return {'decision':'accepted','subject_sha256':n.sha(canonical(ob or self.ob))}
 def prepare(self,ob=None,review=None):return n.prepare_bootstrap(self.new,ob or self.ob,review if review is not None else self.review(),self.controller,'b'*40)
 def test_exact_genesis_and_unchanged_inputs(self):
  before=copy.deepcopy((self.new,self.ob));files=self.prepare();idx=json.loads(files['state/index.json'])
  self.assertEqual(len(files),2);self.assertEqual(idx['generation'],0);self.assertIsNone(idx['parent'])
  for kind in ('operator','intake'):
   self.assertEqual(idx['checkpoints'][kind]['ledger_id'],T['namespace_ledger_ids']['protocol-state-v15'][kind]);self.assertEqual(idx['checkpoints'][kind]['sequence'],0)
  snap=json.loads(files['state/snapshots/'+idx['checkpoints']['publisher']['snapshot_sha256']+'.json'])
  self.assertEqual(snap['state']['generations'],[]);self.assertEqual(snap['state']['targets'],[])
  self.assertEqual(before,(self.new,self.ob));self.assertEqual(files,self.prepare())
 def test_existing_ref_rejected(self):
  self.ob['refs']['protocol-state-v15']='c'*40
  with self.assertRaises(Invalid):self.prepare()
 def test_retired_state_changed_rejected(self):
  self.ob['refs']['protocol-state']='c'*40
  with self.assertRaises(Invalid):self.prepare()
 def test_identity_changes_rejected(self):
  for key,value in [('repository','other/controller'),('repository_id',998),('approved_controller_sha','c'*40)]:
   ob=copy.deepcopy(self.ob);ob[key]=value
   with self.subTest(key=key),self.assertRaises(Invalid):self.prepare(ob,self.review(ob))
 def test_missing_or_stale_review_rejected(self):
  for rev in ({},{'decision':'pending','subject_sha256':self.review()['subject_sha256']},{'decision':'accepted','subject_sha256':'c'*64}):
   with self.subTest(review=rev),self.assertRaises(Invalid):self.prepare(review=rev)
 def test_pending_template_cannot_be_used(self):
  with self.assertRaises((Invalid,TypeError,AttributeError)):n.prepare_bootstrap(T['new_route'],T['bootstrap_observation'],T['bootstrap_review'],self.controller,None)
 def test_single_head_and_lifetime_ownership(self):
  import types
  key='1:2:3:'+('d'*40);self.old['owners'][key]='protocol-state';self.new['owners'][key]='protocol-state'
  cut={'old_branch':'protocol-state','old_state_commit':'b'*40,'old_index_sha256':'e'*64,'no_active_writers':True,'finalization_complete':True}
  self.assertTrue(s.transition(self.old,self.new,cut))
  pub=types.SimpleNamespace(app_id=1,installation_id=2,repository_id=3,target_mode='head')
  with self.assertRaises(Invalid):s.job(self.new,pub,{'head':{'commit':'d'*40}})
  self.new['owners'][key]='protocol-state-v15'
  with self.assertRaises(Invalid):s.transition(self.old,self.new,cut)
 def test_actual_ledger_names_distinct(self):
  cfg={'schema':'protocol-controller/v2','controller_repository':'synthetic/controller','controller_repository_id':999,'jobs':[],'state_routing':self.new}
  self.assertEqual(s.load(cfg),self.new)
  cfg['state_routing']['namespaces']['protocol-state-v15']['intake']=T['namespace_ledger_ids']['protocol-state']['intake']
  with self.assertRaises(Invalid):s.load(cfg)
 def test_transition_rejects_unfinished_or_missing_state(self):
  cut={'old_branch':'protocol-state','old_state_commit':'b'*40,'old_index_sha256':'e'*64,'no_active_writers':True,'finalization_complete':True}
  for k in ('old_state_commit','old_index_sha256','no_active_writers','finalization_complete'):
   c=copy.deepcopy(cut);c[k]=None
   with self.subTest(field=k),self.assertRaises(Invalid):s.transition(self.old,self.new,c)
 def test_full_offline_transition_from_synthetic_genesis(self):
  files=s.initial_files(self.old,{})
  idx=json.loads(files['state/index.json'])
  d={'schema':'protocol-namespace-export/v1','branch':'protocol-state','state_commit':'b'*40,'tree':'c'*40,'index_sha256':n.sha(files['state/index.json']),'files':{p:{'sha256':n.sha(v),'size':len(v)}for p,v in files.items()}}
  old={'schema':'protocol-controller/v1','controller_repository':'synthetic/controller','controller_repository_id':999,'jobs':[]}
  new=copy.deepcopy(old);new.update(schema='protocol-controller/v2',state_routing=self.new)
  cut={'old_branch':'protocol-state','old_state_commit':d['state_commit'],'old_index_sha256':d['index_sha256'],'no_active_writers':True,'finalization_complete':True}
  dh=n.sha(canonical(d));publishers={};keys={'operator':{},'intake':{}}
  subject={'old_config_sha256':n.sha(canonical(old)),'new_config_sha256':n.sha(canonical(new)),'export_sha256':dh,'old_route_sha256':n.sha(canonical(self.old)),'publishers_sha256':n.sha(canonical(publishers)),'cutover':cut}
  rev={'decision':'accepted','subject_sha256':n.sha(canonical(subject))}
  before=copy.deepcopy((files,old,new,cut))
  result=n.prepare_transition(old,new,d,files,dh,self.old,keys,publishers,cut,rev)
  self.assertEqual(result['required_protected_variable']['value'],n.sha(canonical(self.new)))
  self.assertEqual(before,(files,old,new,cut))
  changed=copy.deepcopy(cut);changed['old_state_commit']='d'*40
  with self.assertRaises(Invalid):n.prepare_transition(old,new,d,files,dh,self.old,keys,publishers,changed,rev)

if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(BootstrapTests))
 (O/'TEST-RESULT.json').write_text(json.dumps({'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'success':result.wasSuccessful(),'scope':'Synthetic local data only, using proposed real ledger names; no operational review or observed state asserted.'},indent=2)+'\n')
 sys.exit(not result.wasSuccessful())
