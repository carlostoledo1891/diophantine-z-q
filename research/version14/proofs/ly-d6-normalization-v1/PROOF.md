# Discriminant-six normalization from Lin–Yang Example 30

Author: Gaussian, 8 November 2026. This is a new connecting proof awaiting independent review. It uses the published inputs below and replaces the choice of evaluation point in Example 30. It does not assert Baba–Granath's product-isomorphism conclusions or their explicit conic descent.

## 1. Exact domain and retained published inputs

Let X be the unique discriminant-six quaternionic locus in the principally polarized moduli space A2, identified with X_0^6(1)/W_6. Let P_d denote its CM point of discriminant d for d=-4,-3,-24. Lin–Yang, final Mathematische Zeitschrift295 (2020), Example29 and Example30, printed795–797, uses exactly this X. Let j be the Hauptmodul defined by j(P_-4)=0, j(P_-3)=infinity, j(P_-24)=-16/27. These are its defining three values, not evaluations deduced from an Igusa formula.

The following are explicit retained source statements. They are not inferred from the formula to be proved.

1. On printed793, equations(13),(14), s2=psi4, s3=psi6, s5=2^12*3^5*chi10, s6=2^12*3^6*chi12. Their Siegel weights are4,6,10,12, so the weighted-projective weights used below are2,3,5,6. The universal Igusa conversion is J2=-3 chi12/chi10, J4=(J2^2-psi4)/24, J6=(-J2^3+36 J2 J4+psi6)/216, J10=-4 chi10.
2. Example29 identifies the intersections with the product modular curve Y1. Example30 on796 gives the divisor statements div(s2)=P_-3/3, div(s3)=P_-4/2, div(s5)=P_-3/3+P_-4/2 and the resulting identities

       s3^2/s2^3=c1*j,   s5/(s2*s3)=c2,   s6/s2^3=c3*j+c4.

   We retain these exact global identities on X, including the affine shape of the last ratio. Their role is essential: the first ratio has divisor P_-4-P_-3, the second has zero divisor, and the holomorphic s6 divided by s2^3 has no pole except a possible simple pole at P_-3. On the genus-zero curve these give respectively a scalar multiple of j, a constant, and an affine function of j. We do not obtain the global shape merely by evaluating at finitely many points.
3. On796 the same source gives the Y1 parameterization [s2,s3,s5,s6]=[u^2,u^2(u-1728),0,2^12*3^6*u^4], where u is the elliptic j-function, and identifies the common P_-4 with u=1728. Thus it supplies the required principally polarized product intersection, not just a rational isogeny to a product.
4. On797 it gives the parameterization of the modular curve Y'_5 with period matrices [[3z,5z],[5z,10z]]:

       [s2,s3,s5,s6]=[(x-12)^2, x(x^2-36x-432),
                      -2^10*3^5*x, 2^10*3^5*(x^2+12x+12)],
       x=eta(z)^6/eta(5z)^6+22+125 eta(5z)^6/eta(z)^6.

   It states that X intersects Y'_5 at discriminants -4,-19,-24 and that x at the discriminant -24 points is -6 +/- 6 sqrt(-3). We consume only the -24 intersection and those two x values. This is a published assertion about the elliptic eta-Hauptmodul and the exact CM intersection. It is retained as an input, not proved by a genus-two product-isomorphism argument here. Its intersection framework is the singular-relation/optimal-embedding discussion in Examples29–30 and Proposition36; the general CM-value methods and their named sources are described on794. No claim of a new proof or exhaustive ancestor audit of these inputs is made.

The new calculation below does NOT consume the subsequent assertion on797 that j(P_-19)=81/64. Nor does it use the closing equality with equation(2) on that page as its premise. Thus neither the introduction's attribution of (2) to Baba–Granath nor its CM(-19) normalization comparison is being used to determine the constants.

## 2. Determine all four constants at two unambiguous points

At P_-4 the Y1 formula gives

    (s6/s2^3)(P_-4) = 2^12*3^6*1728^4/1728^6 = 1,

because 1728=2^6*3^3. The denominator is nonzero. Since j(P_-4)=0, c4=1. This is the direct published calculation on796.

Now choose either of the two Y'_5 points of discriminant -24. Its x satisfies

    x^2+12x+144=0,   x^3=1728,   x != 0.

