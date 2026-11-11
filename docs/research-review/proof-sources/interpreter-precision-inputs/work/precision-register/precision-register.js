"use strict";

// Finite generator for the five-input predicate in variable-shift-precision.py.
// Runtime arithmetic below is emitted into natural registers; BigInt at build
// time is used only to spell fixed finite literal constants exactly.
function checkSourceLocks(){
  const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
  const lock=JSON.parse(fs.readFileSync(path.join(__dirname,"source-lock.json"),"utf8"));
  for(const item of lock.sources){
    const bytes=fs.readFileSync(path.resolve(__dirname,"../..",item.path));
    if(crypto.createHash("sha256").update(bytes).digest("hex")!==item.sha256)throw Error("Precision construction source changed: "+item.path);
  }
}
checkSourceLocks();
const {Assembler}=require("../../outputs/universal-interpreter.js");
const {validateProgram}=require("../../outputs/integer-diophantine-compiler.js");

class IR {
  constructor(inputs=5){this.count=inputs;this.inputs=inputs;this.init=[];this.body=[];this.current=this.body;this.constants=new Map();}
  fresh(){return this.count++;}
  emit(x){this.current.push(x);}
  constant(v){v=BigInt(v);if(v<0n)throw Error("Natural literal required");const key=v.toString();if(this.constants.has(key))return this.constants.get(key);const out=this.fresh();this.constants.set(key,out);this.init.push({op:"set",out,value:key});return out;}
  assign(out,x){this.emit({op:"copy",out,x});}
  copy(x){const out=this.fresh();this.assign(out,x);return out;}
  binary(op,x,y){const out=this.fresh();this.emit({op,out,x,y});return out;}
  add(x,y){return this.binary("add",x,y);}
  mul(x,y){return this.binary("mul",x,y);}
  sub(x,y){return this.binary("sub",x,y);}
  sum(xs){return xs.reduce((x,y)=>this.add(x,y),this.constant(0));}
  block(fn){const old=this.current,out=[];this.current=out;fn();this.current=old;return out;}
  ifNZ(x,yes,no=()=>{}){this.emit({op:"ifNZ",x,yes:this.block(yes),no:this.block(no)});}
  ifLT(x,y,yes,no=()=>{}){this.emit({op:"ifLT",x,y,yes:this.block(yes),no:this.block(no)});}
  whileNZ(x,body){this.emit({op:"whileNZ",x,body:this.block(body)});}
  whileLT(x,y,body){this.emit({op:"whileLT",x,y,body:this.block(body)});}
  div2(x){const q=this.fresh(),r=this.fresh();this.emit({op:"div2",x,q,r});return [q,r];}
  divmod(x,y){const q=this.fresh(),r=this.fresh();this.ifNZ(y,()=>{},()=>this.reject());this.emit({op:"divmod",x,y,q,r});return [q,r];}
  accept(){this.emit({op:"accept"});}
  reject(){this.emit({op:"reject"});}
  neq(x,y){return this.add(this.sub(x,y),this.sub(y,x));}
  assignMany(outs,ins){const values=outs.some(x=>ins.includes(x))?ins.map(x=>this.copy(x)):ins;outs.forEach((out,i)=>this.assign(out,values[i]));}
  signed(v){v=BigInt(v);return [this.constant(v>0n?v:0n),this.constant(v<0n?-v:0n)];}
  snormal(p,n){return [this.sub(p,n),this.sub(n,p)];}
  sadd(x,y){return this.snormal(this.add(x[0],y[0]),this.add(x[1],y[1]));}
  sneg(x){return [x[1],x[0]];}
  ssub(x,y){return this.sadd(x,this.sneg(y));}
  smul(x,y){return this.snormal(this.add(this.mul(x[0],y[0]),this.mul(x[1],y[1])),this.add(this.mul(x[0],y[1]),this.mul(x[1],y[0])));}
  sabs(x){return this.add(x[0],x[1]);}
  ssquare(x){const t=this.sabs(x);return [this.mul(t,t),this.constant(0)];}
  sscaleNat(n,x){return [this.mul(n,x[0]),this.mul(n,x[1])];}
  sscale(k,x){return this.sscaleNat(this.constant(k),x);}
  decode(x){const [q,r]=this.div2(x),out=[this.fresh(),this.fresh()];this.assignMany(out,this.signed(0));this.ifNZ(r,()=>this.assign(out[1],this.add(q,this.constant(1))),()=>this.assign(out[0],q));return out;}
  field(a,b=0){return [this.signed(a),this.signed(b)];}
  blankField(){return [[this.fresh(),this.fresh()],[this.fresh(),this.fresh()]];}
  fieldCopy(out,x){this.assignMany(out.flat(),x.flat());}
  fadd(x,y){return [this.sadd(x[0],y[0]),this.sadd(x[1],y[1])];}
  fneg(x){return [this.sneg(x[0]),this.sneg(x[1])];}
  fsub(x,y){return this.fadd(x,this.fneg(y));}
  fmul(x,y){return [this.sadd(this.smul(x[0],y[0]),this.sscale(2,this.smul(x[1],y[1]))),this.sadd(this.smul(x[0],y[1]),this.smul(x[1],y[0]))];}
  fsquare(x){return [this.sadd(this.ssquare(x[0]),this.sscale(2,this.ssquare(x[1]))),this.sscale(2,this.smul(x[0],x[1]))];}
  fscale(k,x){return [this.sscale(k,x[0]),this.sscale(k,x[1])];}
  fscaleNat(n,x){return [this.sscaleNat(n,x[0]),this.sscaleNat(n,x[1])];}
  fnorm(x){return this.ssub(this.ssquare(x[0]),this.sscale(2,this.ssquare(x[1])));}
  fconjugate(x){return [x[0],this.sneg(x[1])];}
  fnz(x){return this.sum(x.flat());}
  blankPoint(){return {origin:this.fresh(),xyz:[this.blankField(),this.blankField(),this.blankField()]};}
  pointCopy(out,p){this.assignMany([out.origin,...out.xyz.flat(2)],[p.origin,...p.xyz.flat(2)]);}
  infinity(out){this.assign(out.origin,this.constant(1));for(const c of out.xyz)this.fieldCopy(c,this.field(0));}
  pointSet(out,xyz){this.assign(out.origin,this.constant(0));xyz.forEach((x,i)=>this.fieldCopy(out.xyz[i],x));}
  basePoint(){return {origin:this.constant(0),xyz:[this.field(13128,-9280),this.field(-1979520,1399728),this.field(8)]};}
  double(p){
    const out=this.blankPoint();
    this.ifNZ(p.origin,()=>this.infinity(out),()=>this.ifNZ(this.fnz(p.xyz[1]),()=>{
      const [X,Y,Z]=p.xyz,A=this.fsquare(X),B=this.fsquare(Y),C=this.fsquare(B);
      const D=this.fscale(4,this.fmul(X,B)),Z4=this.fsquare(this.fsquare(Z));
      const E=this.fadd(this.fscale(3,A),this.fmul(this.field(-11243,7950),Z4));
      const XX=this.fsub(this.fsquare(E),this.fscale(2,D));
      const YY=this.fsub(this.fmul(E,this.fsub(D,XX)),this.fscale(8,C));
      this.pointSet(out,[XX,YY,this.fscale(2,this.fmul(Y,Z))]);
    },()=>this.infinity(out)));
    return out;
  }
  pointAdd(p,q){
    const out=this.blankPoint();
    this.ifNZ(p.origin,()=>this.pointCopy(out,q),()=>this.ifNZ(q.origin,()=>this.pointCopy(out,p),()=>{
      const [X1,Y1,Z1]=p.xyz,[X2,Y2,Z2]=q.xyz;
      const z1s=this.fsquare(Z1),z2s=this.fsquare(Z2);
      const U1=this.fmul(X1,z2s),U2=this.fmul(X2,z1s);
      const S1=this.fmul(Y1,this.fmul(z2s,Z2)),S2=this.fmul(Y2,this.fmul(z1s,Z1));
      const H=this.fsub(U2,U1),R=this.fsub(S2,S1);
      this.ifNZ(this.fnz(H),()=>{
        const H2=this.fsquare(H),H3=this.fmul(H2,H);
        const X=this.fsub(this.fsub(this.fsquare(R),H3),this.fscale(2,this.fmul(U1,H2)));
        const Y=this.fsub(this.fmul(R,this.fsub(this.fmul(U1,H2),X)),this.fmul(S1,H3));
        this.pointSet(out,[X,Y,this.fmul(H,this.fmul(Z1,Z2))]);
      },()=>this.ifNZ(this.fnz(R),()=>this.infinity(out),()=>this.pointCopy(out,this.double(p))));
    }));
    return out;
  }
  multiple(n){
    const count=this.copy(this.sabs(n)),acc=this.blankPoint(),base=this.blankPoint();
    this.infinity(acc);this.pointCopy(base,this.basePoint());
    this.ifNZ(n[1],()=>this.fieldCopy(base.xyz[1],this.fneg(base.xyz[1])));
    this.whileNZ(count,()=>{
      const [q,r]=this.div2(count);
      this.ifNZ(r,()=>this.pointCopy(acc,this.pointAdd(acc,base)));
      this.assign(count,q);
      this.ifNZ(count,()=>this.pointCopy(base,this.double(base)));
    });
    return acc;
  }
  // Fraction in K is num/den, with integral K numerator and positive integer den.
  blankFraction(){return {num:this.blankField(),den:this.fresh()};}
  fractionFromSignedDen(num,den){
    const out=this.blankFraction(),magnitude=this.sabs(den);
    this.ifNZ(magnitude,()=>{},()=>this.reject());
    this.assign(out.den,magnitude);
    this.ifNZ(den[1],()=>this.fieldCopy(out.num,this.fneg(num)),()=>this.fieldCopy(out.num,num));
    return out;
  }
  z(p){
    const out=this.blankFraction();
    this.ifNZ(p.origin,()=>{this.fieldCopy(out.num,this.field(0));this.assign(out.den,this.constant(1));},()=>{
      const [X,Y,Z]=p.xyz;
      const result=this.fractionFromSignedDen(this.fmul(this.fneg(this.fmul(X,Z)),this.fconjugate(Y)),this.fnorm(Y));
      this.fieldCopy(out.num,result.num);this.assign(out.den,result.den);
    });
    return out;
  }
  fractionDivide(x,y){
    const num=this.fscaleNat(y.den,this.fmul(x.num,this.fconjugate(y.num)));
    return this.fractionFromSignedDen(num,this.sscaleNat(x.den,this.fnorm(y.num)));
  }
  artifact(debug={}){return {format:"natural-register-ir-v1",registers:this.count,inputNames:["n_code","kappa_code","a_code","ell_code","j_code"].slice(0,this.inputs),init:this.init,body:this.body,debug};}
}

