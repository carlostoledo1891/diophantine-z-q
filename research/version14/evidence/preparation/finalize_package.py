from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;R=H.parents[1];P=H/'quartic-299-314';S=P/'sources';O=R/'work/quartic-optimization-20261107'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,o):p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def copy(src,dest):
 dest.parent.mkdir(parents=True,exist_ok=True);b=src.read_bytes()
 if dest.exists():assert dest.read_bytes()==b,dest
 else:dest.write_bytes(b)
manifest=json.loads((P/'SOURCE-MANIFEST.json').read_bytes())
def archive(src):
 rel=src.relative_to(R);copy(src,S/rel);manifest[rel.as_posix()]={'sha256':sha(src),'bytes':src.stat().st_size}
reviewdirs=['resume-review-inventory-r6-01','resume-review-v14-compact-01']
for d in reviewdirs:
 for p in (O/d).iterdir():
  if p.is_file():archive(p)
art=json.loads((P/'ARTIFACTS.json').read_bytes())
for name in list(art['files'])+['ARTIFACTS.json']:archive(P/name)
reviews={
 'mathematical-review.md':R/'work/quartic-under300-20261107/10-combination/review-reciprocal299/REVIEW.md',
 's-extension-review.md':O/'resume-depth-20261107/review-s299/REVIEW.md',
 'ordinary-review.md':O/'resume-depth-20261107/review-ordinary299/REVIEW.md',
 'artifact-review.md':O/'resume-review-v14-compact-01/REVIEW.md',
 'inventory-review.md':O/'resume-review-inventory-r6-01/REVIEW.md'}
for name,src in reviews.items():copy(src,P/'reviews'/name);archive(src)
dump(P/'SOURCE-MANIFEST.json',manifest)
plan=json.loads((P/'VERIFICATION-PLAN.json').read_bytes())
for d in reviewdirs:
 step={'script':'work/quartic-optimization-20261107/'+d+'/check.py','args':[]}
 if step not in plan['steps']:plan['steps'].append(step)
dump(P/'VERIFICATION-PLAN.json',plan)
dump(P/'ACCEPTANCE.json',{'scope':'Exact299-r2 mathematical construction, ordinary lift, compact serialization and R6 structural inventory have separate independent acceptances. Packaging wrapper and publication remain separate review scopes.',
 'symbolicCandidateSha256':'8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815',
 'ordinaryCandidateSha256':'02b8b6a8b13a566ef520c7a65ec58fd6e63bafa9d7d447e323864b1bae29a5f7',
 'artifactManifestSha256':sha(P/'ARTIFACTS.json'),
 'reviews':{name:{'sha256':sha(src),'bytes':src.stat().st_size,'originalPath':src.relative_to(R).as_posix()} for name,src in reviews.items()},
 'rejectedCandidateSha256':'ab42bc98539b072ff99f5b6e1a70a1867735175612782b26b2fba169b47581fd',
 'rejectedHistoryPath':'sources/work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299',
 'inventoryPath':'sources/work/quartic-optimization-20261107/resume-release-inventory-20261107-r6',
 'inventoryManifestSha256':'207e7ca6cca93a79fabc19db02ee5c8d2a3d9370d0ec7f19d2847d3bb6e02ae7'})
print(json.dumps({'sourceFiles':len(manifest),'sourceBytes':sum(v['bytes'] for v in manifest.values()),'replayStages':len(plan['steps'])}))
