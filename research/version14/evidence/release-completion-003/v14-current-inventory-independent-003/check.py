from pathlib import Path
import json,hashlib,copy,importlib.util
b=Path.cwd(); pr=b/'work/quartic-v14-release/preview-repository'; d=b/'work/source-risk-review-20261107/v14-current-inventory-003'; prefix='docs/manuscript-revisions/version14/'; rel=prefix+'APPLICATIONS.json'; mr=prefix+'inventory-install-manifest.json'; mp='manuscripts/quartic_v14.tex'
h=lambda x:hashlib.sha256(x).hexdigest()
oldraw=(pr/rel).read_bytes(); newraw=(d/'overlay'/rel).read_bytes(); old=json.loads(oldraw); new=json.loads(newraw)
ot=(b/'work/source-risk-review-20261107/v14-registry-integration-plan-001/preview-001/registered.tex').read_bytes(); nt=(pr/mp).read_bytes(); ol=ot.splitlines(keepends=True); nl=nt.splitlines(keepends=True)
assert h(oldraw)=='a3c7f119e53f59ed81f4f9a3ac6b57f069c1d24da191aef5e150b38a50933abf'
assert h(newraw)=='b6afe631461d60dec2b23bf0fea9c492726bd6605af535497fd72beb39f9a9f1'
assert h(ot)=='b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d'
assert h(nt)=='1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8'
spans=set(); refs=[]
def same(a,c,loc='$'):
 assert type(a) is type(c),loc
 if isinstance(a,dict):
  assert a.keys()==c.keys(),loc
  if a.get('path')==mp:
   assert a['sha256']==h(ot) and c['sha256']==h(nt),loc
   z=copy.deepcopy(c); z['sha256']=a['sha256']
   if 'start_line' in a:
    raw=b''.join(ol[a['start_line']-1:a['end_line']]); now=b''.join(nl[c['start_line']-1:c['end_line']])
    assert h(raw)==a['sha256_raw_utf8_span'] and h(now)==c['sha256_raw_utf8_span'],loc
    assert raw==now and nt.count(raw)==1,loc
    spans.add((a['start_line'],a['end_line'],a['sha256_raw_utf8_span']))
    for k in ('start_line','end_line','sha256_raw_utf8_span'):z[k]=a[k]
   else:assert loc=='$/manuscript',loc
   assert z==a,loc
   refs.append(loc);return
  for k in a:same(a[k],c[k],loc+'/'+k)
 elif isinstance(a,list):
  assert len(a)==len(c),loc
  for i,(x,y) in enumerate(zip(a,c)):same(x,y,loc+'/'+str(i))
 else:assert a==c,loc
same(old,new)
assert len(spans)==66 and len(refs)==1133
om=json.loads((pr/mr).read_bytes()); nm=json.loads((d/'overlay'/mr).read_bytes()); restored=copy.deepcopy(nm)
assert nm['files'][rel]=={'sha256':h(newraw),'bytes':len(newraw)}
assert nm['readOnlyDependencies'][mp]=={'sha256':h(nt),'bytes':len(nt)}
restored['files'][rel]=om['files'][rel];restored['readOnlyDependencies'][mp]=om['readOnlyDependencies'][mp]
assert restored==om
vf=pr/(prefix+'validate-applications.py'); spec=importlib.util.spec_from_file_location('v14validation',vf); v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
overlay={p.relative_to(d/'overlay').as_posix():p.read_bytes() for p in (d/'overlay').rglob('*') if p.is_file()}
assert set(overlay)=={rel,mr}
schema=v.parse((pr/(prefix+'validation-schema.json')).read_bytes()); result=v.validate(v.parse(newraw),schema,v.Files(pr,overlay))
mutations=[lambda x:x['applications'].pop(),lambda x:x['applications'][0]['obligations'].pop('required_inputs'),lambda x:x['edgeBindings'].pop(),lambda x:x.update(mathematicalAcceptanceClaim=True),lambda x:x['selected'].update(ordinary='ordinaryReciprocal299_315')]
for mutate in mutations:
 x=copy.deepcopy(new);mutate(x)
 try:v.validate(x,schema,v.Files(pr,overlay))
 except (v.Invalid,KeyError):pass
 else:raise AssertionError('negative control accepted')
print(json.dumps({'unique_raw_identical_spans':len(spans),'current_references':len(refs),'all_other_values_types_keys_preserved':True,'install_manifest_only_two_pin_changes':True,'validator':result,'negative_controls_rejected':len(mutations),'pins':{str(p.relative_to(b)):h(p.read_bytes()) for p in [d/'prepare.mjs',d/'DELTA.json',d/'RUN.json',d/'overlay'/rel,d/'overlay'/mr,vf,pr/(prefix+'validation-schema.json')]}}))
