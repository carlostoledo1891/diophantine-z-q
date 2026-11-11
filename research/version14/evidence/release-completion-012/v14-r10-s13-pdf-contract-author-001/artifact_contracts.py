"""Exact artifact contracts, not a mathematical or authentication verifier."""
import json
import re
from pathlib import Path
from release_common import safe, sha, pinned, V14_TEX, V14_PDF, V13_ARCHIVE_SHA

PROJECT_PDFS_SHA = '40b2fd8d9a082c32205e5bacc71c483789f2107e06a2669fd5835e7f2f884941'
ANNEX = 'research/version14/z-in-q-version14-research-annex.zip'
ROLES = {'inventory','assembly','connections','related_use','consistency',
         'independent_decisions','gate_result','build_visual'}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def decode(raw):
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d, 'Duplicate JSON key: '+k)
            d[k]=v
        return d
    return json.loads(raw, object_pairs_hook=pairs)

def keys(value, fields, label):
    require(type(value) is dict and set(value)==set(fields), 'Wrong fields: '+label)

def pin_shape(pin):
    keys(pin, ('path','sha256','bytes'), 'pin')
    safe(pin['path'])
    require(type(pin['sha256']) is str and re.fullmatch('[0-9a-f]{64}',pin['sha256']), 'Invalid SHA256')
    require(type(pin['bytes']) is int and pin['bytes']>=0, 'Invalid byte count')

def check_pin(pin, current):
    pin_shape(pin)
    require(pin['path'] in current, 'Missing selected evidence: '+pin['path'])
    raw=current[pin['path']]
    require(sha(raw)==pin['sha256'] and len(raw)==pin['bytes'], 'Changed selected evidence: '+pin['path'])
    return raw

def project_pdfs():
    raw=Path(__file__).with_name('project-pdfs.json').read_bytes()
    data=decode(pinned(raw, PROJECT_PDFS_SHA, 'reviewed project PDF/source allowlist'))
    keys(data, ('schema','provenance','entries'), 'project PDF allowlist')
    require(data['schema']=='v14-reviewed-project-pdfs/v1', 'Wrong project PDF schema')
    result={}
    for item in data['entries']:
        keys(item, ('pdf','sources'), 'project PDF entry')
        pin_shape(item['pdf'])
        require(item['pdf']['path'] not in result, 'Repeated project PDF')
        require(type(item['sources']) is list and item['sources'], 'Missing project TeX source')
        for p in item['sources']:pin_shape(p)
        result[item['pdf']['path']]=item
    return data, result

def check_project_pdfs(current):
    data, entries=project_pdfs()
    # Every approved project PDF is a required part of this exact release scope.
    for item in entries.values():
        require(check_pin(item['pdf'],current).startswith(b'%PDF-'), 'Project PDF header missing')
        for p in item['sources']:check_pin(p,current)
    for p in data['provenance']:check_pin(p,current)

def source_map(data, current):
    keys(data, ('schema','base_sha256','annex_sha256','files','exclusions'), 'cumulative source map')
    require(data['schema']=='v14-cumulative-source-map/v1', 'Wrong cumulative map schema')
    require(data['base_sha256']==V13_ARCHIVE_SHA, 'Wrong historical base')
    require(ANNEX in current and data['annex_sha256']==sha(current[ANNEX]), 'Wrong annex pin')
    require(type(data['files']) is dict and set(data['files'])==set(current), 'Map must cover exactly every selected file')
    for name,item in data['files'].items():
        safe(name)
        keys(item, ('sha256','bytes','role','origin'), 'mapped file')
        require(item['role'] in ('current','historical'), 'Unclassified mapped file')
        keys(item['origin'], ('kind','path'), 'file origin')
        require(item['origin']['kind']=='selected_repository', 'Unsupported or private origin kind')
        require(item['origin']['path']==name, 'Origin must name exact selected repository path')
        check_pin({'path':name,'sha256':item['sha256'],'bytes':item['bytes']},current)
    require(type(data['exclusions']) is list, 'Exclusions list required')
    seen=set()
    for item in data['exclusions']:
        keys(item, ('path','sha256','reason'), 'excluded historical file')
        safe(item['path'])
        require(item['path'] not in current and item['path'] not in seen, 'Excluded file is selected or repeated')
        seen.add(item['path'])
        require(type(item['sha256']) is str and re.fullmatch('[0-9a-f]{64}',item['sha256']), 'Bad exclusion SHA')
        require(type(item['reason']) is str and item['reason'].strip(), 'Exclusion reason required')

def final_inputs(data, current, oid, coverage, post_gate):
    keys(data, ('schema','source_commit','manuscript','pdf','roles','gate_binding'), 'final release inputs')
    require(data['schema']=='v14-final-release-inputs/v1', 'Wrong release input schema')
    require(data['source_commit']==oid, 'Final inputs bind another commit')
    require(data['manuscript']['path']==V14_TEX and data['pdf']['path']==V14_PDF, 'Wrong main artifact paths')
    check_pin(data['manuscript'],current);check_pin(data['pdf'],current)
    require(type(data['roles']) is dict and set(data['roles'])==ROLES, 'Every final evidence role is required')
    evidence_paths=set(coverage['coverage']+coverage['profiles']+coverage['evidence'])
    for role,pins in data['roles'].items():
        require(type(pins) is list and pins, 'Missing final role: '+role)
        seen=set()
        for item in pins:
            keys(item, ('domain','pin'), 'final role reference')
            domain,pin=item['domain'],item['pin']
            require(domain in ('source','post_gate'), 'Unknown evidence domain')
            if role=='gate_result':require(domain=='post_gate', 'Gate result must be outside source commit')
            if role in ('inventory','connections','related_use','consistency'):
                require(domain=='source', 'Current source records must be selected Git bytes')
            check_pin(pin,current if domain=='source' else post_gate)
            if domain=='source':require(pin['path'] in evidence_paths, 'Final role absent from explicit evidence selection')
            identity=(domain,pin['path'])
            require(identity not in seen, 'Repeated pin in final role')
            seen.add(identity)
    gate_binding(data['gate_binding'],post_gate,oid)
    # This deliberately checks artifact identity and presence only. Actual App
    # result authenticity is checked by the independent protocol pipeline.

