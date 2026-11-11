"""Independent checker for scalar forward-power denominator consolidation."""
import json,hashlib,math
from pathlib import Path
from fractions import Fraction as Q
H=Path(__file__).resolve().parent
SRC=H.parent.parent/'quartic-version6-release/repository/quartics/quartic-498-514/candidate498-ir.json'
def read(ts):return {(t.get('sPower',0),tuple(t['monomial'])):Q(t['coefficient']) for t in ts if Q(t['coefficient'])}
def add(a,b):
 a=a.copy()
 for k,v in b.items():a[k]=a.get(k,Q(0))+v
 return {k:v for k,v in a.items() if v}
def times(a,b):
 d={}
 for (s,m),v in a.items():
  for (t,n),w in b.items():
   k=s+t,tuple(sorted(m+n));d[k]=d.get(k,Q(0))+v*w
 return {k:v for k,v in d.items() if v}
def sc(a,x):return {k:v*x for k,v in a.items() if v*x}
def v(i):return {(0,(i,)):Q(1)}
def c(x):return {(0,()):Q(x)} if x else {}
def primitive(a):
 den=math.lcm(*(x.denominator for x in a.values()));g=math.gcd(*(int(x*den) for x in a.values()))
 return sc(a,Q(den,abs(g)))
def same(a,b):
 a,b=primitive(a),primitive(b)
 return a==b or a==sc(b,-1)
def subst(a,i,p):
 out={}
 for (s,m),z in a.items():
  t={(s,tuple(j for j in m if j!=i)):z}
  for _ in range(m.count(i)):t=times(t,p)
  out=add(out,t)
 return out
base=json.loads(SRC.read_text());new=json.loads((H/'candidate496-ir.json').read_text());table=json.loads((H/'polynomial496.json').read_text())
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==new['status']['sourceSha256']
a={x['id']:read(x['terms']) for x in base['residuals']};b={x['id']:read(x['terms']) for x in new['residuals']}
removed=set(range(456,462))|{507,508};assert set(a)-set(b)==removed and set(b)-set(a)==set(range(600,606))
assert all(a[i]==b[i] for i in set(a)&set(b)-{509,510})
ac={x['id'] for x in base['coordinates']};bc={x['id'] for x in new['coordinates']}
assert ac-bc==set(range(490,496))|{537,538} and bc-ac==set(range(600,606))
r={}
assert a[456][0,()]==1
for (s,m),q in a[456].items():
 if m:
  assert m.count(490)==1;r[s,tuple(i for i in m if i!=490)]=-q
assert same(a[456],add(c(1),sc(times(r,v(490)),-1)))
for row,i,prev in [(457,491,490),(458,492,491),(459,493,492),(460,494,493),(461,495,494)]:assert same(a[row],add(v(i),sc(times(v(prev),v(prev)),-1)))
assert same(a[507],add(v(537),sc(times(v(495),v(508)),-1)))
assert same(a[508],add(v(538),sc(times(v(495),v(509)),-1)))
assert same(a[509],add(v(539),sc(times(v(538),v(538)),-1)))
assert same(a[510],add(add(v(540),sc(times(v(537),v(537)),-1)),sc(times(r,v(539)),-1)))
# Prove that the actual stored r is the contact polynomial in beta=2*X^2+3.
names={x['name']:x['id'] for x in base['residuals']}
assert same(a[names['inputSquare.definition']],add(v(248),sc(times(v(0),v(0)),-1)))
expanded=r
for coord,name in [(489,'scalar.r.definition'),(488,'scalar.rFour.definition'),(487,'scalar.rPair1.definition')]:
 p=a[names[name]];pivot=p[0,(coord,)]
 assert all(coord not in m or m==(coord,) for s,m in p)
 repl=sc(add(p,sc(v(coord),-pivot)),-1/pivot)
 expanded=subst(expanded,coord,repl)
beta=add(sc(v(248),2),c(3));expected=c(1)
for f in [beta,add(beta,c(-1)),add(beta,c(-2401)),add(sc(beta,32),c(343)),add(sc(beta,2),c(-1))]:expected=times(expected,f)
assert expanded==expected
previous=r
for i in range(600,606):assert same(b[i],add(v(i),sc(times(previous,previous),-1)));previous=v(i)
assert same(b[509],add(v(539),sc(times(v(509),v(509)),-1)))
assert same(b[510],add(add(times(v(605),v(540)),sc(times(v(508),v(508)),-1)),sc(times(r,v(539)),-1)))
# The only repurposed old coordinate is539 and its consumers are exactly these two rows.
assert {i for i,p in a.items() if any(539 in m for s,m in p)}=={509,510}
assert {i for i,p in b.items() if any(539 in m for s,m in p)}=={509,510}
assert len(bc)==496 and len(b)==465 and len(new['coordinates'])==496 and len(new['residuals'])==465
assert {i for p in b.values() for s,m in p for i in m}==bc
assert max(len(m) for p in b.values() for s,m in p)==2
# Upper-triangular square expansion, independently of the producer's multiplication.
sos={}
for p in b.values():
 ts=list(primitive(p).items())
 for i,((s,m),q) in enumerate(ts):
  for j in range(i,len(ts)):
   (t,n),w=ts[j];k=s+t,tuple(sorted(m+n));sos[k]=sos.get(k,Q(0))+q*w*(1 if i==j else 2)
sos={k:q for k,q in sos.items() if q};assert read(table['terms'])==sos
assert table['coordinates']==new['coordinates'] and table['fixedParameter']==new['fixedParameter']==base['fixedParameter']
assert all(q.denominator==1 for q in sos.values())
assert any(s==0 and abs(q)==1 and all(ss==0 for ss,mm in sos if mm==m) for (s,m),q in sos.items())
quad=[(m,q) for (s,m),q in sos.items() if s==2];assert len(quad)==1 and quad[0][1]==16
assert not any(s!=2 and m==quad[0][0] for s,m in sos)
assert max(abs(q.numerator).bit_length() for (s,m),q in sos.items() if s==0)<4096
assert max(abs(q.numerator) for (s,m),q in sos.items() if s==1)<2**4096
out={'verified':True,'variables':496,'witnesses':495,'residuals':465,'degree':4,'monomials':len({m for s,m in sos}),'content':1,'maximumCoefficient':'16*3^(2^26)','sourceSha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'candidateSha256':hashlib.sha256((H/'candidate496-ir.json').read_bytes()).hexdigest(),'polynomialSha256':hashlib.sha256((H/'polynomial496.json').read_bytes()).hexdigest(),'contactPolynomialIdentity':True,'scope':'Exact retained rows, private incidence, forward powers, contact-polynomial expansion, and full SOS. Nonzero r follows from the proved rational input-domain argument in REPORT.md; no new arithmetic input.'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

