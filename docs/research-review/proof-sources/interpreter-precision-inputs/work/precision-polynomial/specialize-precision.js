"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const root=path.resolve(__dirname,"../..");
const sha=x=>crypto.createHash("sha256").update(x).digest("hex");
const locks={
  "outputs/universal-interpreter.js":"6b5576f57ef861cff4ef088c02f4acd6c3f5369cfab991e93edbab26cc1decd5",
  "outputs/integer-diophantine-compiler.js":"c0c7e8f738fe9b7a07c82be1429e1924b772cd360058dc14f2b331555b1dc893",
  "outputs/universal-integer-polynomial.json":"27a840c06c68bfae88da84a934d6e7f0ca2778dd3e56ec2bf3b4d4eb8171fe04",
  "work/precision-register/precision-machine.json":"ec4fb8c7ce2e3448071fa352e94a38e427e0899328633c93d7130c5ac1da98cd"
};
function checkedRead(name){const data=fs.readFileSync(path.join(root,name));if(sha(data)!==locks[name])throw Error("Pinned source changed: "+name);return data;}
checkedRead("outputs/universal-interpreter.js");checkedRead("outputs/integer-diophantine-compiler.js");
const {Assembler,encodeProgram}=require("../../outputs/universal-interpreter.js");
const {validateProgram}=require("../../outputs/integer-diophantine-compiler.js");

function unpair(a,head,tail,code){
  if(head===tail)throw Error("Distinct pair outputs required");
  const rem=a.temp(),sum=a.temp(),count=a.temp(),loop=a.label(),done=a.label();
  a.copy(rem,code);a.clear(sum);a.at(loop);
  a.ifLt(sum,rem,()=>{
    a.copy(count,sum);a.add1(count);a.take(count,()=>a.dec(rem));a.add1(sum);a.jump(loop);
  },()=>{
    a.copy(head,sum);a.copy(count,rem);a.take(count,()=>a.dec(head));a.copy(tail,rem);a.jump(done);
  });
  a.at(done);
}
function buildWrapper(main){
  validateProgram(main.program,main.registers);
  const a=new Assembler(main.registers),rest=a.temp();
  for(let i=0;i<4;i++)unpair(a,i,rest,i===0?0:rest);
  a.copy(4,rest);
  const scratchEnd=a.registers;for(let r=main.registers;r<scratchEnd;r++)a.clear(r);
  const prefix=a.finish(),offset=prefix.program.length;
  const relocated=main.program.map(x=>x.op==="halt"?{op:"halt"}:x.op==="add"?{op:"add",register:x.register,next:x.next+offset}:{op:"sub",register:x.register,nonzero:x.nonzero+offset,zero:x.zero+offset});
  const wrapper={registers:prefix.registers,program:prefix.program.concat(relocated),inputNames:["packed_codes"],meaning:"Inverse four Cantor pairs, then the unchanged five-input precision machine",prefix:{length:offset,scratchStart:main.registers,scratchEnd,mainEntry:offset},sourceMachineSHA256:locks["work/precision-register/precision-machine.json"]};
  validateProgram(wrapper.program,wrapper.registers);return wrapper;
}

