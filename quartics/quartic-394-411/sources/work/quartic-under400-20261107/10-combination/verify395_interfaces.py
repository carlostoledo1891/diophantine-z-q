"""Read-only final scalar normalization and alternate-domain comparison."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def rows(d):return {r['name']:r for r in d['residuals']}
def p(r):
    out={}
    for t in r['terms']:
        key=tuple([-1]*t.get('sPower',0)+t['monomial']);out[key]=out.get(key,0)+F(t['coefficient'])
    return {m:v for m,v in out.items() if v}
def canon(q):return {m:v/q[min(q)] for m,v in q.items()}
weights={51:1,52:1,53:1,54:1,532:1,527:2,534:2}
def subst(q):
    out={}
    for mon,v in q.items():
        xpower=sum(weights.get(i,0) for i in mon)+2*mon.count(531)
        key=tuple(sorted(tuple(i for i in mon if i!=531)+(526,)*xpower))
        out[key]=out.get(key,0)+v
    return {m:v for m,v in out.items() if v}
before=read('combined396-ir.json');final=read('combined395-ir.json');alt=read('combined397-ir.json')
b,f,z=map(rows,[before,final,alt])
deleted=set(b)-set(f);assert len(deleted)==1
dn=next(iter(deleted));assert not subst(p(b[dn]))
private=set(weights)|{531}
affected={n for n,r in b.items() if any(private.intersection(t['monomial']) for t in r['terms'])}
assert len(affected)==6
for n,r in b.items():
    if n==dn:continue
    if n in affected:
        old=subst(p(r));new={tuple(sorted(m+(526,526))):v for m,v in p(f[n]).items()}
        assert canon(old)==canon(new),n
    else:assert r==f[n],n
assert not any(531 in t['monomial'] for r in f.values() for t in r['terms'])
# The variant without H-domain enlargement retains exactly two private square rows.
assert set(z)-set(f)=={'H.chart.x.0.definition','H.chart.x.1.definition'}
assert all(z[n]==r for n,r in f.items())
fc={c['id']:c for c in final['coordinates']};zc={c['id']:c for c in alt['coordinates']}
assert set(zc)-set(fc)=={17,18} and all(zc[i]==c for i,c in fc.items())
assert len(fc)==395 and len(f)==365
print(json.dumps({'passed':True,'candidateSha256':hashlib.sha256((H/'combined395-ir.json').read_bytes()).hexdigest(),'weightedPrivateCoordinates':weights,'deletedCoordinate':531,'allPoleSubstitutionRows':sorted(affected),'alternate397DiffersOnlyByHDomain':True},indent=2))
