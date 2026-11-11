"""Producer-free exact ordinary lifting, decimal table parsing and complete SOS."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json,re
H=Path(__file__).resolve().parent
def read(p,pin):
 raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==pin,p
 return json.loads(raw)
source=read(H.parents[2]/'quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/candidate299-ir.json','8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815')
source_table=read(H.parents[2]/'quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2/polynomial299.json','e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c')
source_rows={r['id']:r for r in source['residuals']};source_coords={c['id']:c for c in source['coordinates']}
K=next(int(t['coefficient']) for t in source_table['terms'] if not t['sPower'] and not t['monomial'])
pins={316: ('07b84f80f2bcbd21f2ad9d7fa41d7bdaea12ff8fd8ec9092729c7e83fb51059f', 'cf01b5e68c9cefb4c11d06176ca97101b458391876d5960958b87c229397b13b', 'd3638977afad0f1c0fc8869294bab760a1768e4dbfd64af0c07fc9c45fd7191f'), 315: ('f9a6fab1b59cb744db80df93c0231b4075f654d8dbf80f4720c24d99036d3e4a', 'c53b8e0f61c37ebd94a44494b142329a7a72a937853adfa629eba838301fdefe', '6ba99ca43675b5c47a102b64e49c11d4bba4d63f9f8f2f6a87443906795e110e'), 314: ('02b8b6a8b13a566ef520c7a65ec58fd6e63bafa9d7d447e323864b1bae29a5f7', '2ea9fb17223a2e2a4fbf98f113d9e0e1da7019a74f4d2c7cefdb31e5b4637028', 'efb34a9664a3a2c5b0abe548463e646ba18d6f7e5ab5d9eff9e80bb8b461291e')}
chains={316:[513]*9+[2]+[0]*6,315:[1025]*10+[2]+[0]*4,314:[2049]+[2048]*11+[0,0]}

def poly(row,symbolic=False):
 if not symbolic:assert all(t['sPower']==0 for t in row['terms'])
 out={tuple([-1]*t['sPower']+t['monomial']):F(t['coefficient']) for t in row['terms']}
 assert len(out)==len(row['terms']) and all(out.values())
 return out
def mul(a,b):
 z=defaultdict(F)
 for m,c in a.items():
  for n,e in b.items():z[tuple(sorted(m+n))]+=c*e
 return {m:c for m,c in z.items() if c}
q={(83,83):F(48),(87,87):F(48),(89,89):F(432)}
assert {r['id'] for r in source['residuals'] if any(t['sPower'] for t in r['terms'])}=={504,1903}
checks=[]
for size,(ih,ph,th) in pins.items():
 path=H/str(size);ir=read(path/'candidate-ir.json',ih);table=read(path/'polynomial.json',ph)
 rr={r['id']:r for r in ir['residuals']};cc={c['id']:c for c in ir['coordinates']}
 assert len(rr)==len(ir['residuals']) and len(cc)==len(ir['coordinates'])
 exponents=chains[size];last=1000+len(exponents);added=set(range(1000,last+1))
 assert set(rr)==set(source_rows)|added and set(cc)==set(source_coords)|added
 assert not added&set(source_rows) and not added&set(source_coords)
 assert all(cc[i]==c for i,c in source_coords.items())
 assert all(rr[i]==r for i,r in source_rows.items() if i not in {504,1903})
 for key,value in source.items():
  if key not in {'coordinates','residuals','status','fixedParameter'}:assert ir[key]==value
 assert ir['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':True,'sourceCoordinate':last}
 assert poly(rr[1000])=={(1000,):1,(83,83):-48,(87,87):-48,(89,89):-432}
 values=[]
 for j,a in enumerate(exponents):
  i=1001+j
  assert poly(rr[i])=={(i,):1,(() if j==0 else (i-1,i-1)):-3**a}
  values.append(a if j==0 else 2*values[-1]+a)
 assert values[-1]==2**25
 assert poly(rr[1903])=={(903,):1,(543,544):-2,(1000,last):-1}
 assert poly(rr[504])=={(55,55):1,(56,56):6,(57,57):-2,(57,last):-4,(903,903):-3}
 # Substitute the uniquely determined Q and final C symbol to recover each source row exactly.
 for rowid in [504,1903]:
  recovered=defaultdict(F)
  for m,c in poly(rr[rowid]).items():
   term={():c}
   for i in m:term=mul(term,q if i==1000 else {(-1,):F(1)} if i==last else {(i,):F(1)})
   for m,c in term.items():recovered[m]+=c
  assert {m:c for m,c in recovered.items() if c}==poly(source_rows[rowid],True)
 total=defaultdict(int);used=set()
 for row in rr.values():
  p=poly(row);assert max(map(len,p))<=2
  used.update(i for m in p for i in m)
  den=lcm(*(c.denominator for c in p.values()));g=gcd(*(int(c*den) for c in p.values()))
  ts=[(m,int(c*den)//g) for m,c in p.items()]
  for j,(m,c) in enumerate(ts):
   for k in range(j,len(ts)):
    n,e=ts[k];total[tuple(sorted(m+n))]+=c*e*(1 if j==k else 2)
 total={m:c for m,c in total.items() if c}
 assert total==poly(table) and used==set(cc)
 assert (len(cc),len(rr),len(total))==(size,size-20,{316: 6678, 315: 6675, 314: 6672}[size])
 assert gcd(*total.values())==1 and max(map(len,total))==4
 maximum=max(abs(c) for c in total.values());assert maximum==3**(2*max(exponents))+K==total[()]
 text=(path/'polynomial.txt').read_bytes();assert hashlib.sha256(text).hexdigest()==th
 parsed={}
 for line in text.decode('ascii').splitlines():
  coefficient,word=line.split('\t');mono=[]
  if word!='1':
   for token in word.split('*'):
    match=re.fullmatch(r'x(\d+)(?:\^(\d+))?',token);assert match
    mono.extend([int(match[1])]*int(match[2] or 1))
  mono=tuple(mono);assert mono==tuple(sorted(mono)) and mono not in parsed
  parsed[mono]=int(coefficient)
 assert parsed==total
 checks.append({'variables':size,'witnesses':size-1,'residuals':len(rr),'monomials':len(total),'chainGates':len(exponents),'valueExponents':values,'maximumCoefficientBits':maximum.bit_length(),'maximumCoefficientDigits':len(str(maximum)),'maximumCoefficientExpression':f'3^{2*max(exponents)}+K','textBytes':len(text),'withinReleased3247BitCap':maximum.bit_length()<=3247,'within8193BitCap':maximum.bit_length()<=8193,'sourceRowsRecovered':True,'allUnchangedObjectsChecked':True,'fullSOSAndTextTable':True})
assert checks[0]['withinReleased3247BitCap'] and not checks[1]['withinReleased3247BitCap']
assert all(r['within8193BitCap'] for r in checks)
out={'status':'PASS','sourceSymbolicSha256':'8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815','inheritedConstantBits':K.bit_length(),'companions':checks,'acceptance':'new composition requires independent review'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
