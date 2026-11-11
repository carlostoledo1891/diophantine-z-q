# Six original J1 height applications

Reviewer /root; source-application author /root/v14_gi_constructors. 2026-11-09T08:47:19.301Z.

Decision: accept the six bounded applications in manifest be18a265ffd1cd8983069fc559f5e8fff7ad34e0ba954636d9e4aa54836b3c74, with the explicit incoming premises recorded below. No manuscript repair is required for these six implications. This is internal review, not acceptance of the entire height proof or source inventory.

## Reading and reuse

Read current main lines8470–8548 and10047–10103. Read the complete earlier exponent19 review, including its same-field Hom descent, effective quotient correction, general source statements and isogeny direction. Read the actual published-Poincare application review with its proof explanation and ground-field conventions. Its Milne1986 final-version check is reused, not claimed freshly repeated here. The present review compares the general source results with the earlier J1(N) consumer rather than treating the specialized J_H conclusion as an available theorem for J1(N).

For direct source checks in this review, read Gaudron–Remond2023 published pages7–8, vonKanel2021 published page5, Javanpeykar2014 published pages89–90 and97–98, the Faltings1983 Hom corollary on361, the displayed Lemma5 on358 in its retained page image, and Faltings1984 erratum381. SOURCE-PINS.json records exact files. The erratum corrects the stationarity claim in Satz2, not the Hom corollary or the single-isogeny variation formula consumed here. No claim of a new proof of those published theorems is made.

## Hom and complement

The current caller supplies the same number field Lprime, semisimple rational Tate modules of A and J, and a common irreducible constituent after a finite coefficient extension. These are required incoming facts. Semisimplicity gives a nonzero equivariant map. The invariant subspace of the finite-dimensional Hom space is the intersection of kernels of linear operators; a finite subcollection has the same intersection. Thus extending coefficients commutes with that invariant space. Nonzero after faithful scalar extension implies nonzero before extension. Faltings' rational Hom comparison over Lprime then yields a nonzero Lprime-homomorphism A to J after clearing denominators.

Given the separate absolute-simplicity premise for the original dimension-two A, its image B is an abelian subvariety isogenous to A. Apply the ground-field Poincare complement construction to B inside J. Addition gives B times Z to J, and composition gives A times Z to J over Lprime. Hence g=dimJ>=2. No new field, degree estimate, principal polarization of A or Z, or identification of an unrelated factor is introduced.

## Belyi height

Javanpeykar's Theorem1.1.1 applies to the smooth projective connected curve over the algebraic closure, with positive genus. Section2.3 identifies its hFal with the stable height of its Jacobian. The caller's separate bounds g<=N²/24 and deg_B<=N² give hF(J)<=13000000*g*N^10<=13000000*N^12. The theorem itself supplies no extra coefficient-degree term, squarefree-level condition or trivial-character restriction. The genus/Belyi bounds remain distinct incoming source applications and are not certified by this six-row review.

## Quantitative isogeny direction and normalization

Gaudron–Remond define Xi(B)=((7g)^(8g²)*[K:Q]*max(1,log[K:Q],hF(B)))^(2g²) in the original stable Faltings normalization. Their Theorem1.9(1) gives both directions of an isogeny between isogenous varieties with bound Xi(B)^2. Take their K and their extension both to be the current Lprime, take B in this formula to be J, and use A times Z as the target. The preliminary opposite-direction isogeny establishes isogeny but is not used as a bounded map. One half of log(Xi(J)^2) equals

2g²*(8g²*log(7g)+log(dprime)+log(max(1,log(dprime),hF(J)))),

which is exactly V at main8515–8516. The general theorem is used without its optional MM improvement and without replacing it by a different GR2014 special case.

Faltings' Lemma5 has target height equal to source height plus half-log-degree minus a nonnegative finite term. After passing to a common semistable field and using stable-height invariance, its needed one-sided consequence remains hF(target)<=hF(source)+half-log-degree. Product additivity gives hF(A)+hF(Z)<=hF(J)+V for this same J-to-A-times-Z map.

## Lower bound and scope

The published equation2.2 is hF(Z)>=-dim(Z)/2*log(2*pi²), in the same original metric, and the source explicitly sets hF(0)=0. Since log(2*pi²)<3 and dimZ=g-2, this implies hF(Z)>-3g/2, including dimZ=0. Thus the exact lower-bound application is valid.

Accepted row IDs are listed in REVIEW.json. The actual common constituent, modular realization, sign splitting, Lprime degree, absolute simplicity, genus/Belyi estimates, conductor bound and the later elementary LT4–LT7 inequalities are outside this bounded review. Its R^24 consumer is kept distinct from the later R^19 argument. The review accepts the connections to already established general published results; it does not close those incoming construction obligations by assumption.
