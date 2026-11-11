"""Fixture-only local-store and evidence-bridge integration tests."""
import base64,copy,concurrent.futures,json,shutil,sqlite3,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import operator_ledger as l
from protected_ledger_store import ProtectedPath,SQLiteAnchor,LedgerStore,Conflict,RecoveryRequired,connect
from ledger_evidence_bridge import VerifiedContext,LedgerEvidenceBridge,inventory
import test_manifest_gate as fixtures

def observation(n):return {'capture_id':'synthetic-'+str(n),'tool':'operator_capture','raw_base64':base64.b64encode(('SYNTHETIC '+str(n)).encode()).decode()}
def run(n):return {'kind':'run_observed','observation':observation(n),'run_id':'run'+str(n),'agent_id':'agent'+str(n),'model':'fixture','tools':['read']}

class StoreFixture(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name).resolve()
  for d in ['candidate','ledger','external-anchor']:(self.root/d).mkdir()
  self.keys={'fixture':{'operator_id':'fixture-operator','secret':b'\x11'*32}}
  self.loc=ProtectedPath(self.root/'ledger/events.sqlite',(self.root/'candidate',))
  self.aloc=ProtectedPath(self.root/'external-anchor/head.sqlite',(self.root/'candidate',))
  self.anchor=SQLiteAnchor(self.aloc);self.store=LedgerStore(self.loc,self.anchor,'fixture-ledger',self.keys);self.store.initialize()
 def tearDown(self):self.tmp.cleanup()
 def cp(self):return self.anchor.read()

class StoreTests(StoreFixture):
 def test_atomic_append_and_verified_reopen(self):
  cp=self.store.append(run(1),'fixture',self.cp());s=LedgerStore(self.loc,SQLiteAnchor(self.aloc),'fixture-ledger',self.keys)
  rows,got,state=s.read_verified();self.assertEqual(got,cp);self.assertIn('run1',state['runs']);self.assertEqual(len(rows),1)
 def test_failed_event_rolls_back_transaction(self):
  old=self.cp()
  with self.assertRaises(l.Invalid):self.store.append({'kind':'invalid'},'fixture',old)
  self.assertEqual(self.store.read_verified()[1],old)
 def test_stale_cas_rejected_without_write(self):
  old=self.cp();self.store.append(run(1),'fixture',old)
  with self.assertRaises(Conflict):self.store.append(run(2),'fixture',old)
  self.assertEqual(len(self.store.read_verified()[0]),1)
 def test_two_writers_only_one_cas_wins(self):
  old=self.cp()
  def append(n):
   try:self.store.append(run(n),'fixture',old);return 'accepted'
   except Conflict:return 'conflict'
  with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:result=list(pool.map(append,[1,2]))
  self.assertEqual(sorted(result),['accepted','conflict']);self.assertEqual(len(self.store.read_verified()[0]),1)
 def test_committed_tail_anchor_failure_blocks_until_explicit_recovery(self):
  old=self.cp()
  with patch.object(self.anchor,'compare_and_swap',return_value=False):
   with self.assertRaises(RecoveryRequired) as err:self.store.append(run(1),'fixture',old)
  pending=err.exception.pending_checkpoint
  with self.assertRaises(RecoveryRequired):self.store.read_verified()
  self.assertEqual(self.store.recover_forward(old,pending),pending)
  self.assertEqual(len(self.store.read_verified()[0]),1)
 def test_database_only_rollback_detected(self):
  backup=self.root/'old.sqlite';shutil.copyfile(self.loc.path,backup)
  self.store.append(run(1),'fixture',self.cp());shutil.copyfile(backup,self.loc.path)
  with self.assertRaises(RecoveryRequired):self.store.read_verified()
  with self.assertRaises(l.Invalid):self.store.recover_forward(self.cp(),l.genesis('fixture-ledger'))
 def test_rolling_back_both_stores_is_outside_the_trust_guarantee(self):
  dbcopy=self.root/'old-db.sqlite';acopy=self.root/'old-anchor.sqlite'
  shutil.copyfile(self.loc.path,dbcopy);shutil.copyfile(self.aloc.path,acopy)
  self.store.append(run(1),'fixture',self.cp())
  shutil.copyfile(dbcopy,self.loc.path);shutil.copyfile(acopy,self.aloc.path)
  self.assertEqual(self.store.read_verified()[0],[]) # Explicit limitation, not claimed protected.
 def test_database_tamper_rejected(self):
  self.store.append(run(1),'fixture',self.cp())
  with connect(self.loc) as db:db.execute('UPDATE entries SET payload=? WHERE sequence=1',(b'{}',))
  with self.assertRaises(l.Invalid):self.store.read_verified()
 def test_noncanonical_storage_rejected(self):
  self.store.append(run(1),'fixture',self.cp())
  with connect(self.loc) as db:
   raw=db.execute('SELECT payload FROM entries').fetchone()[0];db.execute('UPDATE entries SET payload=?',(b' '+raw,))
  with self.assertRaisesRegex(l.Invalid,'noncanonical'):self.store.read_verified()
 def test_candidate_writable_path_rejected(self):
  with self.assertRaisesRegex(l.Invalid,'candidate'):ProtectedPath(self.root/'candidate/db.sqlite',(self.root/'candidate',)).checked()
 def test_missing_candidate_roots_rejected(self):
  with self.assertRaisesRegex(l.Invalid,'explicit candidate'):ProtectedPath(self.root/'ledger/db.sqlite',()).checked()
 def test_missing_database_not_recreated(self):
  missing=ProtectedPath(self.root/'ledger/missing.sqlite',(self.root/'candidate',))
  other=LedgerStore(missing,self.anchor,'fixture-ledger',self.keys)
  with self.assertRaises(l.Invalid):other.read_verified()
  self.assertFalse(missing.path.exists())
 def test_existing_bootstrap_refused(self):
  with self.assertRaises(FileExistsError):self.store.initialize()
 def test_same_database_as_anchor_refused(self):
  with self.assertRaises(l.Invalid):LedgerStore(self.loc,SQLiteAnchor(self.loc),'fixture-ledger',self.keys)
 def test_no_key_material_persisted(self):
  self.store.append(run(1),'fixture',self.cp())
  self.assertNotIn(self.keys['fixture']['secret'],self.loc.path.read_bytes())

