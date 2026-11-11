"""Independently expand the pinned symbolic source; no producer imports."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent;W=H.parents[2]
def load(path,pin):
    raw=path.read_bytes(); assert hashlib.sha256(raw).hexdigest()==pin,path
    return json.loads(raw)
P=W/'quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2'
ir=load(P/'candidate299-ir.json','8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815')
tab=load(P/'polynomial299.json','e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c')
old=load(W/'quartic-optimization-20261107/resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json','6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a')
rr={r['id']:r for r in ir['residuals']}; cc={c['id']:c for c in ir['coordinates']}
oldrr={r['id']:r for r in old['residuals']}
assert len(rr)==len(ir['residuals'])==279 and len(cc)==len(ir['coordinates'])==299
assert all(rr[i]==oldrr[i] for i in [504,1903])
assert ir['fixedParameter']==old['fixedParameter']
assert {r['id'] for r in rr.values() if any(t['sPower'] for t in r['terms'])}=={504,1903}
total=defaultdict(int); used=set()
for r in rr.values():
    q={(t['sPower'],tuple(t['monomial'])):F(t['coefficient']) for t in r['terms']}
    assert len(q)==len(r['terms']) and all(q.values())
    assert all(len(m)<=2 for s,m in q)
    used.update(i for s,m in q for i in m)
    den=lcm(*(c.denominator for c in q.values())); g=gcd(*(int(c*den) for c in q.values()))
    terms=[(s,m,int(c*den)//g) for (s,m),c in q.items()]
    for j,(s,m,c) in enumerate(terms):
        for k in range(j,len(terms)):
            t,n,d=terms[k];total[(s+t,tuple(sorted(m+n)))]+=c*d*(1 if j==k else 2)
total={k:v for k,v in total.items() if v}
actual={(t['sPower'],tuple(t['monomial'])):int(t['coefficient']) for t in tab['terms']}
assert total==actual and len(actual)==len(tab['terms'])
assert used==set(cc) and max(len(m) for s,m in total)==4 and gcd(*total.values())==1
out={'status':'PASS','sourceSha256':'8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815',
     'variables':len(cc),'residuals':len(rr),'coefficientPowerEntries':len(total),
     'monomials':len({m for s,m in total}),'degree':4,'content':1,
     'unchangedParameterRows':[504,1903], 'onlyParameterConsumers':[504,1903],
     'scope':'Finite construction only; no new reciprocal299 arithmetic acceptance.'}
(H/'SOURCE-CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
