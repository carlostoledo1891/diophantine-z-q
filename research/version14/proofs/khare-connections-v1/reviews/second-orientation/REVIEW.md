# Independent review of the second-family inertia ordering correction

Reviewer: `/root`. Author: `/root/astra_quartic_opt05_anchor`.
Date: 2026-11-08.

I accept only the changed ordering paragraph in orientation-successor-001,
manifest `48a2e0d2ddb8b9dfa2f3dadeb0aab8b0c48f7d076df23fc0bfbe76b032b067a8`,
proof `92dc7f297a6a145e5012c058eb20c1d7dccbeb60653b4a5d5eda24e666bd34e1`.
This does not accept the full second-family construction or discharge its
general-coefficient finite-flat input.

## Evidence and independence

I read the complete base and successor proofs and their exact delta. I
also read and visually checked final Khare--Wintenberger I, printed 492,
and II, printed 532. The former requires inertia diagonal (chi,1) in its
prescribed-type case; the latter uses an upper-triangular decomposition
representation and records Frobenius invariance of the prescribed tame
character. SourceReview identified the missing ordering explanation and
suggested its repair. I did not contribute to that correction before this
review. Its independent decision is therefore separate from SourceReview's
decision on the other parts of the construction.

## Reconstructed argument

Retain the exact preceding premises: P differs from the coefficient
characteristic l, wild inertia at P acts trivially, the representation is
ramified, and its inertia-fixed space is a line. The determinant character
on inertia is chi of order dividing P-1. Continuity over the finite residual
coefficient field makes the inertia image finite. The tame inertia quotient
is procyclic, so its image has a generator M.

The fixed line is stable under the local decomposition group because
inertia is normal. A basis beginning with that line gives inertia diagonal
(1,chi). This explains why the old paragraph's immediate ordering claim
needed an additional argument.

If chi is nontrivial, choose the tame generator so that lambda=chi(M) is
nontrivial. The two eigenvalues of its matrix are 1 and lambda, which are
distinct and belong to the chosen coefficient field. Hence the matrix is
diagonalizable. Every element of inertia preserves the two eigenlines,
since all such elements belong to this cyclic image.

Let F be an arithmetic Frobenius lift. The tame relation gives
F*M*F^(-1)=M^P. Since lambda^(P-1)=1, diagonalizability gives M^P=M.
Thus F commutes with M and preserves both eigenlines. Inertia and a
Frobenius lift generate the local decomposition quotient relevant to this
representation, so both lines are decomposition-group stable. Taking the
chi line first gives the required ordered upper-triangular representation.
In fact it is diagonal in this case. This is a property of the actual
representation, not merely its semisimplification. Using geometric
Frobenius reverses the exponent relation and yields the same stability.

If chi=1, the original fixed-line basis already has the required diagonal
(1,1). A possible nonzero upper-right entry remains. No splitting or
interchange of a nonsplit extension is asserted. In the ramified branch,
that upper-right inertia action can be nontrivial and is retained.

These two cases exhaust the stated input, including l=3. No statement at
coefficient characteristic 2 or outside the tame ramified branch follows
from this review.

## Binding and limits

The exact replacement is confined to the base proof's line-17 paragraph.
The file checker compares the complete before and after bytes by the
declared literal replacement, rather than accepting matching hashes alone.
It also checks the final-source identities and the successor members.

The conductor calculation, initial family, chosen character, existence of
the second family, same-member local comparison, general-coefficient Serre
weight, publication qualifications and final caller assembly retain their
own premises and reviews. This decision does not extend to them. It is
not a manuscript incorporation or release approval.
