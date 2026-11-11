from pathlib import Path
import hashlib,json,sys
O=Path(__file__).resolve().parent
R=O.parents[2]
def H(b): return hashlib.sha256(b).hexdigest()
def J(p): return json.loads(p.read_text(encoding='utf-8-sig'))
files={}; spans={}; checks=0
def bind(p,h,size=None):
    global checks
    b=p.read_bytes()
    assert H(b)==h,(str(p),'hash')
    if size is not None: assert len(b)==size,(str(p),'bytes')
    files[p.relative_to(R).as_posix()]={'sha256':h,'bytes':len(b)}
    checks+=1
    return b
def walk(x):
    global checks
    if isinstance(x,dict):
        if {'path','sha256'}<=x.keys():
            b=bind(R/x['path'],x['sha256'],x.get('bytes'))
            if {'line_start','line_end','raw_span_sha256'}<=x.keys():
                a,z=x['line_start'],x['line_end'];ls=b.splitlines(keepends=True)
                assert 1<=a<=z<=len(ls),(x['path'],a,z)
                assert H(b''.join(ls[a-1:z]))==x['raw_span_sha256'],(x['path'],a,z,'span')
                spans[(x['path'],a,z)]=x;checks+=1
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
def main():
    target=R/'work/source-risk-review-20261107/b11-marking-descent-sources-theta-006'
    counts={}
    for n in range(1,7):
        p=target.with_name('b11-marking-descent-sources-theta-'+str(n).zfill(3))
        m=J(p/'MANIFEST.json');bind(p/'MANIFEST.json',H((p/'MANIFEST.json').read_bytes()))
        counts[p.name]=len(m['members'])
        for row in m['members']:bind(p/row['path'],row['sha256'],row.get('bytes'))
    for name in ['APPLICATIONS.json','SOURCE-USES.json','SOURCES.json','CURRENT-CONSUMERS.json','INPUTS.json','INCOMING-INTERFACES.json','DELTA.json','EFFECTIVE-PACKET.json']:
        p=target/name
        if p.exists():walk(J(p))
    apps=J(target/'APPLICATIONS.json')['applications']
    uses=J(target/'SOURCE-USES.json')
    assert len(apps)==3 and len(uses)==7
    assert all(len(a['obligations'])==9 for a in apps)
    assert all(len(u['assertion'])==10 for u in uses)
    q=next(a for a in apps if a['id']=='B11-STD-QUOTIENT')
    assert 'B11-STD-MARKING' in q['dependencies']
    inc=J(target/'INCOMING-INTERFACES.json')
    assert 'canonical generic full-three' in inc[4]['required_assertion']
    proof=(target/'PROOF.md').read_text(encoding='utf-8')
    assert '29.44.14' in proof
    old=target.with_name('b11-marking-descent-sources-theta-003')
    delta=J(target/'DELTA.json')['proof_replacement']
    old_bytes=(old/'PROOF.md').read_bytes()
    assert old_bytes.count(delta['old'].encode())==1
    assert old_bytes.replace(delta['old'].encode(),delta['new'].encode())==(target/'PROOF.md').read_bytes()
    old_sources=J(old/'SOURCES.json');new_sources=J(target/'SOURCES.json')
    source_changes=[a['id'] for a,b in zip(old_sources,new_sources) if a!=b]
    assert len(old_sources)==len(new_sources) and source_changes==['STACKS-01W7']
    old_inc=J(old/'INCOMING-INTERFACES.json')
    old_inc[4]['required_assertion']=inc[4]['required_assertion']
    assert old_inc==inc
    out={'status':'PASS','scope':'File, raw-span, schema-count and explicit correction checks only; mathematical review is separate.','target_manifest':{'path':(target/'MANIFEST.json').relative_to(R).as_posix(),'sha256':H((target/'MANIFEST.json').read_bytes())},'checks':checks,'member_counts':counts,'files':files,'spans':list(spans.values()),'applications':3,'comparisons':27,'source_uses':7}
    (O/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['status','target_manifest','checks','member_counts','applications','comparisons','source_uses']}))
if __name__=='__main__':main()
