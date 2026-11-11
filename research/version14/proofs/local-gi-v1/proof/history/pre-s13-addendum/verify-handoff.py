"""Verify only the explicitly reduced cumulative GI directory."""
from pathlib import Path,PurePosixPath
import hashlib,json,sys
EXPECTED='2a3681bc015e4f0ce73e18fc4ea62cefac31ed9ff9bf2f087841b4589f0e14ad'
H=lambda b:hashlib.sha256(b).hexdigest()
def need(ok,msg):
 if not ok:raise ValueError(msg)
def decode(b):
 def pairs(items):
  d={}
  for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
  return d
 return json.loads(b,object_pairs_hook=pairs)
def safe(s):
 need(type(s) is str and s and '\\' not in s and ':' not in s,'unsafe path')
 p=PurePosixPath(s);need(not p.is_absolute() and '..' not in p.parts and p.as_posix()==s,'unsafe path');return s
def run():
 script=Path(__file__);need(not script.is_symlink() and not script.parent.is_symlink(),'symlinked verifier/root');root=script.resolve().parent
 raw=(root/'CUMULATIVE-HANDOFF.json').read_bytes();need(H(raw)==EXPECTED,'handoff manifest changed');m=decode(raw);need(m['schema']=='v14-gi-cumulative-handoff/v1','schema')
 def check(row):
  name=safe(row['path']);p=root/name;need(p.is_file() and not p.is_symlink(),'missing/symlink: '+name);b=p.read_bytes();need(len(b)==row['bytes'] and H(b)==row['sha256'],'changed: '+name);return b
 full=decode(check(m['full_package_manifest']));original={r['path']:r for r in full['files']};need(len(original)==len(full['files'])==m['original_members'],'full manifest duplicate/count')
 keep={r['path']:r for r in m['retained']};omit={r['path']:r for r in m['excluded']};need(len(keep)==len(m['retained']) and len(omit)==len(m['excluded']),'duplicate partition');need(not(set(keep)&set(omit)) and set(keep)|set(omit)==set(original),'partition')
 for name,row in {**keep,**omit}.items():need({k:row[k] for k in ('path','sha256','bytes')}==original[name],'partition pin mismatch')
 for row in omit.values():need(row['retained_source']['path'] in keep and row['retained_source']==keep[row['retained_source']['path']],'missing source counterpart')
 expected=set(keep)|{m['full_package_manifest']['path'],'CUMULATIVE-HANDOFF.json','verify-handoff.py'}|{r['path'] for r in m['added_text']}
 seen=set()
 for p in root.rglob('*'):
  need(not p.is_symlink(),'symlink in handoff')
  if p.is_file():seen.add(p.relative_to(root).as_posix())
 need(seen==expected,'missing/extra files: '+repr(sorted(seen^expected)))
 for row in list(keep.values())+m['added_text']:check(row)
 return {'scope':'reduced cumulative GI only; not full package or mathematical/gate acceptance','retained_checked':len(keep),'excluded_full_manifest_members':len(omit),'exact_file_set':True,'failures':[]}
if __name__=='__main__':
 try:result=run()
 except (ValueError,OSError,KeyError,TypeError) as e:print(json.dumps({'scope':'reduced cumulative GI','failure':str(e)}));sys.exit(1)
 print(json.dumps(result,indent=2))
