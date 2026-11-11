import copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
OLD=OUT.with_name('v14-theta-active-author-001')
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def write(n,x):(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
assert sha((OLD/'MANIFEST.json').read_bytes())=='01fbaedacfbc2efa04a8359f6157a10aec4bc9e64c8011b040d6588ce490b80e'
raw=(ROOT/'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex').read_bytes();lines=raw.splitlines(keepends=True)
components=json.loads((OLD/'COMPONENTS.json').read_bytes())
for c in components:
    id=c['use']['id']
    if id in ('ACTIVE-THETA-T043','ACTIVE-THETA-T044'):
        a,b=(15705,15797) if id.endswith('T043') else (15798,15841)
        p={'pin':{'side':'head','path':'manuscripts/quartic_v14.tex','sha256':sha(raw)},'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(lines[a-1:b]))}
        c['use']['supplier']['location']=copy.deepcopy(p);c['use']['inline_argument']=copy.deepcopy(p)
        c['connection']['connecting_derivation']['location']=copy.deepcopy(p)
        c['connection']['adverse_cases']['evidence']=[p['pin']]
        c['connection']['use_sha256']=digest(c['use'])
    if c['use']['classification']!='dependency':
        c['historical_citation_inventory']=c['retained_separate_inputs'];c['retained_separate_inputs']=[]
    c['source_ancestry_status']='Historical family matches are candidates for exact current-source classification, not required use of superseded publications. No current source approval or ordinary ID is inferred from this inventory.'
write('COMPONENTS.json',components)
ancestry=[x for x in json.loads((OLD/'SOURCE-ANCESTRY.json').read_bytes()) if x['theta_use'] not in ('ACTIVE-THETA-T001','ACTIVE-THETA-T074')]
for x in ancestry:
    x['needed_source_binding']='Classify actual current import against accepted source/version records; preserve narrower local proof scope. Historical family label is not itself a required external theorem.'
    if x['historical_id'] in ('A028','A052'):
        x['current_route_notice']='Use current conductor-one, CM, specialization and Ribet/Voight scopes as appropriate. Old Cornut–Jetchev/Jetchev–Kane attribution is not automatically an active dependency.'
write('SOURCE-ANCESTRY.json',ancestry)
write('DELTA.json',{'predecessor_manifest_sha256':sha((OLD/'MANIFEST.json').read_bytes()),'changes':['T043 heading-only primary replaced by actual optimal-embedding and torsor proof15705–15797.','T044 blank primary replaced by actual conductor-one argument and finite sum15798–15841.','Background T001/T074 references removed from required ancestry inventory and retained as historical citations.','Source-family inventory explicitly requires current-source classification, preserving superseded CJ/Jetchev boundaries.'],'unchanged':'All mathematical assertions, classifications, consumer passages and other proof locations retained.'})
checks=[]
for c in components:
    if 'connection' not in c:continue
    for p in [c['use']['supplier']['location'],c['use']['inline_argument'],c['connection']['connecting_derivation']['location']]+c['connection']['consumer_locations']:
        assert p['excerpt_sha256']==sha(b''.join(lines[p['start_line']-1:p['end_line']]))
    assert digest(c['use'])==c['connection']['use_sha256']
    checks.append(c['use']['id'])
write('CHECKS.json',{'dependency_connections':len(checks),'all_primary_and_consumer_raw_spans':True,'all_canonical_use_digests':True,'background_records':2,'source_ancestry_is_not_closed':True})
write('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((OUT/'MANIFEST.json').read_bytes()))
