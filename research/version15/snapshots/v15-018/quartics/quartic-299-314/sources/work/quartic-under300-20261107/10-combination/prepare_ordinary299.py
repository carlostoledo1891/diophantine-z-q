"""Prepare new source-pinned ordinary companions of accepted299-r2."""
from pathlib import Path
import json,subprocess,sys
H=Path(__file__).resolve().parent;O=H/'ordinary-reciprocal299';O.mkdir(exist_ok=True)
def adapt(s):
    return (s.replace('reciprocal307-20261107','resume-elimination-20261107/reciprocal299-r2')
        .replace('candidate307-ir.json','candidate299-ir.json').replace('polynomial307.json','polynomial299.json')
        .replace('0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1','8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815')
        .replace('90256d39e58b84a00b06003a4457ed56c1b282cd80a0c21c882a93411c660106','e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c')
        .replace('reciprocal307','reciprocal299'))
def fresh(p,t):
    b=t.encode()
    if p.exists():assert p.read_bytes()==b,p
    else:p.write_bytes(b)
b=adapt((H/'ordinary-reciprocal307/build.py').read_text()).replace('size=308+count','size=300+count')
fresh(O/'build.py',b);subprocess.run([sys.executable,str(O/'build.py')],check=True)
summary=json.loads((O/'SUMMARY.json').read_bytes())
v=adapt((H/'ordinary-reciprocal307/verify.py').read_text())
i=v.index('pins=');j=v.index('\ndef poly(',i)
v=v[:i]+'pins='+repr({r['variables']:(r['candidateSha256'],r['polynomialSha256'],r['textSha256']) for r in summary})+'\nchains={316:[513]*9+[2]+[0]*6,315:[1025]*10+[2]+[0]*4,314:[2049]+[2048]*11+[0,0]}\n'+v[j:]
v=v.replace('size-12,{324: 6486, 323: 6483, 322: 6480}[size]','size-20,'+repr({r['variables']:r['monomials'] for r in summary})+'[size]')
fresh(O/'verify.py',v);subprocess.run([sys.executable,str(O/'verify.py')],check=True)
check=adapt((H/'ordinary-reciprocal307/check_source.py').read_text()).replace("==295 and len(cc)==len(ir['coordinates'])==307","==279 and len(cc)==len(ir['coordinates'])==299")
fresh(O/'check_source.py',check);subprocess.run([sys.executable,str(O/'check_source.py')],check=True)
