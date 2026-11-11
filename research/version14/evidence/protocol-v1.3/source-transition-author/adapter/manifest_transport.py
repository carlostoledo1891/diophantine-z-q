"""Optional authenticated manifest transport between separately trusted processes.

This authenticates a shared-secret holder, not GitHub origin or agent provenance.
A same-process collector/evaluator needs no extra transport key. Keys must never
be read from the candidate or made available to candidate programs.
"""
import hashlib
import hmac
import re
from git_manifest import Invalid, canonical, fields, need, sha, verify_manifest

PURPOSE='research-git-manifest-transport/v1'

def validate_binding(binding):
    fields(binding,'repository_id commit tree collector_sha256')
    need(type(binding['repository_id']) is int and binding['repository_id']>0,'invalid repository identity')
    need(type(binding['commit']) is str and re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}',binding['commit']) is not None,'invalid commit')
    need(type(binding['tree']) is str and len(binding['tree'])==len(binding['commit']) and re.fullmatch('[0-9a-f]+',binding['tree']) is not None,'invalid tree')
    need(type(binding['collector_sha256']) is str and re.fullmatch('[0-9a-f]{64}',binding['collector_sha256']) is not None,'invalid collector digest')

def key_bytes(key):
    need(type(key) is bytes and len(key)>=32,'transport key must contain at least 32 bytes')
    return key

def seal(manifest,binding,key_id,key):
    """For an isolated trusted collector only. Does not verify repository origin."""
    validate_binding(binding);verify_manifest(manifest)
    need(binding['commit']==manifest['commit'] and binding['tree']==manifest['tree'],'wrong manifest binding')
    need(type(key_id) is str and re.fullmatch('[A-Za-z0-9._-]{1,100}',key_id) is not None,'invalid key identity')
    envelope={'purpose':PURPOSE,'key_id':key_id,'binding':binding,'manifest_sha256':sha(canonical(manifest))}
    envelope['signature']=hmac.new(key_bytes(key),canonical(envelope),hashlib.sha256).hexdigest()
    return envelope

def verify(manifest,envelope,expected_binding,trusted_keys):
    """trusted_keys and expected_binding must originate outside the candidate."""
    validate_binding(expected_binding)
    fields(envelope,'purpose key_id binding manifest_sha256 signature')
    need(envelope['purpose']==PURPOSE,'wrong transport purpose')
    validate_binding(envelope['binding'])
    need(canonical(envelope['binding'])==canonical(expected_binding),'unexpected repository/commit/collector binding')
    need(type(envelope['key_id']) is str and envelope['key_id'] in trusted_keys,'unknown transport signer')
    unsigned={k:v for k,v in envelope.items() if k!='signature'}
    expected=hmac.new(key_bytes(trusted_keys[envelope['key_id']]),canonical(unsigned),hashlib.sha256).hexdigest()
    need(type(envelope['signature']) is str and hmac.compare_digest(envelope['signature'],expected),'bad transport authentication')
    need(envelope['manifest_sha256']==sha(canonical(manifest)),'changed manifest')
    checked=verify_manifest(manifest)
    need(manifest['commit']==expected_binding['commit'] and manifest['tree']==expected_binding['tree'],'wrong manifest identity')
    return dict(checked,transport_authenticated=True,github_origin_authenticated=False,
        live_pr_authenticated=False,agent_provenance_authenticated=False,merge_authorized=False)
