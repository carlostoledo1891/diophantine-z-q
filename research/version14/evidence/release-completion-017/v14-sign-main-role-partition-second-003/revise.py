from pathlib import Path
import json,hashlib,shutil
R=Path('work/source-risk-review-20261107');A=R/'v14-sign-main-role-partition-002';O=R/'v14-sign-main-role-partition-second-003'
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(x):return hashlib.sha256(x).hexdigest()
def wr(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for p in A.iterdir():
 if p.is_file() and p.name not in ['MANIFEST.json','prepare.py']:shutil.copyfile(p,O/p.name)
rows=rd(A/'INDEX.json');pending=rd(A/'PENDING.json');bindings=[]
trace=next(c for c in rd(R/'v14-dual-exponential-application-001/COMPONENTS.json') if c['use']['id']=='ACTIVE-THETA-DUAL-EXPONENTIAL-TRACE')
gauss=rd(R/'v14-quadratic-gauss-application-001/COMPONENTS.json')[0]
for row in rows:
 if row['location']['start_line']==13590:
  row['use_ids'].append(trace['use']['id']);row['reason']+=' The separately reviewed finite-trace input supplies exp-star/corestriction functoriality with the actual twisted endpoint W.'
  bindings.append(dict(index_id=row['id'],use_id=trace['use']['id'],use_sha256=trace['connection']['use_sha256'],actual_consumer_locations=trace['connection']['consumer_locations']))
for row in pending:
 if row['location']['start_line'] in [13627,13660]:
  row.update(status='reviewed',source_role='primitive_local_input',use_ids=[gauss['use']['id']],claim_ids=['V14-MAIN-POLYNOMIAL-DEFINITION'],reason='The independently reviewed finite-DFT proof supplies the primitive quadratic Gauss square and invariant-basis ratio in {1,-1,2,-2}; actual primitive character and signed-discriminant conventions remain explicit.')
  rows.append(row);bindings.append(dict(index_id=row['id'],use_id=gauss['use']['id'],use_sha256=gauss['connection']['use_sha256'],actual_consumer_locations=[l for l in gauss['connection']['consumer_locations'] if l['start_line']==row['location']['start_line']]))
wr('INDEX.json',sorted(rows,key=lambda r:r['location']['start_line']));wr('PENDING.json',[r for r in pending if r['location']['start_line']==13668]);wr('BINDINGS.json',bindings)
wr('DELTA.json',dict(changed_starts=[13590,13627,13660],trace_review_sha256='52fd84e34ca5b8d3360afbd121e12a82e3d7f07e11c8314a55e2d513e95d3f32',gauss_review_sha256='d829103a40e6b8d5010171ac6e2aacd67179f068bbf3da5b97f78413b08b621a',remaining_pending=[13668,13676]))
wr('MANIFEST.json',dict(files={p.name:dict(sha256=sha(p.read_bytes()),bytes=p.stat().st_size) for p in sorted(O.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}));print(sha((O/'MANIFEST.json').read_bytes()))
