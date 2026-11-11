# Author proposal: complete 223-variable circuit

Parent: global/resume-20261110/shared-T-redundancy224-006/candidate224-ir.json (accepted 224/198). This packet is not an independent acceptance.

## Contributions and scope
The paired-factor construction and full assembly are by arithmetic_author. H6 supplied the M-free root/label normalization in normalizer-shared-root-109. GI supplied the trace organization in gi-scaled-trace-005. The trace-independent q domain is H6's detector-q-nonzero-107, independently reviewed at work/quartic224-detector-q-review-001/REVIEW.json. Older scalar arithmetic is reused, not re-proved here.

## Coordinates and inverse
Use parent indices throughout this paragraph. q=x102, q²=x104, R=x126, R²=x125. Delete six FU coordinates62,63,66,67,68,69. New coordinates167..178,195..202,209..216 equal(q/R) times old. New179,180,203..208,217..222 equalq times old. New47..54,56..59 equalold/R. All other retained coordinates are unchanged. MAPS.json gives final index conversion.

Recover old scaled coordinates by the reciprocal stated factors. For pairs(U0,U1)=(179,180),(207,208),(221,222), recover deleted FU pairs as((U0²+2U1²)/q²,U0U1/q²). Add five helpers H=Q1*h0-Q0*h1, J=Q1*j0-Q0*j1, K=Q1*q0-Q0*q1, G=8*x4*x98-[(x185-x187)²+2(x186-x188)²], and Z=sum of new root trace squares for pairs(171,173),(199,201),(213,215). Every helper is uniquely defined by a quadratic residual.

## Domains and both directions
Parent rows9,43,44,45,46,56,57,68,71,73 are literally retained up to index relabeling and constant primitive normalization. They imply R!=0 and q!=0 without any root, trace or paired-factor assumption, by the separately accepted107 proof. Thus all inverse factors exist on every new solution. No individual component, label, root numerator or q+1 is divided by; their zero strata remain included.

Every changed root/label residual is obtained by exact Laurent substitution and multiplication by a nonzero q/R monomial. Six FU definition residuals become identically zero under reconstruction. For factors1,2,4 retain the detector1 definition and replace detector0 by Q1*det0-Q0*det1 after normalizing the output coefficient. Its coefficients are H,J,K as above. SinceQ1!=0 this row operation is reversible, even ifQ0=0. All actual factor values and downstream norm/pole inputs remain unchanged.

The old trace multiplied byq² is Q1*G-R²*Z. Hence the trace with its two helper definitions is equivalent in both directions. These statements include every deleted-coordinate consumer; verify.py checks the exact polynomial identities for all parent rows. Constant primitive normalizations are nonzero and recorded.

Count:224-6+5=223 coordinates;198-6+5=197 residuals. Every residual is quadratic, so their sum of squares vanishes overQ exactly at their simultaneous zero set. Full expansion has2964 coordinate monomials and2965 parameter-separated terms, degree4, content1; all223 coordinates occur. Fixed input coordinate1 and parameterA are unchanged. The uniqueA² coefficient is at newx108², with constantoffset1; coefficientheight A_N²+1 forN>=53. This coefficient statement does not make the inherited defining threshold effective.

The full candidate preserves the parent's arithmetic hypotheses and eventual integer-definition conclusion. It is unrelated to conditional square-attainment226/229. No manuscript adoption.
