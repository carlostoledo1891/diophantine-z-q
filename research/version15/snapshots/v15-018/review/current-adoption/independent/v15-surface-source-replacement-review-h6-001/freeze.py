from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[1]
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proposal=R/'work/v15-surface-height-source-replacement-001/PROPOSAL.json'
assert h(proposal)=='b8414335aaaafa560a359563e97cc872868f98796bd3dfa404e233aedb666379'
gr=R/'work/v15-surface-height-review-h6-001/gaudron-remond-published-2023.pdf'
assert h(gr)=='b1e2e32bec626cf6d27fb7d6d8702b5c707e0c3dc002d979088e62d8cda514a4'
changes=R/'work/version15-protocold-233-20261110/consolidated-tex-proposal-030/CHANGES.json'
change=json.loads(changes.read_bytes())['changes'][0]
assert hashlib.sha256(change['after'].encode()).hexdigest()==change['after_sha256']=='60547e0593235899cc538103266aea3bb6789f21ef23a72948d22434c28e90b7'
factor=R/'work/v15-surface-factor-review-arithmetic-001/REVIEW.json'
assert h(factor)=='ab872825e746eb399557136b3409f4cb6da3f58ffe57f62bb85ddce7a2ed3beb'
sources=[gr,R/'work/v15-surface-height-review-h6-001/gaudron-remond-published-2014.pdf',factor,changes]
review={'decision':'accepted','scope':'New published2023 surface-height source application and exact030 surface after-text; not installed or retroactive closure','subject_sha256':h(proposal),'after_text_sha256':change['after_sha256'],'reasoning_sha256':h(P/'REVIEW.md'),'reviewer':'/root/v14_h6_coverage','same_field':True,'multiplicities_preserved':True,'original_stable_height':True,'same_bound':True,'sources':[{'path':str(p),'sha256':h(p)} for p in sources],'required_adoption_work':['Bind new immediate supplier in changed source contract','Retain indirect Remond2022Cor1.3 and2017Thm1.6 dependencies','Compare actual installed manuscript change; no unchanged8867 retroactive closure'],'remaining_source_limitation':'No direct final2022 edition comparison is claimed or supplied.'}
(P/'REVIEW.json').write_text(json.dumps(review,indent=2)+'\n')
(P/'MANIFEST.json').write_text(json.dumps({'members':[{'path':x.name,'sha256':h(x),'bytes':x.stat().st_size} for x in sorted(P.iterdir()) if x.is_file() and x.name!='MANIFEST.json']},indent=2)+'\n')
print(json.dumps({'review_sha256':h(P/'REVIEW.json'),'manifest_sha256':h(P/'MANIFEST.json')}))
