"""Independent exact compact-coordinate transport and serialization check."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import gcd,lcm
import hashlib,json,copy,re
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
PACK=ROOT/'work/quartic-v14-prep/quartic-299-314';PRODUCER=PACK.parent/'package_v14.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unique(pairs):
 d={}
 for k,v in pairs:
  assert k not in d,'duplicate JSON key';d[k]=v
 return d
def read(p):return json.loads(p.read_bytes(),object_pairs_hook=unique)
assert sha(PACK/'ARTIFACTS.json')=='4ad263949b42d7bc5c306f68a168f4375275271e4bf649225b9479340cbe67af'
assert sha(PRODUCER)=='d638a7251a6540aeacf31b2cb66d457589f1d5dd3e010c9c94b3fc6d5b1b5af6'
manifest=read(PACK/'ARTIFACTS.json');snapshot={name:sha(PACK/name) for name in manifest['files']}
for name,desc in manifest['files'].items():
 assert snapshot[name]==desc['sha256'] and (PACK/name).stat().st_size==desc['bytes'],name
source_paths={299:ROOT/'work/quartic-optimization-20261107/resume-elimination-20261107/reciprocal299-r2',314:ROOT/'work/quartic-under300-20261107/10-combination/ordinary-reciprocal299/314'}
review_pins={
 'work/quartic-under300-20261107/10-combination/review-reciprocal299/REVIEW.md':'f51b3e1f571820f2d3b5bf6fb7b60e8b3a7506457bca0a72cbd3a3cfd8feb699',
 'work/quartic-optimization-20261107/resume-depth-20261107/review-ordinary299/REVIEW.md':'13ed2acad2b751abfdb8000a931e6f93bd41b038a965f38c4c2d4902c17318db'}
for path,pin in review_pins.items():assert sha(ROOT/path)==pin
expected_pins={299:('8ea42607ad482290421f2dabc7738846d5109c3ca734d30c7a183a4943377815','e208b503cad67bb53eb42fd78e64b3ebe9e99223692af91dd6c6b5b5b405ca3c'),314:('02b8b6a8b13a566ef520c7a65ec58fd6e63bafa9d7d447e323864b1bae29a5f7','2ea9fb17223a2e2a4fbf98f113d9e0e1da7019a74f4d2c7cefdb31e5b4637028')}
def decode(row):
 d={}
 for t in row['terms']:
  assert set(t)=={'sPower','monomial','coefficient'}
  power=t['sPower'];mon=tuple(t['monomial']);value=Q(t['coefficient'])
  assert isinstance(power,int) and power>=0 and tuple(sorted(mon))==mon and all(isinstance(i,int) for i in mon)
  assert value and (power,mon) not in d;d[power,mon]=value
 return d
def mapped(poly,mapping):return {(p,tuple(mapping[i] for i in m)):c for (p,m),c in poly.items()}
def sos(ir):
 out=defaultdict(int)
 for row in ir['residuals']:
  p=decode(row);assert max(len(m) for power,m in p)<=2
  den=lcm(*(c.denominator for c in p.values()));ints={m:int(c*den) for m,c in p.items()};g=gcd(*ints.values())
  ints={m:c//g for m,c in ints.items()}
  for (power,m),c in ints.items():
   for (power2,m2),c2 in ints.items():out[power+power2,tuple(sorted(m+m2))]+=c*c2
 return {m:Q(c) for m,c in out.items() if c}
def parse_compact_text(path):
 data=path.read_bytes();assert b'\r' not in data and data.endswith(b'\n');lines=data.decode('ascii').splitlines();out={};comments=[]
 for line in lines:
  if line.startswith('#'):comments.append(line);continue
  fields=line.split(' | ');assert len(fields)==3
  value=Q(fields[0]);assert value.denominator==1 and str(value)==fields[0]
  power=int(fields[1]);assert str(power)==fields[1] and power>=0
  mon=tuple(map(int,fields[2].split(','))) if fields[2] else ()
  assert tuple(sorted(mon))==mon and value and (power,mon) not in out
  out[power,mon]=value
 return out,comments,data
results={};source_tables={};negative=[]
for n,rows,terms,size in [(299,279,6630,228028),(314,294,6672,264430)]:
 original_ir=source_paths[n]/('candidate299-ir.json' if n==299 else 'candidate-ir.json')
 original_poly=source_paths[n]/('polynomial299.json' if n==299 else 'polynomial.json')
 assert sha(original_ir)==expected_pins[n][0] and sha(original_poly)==expected_pins[n][1]
 assert original_ir.read_bytes()==(PACK/f'candidate{n}-ir.json').read_bytes()
 assert original_poly.read_bytes()==(PACK/f'polynomial{n}.json').read_bytes()
 source=read(original_ir);compact=read(PACK/f'compact{n}-ir.json');table=decode(read(original_poly));source_tables[n]=table
 declared={x['id'] for x in source['coordinates']};assert len(declared)==len(source['coordinates'])==n
 order=sorted(declared);forward={old:j+1 for j,old in enumerate(order)};backward={new:old for old,new in forward.items()}
 assert order[0]==0 and forward[0]==1 and set(forward.values())==set(range(1,n+1))
 serialized_map=read(PACK/f'coordinate-map{n}.json')
 assert serialized_map=={'sourceInput':0,'compactInput':1,'sourceToCompact':{str(k):v for k,v in forward.items()},'compactToSource':{str(k):v for k,v in backward.items()}}
 oldcoords={x['id']:x for x in source['coordinates']}
 expected_coords=[dict(oldcoords[i],id=forward[i],sourceId=i) for i in order]
 assert compact['coordinates']==expected_coords and compact['coordinates'][0]['kind']=='input'
 assert len(source['residuals'])==len(compact['residuals'])==rows
 for before,after in zip(source['residuals'],compact['residuals']):
  assert {k:v for k,v in before.items() if k!='terms'}=={k:v for k,v in after.items() if k!='terms'}
  assert decode(after)==mapped(decode(before),forward)
  assert mapped(decode(after),backward)==decode(before)
 expected_meta={k:copy.deepcopy(v) for k,v in source.items() if k not in ['coordinates','residuals']}
 if expected_meta['fixedParameter']['coordinate']:
  original_c=expected_meta['fixedParameter']['sourceCoordinate'];expected_meta['fixedParameter']['sourceCoordinate']=forward[original_c]
  assert original_c==1014 and forward[original_c]==304
 expected_meta['coordinateConvention']={'range':[1,n],'inputCoordinate':1,'sourceInputCoordinate':0}
 assert {k:v for k,v in compact.items() if k not in ['coordinates','residuals']}==expected_meta
 stem=f'quartic-{n}-'+('symbolic' if n==299 else 'ordinary')+'-coefficients'
 ct=read(PACK/(stem+'.json'));cp=decode(ct);expected=mapped(table,forward)
 assert cp==expected and mapped(cp,backward)==table and len(cp)==len({m for power,m in cp})==terms
 assert set(ct)=={'format','variables','witnesses','degree','inputCoordinate','coordinates','terms'}|({'fixedParameter'} if n==299 else set())
 assert ct['format']=='integer-quartic-consecutive-coordinates-v2' and ct['coordinates']==expected_coords
 assert (ct['variables'],ct['witnesses'],ct['degree'],ct['inputCoordinate'])==(n,n-1,4,1)
 if n==299:assert ct['fixedParameter']==source['fixedParameter']=={'name':'C','value':'3^(2^25)','coordinate':False}
 assert sos(compact)==cp
 assert max(len(m) for power,m in cp)==4 and gcd(*(int(v) for v in cp.values()))==1
 assert {i for power,m in cp for i in m}==set(range(1,n+1))
 parsed,comments,raw=parse_compact_text(PACK/(stem+'.txt'));assert parsed==cp and len(raw)==size
 headers=[f'# Integer quartic in {n} rational variables; x1 is the input.',
 '# Compact physical coordinates run from1 through the total variable count.',
 '# Rows: coefficient | C exponent | variable indices.',
 '# C=3^(2^25) is a fixed integer.' if n==299 else '# Every C exponent is zero; every coefficient is an explicit decimal integer.']
 headers += [f'# x{co["id"]} = source coordinate {co["sourceId"]}: {co["name"]}' for co in expected_coords]
 assert comments==headers
 serialized=headers+[str(v)+' | '+str(power)+' | '+','.join(map(str,mon)) for (power,mon),v in sorted(cp.items())]
 assert raw==('\n'.join(serialized)+'\n').encode('ascii')
 stats=manifest['statistics'][str(n)]
 for key,value in [('variables',n),('witnesses',n-1),('residuals',rows),('monomials',terms),('coefficientPowerEntries',terms),('degree',4),('content',1),('compactTextBytes',size),('sourceCandidateSha256',expected_pins[n][0]),('sourcePolynomialSha256',expected_pins[n][1])]:assert stats[key]==value
 if n==299:
  assert stats['maximumCoefficient']=='186624*3^(2^26)'
  assert max(power for power,mon in cp)==2
  assert max(abs(v) for (power,mon),v in cp.items() if power==2)==186624
  assert all(abs(v).numerator.bit_length()<2048 for (power,mon),v in cp.items() if power<2)
  assert any(power==0 and abs(v)==1 for (power,mon),v in cp.items())
 else:
  assert all(power==0 and value.denominator==1 for (power,mon),value in cp.items())
  maximum=max(abs(int(value)) for value in cp.values());assert maximum==int(stats['maximumCoefficient'])
  assert maximum.bit_length()==stats['maximumCoefficientBits']==6496 and len(str(maximum))==stats['maximumCoefficientDigits']==1956
  assert 2**6495<=maximum<2**6496 and maximum==3**4098+source_tables[299][0,()]
 results[str(n)]={'variables':n,'witnesses':n-1,'rows':rows,'terms':terms,'canonical_text_bytes':size,'input':1,'coordinate_bijection_exact':True,'all_residuals_and_coefficients_matched':True}
# Parse the retained source-ID text independently as well.
source_text=PACK/'quartic-314-source-id-coefficients.txt'
assert source_text.read_bytes()==(source_paths[314]/'polynomial.txt').read_bytes()
assert source_text.stat().st_size==222890 and sha(source_text)=='efb34a9664a3a2c5b0abe548463e646ba18d6f7e5ab5d9eff9e80bb8b461291e'
parsed={}
for line in source_text.read_text(encoding='ascii').splitlines():
 coefficient,word=line.split('\t');value=int(coefficient);indices=[]
 if word!='1':
  for factor in word.split('*'):
   match=re.fullmatch(r'x(\d+)(?:\^(\d+))?',factor);assert match
   indices.extend([int(match[1])]*int(match[2] or 1))
 key=(0,tuple(indices));assert key not in parsed and value and tuple(sorted(indices))==tuple(indices);parsed[key]=Q(value)
assert parsed==source_tables[314]
assert (PACK/'ordinary314-source-certificate.json').read_bytes()==(source_paths[314]/'CERTIFICATE.json').read_bytes()
lift=manifest['constantLift'];assert lift=={'constantGates':14,'rootSumGates':1,'exponents':[2049]+[2048]*11+[0,0],'targetExponent':2**25,'coefficientBound':'<2^6496'}
exponent=lift['exponents'][0]
for v in lift['exponents'][1:]:exponent=2*exponent+v
assert exponent==2**25
assert {name:sha(PACK/name) for name in manifest['files']}==snapshot
assert sha(PACK/'ARTIFACTS.json')=='4ad263949b42d7bc5c306f68a168f4375275271e4bf649225b9479340cbe67af'
assert sha(PRODUCER)=='d638a7251a6540aeacf31b2cb66d457589f1d5dd3e010c9c94b3fc6d5b1b5af6'
result={'status':'PASS','scope':'Exact compact renaming and serialization; no new source-mathematics acceptance','artifact_manifest_sha256':sha(PACK/'ARTIFACTS.json'),'results':results,'ordinary_source_text_bytes':222890,'ordinary_canonical_text_bytes':264430,'ordinary_strict_bound':'2^6496','all_frozen_artifacts_unchanged':True,'author_producer_executed':False,'source_review_pins':review_pins}
(HERE/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
