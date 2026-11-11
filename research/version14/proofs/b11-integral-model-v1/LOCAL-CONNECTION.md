# The two direct Buzzard applications and the three-adic lattice connection

Author proposal for independent review. The target is combined004,
`manuscripts/quartic_v14.tex`, SHA256
`ed992fd5876ad89383dc58848bab378045820cf411535dbd6045e3bea0b3a68f`.
This document supplies connections for the six B11 phase records. It does not
approve them, replace the entire source inventory, or claim the height theorem.

## 1. Inputs kept separate

The quaternion algebra is B=(2,-3) over Q, with reduced discriminant 6. The
maximal order O and its canonical principal polarization datum are the objects
constructed at manuscript lines 724-741. Their construction is the separate
A001 input; this note does not infer a principal polarization from a theorem
about arbitrary quaternion actions. The normalizer computation at lines 742-759
is another direct input, used only in the last phase to retain the degree bound
324. It is not an output of the integral-model theorem.

The geometric background still requiring its own exact source records consists
of: the rank and torsion comparison for Tate modules of abelian surfaces away
from the characteristic; finite-etale representability of the required Isom
sheaves; faithfulness of endomorphisms on the Tate module; finiteness of
polarization-preserving group automorphisms; and the projective quotient and
effective descent results. Their absence from this note is not a classification
of these inputs as irrelevant background. The separate author packets must
provide them before the complete B11 construction can be accepted.

## 2. The initial model, lines 762-765

Use Buzzard, *Integral models of certain Shimura curves*, Duke Mathematical
Journal 87 (1997), 591-612, DOI 10.1215/S0012-7094-97-08719-6. The exact final
PDF already held by the project has SHA256
`ed34a072898d0e6ef6526c877159fbe627ae695265d4f5b2f2a1d6e35c9bac65`.
The required source passages are the level definitions and conditions on
printed page 594, Theorem 2.1 and Lemma 2.2 on pages 595-596, and Corollary 2.3
on page 597. They supply the proper smooth fine scheme and projectivity at
the admissible initial level, together with its represented universal object.

Choose U=V_1(5), defined by the lower row (0,1) modulo 5. For each a in
F_5^*, diag(a,1) is in the corresponding subgroup. Thus its determinant image
modulo 5 is all F_5^*, and the full local determinant image at 5 is Z_5^*.
At other split primes the maximal-order unit group is GL_2(Z_l), whose
determinant image is Z_l^*. At the division primes 2 and 3 the reduced norms
of maximal-order units give Z_l^*, as required by the retained local norm
input. These assertions verify the full adelic determinant condition; checking
only the determinant at 5 would not suffice.

The subgroup is maximal at the primes dividing 6. Its level parameter is 5,
which is prime to 6 and satisfies the printed smallness bound. Hence the base
in the theorem is Z[1/(5*6)]=Z[1/30]. The initial model is the V_1(5) model.
The theorem is not applied a second time to the full-five subgroup, whose
determinant condition differs, or to a subgroup with level at the division
prime 3. The polarization convention remains the separately fixed canonical
one, preserved by the morphisms in this moduli problem.

## 3. The full-five refinement, lines 766-768

There is a second, distinct direct application of Buzzard on printed page
593, Definition 1.1 and the paragraphs before Definition 1.2. For M prime to
the discriminant and over Z[1/(Md)], the full-M marking sheaf is a finite
etale (O/MO)^*-torsor. Its H-orbit sheaf represents an H-level marking.

Take M=5 and H the subgroup defining V_1(5). Pull back the full-marking
torsor along the section of its H-orbit sheaf supplied by the existing
V_1(5) marking. Etale locally the torsor is trivial, the orbit is a coset,
and the fiber over that coset is an H-torsor. Consequently this pullback is
finite etale and surjective over the V_1(5) model. This is exactly the
full-five refinement used in the manuscript. No determinant component is
discarded.

A full marking is an O-linear isomorphism from the left regular level module
to A[5]. Endomorphisms of the source left regular module are right
multiplications. Thus alpha maps to alpha composed with r_delta; this is the
left action convention used in Buzzard. Reversing the side of multiplication
would change the action formula. Nothing in this step treats O/3O as a split
matrix algebra: the same source paragraph has a prime-to-discriminant
hypothesis and is not a supplier for the three-marking step.

## 4. The local division-order input

