# Conditional height detectors, candidate387

This is a proposed reduction of accepted390 to387 rational variables. It is pending independent mathematical review. The three removed coordinates are inverse witnesses for the real components of the three detector products. Their only three residuals are deleted. Every other coordinate and residual object is unchanged.

The result has387 variables,386 witnesses,357 quadratic residuals and6983 quartic monomials. It has degree four, integer content one and maximum coefficient16*3^(2^26). It does not reach the below300 publication threshold. Version13 is unchanged.

Author: `/root/astra_quartic_opt10_combination`. Agent03 contributed the essential zero-weight branch analysis and the conditional application discussion recorded in `03-depth/detector-domain/NOTES.md`. Agent03 is therefore not an independent reviewer of this proposal.

## Exact sources and artifacts

Paths below are relative to `work/quartic-under300-20261107`.

| Artifact | SHA256 |
| --- | --- |
| `01-elimination/squared-h/candidate390-ir.json` | `c986ee02f33aef0cf729bfbd73e590ac9672941be6c8f92dc3f389247daeaced` |
| Source author `01-elimination/squared-h/REPORT.md` | `18682f8f61cbf7642e074a7e47641fb91aa1023b8c81c29edf233ca232d4f02a` |
| Source acceptance `03-depth/review390/REVIEW.md` | `61b755da24b3934ca8725159ac96c59c8b5090a4c7a032fe5487646853e7a667` |
| Co-contributor `03-depth/detector-domain/NOTES.md` | `6dedf2fd0d59232c864d3bad772203251896d4414518ec7f261acc60892e6ea6` |
| `10-combination/candidate387-ir.json` | `a5fe7019a44e730cef0df91e8a0def2823433217e3a5452f701ee1f104abf85a` |
| `10-combination/polynomial387.json` | `dc9883905b72ed5210a2a466ae58f3cc8c9913837b2af07cada808312913bced` |
| Producer-free `10-combination/verify387.py` | `e1788fe72449a876fc2f741e25855ac2c292a30ef7e688f18959728d7edb11cb` |

