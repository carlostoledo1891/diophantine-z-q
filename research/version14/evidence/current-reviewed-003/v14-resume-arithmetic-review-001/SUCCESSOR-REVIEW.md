# Arithmetic successor decisions

Reviewer: /root/v14_arithmetic_review, internal model reviewer, 2026-11-09 UTC. This adds exact successor decisions to REVIEW.md without replacing its historical assessments. The author supplied the changes; the reviewer independently checked their mathematical effect and reread the complete frozen proof texts.

## General all-prime irreducibility

Accept all-prime-irreducibility-matrix-units-002/MANIFEST.json, SHA-256 f8c0bfa8efad8ed2c83199ea0f909ae2a664b8401465add67790482f532a2f95, with PROOF.md ec1f11878335336783f65789d8d6de108170019177dfca68b4608bc3e610f107, as a conditional theorem for every rational coefficient prime, including 2. CONTRACT.json now uses the original matrix units and primitive image, rather than assuming an additional embedded quadratic coefficient field. Both changes were read directly.

The original idempotent is retained. If the computation uses different matrix units, an invertible element of the split matrix algebra conjugates the systems. Because the normalized action commutes with the quaternion algebra and coefficient scalars, that element is G_Q-equivariant and identifies the factors. The commutant and semisimplicity proof therefore concerns the original r_ell. The finite-extension argument proves absolute irreducibility, not merely irreducibility over the initial completion. There is no exception at ell=2 in characteristic-zero scalar extension.

Acceptance remains conditional on the actual common endomorphism field, full geometric End=B, the original normalized-family restriction, and the retained Faltings/coefficient-extension inputs. It does not itself attach those inputs to either family or resolve the unchanged ordinary_attachment field.

## First beta-family attachment and proposed text

Accept v14-resume-arithmetic-author-proxy-002/MANIFEST.json, SHA-256 c87a3dbd28a55b58d95af08cfc70aa571472ac2cff6c8da20426fd3d5c6d2efc, PROOF.md 0ccb4a3ee6b2ed28e52077bc23b9b0492645e59fdfb443075587077214e6b7e1, and the arithmetic argument in PROPOSED-REPLACEMENT.tex c4b7a310b5eab43a05b32e42161613770326343b1ba3039c6692541b9b1bef63. The target is manuscript 99d35bfe017ffdea59f134520a05a5ae15ccfa41c9d0004da02bee4f67431cee, proposed replacement of lines 1390-1408. Current-target transport and final source/application registration remain separate.

The beta input trace was checked against actual 99d1181-1214, 1270-1290, 1333-1355 and 1357-1408. Its L defines every geometric endomorphism and the required Hom groups. The non-CM branch has full End=B. The actual B-linear isogenies are defined over L, with identity choice on G_L. The beta kernel gives G_L-prime, where both the cochain and normalization are trivial. Thus the restriction is the original Tate action on the same A. These are first-family inputs; the D210 b-family supplier is not used.

The proof now works over an explicitly common finite coefficient extension while retaining the original embeddings and scalar-extended factor. Invariant-space dimensions and Artin/Swan conductors are unchanged by this extension. The matrix-unit argument preserves the original r_ell up to G_Q-isomorphism. The Frobenius calculation uses actual integral isogenies, whose denominators were already cleared, so no missing denominator factor occurs. The two-copy factor 1/2 is present. Relative arithmetic p-Frobenius has the correct twist target, and the trace assertion is restricted to coefficient primes different from p.

The successor selects the already reviewed published Milne1986 Proposition12.9, printed125, and the selected ordinary AC-BN and Chebotarev sources. Historical A064 supplies the connecting argument, not a replacement source version. Equality at five is an algebraic equality before embedding at ell. The trace criterion gives a global semisimplification; absolute irreducibility and composition length one recover the actual U_f,ell. Consequently restriction to a decomposition group gives an actual local isomorphism, including its possible nonsemisimple inertia action, rather than merely equal semisimplified local traces.

The final proposed TeX sentence identifying this conductor with v_p(N_f) is conditional on the separate CL1/CL2 conductor-to-level theorem application. This review does not supply or accept that external application. Nor does it reaccept full upstream geometry, sign/cochain construction, numerical field or conductor bounds, or final manuscript assembly. The original r3-at-5/r5-elsewhere choice remains valid; arbitrary ell different from p is also available from the reviewed stronger proof.

The second b-family has the same matrix-unit wording at 99d8100-8120, so the general correction fits its factor construction. This decision does not substitute beta geometry for b geometry or claim a completed b-specific all-prime application. Preserve that separate incoming ownership.
