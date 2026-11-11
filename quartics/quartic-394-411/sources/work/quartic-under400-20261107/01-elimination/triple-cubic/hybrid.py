"""Alternate detector evaluation by products of small shared polynomials."""
from search import *
import copy,itertools
REPO=OUT.parents[2]/'quartic-version6-release/repository'
DEPTH=REPO/'quartics/quartic-498-514/work/03-depth/beta12/final/candidate-ir.json'
depth=json.loads(DEPTH.read_text())
ONE={(0,()):F(1)};ZERO={}
def scale(p,a):return {k:v*a for k,v in p.items() if v*a}
def val(name):
 name=name.replace('testSquare.10.','testSquare.12.').replace('.E10.','.E12.')
 return C.polynomial(depth['values'][name]['terms'])
def fv(name):return val(name+'.0'),val(name+'.1')
def fa(a,b):return C.add(a[0],b[0]),C.add(a[1],b[1])
def fm(a,b):return C.add(C.multiply(a[0],b[0]),C.multiply(a[1],b[1]),F(2)),C.add(C.multiply(a[0],b[1]),C.multiply(a[1],b[0]))
def parts(n,lo=1,maxpart=5):
 if not n:yield ()
 for k in range(lo,min(n,maxpart)+1):
  for tail in parts(n-k,k,maxpart):yield (k,)+tail

