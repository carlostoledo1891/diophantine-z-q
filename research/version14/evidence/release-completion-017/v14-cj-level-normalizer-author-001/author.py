import copy,hashlib,json
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parent;P=O.parents[2]/'work/quartic-v14-release/preview-repository'
def sha(b):return hashlib.sha256(b).hexdigest()
def dig(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def save(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
rel='research/version14/evidence/cj-level-normalizer-001/PROOF.md'
note='''# The split local level normalizer

Fix the already supplied split local Eichler model R=[[Z_p,Z_p],[p^e Z_p,Z_p]], e>=1, with its cyclic level line. No assertion identifying a geometric curve with this model is proved here.

Put n=p^e and w=[[0,1],[-n,0]]. Its determinant is n and w^2=-n I. For y=[[a,b],[n c,d]], multiplication gives w y w^-1=[[d,-c],[-n b,a]]. Thus w normalizes R, exchanges the two diagonal characters modulo n, and has reduced-norm valuation e.

For an actual split unit trace-zero vector x with selected eigenvalue r, let P be the integral projector onto the r-eigenline. At odd p, P=(x+r)/(2r). In the dyadic support use e_x=(1+x)/2 and P=(e_x-(1-r)/2)/r; this is integral because r is odd. In either case P belongs to R, has trace1, and is an idempotent. On the cyclic level line its first diagonal entry is1 modulo n when r is the selected root; its second is0, since the trace is1. Conjugating P by w exchanges these entries. Therefore the r-projector acts as0 on the fixed level line for w x w^-1, and its complementary projector acts as1. The selected eigenvalue becomes -r. This projector argument also applies at p=2 when the residues of r and -r alone cannot distinguish the two projectors.

For the prescribed root character alpha_p, the root-weight ratio is alpha_p(-r)/alpha_p(r)=alpha_p(-1). By its chosen parity this is w_(p^e)*chi_hstar(p)^e. If chi_hstar is unramified at p then its value on the reduced norm of w is chi_hstar(p)^e. Both are the factors used in the orientation comparison; the actual eigen-action of the modular parametrization remains a separate input.

This establishes the local matrix, selected-root and norm assertions only. The global adelic/geometric identification of this local normalizer with the actual Atkin-Lehner correspondence, the actual character choices, and the principal newform eigen-action are not consequences of the matrix computation.
'''
dest=O/'overlay'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(note,encoding='utf8');(O/'PROOF.md').write_bytes(dest.read_bytes())
def loc(p,a,b):
 raw=dest.read_bytes() if p==rel else (P/p).read_bytes();return {'pin':{'side':'head','path':p,'sha256':sha(raw)},'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(raw.splitlines(keepends=True)[a-1:b]))}
c=copy.deepcopy(json.loads((R/'v14-cj-analytic-inputs-author-001/COMPONENTS.json').read_bytes())[0]);u=c['use'];co=c['connection'];ident='ACTIVE-CJ-SPLIT-LEVEL-NORMALIZER';sl=loc(rel,3,9)
profile=copy.deepcopy(u['assertion']);profile.update(statement='In the supplied split local Eichler model, the exact-level normalizer has reduced norm valuation e and changes the selected unit eigenvalue r to -r, including the dyadic projector support.',hypotheses='The actual split Eichler model and cyclic level line are supplied. The vector satisfies the stated split-unit support and has integral complementary projectors; at2 the support includes (1+x)/2 in R.',exceptional_cases='Dyadic roots are distinguished by integral projectors, not their residues. This does not identify the global geometric correspondence or prove newform eigen-action.')
targets=[loc('manuscripts/quartic_v14.tex',15876,15886),loc('research/version14/proofs/cj-conductor-one-v1/proof.md',83,83)]
u.update(id=ident,assertion=profile,passages=[ident+'-P1',ident+'-P2'],inline_argument=sl,reason='Explicit matrix and integral-projector calculation supplies the local normalizer premise.',shared_contract_justification='Both passages consume the same local split model, level line and selected-root reversal.')
u['supplier'].update(location=sl,statement=profile['statement'])
co.update(use_id=ident,use_sha256=dig(u),supplier_passage_role='proof',available_assertion=copy.deepcopy(profile),needed_assertion=copy.deepcopy(profile),consumer_locations=targets,required_capabilities=[ident],available_capabilities=[ident],derived_capabilities=[])
co['connecting_derivation'].update(kind='derivation',location=sl,output_assertion=copy.deepcopy(profile));co['adverse_cases']={'status':'checked','reason':profile['exceptional_cases'],'evidence':[sl]+targets}
save('COMPONENTS.json',[c]);save('PENDING.json',{'geometric_identification':'The identification of the supplied split Eichler model and its normalizer action with the actual enhanced supersingular/Atkin-Lehner correspondence remains a separate geometric input.','source_ancestry':'This local computation uses only matrix identities and the previously specified integral projectors; it is not an independent proof of those global models.'})
save('MANIFEST.json',{'files':{str(p.relative_to(O)).replace('\\','/'):{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(O.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((O/'MANIFEST.json').read_bytes()))
