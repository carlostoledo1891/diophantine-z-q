from pathlib import Path
import hashlib,json
H=Path(__file__).resolve().parent;W=H.parents[1];O=H/'ordinary-reciprocal299';opt=W/'quartic-optimization-20261107'
def pin(p):return {'path':p.relative_to(W).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
source=opt/'resume-elimination-20261107/reciprocal299-r2';chain=opt/'resume-elimination-20261107/ordinary-chains'
sources=[source/'candidate299-ir.json',source/'polynomial299.json',source/'REPORT.md',source/'MANIFEST.json',H/'review-reciprocal299/REVIEW.md',
 opt/'resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json',opt/'resume-elimination-20261107/exact319/candidate319-ir.json',
 chain/'REPORT.md',chain/'MANIFEST.json',opt/'resume-sol-review-ordinary-chains-20261107/REVIEW.md']+[chain/str(i)/'candidate-ir.json' for i in [336,335,334]]
manifest={'status':'frozen ordinary299 author transport; independent finite transport review pending','pathBase':'work',
 'files':[pin(p) for p in sorted(O.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'],'sources':[pin(p) for p in sources]}
raw=(json.dumps(manifest,indent=2)+'\n').encode();p=O/'MANIFEST.json'
if p.exists():assert p.read_bytes()==raw
else:p.write_bytes(raw)
print(json.dumps({'report':pin(O/'REPORT.md'),'manifest':pin(p),'verifier':pin(O/'verify.py')}))
sfile=H/'STATUS.json';s=json.loads(sfile.read_bytes())
if s['currentAccepted']['candidate']['sha256']!='8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815':
 s.setdefault('priorAccepted',[]).append(s['currentAccepted'])
 s['currentAccepted']={'variables':299,'witnesses':298,'residuals':279,'monomials':6630,'coefficientPowerEntries':6630,
 'maximumCoefficient':'186624*3^(2^26)','candidate':pin(source/'candidate299-ir.json'),'report':pin(source/'REPORT.md'),
 'review':pin(H/'review-reciprocal299/REVIEW.md'),'pathBase':'work','scope':'Independent full299-r2 construction and input-projection arithmetic review; rejected initial299 excluded.'}
entries=[{'variables':r['variables'],'residuals':r['residuals'],'monomials':r['monomials'],'maximumCoefficientBits':r['maxCoefficientBits'],
 'candidate':pin(O/str(r['variables'])/'candidate-ir.json'),'manifest':pin(p),'pathBase':'work','scope':'Ordinary exact lift of accepted299-r2; independent finite transport review pending.'}
 for r in json.loads((O/'SUMMARY.json').read_bytes())]
hashes={r['candidate']['sha256'] for r in entries};s['pending']=entries+[r for r in s.get('pending',[]) if r.get('candidate',{}).get('sha256') not in hashes]
sfile.write_text(json.dumps(s,indent=2)+'\n',encoding='utf-8')
