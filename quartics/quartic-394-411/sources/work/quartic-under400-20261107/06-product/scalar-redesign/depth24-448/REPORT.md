# Scalar depth twenty-four with five powers

This extension saves one more coordinate by reducing the scalar contact power chain from six coordinates to five. It has 448 total variables, 447 witnesses, 425 quadratic residuals and 6,542 quartic monomials. Its degree is four, content is one, and maximum coefficient remains 16*3^(2^26), with the same C=3^(2^25).

The source is the separate root449 candidate, SHA256 `02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549`. The new candidate SHA256 is `e9d6622ef87381ed2f735e849aa537ac178ccc30ec1675f32cee0be38b435609`; its polynomial SHA256 is `66fd7f2f24ce1ea54103069bb82f922c06035a3d246a5fb35a14979d3a9538c6`. The older450 and449 packets remain unchanged. This is an author proposal requiring non-author mathematical review.

## New equations and exact meanings

Use the parent packet's beta=2X^2+2403 and positive contact polynomial

    r=beta*(beta-1)*(beta-2401)*(32beta+343)*(2beta-1)>0.

Keep its five-coordinate positive correction c, supported at primes at most17 and chosen simultaneously to make cr square at2,3,17 for every integral X. Put

    q=Norm(f(H)),  z(R)/z(H)=z0+z1*sqrt(2).

Keep only the powers r2,r4,r8,r16,r32. Change the scalar nodes to

    r32*B = z0^2+r*z1^2,
    Q=q^2,
    r32*W = B^2+r*Q.

The scalar pole input remains b=c*r*W^2, with its nonzero condition and existing private pole implementation. Thus

    B=(z0^2+r*z1^2)/r^32,
    W=(B^2+r*q^2)/r^32.

The quantity q is nonzero, and r>0, so W>0 for every rational solution on the existing point domain. There is no new exceptional division locus.

These equations are quadratic in actual coordinates. The old B-square slot541 becomes Q and is defined by Q=t^2-8u^2 using the existing shared coordinates t=311 and u=312. The B slot is540, W is542, and r32 is604. Delete only coordinate605 and its r64 defining equation. The original affine expression for r is unchanged. The three replacement rows are

    v604*v540 = v508^2+r*v539,
    v541 = v311^2-8*v312^2,
    v604*v542 = v540^2+r*v541.

The existing row v539=v509^2 is retained. Thus the old B-square coordinate is reused rather than supplemented. Incidence checks verify that no other row reads the former meaning of541 and no other row consumes605. This is not a rational equivalence of old scalar witnesses: the scalar test depth, root W and pole input value change, while the arithmetic conclusion needed downstream remains sufficient.

## Local soundness at every consumed prime

Let p>76176 belong to M5(beta). The existing five-contact calculation gives odd eta=v_p(r). If v_p(beta)>=0, then eta>=0. If v_p(beta)<0, all five factors have that valuation, so eta=5v_p(beta)=10v_p(X), which is even. Therefore the odd eta is positive.

The correction is a p-unit, and the existing nonzero pole obstruction gives

    eta+2v_p(W)>0.

In B^2+r*q^2 the two nonzero summands have opposite valuation parity. Hence

    v_p(W)=min(2v_p(B),eta+2v_p(q))-32eta.

The same formula applies when B=0 by assigning infinite valuation to its term. The pole inequality therefore implies

    v_p(B)>(63/4)eta,
    v_p(q)>(61/4)eta>0.

The numerator of B also has opposite valuation parity in its two summands. Using B=(z0^2+r*z1^2)/r^32 gives

    v_p(z0)>(191/8)eta,
    v_p(z1)>(187/8)eta.

Both rational coefficient valuations are therefore at least24. The positive norm valuation v_p(q) supplies a place of K=Q(sqrt(2)) above p where f(H) has positive valuation. At that place H is formal. Both ratio coefficients have depth24, so v(z(R))-v(z(H))>=24 and v(z(R))>0.

This last assertion does not by itself make R formal. As in the fully written argument in root449/REPORT.md, the only possibilities are the formal branch at O and the branch at T0=(0,0). For p not dividing2D, the identities

    z(R)^2=x(R)/(x(R)^2-D),
    x(2R)=(x(R)^2+D)^2/[4x(R)(x(R)^2-D)]

show in either branch that 2R is formal and v(z(2R))=v(z(R)). The case v(x(R))=0 cannot give v(z(R))>0. Apply the same unramified formal logarithm isometry to [h](2R)=[2s]H. It gives v_p(s/h)>=24, and therefore v_p(s)>=24 because h is a nonzero integer. All denominators and points have the same domains as in the accepted scalar construction. In particular no new claim about a point near a nonzero two-torsion point is used.

