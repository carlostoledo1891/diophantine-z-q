from pathlib import Path
import hashlib,json

base=Path(__file__).resolve().parents[3]
target=base/'work/source-risk-review-20261107/ct-salberger-cubic-theta-001'
out=Path(__file__).resolve().parent
sha=lambda b: hashlib.sha256(b).hexdigest()
manifest=json.loads((target/'MANIFEST.json').read_text(encoding='utf-8-sig'))
assert sha((target/'MANIFEST.json').read_bytes())=='33ea0b92e5c06740ea49afbe5ce16baa7e959828bfae15b2c510afda9290ed79'
failures=[]
for row in manifest['files']:
 p=target/row['path']; b=p.read_bytes()
 if sha(b)!=row['sha256'] or len(b)!=row['bytes']: failures.append(row['path'])
edits=json.loads((target/'EDITS.json').read_text(encoding='utf-8-sig'))
old=(target/'previous/quartic_v14.tex').read_bytes()
new=(target/'candidate/manuscripts/quartic_v14.tex').read_bytes()
assert sha(old)==manifest['base_sha256'] and sha(new)==manifest['candidate_sha256']
replay=old
for e in sorted(edits['edits'],key=lambda x:x['byte_offset'],reverse=True):
 a,b=bytes.fromhex(e['old_hex']),bytes.fromhex(e['new_hex']); at=e['byte_offset']
 assert sha(a)==e['old_sha256'] and sha(b)==e['new_sha256']
 assert replay[at:at+len(a)]==a
 replay=replay[:at]+b+replay[at+len(a):]
assert replay==new
unchanged=json.loads((target/'UNCHANGED-CONSUMERS.json').read_text())
ol,nl=old.splitlines(keepends=True),new.splitlines(keepends=True)
for r in unchanged:
 a=b''.join(ol[r['base_start']-1:r['base_end']]); b=b''.join(nl[r['candidate_start']-1:r['candidate_end']])
 assert a==b and sha(a)==r['sha256']
proof=(target/'PROOF.md').read_bytes()
assert proof==(target/'candidate/research/version14/proofs/cubic-unirationality-v1/PROOF.md').read_bytes()
payload=list((target/'candidate').rglob('*'))
external=[str(p.relative_to(target)) for p in payload if p.suffix.lower() in {'.pdf','.png','.jpg','.jpeg'}]
assert not failures and not external
result={'manifest_members_checked':len(manifest['files']),'manifest_failures':failures,'exact_edit_replay':True,'edit_count':len(edits['edits']),'unchanged_contexts':len(unchanged),'proof_payload_identical':True,'external_media_in_candidate':external,'source_uses':len(json.loads((target/'SOURCE-USES.json').read_text())),'comparison_count':len(json.loads((target/'APPLICATION.json').read_text())['comparisons']),'base_sha256':sha(old),'candidate_sha256':sha(new),'proof_sha256':sha(proof)}
(out/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
