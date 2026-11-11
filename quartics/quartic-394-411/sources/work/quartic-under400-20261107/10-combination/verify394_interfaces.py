"""Read-only final anchor transport and pre-anchor scalar-domain check."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
H=Path(__file__).resolve().parent
def read(n):return json.loads((H/n).read_text())
def rows(d):return {r['name']:r for r in d['residuals']}
def p(r):return {(t.get('sPower',0),tuple(t['monomial'])):F(t['coefficient']) for t in r['terms']}
before=read('combined395-ir.json');after=read('combined394-ir.json')
b,a=map(rows,[before,after]);component=rows(read('inputs/anchor-rescale398-ir.json'));cb=rows(read('combined399-ir.json'))
changed={n for n in component.keys()&cb.keys() if p(component[n])!=p(cb[n])}
added=set(component)-set(cb)
deleted=set(cb)-set(component)
assert len(deleted)==2 and len(changed)==1 and len(added)==1
assert set(a)==(set(b)-deleted)|added
for n in added:assert p(a[n])==p(component[n])
for n,r in b.items():
    if n in deleted:continue
    assert p(a[n])==p(component[n]) if n in changed else a[n]==r,n
private={55,56,57,505,549}
assert {n for n,r in b.items() if any(private.intersection(t['monomial']) for t in r['terms'])}==changed|deleted
assert not any(505 in t['monomial'] for r in a.values() for t in r['terms'])
# Every S chart, odd-label, and scalar reciprocal-domain row matches the
# component's source. These identify a nonzero even R before any anchor use.
protected={n for n in cb if (n.startswith('S.') or 'scalar.shiftedS' in n) and n not in deleted|changed}
protected|={n for n,r in cb.items() if n not in changed|deleted and any({543,544}.intersection(t['monomial']) for t in r['terms'])}
for n in protected:assert p(a[n])==p(cb[n]),n
assert len(after['coordinates'])==394 and len(a)==364
print(json.dumps({'passed':True,'candidateSha256':hashlib.sha256((H/'combined394-ir.json').read_bytes()).hexdigest(),'changedRows':sorted(changed),'deletedRows':sorted(deleted),'addedRows':sorted(added),'protectedScalarDomainRows':sorted(protected),'completePrivateIncidence':True},indent=2))
