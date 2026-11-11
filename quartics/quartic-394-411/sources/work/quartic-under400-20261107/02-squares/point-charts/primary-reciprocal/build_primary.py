"""Four reciprocal primary charts, including the natural identity branches."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,copy
H=Path(__file__).resolve().parent;W=H.parents[2];R=H.parents[3]/'quartic-version6-release/repository'
sys.path.insert(0,str(H.parents[1]));import verify494 as P
S=W/'10-combination/combined435-ir.json';SEM=R/'quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json'
assert P.sha(S)=='c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859'
old=P.read(S);sem=P.read(SEM);cn={c['name']:c['id'] for c in old['coordinates']};rn={r['name']:r['id'] for r in old['residuals']}
mp={c['id']:cn[c['name']] for c in sem['coordinates'] if c['name'] in cn}
def v(i):return P.mon(i)
def sc(a,k):return {m:x*k for m,x in a.items() if x*k}
def const(k):return {():F(k)} if k else {}
def fa(a,b):return tuple(P.add(x,y) for x,y in zip(a,b))
def fs(a,b):return tuple(P.add(x,y,-1) for x,y in zip(a,b))
def fc(a,k):return tuple(sc(x,k) for x in a)
def fm(a,b):return P.add(P.mul(a[0],b[0]),P.mul(a[1],b[1]),2),P.add(P.mul(a[0],b[1]),P.mul(a[1],b[0]))
def val(n):return tuple({tuple(sorted(-1 if x==-1 else mp[x] for x in m)):c for m,c in P.poly(sem['values'][n+'.'+str(i)]['terms']).items()} for i in range(2))
def coord(n):return tuple(v(cn[n+str(i)]) for i in range(2))
def encode(p):return [{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(c)} for m,c in sorted(p.items())]
rows={r['id']:copy.deepcopy(r) for r in old['residuals']};remove=set();renames={};ops=[];D=(const(11),const(-6));one=(const(1),{})
s=coord('primary.negativeReciprocalZ0.')
def replace(name,p,newname=None):
 i=rn[name];rows[i]['terms']=encode(p)
 if newname:rows[i]['name']=newname
for i,root in enumerate(['A','S','T','Z'],1):
 primary='U'+root;U='U'+str(i);V='V'+str(i);L='L'+str(i)
 a,b,c=[val(root+'.'+n) for n in ['h','j','x']]
 r=coord(primary+'.chart.h');J=coord(primary+'.chart.j');f=val(U+'.f');fv=val(V+'.f');z=val(V+'.z');ll=val(L)
 g=coord(V+'.slope.');u=coord(V+'.slopeSquare.') if V+'.slopeSquare.0' in cn else tuple(v(cn[V+'.slopeSquare.'+str(k)+'.quadratic']) for k in range(2))
 k=tuple(v(cn[V+'.yProduct.'+str(j)+'.quadratic']) for j in range(2))
 d=fa(c,fm(D,f))
 expressions=[(primary+'.chart.x.', '.definition',fs(f,fm(r,r)),primary+'.reciprocal.f.'),
 (primary+'.chart.equation.', '',fs(fa(fm(J,J),fm(D,fm(f,f))),one),primary+'.reciprocal.curve.'),
 (V+'.slope.definition.', '',fs(fa(fm(d,g),fm(b,r)),fm(a,J)),V+'.reciprocal.g.'),
 (V+'.slopeSquare.', '.definition',fs(fs(u,fm(c,r)),fm(b,g)),V+'.reciprocal.u.'),
 (V+'.yProduct.', '.definition',fa(fs(fm(d,k),fm(b,J)),fc(fm(a,u),2)),V+'.reciprocal.k.'),
 (V+'.f.definition.', '',fs(fv,fm(g,g)),None),
 (V+'.z.definition.', '',fa(fm(k,z),g),None),
 (L+'.definition.', '',fs(fm(J,ll),fm(r,s)),None)]
 changed=[]
 for pre,post,expr,nn in expressions:
  for j in range(2):
   name=pre+str(j)+post;replace(name,expr[j],None if nn is None else nn+str(j));changed.append(rn[name])
 deleted=[rn[U+'.f.definition.'+str(j)] for j in range(2)]+[rn[V+'.completeTangent.'+str(j)] for j in range(2)]
 for j in deleted:del rows[j]
 removed=[cn[primary+'.chart.x.'+str(j)+'.quadratic'] for j in range(2)];remove.update(removed)
 for pre,n in [(primary+'.chart.h',primary+'.reciprocal.r'),(primary+'.chart.j',primary+'.reciprocal.J')]:
  for j in range(2):renames[cn[pre+str(j)]]=n+str(j)
 for pp,nn,suffix in [(V+'.slope.',V+'.reciprocal.g.',''),(V+'.slopeSquare.',V+'.reciprocal.u.','.quadratic'),(V+'.yProduct.',V+'.reciprocal.k.','.quadratic')]:
  for j in range(2):renames[cn[pp+str(j)+suffix]]=nn+str(j)
 ops.append({'primary':primary,'root':root,'U':U,'V':V,'L':L,'changedRows':changed,'deletedRows':deleted,'removedCoordinates':removed})
coords=[dict(c,name=renames.get(c['id'],c['name'])) for c in old['coordinates'] if c['id'] not in remove]
guard=max(c['id'] for c in old['coordinates'])+1
guardrow=max(r['id'] for r in old['residuals'])+1
coords.append({'id':guard,'name':'V0.reciprocal.f0Inverse','kind':'witness','protected':False,'block':'reciprocal_primary_domain'})
rows[guardrow]={'id':guardrow,'name':'V0.reciprocal.f0Inverse.definition','kind':'structural','block':'reciprocal_primary_domain','terms':encode(P.add(P.mon(cn['V0.f.0'],guard),P.mon(),-1))}
new=dict(old,coordinates=coords,residuals=list(rows.values()),status='Candidate pending identity-domain arithmetic review: reciprocal primary charts.')
def write(n,obj):(H/n).write_text(json.dumps(obj,indent=2)+'\n')
write('candidate428-ir.json',new);total={}
for row in new['residuals']:
 p=P.normalized(P.poly(row['terms']));total=P.add(total,P.mul(p,p))
write('polynomial428.json',{'fixedParameter':new['fixedParameter'],'terms':encode(total)})
cert={'source':str(S),'sourceSha256':P.sha(S),'semanticSource':str(SEM),'semanticSourceSha256':P.sha(SEM),'candidateSha256':P.sha(H/'candidate428-ir.json'),'polynomialSha256':P.sha(H/'polynomial428.json'),'operations':ops,'guardCoordinate':guard,'guardRow':guardrow,'counts':{'variables':len(coords),'witnesses':len(coords)-1,'residuals':len(rows),'monomials':len({tuple(x for x in m if x!=-1) for m in total}),'degree':max(sum(x!=-1 for x in m) for m in total)}}
write('certificate428.json',cert);print(json.dumps(cert['counts'],indent=2))
