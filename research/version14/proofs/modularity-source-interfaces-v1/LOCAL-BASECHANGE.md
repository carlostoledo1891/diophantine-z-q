# Local parameter restriction for the actual modular H comparison forms

Author: /root/astra_v14_source_review. This is a new connection submitted for independent review, not a new independent decision. I previously reviewed parts of the H source chain and authored other background connections. The argument below is authored here; its later use in my assembly review must cite a separate nonauthor decision.

## 1. Exact assertion and premises

Let K be totally real and let L/K be a cyclic prime-degree totally real extension in an admissible H tower. Let pi be an already existing cuspidal parallel-weight-two Hilbert representation over K, with the finite unitary central character and coefficient embedding used in H-D4/U04. Let Pi be its cuspidal global base change over L. Assume the actual H residual nonsolvability, or equivalently for this application the previously established absolute irreducibility of all the attached restrictions in this tower. Use the same complex-to-l-adic embedding for both forms, allowing a finite coefficient extension. The prime l may be 2.

The global base-change existence and cuspidality are the retained Langlands input and the accepted H-D4 connection. U04 supplies the Galois attachments over both fields. Skinner's final 2009 equation (1) and Theorem 1 supply full Frobenius-semisimple local compatibility for each form. They apply to k_i=2,w=0 over every totally real field, including places above 2. This assertion concerns pi and Pi, which are already modular. It does not attach a form to the target rho whose modularity remains to be proved.

For every finite w of L above v of K, the conclusion is

    Rec_w(Pi_w) = Rec_v(pi_v)|W_(L_w)

up to isomorphism of Frobenius-semisimple Weil-Deligne pairs in the compatible restriction conventions specified below. The actual H conclusion needed here is the restriction of finite inertia together with preservation of N=0 or N nonzero. We do not assert literal equality of N matrices under independently chosen normalizations. This is a conclusion about this global pair. It is not a theorem for all local GL2 representations independent of globalization.

## 2. The already proved global identification

Write R_pi for Skinner's representation in his geometric-reciprocity convention. Write r_pi=R_pi^vee for its dual in the arithmetic-Frobenius H convention. Use the analogous notation over L. U04 and H-D5 identify these r's with the already attached modular comparison representations, by their characteristic-zero Hecke polynomials. They are not identified with the still nonmodular target merely because the residual representations agree.

At all but finitely many primes, global base change raises the unramified Satake roots to the residue-degree power. H-D4 Section 2 checks the normalization: if q_w=q_v^f, multiplying the unitary roots by q_v^(1/2) before taking their f-th powers is the same as multiplying after base change by q_w^(1/2). Therefore r_Pi and r_pi|G_L have the same characteristic polynomial on all Frobenius elements outside a finite set. Chebotarev and characteristic-zero Brauer-Nesbitt give equal semisimplifications. The actual residual nonsolvability implies the restriction r_pi|G_L is absolutely irreducible, as proved in H-D4 Section 3. Both representations have dimension two, so r_Pi is already irreducible and

    r_Pi = r_pi|G_L.

This is the accepted H-D4 Section 4 conclusion, used as an actual representation isomorphism. No compatibility at the ramified place under examination enters this proof. There is consequently no local base-change assumption hidden in this step.

## 3. Weil-Deligne functor and the two contragredients

For a potentially semistable l-adic representation at a place above l, use the same algebraic closure, B_st and embeddings for K_v and L_w. The union defining D_pst is unchanged on passing to the finite base field extension; the Weil action restricts and the operator N on B_st is the same. Thus the Weil-Deligne pair of a restricted representation is the restriction of its pair. At a place away from l, choose one tame additive character on the ambient inertia and restrict it. The exponential-monodromy construction gives the same statement. Choosing separately normalized tame generators can rescale N by a nonzero scalar; the usual identification of the resulting Weil-Deligne objects gives the same isomorphism class. In particular no nonzero N becomes zero.

Duality sends the Weil action to its contragredient and N to minus its transpose. Both constructions commute with restriction. Frobenius semisimplification also commutes with these operations up to isomorphism. One way to check the restriction assertion is to take a power of Frobenius centralizing finite inertia. Its unipotent Jordan factor commutes with inertia, and discarding this factor before or after taking the residue-degree power gives the same restricted semisimple pair. The semisimple factor still satisfies the same relation with N. These are the usual finite-extension and dual functorialities of WD, not a local automorphic base-change theorem.

Let

    P_K = iota Rec_v(pi_v tensor |det|_v^(-1/2)),
    P_L = iota Rec_w(Pi_w tensor |det|_w^(-1/2)).

Skinner's equation (1) away from l and Theorem 1 above l state WD(R_pi)^Fr-ss=P_K and WD(R_Pi)^Fr-ss=P_L. Applying the FIRST contragredient, to pass to the H representations, gives WD(r_pi)^Fr-ss=P_K^vee and WD(r_Pi)^Fr-ss=P_L^vee. Restrict the global isomorphism from Section 2 and use WD functoriality. It gives

    P_L^vee = (P_K^vee)|W_(L_w).

