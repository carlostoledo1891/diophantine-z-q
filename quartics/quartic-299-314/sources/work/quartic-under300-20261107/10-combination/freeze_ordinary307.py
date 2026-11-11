from pathlib import Path
import hashlib,json
H=Path(__file__).resolve().parent;W=H.parents[1];O=H/'ordinary-reciprocal307';opt=W/'quartic-optimization-20261107'
def pin(p):return {'path':p.relative_to(W).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
source=opt/'reciprocal307-20261107'; chain=opt/'resume-elimination-20261107/ordinary-chains'
sources=[source/'candidate307-ir.json',source/'polynomial307.json',source/'CERTIFICATE.json',
 opt/'resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json',
 opt/'resume-elimination-20261107/exact319/candidate319-ir.json',chain/'REPORT.md',chain/'MANIFEST.json',
 opt/'resume-sol-review-ordinary-chains-20261107/REVIEW.md',opt/'resume-review-ordinary313-20261107/REVIEW.md']+[chain/str(i)/'candidate-ir.json' for i in [336,335,334]]
manifest={'status':'frozen ordinary307 author transport; source arithmetic and transport acceptance are separate',
 'pathBase':'work','files':[pin(p) for p in sorted(O.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'],
 'sources':[pin(p) for p in sources]}
raw=(json.dumps(manifest,indent=2)+'\n').encode();p=O/'MANIFEST.json'
if p.exists():assert p.read_bytes()==raw
else:p.write_bytes(raw)
print(json.dumps({'report':pin(O/'REPORT.md'),'manifest':pin(p),'verifier':pin(O/'verify.py')}))
sfile=H/'STATUS.json';s=json.loads(sfile.read_bytes())
entries=[{'variables':r['variables'],'residuals':r['residuals'],'monomials':r['monomials'],
 'maximumCoefficientBits':r['maxCoefficientBits'],'candidate':pin(O/str(r['variables'])/'candidate-ir.json'),
 'manifest':pin(p),'pathBase':'work','scope':'Ordinary lift of pinned reciprocal307; source arithmetic and independent finite transport acceptance pending.'}
 for r in json.loads((O/'SUMMARY.json').read_bytes())]
hashes={r['candidate']['sha256'] for r in entries};s['pending']=entries+[r for r in s.get('pending',[]) if r.get('candidate',{}).get('sha256') not in hashes]
sfile.write_text(json.dumps(s,indent=2)+'\n',encoding='utf-8')
