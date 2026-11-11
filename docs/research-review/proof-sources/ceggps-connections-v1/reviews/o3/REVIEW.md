# Independent O3 connection review

Reviewer: `/root/astra_quartic_opt05_anchor`. Date: 2026-11-08.

I accept the two bounded mathematical connections in compiler006, relative to the explicitly retained source inputs. This is not acceptance of the complete Breuil–Mezard proof tree, a final-edition equivalence claim, or approval of a manuscript replacement.

The exact target is MANIFEST.json `144791b49bd972e2c9d4263eb09f243e5756567aee2479dd35bf7de3a2718c34` and PROOF.md `a5e9fc76577077471fdc6cf36d60707faa10e4b316593f0f4f50c2bb4b3bf9f8`. I read the proof, both ten-field applications, four comparisons, nine obligations, retained inputs, and the actual source passages. I previously independently reviewed the narrower exactness-to-density bridge and O2. I did not author these new O3 arguments. My only requested correction was the zero-order terminology described below.

## Nonordinary RED

Dospinescu's inspected author text pages 2–5 defines the correct finite-length, fixed-central-character unitary Banach category. At p=5 its supersingular condition is the nonordinary Banach condition; neither smooth supercuspidality nor residual irreducibility may substitute for it. The given Pi and its finite self-extensions belong to that category.

The closure argument is valid. The closure C of X_alg contains the closed first Pi because nonzero Pi_alg is G-stable and dense in the topologically irreducible Pi. Since C contains the quotient kernel, C/Pi is closed in X/Pi. Exactness on algebraic vectors puts the dense algebraic part of the quotient in C/Pi, forcing C=X. No general assertion that images of closed subspaces are closed is used.

Passing to spans then gives R(Pi) contained in Dospinescu's Ext_alg. Proposition 1.5 excludes the special Galois exception precisely from irreducibility of Pi_alg. Theorem 1.3 and Proposition 1.4 give dimension one for the larger space and hence dimension at most one for R(Pi). The determinant is fixed over the dual numbers. The argument uses neither the converse density-to-exactness implication nor an equality R(Pi)=Ext_alg. It covers the stated nonordinary cases and leaves ordinary Banach representations and reducible Pi_alg outside its conclusion.

## RED to first-order type multiplicity

The Yoneda pullback map alpha is in the correct direction. A splitting of the pulled-back K-extension gives a K-equivariant lift of the chosen type map j. Its image consists of locally algebraic vectors because K is open and V is locally algebraic. The G-span remains locally algebraic and maps onto Pi_alg by its irreducibility. The kernel of the induced map is exactly the algebraic part of the first closed Pi. Thus each element of ker(alpha) is an allowed exact-algebraic extension class, so ker(alpha) is contained in R(Pi).

The hypotheses End_G(Pi)=E and dim Hom_G(Pi,X)=1 make the connecting map delta from E^m injective. The K-connecting map is alpha composed with delta by naturality of pullbacks. Therefore its kernel has dimension at most one, and the Hom exact sequence gives dim Hom_K(V,X) at most two. The zero-multiplicity alternative follows from the same left-exact sequence. This includes m=0 and split classes. It does not rely on projectivity of V, flatness of a deformation module, or exactness of the algebraic-vector functor in general.

## Actual consumers and preserved limits

I compared BM 2.42, 4.14–4.21 and 6.5–6.6 in the pinned author version and Hu–Tan 4.9–4.10 and 5.11–5.12 in the final published text. BM 2.42 requires the two bounds on the same dense set of characteristic-zero closed points, as well as its separate projectivity and equidimensionality/associated-prime conditions. It does not restrict the zero-order bound to ordinary Banach points. Compiler005 used ambiguous terminology here. Compiler006 changes exactly that phrase; the checker verifies the complete byte delta and unchanged substantive JSON records.

BM 4.14's multiplicity statement is a separate input from O2 inertia detection. BM 4.16's finite exclusions and the weight-gap-one scalar exception remain necessary. BM 4.21 supplies the actual closed socle, first-order extension and Hom_G dimension one; Section 4 does not manufacture them for arbitrary deformations. The cycles sum over every constituent of the reduction of the full type with its multiplicity.

Hu–Tan 4.10 applies the same criterion to N2 through its separately proved regular-sequence and Cohen–Macaulay conditions. Remark 4.8 explicitly says N2 is not flat over the pseudodeformation ring. The new proof makes no contrary assertion. Hu–Tan 5.11 retains its use of 4.2, 4.10, 5.5 and 5.10. Its crystalline conclusion has the separate 5.12 argument, including the k=2 scalar exception; the O3 result does not replace that argument.

The eight retained-input records remain substantive conditions. In particular, final Dospinescu and final BM edition comparisons remain open. Henniart multiplicity, the ordinary and nonsupercuspidal local inputs, the original module constructions and exceptional rings are not independently reproved here. O4, O5 and final release coverage are outside this decision. BINDINGS.json's statement that O2 was under review is historical author metadata; O2 now has its separate bounded decision and is not reaccepted by this record.

## Verification

The independent checker imports no author modules. It verifies the exact target manifest, 28 unique file pins, 14 raw line-excerpt hashes, the sole compiler005-to006 phrase replacement, six unchanged substantive/source JSON files, and the two application/nine-obligation structure. These are reproducibility checks. The mathematical decision rests on the arguments and source comparisons above, not on those checks.
