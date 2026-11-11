"use strict";
const assert=require("node:assert/strict"),fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),cp=require("node:child_process");
const {IR,CappedIR,maximumPrecisionBoundIR,buildPrecisionIR,lowerIR,runIR}=require("./precision-register.js");
const {validateProgram}=require("../../outputs/integer-diophantine-compiler.js");
const py=process.env.PRECISION_PYTHON||"C:/Users/glaze/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe";
const root=path.resolve(__dirname,"../..");
const sha=x=>crypto.createHash("sha256").update(x).digest("hex");
const si=(r,x)=>r[x[0]]-r[x[1]];
const fi=(r,x)=>x.map(z=>si(r,z).toString());
const enc=x=>x>=0?2*x:-2*x-1;
function pointSnapshot(result,p){return {origin:result.registers[p.origin].toString(),xyz:p.xyz.map(x=>fi(result.registers,x))};}
function primitive(machine,inputs,limit=1000000){
  const tape=Array(machine.registers).fill(0n);inputs.forEach((x,i)=>tape[i]=BigInt(x));let pc=0,atCleanup=null;
  for(let step=0;step<limit;step++){
    if(pc===machine.debug.reject)return {halted:false,rejected:true,steps:step};
    if(pc===machine.debug.cleanup&&!atCleanup)atCleanup=tape.slice();
    const x=machine.program[pc];
    if(x.op==="halt")return {halted:true,allZero:tape.every(z=>z===0n),steps:step,atCleanup};
    if(x.op==="add"){tape[x.register]++;pc=x.next;}
    else if(tape[x.register]>0n){tape[x.register]--;pc=x.nonzero;}else pc=x.zero;
  }
  throw Error("Primitive test budget exhausted; this is not rejection");
}
function checkPrimitiveLayer(){
  const b=new IR(2),add=b.add(0,1),mul=b.mul(0,1),sub=b.sub(0,1),[q,r]=b.divmod(0,1),[q2,r2]=b.div2(0);
  const count=b.copy(b.constant(4)),sum=b.copy(b.constant(0));
  b.whileNZ(count,()=>{b.assign(sum,b.add(sum,0));b.assign(count,b.sub(count,b.constant(1)));});
  b.accept();const ir=b.artifact(),m=lowerIR(ir);validateProgram(m.program,m.registers);let tested=0;
  for(let x=0;x<=8;x++)for(let y=1;y<=5;y++){
    const expected=[x+y,x*y,Math.max(x-y,0),Math.floor(x/y),x%y,Math.floor(x/2),x%2,4*x].map(BigInt);
    const ids=[add,mul,sub,q,r,q2,r2,sum],a=runIR(ir,[x,y]),p=primitive(m,[x,y]);
    assert(p.halted&&p.allZero);assert.deepEqual(ids.map(i=>a.registers[i]),expected);
    assert.deepEqual(ids.map(i=>p.atCleanup[m.debug.irMap[i]]),expected);tested++;
  }
  const reject=new IR(1);reject.reject();const rm=lowerIR(reject.artifact()),state=rm.program[rm.debug.reject];
  assert(state.op==="sub"&&state.nonzero===rm.debug.reject&&state.zero===rm.debug.reject);
  assert(primitive(rm,[7]).rejected);
  // The only halt is last, and the entire cleanup suffix clears each register.
  assert.equal(m.program.filter(x=>x.op==="halt").length,1);
  assert.equal(m.program.length-m.debug.cleanup,m.registers+1);
  m.program.slice(m.debug.cleanup,-1).forEach((x,i)=>assert.deepEqual(x,{op:"sub",register:i,nonzero:m.debug.cleanup+i,zero:m.debug.cleanup+i+1}));
  const five=new IR(5),total=five.sum([0,1,2,3,4]);five.accept();const fm=lowerIR(five.artifact()),fr=primitive(fm,[1,2,3,4,5]);
  assert.deepEqual(fm.debug.irMap.slice(0,5),[0,1,2,3,4]);assert(fr.halted&&fr.allZero);assert.equal(fr.atCleanup[fm.debug.irMap[total]],15n);
  return {arithmeticCases:tested,fiveInputMappingChecked:true,primitiveRegisters:m.registers,primitiveInstructions:m.program.length,rejectSinkChecked:true,cleanupChecked:true};
}
function pointFixtures(){
  const fixtures=[];
  for(let n=-6;n<=6;n++){
    const b=new IR(0),p=b.multiple(b.signed(n));b.accept();const r=runIR(b.artifact(),[]);
    fixtures.push({kind:"multiple",n,actual:pointSnapshot(r,p)});
  }
  for(const kind of ["O+P","P+O","P+P","P+-P","P+scaledP","T+T","doubleT","P+2P"]){
    const b=new IR(0),p=b.basePoint(),O=b.blankPoint();b.infinity(O);
    const T={origin:b.constant(0),xyz:[b.field(0),b.field(0),b.field(1)]};
    const neg={origin:b.constant(0),xyz:[p.xyz[0],b.fneg(p.xyz[1]),p.xyz[2]]};
    const scaled={origin:b.constant(0),xyz:[b.fscale(4,p.xyz[0]),b.fscale(8,p.xyz[1]),b.fscale(2,p.xyz[2])]};
    const choices={"O+P":()=>b.pointAdd(O,p),"P+O":()=>b.pointAdd(p,O),"P+P":()=>b.pointAdd(p,p),"P+-P":()=>b.pointAdd(p,neg),"P+scaledP":()=>b.pointAdd(p,scaled),"T+T":()=>b.pointAdd(T,T),"doubleT":()=>b.double(T),"P+2P":()=>b.pointAdd(p,b.double(p))};
    const out=choices[kind]();b.accept();fixtures.push({kind,actual:pointSnapshot(runIR(b.artifact(),[]),out)});
  }
  for(const n of [-4,-1,0,1,2,4]){
    const b=new IR(0),z=b.z(b.multiple(b.signed(n)));b.accept();const r=runIR(b.artifact(),[]);
    fixtures.push({kind:"z",n,num:fi(r.registers,z.num),den:r.registers[z.den].toString()});
  }
  for(const [a,j] of [[1,1],[1,-1],[2,4],[2,-4],[3,0],[3,6]]){
    const b=new IR(0),z=b.fractionDivide(b.z(b.multiple(b.signed(j))),b.z(b.multiple(b.signed(a))));b.accept();const r=runIR(b.artifact(),[]);
    fixtures.push({kind:"center",a,j,num:fi(r.registers,z.num),den:r.registers[z.den].toString()});
  }
  const b=new IR(0),T={origin:b.constant(0),xyz:[b.field(0),b.field(0),b.field(1)]};b.z(T);b.accept();assert.equal(runIR(b.artifact(),[]).accepted,false);
  const c=new IR(0);c.fractionFromSignedDen(c.field(1),c.signed(0));c.accept();assert.equal(runIR(c.artifact(),[]).accepted,false);
  return fixtures;
}
function cappedChecks(){
  const b=new IR(3),c=new CappedIR(b,2),power=c.power(0,1),product=c.mul(0,1),sum=c.add(0,1);b.accept();const ir=b.artifact();let cases=0;
  for(let cap=1;cap<=8;cap++)for(let x=0;x<=10;x++)for(let n=0;n<=7;n++){
    const r=runIR(ir,[x,n,cap]).registers,clip=x=>x>BigInt(cap)?BigInt(cap+1):x;
    assert.equal(r[power],clip(BigInt(x)**BigInt(n)));assert.equal(r[product],clip(BigInt(x*n)));assert.equal(r[sum],clip(BigInt(x+n)));cases++;
  }
  const h=new IR(1),height=new CappedIR(h,0).height();h.accept();const hir=h.artifact(),heights=[];
  for(const cap of [1,2,3,10,100,1000,1000000]){const r=runIR(hir,[cap]);heights.push({cap,value:r.registers[height].toString()});}
  return {cases,heights};
}
const macro=checkPrimitiveLayer(),points=pointFixtures(),capped=cappedChecks(),ir=buildPrecisionIR();
const boundBuilder=new IR(2),boundResult=maximumPrecisionBoundIR(boundBuilder,0,1);boundBuilder.accept();const boundIR=boundBuilder.artifact(),precisionBounds=[];
for(let u=1;u<=12;u++)for(const d of [1,4*u,16*u,16*u+1,64*u,64*u+1,256*u+1,1024*u+1]){
  const r=runIR(boundIR,[u,d]);precisionBounds.push({u,d,accepted:r.accepted,bound:r.accepted?r.registers[boundResult].toString():null});
}
const cases=[[0,1,1,1,0],[-15,1,1,1,-15],[1,0,1,1,1],[1,1,0,1,0],[1,1,1,0,1],[1,1,1,1,2],[1,1,-1,1,-1],[-1,-1,1,1,-1]];
for(let ell=1;ell<=8;ell++)for(const n of [-2,1,3])cases.push([n,1,2,ell,2*n]);
const predicates=cases.map(values=>({values,naturalInputs:values.map(enc),accepted:runIR(ir,values.map(enc)).accepted}));
const payload={points,heights:capped.heights,predicates,precisionBounds};
fs.writeFileSync(path.join(__dirname,"comparison-fixtures.json"),JSON.stringify(payload)+"\n");
const python=String.raw`
import importlib.util,json,sys
from fractions import Fraction as Q
sys.set_int_max_str_digits(0)
spec=importlib.util.spec_from_file_location('reference',sys.argv[1]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
d=json.load(sys.stdin)
def readpoint(a):
    if a['origin']=='1': return None
    X,Y,Z=[tuple(Q(int(v)) for v in pair) for pair in a['xyz']]
    assert Z!=m.ZERO
    return m.divide(X,m.mul(Z,Z)),m.divide(Y,m.mul(m.mul(Z,Z),Z))
P=m.POINT_P;O=None;T=(m.ZERO,m.ZERO);N=(P[0],m.neg(P[1]))
for f in d['points']:
    k=f['kind']
    if k=='z':
        got=tuple(Q(int(v),int(f['den'])) for v in f['num']);want=m.z(m.point_multiple(f['n']))
    elif k=='center':
        got=Q(int(f['num'][0]),int(f['den']));want=m.center(f['a'],f['j'])
    else:
        got=readpoint(f['actual'])
        if k=='multiple':want=m.point_multiple(f['n'])
        else:
            pairs={'O+P':(O,P),'P+O':(P,O),'P+P':(P,P),'P+-P':(P,N),'P+scaledP':(P,P),'T+T':(T,T),'doubleT':(T,T),'P+2P':(P,m.point_multiple(2))}
            want=m.point_add(*pairs[k])
        assert m.on_curve(got)
    assert got==want,(k,f.get('n'))
for f in d['heights']:assert int(f['value'])==m.height_constant_capped(f['cap'])
for f in d['predicates']:assert f['accepted']==m.accepts_naturals(*f['naturalInputs'])
for f in d['precisionBounds']:
    bound=m.maximum_precision_exponent(Q(f['u'],f['d']))
    assert f['accepted']==(bound>=1)
    if f['accepted']:assert int(f['bound'])==bound
print(json.dumps({'pointAndCoordinateCases':len(d['points']),'heightCases':len(d['heights']),'precisionBoundCases':len(d['precisionBounds']),'predicateCases':len(d['predicates']),'acceptedPredicateSamples':sum(f['accepted'] for f in d['predicates'])}))
`;
const compared=cp.spawnSync(py,["-c",python,path.join(root,"outputs/variable-shift-precision.py")],{input:JSON.stringify(payload),encoding:"utf8",maxBuffer:4*1024*1024});
if(compared.status!==0)throw Error(compared.stderr||compared.error||"Python comparison failed");
const sources=["outputs/variable-shift-precision.py","outputs/integer-diophantine-compiler.js","outputs/integer-halting-correctness-proof.txt","outputs/universal-interpreter.js","work/precision-register/precision-register.js"];
const fresh=lowerIR(ir),saved=fs.readFileSync(path.join(__dirname,"precision-machine.json"));
assert.equal(sha(Buffer.from(JSON.stringify(fresh)+"\n")),sha(saved));
assert.equal(fresh.program.filter(x=>x.op==="halt").length,1);
assert.equal(fresh.program.length-fresh.debug.cleanup,fresh.registers+1);
fresh.program.slice(fresh.debug.cleanup,-1).forEach((x,i)=>assert.deepEqual(x,{op:"sub",register:i,nonzero:fresh.debug.cleanup+i,zero:fresh.debug.cleanup+i+1}));
const sink=fresh.program[fresh.debug.reject];assert(sink.op==="sub"&&sink.nonzero===fresh.debug.reject&&sink.zero===fresh.debug.reject);
const report={status:"passed",primitive:macro,cappedArithmeticCases:capped.cases,pythonComparison:JSON.parse(compared.stdout),fullMachine:{registers:fresh.registers,instructions:fresh.program.length,regenerationMatches:true,uniqueFinalHalt:true,allRegisterCleanup:true,absorbingRejectSink:true,sha256:sha(saved)},sourceHashes:sources.map(file=>({file,sha256:sha(fs.readFileSync(path.join(root,file)))})),limitations:["Finite tests do not prove the general semantic correspondence.","No true sample of the full astronomical-height predicate was found or claimed.","Full generated-machine executions were not used as a substitute for the lowering proof."]};
fs.writeFileSync(path.join(__dirname,"checks.json"),JSON.stringify(report,null,2)+"\n");console.log(JSON.stringify(report,null,2));
