"""Write current hash-bound accepted baseline and open integration interfaces."""
from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent
def pin(p):
 p=p.resolve()
 return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def rel(n):return pin(H/n)
status={
 'scope':'Research optimization only. Published Version12 remains498. Next release requires strictly fewer than400 TOTAL variables.',
 'currentAccepted':{'variables':470,'witnesses':469,'residuals':439,'degree':4,'monomials':6646,'maximumCoefficient':'16*3^(2^26)',
  'candidate':rel('../01-elimination/triple-cubic/elimination/candidate470-ir.json'),
  'polynomial':rel('../01-elimination/triple-cubic/elimination/polynomial470.json'),
  'nonAuthorReview':rel('reviews/triple/REVIEW.md')},
 'lineage':[
  {'variables':498,'candidate':rel('inputs/released498.json'),'status':'Published Version12'},
  {'variables':486,'candidate':rel('combined486-ir.json'),'certificate':rel('combined486-certificate.json'),'nonAuthorReview':rel('reviews/bl5/REVIEW.md'),
   'changes':['Order10 detector source argument','Four factored second conics','Scalar reciprocal k elimination','Scalar preparation conic','Scalar forward r powers']},
  {'variables':479,'candidate':rel('../01-elimination/triple-cubic/candidate479-ir.json'),'change':'Reordered triple hybrid detector polynomial circuit; exact affine W output maps'},
  {'variables':470,'candidate':rel('../01-elimination/triple-cubic/elimination/candidate470-ir.json'),'certificate':rel('../01-elimination/triple-cubic/elimination/elimination470-certificate.json'),
   'change':'Nine constant-pivot eliminations: six triple-product components and three q1 fifth-power seed coordinates','nonAuthorReview':rel('reviews/triple/REVIEW.md')}
 ],
 'pending':[
  {'name':'V0 reciprocal chart','saving':5,'candidate':rel('v0-493-ir.json'),'proof':rel('V0_REPORT.md'),'verifier':rel('verify_v0.py'),'reviewer':'06-product',
   'openInterface':'Uses unchanged V1 G2 numerator to exclude ell0=0 and g=0. Arithmetic chart extension admits H=-P. Overlaps V0 tangent-guard removal.'},
  {'name':'Tangent comparison guards','savingAgainstCurrentWithV0':4,'fullCandidate':rel('../05-anchor/candidate493-ir.json'),'proof':rel('../05-anchor/REPORT.md'),'reviewer':'02-squares',
   'openInterface':'Use V1,V2,V3,V4 only if reciprocal V0 accepted. These changes retain actual difference-point semantics, including valid doubling.'},
  {'name':'Rational logarithms','saving':8,'sourceProof':rel('../03-depth/REPORT.md'),'implementation':rel('rational490-ir.json'),'verifier':rel('verify_rational_component.py'),'reviewer':'05-anchor',
   'openInterface':'Keeps original scaled w^2 slots and equations needed by470 triple eliminations. Reuses w^3 slots as actualw4, deletesmiddle, recenterspolynomialslotstoR. Apply afterV0 to rewriteitsnewlogconsumer. V1G2unchanged.'}
 ],
 'projectionIfAllPendingAccepted':453,
 'restrictions':['Do not claim pending arithmetic accepted from finite checks alone.','Preserve all frozen accepted bytes.','Do not publish intermediate counts.','Version13 onward subtitle has no trailing period.']
}
status['integratedComponents']=status.pop('pending')
for component,review in zip(status['integratedComponents'],['v0-review.md','tangent-review.md','rational-review.md']):
 component['status']='Non-author arithmetic and component implementation accepted; composed finite transport verified.'
 component['nonAuthorReview']=rel('inputs/'+review)
status.pop('projectionIfAllPendingAccepted')
status['currentCandidate']={'variables':453,'witnesses':452,'residuals':430,'degree':4,'monomials':6584,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('rational453-ir.json'),'polynomial':rel('rational453-polynomial.json'),'report':rel('REPORT453.md'),
 'status':'Frozen, all component changes accepted and finite composition verified; final non-author whole-composition review pending.'}
