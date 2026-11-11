from pathlib import Path
import hashlib,json,subprocess,sys
H=Path(__file__).resolve().parent;O=H/'ordinary-anchor313';O.mkdir(exist_ok=True)
base="H.parents[2]/'quartic-optimization-20261107/resume-anchor-shared314-20261107/anchor-gamma313/"
def adapt(s):
 return s.replace("H.parent/'sparse-shared314/",base).replace('candidate314-ir.json','candidate313-ir.json').replace('polynomial314.json','polynomial313.json').replace('aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382','6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a').replace('1fc9ba1e03e5134bd3173f22d80ecc5c29838996c1cb58839264844f6358d77e','d3eaca34d9b5bb3f24593ca601f30f22c430f4b71e47e9f607a050501fc8d63d').replace('sparse-shared314','anchor-gamma313')
def fresh(p,t):
 b=t.encode()
 if p.exists():assert p.read_bytes()==b,p
 else:p.write_bytes(b)
b=adapt((H/'ordinary-sparse-shared314/build.py').read_text()).replace('size=315+count','size=314+count')
fresh(O/'build.py',b);subprocess.run([sys.executable,str(O/'build.py')],check=True)
summary=json.loads((O/'SUMMARY.json').read_bytes())
v=adapt((H/'ordinary-sparse-shared314/verify.py').read_text())
i=v.index('pins=');j=v.index('\ndef poly(',i)
v=v[:i]+'pins='+repr({r['variables']:(r['candidateSha256'],r['polynomialSha256'],r['textSha256']) for r in summary})+'\nchains={330:[513]*9+[2]+[0]*6,329:[1025]*10+[2]+[0]*4,328:[2049]+[2048]*11+[0,0]}\n'+v[j:]
v=v.replace('size-31,{331: 6122, 330: 6119, 329: 6116}[size]','size-30,'+repr({r['variables']:r['monomials'] for r in summary})+'[size]')
fresh(O/'verify.py',v);subprocess.run([sys.executable,str(O/'verify.py')],check=True)
