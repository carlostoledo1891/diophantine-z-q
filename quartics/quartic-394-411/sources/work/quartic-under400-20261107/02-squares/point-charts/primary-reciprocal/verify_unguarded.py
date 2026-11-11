"""Exact deletion certificate; does not prove the arithmetic V0 exclusion."""
from pathlib import Path
import sys,json,copy,math,functools
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parents[1]));import verify494 as P
c=P.read(H/'certificate428.json');g=P.read(H/'candidate428-ir.json');u=P.read(H/'candidate427-ir.json');uc=P.read(H/'certificate427.json')
assert P.sha(H/'candidate428-ir.json')==c['candidateSha256']=='236e837094097aef4596a225f541347f314f7596511b75cbae09b722fa4a184d'
assert P.sha(H/'candidate427-ir.json')==uc['candidateSha256']
expected=copy.deepcopy(g);expected['coordinates']=[x for x in g['coordinates'] if x['id']!=c['guardCoordinate']];expected['residuals']=[x for x in g['residuals'] if x['id']!=c['guardRow']]
assert expected==u
total={}
for row in u['residuals']:
 p=P.normalized(P.poly(row['terms']));assert max(sum(x!=-1 for x in m) for m in p)<=2
 total=P.add(total,P.mul(p,p))
assert total==P.poly(P.read(H/'polynomial427.json')['terms'])
assert P.sha(H/'polynomial427.json')==uc['polynomialSha256']
assert {v for m in total for v in m if v!=-1}=={x['id'] for x in u['coordinates']}
assert len(u['coordinates'])==427 and len(u['residuals'])==396
assert functools.reduce(math.gcd,(abs(v.numerator) for v in total.values()),0)==1
result={'passed':True,'sourceCandidate428Sha256':c['candidateSha256'],'candidate427Sha256':uc['candidateSha256'],'polynomial427Sha256':uc['polynomialSha256'],'counts':uc['counts'],'scope':'Only exact guard deletion and full SOS; guard-free arithmetic requires independent review.'}
(H/'verification427.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
