# Prime-five auxiliary cohomology and element selection

This versioned project proof supplies connecting arguments for Pan's author-version §§4.3.5 and 4.3.8–4.3.11 at the actual auxiliary prime five. Its exact source and review bindings are in SOURCES.json and REVIEW-SCOPES.json. This assembled proof is newly authored and requires its own independent review. Supporting files preserve the exact earlier authored texts; the controlling choices and boundaries of this version are stated here.

## 1. Domain and imported premises

Let F be a totally real number field in which five splits completely. Let k be a finite field of characteristic five, A=k[[T]], and K=k((T)). Let r:G_(F,P)→GL₂(A) be the continuous lattice representation attached to Pan's nice prime. Its K-representation is irreducible, its determinant is the finite-order odd residual character bar-chi, and its residual representation is a nonsplit extension with semisimplification 1⊕bar-chi. The finite set P contains the ramified primes and those above five. Put M=ad⁰(r)(1), with the T-adic topology. The twist on this characteristic-five module is the mod-five cyclotomic character. Let N be the common kernel of r and the full five-adic cyclotomic character, and Gamma=G_(F,P)/N. Write H=G_(F(zeta_(5^infinity))); use its image in G_(F,P) where necessary.

These are the auxiliary characteristic-five objects, not the characteristic-zero multiplicity representation used in the manuscript's modularity application. Retain the following explicit premises.

* Pan's actual nice-prime lattice, irreducibility and number-field reduction have been constructed. This proof does not construct a new Hecke point or impose a new restriction on that point.
* The continuous global module C=H¹(G_(F,P),M) is finitely generated over A, as used by Pan §4.3.9. This arithmetic finiteness input is retained, not proved here.
* In the geometrically non-dihedral case, use the final published Skinner–Wiles §6.1–6.6 and Lemma6.9 argument under the transferred representation inputs described in Section3 below. The published measure and finite-index cohomology argument remains an imported proof. It is not replaced by a claim that every cohomology group of a compact group is uniformly finite.
* Cohomology is continuous cohomology. For a compact lattice M=lim M/TⁿM, its degree-one comparison has the usual derived-limit term from degree-zero cohomology. The finite H⁰ terms satisfy Mittag–Leffler, so that term vanishes. The continuous Hochschild–Serre inflation map is used with a kernel acting trivially on M. These compact-cohomology facts are the exact interface being used.

Only the first three standing representation conditions above enter the following geometric dichotomy. An inducing character is allowed to become visible after a finite coefficient extension; this interpretation is essential.

## 2. Geometric dichotomy on the same point

Oddness gives a K-rational involution with distinct eigenvalues +1 and -1. Any invariant line over an algebraic closure is one of its two rational eigenlines, hence descends. The assumed K-irreducibility therefore gives absolute irreducibility.

The trace pairing on sl₂ has Gram determinant -2 and is nondegenerate. If its adjoint representation has a proper invariant subspace, it has an invariant line, by taking an orthogonal complement when needed. A nonzero nilpotent generator of that line would give an invariant line of the original two-dimensional representation. A generator with nonzero determinant transforms under a quadratic character; if that character were trivial, absolute irreducibility would make it scalar and trace zero would make it zero. Otherwise its two eigenspaces are preserved by the quadratic kernel and exchanged by the other coset. Thus r is geometrically induced from that quadratic subgroup. This is the dichotomy used throughout this proof.

In the geometric dihedral case, let L/F be the quadratic inducing field. On its nontrivial coset tr(r(g))=0. Reduction of the original lattice trace gives 1+bar-chi(g)=0 on that entire coset. Multiplication by a fixed coset representative then gives bar-chi(h)=1 for h∈G_L. Therefore L=F(bar-chi), without assuming that an inducing character was K-valued. Oddness makes L totally imaginary.

Complete splitting of five in F and total ramification of Q(zeta₅)/Q at five give F∩Q(zeta₅)=Q. Its cyclic order-four Galois group has the unique quadratic subfield Q(sqrt5). Thus the unique quadratic subfield of F(zeta₅)/F is totally real F(sqrt5), and differs from L. Consequently L∩F(zeta₅)=F. This proves the required geometric disjointness for the already constructed point; it is not a strengthened hypothesis that must be met by a new point construction.

For the full coefficient and field argument, including the finite extension which names the inducing lines, see [the geometric proof](support/geometric-p5.md). In particular its rotation image is an abelian pro-five group, the other coset acts by inversion, and squaring is an automorphism of the rotation image. The image's only possible nontrivial abelian quotient is therefore the quadratic one. Any quadratic subextension of the five-power cyclotomic tower lies in its first layer. If E is the fixed field of ker(r), it follows that E∩F(zeta_(5^infinity))=F.

