import fs from 'node:fs/promises';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const base=process.argv[2]||process.cwd();
const root=base.replaceAll('\\','/')+'/';
const pr=root+'work/quartic-v14-release/preview-repository/';
const dir=root+'work/source-risk-review-20261107/v14-legacy-normalization-author-001/';
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=async p=>JSON.parse(await fs.readFile(p,'utf8'));
const manifest=await read(dir+'MANIFEST.json');
assert.equal(hash(await fs.readFile(dir+'MANIFEST.json')),'ad19f8b6b18a1057af5854225a9857a6866964a9c951f6104b654a5b2e37455f');
for(const f of manifest.files){const b=await fs.readFile(dir+f.path);assert.equal(hash(b),f.sha256);assert.equal(b.length,f.bytes);}
const applications=await read(dir+'APPLICATIONS.json'),maps=await read(dir+'SOURCE-MAPS.json');
const provenance=await read(dir+'PROVENANCE.json');
const files=new Map(),spans=new Set();
async function walk(x){if(!x||typeof x!=='object')return;if(x.path&&x.sha256){const key=x.path+'@'+x.sha256;let b=files.get(key);if(!b){const resolved=x.path==='manuscripts/quartic_v14.tex'&&x.sha256==='b8421edc569a832c9c4271e3592b10df58e75d25f4dc5619c2b4a6766157044d'?root+'work/source-risk-review-20261107/v14-registry-integration-plan-001/preview-001/registered.tex':pr+x.path;b=await fs.readFile(resolved);files.set(key,b);}assert.equal(hash(b),x.sha256,x.path);if(x.sha256_raw_utf8_span){const lines=b.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];assert.equal(hash(lines.slice(x.start_line-1,x.end_line).join('')),x.sha256_raw_utf8_span,x.path);spans.add(x.path+':'+x.start_line+':'+x.end_line);}}for(const v of Object.values(x))await walk(v);}
await walk(applications);await walk(maps);
const dims=['source_hypotheses','constructed_objects','index_domain_coverage','transition_maps','consumed_object_identity','coefficient_conventions','local_conditions','exceptional_cases','downstream_consumption'].sort();
assert.equal(applications.length,87);assert.equal(new Set(applications.map(x=>x.id)).size,87);
for(const a of applications){assert.deepEqual(Object.keys(a.obligations).sort(),dims);assert.deepEqual(a.authors,['01a1bec6-0130-7a60-9b2e-a56bb4ae7c18']);const m=maps.find(x=>x.id===a.id);if(a.kind==='editorial'){assert.equal(a.dependencies.length,0);assert(m.consumer_edges.every(e=>e.role==='archived'));}else if(a.id.startsWith('V13-'))assert.deepEqual(a.dependencies,[...new Set(m.edges.filter(e=>e.role==='current_consumer'||e.role==='supporting_derivation').map(e=>e.entryId))]);}
const old=await read(pr+'docs/manuscript-revisions/version14/APPLICATIONS.json');
const mapping={source_hypotheses:'required_inputs',constructed_objects:'constructed_inputs',index_domain_coverage:'domain_and_index_coverage',transition_maps:'transition_maps_and_scalars',consumed_object_identity:'identity_of_consumed_object',exceptional_cases:'exceptional_cases',downstream_consumption:'affected_downstream_claims'};
for(const a of applications.slice(0,39)){const o=old.applications.find(x=>x.id===a.id);for(const [n,k]of Object.entries(mapping))assert.equal(a.obligations[n].required,o.obligations[k]);const p=provenance.find(x=>x.id===a.id);assert.equal(p.original_prior_record_sha256,o.priorRecordSha256);assert.deepEqual(p.original_source_version_and_conventions,o.sourceVersionAndConventions);assert.equal(typeof p.original_validation_scope,'string');}
console.log(JSON.stringify({status:'pass',applications:87,source_files:files.size,raw_spans:spans.size,kinds:Object.fromEntries([...new Set(applications.map(a=>a.kind))].map(k=>[k,applications.filter(a=>a.kind===k).length])),scope:'Pins, dimensions, legacy required mappings, provenance and edge classification only; semantic review is separate.'},null,2));
