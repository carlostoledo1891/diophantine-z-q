from pathlib import Path
import hashlib,json,difflib,datetime,re

OUT=Path(__file__).parent
SRC=Path('work/v15-222-manuscript-author-001/successor-002/quartic_v15.tex')
OLD=Path('work/version15-protocold-233-20261110/repository/manuscript/quartic_v15.tex')
DELIVERED=Path('work/v15-222-manuscript-author-001/quartic_v15.tex')
sha=lambda b:hashlib.sha256(b).hexdigest()
raw=SRC.read_bytes(); lines=raw.splitlines(keepends=True)
assert sha(raw)=='b379fef539ed1481754e770d683577754198d491d4b883323469be4ba16cefb5'
pin={'path':SRC.as_posix(),'sha256':sha(raw)}
def loc(a,b):
    # The observations were made on delivered43c873; successor adds one line at35798.
    a+=a>=35799;b+=b>=35799
    return {'pin':pin,'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(lines[a-1:b]))}
def save(name,obj):
    p=OUT/name;assert not p.exists(),p
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return {'path':p.as_posix(),'sha256':sha(p.read_bytes())}

# Independently reconstructed from the printed proof, before consulting the new inventory.
# Columns: subject, supplier passages, consumer passages, statement, hypotheses/domain,
# normalization/constants, exceptional cases/order, dependency subjects.
rows=[
('four-contact arithmetic construction',[(37087,37108),(32389,32397)],[(37109,37131)],
 'Replacing the extra five-factor normalizer by r4=beta(beta-1)(beta-2401)(32beta+343), beta=2504+51x^2, retains exactly the finite odd contacts of M5; the infinity contact has even valuation for rational input. The displayed changed row computes r4 after deleting one helper.',
 'Rational x; the retained M5 is the odd contact radical outside76176 for infinity,0,1,2401,-343/32.',
 'R=A*r4/(1+149^2*r4), A=149^(2N+1); retain raw233 t=x63=x^2 and u=x121=(51t+2501)^2/4.',
 'This is an arithmetic redesign, not a bijection of every old witness. Positivity r4>=1 is proved before R is divided by.',[]),
('forced149 scalar depth',[(37109,37124),(35036,35116)],[(37125,37131),(37190,37199),(37298,37317)],
 'The four-contact normalizer has v149(R)=2N+1 or2N-1 and positive odd valuation at each selected contact. The retained scalar criterion gives v_p(a)>9v_p(R)/4, formal depth and exclusion of exceptional reference points.',
 'N>=1; p=149 or p>76176 at a positive odd contact; actual elliptic point and unchanged physical scalar variables.',
 'The residues59,97,109,108 are nonsquares at149; when v149(x)<0, v149(r4)=8v149(x). Scalar W=Z0^4/R^10+Z1^2/R^5+F^2/R^4.',
 'Zero rational components are allowed with infinite valuation. Pole obstruction and F!=0 must be available; reference exclusions precede reference divisions and do not assume w interpretation.',[1]),
('contact divisibility and soundness',[(37120,37131),(35104,35129)],[(39082,39090)],
 'For the nonzero scalar index a, 149^(floor(9(2N-1)/4)+1)*M5(beta)^3 divides |a|. The retained two height/Lucas contradictions and squarefree51 denominator argument then force rational input x to be integral.',
 'All retained group, height, aggregate, scalar and comparison premises remain in force; sufficiently large N uniform in x.',
 'Use |a|, not the earlier baseline a-1. Constants C3 and retained contact/aggregate bounds are unchanged; finite coefficient N>=53 is unrelated.',
 'Exclude a=0 by the retained scalar construction, then apply the two contradictions in their original order. No fresh proof of upstream foundations is asserted.',[1,2]),
('integer completeness of changed normalizer',[(37133,37156),(35783,35802)],[(39082,39090)],
 'For every integer input, the four-contact construction admits witnesses for all sufficiently large N with one uniform ineffective threshold. Local square and integrality conditions, real pole interval and prime choices remain compatible.',
 'Integer x; retained elliptic recurrence, local approximation, pole/conic realization and prime selection results with their original domains.',
 'v2(r4) in{2,3}; r4=1 mod3 and13 mod17; v3(R)=v17(R)=0. 9792=2^6*3^2*17. Reduced denominator of R(R+9792) is (1+149^2*r4)^2. b=O(R^-6) lies in(0,17).',
 'Choose H formal at the finite support first, then a deeper index and real neighborhoods; choose later contact primes outside that support. No exact-square attainment or transfer of arbitrary old pole witnesses is assumed.',[1,2]),
('shared alternate ratio T',[(37158,37205)],[(37207,37223),(37325,37330)],
 'Four alternate field ratios and their comparison equations are equivalent to Dr*T=Nr and E_i*T=K_i*L_i for i=0..3, with inverse z_i=-L_i/T. All eight removed components have the displayed complete consumer list.',
 'Admitted arithmetic family after the independent149 scalar/reference argument; K=Q(sqrt2).',
 'Nr=alpha*S+gamma+delta*g, Dr=beta0*S+alpha with printed constants; norms alpha=43911/2 and beta0=6724 are149-units. Replace eight coordinates by two:232 to226.',
 'Nr and Dr have equal finite valuation and T is a unit. Never divide by K_i,L_i,E_i, a rational component or a root numerator; their zero cases remain.',[2]),
('reference recovery before w',[(37207,37306)],[(37307,37324)],
 'The printed field quadrics Q0,Q1,Q3 recover F=(a+cf)g+bfS+ef and E=bSg-eg-af+8. Their f=0 specialization is impossible; their combination yields f*S^2+D_c*f^2=1 before interpreting w.',
 'K=Q(rho), rho^2=2; B=f^2; g is the printed affine expression in S,T with nonzero constant divisor delta.',
 'a=57-28rho,b=8-14rho,c=88-48rho,e=39-36rho; the f=0 contradiction has norm4905889/107584.',
 'The curve and nonzero f are recovered algebraically before scalar149 depth is used to determine w. This prevents circular use of a discarded reference relation.',[5]),
('reference square and redundant relation',[(37307,37330)],[(37332,37396)],
 'After recovering the reference curve, Q2=M*w+L has M nonzero, so w=g^4/f^2; Q4 fixes W=w^2 and Q5 follows. The six displayed identities reduce to zero after the stated denominator clearing; retaining Q0..Q4 removes two coordinates.',
 'Recovered reference point; v149(f)=m>0,v149(S)=-m/2,v149(g)=m/2 supplied without w. a+cf and Dr nonzero.',
 'M has a unique lowest-valuation S term whose coefficient norm is414947904808977/2612163717219896. Clear by (a+cf)^16*Dr^2.226 to224,200 to198 equations; final B,w,W component scales are printed.',
 'Allow zero numerators and rational components. First recover f!=0, then apply149 depth, then infer M!=0 and w; no division by M is justified merely by genericity.',[2,5,6]),
('q nonzero independently of trace',[(37332,37343)],[(37344,37414)],
 'The retained contact equation (1+q)P5(r)=r^5 with r=(t-1)^2 forces q!=0 over Q, independently of root and trace equations.',
 'R!=0 from positive normalizer; actual unchanged contact equation.',
 'Modulo5, P5(r)=(r-1)^2(r-4)^3; integral t gives r=0,1,4. For negative v5(t), P5-r^5 has degree4 with unit leading coefficient.',
 'q=-1 is allowed. Do not use positivity of a trace or nonzero root component to establish this domain.',[1]),
('root and Lucas scaling with six helper deletions',[(37344,37368)],[(37369,37396),(37398,37414)],
 'The printed rescaling of three ordinary root blocks and all Lucas/comparison consumers makes six FU helper definitions identities; every retained row remains quadratic and inverse formulas reconstruct all six helpers.',
 'R>0 and q!=0; exact raw224 indexing and complete consumer list, not a local root-only change.',
 'New U=q*oldU; FU=((U0^2+2U1^2)/q^2,U0U1/q^2). Remaining listed roots scale q/R or q; listed comparison/Lucas pairs scale1/R.',
 'The special second root and physical scalar ratio remain unchanged. The odd-q special FU contribution is retained; zero root components are permitted.',[7,8]),
('paired detector row operations',[(37369,37388)],[(37389,37396),(39082,39090)],
 'For factors1,2,4, replacing detector0 by Q1*F0-Q0*F1 while retaining detector1 is reversible and removes the ordinary FU consumers. H,J,K* encode the printed paired coefficients.',
 'Q1=q^2!=0, Q0=q0^2; exact factors with S* occurring only in factor2.',
 'H=Q1*h0-Q0*h1,J=Q1*j0-Q0*j1,K*=Q1*q0-Q0*q. Identity Q1F0-Q0F1=Q1-Q0+H*A+J*C+K*S*.',
 'No division by H,J,K*,their differences or components. Physical factor products, norms and pole values must remain unchanged, including their zero branches.',[8,9]),
('trace reconstruction and consumer census',[(37389,37396)],[(37398,37414)],
 'After the root scaling, the old trace equation is equivalent to Q1*G-R^2*Z=0, together with G=P-T2 and Z=T1+T3+T4; these are the only consumers of the two trace helpers.',
 'Exact reindexed raw223 system after the six deletions and five new paired/trace helpers.',
 'The new trace is q^2 times the old trace. G=8*x4*x98 minus the special squared trace; Z is the sum of the other three squared traces with imaginary coefficient2.',
 'No trace component is assumed nonzero. Census must include the entire residual system, not just the displayed trace definitions.',[9,10]),
('final trace quotient223 to222',[(37398,37414)],[(37416,37522),(39082,39090)],
 'Replace G,Z by U*=Z/Q1 and the two quadrics R^2*U*-P+T2=0, Q1*U*-T1-T3-T4=0. The inverse G=R^2*U*,Z=Q1*U* restores the old three relations.',
 'q!=0 from contact alone; exact three-consumer census for raw223 coordinates222,223.',
 'Q1=raw223 x98,R^2=x119. Keep coordinates1..221 and U* at222;197 equations become196.',
 'All zero trace cases and distinguished input preserved. No inverse of a trace or arbitrary new denominator is used; no arithmetic threshold change from this bijection.',[8,11]),
('affine and residual presentation maps',[(37416,37522)],[(37524,39080)],
 'The eight ordered affine stages and constant invertible residual operations identify raw222 with the displayed integral quadratic system. They commute with the trace quotient because coordinates222,223,98,119 are untouched.',
 'Exact printed stage order, reindexing and rational constant inverses; denominator clearing by nonzero constants only.',
 'Includes root half-sum/difference stages, positive gcd normalization and final Q124->3Q124+11Q125, Q125 fixed; former trace row186 removed.',
 'Inverse coordinate stages must be traversed in reverse order. No rational-point exclusions arise from these constant affine maps or constant invertible row operations.',[12]),
('exact196-quadratic specification',[(37524,39080)],[(39082,39100),(104,109)],
 'All196 printed integer quadrics, eight kappa constants and coordinate labels equal the transformed system; no row, coefficient or parameter dependence is omitted.',
 'A=149^(2N+1);222 rational coordinates with z1 fixed as input.',
 'This is a finite exact coefficient/table obligation, distinct from arithmetic soundness. Last rows are the two trace quotient definitions.',
 'Initial reconstruction does not claim a fresh independent row-by-row expansion. GLOBAL reported this bounded equality check; its exact receipt will be examined after this freeze.',[13]),
('positive weighted sum equivalence',[(37524,37541)],[(39082,39095),(104,109)],
 'P_N=sum_i w_i*Q_i^2 vanishes over Q exactly when all196 quadrics vanish, since each weight is strictly positive.',
 'All variables rational and weights the printed positive integers.',
 'Default weight2; listed replacements1,4,6,8; total428. Weighted196 squares are not196 unit squares.',
 'No cancellations between positive weighted rational squares. Degree/content/support require a separate finite coefficient check.',[14]),
('finite coefficient profile',[(39091,39100)],[(104,109),(69,69)],
 'The weighted polynomial has degree4, content1, all222 coordinates,2277 coordinate monomials and2278 parameter-separated terms. For N>=53 its exact largest coefficient magnitude is A^2+1.',
 'Exact weighted expansion of the printed196 quadrics; integer N>=53 for the height assertion.',
 'Only quadratic A dependence is coefficient z108^2=A^2+1; linear-A coefficients <=44402 in absolute value and parameter-free coefficients <149^214.',
 'The finite N>=53 coefficient condition does not certify the defining property or make N0 effective.',[14,15]),
('full uniform integer-definition composition',[(39082,39105),(104,111)],[(69,69)],
 'There is one ineffective N0 such that for every N>=N0 and every rational x, integral x is equivalent to a rational solution of the displayed222-variable weighted quartic with first coordinate x.',
 'Both arithmetic directions for the changed four-contact construction plus every exact admitted-family map, field-relation consequence and presentation equivalence.',
 'A_N=149^(2N+1);221 existential witnesses. N0 may increase for the arithmetic redesign but remains uniform in the input.',
 'Do not compose the233 result as an arbitrary-witness bijection through the232 redesign. Separate soundness/completeness and preserve all domain proofs before inversion.',[3,4,5,6,7,8,9,10,11,12,13,14,15]),
('retained constructions and corrected theorem routing',[(33775,33775),(35022,35023),(35797,35798),(39102,39105),(39879,39879)],[(111,111),(104,109)],
 'Original huge polynomial and explicit314 quartic remain separate retained constructions;233 is a proof intermediate. The three repaired predecessor references route the222 theorem through the new sections rather than claiming233 alone proves it.',
 'Unchanged predecessor bytes retain their earlier supplier/use scopes and qualifications; only the new theorem routing changes.',
 'Successor002 changes three reference passages only relative to delivered43c873; the inserted222 mathematics is identical.',
 'Historical statements of233/238 coefficient counts are not current222 counts. This use is assembly/context, not a new arithmetic premise of the original or314 constructions.',[17]),
]
uses=[]
for i,(title,ss,cc,statement,hyp,norm,exception,deps) in enumerate(rows,1):
    uses.append({'id':f'V222-SF{i:02d}','subject':title,'supplier_passages':[loc(*r) for r in ss],
      'consumer_passages':[loc(*r) for r in cc],
      'assertion':{'statement':statement,'objects':title+' in the exact printed source and coordinate conventions.',
       'hypotheses':hyp,'quantifiers':'As stated in the required assertion and hypotheses; no extension beyond the admitted family or printed parameter range.',
       'parameter_range':hyp,'uniformity':'Only the uniformity explicitly stated in this assertion and its retained premises is required; finite identities hold on their stated domains.',
       'constants':norm,'normalizations':norm,'exceptional_cases':exception,'limit_order':exception},
      'dependencies':[f'V222-SF{d:02d}' for d in deps],
      'classification':'assembly_context' if i==18 else 'substantive_source_use',
      'status':'source-derived obligation; initial reconstruction, not a blanket acceptance',
      'shared_contract_justification':'Supplier windows may support several later consumers; each separately stated domain and conclusion remains required.'})

parts=[]
oldlines=OLD.read_bytes().splitlines(keepends=True)
for n,(tag,a,b,c,d) in enumerate(difflib.SequenceMatcher(None,oldlines,lines,autojunk=True).get_opcodes(),1):
    if c==d:continue
    matching=[u['id'] for u in uses if any(not(p['end_line']<c+1 or p['start_line']>d) for p in u['supplier_passages']+u['consumer_passages'])]
    parts.append({'id':f'V222-P{n:02d}','kind':tag,'start_line':c+1,'end_line':d,'excerpt_sha256':sha(b''.join(lines[c:d])),
      'old_range':None if a==b else [a+1,b],
      'scope':'Exact unchanged byte transport; retain previously accepted supplier/current-use scopes, without claiming no imports or a fresh full-proof audit.' if tag=='equal' else 'Changed source inspected directly; substantive uses listed separately, documentary changes remain documentary.',
      'overlapping_new_uses':matching})
assert parts[0]['start_line']==1 and parts[-1]['end_line']==len(lines)
assert all(a['end_line']+1==b['start_line'] for a,b in zip(parts,parts[1:]))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
meta={'schema':'v15-222-independent-source-reconstruction/v1','frozen_utc':now,'source':pin,
 'predecessor':{'path':OLD.as_posix(),'sha256':sha(OLD.read_bytes())},'delivered_source':{'path':DELIVERED.as_posix(),'sha256':sha(DELIVERED.read_bytes())},
 'reviewer':'/root/v15_sourcefirst_review','host_observation':json.loads((OUT/'REVIEW-SESSION.json').read_text())['host_observation'],
 'prior_exposure':['Full predecessor manuscript, earlier45/46-use inventories and accepted scoped reviews.','Accepted223/222 optimization artifacts, team summaries and own bounded conic/exponent analyses.','GLOBAL reported finite equation/map checks and three inherited reference defects before this freeze; I then read those passages and the exact three successor corrections directly.','No new222 author inventory or proposed coverage table opened before this freeze.'],
 'scope':'Independent reconstruction of the new222 source uses, including complete source-line transport coverage. This is a prior-exposed delta pass, not a blind full-manuscript reconstruction or mathematical approval.',
 'reading':'Read all new mathematical narrative, domains, six field quadrics, recovery identities, ordered affine/row maps, weighted definition and coefficient claims directly. Did not independently re-expand every one of196 printed quadrics in this initial pass.',
 'original_history':'Original8867 blind45 freeze, laterSF46 and exposed five-edit reconstruction remain authoritative and unchanged.',
 'uses':uses,'passages':parts,
 'findings':[{'id':'V222-REF-01','statement':'Delivered43c873 retained three references suggesting the233 predecessor alone proved the now222 main theorem.','delivered_lines':[33775,35022,35797],'disposition':'Successor002 directly checked: all three now route to new222 sections. This is a reference/assembly correction, not a demonstrated arithmetic defect.'}],
 'pending':['Post-freeze author inventory comparison.','Exact independent finite/math receipts and admitted-family dependency matching.','Current inherited coverage and old related-use corrections.','Actual selected proof-source contributor eligibility and exact final target adoption.']}
p=save('INITIAL-RECONSTRUCTION.json',meta)
manifest=save('INITIAL-FREEZE.json',{'schema':'independent-initial-freeze/v1','frozen_utc':now,'files':[p,{'path':(OUT/'freeze_initial.py').as_posix(),'sha256':sha(Path(__file__).read_bytes())}],'source':pin,'status':'Frozen before new222 inventory comparison; not final coverage approval.'})
print(json.dumps({'uses':len(uses),'passages':len(parts),'lines':len(lines),'freeze':manifest,'table':p},indent=2))
