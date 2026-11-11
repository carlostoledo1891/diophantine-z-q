import copy,hashlib,json
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def dig(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def save(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
old=R/'v14-cj-local-structure-author-001'
src=old/'SOURCE-CONNECTION.md';raw=src.read_bytes();lines=raw.splitlines(keepends=True)
rel='research/version14/evidence/cj-local-structure-001/SOURCE-CONNECTION.md'
def loc(a,b):return {'pin':{'side':'head','path':rel,'sha256':sha(raw)},'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(lines[a-1:b]))}
components=json.loads((old/'COMPONENTS.json').read_bytes())
spec=[('QUADRATIC-EMBEDDING',6,[(7,7)]),('CONJUGACY',10,[(11,11),(19,19)]),('CENTRALIZER',14,[(15,15)]),('LOCAL-DIVISION',18,[(19,19)])]
out=[]
for c,(name,l,places) in zip(components,spec):
 c=copy.deepcopy(c);u=c['use'];co=c['connection'];ident='ACTIVE-CJ-LOCAL-PRIMITIVE-'+name
 profile=copy.deepcopy(co['available_assertion'])
 u.update(id=ident,passages=[ident+'-P'+str(i+1) for i in range(len(places))],assertion=profile,reason='Primitive published input used inside the local-structure proof; the specialized output of that proof is not used as its own premise.',inline_argument=loc(places[0][0],places[-1][1]),shared_contract_justification='The same specified-conjugacy theorem is used for the global/local identification and the later local embedding-class argument.' if len(places)>1 else None)
 u['supplier']['location']=loc(l,l);u['supplier']['statement']=profile['statement']
 co.update(use_id=ident,use_sha256=dig(u),supplier_passage_role='source_statement',available_assertion=copy.deepcopy(profile),needed_assertion=copy.deepcopy(profile),required_capabilities=[ident],available_capabilities=[ident],derived_capabilities=[],consumer_locations=[loc(a,b) for a,b in places])
 co['connecting_derivation'].update(kind='identification',location=loc(places[0][0],places[-1][1]),application_id=None,output_assertion=copy.deepcopy(profile))
 co['adverse_cases']={'status':'checked','reason':'Primitive statement only. Its specialized rational embedding, pointwise stabilizer and two local classes are derived separately. Geometric, integral global and analytic assertions are not supplied.','evidence':[loc(l,l)]+[loc(a,b) for a,b in places]}
 c['state']='Author proposal pending independent review';c['initial_mapping']=[];out.append(c)
save('COMPONENTS.json',out)
initial=R/'v14-final-composite-review-001/cj-local-source-initial-001/INITIAL-SOURCE-USES.json'
olduses=json.loads(initial.read_bytes())['uses']
roles=[('literal_source_statement',[out[0]['use']['id']],6,6),('local_specialization',[out[0]['use']['id']],7,7),('literal_source_statement',[out[1]['use']['id']],10,10),('local_specialization',[out[1]['use']['id']],11,11),('literal_source_statement',[out[2]['use']['id']],14,14),('local_dimension_argument',[out[2]['use']['id']],15,15),('literal_source_statement',[out[3]['use']['id']],18,18),('local_embedding_class_argument',[out[1]['use']['id'],out[3]['use']['id']],19,19),('correction_and_scope_boundary',[],20,23)]
rows=[]
for use,(role,ids,a,b) in zip(olduses,roles):
 rows.append({'initial_use_id':use['id'],'initial_use_sha256':dig(use),'classification':use['classification'],'source_role':role,'location':loc(a,b),'incoming_use_ids':ids if role!='literal_source_statement' else [],'outgoing_provenance_use_ids':ids if role=='literal_source_statement' else [],'scope':'Literal statements are declarations, not self-consumption. Local calculations consume only the listed primitive inputs; all geometric and analytic caller conditions remain separate.','unresolved_claims':[]})
save('RECONCILIATION.json',{'initial_pin':{'path':str(initial),'sha256':sha(initial.read_bytes())},'rows':rows,'scope':'Nine fresh source observations, four primitive theorem imports. This is not full CJ closure.'})
save('CHECKS.json',{'rows':len(rows),'components':len(out),'use_hashes_match':all(dig(c['use'])==c['connection']['use_sha256'] for c in out),'source_sha256':sha(raw),'passage_counts_match':all(len(c['use']['passages'])==len(c['connection']['consumer_locations']) for c in out)})
save('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
