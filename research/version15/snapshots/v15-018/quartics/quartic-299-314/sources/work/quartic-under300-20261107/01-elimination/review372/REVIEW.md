# Independent acceptance of contact-polynomial candidate372

Accepted for the exact standalone research candidate below, on the inherited arithmetic inputs. It has the same rational input projection as accepted390. Its 372 total variables comprise the input and 371 witnesses. There are 342 quadratic residuals and 6,574 quartic monomials, with degree four, integer content one and maximum coefficient 16*3^(2^26).

Reviewer: `/root/astra_quartic_opt01_elimination`. Agent10 authored the new detector and bounded pole input. I did not author this change. I authored the earlier squared-H component, whose separate independent acceptance is part of the baseline. This review covers the new detector's finite realization, soundness and ordered completeness. It approves neither a later guard-deletion composition nor a manuscript or ordinary-coefficient artifact. Version13 is unchanged. The six-variable saving of the earlier384 proposal is included in these eighteen deletions, not additive to them.

## Frozen bindings

Paths are relative to `work/quartic-under300-20261107`.

| Artifact | SHA-256 |
|---|---|
| Source `01-elimination/squared-h/candidate390-ir.json` | `c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced` |
| Source independent acceptance `03-depth/review390/REVIEW.md` | `61b755da24b3934ca8725159ac96c59c8b5090a4c7a032fe5487646853e7a667` |
| Proposal `10-combination/unweighted372/REPORT.md` | `f81c3e6b170881c54019cb876173de1fda651a17474376257152797426669daa` |
| Candidate `10-combination/unweighted372/candidate372-ir.json` | `ff487de4c99d74214eef654dafb1bb2a0a5faca0df3fde5cb636de92297222ce` |
| Polynomial `10-combination/unweighted372/polynomial372.json` | `5bcf7797a65f954719fcd21515a3b6bf022e28876f58aa5ca42a23643377336f` |
| Author checker `10-combination/unweighted372/verify.py` | `0a1273da5d6b9c778e96cb4fc441fd8688d715c6292dfd685be6addcba32493d` |
| Independent local `check.py` | `f819efbf6b0b13e6f72807bfbad50355edae51de276ec7202a9047675dbf285a` |

