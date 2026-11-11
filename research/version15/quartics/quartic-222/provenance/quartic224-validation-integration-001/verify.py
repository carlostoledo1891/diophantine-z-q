"""Exact sparse-Q[A,x] checks. No numerical or authenticated-proof claims."""
import json,hashlib,argparse
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def clean(p):return {k:v for k,v in p.items() if v}
def add(*ps):
 r=defaultdict(F)
 for p in ps:
  for k,v in p.items():r[k]+=v
 return clean(r)
def scale(p,c):return clean({k:v*F(c) for k,v in p.items()})
def mul(p,q):
 r=defaultdict(F)
 for (a,m),v in p.items():
  for (b,n),w in q.items():r[a+b,tuple(sorted(m+n))]+=v*w
 return clean(r)
def terms(ts):
 r=defaultdict(F)
 for t in ts:
  a=t['parameterPower'];m=t['monomial']
  assert isinstance(a,int) and a>=0
  assert all(isinstance(i,int) and i>0 for i in m)
  r[a,tuple(sorted(m))]+=F(t['coefficient'])
 return clean(r)
def variable(i):return {(0,(i,)):F(1)}
def subst(p,maps):
 r={}
 for (a,m),v in p.items():
  t={(a,()):v}
  for i in m:t=mul(t,maps[i])
  r=add(r,t)
 return r
def ircheck(ir):
 n=ir['variables'];assert ir['inputCoordinate']==1
 assert [c['id'] for c in ir['coordinates']]==list(range(1,n+1))
 assert len({c['name'] for c in ir['coordinates']})==n
 assert ir['fixedParameter']['coordinate'] is False
 assert ir['fixedParameter']['base']==149 and ir['fixedParameter']['exponent']=='2*N+1'
 ids=[r['id'] for r in ir['residuals']];assert len(set(ids))==len(ids)
 ps=[terms(r['terms']) for r in ir['residuals']]
 assert all(len(m)<=2 and all(i<=n for i in m) for p in ps for a,m in p)
 consumers={str(i):[r['id'] for r,p in zip(ir['residuals'],ps) if any(i in m for a,m in p)] for i in range(1,n+1)}
 return ps,consumers

def identity(lhs,basis,certificate):
 rhs={}
 for row in certificate:rhs=add(rhs,mul(terms(row['multiplier']),basis[row['residual_index']]))
 assert lhs==rhs,'polynomial identity failed'

def check(parent,child,poly,cert=None):
 pp,pc=ircheck(parent);cp,cc=ircheck(child)
 assert parent['fixedParameter']==child['fixedParameter'],'parameter/domain changed'
 assert poly['variables']==child['variables'] and poly['inputCoordinate']==1
 assert poly['fixedParameter']==child['fixedParameter']
 weights=poly.get('positiveRowWeights',['1']*len(cp));assert len(weights)==len(cp)
 assert all(F(w)>0 for w in weights),'nonpositive weight'
 sos=add(*(scale(mul(p,p),w) for p,w in zip(cp,weights)))
 assert sos==terms(poly['terms']),'full SOS mismatch'
 assert max(map(lambda k:len(k[1]),sos),default=0)==4
 result={'full_sos_equal':True,'variables':child['variables'],'residuals':len(cp),'formal_terms':len(sos),'coordinate_monomials':len({m for a,m in sos}),'consumers':cc,'map_certificate_checked':False}
 if cert is not None:
  # Each map is total: source coordinate -> polynomial in destination coordinates.
  forward={int(k):terms(v) for k,v in cert['parent_in_child'].items()}
  inverse={int(k):terms(v) for k,v in cert['child_in_parent'].items()}
  assert set(forward)==set(range(1,parent['variables']+1))
  assert set(inverse)==set(range(1,child['variables']+1))
  assert forward[1]==inverse[1]==variable(1),'input changed'
  assert all(i<=child['variables'] for p in forward.values() for a,m in p for i in m)
  assert all(i<=parent['variables'] for p in inverse.values() for a,m in p for i in m)
  assert len(cert['parent_residuals_from_child'])==len(pp)
  assert len(cert['child_residuals_from_parent'])==len(cp)
  for p,c in zip(pp,cert['parent_residuals_from_child']):identity(subst(p,forward),cp,c)
  for p,c in zip(cp,cert['child_residuals_from_parent']):identity(subst(p,inverse),pp,c)
  assert len(cert['parent_roundtrip'])==parent['variables']
  assert len(cert['child_roundtrip'])==child['variables']
  for i,c in enumerate(cert['parent_roundtrip'],1):identity(add(subst(forward[i],inverse),scale(variable(i),-1)),pp,c)
  for i,c in enumerate(cert['child_roundtrip'],1):identity(add(subst(inverse[i],forward),scale(variable(i),-1)),cp,c)
  result['map_certificate_checked']=True
 return result

def main():
 ap=argparse.ArgumentParser();ap.add_argument('request');ap.add_argument('output');args=ap.parse_args()
 req=json.loads(Path(args.request).read_bytes());data={}
 for key in ['parent','child','polynomial']+(['certificate'] if 'certificate' in req else []):
  pin=req[key];assert digest(pin['path'])==pin['sha256'],key+' pin mismatch';data[key]=json.loads(Path(pin['path']).read_bytes())
 result=check(data['parent'],data['child'],data['polynomial'],data.get('certificate'))
 result.update(input_pins=req,scope='Exact local finite identities only; rational maps require separate domain proof; no source theorem or threshold re-audit.')
 Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
