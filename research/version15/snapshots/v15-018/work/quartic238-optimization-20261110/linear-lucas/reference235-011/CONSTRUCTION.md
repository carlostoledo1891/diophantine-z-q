# Exact 235-variable, 209-equation construction

This finite construction starts from raw parity237 IR64649e6f06b3d8dc1f592805610f550b9500a7a44d4ed13796af0f83544e3c9b. The selected direct mathematical proof is global/reference-kummer-235-017/DIRECT-PROOF-209.md, SHAe39c920bd90e913cf0776aeab66ba6f89af1a94346b1bf0dd02a2a5b1c2d7236, bound by MANIFEST-002.json aae76c52dbce2083bb01eef01245810502a76750c2a17ef2279e261959441470. Independent mathematical acceptance is norm-guards/reference-kummer235-review-017/MATH-REVIEW.json3ce6e6741b99e1375b550f5b4e6d6caab939ce6611e5e49c9d35ae264c458976. Full finite acceptance remains separate.

Let f=x19+sqrt(2)x20, S=x21+sqrt(2)x22, g=x139+sqrt(2)x140 and v=x23+sqrt(2)x24 in old coordinates. Retain g²=fv. Delete old coordinates17,18 and exactly old rows1,2,3,4,88,89. Replace them with the four rational components of

F=(a+c f)g+b fS+d f,
E=b Sg-d g-a f+8,

a=57-28sqrt(2), b=8-14sqrt(2), c=88-48sqrt(2), d=39-36sqrt(2).

There is no new guard coordinate. All205 remaining rows are unchanged under i↦i for i<17 and i↦i-2 for i>18. The constructor asserts that neither deleted coordinate occurs in any retained row. MAP.json gives the complete coordinate and unchanged-row maps and exact nonzero normalization factors for the four added rows. Parameter A_N and input coordinate1 are unchanged.

Forward map: discard old17 and old18, retaining every other coordinate through the deletion map. The accepted proof shows F=E=0 on the admitted parent family; its exceptional value is excluded by the unchanged parity scalar argument at149. This is not an assertion of equivalence for an arbitrary symbolic parameter A.

Reverse map: f0=new17, f1=new18, delta=f0²-2f1². The retained G=g²-fv and new E imply f!=0, since f=0 would force g=0 and then E=8. Hence delta!=0 over Q. Recover old17=f0/delta and old18=-f1/(2delta), respecting the factor-two imaginary convention for old chi. All other values follow the inverse coordinate map. The exact identity F*(bS-d)-(a+cf)*E=b²*(fS²-1+(11-6sqrt(2))*f²) recovers the H curve without dividing by a+cf or by S,g,v. The first new equation divided by f recovers the old reference equation. These maps are inverse on the full rational solution sets in the admitted family and retain all permitted zero components.

VERIFICATION.json hashes the exact transported terms of all205 unchanged rows and verifies a separately ordered full integer sum-of-squares convolution. The result has235 variables,209 quadratic residuals,3033 coordinate monomials,3034 parameter-separated terms, degree4 and content1. All235 coordinates occur. The full coefficient profiles give maximal coefficient A_N²+1 for N>=53. This is only a coefficient-size bound; the sufficient defining threshold remains ineffective. No V14/V15 or release files changed.
