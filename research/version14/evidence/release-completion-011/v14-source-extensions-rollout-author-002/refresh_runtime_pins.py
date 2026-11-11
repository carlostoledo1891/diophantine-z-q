"""Produce a new binder preparation using actual committed controller bytes."""
import argparse, hashlib, json, pathlib, shutil, subprocess
HERE=pathlib.Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('controller',type=pathlib.Path);p.add_argument('predecessor',type=pathlib.Path);p.add_argument('output',type=pathlib.Path);a=p.parse_args()
    root=a.controller.resolve();targets=json.loads((HERE/'TARGETS.json').read_bytes());manifest_raw=(a.predecessor/'MANIFEST.json').read_bytes()
    if sha(manifest_raw)!='fc48a64230f558e75ab5f3ea78c58cd9b53dd43add55d8b306fb4e38db1a3a03':raise ValueError('wrong predecessor manifest')
    manifest=json.loads(manifest_raw)
    for name,row in manifest['files'].items():
        path=(a.predecessor/name).resolve()
        if not path.is_relative_to(a.predecessor.resolve()):raise ValueError('predecessor path escape')
        raw=path.read_bytes()
        if sha(raw)!=row['sha256'] or len(raw)!=row['bytes']:raise ValueError('changed predecessor member')
    pin_raw=(a.predecessor/'RUNTIME-PINS.json').read_bytes()
    if sha(pin_raw)!='4cf3249ea5c0016422f0979614eb2e449ea0f55917a1fdd7ea07f67e32bf1d4b':raise ValueError('wrong predecessor pins')
    old=json.loads(pin_raw)
    commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
    if commit==targets['baseline_commit']:raise ValueError('new reviewed controller commit required')
    subprocess.check_call(['git','merge-base','--is-ancestor',targets['baseline_commit'],commit],cwd=root)
    for row in targets['files']:
        raw=subprocess.check_output(['git','show',commit+':'+row['path']],cwd=root)
        if (root/row['path']).read_bytes()!=raw:raise ValueError('worktree differs from committed overlay')
        if sha(raw)!=row['after_sha256']:raise ValueError('committed overlay mismatch: '+row['path'])
    changes={r['path']:r for r in targets['files']}
    new=json.loads(json.dumps(old));new['commit']=commit
    for row in new['files']:
        raw=subprocess.check_output(['git','show',commit+':'+row['path']],cwd=root)
        expected=changes[row['path']]['after_sha256'] if row['path'] in changes else row['sha256']
        if (root/row['path']).read_bytes()!=raw:raise ValueError('worktree differs from committed runtime')
        if sha(raw)!=expected:raise ValueError('unreviewed runtime change: '+row['path'])
        row.update(sha256=sha(raw),bytes=len(raw))
    extra='adapter/test_source_extensions.py';raw=subprocess.check_output(['git','show',commit+':'+extra],cwd=root)
    if extra in {r['path'] for r in new['files']}:raise ValueError('duplicate new test')
    new['files'].append(dict(path=extra,sha256=sha(raw),bytes=len(raw)))
    if len({r['path'] for r in new['files']})!=len(new['files']):raise ValueError('duplicate runtime path')
    if a.output.exists():raise ValueError('successor output already exists')
    a.output.mkdir(parents=True)
    for name in manifest['files']:
        dest=a.output/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((a.predecessor/name).read_bytes())
    (a.output/'history').mkdir()
    (a.output/'history/PREDECESSOR-MANIFEST.json').write_bytes(manifest_raw)
    (a.output/'history/PREDECESSOR-README.md').write_bytes((a.predecessor/'README.md').read_bytes())
    (a.output/'README.md').write_text('Current runtime binding successor. RUNTIME-PINS.json binds the actual new controller commit. bind.py and its input templates remain byte-identical. Prior DELTA, transition, tests, freeze.py and prepare_templates.py are preserved history; do not rerun historical generators. Source proof profile, authenticated observations and final approvals remain separately required. No controller activation is claimed.\n',encoding='utf8')
    (a.output/'RUNTIME-PINS.json').write_text(json.dumps(new,indent=2)+'\n',encoding='utf8')
    transition=dict(schema='source-extension-runtime-transition/v1',old_commit=old['commit'],new_commit=commit,changed_runtime_paths=[r['path'] for r in old['files'] if r['path'] in changes],added_test=extra,scope='Byte binding only; no activation, accepted dossier, or authenticated receipt selected.')
    (a.output/'SOURCE-EXTENSION-TRANSITION.json').write_text(json.dumps(transition,indent=2)+'\n',encoding='utf8')
    members={}
    for path in sorted(a.output.rglob('*')):
        if path.is_file():
            raw=path.read_bytes();members[path.relative_to(a.output).as_posix()]=dict(sha256=sha(raw),bytes=len(raw))
    (a.output/'MANIFEST.json').write_text(json.dumps(dict(schema='v14-controller-preparation-manifest/v1',author='/root/v14_h6_coverage',status='actual commit-bound proposal; independent review required',files=members),indent=2)+'\n',encoding='utf8')
    print(json.dumps(transition))
if __name__=='__main__':main()
