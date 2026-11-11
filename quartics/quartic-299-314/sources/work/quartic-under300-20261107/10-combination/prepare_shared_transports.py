from pathlib import Path
import hashlib,json,subprocess,sys
H=Path(__file__).resolve().parent
P=H/'sparse-shared314';P.mkdir(exist_ok=True)
source=H.parents[1]/'quartic-optimization-20261107/resume-elimination-20261107/shared-scale314/candidate314-ir.json'
assert source.exists()
src="H.parents[2]/'quartic-optimization-20261107/resume-elimination-20261107/shared-scale314/candidate314-ir.json'"
old='d450a34735fe84bab0900abb3931740d4f7cedb1004ede7a81e1a09c4249f8b8'
new='7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5'
def fresh(path,text):
 b=text.encode()
 if path.exists():assert path.read_bytes()==b,path
 else:path.write_bytes(b)
b=(H/'sparse315/build.py').read_text().replace("H.parent/'combined315/candidate315-ir.json'",src).replace(old,new).replace('accepted315','accepted shared314').replace('candidate315-ir.json','candidate314-ir.json').replace('polynomial315.json','polynomial314.json')
fresh(P/'build.py',b)
subprocess.run([sys.executable,str(P/'build.py')],check=True)
ih=hashlib.sha256((P/'candidate314-ir.json').read_bytes()).hexdigest();ph=hashlib.sha256((P/'polynomial314.json').read_bytes()).hexdigest()
v=(H/'sparse315/verify.py').read_text().replace("H.parent/'combined315/candidate315-ir.json'",src).replace(old,new).replace('cf9d5af5a8fa99fc18f7b87218e14cc6d6ccd4e3d98cc2fa8a58486099c2cd17',ih).replace('225f339d40a1dc00bfde8d513528b9b40d65540f6618e68652e9599bc2a76a11',ph).replace('candidate315-ir.json','candidate314-ir.json').replace('polynomial315.json','polynomial314.json').replace('5671','6077').replace('5668','6074').replace('len(used)==315','len(used)==314').replace('len(rr)==285','len(rr)==283').replace("'variables':315,'residuals':285","'variables':314,'residuals':283")
fresh(P/'verify.py',v)
subprocess.run([sys.executable,str(P/'verify.py')],check=True)
O=H/'ordinary-sparse-shared314';O.mkdir(exist_ok=True)
b=(H/'ordinary-sparse315/build.py').read_text().replace('sparse315','sparse-shared314').replace('candidate315-ir.json','candidate314-ir.json').replace('polynomial315.json','polynomial314.json').replace('cf9d5af5a8fa99fc18f7b87218e14cc6d6ccd4e3d98cc2fa8a58486099c2cd17',ih).replace('225f339d40a1dc00bfde8d513528b9b40d65540f6618e68652e9599bc2a76a11',ph).replace('size=316+count','size=315+count')
fresh(O/'build.py',b)
subprocess.run([sys.executable,str(O/'build.py')],check=True)
summary=json.loads((O/'SUMMARY.json').read_bytes())
v=(H/'ordinary-sparse315/verify.py').read_text().replace('sparse315','sparse-shared314').replace('candidate315-ir.json','candidate314-ir.json').replace('polynomial315.json','polynomial314.json').replace('cf9d5af5a8fa99fc18f7b87218e14cc6d6ccd4e3d98cc2fa8a58486099c2cd17',ih).replace('225f339d40a1dc00bfde8d513528b9b40d65540f6618e68652e9599bc2a76a11',ph)
start=v.index('pins={');end=v.index('\ndef poly(',start)
v=v[:start]+'pins='+repr({r['variables']:(r['candidateSha256'],r['polynomialSha256'],r['textSha256']) for r in summary})+'\nchains={331:[513]*9+[2]+[0]*6,330:[1025]*10+[2]+[0]*4,329:[2049]+[2048]*11+[0,0]}\n'+v[end:]
v=v.replace('size-30,{332:5716,331:5713,330:5710}[size]','size-31,'+repr({r['variables']:r['monomials'] for r in summary})+'[size]')
fresh(O/'verify.py',v)
subprocess.run([sys.executable,str(O/'verify.py')],check=True)