status['lineage'].extend([
 {'variables':461,'candidate':rel('combined461-ir.json'),'certificate':rel('combined461-certificate.json'),'change':'V0 reciprocal plus four complete tangent charts'},
 {'variables':453,'candidate':rel('rational453-ir.json'),'certificate':rel('rational453-certificate.json'),'interfaces':rel('interfaces453.json'),'change':'Four rational logarithm evaluations'}])
status['pending']=[{'name':'Final non-author453 composition audit','reviewer':'astra_bl5_models','interfaces':['V1 tangent chart still establishes the doubled-point domain needed by V0','V0 reciprocal equation consumes literal R0 after affine output recentering','Six square rows used by470 eliminations remain unchanged','Rational-log local and completeness estimates compose with order10 and factored-pole source changes']}]
status['currentAccepted']=dict(status['currentCandidate'])
status['currentAccepted']['status']='Accepted by independent whole-composition review.'
status['currentAccepted']['nonAuthorReview']=rel('inputs/composition453-review.md')
status['lineage'][-1]['nonAuthorReview']=rel('inputs/composition453-review.md')
status['currentCandidate']={'variables':445,'witnesses':444,'residuals':422,'degree':4,'monomials':6568,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('../03-depth/further/candidate445-ir.json'),'polynomial':rel('../03-depth/further/polynomial445.json'),
 'report':rel('../03-depth/further/REPORT.md'),'firstNonAuthorReview':rel('reviews/primary445/REVIEW.md'),
 'status':'Finite checked and accepted by combination-agent non-author review; parent-requested bl5 review pending before authoritative promotion.'}
status['pending']=[{'name':'Final non-author445 review requested by parent','reviewer':'astra_bl5_models','interfaces':['Primary z0 slot is now s=-1/z0','All Li and point values preserved','Every h and j denominator nonzero from retained chart equations','Complete deleted-z consumer coverage']}]
status['currentAccepted']=dict(status['currentCandidate'])
status['currentAccepted']['status']='Accepted by parent-requested independent non-author review.'
status['currentAccepted']['nonAuthorReview']=rel('inputs/composition445-review.md')
status['currentAccepted']['candidate']=rel('inputs/accepted445-ir.json')
status['lineage'].append({'variables':445,'candidate':rel('inputs/accepted445-ir.json'),'certificate':rel('../03-depth/further/certificate445.json'),'nonAuthorReview':rel('inputs/composition445-review.md'),'change':'Common primary reciprocal removes eight private z coordinates; exact rational witness equivalence'})
status['currentCandidate']=status['currentAccepted']
status['pending']=[
 {'name':'Four odd-root chart reductions','author':'02-squares','claimedSaving':4,'state':'Derivation and exact artifact in progress; not accepted'},
 {'name':'Scalar guard replacement','author':'02-squares','claimedSaving':1,'state':'Derivation and exact artifact in progress; not accepted'},
 {'name':'Positive scalar correction redesign','author':'06-product','claimedSaving':3,'state':'New beta shift and local squareclass proof in progress; not accepted'},
 {'name':'Further detector grouping','author':'01-elimination','state':'Search only; no further accepted saving'}]
status['currentCandidate']={'variables':443,'witnesses':442,'residuals':420,'degree':4,'monomials':6616,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('scalar443-ir.json'),'polynomial':rel('scalar443-polynomial.json'),'certificate':rel('scalar443-certificate.json'),'report':rel('REPORT443.md'),
 'status':'Frozen and fully finite-checked; awaiting parent non-author review of shared-primary/scalar reciprocal equivalence.'}