def canonical_digest(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode('utf-8'))

def gate_binding(data, post_gate, oid):
    fields=('job','app_id','target_mode','context_sha256','profile_canonical_sha256',
            'packet_canonical_sha256','controller_result','check_run','pull_request','profile','packet','collection_review')
    keys(data,fields,'offline gate binding')
    require(type(data['job']) is str and data['job'], 'Gate job ID required')
    require(type(data['app_id']) is int and data['app_id']>0, 'Trusted App ID required')
    require(data['target_mode'] in ('head','merge'), 'Unsupported gate target mode')
    require(type(data['context_sha256']) is str and re.fullmatch('[0-9a-f]{64}',data['context_sha256']), 'Gate context digest required')
    values={}
    for role in ('controller_result','check_run','pull_request','profile','packet','collection_review'):
        raw=check_pin(data[role],post_gate)
        if role!='collection_review':values[role]=decode(raw)
    profile,packet=values['profile'],values['packet']
    require(canonical_digest(profile)==data['profile_canonical_sha256'], 'Profile canonical hash mismatch')
    require(canonical_digest(packet)==data['packet_canonical_sha256'], 'Packet canonical hash mismatch')
    require(profile.get('protocol_version')=='1.4', 'Gate profile is not protocol1.4')
    require(packet['head']['commit']==oid, 'Packet head does not bind selected source commit')
    pr=values['pull_request']
    require(pr['head']['sha']==oid and pr['base']['sha']==packet['base']['commit'], 'PR readback base/head mismatch')
    require(pr['number']==packet['pull_request'], 'PR number mismatch')
    require(pr['base']['repo']['id']==packet['repository_id'], 'PR repository mismatch')
    target=oid if data['target_mode']=='head' else pr['merge_commit_sha']
    require(type(target) is str and re.fullmatch('[0-9a-f]{40}',target), 'Exact gate target required')
    results=values['controller_result']
    require(type(results) is list, 'Raw controller result list required')
    matches=[r for r in results if type(r) is dict and r.get('job')==data['job']]
    require(len(matches)==1, 'Missing or ambiguous controller job result')
    result=matches[0]
    require(result.get('status')=='success' and result.get('published_success') is True, 'Controller did not publish success')
    require(result.get('target_sha')==target and result.get('target_mode')==data['target_mode'], 'Controller target mismatch')
    require(result.get('context_sha256')==data['context_sha256'], 'Controller context mismatch')
    require(type(result.get('generation')) is int and result['generation']>0, 'Controller generation required')
    check=values['check_run']
    require(type(result.get('check_id')) is int and result['check_id']>0 and check.get('id')==result['check_id'], 'Check ID mismatch')
    require(check.get('head_sha')==target and check.get('name')=='Protocol / independent agent audit', 'Wrong check target/name')
    require(check.get('app',{}).get('id')==data['app_id'], 'Wrong publisher App')
    require(check.get('status')=='completed' and check.get('conclusion')=='success', 'Check readback not successful')
    # No saved-JSON comparison authenticates GitHub or reconstructs the live
    # ledger/session checks. collection_review is an exact external review pin,
    # not prose interpreted as a proof or an authentication token.

def load_post_gate(directory, manifest, admissible, check_private):
    """Load exact, separately reviewed evidence collected after the source commit."""
    keys(manifest, ('schema','files'), 'post-gate evidence manifest')
    require(manifest['schema']=='v14-post-gate-evidence/v1', 'Wrong post-gate schema')
    require(type(manifest['files']) is dict and manifest['files'], 'Post-gate evidence is required')
    require(not directory.is_symlink() and directory.is_dir(), 'Invalid post-gate directory')
    root=directory.resolve()
    names=set();case_names=set();total=0
    for name,pin in manifest['files'].items():
        safe(name);admissible(name)
        require(Path(name).suffix.lower() in ('.json','.md','.txt'), 'Post-gate evidence must be passive text')
        require(name.casefold() not in case_names, 'Case-colliding post-gate paths')
        case_names.add(name.casefold());names.add(name)
        keys(pin, ('sha256','bytes'), 'post-gate file')
        pin_shape({'path':name,**pin})
        require(pin['bytes']<=32*1024*1024, 'Post-gate file exceeds bounded input size')
        total+=pin['bytes']
    require(total<=128*1024*1024, 'Post-gate bundle exceeds bounded input size')
    observed=set()
    for path in root.rglob('*'):
        require(not path.is_symlink(), 'Symlink in post-gate bundle')
        if path.is_file():observed.add(path.relative_to(root).as_posix())
    require(observed==names, 'Post-gate directory must match manifest exactly')
    out={}
    for name,pin in manifest['files'].items():
        path=root/name
        require(path.resolve().is_relative_to(root), 'Post-gate path escapes root')
        require(path.stat().st_size==pin['bytes'], 'Wrong post-gate byte count')
        raw=path.read_bytes()
        require(len(raw)==pin['bytes'] and sha(raw)==pin['sha256'], 'Changed post-gate evidence')
        check_private(name,raw)
        out[name]=raw
    return out
