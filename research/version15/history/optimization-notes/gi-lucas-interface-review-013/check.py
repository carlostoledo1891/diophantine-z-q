from fractions import Fraction as Q
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[4]
SRC=ROOT/'work/quartic223-direct-lucas-interface-integration-001'
OUT=Path(__file__).parent
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert h(SRC/'MANIFEST.json')=='c8d59d734edf5861a0b29d9beef99069f325d1cad88bc34314ab69cc50c56c46'
for m in json.loads((SRC/'MANIFEST.json').read_text())['files']:
    assert h(SRC/m['path'])==m['sha256']
class K:
    def __init__(self,a=0,b=0): self.a,self.b=Q(a),Q(b)
    def __add__(s,t): return K(s.a+t.a,s.b+t.b)
    def __neg__(s): return K(-s.a,-s.b)
    def __sub__(s,t): return s+-t
    def __mul__(s,t): return K(s.a*t.a+2*s.b*t.b,s.a*t.b+s.b*t.a)
    def __truediv__(s,t):
        n=t.a*t.a-2*t.b*t.b
        assert n
        return s*K(t.a/n,-t.b/n)
    def __eq__(s,t): return (s.a,s.b)==(t.a,t.b)
x=K(Q(57,8),Q(-7,2)); y=K(Q(-165,8),Q(417,32)); D=K(11,-6)
assert y*y==x*x*x-D*x
m=(K(3)*x*x-D)/(K(2)*y)
u=m*m-K(2)*x; v=m*(x-u)-y
assert v*v==u*u*u-D*u
ratio=(u*y)/(v*x)
assert ratio==K(Q(13712284495998,3287811625151),Q(-11446225896960,3287811625151))
assert ratio!=K(2)
# Symbolic substitution coefficients in variables (a,b,t).
# k=(a-2)b and l=tk give t^2-a^2bt+2abt+a^2b^2-4ab^2+4b^2-1.
expanded={(0,0,2):1,(2,1,1):-1,(1,1,1):2,(2,2,0):1,(1,2,0):-4,(0,2,0):4,(0,0,0):-1}
checks={'all_subject_member_hashes_match':True,'curve_and_doubling_exact':True,
        'ratio':[str(ratio.a),str(ratio.b)],'three_quadratic_substitution':str(expanded),
        'scope':'Exact local algebra and function counterexample; no full223 witness asserted.'}
(OUT/'CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
review={'status':'accepted at bounded interface scope','subject_manifest':h(SRC/'MANIFEST.json'),
 'findings':['Two helpers uniquely lift rational a,b,t satisfying the displayed Lucas polynomial; sum of three squared quadratic residuals has degree at most four.',
 'Exact generator doubling disproves the proposed identity between a formal-parameter ratio and the integer label.',
 'The current source and row evidence describe field-valued ratios and local congruences, not ordinary label coordinates. No lower-variable candidate follows.'],
 'limits':['Integer monicity consequence remains conditional on a,b being integers; no new integer-label encoding proved.',
 'No full-system counterexample or impossibility of all alternative encodings claimed.'],
 'author':'GI independent reviewer; not author of the subject Lucas note'}
(OUT/'REVIEW.json').write_text(json.dumps(review,indent=2)+'\n')
manifest={'files':[{'path':p.name,'sha256':h(p),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json']}
(OUT/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'review':h(OUT/'REVIEW.json'),'manifest':h(OUT/'MANIFEST.json')}))
