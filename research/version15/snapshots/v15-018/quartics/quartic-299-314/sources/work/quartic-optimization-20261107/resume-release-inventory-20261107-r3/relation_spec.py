"""Manually reconciled inventory interfaces, not a union of the r2 lists.

An edge records a direct changed application, exact transport, or explicitly
restored hypothesis of the named baseline application. It is not a claim that
every transitive consumer is listed or that every edge uses new arithmetic.
"""
SPEC = {
 1: ('H-EXACT-RESCALING SHARED-RECIPROCAL H-SUBTRACTION RECIPROCAL-IDENTITY SCALAR-NORM24 H-NO-ROOT',
     'The affine Kummer map preserves the physical H, subtraction and scalar inputs; the restored H value also licenses the retained no-root denominator argument.'),
 2: ('H-EXACT-RESCALING H-SUBTRACTION H-NO-ROOT H-HALF-INDEX SCALAR-NORM24',
     'Reconstruction on UQ nonzero restores the exact H and comparison values consumed by the half-index, subtraction, no-root and scalar-norm interfaces.'),
 3: ('V0-EXCLUSION H-TORSION-EXCLUSION H-HALF-INDEX HEIGHT HEIGHT-CONTRADICTIONS H-NO-ROOT H-LOG-IDENTITIES H-EXACT-RESCALING',
     'The two new squared-H branches require a pre-H unit/height contradiction. Excluding them licenses the H reconstruction and its domain-dependent index, torsion, logarithm and no-root steps.'),
 4: ('HEIGHT GROUPED-POLYNOMIALS TORIC-POWERS FACTORED-POLES PREPARATION-CONIC HEIGHT-CONTRADICTIONS',
     'The new R and B are consumed by the detector powers and pole obstruction. Their local implication restores the orders used by the height argument and its contradictions.'),
 5: ('REAL-INITIAL FINITE-SUPPORT REAL-FINAL-CRT PREPARATION-ZERO FACTORED-POLES FINAL-COMPLETENESS',
     'The replacement B needs new finite support, small-prime, real and ordered final-witness checks before the same preparation and pole realization apply.'),
 6: ('V0-EXCLUSION HEIGHT-CONTRADICTIONS FACTORED-POLES PREPARATION-CONIC',
     'Conditional trace/B nonvanishing is used only at required contacts, while the radical-free exceptional case uses the retained height contradiction.'),
 7: ('MODEL ODD-NORM ANCHOR-COEFFICIENT ANCHOR-RESCALING',
     'The model supplies integral indices; the old anchor and coefficient lemma now prove S oddness before restoring its deleted odd chart.'),
 8: ('ODD-NORM MODEL ANCHOR-RESCALING FINAL-COMPLETENESS',
     'The global S sign action and half point restore the odd chart and private anchor with the same physical input; both directions belong to whole-witness reconstruction.'),
 9: ('BIQUADRATIC H-SUBTRACTION V0-EXCLUSION LOG-APPROX GROUPED-POLYNOMIALS',
     'The primary biquadratic outputs, Kummer identity and logarithm caches provide the actual pre-H valuation classes and grouped leaves.'),
 10: ('GROUPED-POLYNOMIALS HEIGHT LOG-TRANSFER HEIGHT-CONTRADICTIONS REAL-FINAL-CRT FINAL-COMPLETENESS',
      'Four-group separation supplies the common-place depths consumed by log transfer and height; its original Pi19 witness construction also checks the final real/CRT choice.'),
 11: ('GROUPED-POLYNOMIALS LOG-TRANSFER REAL-FINAL-CRT FINAL-COMPLETENESS',
      'Only on the strong-H alternative, the stronger H slot changes the grouped depth and requires the Pi39 completion; this is not a selected315 premise.'),
 12: ('TORIC-POWERS SOS-FINITE',
      'The exact Laurent-helper map changes power equations and their polynomial presentation while preserving all outputs; it is not the baseline constant-pivot elimination.'),
 13: ('GROUPED-POLYNOMIALS BIQUADRATIC HEIGHT LOG-TRANSFER V0-EXCLUSION HEIGHT-CONTRADICTIONS H-TORSION-EXCLUSION H-LOG-IDENTITIES TORIC-POWERS',
      'Three-group separation consumes the actual biquadratic leaves and E157/E39 powers, supplies the common-place orders, and licenses the pre-ratio torsion and H-log domain arguments.'),
 14: ('LOG-APPROX LOG-TRANSFER REAL-INITIAL FINITE-SUPPORT REAL-FINAL-CRT PREPARATION-ZERO FINAL-COMPLETENESS',
      'The actual G2 precision12, primary precision80 and Pi19 progression supply the revised margins and require the same ordered small-prime/real/pole completion.'),
 15: ('MODEL ODD-NORM ANCHOR-COEFFICIENT',
      'The new root abscissa coefficient formulas use the fixed model and furnish the parity and local integrality facts needed beside the scalar coefficient formula.'),
 16: ('ODD-NORM ANCHOR-RESCALING ANCHOR-COEFFICIENT HEIGHT HEIGHT-CONTRADICTIONS FINAL-COMPLETENESS SCALAR-HEIGHT',
      'The shifted quaternion parameter changes a real theorem application. It restores root oddness and the old anchor, including the lower bound explicitly used in the scalar-height inequality, and needs new private witnesses.'),
 17: ('MODEL ODD-NORM BIQUADRATIC FINAL-COMPLETENESS',
      'The A,T,Z sign actions restore actual half charts and preserve the biquadratic point rows; the full solution reconstruction is used in the completion proof.'),
 18: ('ANCHOR-RESCALING CONSTANT-PIVOT SOS-FINITE FINITE-COUNTS ORDINARY-GATE FINAL-COMPLETENESS',
      'The private unscaling and uniquely defined Q elimination are exact maps, change the finite anchor polynomial and ordinary-lift degree constraint, and extend complete witnesses without new arithmetic.'),
 19: ('ANCHOR-COEFFICIENT ANCHOR-RESCALING ODD-NORM FINAL-COMPLETENESS',
      'Only in the alternative358 branch, the squared-g1 valuation equality licenses a different quaternion parameter and the same root-parity restoration with fresh private witnesses.'),
 20: ('TORIC-POWERS GROUPED-POLYNOMIALS FINAL-COMPLETENESS SOS-FINITE FINITE-COUNTS',
      'The shorter chain gives exactly the old grouped weights; its unique private assignments preserve completion and change the finite system and count.'),
 21: ('ORDINARY-GATE ANCHOR-RESCALING SOS-FINITE FINITE-COUNTS FINAL-COMPLETENESS',
      'Only on exact319, the constant chain and Q lift restore the fixed coefficient exactly and provide bijective ordinary extensions with separately checked tables.'),
 22: ('LOG-TRANSFER GROUPED-POLYNOMIALS FINAL-COMPLETENESS SOS-FINITE FINITE-COUNTS',
      'The affine Lucas recentering preserves the physical polynomial F fed by the logarithm comparisons and consumed by grouped tests; the exact witness map and finite table change, but the input parity lemma does not.'),
 23: ('ORDINARY-GATE FINITE-COUNTS',
      'The optional lower bound concerns only the explicit isolated constant-chain architecture and fixed Q lift, not any arithmetic soundness or completeness premise.'),
}

