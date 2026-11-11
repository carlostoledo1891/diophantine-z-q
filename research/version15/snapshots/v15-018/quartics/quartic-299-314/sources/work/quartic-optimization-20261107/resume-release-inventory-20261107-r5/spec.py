"""Explicit revision5 entries and direct baseline application edges."""
O='work/quartic-optimization-20261107/'
U='work/quartic-under300-20261107/10-combination/'
NEW=[{'id': 'N34-ORDINARY-ANCHOR313',
  'component': 'ordinaryAnchor313_330',
  'covered': ['ordinaryAnchor313_330', 'ordinaryAnchor313_329', 'ordinaryAnchor313_328'],
  'selected': False,
  'kind': 'exact_unique_constant_chain_lift_no_new_arithmetic',
  'author': '10',
  'reviewer': '05',
  'review': 'work/quartic-optimization-20261107/resume-review-ordinary313-20261107/REVIEW.md',
  'old': 'Symbolic C in anchorGamma313.',
  'new': 'Three source-specific ordinary lifts330/329/328.',
  'lemma': 'Unique output-linear weighted chains reach exponent2^25; Q=48v83^2+48v87^2+432v89^2. Substitution '
           'recovers source504/1903 exactly. Forget added coordinates to invert the extension, including every '
           'input fiber.',
  'targets': 'ORDINARY-GATE ANCHOR-RESCALING FINAL-COMPLETENESS SOS-FINITE FINITE-COUNTS',
  'sources': [('work/quartic-under300-20261107/10-combination/ordinary-anchor313/REPORT.md', 'Whole report')],
  'consumers': 'Only anchor rows504/1903 change; fresh1000..1016 prefixes. All281 other source rows and original '
               'coordinates unchanged. Actual maxima1627/3250/6496bits; the329 lift exceeds3247bits.',
  'inputs': 'Exact rational substitution and finite tables only. No new arithmetic application.'},
 {'id': 'N35-POSITIVE-SOS-WEIGHTS',
  'component': 'positiveWeights313',
  'covered': ['positiveWeights313', 'positiveWeights328'],
  'selected': False,
  'kind': 'positive_integer_weighted_sum_equivalence',
  'author': 'root',
  'reviewer': '01',
  'review': 'work/quartic-optimization-20261107/resume-review-weighted313-01/REVIEW.md',
  'old': 'Unweighted primitive residual squares of313 and its328 ordinary lift.',
  'new': '42 strictly positive integer weight overrides; every other weight1.',
  'lemma': 'Over Q, a sum of positive multiples of squares vanishes exactly when all residuals vanish. Identity '
           'witness maps. Weighting commutes with the328 lift because504/1903 and all added rows have weight1. No '
           'square root of a weight or extra coordinate.',
  'targets': 'SOS-FINITE FINITE-COUNTS ORDINARY-GATE FINAL-COMPLETENESS',
  'sources': [('work/quartic-optimization-20261107/root-sparse313/REPORT.md', '## Construction and proof'),
              ('work/quartic-optimization-20261107/root-sparse313/REPORT.md', '## Ordinary lift')],
  'consumers': 'Same IRs as anchorGamma313 and ordinaryAnchor313_328, but distinct polynomial artifacts5982/6024 '
               'monomials. Symbolic maximum186624*C^2+64; ordinary maximum6496bits. These weights are not applied '
               'to reciprocal307.',
  'inputs': 'Usual ordered-field property of rational squares and exact integer coefficients. No changed '
            'elliptic, local or approximation application.'},
 {'id': 'N36-AUXILIARY-ALL-E-VALUATIONS',
  'component': 'reciprocal307',
  'selected': True,
  'kind': 'new_domain_application_of_retained_local_detector_argument',
  'author': '05',
  'reviewer': '10',
  'review': 'work/quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md',
  'old': 'U_i,V_i in2E(K), supplying square f and even valuations.',
  'new': 'A/T/Z auxiliary points inE(K) minusT0, represented by raw reciprocal cubics; S pair unchanged.',
  'lemma': 'At unramified p>76176 with D unit, h^2=f(1-Df^2) forces v(f) even for v(f)>0 and for v(f)<0; v(f)=0 '
           'harmless. f=0 meansO and its zero leaf is omitted. Thus f^2/f^4/f^8 have exactly old periods before H '
           'or logarithms. Positive low tests exclude finite2torsion and imply formality at the same successful '
           'place.',
  'targets': 'MODEL BIQUADRATIC IDENTITY-CHARTS TORIC-POWERS GROUPED-POLYNOMIALS FACTORED-POLES '
             'H-TORSION-EXCLUSION',
  'sources': [('work/quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md',
               '## Valuation periods before logarithms'),
              ('work/quartic-optimization-20261107/reciprocal307-20261107/REPORT.md',
               '## Ratios, auxiliary domain and soundness')],
  'consumers': 'Physical Y pairs255/256,259/260,261/262 and Yalt190/191,208/209,220/221 retain meaning f^2/F^2 '
               'with imaginaryfactor2; all later powers, conjugations, shared-gamma groups, W/norm/pole rows '
               'unchanged. Full307 review establishes the conditional point/root inputs.',
  'inputs': 'Retained good-place curve equation and accepted shared314 unique-minimum/pole argument, now applied '
            'to allE auxiliary points. No new external theorem. Roots retain2E domain.'},
 {'id': 'N37-ZERO-SAFE-RAW-RATIOS',
  'component': 'reciprocal307',
  'selected': True,
  'kind': 'new_exact_regular_ratio_interface',
  'author': '05+10',
  'reviewer': '01',
  'review': 'work/quartic-optimization-20261107/resume-review-reciprocal307-01/REVIEW.md',
  'old': 'Square-root reciprocal ratios forced zeros atO.',
  'new': 'Raw ratios plus regular equations (1-DY)L+hS=0 and (1-DYalt)z-k=0; S=-1/z(H).',
  'lemma': 'AtO the regular coefficient equals1 and forces L orz to0. Away fromO/torsion, h^2=f(1-DY) gives '
           'z=f/h=h/(1-DY), hence L=z(U)/z(H). Use local tests to exclude finite2torsion before dividing. Both '
           'raw equations remain; no arbitrary identity output.',
  'targets': 'SHARED-RECIPROCAL IDENTITY-CHARTS RECIPROCAL-IDENTITY BIQUADRATIC LOG-TRANSFER',
  'sources': [('work/quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md',
               '## Raw reciprocal point and zero-safe ratios'),
              ('work/quartic-optimization-20261107/reciprocal307-20261107/REPORT.md',
               '## Literal coordinates and signs')],
  'consumers': 'Regular ratio rows2200..2211; L pairs232,240,244 and z pairs164,172,176. Shared S affine '
               'expression uses142/143/700/701 with original physical sign. Unchanged log z*Rlog=ell0*LP '
               'consumers receive same outputs.',
  'inputs': 'Explicit rational polynomial identities. Global H/V0 exclusions and local positivef tests are '
            'retained inputs, with their original order.'},
 {'id': 'N38-AUXILIARY-TORSION-LOG-TRANSFER',
  'component': 'reciprocal307',
  'selected': True,
  'kind': 'new_domain_application_of_group_and_formal_log_inputs',
  'author': '05',
  'reviewer': '10',
  'review': 'work/quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md',
  'old': 'Ui were integer multiples of P; only H required half-integral free indices.',
  'new': 'Ui=k_i R0+T_i and H=m R0+T_H, with rational free indices k_i/2 and m/2.',
  'lemma': 'Use [2m]Ui=[2k_i]H and [2(m-2)]Vi=[2(k_i-2n_i)]V0, killing both 2-torsion terms. Take logarithms only '
           'after formality. At odd p the indices are integral and one of h,h-1 is a unit. Transfer integrality; '
           'then F(0)=-1 gives a unit Li and depth10 H. Relative errors40 and12/40 yield unchanged congruences to '
           'the integer root labels ni. Completeness uses old doubled points and introduces no new finite or real '
           'choice.',
  'targets': 'MODEL H-HALF-INDEX H-LOG-IDENTITIES LOG-APPROX LOG-TRANSFER GROUPED-POLYNOMIALS '
             'HEIGHT-CONTRADICTIONS FINAL-COMPLETENESS',
  'sources': [('work/quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md',
               '## Integral identities and half-integral labels'),
              ('work/quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md',
               '## Denominators, real conditions and completeness')],
  'consumers': 'The same physical F+1=(253,2*254), F^2=(319-2*253+1,4*320-4*254), H4 groups and order10/40 label '
               'tests are retained. Scalar S, depth24 and its oriented scalar point are unchanged. Full307 review '
               'supplies exact Ui-Vi=Qi and root restoration before this step.',
  'inputs': 'Existing E(K)=Z R0+E[2], P=2R0; formal logarithm homomorphism and analytic unit at O; accepted '
            'shared314 H bootstrap. New internal factor2 identities and domain argument, no new external '
            'theorem.'},
 {'id': 'N39-GLOBAL-APPROXIMANT-DOMAIN',
  'component': 'reciprocal307',
  'selected': True,
  'kind': 'new_use_of_retained_global_nonvanishing_certificate',
  'author': '05',
  'reviewer': '10',
  'review': 'work/quartic-under300-20261107/10-combination/review-auxiliary-domain313/REVIEW.md',
  'old': 'Auxiliary doubled points used the real interval 0<=Df^2<=1; global N/Q certificates were already needed '
         'for H.',
  'new': 'Apply the same global N/Q nonvanishing to all E auxiliary cosets.',
  'lemma': 'N has no root modulo71 and Q has none modulo7; both primes split K, while coefficient denominators '
           'and leading coefficients are units. Any K-root would be locally integral by leading-term dominance '
           'and reduce to a forbidden residue root. Thus the old R=N/Q is globally defined and nonzero on the new '
           'domain. G2 needs no global positivity claim and is a unit after formal reduction.',
  'targets': 'H-NO-ROOT LOG-APPROX LOG-TRANSFER IDENTITY-CHARTS FINAL-COMPLETENESS',
  'sources': [('work/quartic-optimization-20261107/resume-auxiliary-domain-20261107/PROPOSAL.md',
               '## Denominators, real conditions and completeness'),
              ('work/quartic-optimization-20261107/reciprocal307-20261107/REPORT.md',
               '## Ratios, auxiliary domain and soundness')],
  'consumers': 'Unchanged rational-log circuits V0,V2,V3,V4 and ell0 denominator. The S-pair V2 remains unchanged '
               'but uses the same certificate. At V1 the G2 polynomial has no variable denominator. The old real '
               'interval is not assumed on arbitrary cosets.',
  'inputs': 'Retained exact rational N,Q and split-prime certificates from v13. New domain application of an '
            'existing input; no changed approximation coefficients or stronger precision.'},
 {'id': 'N40-ORIENTED-RECIPROCAL-CLOSURE',
  'component': 'reciprocal307',
  'selected': True,
  'kind': 'new_internal_complete_secant_tangent_identity',
  'author': 'root+BL+10',
  'reviewer': '01',
  'review': 'work/quartic-optimization-20261107/resume-review-reciprocal307-01/REVIEW.md',
  'old': 'Biquadratic pair charts with square witnesses for auxiliary points.',
  'new': 'Raw cubics and three slope equations: s(f-F)=h+k, s(h-k)=1-D(Y+fF+Yalt), s^2=c-D(f+F).',
  'lemma': 'Translate by T0: U+T0=(-Df,-Dh). The generic slope gives R=U-V. At f=F the first row gives k=-h; the '
           'second excludes h=0 and gives the exact tangent slope. The value yR=Dh-s(Df+c) satisfies the root '
           'curve by a universal polynomial identity. The U=O and V=O endpoints give -V and U; both O is '
           'impossible. Orientation is bound to the negative raw ordinates.',
  'targets': 'BIQUADRATIC MODEL IDENTITY-CHARTS RECIPROCAL-IDENTITY FINITE-COUNTS SOS-FINITE',
  'sources': [('work/quartic-optimization-20261107/root-reciprocal307/PROOF.md', 'Whole report'),
              ('work/quartic-optimization-20261107/reciprocal307-20261107/REPORT.md',
               '## Genuine points and complete oriented addition')],
  'consumers': 'New physical f,h,F,s,k pair bases are A:21/23/110/112/114, T:29/31/126/128/130, '
               'Z:33/35/134/136/138. Exactly54 old rows change and12 regular rows are added; all229 other rows '
               'are literal. The S-root is never reoriented.',
  'inputs': 'Elliptic chord and tangent formulas are used through an explicit polynomial identity and all '
            'exceptional branches. The old single-biquadratic closure is not assumed sufficient.'},
 {'id': 'N41-ROOT-RESTORATION-AND-COMPLETENESS',
  'component': 'reciprocal307',
  'selected': True,
  'kind': 'new_exact_root_recovery_and_retained_descent_application',
  'author': 'root+BL+10',
  'reviewer': '01',
  'review': 'work/quartic-optimization-20261107/resume-review-reciprocal307-01/REVIEW.md',
  'old': 'Root coordinates a,b,x with a^2=x and b^2=x^2-D.',
  'new': 'Keep a^2=c; delete only A/T/Z b pairs3/4,11/12,15/16; define b=yR/a in the proof.',
  'lemma': 'The exact height-product chain makes any c=0 force341=342=0, then343/391/392/393/394=0, contradicting '
           'inverse row352. Thus c and a are nonzero before contacts or logarithms. The root curve gives '
           'b^2=c^2-D, restoring the old oriented 2E roots, integer odd labels and height. Completeness maps old '
           'f=r^2,h=-Jr and chooses the rational chord or tangent slope; no additional H, CRT or real '
           'restriction.',
  'targets': 'MODEL ODD-NORM HEIGHT HEIGHT-CONTRADICTIONS BIQUADRATIC H-TORSION-EXCLUSION V0-EXCLUSION '
             'FINAL-COMPLETENESS',
  'sources': [('work/quartic-optimization-20261107/reciprocal307-20261107/REPORT.md',
               '## Recovering the root square chart and the old labels'),
              ('work/quartic-optimization-20261107/reciprocal307-20261107/REPORT.md',
               '## Completeness and simultaneous choices')],
  'consumers': 'cA=(82,2*83), cS=(84,2*85), cT=(2*86,2*87), cZ=(88,2*89). Product pairs337/338,339/340,341/342 '
               'have imaginary factor2 and the retained interstage factors2. Root-a pairs1/2,9/10,13/14 remain. '
               'Scalar S coordinates5 through8 remain unchanged. Root-a sign actions were checked on every row.',
  'inputs': 'Retained squareclass kernel alpha=1 iff the point is in2E(K), parity/anchor and root-product height. '
            'Apply them only after recovering the exact old root chart. No enlarged root domain or half-index '
            'height theorem.'},
 {'id': 'N42-ORDINARY-RECIPROCAL307',
  'component': 'ordinaryReciprocal307_324',
  'covered': ['ordinaryReciprocal307_324', 'ordinaryReciprocal307_323', 'ordinaryReciprocal307_322'],
  'selected': False,
  'kind': 'exact_unique_constant_chain_lift_no_new_arithmetic',
  'author': '10',
  'reviewer': '05',
  'review': 'work/quartic-optimization-20261107/resume-review-ordinary307-20261107/REVIEW.md',
  'old': 'Unweighted symbolic C source307.',
  'new': 'Source-specific ordinary324/323/322 with16/15/14 constant gates and one Q gate.',
  'lemma': 'Use the same unique chains and Q as N34. Only504/1903 change; all293 other rows are literal. Exact '
           'substitution fixes every original witness and input. Independent307 acceptance discharges the '
           'transport reviews source condition; it does not expand that reviews arithmetic scope.',
  'targets': 'ORDINARY-GATE ANCHOR-RESCALING FINAL-COMPLETENESS SOS-FINITE FINITE-COUNTS',
  'sources': [('work/quartic-under300-20261107/10-combination/ordinary-reciprocal307/REPORT.md', '## Exact maps'),
              ('work/quartic-under300-20261107/10-combination/ordinary-reciprocal307/REPORT.md',
               '## Executable verification and exact coefficients')],
  'consumers': 'Fresh1000 through1016 prefixes. Tables have '
               'variables/residuals/monomials324/312/6486,323/311/6483,322/310/6480 and maximum '
               'coefficients1627/3250/6496 bits. Full source307 SOS and all tables were reviewed. No positive '
               'weights are imported.',
  'inputs': 'Exact rational extension and finite coefficients. No new arithmetic use beyond the separately '
            'accepted source307.'}]
