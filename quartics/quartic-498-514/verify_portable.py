"""Rebuild the pinned mixed source; replay every composition; check all tables."""
from pathlib import Path
from fractions import Fraction
import argparse,hashlib,json,os,subprocess,sys
H=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--repo',type=Path)
 args=parser.parse_args();repo=args.repo
 if repo is None:
  repo=next((p for p in H.parents if (p/'quartics/quartic-523-540').is_dir()),None)
 if repo is None:parser.error('Pass --repo PATH to the reference repository.')
 repo=repo.resolve();os.environ['QUARTIC_REFERENCE_REPO']=str(repo)
 for item in read(H/'MANIFEST.json'):
  path=H/item['path'];assert path.is_file() and sha(path)==item['sha256'],str(path)
 for item in read(H/'repository-pins.json'):
  path=repo/item['path'];assert path.is_file() and sha(path)==item['sha256'],str(path)
 build=H/'build';build.mkdir(exist_ok=True)
 src=repo/'quartics/quartic-523-540/source-reproduction'
 original=(src/'builders/odd-product-asymmetric-source.cjs').read_text()
 edits=[("value:'3^(2^27)'","value:'3^(2^26)'"),
  ("LV=PV.map((p,i)=>log('logV'+i,p,40))","LV=PV.map((p,i)=>log('logV'+i,p,i===1?12:40))"),
  ("tests.push({value:fsub(L[i],LP[i]),order:40})","tests.push({value:fsub(L[i],LP[i]),order:i===1?12:40})"),
  ("tests.push({value:fsub(L[1],[beta,zero]),order:40}","tests.push({value:fsub(L[1],[beta,zero]),order:12}"),
  ('for(let m of [1,40])coeffs[m]','for(let m of [1,12,40])coeffs[m]'),
  ("const n=co.length-1,split=n===9?5:n===7?4:null;","const n=co.length-1,split=n===9?5:n===5?3:n===2?1:null;\n if(n===2){const q2=rsq(name+'.power2',q); return saveF(name,[0,1].map(j=>assign(name+'.sum.'+j,add(co[0][j],mul(co[1][j],q),mul(co[2][j],q2)))));}"),
  ("let w=fmul('detector'+r+'.W',evalSym('detector'+r+'.E1',coeffs[1],q1),evalSym('detector'+r+'.E40',coeffs[40],q40));","let w=fmul('detector'+r+'.W',fmul('detector'+r+'.Wfirst',evalSym('detector'+r+'.E1',coeffs[1],q1),evalSym('detector'+r+'.E12',coeffs[12],q12)),evalSym('detector'+r+'.E40',coeffs[40],q40));")]
 for old,new in edits:
  assert original.count(old)==1;original=original.replace(old,new)
 depth=H/'work/03-depth/beta12'
 assert original==(depth/'build_source.cjs').read_text()
 rebuild=build/'raw-rebuild';(rebuild/'sources').mkdir(parents=True,exist_ok=True)
 (rebuild/'build_source.cjs').write_text(original)
 source_name='diophantine_optimization_20261106_v3.tex'
 (rebuild/'sources'/source_name).write_bytes((src/'sources'/source_name).read_bytes())
 with (build/'source-rebuild.log').open('w') as log:subprocess.run(['node',str(rebuild/'build_source.cjs')],check=True,stdout=log,stderr=subprocess.STDOUT)
 for name in ['raw-ir.json','raw-translated-ir.json','census.json']:assert read(rebuild/name)==read(depth/name),name
 scripts=H/'work/10-combination'
 commands=[['depth_recheck.py'],['build.py'],['verify.py'],['build.py','--product'],['verify.py','--product'],
   ['build504.py'],['verify504.py'],['build501.py'],['verify501.py'],['build499.py'],['verify499.py'],
   ['build498.py'],['ordinary514.py'],['verify498.py']]
 with (build/'replay.log').open('w') as log:
  for command in commands:
   print('Checking',' '.join(command),flush=True)
   subprocess.run([sys.executable,'-B',str(scripts/command[0]),*command[1:]],check=True,stdout=log,stderr=subprocess.STDOUT,env=os.environ)
 for n in [498,514]:
  for name in [f'candidate{n}-ir.json',f'polynomial{n}.json']:
   assert (H/name).read_bytes()==(scripts/name).read_bytes(),'Frozen bytes differ: '+name
  base=read(H/f'polynomial{n}.json');ir=read(H/f'candidate{n}-ir.json')
  stem=f'quartic-{n}-'+('symbolic-coefficients' if n==498 else 'ordinary-coefficients')
  table=read(H/(stem+'.json'));cs=sorted(ir['coordinates'],key=lambda c:c['id'])
  assert table['coordinates']==[{'id':i,'sourceId':c['id'],'name':c['name']} for i,c in enumerate(cs)]
  def poly(ts,mp=None):
   out={}
   for t in ts:
    ids=tuple(mp[v] if mp else v for v in t['monomial']);key=(t.get('sPower',0),ids)
    assert key not in out;out[key]=Fraction(t['coefficient'])
   return out
  assert poly(base['terms'])==poly(table['terms'],{i:c['id'] for i,c in enumerate(cs)})
  parsed=[]
  for line in (H/(stem+'.txt')).read_text().splitlines():
   if not line or line.startswith('#'):continue
   coeff,sp,mon=line.split('|');parsed.append({'coefficient':coeff.strip(),'sPower':int(sp),'monomial':[int(v) for v in mon.strip().split(',')] if mon.strip() else []})
  assert poly(parsed)==poly(table['terms'])
 result={'verified':True,'rawMixedSourceRebuilt':True,'allCompositionStepsReplayed':True,'frozenFinalBytesMatched':True,
  'consecutiveCoordinateTablesChecked':True,'textTablesParsedAndChecked':True,
  'symbolic':{'variables':498,'witnesses':497,'residuals':467,'degree':4,'monomials':24669,'content':1,'maximumCoefficient':'16*3^(2^26)'},
  'ordinary':{'variables':514,'witnesses':513,'residuals':483,'degree':4,'monomials':24716,'content':1,'maximumCoefficient':'3^2048+1005072314676622','maximumCoefficientBits':3247},
  'scope':'Finite reconstruction and exact coefficient checks; arithmetic acceptance is in separately authored reviews.'}
 (build/'VERIFIED.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
