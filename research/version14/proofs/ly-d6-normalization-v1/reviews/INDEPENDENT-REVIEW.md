# Independent review of the Example30 normalization substitution

Reviewer: /root/astra_v14_baseline_compiler. Author: /root/astra_v14_baseline_gaussian.

Accept LY-D6-CM24-NORMALIZATION as the stated new connection under its six retained inputs. The exact author manifest is 54f07eabba99eccfbd7054fca701eb3a306ff3f02a5cafa53e72f5619a37e459 and PROOF.md is b963eca85750ebc724370ec76b271a97461208db7c6cf3e5cbb8aa909779f666. This derives the normalized modular and Igusa formulas without the CM(-19) value or Baba-Granath's explicit conic map. It does not accept the whole A001 application, all published proof ancestors, or either longer proposed BG repair.

I did not author the new evaluation or suggest a repair. I gave provisional feedback that the calculations matched and that the already listed imports should remain explicit. My earlier reviews of source qualifications, Igusa incorporation and B11 are separate. INITIAL-READING.md records the source-first work before the author freeze and cards arrived.

## Source and object match

I independently rendered the final Lin-Yang PDF d90c9de3475820d5b037d22fbd94ebfe93f159e50ee69315c50d840a7db02e18 and visually read printed796-797. I read793-795,812,815, including the exact normalizations in equations13-14, Example29, the complete Example30 calculation, the first parameterization table and the Hauptmodul table. These identify the same unique discriminant-six locus, quotient by W6, and coordinate characterized by values0,infinity,-16/27 at discriminants-4,-3,-24.

The proof properly distinguishes the global identities from their evaluation. The source gives s3^2/s2^3=c1*j, s5/(s2*s3)=c2 and s6/s2^3=c3*j+c4. Their global validity and the affine shape of the last function are retained inputs. Finite evaluations alone would not prove those shapes. The Y1 product parameterization supplies the principally polarized intersection at discriminant-4, not merely an unpolarized isogeny. The source then explicitly gives the Y'_5 parameterization, the discriminant-24 intersection, and x=-6+/-6sqrt(-3). The proof uses that direct published assertion as its input. It does not infer the CM value from the desired genus-two formula.

The source's discussion on794 names the singular-relation and optimal-embedding framework and its CM-value methods. Those source ancestors remain retained. This review accepts the exact immediate published input and its application, not a new derivation of every eta CM value or every embedding count. The later assertion j(P_-19)=81/64 and the closing comparison with equation2 are unnecessary to this connection.

## Exact computation and weighted conventions

At the product point, s6/s2^3=2^12*3^6/1728^2=1 and j=0, so c4=1. The denominator is nonzero. At either discriminant-24 point, x^2+12x+144=0 implies x^3=1728 and x is nonzero. Direct reduction of the source polynomials gives s2=-36x, s3=6912, s5=-248832x and s6=-32845824. Hence the ratios are -16/27,1,11/27. Both roots give the same values and neither denominator vanishes. Equal-weight ratios cancel the unspecified weighted-projective scalar. Substituting the defining value j=-16/27 into the three global identities gives c1=c2=c3=1. There is no choice of conjugate or sign in these rational ratios.

On the dense open set, a=s3/s2^2 gives the weighted representative [j,j^2,j^3,j^3(j+1)] in weights2,3,5,6. This uses a rational scalar and requires no square root. Equations13-14 then give [-(j+1),(j^2+j+1)/24,-(j^3-2j^2+1)/432,-j^3/(2^10*3^5)]. Multiplication by -12 in weights1,2,3,5 gives [12(j+1),6(j^2+j+1),4(j^3-2j^2+1),j^3]. The signs of J2,J6,J10 and every power in this conversion check. The equality is of rational maps, with the decomposable boundary separated from the nonsingular genus-two locus. The independent arithmetic checker corroborates these identities in Q[x]/(x^2+12x+144) and Q[j].

The final proof also identifies the rational function j=s3^2/s2^3=s5^2/s2^5=(12^5*J10)^2/(J2^2-24*J4)^5. The coefficient identity 16*12^10=2^24*3^10 agrees with s5=2^12*3^5*chi10 and J10=-4*chi10. Thus this is the same coordinate over Q once the retained Q-defined moduli map is supplied. Rational coefficients alone are not being used to construct that map or its actual polarized datum.

## Current consumers and boundaries

I read actual ed992 passages724-761,798-866,1206-1230 and the four recorded consumer spans. The first needs the particular principal-polarization datum and its quotient before applying this normalization. The tame cover uses the ordered branch values and the separately proved indices4,6,2. The conjugate-object argument at851-861 positively uses the normalized tuple and the retained polarized equivalence relation. The later theta-height use has the same normalized Igusa coordinates and a weight-zero quotient, so the rescaling conventions agree. No degree, good-prime bound or height constant is changed here.

I also read the final BG statements on737-739 and the completion of Lemma3.1 on740 solely to check the declared source boundary. The quotient and canonical-model statements there are earlier named inputs, distinct from its later product and explicit-conic calculations. Their actual application to the corrected principal datum remains A001-Q-MODULI. This review does not reapprove BG's printed Riemann form, the disputed displayed product map, its abstract product-isomorphism conclusions, or Theorem3.10. It does not retire those inputs from other consumers merely because this normalization can avoid them.

The one application and all nine comparisons are accepted within these stated premises. Exact identities and raw locations are checked separately. No mathematical repair was required. No live source, old packet or manuscript was edited; no whole-source, full A001/B11, inventory or release approval follows.
