import difflib,pathlib,json
p=pathlib.Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/astra-only-review-policy-20261109/')
d=pathlib.Path(r'C:/Users/glaze/Documents/Codex/2026-11-02/lo/work/protocol-ruleset-20261107/deployment-repository/')
m=json.loads((p/'MANIFEST.json').read_text())
out=[]
for f in m['files']:
 r=f['path']; old=(d/r).read_text().splitlines(True) if (d/r).exists() else []; new=(p/'overlay'/r).read_text().splitlines(True)
 out.extend(difflib.unified_diff(old,new,fromfile='a/'+r,tofile='b/'+r))
(p/'PATCH.diff').write_text(''.join(out))
