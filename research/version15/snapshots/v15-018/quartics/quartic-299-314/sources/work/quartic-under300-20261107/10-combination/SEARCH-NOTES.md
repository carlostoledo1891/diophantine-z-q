# Structural search after369

The accepted369 construction is frozen. These notes record incomplete alternatives and prevent their tentative counts from entering the accepted lineage.

The fixed-interface power search in `power-search/REPORT.md` rules out one fewer auxiliary per detector only in the quadratic Laurent-binomial model. Agent03 is examining changes to the shared coefficient and product-evaluation interfaces, which that lower bound does not cover.

## A cubic-over-quadratic contact parameter

Replacing F5(t) by a cubic divided by a quadratic would reduce its direct rational circuit cost. It also reverses the valuation signs at the two denominator contacts. The accepted372 local proof uses positive valuations at every required contact. With its bounded pole input, a negative parameter valuation no longer supplies the same test-order implication. Thus a count obtained by canceling two contact factors is not valid without a different local construction. Restoring a parameter with positive valuations at both zeros and poles through R/(1+R^2) adds reciprocal and product interfaces; no net saving was obtained.

## Removing primary formality tests

The primary quotient z(U)/z(H) being integral does not imply U is formal. The parameter z=-x/y also vanishes near the two-torsion point (0,0). There its first-order relation to the local group logarithm has the opposite sign. Replacing it by z(2U)/2 handles the two-torsion translations but introduces branches near points whose double is (0,0). No argument excluding those branches was established. Therefore no primary square-output test can currently be deleted by this route.

## Removing odd-root certificates

Odd root indices are used before the Lucas equation is proved. They ensure the common weak valuation sign in the product-height lemma. Dropping an odd certificate merely because the later Lucas equation or input relation might force parity is circular. Allowing roots with different powers of two in their indices can permit a formal reduction for one root and a two-torsion reduction for another, destroying the known additive product-height identity. No certificate deletion is claimed.

## A two-integer Lucas variant

The norm equation X^2-a*X*Y+Y^2=1 is monic in Y, so integer a,X and rational Y imply integer Y. Taking X=(a-2)t+1 suggests a growth condition using only integer labels a,t. In the current construction, however, the norm equation is established only after the height contradiction applied to its test residual. A free rational Y has no prior height bound in terms of the retained root indices. Replacing the Z root by Y would remove the bound used to prove that residual vanishes. This is an unresolved height interface, not a reduction.

None of these alternatives changes an accepted artifact. They indicate which additional theorem or representation would be needed for a valid next step.
