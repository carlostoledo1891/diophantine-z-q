from pathlib import Path
exec((Path(__file__).parent/'build.py').read_text().split('s=json.loads(P.read_bytes())')[0])
x=json.loads((O/'candidate233-ir.json').read_bytes());data=json.loads((O/'MAPS.json').read_bytes())
rows=[read(r['terms']) for r in x['residuals']];inverse=[]
for i,f in enumerate(data['normalization_factors']):rows[i]={k:v/F(f) for k,v in rows[i].items()}
for t in reversed(data['stages']):
 if t['kind']=='row_add':rows[t['target']]=plus(rows[t['target']],rows[t['source']],-F(t['factor']))
 elif t['kind']=='row_sum_difference':
  i,j=t['first'],t['second'];p,q=rows[i],rows[j];rows[i]={k:v/2 for k,v in plus(p,q).items()};rows[j]={k:v/2 for k,v in plus(p,q,-1).items()}
 else:
  ss={int(i):read(ts) for i,ts in t['old_in_new'].items()};ids=sorted(ss);n=len(ids)
  a=[[ss[i].get((0,(j,)),F(0)) for j in ids]+[F(i==j) for j in ids] for i in ids]
  for k in range(n):
   j=next(j for j in range(k,n) if a[j][k]);a[k],a[j]=a[j],a[k];v=a[k][k];a[k]=[z/v for z in a[k]]
   for j in range(n):
    if j!=k:
     v=a[j][k];a[j]=[z-v*w for z,w in zip(a[j],a[k])]
  rhs={i:plus({(0,(i,)):F(1)},{k:v for k,v in ss[i].items() if not(k[0]==0 and len(k[1])==1 and k[1][0] in ids)},-1) for i in ids}
  inv={}
  for k,i in enumerate(ids):
   inv[i]={}
   for j,l in enumerate(ids):inv[i]=plus(inv[i],rhs[l],a[k][n+j])
  for i in ids:
   assert sub(ss[i],inv)=={(0,(i,)):F(1)}
   assert sub(inv[i],ss)=={(0,(i,)):F(1)}
  rows=[sub(p,inv) for p in rows];inverse.append({'label':t['label'],'new_in_old':{str(i):ser(p) for i,p in inv.items()}})
assert rows==[read(r['terms']) for r in json.loads(P.read_bytes())['residuals']]
poly={}
for r in x['residuals']:
 ts=list(read(r['terms']).items())
 for i,((a,m),v) in enumerate(ts):
  for j in range(i,len(ts)):
   (b,n),w=ts[j];add(poly,(a+b,tuple(sorted(m+n))),v*w*(1 if i==j else 2))
assert poly==read(json.loads((O/'candidate233-polynomial.json').read_bytes())['terms'])
assert poly[(0,(4,4,4,4))]==1
cmax=max(abs(v) for (a,m),v in poly.items() if a==0);lmax=max(abs(v) for (a,m),v in poly.items() if a==1)
assert 149**214+1>cmax
assert all(a<=2 for a,m in poly)
(O/'INVERSE-MAPS.json').write_text(json.dumps(inverse,indent=2)+'\n')
profiles={}
for (a,m),v in poly.items():profiles.setdefault(m,{})[a]=v
A0=149**107
for m,pr in profiles.items():
 if 2 in pr:assert pr=={0:F(1),2:F(1)}
 else:assert abs(pr.get(0,0))+A0*abs(pr.get(1,0))<=A0*A0+1 and abs(pr.get(1,0))<=2*A0
report={'reverse_all_207_rows_exact':True,'all_affine_maps_two_sided':True,'independent_unordered_pair_expansion_exact':True,'unit_coefficient':'x4^4','constant_max':str(cmax),'linear_parameter_max':str(lmax),'coefficient_threshold_scope':'N>=53 is a coefficient bound only; no effective defining threshold claimed','inverse_coordinate_stages':len(inverse)}
(O/'VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='constant_max'}))



