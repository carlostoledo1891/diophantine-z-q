# Prime-conductor weight-two assembly

Author proposal by /root/astra_quartic_opt05_anchor. This reconstructs the selected Khare Corollary 1.2 application; it is not a comparison with the unavailable final Duke article. Independent review is required. Khare's author version, pp3 and 28, fixes the target and historical argument. No manuscript or prior review is changed.

## 1. Target and source premises

Let p>2. Let rbar be odd, absolutely irreducible and two-dimensional over a finite field of characteristic p, with Serre weight 2 and prime-to-p Artin conductor a prime q. Thus q differs from p. The target is modularity in weight 2 and level Gamma_1(q).

Retain the upstream level-one theorem at odd residual primes. Do not use the full later Serre theorem to prove this consequence. Retain also classical modularity of odd dihedral residual representations and the established residual weight/level refinement. That refinement is needed for the initial dihedral branch if it is handled before constructing a lift. Final early KW, Annals169(2009), p247 explicitly invokes this dihedral input. These are named inputs, not conclusions of this packet.

The main construction uses final early KW Theorems3.3 and4.2(i), pp239,244, including the actual proof on245. Standard local inputs are the exact potentially semistable comparison functor, duality, weak admissibility, local class field theory and the Artin-conductor formula. Crystalline representations of weights(0,1) are Barsotti-Tate, in the precise rational sense used in final Kisin's proof of Lemma2.3.8, which cites Breuil. These theories and their proof ancestors remain explicit inputs.

## 2. Initial reduction and minimal system

If rbar restricted to G_Q(mu_p) is reducible, Clifford theory for this normal subgroup makes rbar dihedral. Indeed a nonscalar restriction has two character constituents permuted through an index-two subgroup; a scalar restriction would leave cyclic projective image, incompatible with absolute irreducibility. The retained classical dihedral modularity and residual weight/level refinement settle this branch.

Otherwise final early KW Theorem3.3 gives a minimal weight-two lift V_p. Its conductor away from p is q; its determinant is epsilon_p times the Teichmuller lift of the residual prime-to-p character, by pp237-238. Theorem4.2(i) puts it in the actual absolutely irreducible compatible system R=(V_iota), over a number field. Keep the specified original p-embedding. Coefficient extensions extend embeddings; they do not replace V_p by another lift.

The case q=2 can be excluded before this construction. Artin conductor exponent1 means zero Swan conductor and a one-dimensional inertia-invariant space. The other semisimple tame inertia character is fixed by Frobenius and hence has order dividing q-1. At q=2 it is trivial. Inertia is unipotent, so rbar is semistable in final early KW Theorem5.2(ii)'s sense. That theorem, p247, excludes conductor2 and weight2 for p>2. Henceforth q is odd.

## 3. The actual ramified q-member

Unramified coefficient-prime compatibility is insufficient here. Use the construction on final early KW p245. Let F/Q be its finite totally real Galois potential-modularity field. That page states that for each F' in F with F/F' solvable, the entire constructed system restricted to G_F' comes from one Hilbert cuspidal representation pi_F'. This is a statement about the characteristic-zero system, not just its residual representation.

Choose Q|q in F. Let D_Q be its decomposition group and F_0=F^{D_Q}. The local Galois group D_Q is solvable: wild inertia is a q-group, tame inertia modulo wild inertia is cyclic, and the residue quotient is cyclic. Thus F/F_0 is solvable. At the selected place v, (F_0)_v=Q_q, since its completion is the fixed field of D_Q in F_Q.

Apply the construction-level statement to pi_0=pi_F_0. Both the p-member and the selected q-member restrict to the corresponding members attached to pi_0. Final Skinner, DocumentaMath14(2009), equation(1) and Theorem1, pp241-243, now apply to the SAME pi_0 at v. Equation(1) identifies the p-member's WD parameter because p differs from q. Theorem1 makes the q-member potentially semistable and identifies its WD parameter. Both use Rec_v(pi_{0,v} tensor |det|_v^(-1/2)), with geometric reciprocity as fixed on242. Their coefficient embeddings are extended consistently.

