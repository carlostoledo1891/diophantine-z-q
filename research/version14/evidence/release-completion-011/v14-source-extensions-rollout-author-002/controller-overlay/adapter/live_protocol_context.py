"""Protected-process live evaluation; no GitHub mutations or merge authority.

Caller protects configuration, stores, transport and receipt selections. Returned
JSON is not a portable authenticated publication token.
"""
import copy
import hashlib
from dataclasses import asdict
from pathlib import Path
import audit_intake
import github_read_context
import ledger_evidence_bridge as bridge
import offline_manifest_gate as core
import operator_ledger

DEPENDENCY_PINS={
    'audit_intake.py':'37fcad21a44f8f7cc87c6d71a8e9f002fdfb908fa9ee4fe8600d3c47e021a167',
    'audit_intake_store.py':'16bbbd514d7f9a3eb23e9553e877427de54ed7a6bc0adba0fa26c2997ec48c8f',
    'durable_intake.py':'3e46f90a6a4247ebc3f4cbe8b329885ac4b38020fe314460977f14ac7e6b950b',
    'operator_ledger.py':'5e2cec65c3b516f62ec4bbd9ae071c431c11ab7456edd4d7000c986782c072d7',
    'protected_ledger_store.py':'8bd48c4439079a75976afd61aa8a7acaf319daf01b6d34df589883a0e2c292d2',
    'ledger_evidence_bridge.py':'73c81da423a173dcbdf0249a6026fbfcf55f20c78de7b6f91b6bf33bd0380e75',
    'offline_manifest_gate.py':'978d954e18b3cbde2ed3440581259aa025def63e2835c12cd6210396b71375da',
    'manifest_transport.py':'e30a0da1349807b370a533bf5f41062013a6b6fee989631cbfc6f499c3f4dc9c',
    'git_manifest.py':'8ca4d7b1ffb49d1a329f5ab8f423b1e415b3c5616f8e6d03a052348f75f9fcef',
    'github_read_context.py':'3f9b3b6041686bf0be5f513dd8aa2c7fed6719c4296e0d487e3ec53278e9fee9',
    'coverage_gate.py':'34f6a740f0fed7356614374b01a09ebe565d863fca3d882047d5f836ad550b93',
    'connections_gate.py':'6ef0d24825db8de3f21bf873728676572ec32a24427ca76ad4166afa93a1ffd4',
}

def verify_dependencies():
    root=Path(__file__).resolve().parent
    for name,expected in DEPENDENCY_PINS.items():
        core.require(hashlib.sha256((root/name).read_bytes()).hexdigest()==expected,
                     'live evaluator dependency pin changed: '+name)

