"""Reproduce frozen427 by dropping the explicit V0 guard from frozen428."""
from pathlib import Path
import sys,json,copy,hashlib
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parents[1]));import verify494 as P
c=P.read(H/'certificate428.json');g=P.read(H/'candidate428-ir.json')
assert P.sha(H/'candidate428-ir.json')=='236e837094097aef4596a225f541347f314f7596511b75cbae09b722fa4a184d'
u=copy.deepcopy(g);u['coordinates']=[x for x in g['coordinates'] if x['id']!=c['guardCoordinate']];u['residuals']=[x for x in g['residuals'] if x['id']!=c['guardRow']]
def output(name,obj,expected):
 data=(json.dumps(obj,indent=2)+'\n').encode();assert hashlib.sha256(data.replace(b'\n',b'\r\n')).hexdigest()==expected or hashlib.sha256(data).hexdigest()==expected
 (H/name).write_text(data.decode())
output('candidate427-ir.json',u,'6e23d292a93d49037d63a72f4dddca33179404a9e8e4467397c168d3862a0ea4')
total={}
for row in u['residuals']:
 p=P.normalized(P.poly(row['terms']));total=P.add(total,P.mul(p,p))
terms=[{'sPower':m.count(-1),'monomial':[i for i in m if i!=-1],'coefficient':str(v)} for m,v in sorted(total.items())]
output('polynomial427.json',{'fixedParameter':u['fixedParameter'],'terms':terms},'256721badc6296a154da5d43fb9c1f67bfd2146bbb96b4b2d174113ffd9c2e84')
print('Reproduced candidate427 and polynomial427.')