The arithmetic weight-two normalization has finite central character, hence Skinner's infinity parameters are k_i=2,w=0. His Hodge-Tate graded degrees are then -1,0, equivalent to V tensor C_q = C_q plus C_q(1), which is the early KW weight-two convention. If comparison is expressed through the dual cohomological realization, the same dual is taken for both members. No one-sided dual or norm twist is inserted. The selected local field is Q_q, not a higher-degree extension.

Therefore WD(V_q|G_Qq) and WD(V_p|G_Qq), after Frobenius semisimplification, identify with the same algebraic local parameter. Their inertia and N agree up to isomorphism. Frobenius semisimplification does not discard N. This is stronger than equality of traces or equality in a Grothendieck group. V_q has weights(0,1). This argument concerns this actually constructed system only; it does not assert ramified compatibility for an arbitrary weakly compatible system.

## 4. Conductor-one local alternatives

The common WD parameter (r,N) has conductor1. The formula a(r,N)=a(r)+dim(r^I)-dim((ker N)^I) forces Swan=0 and dim((ker N)^I)=1.

If N=0, finite inertia is semisimple and r|I=1 plus eta for a nontrivial tame character eta. Frobenius preserves the unique trivial-character summand, so eta is fixed by the q-power action. Its order divides q-1. This type is killed by Q_q(mu_q). V_q becomes crystalline over that extension, with weights(0,1), and the retained crystalline/BT implication makes it Barsotti-Tate there. Scalar type would have conductor0 and is absent in this exact branch.

If N is nonzero, it has rank1. Its commuting finite inertia has the same character on kernel and quotient; the invariant kernel forces that character to be trivial. V_q is semistable over Q_q and noncrystalline. It is ordinary by the following calculation.

Set D=D_st(V_q dual), with filtration jumps0,1 and total Newton number1. The relation N phi=q phi N gives eigenvalues alpha and q alpha, with alpha on ker N. Thus 2 v_q(alpha)+1=1, so alpha is a unit. Weak admissibility on ker N forces its filtration jump to be0. It is a weakly admissible rank-one subobject, so under the contravariant semistable equivalence it gives an unramified quotient of V_q. The other character has weight1. For a stable lattice, the kernel intersection is saturated, and the quotient is free rank1 and unramified. This is the integral ordinary condition of final early KW Definition3.1, p237. No BT assertion is made in this N-nonzero branch.

## 5. Residual modularity and ordinary lifting

V_q is unramified outside q. At p, this uses the unramified WD parameter of the original crystalline p-member and the system definition; elsewhere it uses minimality. Its residual semisimplification rbar_q is odd and unramified outside q. If absolutely irreducible, it is modular by the retained level-one theorem. If geometrically reducible, it is modular in the EXACT definition on final early KW p230, which explicitly includes odd geometrically reducible representations. This checks the terminology of Theorem5.1 rather than equating reducibility with a cuspidal congruence.

Determinant compatibility gives det(V_q)=epsilon_q psi_q, for the same finite even character psi of conductor dividing q supplied by the minimal p-lift. Equality follows from equal good Frobenius values and Chebotarev. The mod-q inertia character of psi has an even exponent as a power of omega_q, since psi is even. Hence det(rbar_q)|I_q is an odd power of omega_q. A global Teichmuller cyclotomic twist changes that exponent by an even integer.

If N is nonzero, Section4 gives ordinarity. Final early KW Theorem5.1, p246, applies: absolute irreducibility, finite ramification, an ordinary stable lattice, weights(0,1), modular reduction under its p230 convention, and odd inertia determinant are all verified. It gives a weight-two newform. Its Skinner-Wiles proof ancestors remain inputs.

