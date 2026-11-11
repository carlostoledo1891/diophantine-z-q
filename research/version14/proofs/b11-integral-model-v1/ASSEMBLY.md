# The six-phase B11 integral-model argument

Author draft for independent review against the combined004 manuscript,
SHA256 ed992fd5876ad89383dc58848bab378045820cf411535dbd6045e3bea0b3a68f,
lines 724--797. This document assembles the actual connections. It is
not a declaration that the provider packets or the entire height theorem
have been accepted.

## Exact objects and retained geometric input

Set R=Z[1/30]. Retain the A001 data: the particular indefinite quaternion
algebra B=(2,-3) of discriminant 6, its specified maximal order O, and
the positive determinant-one principal-polarization convention in
lines 724--741. The moduli objects below have that convention, their
unital O-action, and the indicated left O-module markings. Isomorphisms
preserve the identity section, polarization and action as actual maps.

Also retain the identification of the generic full-three moduli problem
with the actual adelic curve Y3, including all its determinant components,
and the identified normalizer quotient P1_j. Here j is the quaternionic
coordinate in A001. These geometric identifications and the fixed-order
polarization are inputs, not consequences of the integer 324 calculated
below. Their exact source applications must remain visible in the final
inventory.

The following provider arguments are used at their stated strength:

- CONNECTION.md supplies the two direct Buzzard applications, completion
  of the actual maximal order, all-prime reduced-norm surjectivity on
  local units, the division-lattice argument, and the congruence-torsion
  calculation. Its independent review excludes the other providers.
- The Tate/polarized-automorphism packet supplies free Tate modules of
  the required rank away from the residue characteristic, identification
  modulo the torsion prime, faithful action of endomorphisms, and
  finiteness of automorphisms preserving the specified polarization.
  Its corrected finite-generation proof and metadata must be used together.
- The marking/descent packet supplies finite-etale torsion and Isom
  representability, free finite-group quotients, their projectivity,
  and effective descent of the abelian scheme and its specified maps.
  In particular it proves projectivity before invoking projective-case
  duality; it does not replace the principal polarization by a norm multiple.
- FIVE-MARKING-CONNECTION.md supplies the split-prime matrix-unit argument
  for arbitrary full-three objects. NORMALIZER-CONNECTION.md supplies
  the separate degree calculation under the geometric inputs above.

## Phase 1: the V1(5) model

Apply Buzzard's Theorem 2.1 and Corollary 2.3 to V1(5). At 5 the subgroup
has full determinant image, since the upper-left diagonal entry can be
any unit while the lower row is congruent to (0,1). At the remaining
split primes the maximal-order units have full determinant image; at
the two division primes the reduced norms of units are all local units.
These last assertions concern the actual order and are established in
CONNECTION.md. The level is maximal at the division primes, and 5 is
prime to 6 and satisfies the required smallness bound. Thus the theorem
gives the smooth projective fine moduli scheme XV1 over R and its
universal object in the retained polarization convention.

The rigidity assertion is part of the actual published conclusion.
Buzzard defines the groupoid X(U) on printed page 595, and Corollary 2.3
on page 597 identifies it with the stack associated to a regular scheme.
Thus its objects over arbitrary R-schemes have no nonidentity
automorphisms. This is stronger than representability of geometric
isomorphism classes alone. An automorphism preserving a full five-marking
preserves its induced V1(5) marking, so the same rigidity holds after
adding the full five-marking. Buzzard's proof uses DR II.1.14 to pass
from a family automorphism to a geometric fiber; that source ancestry
remains part of the cited corollary.

## Phase 2: full five-marking

Use Buzzard's separate marking definition and H-orbit construction on
printed page 593. The existing V1(5) marking is a section of the quotient
of the full-marking torsor by the corresponding stabilizer H. Pulling
back that torsor along the section gives the finite etale surjective
H-torsor of refinements. Its total space X5 represents full five-markings.
Conversely a full marking has its H-orbit marking, so this construction
does not select or omit a determinant component. A finite cover of the
projective XV1 is projective; etaleness preserves smoothness. Pull back
the universal object to X5.

Our action convention is the following. For g in (O/nO)^*, put r_g(x)=xg.
For a marking m of a left module, define g dot m=m composed with r_g.
Since r_h composed with r_g equals r_(gh), this is a left group action.
This convention is retained at both marking primes and in the quotient.

## Phase 3: full three-marking

Over X5 form the finite-etale Isom scheme

    Isom_O(O/3O, A[3]).

Finite etaleness is the separate Isom representability assertion; the
following calculation proves its surjectivity, including all allowed
positive-characteristic fibers. For an algebraically closed geometric
fiber k, the Tate module T3(A) is free of rank four over Z3, with its
unital O3-action. The rational Tate module V3(A) has Q3-dimension four.
Since B3 is a division algebra of dimension four, for every nonzero
v in V3(A), the map b -> bv from B3 is injective and hence an isomorphism.
Thus V3(A) is a free rank-one left B3-module.

