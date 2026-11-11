# Independent mathematical composition review: frozen395

Accepted on the pinned, inherited arithmetic inputs. The exact candidate below has 395 total rational variables, including one input and 394 existential witnesses, 365 quadratic residuals, and 6,341 monomials in its primitive sum of squares. Its rational zero projection onto the input is the integers. The polynomial has degree four, content one, and maximum coefficient 16*3^(2^26).

Reviewer: `/root/astra_quartic_opt03_depth`. I did not author this composition, its scaled biquadratic charts, H-domain enlargement, preparation-zero argument, or normalized pole. I previously authored the rational-log and primary reciprocal components, which entered the accepted baseline through other reviewers. This review independently checks the new composition and its mathematical interfaces; it does not purport to reprove all published arithmetic inputs behind the accepted baseline.

No actual error requiring a patch was found. No author file or released manuscript was changed. This is acceptance of these frozen mathematical and numerical artifacts, not a claim that a separately written manuscript has been reviewed or published.

## Frozen scope and evidence

Paths in this table are relative to `work/quartic-under400-20261107`.

| Artifact | SHA-256 |
| --- | --- |
| `10-combination/combined417-ir.json` | `b7d124eb221df55d49131854b541a4c97c5689b18882dfa4a24cc6b8c2d1b6a9` |
| `10-combination/inputs/composition417-review.md` | `f0242de339c9a659ecb447aeea6208da0c18cb7face4932b0595606524a3bf44` |
| `10-combination/combined395-ir.json` | `440282e5b3b8a9a19d5d7009399736257a5279105485a1bec073138a64758e6a` |
| `10-combination/combined395-polynomial.json` | `3d7c165ffb4171fe3dc11559b1a2bb29ff24dcb02289303d4544e8c5a5667d85` |
| `10-combination/REPORT395.md` | `380be2dbb69d6d45ff0c41c3753b1a59838f2bbae12233abac50d47fc76c491c` |

The main chain is 417 -> 401 -> 399 -> 396 -> 395. My `check.py` also independently replays 423 -> 417. It derives every component delta from its complete before/after files, checks its application to the actual predecessor, and compares the complete resulting coordinate records and residual records. It checks component and review hashes, all surviving consumers, every final coefficient, unique IDs, the sole input, and the fixed constant. It imports no producer or other verifier. `CHECKS.json` records the hashes and full delta inventories.

In addition to transport, the checker derives the actual beta/contact polynomial, scalar powers, norm square, W and signed pole input from the literal rows. It reconstructs the enlarged H/V0 equations, the actual rational approximation, all four scaled chart equations with their squared-output meanings derived from the old rows, and all five normalized-pole substitution identities. The complete final SOS comparison passes. The fixed constant is kept symbolic; no expansion of 3^(2^25) is used.

