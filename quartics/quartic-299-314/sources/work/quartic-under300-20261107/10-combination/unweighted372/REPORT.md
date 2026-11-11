# Contact-polynomial detectors with a bounded pole input

This proposal reduces accepted390 to372 rational variables. It is pending independent arithmetic review. The exact candidate has342 quadratic residuals and6574 quartic monomials, degree four, integer content one and maximum coefficient16*3^(2^26). It changes the height-detector weights and pole inputs. It does not change any point, logarithm, test value, height scale, scalar predicate or anchor equation.

Author: `/root/astra_quartic_opt10_combination`. No publication is proposed above the below300 milestone. The separate384 scale-removal and387 guard-removal files remain unchanged. This candidate includes neither of their changes by provenance, and is built directly from390. It subsumes the six scale-power deletions of384, while retaining all three real-component inverse guards.

## Frozen artifacts and exact finite scope

The source `../../01-elimination/squared-h/candidate390-ir.json` has SHA256 `c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced`. Its acceptance `../../03-depth/review390/REVIEW.md` has SHA256 `61b755da24b3934ca8725159ac96c59c8b5090a4c7a032fe5487646853e7a667`.

The candidate `candidate372-ir.json` has SHA256 `ff487de4c99d74214eef654dafb1bb2a0a5faca0df3fde5cb636de92297222ce`. The full table `polynomial372.json` has SHA256 `5bcf7797a65f954719fcd21515a3b6bf022e28876f58aa5ca42a23643377336f`.

The eighteen deleted coordinates are352,353,354,384,395,396,397,400,401,402,432,443,444,445,448,449,450,480. They consist of six private scale-power gates, three eDelta gates, and the q1/a/b coordinates in each toric circuit. `CERTIFICATE.json` lists all removed and changed residuals. The producer-free `verify.py` reconstructs every remaining row from the source under the explicit substitutions below, checks all deleted-coordinate consumers, derives each physical contact polynomial, checks the retained Laurent weight circuits, and expands the full primitive SOS. It imports no producer.

## New detector and its quadratic realization

For each of the same three positive rational square scales A, put t=A*lambda and

    R=F5(t)=t(t+1/2)(t+1)(t-1/2399)(t+32/407), E=1/R.

The retained F/t^2/t gates make R an affine expression in existing coordinates. The new E definition is the quadratic equation E*R=1. There is no delta denominator. Define

    W=product_j(1+E^(2*m_j-1)*D_j^2),
    z=Norm(W)/(2*Re(W)),
    B=R*z^2/(1+R)^2.

The orders remain m=1,10,40 and all unweighted D_j are the same physical field tests. The scalar predicate is unrelated to this new R and is unchanged.

The product circuit retains the old symbolic q1/q10/q40 polynomial identities, after setting q1=E, q10=E^19 and q40=E^79. In each old toric chain substitute

    q1=E, a=1, b=R.

The remaining equations become

    E*c=R^2, c*d=E^5, c*q10=d^2, c*q40=q10^4.

The retained q1-square and q1-cube gates give E^2 and E^3, so the E^5 term remains quadratic. The retained q10-square gives the fourth power in the last equation. Since E*R=1, these equations force c=R^3, d=E^8, q10=E^19 and q40=E^79. Every product factor is therefore exactly the displayed new factor. No division by a possibly zero field test is used.

The retained norm equation is

    Re(W)^2-2*Im(W)^2=2*Re(W)*z.

The real-component inverse remains, so W and z are nonzero over Q(sqrt2). Instead of the old eDelta/B equations, use the single quadratic equation

    B*(R+E+2)=z^2.

Indeed R+E+2=(1+R)^2/R. This equation also excludes R=-1 because z!=0. Thus B is nonzero and has exactly the displayed meaning. The old normalized/factored preparation-zero pole rows consume this new B without alteration.

## Soundness at the required primes

Let M_r be the same odd-contact radical of t used by the source height theorem, omitting primes at most76176. At a prime p dividing M_r, exactly one normalized contact factor has odd positive valuation. All fixed contact differences are units. In particular

    alpha=v_p(R)>0 is odd, and v_p(1+R)=0.

This assertion concerns the required radical primes, not every prime at which the rational function R might have odd valuation. Negative valuations of R outside the required radical are not used.

At a place over such a p, each nonconstant factor term has valuation

    2*v(D_j)-(2*m_j-1)*alpha,

an odd integer. Consequently the factor is nonzero and its valuation is its minimum with zero. Write lambda_p for the maximum valuation of W over the places above p. Every factor valuation is nonpositive. With T=Tr(W^-1)=1/z, trace integrality gives v_p(T)>=-lambda_p. Since1+R is a unit,

    v_p(B)=alpha-2*v_p(T)-2*v_p(1+R)
          <= alpha+2*lambda_p.

This valuation is odd. The unchanged pole obstruction forbids it from being negative, so it is positive and lambda_p>-alpha/2. At a place attaining lambda_p every factor has valuation at least lambda_p. For nonzero D_j this gives

    v(D_j)>(m_j-3/4)*alpha>=m_j-3/4,

