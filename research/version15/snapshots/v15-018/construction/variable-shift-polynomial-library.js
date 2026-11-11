"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {buildFiniteModel,finiteArtifact,auditFiniteLibrary}=require("./finite-polynomial-expressions.js");
const {EllipticCore}=require("./rational-elliptic-core.js");
const {fixedMultiple}=require("./rational-model-assembly.js");
const CONTACTS=[0,-15,-20,-24,-30,-60];
const names=(prefix)=>Array.from({length:5},(_,i)=>prefix+"."+i);
const fieldScale=(b,x,s)=>x.map(v=>b.mul(s,v));
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(path.join(__dirname,p))).digest("hex");
const SOURCE_FILES=["z-in-q-variable-shift-bridge.txt","z-in-q-final-bridge-independent-audit.txt",
 "finite-polynomial-expressions.js","rational-elliptic-core.js","rational-polynomial-library.js","rational-model-assembly.js"];
function addVariableShiftTemplates(library){
 // These are finite coordinate templates, not the missing precision relation.
 const ids={};
 const signed={meaning:"N=iota(decode_signed(C)), using one natural code Q",decode_signed:"even c: c/2; odd c: -(c+1)/2",bindings:{}};
 ids.signed_encode=library.define("value.signed_encode",names("N").concat(names("C")),(b,p)=>{
  const e=new EllipticCore(b),N=p.slice(0,5),C=p.slice(5),Q=e.point("Q"),twice=e.point("twiceQ"),plus=e.point("QplusP");
  signed.bindings={N,C,Q,twice,plus};
  return b.and(b.call("member",N),b.call("member",C),b.call("natural",Q),
   b.call("raw_add",Q.concat(Q,twice)),
   b.or(b.and(e.peq(N,Q),e.peq(C,twice)),
    b.and(b.call("raw_add",Q.concat(e.P(),plus)),e.peq(N,e.neg(plus)),
     b.call("raw_add",twice.concat(e.P(),C)))));
 },signed);
 const abs={meaning:"a is the ordinary rational absolute value of x; a is a sum of four rational squares"};
 ids.abs=library.define("value.abs",["x","a"],(b,[x,a])=>{
  const squares=Array.from({length:4},(_,i)=>b.fresh("nonnegative_square."+i));
  return b.and(b.eq(a,b.add(...squares.map(s=>b.square(s)))),b.eq(b.square(a),b.square(x)));
 },abs);
 const close={meaning:"Actual coordinate window |t-Tr(z(J)/z(A))/2| < |coeff0(z(L))|+|coeff1(z(L))|",precisionRelationIncluded:false,bindings:{},positive:[]};
 ids.close_coordinates=library.define("value.close_coordinates",names("A").concat(names("L"),names("J"),["t"]),(b,p)=>{
  const e=new EllipticCore(b),A=p.slice(0,5),L=p.slice(5,10),J=p.slice(10,15),t=p[15],
   za=e.ff("z.A"),zl=e.ff("z.L"),zj=e.ff("z.J"),ratio=e.fdiv(zj,za,"ratio"),
   a0=b.fresh("abs.zL.0"),a1=b.fresh("abs.zL.1"),epsilon=b.add(a0,a1),
   r=ratio.value[0],distance=b.fresh("distance"),margin=b.sub(epsilon,distance),positive=b.positive(margin,"strict_window");
  close.bindings={A,L,J,t,za,zl,zj,ratio:ratio.value,a0,a1,epsilon,r,distance,margin};close.positive=[[positive,margin]];
  return b.and(b.call("member",A),b.call("member",L),b.call("member",J),e.finite(A),e.finite(L),
   e.z(A,za,"z.A"),e.z(L,zl,"z.L"),e.z(J,zj,"z.J"),ratio.formula,
   b.call("value.abs",[zl[0],a0]),b.call("value.abs",[zl[1],a1]),
   b.nonzero(epsilon,"epsilon.inverse"),b.call("value.abs",[b.sub(t,r),distance]),positive);
 },close);
 const test={meaning:"The six raw field-valued tests and exact single pole predicate of variable-shift bridge section 3",contacts:CONTACTS,usesRawZRatios:true,usesFormalLogarithm:false,bindings:{}};
 ids.test=library.define("value.test",names("N").concat(names("Kappa"),["t"]),(b,p)=>{
  const e=new EllipticCore(b),N=p.slice(0,5),Kappa=p.slice(5,10),t=p[10],C1=e.point("C1"),H=e.point("H"),U=e.point("U"),V0=e.point("V0"),V1=e.point("V1"),f=[];
  for(const point of [N,Kappa,C1,H,U,V0,V1])f.push(b.call("member",point));
  f.push(e.finite(Kappa),b.call("multiply",Kappa.concat(N,C1)),
   b.call("raw_add",H.concat(e.neg(Kappa),V0)),b.call("raw_add",U.concat(e.neg(C1),V1)),e.finite(H),e.finite(V0));
  const points=[H,U,V0,V1],ws=[],zs=[];
  points.forEach((point,i)=>{
   const w=e.ff("w."+i),z=e.ff("z."+i);ws.push(w);zs.push(z);
   f.push(e.inverseX(point,w,"w."+i),e.z(point,z,"z."+i));
  });
  const r0=e.fdiv(zs[1],zs[0],"raw_ratio.0"),r1=e.fdiv(zs[3],zs[2],"raw_ratio.1");
  f.push(r0.formula,r1.formula);
  const rationalT=[t,b.constant(0)],D=[ws[0],ws[1],e.fconj(ws[2]),e.fconj(ws[3]),e.fsub(r0.value,rationalT),e.fsub(e.fconj(r1.value),rationalT)],
   F=b.mul(...CONTACTS.map(c=>b.sub(t,b.constant(c)))),eta=b.fresh("eta"),q=b.fresh("q"),R0=b.fresh("R0"),a0=b.fresh("a0"),R=b.fresh("R");
  f.push(b.nonzero(F,"F.inverse"),b.eq(b.square(eta),b.constant(1)),
   b.eq(R0,b.mul(eta,b.constant(2730n**6n),F)),b.eq(a0,b.sub(b.constant(1),b.mul(R0,b.square(q)))),
   b.nonzero(a0,"a0.inverse"),b.eq(R,b.mul(R0,b.square(a0))));
  const C=D.map((d,i)=>{const c=e.ff("normalized."+i);f.push(e.feq(fieldScale(b,c,F),d));return c;});
  let W=e.fc(1);
  for(const c of C)W=e.fmul(W,e.fadd(e.fc(1),fieldScale(b,e.fsquare(c),R)));
  const inverse=e.fdiv(e.fc(1),W,"W.inverse"),theta=b.fresh("Theta"),B=b.fresh("Bpole");
  f.push(inverse.formula,b.eq(theta,b.scale(2,inverse.value[0])),b.nonzero(theta,"Theta.inverse"),
   b.eq(b.mul(B,b.square(theta)),R),b.call("pole",[B]));
  test.bindings={N,Kappa,t,C1,H,U,V0,V1,ws,zs,ratios:[r0.value,r1.value],D,F,eta,q,R0,a0,R,C,W,inverseW:inverse.value,theta,B};
  return b.and(...f);
 },test);
 const exceptions={meaning:"Exactly the six branches N=iota(c) and t=c",contacts:CONTACTS,bindings:{}};
 ids.exceptions=library.define("value.exceptions",names("N").concat(["t"]),(b,p)=>{
  const e=new EllipticCore(b),N=p.slice(0,5),t=p[5],branches=[];
  CONTACTS.forEach(c=>{const s=fixedMultiple(b,e,e.P(),BigInt(c),"constant."+c);
   branches.push(b.and(s.formula,e.peq(N,s.value),b.eq(t,b.constant(c))));});
  exceptions.bindings={N,t};return b.and(b.call("member",N),b.or(...branches));
 },exceptions);
 return ids;
}
function buildVariableShiftLibrary(){const library=buildFiniteModel();addVariableShiftTemplates(library);return library;}
function artifact(){return finiteArtifact(buildVariableShiftLibrary(),{},{
 meaning:"Finite signed/coordinate/Test/exceptional pieces for the variable-shift value bridge",
 sourceHashes:Object.fromEntries(SOURCE_FILES.map(p=>[p,hash(p)])),
 excluded:["translated five-natural-input precision relation","whole Close","whole Val","proof of model arithmetic","proof of global height/pole completeness"]});}
module.exports={CONTACTS,SOURCE_FILES,addVariableShiftTemplates,buildVariableShiftLibrary,artifact};
if(require.main===module){const a=artifact(),audit=auditFiniteLibrary(a);
 fs.writeFileSync(path.join(__dirname,"variable-shift-polynomial-library.json"),JSON.stringify(a)+"\n");
 fs.writeFileSync(path.join(__dirname,"variable-shift-polynomial-structure.json"),JSON.stringify(audit,null,2)+"\n");
 console.log(JSON.stringify(audit.templates.filter(t=>t.name.startsWith("value.")),null,2));}
