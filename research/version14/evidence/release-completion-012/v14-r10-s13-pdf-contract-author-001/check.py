import importlib.util,json,sys,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[2]
ASSEMBLED=BASE/'work/quartic-v14-release-assembled-001'
PR=BASE/'work/quartic-v14-release/preview-repository'
sys.path.insert(0,str(ASSEMBLED))
spec=importlib.util.spec_from_file_location('candidate_contracts',HERE/'artifact_contracts.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
old=json.loads((ASSEMBLED/'project-pdfs.json').read_bytes());new,entries=c.project_pdfs()
assert [x['pdf']['path'] for x in old['entries']]==[x['pdf']['path'] for x in new['entries']] and len(entries)==18
before=(ASSEMBLED/'artifact_contracts.py').read_bytes();after=(HERE/'artifact_contracts.py').read_bytes()
assert before.replace(hashlib.sha256((ASSEMBLED/'project-pdfs.json').read_bytes()).hexdigest().encode(),c.PROJECT_PDFS_SHA.encode())==after
current={p['path']:(PR/p['path']).read_bytes() for item in new['entries'] for p in [item['pdf'],*item['sources']]}
current.update({p['path']:(PR/p['path']).read_bytes() for p in new['provenance']})
c.check_project_pdfs(current)
checks=['same18orderedPDFpaths','literal_only_code_change','all_current_PDF_source_provenance_pins']
def reject(label,change):
 data=dict(current);change(data)
 try:c.check_project_pdfs(data)
 except (ValueError,KeyError):checks.append(label);return
 raise AssertionError(label)
merged='research/version14/proofs/local-gi-v1/GI-SUPPLEMENT.pdf'
s13='research/version14/proofs/local-gi-v1/proof/addenda/s13/GI-S13-BOUNDED-SELECTION.md'
review='research/version14/proofs/local-gi-v1/proof/addenda/s13/S13-ADDITIVE-SOURCE-REVIEW.json'
reject('old_pdf_rejected',lambda d:d.update({merged:(PR/'research/version14/proofs/local-gi-v1/proof/history/pre-s13-addendum/GI-SUPPLEMENT.pdf').read_bytes()}))
reject('missing_source_rejected',lambda d:d.pop(s13))
reject('changed_source_rejected',lambda d:d.update({s13:d[s13]+b'!'}))
reject('missing_review_rejected',lambda d:d.pop(review))
reject('changed_review_rejected',lambda d:d.update({review:d[review]+b'!'}))
import package_v14
package_v14.contracts=c
try:package_v14.admissible('research/version14/proofs/local-gi-v1/proof/history/pre-s13-addendum/GI-SUPPLEMENT.pdf')
except ValueError:checks.append('historical_PDF_still_excluded')
else:raise AssertionError('historical PDF admitted')
print(json.dumps({'status':'pass','checks':checks,'approved_pdf_paths':18,'current_required_files':len(current)},indent=2))
