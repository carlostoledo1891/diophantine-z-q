"""Ordinary integer-coefficient companions of exact319, with bounded constants."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent
SOURCE=H.parent/'exact319/candidate319-ir.json'
PIN='847d21a2d0a45571f043b82289df0da55f4e814167844bdc39fc134e4f4c2676'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN
source=json.loads(SOURCE.read_bytes())
source_table_path=H.parent/'exact319/polynomial319.json'
assert hashlib.sha256(source_table_path.read_bytes()).hexdigest()=='8320b69d290a37017060e34742fb025cbc1c13e40a5b7d750893e9912d3796ef'
inherited_constant=next(int(t['coefficient']) for t in json.loads(source_table_path.read_bytes())['terms'] if not t['monomial'] and not t['sPower'])
N=2**25
def digits(n):
    k=(N+(2**n-1)-1)//(2**n-1);rest=N;out=[]
    for shift in range(n-1,-1,-1):
        a=min(k,rest//2**shift);out.append(a);rest-=a*2**shift
    assert rest==0
    return out
chains={16:digits(16),15:digits(15),14:[2049]+[2048]*11+[0,0]}
def terms(data):return [{'sPower':0,'monomial':list(m),'coefficient':str(c)} for m,c in data]
def write(path,obj):
    path.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='\n')
    return hashlib.sha256(path.read_bytes()).hexdigest()
reports=[]
write(H/'INHERITED-CONSTANT.json',{'definition':'Coefficient of the constant monomial in the frozen polynomial319.json','source_sha256':'8320b69d290a37017060e34742fb025cbc1c13e40a5b7d750893e9912d3796ef','K':str(inherited_constant),'bits':inherited_constant.bit_length()})
for count,aa in chains.items():
    total_vars=320+count;d=H/str(total_vars);d.mkdir(exist_ok=True)
    p=copy.deepcopy(source);last=1000+count
    p['fixedParameter']={'name':'C','value':'3^(2^25)','coordinate':True,'sourceCoordinate':last}
    p['status']='Ordinary integer coefficient lift of exact319; independent review pending.'
    p['coordinates'].append({'id':1000,'name':'ordinary.Qroots','kind':'gate','block':'ordinary_lift','protected':False})
    def row(i,name,data):p['residuals'].append({'id':i,'name':name,'kind':'structural','block':'ordinary_lift','terms':terms(data)})
    row(1000,'ordinary.Qroots.definition',[((1000,),1),((83,83),-48),((87,87),-48),((89,89),-432)])
    ee=[]
    for j,a in enumerate(aa):
        i=1001+j;p['coordinates'].append({'id':i,'name':'ordinary.constant'+str(j),'kind':'constant_gate','block':'ordinary_lift','protected':False})
        row(i,'ordinary.constant'+str(j),[((i,),1),(tuple() if not j else (i-1,i-1),-3**a)])
        ee.append(a if not j else 2*ee[-1]+a)
    assert ee[-1]==N
    for r in p['residuals']:
        if r['id']==903:r['terms']=terms([((903,),1),((543,544),-2),((1000,last),-1)])
        elif r['id']==504:r['terms']=terms([((55,55),1),((56,56),6),((57,57),-2),((57,last),-4),((903,903),-3)])
    poly=defaultdict(int)
    for r in p['residuals']:
        q={tuple(t['monomial']):F(t['coefficient']) for t in r['terms']};assert not any(t['sPower'] for t in r['terms'])
        den=lcm(*(c.denominator for c in q.values()));g=gcd(*(int(c*den) for c in q.values()));q={m:int(c*den)//g for m,c in q.items()}
        for m,c in q.items():
            for v,z in q.items():poly[tuple(sorted(m+v))]+=c*z
    poly={m:c for m,c in poly.items() if c}
    ih=write(d/'candidate-ir.json',p)
    ph=write(d/'polynomial.json',{'terms':terms(sorted(poly.items()))})
    maximum=max(abs(c) for c in poly.values())
    assert maximum==3**(2*max(aa))+inherited_constant
    cert={'source_sha256':PIN,'candidate_sha256':ih,'polynomial_sha256':ph,'variables':len(p['coordinates']),'witnesses':len(p['coordinates'])-1,'residuals':len(p['residuals']),'monomials':len(poly),'degree':max(map(len,poly)),'chain_coordinates':count,'multiplier_exponents':aa,'value_exponents':ee,'max_multiplier_exponent':max(aa),'max_coefficient_bits':maximum.bit_length(),'max_coefficient_decimal_digits':len(str(maximum)),'max_coefficient_expression':'3^'+str(2*max(aa))+' + K','independent_review':'required'}
    write(d/'CERTIFICATE.json',cert);reports.append(cert)
write(H/'SUMMARY.json',reports)
print(json.dumps(reports,indent=2))