class CappedIR {
  constructor(b,cap){this.b=b;this.cap=cap;this.over=b.add(cap,b.constant(1));}
  value(x){const b=this.b,out=b.copy(x);b.ifLT(this.cap,out,()=>b.assign(out,this.over));return out;}
  add(...xs){return this.value(this.b.sum(xs));}
  mul(x,y){return this.value(this.b.mul(x,y));}
  max(...xs){const b=this.b,out=b.copy(xs[0]);for(const x of xs.slice(1))b.ifLT(out,x,()=>b.assign(out,x));return out;}
  power(x,n){
    const b=this.b,count=b.copy(n),base=this.value(x),out=b.copy(b.constant(1));
    b.whileNZ(count,()=>{
      b.assign(count,b.sub(count,b.constant(1)));
      b.assign(out,this.mul(out,base));
      b.ifLT(this.cap,out,()=>b.assign(count,b.constant(0)));
    });
    return out;
  }
  factorial324(){const b=this.b,out=b.copy(b.constant(1)),i=b.copy(b.constant(2)),end=b.constant(325);b.whileLT(i,end,()=>{b.assign(out,this.mul(out,i));b.assign(i,b.add(i,b.constant(1)));b.ifLT(this.cap,out,()=>b.assign(i,end));});return out;}
  height(){
    const b=this.b,k=x=>b.constant(x),d0=this.factorial324();
    const d=this.mul(d0,this.power(k(3),this.mul(k(256),this.power(d0,k(4)))));
    const g0=this.value(k(116064000000n)),e0=this.mul(k(10),this.power(this.mul(d,g0),k(2)));
    const r=this.max(d,this.value(k(317)),this.value(k(1000000000000n)));
    const q0=this.power(r,this.mul(r,e0)),d2=this.power(d,k(2));
    const bcm=this.add(this.mul(d2,this.power(k(3),this.mul(k(21000),d2))),k(1));
    const ccm=this.add(this.mul(k(2),bcm),this.mul(k(4096),this.add(k(1028),this.mul(k(5),d),this.mul(k(84000),d2))));
    return this.mul(k(20000000000000n),this.max(k(1),ccm,this.power(q0,k(17))));
  }
}

