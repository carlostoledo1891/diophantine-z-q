import copy,hashlib,json
from pathlib import Path
W=Path.cwd(); P=Path(__file__).parent; A=P.parent/'v14-aggregate-schema2-author-002'
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def pin(p): return {'path':p.relative_to(W).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
def save(n,x): (P/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
old=load(A/'AGGREGATE.json'); new=copy.deepcopy(old)
ids=['KATO-1999-INDEX-AND-CLASS','QUARTIC-299-COMPOSITION','QUARTIC-394-COMPOSITION','QUARTIC-498-COMPOSITION']
placeholder='PENDING-CURRENT-KATO-AND-COMPOSITION-CARRYFORWARDS'
assert new['dependencies'].count(placeholder)==1
new['dependencies']=[d for d in new['dependencies'] if d!=placeholder]+ids
cf=P.parent/'v14-current-carryforward-adoption-002/MANIFEST.json'
review=P.parent/'v14-current-carryforward-adoption-review-001/REVIEW.md'
assert pin(cf)['sha256']=='053dac58ccfc52b43cd10ceda9c05bd41f43f112f828afceb71172eaed45beee'
assert pin(review)['sha256']=='1006f52298f71d7808d4e2a00ecc3867dbd9d42ab9cdad86992b528f10c4d16d'
assert {k:v for k,v in old.items() if k!='dependencies'}=={k:v for k,v in new.items() if k!='dependencies'}
save('AGGREGATE.json',new)
save('TRANSITION.json',{'predecessor':pin(A/'AGGREGATE.json'),'carryforward_manifest':pin(cf),'independent_carryforward_review':pin(review),'only_change':{'removed_dependency':placeholder,'added_dependencies':ids},'scope':'Bind the four accepted current carryforward applications at their exact conditional scopes. Historical394/411 and498/514 claims are not renamed299/314. All nine aggregate obligations, files and authors remain byte-equivalent values.','remaining':'GI proposals and original datum/beta quantitative normalization have their separate reviews. This transition is not a whole graph closure.','independent_transition_review':'pending'})
save('MANIFEST.json',{'files':[pin(p) for p in sorted(P.iterdir()) if p.is_file() and p.name!='MANIFEST.json']})
print(json.dumps({'manifest':pin(P/'MANIFEST.json'),'aggregate':pin(P/'AGGREGATE.json')}))
