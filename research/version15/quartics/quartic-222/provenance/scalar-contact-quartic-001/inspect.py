from fractions import Fraction as F
import json,sys
r=json.load(open(sys.argv[1]));d={x['id']:x for x in r['residuals']}
for t in [0,1,2]:
 v={63:F(t)}
 for rid,out in [(70,121),(71,122),(72,123)]:
  rest=F(0);co=F(0)
  for z in d[rid]['terms']:
   if z['monomial']==[out]:co+=F(z['coefficient']);continue
   y=F(z['coefficient'])
   for i in z['monomial']:y*=v[i]
   rest+=y
  v[out]=-rest/co
 beta=51*t+2504;r4=beta*(beta-1)*(beta-2401)*(32*beta+343)
 print(t,str(v[123]/r4),2*beta-1)
