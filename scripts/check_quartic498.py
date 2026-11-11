"""Rebuild the 498/514-variable quartics and verify their public downloads."""
from pathlib import Path
import json,subprocess,sys,shutil
ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/'quartics/quartic-498-514'
def main():
    out=ROOT/'build/quartic-498';out.mkdir(parents=True,exist_ok=True)
    try:
        subprocess.run([sys.executable,'-B',str(PACKET/'verify_portable.py'),'--repo',str(ROOT)],check=True,cwd=ROOT)
    finally:
        for log in (PACKET/'build').glob('*.log'):
            shutil.copyfile(log,out/log.name)
    copies={
        'quartic-498-symbolic-coefficients.json':'quartic-498-symbolic-coefficients.json',
        'quartic-498-symbolic-coefficients.txt':'quartic-498-symbolic-coefficients.txt',
        'quartic-514-ordinary-coefficients.txt':'quartic-514-fully-expanded.txt',
    }
    for source,download in copies.items():
        if (PACKET/source).read_bytes()!=(ROOT/'quartics'/download).read_bytes():
            raise ValueError('Public coefficient download differs: '+download)
    result=json.loads((PACKET/'build/VERIFIED.json').read_bytes())
    (out/'verified.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: 498/514 source reconstruction, certificates, coefficients and public downloads.')
if __name__=='__main__':main()