Under such an identification, the Tate lattice is an O3-stable full
lattice L in B3. Normalize the division valuation as w=v3(nrd)/2.
The valuations of its nonzero elements are bounded below and discrete,
so choose x in L with minimum valuation. For y in L, w(yx^(-1))>=0;
the reviewed valuation-ring assertion gives yx^(-1) in O3. Consequently
L=O3 x as a left module. Reduction modulo the central element 3 and
the Tate/torsion identification give A[3] isomorphic to O/3O.

The Isom scheme is therefore surjective. Call its total space X35.
It is smooth and projective over R, by its finite-etale map to X5, and
has the two full markings and the pulled-back universal object.

## Phase 4: freeness of the five-marking action

The group G5=(O/5O)^* acts by changing the five-marking only. If a
geometric point is fixed by g, its represented object admits a polarized
O-linear automorphism alpha preserving the full three-marking and
carrying its five-marking to the relabeled one. The finite polarized
automorphism theorem gives alpha finite order. On T3(A), preservation
of A[3] places its matrix in 1+3M4(Z3).

The explicit first-term binomial argument in CONNECTION.md shows this
group is torsion-free. Thus alpha acts trivially on T3(A); faithfulness
of the Tate action gives alpha=1 as an endomorphism, not merely up to
isogeny. The full five-marking is an isomorphism, so its stabilizer in
G5 is trivial and g=1.

This proves freeness of the scheme action as well. For each nonidentity
element of the constant finite group, its equalizer with the identity
has no geometric points and is empty. The identity component of the
stabilizer is the identity section itself. No invertibility of |G5|
has been inferred from invertibility of 5.

The same argument, without the last five-marking step, proves geometric
rigidity for every full-three object. An additional step is required
over an arbitrary, possibly nonreduced R-scheme T. Let alpha be an
automorphism of a full-three object over T. Its action on the finite-etale
A[5] is identity on every geometric fiber, hence identity as a morphism
of the finite-etale scheme, by the finite locally constant sheaf
description. Pull back to the finite-etale surjective full-five marking
cover supplied by FIVE-MARKING-CONNECTION.md. On that cover alpha
preserves the full five-marking. Rigidity of the initial full-five
groupoid, explicitly retained in Phase 1, forces alpha=1 there. Faithful
flat descent of morphisms gives alpha=1 over T. This proves the arbitrary
base rigidity needed in Phase 6, without inferring equality of general
scheme morphisms merely from equality on geometric fibers.

## Phase 5: quotient and descent of the exact object

Apply the free finite-group quotient theorem to get a scheme
Y=X35/G5 and a G5-torsor q:X35 -> Y. The marking/descent provider shows
that q is finite etale and surjective, Y/R is smooth and projective,
and the universal abelian scheme descends effectively. It uses a norm
of an ample sheaf only for projectivity of the base quotient. That norm
does not alter the abelian-scheme polarization.

The relabeling isomorphisms of the universal object satisfy the cocycle
identity: they come from the same fine moduli problem and do not change
the three-marking, O-action or specified polarization. For effective
scheme descent, the provider first obtains projectivity of the universal
abelian scheme over the regular base X35; this is independent of the
subsequent projective-case duality argument. Morphism descent transports
the identity, multiplication, inverse and all ring-action identities.

After descent, base-compatible duality identifies the pullback of A^vee
with the dual of the original universal abelian scheme. The actual
principal-polarization map descends under this identification. Its being
an isomorphism is faithfully-flat local, and its geometric fibers are
the original polarizations. It therefore still has degree one. The
O-action and full three-marking descend as actual maps as well.

## Phase 6: identification with the whole full-three functor

Let T be any R-scheme and let a be an object of the specified full-three
problem over T. Form the sheaf of its full five-markings. Its finite-etale
representability is supplied by the marking/descent theorem. Its local
nonemptiness for this arbitrary object follows from the split-prime
matrix-unit proof in FIVE-MARKING-CONNECTION.md, rather than from any
assumption that a was already obtained from X35. It is a G5-torsor P/T.

Adding the tautological five-marking over P gives a G5-equivariant map
P -> X35. Its composition to Y is invariant and descends to T -> Y.
Conversely pullback of the descended universal object along T -> Y
gives a full-three object. After the faithfully flat marking cover the
two constructions are inverse, and uniqueness of the isomorphisms
follows from the three-level automorphism calculation in Phase 4.
They are consequently inverse on T and compatible with its arbitrary
base changes. Hence Y represents the full-three functor, with all
components and the same retained polarization convention.

Its generic fiber is the specified Y3, by the retained geometric
identification. The separate normalizer calculation bounds the degree
of this precise Y3 -> P1_j by 324. The five-marking cover has been
quotiented out in this functor comparison; its degree does not enter
that bound.

## What is still required before adoption

The proof providers, this full assembly, the matrix-unit connection,
and their exact current-source use records require independent review.
Acceptance of a provider is not by itself acceptance of this assembly.
The A001 geometric inputs must retain their own direct source records;
no conclusion about their proof is inferred from the local calculations.
Subsequent claims about genus, stable reduction, branch divisors, height
bounds or the rest of the manuscript lie outside these six phases.
