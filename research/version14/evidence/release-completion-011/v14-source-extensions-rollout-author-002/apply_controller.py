"""Apply only the reviewed local controller overlay; no commit or network calls."""
import argparse, hashlib, json, pathlib, subprocess
HERE=pathlib.Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('controller',type=pathlib.Path);p.add_argument('--apply',action='store_true');a=p.parse_args()
    root=a.controller.resolve();spec=json.loads((HERE/'TARGETS.json').read_bytes())
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
    if head!=spec['baseline_commit']:raise ValueError('controller baseline commit changed')
    for row in spec['files']:
        target=(root/row['path']).resolve();source=HERE/'controller-overlay'/row['path']
        if not target.is_relative_to(root):raise ValueError('target outside controller')
        actual=sha(target.read_bytes()) if target.exists() else None
        if actual!=row['before_sha256']:raise ValueError('target changed: '+row['path'])
        if sha(source.read_bytes())!=row['after_sha256']:raise ValueError('overlay changed: '+row['path'])
    for row in spec['unchanged_pins']:
        if sha((root/row['path']).read_bytes())!=row['sha256']:raise ValueError('protected input changed')
    if a.apply:
        for row in spec['files']:
            target=root/row['path'];target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes((HERE/'controller-overlay'/row['path']).read_bytes())
    print(json.dumps({'verified':len(spec['files']),'applied':a.apply,'network_operations':0}))
if __name__=='__main__':main()
