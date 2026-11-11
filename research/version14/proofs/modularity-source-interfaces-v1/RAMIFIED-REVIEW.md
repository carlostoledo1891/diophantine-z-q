# Independent review of the H-D5 local connections

Reviewer: /root/astra_v14_baseline_gaussian. Author: /root/astra_v14_assertions_arithmetic.

This review concerns the new local source-to-consumer transitions, conditional on the retained inputs identified below. I authored U04's attachment proposal, the staged H003 proposal, and F01's component proposal. Their separate independent decisions are reused only within their accepted scopes; this review does not independently reapprove them. The new use of Skinner Theorem 1 and the explicit period-module descent were not authored by me. During review I requested that the author distinguish an already modular comparison representation from the target whose modularity is still being proved. That clarification must remain explicit.

## Published source and representation

I read final Skinner pp.241-243 and visually checked p.242, including Theorem 1, the definition of the Hodge indices, geometric reciprocity, and the WD comparison. Its hypotheses permit every coefficient prime, including 2, and every totally real degree. With k_i=2,w=0 the infinity type applies to the weight-two forms in the actual caller. Page 243 explicitly includes the even-degree case without a finite discrete-series place; importing only Saito's restricted case would leave that case untreated.

The externally accepted U04 convention identifies the already attached modular representation rho_f or rho_g with the dual of Skinner's rho_pi, using the same coefficient embedding and characteristic-zero Hecke data at almost all places. This is not an identification of the still nonmodular target rho with rho_f. Their residual equality alone gives no such conclusion. The target's local assumptions retain their independent origin. Once the modular representation is identified globally, restricting that isomorphism gives the representation to which the new local theorem is applied.

## Inertia, monodromy, and weights

The Frobenius semisimplification in the published comparison retains the inertia representation and the operator N up to isomorphism. Thus it suffices for the claimed zero/nonzero tests. On a dual N is minus its transpose; inertia is contragredient. Trivial inertia and zero or nonzero N are therefore preserved. No assertion about the omitted unipotent part of Frobenius is required.

The displayed Hodge indices have gap one at k_i=2. Duality preserves that gap. In the stated covariant Tate convention the actual modular determinant is a finite character times the cyclotomic character, of weight one at every local embedding. The two integer weights consequently have sum one and gap one, forcing 0 and 1. This uses the determinant and the same convention as the reviewed integral BT input; it does not infer the sign or common shift from a Frobenius trace. Potential semistability supplied by the theorem ensures the needed Hodge-Tate property.

## Period descent and crystallinity

I read Fontaine's final Expose III 4.2.5-6 and 5.1.4-7, and visually checked pp.146-147 and 157-158. In particular 4.2.5 identifies the essential image of scalar extension with modules on which relative inertia acts trivially, with quasi-inverse given by Galois invariants. This is the relevant module descent, not descent of an integral group scheme.

Let L/K be finite Galois and make the representation semistable. D_st,L is full-dimensional over L_0 and carries semilinear Gal(L/K) action. Trivial inertia on D_pst implies that the inertia subgroup acts trivially on D_st,L. The remaining action is semilinear for the finite unramified extension L_0/K_0. Galois descent preserves rank. Its invariant module is D_st,K by taking successive invariants inside B_st tensor V. Fontaine's dimension criterion then gives semistability over K itself. This argument does not require K to be unramified over Q2.

Fontaine 5.1.6 identifies D_cris,K with ker(N) inside D_st,K. Thus zero N makes D_cris full-dimensional and gives crystallinity. Nonzero N prevents that equality. The published dual compatibility in 5.1.7(ii) also confirms that the preceding dual operation respects the period modules. Forgetting E coefficients, or splitting coefficient factors after scalar extension, does not change these tests. A finite local extension killing a finite inertial type exists, and restriction preserves N=0; hence the same argument gives crystallinity after that extension for the principal-series and cuspidal N=0 cases.

## Actual local consumers and limits

I read final Kisin pp.630-633. At the early ordinary step the representation attached to f' is the one asserted to arise from a p-divisible group when its local type is trivial; for the special type the needed conclusion is semistability with weights 0,1. The new source connection supplies these rational local conclusions. The integral passage uses the independently reviewed H-D2 Kim comparison for the actual lattice, including its crystalline full-faithfulness premise. It neither chooses a substitute lattice nor descends a group scheme through a ramified extension.

For the later cuspidal or ramified principal-series cases, trivializing finite inertia with N=0 gives the claimed crystalline restriction. At places away from 2, the usual WD construction gives actual unramifiedness from trivial finite inertia and N=0. Removing special type alone would be insufficient; final Kisin p.633 also requires the subsequent extension killing finite inertial characters. The proposed connection respects that order.

The ordinary filtration and exact unramified gamma, the construction of the new automorphic types, local automorphic base change with parameter restriction, and preservation of the chosen ordinary/nonordinary component remain distinct premises. This review does not derive any of them from potential semistability. It also does not reapprove F01, the field-prescription theorem, U04, or the complete proof ancestry of Skinner's published theorem. No whole-H, whole-Serre, or manuscript acceptance follows.

The precise target and bounded decision are recorded in DECISION.json after readback of the author successor. The earlier 001 target is preserved in the history; the object clarification does not change any period-module calculation.
