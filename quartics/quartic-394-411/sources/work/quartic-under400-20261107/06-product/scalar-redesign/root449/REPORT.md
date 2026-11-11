# Removing the scalar constant branch

This separate extension saves one further coordinate after the positive-contact shift. It takes the frozen 450-variable candidate in the parent directory to 449 variables, 448 witnesses, 426 quadratic residuals, and 6,582 quartic monomials. Content, degree and maximum coefficient remain 1, 4, and 16*3^(2^26). No file in the frozen parent packet is changed.

Source SHA256: `31d5e21d5101f31fd47352dea36dae7eb0faa5498a22cab26ebb62799d9be7e6`.
Candidate SHA256: `02ce0dcbeeba90a52bfba28c6968f09bcd3471c4b76847b57987f72cb6175549`.
Polynomial SHA256: `70bea702b8e5ddef1690ab08ecb29ade8aac46339ee2aeb1c41059ee56bc2a36`.

## Equations

Retain beta=2X^2+2403 and its strictly positive contact product r. Write

    q=Norm(f(H)),
    z(R)/z(H)=z0+z1*sqrt(2),
    B=(z0^2+r*z1^2)/r^64.

The rational number q is nonzero, since f(H) is a nonzero field element. The old root is

    A=1+q^2/r,
    W=A^2+r*B^2.

Replace it by the single reversed norm node

    W=B^2+q^2/r = N_r(B,q/r).

Retain the same pole input b=c*r*W^2, its nonzero condition and all remaining scalar and detector interfaces. This changes the value of b, so it is an arithmetic replacement, not an equality of old and new pole witnesses.

The existing shared norm-square expression is q^2=t^2-8u^2, where t and u are coordinates311 and312. The existing B-square coordinate is541. Thus the single new root row

    r*W=t^2-8u^2+r*B2

is quadratic. Delete A, coordinate536, and its defining row506; replace only the root row512. The retained equation B2=B^2 and every other row remain unchanged. In actual coordinates r is the affine expression

    -99006679260 -82479248*v248 -21050600*v487
    -7629700*v488 -45771136*v489.

Its seemingly negative coefficients reflect the compiler's intermediate coordinate normalization. It is the positive five-contact product in the parent proof, not its negative. The checker verifies its sign and normalization against the old constant-node and root rows.

## Soundness

Let p>76176 be a consumed prime in M5(beta), and normalize its valuation by v_p(p)=1. The unchanged contact calculation says eta=v_p(r) is odd. In fact eta is automatically positive, without a constant leaf. If v_p(beta)>=0, every factor of r is integral, so eta>=0. If v_p(beta)<0, each of beta, beta-1, beta-2401, 32beta+343 and 2beta-1 has valuation v_p(beta), because p is larger than all their fixed coefficient primes. Then eta=5v_p(beta). But v_p(beta)=2v_p(X) is even. That case cannot give odd eta. Therefore eta is a positive odd integer.

The correction c is a p-unit. The unchanged nonzero scalar pole gives

    eta+2v_p(W)>0.

In the new root, the terms B^2 and q^2/r have even and odd valuations respectively, so they cannot cancel. Zero B is harmless under the convention v(0)=infinity; q is nonzero. It follows that

    v_p(q)>eta/4>0,
    v_p(B)>-eta/4.

In B the two numerator terms again have opposite parity. Consequently

    v_p(z0)>(32-1/8)*eta,
    v_p(z1)>(32-5/8)*eta.

Since eta>=1 and the coefficient valuations are integers, both coefficients have valuation at least32. The strict positivity of v_p(q) means that f(H) has positive valuation at some place of K above p. This is immediate at a split prime from the sum of its two valuations, and at an inert prime from the norm valuation formula. At that place H is formal, and the ratio z(R)/z(H) has valuation at least32.

For completeness of the torsion analysis, write E:y^2=x^3-Dx, where p does not divide 2D. The relation z(R)^2=x(R)/(x(R)^2-D) shows that v(z(R))>0 permits two cases. If v(x(R))<0, R is near O and v(z(R))=-v(x(R))/2. If v(x(R))>0, R is near T0=(0,0) and v(z(R))=v(x(R))/2. The case v(x(R))=0 cannot give positive v(z(R)): its denominator is integral. In both permitted cases,

    x(2R)=(x(R)^2+D)^2/[4x(R)(x(R)^2-D)]

