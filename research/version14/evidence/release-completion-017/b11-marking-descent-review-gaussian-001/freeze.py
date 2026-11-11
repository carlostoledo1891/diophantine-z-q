from pathlib import Path
import hashlib,json,subprocess,sys
O=Path(__file__).resolve().parent;R=O.parents[2]
H=lambda b:hashlib.sha256(b).hexdigest()
def J(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(name,x):(O/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def pin(p):
    b=p.read_bytes();return {'path':p.relative_to(R).as_posix(),'sha256':H(b),'bytes':len(b)}
subprocess.run([sys.executable,str(O/'check.py')],check=True)
P=R/'work/source-risk-review-20261107/b11-marking-descent-sources-theta-006'
assert H((P/'MANIFEST.json').read_bytes())=='62bbcd242d6cee3511a787e926350986a2f500b2e0ea5c146000bb4955ca88b4'
assert H((P/'PROOF.md').read_bytes())=='90456a2a5375ebd6999fcea7bc5c9c3073efd38e557422cec5392d52fd6de469'
checks=J(O/'CHECKS.json')
put('SOURCE-PINS.json',{'target_manifest':pin(P/'MANIFEST.json'),'target_proof':pin(P/'PROOF.md'),'verified_files':checks['files'],'note':'References only; complete third-party sources and page images are not copied into this review.'})
put('PASSAGES.json',{'convention':'Inclusive lines, bytes.splitlines(keepends=True), no normalization','verified_spans':checks['spans']})
put('DECISION.json',{'schema':'bounded-independent-review/v1','reviewer':'gaussian','date':'2026-11-08','status':'accepted_conditional_provider_scope','target_manifest':pin(P/'MANIFEST.json'),'proof':pin(P/'PROOF.md'),'review':pin(O/'REVIEW.md'),'accepted_applications':['B11-STD-MARKING','B11-STD-QUOTIENT','B11-STD-DESCENT'],'accepted_source_uses':['B11-STD-U0'+str(i) for i in range(1,8)],'obligation_comparisons':27,'retained_incoming_interfaces':J(P/'INCOMING-INTERFACES.json'),'authorship':'No authorship of the submitted geometric proof. Reviewer requested explicit missing arguments/conditions and record edges. Author supplied the final proof, including the direct qcqs-base composition lemma; reviewer suggested but did not adopt an alternative H-projective route. See REVIEW.md.','exclusions':['Independent acceptance of the initial Buzzard/full-five model and rigid groupoid match','Independent proof of marking nonemptiness, geometric automorphism/congruence theorem, exact relabeling action, and numerical index','Whole six-phase B11 assembly or global dependency graph','Full predecessor-source reconstruction or new comparison of Murre/FGA/Mumford editions','Live manuscript incorporation, gate passage, release or public-curation approval']})
put('README.json',{'purpose':'Independent conditional marking/descent source-provider review. This is not a whole B11 or release decision.','target':pin(P/'MANIFEST.json'),'entry_points':['REVIEW.md','DECISION.json'],'verification':['CHECKS.json','SOURCE-PINS.json','PASSAGES.json'],'local_only_source_policy':'Original source PDFs, scans and HTML remain at their pinned author local-only paths; no copies here.'})
members=[]
for p in sorted(O.iterdir()):
    if p.is_file() and p.name!='MANIFEST.json':
        b=p.read_bytes();members.append({'path':p.name,'sha256':H(b),'bytes':len(b)})
put('MANIFEST.json',{'schema':'immutable-independent-review/v1','status':'accepted conditional provider scope; see DECISION.json','target_manifest':pin(P/'MANIFEST.json'),'members':members})
print(json.dumps({n:H((O/n).read_bytes()) for n in ['MANIFEST.json','REVIEW.md','DECISION.json']}))
