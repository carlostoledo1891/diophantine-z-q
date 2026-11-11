from package_paths import reference_repo
"""Read-only replay of certificates and sum of squares; no producer imports."""
from pathlib import Path
import json,hashlib,importlib.util,subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'03-depth'
REPO=reference_repo()
SRC=REPO/'quartics/quartic-523-540/source-reproduction'
def load(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
V=load('V',REPO/'quartics/quartic-523-540/final523_540/verify_elimination.py')
A=load('A',REPO/'quartics/quartic-523-540/final523_540/verify_all.py')
def read(p):return json.loads(p.read_text())
d=ROOT/'beta12';f=d/'final'
assert (ROOT/'checker.cjs').read_text()==(SRC/'tools/checker.cjs').read_text().replace('3^(2^27)','3^(2^26)')
assert (ROOT/'compile_ir.py').read_text()==(SRC/'tools/compile_ir.py').read_text().replace('3^(2^27)','3^(2^26)')
subprocess.run(['node',str(ROOT/'checker.cjs'),'--input',str(d/'raw-translated-ir.json'),'--compiled',str(d/'compiled/compiled-ir.json'),'--certificate',str(d/'compiled/reduction-certificate.json'),'--coordinate-map',str(d/'compiled/coordinate-map.json'),'--quartic',str(d/'compiled/polynomial.json'),'--report',str(HERE/'depth-independent-check.json')],check=True,stdout=(HERE/'depth-checker.log').open('w'))
source=read(d/'compiled/compiled-ir.json');cert=read(f/'modulo-certificate.json')
assert hashlib.sha256((d/'compiled/compiled-ir.json').read_bytes()).hexdigest()==cert['baselineSha256']
rows={r['id']:V.readpoly(r['terms']) for r in source['residuals']};coords={c['id']:c for c in source['coordinates']}
for op in cert['operations']:
 if op.get('kind')=='shear':
  free=op['free'];assert free in coords
  for sh in op['shears']:
   x=sh['coordinate'];assert x in coords and x!=free and x!=0 and not coords[x].get('protected')
   q={(0,(x,)):V.Q(1),(0,(free,)):V.Q(sh['factor'])}
   rows={r:V.subst(p,x,q) for r,p in rows.items()}
  assert all(V.degree(p)<=2 for p in rows.values())
  continue
 x=op['coordinate'];pivot=op['pivot'];p=rows[pivot];q=V.readpoly(op['replacement'])
 assert x!=0 and not coords[x].get('protected') and x not in V.variables(q)
 assert p.get((0,(x,))) and V.subst(p,x,q)=={}
 assert all(x not in m or (s,m)==(0,(x,)) for s,m in p)
 affected={r for r,p in rows.items() if x in V.variables(p)}
 assert {z['row'] for z in op['changes']}==affected-{pivot}
 assert len(op['changes'])==len(affected)-1
 changes={}
 for z in op['changes']:
  r=z['row'];expected=V.subst(rows[r],x,q)
  for mm in z['multiples']:
   rr=mm['row'];factor=V.readpoly(mm['factor'])
   assert rr not in affected and x not in V.variables(factor)
   expected=V.add(expected,V.mul(factor,rows[rr]))
  actual=V.readpoly(z['result'])
  assert actual==expected and V.degree(actual)<=2 and x not in V.variables(actual)
  changes[r]=actual
 rows.update(changes);del rows[pivot];del coords[x]
candidate=read(f/'candidate-ir.json')
assert {r['id']:V.readpoly(r['terms']) for r in candidate['residuals']}==rows
assert {c['id']:c for c in candidate['coordinates']}==coords
assert len(coords)==519 and candidate['fixedParameter']['value']=='3^(2^26)'
A.check_compile_relation(f,f/'candidate-ir.json')
stats=A.check_table(f)
assert stats['coordinates']==519 and stats['degree']==4 and stats['monomials']==24986
result={'sourceCheck':read(HERE/'depth-independent-check.json'),'finalAlgebra':stats,'certificateOperations':len(cert['operations']),'constant':'3^(2^26)','arithmeticStatus':'Internal derivation in REPORT.md, not independent arithmetic acceptance.'}
(HERE/'depth-VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(stats,indent=2))

