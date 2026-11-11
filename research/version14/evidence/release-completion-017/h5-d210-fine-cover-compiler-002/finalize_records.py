from pathlib import Path
import copy,hashlib,json
R=Path.cwd(); P=Path(__file__).resolve().parent
Q=R/'work/source-risk-review-20261107/h5-d210-connections-compiler-001'
T='H5-D210-TAME-MODEL'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=p.resolve().relative_to(R.resolve()).as_posix(),sha256=sha(b),bytes=len(b))
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
changes=[]; selected={}
for name in ['APPLICATIONS.json','OBLIGATION-COMPARISONS.json']:
 old=json.loads((Q/name).read_text(encoding='utf-8'));new=copy.deepcopy(old);selected[name]=0
 def walk(x,path='$'):
  if isinstance(x,dict):
   if x.get('application_id')==T or x.get('id')==T:
    selected[name]+=1
    for key in ['available','source_available']:
     if key in x:
      before=copy.deepcopy(x[key]);x[key]='Yuan supplies only the proper regular semistable maximal stack. H5-FINE-CONSTRUCTION-002 supplies the full-isomorphism principal-three projective scheme, universal family and entire canonical Q-model. DM69 and the D210 branch supplier retain their separate roles.'
      changes.append(dict(file=name,json_path=path+'.'+key,before=before,after=x[key]))
    if 'source_ids' in x:
     before=copy.deepcopy(x['source_ids']);assert isinstance(before,list)
     x['source_ids']=before+['H5-FINE-CONSTRUCTION-002'];changes.append(dict(file=name,json_path=path+'.source_ids',before=before,after=x['source_ids']))
    if x.get('id')==T and 'proof_locations' in x:
     before=copy.deepcopy(x['proof_locations']);p=pin(P/'PROOF.md');p.update(lines=[1,len((P/'PROOF.md').read_bytes().splitlines())],excerpt_sha256=p['sha256'])
     x['proof_locations']=before+[p];changes.append(dict(file=name,json_path=path+'.proof_locations',before=before,after=x['proof_locations']))
    for key in ['derivation','needed','connecting_derivation']:
     if isinstance(x.get(key),str) and 'Yuan supplies the model;' in x[key]:
      before=x[key];x[key]=before.replace('Yuan supplies the model;','Yuan supplies the maximal stack; H5-FINE-CONSTRUCTION-002 supplies the full-isomorphism principal-three model;')
      changes.append(dict(file=name,json_path=path+'.'+key,before=before,after=x[key]))
    if str(x.get('id','')).endswith('::dependencies') or x.get('obligation')=='dependencies':
     if isinstance(x.get('needed'),str):
      before=x['needed'];x['needed']=before+'; H5-FINE-CONSTRUCTION-002 (the seven exact construction applications).';changes.append(dict(file=name,json_path=path+'.needed',before=before,after=x['needed']))
   for k,v in list(x.items()):walk(v,path+'.'+k)
  elif isinstance(x,list):
   for i,v in enumerate(x):walk(v,path+'['+str(i)+']')
 walk(new)
 put(P/('EFFECTIVE-PARENT-'+name),new)
assert selected=={'APPLICATIONS.json':1,'OBLIGATION-COMPARISONS.json':9},selected
assert any(c['file']=='APPLICATIONS.json' and c['json_path'].endswith('.source_available') for c in changes)
assert any(c['file']=='APPLICATIONS.json' and c['json_path'].endswith('.source_ids') for c in changes)
put(P/'PARENT-SOURCE-OVERRIDE.json',dict(status='author source-attribution successor; independent review pending',parent_files=[pin(Q/n) for n in ['PROOF.md','APPLICATIONS.json','OBLIGATION-COMPARISONS.json','INCOMING.json','SOURCES.json']],supplier=dict(source_id='H5-FINE-CONSTRUCTION-002',proof=pin(P/'PROOF.md'),applications=pin(P/'APPLICATIONS.json')),scope='The fine-scheme availability assertion in parent PROOF section1, INCOMING and YUAN-FINAL source attribution is overridden by this provider selection. The effective application and nine comparison rows below replace that attribution explicitly. Yuan itself supplies only the maximal stack. All other parent mathematical claims remain at their prior conditional scope; no independent approval is created.',selected_records=selected,changes=changes))
# The checker must use the actual application ID field as well as the comparison field.
c=P/'check.py';s=c.read_text(encoding='utf-8');s=s.replace("if x.get('application_id')=='H5-D210-TAME-MODEL':","if x.get('application_id')=='H5-D210-TAME-MODEL' or x.get('id')=='H5-D210-TAME-MODEL':");c.write_text(s,encoding='utf-8')
# Make the genus source explicit in the projectivity application.
apps=json.loads((P/'APPLICATIONS.json').read_text(encoding='utf-8'))
for a in apps:
 if a['application_id']=='H5-FINE-PROJECTIVITY' and 'GR-GENUS' not in a['source_ids']:a['source_ids'].append('GR-GENUS')
