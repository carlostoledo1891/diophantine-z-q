"""Synthetic operator-ledger tests; no actual keys or reviews are created."""
import base64,copy,hashlib,unittest
import operator_ledger as l

def b64(raw):return base64.b64encode(raw).decode()
def observation(n):return {'capture_id':'fixture-capture-'+str(n),'tool':'collaboration','raw_base64':b64(('SYNTHETIC tool observation '+str(n)).encode())}
def binding():
 return {'record_schema':2,'repository_id':1,'pull_request':2,'git_hash':'sha1','policy_sha256':'a'*64,
  'base_commit':'1'*40,'base_tree':'2'*40,'head_commit':'3'*40,'head_tree':'4'*40,
  'base_manifest_sha256':'b'*64,'head_manifest_sha256':'c'*64}
def run_event(run,agent,n):return {'kind':'run_observed','observation':observation(n),'run_id':run,'agent_id':agent,'model':'fixture-model','tools':['read']}
def freeze_event(n=3):return {'kind':'target_frozen','observation':observation(n),'freeze_id':'freeze1','target_kind':'application','target_id':'A','target_sha256':'d'*64,'dependency_sha256':'e'*64,'binding':binding(),'author_runs':['author-run']}
def report_event(n=4):return {'kind':'report_observed','observation':observation(n),'report_id':'report1','run_id':'review-run','freeze_id':'freeze1','decision':'accepted','scope':'Synthetic scope','body_base64':b64(b'SYNTHETIC original report bytes\r\n')}

