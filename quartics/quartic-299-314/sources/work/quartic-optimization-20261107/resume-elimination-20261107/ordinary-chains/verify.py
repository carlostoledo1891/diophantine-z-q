"""Independent replay of all ordinary chain/consumer identities and full SOS."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
H=Path(__file__).resolve().parent
def read(p,pin):
    assert hashlib.sha256(p.read_bytes()).hexdigest()==pin,p
    return json.loads(p.read_bytes())
old=read(H.parent/'exact319/candidate319-ir.json','847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676')
oldtable=read(H.parent/'exact319/polynomial319.json','8320b69d290a37017060e34742fb025cbc1c13e40a5b7d750893e9912d3796ef')
K=next(int(t['coefficient']) for t in oldtable['terms'] if not t['monomial'] and not t['sPower'])
pins={336:('72ef14cca86d1b4a817f93c5c2abf15b3a88a479ad7477f19b96c619daee6c39','0b87575e8d9539935fd9f073903e1d8a7babd6c1d11b5606e575100354d27f03'),335:('0985485cfda55f03b3dbde5949141fbad0846cd33fc0109aec7af024527fd217','6e2f547800d23c794801583ef3f5afced5e70daf9b0f0895f15bedb04c44a166'),334:('8cfc3dbbd900d5393a23572d2d4571b49fa1927a02a1297dcab281017c252951','7d71c71c5f1b243b3c6cf46a6d0179e695bb5342bc04ebffa9cb228bbfccd18d')}
chains={336:[513]*9+[2]+[0]*6,335:[1025]*10+[2]+[0]*4,334:[2049]+[2048]*11+[0,0]}
def dec(r):
    assert all(t['sPower']==0 for t in r['terms'])
    p={tuple(t['monomial']):F(t['coefficient']) for t in r['terms']}
    assert len(p)==len(r['terms'])
    return p
oo={r['id']:r for r in old['residuals']};oldcoords={c['id']:c for c in old['coordinates']}
assert {r['id'] for r in old['residuals'] if any(t['sPower'] for t in r['terms'])}=={504,903}
assert {tuple(t['monomial']):F(t['coefficient']) for t in oo[903]['terms'] if t['sPower']==1}=={(83,83):-48,(87,87):-48,(89,89):-432}
assert {tuple(t['monomial']):F(t['coefficient']) for t in oo[504]['terms'] if t['sPower']==1}=={(57,):-4}
outputs=[]
for size,(ih,ph) in pins.items():
    p=read(H/str(size)/'candidate-ir.json',ih);table=read(H/str(size)/'polynomial.json',ph)
    aa=chains[size];last=1000+len(aa);rr={r['id']:r for r in p['residuals']};cc={c['id']:c for c in p['coordinates']}
    assert set(rr)==set(oo)|set(range(1000,last+1))
    assert set(cc)==set(oldcoords)|set(range(1000,last+1))
    assert all(cc[i]==c for i,c in oldcoords.items())
    assert all(rr[i]==oo[i] for i in oo if i not in {504,903})
    for key in old:
        if key not in {'coordinates','residuals','status','fixedParameter'}:assert p[key]==old[key]
    assert p['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':True,'sourceCoordinate':last}
    assert dec(rr[1000])=={(1000,):1,(83,83):-48,(87,87):-48,(89,89):-432}
    exponent=0
    for j,a in enumerate(aa):
        i=1001+j
        assert dec(rr[i])=={(i,):1,(() if j==0 else (i-1,i-1)):-3**a}
        exponent=a if j==0 else 2*exponent+a
    assert exponent==2**25
    assert dec(rr[903])=={(903,):1,(543,544):-2,(1000,last):-1}
    assert dec(rr[504])=={(55,55):1,(56,56):6,(57,57):-2,(57,last):-4,(903,903):-3}
    total=defaultdict(int);used=set()
    for r in rr.values():
        q=dec(r);assert max(map(len,q))<=2;used.update(i for m in q for i in m)
        den=lcm(*(c.denominator for c in q.values()));g=gcd(*(int(c*den) for c in q.values()));terms=[(m,int(c*den)//g) for m,c in q.items()]
        for j,(m,c) in enumerate(terms):
            for k in range(j,len(terms)):
                n,d=terms[k];total[tuple(sorted(m+n))]+=c*d*(1 if j==k else 2)
    total={m:c for m,c in total.items() if c}
    assert total==dec(table) and used==set(cc)
    assert (len(cc),len(rr),len(total),max(map(len,total)))==(size,size-30,3*size+4699,4)
    assert gcd(*total.values())==1
    maximum=max(abs(c) for c in total.values())
    assert maximum==3**(2*max(aa))+K and total[()]==maximum
    outputs.append({'variables':size,'rows':len(rr),'monomials':len(total),'max_bits':maximum.bit_length(),'max_decimal_digits':len(str(maximum)),'max_expression':f'3^{2*max(aa)}+K','chain_gates':len(aa),'chain_final_exponent':exponent,'full_SOS':True})
# Lower bounds apply only to explicit monomial multiplication chains, not all encodings.
limits=[]
for cap,n in [(3247,16),(8193,14)]:
    k=0
    while (3**(2*(k+1))).bit_length()<=cap:k+=1
    assert k*(2**(n-1)-1)<2**25
    limits.append({'coefficient_bit_cap':cap,'maximum_multiplier_exponent':k,'minimum_chain_gates_in_model':n,'upper_exponent_with_one_fewer':k*(2**(n-1)-1)})
out={'companions':outputs,'restricted_chain_lower_bounds':limits,'inherited_constant_bits':K.bit_length(),'independent_review':'required'}
(H/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