Use John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288,
Springer (2021), Chapter 13, DOI 10.1007/978-3-030-56694-4_13. The final chapter
is available from the publisher. The selected results are Lemma 13.3.2 and
Proposition 13.3.4, printed pages 205-206. They state the discrete valuation
properties and identify the nonnegative-valuation ring with the unique
maximal order of a division algebra over the complete discretely valued
field. The valuation convention is

    w(x) = v_3(nrd(x))/2,       w(3)=1.

It is not the integer-normalized valuation that assigns a quaternion
uniformizer value 1. A rescaling would not alter the inequalities below,
but the recorded convention must match the source.

The relevant proof uses multiplicativity of reduced norm, the valuation on
each commutative field Q_3(x), and integrality to identify the maximal order.
The analogous assertion for a split algebra is false and is not used here.
The source's finite field-extension valuation theorem is a retained
published antecedent, not a consequence of the manuscript's height argument.
Final source bytes and the errata search are recorded separately at freeze.

The final chapter PDF is pinned at SHA256
`8f8089860649fa19b8467fd76d0959950d01fdee977b92fced25db5078f2e9f7`.
The author-posted errata retrieved with it has SHA256
`42987c03960d3c5d36e5920243e6defc587710cd7e106e79b3a688d1e3bf3232`.
The proof of Proposition 13.3.4, first two lines of page 206, prints an
equality w(alpha)=v(nrd(alpha)) that omits the divisor n from (13.3.1).
I checked the page image, not just extracted text. Replace that equality
by w(alpha)=v(nrd(alpha))/n. Its only use there is nonnegativity, which
is unchanged because n>0. The current argument uses the normalized formula
throughout. This local correction is proposed for independent review; it
is not a claim that the source's entire proof has been audited.

The same omitted divisor occurs in the proof of Theorem 13.3.11(b),
page 207, in the comparison of w(alpha) with v(nrd(alpha)). Restoring
the divisor 2 also leaves that nonnegativity test unchanged. Thus the
correction is recorded for both occurrences in the selected dependency
slice, rather than only the first occurrence on page 206.

There is also a missing word in the prose following (13.3.9), which calls
P the unique left or right ideal. The following sentence makes the intended
maximal-ideal assertion explicit. Neither the claim that there is only one
ideal nor that claim's use is part of the present argument. The arguments
below use only the valuation-ring identification and valuation inequalities.

### 4a. Completion of the fixed maximal order

Here is the local-to-global step needed to identify the actual completed
order O tensor Z_p with a maximal order, rather than silently replacing it
by another order. Suppose R is a Z_p-order properly containing O_p.
Because both are full Z_p-lattices, R is contained in p^(-k)O_p for some
k>=0. Define O'={x in O[1/p] : x_p in R}. This is a subring containing O.
Writing x in a fixed Z-basis of O, the condition x_p in p^(-k)O_p shows
that each coefficient lies in Z[1/p] intersect p^(-k)Z_p=p^(-k)Z.
Consequently O' is a subgroup of the finitely generated free abelian group
p^(-k)O, so it is an order.

Choose y in R outside O_p. Its coset y+O_p is an open subset of B_p
contained in R and disjoint from O_p. The coordinate density of Z[1/p]
in Q_p gives x in O[1/p] in that coset. Thus x belongs to O' but not O.
This contradicts the maximality of the actual O. Hence O_p is maximal.
At p=3 the unique-maximal-order assertion of Proposition 13.3.4 now
identifies O_3 with the nonnegative division-valuation ring used in section 5.

### 4b. The determinant image at the other primes

At a split prime p, identify B_p with M_2(Q_p). Choose a full Z_p-lattice
M_0 in Q_p^2 and set M=O_p M_0. This is a full lattice because O_p is
finite over Z_p and contains 1. The order End_Zp(M) contains O_p, so the
maximality proved above gives equality. A basis of M identifies that order
with M_2(Z_p). Its units have arbitrary determinant in Z_p^*.

At a division prime use Voight's final Theorem 13.3.11 on pages 206-207.
It identifies the unique maximal order as S+Sj, where S is the integers
of an unramified quadratic extension K/Q_p. Section 13.2.5, page 203,
gives N(K^*)=Z_p^* p^(2Z). An element with unit norm has valuation zero,
so it belongs to S^*. Thus N(S^*)=Z_p^*. The restriction of reduced norm
to the quadratic field is its field norm, giving nrd(O_p^*)=Z_p^*.
This covers p=2 as well as p=3; no odd-residue-characteristic restriction
is introduced. At p=5, the specific V_1(5) subgroup already has full
determinant by section 2. These statements complete that determinant check.