function maximumPrecisionBoundIR(b,epsNum,epsDen){
  b.ifNZ(epsNum,()=>{},()=>b.reject());
  const [limit]=b.divmod(b.sub(epsDen,b.constant(1)),b.mul(b.constant(4),epsNum));
  b.ifNZ(limit,()=>{},()=>b.reject());
  const bound=b.copy(b.constant(0)),remaining=b.copy(limit);
  b.whileLT(b.constant(3),remaining,()=>{const [q]=b.divmod(remaining,b.constant(4));b.assign(remaining,q);b.assign(bound,b.add(bound,b.constant(1)));});
  b.ifNZ(bound,()=>{},()=>b.reject());
  return bound;
}

function buildPrecisionIR(){
  const b=new IR(5),[n,kappa,a,ell,j]=[0,1,2,3,4].map(x=>b.decode(x));
  for(const c of [0,-15,-20,-24,-30,-60])b.ifNZ(b.sabs(b.ssub(n,b.signed(c))),()=>{},()=>b.reject());
  b.ifNZ(b.sabs(kappa),()=>{},()=>b.reject());
  for(const index of [a,ell]){b.ifNZ(index[1],()=>b.reject());b.ifNZ(index[0],()=>{},()=>b.reject());}
  b.ifNZ(b.sabs(b.ssub(j,b.smul(n,a))),()=>b.reject());
  const ep=b.z(b.multiple(ell)),epsNum=b.add(b.sabs(ep.num[0]),b.sabs(ep.num[1])),epsDen=ep.den;
  const bound=maximumPrecisionBoundIR(b,epsNum,epsDen);
  const c=new CappedIR(b,bound),height=c.height();
  let contact=b.signed(1);for(const cc of [0,-15,-20,-24,-30,-60])contact=b.smul(contact,b.ssub(n,b.signed(cc)));
  const required=c.mul(height,c.power(b.sabs(b.smul(kappa,contact)),b.constant(24)));
  b.ifLT(bound,required,()=>b.reject());
  const center=b.fractionDivide(b.z(b.multiple(j)),b.z(b.multiple(a)));
  const error=b.sabs(b.ssub(center.num[0],b.sscaleNat(center.den,n)));
  const left=b.mul(error,epsDen),right=b.mul(epsNum,center.den);
  b.ifLT(left,right,()=>b.accept(),()=>b.reject());
  return b.artifact({decoded:{n,kappa,a,ell,j},epsNum,epsDen,bound,height,required,left,right});
}

