import json,re,hashlib,sys
from pathlib import Path
from fractions import Fraction
src=Path(sys.argv[1]); out=Path(sys.argv[2]); ir=Path(sys.argv[3])
s=src.read_text(encoding='utf-8'); target=json.loads(ir.read_bytes())
start=s.index('\\section{The explicit 222-variable quartic}')
end=s.index('\\subsection{Completion and coefficient profile}',start)
block=s[start:end]

# Read arithmetic definitions from the TeX itself, not the author sidecar.
constants={}
for kid,expr in re.findall(r'\\kappa_\{(\d+)\}=\{\}&(.*?)\\end\{align\*\}',block,re.S):
 expr=re.sub(r'\s+','',expr.replace('\\\\','').replace('&',''))
 total=0
 for summand in expr.split('+'):
  m=re.fullmatch(r'(\d+)(?:\\cdot10\^\{(\d+)\})?',summand)
  assert m,('unknown coefficient notation',kid,summand)
  total+=int(m[1])*10**int(m[2] or 0)
 assert kid not in constants
 constants[kid]=total
assert set(constants)==set(map(str,range(1,9))),constants.keys()
block=re.sub(r'\\kappa_\{(\d+)\}',lambda m:str(constants[m[1]]),block)
found=re.findall(r'Q_\{(\d+),N\}=\{\}&(.*?)\\end\{aligned\}',block,re.S)
assert len(found)==196,len(found)
result=[]
for idx,body in found:
 body=body.replace('\\\\','').replace('&','');body=re.sub(r'\s+','',body)
 parts=re.findall(r'[+-]?[^+-]+',body)
 p={}
 for term in parts:
  sign=-1 if term.startswith('-') else 1;term=term.lstrip('+-')
  mat=re.match(r'\d+',term); c=int(mat[0]) if mat else 1
  if mat:term=term[len(mat[0]):]
  power=0;mon=[]
  while term:
   if term.startswith('A_N'):power+=1;term=term[3:];continue
   mat=re.match(r'z_\{(\d+)\}(?:\^\{(\d+)\})?',term)
   assert mat,(idx,term)
   mon.extend([int(mat[1])]*int(mat[2] or 1));term=term[len(mat[0]):]
  key=(power,tuple(sorted(mon)));p[key]=p.get(key,0)+sign*c
 p={k:v for k,v in p.items() if v}
 row=target['residuals'][int(idx)-1]
 expected={(t['parameterPower'],tuple(t['monomial'])):Fraction(t['coefficient']) for t in row['terms']}
 assert p==expected,dict(row=idx,missing=str(set(expected.items())-set(p.items())),extra=str(set(p.items())-set(expected.items())))
 result.append(int(idx))
assert result==list(range(1,197))
report={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'ir_sha256':hashlib.sha256(ir.read_bytes()).hexdigest(),'matched_rows':result,'tex_integer_abbreviations':{k:str(v) for k,v in constants.items()},'unknown_notation':False,'scope':'Exact printed196 RHS parsing only; tags, proof text, weights and PDF rendering are separate.'}
out.write_text(json.dumps(report,indent=2)+chr(10))
print(json.dumps({k:v for k,v in report.items() if k!='matched_rows'}))