status['pending'].insert(0,{'name':'Shared reciprocal scalar z removal','author':'10-combination with bl5 derivation','reviewer':'root','saving':2,'state':'Frozen443 ready for non-author review','openInterface':'Retained s is nonzero; exact T*rho-a*N*s equation preserves all scalar-ratio consumers.'})
status['currentAccepted']=dict(status['currentCandidate'])
status['currentAccepted']['status']='Accepted by parent non-author mathematical and implementation review.'
status['currentAccepted']['nonAuthorReview']=rel('inputs/scalar443-review.md')
status['lineage'].append({'variables':443,'candidate':rel('scalar443-ir.json'),'certificate':rel('scalar443-certificate.json'),'nonAuthorReview':rel('inputs/scalar443-review.md'),'change':'Common primary reciprocal eliminates the scalar z pair'})
status['currentCandidate']={'variables':439,'witnesses':438,'residuals':416,'degree':4,'monomials':6568,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined439-ir.json'),'polynomial':rel('combined439-polynomial.json'),'certificate':rel('combined439-certificate.json'),'report':rel('REPORT439.md'),
 'status':'All component mathematics independently accepted and exact transport verified; parent final transport review pending.'}
status['pending']=[x for x in status['pending'] if x['name'] not in ['Shared reciprocal scalar z removal','Four odd-root chart reductions']]
status['pending'].insert(0,{'name':'439 final odd-root transport review','reviewer':'root','state':'Ready','componentNonAuthorReview':rel('inputs/odd-norm-review.md'),'openInterface':'Only four private odd-root blocks change; h,j,x and all outside consumers remain fixed.'})
status['currentAccepted']=dict(status['currentCandidate'])
status['currentAccepted']['status']='Accepted by parent independent composition review.'
status['currentAccepted']['nonAuthorReview']=rel('inputs/composition439-review.md')
status['lineage'].append({'variables':439,'candidate':rel('combined439-ir.json'),'certificate':rel('combined439-certificate.json'),'nonAuthorReview':rel('inputs/composition439-review.md'),'change':'Four odd-root augmentations replaced by norm charts, preserving all shared coordinates'})
status['currentCandidate']={'variables':435,'witnesses':434,'residuals':412,'degree':4,'monomials':6572,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined435-ir.json'),'polynomial':rel('combined435-polynomial.json'),'certificate':rel('combined435-certificate.json'),'report':rel('REPORT435.md'),'consumerVerification':rel('consumers435.json'),
 'status':'Both component changes independently accepted; full finite composition verified; final non-author composition review pending.'}
status['pending']=[
 {'name':'435 guard and positive-correction composition','reviewer':'root','componentReviews':[rel('inputs/scalar-guard-review.md'),rel('inputs/scalar-shift-review.md')],'state':'Ready for final composition review'},
 {'name':'H.j removal with V0 rescaling','author':'10-combination','candidate':rel('primary437-ir.json'),'report':rel('REPORT437.md'),'reviewer':'astra_bl5_models','saving':2,'state':'Separate frozen439-to437 candidate; not integrated into435'},
 {'name':'Further scalar norm-tree reduction','author':'06-product','reviewer':'05-anchor','claimedSaving':1,'state':'Not integrated; awaiting acceptance'},
 {'name':'Further detector grouping','author':'01-elimination','state':'Search only; no further accepted saving'}]
status['lineage'].extend([
 {'variables':435,'candidate':rel('combined435-ir.json'),'certificate':rel('combined435-certificate.json'),'nonAuthorReview':rel('inputs/composition435-review.md'),'change':'Scalar f1 guard and positive five-generator correction with shifted beta'},
 {'variables':433,'candidate':rel('combined433-ir.json'),'certificate':rel('combined433-certificate.json'),'nonAuthorReview':rel('inputs/composition433-review.md'),'change':'Eliminate H.j using shared reciprocal and rescaled V0 coordinate'}])
