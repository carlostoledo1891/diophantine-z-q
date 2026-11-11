import json,re,sys,hashlib
from pathlib import Path
from fractions import Fraction as F
src=Path(sys.argv[1]);out=Path(sys.argv[2]);root=Path(sys.argv[3]);s=src.read_text(encoding='utf8')
s=s[s.index('\\subsection{Polynomial reference elimination}'):s.index('\\subsection{Paired factors and three root normalizations}')]
rels=json.loads((root/'FIELD-RELATIONS.json').read_bytes())[0]
cert=json.loads((root/'CONVERSE-RESULT.json').read_bytes())
var={v:i for i,v in enumerate(rels['variables'])}
def coeff(x):
 x=re.sub(r'\\frac\{([+-]?\d+)\}\{(\d+)\}',r'\1/\2',x)
 x=re.sub(r'\s+','',x).replace('\\rho','')
 pieces=re.findall(r'[+-]?\d+(?:/\d+)?',x)
 assert ''.join(pieces)==x and len(pieces)==2,(x,pieces)
 return tuple(F(z) for z in pieces)
def mono(x):
 x=re.sub(r'\s+','',x)
 x=x.replace('\\\\','').replace('&','').strip('+.')
 result=[]
 while x:
  m=re.match(r'([fSgBwWT])(?:\^\{(\d+)\})?',x);assert m,x
  result.extend([var[m[1]]]*int(m[2] or 1));x=x[len(m[0]):]
 return tuple(sorted(result))
def terms(body,certificate=False):
 matches=list(re.finditer(r'\\left\((.*?)\\right\)',body,re.S));res=[]
 for i,m in enumerate(matches):
  tail=body[m.end():matches[i+1].start() if i+1<len(matches) else len(body)]
  if certificate:
   q=re.search(r'Q_(\d)',tail);assert q,tail
   mult=tail[:q.start()];rest=tail[q.end():]
   assert not rest.replace('\\\\','').replace('&','').strip(' +.\n\r\t'),rest
   res.append((int(q[1]),mono(mult),coeff(m[1])))
  else:res.append((mono(tail),coeff(m[1])))
 return res
for i in range(6):
 m=re.search(r'Q_'+str(i)+r'&=(.*?)\\end\{align\*\}',s,re.S);assert m,i
 actual=terms(m[1]);expected=[(tuple(t['monomial']),tuple(F(c) for c in t['coefficient'])) for t in rels['relations'][i]]
 assert actual==expected,(i,actual,expected)
for name in ['F','E']:
 m=re.search(r'\\mathcal '+name+r'&=(.*?)\\end\{align\*\}',s,re.S);assert m,name
 actual=terms(m[1],True);expected=[(t['relation'],tuple(t['multiplier']),tuple(F(c) for c in t['coefficient'])) for t in next(c for c in cert['checks'] if c['name']==name)['certificate']]
 assert actual==expected,(name,actual,expected)
report={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'six_field_quadrics_match':True,'F_E_recovery_certificates_match':True,'source_field_relations_sha256':hashlib.sha256((root/'FIELD-RELATIONS.json').read_bytes()).hexdigest(),'scope':'Printed coefficient correspondence to independently accepted224 certificate; not fresh self-approval of original authored identities.'}
out.write_text(json.dumps(report,indent=2)+chr(10));print(json.dumps(report))
