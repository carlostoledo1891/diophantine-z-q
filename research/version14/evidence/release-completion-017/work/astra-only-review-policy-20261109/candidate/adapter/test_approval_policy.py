"""Synthetic policy tests; no real approval or operator keys."""
import copy, unittest
import approval_policy as policy
import operator_ledger as ledger
from test_operator_ledger import run_event, freeze_event, report_event
from test_manifest_gate import fixture, refresh
import offline_manifest_gate as gate

class PolicyTests(unittest.TestCase):
 def test_exact_model_and_scope(self):
  for model in ['gpt-6.1-sol','GPT-6-ASTRA','Astra','gpt-6-astra-latest','gpt-6-astra ', '', None, 'requested gpt-6-astra; serving model unknown']:
   self.assertFalse(policy.approval_allowed(1446122118,model))
   self.assertTrue(policy.approval_allowed(1447509909,model))
  self.assertTrue(policy.approval_allowed(1446122118,'gpt-6-astra'))
  self.assertFalse(policy.approval_allowed(1446122118,'gpt-6-astra','human'))
 def ledger_case(self, model='gpt-6-astra', repository=1446122118, kind='application', target='coverage', decision='accepted', self_author=False):
  keys={'key':{'operator_id':'synthetic-operator','secret':b'x'*32}}
  entries=[]; checkpoint=ledger.genesis('synthetic-ledger')
  author=run_event('author-run','author-agent',1)
  reviewer=run_event('review-run','author-agent' if self_author else 'review-agent',2);reviewer['model']=model
  freeze=freeze_event();freeze['binding']['repository_id']=repository;freeze['target_kind']=kind;freeze['target_id']=target
  report=report_event();report['decision']=decision
  for event in [author,reviewer,freeze,report]:entries,checkpoint=ledger.append(entries,event,'key',keys,checkpoint)
  expected={k:freeze[k] for k in ['target_kind','target_id','target_sha256','dependency_sha256','binding']}
  return entries,keys,checkpoint,expected
 def export(self,case):
  entries,keys,checkpoint,expected=case
  return ledger.export_receipt(entries,'report1',expected,keys,checkpoint)
 def test_public_all_required_kinds(self):
  for kind,target in [('application','mathematical'),('application','coverage'),('finding','resolution'),('assembly','complete')]:
   with self.subTest(kind=kind,target=target):
    self.assertEqual(self.export(self.ledger_case(kind=kind,target=target))['model'],'gpt-6-astra')
    with self.assertRaisesRegex(ledger.Invalid,'trusted exact'):self.export(self.ledger_case(model='gpt-6.1-sol',kind=kind,target=target))
 def test_private_unchanged(self):self.export(self.ledger_case(model='gpt-6.1-sol',repository=1447509909))
 def test_self_approval(self):
  with self.assertRaisesRegex(ledger.Invalid,'authoring agent'):self.export(self.ledger_case(self_author=True))
 def test_negative_other_model_preserved(self):
  c=self.ledger_case(model='gpt-6.1-sol',decision='changes_required')
  self.assertIn('report1',ledger.verify(c[0],c[1],c[2])['reports'])
  with self.assertRaisesRegex(ledger.Invalid,'does not accept'):self.export(c)
 def test_historical_non_astra_preserved_not_eligible(self):
  c=self.ledger_case(model='gpt-6.1-sol');ledger.verify(c[0],c[1],c[2])
  with self.assertRaisesRegex(ledger.Invalid,'trusted exact'):self.export(c)
 def test_candidate_model_spoof_rejected(self):
  c=self.ledger_case(model='gpt-6.1-sol');c[3]['model']='gpt-6-astra'
  with self.assertRaises(ledger.Invalid):self.export(c)
 def test_core_all_decisions_and_non_astra_authors(self):
  p,e,b=fixture();p['repository_id']=1446122118;refresh(p,e)
  for r in e['runs']:
   if r['id'] in ['reviewer','assembler']:r['model']='gpt-6-astra'
  gate.check_records(p,e,b)
  for receipt in e['receipts']:
   changed=copy.deepcopy(e)
   run=next(r for r in changed['runs'] if r['id']==receipt['run_id']);run['model']='gpt-6.1-sol'
   with self.subTest(kind=receipt['kind']):
    with self.assertRaisesRegex(gate.Invalid,'public-required-approval'):gate.check_records(p,changed,b)
 def test_core_human_not_eligible(self):
  p,e,b=fixture();p['repository_id']=1446122118;refresh(p,e)
  for r in e['runs']:
   if r['id'] in ['reviewer','assembler']:r.update(reviewer_type='human',model=None)
  with self.assertRaisesRegex(gate.Invalid,'public-required-approval'):gate.check_records(p,e,b)
if __name__=='__main__':unittest.main()
