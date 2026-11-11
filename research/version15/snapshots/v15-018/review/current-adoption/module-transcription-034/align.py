import json,re,difflib,pathlib
p=pathlib.Path(__file__).parent
items=json.loads((p/'ALIGNMENT-INPUTS.json').read_text())
def norm(s,current=False):
 if current:
  s=re.sub(r'\\GI[A-P]([A-Za-z]+)',lambda m:'\\'+m[1],s)
  s=re.sub(r'v15-gi-\d+-','',s)
  s=re.sub(r'v15:gi:\d+:','',s)
  s=s.replace('\\subsubsection','\\SUBSEC').replace('\\subsection','\\section').replace('\\SUBSEC','\\subsection')
 return re.sub(r'\s+','',s)
out=[]
for a in items:
 old=[norm(s) for s in a['old']];new=[norm(s,True) for s in a['current']]
 ops=difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes()
 changed=[];pairs=[]
 for kind,i,j,k,l in ops:
  if kind=='equal': pairs += [[ii+1,a['current_start']+k+ii-i] for ii in range(i,j)]
  elif any(i<r['end'] and j>=r['start'] for r in a['ranges']):
   changed.append({'kind':kind,'old_lines':[i+1,j],'current_lines':[a['current_start']+k,a['current_start']+l-1],'old':a['old'][i:j],'current':a['current'][k:l]})
 out.append({'path':a['path'],'pairs':pairs,'differences':changed})
(p/'ALIGNMENT-OUTPUT.json').write_text(json.dumps(out,indent=2))
print(json.dumps([{'path':x['path'],'pairs':len(x['pairs']),'differences':len(x['differences'])} for x in out],indent=2))