function lowerIR(ir){
  const a=new Assembler(ir.inputNames.length),map=Array.from({length:ir.inputNames.length},(_,i)=>i);
  for(let i=map.length;i<ir.registers;i++)map.push(a.temp());
  const accept=a.label(),reject=a.label();
  function setBig(out,value){a.clear(out);for(const bit of BigInt(value).toString(2)){a.addInto(out,out);if(bit==="1")a.add1(out);}}
  function lower(code){for(const c of code){
    const out=map[c.out],x=map[c.x],y=map[c.y];
    if(c.op==="set")setBig(out,c.value);
    else if(c.op==="copy")a.copy(out,x);
    else if(c.op==="add"){let yy=y;if(out===y){yy=a.temp();a.copy(yy,y);}a.copy(out,x);a.addInto(out,yy);}
    else if(c.op==="sub"){const count=a.temp();a.copy(count,y);a.copy(out,x);a.take(count,()=>a.dec(out));}
    else if(c.op==="mul"){const acc=a.temp(),count=a.temp();a.clear(acc);a.copy(count,x);a.take(count,()=>a.addInto(acc,y));a.copy(out,acc);}
    else if(c.op==="div2")a.divmod2(map[c.q],map[c.r],x);
    else if(c.op==="divmod")a.divmod(map[c.q],map[c.r],x,y);
    else if(c.op==="ifNZ")a.ifNZ(x,()=>lower(c.yes),()=>lower(c.no));
    else if(c.op==="ifLT")a.ifLt(x,y,()=>lower(c.yes),()=>lower(c.no));
    else if(c.op==="whileNZ")a.whileNZ(x,()=>lower(c.body));
    else if(c.op==="whileLT"){const loop=a.label(),end=a.label();a.at(loop);a.ifLt(x,y,()=>{lower(c.body);a.jump(loop);},()=>a.jump(end));a.at(end);}
    else if(c.op==="accept")a.jump(accept);
    else if(c.op==="reject")a.jump(reject);
    else throw Error("Unknown IR operation: "+c.op);
  }}
  lower(ir.init);lower(ir.body);a.jump(reject);a.at(reject);a.jump(reject);a.at(accept);
  const total=a.registers;for(let r=0;r<total;r++)a.clear(r);a.code.push({op:"halt"});
  const machine={...a.finish(),inputNames:ir.inputNames,meaning:"accepts_naturals of variable-shift-precision.py; true iff final zero halt",debug:{irMap:map,reject:a.labels.get(reject),cleanup:a.labels.get(accept)}};
  validateProgram(machine.program,machine.registers);return machine;
}