class LedgerTests(unittest.TestCase):
 def setUp(self):
  self.keys={'fixture-key':{'operator_id':'fixture-operator','secret':b'\x11'*32}}
  self.entries=[];self.checkpoint=l.genesis('fixture-ledger')
  for event in [run_event('author-run','author-agent',1),run_event('review-run','review-agent',2),freeze_event(),report_event()]:self.add(event)
 def add(self,event,key='fixture-key'):
  self.entries,self.checkpoint=l.append(self.entries,event,key,self.keys,self.checkpoint)
 def target(self):return {k:freeze_event()[k] for k in ['target_kind','target_id','target_sha256','dependency_sha256','binding']}
 def export(self):return l.export_receipt(self.entries,'report1',self.target(),self.keys,self.checkpoint)
 def rejects_verify(self,text):
  with self.assertRaisesRegex(l.Invalid,text):l.verify(self.entries,self.keys,self.checkpoint)
 def test_valid_receipt_original_bytes(self):
  r=self.export();self.assertFalse(r['merge_authorized']);self.assertFalse(r['provider_cryptographic_attestation'])
  self.assertEqual(r['attestation_basis'],'trusted operator observation')
  self.assertEqual(base64.b64decode(r['body_base64']),b'SYNTHETIC original report bytes\r\n')
  self.assertEqual(r['report_sha256'],hashlib.sha256(b'SYNTHETIC original report bytes\r\n').hexdigest())
 def test_no_registry_fails_closed(self):
  with self.assertRaises(l.IntegrationMissing):l.verify(self.entries,expected_checkpoint=self.checkpoint)
 def test_no_checkpoint_fails_closed(self):
  with self.assertRaises(l.IntegrationMissing):l.verify(self.entries,self.keys)
 def test_truncation_rejected(self):self.entries.pop();self.rejects_verify('truncation')
 def test_removed_middle_rejected(self):self.entries.pop(1);self.rejects_verify('truncation')
 def test_reordering_rejected(self):self.entries[0],self.entries[1]=self.entries[1],self.entries[0];self.rejects_verify('sequence/hash')
 def test_body_tamper_rejected(self):self.entries[-1]['event']['body_base64']=b64(b'altered');self.rejects_verify('authentication')
 def test_operator_tamper_rejected(self):self.entries[-1]['operator_id']='candidate';self.rejects_verify('identity mismatch')
 def test_wrong_key_rejected(self):self.keys['fixture-key']['secret']=b'\x12'*32;self.rejects_verify('authentication')
 def test_unknown_key_rejected(self):self.keys={};self.rejects_verify('unknown operator key')
 def test_wrong_checkpoint_rejected(self):self.checkpoint['entry_sha256']='0'*64;self.rejects_verify('checkpoint')
 def test_wrong_ledger_rejected(self):self.checkpoint['ledger_id']='different-ledger';self.rejects_verify('wrong ledger')
 def test_boolean_sequence_rejected(self):self.checkpoint['sequence']=True;self.rejects_verify('checkpoint position')
 def test_no_candidate_verified_flag(self):
  event=report_event(5);event['report_id']='other';event['verified']=True
  with self.assertRaisesRegex(l.Invalid,'schema'):self.add(event)
 def test_duplicate_capture_rejected(self):
  with self.assertRaisesRegex(l.Invalid,'capture'):self.add(run_event('new','new-agent',1))
 def test_duplicate_run_rejected(self):
  with self.assertRaisesRegex(l.Invalid,'run identity'):self.add(run_event('author-run','renamed-agent',5))
 def test_unknown_author_rejected(self):
  f=freeze_event(5);f['freeze_id']='f2';f['author_runs']=['unobserved']
  with self.assertRaisesRegex(l.Invalid,'authorship'):self.add(f)
 def test_unobserved_reviewer_rejected(self):
  r=report_event(5);r['report_id']='r2';r['run_id']='invented-reviewer'
  with self.assertRaisesRegex(l.Invalid,'unobserved'):self.add(r)
 def test_same_agent_second_run_rejected(self):
  self.add(run_event('second-author-run','author-agent',5));r=report_event(6);r.update(report_id='r2',run_id='second-author-run');self.add(r)
  with self.assertRaisesRegex(l.Invalid,'authoring agent'):l.export_receipt(self.entries,'r2',self.target(),self.keys,self.checkpoint)
 def test_self_report_preserved_but_not_independent_acceptance(self):
  r=report_event(5);r.update(report_id='self',run_id='author-run');self.add(r)
  state=l.verify(self.entries,self.keys,self.checkpoint);self.assertIn('self',state['reports'])
  with self.assertRaisesRegex(l.Invalid,'authoring agent'):l.export_receipt(self.entries,'self',self.target(),self.keys,self.checkpoint)
 def test_incomplete_report_preserved_not_exported(self):
  r=report_event(5);r.update(report_id='incomplete',decision='incomplete');self.add(r)
  with self.assertRaisesRegex(l.Invalid,'does not accept'):l.export_receipt(self.entries,'incomplete',self.target(),self.keys,self.checkpoint)
 def test_reviewer_retraction_invalidates_old_acceptance(self):
  r=report_event(5);r.update(report_id='retraction',decision='changes_required');self.add(r)
  with self.assertRaisesRegex(l.Invalid,'superseded'):self.export()
  self.assertIn('report1',l.verify(self.entries,self.keys,self.checkpoint)['reports'])
 def test_new_run_of_same_agent_can_retract(self):
  self.add(run_event('review-again','review-agent',5));r=report_event(6)
  r.update(report_id='retraction',run_id='review-again',decision='rejected');self.add(r)
  with self.assertRaisesRegex(l.Invalid,'superseded'):self.export()
 def test_stale_candidate_binding_rejected(self):
  target=self.target();target['binding']['head_commit']='f'*40
  with self.assertRaisesRegex(l.Invalid,'stale or wrong'):l.export_receipt(self.entries,'report1',target,self.keys,self.checkpoint)
 def test_stale_dependency_rejected(self):
  target=self.target();target['dependency_sha256']='f'*64
  with self.assertRaisesRegex(l.Invalid,'stale or wrong'):l.export_receipt(self.entries,'report1',target,self.keys,self.checkpoint)
 def test_float_binding_rejected(self):
  target=self.target();target['binding']['repository_id']=1.0
  with self.assertRaisesRegex(l.Invalid,'identity'):l.export_receipt(self.entries,'report1',target,self.keys,self.checkpoint)
 def test_refreshed_authorship_invalidates_old_freeze(self):
  f=freeze_event(5);f.update(freeze_id='new-freeze',author_runs=['author-run','review-run']);self.add(f)
  with self.assertRaisesRegex(l.Invalid,'refreshed'):self.export()
 def test_refreshed_target_requires_new_report(self):
  f=freeze_event(5);f.update(freeze_id='new-freeze',dependency_sha256='f'*64);self.add(f)
  r=report_event(6);r.update(report_id='new-report',freeze_id='new-freeze');self.add(r)
  target=self.target();target['dependency_sha256']='f'*64
  self.assertEqual(l.export_receipt(self.entries,'new-report',target,self.keys,self.checkpoint)['report_id'],'new-report')
 def test_key_rotation_preserves_identity_and_chain(self):
  self.keys['next-key']={'operator_id':'same-trusted-operator','secret':b'\x22'*32}
  self.add(run_event('new-run','new-agent',5),'next-key')
  self.assertIn('new-run',l.verify(self.entries,self.keys,self.checkpoint)['runs'])
 def test_prior_checkpoint_cannot_verify_extension(self):
  old=dict(self.checkpoint);self.add(run_event('new-run','new-agent',5))
  with self.assertRaisesRegex(l.Invalid,'unexpected extension'):l.verify(self.entries,self.keys,old)
 def test_hash_chain_rejects_forged_tail_without_operator_key(self):
  e=copy.deepcopy(self.entries[-1]);e['sequence']=5;e['previous_sha256']=self.checkpoint['entry_sha256'];e['event']['report_id']='forged';e['event']['observation']=observation(5)
  self.entries.append(e);self.checkpoint['sequence']=5;self.checkpoint['entry_sha256']=l.digest(e)
  self.rejects_verify('authentication')
 def test_append_does_not_mutate_existing_list(self):
  original=list(self.entries);n,_=l.append(self.entries,run_event('another','another-agent',5),'fixture-key',self.keys,self.checkpoint)
  self.assertEqual(self.entries,original);self.assertEqual(len(n),len(original)+1)

if __name__=='__main__':unittest.main(verbosity=2)
