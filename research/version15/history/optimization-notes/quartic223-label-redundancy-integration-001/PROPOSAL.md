# A late Lucas-label redundancy and the earlier certificate boundary

Author research note on accepted raw223, not a changed construction.

## Exact lemma

Let a,b be integers and t rational. If

 t²-a(a-2)tb+(a-2)²b²-1=0,

then t is an integer. Indeed write t=u/v in lowest terms with v>0. Multiplication by v² gives u² divisible by v. Coprimality implies v=1. Thus the explicit condition t in Z is redundant in this exact abstract Lucas relation once a,b in Z are known.

This statement includes every sign and zero case. It adds no conjecture or new arithmetic source. It does not remove the need for the exact relation itself.

## The asymmetry is real

Integrality of b is not similarly implied by integral a,t. For each integer a>=4 set t=a and b=1/(a-2). Then w=(a-2)b=1 and the displayed equation is a²-a²+1-1=0. Here b is nonintegral. With c=a-1 and B=max(|a|,|t|,|b|), B=a, so the exponential Lucas growth conclusion used in the construction fails for arbitrarily large c. This is a counterexample to the weakened abstract Lucas assertion only, not a solution of the full accepted IR or its scalar constraints.

## Why this is not a deletion of root3

The source has Q1=[n]P,Q2=[a]P,Q3=[t]P,Q4=[b]P. It first uses all four genuine roots in the aggregate-height bound on B, then uses that bound and integral local divisibility to prove the exact Lucas relation. Applying the lemma to justify deleting Q3 before this step would be circular.

The actual223 root3 coordinates189..202 store a root-product chart and auxiliary comparisons, not t itself. Their exact consumer list is attached: besides the block equations they feed detector factor1, the alternate comparison and the aggregate trace. Deleting only the root equations while retaining those consumers leaves their arithmetic meaning unjustified. A successful use of the lemma would need a new sound way to establish the exact relation and height control without that root certificate, followed by a complete integer-witness construction.

Nor can the integer group index be silently recovered as an ordinary rational function of the point. If P is nontorsion and a rational function f on the elliptic curve satisfied f([n]P)=n for all positive integers n, then g(Q)=f(Q+P)-f(Q)-1 has infinitely many zeros and is identically zero. The pole set of f would then be invariant under translation by P. A nonempty finite pole set cannot be invariant under a nontorsion translation. Hence f has no poles, is constant on the complete curve, and cannot satisfy this identity. This proves only that a global rational index-extraction shortcut is unavailable; it does not preclude a different Diophantine certificate.

## Status and authorship

This is a precise simplification lemma at the abstract-label level plus a scoped obstruction to applying it directly to the accepted compilation. No variable savings, global lower bound or manuscript change is claimed. Integration authored this note and requests disjoint review. Existing source acceptance and full223 equivalence are reused within their scopes.
