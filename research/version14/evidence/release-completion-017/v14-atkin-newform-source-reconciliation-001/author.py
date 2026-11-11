import copy,hashlib,json
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def dig(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def save(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
initial=R/'v14-atkin-newform-source-initial-root-001/INITIAL002.json';iv=json.loads(initial.read_bytes())
raw=(R/'v14-atkin-newform-input-author-002/SOURCE-CONNECTION.md').read_bytes();assert sha(raw)==iv['source_sha256']
def loc(a,b):return {'pin':{'side':'head','path':iv['source_path'],'sha256':sha(raw)},'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(raw.splitlines(keepends=True)[a-1:b]))}
cc=json.loads((R/'v14-active-connection-collection-017/COMPONENTS.json').read_bytes());byid={c['use']['id']:c for c in cc}
c=copy.deepcopy(byid['ACTIVE-HEEGNER-ATKIN-BASED-FORMULA']);u=c['use'];co=c['connection'];ident='ACTIVE-ATKIN-NEWFORM-QUOTIENT-DIFFERENTIAL';profile=copy.deepcopy(co['available_assertion'])
u.update(id=ident,assertion=profile,passages=[ident+'-P1'],inline_argument=loc(11,11),reason='The primitive Shimura differential-line input is consumed by the actual quotient comparison, separately from Atkin-Lehner eigen-action.',shared_contract_justification=None)
co.update(use_id=ident,use_sha256=dig(u),needed_assertion=copy.deepcopy(profile),required_capabilities=[ident],available_capabilities=[ident],derived_capabilities=[],consumer_locations=[loc(11,11)])
co['connecting_derivation'].update(kind='identification',location=loc(11,11),application_id=None,output_assertion=copy.deepcopy(profile));co['adverse_cases']={'status':'checked','reason':'For pi obtained by composition with a nonzero characteristic-zero isogeny, pullback of a nonzero invariant differential is nonzero, so only its scalar changes. This input neither supplies W eigen-action nor the cuspidal annihilator.','evidence':[loc(11,11),u['supplier']['location']]}
c['initial_mapping']=[];save('COMPONENTS.json',[c])
mapping={1:[],2:[],3:[],4:[],5:['ACTIVE-ATKIN-LEHNER-PRIMITIVE-EIGENLINE','ACTIVE-RC-AMIR-HONG-NEWFORM'],6:[ident,'ACTIVE-HEEGNER-ATKIN-BASED-FORMULA'],7:[]}
reasons={1:'Title only.',2:'Literal published theorem declaration. Its actual invocation is line9, not a self-use of the resulting eigenline.',3:'Published conventions and definitions; used to interpret the primitive theorem, not a new derived conclusion.',4:'Local derivative calculation: quotient rule gives determinant/(cz+d)^2, equal to the source slash when k=1; scalar matrices cancel.',5:'Apply the primitive theorem to the already supplied normalized newform with trivial character and exact level; no oldspace assertion.',6:'The generic quotient differential theorem gives the same line. A nonzero isogeny only rescales it. The based formula is then invoked under the eigen-action established above; its finite annihilator and specialization remain separate supplied conditions.',7:'Explicitly excludes global root number, sign products and twist formulas.'}
rows=[]
for i,row in enumerate(iv['rows'],1):
 assert loc(row['start'],row['end'])['excerpt_sha256']==row['excerpt_sha256']
 rows.append({'initial_row':copy.deepcopy(row),'location':loc(row['start'],row['end']),'incoming_use_ids':mapping[i],'source_role_explanation':reasons[i],'outgoing_provenance_use_ids':['ACTIVE-ATKIN-LEHNER-PRIMITIVE-EIGENLINE'] if i in [2,3] else []})
save('RECONCILIATION.json',{'initial_path':str(initial),'initial_sha256':sha(initial.read_bytes()),'rows':rows,'scope':'Full thirteen-line source role reconciliation; underlying quotient and finite-annihilator conditions retain their original scope.'})
save('USE-LOCATION-DELTAS.json',[{'use_id':ident,'old_use_sha256':dig(byid[ident]['use']),'append_consumer_locations':[loc(line,line)],'shared_contract_justification':reason,'preserve_assertion':True} for ident,line,reason in [('ACTIVE-RC-AMIR-HONG-NEWFORM',9,'The same already constructed primitive rational weight-two form at its conductor is used in the Atkin theorem application.'),('ACTIVE-HEEGNER-ATKIN-BASED-FORMULA',11,'This invokes the same conditional based formula after the independent eigen-action is supplied; it does not use that formula to establish the eigen-action.')]])
save('CHECKS.json',{'initial_rows':len(rows),'raw_hashes':True,'use_hash':dig(u)==co['use_sha256']})
save('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
