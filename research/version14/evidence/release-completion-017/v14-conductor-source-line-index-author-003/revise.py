import copy,hashlib,json
from pathlib import Path
OUT=Path(__file__).resolve().parent;R=OUT.parent;ROOT=OUT.parents[2];P=ROOT/'work/quartic-v14-release/preview-repository';OLD=R/'v14-conductor-source-line-index-author-001'
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def write(n,x):(OUT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
rows=json.loads((OLD/'INDEX.json').read_bytes());roles=json.loads((OLD/'SOURCE-ROLES.json').read_bytes())
path='research/version14/evidence/current-reviewed-003/v14-sign-conductor-002/PROOF.md';raw=(P/path).read_bytes();ls=raw.splitlines(keepends=True)
def loc(a,b):return {'pin':{'side':'head','path':path,'sha256':sha(raw)},'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(ls[a-1:b]))}
coll=json.loads((R/'v14-active-connection-collection-012/COMPONENTS.json').read_bytes());template=next(c for c in coll if c['use']['id']=='ARITH-ACTIVE-B-SIGN-DEGREE')
c={'use':copy.deepcopy(template['use']),'connection':copy.deepcopy(template['connection'])};u=c['use'];co=c['connection'];ident='ACTIVE-SIGN-NOTE-INTEGRAL-DEGREE'
profile=copy.deepcopy(co['available_assertion']);profile['statement']='For genuine isogenies of abelian surfaces, degree is multiplicative and deg([n])=n^4 for nonzero integers n.'
profile['objects']='Integral denominator-cleared isogenies [m]u and their compositions with multiplication maps on abelian surfaces.'
profile['hypotheses']='Characteristic zero; m,n are positive integers for which the representatives are genuine isogenies.'
profile['quantifiers']='Every such integral representative and positive m,n.'
profile['parameter_range']='Genuine integral isogenies only; rational quasi-isogeny degree is subsequently defined and proved well-defined.'
profile['constants']='deg([n]([m]u))=n^4 deg([m]u).'
profile['exceptional_cases']='No degree assigned to [1/m] as an algebraic morphism; no rational discrepancy or finite cochain conclusion in this source input.'
profile['limit_order']='Apply the integral theorem before dividing numerical degrees by m^4.'
u.update(id=ident,consumer='H5-CURRENT-SIGN-COCYCLE',passages=[ident+'-P1'],assertion=profile,reason='Apply the integral multiplication-degree theorem to the two cleared representatives at lines17–18; the following local algebra derives denominator independence and the scalar law. This source input is not that derived output.',shared_contract_justification=None,inline_argument=loc(17,18))
co.update(use_id=ident,use_sha256=digest(u),available_assertion=copy.deepcopy(profile),needed_assertion=copy.deepcopy(profile),required_capabilities=['integral-multiplication-degree'],available_capabilities=['integral-multiplication-degree'],derived_capabilities=[],consumer_locations=[loc(17,18)])
co['connecting_derivation'].update(kind='derivation',location=loc(17,18),application_id=None,output_assertion=copy.deepcopy(profile))
co['adverse_cases']={'status':'checked','reason':profile['exceptional_cases'],'evidence':[loc(13,26)]}
c.update(state='author proposal pending independent review',initial_mapping=[])
for row,role in zip(rows,roles):
 i=row['location']['start_line'];olduses=row['use_ids'];role['outgoing_family_uses_provenance_only']=olduses
 row['use_ids']=[];row['claim_ids']=[]
 if i in [17,18]:
  row.update(use_ids=[ident],claim_ids=['H5-CURRENT-SIGN-COCYCLE'],reason='Actual application of the integral Milne multiplication-degree law to cleared isogenies.',no_imports_reason=None)
  role.update(role='actual integral-degree application',source_binding_use_ids=[ident])
 elif 15<=i<=38 and ls[i-1].strip():
  row.update(reason='Local algebra following the explicitly bound integral degree input: clearing denominators, comparing equal maps, positive real fourth roots and coboundary multiplication.',no_imports_reason='This passage derives the generic lemma; later family-specific applications of that lemma are outgoing provenance, not inputs to its own proof.')
  role['role']='local derivation'
 elif i==13:
  role['source_binding_use_ids']=[ident]
 elif i==46:
  row.update(reason='Elementary restriction of an assumed global isomorphism to subgroups and equality of the terms defining the conductor.',no_imports_reason='The global isomorphism is an explicit conditional premise. No actual beta or b global isomorphism is established or invoked in this generic argument.')
  role['role']='conditional local derivation'
 elif i==48:
  row.update(reason='Declares the separate modular conductor theorem needed by any caller and the additional multiplicity data required for larger Tate modules.',no_imports_reason='This is a required-input boundary, not a proof or a family-specific application of Carayol. Actual family level uses remain outgoing provenance only.')
  role['role']='conditional source requirement'
write('COMPONENTS.json',[c]);write('INDEX.json',rows);write('SOURCE-ROLES.json',roles);write('USE-LOCATION-DELTAS.json',[])
for n in ['PENDING.json','PROVENANCE.json']:(OUT/n).write_bytes((OLD/n).read_bytes())
write('CHECKS.json',{'lines':52,'all_lines_exact_once':[r['location']['start_line'] for r in rows]==list(range(1,53)),'new_use_hash':digest(u)==co['use_sha256'],'family_output_as_input_removed':True,'old_use_bodies_changed':False})
write('DELTA.json',{'prior_manifest':sha((OLD/'MANIFEST.json').read_bytes()),'correction':'Replace output-as-input appends by a narrow integral degree application at17–18 and explicit local derivation/source-role classifications. No audit aggregate is used as mathematical consumer.'})
write('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((OUT/'MANIFEST.json').read_bytes()))
