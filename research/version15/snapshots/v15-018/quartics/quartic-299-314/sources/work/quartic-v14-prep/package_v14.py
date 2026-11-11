"""Prepare exact selected artifacts. This does not approve or publish a release."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import json,hashlib,copy
H=Path(__file__).resolve().parent;W=H.parent;O=H/'quartic-299-314';O.mkdir(exist_ok=True)
S=W/'quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2'
T=W/'quartic-under300-20261107/10-combination/ordinary-reciprocal299/314'
PINS={'symbolic':'8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815','symbolicPolynomial':'e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,obj):
    b=(json.dumps(obj,indent=2)+'\n').encode()
    if p.exists():assert p.read_bytes()==b,p
    else:p.write_bytes(b)
def copy_exact(src,dst):
    b=src.read_bytes()
    if dst.exists():assert dst.read_bytes()==b,dst
    else:dst.write_bytes(b)
def load(p):return json.loads(p.read_bytes())
def poly(obj):
    out={(t['sPower'],tuple(t['monomial'])):F(t['coefficient']) for t in obj['terms']}
    assert len(out)==len(obj['terms']) and all(out.values());return out
def terms(p):return [{'sPower':s,'monomial':list(m),'coefficient':str(c)} for (s,m),c in sorted(p.items()) if c]
def sos(ir):
    total=defaultdict(F)
    for r in ir['residuals']:
        p=poly(r);den=lcm(*(c.denominator for c in p.values()));g=gcd(*(int(c*den) for c in p.values()))
        ts=[(s,m,c*F(den,g)) for (s,m),c in p.items()]
        for j,(s,m,c) in enumerate(ts):
            for k in range(j,len(ts)):
                t,n,d=ts[k];total[s+t,tuple(sorted(m+n))]+=c*d*(1 if j==k else 2)
    return {m:c for m,c in total.items() if c}
assert sha(S/'candidate299-ir.json')==PINS['symbolic'] and sha(S/'polynomial299.json')==PINS['symbolicPolynomial']
cert=load(T/'CERTIFICATE.json')
for name,key in [('candidate-ir.json','candidateSha256'),('polynomial.json','polynomialSha256'),('polynomial.txt','textSha256')]:assert sha(T/name)==cert[key]
assert (T/'polynomial.txt').stat().st_size==222890
stats={};files={}
for n,ip,pp in [(299,S/'candidate299-ir.json',S/'polynomial299.json'),(314,T/'candidate-ir.json',T/'polynomial.json')]:
    ir=load(ip);table=load(pp);p=poly(table);assert sos(ir)==p
    copy_exact(ip,O/f'candidate{n}-ir.json');copy_exact(pp,O/f'polynomial{n}.json')
    coords=sorted(ir['coordinates'],key=lambda c:c['id']);mapping={c['id']:j+1 for j,c in enumerate(coords)}
    assert len(coords)==n and mapping[0]==1 and coords[0]['kind']=='input'
    cs=[dict(c,id=mapping[c['id']],sourceId=c['id']) for c in coords]
    compact=copy.deepcopy(ir);compact['coordinates']=cs
    compact['residuals']=[dict(r,terms=terms({(s,tuple(mapping[i] for i in m)):c for (s,m),c in poly(r).items()})) for r in ir['residuals']]
    compact['coordinateConvention']={'range':[1,n],'inputCoordinate':1,'sourceInputCoordinate':0}
    if compact['fixedParameter'].get('coordinate'):compact['fixedParameter']['sourceCoordinate']=mapping[ir['fixedParameter']['sourceCoordinate']]
    dump(O/f'compact{n}-ir.json',compact)
    cp={(s,tuple(mapping[i] for i in m)):c for (s,m),c in p.items()};assert sos(compact)==cp
    stem=f'quartic-{n}-'+('symbolic' if n==299 else 'ordinary')+'-coefficients'
    compactTable={'format':'integer-quartic-consecutive-coordinates-v2','variables':n,'witnesses':n-1,'degree':4,
        'inputCoordinate':1,'coordinates':cs,'terms':terms(cp)}
    if n==299:compactTable['fixedParameter']=ir['fixedParameter']
    dump(O/(stem+'.json'),compactTable)
    lines=[f'# Integer quartic in {n} rational variables; x1 is the input.',
        '# Compact physical coordinates run from1 through the total variable count.',
        '# Rows: coefficient | C exponent | variable indices.',
        '# C=3^(2^25) is a fixed integer.' if n==299 else '# Every C exponent is zero; every coefficient is an explicit decimal integer.']
    lines += [f'# x{c["id"]} = source coordinate {c["sourceId"]}: {c["name"]}' for c in cs]
    lines += [t['coefficient']+' | '+str(t['sPower'])+' | '+','.join(map(str,t['monomial'])) for t in compactTable['terms']]
    text=('\n'.join(lines)+'\n').encode('ascii');tp=O/(stem+'.txt')
    if tp.exists():assert tp.read_bytes()==text
    else:tp.write_bytes(text)
    dump(O/f'coordinate-map{n}.json',{'sourceInput':0,'compactInput':1,'sourceToCompact':mapping,'compactToSource':{v:k for k,v in mapping.items()}})
    st={'variables':n,'witnesses':n-1,'residuals':len(ir['residuals']),'monomials':len({m for s,m in p}),
        'coefficientPowerEntries':len(p),'degree':4,'content':gcd(*(int(c) for c in p.values())),
        'compactTextBytes':len(text),'sourceCandidateSha256':sha(ip),'sourcePolynomialSha256':sha(pp)}
    if n==299:st['maximumCoefficient']='186624*3^(2^26)'
    else:
        maximum=max(abs(c) for c in p.values());assert maximum.denominator==1
        st.update(maximumCoefficient=str(maximum),maximumCoefficientBits=int(maximum).bit_length(),maximumCoefficientDigits=len(str(maximum)),sourceTextBytes=222890,sourceTextSha256=cert['textSha256'])
    stats[str(n)]=st
copy_exact(T/'polynomial.txt',O/'quartic-314-source-id-coefficients.txt')
copy_exact(T/'CERTIFICATE.json',O/'ordinary314-source-certificate.json')
dump(O/'ARTIFACTS.json',{'status':'Author preparation; compact remapping/package review pending','inputCoordinate':1,
    'coordinateRange':'1..totalVariables','statistics':stats,'constantLift':{'constantGates':14,'rootSumGates':1,
    'exponents':[2049]+[2048]*11+[0,0],'targetExponent':2**25,'coefficientBound':'<2^6496'},
    'files':{p.name:{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(O.iterdir()) if p.is_file() and p.name!='ARTIFACTS.json'}})
print(json.dumps({n:{k:v for k,v in s.items() if k!='maximumCoefficient'} for n,s in stats.items()},indent=2))