// Mutates a private parsed copy of H; no original artifact is written.
function specialize(H,programCode,metadata={}){
  const oldVariableCount=H.variableCount||H.variables.length,oldRoot=H.root,oldNodeCount=H.nodes.length;
  const oldE=H.variables.find(v=>v.index===0),oldN=H.variables.find(v=>v.index===1);
  if(!oldE||!oldN||oldE.kind!=="input"||oldN.kind!=="input")throw Error("Expected two original inputs");
  if(H.nodes[oldE.node].op!=="var"||H.nodes[oldE.node].args[0]!==0||H.nodes[oldN.node].op!=="var"||H.nodes[oldN.node].args[0]!==1)throw Error("Input node mismatch");
  for(const n of H.nodes){
    if(n.op==="var"){
      if(n.args[0]===0){n.op="const";n.args=[BigInt(programCode).toString()];}
      else n.args[0]=n.args[0]===1?5:n.args[0]+7;
    }else if(n.op==="call")n.args[n.args.length-1]+=7;
  }
  H.variables=H.variables.filter(v=>v.index>=2).map(v=>({...v,index:v.index+7}));
  H.witnessBlocks=(H.witnessBlocks||[]).map(b=>({...b,start:b.start+7}));
  const node=(op,args)=>{const id=H.nodes.length;H.nodes.push({op,args});return id;};
  const add=(a,b)=>node("add",[a,b]),mul=(a,b)=>node("mul",[a,b]);
  const codes=Array.from({length:5},(_,i)=>{const n=node("var",[i]);H.variables.push({index:i,name:"code_"+i,kind:"input",node:n});return n;});
  const tuples=[oldN.node];H.variables.push({index:5,name:"tuple_0",kind:"witness",node:oldN.node});
  for(let i=1;i<4;i++){const n=node("var",[5+i]);tuples.push(n);H.variables.push({index:5+i,name:"tuple_"+i,kind:"witness",node:n});}
  const one=node("const",["1"]),two=node("const",["2"]),minusOne=node("const",["-1"]);
  const equations=[];
  for(let i=0;i<4;i++){
    const a=codes[i],b=i===3?codes[4]:tuples[i+1],t=tuples[i];
    const sum=add(a,b),product=mul(sum,add(sum,one));
    equations.push(add(mul(two,t),mul(minusOne,add(product,mul(two,b)))));
  }
  let result=mul(oldRoot,oldRoot);for(const q of equations)result=add(result,mul(q,q));
  H.root=result;H.variableCount=oldVariableCount+7;H.inputNames=codes.map((_,i)=>"code_"+i);H.variables.sort((a,b)=>a.index-b.index);
  delete H.formula;delete H.formulas;delete H.macroCounts;
  H.metadata={meaning:"Five-natural-input precision predicate via four Cantor equations and a fixed universal-H specialization",inputNames:H.inputNames,variableDomain:"nonnegative integers",sourceUniversalSHA256:locks["outputs/universal-integer-polynomial.json"],sourceMachineSHA256:locks["work/precision-register/precision-machine.json"],sourceUniversalRoot:oldRoot,sourceUniversalNodeCount:oldNodeCount,sourceUniversalVariableCount:oldVariableCount,codeNodes:codes,tupleNodes:tuples,pairingEquationNodes:equations,programCodeNode:oldE.node,...metadata};
  return H;
}

function main(){
  const started=Date.now(),machine=JSON.parse(checkedRead("work/precision-register/precision-machine.json")),wrapper=buildWrapper(machine);
  const code=encodeProgram(wrapper.program),hex=code.toString(16)+"\n";
  const wrapperText=JSON.stringify(wrapper)+"\n";
  fs.writeFileSync(path.join(__dirname,"precision-wrapper.json"),wrapperText);
  fs.writeFileSync(path.join(__dirname,"precision-wrapper-code.hex"),hex);
  const H=JSON.parse(checkedRead("outputs/universal-integer-polynomial.json"));
  const artifact=specialize(H,code,{wrapperSHA256:sha(wrapperText),wrapperCodeHexSHA256:sha(hex)});
  const polynomialText=JSON.stringify(artifact)+"\n";
  fs.writeFileSync(path.join(__dirname,"precision-natural-polynomial.json"),polynomialText);
  const codeDecimal=artifact.nodes[artifact.metadata.programCodeNode].args[0];
  const report={format:"precision-specialization-generation-v1",sourceLocks:locks,wrapper:{registers:wrapper.registers,instructions:wrapper.program.length,prefixLength:wrapper.prefix.length,bytes:Buffer.byteLength(wrapperText),sha256:sha(wrapperText)},programCode:{bits:code.toString(2).length,hexDigits:hex.length-1,decimalDigits:codeDecimal.length,hexFileSHA256:sha(hex)},polynomial:{file:"precision-natural-polynomial.json",inputCount:5,totalVariables:artifact.variableCount,witnessCount:artifact.variableCount-5,parentNodes:artifact.nodes.length,ordinaryVariableRecords:artifact.variables.length,witnessBlocks:artifact.witnessBlocks.length,templateCount:artifact.templates.length,templateNodes:artifact.templates.map(t=>t.nodes.length),bytes:Buffer.byteLength(polynomialText),sha256:sha(polynomialText)},elapsedMilliseconds:Date.now()-started,rss:process.memoryUsage().rss};
  fs.writeFileSync(path.join(__dirname,"specialization-generation.json"),JSON.stringify(report,null,2)+"\n");console.log(JSON.stringify(report,null,2));return report;
}
module.exports={locks,unpair,buildWrapper,specialize,main};
if(require.main===module)main();