function runIR(ir,inputs,limit=1000000){
  if(inputs.length!==ir.inputNames.length)throw Error("Wrong input count");
  const r=Array(ir.registers).fill(0n);inputs.forEach((x,i)=>{r[i]=BigInt(x);if(r[i]<0n)throw Error("Natural inputs required");});let ticks=0;
  function run(code){for(const c of code){
    if(++ticks>limit)throw Error("IR simulation budget exhausted (not predicate rejection)");
    if(c.op==="set")r[c.out]=BigInt(c.value);
    else if(c.op==="copy")r[c.out]=r[c.x];
    else if(c.op==="add")r[c.out]=r[c.x]+r[c.y];
    else if(c.op==="sub")r[c.out]=r[c.x]>r[c.y]?r[c.x]-r[c.y]:0n;
    else if(c.op==="mul")r[c.out]=r[c.x]*r[c.y];
    else if(c.op==="div2"){const x=r[c.x];r[c.q]=x/2n;r[c.r]=x%2n;}
    else if(c.op==="divmod"){const x=r[c.x],y=r[c.y];if(y===0n)throw Error("unguarded zero division");r[c.q]=x/y;r[c.r]=x%y;}
    else if(c.op==="ifNZ"||c.op==="ifLT"){const yes=c.op==="ifNZ"?r[c.x]!==0n:r[c.x]<r[c.y];const result=run(yes?c.yes:c.no);if(result)return result;}
    else if(c.op==="whileNZ"||c.op==="whileLT"){while(c.op==="whileNZ"?r[c.x]!==0n:r[c.x]<r[c.y]){const result=run(c.body);if(result)return result;}}
    else if(c.op==="accept"||c.op==="reject")return c.op;
    else throw Error("Unknown operation "+c.op);
  }}
  const result=run(ir.init)||run(ir.body);if(!result)throw Error("IR did not decide");return {accepted:result==="accept",ticks,registers:r};
}

module.exports={IR,CappedIR,maximumPrecisionBoundIR,buildPrecisionIR,lowerIR,runIR};
if(require.main===module){
  const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
  const ir=buildPrecisionIR(),machine=lowerIR(ir);
  const save=(name,x)=>{const text=JSON.stringify(x)+"\n";fs.writeFileSync(path.join(__dirname,name),text);return {file:name,bytes:Buffer.byteLength(text),sha256:crypto.createHash("sha256").update(text).digest("hex")};};
  const report={irRegisters:ir.registers,registers:machine.registers,instructions:machine.program.length,files:[save("precision-ir.json",ir),save("precision-machine.json",machine)]};
  fs.writeFileSync(path.join(__dirname,"generation.json"),JSON.stringify(report,null,2)+"\n");console.log(JSON.stringify(report,null,2));
}
