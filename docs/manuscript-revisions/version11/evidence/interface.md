# Issue 2 Kato index repair: manuscript interface audit

Date: 2026-11-07. This audit concerns the proposed repair to the application of Kato 1999, Theorem 0.8. It does not certify the whole manuscript. No manuscript or GitHub file was changed.

## Result

The reviewer identifies a real missing interface in v10. The system defined at K8 on the 2004 index set does not, as written, supply the levels required by the 1999 definition. The proposed extension supplies them, and its norm to the cyclotomic tower is the same retained class. I found no residual mathematical hypothesis or circularity in this repair. Two small clarifications should accompany it: distinguish the two uses of xi, and explicitly carry the fixed lattice-clearing factor. These are included in `CORRECTION.tex`.

## Inputs checked

* `work/github-issue-review-20261107/quartic_v10-current.tex`, SHA256 `9559b22cc581346da1b3150fa9b8dfb62cfb048f6aac0b866448ae7ae879ff38`, especially lines 12238–12795.
* `work/github-issue-review-20261107/issue2-latest-20261108T003953Z.json`, SHA256 `b1173c2a75171dfbf7923e4225f016062be228af0940767730cc8b67a84c12c4`, reviewer comment dated 2026-11-07T23:20:51Z.
* The reports and source pins in `work/astra-kato-primary-closure-002` and `work/astra-kato-primary-001`. Their earlier acceptance labels were not substituted for the index check.
* Original page images freshly inspected: Kato 1999 pp.314 and 318, and Kato 2004 p.186. The 1999 text of §§0.4–0.8 was also read. The original 2004 Proposition 8.12 permits the enlarged indices used below. Original URLs are https://www.numdam.org/article/AST_2004__295__117_0.pdf and https://doi.org/10.2996/kmj/1138044090 . Fresh web fetches failed because of size/access; the pinned original local page images supplied the evidence.

## Symbol and support ledger

| Symbol | Meaning in this manuscript | Interface requirement |
|---|---|---|
| N | Conductor of the one fixed elliptic curve | Not Kato 1999's index modulus |
| D=2^a d | Primitive conductor of the chosen quadratic character | d is its odd part; d divides F |
| F | Squarefree common odd conductor support | Not the coefficient field called F in Kato 1999 §0.1, which here is Q_2 |
| c,d_s | Retained smoothers, both 1+2^e 3N_odd F | Prime to 2Nd; may depend on F; never divided out |
| Sigma | prime(2Nd c d_s) | Excluded support for the original 2004 subfamily, not the inverted support of the 1999 application |
| N_K | 2Nd | Divisible by 2 and supported on all ramification of T chi |
| N'_K | c d_s | Coprime to N_K; its primes are excluded from indices, not inverted |
| d_K | 1 in Kato 1999 §0.4 | Distinct from the manuscript's odd conductor d |
| xi | Fixed modular-symbol combination in K4 | Must not silently become the Iwasawa class in Kato 1999 §0.7 |
| xi_K | Norm-image class used by Kato 1999 | Equals the retained y-system after the fixed lattice comparison |

The reviewer's sentence saying Sigma contains 3 is not needed and is not true for every fixed curve/character. The factor 3 in K5 makes the smoothers prime to 3; it does not insert 3 into Sigma. This does not affect the proposed repair. Every prime of N or d is present in the support of z_Dm even before it is present in m.

## Complete index and transition check

The defining expression for K8 makes sense for every positive m with (m,c d_s)=1. Indeed, prime(c d_s) is disjoint from prime(2NDm), by K5 and d|F. Kato 2004 §8 constructs the class z_Dm with S_Dm=prime(2NDm), and K7 transfers its integral j_* condition. This is an extension of the definition, not an application of the old restricted index condition to inadmissible m.

Restrict this extended family to N_K|m and (m,N'_K)=1. Its classes map to H^1(Z[zeta_m,1/N_K],T chi), after the one fixed lattice clearing if necessary. The sheaf is lisse there, since all ramification of T chi is supported on 2Nd. The j_* class is restricted to this open. No new projector or trace denominator is used.

For every prime l not dividing N'_K:

* If l|m, then S_Dml=S_Dm. Proposition 8.12 has an empty product and gives the required norm equality, including repeated powers and primes dividing N_K.
* If l does not divide m, then l does not divide 2Nd because N_K|m. Thus l is good for the original curve and unramified for chi, S_Dml minus S_Dm={l}, and twisted equivariance gives exactly K9. This is Kato 1999 (0.1.1), with arithmetic Frobenius in P_l and inverse deck action in its argument.

The two cases exhaust the 1999 definition. There is no need to define P_l by the good-prime formula at l|N_K, because such l always divide m and enter the first case.

## Identity of the retained class

For n on the cofinal cyclotomic tail, transitivity gives

    cor_{Q(zeta_(N_K 2^n))/Q(zeta_(2^n))}(y_(N_K 2^n))
      = cor_{Q(zeta_(D N_K 2^n))/Q(zeta_(2^n))}(z_(D N_K 2^n) tensor e_chi).

Both original z-classes have support prime(2Nd), because

    S_(D N_K 2^n)=S_(D 2^n)=prime(2Nd).

Proposition 8.12 therefore replaces the inner class by z_(D 2^n) under norm, with no Euler factor and no field-degree scalar. The result is y_(2^n). This proof uses the original class at conductor D; it does not change the signed discriminant convention or lose the dyadic part of chi.

Kato 1999 §0.7 defines xi_K by exactly this norm from levels N_K 2^n, with d_K=1. If the original lattice is already the chosen T-lattice, xi_K is the image of y_(2^infty). Otherwise choose the fixed lattice multiplier u_E=2^{c_E}; then xi_K is the image of u_E y_(2^infty). At every height-one localization under consideration, 2 is invertible, so u_E is a unit and the coordinate ideals and index lengths agree. This assertion does not divide out either smoother.

The full cyclotomic sign component is then identified with the manuscript's real-tower coefficient convention as already explained after K10. Integral corestriction is not a normalized sign projector. Rational passage to a sign component is permitted only after inverting two. The repaired identification precedes that passage and so determines the actual class in either convention.

## Downstream dependencies and circularity

Kato 1999 requires a nontorsion supplied class, not a chosen generator. The earlier nonvanishing argument uses the same original symbol combination and smoothers. The new norm identity identifies that class with xi_K; it does not infer their equality from rank one or from a length bound. The fixed lattice multiplier preserves nontorsionness.

The application retains the stronger abelian-kernel unipotent hypothesis and the already printed rational irreducibility argument. No residual irreducibility at two is added. Purity and oddness are unchanged. The comparison of full-open and j_* subscript-zero groups uses the local cone K16; the printed proof of K16 uses no Euler-system bound. Thus identifying xi_K first does not create a circular dependency with K15.

The replacement does not alter E.1, K3, or the allocation of local factors. At a bad prime N_K already includes it; at an active conductor prime the ramified quadratic contribution remains as printed; smoother primes stay outside the inverted support. Although N_K depends on the chosen constituent d, no uniform bound on its magnitude is needed in the 1999 theorem. The later fixed-error argument still charges only fixed bad/local types and the explicitly retained unused-good Euler factors.

## Scope of acceptance

Accepted: the enlarged index family, both norm cases, its membership in the 1999 coefficient groups, and its actual retained-class identification, together with compatibility of the proposed repair with K5–K9 and the printed downstream index calculation.

This is not a new audit of every local-control theorem, every reciprocity normalization, or the entire restricted converse. Those remain the separately stated inputs of the manuscript and source records. No additional repair to those inputs was found in this interface audit.
