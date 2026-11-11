# Classical modularity in the solvable-image exits

Author: /root. Proposed connection, awaiting independent review.

## 1. Exact output and selected published input

Let p be odd. Let r: G_Q -> GL_2(F) be continuous, odd and absolutely irreducible over a finite field F of characteristic p. Assume its image is solvable. We prove that, after a finite coefficient extension, an actual stable lattice in the representation of a classical normalized cuspidal newform of weight at least two reduces to r. The level and weight need not be optimal. In particular this supplies the irreducible branch of the modularity convention on final early Khare–Wintenberger printed 230. It does not assert modularity of an arbitrary characteristic-zero lift of r.

The selected Moon–Taguchi input is the intermediate assertion in the proof of Theorem 4 on final printed 648: an odd irreducible characteristic-zero Artin lift of r exists and comes from a classical weight-one form. Its image remains finite and solvable. The subsequent Edixhoven refinement is not used here. The bibliography's reference [7] is listed as in preparation, but the selected intermediate argument is printed in the article and names Fong–Swan and Langlands–Tunnell as its suppliers. Those published ancestors remain explicit. This connection does not reprove them or assert the correctness of every other statement in that article. No GRH input is used.

All algebraic coefficients are realized using the prescribed characteristic-zero and residue embeddings. Fong–Swan lifts the given finite-image representation, allowing finite residue extension. Choose its place over p compatibly with the original embedding F -> F_p-bar and extend this place when enlarging coefficient fields. The corresponding complex Artin representation and classical form are taken with these choices. No unrelated residual representation or separately chosen characteristic-zero lift is substituted.

## 2. An integral cuspidal vector

Write f for the classical weight-one cuspidal eigenform supplied by that Artin input, of level N and finite nebentype epsilon. At every rational prime q outside Np its eigenvalue is the trace of the same Artin lift at arithmetic Frobenius, hence is integral at the selected place: the eigenvalues of a finite-order matrix are roots of unity. Its determinant is epsilon(q), whose reduction is det r(Frob_q).

Use the classical coefficient lattice used in Deligne–Serre section 6.10, on printed 522. For each fixed weight, level and character, the module of forms with coefficients in the chosen localized integer ring is finite free and spans the characteristic-zero space. The cuspidal submodule is saturated: multiplication by a nonzero scalar cannot change whether all constant terms at cusps vanish. It is therefore finite free as well. The good Hecke operators preserve it, by the Fourier formula and cuspidality statement in section 1.6, printed 509. These classical coefficient-lattice facts are retained named inputs, not inferred from Katz base change.

Choose a scalar multiple f_0 of f primitive in this weight-one cusp lattice. It is integral and has nonzero coefficientwise reduction. Indeed, if all coefficients were in the maximal ideal, division by a uniformizer would still belong to the same coefficient lattice, contradicting primitivity. Scaling preserves every good Hecke eigenvalue. This avoids any unproved assumption that an arbitrarily selected eigenvector already has integral coefficients or a unit first coefficient.

## 3. Raise the weight without changing the residual packet

Set n=2(p-1) and w=n+1=2p-1. The integer n is even and greater than two, including when p=3. Deligne–Serre section 6.9, printed 522, supplies the normalized level-one Eisenstein form E_n, integral at p with coefficientwise reduction 1 for this choice. Let g=f_0 E_n. It is a cusp form of weight w, level N and character epsilon: at every cusp a holomorphic factor multiplies a factor with zero constant term. Its reduction equals that of f_0 and is nonzero.

For q outside Np, compare the section 1.6 Fourier formulas at weights 1 and w. Their second terms differ by q^(w-1)=q^(2(p-1)), which is 1 modulo p. All other coefficients agree modulo the selected maximal ideal. Consequently the nonzero reduction of g is a common eigenvector of every such T_q, with eigenvalue tr r(Frob_q). Its diamond eigenvalues are the reductions of epsilon. The same calculation shows that the good determinant term epsilon(q)q^(w-1) reduces to det r(Frob_q).

