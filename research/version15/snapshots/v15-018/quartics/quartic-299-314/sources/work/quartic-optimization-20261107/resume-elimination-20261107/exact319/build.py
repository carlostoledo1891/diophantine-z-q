"""Exact rational unscaling of the private anchor; no arithmetic change."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import copy,hashlib,json
H=Path(__file__).resolve().parent
WORK=H.parents[2]
SOURCE=WORK/'quartic-under300-20261107/10-combination/combined320/candidate320-ir.json'
PIN='d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN
old=json.loads(SOURCE.read_bytes());new=copy.deepcopy(old)
new['coordinates']=[c for c in new['coordinates'] if c['id']!=904]
for c in new['coordinates']:
    if c['id'] in (55,56,57,903):c['name']='exactUnscaledAnchor.'+{55:'u',56:'v',57:'w',903:'T'}[c['id']]
new['residuals']=[r for r in new['residuals'] if r['id']!=904]
def terms(data):return [{'sPower':e,'monomial':m,'coefficient':str(c)} for e,m,c in data]
for r in new['residuals']:
    if r['id']==903:
        r['name']='exactUnscaledAnchor.T.definition'
        r['terms']=terms([(0,[903],1),(0,[543,544],-2),(1,[83,83],-48),(1,[87,87],-48),(1,[89,89],-432)])
    if r['id']==504:
        r['name']='exactUnscaledAnchor.quaternion'
        r['terms']=terms([(0,[55,55],1),(0,[56,56],6),(0,[57,57],-2),(1,[57],-4),(0,[903,903],-3)])
new['status']='Research319: exact rational private-anchor unscaling from accepted320; independent review pending.'
total=defaultdict(int)
for r in new['residuals']:
    p={(t['sPower'],tuple(t['monomial'])):F(t['coefficient']) for t in r['terms']}
    den=lcm(*(c.denominator for c in p.values()));g=gcd(*(int(c*den) for c in p.values()))
    p={m:int(c*den)//g for m,c in p.items()}
    for (e,m),c in p.items():
        for (f,n),d in p.items():total[e+f,tuple(sorted(m+n))]+=c*d
def write(name,obj):
    p=H/name;p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='\n')
    return hashlib.sha256(p.read_bytes()).hexdigest()
ih=write('candidate319-ir.json',new)
ph=write('polynomial319.json',{'terms':[{'sPower':e,'monomial':list(m),'coefficient':str(c)} for (e,m),c in sorted(total.items()) if c]})
cert={'source_sha256':PIN,'candidate_sha256':ih,'polynomial_sha256':ph,'removed_coordinates':[904],'removed_rows':[904],'changed_rows':[504,903],'changed_coordinate_meanings':[55,56,57,903],
      'variables':len(new['coordinates']),'residuals':len(new['residuals']),'coefficient_terms':sum(bool(c) for c in total.values()),'monomials':len({m for (e,m),c in total.items() if c}),'degree':max(len(m) for (e,m),c in total.items() if c),'status':'Exact maps provided; independent review pending.'}
write('CERTIFICATE.json',cert)
print(json.dumps(cert,indent=2))
