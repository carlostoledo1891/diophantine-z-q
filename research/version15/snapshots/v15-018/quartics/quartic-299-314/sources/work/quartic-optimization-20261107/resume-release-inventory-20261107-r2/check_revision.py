"""Read-only structural consistency checks, not a mathematical proof checker."""
from pathlib import Path
import hashlib
import json
import re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
def read(name):
    return json.loads((HERE/name).read_bytes())
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

pins=read('SOURCE-PINS.json')
for path,meta in pins.items():
    if path.endswith('/STATUS.json'):
        continue  # Mutable navigation only; its captured snapshot is retained.
    assert sha(ROOT/path)==meta['sha256'],path
for p in read('PREVIOUS-REVISION.json').values():
    assert sha(ROOT/p['path'])==p['sha256']
apps=read('APPLICATION-DELTA.json')
c=read('CANDIDATES.json')
m=read('INTEGRATION-MAP.json')
assert len(apps['applications'])==39
assert len(apps['newInternalEntries'])==23
assert len(c['components'])==22
assert c['selectedAcceptedCandidate']=='combined315'
assert c['components']['combined315']['variables']==315
assert len(set(x['canonicalCandidateId'] for x in c['components'].values()))==22
assert c['components']['combined318']['recordedStatus']=='accepted_composition'
for key,x in c['components'].items():
    assert x['canonicalCandidateId']=='sha256:'+x['candidate']['sha256']
    assert sha(ROOT/x['candidate']['path'])==x['candidate']['sha256']
    if x['review']:
        assert sha(ROOT/x['review']['path'])==x['review']['sha256']
    assert not x['newApprovalCreatedHere']
assert sha(ROOT/m['outline']['path'])==m['outline']['sha256']
tex=(ROOT/m['outline']['path']).read_text(encoding='utf-8')
lines=tex.splitlines()
byid={a['id']:a for a in apps['applications']}
entries={e['id']:e for e in apps['newInternalEntries']}
assert set(entries)=={x['entryId'] for x in m['entries']}
for x in m['entries']:
    assert '\\label{'+x['outlineLabel']+'}' in lines[x['outlineLabelLine']-1]
    assert set(x['constructionConsumers'])<=c['components'].keys()
    assert {a['applicationId'] for a in x['inventoryConsumers']}==set(entries[x['entryId']]['baselineApplications'])
    for a in x['inventoryConsumers']:
        assert a['baselineConsumerSpans']==byid[a['applicationId']]['baselineConsumers']
    for s in x['authorProof']:
        assert sha(ROOT/s['path'])==s['sha256']
        source=(ROOT/s['path']).read_text(encoding='utf-8-sig').splitlines()
        assert 1<=s['startLine']<=s['endLine']<=len(source)
        if s['heading']!='Whole report':
            assert source[s['startLine']-1]==s['heading']
# Lexical TeX checks only. Compilation was blocked by local MiKTeX setup.
body='\n'.join(s.split('%',1)[0] for s in lines)
depth=0
for i,ch in enumerate(body):
    if i and body[i-1]=='\\':
        continue
    if ch=='{':depth+=1
    if ch=='}':depth-=1
    assert depth>=0
assert depth==0
stack=[]
for typ,name in re.findall(r'\\(begin|end)\{([^}]+)\}',body):
    if typ=='begin':stack.append(name)
    else:assert stack.pop()==name
assert not stack
labels=re.findall(r'\\label\{([^}]+)\}',body)
assert len(set(labels))==len(labels)
print(json.dumps({'structuralChecks':'pass','previousPacket':'unchanged','applications':39,'entries':23,
 'canonicalCandidates':22,'sourcePinsCheckedExceptMutableNavigation':len(pins)-1,
 'texBracesEnvironmentsLabels':'pass','texCompilation':'not_completed_MiKTeX_setup_denied_before_source_read',
 'newMathematicalAcceptance':False}))
