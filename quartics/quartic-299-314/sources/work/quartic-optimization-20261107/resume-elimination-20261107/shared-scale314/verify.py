"""Producer-free, exact finite verification of candidate314.

Does not prove the new arithmetic projection argument.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd,lcm
import hashlib,json
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[2]/'quartic-under300-20261107/10-combination/combined315/candidate315-ir.json'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(SOURCE)=='d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8'
assert digest(HERE/'candidate314-ir.json')=='7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5'
source=json.loads(SOURCE.read_bytes());target=json.loads((HERE/'candidate314-ir.json').read_bytes())
src={r['id']:r for r in source['residuals']};dst={r['id']:r for r in target['residuals']}
def p(row):
    out={(t['sPower'],tuple(t['monomial'])):F(t['coefficient']) for t in row['terms']}
    assert len(out)==len(row['terms']) and all(c for c in out.values())
    return out
def v(i,c=1):return {(0,(i,)):F(c)}
ONE={(0,()):F(1)}
def add(*ps):
    out=defaultdict(F)
    for z in ps:
        for m,c in z.items():out[m]+=c
    return {m:c for m,c in out.items() if c}
def neg(z):return {m:-c for m,c in z.items()}
def mul(a,b):
    out=defaultdict(F)
    for (e,m),c in a.items():
        for (f,n),d in b.items():out[e+f,tuple(sorted(m+n))]+=c*d
    return {m:c for m,c in out.items() if c}
def scaled(z,c):return {m:c*d for m,d in z.items() if c*d}
def check(row,expected):assert p(dst[row])==expected,(row,p(dst[row]),expected)
removed={326,376,426,526,533,540,541,544,545,546,547,550,551,552,553,556,557,558,745,760,775,918,929,940}
groupids=set(range(919,925))|set(range(930,936))|set(range(941,947))
sharedids=set(range(900,918))
assert set(src)-set(dst)==removed
assert set(dst)-set(src)==set(range(2000,2022))
changed={i for i in set(src)&set(dst) if src[i]!=dst[i]}
assert changed==groupids|sharedids
for i in set(src)&set(dst)-changed:assert src[i]==dst[i]
oldids={c['id'] for c in source['coordinates']};ids={c['id'] for c in target['coordinates']}
dropped={360,369,374,408,417,422,456,465,470,843,844,845}
assert oldids-ids==dropped and ids-oldids==set(range(1100,1111))
assert len(ids)==len(target['coordinates'])==314
assert len(dst)==len(target['residuals'])==283
for row in dst.values():
    for (e,m),c in p(row).items():
        assert len(m)<=2 and set(m)<=ids and tuple(sorted(m))==m
assert source['input']==target['input'] if 'input' in source else True
for key in source:
    if key not in {'coordinates','residuals','status'}:assert source[key]==target[key]
# All rescaled outputs are private to their own definitions and detector groups.
scale_map={826:1108,827:1108,820:1108,821:1108,822:1108,823:1108,835:1108,836:1108,828:1108,829:1108,
           837:1106,838:1106,839:1106,840:1106,830:1107,831:1107,841:1107,842:1107}
for coord,power in scale_map.items():
    uses={i for i,r in src.items() if any(coord in m for e,m in p(r))}
    assert uses<=sharedids|groupids
for i in sharedids:
    expected={}
    for (e,m),c in p(src[i]).items():
        if len(m)==1 and m[0] in scale_map:m=tuple(sorted((m[0],scale_map[m[0]])))
        expected[e,m]=c
    check(i,expected)
# Physical field components; all imaginary entries are coefficients of sqrt(2).
leaf={name:(v(a),v(b)) for name,a,b in [('H1',826,827),('H2',820,821),('H3',822,823),('H4',835,836),
        ('M0',837,838),('M1',839,840),('P2',828,829),('P3',830,831),('P4',841,842),('P1square',1109,1110)]}
leaf['U']=(v(311),v(312,2));leaf['P1']=(v(255),v(256,2))
for name,a,b in [('T0',182,183),('T2',200,201),('T3',212,213),('T4',224,225)]:
    leaf[name]=(add(v(a,F(72097,5764801)),v(b,F(101904,5764801))),add(v(a,F(-50952,5764801)),v(b,F(-72097,5764801))))
leaf['Z1']=(add(v(192,F(37249,2401)),v(193,F(-34848,2401))),add(v(192,F(-25476,2401)),v(193,F(25476,2401))))
# Bind these maps against the actual original groups, including their output normalizations.
source_groups=[[('H1',374),('H4',843),('M0',369),('T0',356),('T4',832)],
               [('H2',374),('U',360),('T2',356),('Z1',832),('P1',350)],
               [('H3',374),('M1',369),('T3',356),('P2',843),('P3',832),('P4',350)]]
for group,spec in enumerate(source_groups):
    for component in (0,1):
        expected=add(v(634+group*2+component),neg(ONE) if component==0 else {},
                     *[neg(mul(v(w),leaf[name][component])) for name,w in spec])
        assert p(src[919+2*group+component])==expected
common=[add(v(1101),neg(mul(v(1100),v(1100)))),add(v(1102),neg(mul(v(1101),v(1101)))),
        add(v(1103),neg(mul(v(1102),v(1102)))),add(v(1104),neg(mul(v(1103),v(1103)))),
        add(mul(v(1104),v(1105)),neg(ONE)),add(mul(v(1106),v(1105)),neg(mul(v(1104),v(1103)))),
        add(v(1107),neg(mul(v(1106),v(1106)))),add(v(1108),neg(mul(v(1107),v(1107)))),
        add(v(1109),neg(mul(v(255),v(255))),scaled(mul(v(256),v(256)),-8)),
        add(v(1110),scaled(mul(v(255),v(256)),-4))]
for i,row in enumerate(common,2000):check(i,row)
rs=[add(v(37,F(-16,976393)),v(346,F(76265,1952786)),v(348,F(3081901,1952786))),
    add(v(391,F(-64,976393)),v(392,F(610120,976393)),v(394,F(38573184,976393))),
    add(v(37,F(-16,976393)),v(439,F(-512,976393)),v(440,F(76265,1952786)),v(442,F(602706,976393)))]
specs=[[('R','H1'),('R2','H2'),('E','U'),('E4','Z1')],
       [('R','H3'),('R2','H4'),('R3','P2'),('E4','P4'),('E','P1square'),('E8','T0')],
       [('R','M0'),('R2','M1'),('R3','P3'),('E8','T2'),('E4','T3'),('E','T4')]]
for j,(E,R2,R3,E4,E8,gstart,outstart) in enumerate([(350,355,359,832,356,919,634),(398,403,407,833,404,930,654),(446,451,455,834,452,941,674)]):
    R=rs[j];assert p(src[302+50*j])==add(mul(v(E),R),neg(ONE))
    local=[add(v(R2),neg(mul(R,R))),add(v(R3),neg(mul(R,v(R2)))),
           add(mul(v(E4),v(R3)),neg(v(E))),add(v(E8),neg(mul(v(E4),v(E4))))]
    for i,row in enumerate(local,2010+4*j):check(i,row)
    weights={'R':R,'R2':v(R2),'R3':v(R3),'E':v(E),'E4':v(E4),'E8':v(E8)}
    for g,spec in enumerate(specs):
        for c in (0,1):
            expected=add(v(outstart+2*g+c),neg(ONE) if c==0 else {},
                *[neg(mul(weights[w],leaf[name][c])) for w,name in spec])
            if g==0 and c==0:expected=add(expected,neg(mul(v(1104),v(E8))))
            check(gstart+2*g+c,expected)
# Reconstruct the canonical sum of primitive integral squares, without the producer.
total=defaultdict(int)
for row in dst.values():
    q=p(row);den=lcm(*(x.denominator for x in q.values()));content=gcd(*(int(x*den) for x in q.values()))
    q={m:int(x*den)//content for m,x in q.items()}
    for (e,m),a in q.items():
        for (f,n),b in q.items():total[e+f,tuple(sorted(m+n))]+=a*b
total={m:c for m,c in total.items() if c}
artifact=json.loads((HERE/'polynomial314.json').read_bytes())
actual={(t['sPower'],tuple(t['monomial'])):int(t['coefficient']) for t in artifact['terms']}
assert total==actual and len(actual)==len(artifact['terms'])==6138
assert len({m for e,m in actual})==6135
assert max(len(m) for e,m in actual)==4
assert gcd(*actual.values())==1
by_monomial=defaultdict(dict)
for (e,m),c in actual.items():by_monomial[m][e]=c
assert by_monomial[(89,89,89,89)]=={0:64,2:186624}
assert max(e for e,m in actual)==2
assert all(abs(cs.get(2,0))<186624 for m,cs in by_monomial.items() if m!=(89,89,89,89))
assert max(abs(c).bit_length() for c in actual.values())<=1520
# C=3^(2^25)>2^1522. Thus the lower two coefficients of any other
# monomial contribute less than C^2, below the integer leading gap.
assert digest(HERE/'polynomial314.json')=='82f10a736855acba8c12a09406a5c954ddefa22825dbffa2d773005a6b6b05e8'
result={'status':'PASS: exact finite circuit, consumer coverage and SOS only; arithmetic proof separate',
 'source_sha256':digest(SOURCE),'candidate_sha256':digest(HERE/'candidate314-ir.json'),
 'variables':314,'residuals':283,'degree':4,'monomials':6135,'coefficient_entries':6138,'content':1,
 'largest_absolute_coefficient':'186624*C^2+64, C=3^(2^25)',
 'unchanged_old_rows':len(set(src)&set(dst)-changed),'changed_old_rows':sorted(changed),
 'removed_old_rows':sorted(removed),'new_rows':list(range(2000,2022))}
(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
