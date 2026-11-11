# Kato index extension and norm identification

Audit date: 7 November 2026. Scope: the missing index-set step in Issue 2, point 4. The current manuscript is `work/github-issue-review-20261107/quartic_v10-current.tex`, especially K4--K9 and lines 12680--12690. No manuscript or public issue was edited.

## Verdict

The reviewer's proposed repair is mathematically correct. Kato 2004 Proposition 8.12 applies to the retained classes at the additional indices needed by Kato 1999. The extension requires an explicit definition, because the displayed K8 currently only defines the classes on the smaller 2004 index set. The norm to the pure dyadic tower is exactly the old class, with no extra Euler factor or field-degree multiplier.

The proof below uses the original page images, not the earlier audit's conclusion. This audit does not recheck every other hypothesis of Theorem 0.8 or the manuscript's separate comparison of the full and j-star cohomology conventions.

## Original formulas inspected

Kato 2004, printed p.180, formula (8.1.3), constructs the retained class for an arbitrary positive integer m, subject to the conditions inherited from (8.1.2). Those include exclusion of the smoothing primes from S. There is no requirement that m belong to the later set Xi of Section 13.1. For an SL2(Z) symbol, Section 8.9, printed p.185, takes an auxiliary level divisible by both m and N with prescribed prime support S. This explicitly permits m to contain primes dividing N.

Proposition 8.12, printed p.186, takes m | m', requires S union prime(m') contained in S', and requires prime(c d_s) disjoint from S'. Its norm multiplier is

    product over ell in S' minus S of
    [1 - conjugate(a_ell) sigma_ell^(-1) ell^(-r)
       + conjugate(epsilon(ell)) sigma_ell^(-2) ell^(k-1-2r)].

For the fixed rational weight-two elliptic newform, trivial nebentype, and r=1, a new good prime contributes

    1 - (a_ell/ell) sigma_ell^(-1) + (1/ell) sigma_ell^(-2).

The indexing is a set difference. Increasing exponents of primes already in S contributes no factor. Nor does adjoining a prime already included in S for another reason.

