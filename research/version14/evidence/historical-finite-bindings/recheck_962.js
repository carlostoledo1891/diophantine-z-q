// Only the report in this proposal directory is written.
const path=require('path');
const fs=require('fs');
if(!process.argv[2])throw Error('Usage: node recheck_962.js REPOSITORY [REPORT]');
const repo=path.resolve(process.argv[2]);
const p=path.join(repo,'quartics/quartic-962');
const checker=require(path.join(p,'checker/checker.cjs'));
const r=checker.run({input:path.join(p,'raw-translated-ir.json'),compiled:path.join(p,'compiled-ir.json'),certificate:path.join(p,'reduction-certificate.json'),coordinateMap:path.join(p,'coordinate-map.json'),quartic:path.join(p,'polynomial.json')});
for(const item of Object.values(r.artifactHashes))item.file=path.relative(repo,item.file).replaceAll('\\','/');
if(process.argv[3])fs.writeFileSync(path.resolve(process.argv[3]),JSON.stringify(r,null,2)+'\n');
console.log(JSON.stringify({status:r.status,coordinates:r.coordinateCount,residuals:r.residualCount,degree:r.statistics.degree,monomials:r.statistics.monomials,content:r.statistics.primitiveContent,gates:r.gateIdentities.checked,certificate_operations:r.transformation.operations}));
