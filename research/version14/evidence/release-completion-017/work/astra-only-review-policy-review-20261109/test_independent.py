import copy,json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(sys.argv.pop(1))/'adapter'))
import offline_manifest_gate as g
import test_manifest_gate as t
import test_coverage_gate as cov
import test_approval_policy as a
import operator_ledger as ledger
class IndependentPolicyTests(unittest.TestCase):
 def case(self):
  p,e,b=t.fixture();p['repository_id']=1446122118;t.refresh(p,e)
  for r in e['runs']:
   if r['id'] in ('reviewer','assembler'):r['model']='gpt-6-astra'
  return p,e,b
 def test_each_receipt_separately_rejected(self):
  for index in range(len(self.case()[1]['receipts'])):
   p,e,b=self.case();bad=copy.deepcopy(e['runs'][2]);bad.update(id='wrong-run',agent_id='independent-wrong-agent',model='gpt-6.1-sol');e['runs'].append(bad);e['receipts'][index]['run_id']='wrong-run'
   with self.subTest(index=index),self.assertRaisesRegex(g.Invalid,'public-required-approval'):g.check_records(p,e,b)
 def test_actual_coverage_receipt_separately_rejected(self):
  c=cov.Case();c.p['repository_id']=1446122118;c.sync()
  for r in c.e['runs']:
   if r['id'] in ('reviewer','assembler'):r['model']='gpt-6-astra'
  self.assertTrue(c.run()['records_consistent'])
  bad=copy.deepcopy(c.e['runs'][2]);bad.update(id='wrong-cover',agent_id='wrong-cover-agent',model='gpt-6.1-sol');c.e['runs'].append(bad)
  next(r for r in c.e['receipts'] if r['target']==cov.c.COVERAGE_ID)['run_id']='wrong-cover'
  with self.assertRaisesRegex(g.Invalid,'public-required-approval'):c.run()
 def test_unknown_receipt_run_rejected(self):
  p,e,b=self.case();e['receipts'][0]['run_id']='unobserved'
  with self.assertRaisesRegex(g.Invalid,'invalid-review-decision'):g.check_records(p,e,b)
 def test_private_same_evidence_unrestricted(self):
  p,e,b=self.case();p['repository_id']=1447509909;t.refresh(p,e)
  for r in e['runs']:r['model']='gpt-6.1-sol'
  self.assertTrue(g.check_records(p,e,b)['records_consistent'])
 def test_candidate_model_labels_do_not_override(self):
  p,e,b=self.case();p['model']='gpt-6-astra'
  next(r for r in e['runs'] if r['id']=='reviewer')['model']='unknown'
  with self.assertRaises(g.Invalid):g.check_records(p,e,b)
 def test_no_auth_adapter_still_fails(self):
  p,e,b=self.case()
  with self.assertRaises(g.IntegrationMissing):g.validate_offline(p,blob_reader=b)
 def test_signed_ledger_model_tamper_fails(self):
  fixture=a.PolicyTests();entries,keys,checkpoint,target=fixture.ledger_case(model='gpt-6.1-sol')
  entries=copy.deepcopy(entries)
  # Changing any signed serialized run bytes must fail signature verification.
  raw=json.dumps(entries).replace('gpt-6.1-sol','gpt-6-astra');entries=json.loads(raw)
  with self.assertRaises(ledger.Invalid):ledger.export_receipt(entries,'report1',target,keys,checkpoint)
if __name__=='__main__':unittest.main(verbosity=2)