status['currentAccepted']={'variables':433,'witnesses':432,'residuals':410,'degree':4,'monomials':6507,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined433-ir.json'),'polynomial':rel('combined433-polynomial.json'),'nonAuthorReview':rel('inputs/composition433-review.md'),'status':'Accepted by parent independent composition review.'}
status['currentCandidate']={'variables':432,'witnesses':431,'residuals':409,'degree':4,'monomials':6496,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined432-ir.json'),'polynomial':rel('combined432-polynomial.json'),'certificate':rel('combined432-certificate.json'),'report':rel('REPORT432.md'),'consumerVerification':rel('interfaces432.json'),
 'status':'Norm-root component accepted; final finite composition verified; awaiting assigned01 composition review.'}
status['pending']=[
 {'name':'Scalar norm-root composition','reviewer':'01-elimination','componentReview':rel('inputs/scalar-root-review.md'),'state':'432 frozen and ready'},
 {'name':'Depth24 scalar extension','author':'06-product','claimedSaving':1,'state':'Not integrated; component arithmetic review pending'},
 {'name':'Primary reciprocal identity charts','author':'02-squares','claimedSaving':7,'state':'Not integrated; new identity cases and V0 nonzero dependency under arithmetic review'},
 {'name':'Further detector grouping','author':'01-elimination','state':'Search only; no further accepted saving'}]
status['lineage'].append({'variables':432,'candidate':rel('combined432-ir.json'),'certificate':rel('combined432-certificate.json'),'nonAuthorReview':rel('inputs/composition432-review.md'),'change':'Positive scalar norm-root arithmetic replacement'})
status['currentAccepted']=dict(status['currentCandidate'])
status['currentAccepted']['status']='Accepted by assigned independent composition review.'
status['currentAccepted']['nonAuthorReview']=rel('inputs/composition432-review.md')
status['currentCandidate']={'variables':431,'witnesses':430,'residuals':408,'degree':4,'monomials':6456,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined431-ir.json'),'polynomial':rel('combined431-polynomial.json'),'certificate':rel('combined431-certificate.json'),'report':rel('REPORT431.md'),
 'status':'Scalar-depth24 component independently accepted; full finite transport verified; assigned01 final composition audit pending.'}
status['pending']=[
 {'name':'431 scalar-depth24 composition','reviewer':'01-elimination','componentReview':rel('inputs/scalar24-review.md'),'state':'Frozen and ready'},
 {'name':'Reduced scalar correction and input-label proposals','author':'06-product with root and10 derivations','state':'Not integrated; independent arithmetic review required'},
 {'name':'Primary reciprocal identity charts','author':'02-squares','claimedSaving':7,'state':'Not integrated; identity and V0 nonzero arguments under independent review'},
 {'name':'Further detector grouping','author':'01-elimination','state':'Search only; no further accepted saving'}]
status['lineage'].append({'variables':431,'candidate':rel('combined431-ir.json'),'certificate':rel('combined431-certificate.json'),'nonAuthorReview':rel('inputs/composition431-review.md'),'change':'Scalar depth24 arithmetic replacement'})
status['currentAccepted']={'variables':431,'witnesses':430,'residuals':408,'degree':4,'monomials':6456,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined431-ir.json'),'polynomial':rel('combined431-polynomial.json'),'nonAuthorReview':rel('inputs/composition431-review.md'),'status':'Accepted by assigned independent composition review.'}
status['currentCandidate']={'variables':423,'witnesses':422,'residuals':392,'degree':4,'monomials':6172,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined423-ir.json'),'polynomial':rel('combined423-polynomial.json'),'certificate':rel('combined423-certificate.json'),'report':rel('REPORT423.md'),
 'status':'Identity-chart component independently accepted; full finite transport verified; assigned05 final arithmetic composition audit pending.'}
status['pending']=[
 {'name':'423 identity-chart composition','reviewer':'05-anchor','componentReview':rel('inputs/identity-chart-review.md'),'state':'Frozen and ready; refreshed V0 proof mandatory'},
 {'name':'One-correction input label','author':'root/06-product','reviewer':'03-depth','state':'Not integrated; arithmetic and actual numeric binding pending'},
 {'name':'Scaled final correction','author':'06-product','componentReview':'05 accepted general algebra; one-correction numeric binding still required','state':'Not integrated'},
 {'name':'Further detector grouping','author':'01-elimination','state':'Search only; no further accepted saving'}]
status['currentAccepted']=dict(status['currentCandidate'])
status['currentAccepted']['status']='Accepted by assigned independent arithmetic and finite composition review.'
status['currentAccepted']['nonAuthorReview']=rel('inputs/composition423-review.md')
status['currentCandidate']=dict(status['currentAccepted'])
status['lineage'].append({'variables':423,'candidate':rel('combined423-ir.json'),'certificate':rel('combined423-certificate.json'),'nonAuthorReview':rel('inputs/composition423-review.md'),'change':'Identity-inclusive primary reciprocal charts, with renewed pre-ratio V0 exclusion'})
status['pending']=[
 {'name':'One-correction label and deterministic scalar correction','saving':6,'componentReviews':[rel('inputs/one-correction-review.md'),rel('inputs/deterministic-correction-review.md')],'state':'Components accepted; final composition in progress','openInterface':'Rediscover every input-square consumer; preserve odd input bridge, scalar depth24, and enlarged completeness support'},
 {'name':'Scaled biquadratic primary comparison charts','saving':16,'author':'10-combination proof and02-squares implementation','reviewer':'03-depth','state':'Component candidate in progress; not accepted','openInterface':'All old fU/fV consumers must factor through retained squared outputs; preserve their exact component scales'},
 {'name':'H domain extension','saving':2,'componentReview':rel('../01-elimination/review-H-domain/REVIEW.md'),'state':'Component accepted; final composition pending','openInterface':'Renew half-index, torsion and scalar height arguments on the full combined source'}]
status['currentCandidate']={'variables':417,'witnesses':416,'residuals':386,'degree':4,'monomials':6296,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined417-ir.json'),'polynomial':rel('combined417-polynomial.json'),'certificate':rel('combined417-certificate.json'),'report':rel('REPORT417.md'),
 'status':'Both arithmetic components accepted and full finite transport verified; final independent composition review pending.'}
status['pending'][0]['state']='Combined417 frozen; assigned01 independent final composition review pending'
status['currentCandidate']={'variables':399,'witnesses':398,'residuals':368,'degree':4,'monomials':6352,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined399-ir.json'),'polynomial':rel('combined399-polynomial.json'),'certificate':rel('combined399-certificate.json'),'report':rel('REPORT399.md'),
 'status':'All components independently accepted; full finite chain verified. Final non-author whole-composition review pending. No release claim.'}
status['pending'][1]['state']='Component411 accepted by03; composed401 and399 frozen, final composition review pending'
status['pending'][1]['componentReview']=rel('inputs/biquadratic-review.md')
status['pending'][2]['state']='Component accepted by01; composed399 frozen, final arithmetic composition review pending'
status['pending'].append({'name':'Preparation-zero scalar reduction','saving':3,'componentReview':rel('../05-anchor/review-preparation-zero.md'),'state':'Component accepted; not integrated into frozen399'})
status['pending'].append({'name':'Normalized scalar pole','saving':1,'state':'Component pending independent review; not integrated'})
status['currentAccepted']={'variables':417,'witnesses':416,'residuals':386,'degree':4,'monomials':6296,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined417-ir.json'),'polynomial':rel('combined417-polynomial.json'),'certificate':rel('combined417-certificate.json'),'report':rel('REPORT417.md'),
 'nonAuthorReview':rel('inputs/composition417-review.md'),'status':'Accepted by assigned independent whole-composition review.'}
status['lineage'].append({'variables':417,'candidate':rel('combined417-ir.json'),'certificate':rel('combined417-certificate.json'),'nonAuthorReview':rel('inputs/composition417-review.md'),'change':'Odd affine-square input label and deterministic scalar correction'})
status['pending']=status['pending'][1:]
status['currentCandidate']={'variables':396,'witnesses':395,'residuals':366,'degree':4,'monomials':6344,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined396-ir.json'),'polynomial':rel('combined396-polynomial.json'),'certificate':rel('combined396-certificate.json'),'report':rel('REPORT396.md'),
 'status':'All components independently accepted; full finite chain verified. Final non-author whole-composition review pending. No release claim.'}
status['currentCandidate']={'variables':395,'witnesses':394,'residuals':365,'degree':4,'monomials':6341,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined395-ir.json'),'polynomial':rel('combined395-polynomial.json'),'certificate':rel('combined395-certificate.json'),'report':rel('REPORT395.md'),
 'status':'All components independently accepted; all finite checks passed. Frozen for assigned03 final mathematical composition review. No release claim.'}
status['alternateCandidate']={'variables':397,'residuals':367,'monomials':6347,'candidate':rel('combined397-ir.json'),'polynomial':rel('combined397-polynomial.json'),'certificate':rel('combined397-certificate.json'),'status':'Same final equations except retains two H square-root coordinates and their defining equations. Final composition review pending.'}
status['pending']=[{'name':'Final395 mathematical composition review','reviewer':'03-depth','state':'Frozen and ready','interfaces':['Scaled biquadratic maps preserve all actual squared tests and ratio outputs','General H soundness uses pre-ratio exceptional exclusion and revised group identities','Deterministic correction and preparation-zero use one complete finite and real choice order','Normalized scalar pole input nonzero follows from unchanged external scalar equations'],'report':rel('REPORT395.md')}]
status['currentAccepted']=dict(status['currentCandidate'])
status['currentAccepted']['status']='Accepted by assigned03 independent mathematical and finite composition review.'
status['currentAccepted']['nonAuthorReview']=rel('inputs/composition395-review.md')
status['lineage'].append({'variables':395,'candidate':rel('combined395-ir.json'),'certificate':rel('combined395-certificate.json'),'nonAuthorReview':rel('inputs/composition395-review.md'),'change':'Scaled biquadratic charts, enlarged H domain, specialized preparation and normalized scalar pole'})
status['currentCandidate']={'variables':394,'witnesses':393,'residuals':364,'degree':4,'monomials':6338,'content':1,'maximumCoefficient':'16*3^(2^26)',
 'candidate':rel('combined394-ir.json'),'polynomial':rel('combined394-polynomial.json'),'certificate':rel('combined394-certificate.json'),'report':rel('REPORT394.md'),
 'status':'Frozen Version13 selection, all components accepted and finite checks passed; assigned03 final anchor composition review pending.'}
status['pending']=[{'name':'Final394 mathematical composition review','reviewer':'03-depth','state':'Frozen and ready','componentReview':rel('inputs/anchor-rescale-review.md')},
 {'name':'Compact394 and ordinary411 artifact audit','reviewer':'02-squares','state':'Frozen and ready','artifactManifest':rel('release394/ARTIFACTS.json')}]
status['currentAccepted']=dict(status['currentCandidate'])
status['currentAccepted']['status']='Accepted by assigned03 independent mathematical and finite composition review.'
status['currentAccepted']['nonAuthorReview']=rel('inputs/composition394-review.md')
status['currentCandidate']=dict(status['currentAccepted'])
status['lineage'].append({'variables':394,'candidate':rel('combined394-ir.json'),'certificate':rel('combined394-certificate.json'),'nonAuthorReview':rel('inputs/composition394-review.md'),'change':'Private scalar-anchor rescaling and g0 guard'})
status['pending']=[{'name':'Compact394 and ordinary411 artifact audit','reviewer':'02-squares','state':'Frozen and ready','artifactManifest':rel('release394/ARTIFACTS.json')}, {'name':'Portable source and inventory bundle','state':'Assembly in progress; final release belongs to parent task'}]
(H/'STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
print('Updated STATUS.json; accepted394, ordinary411 artifact review and portable bundle pending.')
