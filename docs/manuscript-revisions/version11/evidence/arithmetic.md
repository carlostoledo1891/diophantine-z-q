# Independent audit of the Kato 1999 index-set repair

Date: 7 November 2026. Scope: the remaining Point 4 in GitHub Issue 2, as recorded in `issue2-latest-20261108T003953Z.json`. This checks the proposed repair itself against Kato's primary definitions, not merely the old representation-theoretic applicability argument. No manuscript or GitHub content was changed.

## Verdict

The repair is valid. Formula (K8) extends to all indices required by Kato 1999 with

    p=2,  N_K=2Nd,  N'_K=c d_s.

The extended classes satisfy Definition 0.1 exactly. Their image under the norm in section 0.7 is the full-cohomology image of the original retained class y_{2^infinity}, with no extra factor. Thus the existing nonvanishing argument and coordinate ideal concern the class actually used by Theorem 0.8.

Three clarifications improve the proposed insertion. Identify the full-cohomology target explicitly; distinguish Kato 1999's element xi from the modular-symbol combination already called xi; and state the norm equality on a cofinal tail n>=1, since the old index condition in (K8) does not include m=1. These are precision improvements, not a failure of the suggested fix.

## 1. What is missing from the current passage

The frozen current TeX defines (K8) at lines 12394-12407 only when prime(m) intersects Sigma in {2}, with Sigma=prime(2Ndcd_s). This is the index convention of Kato 2004, section 13.1. It excludes levels divisible by odd primes of Nd.

Kato 1999, section 0.1, instead requires a class at every positive integer m divisible by his N and coprime to his N'. The present lines 12680-12684 assert this norm relation without extending the index set. They also leave implicit the identification of the element in section 0.7 with the previously retained cyclotomic class. The latest reviewer comment correctly isolates these two linked omissions.

The construction in Kato 2004, section 8.1, is broader than the index convention in section 13.1. That construction, rather than a formal reindexing of the already printed restricted system, supplies the missing classes.

## 2. Exact 1999 hypotheses and notation

The primary PDF was inspected visually on printed pages 314-318. In section 0.1:

* p is any prime; the coefficient field is a finite extension of Q_p, and T is a finite free lattice with continuous G_Q action.
* N>=1 is divisible by p, and T is unramified at every prime not dividing N.
* N'>=1 is coprime to N.
* The Euler-system elements belong to H^1(Z[zeta_m,1/N],T) for every m>=1 satisfying N|m and gcd(m,N')=1.
* For every prime ell not dividing N', corestriction from m ell to m gives the old class if ell|m, and P_ell(ell^{-1} sigma_{ell,m}^{-1}) times that class otherwise.

Here P_ell(X)=det(1-Fr_ell X|T), with arithmetic Frobenius. In the second case ell does not divide N automatically, since N|m. No polynomial at a ramified prime is needed there.

Section 0.4, printed page 315, allows any divisor d_Kat>=1 of N. Take d_Kat=1, not the odd part d of the quadratic conductor. Section 0.5 then defines

    H^q = lim_n H^q(Z[zeta_{2^n},1/N_K],T chi)

with corestriction transitions. Section 0.7, printed page 318, defines xi_Kat as the norm image in this H^1 of the inverse system at levels N_K 2^n. Its coordinate ideal is the image of evaluation at xi_Kat on Hom_Lambda(H^1,Lambda).

For a height-one prime not containing 2, section 0.4.1 gives the DVR property needed by Theorem 0.8. The theorem uses conditions 0.6(i), (ii), (iii) in that case; the strong residual and integral-cokernel versions are required only for primes containing p. Condition 0.6(iv) is n(V,mathfrak p)=1 and yields the index formulation. The existing odd elliptic representation supplies that dimension. There is no odd-p restriction in this statement of Theorem 0.8.

The theorem's non-torsion hypothesis is on the localized xi_Kat, not on an unspecified generator. Section 5 below supplies the exact class identity needed to reuse the manuscript's established nonvanishing argument.

## 3. Construction at every missing index

Keep the manuscript's notation D=2^a d for the primitive quadratic conductor, with d odd, and the original modular level N. The factor d divides the squarefree odd conductor product F. Formula (K5) gives c=d_s=1+2^e 3N_odd F. Thus c and d_s are odd and coprime to 3NF, hence to 2Nd. Consequently gcd(N_K,N'_K)=1.