I read the 417, 399, 396 and 395 reports; the independent 417 review; the H-domain proposal and review; the identity-extension argument; the preparation-zero proposal and review; the normalized-pole proposal and review; and my earlier scaled-chart, scalar24, and correction reviews. I revisited the actual source statements for preparation zero, real progressions, the zero-tolerant one-place detector, the root-height implication and the scalar O/T0 argument in `quartic_v12.tex`, SHA `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. Relevant labels include `v5:preparation-zero-bridge`, `v5:real-progression-bridge`, `lem:v5-one-place`, `v9:eq:height-transfer`, and `eq:v12-duplication`. These are the inputs actually needed below.

## Soundness starts before interpreting logarithm ratios

Write rho^2=2, d0=3-rho, D=d0^2, and E: y^2=x^3-Dx. The retained odd root charts still give four nonzero odd multiples Q_i=[n_i]P, including labels (n,a,t,b_root), with P=2R0 and 2E(K)=ZP. The exact root equations are untouched. Their nonzero square roots a_i satisfy c_i=a_i^2 and b_i^2=c_i^2-D. In particular c_i>0 at both real embeddings and a_i is nonzero. The scalar point Rscalar=[s]P, s=a-1, retains its nonzero guard and anchor.

The new input label is beta=51(2X+1)^2+2504. The checker eliminates the literal intermediate coordinates 487,488,489 and proves that the affine expression consumed by the scalar powers is

    r=beta(beta-1)(beta-2401)(32beta+343)(2beta-1).

For every rational X, beta>=2504, so r>0 and c=r+4896>0. These statements do not require X to be integral.

The final H equations are exactly x*fH=1 and S^2=x-D*fH, with physical x=v90+2*v91*rho and S=v142+v143*rho. Thus H=(x,xS) is a finite point with nonzero abscissa. Its abscissa need not be a square. The nonzero field element fH has nonzero norm q. The actual scalar equations are

    B=(z0^2+r*z1^2)/r^32,
    W=(B^2+r*q^2)/r^32,
    b_pole=c*r*W^2.

Here z0,z1 are initially just the stored rational slots; their ratio meaning will be established later. Already q!=0 and r>0 imply W>0 and b_pole>0. Consequently the scalar pole input is nonzero before interpreting those ratio slots. This prevents a circular reliance on the deleted preparation inverse or on a logarithm denominator.

More precisely, the current rows give v600=r^2 and

    (v600+4896*r)*v525+82479248*v526=0.

If J is the positive coefficient in J*v525-v542^2=0, the actual pole normalization is b_pole=-K*v526 with K=82479248*J>0. My checker obtains K independently from the old factored h row and verifies this equality. Thus v526 is strictly negative and cannot create an extra zero component in the normalized pole.

## The larger H-domain and exceptional points

The inherited group description gives H=[m]R0+T with m integral and 2T=O. Put h=m/2 as a rational index, not an asserted group operation [h]P. We must exclude exceptional H before dividing by either denominator logarithm.

All finite points in E[2], P+E[2], and -P+E[2] have fH a unit at every consumed place over p>76176. The two already forbidden cases O,T0 need no extra argument. For the others, the abscissa formulas use cP=x(P), d0, cP-d0 and cP+d0, whose norms are 41^2/64, 7, 17^2/64 and 63^2/64. The translation abscissae are -D/cP, d0*(cP+d0)/(cP-d0), and -d0*(cP-d0)/(cP+d0). The factors and their inverses are integral outside {2,3,7,17,41}; this proves a unit assertion at each place, not merely a unit norm.

For any of the three contact radicals, the retained one-place detector would then force positive valuation of fH via its order40 test, a contradiction. The detector lemma applies to arbitrary field tests, including zero tests, and needs no interpretation of the possibly unconstrained LP slots. Hence all three radicals would equal one. The unchanged root-height implication would give Bmax^2-6<7*Hcal, whereas the independent scalar anchor gives Bmax>=|a|>(40*Hcal)^10. These contradict each other. The exclusion uses no scalar upper bound for h(beta), so it precedes the scalar ratio argument without circularity.

It follows that m is not 0,2,-2; H and H-P are nontorsion, S!=0, and H is neither P nor -P. This is stronger than merely declaring V0 nonidentity.

The actual remaining V0 equations use the fixed P chart (aP,bP,cP), and are

    d=cP*x+D, N=aP*S-bP, d*v=N,
    fV0*fH=v^2,
    Tprime=-2D-aP*bP*S+2D*bP*v,
    Tprime*ell0+aP*N*R(w0)=0.

The checker matches these field equations including the physical factor 2 in x. If d=0, the curve equation gives an excluded translate by T0. If N=0, x*N*(aP*S+bP)=(x-cP)*(cP*x+D) likewise gives excluded points. Hence d,N,v are nonzero. Ordinary subtraction is valid because x!=cP, and gives x(H-P)=1/(x*v^2), y(H-P)=Tprime/(aP*d*x*v^3). Thus fV0 is the actual reciprocal abscissa and Tprime is nonzero. The last equation gives ell0=z(H-P)*R(w0).

One cannot reuse positivity of w0 on this larger domain. Instead the actual numerator N8 has no root modulo71 and denominator Q2 has no root modulo7, as my checker verifies over every residue. Both polynomials have integral coefficients and unit leading coefficient at their respective primes, and those primes split in K. A K-root would give a Q_p-root; negative valuation is impossible by the leading-term valuation, and integral valuation contradicts the residue calculation. Therefore neither polynomial vanishes anywhere in K. The checker binds this argument to the literal final approximation equations, not just a copied coefficient list. Consequently ell0!=0 globally even for negative real abscissae. At formal points the same local tail estimate still has order40.

## Scaled charts, identities and local comparison

For each root chart, the new variables satisfy

    V*Q=c_i*W,
    V^2+Q^2+D*W^2+2b_i*W=1,
    a_i*I=b_i*V+c_i*Q+D*V*W,
    a_i*K=-b_i*Q-c_i*V-D*Q*W,
    I*L_i=V*S, K*zVi=-Q,
    D*c_i*YU+I^2=c_i, D*c_i*YV+K^2=c_i.

The inverse map is rU=V/a_i, g=Q/a_i, J=I/a_i, k=K/a_i, fU=rU^2, fV=g^2, u_aux=c_i*rU+b_i*g. The cross equation forces W=rU*g. The three universal identities in the accepted scaled-chart proof recover both reciprocal conics and the oriented difference equations. The only divisions are by nonzero a_i,c_i,D and c_i+D*rU^2, the last positive at both real embeddings. Comparing the recovered conics with the last two equations proves YU=rU^4=fU^2 and YV=g^4=fV^2. My checker independently derives the physical YU/YV expressions from the old square rows and matches all these final equations.

No nonzero condition on rU or g is introduced. At rU=0, U=O and V_i=-Q_i; at g=0, U=Q_i and V_i=O. Both cannot vanish because Q_i is nonidentity. The reciprocal J and k are nonzero by the same norm-7 obstruction as in the accepted chart proof. At O, f and z are their regular extensions with value zero; the full logarithm and approximate numerator also have value zero. Thus the surviving L_i and LP_i equations represent the actual ratios, including zero numerators, once the H/V0 denominators established above are used. No value of x(O) enters a height estimate: all height targets are the unchanged nonidentity roots.

At consumed odd primes, h and h-1 are p-integral and one is a unit. The exact integral group identities are

    [m]U_i=[2u_i]H,
    [m-2]V_i=[2(u_i-n_i)](H-P).

They kill the possible two-torsion T. Formal logarithms are applied only to the formal points in these equations, never to R0 or T. The full ratios are u_i/h and (u_i-n_i)/(h-1). Analytic unit factors, defined with value one at O, connect them to the actual stored ratios. A unit denominator first makes one ratio integral; the positive-order cross-test then transfers integrality to the other. Only afterward does one infer depth at least20 for a nonidentity U_i. An identity numerator instead has exactly zero error.

The primary error therefore has order80; the alternate error has order12 for i=1 and order40 for i=2,3,4. These suffice for the retained order10 and order40 tests. Multiplication by p-integral h and h-1 and subtraction give the same label congruences as before. No modular division by m is used. Conjugation at split places and its valuation-preserving action at inert places are unchanged. The scaled maps fix every ratio and squared-test output consumed here.

## Scalar depth24, height margins and the integer bridge

At a consumed scalar prime p>76176, an odd eta=v_p(r) is positive independently of c. Indeed if v_p(beta)<0 then 51 is a unit and v_p(beta)=2v_p(2X+1) is even; all five contact factors have that valuation, so eta is even. Otherwise the factors are integral. Only after this argument is c=r+4896 declared a p-unit. No assertion that c is a unit at every large prime is made.

The scalar pole obstruction gives eta+2v_p(W)>0. The two terms of each norm numerator have distinct valuation parity; allowing zero terms with infinite valuation causes no problem. The actual nested equations imply

    v_p(B)>63eta/4, v_p(q)>61eta/4,
    v_p(z0)>191eta/8, v_p(z1)>187eta/8.

Thus both coefficient depths are at least24, not necessarily24eta. Positive norm valuation supplies a place with v(fH)>0, hence H is formal there. The actual scalar ratio gives v(z(Rscalar))>=v(z(H))+24.

The source explicitly treats both signs of v(x(Rscalar)): Rscalar may approach O or T0. The exact duplication formula makes [2]Rscalar formal with the same z valuation in both cases. In the enlarged H domain the appropriate identity is

    [m]([2]Rscalar)=[4s]H.

Formal-log isometry yields v_p(s/h)>=24. Since h is p-integral and nonzero, v_p(s)>=24. This step uses neither a square root of x(H) nor integrality of h at2.

The inherited exponent19 theorem therefore gives h(beta)<=Hcal*|s|^(19/24). The literal unchanged anchor gives log2|s|>25165823.5 and Hcal<2^2093966. The exact inequality (5/24)*25165823.5>2093966+7 implies h(beta)<|a|/40; the retained anchor also gives log(48Hcal)<|a|/40. These margins hold for either sign of s.

The unchanged order40 argument forces the Lucas polynomial F to vanish, and hence log Bmax>|a|-3. If n-beta were nonzero, the order10 argument would give log Bmax<10log(48Hcal)+19h(beta)<29|a|/40, a contradiction. The final input conclusion uses the retained oddness of n. For tau=2X+1=u/v in lowest terms, n=51tau^2+2504 integral forces v^2|51, hence v=1. Since n is odd, tau is odd, and X=(tau-1)/2 is an integer. Integrality of beta alone is not substituted for this argument.

## Completeness uses one simultaneous global construction

For an integer X, tau is odd. The established exact local calculations give v2(r)=2 with r/4=1 mod8, v3(r)=1, and r=15 mod17. Since 4896=2^5*3^2*17, c/r=1+4896/r is a square in Q2,Q3,Q17. Thus cr is a positive integer, a local square at these places, with valuations4,2,0 respectively.

First fix the full support S*=supp(cr) union {2,3,17}. New large prime factors of c are included. In particular17 is explicitly included even though it does not divide cr. Let G be the paired real orbit closure and m0=|G/G0|. The actual source real-progression lemma supplies density in G0 for progressions whose residue and modulus are multiples of m0; its weaker boundedness statement alone would not suffice.

Choose a positive integer progression of shared indices divisible by64,m0 and the finite formal-subgroup indices needed at S*. Its positive tail is dense in G0. Choose H0 in that same progression sufficiently close to (O,O) in the paired real topology, making q(H0) small while retaining every finite depth bound. Then fix H0 and choose a scalar-index progression divisible by6,m0, the anchor modulus and the larger finite subgroup indices. Its positive tail is again dense in G0. Choose a sufficiently large positive s there with Rscalar close enough to (O,O) that both coefficients of z(Rscalar)/z(H0) are small. The same globally defined points, not separately chosen local and real solutions, meet these conditions.

These choices make 0<b_pole(H0,Rscalar)<17/4. The finite bounds at p|r can be at least8eta on fH coefficients and24eta on ratio coefficients, giving v(q)>=16eta, v(B)>=16eta and v(W)>=0. At p|c, p not dividing r, positive coefficient depths suffice. At17 impose positive depths separately; they give v17(W)>=4. Consequently b_pole has square reduced denominator, is a local square at2,3,17, and satisfies v2>=4,v3>=2,v17>=8, more than the specialized pole theorem requires.

Now fix Rscalar. Real continuity gives a nonempty neighborhood of H0 in G0 on which 0<b_pole<17, and finite continuity gives h=h0 modL preserving the required depths. Require64|L and m0|L. Fix the remaining labels, roots and scales and increase L for their fixed continuity requirements. The finite union of comparison poles has measure zero in G0 by the source hypothesis; choose a nonempty open set with compact closure within the previous neighborhood and away from those poles. Uniform comparison bounds on that compact set are fixed before the contact-prime choices.

Only then choose the later primes. The separation argument still permits every added fixed odd factor of L and gives the same compatible CRT: h=0 mod Pi^19*Mminus, h=1 modMplus, h=h0 modL, with gcd(Mminus,L)=16 and the other required gcds one. Because64|h0, compatibility is retained. The resulting progression has both residue and modulus divisible by m0, so its positive tail meets the chosen open set in G0. Choose one sufficiently large h. This single final H preserves the finite preparation, real bound, comparison domains, uniform estimates and contact depths simultaneously.

Apply the existing preparation-zero theorem to this final b_pole. Its actual hypotheses are positivity, b_pole<17, square reduced denominator, local squareness and the three valuation lower bounds; all have just been checked. It produces fresh pole witnesses with U=b_pole and allows zero private values. Completeness is not a claim that every old preparation can be specialized. The subsequent normalization is an exact rational change of these private witnesses: multiply/divide coordinates51,52,53,54,532 by v526 and coordinates527,534 by v526^2, and set old531=v526^2. Each of the five pole rows is multiplied by v526^2. No private coordinate is divided by, so all its zero branches survive.

Completeness may and does keep H in the original subgroup2E(K), which is allowed by the larger H chart. Forgetting its square-root coordinates and applying the scaled comparison maps and normalized pole maps preserves every shared value. No new real/local approximation theorem or new prime theorem is needed.

## Decision

The actual final equations support the refreshed soundness argument on the enlarged H domain and the simultaneous completeness construction above. The maps preserve every shared test, ratio, root and scalar value at their interfaces; all nonzero divisors have been justified in the required order. The exact frozen395 candidate and polynomial are accepted. The inherited published arithmetic theorems remain dependencies, and a later altered IR or manuscript requires its own review.

Reproduce the independent finite evidence with `python -B check.py` in this directory. Its only output file is the local `CHECKS.json`; all earlier packets and all author artifacts remain untouched.
