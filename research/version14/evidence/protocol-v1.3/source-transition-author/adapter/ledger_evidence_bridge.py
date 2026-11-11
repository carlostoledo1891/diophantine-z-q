"""Derive schema-2 evidence from a protected verified ledger, never unsigned exports.

A separate trusted context verifier must supply authenticated snapshot origin,
old policy and complete findings intake. No live verifier is implemented here.
"""
from dataclasses import dataclass
from typing import Protocol
import copy
import base64
import hashlib
import operator_ledger as ledger
import offline_manifest_gate as core

@dataclass(frozen=True)
class VerifiedContext:
    binding: dict
    policy_paths: list
    findings: list
    selected_reports: dict
    ledger_checkpoint: dict
    ledger_inventory_sha256: str

class ContextVerifier(Protocol):
    def verify_context(self,packet,checkpoint,report_inventory)->VerifiedContext:
        """Authenticate origin/policy/intake and account for every signed report.

        Returning candidate JSON as this object is a violation of the trust
        contract. The current checkpoint and inventory digest must be reviewed.
        """
        ...

def targets(packet):
    apps=core.unique(packet['applications'],'id','applications')
    findings=core.unique(packet['findings'],'id','findings')
    closures={};active=set()
    def app_hash(a):
        core.require(a in apps and a not in active,'missing/cyclic application dependency')
        if a not in closures:
            active.add(a);deps=core.string_set(apps[a]['dependencies'],'dependencies')
            closures[a]=core.digest({'application':apps[a],'dependencies':{d:app_hash(d) for d in sorted(deps)}})
            active.remove(a)
        return closures[a]
    for a in apps:app_hash(a)
    fclosures={};visiting=set()
    def finding_hash(f):
        core.require(f in findings and f not in visiting,'missing/cyclic finding dependency')
        if f not in fclosures:
            visiting.add(f);value=findings[f];dup=value['duplicate_of']
            linked=None if dup is None else {'finding':findings[dup],'dependencies':finding_hash(dup)}
            fclosures[f]=core.digest({'applications':{a:closures[a] for a in sorted(value['applications'])},'duplicate_target':linked})
            visiting.remove(f)
        return fclosures[f]
    out={}
    for a in apps:out['application:'+a]=('application',a,core.digest(apps[a]),closures[a])
    for f in findings:out['finding:'+f]=('finding',f,core.digest(findings[f]),finding_hash(f))
    out['assembly:complete']=('assembly','complete',core.digest(packet),core.digest(closures))
    return out

def inventory(state):
    # Include negative and superseded reports too. A context adapter must account
    # for them; selecting one positive receipt does not remove their findings.
    return {rid:{'report':record['event'],
        'freeze':state['freezes'][record['event']['freeze_id']]['event'],
        'operator_id':record['operator_id'],'sequence':record['sequence']}
        for rid,record in sorted(state['reports'].items())}

class LedgerEvidenceBridge:
    def __init__(self,store,context_verifier=None,coverage_profile=None):
        self.store=store;self.context_verifier=context_verifier
        # Operator-protected configuration, never loaded from the packet.
        self.coverage_profile=copy.deepcopy(coverage_profile)
    def _derive(self,packet):
        if self.context_verifier is None:
            raise core.IntegrationMissing('authenticated snapshot/policy/findings context adapter not implemented')
        entries,checkpoint,state=self.store.read_verified()
        reports=inventory(state)
        context=self.context_verifier.verify_context(packet,checkpoint,reports)
        core.require(type(context) is VerifiedContext,'context verifier did not supply verified context')
        context=copy.deepcopy(context)
        core.require(core.canonical(context.ledger_checkpoint)==core.canonical(checkpoint),'stale context checkpoint')
        core.require(context.ledger_inventory_sha256==core.digest(reports),'unreconciled ledger report inventory')
        bm,_=core.snapshot(packet['base'],packet['git_hash']);hm,_=core.snapshot(packet['head'],packet['git_hash'])
        expected_binding=core.binding(packet,bm,hm)
        core.require(core.same_binding(context.binding,expected_binding),'wrong authenticated context binding')
        expected=targets(packet)
        core.require(type(context.selected_reports) is dict and set(context.selected_reports)==set(expected),'incomplete receipt selection')
        receipts=[];authorship={}
        for selection,(kind,target_id,target_hash,dependency_hash) in expected.items():
            target={'target_kind':kind,'target_id':target_id,'target_sha256':target_hash,
                    'dependency_sha256':dependency_hash,'binding':expected_binding}
            observed=ledger.export_receipt(entries,context.selected_reports[selection],target,self.store.keys,checkpoint)
            matches=sorted(path for path,item in packet['head']['files'].items() if item['sha256']==observed['report_sha256'])
            core.require(matches,'observed report not present in candidate tree')
            if kind!='assembly':authorship[selection]=observed['author_runs']
            receipts.append({'id':'operator-ledger:'+observed['report_id'],'kind':kind,'target':target_id,
                'target_sha256':target_hash,'dependency_sha256':dependency_hash,'run_id':observed['run_id'],
                'decision':observed['decision'],'scope':observed['scope'],'binding':expected_binding,
                'report':{'side':'head','path':matches[0],'sha256':observed['report_sha256']}})
        runs=[{'id':rid,'agent_id':record['event']['agent_id'],'reviewer_type':'model',
                'model':record['event']['model'],'tools':record['event']['tools']}
                for rid,record in state['runs'].items()]
        evidence={'binding':context.binding,'policy_paths':context.policy_paths,'runs':runs,
            'authorship':authorship,'findings':context.findings,'receipts':receipts}
        self.store.assert_current(checkpoint)
        return evidence,checkpoint
    def evaluate(self,packet,blob_reader=None):
        packet=copy.deepcopy(packet)
        evidence,checkpoint=self._derive(packet)
        result=core.check_records(packet,evidence,blob_reader,self.coverage_profile)
        self.store.assert_current(checkpoint)
        result['authentication']='operator ledger verified; external context supplied by trusted adapter'
        result['operator_ledger_checkpoint']=checkpoint
        result['provider_cryptographic_attestation']=False
        return result
