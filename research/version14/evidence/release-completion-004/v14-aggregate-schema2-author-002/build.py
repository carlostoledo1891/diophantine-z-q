import copy,hashlib,json
from pathlib import Path
W=Path.cwd(); P=Path(__file__).parent; A=P.parent/'v14-aggregate-schema2-author-001'
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x): (P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert sha(A/'MANIFEST.json')=='91d03dbfca6909de883f7a4f618aed27716fb69930232b90caea69370001ef2b'
h6=load(A/'H6-APPLICATIONS.json'); agg=load(A/'AGGREGATE.json')
author='01a1bed7-e1a5-71d2-ad81-4ebad20c2845'
for app in h6+[agg]: app['authors']=[author]
for app in h6:
 if app['id']=='H6-FULL-ENDOMORPHISM-FIELD-HODGE': app['dependencies'].append('CURRENT-MILNE-CAV-HODGE')
 if app['id']=='H6-CM-FACTOR-OVER-L':
  for field in ['required','constructed']:
   app['obligations']['exceptional_cases'][field]=app['obligations']['exceptional_cases'][field].replace('The full CM order may be nonmaximal and has discriminant -3 or -4 without exclusion.','The full CM order may be nonmaximal; discriminants -3 and -4 are included without exclusion.')
geometry=['CURRENT-CTS-CUBIC','CURRENT-DELIGNE-CANONICAL-ACTION','CURRENT-MILNE-CAV-HODGE','CURRENT-VOIGHT-RAMIFICATION','CURRENT-VOIGHT-EMBEDDING','CURRENT-VOIGHT-SCALAR','CURRENT-YUAN-MODEL','CURRENT-YUAN-INTEGRAL','CURRENT-YUAN-METRIC']
gi=['GI-00-ASSEMBLY','GA-MAJORANT-FIXED-E','GA-RELATIVE-INVERSE','GA-CENTERED-SLOW-CUTOFF','GA-S1-OUTER-CLOSURE']
agg['dependencies']=[d for d in agg['dependencies'] if d not in ['PENDING-CURRENT-GI-FAMILY-AND-OUTER-INPUTS','PENDING-CURRENT-MAIN-GEOMETRY-AND-SOURCE-APPLICATIONS']]+geometry+gi
save('H6-APPLICATIONS.json',h6); save('AGGREGATE.json',agg)
norm=load(A/'NORMALIZATION.json'); norm['predecessor']={'path':(A/'MANIFEST.json').relative_to(W).as_posix(),'sha256':sha(A/'MANIFEST.json')}; norm['successor_changes']=['Author attribution bound to parent-observed current author run; source authors remain in pinned original records.','H6 field/Hodge adds the actual separately normalized Hodge supplier.','Aggregate replaces broad geometry and GI placeholders with exact proposed supplier IDs; these are not represented as independently accepted by this record.']; save('NORMALIZATION.json',norm)
save('AUTHORSHIP.json',{'author_run_id':author,'thread_id':'01a1be27-25d1-7301-8aeb-311d675aeeea','task':'/root/v14_sign_conductor','observation':'Parent /root observed this in-progress run via desktop wait_threads and supplied it for the new package.','limit':'Observation is not authenticated gate approval. Original proof authors and historical approvals remain as recorded in pinned source files.'})
known=load(W/'work/source-risk-review-20261107/v14-declared-proposal-assembly-author-001/APPLICATIONS.json')
geo=load(W/'work/source-risk-review-20261107/v14-current-geometry-source-adoption-001/APPLICATIONS.json')
if isinstance(geo,dict): geo=geo['applications']
knownids={x['id'] for x in known+geo+h6+[agg]}
missing=sorted({d for a in h6+[agg] for d in a['dependencies'] if d not in knownids})
save('PENDING.json',{'status':'author_schema2_proposal_not_approved_for_gate','absent_normalized_supplier_ids':missing,'present_but_independent_adoption_pending':geometry,'meaning':'Do not claim closed graph or authenticated gate acceptance. Missing records are not findings of missing mathematical proofs.','boundaries':{'H6-ORIGINAL-POLARIZED-QM-DATUM':'Original finite cover, good reduction, principal polarization and normalized coordinate construction; not proved by Hom-field argument.','H6-BETA-QUANTITATIVE-DESCENT-LEVEL':'Actual beta-family dprime<=QM and N<=QM^2 from scalar/character/local-ramification proof; not b-family substitution or C6/Carayol alone.','PENDING-CURRENT-KATO-AND-COMPOSITION-CARRYFORWARDS':'Normalize four accepted current carryforward contracts with actual incoming suppliers; V13 quartic-transform nodes are not aliases for these.'}})
oldh={x['id']:x for x in load(A/'H6-APPLICATIONS.json')}
for x in h6:
 expected=copy.deepcopy(oldh[x['id']]['obligations'])
 if x['id']=='H6-CM-FACTOR-OVER-L':
  for field in ['required','constructed']:
   expected['exceptional_cases'][field]=expected['exceptional_cases'][field].replace('The full CM order may be nonmaximal and has discriminant -3 or -4 without exclusion.','The full CM order may be nonmaximal; discriminants -3 and -4 are included without exclusion.')
 assert x['obligations']==expected
assert agg['obligations']==load(A/'AGGREGATE.json')['obligations']
save('CHECKS.json',{'h6_obligations_unchanged':17*9-1,'h6_wording_correction':'CM-factor exceptional_cases required/constructed now says discriminants -3 and -4 are included, not that all discriminants equal them. Requested by independent reviewer.','aggregate_obligations_unchanged':9,'h6_count':len(h6),'aggregate_dependency_count':len(agg['dependencies']),'missing':missing,'source_evidence_checks':'Predecessor generator verified all27 aggregate file pins against canonical bytes; successor changes no file pins.','not_claimed':'Independent acceptance, complete dependency graph, or authenticated authorship.'})
save('MANIFEST.json',{'files':[{'path':p.relative_to(W).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(P.iterdir()) if p.is_file() and p.name!='MANIFEST.json']})
print(json.dumps({'manifest':sha(P/'MANIFEST.json'),'h6':sha(P/'H6-APPLICATIONS.json'),'aggregate':sha(P/'AGGREGATE.json'),'missing':missing}))