The exact source claims from 13.2.5 and 13.3.11, including the correction
list's notation clarification before 13.3.11, must be recorded alongside
13.3.2 and 13.3.4. No class-number theorem or global strong-approximation
claim is needed for the local determinant calculation.

## 5. Why the three-adic lattice is principal, lines 773-778

Let A be any geometric fiber, over an algebraically closed field of
characteristic different from 3. Write T=T_3(A), and V=T tensor_Z3 Q_3.
The Tate-module input gives T free of rank 4 and identifies T/3T with A[3].
The O action extends to a unital O_3 action on T and a unital B_3 action on V.

B_3 is a division algebra of dimension 4 over Q_3. Choose 0 != v in V.
The B_3-linear map B_3 -> V, a |-> av, is injective: if av=0 and a != 0,
then multiplying by a^{-1} gives v=0. Equal Q_3 dimensions make this map
an isomorphism. Thus V is a rank-one left B_3-module. This particular
argument does not require the more general theorem that End(A) acts
faithfully on T; that theorem remains relevant in the stabilizer argument.

Under this isomorphism let L be the lattice corresponding to T. Choose a
Z_3-basis e_1,...,e_4 of L. For y=sum a_i e_i in L, the valuation inequalities
give w(y) >= min_i w(e_i), since w(a_i)>=0. Therefore the nonzero lattice
elements have valuations bounded below. Their values lie in the discrete
group (1/2)Z, so the set of values has a minimum. Choose a nonzero x in L
with that minimum.

For nonzero y in L, w(y x^{-1})=w(y)-w(x)>=0. The maximal-order theorem
then gives y x^{-1} in O_3, so y is in O_3 x. Conversely O_3 x is contained
in L because L is O_3-stable. Hence L=O_3 x. The map a |-> ax is an
isomorphism of left O_3-modules, and reduction modulo the central element 3
gives O_3/3O_3 isomorphic to T/3T and thus to A[3].

This proves nonemptiness of the geometric marking sets in every allowed
characteristic directly. Finite-etale representability then yields the
stated nonempty marking cover. It does not assume semisimplicity of O/3O,
and it does not rely on every connected component having a characteristic
zero point. The alternative local-constancy sentence at lines 779-781 is
unnecessary for this argument and is not used to close the current record.

## 6. The torsion-free calculation, lines 786-791

Assume the separately sourced facts that a polarization-preserving group
automorphism of A has finite order and that its action on T is faithful.
A stabilizer for the change of full-five marking preserves the full-three
marking, so its matrix lies in 1+3M_4(Z_3).

Suppose this congruence group has a nonidentity finite-order element. Taking
a suitable power gives an element h of prime order ell. Write h=1+3^r M,
where r>=1 and at least one entry of M is a 3-adic unit. If ell !=3, the
linear term in h^ell-1 has minimum entry valuation r, while every higher
term has all entries of valuation at least 2r. Cancellation is impossible.
If ell=3, the terms are 3^(r+1)M, 3^(2r+1)M^2 and 3^(3r)M^3. The latter
two have valuation at least r+2, while the first has minimum entry
valuation r+1. Again h^ell !=1, a contradiction.

Thus the stabilizer automorphism has identity Tate action and is identity.
Since a full-five marking is an isomorphism, its precomposition by a
nonidentity right multiplication cannot equal itself. The element of G_5
is therefore identity too. This proves geometric freeness. There is no
analogous assertion here about 1+2M_4(Z_2).

## 7. What is not closed by this note

Freeness is not by itself a proof of projective representability of the
quotient or effectiveness of descent of its universal abelian scheme.
Those source-to-object comparisons remain separate phase-five inputs.
The norm image used in section 2 and the local-to-global maximal-order
identification in section 5 are derived in sections 4a-4b above. Their
source records and independent acceptance must be retained even if the
same facts occur in the previously reviewed normalizer calculation.
The full-three functor identity and the degree324 consumer remain the sixth
phase with the separate normalizer input. No temporary level-five degree
is multiplied into that bound.

The current note is an authored derivation for independent review, not a
new independent decision on the earlier six cards or a blanket acceptance
of their unchanged hypotheses.
