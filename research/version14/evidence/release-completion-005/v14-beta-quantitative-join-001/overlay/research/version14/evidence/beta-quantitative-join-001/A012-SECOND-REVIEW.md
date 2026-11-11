# A012 independent second review

Reviewed 2026-11-05 against manuscript SHA256 `a17e021ea3a6b90f861d87aff048f905b1dc31226e3445caf273739f7659e51e`, the A012 section of `parallel-009/galois-height/REPORT.md`, and its proposed `PATCH.diff`.

## Verdict

Accept the A012 replacement. The bound is valid with the manuscript's actual constants U_0=4(DG_0)^2 and E_0=10(DG_0)^2. No missing residue-degree, extension-degree, or [L':Q] factor was found. The replacement correctly identifies the inspected source as Serre's chapter in Cassels–Frohlich, not the uninspected 1979 *Local Fields* book. The direct derivative and subgroup-reindexing proofs in the first review should remain part of the recorded evidence, because the short replacement citation alone does not spell out those calculations.

No required mathematical correction to the patch was found. Below are the independent checks and the precise retained premises.

## Source identity and conventions

I independently inspected the rendered chapter title and printed pp.155–159 of `work/independent-height-review-20261104/conductor/primary/serre-local-cft.pdf`. SHA256 was recomputed as `e0367b25a022eb27ec220e3c15b474a94fb96d70a6bb89b77f4a02c2231950fe`. The title page is Chapter VI, *Local Class Field Theory*, J.-P. Serre. The chapter's own contents starts at p.128, with Section 4.1 on p.155, Section 4.2 on p.157, and Section 4.3 on p.158. It is an extract, not the full Cassels–Frohlich volume.

On p.155, lower ramification uses i_G(s)=v_L(s(x)-x) and s in G_u exactly when i_G(s)>=u+1. For nonintegral positive u the Herbrand derivative is phi'(u)=1/(G_0:G_u)=|G_u|/|G_0|. Upper numbering is G^v=G_u with v=phi(u). The same page states quotient compatibility (G/H)^v=image(G^v), allowing passage to infinite extensions. Its Theorem 1 identifies local reciprocity images of U_K^v with G^v for abelian extensions. The unit filtration convention is U_K^v=U_K^n when n-1<v<=n.

Section 4.2 Proposition 1, p.157, identifies the conductor with last upper break plus one. Section 4.3, p.158, defines the Artin conductor by the weighted lower-group codimensions, with weight |G_i|/|G_0|. These are exactly the conventions used by the proposed replacement.

## Normal closure and derivative estimate

Let K'/Q_p have degree n<=a. Its normal closure M has Galois group acting faithfully on the n embeddings, so [M:Q_p]<=n!<=a!. This factorial bound is legitimate even though the extension originally giving semistability need not be normal. No assertion that its normal closure has degree only a is used.

Let e=e(M/Q_p) and let M_0 be the maximal unramified subfield. Then M/M_0 is totally ramified Galois of degree e. A uniformizer pi generates O_M over O_(M_0) and has Eisenstein polynomial

`f(X)=X^e+b_(e-1)X^(e-1)+...+b_0`.

For every nonzero derivative term i b_i pi^(i-1), including the leading term e pi^(e-1), its valuation is congruent to i-1 modulo e: coefficients from M_0 have valuations in eZ. The residues are distinct for i=1,...,e. Consequently the least valuation among nonzero terms is attained once, so cancellation cannot increase it. Taking the leading term as an upper bound gives

`d=v_M(f'(pi)) <= e-1+e v_p(e)`.

This argument does not assume that e is prime to p. The unramified base M_0/Q_p ensures v_(M_0)(e)=v_p(e). The case e=1 gives d=0 directly.

Because M/M_0 is Galois,

`f'(pi)=product_(sigma in I, sigma!=1)(pi-sigma(pi))`.

Counting the integer valuations v_M(pi-sigma pi) by the stated lower-group definition gives

`d=sum_(i>=0)(|G_i|-1)`.

Thus the formula needed here is proved without silently importing a missing different theorem. If d is called the different exponent, that agrees with the usual monogenic formula, but this identification is not needed for the bound itself.

## Change to upper numbering and the constant

Separate i=0 and integrate the positive lower intervals. The exact formula is

`d/e = 1-1/e + integral_(u>0)(1-1/|G^u|) du`.

Here e=|G_0| is the ramification index, not the total degree. On the interval from zero to the last positive upper break b, G^u is nontrivial apart from irrelevant endpoints, so 1-1/|G^u|>=1/2. Therefore

`b <= 2d/e <= 2(1+v_p(e)) <= 2(1+log_2(a!)) <= 4a^2`.

For a>=2, log_2(a!)<=a log_2(a)<=a^2 and 1+a^2<=2a^2. For a=1 there is no positive break. Unramified and tame extensions also have no positive break. The replacement's 4a^2 is therefore a safe bound, with no residue-degree factor omitted.

## Subgroups: the inverse Herbrand function is in the correct direction

For a finite Galois tower M/F/K, let G=Gal(M/K), H=Gal(M/F), Q=Gal(F/K). The lower-group equality is H_t=H cap G_t. Quotient compatibility gives

`|Q^(phi_G(t))| = |G_t|/|H_t|`, and `|Q_0|=|G_0|/|H_0|`.