Apply Deligne–Serre Lemma 6.11 to the finite free weight-w cusp lattice, with this commuting family of good Hecke and diamond operators. It provides a nonzero characteristic-zero cusp eigenvector h after a finite extension, with the prescribed residual eigenvalues. It lifts the eigenvalues, not necessarily the vector g; no claim that h reduces to g is needed. This use does not require p to be prime to N.

If p does not divide N, T_p has not yet been included. It commutes with the specified family and preserves their simultaneous characteristic-zero eigenspace. Choose an eigenvector of T_p in that nonzero finite-dimensional space after a finite extension. This keeps all already prescribed good eigenvalues. Thus h can be taken as a common eigenform for every T_q with q not dividing N. Its character is still epsilon because the lattice was in that fixed character space.

Li's final printed 294 supplies the invariant old/new decomposition and primitive extraction for this actual nonzero common eigenform. A nonzero new component is already a common eigenform and has a nonzero first coefficient. If only an old component occurs, primitive extraction gives a newform at divisor level. In either case obtain a normalized primitive form H of weight w and some level N' dividing N, preserving the eigenvalues at primes outside Np and the corresponding inflated character. The missing T_p step above ensures that the input to Li is the one its statement requires. No claim about the least possible residual level or weight follows.

## 4. The actual residual representation and lattice

The general-weight attachment on final Ghate–Vatsal printed 2143–2144 applies to H before that source introduces an ordinarity hypothesis. At the chosen prime over p it gives rho_H. For q outside Np its characteristic polynomial reduces to

    X^2 - tr r(Frob_q) X + det r(Frob_q).

Both the trace and determinant have been checked. The relevant Frobenius convention is arithmetic. Neither local ordinarity nor the source's splitting theorem is used.

Choose a stable lattice T in rho_H. Existence follows from compactness: start with any lattice L; the compact image is bounded, so the O-module generated by all translates of L lies between L and a fixed inverse-uniformizer multiple of L, is finitely generated, and is stable. Its residual semisimplification and r have finite images. Apply finite Chebotarev to their common finite quotient, so equality of good Frobenius characteristic polynomials becomes equality on every element of that quotient. The finite-field characteristic-polynomial form of Brauer–Nesbitt, explicitly used in Deligne–Serre section 6.13 on printed 523, identifies the semisimplifications after finite residue extension. This is not the characteristic-zero trace-only argument used in the separate untwist packet.

Since r is absolutely irreducible of dimension two, the semisimplification of T modulo its coefficient uniformizer is a single simple constituent of dimension two. The original residual module therefore already has composition length one and is isomorphic to r. Conjugate its basis after finite residue extension if needed. This supplies an actual integral realization in the early-KW convention. It does not identify rho_H with the original first-family characteristic-zero representation; that identification requires the separately reviewed lifting theorem.

## 5. Actual uses and boundaries

ORIGINAL: the induction's original S-type representation, if solvable, satisfies this proposition and is modular without entering the nonsolvable compatible-system construction. All relevant coefficient primes are odd. No new level-one optimal-weight conclusion is asserted by this exit.

FIRST: take the actual globally absolutely irreducible solvable reduction of A_ell in caller13, with ell odd and ell != P. Its continuity, oddness, finite coefficient field and specified lattice come from construction14 and criterion17. Ramification at the old prime P is allowed. The proof covers ell=3, with w=5. Its output supplies only the residual-modularity premise of the conditional FIRST lifting theorem; the latter's characteristic-zero irreducibility, crystalline, determinant and finite-ramification hypotheses remain separately checked. The unramified-at-P and geometrically reducible branches retain base21 and are not needed to justify this solvable branch.

RETURN: whenever the actual returned residual representation at the odd old prime P is globally absolutely irreducible and solvable, this proposition supplies its modularity. The returned weight computation and the nonsolvable lower-weight induction are separate. If a later argument needs an optimal level/weight realization, that remains a distinct refinement theorem and cannot be supplied by this weak modularity result.

The initial candidate involving Moon–Taguchi's refined Katz conclusion and Herremans's comparison has not been selected. Its source files and the initial independent requirements remain preserved. The selected route uses the classical Artin intermediate and the explicit weight-raising argument above; no assertion that all Katz weight-one forms lift is made.

Current manuscript incorporation, ordinary source-use records, a completed induction and whole-proof/release approval are not conclusions of this packet.
