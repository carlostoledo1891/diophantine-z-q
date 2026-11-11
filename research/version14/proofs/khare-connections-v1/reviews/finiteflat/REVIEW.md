# Independent review of the general-coefficient finite-flat criterion

Reviewer: /root, model agent. Author: /root/astra_quartic_opt05_anchor.
Date: 2026-11-08. Decision: accept the stated coefficient-field connection
and its specified lattice application, under the published inputs below.

The target is khare-finiteflat-coefficients-17, manifest
ee962e9d7188b101b158bc393f1a34d2b6c99e5d167bbea2726c9f7d73b0249a,
proof ce463537dd53f1539a5f0173d3c9df2bd85ba0a7a8fe0d1755f0815dd2d65bcc.
This review also checks the exact selection of this lemma by
khare-second-family-15/finiteflat-successor-002, manifest
34f6d405df91ffa10611ef91d4f3c0c1722eef34b7c2ca01afe795129377b587.
It does not accept the complete second-family construction or its later
modularity argument by itself.

## Independence and actual reading

I read the entire proposed proof, its nine comparisons, source records and
the successor's replacement paragraph. I did not author this proof or supply
its finite-field repair. SourceReview identified the earlier coefficient
scope problem and contributed the proposed strategy; this decision is
independent of that agent. My earlier review of the tame character ordering
in family15 is a different inference and remains separately bound.

I read final Raynaud pages241,259-260,267-270; final Serre pages184-187 and
189-190; and final Kisin page1122. The exact PDFs and page extracts are bound
in INPUTS.json. Raynaud268 and270 were also visually inspected. The separate
visual receipt records any further rendered pages actually inspected. No
whole-paper proof audit or new verification of all their ancestors is claimed.

## General coefficient action and tame factors

Raynaud Theorem3.3.3 is a uniqueness statement for all finite commutative
p-power group schemes over a mixed-characteristic DVR with e<p-1. His
Corollary3.3.6 supplies extension of every generic morphism and flat
kernels/cokernels. These statements apply over Z_p and its strict
henselization with e=1, including p=3. They are not limited to the
rank-q vector schemes of Proposition3.3.2. Extending the generic k-action
therefore preserves the field identities by uniqueness. A finite coefficient
extension is a direct sum on underlying F_p representations; product models
and the same full faithfulness supply its action. No rank-p-squared claim
is made about the original model when [k:F_p]>1.

For trivial wild inertia, the two tame eigencharacters are permuted by
Frobenius's p-power action. Their minimal niveaux are at most two. Applying
Raynaud Corollary3.4.4 after passage to the strictly henselian base gives
digits0 or1 for the underlying F_p Jordan-Hoelder factors. Level one thus
gives characters1 and omega; determinant omega forces exactly this pair
when p>2. A genuine level-two pair must be psi and psi^p. The repeated
digits00 and11 have level one. Serre184-185 gives weight2 for both allowed
pairs. Possible unramified nonsemisimplicity does not change these inertia
definitions. The finite coefficient field may be larger than F_(p^2);
the argument bounds the character's minimal niveau, not that field.

## The actual wild extension

A nontrivial finite p-group acting on a two-dimensional characteristic-p
space has a one-dimensional fixed subspace. Normality makes it stable under
the decomposition group. Its character and the quotient character are
level one on inertia. Schematic closure and finite-flat quotient preserve
these actual subobjects. After unramified base change their models are
constant k and mu_p tensor k, by the uniqueness theorem. No residual
semisimplification has replaced the original extension.

The argument excluding the opposite orientation is valid. Over the strictly
henselian DVR, an extension with constant etale kernel and connected
multiplicative quotient is an etale torsor over that quotient. On the
special fiber the connected local base has algebraically closed residue
field, so the torsor is a disjoint union of copies. Henselian lifting of
the component containing the identity gives an open-and-closed finite-flat
subscheme. Its group operations stay in that component, as can be checked
on special fibers and lifted idempotents. The map to the multiplicative
quotient has equal finite-free ranks and is an isomorphism modulo the
maximal ideal, hence is an isomorphism by Nakayama. This supplies the group
section claimed by the author. It does not split the other orientation.
Thus the genuinely wild case has cyclotomic subcharacter and trivial
quotient after this base change.

Pulling back along F_p -> k, 1 -> 1, and pushing out through each
F_p-coordinate functional on the multiplicative subgroup are legitimate
finite-flat group operations. They need not be k-linear. Each resulting
rank-p-squared extension is still killed by p. Its fiber above1 is a
mu_p-torsor, so the fppf Kummer sequence over the local ring, whose Picard
group is zero, gives a unit class. On the generic fiber this is exactly
the corresponding coordinate of the original extension cocycle. These
coordinates recover that cocycle, and their Kummer compositum recovers
its inertia splitting field after adjoining mu_p. Subextensions use
products of unit classes, so no uniformizer class is introduced.

Serre186 expressly permits an elementary abelian wild group of rank m
and defines peu ramifie by the valuation of every Kummer class modulo p.
It is not confined to m=1. The unit classes satisfy that definition.
With ordered exponents beta=1 and alpha=0, Serre187 gives weight2.
This checks the full extension class, including exclusion of the very
ramified case. The proof does not merely list its diagonal characters.

## Exact auxiliary lattice and successor

The actual caller supplies a crystalline A_l of weights0,1 with l odd.
Restriction of coefficients preserves these weights. Kisin1122 explicitly
uses Breuil5.3.1 to obtain a Barsotti-Tate lattice and the finite-flat
subquotient argument to handle another stable lattice. The finite-flat
source theorem is retained, not newly proved by this review. The original
T/varpi T is a quotient of T/lT since l belongs to the ideal(varpi), and
schematic closure and quotient preserve finite flatness. Raynaud extends
its actual residue-field action. The caller's finite determinant factor is
unramified at l, giving det on inertia equal to omega_l. The criterion
therefore yields weight2 for this same reduction, also at l=3.

The successor replaces only the earlier retained finite-field criterion
paragraph by this explicit lemma and its application. Its exact replacement
is checked against the orientation successor; all other proof bytes remain
unchanged. The source corrections do not assert a characteristic-two case,
a ramified-base case, or an arbitrary extension of the published lattice
theorem. Earlier source/family decisions keep their original scope.

## Decision boundary

All nine listed comparisons and the Section5 application are accepted.
The missing general-coefficient implication R15-WEIGHT now has a reviewed
connecting proof under the identified published inputs. The original
prime-field wording of Serre Proposition4 has not been silently enlarged.

This retains Raynaud's stated theorems, the crystalline/finite-flat input
used by Kisin and Breuil, the fppf Kummer sequence, and Serre's definitions.
It does not certify all of those proofs recursively, the existence or
properties of the initial family beyond the stated caller hypotheses,
the complete Serre route, ordinary-inventory coverage, manuscript
incorporation or release. The checker verifies bindings and replacement
scope; the mathematical acceptance is this source-based review.
