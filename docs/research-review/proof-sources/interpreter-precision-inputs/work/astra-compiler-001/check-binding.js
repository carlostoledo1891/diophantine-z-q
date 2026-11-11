"use strict";
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../..');
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const pins={};
const read=p=>{const b=fs.readFileSync(path.join(root,p));pins[p]=sha(b);return b;};
const json=p=>JSON.parse(read(p));
const expected={
 'outputs/integer-diophantine-compiler.js':'c0c7e8f738fe9b7a07c82be1429e1924b772cd360058dc14f2b331555b1dc893',
 'outputs/hierarchical-integer-compiler.js':'0c933abc1fb04f294d48d18943f6b9484c8663655a472644c8cc955e1c4abbee',
 'outputs/universal-interpreter.js':'6b5576f57ef861cff4ef088c02f4acd6c3f5369cfab991e93edbab26cc1decd5',
 'outputs/universal-integer-polynomial.json':'27a840c06c68bfae88da84a934d6e7f0ca2778dd3e56ec2bf3b4d4eb8171fe04',
 'work/precision-register/precision-register.js':'ae4d930c83bb5ac9dd878df22d43079e1972855bff30e4e20d2a05a5989c4af9',
 'work/precision-polynomial/specialize-precision.js':'4b31cf8719f060ce54735737318e916be85634d6ea8f6f0d156dc7752d69d0cf',
 'work/precision-polynomial/precision-natural-polynomial.json':'f3e163f5c60b972c98b48647274f956dd7d78428e27ddc0543574a5f18120b8c',
 'formalization/z-in-q/ProofSources/work/Exponentiation.thy.txt':'203431b551fd0ca218722583a2ba62c5959d8e72aea8c47eca975118e74f0946'
};
for(const [p,h] of Object.entries(expected)){read(p);assert.equal(pins[p],h,p);}
const U=require(path.join(root,'outputs/universal-interpreter.js'));
const HC=require(path.join(root,'outputs/hierarchical-integer-compiler.js'));
const PR=require(path.join(root,'work/precision-register/precision-register.js'));
const SP=require(path.join(root,'work/precision-polynomial/specialize-precision.js'));
const checks=[];
function eq(name,a,b){assert.deepEqual(a,b,name);checks.push(name);console.log(name);}
const machine=U.buildUniversalInterpreter(),savedMachine=json('outputs/universal-interpreter-program.json');
eq('universal program',machine,savedMachine);
const freshH=HC.compileHierarchical(machine.program,machine.registers,['e','n']);
const H=json('outputs/universal-integer-polynomial.json');
for(const key of ['nodes','root','variables','variableCount','templates','witnessBlocks'])eq('H '+key,freshH[key],H[key]);
const structure=HC.auditStructure(H);
const ir=PR.buildPrecisionIR(),savedIR=json('work/precision-register/precision-ir.json');
eq('precision IR',ir,savedIR);
const pm=PR.lowerIR(ir),savedPM=json('work/precision-register/precision-machine.json');
eq('precision primitive program',pm,savedPM);
const wrapper=SP.buildWrapper(pm),savedWrapper=json('work/precision-polynomial/precision-wrapper.json');
eq('precision wrapper',wrapper,savedWrapper);
const code=U.encodeProgram(wrapper.program),hex=code.toString(16)+'\n';
eq('wrapper code',hex,read('work/precision-polynomial/precision-wrapper-code.hex').toString());
const wrapperText=JSON.stringify(wrapper)+'\n';
const specialized=SP.specialize(H,code,{wrapperSHA256:sha(wrapperText),wrapperCodeHexSHA256:sha(hex)});
const savedN=json('work/precision-polynomial/precision-natural-polynomial.json');
eq('entire precision natural artifact',specialized,savedN);
const receipt={date:'2026-11-04',status:'PASS',checks,structure,pins,precisionVariables:savedN.variableCount,scope:'Source regeneration and exact JSON identity. Mathematical semantics proved separately in report.md.'};
fs.writeFileSync(path.join(__dirname,'binding-receipt.json'),JSON.stringify(receipt,null,2)+'\n');
console.log(JSON.stringify({status:receipt.status,checks:checks.length,precisionVariables:receipt.precisionVariables}));
