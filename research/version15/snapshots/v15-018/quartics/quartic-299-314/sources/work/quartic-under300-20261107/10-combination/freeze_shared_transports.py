from pathlib import Path
import hashlib,json
H=Path(__file__).resolve().parent;W=H.parents[1]
def pin(p):return {'path':p.relative_to(W).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
def write(p,obj):
 raw=(json.dumps(obj,indent=2)+'\n').encode()
 if p.exists():assert p.read_bytes()==raw,p
 else:p.write_bytes(raw)
opt=W/'quartic-optimization-20261107'
shared=opt/'resume-elimination-20261107/shared-scale314'
common=[shared/'candidate314-ir.json',shared/'polynomial314.json',shared/'REPORT.md',opt/'resume-depth-20261107/shared314/PROOF.md',opt/'resume-review-shared314-20261107/REVIEW.md',H/'review-shared314/REVIEW.md']
sparse=H/'sparse-shared314';ordinary=H/'ordinary-sparse-shared314'
sources=common+[H/'sparse315/candidate315-ir.json',H/'sparse315/REPORT.md',opt/'resume-sol-review-sparse315-20261107/REVIEW.md']
write(sparse/'MANIFEST.json',{'status':'frozen author composition; independent review pending','pathBase':'work','files':[pin(p) for p in sorted(sparse.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'],'sources':[pin(p) for p in sources]})
chain=opt/'resume-elimination-20261107/ordinary-chains'
sources=[sparse/'candidate314-ir.json',sparse/'polynomial314.json',sparse/'REPORT.md',sparse/'MANIFEST.json',opt/'resume-elimination-20261107/exact319/candidate319-ir.json',chain/'REPORT.md',chain/'MANIFEST.json',opt/'resume-sol-review-ordinary-chains-20261107/REVIEW.md']+[chain/str(size)/'candidate-ir.json' for size in [336,335,334]]
write(ordinary/'MANIFEST.json',{'status':'frozen author composition; independent review pending','pathBase':'work','files':[pin(p) for p in sorted(ordinary.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'],'sources':[pin(p) for p in sources]})
for folder in [sparse,ordinary]:print(json.dumps({'report':pin(folder/'REPORT.md'),'manifest':pin(folder/'MANIFEST.json')}))
statuspath=H/'STATUS.json';status=json.loads(statuspath.read_bytes())
if status['currentAccepted']['candidate']['sha256']!='7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5':
 status.setdefault('priorAccepted',[]).append(status['currentAccepted'])
 status['currentAccepted']={'variables':314,'witnesses':313,'residuals':283,'monomials':6135,'coefficientPowerEntries':6138,'maximumCoefficient':'186624*3^(2^26)+64','candidate':pin(shared/'candidate314-ir.json'),'report':pin(shared/'REPORT.md'),'reviews':[pin(opt/'resume-review-shared314-20261107/REVIEW.md'),pin(H/'review-shared314/REVIEW.md')],'scope':'Shared-scale314 new arithmetic accepted by05 and finite construction accepted by10; inherited premises retained.'}
pending=[{'variables':314,'candidate':pin(sparse/'candidate314-ir.json'),'manifest':pin(sparse/'MANIFEST.json'),'scope':'Sparse Lucas exact composition; independent review pending.'}]
for item in json.loads((ordinary/'SUMMARY.json').read_bytes()):
 pending.append({'variables':item['variables'],'candidate':pin(ordinary/str(item['variables'])/'candidate-ir.json'),'manifest':pin(ordinary/'MANIFEST.json'),'monomials':item['monomials'],'maximumCoefficientBits':item['maxCoefficientBits'],'scope':'Ordinary companion of sparse shared314; independent composition review pending.'})
oldpending=status.get('pending',[]);hashes={p['candidate']['sha256'] for p in pending}
status['pending']=pending+[p for p in oldpending if p.get('candidate',{}).get('sha256') not in hashes]
statuspath.write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')
