# Direct Lucas encoding: valid algebra, absent label interface

This author research note concerns the accepted223 IR, not an installed change.

If ordinary rational variables a,b,t really are the integer root labels, introduce k,l with

 k-(a-2)b=0,
 l-tk=0,
 t²-a l+k²-1=0.

All three equations have degree at most two. The first two uniquely determine k,l; substituting them into the third gives exactly Delta=0. Conversely every rational a,b,t with Delta=0 has a unique lift. Their sum of squares is a quartic over Q, nonnegative on real tuples and zero precisely when all three hold. If a,b are integers, monicity gives t integer as proved in the separately reviewed label lemma. No real-solubility shortcut is used.

The cost is two auxiliary rational variables when a,b,t already exist, or three new variables t,k,l when only a,b exist. This is not the current223 interface. None of its ordinary coordinates is the discrete label a or b. The source labels occur as Q2=[a]P,Q4=[b]P, while the rational variables store elliptic coordinates, comparison ratios and algebraic gates. Its apparent L2/L3/L4 coordinates represent z(Ui)/z(H), after the stated nonzero rescalings, not the indices themselves. They are K-valued, represented by two rational components. The source proves only selected local congruences Li congruent ni; it does not identify these functions globally with ni.

In particular Lucas.C and Lucas.AT are products of those comparison functions. Actual rows10-13 confirm this, including their R scaling. They are not exact scalar products ab and at. Rows14-15 compute the corresponding comparison residual, which is subjected to local tests rather than imposed as zero. Reusing these nodes as exact labels would change the equations and require a new soundness and completeness proof.

A concrete function-level check on the exact curve and generator gives z([2]P)/z(P)=(13712284495998-11446225896960 sqrt(2))/3287811625151, not2. This example does not claim H=P satisfies the complete construction's anchor exclusions. Its purpose is to rule out the proposed rational-function identity. The separately reviewed global index-extraction lemma also excludes obtaining all integer indices by a rational function of a point.

Therefore the advertised two auxiliaries do not presently replace Q3. Adding all five ordinary variables a,b,t,k,l would still leave the indispensable links a<->Q2 and b<->Q4 unencoded. No bounded gate cost or completeness claim can be assigned to those absent links. Applying the same three equations directly over K to the existing comparison values is a different condition; monicity over integral a,b no longer applies and accepted integer witnesses are not shown to satisfy it.

Conclusion: the three-quadratic algebra is valid and potentially useful if an honest ordinary-label interface is independently constructed. The current circuit/source provides none. No smaller candidate, unavailable index assumption, or manuscript change is asserted. Integration authored this note and requests independent review.