class BridgeTests(StoreFixture):
 def setUp(self):
  super().setUp();self.p,self.e,self.blobs=fixtures.fixture();count=100;selected={}
  for r in self.e['runs']:
   count+=1;event={'kind':'run_observed','observation':observation(count),'run_id':r['id'],'agent_id':r['agent_id'],'model':r['model'],'tools':r['tools']}
   self.store.append(event,'fixture',self.cp())
  for r in self.e['receipts']:
   name=r['kind']+':'+r['target'];count+=1
   authors=self.e['authorship'][name] if r['kind']!='assembly' else sorted({a for authors in self.e['authorship'].values() for a in authors})
   freeze={'kind':'target_frozen','observation':observation(count),'freeze_id':'freeze-'+name,'target_kind':r['kind'],'target_id':r['target'],
    'target_sha256':r['target_sha256'],'dependency_sha256':r['dependency_sha256'],'binding':copy.deepcopy(self.e['binding']),'author_runs':authors}
   self.store.append(freeze,'fixture',self.cp());count+=1;rid='report-'+name;selected[name]=rid
   report={'kind':'report_observed','observation':observation(count),'report_id':rid,'run_id':r['run_id'],'freeze_id':freeze['freeze_id'],
    'decision':r['decision'],'scope':r['scope'],'body_base64':base64.b64encode(self.blobs.values[r['report']['sha256']]).decode()}
   self.store.append(report,'fixture',self.cp())
  _,cp,state=self.store.read_verified()
  self.context=VerifiedContext(copy.deepcopy(self.e['binding']),self.e['policy_paths'],self.e['findings'],selected,cp,fixtures.g.digest(inventory(state)))
  context=self.context
  class FixtureContext:
   def verify_context(self,packet,checkpoint,report_inventory):return context
  self.provider=FixtureContext();self.bridge=LedgerEvidenceBridge(self.store,self.provider)
 def test_valid_protected_ledger_to_core(self):
  result=self.bridge.evaluate(self.p,self.blobs);self.assertTrue(result['records_consistent']);self.assertFalse(result['merge_authorized']);self.assertFalse(result['provider_cryptographic_attestation'])
 def test_context_adapter_missing(self):
  with self.assertRaises(fixtures.g.IntegrationMissing):LedgerEvidenceBridge(self.store).evaluate(self.p,self.blobs)
 def test_unsigned_export_dict_not_a_context(self):
  class CandidateJSON:
   def verify_context(self,*args):return {'verified':True}
  with self.assertRaises(fixtures.g.Invalid):LedgerEvidenceBridge(self.store,CandidateJSON()).evaluate(self.p,self.blobs)
 def test_new_ledger_event_invalidates_context(self):
  self.store.append(run(999),'fixture',self.cp())
  with self.assertRaisesRegex(fixtures.g.Invalid,'stale context'):self.bridge.evaluate(self.p,self.blobs)
 def test_incomplete_inventory_digest_rejected(self):
  bad=VerifiedContext(self.context.binding,self.context.policy_paths,self.context.findings,self.context.selected_reports,self.context.ledger_checkpoint,'0'*64)
  class Bad:
   def verify_context(self,*args):return bad
  with self.assertRaisesRegex(fixtures.g.Invalid,'unreconciled'):LedgerEvidenceBridge(self.store,Bad()).evaluate(self.p,self.blobs)
 def test_missing_report_selection_rejected(self):
  self.context.selected_reports.pop('application:A')
  with self.assertRaisesRegex(fixtures.g.Invalid,'incomplete receipt'):self.bridge.evaluate(self.p,self.blobs)
 def test_wrong_report_target_rejected(self):
  self.context.selected_reports['application:A']=self.context.selected_reports['application:B']
  with self.assertRaisesRegex(l.Invalid,'stale or wrong'):self.bridge.evaluate(self.p,self.blobs)
 def test_forged_candidate_authorship_rejected(self):
  self.p['applications'][0]['authors']=['reviewer']
  with self.assertRaises(l.Invalid):self.bridge.evaluate(self.p,self.blobs)
 def test_mutation_during_blob_verification_rejected(self):
  base=self.blobs;store=self.store;done=[False]
  class RacingReader:
   def open(self,side,path,entry):
    if not done[0]:done[0]=True;store.append(run(999),'fixture',store.anchor.read())
    return base.open(side,path,entry)
  with self.assertRaises(Conflict):self.bridge.evaluate(self.p,RacingReader())

if __name__=='__main__':unittest.main(verbosity=2)