def build(partitions):
 base=copy.deepcopy(data)
 coords={x['id']:x for x in base['coordinates']};rows={r['name']:r for r in base['residuals']}
 byname={x['name']:x['id'] for x in coords.values()}
 keepcoords=set();keeprows=set();powers={}
 for detector in range(3):
  for order in [1,10,40]:
   pre=f'detector{detector}.E{order}.'
   cap=max(partitions[order]);required=set(range(2,cap+1))
   if order==1:required|={2,3,5}
   if order==10:required|={2}
   powers[detector,order]=[ONE,{(0,(byname[f'detector{detector}.q'+('1' if order==1 else str(order))],)):F(1)}]
   for k in sorted(required):
    cname=pre+f'power{k}.quadratic';rname=pre+f'power{k}.definition'
    if cname in byname:
     keepcoords.add(byname[cname]);keeprows.add(rname)
     if k==len(powers[detector,order]):powers[detector,order].append({(0,(byname[cname],)):F(1)})
     else:assert k>len(powers[detector,order]) and k>cap
  for j in range(2):keepcoords.add(byname[f'detector{detector}.W.{j}.quadratic'])
 prefixes=['symmetric.']+[f'detector{i}.{name}.' for i in range(3) for name in ['E1','E10','E40','Wfirst','W']]
 dropcoords={i for i,x in coords.items() if any(x['name'].startswith(p) for p in prefixes)}-keepcoords
 droprows={name for name in rows if any(name.startswith(p) for p in prefixes)}-keeprows
 rows={name:r for name,r in rows.items() if name not in droprows};coords={i:x for i,x in coords.items() if i not in dropcoords}
 # Normalize the compiler's affine W coordinates to the actual field outputs.
 # The old semantic W values include lower eval coordinates. Recenter the
 # two W coordinates before deleting those private coordinates.
 outputids={}
 for detector in range(3):
  for j in range(2):
   x=byname[f'detector{detector}.W.{j}.quadratic'];outputids[detector,j]=x
   semantic=val(f'detector{detector}.W.{j}');a=semantic[(0,(x,))]
   rest=C.add(semantic,{(0,(x,)):-a})
   assert C.degree(semantic)<=1 and all(byname[f'detector{detector}.W.{k}.quadratic'] not in C.variables(rest) for k in range(2))
   replacement=scale(C.add({(0,(x,)):F(1)},rest,F(-1)),1/a)
   for r in rows.values():r['terms']=C.terms(C.substitute(C.polynomial(r['terms']),x,replacement))
   coords[x]['name']=f'detector{detector}.actualW.{j}'
 assert not any(C.variables(C.polynomial(r['terms']))&dropcoords for r in rows.values())
 nextid=max(x['id'] for x in base['coordinates'])+1;nextrow=max(x['id'] for x in base['residuals'])+1
 def row(name,p):
  nonlocal nextrow
  assert C.degree(p)<=2
  rows[name]={'id':nextrow,'name':name,'kind':'gate','block':'hybrid_detector','terms':C.terms(p)};nextrow+=1
 def assign(name,p):
  nonlocal nextid
  assert C.degree(p)<=2
  if C.degree(p)<=1:return p
  x=nextid;nextid+=1;coords[x]={'id':x,'name':name,'kind':'gate','block':'hybrid_detector','protected':False}
  q={(0,(x,)):F(1)};row(name+'.definition',C.add(q,p,F(-1)));return q
 def fassign(name,p):return tuple(assign(name+f'.{j}',p[j]) for j in range(2))
 def fmul(name,a,b):return fassign(name,fm(a,b))
 def polyprod(name,ys):
  if len(ys)==1:return [(ONE,ZERO),ys[0]]
  cut=len(ys)//2;aa=polyprod(name+'.left',ys[:cut]);bb=polyprod(name+'.right',ys[cut:]);out=[]
  for k in range(len(aa)+len(bb)-1):
   z=(ZERO,ZERO)
   for i in range(max(0,k-len(bb)+1),min(k,len(aa)-1)+1):z=fa(z,fm(aa[i],bb[k-i]))
   out.append(fassign(name+f'.co{k}',z))
  return out
 groups={}
 for order in [1,10,40]:
  offset=0;groups[order]=[]
  for g,n in enumerate(partitions[order]):
   permutation=[4,0,1,5,2,3,6,7,8] if order==1 else list(range(sum(partitions[order])))
   leaves=[fv(f'testSquare.{order}.{permutation[i]}') for i in range(offset,offset+n)];offset+=n
   assert not any((C.variables(p)&dropcoords) for f in leaves for p in f)
   groups[order].append(polyprod(f'hybrid.{order}.group{g}',leaves))
 for det in range(3):
  outputs=[]
  for order in [1,10,40]:
   groupoutputs=[]
   cap=max(partitions[order]);pw=powers[det,order]
   while len(pw)<=cap:
    k=len(pw);pw.append(assign(f'hybrid.det{det}.power{order}.{k}',C.multiply(pw[k//2],pw[k-k//2])))
   for g,co in enumerate(groups[order]):
    v=(ZERO,ZERO)
    for k,ck in enumerate(co):v=fa(v,(C.multiply(ck[0],pw[k]),C.multiply(ck[1],pw[k])))
    groupoutputs.append(fassign(f'hybrid.det{det}.eval{order}.{g}',v))
   product=groupoutputs[0]
   for g,nextgroup in enumerate(groupoutputs[1:],1):product=fmul(f'hybrid.det{det}.order{order}.product{g}',product,nextgroup)
   outputs.append(product)
  serial=0
  while len(outputs)>2:
   fresh=[]
   for j in range(0,len(outputs),2):
    if j+1==len(outputs):fresh.append(outputs[j])
    else:
     fresh.append(fmul(f'hybrid.det{det}.product{serial}',outputs[j],outputs[j+1]));serial+=1
   outputs=fresh
  final=fm(*outputs) if len(outputs)==2 else outputs[0]
  for j in range(2):row(f'hybrid.det{det}.W.{j}',C.add({(0,(outputids[det,j],)):F(1)},final[j],F(-1)))
 base['coordinates']=list(coords.values());base['residuals']=list(rows.values())
 base['format']='hybrid-shared-detector-polynomials-v1'
 base['hybridPartitions']={str(k):list(v) for k,v in partitions.items()}
 active=set().union(*(C.variables(C.polynomial(r['terms'])) for r in rows.values()))
 assert active==set(coords),(set(coords)-active,active-set(coords))
 return base,{'partitions':partitions,'coordinates':len(coords),'residuals':len(rows),'removedCoordinates':sorted(dropcoords),'removedRows':sorted(droprows)}

if __name__=='__main__':
 results=[];best=None
 for a in parts(9):
  for b in parts(2):
   for cpart in parts(5):
    output,stats=build({1:a,10:b,40:cpart});results.append(stats)
    if best is None or stats['coordinates']<best[1]['coordinates']:
     best=output,stats;print('BEST',stats['coordinates'],a,b,cpart,flush=True)
 output,stats=best
 (OUT/'hybrid-search.json').write_text(json.dumps(results,indent=2)+'\n')
 (OUT/'hybrid-best-ir.json').write_text(json.dumps(output,indent=2)+'\n')
 (OUT/'hybrid-best-summary.json').write_text(json.dumps(stats,indent=2)+'\n')
 print(json.dumps(stats,indent=2))

