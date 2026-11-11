from pathlib import Path
import json
import subprocess
import sys
root = Path(__file__).resolve().parent
results = []
for directory in ('controller', 'adapter', 'publisher', 'gate', 'immutable-cache'):
    command = [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', '.', '-p', 'test_*.py', '-v']
    result = subprocess.run(command, cwd=root/'tree'/directory, capture_output=True, text=True)
    output = result.stdout + result.stderr
    (root / (directory + '-tests.log')).write_text(output, encoding='utf-8')
    results.append({'directory': directory, 'command': command, 'returncode': result.returncode, 'output': output})
(root/'TEST-RESULTS.json').write_text(json.dumps(results, indent=2)+'\n', encoding='utf-8')
print(json.dumps([{'directory': r['directory'], 'returncode': r['returncode'], 'tail': r['output'][-500:]} for r in results], indent=2))
raise SystemExit(any(r['returncode'] for r in results))
