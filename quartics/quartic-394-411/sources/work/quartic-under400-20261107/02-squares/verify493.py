"""Independent exact identities for the guarded-conic preparation replacement."""
from pathlib import Path
from fractions import Fraction as F
import json,functools,math
import verify494 as V
H=Path(__file__).resolve().parent

def scale(p,k):return {m:k*c for m,c in p.items() if k*c}
def main():
 V.main()
 c=V.read(H/'certificate493.json');src=Path(c['source']);assert V.sha(src)==c['sourceSha256']
 assert V.sha(H/'candidate493-ir.json')==c['candidateSha256'];assert V.sha(H/'polynomial493.json')==c['polynomialSha256']
 old=V.read(src);new=V.read(H/'candidate493-ir.json');before={r['id']:V.poly(r['terms']) for r in old['residuals']};after={r['id']:V.poly(r['terms']) for r in new['residuals']}
 b,t,t2,T,W,u2=[c['ids'][x] for x in ['b','t','t2','T','V','u2']];ra,rb,rc,rd=[c['rows'][x] for x in ['square','inverse','Vplus','U2']];K=F(c['K']);assert K>0
 B=scale(V.mon(b),-K);N=scale(V.mon(u2),K*K)
 old_t=V.mon(t);old_t2=V.mon(t2);old_T=V.mon(T);old_W=V.mon(W)
 assert before[ra]==V.add(V.mul(old_t,old_t),old_t2,-1)
 assert before[rb]==V.add(V.mon(),V.mul(B,V.add(old_T,old_t2,-1)),-1)
 assert before[rc]==V.add(scale(V.mon(),2),V.mul(old_T,old_W),-1)
 assert before[rd]==V.add(V.mul(V.add(old_W,B,-1),V.add(old_W,B,-1)),N,-1)
 A=V.add(V.mon(t,t),N,-1);I=V.add(V.mon(),V.mul(B,V.mon(t2)),-1);C=V.add(V.add(V.mul(N,V.mon(t2)),V.mon(T,T)),B,-1)
 assert after[ra]==A and after[rb]==I and after[rc]==C and rd not in after
 private={t,t2,T,W};block={ra,rb,rc,rd}
 assert all(not private.intersection(m) for r,p in before.items() if r not in block for m in p)
 assert all(after[r]==p for r,p in before.items() if r not in block)
 # Forward map newU=oldW-B; newJ=oldT-oldt2; newV=oldt*oldW.
 Jold=V.add(old_T,old_t2,-1)
 mp={t:V.add(old_W,B,-1),t2:Jold,T:V.mul(old_t,old_W)}
 assert V.sub(A,mp)==before[rd]
 assert V.sub(I,mp)==before[rb]
 expected=V.add(V.add(V.add(scale(V.mul(old_W,before[rc]),-1),V.mul(V.mul(old_W,old_W),before[ra])),V.mul(V.add(scale(old_W,2),B,-1),before[rb])),V.mul(Jold,before[rd]),-1)
 assert V.sub(C,mp)==expected
 # Reverse on d=B+U !=0: oldt=newV/d, oldt2=newV^2/d^2,
 # oldT=oldt2+J, oldW=d. Clearing d from old C gives this identity.
 U=V.mon(t);J=V.mon(t2);Y=V.mon(T);d=V.add(B,U)
 numerator=V.add(V.add(scale(d,2),V.mul(Y,Y),-1),V.mul(J,V.mul(d,d)),-1)
 identity=V.add(V.add(V.mul(V.add(B,scale(U,2)),I),V.mul(J,A),-1),C,-1)
 assert numerator==identity
 assert V.add(V.mul(V.add(d,B,-1),V.add(d,B,-1)),N,-1)==A
 # Exceptional branch U=-B: C+J*A+B*I = Y^2, hence Y=0 over Q.
 abranch=V.sub(A,{t:scale(B,-1)});cbranch=V.sub(C,{t:scale(B,-1)})
 assert V.add(V.add(cbranch,V.mul(J,abranch)),V.mul(B,I))==V.mul(Y,Y)
 # With oldt=0, oldt2=0, oldT=J and oldW=2B: residuals are0,I,2I,B^2-N.
 assert V.add(V.mul(B,B),N,-1)==abranch
 assert set(after)==set(before)-{rd}
 assert {x['id'] for x in new['coordinates']}=={x['id'] for x in old['coordinates']}-{W}
 assert old['fixedParameter']==new['fixedParameter'] and old['coordinates'][0]==new['coordinates'][0]
 assert {x for p in after.values() for m in p for x in m if x!=-1}=={x['id'] for x in new['coordinates']}
 assert all(sum(x!=-1 for x in m)<=2 for p in after.values() for m in p)
 total={}
 for p in after.values():
  terms=list(V.normalized(p).items())
  for i,(m,a) in enumerate(terms):
   for j in range(i,len(terms)):
    n,bb=terms[j];z=tuple(sorted(m+n));total[z]=total.get(z,F(0))+a*bb*(1 if i==j else 2)
 total={m:v for m,v in total.items() if v}
 assert total==V.poly(V.read(H/'polynomial493.json')['terms'])
 assert max(sum(x!=-1 for x in m) for m in total)==4
 assert functools.reduce(math.gcd,(abs(v.numerator) for m,v in total.items() if -1 not in m),0)==1
 assert len(new['coordinates'])==493 and len(after)==462 and len({tuple(x for x in m if x!=-1) for m in total})==24645
 assert {m:v for m,v in total.items() if m.count(-1)==2}=={(-1,-1,57,57):F(16)}
 assert (57,57) not in total and (-1,57,57) not in total
 assert max(abs(v) for m,v in total.items() if m.count(-1)==1)<=48
 assert max(abs(v.numerator).bit_length() for m,v in total.items() if -1 not in m)<2048
 print(json.dumps({'verified':True,'variables':493,'witnesses':492,'residuals':462,'degree':4,'monomials':24645,'content':1,'maxCoefficient':'16*3^(2^26)','candidateSha256':c['candidateSha256'],'polynomialSha256':c['polynomialSha256'],'preparationEquivalence':'Exact rational maps on all solutions; exceptional U=-B branch preserves U^2; B nonzero enforced by retained inverse equation.'},indent=2))
if __name__=='__main__':main()
