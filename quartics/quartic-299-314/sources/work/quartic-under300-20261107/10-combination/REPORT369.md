# Guard removal on the new contact-polynomial detectors

Candidate369 composes the guard-removal idea with the independently accepted372 detector construction. It has369 rational variables,368 witnesses,339 quadratic residuals and6568 quartic monomials. Its degree is four, content one and maximum coefficient16*3^(2^26). Independent composition review is pending. It is not approved merely by the two component acceptances.

The source `unweighted372/candidate372-ir.json` has SHA256 `ff487de4c99d74214eef654dafb1bb2a0a5faca0df3fde5cb636de92297222ce`. Its independent review is `../01-elimination/review372/REVIEW.md`, SHA256 `3e5a5fe8a14025979b27bbb45c55f35d55c0237082f4fd7a299babc9b3e9d997`. The earlier guard component review `../01-elimination/review387/REVIEW.md` has SHA256 `bb99170b47becab99d5b4b46096d161cd512d7b805add19989a321995385368a`.

The new `candidate369-ir.json` has SHA256 `b359a64365d05c86ad009b2b93664bd491bc1830e0077383030a0b48556e7095`; `polynomial369.json` has SHA256 `906179089ce38d574ae8ff64398078db63d4a035d3e3b15d537a963972c20267`. Only coordinates382,430,478 and their inverse rows334,384,434 are deleted. All other coordinate objects, residual objects and metadata except the status line are identical to372. `verify369.py` checks that exact delta, its complete incidence, all three physical E/norm/B interfaces, and every coefficient of the full SOS without importing a producer.

## The new interface, rather than the old normalization

For each detector, the accepted source372 proves the literal identities

    R=F5(A*lambda), E*R=1,
    W=product_j(1+R^(1-2*m_j)*D_j^2),
    Norm(W)=2*w0*z,
    B*(R+E+2)=z^2.

The orders are1,10,40 and every D_j is the same unweighted field test. Unlike the earlier387 source, there is no E=0 or delta-denominator case. The equation E*R=1 makes E and R nonzero globally, so the entire univariate toric chain decodes before considering the trace domain. It also excludes all five contact values of t=A*lambda.

Fix a prime in this detector's required odd-contact radical. The accepted contact argument gives an odd positive alpha=v_p(R). Each nonconstant factor term, including a permitted sign minus in a classified squared-H exception, has an odd valuation. Hence no factor is zero, and W!=0. The retained norm equation implies w0!=0: otherwise rationality would force both components of W to vanish. Consequently z=Norm(W)/(2*w0)!=0 and T=Tr(W^-1)=1/z is well-defined.

At this prime1+R is a unit. In particular R+1 is globally nonzero for a detector with such a prime. The retained B equation now gives

    B=R/(T^2*(1+R)^2)!=0.

The unchanged normalized/factored pole rows therefore supply the same nonnegative-odd-valuation obstruction on this B. No positivity assumption is needed for this soundness conversion. The accepted372 local proof applies verbatim because its only uses of the inverse guard were to establish the trace and nonzero B domains just recovered. All unweighted field tests have their required orders at one place above the prime.

If a detector has no prime in its radical, its local obligations are empty. Its possibly zero product needs no trace interpretation in the height argument. The additional algebraic possibility R=-1 also belongs only to this case: every valuation of the rational number-1 is zero, whereas a prime in the radical would force an odd positive valuation. There is no need to assert a global inverse of w0 or a global inverse of1+R on such a detector.

## The order of the whole proof

First repeat the accepted390 exceptional-branch classification. On U=0 the low-order leaf is the square of a fixed unit. On Q_H=0 the two relevant leaves are signed squares of fixed units. At any prime in any detector radical, the conditional local argument above forces positive valuation of a unit, a contradiction. Thus all radicals would be1, and the same pre-H root-height and independently restored scalar-anchor bounds contradict one another. This step uses no trace at a radical-free detector and no assumed H or logarithm interpretation.

Reconstruct H after excluding those branches. The subsequent H/V0 fixed-point exclusions use the same fixed-unit and radical-height contradiction. Then the unchanged primary charts, rational logarithms and direct tests have the meanings used in372. At every prime in every radical, the conditional local lemma gives exactly the hypotheses of the local comparison theorem. It follows that the same powers of the radicals divide the Lucas residual and the input-error numerator. A radical equal to1 contributes a vacuous divisibility statement. The same three-scale height bounds, scalar depth24 estimate, anchor and parity-sensitive input bridge then imply that the input is an integer.

This is a fresh soundness argument through the actual new R/B interface. It is not a claimed lift of every369 witness to372. The extra zero-product witnesses at radical-free detectors may have no inverse of w0.

For completeness, take the372 witnesses supplied by its independently reviewed construction and forget the three inverse coordinates. All other values remain fixed, so the same ordered finite, real and CRT choices work. This establishes the opposite inclusion of input projections without any new arithmetic premise.

The combination retains all accepted372 coefficient bounds. The unique C^2 term is16*C^2*v57^2*v549^2, other C-linear coefficients are at most96 and C-independent coefficients have fewer than2048 bits. The publication threshold remains strictly below300; Version13 is untouched.