This gives Gamma as the direct product of the representation image and the cyclotomic image. Choose a central element z in the latter factor with omega(z)≠1. On M it acts by the scalar omega(z), whose difference from one is a unit in A. For a continuous cocycle f the equality zg=gz gives

`(omega(z)-1) f(g)=(g-1) f(z)`.

It follows that f is a coboundary over the original A-lattice. Thus H¹(Gamma,M)=0 in the geometric dihedral case. The same scalar kills finite-level invariants of M/TⁿM for every n.

## 3. Non-dihedral Skinner–Wiles transfer and compact conclusion

In the geometrically non-dihedral branch the adjoint is irreducible by Section2. This replaces the older local infinite-order ordinary hypothesis at the exact place it is used to establish the representation lemmas; that local hypothesis is not asserted for Pan's point.

The [original transfer](support/transfer-original.md), in its sections on the subsequent representation lemmas and the full6.9 argument, retains the odd determinant, residual extension, pro-five subgroup after killing the determinant, and the order-two quotient. Its finite-index argument supplies adjoint irreducibility on the fixed subgroups used by SW6.5–6.6. Compactness of the primitive vectors of the lattice gives a spanning exponent uniform for each fixed representation and fixed subgroup. The SW6.9 proof then supplies one T-power annihilator of H¹(Gamma,M/TⁿM), independent of n and of the cocycle.

Two clarifications control the use of that supporting text. Its historical C1 coefficient-convention reservation is resolved for this p5 domain by Section2, not by an unsupported convention change. Its phrase “a nonzero off-diagonal entry” is superseded by the exact condition that both entries b_tau and c_tau are nonzero. The [uniformity note](support/sw69-uniformity.md) explains this condition and the discriminant bound on the closure of the positive-measure set. The trace used to define H_M is tr(r(h)), while the discriminant after the limiting map equals its square. The fixed discriminant valuation excludes finite-order eigenvalues throughout the relevant closure. For the selected tau, a power multiplies both off-diagonal entries by the same nonzero factor `(beta^s-beta^(-s))/(beta-beta^(-1))`. The measure sets and resulting finite-index subgroup are selected from r, independently of n and the cocycle. The exact independent scope for this supplementary note is recorded separately; it must not be inferred from review of the geometric argument alone.

Pan's trace pairing followed by extraction of the T^(n−1) coefficient identifies the finite dual with M/TⁿM. It uses twist +1. The finite degree-zero cohomology groups remove the possible derived-limit obstruction, so the same T-power annihilates H¹(Gamma,M). Inflation injects it into C because N acts trivially on M. Since C is finitely generated over the Noetherian DVR A, its submodule is finitely generated. A finitely generated module killed by a T-power has finite length. This proves the exact conclusion needed from Pan4.3.11, conditional on the stated published SW proof and arithmetic finite-generation premises. An annihilator alone would not imply finite length.

## 4. The p52 distinct-eigenvalue element

Use [the elementary eigenvalue proof](support/eigenvalue-p5.md) for this step. This choice supersedes the alternative appeal to transferred SW6.3(i) in the geometric supporting file's paragraph about the non-dihedral p52 occurrence; it does not remove SW6.3 from the SW6.9 proof itself.

For clarity, the argument applies to the same r and H of Section1. If all r(H) had repeated eigenvalues, every nonidentity projective image would be unipotent. Two unipotents with different fixed lines can be normalized as I+A and I+B with opposite nonzero off-diagonal entries a,b. The five products (I+tA)(I+B), t∈F5, have determinant1 and distinct traces2+tab. At most two have repeated eigenvalues, a contradiction. Thus a nontrivial projective H image has a unique common fixed line. Normality of H makes that line G_F-invariant, contradicting absolute irreducibility.

If the projective H image is trivial, it factors continuously through Gal(F(zeta_(5^infinity))/F)=Z_5^×. Complete splitting gives this equality by the same total-ramification intersection argument at every finite layer. This group is procyclic. An eigenline of a lift of a topological generator, over a finite extension of K, has closed stabilizer. Density of its powers makes it invariant under the whole projective image, again a contradiction. Therefore there is sigma_0∈H with nonzero discriminant under r. No eigenvalue is treated as a new A-coordinate.

## 5. The p53 choices and the actual cocycle connection

In the geometric dihedral case Section2 shows that H surjects onto im(r). Over a finite coefficient extension the adjoint decomposes into its diagonal quadratic line D and its off-diagonal irreducible two-dimensional constituent U. The latter is irreducible: equality of its two inducing characters would give theta⁴=1, impossible for a nontrivial character with pro-five image. A nontrivial rotation has distinct eigenvalues theta,theta^(-1) and adjoint fixed line D. A reflection has trace0, determinant−1 and eigenvalues+1,−1; its adjoint fixed line lies in U. Surjectivity gives elements of the original H realizing both choices. This is stronger than the existence of just one distinct-eigenvalue element, and is the actual p53 requirement.