put(P/'APPLICATIONS.json',apps)
ov=json.loads((P/'PARENT-SOURCE-OVERRIDE.json').read_text(encoding='utf-8'));ov['supplier']['applications']=pin(P/'APPLICATIONS.json');put(P/'PARENT-SOURCE-OVERRIDE.json',ov)
# Preserve the earlier qualification as a separate author-frozen historical supplement.
S=Q/'fine-level-source-supplement-001'
put(S/'SOURCES.json',dict(parent=pin(Q/'MANIFEST.json'),yuan=pin(R/'work/source-risk-review-20261107/translation-final-comparison-root-001/local-only/yuan-final.pdf'),translation=pin(R/'work/private-15671-20261105/yuan-published/primary/yuan-author-translation.pdf'),buzzard=pin(R/'work/source-risk-review-20261107/buzzard-final-comparison-root-001/local-only/published.pdf')))
put(S/'SOURCE-CAVEATS.json',dict(yuan='Printed230–231: the eta condition says O-linear map, not full isomorphism; equality U=U(3) avoids only the separate supergroup-containment defect.',buzzard='Final594 assumption(ii) requires maximality at every discriminant prime. Its Section2 level theorem does not cover D210 with principal level3. Final592 canonical-polarization paragraph is a separate statement before those level restrictions.',resolution='The later h5-d210-fine-cover-compiler-002 is a separate author construction, requiring independent review. This historical qualification is not erased.'))
assert not (S/'MANIFEST.json').exists(),'Preserve existing historical supplement.'
put(S/'MANIFEST.json',dict(status='author-frozen conditional source qualification',members=[dict(path=f.name,sha256=sha(f.read_bytes()),bytes=len(f.read_bytes())) for f in sorted(S.iterdir()) if f.is_file() and f.name!='MANIFEST.json']))
inputs=json.loads((P/'INPUTS.json').read_text(encoding='utf-8'));inputs['historical_source_qualification']=pin(S/'MANIFEST.json');put(P/'INPUTS.json',inputs)
put(P/'READING-RECORD.json',dict(author='/root/astra_v14_baseline_compiler',primary_readings=[dict(source='Yuan final',pages='230–231',method='Chinese page images visually read; literal eta/supergroup boundaries preserved.'),dict(source='Milne2005 final',pages='319–330,348–349,352–355',method='Actual local PDF text read;327 rendered image additionally inspected. Full7.4 Hodge condition and type-A/C canonical criterion retained.'),dict(source='Buzzard final',pages='592,594–597',method='Actual local PDF text read; polarization statement distinguished from restricted level theorem.'),dict(source='Stacks Project',pages='03YR,0ADD,0A18,0E83,0D3A,0D32,0B45',method='Actual official statements and displayed proofs read, with downloaded HTML pins.'),dict(source='Milne1986 and Voight13',pages='See SOURCES exact locators',method='Previously source-read local final inputs reused at their exact scope; current application is newly authored.')],errata='Official2005a and xnotes/errata pages read through web2026-11-08. HTTP406 retrieval failures preserved; no raw HTML identity claimed.',scope='Source reading and author application only, not an independent review.'))
public=['PROOF.md','README.md','SOURCES.json','ERRATA-READING.json','INPUTS.json','CONSUMERS.json','APPLICATIONS.json','OBLIGATION-COMPARISONS.json','DEPENDENCIES.json','AUTHORSHIP.json','EFFECTIVE-PARENT-APPLICATIONS.json','EFFECTIVE-PARENT-OBLIGATION-COMPARISONS.json','PARENT-SOURCE-OVERRIDE.json','READING-RECORD.json','SIGN-CLARIFICATION.json']
put(P/'PUBLIC-SELECTION.json',[pin(P/n) for n in public])
print(json.dumps(dict(selected=selected,field_changes=len(changes),historical_supplement=pin(S/'MANIFEST.json'),proof=pin(P/'PROOF.md')),indent=2))
