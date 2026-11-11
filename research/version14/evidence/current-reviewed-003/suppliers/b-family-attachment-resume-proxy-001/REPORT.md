# The second family's all-prime application

Author: /root/v14_arithmetic_author. Status: proposed, awaiting independent review. The target is classical-local-tex-integration-root-002/PROPOSED.tex, SHA-256 99d35bfe017ffdea59f134520a05a5ae15ccfa41c9d0004da02bee4f67431cee. This report concerns the discriminant-210 b-family only. It does not use the first beta-family's geometric construction.

## Actual supplying objects

The non-CM level-bound introduction specifies the actual fiber A/L, the normal field L with degree dividing 576, all geometric homomorphisms between conjugate fibers defined over L, and the full geometric algebra End^0(A_Qbar)=B of discriminant 210. The current scalar-lift paragraph chooses B-compatible isogenies mu_sigma over this L, with mu_1=1, inflated from Gal(L/Q). Its normalized cochain is b, with b^2=chi and delta b=epsilon. LR3 defines L' by the kernel of b on G_L. These are the objects in the representations at lines 8100-8120.

The actual geometric supplier is the ordinary002 candidate's h5-full-three-v1/GEOMETRIC-ISOGENY.md. Section 3 obtains the full algebra B from the retained Hodge-centralizer and descent arguments in the non-CM case. Section 5 supplies the common field L for all homomorphisms and their rationalizations. We use these full-algebra and common-field conclusions, not merely Section 4's compatibility with a specified quadratic field.

The corresponding SCALAR-NORMALIZER.md Sections 1-2 retain the same full-three PEL fiber and prove B-linearity on every component. Section 4 chooses the actual finite family mu_sigma: sigma A to A, with mu_1=1, shows that its discrepancy is central in B and hence rational, and applies the Tate functor at every coefficient prime with the same composition identities. The prime-to-11 construction in Section 3 supports the separate torsion caller; no prime-to-ell property of the isogenies is required here because the representations are rational Tate modules.

The ordinary002 FAMILY-CONNECTION.md identifies the same normalized family rho_ell=b^-1 a mu composed with sigma and its restriction to G_L'. In that subgroup the inflated mu is the identity, a=1 and b=1. Thus this restriction is the actual Tate action of A. Since L' contains L, every geometric endomorphism is defined over L' as well. No new definition field is constructed.

## Application at every coefficient prime

Apply the accepted all-prime-irreducibility-matrix-units-002 argument with this A, this L', and this full B. Its original primitive-idempotent formulation applies directly to the matrix-unit factor in the current construction. No embedded quadratic coefficient field is required. If matrix units are chosen after changing a splitting, conjugation by an invertible element of the split B identifies their primitive images; this element commutes with rho_ell, so the identification is G_Q-equivariant.

For clarity, Faltings gives semisimplicity and End_G_L'(V_ell(A))=B tensor Q_ell. After finite coefficient extension the commutant is M_2(F_ell). The original decomposition is F_ell^2 tensor r_ell, so the factor has scalar commutant. Semisimplicity and the same calculation over each finite extension imply absolute irreducibility, including at ell=2. These are exactly the supplied hypotheses of the accepted general proof. This is a new application for all ell, not a change to the scope of the old prime-three receipt.

The current paragraph identifies the original r_5 with a primitive weight-two form f. It explicitly distinguishes the finite character delta absorbed to obtain f from the controlled character chi=b^2. The all-prime comparison retains that same f and the original b, L', and r_ell. It does not absorb a new twist into the controlled family.

Apply all-prime-compatibility-sol-001 to eta=b, using the original matrix-unit factor and the just-established all-prime irreducibility. The required map and trace calculation is supplied concretely by ordinary002 FIVE-TO-THREE-CONNECTION.md, with the variable ell in place of 3. At a good comparison prime p different from 5 and ell, choose an arithmetic Q_p-Frobenius lift sigma_p, acting on residues by x maps to x^p. Its relative p-Frobenius goes from A_v to its sigma_p twist. Composing with the reduction of mu_sigma_p gives an endomorphism. If a common integer m is used to clear quasi-isogeny denominators, the rational endomorphism is e_p/m and its trace is Tr(e_p)/m; the factor must not be dropped. The current maps are actual isogenies, so m=1 is available.

