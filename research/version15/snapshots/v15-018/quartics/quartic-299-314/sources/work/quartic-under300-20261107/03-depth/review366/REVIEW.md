# Independent acceptance of the S-chart reduction to 366 variables

I accept this exact 369-to-366 reduction on the stated inherited arithmetic inputs. The candidate and accepted369 have the same rational input projection. The new candidate has 366 total variables, 365 witnesses, 336 quadratic residuals and 6,527 quartic monomials. Its degree is four, its integer content is one and its largest coefficient is `16*3^(2^26)`.

Reviewer: `/root/astra_quartic_opt03_depth`. Author of the changed component: `/root/astra_quartic_opt01_elimination`. I did not contribute to the new parity proof or sign-normalization construction before this review. I authored some earlier components in the inherited chain, so this is an independent review of the present reduction, not a fresh wholly non-author review of every preceding component or external theorem. No publication approval or below-300 result is asserted.

## Exact scope

Paths are relative to `work/quartic-under300-20261107` unless stated otherwise.

| Artifact | SHA-256 |
|---|---|
| `10-combination/candidate369-ir.json` | `b359a64365d05c86ad009b2b93664bd491bc1830e0077383030a0b48556e7095` |
| `01-elimination/review369/REVIEW.md` | `908c25a0676875eef83cbe6fc5a94c152b5fcf94056fcdcf9537adfe73b66d89` |
| `01-elimination/s-odd366/REPORT.md` | `e2a482e2f08712c6375bfaca4fea78bea35034727946c582ce7b3dde02608c7b` |
| `01-elimination/s-odd366/candidate366-ir.json` | `0c25b69cfc6d1aa96fd7b99d9b3534c2f29e9b6976ed613c3567fb83fa16ae56` |
| `01-elimination/s-odd366/polynomial366.json` | `f9219fb79cc687a5af567e6e8cc7b7591ccb1ea4d8f803b7d7189122412e5e64` |
| `03-depth/review366/check.py` | `a0354d78f0dead0f670ec463c7788caae05727ea99955ab2088f29e12ab8e761` |
| `03-depth/review366/CHECKS.json` | `e19970be1c0c9ea992c7d2f6d801ed88875ecdd3a665838a82e096aa5bc0ca9b` |

I read the proposal, its checker, the actual source and candidate rows, the accepted369 composition proof, and the relevant inherited arguments. The manuscript `work/quartic-version6-release/repository/manuscripts/quartic_v12.tex` has SHA-256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. Its lines 19539–19581 supply the squareclass homomorphism, group decomposition and half-point construction. Its reciprocal subtraction argument around 20385–20445 includes the equal-abscissa cases. The earlier norm-chart review `work/quartic-under400-20261107/03-depth/review-odd-norm.md`, SHA-256 `f554c3930f8849355d64fc774a935eca169c4fd1d1e0ba35282d8664efe0eaf8`, supplies the exact meaning of the deleted norm equations. These historical arguments supply inputs; they do not by themselves imply that the S-chart is redundant.

## Initial index and scalar point

The actual retained rows give `x=h^2`, `j^2=x^2-D` with `x=v84+2*v85*rho`, not the unscaled coordinate pair. Here `D=(3-rho)^2` is positive at both real embeddings. If h were zero, j squared would equal -D, which is impossible. Thus S=(x,hj) is a finite point with nonzero square abscissa.

The inherited decomposition is over all of E(K): `E(K)=Z*R0+E[2]`, `2R0=P`. It does not require an odd index. The classes of epsilon=1+rho, -1 and d=3-rho are independent: the norm of `epsilon^m*(-1)^e*d^f` modulo rational squares is `(-1)^m*7^f`; after m and f are even, real signs exclude e odd. Hence alpha(S)=1 forces S=[a]P for an integer a and no torsion translate. Finiteness forces a nonzero. This deduction uses none of the deleted equations.

The actual scalar rows are eight times the two components of `(c*x+D)g=aP*j-bP*h`. Since c and x are positive at both real embeddings, `c*x+D` is nonzero. The retained row `g0*tau=1` implies g is nonzero. The inherited reciprocal identity therefore identifies `g^2=f(S-P)` when x differs from c. When x=c, the retained chart gives the two point possibilities S=P and S=-P. The first forces g=0 and is excluded. The second is exactly the duplication value for -2P. The source proof treats this case before its later anchor exclusion; that later exclusion is not used here. Thus the scalar point is the nonzero integral multiple `[a-1]P` before knowing a is odd.

## The new parity argument