# Explicitly rejected r2 edges. Every other disputed edge is retained for the
# reason in its manually specified entry above. No union operation is used.
REJECTED = {
 ('V13-IDENTITY-CHARTS',2): 'The unchanged Ui/Vi identity-inclusive charts are not the new squared-H exceptional branches. Their independent zero-numerator proof is untouched.',
 ('V13-IDENTITY-CHARTS',3): 'N03 excludes new H/V0 reconstruction branches; it does not change the accepted Ui=O or Vi=O chart extension.',
 ('V13-BIQUADRATIC',3): 'N03 uses the squared-H Kummer branch classification, not a change to the primary biquadratic identities. Those identities are consumed explicitly by N09 and N13.',
 ('V13-INPUT-PARITY',13): 'N13 restores local comparison depths. The parity bridge beta odd implies X integral remains unchanged and is reached through the separately listed height contradiction.',
 ('V13-SCALAR-TORSION-LOG',7): 'S parity restores its odd chart and old anchor. The scalar torsion/log step still uses the same integral group identity and local formal cases, without a new parity application.',
 ('V13-CONSTANT-PIVOT',12): 'The Laurent-helper equivalence uses retained nonzero E/R, not the constant-pivot elimination principle. It belongs under TORIC-POWERS and SOS-FINITE.',
 ('V13-INPUT-PARITY',22): 'The sparse Lucas helper map fixes all physical outputs. It neither changes nor reproves the beta/X parity bridge.',
}
