"""Check the exact historical F8 finite data; no arithmetic check is implied."""
import argparse,hashlib,json,sys
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--package',required=True,type=Path)
parser.add_argument('--repo',required=True,type=Path)
parser.add_argument('--report',type=Path)
args=parser.parse_args()
archive=args.package.resolve()
repo=args.repo.resolve()
sys.path.insert(0,str(archive))
from polynomial import instantiate,expand,EXPECTED
from formats import read_rows,read_expansion,row_bytes,sha

header,rows=read_rows(archive/'residuals.jsonl.gz')
derived,certificate=instantiate(archive)
assert rows==derived
assert certificate==json.loads((archive/'construction-certificate.json').read_bytes())
assert header==json.loads((archive/'counts.json').read_bytes())
table=expand(rows)
assert table==read_expansion(archive/'polynomial.expanded.txt.gz')
module_matches=[]
for p in sorted((archive/'modules').glob('*.json')):
    q=repo/'degree8-original/modules'/p.name
    assert p.read_bytes()==q.read_bytes()
    module_matches.append({'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
result={'status':'passed_exact_finite_check','scope':'Exact finite recursion from literal modules, every residual, construction certificate and full ordered-pair SOS expansion. Current repository modules match byte-for-byte. No archived producer rebuild, broader historical audit command or arithmetic theorem is checked.',**EXPECTED,'maximum_absolute_coefficient':str(EXPECTED['maximum_absolute_coefficient']),'total_variables':15672,'input_coordinate':0,'residual_rows_sha256':sha(row_bytes(rows)),'current_module_matches':module_matches}
if args.report:args.report.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','total_variables','residuals','monomials','degree']}))
