import hashlib,json
from pathlib import Path
W=Path.cwd(); B=W/'work/quartic-v14-release/preview-repository'; P=Path(__file__).parent
def sha(b): return hashlib.sha256(b).hexdigest()
def pin(n): return {'side':'head','path':n,'sha256':sha((B/n).read_bytes())}
def save(n,x): (P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
base='research/version14/proofs/'
source_paths=[
'a001-moduli-current-v1/PROOF.md','a001-moduli-current-v1/reviews/INDEPENDENT-REVIEW.md',
'ly-d6-normalization-v1/PROOF.md','ly-d6-normalization-v1/CURRENT-INTERFACE.md','ly-d6-normalization-v1/reviews/INDEPENDENT-REVIEW.md','ly-d6-normalization-v1/reviews/CURRENT-INTERFACE-REVIEW.md',
'b11-integral-model-v1/LOCAL-CONNECTION.md','b11-integral-model-v1/TATE-POLARIZED.md','b11-integral-model-v1/MARKING-DESCENT.md','b11-integral-model-v1/FIVE-MARKING.md','b11-integral-model-v1/NORMALIZER.md','b11-integral-model-v1/ASSEMBLY.md','b11-integral-model-v1/GENERIC-FUNCTOR.md',
'b11-integral-model-v1/reviews/b11-connection-review-compiler-001.md','b11-integral-model-v1/reviews/b11-tate-polarized-review-gaussian-001.md','b11-integral-model-v1/reviews/b11-marking-descent-review-gaussian-001.md','b11-integral-model-v1/reviews/b11-normalizer-review-compiler-001.md','b11-integral-model-v1/reviews/b11-assembly-review-compiler-001.md','b11-integral-model-v1/reviews/b11-provider-update-review-compiler-001.md','b11-integral-model-v1/reviews/GENERIC-FUNCTOR-REVIEW.md']
files=[pin('manuscripts/quartic_v14.tex')]+[pin(base+n) for n in source_paths]+[pin('research/version14/evidence/current-reviewed-003/h6-current-joins-independent-003/REVIEW.md')]
assert files[0]['sha256']=='1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8'
dest='research/version14/evidence/current-h6-original-datum-001/PROOF.md'
newpin={'side':'head','path':dest,'sha256':sha((P/'PROOF.md').read_bytes())}
files.append(newpin)
dims=['source_hypotheses','constructed_objects','index_domain_coverage','transition_maps','consumed_object_identity','coefficient_conventions','local_conditions','exceptional_cases','downstream_consumption']
apps=[]
def add(i,deps,vals,section):
 obs={}
 for d,v in zip(dims,vals): obs[d]={'status':'checked','required':'For this bounded application: '+v,'constructed':v,'justification':'The new composition proof, section '+section+', connects the pinned accepted supplier arguments to this exact construction. Original published-source qualifications and later provider updates remain in force; this is not a new audit of all source ancestors.','evidence':files}
 apps.append({'id':i,'kind':'argument','authors':['01a1bed7-e1a5-71d2-ad81-4ebad20c2845'],'dependencies':deps,'files':files,'obligations':obs})
coarse='H6-POLARIZED-COARSE-AND-COORDINATE'; cover='H6-FINE-THREE-INTEGRAL-COVER'; tame='H6-TAME-CONTACT-PULLBACK'; datum='H6-ORIGINAL-POLARIZED-QM-DATUM'
add(coarse,[],[
'Fixed discriminant-six maximal order O in B=(2,-3), mu=2j+ij; accepted A001 polarized quotient and corrected Lin–Yang normalization inputs.',
'The actual positive principal form E=Trd(mu^-1 x bar(y)) on O and its principally polarized moduli object.',
'The full four-element positive-normalizer quotient, with all three ordered marks.',
'A001 matches the Rosati involution and preservation relation; the three marked CM values identify the same rational Hauptmodul; accepted LY substitution gives the weighted Igusa tuple.',
'The same principally polarized coarse point has coordinate j and tuple [12(j+1),6(j^2+j+1),4(j^3-2j^2+1),j^3].',
'E is unimodular; the printed 6E is not called principal. Weighted rescaling is at the stated weights and does not assert a rational genus-two model.',
'This characteristic-zero coarse identification does not supply a fine integral model.',
'Finite nonzero j is the locus consumed later; disputed BG product-isomorphism and explicit-conic arguments are not used.',
'Supplies the fixed polarized datum, ordered j coordinate and common geometric point criterion to the actual cover and H6.'
],'Fixed polarized point and coordinate')
add(cover,[coarse],[
'The same polarized datum and accepted Buzzard, Tate, marking/descent, generic-functor and local-normalizer inputs.',
'X35 over Z[1/30], with full three- and five-markings; its quotient Y by five relabeling and descended universal principally polarized O-surface.',
'All determinant components and arbitrary test schemes; full-three at the ramified prime3 is supplied by the division-lattice proof.',
'Refine V1(5), add full three, use actual free quotient/effective descent, then the Q-defined PEL/Siegel comparison and canonical right-action conversion.',
'The actual fine full-three Y3 and its same j map, of total degree at most324, carrying the same universal family and degree-one polarization.',
'Left O-module markings and inverse-frame/right-action convention; ample-sheaf norm proves projectivity only and does not replace polarization.',
'Smooth proper model over Z[1/30]; corrected projectivity uses the affine quasi-compact quasi-separated terminal base.',
'No chosen determinant component, no five-level degree factor, no coarse-line universal family, no arbitrary complex-isomorphism descent.',
'Supplies the actual integral cover and abelian scheme for tame pullback and fiber specialization.'
],'Actual full-three cover and universal object')
add(tame,[coarse,cover],[
'S contains every prime<=324; u avoids six contacts; the identified degree<=324 cover has branch orders4,6,2.',
'Normalized pullback by J(u)=-57600F(u)^2/G(u)^6 and the six-contact divisor.',
'Every p>324, including positive and negative contact valuations; all cover components remain included.',
'Tame cyclic stabilizers and unique fixed lifts preserve branch sections; G^6-97200F^2=H^2 gives pullback multiplicities2,6,2 and normalized indices2,1,1.',
'Degree<=324 cover of the u line, branched only at six contacts, locally u-c=z^2 after unramified extension.',
'Same ordered rational j coordinate; discriminant/resultant prime support<=13 introduces no further discarded prime.',
'Positive even contact valuation is unramified; negative valuation specializes at unbranched infinity. The ramification support is contained in S union supp(M_S(u)).',
'No new branch orbit/collision in tame reduction; no multiplication of324 by the rational-map degree12.',
'Supplies the finite etale fiber and its controlled splitting field used to define A/K.'
],'Tame pullback and the field')
add(datum,[coarse,cover,tame],[
'The original six-contact u and S, together with the three constructed source outputs; no height conclusion assumed.',
'K is the splitting field of the finite etale fiber of the normalized cover at u; A/K is a chosen universal-fiber principally polarized O-surface.',
'K/Q is normal of degree<=324!=F0; every conjugate and every place outside S are included.',
'Choose a fiber point over K and pull back the actual universal abelian scheme; compare conjugates through the same rational finite nonzero j=J(u).',
'The original A/K, good reduction outside S, K unramified outside T=S union supp(M_S(u)), and one common geometric polarized moduli point for its conjugates.',
'The same degree-one polarization and O-action, not an isogenous or scaled replacement; no rational model inferred from the weighted tuple alone.',
'Good reduction holds at every K-place not above S, even above supp(M_S(u)); only K ramification is allowed at T.',
'u outside C ensures etale fiber and F(u)!=0; negative discriminant of G ensures finite j; the coarse relation is not a fine moduli assertion.',
'Supplies precisely H6-FULL-ENDOMORPHISM-FIELD-HODGE and H6-A017-IGUSA-THETA original-datum prerequisites, with no beta/conductor or height claim.'
],'Tame pullback and the field')
save('APPLICATIONS.json',apps)
save('INLINE-SUPPLIERS.json',{'scope':'Concrete accepted source/provider proofs are inline inputs, not metadata-only dependency aliases. No claim of an exhaustive graph of every published ancestor.','suppliers':[{'path':f['path'],'sha256':f['sha256']} for f in files if f!=newpin],'composition_proof':newpin,'accepted_source_decisions':'Read the A001 and LY decisions, B11 local/normalizer/assembly decisions, provider-update decision and generic-functor decision together; the old conditional B11 assembly decision is insufficient alone.'})
save('INSTALLATION.json',{'status':'proposal_not_installed','copies':[{'from':(P/'PROOF.md').relative_to(W).as_posix(),'to':dest,'sha256':newpin['sha256']}],'canonical_mutations_performed':False})
save('PENDING.json',{'independent_review':'required for this new four-node composition','installation':'new PROOF.md must be copied byte-identically to its proposed head path before runtime use','not_claimed':['all published source ancestors reconstructed','beta quantitative bounds','full H6 or manuscript closure','authenticated gate approval']})
save('MANIFEST.json',{'files':[{'path':p.relative_to(W).as_posix(),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(P.iterdir()) if p.is_file() and p.name!='MANIFEST.json']})
print(json.dumps({'manifest':sha((P/'MANIFEST.json').read_bytes()),'applications':sha((P/'APPLICATIONS.json').read_bytes()),'nodes':len(apps),'proof':newpin}))