Kato 1999, printed p.314, Section 0.1 and (0.1.1), requires classes at every m with N | m and gcd(m,N')=1. For ell not dividing N', the norm from m ell to m is the identity if ell | m, and is P_ell(ell^(-1) sigma_(ell,m)^(-1)) if ell does not divide m. Here P_ell(X)=det(1-phi_ell X | T), and phi_ell is arithmetic Frobenius. Printed p.318, Section 0.7, defines the supplied element by norm from the N p^n tower to the d p^n tower of Section 0.4. The relevant choice is d=1 there.

## Extension of the retained construction

Keep the manuscript's notation D=2^a d for the primitive quadratic conductor, with d odd, and keep its fixed symbol combination and smoothers. Set

    N_K=2Nd,       N'=c d_s.

K5 gives gcd(N_K,N')=1. Indeed, the smoothers are odd and prime to N and F, while d | F. The factor 2^a in D need not divide N_K: only its prime support is needed for the inverted arithmetic support, and the field L_m below always contains the full conductor D.

For every m satisfying N_K | m and gcd(m,N')=1, define

    K_m=Q(zeta_m),   L_m=Q(zeta_(Dm)),
    y_m=cor_(L_m/K_m)(z_(Dm) tensor e_chi),
    S_(Dm)=prime(2NDm).

The notation Dm means the product, as in the current K8, not a least common multiple. It causes no problem when D and m overlap.

All the construction's hypotheses hold. The support S_(Dm) contains prime(Dm), prime(N), and 2. It is disjoint from prime(N'). Section 8.9 therefore supplies the retained class for exactly the same lattice and symbol. The character chi is trivial on L_m, so tensoring by e_chi is defined there. The already stated Mackey argument K7 gives the integral j-star condition after corestriction. Restriction to the open scheme with N_K inverted then places the same class in the full cohomology group used in 1999.

This definition agrees with the old K8 wherever both apply. It is an extension of the index set, not a renormalization. If the manuscript uses a fixed power of two to put the original image lattice into T, apply that same power at every old and new level. Every identity below commutes with it; away from two that power is a unit.

## The two norm cases

Let N_K | m, gcd(m,N')=1, and let ell be a prime not dividing N'.

If ell | m, then S_(Dm ell)=S_(Dm). Apply Proposition 8.12 to the old modular indices Dm | Dm ell. It gives

    cor_(L_(m ell)/L_m) z_(Dm ell)=z_(Dm).

Corestriction transitivity, and the fact that chi is trivial over both fields in this displayed norm, give

    cor_(K_(m ell)/K_m) y_(m ell)=y_m.

This includes ell=2, every bad prime of E, and every prime of d, since they already divide m.

If ell does not divide m, the divisibility N_K | m implies ell does not divide 2Nd. Hence ell is a good odd prime, chi is unramified at ell, and ell does not divide Dm. Consequently

    S_(Dm ell) minus S_(Dm)={ell}.

The displayed good-prime factor from Proposition 8.12 is the only factor. For a deck transformation g the tensor/corestriction identity is

    cor((g z) tensor e_chi)=chi(g)^(-1) g cor(z tensor e_chi).

Taking g=sigma_ell^(-1) multiplies its linear term by chi(sigma_ell)=chi(ell). The quadratic term is unchanged because chi^2=1. Thus

    cor_(K_(m ell)/K_m) y_(m ell)
      =[1-a_ell chi(ell) ell^(-1) sigma_ell^(-1)
          +ell^(-1) sigma_ell^(-2)] y_m.

Arithmetic Frobenius on T_2(E) tensor chi has trace a_ell chi(ell) and determinant ell. Therefore

    P_ell(X)=1-a_ell chi(ell)X+ell X^2,

and the factor is exactly P_ell(ell^(-1) sigma_ell^(-1)), namely K9. The coefficient representation is T chi, not its dual. Kato's accompanying interpretation of P_ell(X)^(-1) using the dual sheaf's zeta function does not instruct us to dualize T again. The inverse in the norm factor concerns the cyclotomic deck element; the definition of P_ell uses arithmetic Frobenius on T chi. These conventions agree with the manuscript.

No polynomial at a bad or twisting prime is needed in the new-prime case. All such primes divide N_K and hence m. Smoothing primes are excluded by N', rather than inverted in the arithmetic support.

## Exact identification of the supplied Iwasawa class

For n>=1, the old K8 class y_(2^n) is defined. The upper and lower modular supports are

    S_(D N_K 2^n)=S_(D 2^n)=prime(2Nd).

Proposition 8.12 therefore gives the exact retained-class equality

    cor_(L_(N_K 2^n)/L_(2^n)) z_(D N_K 2^n)=z_(D 2^n).

Both L-fields contain the character conductor. Tensoring by e_chi commutes with this norm. Transitivity along the two towers now gives

    cor_(K_(N_K 2^n)/K_(2^n)) y_(N_K 2^n)
      =cor_(L_(2^n)/K_(2^n))(z_(D 2^n) tensor e_chi)
      =y_(2^n).

This is corestriction of the actual upper class, not corestriction of a restriction. Thus no multiplication by an extension degree appears. The added primes dividing N or d are already in the lower modular support, so no Euler factor appears either. Higher dyadic exponents likewise add no support prime.

The equalities commute with transition maps. Section 0.7 of Kato 1999 with d=1 therefore supplies precisely the image of y_(2^infinity), in the full-cohomology convention of that source. A cofinal n>=1 tail suffices. The further n>=a conductor simplification in the manuscript is compatible but is not needed for this identity.

## Source record and integration

Original 2004 publication: Kato, Astérisque 295 (2004), 117--290, https://www.numdam.org/article/AST_2004__295__117_0.pdf . Local file `work/kato-2004.pdf`, SHA256 `3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`.

Original 1999 publication: local `work/astra-kato-primary-001/kato-1999.pdf`, SHA256 `483dc18c56b2fe9cfac4e37f2e6594399625c3f0ea98a05bb69116377c67fc06`. Its original pages 314 and 318 were read visually, along with 317 for context. The printed definition of Section 0.4 was also checked against the existing original text extraction.

Fresh visual reads used the existing page renders for 2004 pp.153,180,185,186,224 and 1999 pp.314,317,318. The high-resolution p.186 render is `work/astra-kato-primary-closure-002/kato-p186.png`. The page hashes are in the supplied primary-source manifests.

`replacement.tex` replaces the paragraph beginning at current line 12680 through the words "need not be inverted." It leaves the subsequent nonvanishing, representation, and cohomology-comparison arguments in place. The replacement makes the enlarged index set and exact Section 0.7 identification explicit.
