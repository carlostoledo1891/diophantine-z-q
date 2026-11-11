# Independent review of anchor-gamma313

I accept the frozen 313-variable construction and its new completeness argument, relative to the explicitly inherited arithmetic inputs of accepted sparse-shared314. This is a fresh review of the coupling between the anchor and gamma. It is not inferred from the 314-variable acceptance. I found no required repair or strengthened premise.

Reviewer: `/root/astra_quartic_opt10_combination`, November 7, 2026. Agent05 authored the coupling and compiler; agent03 contributed the constructive approximation proof. I authored neither adaptation. I previously authored the exact sparse transport and reviewed the shared314 compiler; those inherited approvals retain their separate scopes. No author file was changed.

## Frozen scope and independent checks

All source paths below are relative to `work`.

| Object | SHA256 |
|---|---|
| `quartic-under300-20261107/10-combination/sparse-shared314/candidate314-ir.json` | `aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382` |
| `quartic-optimization-20261107/resume-anchor-shared314-20261107/anchor-gamma313/candidate313-ir.json` | `6f21646b18c1098d378ebf0d1607ec44ca57e1dc1215b474aff13e8f9220982a` |
| Same directory, `polynomial313.json` | `d3eaca34d9b5bb3f24593ca601f30f22c430f4b71e47e9f607a050501fc8d63d` |
| Same directory, `REPORT.md` | `c8c5e7cc7e91a08fe9ec074bdaa450e83c55060bdb4b3cd2bdffbc676a1ad361` |
| Same directory, `MANIFEST.json` | `4793c28883c1a679f97e605042bafbe7ad3c5d3a7920d82c69e4e7c3461dbf8b` |
| `quartic-optimization-20261107/resume-depth-20261107/anchor313/PROOF.md` | `ba0b08bf1d155d22d152e1dd2ec23f1b264951663cb53e90f1ed3da214b271a1` |
| My `check.py` | `f5caaf2b03c2e1b0fde16cbe0673c16a3456d82d8ed63b3fa769b523c880f28f` |
| My `check_approximation.py` | `7308fa52550d8ed689ffd586379d4ea8e9d70b330a8cde797bb21b05ad5d6856` |
| My `FINITE-CHECKS.json` | `8b6ee3075aee336341caae5ad821318bcb56b7371b87cfed24a2305a2eee7b4b` |
| My `APPROXIMATION-CHECKS.json` | `9d8c6190d3ab06525653a5ab9e162811809cf50ec15644225ae295e06204081f` |

Both checkers are independent implementations and import no author program. I checked all file lengths and hashes in the author manifest, including its source pins, before and after the finite check. The approximation checker verifies the local algebra, all odd dyadic residue cases and the universal rational-map identity. The unbounded density, approximation and choice-order arguments are reviewed below rather than inferred from samples.

## Literal map and polynomial

Exactly coordinate1100 is removed. Exactly rows919,930,941,2000,2005 change. The other278 residual objects are identical, including metadata. Only the names of surviving coordinates1101 through1105 change. All other coordinate objects and inherited top-level data, apart from status, are identical. There are no duplicate coordinate or row IDs.

With u=v55, rows2000 through2004 force v1101=u^2, v1102=u^4, v1103=u^8, v1104=u^16 and v1105=u^-16. In particular u is nonzero. Row2005 then gives v1106=u^-40; the final squares give v1107=u^-80 and v1108=u^-160. Every helper is uniquely determined.

Set the old gamma to 1/u, reconstruct its old powers and inverse sixteenth power, and keep every non-chain coordinate fixed. Each old group guard becomes the new v1105*E8 term. My checker substitutes both chains as Laurent monomials in the nonzero u and compares every old and new equation exactly. This proves soundness by a map to accepted sparse-shared314 before any point, valuation or index interpretation. It does not prove that arbitrary old choices lift; completeness requires the new argument.

The old u occurred only in row504. The new use is precisely row2000. The other private anchor coordinates56 and57 still occur only in row504. I checked all changed-chain consumers and all three root half-chart sign actions against every final residual. No new obstruction to the inherited root restoration is introduced.

The full independent primitive-residual expansion has313 variables,312 witnesses,283 quadratic residuals,6076 C-power entries and6073 specialized monomials. Every coordinate occurs. Degree is four, content is one, and the exact largest absolute coefficient is186624*C^2+64 on v89^4, with C=3^(2^25). All stored integer coefficients have at most1520 bits; the usual leading-power domination using C>2^1522 proves the specialization count and maximum. The new contribution to u^4 is included in this expansion.

## The quadric and data fixed before approximation

The actual unchanged rows504 and1903 give

    Q(u,v,z)=u^2+6v^2-2z^2=N,
    z=w+C, N=3T^2-2C^2, T=Fs+Cq,
    Fs=2g0g1, q=48v83^2+48v87^2+432v89^2.

N is nonzero: N=0 would make a rational square equal2/3, impossible already by its odd3-adic valuation. The form is nondegenerate, so every point of this nonzero level is smooth.

T is fixed before the final H. This is a physical dependency claim, not a naming convention: row1903 uses only the root abscissae and g0,g1. The latter's defining rows513/514 involve only S coordinates5,6,7,8,84,85 and g0,g1. They involve neither H nor a private anchor witness. Thus changing the anchor point later leaves T, q, the roots, scalar point and all comparison bounds fixed.

I read the pinned Version13 scalar construction at lines21430–21439 and its surrounding preparation argument. After H0 it chooses a sufficiently divisible N0 before selecting s, explicitly allowing arbitrary further formal depths. Requiring Fs in8Z2 is therefore a permitted additional finite depth. It is compatible with the existing3-adic anchor and all other scalar conditions: one takes a common multiple of finitely many formal subgroup indices. The positive progression still has a dense real tail, so its strict scalar real inequalities and size requirement remain attainable. This is not an exact-valuation congruence imposed after those choices.

