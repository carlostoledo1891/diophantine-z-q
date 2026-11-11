# The separate normalizer-degree input to the sixth B11 phase

Author proposal for independent review. Target: combined004 manuscript
`ed992fd5876ad89383dc58848bab378045820cf411535dbd6045e3bea0b3a68f`,
lines 742-759, consumed at lines 795-797. This is an explicit expansion of
that existing argument, not an independently accepted replacement.

## Retained geometric input

Keep the fixed B=(2,-3), its maximal order O, and the positive principal
polarization datum of A001. Keep the identified generic full-three Shimura
curve Y_3 with all determinant components, its adelic level description,
the right normalizer action, and the source identification of the full
normalizer quotient with P^1_j. These are geometric inputs to the following
finite-index calculation. The calculation does not construct that quotient
identification or prove its field of definition. It uses the same Y_3 and
the same j-map as the integral-model construction.

Put K_0=Ohat^*, let K_3 be the kernel of reduction to (O/3O)^*, and let N
be the finite-adelic normalizer of Ohat. Conjugation by an element of N
preserves the ideal 3Ohat, so it preserves K_3. Thus the given right action
is an action at this same level, not a map to a different level curve.

## Local normalizers and their global index

At each prime p, O_p is maximal by the completion argument in section 4a
of the separately frozen CONNECTION.md. At a split prime, identify O_p
with End_Zp(L) for a rank-two lattice L, as in its section 4b. If g normalizes
this order, the lattice gL is stable under End_Zp(L). In a basis of L,
stability under the two coordinate projections splits gL as I_1 e_1 plus
I_2 e_2, with fractional Z_p-ideals I_i. Stability under the two off-diagonal
matrix units gives I_1=I_2. Therefore gL=p^r L for some integer r, so
g is in Q_p^* O_p^*. Conversely every such g normalizes O_p. This proves
the split local normalizer assertion without assuming it as a new source.

At a division prime, uniqueness of the maximal order in Voight 13.3.4
makes every element of B_p^* normalize O_p. The valuation w=v_p(nrd)/2
has kernel O_p^* on B_p^*. Its image is (1/2)Z: Voight 13.3.11 supplies
an element j with j^2 a uniformizer. The image of the central Q_p^* is Z.
It follows that B_p^*/(Q_p^* O_p^*) has order two.

The only division primes are 2 and 3. The two local valuation parities
therefore define N/(A_f^* K_0) as a group of order four. More explicitly,
the kernel consists of central local factors times local order units;
the central factors assemble to a finite idele because only finitely many
are nonunits. A quaternion uniformizer at either division prime, with
identity components elsewhere, realizes either parity independently.

## Why the center acts trivially at full level three

Let a=(a_p) be a central finite idele. Choose r in Q^* with
v_p(r)=-v_p(a_p) for every p. Only finitely many valuations are nonzero,
so such r exists as a signed product of prime powers. Then ra belongs
to the central subgroup Zhat^*. Choose the sign of r so that its component
at 3, multiplied by a_3, reduces to 1 in F_3^*. This is possible because
F_3^* consists of 1 and -1.

Consequently ra is in K_3. In the full adelic description of Y_3, the
rational central element r acts trivially on the symmetric domain and
can be absorbed on the rational left side. The remaining ra is absorbed
on the level right side. Hence a acts trivially. This reasoning uses the
whole level curve; it does not select a connected component or assume
that a chosen component is stable under every normalizer element.

## Degree bound and its consumer

The acting finite group is thus a quotient of G=N/(A_f^* K_3), and

    |G| <= 4 [K_0:K_3] <= 4 |(O/3O)^*| <= 4*3^4 = 324.

The middle inequality uses the kernel definition of K_3; it does not
require an unproved surjectivity assertion for the reduction map. The
last inequality uses the rank-four Z-basis of the actual order O.
With the retained normalizer-quotient identification, a geometric generic
fiber of Y_3 -> P^1_j is an orbit of the finite group, hence has at most
|G| points. In characteristic zero the resulting finite curve map is
generically separable, so its degree is at most 324. The same orbit bound
applies with all components retained.

The sixth phase identifies the generic fiber of X_35/G_5 with this Y_3,
with the same j-map. Only after that identity has been established may
this bound be consumed by the integral-model argument. The temporary
full-five cover is not a factor in this degree calculation.

## Boundaries for the eventual application record

The explicit incoming geometric assertions are the fixed order and
polarization, the full adelic description and its normalizer action,
and the P^1_j normalizer quotient. The local division-order input is the
same published one as in CONNECTION.md. The outgoing assertion is only
the degree bound for this exact generic j-map. Torsor representability,
effective descent, reduction types, genus, discriminants and the height
estimate are not proved by this calculation. Its source-to-consumer record
must retain those boundaries and receive non-author review.
