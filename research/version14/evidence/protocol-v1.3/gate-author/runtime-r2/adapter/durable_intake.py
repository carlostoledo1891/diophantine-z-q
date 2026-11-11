"""Trusted-process capture of GitHub observations and collector provenance.

No unsigned observation import, candidate-authenticated flag, or receipt selection.
"""
import copy
import audit_intake as intake
import ledger_evidence_bridge as bridge
import manifest_transport
import offline_manifest_gate as core

class AuditObservationSource:
    """Archive current intake independently of whether CI is green.

    Uses the accepted reader's fixed-origin state, source and pagination methods.
    This is explicitly an intake-only observation, never a successful CI result.
    """
    def __init__(self, reader):
        self.reader=reader;self.policy=reader.policy

    def observe(self, packet):
        packet=copy.deepcopy(packet)
        core.require(type(packet.get('schema')) is int and packet['schema']==2 and packet.get('git_hash')=='sha1',
                     'intake source requires schema2 SHA1')
        core.require(type(packet.get('repository_id')) is int and packet['repository_id']==self.policy.repository_id and
                     type(packet.get('pull_request')) is int and packet['pull_request']>0,'invalid intake repository/PR')
        bm,_=core.snapshot(packet['base'],'sha1');hm,_=core.snapshot(packet['head'],'sha1')
        number=packet['pull_request'];before=self.reader.state(number)
        for side in ('base','head'):
            core.require(all(packet[side][k]==before['commits'][side][k] for k in ('commit','tree')),'intake origin mismatch')
        self.reader.sources(before,packet)
        current=self.reader.intake(number)
        core.require(core.canonical(current)==core.canonical(self.reader.intake(number)),'intake changed during archive')
        core.require(core.canonical(before)==core.canonical(self.reader.state(number)),'PR changed during archive')
        return {'schema':'research-github-intake-observation/v1','binding':core.binding(packet,bm,hm),
                'state':before,'intake':current,'ci_evaluated':False,
                'merge_authorized':False,'deployment_eligible':False}

class IntakeRecorder:
    def __init__(self, audit_store, operator_store, github_reader,
                 collector_sha256, collector_keys):
        intake.need(core.hexhash(collector_sha256) and type(collector_keys) is dict and collector_keys,
                    'protected collector identity and keys required')
        self.audit_store=audit_store;self.operator_store=operator_store
        self.github_reader=github_reader;self.collector_sha256=collector_sha256
        self.collector_keys=copy.deepcopy(collector_keys)

    def capture(self, packet, envelopes, capture_id, key_id, expected_checkpoint):
        packet=copy.deepcopy(packet);envelopes=copy.deepcopy(envelopes)
        intake.fields(envelopes,'base head')
        # Never learn the approved collector identity or key from an envelope.
        repository_id=self.github_reader.policy.repository_id
        intake.need(type(packet.get('repository_id')) is int and packet['repository_id']==repository_id,
                    'collector repository mismatch')
        attestations={}
        for side in ('base','head'):
            manifest=packet[side]
            expected={'repository_id':repository_id,'commit':manifest['commit'],
                      'tree':manifest['tree'],'collector_sha256':self.collector_sha256}
            manifest_transport.verify(manifest,envelopes[side],expected,self.collector_keys)
            attestations[side]={'manifest_sha256':intake.digest(manifest),'transport_envelope':envelopes[side]}
        _,operator_checkpoint,state=self.operator_store.read_verified()
        reports=bridge.inventory(state)
        # Only the configured live reader may supply observations. Calling code
        # must protect the reader/transport just as it protects keys and policy.
        observation=self.github_reader.observe(packet)
        bm,_=core.snapshot(packet['base'],packet['git_hash']);hm,_=core.snapshot(packet['head'],packet['git_hash'])
        binding=core.binding(packet,bm,hm)
        intake.need(core.same_binding(observation.get('binding'),binding),'observation binding mismatch')
        self.operator_store.assert_current(operator_checkpoint)
        event={'kind':'capture','capture_id':capture_id,'binding':binding,
            'packet_sha256':intake.digest(packet),'manifests':attestations,
            'observation':observation,'operator_checkpoint':operator_checkpoint,'reports':reports}
        checkpoint=self.audit_store.append(event,key_id,expected_checkpoint)
        # If this fails, the durable capture remains, but is stale and cannot
        # reconcile successfully. Never roll back the captured evidence.
        self.operator_store.assert_current(operator_checkpoint)
        return checkpoint

    def reconcile(self, packet):
        packet=copy.deepcopy(packet)
        _,audit_checkpoint,state=self.audit_store.read_verified()
        _,operator_checkpoint,operator_state=self.operator_store.read_verified()
        result=intake.reconcile(state,packet,operator_checkpoint,bridge.inventory(operator_state))
        current=state['captures'][state['latest'][intake.scope(result['binding'])]]
        for side in ('base','head'):
            manifest=packet[side]
            expected={'repository_id':self.github_reader.policy.repository_id,'commit':manifest['commit'],
                      'tree':manifest['tree'],'collector_sha256':self.collector_sha256}
            manifest_transport.verify(manifest,current['manifests'][side]['transport_envelope'],
                                      expected,self.collector_keys)
        self.operator_store.assert_current(operator_checkpoint)
        self.audit_store.assert_current(audit_checkpoint)
        result['intake_checkpoint']=audit_checkpoint
        result['operator_checkpoint']=operator_checkpoint
        result['fresh_github_state_checked']=False
        result['verified_context_implemented']=False
        return result

    def verify_context(self, packet, checkpoint, report_inventory):
        raise core.IntegrationMissing('fresh publication-context binding and receipt selection not implemented')