has valuation -2v(z(R)), and therefore 2R is formal with v(z(2R))=v(z(R)). Apply the inherited unramified formal logarithm isometry to

    [h](2R)=[2s]H.

Both sides are in the same formal group, and 2 is a p-unit. Hence v_p(s/h)=v(z(2R))-v(z(H))>=32. The nonzero integer h has nonnegative p-valuation, so v_p(s)>=32. This is exactly the conclusion consumed by the scalar height bound. No claim that R itself is formal is made.

Thus M5(beta)^32 divides s and h(beta)<=H*abs(s)^(19/32), with all quantitative height and anchor arguments unchanged from the parent packet and its pinned source. The same formal logarithm theorem is used on the same unramified, positive-depth domain; no stronger theorem is assumed.

## Completeness and the loss of the unit condition

Take an integer X and choose the parent packet's positive correction c, so that cr is positive and square at Q2,Q3,Q17. Set S0 to the finite support of this positive integer. Use the same ordered scalar preparation: choose h0 sufficiently divisible, then choose the positive scalar index s sufficiently divisible relative to h0 and large enough for the anchor. The original six-leaf preparation can make the coefficients of f(H) and z(R)/z(H) attain all of the following bounds simultaneously.

For p dividing r, put eta=v_p(r)>0. Require each coefficient of f(H) to have valuation at least eta and each coefficient of z(R)/z(H) to have valuation at least32eta. Then v_p(q)>=2eta, v_p(q^2/r)>=3eta, and v_p(B)>=0. Hence v_p(W)>=0. At p dividing c but not r, require those coefficients to have positive valuation; again q^2/r, B and W are integral. The norm coefficient2 causes no problem at p=2, since it can only raise these lower bounds. These are finite bounds covered by the same deep formal-subgroup preparation, including its ramified and bad places.

The new W need not be a unit on S0. No unit conclusion is required. For every rational assignment on the stated point domain, r>0 and q^2>0, so

    W=B^2+q^2/r>0.

Thus b=crW^2 is nonzero and positive. At p in S0, its valuation is nonnegative by integrality of W. Outside S0, its valuation is even. Its reduced denominator is therefore a square. Multiplication by the nonzero square W^2 preserves the squareclasses of cr at2,3,17. These are exactly the hypotheses of the existing scalar pole-completeness lemma, so fresh pole witnesses exist. The subsequent factored-pole and preparation-conic transformations in the source require this positive input and retain all their permitted zero branches.

With R fixed, integrality of the finitely many scalar rational functions at the places above S0 persists on a sufficiently small neighborhood of the prepared H. The existing continuity-modulus argument therefore supplies L just as before. Global nonvanishing of W is already guaranteed by positivity. The remaining root choices, height scales, contact-prime selection, primary/opposite CRT and real-progression choice follow in the same order as in the parent packet. No new simultaneous realization assertion is used. In particular, the stronger old statement that W was a unit is replaced at each use by the precise properties actually needed: nonzero, integral at S0, and a square factor in b.

## Verification and source bindings

The sources and conventions are exactly the parent `CONSUMERS.json` bindings, together with the parent candidate hash above. The new obligations are the automatic positivity of odd eta, the two new parity bounds, and replacing the unit-root completeness argument by the integrality argument. The proof above supplies all three. The nonzero q input and doubled-point domains are retained from the same point charts. The torsion and logarithm transition is written out above rather than inferred from a positive z valuation.

`verify.py` imports no producer. It checks the actual r normalization, q-square expression, B-square row, every other residual, deleted-coordinate incidence, fixed parameter, coordinate support and all coefficients of the primitive integer sum of squares. Its pass result is computational evidence for the encoding, not an independent mathematical acceptance.

This extension can be composed with the scalar ratio fusion because it reads only the same rational coefficient norm B. Its dependence on the positive-contact shift is explicit. The five-generator correction proof and this root proof are separately reviewable; no acceptance of either is asserted here.
