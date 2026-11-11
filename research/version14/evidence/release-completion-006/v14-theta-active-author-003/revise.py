import copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent;OLD=OUT.with_name('v14-theta-active-author-002')
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def write(n,x):(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
assert sha((OLD/'MANIFEST.json').read_bytes())=='99cd3e626c4082d4ff9e398edde90a403a18e072791ccbb2b7609301ac9b6f69'
raw=(ROOT/'work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex').read_bytes();lines=raw.splitlines(keepends=True)
hyp={
2:'Fixed non-CM E/Q, weight-two newform, T2E and period convention; finite quadratic family with one real sign and fixed local squareclasses at2N; varying conductor primes good and odd.',
3:'The fixed original weight-two form and its integral image lattice; a rational comparison with T2E; nonzero projections of the modular-symbol span onto both Betti sign lines.',
4:'e is fixed at least max(3,v2(N)) and large enough for the fixed dyadic data; F is the squarefree odd conductor product; c=d_s=1+2^e*3*N_odd*F.',
5:'Finite Galois modules T/2^aT, the actual generic-point map of Spec O_K[1/2], and a finite extension L/K; upper inertia restrictions vanish.',
6:'The retained original classes and fixed smoothers; primitive quadratic character of conductor D; m is prime to the smoothers; tensoring occurs over the field where the character is trivial.',
7:'The same original classes, finite quadratic family and sufficiently deep dyadic levels; all characters factor through the displayed finite cyclotomic group and the maps use inverse deck action.',
8:'The actual primitive class and unnormalized weighted corestriction; k=2 and r=rprime=1; rational elliptic newform and fixed Betti/de Rham period bases; h is odd and signed.',
9:'Odd squarefree h ranges through the fixed local squareclasses at2N; the active varying primes are good and quadratic-ramified.',
10:'Non-CM rational Tate representation with the retained integral Euler system; both generic sign components nonzero, real eigenspaces rank one, inverse-Frobenius purity weight minus one and the rational unipotent condition.',
11:'N_K=2Nd, Nprime_K=cd_s are coprime; the enlarged original system exists on every required N_K-divisible index prime to Nprime_K; localization is at height-one primes where2 is invertible.',
12:'Actual j-star and full global cochains at the same rational constituent and height-one localization; odd local cones use H1(I_q,Vchi) and their nonzero determinant differential.',
13:'Finitely many fixed old local types; local rational Tate invariants vanish, local derived control and H3_Iw=0 apply; the actual retained class and full-global index are unchanged.',
14:'The retained Kato system with common real sign and local squareclasses; E[2](Q) is the full two-dimensional trivial representation; ordinary real degree zero is retained.',
15:'The actual continuous positive cochains over successive finite Artin quotients have the finite residual cohomology and bounded models used in this proof; transitions are surjective and coefficient changes are derived.',
16:'K_n=Q(zeta_(2^(n+2)))^+ is the real cyclotomic tower; S_n lies above2 and a fixed finite odd support; scalar coefficient F2=mu2 and ordinary real cochains are used.',
17:'The real cyclotomic dimension calculation and compatible finite free models; fixed finite support; full rational E[2]; B=O[G] is the stated local ring, and the real sign is fixed.',
18:'One generator of the fixed real invariant line; the same retained z=F_E Z_F; a positive integral lift after the one fixed clearing power and the real factor2.',
19:'The same positive complex and determinant basis; full-global K2 for z at every height-one prime away from2; free rank-two model over O[G] and the coefficientwise intersection A intersect O=Lambda.',
20:'The fixed scalar and original determinant basis at a corank-zero constituent with finite two-primary Sha; the numerical nonzero-value calculation also assumes Lstar(h) nonzero.',
21:'The actual E^h/Q has full rational2-torsion and corank-zero finite Selmer group; use the bounded real Kummer complex with full H0, finite local Kummer conditions, and compact/discrete duality limits.',
22:'The same corank-zero finite-Sha constituent, retained class, cone maps, and local bases; K3 is evaluated before canceling unused local terms; the forward theorem supplies these hypotheses only at nonzero Lstar.',
23:'Fixed sign and local unit filter at S0 containing2N; a positive squarefree reference D0 has nonzero Lstar(sigma D0); use its actual Shimura–Waldspurger packet.',
24:'A smooth local packet vector has nonzero D0 functional, D0 is a unit, and the unit character has the prescribed parity; choose depths before normalizing the global form.',
25:'The nonzero scalar good-Hecke eigenspace has all old multiplicities; D and D0 are positive squarefree in the same squareclass at every level prime, including2; reference central value is nonzero.',
26:'The characteristic-zero half-integral section model over a number field contains the nonzero reference eigenspace; all linear character, support, cusp and Hecke conditions are algebraic; general Hasse bounds separate unary eigenvalues.',
27:'The chosen algebraic vector is reference-normalized and both conjugation and character twist lie at a common level supported on S0; D/D0 is a local square at the character conductor.',
28:'The already normalized even source and its fixed initial filter; later finite exclusions avoid D0; the good Hecke recurrence is used outside enlarged support; the arithmetic coefficient lower bound is available.',
29:'The fixed E/Q has full Selmer corank one; the prepared positive unit filter contains1; signed nonvanishing applies to the actual modular form with all old primes in its finite splitting set.',
30:'The conductor-one genus point lies in the biquadratic field of degree at most4; h_star has nonzero central value and D_w has nonzero derivative; the unaveraged height formula and actual cusp-torsion multiplier are available.',
31:'The actual A=E^(D_w) is non-CM and Q=L P_(D_w) is rational nontorsion; compatible division points are chosen; F0 is a fixed finite Galois extension and actual complex conjugation is retained.',
32:'The same fixed sigma and witness, at finite precision M>c_w; exclude bad primes and2; use good reduction of the actual elliptic curve and its prime-to-residue-characteristic division points.',
33:'An actual detecting stage with ell_0 odd good and N prime to ell_0; the quaternion algebra is ramified exactly at ell_0 and infinity; cyclic N-enhancement and actual parametrization with killed cusp translations are retained.',
34:'The actual Eichler local orders and selected cyclic quotients; fixed h_star and root characters; dyadic projectors, nilpotent support at primes of m and trace-zero nonzero residue at ell_0.',
35:'The actual finite supersingular class set, P_M and local Schwartz weights; each definite order-unit group is finite; all lifts are integral in the fixed character ring.',
36:'The specified nondegenerate ternary form and actual compact open locally constant weights; the common additive character and self-dual measures are fixed, including at2.',
37:'The same additive character and Weil-index convention for both ternary forms; Q_B is trace-zero quaternion norm and m is the fixed positive odd integer.',
38:'Nondegenerate ternary Q and Q0 over Q_p or R, the stated Fourier convention and self-dual measure; use the same central element and lifts in the common double cover.',
39:'The actual Q/Q0 eigenvectors at congruence depth large enough for their lower-unipotent and character conductors; common lifts and inverse-idele classical convention.',
40:'At primes outside the prescribed support the algebra is split, the odd trace-zero lattice is self-dual and weights unramified; globally Q is positive definite and finite weights are Schwartz–Bruhat.',
41:'The support has v_p(Q_B)=1 at every p dividing m and integral norm elsewhere; keep finite weights and replace Q_B and its real Gaussian by Q_B/m.',
42:'The prime p avoids the entire coefficient support; actual p-neighbors, mass1/Aut, norm characters and parametrization eigenvalues are retained; nonintegral Fourier indices mean zero.',
43:'The maximal imaginary quadratic order has units plus or minus one, split prime-power level and an odd inert detector prime; actual integral spectral projectors and a rational embedding into B are used.',
44:'The fixed CM type, one reduction place and actual reference point; maximal order, split prime-power level and odd inert ell_0 prime to N*disc(F); separate CM, good-reduction and enhanced supersingular inputs are retained.',
45:'The same actual P_M and labelled embeddings; order-unit stabilizer equals plus or minus one, c0 clears all order-unit masses, L kills cusp translations and lambda_M has Frobenius sign plus one.',
46:'The actual odd theta form and unaveraged point comparison; for the native-index inequality D is a known simple zero, while the visibility implication treats every admissible D and kills torsion by the same L.',
47:'The actual source form with full rational2-torsion and coefficient support S; added odd p lies outside S; unary corrections and their old/new level blocks are kept separately.',
48:'The originating squarefree parameter is (U minus J)r; integral all-index recurrences hold; for odd forms fix a finite operator budget and R at least2 before choosing a valid actual stage.',
49:'The actual weight-two forms theta H_U and correction blocks over a common finite coefficient field; retain all cuspidal and Eisenstein constituents, old multiplicities and diamond translates.',
50:'A fresh prime avoids coefficient support and U; use the same source, phase, minimum and valid stage for every omission; stage precision leaves at least one integer factor2 after division.',
51:'The closed integral trace module and actual diamond correction are available; two distinct fresh primes fit the fixed valid-stage budget and satisfy the integer divisibility estimates.',
52:'Actual weight-two cuspidal constituent of a block whose odd local level exponent is at most1 and determinant is primitive quadratic there; use coefficient prime2, normalized induction and both stated duals.',
53:'The conductor-one principal-series new line with the lower-right character convention; actual Whittaker Fourier normalization; separate unramified old blocks and Eisenstein character pairs are retained.',
54:'The actual characteristic-zero O.12 identity on the closed integral module; common precise quotient realizes all fresh Frobenius elements and stationary tests; omissions keep the same source and stage.',
55:'Compatible finite typed graphs within the fixed budget and fixed-U elementary-quotient invariance; CRT/Dirichlet supplies fresh copies with compatible reciprocity bits.',
56:'Fixed modular A/Q, S contains2,3 and its bad primes; a nonempty signed unit filter has even root number and finite exclusions are fixed for this application.',
57:'Prepared positive odd-sign h-filter; dummy label count is fixed before h but realizing primes afterward; apply nonvanishing to the actual varying E^(h a q0), retaining fixed even-source minima.',
58:'Finitely many prepared even sources and nonempty seeds; stationary one-symbol address construction and common fixed-denominator scalar; its base is known corank zero.',
59:'The native height comparisons, arithmetic lower bound and already proved rough companion; no odd minimum has yet been selected.',
60:'The actual detecting sequence has M tending to infinity, fixed visible witness and all-D coarse bound; one nonprincipal ultrafilter is chosen and each operator budget is finite.',
61:'The tested squarefree output range and valid stage are fixed; visibility is used only inside that range; choose the negative even unit k with fresh ramification before address dimension.',
62:'Fixed complementary twist k<0 with old unit at abs(k); new source for E^k normalized at1; D is prime to the full new support and in its prescribed square unit classes.',
63:'Assume no nonempty K-split unit seed for the normalized even source; use actual integral B,H and all theta convolution terms, with determinant scalars on each actual block.',
64:'The preceding no-seed assumption and trace identities; matching fresh K-split primes and the positive-twist phase; for the contradiction choose p=1 mod4 with ell nonsquare and k square modulo p.',
65:'The same odd minimum and ultrafilter; bounded elementary label groups and their projection data; each finite graph cutoff has a valid-stage large set before selecting its truth table.',
66:'Both final symbols have nonempty unit seeds and total projected label zero; the actual common alphabet projects surjectively to each separately; finite address dimension is fixed.',
67:'Compatible terminal and stationary data; nonempty contraction outputs and primary isolation rules; networks use commuting nilpotent pair differences and actual finite graph realizations.',
68:'At each nonzero address the one or two terminal polynomials are nonzero; use the ordinary polynomial ring, finite dimension and disjoint auxiliary networks with the specified first-degree actions.',
69:'Fixed k,K, common alphabet and address dimension; the full finite graph/output budget is chosen before an actual theta stage; prime realizations retain all coefficient exclusions and K-splitting.',
70:'The final family and same retained Heegner coordinate, bases and integral support correction; finite Sha only at known nonzero-address simple zeros, never assumed at the unknown base.',
71:'The fixed-field denominator and residual coefficient-transfer assertions for that same coordinate; choose M above B+2c_det before dimension, graph budget and actual theta stage; nonzero L(E^k,1).'}
c=json.loads((OLD/'COMPONENTS.json').read_bytes())
for x in c:
    if x['use']['classification']!='dependency':continue
    n=int(x['use']['id'].split('-T')[-1]);assert n in hyp
    x['use']['assertion']['hypotheses']=hyp[n]
    for field in ('available_assertion','needed_assertion'):x['connection'][field]['hypotheses']=hyp[n]
    x['connection']['connecting_derivation']['output_assertion']['hypotheses']=hyp[n]
    x['historical_source_navigation']=x.pop('retained_separate_inputs')
    x['source_ancestry_status']='Historical source families are navigation only. The active conditions are the clause-specific hypotheses; unrelated historical constructed objects and special-case hypotheses are not imported.'
    if n in (20,33,45):
        a,b={20:(14195,14371),33:(15014,15087),45:(15842,15952)}[n]
        p={'pin':{'side':'head','path':'manuscripts/quartic_v14.tex','sha256':sha(raw)},'start_line':a,'end_line':b,'excerpt_sha256':sha(b''.join(lines[a-1:b]))}
        x['use']['supplier']['location']=copy.deepcopy(p);x['use']['inline_argument']=copy.deepcopy(p);x['connection']['connecting_derivation']['location']=copy.deepcopy(p)
    x['connection']['use_sha256']=digest(x['use'])
write('COMPONENTS.json',c)
write('SOURCE-ANCESTRY.json',json.loads((OLD/'SOURCE-ANCESTRY.json').read_bytes()))
write('DELTA.json',{'predecessor_manifest_sha256':sha((OLD/'MANIFEST.json').read_bytes()),'changes':'Replace all blanket historical hypothesis concatenations by actual clause-specific conditions; move old family contracts to navigation only. Extend T020 to include central cancellation, T033 to include Ribet/class-set/Frobenius/specialization, and T045 to include precision and witness conclusion. Retain earlier T043/T044 primary repairs.','reviewer_findings_addressed':['Real cyclotomic versus imaginary-field shortcuts','General Hasse bound versus CM-generator special case','Degree-at-most-four torsion injection versus special fixed K0 primes','Finite-field Kummer specialization versus W0 descent','Split-cubic halving versus rank-one premise','Real duality versus imaginary shortcut'],'unchanged':'All statements, classifications, consumer passages and mathematical conclusions.'})
for x in c:
    if 'connection' not in x:continue
    assert digest(x['use'])==x['connection']['use_sha256']
    for p in [x['use']['supplier']['location'],x['use']['inline_argument'],x['connection']['connecting_derivation']['location']]+x['connection']['consumer_locations']:
        assert p['excerpt_sha256']==sha(b''.join(lines[p['start_line']-1:p['end_line']]))
write('CHECKS.json',{'components':len(c),'connections':70,'raw_spans_and_use_digests':True,'historical_conditions_imported_as_active':False,'source_ancestry_closed':False})
write('MANIFEST.json',{'files':{p.name:{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(sha((OUT/'MANIFEST.json').read_bytes()))
