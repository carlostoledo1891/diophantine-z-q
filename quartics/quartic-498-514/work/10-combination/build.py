from package_paths import reference_repo
"""Compose exact, name-matched patches; expand all residual squares over Z[C]."""
from pathlib import Path
from fractions import Fraction as Q
from functools import reduce
from math import gcd,lcm
import json,hashlib,copy
H=Path(__file__).resolve().parent
W=H.parent
R=reference_repo()
BASE=R/'quartics/quartic-523-540/final523_540/symbolic523/candidate-ir.json'
DEPTH=W/'03-depth/beta12/final/candidate-ir.json'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pol(ts):return {(t.get('sPower',0),tuple(t['monomial'])):Q(t['coefficient']) for t in ts}
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(c)} for (s,m),c in sorted(p.items()) if c]
def norm(p):
 d=reduce(lcm,(c.denominator for c in p.values()),1);g=reduce(gcd,(abs(int(c*d)) for c in p.values()),0)
 return {m:c*Q(d,g) for m,c in p.items()}
def remap(p,mp):return {(s,tuple(sorted(mp[i] for i in m))):c for (s,m),c in p.items()}
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n', encoding='utf-8', newline='\r\n')
def build(product=False):
 b=read(BASE); d=read(DEPTH); bc={c['id']:c for c in b['coordinates']}; names={c['name']:c['id'] for c in d['coordinates']}
 mapping={i:names[c['name']] for i,c in bc.items() if c['name'] in names}
 br={r['id']:r for r in b['residuals']}; rows={r['name']:copy.deepcopy(r) for r in d['residuals']}
 coords={c['id']:copy.deepcopy(c) for c in d['coordinates']}; operations=[]
 specs=[('02-squares/candidate520-ir.json',[399,443,487],[370,414,458]),
        ('04-charts/candidate-518.json',[101,109,117,125,133],[53,61,69,77,85]),
        ('05-anchor/candidate522-smallcoeff-ir.json',[539],[507])]
 # Deleted pole rows are identified by exact names below, not guessed IDs.
 specs[0]=(specs[0][0],specs[0][1],[r['id'] for r in b['residuals'] if r['name'] in [f'detector{k}.U2.definition' for k in range(3)]])
 if product:specs.append(('06-product/candidate518-ir.json',list(range(515,528)),list(range(481,494))))
 for path,removed,deleted in specs:
  p=W/path; patch=read(p); pr={r['id']:r for r in patch['residuals']}; pc={c['id']:c for c in patch['coordinates']}
  local=dict(mapping)
  for i,c in pc.items():
   if i not in bc:
    new=max(coords)+1;local[i]=new;coords[new]=dict(c,id=new)
  changes=[]
  for i,r in br.items():
   old=r['name'];before=pol(r['terms'])
   if i in deleted:
    assert norm(pol(rows[old]['terms']))==norm(remap(before,local)),old
    del rows[old];continue
   assert i in pr
   after=pol(pr[i]['terms'])
   if norm(before)==norm(after):continue
   assert norm(pol(rows[old]['terms']))==norm(remap(before,local)),old
   rows[old]=dict(rows[old],terms=terms(remap(after,local)))
   changes.append({'sourceRow':i,'name':old,'targetRow':rows[old]['id']})
  for i,r in pr.items():
   if i not in br:
    new=max(rr['id'] for rr in rows.values())+1
    rows[r['name']]=dict(r,id=new,terms=terms(remap(pol(r['terms']),local)))
  for i in removed:del coords[local[i]]
  for i,c in pc.items():
   if i in bc and bc[i]['name']!=c['name']:coords[local[i]]['name']=c['name']
  operations.append({'source':str(p),'sha256':sha(p),'removedCoordinates':[local[i] for i in removed],
                     'deletedRows':[br[i]['name'] for i in deleted],'changedRows':changes,'coordinateMap':local})
 out={'format':'combined-quadratic-residual-system-v1','fixedParameter':{'name':'C','value':'3^(2^25)','coordinate':False},
      'coordinates':list(coords.values()),'residuals':list(rows.values()),'status':'candidate; inherited arithmetic assumptions retained'}
 count=len(coords);tag=str(count);write('candidate'+tag+'-ir.json',out)
 total={}
 for r in out['residuals']:
  p=norm(pol(r['terms']))
  for (s,m),a in p.items():
   for (t,n),bval in p.items():
    k=(s+t,tuple(sorted(m+n)));total[k]=total.get(k,0)+a*bval
 total={k:v for k,v in total.items() if v}
 assert {i for s,m in total for i in m}==set(coords)
 assert max(len(m) for s,m in total)==4
 grouped={}
 for (s,m),v in total.items():grouped.setdefault(m,{})[s]=int(v)
 assert any(v=={0:1} for v in grouped.values())
 fixed=max(abs(v) for (s,m),v in total.items() if s==0)
 assert fixed.numerator.bit_length()<2048
 c2=[(m,v) for m,v in grouped.items() if 2 in v]
 assert c2==[((57,57),{2:16})],c2
 assert max(abs(v) for (s,m),v in total.items() if s==1)<=48
 write('polynomial'+tag+'.json',{'fixedParameter':out['fixedParameter'],'terms':terms(total)})
 stats={'coordinates':count,'witnesses':count-1,'residuals':len(rows),'degree':4,'monomials':len(grouped),'coefficientTerms':len(total),
        'content':1,'maxFixedCoefficientBits':fixed.numerator.bit_length(),'largestAbsoluteCoefficient':'16*C^2; C=3^(2^25)',
        'candidateSha256':sha(H/('candidate'+tag+'-ir.json')),'polynomialSha256':sha(H/('polynomial'+tag+'.json'))}
 write('certificate'+tag+'.json',{'baseline':str(BASE),'baselineSha256':sha(BASE),'depthSource':str(DEPTH),'depthSha256':sha(DEPTH),'operations':operations,'statistics':stats})
 print(json.dumps(stats,indent=2))
if __name__=='__main__':
 import sys
 build('--product' in sys.argv)

