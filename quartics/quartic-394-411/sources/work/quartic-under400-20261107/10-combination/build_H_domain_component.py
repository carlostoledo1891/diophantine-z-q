"""Materialize exactly the independently reviewed H-domain deletion."""
from pathlib import Path
import hashlib,json
H=Path(__file__).resolve().parent
p=H/'primary437-ir.json'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='e488bf3c4e70fda6e0484a51a3a5421cb5b4b0540d3f4cfc3a4192471b00739e'
d=json.loads(p.read_text());removed={17,18}
consumers={r['name'] for r in d['residuals'] if any(removed.intersection(t['monomial']) for t in r['terms'])}
assert consumers=={'H.chart.x.0.definition','H.chart.x.1.definition'}
assert {r['id'] for r in d['residuals'] if r['name'] in consumers}=={32,33}
d['coordinates']=[c for c in d['coordinates'] if c['id'] not in removed]
d['residuals']=[r for r in d['residuals'] if r['name'] not in consumers]
assert len(d['coordinates'])==435
(H/'inputs/H-domain435-ir.json').write_text(json.dumps(d,indent=2)+'\n')
print('Materialized reviewed two-coordinate H-domain deletion; no other object changed.')
