from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;W=H.parents[1]
R=W/'quartic-optimization-20261107/resume-review-transports314-20261107/REVIEW.md'
assert hashlib.sha256(R.read_bytes()).hexdigest()=='abc780609bf1b9a65100608eac4bec936f8844ea9b91fdeed973b24241c0efa7'
def pin(p):return {'path':p.relative_to(W).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pathBase':'work'}
p=H/'STATUS.json';s=json.loads(p.read_bytes())
target=H/'sparse-shared314/candidate314-ir.json'
if s['currentAccepted']['candidate']['sha256']!=pin(target)['sha256']:
 s.setdefault('priorAccepted',[]).append(s['currentAccepted'])
 s['currentAccepted']={'variables':314,'witnesses':313,'residuals':283,'monomials':6074,'coefficientPowerEntries':6077,'maximumCoefficient':'186624*3^(2^26)+64','candidate':pin(target),'report':pin(H/'sparse-shared314/REPORT.md'),'review':pin(R),'scope':'Accepted shared314 followed by independently reviewed exact sparse Lucas transport.'}
hashes={pin(target)['sha256']}
accepted=[]
for r in json.loads((H/'ordinary-sparse-shared314/SUMMARY.json').read_bytes()):
 hashes.add(r['candidateSha256'])
 accepted.append({'variables':r['variables'],'residuals':r['residuals'],'monomials':r['monomials'],'maximumCoefficientBits':r['maxCoefficientBits'],'candidate':pin(H/f"ordinary-sparse-shared314/{r['variables']}/candidate-ir.json"),'review':pin(R),'scope':'Independently accepted exact ordinary lift of sparse shared314.'})
s['acceptedOrdinaryShared314']=accepted
s['pending']=[r for r in s['pending'] if r.get('candidate',{}).get('sha256') not in hashes]
p.write_text(json.dumps(s,indent=2)+'\n',encoding='utf-8')
print('Recorded accepted sparse314 and ordinary331/330/329; author packets unchanged.')