Away from breaks,

`d/dt [psi_Q(phi_G(t))] = (|Q_0|/|Q^(phi_G(t))|)(|G_t|/|G_0|) = |H_t|/|H_0|`.

Both sides vanish at t=0, hence phi_H=psi_Q composed with phi_G. It follows that

`H cap G^u = H^(psi_Q(u))`.

Passage through finite Galois quotients gives the absolute formula in the manuscript. Since psi_Q'(u) is an index, it is at least one for u>=0, and psi_Q(u)>=u. Replacing psi by phi in that displayed subgroup formula would be wrong; the manuscript uses psi correctly.

In the beta argument F=L_v is Galois over Q_p because L/Q is Galois. In the semistability argument one can first take the normal closure of the torsion extension. Semistability is preserved under further finite extension. Thus the proof does not use a Galois quotient formula for a non-Galois extension.

## Wild inertia and the actual descended representation

The torsion extension F(A[3])/Q_p, or F(A[5]) when p=3, has degree at most DG_0. Here G_0=|GL_4(F_5)|=116064000000 also dominates |GL_4(F_3)|=24261120. This consumes the separate degree bound on F and the stated semistability criterion.

After passing to its normal closure M, semistability makes inertia act unipotently on V_l(A) for l!=p. Its wild inertia action is trivial. A precise justification is to choose a stable l-adic lattice. The kernel of reduction is pro-l, so the pro-p wild image has trivial intersection with it and is finite. Every element of this finite image is unipotent in characteristic zero, hence has to be the identity. This avoids relying on an unspecified 'unipotent subgroup' being pro-l.

For absolute upper u>4(DG_0)^2, quotient compatibility makes G_(Q_p)^u lie in G_M. Such a positive ramification group is pro-p and lies in wild inertia of M, equivalently its relative upper index is positive by the subgroup formula. It therefore acts trivially on V_l(A). It also lies in G_L. On G_L the finite choice mu_sigma is mu_1=1 and a_sigma=a_1=1. Consequently the only remaining factor in rho_l is beta^(-1), exactly as the manuscript states. Triviality of rho_l gives triviality of its summand r_l; no extra multiplicity factor is introduced here.

## Beta at odd primes and at two

The input is an actual character beta|G_F satisfying beta^2=chi|G_F, where chi is the chosen Dirichlet character. At odd p, chi is tame. Its pullback remains trivial on the pro-p wild inertia of F. Thus beta has order dividing two there, and a pro-p group for odd p has no nontrivial quotient of order two.

At p=2, the non-2 Dirichlet factors of chi are unramified locally and trivial on Q_2-units. Its possible 2-primary factor is the character modulo four and has order at most two. Local reciprocity gives the restriction rule via N_(F/Q_2):F^*->Q_2^*. Norms of units are units. Therefore beta^4=chi^2=1 on O_F^*. There is no factor of [F:Q_2] in this exponent assertion: it is a composition with a norm, and the target unit character already has order at most two.

Put e=v_F(2). On the ideal p_F^(e+1), every nonlinear logarithm or exponential term has strictly larger valuation than the linear term. For example v_F(x^n/n)>=n(e+1)-e v_2(n)>e+1 for n>=2, and the analogous estimate uses v_2(n!)<=n-1. Hence log and exp are inverse isometries between U_F^(e+1) and p_F^(e+1). Multiplication by four maps that ideal onto p_F^(3e+1). Therefore

`(U_F^(e+1))^4 = U_F^(3e+1)`.

Since beta has exponent dividing four on units, it is trivial on U_F^(3e+1). The source's reciprocity and conductor conventions give conductor exponent <=3e+1 and last relative upper break <=3e. The strict condition u>3e in the manuscript is correct.

The normal-closure bound gives last upper break of F/Q_2 at most 4D^2. For absolute u>max(4D^2,3e), the group lies in G_F and its relative upper index is psi_(F/Q_2)(u)>=u>3e. Beta is consequently trivial there. Since e<=D and G_0>=1,

`max(4D^2,3e) <= 4(DG_0)^2 = U_0`.

This argument consumes the construction of beta and norm compatibility, but it does not consume the potentially much larger degree of its kernel field L'.

## Final conductor bound and retained premises

The tame codimension of the two-dimensional r_l is at most two. Its wild image is finite, and its positive-upper codimension is at most two and vanishes for u>U_0. Changing the source's lower-group Artin sum to upper numbering gives Swan(r_l)<=2U_0. Possible infinite tame unipotent monodromy affects the tame invariant codimension, not this wild integral. Thus

`a_p(r_l) <= 2+2U_0 = 2+8(DG_0)^2 <= 10(DG_0)^2 = E_0`.

The last inequality needs only DG_0>=1. There is no factor [L':Q] or unramified residue degree. At p=5 one uses r_3; at all other p one can use r_5, so the auxiliary coefficient prime is always distinct from p as required by the wild-inertia argument.

The second review accepts the local calculation and the replacement bibliography. It retains, rather than re-proves, the construction of A and L, the semistability-after-torsion input, the beta splitting and norm reciprocity, the compatible r_3/r_5 realization, and the good-reduction assertion used in the separate p>R improvement. Those dependencies are not consequences of Serre's ramification chapter.