and hence v(D_j)>=m_j. A zero D_j already satisfies that conclusion. These are the same physical test orders used by the source. There is no adjusted D/delta factor in the new detector.

The argument permits a sign epsilon_j=+1 or-1 on the nonconstant term. Such a sign changes none of the valuations. This is needed only for the classified squared-H exception in390, not for arbitrary nonsquare leaves.

On the U=0 exception, the low-order conjugate-V leaf is the square of the fixed unit1/conjugate(c). On the Q_H=0 exception, the two affected leaves are minus the squares of the fixed units identified in the accepted390 proof. At any prime in any M_r the new local implication forces positive valuation of the relevant fixed unit, a contradiction. Thus all M_r would equal1. The unchanged pre-H anchor and root-height argument excludes both exceptions. The H reconstruction is then valid. Later H/V0 fixed-point exclusions use the same renewed local implication and unchanged root/anchor contradiction.

For genuine points, the local comparison, logarithm and polynomial steps are unchanged. They turn these same test orders into the same divisibilities by powers of each M_r. The same three-scale height theorem, Lucas contradiction, scalar depth24 bound and parity-sensitive input bridge therefore show that the input is an integer. This proof applies to the new product and new B together. It does not combine an old trace with a new pole parameter.

## Completeness and its ordering

Use the inherited construction with the same order of choices. First fix the integer input, scalar data, initial H point, four odd roots and scales. Then fix finite neighborhoods and the progression for H. Choose D0 and the simultaneous contact primes using the same forms u-(theta/A)*v, with v=D0^2*w^2 and lambda=u/v. The existing construction excludes all numerator and denominator primes of the fixed scales and contact differences from the selected large primes. Finally choose H in the combined progression attaining the uniform real bounds.

For comparison with the source rational function write

    Rold=F5(t)/(A^5*(t-1)^6),
    R=A^5*(t-1)^6*Rold.

The multiplier is a rational square because A is a positive rational square. At every selected contact prime it is a unit. Hence R has valuation one at the contact primes of this detector and even valuation elsewhere. The same formal-group construction gives v(D_j)>=m_j at the successful place. Each inverse factor there has residue1. At the other place each inverse factor has residue0 or1. Therefore T has residue1 or2 and is a unit at each selected contact prime. Also1+R is a unit there, so B has positive odd valuation one.

At all other primes, v(R) is even, and both denominators T^2 and(1+R)^2 change valuation by an even integer. Thus B has square reduced denominator. Additional primes dividing1+R cause only even valuations; no new finite preparation of H at those primes is required.

At p=2,3,17, put nu=v_p(v), eta=v_p(A). The common form u is a selected large prime and is a unit here. For sufficiently large prescribed nu, t has negative valuation eta-nu and the leading term of F5 dominates. Thus

    v_p(R)=5*(eta-nu), v_p(E)=5*(nu-eta).

The fixed neighborhoods give v(D_j)>=-c_p. Every nonconstant product term has valuation at least

    5*(2*m_j-1)*(nu-eta)-2*c_p,

which tends to infinity for all retained orders. Therefore T can be made arbitrarily close to2. The square multiplier relating R to Rold preserves the source local squareclasses at2,3,17; hence R, and then B, are squares there. Since v_p(1+R)=v_p(R),

    v_p(B)=-v_p(R)-2*v_p(T)
          =5*(nu-eta)-2*v_p(T),

which exceeds the same preparation-zero thresholds. All eta and c_p are fixed before the freely prescribed divisibility of w. This preserves the source's ordering of choices and the previously arranged scalar conditions.

At the real places, R~(A*lambda)^5 tends to positive infinity. Uniformly bounded test values give W=1+O(lambda^-5), T=2+O(lambda^-5), and

    B~1/(4*(A*lambda)^5).

The same large positive lambda therefore makes0<B<17 simultaneously for all three detectors. Real positivity also makes each factor positive at both embeddings, so all real-component guards hold. The preparation-zero completeness lemma now fills the new B inputs. Its accepted normalized/factored conversions supply the actual witnesses used by the candidate. No old pole witness is asserted to be preserved.

The unchanged point and scalar rows use the same final H chosen in the same retained finite neighborhoods. Thus every integer input has a complete witness for the new system.

## Evidence and limits

The checker verifies all eighteen deletions and every affected consumer, not only rows whose names mention the removed coordinates. In particular it replaces q1 in each actual hybrid evaluation. It independently expands F5(A*lambda) from all three physical contact circuits and checks the Laurent exponents1,19,79. The full quartic table is checked coefficient by coefficient. The leading coefficient remains16*C^2 on v57^2*v549^2, with C-linear multipliers at most96 and constant coefficients of fewer than2048 bits.

The source arithmetic passages read for this application are the pinned `quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`: preparation zero at lines10564 onward, one-place and radical/height transitions at11038 onward, and the simultaneous-prime/real completeness construction at11217 onward. The accepted390 review supplies the exact current signed exceptions and downstream interfaces.

This is a changed arithmetic construction, not a rational bijection of old detector fibers. Its soundness only needs the local implication at the required positive contact valuations. Independent review must verify that restriction, the new B identity, the two classified signed branches, and every finite and real completeness condition. A passing finite checker alone does not approve those arguments.