class TrustedContextVerifier:
    """Single-use verifier for one exact packet and one protected selection map."""
    def __init__(self, recorder, live_reader, selected_reports):
        core.require(type(live_reader) is github_read_context.ReadContext,
                     'strict live ReadContext required, not an intake-only source')
        core.require(core.canonical(asdict(recorder.github_reader.policy))==core.canonical(asdict(live_reader.policy)),
                     'capture and live policy configurations differ')
        core.require(type(selected_reports) is dict and all(core.text(k) and core.text(v) for k,v in selected_reports.items()),
                     'protected explicit receipt selection required')
        self.recorder=recorder;self.reader=live_reader
        self.policy_snapshot=copy.deepcopy(asdict(live_reader.policy))
        self.selected=copy.deepcopy(selected_reports)
        self.used=False;self.finished=False;self.packet=None
        self.observation=None;self.audit_checkpoint=None;self.operator_checkpoint=None

    def verify_context(self, packet, checkpoint, report_inventory):
        core.require(not self.used,'live context verifier is single-use')
        self.used=True;packet=copy.deepcopy(packet)
        entries,current,operator_state=self.recorder.operator_store.read_verified()
        reports=bridge.inventory(operator_state)
        core.require(core.canonical(checkpoint)==core.canonical(current) and
                     core.canonical(report_inventory)==core.canonical(reports),'bridge operator inventory is not current')
        intake_result=self.recorder.reconcile(packet)
        core.require(core.canonical(intake_result['operator_checkpoint'])==core.canonical(current),'operator changed during reconciliation')
        _,audit_checkpoint,audit_state=self.recorder.audit_store.read_verified()
        core.require(core.canonical(audit_checkpoint)==core.canonical(intake_result['intake_checkpoint']),
                     'intake changed during reconciliation')
        expected=bridge.targets(packet)
        core.require(set(self.selected)==set(expected),'incomplete explicit receipt selection')
        for name,(kind,target_id,target_sha,dependencies) in expected.items():
            operator_ledger.export_receipt(entries,self.selected[name],
                {'target_kind':kind,'target_id':target_id,'target_sha256':target_sha,
                 'dependency_sha256':dependencies,'binding':intake_result['binding']},
                self.recorder.operator_store.keys,current)
        observation=self.reader.observe(packet)
        core.require(core.same_binding(observation['binding'],intake_result['binding']),'fresh GitHub binding mismatch')
        which=audit_intake.scope(intake_result['binding'])
        captured=audit_state['captures'][audit_state['latest'][which]]['observation']
        core.require(core.canonical(observation['state'])==core.canonical(captured['state']),
                     'GitHub state differs from registered capture')
        core.require(core.canonical(observation['intake'])==core.canonical(captured['intake']),
                     'current audit intake differs from registered capture')
        core.require(observation.get('ci') and
                     observation.get('policy_paths')==list(self.reader.policy.policy_paths),
                     'strict CI or policy observation missing')
        self.recorder.operator_store.assert_current(current)
        self.recorder.audit_store.assert_current(audit_checkpoint)
        self.packet=packet;self.observation=copy.deepcopy(observation)
        self.audit_checkpoint=copy.deepcopy(audit_checkpoint);self.operator_checkpoint=copy.deepcopy(current)
        return bridge.VerifiedContext(intake_result['binding'],list(self.reader.policy.policy_paths),
            intake_result['findings'],copy.deepcopy(self.selected),current,core.digest(reports))

    def finish(self):
        """Reobserve after actual blob/core checks; no future atomicity claim."""
        core.require(self.used and self.observation is not None and not self.finished,
                     'live context did not complete or finish already consumed')
        self.finished=True
        return self._reobserve()

    def _reobserve(self):
        core.require(self.finished and self.observation is not None,'evaluation not finished')
        verify_dependencies()
        core.require(core.canonical(asdict(self.reader.policy))==core.canonical(self.policy_snapshot) and
                     core.canonical(asdict(self.recorder.github_reader.policy))==core.canonical(self.policy_snapshot),
                     'protected policy changed during evaluation session')
        reconciled=self.recorder.reconcile(self.packet)
        core.require(core.canonical(reconciled['intake_checkpoint'])==core.canonical(self.audit_checkpoint) and
                     core.canonical(reconciled['operator_checkpoint'])==core.canonical(self.operator_checkpoint),
                     'reconciled provenance changed during evaluation session')
        now=self.reader.observe(self.packet)
        core.require(core.canonical(now)==core.canonical(self.observation),'GitHub changed during core evaluation')
        self.recorder.operator_store.assert_current(self.operator_checkpoint)
        self.recorder.audit_store.assert_current(self.audit_checkpoint)
        return {'observation_sha256':core.digest(now),
                'intake_checkpoint':copy.deepcopy(self.audit_checkpoint),
                'operator_checkpoint':copy.deepcopy(self.operator_checkpoint)}

_SESSION_TOKEN=object()

class LiveEvaluation:
    """In-process evaluation capability, never a portable signed JSON token.

    This boundary assumes candidate code cannot execute inside this process.
    Python privacy/type checks are not a sandbox against hostile caller code.
    """
    def __init__(self, verifier, result, token):
        core.require(token is _SESSION_TOKEN and verifier.finished,'use evaluate_session to create live evaluation')
        self._verifier=verifier;self._result=copy.deepcopy(result);self._failed=False

    @property
    def binding(self):return copy.deepcopy(self._verifier.observation['binding'])

    @property
    def result(self):return copy.deepcopy(self._result)

    @property
    def observation(self):return copy.deepcopy(self._verifier.observation)

    def recheck(self):
        core.require(not self._failed,'evaluation session permanently invalidated')
        try:
            return self._verifier._reobserve()
        except Exception:
            self._failed=True
            raise

def evaluate_session(packet, recorder, live_reader, selected_reports, blob_reader, coverage_profile=None):
    """Runnable end-to-end evaluation for trusted local orchestration.

    Requires actual authenticated collector envelopes already registered through
    recorder.capture, a fully classified durable intake, and observed independent
    operator receipts. It never invents or auto-selects an acceptance.
    """
    verify_dependencies();packet=copy.deepcopy(packet)
    verifier=TrustedContextVerifier(recorder,live_reader,selected_reports)
    result=bridge.LedgerEvidenceBridge(recorder.operator_store,verifier,coverage_profile).evaluate(packet,blob_reader)
    final=verifier.finish()
    result.update(final)
    result['live_context_verified']=True
    result['live_github_state']='strict complete observation matched before and after core checks'
    result['authentication']='protected operator ledger, collector transport, durable intake and authenticated live GitHub reads'
    result['publication_token_authenticated']=False
    result['merge_authorized']=False
    result['deployment_eligible']=False
    result['limitation']='Trusted-process evaluation only; publication must preserve provenance and recheck freshness. No mathematical proof or atomic GitHub transaction.'
    return LiveEvaluation(verifier,result,_SESSION_TOKEN)

def evaluate(packet, recorder, live_reader, selected_reports, blob_reader, coverage_profile=None):
    """Convenience result only. A publisher must use the in-process session API."""
    return evaluate_session(packet,recorder,live_reader,selected_reports,blob_reader,coverage_profile).result
