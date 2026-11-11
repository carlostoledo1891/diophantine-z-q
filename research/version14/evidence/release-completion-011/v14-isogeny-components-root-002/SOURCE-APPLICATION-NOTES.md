# Two arithmetic source applications

Author: /root. Status: awaiting independent review.

The target is the current Version14 manuscript, SHA256 1f7bf748843d67c6a67d9863931ff0a15ca2548ae171ec1c1ce34b9002eb70a8. These records map published inputs to existing passages; they do not change the manuscript or certify the entire converse.

## Milne isogeny ratio

I read the retained 2006 edition, printed pages97–100, including the full proof after equation7.3.1. The theorem heading asserts BSD invariance, but the finite-group identity itself is proved from duality and the global Euler characteristic. The current use only takes that arithmetic identity. Finiteness of Sha is supplied at the known simple-zero constituents by the forward results, not by the desired converse or by a corank-only assertion.

Use z(f)=#ker(f)/#coker(f). For the current principally polarized A and B, dual maps phi and psi compose to[2]. Their rank-one free indices I and J have IJ=2. Counting torsion and free cokernels gives z(phi(Q))/z(psi(Q))=(#A(Q)_tors/#B(Q)_tors)^2·J/I. Canonical height functoriality identifies J/I=2/I²=Reg_B/Reg_A. The Sha pairing identifies #kerSha(psi)/#kerSha(phi)=#Sha(B)/#Sha(A). Substituting both into7.3.1 and identifying local z with pullback measure ratios gives exactly the orientation at current5038–5044.

Milne initially chooses omega_A=phi*omega_B. The manuscript instead specifies Néron cotangent generators with phi*omega_B=a·omega_A. The change over every place multiplies by |a|_v, whose product over Q is1. Thus no measure factor is silently discarded. At good primes the common isogeny-invariant Euler factors cancel; Néron finite measure factors leave component numbers. The separate current5022–5035 paragraph retains the real kernel/cokernel ratio and integral a,b with ab=4. Their bounded valuations are not a BSD premise.

The source result does not supply finite Sha, the constructed dual isogenies, the polarization, the rank-one indices, or the component calculation. All are explicit incoming requirements. The prior A040 argument was read, not merely its acceptance label.

## Edixhoven components

I read Sections2,4 and5.1–5.4 of the pinned published1992 paper, including the page images299–300. At every companion prime, p is odd, E0=E^(h) has good reduction, L/F is totally ramified quadratic, and mu2 is in the base DVR. These are the hypotheses for n=2 in Theorem5.3; the source's theorem does not require an algebraically closed residue field.

The ramified twist has descent action[-1] on the good special fiber. Gr0 is the fixed subgroup, namely E0_tilde[2]. This is finite étale because p is odd. The positive filtration part is connected, so Remark5.4.1 gives Phi as this same finite étale residue-field group scheme. Hence its rational component number is #E[2]^Frob_p, not the geometric cardinal4. The identification preserves Frobenius; geometric and arithmetic Frobenius have the same fixed points. Twisting by h changes no2-torsion representation. Only the actual full rational2-torsion hypothesis sets t_p=2.

For the restriction of scalars, Proposition4.1 supplies the Néron model. Section5.1 before taking G-invariants describes the reduction filtration. Since O_L/p is the length-two ramified thickening and the good model is smooth, the reduction kernel is a vector group and the quotient is the connected good elliptic fiber. Thus this restricted model is connected and its component number is1. This is the Weil restriction before taking invariants, not the twist's fixed subgroup. The model is the base change of E0, as required by that proposition.

At split primes the local factors agree. The stated local squareness at2N and at active primes covers old bad/active support; outside it and hk the models have good reduction. Thus the remaining ratio is sum t_p at companions. Its positive sign in s_A−s_B becomes negative in the inverse determinant expression containing−s_A. No inference about the global determinant construction follows from this component calculation alone.

## Scope and provenance

The published PDFs were locally hash-verified. Prior A040 and A069 reports were read and compared against the current consuming passages. No claim is made that all earlier audits checked every convention. Original frozen DIRECT-MAIN-017 contains both clauses but also several other inputs; these two records cover only the isogeny and component clauses. The current integral-calibration application still requires its separately reviewed determinant and specialization construction. All source PDF copies and page images stay local-only.
