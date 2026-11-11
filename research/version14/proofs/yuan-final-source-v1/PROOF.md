# Published Yuan source and the direct stack argument

Authors of this source-use reconciliation: root, drawing on the explicitly attributed analysis of `/root/astra_quartic_opt05_anchor`. This proposal awaits independent acceptance. It does not alter Yuan's theorem or provide a new proof of it.

The source is Xinyi Yuan, Explicit Kodaira–Spencer maps over Shimura curves, Acta Mathematica Sinica, Chinese Series 67 (2024), 227–249, DOI10.12386/A20220154. The published Chinese file and April30,2024 English file have separate hashes in SOURCE-PINS.json. This comparison concerns the current maximal-stack height argument only.

## Exact published suppliers

Section2.1 on230–231 states the integral moduli-stack properties used here: regularity, flatness, semistability, smoothness away the quaternion discriminant and properness when the quaternion algebra is a division algebra. For maximal level n(U)=1. Our discriminant is210. The actual principal level is U(3), so the fine-level property does not rely on reading the source's general containment phrasing in the wrong direction.

Theorem1.1 on229 gives the injection from the square of the Hodge line to the square of the stack dualizing line, with image d_B times that target, and states its isometry. The source's norm definitions are on228–229. In particular the Petersson norm of d tau is2 Im(tau). These are the integral and metric conclusions the present H5 proof needs.

The manuscript first constructs generic-fiber bicanonical sections q_i. It then proves integrality of J^2 q_i directly on the maximal regular stack at vertical generic points. Semistability supplies a uniformizer p; the relative differential kills p. The displayed valuation inequalities control the poles. Regularity extends the sections across codimension two. This step does not construct a coarse-model line bundle or invoke an integral coarse-to-stack pullback. The independent tame-cover argument runs only over Z[1/210], where its finite group orders are invertible. Neither step asserts a tame coarse cover at the bad primes.

The point is then evaluated on the proper maximal stack. The source isometry applies to that same stack and universal abelian scheme. The existing curvature, norm, arithmetic degree and normalization computations remain separate manuscript arguments. They are not extra conclusions attributed to Yuan. In particular the positive log210 term arises when solving the sublattice-height relation for the target height, not from reversing the injection.

## The source-proof difference is preserved

The final Chinese Lemma2.1, on232–233, has a shorter proof than the English version on8–10. Its last separability inference does not follow merely from the stated flatness and reduced-fiber properties. The general inference is tested by the finite flat map Z_p[t] to Z_p[x], t=x^p, localized at the vertical generic points. Both special fibers are geometrically reduced over F_p, but the residue extension F_p(t) to F_p(x) is purely inseparable. This is not a Shimura moduli map and does not disprove the lemma. The English proof supplies additional geometric stabilizer arguments; their mere presence does not certify all their inputs.

That finding remains SOURCE-YUAN-LEMMA21-SEPARABILITY. The current height calculation avoids the coarse Lemma2.1 and the coarse arithmetic-intersection consequence Theorem2.2. It instead uses the stack statements identified above and its own direct vertical-section construction. The independent review must also inspect the proof of Theorem1.1 to check that the disputed coarse lemma is not an indirect premise. No claim is made that the complete Chinese and English proofs agree.

Earlier records that used only the author-attested English translation remain historical. Their broad YKS-COARSE card is not silently promoted to a current supplier. Direct uses of Lemma2.1, Theorem2.2 or the related similar-proof Lemma5.2 outside this precise stack argument still require a separate disposition. Current-source edits and incorporation are bound separately; this note supplies neither full inventory coverage nor final release approval.
