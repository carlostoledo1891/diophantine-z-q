from pathlib import Path
import json,hashlib
ROOT=Path.cwd(); P=ROOT/'work/quartic-optimization-20261107/resume-release-inventory-20261107-r2'; OUT=ROOT/'work/quartic-optimization-20261107/resume-review-inventory-r2-sol'
def load(p): return json.loads(p.read_bytes())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def canon(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
assert sha(P/'FROZEN-MANIFEST.json')=='56a0e6a76318e56af6158ea1ccb325457b0c3a4772974c5849b935b52c9ba97d'
for n,v in load(P/'FROZEN-MANIFEST.json').items(): assert sha(P/n)==v['sha256'] and (P/n).stat().st_size==v['bytes'],n
C=load(P/'CANDIDATES.json')['components']; A=load(P/'APPLICATION-DELTA.json'); repo=ROOT/'work/quartic-version6-release/repository'; B=load(repo/'docs/manuscript-revisions/version13/APPLICATIONS.json'); base={a['id']:a for a in B['applications']}
assert len(base)==len(A['applications'])==39
span_count=0
def walk(x):
 global span_count
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:
   f=ROOT/x['path']
   if not f.exists(): f=repo/x['path']
   assert f.exists(),x['path']
   assert sha(f)==x['sha256'],x['path']
   if 'start_line' in x:
    lines=f.read_bytes().splitlines(keepends=True); raw=b''.join(lines[x['start_line']-1:x['end_line']]); assert hashlib.sha256(raw).hexdigest()==x['sha256_raw_utf8_span'],x
    span_count+=1
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(A)
for a in A['applications']:
 assert canon(base[a['id']])==a['baselineRecordSha256Canonical'],a['id']
 assert a['baselineSource']==base[a['id']]['source']
 assert a['baselineConsumers']==base[a['id']]['consumers']
for key,c in C.items():
 ir=load(ROOT/c['candidate']['path']); assert len(ir['coordinates'])==c['variables'] and len(ir['residuals'])==c['residuals']
 assert c['componentAuthor']!=c['recordedReviewer'],key
 if c.get('comparedWith'):
  src=load(ROOT/C[c['comparedWith']]['candidate']['path'])
  for field in ('coordinates','residuals'):
   a={v['id']:v for v in src[field]}; b={v['id']:v for v in ir[field]}
   actual={'deleted':sorted(a.keys()-b.keys()),'added':sorted(b.keys()-a.keys()),'changed':sorted(i for i in a.keys()&b.keys() if a[i]!=b[i])}
   assert actual==c['objectDelta'][field],(key,field)
entries={e['id']:e for e in A['newInternalEntries']}
mismatches=[]
for a in A['applications']:
 forward=set(a['newEntryIds']); reverse={e['id'] for e in entries.values() if a['id'] in e['baselineApplications']}
 if forward!=reverse: mismatches.append({'application':a['id'],'onlyApplicationSide':sorted(forward-reverse),'onlyEntrySide':sorted(reverse-forward)})
R=load(P/'RETAINED-SOURCES.json')
for field in ('text','baselineManuscript','existingSourceCatalog','externalSources','inheritedInventory','compatibilityInventory','explicitInheritedReferences'): assert R[field]==B[field],field
result={'manifest':'passed','all_baseline_records_and_source_qualifications':'exact','raw_source_and_consumer_spans':span_count,'all_22_coordinate_and_residual_deltas':'passed','entry_application_edge_mismatches':mismatches}
(OUT/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n'); print(result)