The representation T chi is unramified outside prime(2Nd): T is unramified outside 2N, and chi outside D. The integer N_K need not contain the full power of 2 in D; section 0.1 requires the ramification support to be contained in prime(N_K), not divisibility by the Artin conductor.

For every m with N_K|m and gcd(m,N'_K)=1, set K_m=Q(zeta_m), L_m=Q(zeta_{Dm}), and define y_m by precisely the formula (K8), using the same retained smoothing integers, symbol combination, lattice map and any fixed lattice-clearing multiplier already used there. No new m-dependent choice is made.

The original class z_{Dm} exists. Kato 2004, (8.1.2)-(8.1.3), printed page 180, allows every level M>=1 with the stated support and smoothing conditions. For an SL_2(Z) symbol, (5.1.1) requires the construction set to contain prime(MN). Taking M=Dm and S_{Dm}=prime(2DmN) satisfies this and includes p=2. The remaining conditions are prime(cd_s) disjoint from S_{Dm}, gcd(cd_s,6)=1, and gcd(d_s,N)=1. They follow from (K5) and gcd(m,c d_s)=1. A fixed integral linear combination of symbols preserves these conditions and all norm identities.

The character is trivial on G_{L_m}, so tensoring with e_chi is the same integral operation as before. The already printed Mackey argument (K7) preserves the j_* condition under corestriction. Restricting the resulting class to Spec Z[zeta_m,1/N_K] gives the class in the full group required by 1999. On that scheme T chi is lisse.

The sets S_{Dm} are the 2004 construction and Euler-modification supports. They are not the sets of primes inverted in the fixed 1999 cohomology groups. In particular, a fresh prime dividing m need not be inverted in N_K. Conversely, primes excluded only by smoothing belong to N'_K and are not added to N_K.

## 4. The complete norm relation

Let m be an admissible 1999 index and let ell be any prime not dividing N'_K. Then m ell is also admissible. Proposition 8.12 of Kato 2004, printed page 186, applies because Dm divides Dm ell, S_{Dm} union prime(Dm ell) is contained in S_{Dm ell}, and the smoothing primes are disjoint from the latter support.

If ell divides m, then S_{Dm ell}=S_{Dm}. The product in Proposition 8.12 is empty, even if ell is a bad prime or a conductor prime. Thus the norm of z_{Dm ell} to z_{Dm} has no factor.

If ell does not divide m, then ell does not divide 2Nd because N_K|m. It is a good odd prime for the original elliptic curve and unramified for chi. Also ell does not divide D, so S_{Dm ell} minus S_{Dm} is exactly {ell}. For weight 2 and r=1, Proposition 8.12 gives the factor

    1 - (a_ell/ell) sigma_ell^{-1} + (1/ell) sigma_ell^{-2}

before twisting. Transitivity compares the two paths from L_{m ell} to K_m, through K_{m ell} or through L_m. The deck-equivariance identity printed immediately before (K9) moves this factor through twisted corestriction. Since chi is quadratic, the resulting factor is

    1 - (a_ell chi(ell)/ell) sigma_ell^{-1}
      + (1/ell) sigma_ell^{-2}
    = P_ell(ell^{-1} sigma_ell^{-1})

for T chi. The determinant term is unchanged because chi(ell)^2=1. This is exactly (K9) and Definition 0.1.1, including the inverse deck action and both cases of the relation. The integer ell is odd in the second case, so its denominator is a 2-adic unit.

No unused bad-prime Euler polynomial is being substituted into the new-prime case. The requirement N_K|m is what excludes that error.

## 5. Exact identification of xi_Kat

For n>=1 consider the field diamond

    A_n = Q(zeta_{D N_K 2^n}),
    B_n = Q(zeta_{N_K 2^n}),
    C_n = Q(zeta_{D 2^n}),
    E_n = Q(zeta_{2^n}).

Both B_n and C_n are intermediate fields in A_n/E_n. There is no need to assume that they are nested relative to one another. By transitivity,

    cor_{B_n/E_n}(y_{N_K 2^n})
      = cor_{A_n/E_n}(z_{D N_K 2^n} tensor e_chi)
      = cor_{C_n/E_n} cor_{A_n/C_n}
          (z_{D N_K 2^n} tensor e_chi).

The construction supports satisfy

    S_{D N_K 2^n}=S_{D 2^n}=prime(2Nd).

Proposition 8.12 with those equal supports sends z_{D N_K 2^n} to z_{D 2^n}. Tensoring commutes with this transfer because chi is already trivial over C_n. Therefore

    cor_{B_n/E_n}(y_{N_K 2^n}) = y_{2^n}.

This is an equality of the actual retained classes. It is not a restriction-corestriction composition, so no field-degree multiplier appears. Equal construction supports give an empty Euler-factor product, so no extra Euler factor appears either. One does not average over a Galois group or divide by a projector.

Passing to the inverse limit over this cofinal tail and then to the full-cohomology groups gives exactly the element of 1999 section 0.7, with d_Kat=1. The old definition of (K8) begins at 2-divisible indices; n>=1 avoids pretending that it already defined y_1. A cofinal tail determines the same inverse limit. If the manuscript also uses a tail n>=a for the primitive conductor comparison, take n>=max(1,a); the identity is unchanged.

The equality survives rational sign projection and localization. Hence the coordinate ideal of xi_Kat is the coordinate ideal of the actual retained y_{2^infinity} under the previously printed j_* to full-cohomology H^1 identification. The existing comparison of subscript-zero H^2 groups is separate and is not altered by this repair.

## 6. What the replacement should and should not claim

The proposed reviewer insertion correctly repairs the index set and class identification. A precise replacement is provided in `proposed-replacement.tex`. It is intended to replace the paragraph beginning at line 12680 through the sentence ending “need not be inverted.” The following nonvanishing and Theorem 0.8 discussion can then continue as printed.

The replacement does not change the retained scalar, introduce extra inverted smoothing primes, change the original modular symbol combination, or replace the supplied class by a generator of a rank-one module. It does not independently reprove the representation-theoretic and nonvanishing parts of the manuscript; it identifies the Euler system and class to which those already printed arguments apply.

## Primary sources and frozen inputs

1. Kato, *Euler systems, Iwasawa theory, and Selmer groups*, Kodai Mathematical Journal 22 (1999), 313-372. Local primary PDF `work/astra-kato-primary-001/kato-1999.pdf`. Definition 0.1 and relation 0.1.1: printed 314-315; divisor and algebra in 0.4: 315-316; full cohomology in 0.5: 316; hypotheses in 0.6: 317; element in 0.7 and Theorem 0.8: 318. The local OCR misreads several >= signs and omits displayed formulas, so the rendered pages were checked directly. [Publisher record](https://www.jstage.jst.go.jp/article/kodaimath1978/22/3/22_3_313/_article/-char/en).
2. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Asterisque 295 (2004), 117-290. Local primary PDF `work/kato-2004.pdf`. Definition (5.1.1): printed 147; (8.1.2)-(8.1.3) and start of 8.2: 180; Proposition 8.12: 186; restricted index convention in 13.1: 224-225. The construction and norm formula on pages 180 and 186 were checked visually. [Primary PDF](https://www.numdam.org/article/AST_2004__295__117_0.pdf).
3. Frozen current TeX: `work/github-issue-review-20261107/quartic_v10-current.tex`, especially K4-K9 at lines 12311-12424 and the consuming passage at 12680-12721.
4. Reviewer comment: `https://github.com/elliotglazer/diophantine-z-q/issues/2#issuecomment-6714388221`, read from the supplied JSON snapshot.

SHA-256 bindings:

    kato-1999.pdf
    483dc18c56b2fe9cfac4e37f2e6594399625c3f0ea98a05bb69116377c67fc06
    kato-2004.pdf
    3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d
    quartic_v10-current.tex
    9559b22cc581346da1b3150fa9b8dfb62cfb048f6aac0b866448ae7ae879ff38
    issue2-latest-20261108T003953Z.json
    b1173c2a75171dfbf7923e4225f016062be228af0940767730cc8b67a84c12c4

Rendered evidence is retained in `arithmetic/source-pages/`. This audit approves this specific index-set repair, not the entire manuscript.
