from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
T=ROOT/'work/source-risk-review-20261107/yuan-final-adoption-root-001'
def h(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
checks=[]
def ck(name,value):
 checks.append({'name':name,'passed':bool(value)})
 assert value,name
ck('frozen author manifest',h((T/'MANIFEST.json').read_bytes())=='7fa1c3c7e11027a522cd2589f51a9a38e74d06f4454e66c4fc7c989b3526c0ad')
m=read(T/'MANIFEST.json')
for x in m['files']:
 b=(T/x['path']).read_bytes();ck('member '+x['path'],h(b)==x['sha256'] and len(b)==x['bytes'])
for x in read(T/'SOURCE-PINS.json'):
 b=(ROOT/x['path']).read_bytes();ck('input '+x['id'],h(b)==x['sha256'] and len(b)==x['bytes'])
e=read(T/'EDITS.json');base=(ROOT/e['base']['path']).read_bytes();candidate=(ROOT/e['candidate']['path']).read_bytes()
ck('base',h(base)==e['base']['sha256']);ck('candidate',h(candidate)==e['candidate']['sha256']);result=base;positions=[]
for x in e['edits']:
 a=x['old'].encode();b=x['new'].encode();ck(x['id']+' old digest',h(a)==x['old_sha256']);ck(x['id']+' new digest',h(b)==x['new_sha256']);ck(x['id']+' unique',base.count(a)==1)
 pos=base.index(a);positions.append((pos,pos+len(a)));ck(x['id']+' offset',pos==x['byte_offset']);ck(x['id']+' line',base[:pos].count(b'\n')+1==x['start_line']);result=result.replace(a,b)
ck('five edits',len(e['edits'])==5);ck('full replay',result==candidate);positions.sort();ck('no overlap',all(a[1]<=b[0] for a,b in zip(positions,positions[1:])))
for x in read(T/'LOCATIONS.json'):
 b=(ROOT/x['path']).read_bytes();ck(x['id']+' whole',h(b)==x['source_sha256']);span=b''.join(b.splitlines(keepends=True)[x['start_line']-1:x['end_line']]);ck(x['id']+' span',h(span)==x['excerpt_sha256']);ck(x['id']+' inline',span==x['excerpt'].encode())
R=ROOT/'work/quartic-v14-prep/independent-source-review/yuan-h5-review-001'
ck('source review manifest',h((R/'MANIFEST.json').read_bytes())=='d18733fb25bfbc8258104b9f3b8148bcf3f2c1b81b56179ba87f9d159c21e313')
for x in read(R/'MANIFEST.json')['files']:
 b=(ROOT/x['path']).read_bytes();ck('source review member '+Path(x['path']).name,h(b)==x['sha256'] and len(b)==x['bytes'])
ck('two active Yuan cites',len(re.findall(rb'\\cite(?:\[[^\]]*\])?\{Yuan2024\}',candidate))==2)
ck('canonical intended path',m['canonical_proof_path']=='research/version14/proofs/yuan-final-source-v1/PROOF.md')
(OUT/'CHECKS.json').write_text(json.dumps({'scope':'Exact structural checks, not mathematical automation','checks':checks,'passed':len(checks),'candidate_sha256':h(candidate)},indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'passed':len(checks),'candidate_sha256':h(candidate)}))
