"""Independent complete finite check of the ordinary299 transports."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations_with_replacement
from math import gcd,lcm
import hashlib,json,re

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];WORK=ROOT/'work'
PACKET=WORK/'quartic-under300-20261107/10-combination/ordinary-reciprocal299'
SOURCE=WORK/'quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(PACKET/'MANIFEST.json')=='904ccb6a91c8fae93071a8009c2403f852bf546db4fc6da2457d91f09f139e05'
assert sha(PACKET/'REPORT.md')=='2139ab1681a9ec6ec63c547ea3278b8ea981cf9311c36893713ae291b685e809'
manifest=json.loads((PACKET/'MANIFEST.json').read_bytes())
records=manifest['files']+manifest['sources']
for item in records:
    path=WORK/item['path'];raw=path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==item['sha256'],path
    assert len(raw)==item['bytes'],path
assert sha(SOURCE/'candidate299-ir.json')=='8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815'
assert sha(SOURCE/'polynomial299.json')=='e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c'
source=json.loads((SOURCE/'candidate299-ir.json').read_bytes())

def readpol(obj):
    result={}
    for term in obj['terms']:
        key=(term['sPower'],tuple(term['monomial']))
        assert key not in result and tuple(sorted(key[1]))==key[1]
        value=Fraction(term['coefficient']);assert value
        result[key]=value
    return result
def plus(*ps):
    out={}
    for p in ps:
        for m,c in p.items():out[m]=out.get(m,0)+c
    return {m:c for m,c in out.items() if c}
def times(p,q):
    out={}
    for (i,m),a in p.items():
        for (j,n),b in q.items():
            key=(i+j,tuple(sorted(m+n)));out[key]=out.get(key,0)+a*b
    return {m:c for m,c in out.items() if c}
def ordinary(p):
    assert all(i==0 for i,m in p)
    return {m:c for (i,m),c in p.items()}
def sos(ir):
    result={};active=set()
    for row in ir['residuals']:
        p=readpol(row);assert max(len(m) for i,m in p)<=2
        active.update(v for i,m in p for v in m)
        denominator=lcm(*(c.denominator for c in p.values()))
        nums={m:int(c*denominator) for m,c in p.items()}
        content=gcd(*nums.values());p={m:c//content for m,c in nums.items()}
        result=plus(result,times(p,p))
    assert active=={c['id'] for c in ir['coordinates']}
    return result
sr={r['id']:r for r in source['residuals']};sc={c['id']:c for c in source['coordinates']}
assert len(sr)==len(source['residuals'])==279 and len(sc)==299
source_table=readpol(json.loads((SOURCE/'polynomial299.json').read_bytes()))
assert sos(source)==source_table and len(source_table)==6630
assert {i for i,r in sr.items() if any(s for s,m in readpol(r))}=={504,1903}
K=source_table[(0,())];assert K.denominator==1;K=int(K)
assert K.bit_length()==1514
inherited=json.loads((PACKET/'INHERITED-CONSTANT.json').read_bytes())
assert int(inherited['K'])==K and inherited['bits']==1514
q={(0,(83,83)):48,(0,(87,87)):48,(0,(89,89)):432}
chains={316:[513]*9+[2]+[0]*6,315:[1025]*10+[2]+[0]*4,314:[2049]+[2048]*11+[0,0]}
results=[]
for count,chain in chains.items():
    folder=PACKET/str(count);ir=json.loads((folder/'candidate-ir.json').read_bytes())
    rows={r['id']:r for r in ir['residuals']};coords={c['id']:c for c in ir['coordinates']}
    last=1000+len(chain);extra=set(range(1000,last+1))
    assert not(extra&set(sr)) and not(extra&set(sc))
    assert len(rows)==len(ir['residuals']) and len(coords)==len(ir['coordinates'])
    assert set(rows)==set(sr)|extra and set(coords)==set(sc)|extra
    assert all(coords[i]==row for i,row in sc.items())
    assert all(rows[i]==row for i,row in sr.items() if i not in {504,1903})
    for key,value in source.items():
        if key not in {'coordinates','residuals','status','fixedParameter'}:assert ir[key]==value
    assert ir['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':True,'sourceCoordinate':last}
    assert ordinary(readpol(rows[1000]))=={(1000,):1,(83,83):-48,(87,87):-48,(89,89):-432}
    exponents=[]
    for j,a in enumerate(chain):
        i=1001+j;mon=() if not j else (i-1,i-1)
        assert ordinary(readpol(rows[i]))=={(i,):1,mon:-3**a}
        exponents.append(a if not j else 2*exponents[-1]+a)
    assert exponents[-1]==2**25
    assert ordinary(readpol(rows[504]))=={(55,55):1,(56,56):6,(57,57):-2,(57,last):-4,(903,903):-3}
    assert ordinary(readpol(rows[1903]))=={(903,):1,(543,544):-2,(1000,last):-1}
    for i in [504,1903]:
        recovered={}
        for m,c in ordinary(readpol(rows[i])).items():
            term={(0,()):c}
            for v in m:
                term=times(term,q if v==1000 else {(1,()):1} if v==last else {(0,(v,)):1})
            recovered=plus(recovered,term)
        assert recovered==readpol(sr[i])
    table=readpol(json.loads((folder/'polynomial.json').read_bytes()))
    total=sos(ir);assert total==table
    decimal=ordinary(total);assert all(c.denominator==1 for c in decimal.values())
    assert len(coords)==count and len(rows)==count-20
    assert len(decimal)=={316:6678,315:6675,314:6672}[count]
    assert max(map(len,decimal))==4 and gcd(*(int(c) for c in decimal.values()))==1
    maximum=max(abs(int(c)) for c in decimal.values())
    assert maximum==decimal[()]==3**(2*chain[0])+K
    bits=maximum.bit_length();assert bits=={316:1627,315:3250,314:6496}[count]
    assert (1<<(bits-1))<=maximum<(1<<bits)
    text=(folder/'polynomial.txt').read_bytes();parsed={}
    for line in text.decode('ascii').splitlines():
        coefficient,word=line.split('\t');assert re.fullmatch(r'-?[0-9]+',coefficient)
        mon=[]
        if word!='1':
            for token in word.split('*'):
                match=re.fullmatch(r'x([0-9]+)(?:\^([0-9]+))?',token);assert match
                mon += [int(match[1])]*int(match[2] or 1)
        mon=tuple(mon);assert mon==tuple(sorted(mon)) and mon not in parsed
        parsed[mon]=int(coefficient)
    assert parsed==decimal
    cert=json.loads((folder/'CERTIFICATE.json').read_bytes())
    for key,value in {'variables':count,'witnesses':count-1,'residuals':len(rows),'monomials':len(decimal),'degree':4,'content':1,'constantGates':len(chain),'rootSumGates':1,'maxCoefficientBits':bits,'maxCoefficientDigits':len(str(maximum)),'textBytes':len(text)}.items():assert cert[key]==value
    assert int(cert['maxCoefficient'])==maximum
    results.append({'variables':count,'witnesses':count-1,'residuals':len(rows),'monomials':len(decimal),'chain_exponents':exponents,'constant_gates':len(chain),'root_sum_gates':1,'maximum_expression':f'3^{2*chain[0]}+K','maximum_bits':bits,'maximum_digits':len(str(maximum)),'text_bytes':len(text),'ir_sha256':sha(folder/'candidate-ir.json'),'polynomial_sha256':sha(folder/'polynomial.json'),'text_sha256':sha(folder/'polynomial.txt')})
# Recheck immutable author/source objects after the complete computation.
assert all(sha(WORK/item['path'])==item['sha256'] for item in records)
output={'status':'PASS independent exact finite transport check','manifest_sha256':sha(PACKET/'MANIFEST.json'),'source_ir_sha256':sha(SOURCE/'candidate299-ir.json'),'source_polynomial_sha256':sha(SOURCE/'polynomial299.json'),'manifest_objects_verified':len(records),'source_C_consumers':[504,1903],'source_monomials':6630,'K_bits':K.bit_length(),'companions':results,'author_objects_unchanged':True}
(HERE/'CHECKS.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps(output,indent=2))
