"""Run existing finite checks in a fresh copy, leaving the selected snapshot untouched."""
import argparse,json,shutil,subprocess,sys
from pathlib import Path
from check_snapshot import check
ap=argparse.ArgumentParser();ap.add_argument('--repository',required=True);ap.add_argument('--manifest-sha256',required=True);ap.add_argument('--scratch',required=True);ap.add_argument('--kind',choices=['314','233','huge'],required=True)
a=ap.parse_args();repo=Path(a.repository).resolve();out=Path(a.scratch).resolve()
check(repo,a.manifest_sha256)
if out==repo or repo in out.parents or out in repo.parents: raise ValueError('scratch overlaps repository')
out.mkdir(parents=True,exist_ok=False)
if a.kind=='314':
    rel=Path('quartics/quartic-299-314');shutil.copytree(repo/rel,out/rel)
    script=rel/'verify_lineage.py';args=[]
elif a.kind=='233':
    rel=Path('work/quartic238-optimization-20261110/linear-lucas')
    for name in ['reference233-014','reference233-sparse-015','reference235-011','reference235-sparse-012']: shutil.copytree(repo/rel/name,out/rel/name)
    script=rel/'reference233-sparse-015/verify.py';args=[]
else:
    shutil.copytree(repo/'construction',out/'construction');(out/'scripts').mkdir()
    shutil.copy2(repo/'scripts/check_construction.py',out/'scripts/check_construction.py')
    script=Path('scripts/check_construction.py');args=['--report','build/construction-checks.json']
result=subprocess.run([sys.executable,'-B',str(script),*args],cwd=out,capture_output=True,text=True,timeout=1800)
(out/'stdout.txt').write_text(result.stdout);(out/'stderr.txt').write_text(result.stderr)
if result.returncode: raise RuntimeError('finite verifier failed; retained scratch logs')
if a.kind=='233':
    for name in ['INVERSE-MAPS.json','VERIFICATION.json']:
        if (out/rel/'reference233-sparse-015'/name).read_bytes()!=(repo/rel/'reference233-sparse-015'/name).read_bytes(): raise ValueError('replayed output differs: '+name)
check(repo,a.manifest_sha256)
print(json.dumps({'kind':a.kind,'exit_code':0,'scope':'existing finite verifier only','scratch':str(out)}))