The degree-polynomial supplier is the already selected Milne, Abelian Varieties (1986), Proposition 12.9, printed p.125. Prime-to-p torsion specialization gives

    tr(r_ell(sigma_p)) = iota_ell(a_sigma_p b(sigma_p)^(-1) Tr(e_p)/(2m)).

This formula is asserted only for ell different from p. The one-half comes from the two-copy decomposition. Exclude the finite spreading set, 5, ell and the primes dividing N. These comparison exceptions do not replace or enlarge T in any bound. Enlarge the algebraic coefficient field to contain f's coefficients, extending the original embeddings and retaining the embedding at five. At ell use a common finite extension F/Q_ell containing both coefficient images. The isomorphism below is over F and compares the scalar extension of the original r_ell.

At five the algebraic trace is a_p(f); injectivity makes that an equality in the common number field. Transport to ell, Chebotarev, and the selected characteristic-zero trace criterion give r_ell tensor F = U_f,ell^ss over F. The absolute irreducibility of r_ell forces that semisimplification to have one simple composition factor. Therefore the actual U_f,ell has length one and is isomorphic to r_ell tensor F. The external density, trace and classical-realization inputs are the same selected ordinary002 inputs; their source versions are not changed here.

## Consumers and scope

For each residue prime p select ell different from p and restrict the actual isomorphism to the same decomposition group. It identifies inertia, higher ramification and the full local representation, not merely unramified traces. Coefficient extension preserves invariant-space dimensions and the Artin and Swan conductors. Thus the local conductor of the original r_ell equals that of the corresponding U_f,ell. The equality with v_p(N) is the separately reviewed CL1/CL2 input. The current choices r_3 at p=5 and r_5 elsewhere remain available. No fixed r_3 prime-to-ell conductor calculation is asserted at p=3.

The numerical local estimates and the level bound keep the same original controlled family. The C6 Jacobian-placement use remains separate and unchanged. This packet supplies neither a new conductor-level theorem nor a new quantitative estimate. Upstream full-three geometry, sign construction and source versions retain their existing scoped decisions. No historical unresolved status is overwritten.

## Ordinary contract ownership

Add two current applications, COV-B-ALL-PRIME-IRREDUCIBILITY and COV-B-ALL-PRIME-COMPATIBILITY, authored by this agent and accepted only by a non-author reviewer. The former uses the general matrixunits002 proof, the b-family full-End/common-field suppliers, H5-B-SCALAR-DISCREPANCIES, CURRENT-A007-RAMIFICATION and QM-SEMISIMPLE-BASE-CHANGE. The latter uses the former, DIRECT-SECOND-CALLER, the retained Frobenius/degree-polynomial connection, AC-CHEBOTAREV and AC-BRAUER-NESBITT. Bind their construction, application and consumer spans to the assembled manuscript after adoption.

Retain COV-R3-ABSOLUTE-IRREDUCIBILITY and COV-FIVE-TO-THREE as their exact historical scopes. Do not overwrite their prime-three predicates or the 45 unresolved status fields in ordinary002 to claim a universal result. Copy their relevant direct source uses into new universally quantified current uses, retaining distinct full-End and common-field inputs rather than routing both through the normalizer-map input. The new compatibility application provides the actual local-representation input to CL1/CL2. CL1/CL2 owns the level equality and the local-bound argument owns the numerical inequality. The original 3-and-5 choices can be retained for the level-bound caller.

EDIT1.tex makes the full geometric field-of-definition input explicit at the existing irreducibility sentence. EDIT2.tex replaces only the comparison from 'The conductor at $5$ is not omitted.' through 'conductor at $5$ and $r_5$ at every other prime.' The following modular-level/CL1/CL2 discussion is outside this edit and remains under its own owner. The proposal does not edit canonical TeX or any old record.
