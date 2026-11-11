"""Read-only replay of the packaged checker; write only this proposal's report."""
import argparse,importlib.util,json
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repo',required=True,type=Path)
parser.add_argument('--report',type=Path)
args=parser.parse_args()
repo=args.repo.resolve()
package=repo/'quartics'/'quartic-4973'
spec=importlib.util.spec_from_file_location('historical_4973_checker',package/'verify_certificate.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
result=module.verify(package,write_report=False)
if args.report:args.report.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','variables','rows','monomials','degree','total_operations','seconds']}))