The underlying manuscript is `quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. I read the actual preparation-zero obstruction/completeness lemma, the one-place proof, the definition and use of the odd-contact radical, the three-scale root-height argument, and the ordered simultaneous-prime and real-progression construction. Relevant passages begin around lines 10562, 11038, 11102, 11217 and 19497. The current source's depth24, order10, enlarged-H and anchor replacements remain the relevant later interfaces.

## Independent finite reconstruction

The checker imports no producer or other checker. It derives the affine R expression from each new E row, expands the retained contact gates and verifies R=F5(A*lambda) with the exact five contacts and physical scale. It then reconstructs every surviving row from the old source under q1=E, a=1, b=R, except for the explicitly replaced E and B definitions. This includes every hybrid evaluation that consumes q1. It compares all non-polynomial metadata, every surviving coordinate object, the complete set of deleted rows and the incidence of each of the eighteen deleted coordinates.

The eighteen deleted coordinates are 352,353,354,384,395,396,397,400,401,402,432,443,444,445,448,449,450,480. No remaining polynomial refers to them. The local evidence records all old consumers and all 33 changed rows; the audit is not restricted to names containing the deleted variables.

The retained toric equations are checked as exact Laurent identities. From ER=1 they give c=R³, d=E^8, q10=E^19 and q40=E^79. The E²,E³,q10² and higher square/cube gates agree with those values. Hence each actual product has factors 1+E^(2m-1)*D² for m=1,10,40 and the original unweighted physical D. No delta-adjusted test is used in this new construction.

Every primitive residual square was expanded independently and every coefficient matched the frozen quartic table. All 372 coordinates occur. No symbolic C powers collide on an ordinary coordinate monomial. The sole C² term is 16*C²*v57²*v549²; other C-linear multipliers are at most 96 and C-independent coefficients have fewer than 2048 bits. This proves the asserted maximum without expanding C.

I also replayed the frozen author verifier, redirecting its only output write to this review directory. Its result agrees. A before/after hash comparison confirms that all author-directory files were preserved. Reproduction: `python -B check.py` and `python -B replay.py` here.

## Exact new domains and pole meaning

For each detector write

    R=F5(t), E=1/R, t=A*lambda,
    W=product(1+E^(2m-1)*D²), T=Tr(W^-1).

The row ER=1 excludes all five contacts and licenses the toric divisions. Unlike the old construction, t=1 is not singular; it is simply a contact-radical-free value with nonzero R.

All three real-component inverse guards remain. Together with the unchanged norm equation w0²-2w1²=2w0*z they force W,z,T to be defined and nonzero, with z=1/T. The replacement B row is

    B*(R+E+2)=z².

Since R+E+2=(1+R)²/R, it excludes R=-1 and forces B nonzero. It gives exactly

    B=R/((1+R)²*T²).

These are the values used in both directions of the proof. The old normalized and factored pole rows remain unchanged and reconstruct the preparation-zero certificate on this B, including zero private conic factors. Their soundness conversion requires B nonzero, not B positive. No old B or old trace is retained implicitly.

## Soundness uses the required positive contact valuations

The source odd-contact radical is unchanged because t, the five contacts and the scales are unchanged. At a prime p>76176 counted in this radical, exactly one contact factor has odd positive valuation and the others are units. Thus alpha=v_p(R)>0 is odd and 1+R is a unit. This is the precise scope of the argument: no claim about the pole obstruction at every possible odd valuation of F5(t) is needed.

For a factor 1+epsilon*R*(D/R^m)², epsilon=1 or -1, the nonconstant term has odd valuation 2v(D)-(2m-1)alpha when D is nonzero. Hence its valuation is the minimum of that integer and zero. A zero D gives factor 1. All factor valuations are nonpositive. If lambda_p is the largest valuation of W over places above p, trace integrality gives v_p(T)>=-lambda_p. Because 1+R is a unit,

    v_p(B)=alpha-2v_p(T)<=alpha+2lambda_p.

This is an odd valuation, so the unchanged pole obstruction makes it positive. Consequently lambda_p>-alpha/2. At a place attaining lambda_p each factor has valuation at least lambda_p, and therefore

    v(D)>(m-3/4)*alpha>=m-3/4.

Unramified integrality gives v(D)>=m. Thus the same physical tests have their same simultaneous local orders. The denominator (1+R)² has caused no loss at any prime the height argument consumes.

The signs in this proof are necessary before reconstructing H. On the accepted390 branch U=0, the low-order conjugate-V leaf is the square of the fixed unit 1/conjugate(c). On Q_H=0 the two affected leaves are negative squares of the two explicitly classified fixed units. The other leaves remain squares independently of H. The exact product identities continue to hold because their q variables were substituted throughout, as verified above. Applying the local conclusion on either branch would force a fixed unit to have positive valuation. Therefore all three radicals would be 1, contradicting the unchanged pre-H root-height estimate and independently restored scalar anchor. This excludes both branches without assuming a square root of arbitrary U or V.

After that exclusion the source H/Kummer objects are reconstructed. The later finite H/V0 exclusions use the same fixed-unit local argument and the same anchor-height contradiction. Their global rational-log denominator/nonvanishing proofs and half-index identities are unchanged. The comparison argument then supplies order40 divisibility for the Lucas residual and order10 divisibility for the input-error numerator at each radical. The three-scale height theorem needs those divisibilities and contact parameters, not the old rational weight formula. The scalar depth24 subsystem is literally unchanged. Hence the current Lucas and input contradictions, with beta=51*(2X+1)²+2504 and its odd-label bridge, still force X to be an integer.

## Ordered completeness with the new B

The source construction first fixes the integer input, current scalar data, initial shared point, scalar point, odd roots and the three positive rational square scales. It then fixes finite neighborhoods preserving the scalar conditions and bounding all test valuations at 2,3,17. The real-progression theorem supplies bounds for the tests independent of later progression moduli. Only after these bounds and scales are fixed are D0, the prescribed divisibility of w, the real lower bound for lambda and the simultaneous contact primes chosen. The final shared point is chosen in the combined progression while attaining those real bounds.

For comparison with the source put

    Rold=F5(t)/(A^5*(t-1)^6),
    R=A^5*(t-1)^6*Rold.

On this construction t is large and positive. The multiplier is a nonzero rational square because A is a rational square. At a selected contact prime it is a unit: the prime avoids all fixed scale/contact-difference support and t is close to a contact different from 1. Thus R has valuation one at each selected contact prime of its detector, and even valuation at every other prime. The latter follows directly from the source's product of five selected primes over a square, not from any cancellation assumption about split places.

The final formal-group construction supplies the same D orders at the successful place. Inverse factors have residue 0 or 1 at either place and all have residue 1 at the successful place. Therefore T has residue 1 or 2 and is a unit at every selected contact prime. Also 1+R is a unit there. It follows that B has positive valuation one there. At other primes, v(R) is even and both denominator squares change the valuation by even integers. Thus the reduced denominator of B is a square. New primes dividing 1+R need no additional finite preparation: they contribute only even valuation.

At p=2,3,17 write nu=v_p(D0²*w²), eta=v_p(A). The common form u is a selected large prime, so it is a p-unit. For sufficiently large prescribed nu, all five factors of F5(t) have valuation eta-nu and

    v_p(R)=5(eta-nu)<0.

If v(D)>=-c_p on the fixed neighborhoods, each nonconstant factor term has valuation at least

    5(2m-1)(nu-eta)-2c_p,

which tends to infinity for every retained order and place. The new T is therefore as close to 2 as needed, including at the ramified prime 2. In particular v_p(T)=v_p(2). Since v_p(1+R)=v_p(R),

    v_p(B)=5(nu-eta)-2v_p(2).

These valuations exceed the original preparation-zero thresholds after prescribing enough divisibility of w. R has the same local squareclass as Rold, whose class is square at these primes by the selected Gaussian-prime conditions. Dividing by (1+R)²*T² preserves that class. Eta and c_p were fixed before this choice of nu, so there is no circular change of the roots, neighborhoods or scalar preparation.

At the real embeddings, R~(A*lambda)^5 tends to positive infinity. Bounded D gives W=1+O(lambda^-5), T=2+O(lambda^-5) and

    B~1/(4*(A*lambda)^5).

Thus all three B values lie in (0,17) for a sufficiently large allowed lambda. Every factor is then positive at both embeddings, so the retained real-component guards can also be filled. The new pole inputs have the required real interval, local squareclasses, local valuation bounds and square reduced denominators. The preparation-zero completeness lemma supplies their witnesses, and the accepted normalization/factoring maps give the exact candidate coordinates. These are new pole witnesses; there is no claimed transport of arbitrary old detector fibers.

All unchanged point, logarithm, scalar and anchor rows use the same final shared point in the same finite neighborhoods. This completes a candidate372 witness for every integer input without changing the simultaneous-prime theorem or its allowed ordering.

## Decision

Both directions establish equality of rational input projections. The changed rational parameter is used consistently in the products, trace, bounded B input, local proof and completeness estimates. The eighteen-coordinate reduction and its exact finite realization are accepted for the frozen372 candidate only. The below-300 release threshold remains unmet.
