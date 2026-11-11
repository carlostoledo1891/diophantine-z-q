import json,re,sys,hashlib
from pathlib import Path
from fractions import Fraction as F
src=Path(sys.argv[1]);maps=Path(sys.argv[2]);out=Path(sys.argv[3]);s=src.read_text(encoding='utf8')
s=s[s.index('\\subsection{Exact final affine and row presentation}'):s.index('\\section{The explicit 222-variable quartic}')]
def rational(x):
 x=re.sub(r'\\frac\{(\d+)\}\{(\d+)\}',r'\1/\2',x)
 return F(re.sub(r'\s+','',x))
def polynomial(x):
 x=x.replace('\\\\','').replace('\\rm new','NEW')
 x=re.sub(r'x_\{(\d+)\}\^\{NEW\}',r'z{\1}',x)
 x=re.sub(r'\\frac\{(\d+)\}\{(\d+)\}',r'\1/\2',x)
 x=re.sub(r'\s+','',x);p={}
 for t in re.findall(r'[+-]?[^+-]+',x):
  m=re.fullmatch(r'([+-]?(?:\d+(?:/\d+)?)?)(z\{(\d+)\})?',t);assert m,t
  c=F(m[1]+'1' if m[1] in ('','+','-') else m[1]); key=() if m[3] is None else (int(m[3]),)
  p[key]=p.get(key,F(0))+c
 return {k:c for k,c in p.items() if c}
expected=json.loads(maps.read_bytes())['stages'];actual=[]
chunks=re.split(r'\\paragraph\{Affine stage \d+\.\}',s)[1:]
assert len(chunks)==8
for ch in chunks:
 block=re.search(r'\\begin\{align\*\}(.*?)\\end\{align\*\}',ch,re.S);assert block
 eqs={}
 for m in re.finditer(r'x_\{(\d+)\}\^\{\\rm old\}&=(.*?)(?=\\\\|$)',block[1],re.S):eqs[int(m[1])]=polynomial(m[2])
 actual.append(('coordinates',eqs))
 for m in re.finditer(r'Replace residual (\d+) by itself plus \$(.*?)\$ times residual (\d+)\.|Replace residuals (\d+),(\d+) by their sum and difference',ch):
  if m[1]:actual.append(('row_add',int(m[1])-1,int(m[3])-1,rational(m[2])))
  else:actual.append(('row_pair',int(m[4])-1,int(m[5])-1))
assert len(actual)==len(expected),(len(actual),len(expected))
for a,e in zip(actual,expected):
 if e['kind']=='coordinates':
  ee={int(i):{tuple(t['monomial']):F(t['coefficient']) for t in ts} for i,ts in e['old_in_new'].items()}
  ee={i:p for i,p in ee.items() if p!={(i,):F(1)}}
  assert a==('coordinates',ee),(a,ee)
 elif e['kind']=='row_add':assert a==('row_add',e['target'],e['source'],F(e['factor'])),(a,e)
 else:assert a==('row_pair',e['first'],e['second']),(a,e)
report={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'maps_sha256':hashlib.sha256(maps.read_bytes()).hexdigest(),'all_ordered_stages_match':True,'stage_count':len(expected),'coordinate_stages':8}
out.write_text(json.dumps(report,indent=2)+chr(10));print(json.dumps(report))
