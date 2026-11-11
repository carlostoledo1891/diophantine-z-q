"""Prepare new, source-pinned ordinary lifts; never alter source packets."""
from pathlib import Path
import json, subprocess, sys
H=Path(__file__).resolve().parent
O=H/'ordinary-reciprocal307'
O.mkdir(exist_ok=True)
def adapt(s):
    return (s.replace('resume-anchor-shared314-20261107/anchor-gamma313','reciprocal307-20261107')
        .replace('candidate313-ir.json','candidate307-ir.json').replace('polynomial313.json','polynomial307.json')
        .replace('6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a','0b94aaf7669b3fe89cdf48f4718750991cfea4dd289695543f29b0cd533f29a1')
        .replace('d3eaca34d9b5bb3f24593ca601f30f22c430f4b71e47e9f607a050501fc8d63d','90256d39e58b84a00b06003a4457ed56c1b282cd80a0c21c882a93411c660106')
        .replace('anchor-gamma313','reciprocal307'))
def fresh(p,t):
    b=t.encode()
    if p.exists(): assert p.read_bytes()==b,p
    else: p.write_bytes(b)
b=adapt((H/'ordinary-anchor313/build.py').read_text()).replace('size=314+count','size=308+count')
fresh(O/'build.py',b)
subprocess.run([sys.executable,str(O/'build.py')],check=True)
summary=json.loads((O/'SUMMARY.json').read_bytes())
v=adapt((H/'ordinary-anchor313/verify.py').read_text())
i=v.index('pins=');j=v.index('\ndef poly(',i)
v=v[:i]+'pins='+repr({r['variables']:(r['candidateSha256'],r['polynomialSha256'],r['textSha256']) for r in summary})+'\nchains={324:[513]*9+[2]+[0]*6,323:[1025]*10+[2]+[0]*4,322:[2049]+[2048]*11+[0,0]}\n'+v[j:]
v=v.replace('size-30,{330: 6121, 329: 6118, 328: 6115}[size]','size-12,'+repr({r['variables']:r['monomials'] for r in summary})+'[size]')
fresh(O/'verify.py',v)
subprocess.run([sys.executable,str(O/'verify.py')],check=True)
