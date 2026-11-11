import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const workspace="C:/Users/glaze/Documents/Codex/2026-11-02/lo", repo=path.join(workspace,'work/quartic-v14-release/preview-repository'), out=path.join(workspace,'work/source-risk-review-20261107/v14-legacy-normalization-author-001');
const H=b=>crypto.createHash('sha256').update(b).digest('hex');
const APath='docs/manuscript-revisions/version14/APPLICATIONS.json', SPath='docs/manuscript-revisions/version14/evidence/selected-entries.json', MPath='manuscripts/quartic_v14.tex';
const Araw=await fs.readFile(path.join(repo,APath)),Sraw=await fs.readFile(path.join(repo,SPath)),A=JSON.parse(Araw),S=JSON.parse(Sraw);
assert.equal(H(Araw),'b6afe631461d60dec2b23bf0fea9c492726bd6605af535497fd72beb39f9a9f1');
assert.equal(H(Sraw),'8df367e0fb28f624a3ab019cb4935f66f6315e97ae5840854e2c33512e6875bc');
const D=JSON.parse(await fs.readFile(path.join(workspace,'work/source-risk-review-20261107/v14-current-inventory-003/DELTA.json')));
const authored=JSON.parse(await fs.readFile(path.join(out,'AUTHORED-SEMANTICS.json'))), {semantics,localProfiles,legacyExtra}=authored;
const fileCache=new Map(), spanChecks=new Map();
async function file(p){if(!fileCache.has(p)) fileCache.set(p,await fs.readFile(path.join(repo,p))); return fileCache.get(p);}
async function pin(p){return {side:'head',path:p,sha256:H(await file(p))};}
const AP=await pin(APath),SP=await pin(SPath),MP=await pin(MPath);assert.equal(MP.sha256,'1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8');
async function validate(s){const b=await file(s.path);assert.equal(H(b),s.sha256,s.path);if(s.start_line){const lines=b.toString('utf8').match(/[^\n]*\n|[^\n]+$/g)||[];assert.equal(H(Buffer.from(lines.slice(s.start_line-1,s.end_line).join(''))),s.sha256_raw_utf8_span,JSON.stringify(s));spanChecks.set(JSON.stringify(s),s);}return {side:'head',path:s.path,sha256:s.sha256};}
function transport(s){if(s.sha256===MP.sha256)return s;const x=D.changes.find(c=>c.raw_bytes_identical&&JSON.stringify(c.before)===JSON.stringify(s));assert(x,'missing transport '+JSON.stringify(s));return x.after;}
function unique(rows){return [...new Map(rows.map(r=>[JSON.stringify(r),r])).values()];}
async function evidence(spans,extra=[]){return unique([AP,...extra,...await Promise.all(spans.map(validate))]);}
const proposals=[],provenance=[],mapping=[];
const dimensions=['source_hypotheses','constructed_objects','index_domain_coverage','transition_maps','consumed_object_identity','coefficient_conventions','local_conditions','exceptional_cases','downstream_consumption'];
function obligation(required,constructed,justification,evidence,status='checked'){assert(required&&constructed&&justification&&evidence.length);return {status,required,constructed,justification,evidence};}
const oldMap={source_hypotheses:'required_inputs',constructed_objects:'constructed_inputs',index_domain_coverage:'domain_and_index_coverage',transition_maps:'transition_maps_and_scalars',consumed_object_identity:'identity_of_consumed_object',exceptional_cases:'exceptional_cases',downstream_consumption:'affected_downstream_claims'};
for(let i=0;i<A.applications.length;i++){
 const a=A.applications[i],o=a.obligations,extra=legacyExtra[a.id.slice(4)];assert(extra,a.id);
 const edges=A.edgeBindings.filter(e=>e.applicationId===a.id&&e.role!=='archived');
 const obligations={},all=[];
 for(const [key,old] of Object.entries(oldMap)){
  const loc=a.dependencyDisposition[old];assert(loc,a.id+old);
  const ev=await evidence([...loc.sourceSpans,...loc.consumerSpans]);all.push(...ev);
  let constructed=o[old],just=loc.justification;
  if(key==='source_hypotheses')constructed=o.constructed_inputs+' Domain: '+o.domain_and_index_coverage;
  if(key==='constructed_objects')just=o.transition_maps_and_scalars+' '+loc.justification;
  if(key==='consumed_object_identity')just=o.transition_maps_and_scalars+' '+o.exceptional_cases;
  if(key==='downstream_consumption')just+=' Current direct selected suppliers: '+edges.map(e=>e.entryId).join(', ')+'.';
  obligations[key]=obligation(o[old],constructed,just,ev);
 }
 const loc=a.dependencyDisposition.source_version_and_conventions;
 const ev=await evidence([...loc.sourceSpans,...loc.consumerSpans]);all.push(...ev);
 obligations.coefficient_conventions=obligation(extra[0],extra[0],o.source_version_and_conventions+' This is a new coefficient/convention obligation; the historical source-version field is retained separately, not renamed as an equivalent dimension.',ev);
 const local=localProfiles[extra[1]];
 obligations.local_conditions=obligation(local.text,local.text+' Specific domain: '+o.domain_and_index_coverage,'Apply only to this contract: '+o.required_inputs+' Exceptional scope: '+o.exceptional_cases,ev,local.status);
 const dependencies=[...new Set(edges.map(e=>e.entryId))].sort();
 proposals.push({id:a.id,kind:['V13-FINITE-COUNTS','V13-SOS-FINITE'].includes(a.id)?'computation':'argument',authors:[authored.author_run],dependencies,files:unique(all),obligations});
 provenance.push({id:a.id,author:authored.author,author_run:authored.author_run,source:{...AP,json_pointer:'/applications/'+i},original_prior_record_sha256:a.priorRecordSha256,original_source_version_and_conventions:a.sourceVersionAndConventions,original_validation_scope:o.validation_and_acceptance_scope,scope:'New current adoption proposal; original author_records_pending_independent_review and all historical decisions are unchanged. No independent acceptance is fabricated.'});
 mapping.push({id:a.id,dimension_map:Object.fromEntries(Object.entries(oldMap).map(([k,v])=>[k,{source_dimension:v,...a.dependencyDisposition[v]}])),new_dimensions:{coefficient_conventions:{authored_statement:extra[0],source:loc},local_conditions:{profile:extra[1],authored_statement:local.text,source:loc}},edges});
}
for(let i=0;i<S.entries.length;i++){
 const e=S.entries[i],n=e.entryId.split('-')[0],data=semantics[n],current=e.currentDerivationSpans.map(transport);
 const src=e.portableProofSpans||[],ev=await evidence([...src,...current], [SP,...await Promise.all((e.portableReviewPins||[]).map(validate))]);
 const edges=A.edgeBindings.filter(x=>x.entryId===e.entryId),active=edges.filter(x=>x.role!=='archived');
 const obligations={};
 if(data){
  assert(current.length,e.entryId);const [hyp,obj,domain,maps,except,coef,lp,output]=data,local=localProfiles[lp];
  const reason='Authored conditional source-fragment proposal at the exact current spans. '+e.justification+' The stated incoming hypotheses remain explicit; source binding and historical review are not an independent acceptance of this new proposal.';
  obligations.source_hypotheses=obligation(hyp,hyp,reason,ev);
  obligations.constructed_objects=obligation(obj,obj,maps,ev);
  obligations.index_domain_coverage=obligation(domain,domain,except,ev);
  obligations.transition_maps=obligation(maps,maps,'The current source gives the displayed construction, identity or estimate on precisely this domain: '+domain,ev);
  obligations.consumed_object_identity=obligation('The consumer must use these actual objects: '+obj,obj+' Output: '+output,maps+' '+except,ev);
  obligations.coefficient_conventions=obligation(coef,coef,'These literal constants/signs/scales are retained in the current source; no historical alternative is substituted.',ev);
  obligations.local_conditions=obligation(local.text,local.text+' Domain: '+domain,hyp+' '+except,ev,local.status);
  obligations.exceptional_cases=obligation(except,except,'The construction is asserted only on its recorded domain. '+domain,ev);
  obligations.downstream_consumption=obligation(output,output,'Current mapped consumers: '+[...new Set(active.map(x=>x.applicationId))].join(', ')+'. Incoming requirements are not silently discharged by this fragment.',ev);
 } else {
  assert.equal(current.length,0);assert(edges.every(x=>x.role==='archived'));
  for(const dim of dimensions){const activeDim=['source_hypotheses','constructed_objects','consumed_object_identity','downstream_consumption'].includes(dim);
   obligations[dim]=obligation('Preserve the disposition '+e.disposition+' of '+e.entryId+'.',e.justification,'Editorial research-history classification only. Every recorded edge is archived and there is no current derivation span. No mathematical result from this item is adopted as a current supplier.',ev,activeDim?'checked':'not_applicable');
  }
 }
 proposals.push({id:e.entryId,kind:data?'source':'editorial',authors:[authored.author_run],dependencies:[],files:ev,obligations});
 provenance.push({id:e.entryId,author:authored.author,author_run:authored.author_run,source:{...SP,json_pointer:'/entries/'+i},original_disposition:e.disposition,original_new_acceptance_created:e.newAcceptanceCreated,historical_proof:e.historicalAuthorProof,historical_review:e.historicalRecordedReview,scope:data?'Conditional current source-fragment adoption, with historical proof/review scope preserved.':'Editorial disposition only; excluded from active mathematical dependencies.'});
 mapping.push({id:e.entryId,original_derivation_spans:e.currentDerivationSpans,current_derivation_spans:current,portable_proof_spans:src,consumer_edges:edges,scope:data?'Current fragments plus exact consumer mapping; no assertion of a complete upstream graph.':'No current derivation or active consumer.'});
}
assert.equal(proposals.length,87);const ids=new Set(proposals.map(x=>x.id));assert.equal(ids.size,87);
for(const p of proposals){assert.deepEqual(Object.keys(p.obligations).sort(),dimensions.slice().sort());for(const d of p.dependencies)assert(ids.has(d));for(const o of Object.values(p.obligations)){assert(['checked','not_applicable'].includes(o.status));for(const e of o.evidence)assert(p.files.some(f=>JSON.stringify(f)===JSON.stringify(e)));}for(const f of p.files)assert.equal(H(await file(f.path)),f.sha256);}
assert.equal(H(await fs.readFile(path.join(repo,APath))),H(Araw));assert.equal(H(await fs.readFile(path.join(repo,SPath))),H(Sraw));
const stats={status:'AUTHOR_CHECK_PASS_NOT_INDEPENDENT_ACCEPTANCE',applications:87,legacy_adoptions:39,current_source_fragments:37,editorial_historical_dispositions:11,unique_source_files:fileCache.size,unique_raw_spans:spanChecks.size,original_inventories_unchanged:true,complete_upstream_graph_claimed:false,author:authored.author,author_run:authored.author_run};
const readme='# Current legacy and transformation adoption proposals\n\nAuthor: '+authored.author+'; observed desktop run '+authored.author_run+'. This is new proposal authorship, not a claim to have authored the historical mathematics. Add this author to the final coverage forbidden-author union. The run still needs the normal authenticated gate binding.\n\nAPPLICATIONS.json contains 39 current legacy-contract adoptions, 37 conditional current source-fragment proposals and 11 editorial historical-disposition proposals. checked means the present author asserts the specified obligation within that proposal; it is not an independent approval or a change to any historical status. The latter 11 have no active mathematical edges. All exact source/consumer spans are in SOURCE-MAPS.json. PROVENANCE.json preserves prior statuses, original source versions and review scopes.\n\nSeven legacy dimensions use their actual semantically matching current statements; coefficient_conventions and local_conditions are separately authored in AUTHORED-SEMANTICS.json. They are not obtained by renaming source_version_and_conventions or validation_scope. The N fragments state their incoming hypotheses expressly. Existing current/supporting V13-to-N edges are preserved; archived edges remain provenance. This batch does not claim a complete upstream graph: final source-first reconstruction and reconciliation must determine missing supplier edges and whole-assembly closure.\n\nDo not expose these declared proposals to the source-first reviewer before its independent freeze. Independent review and final authenticated runtime authorship remain required. No canonical file is edited.\n';
for(const [name,value] of Object.entries({'APPLICATIONS.json':proposals,'PROVENANCE.json':provenance,'SOURCE-MAPS.json':mapping,'CHECKS.json':stats}))await fs.writeFile(path.join(out,name),JSON.stringify(value,null,2)+'\n');
await fs.writeFile(path.join(out,'README.md'),readme);
const names=['AUTHORED-SEMANTICS.json','APPLICATIONS.json','PROVENANCE.json','SOURCE-MAPS.json','CHECKS.json','README.md','prepare.mjs'];
const pins=[];for(const name of names){const b=await fs.readFile(path.join(out,name));pins.push({path:name,sha256:H(b),bytes:b.length});}
await fs.writeFile(path.join(out,'MANIFEST.json'),JSON.stringify({author:authored.author,author_run:authored.author_run,status:'new current proposals requiring independent review',files:pins},null,2)+'\n');
console.log(JSON.stringify(stats));
