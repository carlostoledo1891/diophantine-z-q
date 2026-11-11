"""Independent finite delta, current interfaces and SOS for combined423."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
import json,hashlib
H=Path(__file__).resolve().parent;D=H.parent/'10-combination'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def p(ts):return {tuple([-1]*t.get('sPower',0)+t['monomial']):F(t['coefficient']) for t in ts}
def v(i):return {(i,):F(1)}
def c(q):return {():F(q)} if q else {}
def add(a,b,k=1):
    d=a.copy()
    for m,q in b.items():d[m]=d.get(m,0)+k*q
    return {m:q for m,q in d.items() if q}
def scale(a,k):return {m:q*k for m,q in a.items() if q*k}
def mul(a,b):
    d={}
    for m,q in a.items():
        for n,r in b.items():
            t=tuple(sorted(m+n));d[t]=d.get(t,0)+q*r
    return {m:q for m,q in d.items() if q}
def sub(a,mp):
    d={}
    for m,q in a.items():
        t=c(q)
        for i in m:t=mul(t,mp.get(i,v(i)))
        d=add(d,t)
    return d
def norm(a):
    den=reduce(lcm,(q.denominator for q in a.values()),1);g=reduce(gcd,(abs(int(q*den)) for q in a.values()),0)
    return scale(a,F(den,g)*(1 if a[min(a)]>0 else -1))
def vars(a):return {i for m in a for i in m if i!=-1}
def rows(a):
    d={r['name']:r for r in a['residuals']};assert len(d)==len(a['residuals'])==len({r['id'] for r in a['residuals']});return d
pins={'combined431-ir.json':'180968baa12a26f0171eeeb337df61b293a3a122786929e28b9fc94c55ba5573','combined435-ir.json':'c4c8a0623be27e675f73363043ce2bc44956bd128257060e471abca9b53a0859','inputs/identity-chart427-ir.json':'6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4','combined423-ir.json':'3c19ce0d46ae80732e76fd243b7fd1c91599f4274e1c67b9a4ac6c5bd86899bf','combined423-polynomial.json':'a6342d78d4ac081f59dfd11599e725e93f52f945b21b7f1d54391c2779045689','REPORT423.md':'2b97f78a85ff62ef3ee5b498388e52efda03257d9d218c9152ccb6e349034f6e'}
for name,h in pins.items():assert sha(D/name)==h
base=read(D/'combined431-ir.json');before=read(D/'combined435-ir.json');after=read(D/'inputs/identity-chart427-ir.json');out=read(D/'combined423-ir.json')
br,cr,nr,rr=map(rows,[base,before,after,out])
bc,cc,nc,rc=[{x['id']:x for x in a['coordinates']} for a in [base,before,after,out]]
deleted=set(cr)-set(nr);added=set(nr)-set(cr)
changed={name for name in cr.keys()&nr.keys() if norm(p(cr[name]['terms']))!=norm(p(nr[name]['terms']))}
removed=set(cc)-set(nc);renamed={i for i in cc.keys()&nc.keys() if cc[i]['name']!=nc[i]['name']}
assert not set(nc)-set(cc) and removed==set(range(92,100))
assert set(rr)==(set(br)-deleted)|added
for name,row in br.items():
    if name in deleted|changed:assert norm(p(row['terms']))==norm(p(cr[name]['terms']))
    if vars(p(row['terms']))&(removed|renamed):
        assert name in cr and norm(p(row['terms']))==norm(p(cr[name]['terms']))
    if name in deleted:continue
    if name in changed:
        assert norm(p(rr[name]['terms']))==norm(p(nr[name]['terms']))
        assert {k:q for k,q in rr[name].items() if k!='terms'}=={k:q for k,q in row.items() if k!='terms'}
    else:assert rr[name]==row
for name in added:
    assert norm(p(rr[name]['terms']))==norm(p(nr[name]['terms']))
    assert {k:q for k,q in rr[name].items() if k not in ['id','terms']}=={k:q for k,q in nr[name].items() if k not in ['id','terms']}
assert set(rc)==set(bc)-removed
for i,x in rc.items():
    expected=bc[i].copy()
    if i in renamed:assert bc[i]['name']==cc[i]['name'];expected['name']=nc[i]['name']
    assert x==expected
for k in base:
    if k not in {'coordinates','residuals','status'}:assert out[k]==base[k]
# Field interfaces after H.j elimination, using the actual component scaling.
def fa(a,b,k=1):return tuple(add(x,y,k) for x,y in zip(a,b))
def fm(a,b):return add(mul(a[0],b[0]),mul(a[1],b[1]),2),add(mul(a[0],b[1]),mul(a[1],b[0]))
def fc(a,k):return tuple(scale(x,k) for x in a)
one=(c(1),{});DD=(c(11),c(-6));aa=(c(-1),c(F(7,4)));bb=(c(F(39,8)),c(F(-9,2)))
hh=(v(17),v(18));xx=(v(90),scale(v(91),2));ff=(v(140),v(141));ss=(v(142),v(143));vv=(v(700),v(701));fv=(v(160),v(161));ell=(v(188),v(189));R0=(v(186),v(187))
def match(name,expr,suffix=''):
    for j in range(2):assert norm(p(rr[name+str(j)+suffix]['terms']))==norm(expr[j]),name+str(j)
match('H.chart.x.',fa(fm(hh,hh),xx,-1),'.definition')
match('U0.f.definition.',fa(fm(xx,ff),one,-1))
match('H.chart.equation.',fa(fa(fm(ss,ss),xx,-1),fm(DD,ff)))
dd=fa(fm(fm(aa,aa),xx),DD);N=fa(fm(aa,ss),bb,-1)
match('V0.reciprocal.g.definition.',fa(fm(dd,vv),N,-1))
match('V0.f.definition.',fa(fm(vv,vv),fm(fv,ff),-1))
Tp=fa(fa(fc(DD,-2),fm(fm(aa,bb),ss),-1),fc(fm(fm(DD,bb),vv),2))
match('logV0.definition.',fa(fm(Tp,ell),fm(fm(aa,N),R0)))
# Source-sensitive scalar, anchor, odd-root and detector interfaces are unchanged.
keyrows=['anchor.translatedEquation','scalar.shiftedS.reciprocal.f1Inverse.definition','reduced_scalar.root','scalar.ratio_node.consolidated_denominator','reduced_scalar.ratio_node_squared']
for name in keyrows:assert rr[name]==br[name]
r=c(-99006679260)
for i,q in [(248,-82479248),(487,-21050600),(488,-7629700),(489,-45771136)]:r=add(r,v(i),q)
assert norm(p(rr['reduced_scalar.ratio_node_squared']['terms']))==norm(add(add(v(541),mul(v(311),v(311)),-1),mul(v(312),v(312)),8))
assert norm(p(rr['scalar.ratio_node.consolidated_denominator']['terms']))==norm(add(add(mul(v(604),v(540)),mul(v(508),v(508)),-1),mul(r,v(539)),-1))
assert norm(p(rr['reduced_scalar.root']['terms']))==norm(add(add(mul(v(604),v(542)),mul(v(540),v(540)),-1),mul(r,v(541)),-1))
prev=r
for j,i in enumerate(range(600,605)):
    assert norm(p(rr[f'scalar.r_power_{2**(j+1)}.definition']['terms']))==norm(add(v(i),mul(prev,prev),-1));prev=v(i)
for name in br:
    if '.odd.' in name or name.startswith(('heightProduct.','detector','hybrid.')):assert rr[name]==br[name]
assert p(rr['anchor.translatedEquation']['terms'])=={(55,55):F(1),(56,56):F(6),(57,57):F(-2),(505,505):F(-3),(-1,57):F(-4)}
# Exact new scalar depth thresholds and the anchor margins, independent of ratios.
assert F(191,8)>23 and F(187,8)>23
assert F(5,24)*F(50331647,2)>2093966+7
assert 10*(7+2093966)<F(50331647,2)
assert 40**20>13
sos={}
for row in rr.values():
    q=norm(p(row['terms']));assert max(sum(i!=-1 for i in m) for m in q)<=2
    sos=add(sos,mul(q,q))
assert sos==p(read(D/'combined423-polynomial.json')['terms'])
assert (len(rc),len(rr),len(sos))==(423,392,6172)
assert {i for m in sos for i in m if i!=-1}==set(rc)
assert any(-1 not in m and abs(q)==1 for m,q in sos.items())
assert {m:q for m,q in sos.items() if m.count(-1)==2}=={(-1,-1,57,57):F(16)}
assert (-1,57,57) not in sos and (57,57) not in sos
assert max(abs(q.numerator).bit_length() for m,q in sos.items() if -1 not in m)<2048
assert max(abs(q) for m,q in sos.items() if m.count(-1)==1)<=48
paths=list(pins)+['inputs/composition431-review.md','inputs/identity-chart-review.md','inputs/primary437-review.md','inputs/scalar24-review.md']
result={'passed':True,'variables':423,'rows':392,'monomials':6172,'removedCoordinates':sorted(removed),'renamedCoordinates':len(renamed),'changedRows':len(changed),'deletedRows':len(deleted),'addedRows':len(added),'scope':'Independent full delta/metadata/incidence and SOS, actual H/V0 reconstruction including current rational-log output, unchanged scalar/anchor/odd-root/height/detector interfaces and exact depth/anchor inequalities. Mathematical composition review is separate prose.',
        'sourceSha256':{str(D/p):sha(D/p) for p in paths}}
(H/'review-composition423-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