Suppose N=0 and rbar_q is locally reducible. The separately reviewed nonscalar tame ordinary connection applies to V_q: the type is 1 plus eta, eta has order dividing q-1, and V_q is BT over Q_q(mu_q). A global Teichmuller cyclotomic twist makes V_q ordinary. The determinant and residual-modularity checks survive the twist. Apply Theorem5.1 and then untwist the automorphic representation. The type, covariant/dual convention and arbitrary-lattice conclusions remain bound to the accepted tame packet and its required record successor, including its corrected-Savitt source qualification.

This includes globally reducible rbar_q. It also includes absolutely irreducible rbar_q whose restriction to K_q=Q(sqrt((-1)^((q-1)/2)q)) is reducible: the separately reviewed strict-level-one dihedral connection forces local reducibility at q. Apply that lemma to rbar_q, not to the original conductor-q representation in characteristic p. A global cyclotomic weight normalization does not alter local reducibility.

## 6. Remaining potentially BT branch

The remaining N=0 case has rbar_q|G_K_q absolutely irreducible. Apply final Kisin, Annals170(2009), Corollary3.5.8, pp1172-1173, also the theorem on1086. Its Q-hypotheses are precisely: V_q potentially BT at q; determinant epsilon_q times a finite character; modular reduction; and absolute irreducibility over K_q. All have been established. A stable lattice exists after a finite coefficient extension. Thus V_q is modular.

We use this actual Q-corollary, not Hilbert Theorem3.5.5 with unverified strong-residual-modularity or projective-image hypotheses deleted. The corollary's proof and its named local-model, modularity and weight-two inputs remain published ancestors. Nor do we invoke the optional Gee extension removing a residue-field hypothesis. No new audit of all those ancestors is asserted.

## 7. Return to the original member and exact level

The modular V_q belongs to a full modular family of a classical eigenform f. Enlarge coefficient fields to a common number field while preserving the q-embedding and original p-embedding. Equal characteristic-zero Frobenius polynomials outside a finite set identify the p-member of that modular family with the original absolutely irreducible V_p by Chebotarev and Brauer-Nesbitt. This is not an inference from one residual congruence.

For the exact level, apply final Skinner equation(1) and Theorem1 directly to this same classical form f over Q, with its possibly nontrivial finite nebentype. Its attached q-member is the original V_q after undoing the finite twist. Equation(1) identifies the local parameters at all finite places other than q; Theorem1 identifies the parameter at q. The latter has conductor1 by Section4, and all others are unramified. Thus the primitive f has level q. The lifting theorem and the Hodge-Tate weights give weight2. This uses the general-nebentype Skinner statement, not the trivial-nebentype DFG normalization argument in an earlier transfer packet. All finite twists are undone before reading the conductor. The p-member reduces to rbar in the original embedding. This proves the target in the non-dihedral branch. The retained residual weight/level refinement handles the initial dihedral branch.

## 8. Exact scope and remaining obligations

The new connections are the decomposition-field use at a ramified coefficient prime, the conductor-one local case split including N, and their composition with the published Q-corollary and accepted local replacements. The argument retains the upstream level-one theorem, classical dihedral modularity/refinement, full modular-family local compatibility, the published lifting theorems, period equivalences, class field theory, and Chebotarev/Brauer-Nesbitt. It is not a proof of those sources from first principles.

Dependency order is the level-one theorem, then this prime-conductor corollary, then later uses of that corollary in KW. The full later Serre theorem is never an input. Before adoption, the assembled level-one proof must separately be checked not to depend on this corollary. This packet does not supply the original induction or prime-selection arguments.

Independent acceptance of this exact reconstruction and its caller-graph adoption remain pending. The final Khare source comparison remains unclaimed. The accepted nonscalar replacement retains its original-Savitt-final-edition qualification; the independently accepted published corrigendum comparison does not erase it. The current packet does not need a purchase to state its proposed proof, but it does not itself declare all source qualifications or the release closed.
