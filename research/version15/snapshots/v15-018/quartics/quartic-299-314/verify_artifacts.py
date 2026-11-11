"""Check exact compact bijections, full quartics and both text conventions."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json,re
H=Path(__file__).resolve().parent
def load(p):return json.loads(p.read_bytes())
def poly(row):
    p={(t['sPower'],tuple(t['monomial'])):F(t['coefficient']) for t in row['terms']}
    assert len(p)==len(row['terms']) and all(p.values());return p
def sos(ir):
    out=defaultdict(F)
    for r in ir['residuals']:
        p=poly(r);assert all(len(m)<=2 for s,m in p)
        den=lcm(*(c.denominator for c in p.values()));g=gcd(*(int(c*den) for c in p.values()))
        a=[(s,m,c*F(den,g)) for (s,m),c in p.items()]
        for j,(s,m,c) in enumerate(a):
            for k in range(j,len(a)):
                t,n,d=a[k];out[s+t,tuple(sorted(m+n))]+=c*d*(1 if j==k else 2)
    return {k:v for k,v in out.items() if v}
art=load(H/'ARTIFACTS.json')
baseline=H/'sources/work/quartic-version6-release/repository/quartics/quartic-394-411'
if baseline.is_dir():
    assert sos(load(baseline/'candidate394-ir.json'))==poly(load(baseline/'polynomial394.json'))
    print('PASS exact published394 baseline polynomial')
for name,pin in art['files'].items():
    raw=(H/name).read_bytes();assert len(raw)==pin['bytes'] and hashlib.sha256(raw).hexdigest()==pin['sha256'],name
for n in [299,314]:
    src=load(H/f'candidate{n}-ir.json');cp=load(H/f'compact{n}-ir.json');sourcePoly=poly(load(H/f'polynomial{n}.json'))
    mapping=load(H/f'coordinate-map{n}.json');mp={int(i):j for i,j in mapping['sourceToCompact'].items()}
    assert len(mp)==n and set(mp.values())==set(range(1,n+1)) and mp[0]==1
    assert {int(j):i for j,i in mapping['compactToSource'].items()}=={j:i for i,j in mp.items()}
    assert cp['coordinates']==[dict(c,id=mp[c['id']],sourceId=c['id']) for c in sorted(src['coordinates'],key=lambda c:c['id'])]
    sr={r['id']:r for r in src['residuals']};cr={r['id']:r for r in cp['residuals']}
    assert len(sr)==len(src['residuals']) and len(cr)==len(cp['residuals']) and set(sr)==set(cr)
    for i,r in sr.items():
        assert {k:v for k,v in r.items() if k!='terms'}=={k:v for k,v in cr[i].items() if k!='terms'}
        assert poly(cr[i])=={(s,tuple(mp[j] for j in m)):c for (s,m),c in poly(r).items()}
    expectedParameter=dict(src['fixedParameter'])
    if expectedParameter.get('coordinate'):expectedParameter['sourceCoordinate']=mp[expectedParameter['sourceCoordinate']]
    assert cp['fixedParameter']==expectedParameter
    for key,value in src.items():
        if key not in {'coordinates','residuals','fixedParameter'}:assert cp[key]==value
    stem=f'quartic-{n}-'+('symbolic' if n==299 else 'ordinary')+'-coefficients'
    tab=load(H/(stem+'.json'));p=poly(tab)
    assert tab['coordinates']==cp['coordinates'] and tab['inputCoordinate']==1
    assert p=={(s,tuple(mp[j] for j in m)):c for (s,m),c in sourcePoly.items()}==sos(cp)
    assert set(i for s,m in p for i in m)==set(range(1,n+1)) and gcd(*(int(c) for c in p.values()))==1
    assert max(len(m) for s,m in p)==4
    raw=(H/(stem+'.txt')).read_bytes();parsed={}
    for line in raw.decode('ascii').splitlines():
        if line.startswith('#'):continue
        c,s,m=line.split(' | ');key=int(s),tuple(map(int,m.split(','))) if m else ()
        assert key not in parsed;parsed[key]=F(c)
    assert parsed==p
    stats=art['statistics'][str(n)]
    assert (len(cp['coordinates']),len(cr),len(p),len(raw))==(n,stats['residuals'],stats['coefficientPowerEntries'],stats['compactTextBytes'])
    if n==314:
        maximum=max(abs(c) for c in p.values());assert str(maximum)==stats['maximumCoefficient']
        assert 2**6495<=maximum<2**6496 and maximum.numerator.bit_length()==6496
        sourceText=(H/'quartic-314-source-id-coefficients.txt').read_bytes();assert len(sourceText)==222890
        q={}
        for line in sourceText.decode('ascii').splitlines():
            c,word=line.split('\t');m=[]
            if word!='1':
                for token in word.split('*'):
                    match=re.fullmatch(r'x(\d+)(?:\^(\d+))?',token);assert match
                    m.extend([int(match[1])]*int(match[2] or 1))
            key=0,tuple(m);assert key not in q;q[key]=F(c)
        assert q==sourcePoly
    else:
        # Specialized coefficient maximum, checked without expanding C.
        groups=defaultdict(dict)
        for (s,m),c in p.items():groups[m][s]=c
        for a in groups.values():
            for eps in [-1,1]:
                d={s:F(186624 if s==2 else 0)+eps*a.get(s,0) for s in set(a)|{2}}
                d={s:c for s,c in d.items() if c}
                if d:
                    lead=max(d);assert d[lead]>0 and sum(abs(c) for s,c in d.items() if s<lead)<2**2048
        assert groups[(mp[89],)*4]=={2:F(186624)}
    print(f'PASS compact{n}: variables, input bijection, all residuals, full SOS, tables and bounds')
