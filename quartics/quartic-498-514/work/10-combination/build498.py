from package_paths import reference_repo
"""Replay exact norm-coordinate elimination on frozen499, then expand SOS."""
from pathlib import Path
import json,hashlib,importlib.util
from build import pol,terms,norm
H=Path(__file__).resolve().parent;R=reference_repo()
spec=importlib.util.spec_from_file_location('poly',R/'quartics/quartic-523-540/final523_540/verify_elimination.py');V=importlib.util.module_from_spec(spec);spec.loader.exec_module(V)
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
src=H/'candidate499-ir.json';cp=H.parent/'01-elimination/sub500/from501/elimination500-certificate.json';base=H/'candidate501-ir.json'
d=read(src);cert=read(cp);assert cert['baselineSha256']==sha(base)
rows={r['id']:pol(r['terms']) for r in d['residuals']};original={r['id']:pol(r['terms']) for r in read(base)['residuals']};removed=[];deleted=[]
for op in cert['operations']:
 x=op['coordinate'];pivot=op['pivot'];q=pol(op['replacement'])
 assert rows[pivot]==original[pivot] and V.subst(rows[pivot],x,q)=={}
 affected={i for i,r in rows.items() if x in V.variables(r)}
 assert affected=={pivot}|{z['row'] for z in op['changes']}
 for z in op['changes']:
  ri=z['row'];assert rows[ri]==original[ri];expect=V.subst(rows[ri],x,q)
  for mm in z['multiples']:
   j=mm['row'];assert j not in affected and rows[j]==original[j]
   expect=V.add(expect,V.mul(pol(mm['factor']),rows[j]))
  assert expect==pol(z['result']) and V.degree(expect)<=2
  rows[ri]=expect
 del rows[pivot];removed.append(x);deleted.append(pivot)
d['coordinates']=[c for c in d['coordinates'] if c['id'] not in removed]
d['residuals']=[dict(r,terms=terms(rows[r['id']])) for r in d['residuals'] if r['id'] not in deleted]
total={}
for p in rows.values():total=V.add(total,V.mul(norm(p),norm(p)))
assert len(d['coordinates'])==498 and len(rows)==467 and len(total)==24669
assert V.degree(total)==4 and V.variables(total)=={c['id'] for c in d['coordinates']}
def write(n,o):(H/n).write_text(json.dumps(o,indent=2)+'\n', encoding='utf-8', newline='\r\n')
write('candidate498-ir.json',d);write('polynomial498.json',{'fixedParameter':d['fixedParameter'],'terms':terms(total)})
stats={'variables':498,'witnesses':497,'residuals':467,'degree':4,'monomials':len(total),'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidateSha256':sha(H/'candidate498-ir.json'),'polynomialSha256':sha(H/'polynomial498.json')}
write('certificate498.json',{'source499Sha256':sha(src),'source501Sha256':sha(base),'sourceCertificateSha256':sha(cp),'operations':cert['operations'],'statistics':stats})
print(json.dumps(stats,indent=2))
