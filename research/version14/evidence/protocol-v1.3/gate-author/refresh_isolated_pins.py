"""Refresh only this isolated candidate's two live-evaluator pin tables."""
import ast
import hashlib
from pathlib import Path

root = Path(__file__).resolve().parent / 'adapter'
for name in ('live_protocol_context.py', 'live_protocol_context_forks.py'):
    path = root / name
    source = path.read_text(encoding='utf-8')
    tree = ast.parse(source)
    assignment = next(node for node in tree.body if isinstance(node, ast.Assign)
                      and any(isinstance(target, ast.Name) and target.id == 'DEPENDENCY_PINS'
                              for target in node.targets))
    pins = ast.literal_eval(assignment.value)
    pins['coverage_gate.py'] = ''
    pins = {name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in pins}
    lines = source.splitlines(keepends=True)
    replacement = 'DEPENDENCY_PINS={\n' + ''.join('    '+repr(k)+':'+repr(v)+',\n' for k,v in pins.items()) + '}\n'
    lines[assignment.lineno-1:assignment.end_lineno] = [replacement]
    path.write_text(''.join(lines), encoding='utf-8', newline='\n')
    print(name, hashlib.sha256(path.read_bytes()).hexdigest())