At 3 the field K is unramified and inert, with integral basis 1,rho. The curve has good reduction. I independently doubled the literal point R0=(1+rho,2rho), recovered the actual fixed P and checked its reductions `x(P)=rho`, `y(P)=0`, `f(P)=2rho`. It is a nonidentity point of order two in the reduced group.

If a is even, s=a-1 is odd, including negative s. Reduction of [s]P is then P. Its reciprocal abscissa is integral and reduces to 2rho, so its rational rho coefficient `F=2*g0*g1` is a 3-adic unit. No even-index coefficient formula has been invoked.

Multiplying the actual rescaled anchor by g0 squared, using `g0*tau=1`, gives

    u^2+6v^2-2w^2-4Cw-3F^2=0,
    u=g0*U, v=g0*V, w=g0*W.

This identity uses neither F nonzero nor a deleted F inverse. Equivalently,

    u^2-2(w+C)^2+6v^2=3F^2-2C^2.

For rational inputs, every nonzero value of `u^2-2(w+C)^2` has even 3-adic valuation, by anisotropy of that binary form over F3 after extracting the common power of 3. Every nonzero `6v^2` has odd valuation. They cannot cancel at their lowest valuation. The right side has valuation one since F is a unit and C is divisible by 3. Therefore the odd summand must have valuation one, v must be a unit, and the binary summand must have valuation at least two or be zero. After division by 3 the left side has residue two, whereas the right side has residue one. This is impossible. The cases where either summand is zero give the same contradiction or cannot have valuation one.

Thus a is odd. This argument precedes every H reconstruction, height estimate, detector interpretation and scalar depth bound. It supplies exactly the parity missing after removal of the three private equations, without assuming their former conclusion.

## Global sign map and half-point restoration

The proposal correctly avoids claiming that oddness alone restores the deleted witnesses with arbitrary fixed signs of h,j. My independent checker applies the stated sign map to every monomial in every remaining residual. Each residual is fixed or negated. The complete affected-row list, including the L2, scalar ratio, scalar reciprocal, anchor and V2 biquadratic consumers, is in CHECKS.json. The flipped coordinates are precisely

    5,6,7,8,25,26,27,28,55,56,57,120,121,543,544,549.

The input and all other coordinates are fixed. In particular the anchor term `C*tau*W` is preserved because both factors change sign. The retained inverse equation is also preserved. This is a symmetry of the entire candidate, including the exceptional point branches allowed in its domains, rather than just of the S chart.

For odd a choose the actual point T=[a]R0=(A,B). It is nontorsion, so A and B are nonzero. Its squareclass is epsilon, hence `A=epsilon*r^2` for an existential r in K. The inherited duplication formulas give

    h_star=(A^2+D)/(2B),
    j_star=(B/A)^2/2-x,
    h_star^2=x, h_star*j_star=y(S).

I independently checked the denominator-cleared duplication identities modulo `B^2=A^3-D*A`. Since h is nonzero, these equations imply `(h_star,j_star)` is either `(h,j)` or `(-h,-j)`. Apply the full sign symmetry in the latter case. It changes no input and leaves every remaining equation satisfied.

Now reinsert the two rational components of A into coordinates 70,71 and Norm(r) into coordinate 72. The exact deleted equations are the components of `A^2-2(x+j_star)A-D=0` and `Norm(A)+Norm(r)^2=0`. The first follows from the displayed duplication formulas; the second uses Norm(epsilon)=-1. No rational-function choice of r is claimed or required. This constructs a complete accepted369 solution with the same input.

Conversely, forgetting coordinates 70,71,72 from any accepted369 solution gives a candidate366 solution, because exactly their three private rows were deleted. These maps establish equality of input projections. They do not establish a bijection fixing every retained witness, and the review does not assert one.

## Finite evidence and conclusion

The independent checker imports no producer or other checker. It verifies all deleted-coordinate incidence, equality of every retained coordinate and residual object, the scaled S chart, the literal scalar and anchor equations, the deleted norm chart, the full sign symmetry, fixed-point reductions, duplication identities, coordinate use, and all 6,527 coefficients of the primitive SOS. It also verifies the unique C-squared coefficient and bounds all other symbolic coefficient parts without expanding C.

These finite checks do not prove the inherited Mordell-Weil theorem or replace the valuation argument. Together with the source-level argument above, they support acceptance of this exact component. I found no unresolved mathematical or implementation gap in the stated reduction. The earlier accepted369 soundness and completeness are consumed only after an actual source369 witness has been restored. Consequently its domain, real, local and CRT arguments require no new application or changed hypothesis here.