The inherited manuscript source is `quartic_v12.tex`, SHA256 `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. I read its one-place lemma and proof at lines11038 onward, the odd-contact definition and height transition at lines11102 onward, and the soundness and completeness construction immediately following. The current three-scale height application and order10/logarithm changes remain those in the accepted390 ancestry. No external theorem is strengthened by attribution. The conditional local result below is the new argument.

## Physical interfaces and the zero-weight branch

Write

    F5(t)=t(t+1/2)(t+1)(t-1/2399)(t+32/407), delta=t-1.

The actual three positive square scales are

    A0=1, A1=4*v343, A2=1+32*v344+256*v345.

Here v343=v341^2, and the real component of the retained product of four totally positive odd-root abscissae is2*v341, so A1 is nonzero. Also v344=v342^2 and v345=v344^2, giving A2=(1+16*v344)^2>0. These facts need neither H nor a logarithm interpretation. The three physical parameters are t0=v37, t1=4*v391 and t2=v37+32*v439; they equal A_r*v37.

The checker substitutes the literal retained gate definitions, including every affine recentering, and proves that rows302,352,402 are respectively nonzero constant multiples of

    F5(t)*E = A^5*(t-1)^5.

The constants are1952786,1952786/16,1952786. The q rows304,354,404 are exactly

    delta^3*q=E.

Thus t is never one of the five contacts: F5(t)=0 would force delta=0, whereas none of the contacts equals1. If t differs from1, both E and q are nonzero. If t=1, E=0 is possible, and the old toric circuit is not claimed to retain its intended values on this branch.

The odd-contact radical M_r at t=1 is1. Indeed F5(1)=287106/88763, with prime support {2,3,37,109,439,2399}; the contacts and their denominator constants also have no prime above76176 here. This is the source's actual radical convention, not a new definition. The height theorem still applies because t avoids every contact. Such a detector has no local obligations and needs no trace interpretation.

For t different from1, the unchanged toric equations decode exactly as in the accepted order10 circuit. Its nonzero divisions need E and q only, now established from the weight and q rows. All subsequent toric coordinates are then determined and give the same product of sixteen weighted factors as before. This is a conditional reuse of the accepted exact product identities. It does not assume the deleted real-component inverse.

## A local obligation supplies its own trace domain

Fix one detector and a prime p>76176 in its odd-contact radical. The preceding case split gives t!=1 and valid weight/product meanings. As in the retained contact transition,

    R=F5(t)/(A^5*delta^6)=1/(E*delta)

has odd valuation alpha at p. The square scale A and fixed contact differences are exactly the source hypotheses for this implication.

The physical order-m weight is q_m=E^(2m-1)/delta^3 for m=1,10,40. It is not literally R^(1-2m). With the unweighted field test D_j, define Dtilde_j=D_j/delta^(m_j+1). Then exactly q_m*D_j^2=R*(Dtilde_j/R^m_j)^2. At a consumed prime delta is a unit, so D_j and Dtilde_j have the same valuation. In the local argument below D_j denotes this adjusted value; its conclusion therefore gives the required order for the physical unweighted test as well. This distinction also applies to the fixed signed unit leaves in the exceptional branches.

First suppose its factors have the usual form

    1+R*(D_j/R^m_j)^2.

The argument also works with a sign epsilon_j=+1 or-1 on each nonconstant summand. For D_j nonzero that summand has valuation alpha+2(v(D_j)-m_j*alpha), which is an odd integer at either unramified place above p. It cannot have valuation zero, so the factor cannot vanish. A zero D_j gives factor1. Thus the actual field product W is nonzero, with no global positivity assumption.

Write W=w0+w1*rho and let z be the retained norm quotient. The unchanged rows335,385,435 say

    w0^2-2*w1^2=2*w0*z.

If w0=0, rationality gives w1=0, contradicting W!=0. Therefore w0!=0, z=Norm(W)/(2*w0)!=0, and T=Tr(W^-1)=1/z is defined and nonzero. The actual B rows, after their retained eDelta gates, say

    z^2=E*delta*B.

Consequently B=R*z^2=R/T^2 is nonzero. The unchanged normalized and factored pole rows recover the old obstruction on this nonzero input. Their soundness conversion does not require B>0; positivity was used in the old completeness direction only. The deleted inverse coordinate has no consumer in this conversion.

All hypotheses of the one-place proof have now been obtained at a prime where they are needed. The existing valuation calculation applies, including the signed version used in390: alpha>0 and some place above p has v(D_j)>=m_j for every test. Nothing is asserted about a trace at a detector whose product vanishes and whose radical is1.

## Squared-H exceptional branches and the order of the proof

Candidate390 introduced two exceptional branches before reconstructing H. Their exclusion remains valid with the conditional result just proved.

If U=0, the unchanged squared-H equations give W_H=v=0, Q_H=1/c, V=1/c^2. All detector factors have ordinary square meanings before H is reconstructed. At any prime in any detector radical, the preceding local argument forces positive valuation of the low-order unit1/conjugate(c), a contradiction. A detector with t=1 already has radical1 and needs no product meaning.

If Q_H=0, the unchanged equations give U=V=-v^2 and v=1/(c+b) or -1/(c-b). Both are units at every consumed place, as verified in the accepted390 proof. The two affected factors are signed squares. The conditional signed local result forces positive valuation of these fixed units at any prime in any detector radical, again impossible. The other factors retain their square meanings without H, exactly as checked in390.

Thus every radical is1 on either exceptional branch. The same pre-H product-height bound and scalar-anchor restoration give incompatible upper and lower bounds for the four root indices. These steps do not use a scalar pole, a trace at a radical-free detector, or a logarithm interpretation. This excludes the branches before reconstructing the original H values.

Afterwards, reconstruct the accepted392t H/Kummer objects using the accepted390 formulas. Remaining fixed-point exclusions in the inherited H/V0 domain argument use the same pattern: at every prime in a radical, a fixed unit leaf would have positive valuation; hence all radicals would be1 and the unchanged anchor-height contradiction applies. The conditional lemma supplies exactly those local premises. Primary identity branches and the logarithm comparisons are unchanged.

The rest of soundness is rerun through its actual local interface. For every prime dividing M_r, all comparison tests have their original orders at one place. Therefore the same powers of M_r divide the Lucas residual and, later, the input-error numerator. A radical equal to1 imposes a vacuous divisibility condition. The three-scale height estimates, the Lucas contradiction, the depth24 scalar-height bound and the parity-sensitive input bridge are unchanged. They imply that the input is an integer.

This is not a claim that every new witness lifts to390. A detector with radical1 can have a zero product and no inverse of w0. The conclusion is equality of input projections, proved by the conditional local argument and the inherited global soundness proof.

## Completeness and finite checks

Given an old complete witness, forget coordinates382,430,478 and rows334,384,434. All other objects stay fixed. This proves completeness with the same real neighborhoods, prime choices, CRT progressions and pole witnesses. No new global choice restriction is introduced.

`verify387.py` imports no producer. It checks full private incidence, all unchanged objects, the literal trace and B rows, all three contact-weight equations and q equations, the t=1 prime support, and every coefficient of the primitive SOS. All387 coordinates occur. The unique C^2 term is16*C^2*v57^2*v549^2; C-linear coefficients are at most96 and C-independent coefficients have fewer than2048 bits. No huge fixed coefficient is expanded.

`census.py` and `CENSUS390.json` record all390 coordinate consumers. The three detector field evaluations use60 coordinates, their weight/pole/trace blocks use95, and shared detector coefficients use22. These177 coordinates remain the largest structural target. This proposal removes only three private guards; it makes no claim that the other detector coordinates can be deleted.

Independent review must accept the zero-weight and radical-free branches, conditional pole conversion, signed390 branch order, and the renewed whole soundness interface. A finite checker pass alone does not accept those applications.