The accepted odd-root coefficient computation gives v2(X_i)=-1 and X_A=2v83, X_T=2v87, X_Z=2v89. Consequently q=3(2X_A)^2+3(2X_T)^2+27(2X_Z)^2 is1 modulo8. With Fs in8Z2 and C odd, t=T/C is odd. It is also3-integral by the existing anchor preparation. The inherited quaternion criterion therefore supplies one rational basepoint P on Q=N. No new global representation theorem is assumed.

## Local targets and real smallness

At2 choose u=2^nu2, nu2>=1, v=T/2 and

    z^2=C^2-3T^2/4+u^2/2.

After extracting C^2/4, the radicand is4-3t^2+2(u/C)^2, which is1 modulo8. It has a Q2 square root. Direct substitution gives Q=N. No integrality of v or z is required.

At3 choose u=3^nu3 with nu3>v3(C)=2^25, v=0 and z^2=C^2-3T^2/2+u^2/2. Its radicand after extracting C^2 is1 modulo3. The strict lower bound on nu3 is necessary and is explicitly imposed before prime selection. Arbitrarily increasing the preparatory denominator depth is allowed by the same positive-slope estimates used in shared314.

At17 choose u=17^nu17, nu17>=1, v=T/sqrt(2) and z^2=C^2+u^2/2. Here2 has residue square roots6 and11, C is a17-unit, and the latter radicand divided by C^2 is1 modulo17. This works even when T is not17-integral.

At a contact prime p, the prime selection excludes the finitely many denominators of the already fixed T. Since p>76176, N is p-integral and p is different from2 and3. Taking u=1/p leaves 6V^2-2Z^2=p^2N-1 for V=pv,Z=pz. Modulo p the right side is nonzero. If3 is square, the left side is a nonzero scalar times a split product of two independent linear forms. If3 is nonsquare, it is a nonzero scalar times the norm of Fp2/Fp. The norm map is surjective on nonzero elements, as its cyclic-group exponent p+1 has image of size p-1. Hence a solution exists and has a nonzero partial derivative12V or-4Z. One-variable Hensel lifting gives an exact local point with v_p(u)=-1. Repeated contacts impose the same condition once.

For any positive u in(1/(2lambda),1/lambda), choosing real v sufficiently large makes (u^2+6v^2-N)/2 positive and supplies z. All required conditions on u define open subsets of their local quadrics. The later rational approximation needs only to remain in these open sets; it need not preserve the exact displayed u values.

## One rational map and simultaneous approximation

For the rational basepoint P use Phi(d)=P-2B(P,d)d/Q(d), where B is the polar form. My checker verifies Q(Phi(d))=Q(P) after clearing Q(d)^2. If X is a local target with Q(X-P) nonzero, the identity Q(X)=Q(P) gives 2B(P,X-P)=-Q(X-P), so Phi(X-P)=X.

The exceptional tangent section does not contain a local open subset. To verify this without importing weak approximation on quadrics, suppose B(P,X)=N. When P is not proportional to X, there is h in X-perp with B(P,h) nonzero; otherwise the two linear functionals would be proportional by nondegeneracy. The local curve sqrt(1-s^2Q(h)/N)*X+s*h stays on Q=N, tends to X, and its B(P,.) value differs from N by a nonzero first-order term. When P is proportional to X, the two level and tangent equations force P=X. Then X-perp is nondegenerate since Q(X)=N is nonzero, so it contains h with Q(h) nonzero. The same curve leaves the tangent section through its nonzero quadratic term. The square root near1 exists for sufficiently small s at every relevant place, including2. Thus every prescribed local open set contains a point in the image of this same rational map.

Choose such points and directions d locally. Continuity gives open boxes of directions on which Q(d) stays nonzero and Phi(d) stays in the required target set. Rational directions simultaneously meeting all boxes exist by the explicit coordinatewise CRT argument. For clarity, clear the finite local denominators with an integer D, choose sufficiently accurate residue conditions modulo M on the D-scaled targets, and take arbitrarily large L congruent1 modulo M. Integers A+Mk in the fixed residue class give (A+Mk)/(DL), with real mesh M/(DL) tending to zero. Increasing the finite precision first absorbs v_p(D) and ensures division by L preserves each approximation. Apply this to each of the three direction coordinates. This is an elementary construction of the required rational point, not a new arithmetic hypothesis or three new quartic variables.

## Global order and acceptance boundary

The order is important and valid: strengthen the scalar finite preparation; choose scalar and odd-root data; fix T and a rational basepoint; fix comparison neighborhoods and real bounds; enlarge denominator depths including nu3>2^25; select contact primes outside the fixed finite exclusions; choose the original lambda; approximate the anchor point; finally choose H in the unchanged Pi19/continuity progression and real neighborhood.

The selected anchor has gamma=1/u, gamma/lambda in(1,2), v_p(gamma)=1 at contacts and v_p(gamma)=-nu_p at2,3,17. These are exactly the uniform shared314 conditions. No new congruence on H or changed test bound is introduced. Additional denominator primes of the anchor point need no restriction: the shared314 pole valuation parity away from odd-contact support depends on R, and the gamma contribution changes it only by an even amount. The new private values do not enter another equation or bound except through the already controlled gamma powers.

Thus soundness maps every new solution to sparse-shared314, and completeness chooses suitable new witnesses for every integer input. Arbitrary old witness fibers are not claimed equivalent. Both directions preserve the input projection under the inherited source assumptions. This acceptance applies only to the pinned313 artifact and proof, not to dropping its inverse, imposing a different exact valuation, or reusing another private witness without a new argument. It is not a publication approval;313 remains above the strict-under300 milestone.