Substitution into the four displayed polynomials gives

    s2=-36x,  s3=6912,  s5=-248832x,  s6=-32845824.

In particular s2 and s3 are nonzero, and all three weight-zero ratios can be evaluated. Their exact values are

    s3^2/s2^3=-16/27,   s5/(s2*s3)=1,   s6/s2^3=11/27.

Both conjugate values of x give the same answers. These are ratios of equal weights, so the common weighted rescaling in a projective parameterization cancels. No choice of its scalar representative enters the result.

The intersection maps this point to P_-24 on X, at which j=-16/27 by definition. Therefore the global identities in input2 give c1=1 and c2=1. The last gives

    11/27 = (-16/27)c3+1,

so c3=1 as well. This determines the global constants. The argument uses a nonzero finite value of j, so it does not divide by a zero or infinite parameter.

## 3. Recover the weighted modular and Igusa parameterizations

On the dense open set where s2*s3 is nonzero, put a=s3/s2^2. Weighted rescaling by a in weights(2,3,5,6), using the three identities just proved, gives

    [s2,s3,s5,s6]=[j,j^2,j^3,j^3(j+1)].

For example a^2*s2=s3^2/s2^3=j, a^3*s3=j^2, a^5*s5=j^3, and a^6*s6=j^3(j+1). Thus this equality is derived from the ratios, without assuming a globally chosen square root or normalization of a modular form. It is an equality of rational maps and extends wherever the underlying moduli map is defined. At j=0,infinity the object is decomposable; no nonsingular genus-two curve is asserted there.

The universal conversion in input1 then gives the Igusa representative

    [-(j+1), (j^2+j+1)/24,
      -(j^3-2j^2+1)/432, -j^3/(2^10*3^5)].

Rescale by -12 in weights(1,2,3,5). The resulting equality is

    [J2,J4,J6,J10]
      = [12(j+1), 6(j^2+j+1), 4(j^3-2j^2+1), j^3].

This is the normalized formula needed by the current manuscript. It agrees with Lin–Yang(2), but (2) was not used in this derivation. The parameterization is an isomorphism onto the quaternionic locus as asserted for the underlying X and its modular map in the retained inputs; the new calculation identifies the actual functions and their normalization, not a new representability theorem.

## 4. Q-definition and exact consumer boundary

The actual principal-polarization/O-action datum and the identification of its coarse positive-normalizer quotient with X are separate A001 inputs. Baba–Granath Theorem2.1 and the canonical-model statements on737–738, together with Lemma3.1, are the retained coarse-quotient/Q-definition inputs; none of those statements depends on its later Proposition3.7/3.8 or explicit Theorem3.10 map. The current proof still requires their actual application to the chosen datum.

The newly proved identities also give

    j=s3^2/s2^3=s5^2/s2^5
      =(12^5*J10)^2/(J2^2-24*J4)^5.

The equality of constants follows from 16*12^10=2^24*3^10 and J10=-4 chi10. This is a weight-zero rational expression in the rational Igusa invariants on the moduli locus. Consequently, under that Q-defined moduli map, it gives the Q-defined coordinate on X with the stipulated three CM values. One may also use the resulting rational Igusa parameterization. This uses the standard Q-structures of those invariants and of the moduli map; it does not use Baba–Granath's explicit conic isomorphism or its CM(-19) descent test.

For current ed992 lines724–741, this supplies the normalization only after the fixed polarized-datum and branch-index applications are joined. The analytic branch orders4,6,2 remain supplied by the separate normalizer/fixed-point argument. At lines798–850 the cover and its tame extension/pullback use the three branch values and coordinate, not the explicit conic coordinates [h4^3,h6^2,h12]. Lines851–861 use the R=Z polarized equivalence relation and this same rational Igusa tuple to identify the conjugates' geometric polarized moduli point; that is a positive use of the formula, not merely a citation occurrence. At lines1206–1230 the repeated use needs exactly the normalized Igusa tuple above and the separate universal conversions/weight normalization. No degree, excluded prime or height constant is changed by this replacement.

This packet does not prove Baba–Granath3.7 or3.8 false as abstract statements: its displayed natural map is a degree-four isogeny, but another unpolarized isomorphism is a different question. It does not prove its explicit conic descent3.10. It does not retire those dependencies from any other application, archival proof or future consumer without a separate map. Its present consumer audit is limited to the named current proof passages and the associated A001/B11 interfaces.
