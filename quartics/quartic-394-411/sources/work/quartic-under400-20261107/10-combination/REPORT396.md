# Preparation-zero composition at 396 variables

This frozen research candidate adds the independently reviewed scalar preparation-zero component to frozen399. It has 396 total variables, 395 witnesses, 366 quadratic residuals and 6,344 quartic monomials. Degree, content and maximum coefficient remain four, one and 16*3^(2^26). The complete composition remains pending independent acceptance.

| Artifact | SHA-256 |
|---|---|
| Source combined399-ir.json | eae983889586748f5a51aa7562d23769ae46f7fba08fc8efcedbb53bc54a5a3b |
| Candidate combined396-ir.json | 5b7737b62f2341116f47c2ca24443014d1a8fc899c555d327080bc9e5b1aa777 |
| Polynomial combined396-polynomial.json | 5341ba709fa7ee4d0c06f179f12025ee0f7865681da03cd2ab32d50f5aae3529 |

The exact component is inputs/preparation-zero439-ir.json, independently reviewed in inputs/preparation-zero-review.md. It deletes coordinates 50,528,529 and two private preparation rows, then replaces the remaining preparation equation by coordinate531=coordinate526^2. The certificate records the source bindings, deleted and changed rows, coordinate incidence and statistics. verify_combination.py 396 independently replays the full delta and every quartic coefficient.

The source interfaces and arithmetic qualifications in REPORT399.md remain in force. The scalar equations are exactly those reviewed in the component: beta=51(2X+1)^2+2504, c=r+4896, B=(z0^2+r*z1^2)/r^32, W=(B^2+r*Norm(fH)^2)/r^32 and actual pole input b=crW^2. In the enlarged H domain, fH is still a nonzero field element because x*fH=1. Hence its norm is nonzero, W>0 and b>0 on every new witness. This gives the component's new-to-old lift and its nonzero input without an old preparation inverse.

Completeness deliberately chooses H in the old subgroup 2E(K), which the enlarged chart still allows. The component proof constructs the same initial H0 and scalar R with simultaneous finite depth and real smallness. It uses the source G0 open-set statement on divisible integer progressions, includes 17 in the support even when it does not divide cr, fixes the continuity modulus before later prime choices, and chooses the final shared H through the full CRT and the same open set. It obtains 0<b<17 and the required local valuations. The preparation-zero theorem then sets U=b. This is a fresh completeness construction, not a specialization of every old preparation witness.

The scaled primary chart maps preserve all values of this final H and all ratios. They neither change the initial preparation nor add a congruence to the CRT. H-domain completeness only forgets a square-root witness after the original construction. These observations supply the interfaces that must be checked in final independent composition review.

The later normalization of the scalar pole is not included here. All399 artifacts remain unchanged.
