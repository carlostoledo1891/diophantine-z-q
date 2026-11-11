"""Instantiate the explicit sparse coefficient table at a chosen nonnegative N."""
import argparse,json,sys
if hasattr(sys,"set_int_max_str_digits"): sys.set_int_max_str_digits(0)
from pathlib import Path
from verify import check,terms,ROOT
p=argparse.ArgumentParser();p.add_argument('--N',type=int,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
if args.N<0: p.error('N must be nonnegative')
check('sparse')
source=json.loads((ROOT/'tables/sparse222-polynomial.json').read_bytes()); A=149**(2*args.N+1); result={}
for (power,m),c in terms(source['terms']).items(): result[m]=result.get(m,0)+int(c)*A**power
payload={'variables':222,'inputCoordinate':1,'N':args.N,'A_N':str(A),'defining_threshold_certified':False,'limitation':'The defining theorem requires N >= an ineffective N0; choosing N does not certify this premise.','terms':[{'monomial':list(m),'coefficient':str(c)} for m,c in sorted(result.items()) if c]}
with args.output.open('x',encoding='utf8') as f: json.dump(payload,f,indent=2);f.write('\n')
