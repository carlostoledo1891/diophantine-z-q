"""Independent recursive instantiation and integer expansion."""
if not __debug__:
    raise RuntimeError('Run without -O; assertions are part of validation.')
from collections import defaultdict
from pathlib import Path
import json
from math import gcd
from formats import canonical,sha,row_bytes

EXPECTED={'witnesses':15671,'residuals':15107,'degree':8,'monomials':129497,
          'maximum_absolute_coefficient':685783949153203534233601}

def load_modules(root):
    root=Path(root)
    return {p.stem:json.loads(p.read_bytes()) for p in (root/'modules').glob('*.json')}

def instantiate(root):
    root=Path(root);mods=load_modules(root)
    descriptor=json.loads((root/'polynomial.json').read_bytes())
    shared=json.loads((root/'shared.json').read_bytes())
    count=shared['witnesses'];nextid=count+1;rows=[];trace=[];active=[]
    def emit(row,translate):
        assert row and all(type(c) is int and c!=0 for c,m in row)
        assert gcd(*(c for c,m in row))==1
        rows.append([[c,sorted(translate(v) for v in m)] for c,m in row])
    for row in shared['residuals']:emit(row,lambda v:-v)
    def visit(name,args,path):
        nonlocal nextid
        assert name not in active
        d=mods[name];assert len(args)==d['free'];active.append(name)
        start=nextid;nextid+=d['locals'];indices=args+list(range(start,nextid))
        firstrow=len(rows)
        def translate(v):
            if v<0:
                assert 1<=-v<=count
                return -v
            assert 0<=v<len(indices)
            return indices[v]
        for row in d['residuals']:emit(row,translate)
        trace.append({'path':path,'module':name,'arguments':args,'first_local':start,
                      'local_count':d['locals'],'first_residual':firstrow,'residual_count':len(d['residuals'])})
        for i,call in enumerate(d['calls']):
            visit(call['module'],[translate(v) for v in call['args']],path+'/'+str(i))
        active.pop()
    visit(descriptor['root'],[0],descriptor['root'])
    assert nextid-1==15671 and len(rows)==15107
    assert {v for row in rows for c,m in row for v in m}==set(range(15672))
    assert max(len(m) for row in rows for c,m in row)==4
    certificate={'format':'original-degree8-construction/v1','root':descriptor['root'],
                 'shared_witnesses':count,'witnesses':15671,'residuals':15107,
                 'residual_rows_sha256':sha(row_bytes(rows)),'instantiations':trace}
    return rows,certificate

def expand(rows):
    poly=defaultdict(int)
    # All ordered pairs: independent of the archive's triangular expansion loop.
    for row in rows:
        for c,m in row:
            for d,n in row:poly[tuple(sorted(m+n))]+=c*d
    poly={m:c for m,c in poly.items() if c}
    assert len(poly)==129497 and max(map(len,poly))==8
    maximum=max(map(abs,poly.values()))
    assert maximum==685783949153203534233601 and maximum<2**80
    return poly
