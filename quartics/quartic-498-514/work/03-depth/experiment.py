from pathlib import Path
import subprocess, sys, shutil, json
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]/'quartic-version6-release'/'repository'
SRC=REPO/'quartics/quartic-523-540/source-reproduction'
s=(SRC/'builders/odd-product-asymmetric-source.cjs').read_text()
s=s.replace("value:'3^(2^27)'", "value:'3^(2^26)'")
COMPILER=ROOT/'compile_ir.py'
COMPILER.write_text((SRC/'tools/compile_ir.py').read_text().replace('3^(2^27)','3^(2^26)'))
(ROOT/'checker.cjs').write_text((SRC/'tools/checker.cjs').read_text().replace('3^(2^27)','3^(2^26)'))
def edit(a,b):
 global s
 assert s.count(a)==1,(a,s.count(a))
 s=s.replace(a,b)
edit("LV=PV.map((p,i)=>log('logV'+i,p,40))", "LV=PV.map((p,i)=>log('logV'+i,p,i===1?12:40))")
edit("tests.push({value:fsub(L[i],LP[i]),order:40})", "tests.push({value:fsub(L[i],LP[i]),order:i===1?12:40})")
edit("tests.push({value:fsub(L[1],[beta,zero]),order:40}", "tests.push({value:fsub(L[1],[beta,zero]),order:12}")
edit('for(let m of [1,40])coeffs[m]', 'for(let m of [1,12,40])coeffs[m]')
edit("const n=co.length-1,split=n===9?5:n===7?4:null;", "const n=co.length-1,split=n===9?5:n===5?3:n===2?1:null;\n if(n===2){const q2=rsq(name+'.power2',q); return saveF(name,[0,1].map(j=>assign(name+'.sum.'+j,add(co[0][j],mul(co[1][j],q),mul(co[2][j],q2)))));}")
edit("let w=fmul('detector'+r+'.W',evalSym('detector'+r+'.E1',coeffs[1],q1),evalSym('detector'+r+'.E40',coeffs[40],q40));", "let w=fmul('detector'+r+'.W',fmul('detector'+r+'.Wfirst',evalSym('detector'+r+'.E1',coeffs[1],q1),evalSym('detector'+r+'.E12',coeffs[12],q12)),evalSym('detector'+r+'.E40',coeffs[40],q40));")
d=ROOT/'beta12';d.mkdir(exist_ok=True)
(d/'build_source.cjs').write_text(s)
shutil.copytree(SRC/'sources',d/'sources',dirs_exist_ok=True)
with (d/'builder.log').open('w') as f:subprocess.run(['node',str(d/'build_source.cjs')],stdout=f,check=True)
with (d/'compiler.log').open('w') as f:subprocess.run([sys.executable,str(COMPILER),str(d/'raw-translated-ir.json'),str(d/'compiled')],stdout=f,check=True)
data=json.loads((d/'compiled/compiled-ir.json').read_text())
print(json.dumps({'coordinates':len(data['coordinates']),'residuals':len(data['residuals'])}))