Applying the SECOND contragredient, now on Weil-Deligne pairs, gives P_L=P_K|W_(L_w). Both duals are necessary. Leaving just one would compare the contragredient local parameter and invert its inertial characters. No cyclotomic twist is inserted by these dual operations.

## 4. Removing precisely the normalized absolute-value twist

Let eta_v be the one-dimensional Weil character Rec_v(|.|_v), under Skinner's convention that a uniformizer corresponds to geometric Frobenius. Thus eta_v(Frob_v^geom)=q_v^(-1). The norm on L_w^* and restriction of Weil characters give

    eta_v|W_(L_w)=eta_w,

because geometric Frobenius at w maps to the f-th power modulo inertia and q_w=q_v^f. Equivalently |Norm_(L_w/K_v)(x)|_v=|x|_w. This uses residue degree f, not total degree ef. Choose the positive real square root on the complex side, with the same iota throughout. The same restriction identity holds for its half powers.

Compatibility of local Langlands with an unramified determinant twist says P_K=iota Rec_v(pi_v) tensor eta_v^(-1/2), and likewise for L. This unramified-twist normalization is a retained elementary property of Rec, already part of Skinner's displayed normalization. It is not the general base-change assertion being proved. Tensor the equality of Section 3 by eta_w^(1/2). The twists cancel, yielding exactly the conclusion of Section 1. There is no additional unramified quadratic choice, inverse character, Tate twist, or ramification-degree factor in the normalized parameter.

## 5. Actual H-stage consumption

Apply Sections 1-4 to each cyclic step and compose restrictions. An admissible solvable normal closure preserves residual nonsolvability, hence the absolute irreducibility and cuspidality used in Section 2. A nonnormal intermediate field can be handled by ascent to the normal closure and descent along a cyclic tower, as in H-D4; at every step the two modular attachments have the actual restriction isomorphism. A finite descent twist is tracked on both the automorphic and Galois sides as in H-D4 Section 5. No equality merely on the target's residual representation suffices.

In H003 Section 6 step 3 this supplies the local parameter of the base-changed modular comparison form at the preparatory nonordinary places. The ordinary Q2 places kept split have unchanged local factors. It does not prove the separate Kisin type-change lemmas or their ordinary/nonordinary selection. After a type change the newly constructed form is again modular and has its own attachment; a subsequent base change applies this assertion to that form, without identifying it with the previous form or the target.

At step 4, a local extension chosen to kill the finite inertia of an N=0 modular parameter makes the base-changed parameter unramified with N=0. H-D5 then supplies crystallinity and the reviewed H-D2 integral BT passage for the actual modular lattice. The target obtains its own BT property from its separately known potential-BT input and prescribed local extension. This proof does not transfer BT from the modular form to the target by residual congruence.

At step 5, after Kisin's cleaning creates ramified principal series outside the prescribed Steinberg set, killing its finite inertial characters gives trivial inertia and N=0 on the base-changed modular representation. Thus it is genuinely unramified there. At a Steinberg place N stays nonzero under restriction. The separate determinant normalization and unramified quadratic-character comparison remain required; our parameter restriction does not manufacture their equality. Further BT preservation is restriction, not descent of an integral group scheme.

Only after Proposition 3.2.9 supplies target modularity is the target eligible for the final modular descent in H-D4. The argument here supplies no earlier target form. It adds no quantitative bound and changes none of the manuscript's original controlled fields or conductor estimates.

## 6. Source and decision boundaries

This connection removes the need to read IAS Chapter 2(e) as a general ramified local-parameter theorem in these actual modular H base-change pairs, if independently accepted. It leaves the global Langlands base-change and descent theorem as an input, and leaves its original-1980 versus IAS-retypesetting edition qualification unchanged. It also leaves the exact Kisin ordinary/type-change, component, integral BT and patching inputs unchanged.

I directly read final Skinner pp.241-242 and visually checked p.242 for this argument. It explicitly states both displayed comparisons and their geometric reciprocity normalization. Its own theorem proof remains a retained published theorem input; this packet does not reprove it. The WD construction and functorialities in Section 3 are the usual period-module/tame-monodromy definitions, with Fontaine's exact local source already retained by H-D5. Their explicit derivation here distinguishes them from an unproved local automorphic base-change assertion.

In particular the claim used in H survives every nonzero scalar rescaling of N that can arise from a different tame or period normalization. The statement is not a claim that the unscaled numerical matrix attached by two independently normalized implementations agrees. The inertia representation and the dichotomy N=0 versus N nonzero are the normalization-independent outputs required at all the identified consumers.

This author packet is not an assembly approval, source-edition blanket closure, manuscript change or release authorization. The existing frozen proof and review files are unchanged. Only hash/locator metadata, not third-party full text or private correspondence, is included here.
