# Local existence of the forgotten five-marking

Author proposal for independent review. This is the additional input needed
by the full-three functor comparison, not merely the existence of refinements
of an already chosen V1(5) marking.

Let k be an algebraically closed field of characteristic different from
2, 3 and 5. Let A/k be any abelian surface in the specified polarized
O-moduli problem. In particular its O-action is unital. No five-marking
is assumed. The separate finite-etale torsion theorem makes A[5] a constant
finite etale group of order 5^4, killed by 5. Its k-points V therefore form
a four-dimensional vector space over F5. The O-action factors through
O/5O on V.

The fixed quaternion algebra is split at 5. The completion and split-order
arguments in the separately reviewed CONNECTION.md give

    O tensor Z5 = End_Z5(L) for a free rank-two Z5-lattice L.

Reducing a basis of L modulo 5 gives O/5O isomorphic to M2(F5). Let e_ij
be the corresponding matrix units acting on V. Since e_11+e_22=1 and
the two idempotents are orthogonal, V=e_11 V direct-sum e_22 V.
The maps e_21:e_11 V -> e_22 V and e_12:e_22 V -> e_11 V are inverse.
Each summand consequently has dimension two. Choose a basis v_1,v_2
of e_11 V. Define

    F:M2(F5) -> V by F(E_ij)=e_i1 v_j.

The two images with i=1 are a basis of e_11 V, and those with i=2 are
a basis of e_22 V. Hence F is a vector-space isomorphism. For all matrix
units E_ab and E_ij,

    e_ab F(E_ij) = delta_bi e_a1 v_j = F(E_ab E_ij).

It is thus a left M2(F5)-module isomorphism. Via the chosen order
identification, this is an O-linear isomorphism O/5O -> V. Since finite
etale schemes over k are constant, it is also an isomorphism of the
corresponding O-module group schemes with A[5].

For a family A/T, the finite-etale Isom representability theorem in the
separate marking/descent packet now shows that

    Isom_O(O/5O, A[5]) -> T

is finite etale and surjective: every geometric fiber is nonempty by
the calculation above. The automorphism group of the left regular
module consists of right multiplications by units of O/5O. With the
left action g dot m = m composed with r_g, this Isom scheme is a torsor
under the constant group G5=(O/5O)^*. Indeed any two markings differ
by a unique such right multiplication, and that identification holds
etale-locally and hence globally as an isomorphism of torsor diagrams.

This argument supplies the forgotten-marking cover for every object
in the full-three moduli problem. It does not rely on having already
obtained that object by descending an X35 point, so the functor
comparison is not circular. It makes no determinant-component choice.
It does not need the separate Tate-module faithfulness theorem.

The exact incoming assertions are finite-etale five-torsion of rank
5^4, the unital order action, the fixed algebra being split at 5,
the reviewed maximal-order completion argument, and finite-etale
Isom representability. Independent review of this additional matrix-unit
connection and its use in the six-phase assembly remains required.
