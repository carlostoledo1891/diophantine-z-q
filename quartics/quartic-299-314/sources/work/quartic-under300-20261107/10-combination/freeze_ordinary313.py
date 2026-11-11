from pathlib import Path
import hashlib,json
H=Path(__file__).resolve().parent;W=H.parents[1];O=H/'ordinary-anchor313';opt=W/'quartic-optimization-20261107'
def pin(p):return {'path':p.relative_to(W).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
source=opt/'resume-anchor-shared314-20261107/anchor-gamma313'
chain=opt/'resume-elimination-20261107/ordinary-chains'
sources=[source/'candidate313-ir.json',source/'polynomial313.json',source/'REPORT.md',source/'MANIFEST.json',H/'review-anchor-gamma313/REVIEW.md',opt/'resume-elimination-20261107/exact319/candidate319-ir.json',chain/'REPORT.md',chain/'MANIFEST.json',opt/'resume-sol-review-ordinary-chains-20261107/REVIEW.md',opt/'resume-review-transports314-20261107/REVIEW.md']+[chain/str(i)/'candidate-ir.json' for i in [336,335,334]]
manifest={'status':'frozen ordinary313 author composition; independent review pending','pathBase':'work','files':[pin(p) for p in sorted(O.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'],'sources':[pin(p) for p in sources]}
raw=(json.dumps(manifest,indent=2)+'\n').encode();p=O/'MANIFEST.json'
if p.exists():assert p.read_bytes()==raw
else:p.write_bytes(raw)
print(json.dumps({'report':pin(O/'REPORT.md'),'manifest':pin(p)}))
sfile=H/'STATUS.json';s=json.loads(sfile.read_bytes())
if s['currentAccepted']['candidate']['sha256']!='6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a':
 s.setdefault('priorAccepted',[]).append(s['currentAccepted'])
 s['currentAccepted']={'variables':313,'witnesses':312,'residuals':283,'monomials':6073,'coefficientPowerEntries':6076,'maximumCoefficient':'186624*3^(2^26)+64','candidate':pin(source/'candidate313-ir.json'),'report':pin(source/'REPORT.md'),'review':pin(H/'review-anchor-gamma313/REVIEW.md'),'pathBase':'work','scope':'Independent acceptance of new anchor/gamma approximation and complete313 construction.'}
entries=[{'variables':r['variables'],'monomials':r['monomials'],'maximumCoefficientBits':r['maxCoefficientBits'],'candidate':pin(O/str(r['variables'])/'candidate-ir.json'),'manifest':pin(O/'MANIFEST.json'),'pathBase':'work','scope':'Ordinary exact lift of accepted313; independent composition review pending.'} for r in json.loads((O/'SUMMARY.json').read_bytes())]
hashes={r['candidate']['sha256'] for r in entries};s['pending']=entries+[r for r in s['pending'] if r.get('candidate',{}).get('sha256') not in hashes]
s['latestCrossInterfaceStudy']={'report':pin(H/'cross-interface313/REPORT.md'),'checks':pin(H/'cross-interface313/CHECKS.json'),'scope':'New313 boundary only; no symbolic gain claimed.'}
sfile.write_text(json.dumps(s,indent=2)+'\n',encoding='utf-8')
