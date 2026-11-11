# Author scope and related-use finding

Author /root/sol_protocol_final_review. This packet supplies LP02 and LP03 as a project proof conditional on the linked shift unit and the specified published inputs. It is ready for nonauthor scrutiny. No independent decision or complete inverse-theorem acceptance is asserted.

## Finding GTZ-LP-VECTOR-SCALAR-SHIFT

The available result of published E.5 is a finite sum of scalar contractions of vector-valued unit nilcharacters, each multiplied by a lower-degree factor. The erratum p.4 moves a purported scalar nilcharacter from n to n+h by an identity which requires modulus one at n+h. E.5 does not supply that property for a coordinate. For example the first coordinate of the constant unit vector (1/2, sqrt(3)/2) is 1/2, and multiplying it by its shifted squared modulus gives 1/8 rather than 1/2. A coordinate may also vanish, so division by it is unavailable.

The required result is a finite sum with the higher-degree factor depending only on k and m=n+h. The proof retains the vector and inserts the sum of squared moduli of all coordinates at m. Every matrix entry of the two-time outer product is lower degree by the linked shift result, and finite pigeonholing selects a term without a vanishing denominator. The proof uses a standard finite number of entries and makes no parameterwise scalar-unit choice.

## Bounded related-use check

Scope covers the E.5 supplier, the immediately following E.6, original Section 8 and the erratum's two Cauchy–Schwarz pages. It also covers the actual two shift applications in this packet.

- Published E.5 uses sphere-valued vector tests and bounded linear contractions. Its conclusion does not imply that a coordinate has modulus one. The proposal imports the vector conclusion.
- Published E.6 uses finite summation and tensor products. In its proof, the reduction to scalar input f is not a scalar-unit assumption on the nilcharacter. No division by its coordinates was found in that argument.
- The original Section 8 phase c(n) is a scalar circle-valued character of the linearised representation, hence genuinely unit modulus in that argument. This does not rescue the false original Proposition 8.3 or supply the missing scalar-unit property of E.5. The original route is not consumed.
- The erratum p.4 step moving its high factor across the shift is the occurrence repaired here. The remaining use of a bounded high factor in p.5 Cauchy–Schwarz needs a bound only. The proof retains the bound and eliminates that factor by averaging over the correct parameters.
- The two shift uses are on the full vector tensors, first for the multidegree difference and then for the one-variable matrix entries. Taking coordinates happens after the support bound.

This is a bounded local related-use check. The remaining GTZ proof, especially the independent E.8(v), E.9 and Section 12 tasks, has its own coverage review. This finding is author-identified and the proposed disposition is pending nonauthor review.

## Source and release handling

Source PDFs, page images and extracted source text stay local. SOURCES.json records exact versions, hashes and locators. The erratum is a construction guide, not an imported theorem. No manuscript or earlier evidence was edited.