Here is the connection to Pan4.3.10's cocycle statement, making the object identity explicit. Let a nonzero non-torsion class [phi]∈C be given. By Section3 or Section2, H¹(Gamma,M) is torsion, so restriction to N cannot vanish. Since N acts trivially on M, phi|N is an actual homomorphism. Its K-span B inside M_K is a nonzero Gamma-subrepresentation.

In the non-dihedral branch B=M_K by adjoint irreducibility. Choose sigma_0 by Section4. In the dihedral branch B contains at least one of the simple constituents D,U; choose the corresponding sigma_0 just described. In either case the projection of B to the rank-one quotient

`Q_sigma = M_K/(sigma_0-1)M_K`

is nonzero. Indeed sigma_0 has distinct eigenvalues on the two-dimensional representation and trivial cyclotomic twist, so its adjoint is semisimple and its one-dimensional invariant subspace maps isomorphically to this quotient. The chosen B contains that invariant subspace in the dihedral branch.

There is tau∈N with phi(sigma_0)+phi(tau) nonzero in Q_sigma. If this failed for every tau, taking tau=1 would first make phi(sigma_0) zero in the quotient, and then all phi(N) would map to zero, contrary to the preceding projection statement. Set sigma=sigma_0 tau. Because tau∈N, sigma has the same r-image and cyclotomic value as sigma_0. The cocycle identity gives

`phi(sigma)=phi(sigma_0)+sigma_0 phi(tau)`.

Modulo (sigma_0−1)M_K this is phi(sigma_0)+phi(tau), which is nonzero. Thus M/((sigma−1)M+A phi(sigma)) is a finitely generated torsion A-module and has finite length. This is the exact finite-length conclusion of the element-selection step. It uses the same class, lattice and group element throughout. Evaluation is well-defined on cohomology classes because a coboundary evaluates into (sigma−1)M.

## 6. Related uses and finite coefficient descent

For §4.3.5, the geometric dihedral central scalar already kills all finite-level invariants. Otherwise M_K is an irreducible three-dimensional representation and has no invariants. Finitely many group elements give a combined action-difference matrix injective over K. A nonzero maximal minor of valuation d implies, by its adjugate, that its kernel modulo Tⁿ is killed by T^d. That kernel is a submodule of (A/Tⁿ)^3 and has length at most3d. The bound is independent of n for the fixed representation.

For §4.3.8, let r_C=dim_K(C⊗K). This is exactly Pan's r=dim_K H¹(G_F,P,M_K). To check the identification, every continuous cochain on the compact profinite space G_F,P^n with values in the finite-dimensional K-space M_K has compact, hence bounded, image. A power of T therefore carries its whole image into the fixed lattice M. Thus the continuous cochain complex with coefficients M_K is the localization at T of the complex with coefficients M, degree by degree and with the same differentials. Localization is exact, so it commutes with kernels, images and cohomology. Consequently C⊗_A K=H¹(G_F,P,M_K), with its natural map, and the two ranks agree. The denominator may depend on the cochain; no uniform bound over all cochains is needed.

Section5 gives an evaluation functional nonzero on each nonzero vector of C⊗K, after clearing a denominator and choosing a non-torsion integral class. Each quotient Q_sigma has dimension one. Their kernels have zero intersection. Successively choosing a functional nonzero on the current nonzero common kernel yields r_C evaluations with zero common kernel. The resulting map between K-vector spaces of dimension r_C is an isomorphism. Over A both source C and the selected integral coinvariant quotients are finitely generated of the same rank; consequently kernel and cokernel have finite length. If r_C=0, take the empty tuple of evaluations. The target is zero, C is finitely generated torsion over A and therefore has finite length, and the kernel and cokernel conclusions still hold.

A finite extension K'/K used to name dihedral constituents preserves all these ranks. Its integral closure A' is a finite free faithfully flat DVR over A. Continuous cochains with finite free coefficient base change commute with that base change, by choosing an A-basis of A'. Torsion and zero conclusions descend. A discriminant is already `(tr r(sigma))²−4det r(sigma)` in A; no chosen square root changes its valuation or its nonvanishing. Thus the selected elements and the rank statements refer to the original coefficient ring.

The source's later §4.3.9 approximation by Frobenius elements, Chebotarev input, local/global duality in §4.3.4 and subsequent patching are not proved here. The point-construction occurrences in §§5–7 retain their own pro-modularity, dimension, local-triviality and base-change obligations. The geometric p5 argument adds no new condition for those constructions, since their stated Section4 target domain already supplies total reality and complete splitting. Generic odd primes, final Pan version matching, SW01 corrections and the full modularity proof are outside this proof's conclusion.
