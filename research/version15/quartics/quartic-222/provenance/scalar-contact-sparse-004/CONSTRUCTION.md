# Sparse232 presentation

This is an exact reversible presentation of the frozen raw232 author candidate in sibling scalar-contact-quartic-001, IR87601e9690f94240e22d949b774522467572d562035d1c3143d04d4c36dc4f35. Its arithmetic status is inherited; this file does not independently approve that arithmetic.

Start from the exact accepted sparse233 MAPS.json. Omit only the row addition whose target is deleted old row71, and the coordinate shear whose only output is deleted old coordinate122. Neither operation supplies a surviving coordinate or a surviving row. Map all other row positions by their exact parent names, and all surviving coordinate indices by i -> i-1 for i>122, otherwise i. Apply the32 surviving stages in their original order. Recompute each nonzero rational primitive-normalization factor from the resulting row coefficients.

MAPS.json records all32 stages and both omitted operations. INVERSE-MAPS.json records the8 inverse affine stages, all with constant rational denominators. The verifier reverses every normalization and every row/coordinate operation, checking that all206 raw232 residuals return exactly. It also verifies each affine map in both directions. No variable-dependent division or new exceptional set is introduced; input1 and A_N stay fixed. The sum of squares has the same rational zero set because all row operations are invertible overQ.

Full expansion gives232variables,206quadraticrows,2500coordinate monomials and2501parameter-separated terms, degree4/content1. This compares with233/207/2514 in the accepted sparse parent. The coefficient height remainsA_N²+1 forN>=53; this is only the coefficient threshold, not an effective definingN0. All232coordinates occur.

No manuscript, accepted baseline or release file is modified. Independent review is required before adoption.
