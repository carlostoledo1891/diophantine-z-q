"""Scaled biquadratic addition charts, proposed by agent10."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,copy
H=Path(__file__).resolve().parent;R=H.parents[3]/'quartic-version6-release/repository';sys.path.insert(0,str(H.parents[1]));import verify494 as P
S=H.parent/'primary-reciprocal/candidate427-ir.json';M=R/'quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json'
assert P.sha(S)=='6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4'
old=P.read(S);sem=P.read(M);cn={c['name']:c['id'] for c in old['coordinates']};mp={c['id']:cn[c['name']] for c in sem['coordinates'] if c['name'] in cn}
def val(n):return tuple({tuple(sorted(-1 if x==-1 else mp[x] for x in m)):c for m,c in P.poly(sem['values'][n+'.'+str(i)]['terms']).items()} for i in range(2))
def v(n):return tuple(P.mon(cn[n+str(i)]) for i in range(2))
def add(a,b):return tuple(P.add(x,y) for x,y in zip(a,b))
def sub(a,b):return tuple(P.add(x,y,-1) for x,y in zip(a,b))
def sc(a,k):return tuple({m:c*k for m,c in x.items() if c*k} for x in a)
def mul(a,b):return P.add(P.mul(a[0],b[0]),P.mul(a[1],b[1]),2),P.add(P.mul(a[0],b[1]),P.mul(a[1],b[0]))
def encode(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(c)} for m,c in sorted(p.items())]
new=copy.deepcopy(old);rows={r['name']:r for r in new['residuals']};removed=set();deleted=set();ops=[];renames={};D=({():F(11)},{():F(-6)});one=({():F(1)},{})
s=v('primary.negativeReciprocalZ0.')
for i,root in enumerate(['A','S','T','Z'],1):
 Vname='V'+str(i);Uname='U'+str(i);primary='U'+root;pre=Vname+'.biquadratic.'
 a,b,c=[val(root+'.'+n) for n in ['h','j','x']]
 V,I,Q,W,K=[v(n) for n in [primary+'.reciprocal.r',primary+'.reciprocal.J',Vname+'.reciprocal.g.',Vname+'.reciprocal.u.',Vname+'.reciprocal.k.']]
 L=val('L'+str(i));z=val(Vname+'.z');YU=val('testSquare.1.'+str(i-1));YV=val('log'+Vname+'.fSquare')
 ex=[(primary+'.reciprocal.f.',sub(mul(V,Q),mul(c,W)),pre+'cross.'),
 (primary+'.reciprocal.curve.',sub(add(add(add(mul(V,V),mul(Q,Q)),mul(D,mul(W,W))),sc(mul(b,W),2)),one),pre+'curve.'),
 (Vname+'.reciprocal.g.',sub(sub(sub(mul(a,I),mul(b,V)),mul(c,Q)),mul(D,mul(V,W))),pre+'I.'),
 (Vname+'.reciprocal.u.',add(add(add(mul(a,K),mul(b,Q)),mul(c,V)),mul(D,mul(Q,W))),pre+'K.'),
 ('L'+str(i)+'.definition.',sub(mul(I,L),mul(V,s)),None),
 (Vname+'.z.definition.',add(mul(K,z),Q),None),
 ('testSquare.1.'+str(i-1)+'.',sub(add(mul(D,mul(c,YU)),mul(I,I)),c),None),
 ('log'+Vname+'.fSquare.',sub(add(mul(D,mul(c,YV)),mul(K,K)),c),None)]
 changed=[]
 for oldpre,expr,newpre in ex:
  post='.definition' if oldpre.startswith('testSquare') or oldpre.endswith('fSquare.') else ''
  for j in range(2):
   name=oldpre+str(j)+post;row=rows[name];row['terms']=encode(expr[j]);changed.append(row['id'])
   if newpre:row['name']=newpre+str(j)
 for oldpre,newpre in [(primary+'.reciprocal.r',pre+'V.'),(primary+'.reciprocal.J',pre+'I.'),(Vname+'.reciprocal.g.',pre+'Q.'),(Vname+'.reciprocal.u.',pre+'W.'),(Vname+'.reciprocal.k.',pre+'K.')]:
  for j in range(2):renames[cn[oldpre+str(j)]]=newpre+str(j)
 for n in [Vname+'.reciprocal.k.',Vname+'.f.definition.']:
  for j in range(2):deleted.add(n+str(j))
 drop=[cn[n+'.f.'+str(j)] for n in [Uname,Vname] for j in range(2)];removed.update(drop)
 ops.append({'root':root,'primary':primary,'V':Vname,'U':Uname,'removedCoordinates':drop,'changedRows':changed})
new['residuals']=[r for n,r in rows.items() if n not in deleted];new['coordinates']=[dict(c,name=renames.get(c['id'],c['name'])) for c in new['coordinates'] if c['id'] not in removed];new['status']='Candidate pending independent review: scaled biquadratic addition.'
def write(n,obj):(H/n).write_text(json.dumps(obj,indent=2)+'\n')
write('candidate411-ir.json',new);total={}
for row in new['residuals']:
 p=P.normalized(P.poly(row['terms']));total=P.add(total,P.mul(p,p))
write('polynomial411.json',{'fixedParameter':new['fixedParameter'],'terms':encode(total)})
cert={'source':str(S),'sourceSha256':P.sha(S),'semanticSource':str(M),'semanticSourceSha256':P.sha(M),'candidateSha256':P.sha(H/'candidate411-ir.json'),'polynomialSha256':P.sha(H/'polynomial411.json'),'operations':ops,'deletedRowNames':sorted(deleted),'counts':{'variables':len(new['coordinates']),'witnesses':len(new['coordinates'])-1,'residuals':len(new['residuals']),'monomials':len({tuple(x for x in m if x!=-1) for m in total}),'degree':max(sum(x!=-1 for x in m) for m in total)}}
write('certificate411.json',cert);print(json.dumps(cert['counts'],indent=2))