Consequently

    M5(beta)^24 divides s,
    h(beta)<=H*abs(s)^(19/24),

using the same exponent-nineteen contact-height theorem. The theorem is applied to exactly the same beta and five-contact radical; only the proved divisibility exponent changes.

## The existing anchor is more than sufficient

Write kappa=abs(s). The retained physical anchor supplies

    log2(kappa)>25,165,823.5,
    H<2^2,093,966.

Since

    (5/24)*25,165,823.5 > 2,093,966+7 > log2(80H),

we have kappa^(5/24)>80H. The new scalar bound therefore gives

    h(beta)<=H*kappa^(19/24)<kappa/80<=abs(a)/40.

Here a=s+1 and kappa>=2, so abs(a)>=kappa/2. The other required estimate, log(48H)<abs(a)/40, follows from the unchanged anchor exactly as in the accepted order-ten proof. Its existing stronger bound kappa>(80H)^10 is unchanged; no new fixed coefficient or anchor coordinate is introduced.

All three Lucas-label tests still have order40. The product-height estimate and Lucas contradiction therefore still give F=0 and log(Bmax)>abs(a)-3. The input comparison remains order10, so for a hypothetical nonzero numerator of n-beta the same argument gives

    log(Bmax)<10log(48H)+19h(beta)<29abs(a)/40<abs(a)-3.

This contradiction still proves n=beta. Finally beta=2X^2+2403 integral implies X integral by the unchanged coefficient2 denominator argument. Thus depth24 suffices for the exact integer projection despite being weaker than the old scalar depth32.

## Simultaneous completeness

Fix an integer X and choose the single positive finite correction c from the parent450 proof. Let S0 be the finite support of the positive integer cr. The scalar preparation theorem permits arbitrary finite lower bounds at the places over S0, including ramified and bad places; it first chooses H0=[h0]P sufficiently deep and then R=[s]P sufficiently deep relative to H0. Retain all divisibility requirements on h0 and s and the same physical anchor.

At a prime p dividing r put eta=v_p(r)>0. It is sufficient to require every rational coefficient of f(H0) to have valuation at least8eta and every coefficient of z(R)/z(H0) to have valuation at least24eta. Then

    v_p(q)>=16eta,
    v_p(B)>=16eta,
    v_p(B^2)>=32eta,
    v_p(r*q^2)>=33eta.

It follows that v_p(W)>=0. At a prime dividing c but not r, require positive valuations of the same coefficients; r32 is then a unit, and W is again integral. These are finite bounds allowed by the existing preparation; no density, genericity or independent-prime assumption is added.

The new root W is positive and nonzero globally. At S0, b=crW^2 has nonnegative valuation; outside S0 its valuation is even. Thus its reduced denominator is a square. It is positive and has the same local squareclasses as cr at2,3,17. These are precisely the hypotheses of the existing scalar pole-completeness lemma. It supplies fresh pole witnesses, after which the already accepted private pole transformations apply with a positive semantic input.

The new scalar expressions are rational functions of H with nonzero denominators at the prepared point. Their finitely many integrality bounds persist on a sufficiently small neighborhood. Choose the continuity modulus L after this preparation, before the contact-prime selection. The remaining roots, height scales, primary/opposite reduction orders, simultaneous CRT and real-progression selection proceed in the same order as in the parent proof. The deeper preparatory condition on H0 only enlarges the fixed modulus. The existing prime-selection theorem permits precisely this fixed finite data. No assertion of preserving old pole witness values or a unit value of W is needed.

## Evidence and source application boundaries

The source references, versions, exact manuscript hashes and original application locators are pinned in the parent `CONSUMERS.json`. The unchanged source453 order-ten proof is pinned there as well. The changed application is the scalar contact-height theorem: its input is now the proved M5(beta)^24 divisibility, and the displayed anchor calculation verifies the precise bound its next consumer needs. The formal-log application keeps the same unramified field, valuation normalization, positive-depth hypothesis and doubled-R comparison map. The pole-completeness application receives the same three local-square hypotheses, positivity and square reduced denominator, all checked above.

`verify.py` independently checks all three replacement rows, deleted and repurposed-coordinate consumers, every unchanged row, the exact rational anchor-margin inequality, and every final quartic coefficient. It imports no producer. The finite result does not substitute for review of the arithmetic change. The candidate and proof are frozen for that review; no released manuscript is changed.
