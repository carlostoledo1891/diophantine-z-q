# Same-step linearization application comparisons

Author proposal under protocol v1.4. Application ID: GTZ-LP-INCREMENT-LINEARIZATION. The nine comparisons below are unresolved pending independent review. Proof sections and source-use cards are pinned by the manifest. The theorem retains the same-step linear interface and does not accept the polynomial inverse theorem as already proved.

## Source hypotheses

Available: the accepted tautification theorem supplies an exactly equal sequence on a fixed rational degree filtration with G0=G1, bounded normalization at zero and uniform test-function bounds. Needed: an h with h(0)=1, on a fixed taut geometric object, to construct its increment. Proof section 1 applies precisely that theorem. Sections 2–3 use B.4, B.6 and B.9 only as algebraic results for valid shifted filtrations, which need not themselves be taut. The unchanged published source hypotheses and the actual shifted groups appear in LIN-U01 through U03.

## Constructed objects

Available: h is a polynomial of degree at most s. Needed: a fixed connected simply connected group of step at most s and a fixed lattice representing h by a linear orbit. The proof constructs P1, its coefficient Lie algebra V1, the smooth real shift, the semidirect group P1 ⋊ R, and the exact lattice Lambda1 ⋊ Z. The bracket filtration proves the step bound. The Taylor-reduction argument proves the lattice claim, rather than inheriting it from an informal suspension analogy. Evidence: sections 2–3 and LIN-U03/U04.

## Domain and index coverage

Available: integer polynomial maps in every shifted filtration. Needed: all integer inputs, positive and negative orbit powers, every shift index, and a real clock action. Coefficient descriptions define V_i through i=s and zero above; differentiation and brackets respect all indices. Integer-valued binomial polynomials cover negative arguments. The cocycle identity proves the orbit formula for all n in Z. Real shifts preserve V_i by coefficient expansion. Evidence: sections 2–4 and LIN-U02 through U05.

## Transition and comparison maps

Available: the source convention uses the left difference h(t+1)h(t)^-1. Needed: the right increment b=h(t)^-1h(t+1) for the telescoping product. Section 4 proves its membership in P1 by normality from B.6, then uses the explicitly declared semidirect product law. The compact-fiber map is evaluation at zero modulo the exact lattice; right multiplication by the integer clock removes the clock coordinate. These maps identify the orbit, rather than merely its degree. Evidence: LIN-U02/U05 and section 4.

## Identity of the consumed object

Available: the polynomial part of (b,1)^n is h(t)^-1h(t+n). Needed: the original values F(g(n)Gamma). Evaluating at zero uses h(0)=1, giving h(n)Gamma. Bounded normalization gives F_q(h(n)Gamma)=F(g(n)Gamma), and the Lipschitz extension agrees exactly on the compact fiber containing every integer orbit point. Thus the sequences and correlations are equal, with no approximation or scalar loss. Evidence: equations in sections 1, 4 and 5, LIN-U01/U05/U06.

## Coefficient and normalization conventions

Available: P_i has Lie coefficients X_j in g_(j+i). Needed: the same step s, not an unspecified finite step. The construction uses P1, with the clock at degree one, and verifies [V_i,V_j] subset V_(i+j) and differentiation V_i to V_(i+1). The full P0 suspension is expressly excluded by the recorded counterexample. Complex tests remain 1-bounded by projection onto the unit disk; the explicit extension costs only a fixed Lipschitz factor. No Gowers-norm convention changes. Evidence: sections 2, 3, 5 and 6.

## Local conditions

Available: each G_i intersect Gamma is a lattice. Needed: the polynomial lattice, semidirect lattice and compact fiber must be valid with uniform geometry. Section 3 reduces Taylor coefficients successively using fixed compact fundamental sets, proves discreteness using finitely many evaluations, and proves integer-shift invariance. Left reduction of the clock followed by polynomial reduction gives cocompactness of the semidirect lattice. Section 4 verifies the precise equivalence relation in the fiber and the well-defined evaluation map. These are deterministic group and compactness arguments, with no stopping-time or probability-law change. Evidence: LIN-U03/U04/U05.

## Exceptional cases

Available: the original filtration can have smaller actual degree, a point group, or s=1; polynomial coefficients can be unbounded and n can be negative. Needed: none of these may invalidate the construction or constants. The proof allows trivial P_i, treats the point and s=1 cases explicitly, uses bounded q rather than unbounded g(0) in the test function, and uses the cocycle identity for negative powers. Constant test functions have a constant extension and preserve the stated zero Lipschitz bound. Evidence: theorem statement and sections 1, 3–5.

## Downstream consumption

Available: an exact same-step linear representation for each polynomial nilsequence, on a nilmanifold fixed independently of its coefficients. Needed: GI(s) supplies one finite family and constants independent of N. Section 5 applies the construction separately to each member of the finite polynomial family and takes a finite maximum of the geometric constants. Correlation is unchanged by exact sequence equality. The finite polynomial inverse theorem, its ultralimit extraction and all remaining GI proof joins remain explicit premises; this unit does not discharge them. The manuscript consumers are GI(20), GI(39), and the proposed relative-inverse input at fixed k=r-1. Their current version bindings belong to the separate assembly packet.

## Related-use scope and repeated assertions

The original failure is a same-step claim for the full polynomial semidirect group. This repair checks both the real and integer clock actions on the increment group, the subgroup/lattice and fiber construction, the evaluation map, and the polynomial-to-linear finite-family join. These are the direct occurrences in Appendix C requiring the repaired object. The adverse abelian polynomial example is checked explicitly in section 6. It is not repaired merely by tautification, and no claim of that kind is retained here.

All current assertions in this packet use P1 and the same fixed step bound. The conditional GI interface remains conditional; no metadata sentence declares its corrected source qualification discharged. Historical P0 construction and prior reports are preserved. Other suspension or orbit-linearization uses in the whole GI chain remain part of the independent related-use coverage audit; this local comparison does not claim that audit complete.
