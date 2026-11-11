# Independent review of two corrected connections

Reviewer: /root/astra_v14_baseline_gaussian. Author: /root/astra_v14_baseline_theta. Compiler proposed the two corrections reviewed here and excluded them from his own independent decision. I did not contribute either correction. I did identify and propose a further scalar-order clarification below; that new argument requires a different reviewer.

Target manifest: kwii-general-field-tw-theta-001/MANIFEST.json, f2e616320c6f8179485b5baa112b1847a2e64aa517309188bf94fc9cc0e857a1. Target PROOF.md: 02adafa304e6b4f733c99330268bab678ab1376468f03ecc3443b9e6638b6d8e. I read the full proof for context and independently assessed the corrected connections at lines 46 and 50. Other constructed steps and external inputs retain their separate decisions.

## Line 46: restriction kernel

Accepted relative to the incoming field construction, disjointness at line 44 and Section 2's finite-group calculation. On G_K the cocycle c is a homomorphism because A is trivial there. Coboundaries vanish there. Thus a class vanishing on G_(T_j) has its actual cocycle zero on G_(K T_j). By the definition of L, the restricted homomorphism factors through Gal(L/K). Disjointness makes G_(K T_j) map onto Gal(L F_j/K F_j), so the cocycle vanishes on G_(K F_j). Inflation-restriction then places the class in H^1(K F_j/F,A). The stated H^1(G,A)=0 and A^G=Z identify this group with inflated H^1(F_j/F,Z).

Conversely inflated scalar classes vanish on G_(T_j), since T_j contains F_j. They lie in V because F_j/F is unramified outside the places above 2, all in S. Inflation is injective and the elementary abelian quotient has rank two. Hence the common kernel has k-dimension two. The same characterization holds for restriction to F_j. No unsupported vanishing on all G_K is inferred.

## Line 50: additive image versus its linear span

The corrected span argument is accepted. For c outside the kernel, c restricted to G_(K T_j) is nonzero: otherwise the preceding surjectivity and inflation argument would put c back in that kernel. Its actual image I is an F_2-subspace of A. Normality and the cocycle identity give c(hnh^-1)=h c(n), so W=span_k(I) is a nonzero k[G]-submodule. The retained finite-group premise gives Z contained in W. It is W, not I, to which this premise applies.

Choose a in k_0^* different from 1. Since the characteristic is two, diag(a,a^-1) has distinct eigenvalues. Its conjugation action is semisimple, and Z is in the fixed eigenspace, disjoint from the image (g-1)A. Consequently W is not contained in (g-1)A. The latter is k-linear, so I cannot be contained in it either. An actual cocycle value outside (g-1)A therefore exists. After lifting g to G_(T_j), either the lift already detects c or multiplying it by the chosen element adds this nonzero quotient value. This establishes the intended detection argument without treating I as k-linear.

## Additional exact-wording issue and proposed correction

The frozen line 50 also says that multiplication leaves the residual matrix unchanged. K was defined as the field cut out by A=ad(r), not by r. The chosen tau can therefore have a nontrivial scalar residual image. The unchanged-matrix sentence is not justified as written. Scalar multiplication does preserve the conjugation action and distinct eigenvalues, which are enough for the stated Chebotarev target, but an explicit exact repair is available.

Proposed additional argument, authored by this reviewer: let m be the order of scalar r(tau). It is odd because k has characteristic two. Replace tau by tau^m. It stays in G_(K T_j), has residual image one, and c(tau^m)=m c(tau)=c(tau), since tau acts trivially on A. The residual matrix is then literally unchanged on multiplication. Root has assigned independent review of this new clarification after the author freezes a successor. I do not independently approve my own addition.

Decision: accept the two compiler-suggested corrections, namely the K F_j inflation argument and the additive-image/k-span argument, relative to their stated incoming premises. Do not interpret this as word-for-word acceptance of all of frozen line 50 or the future scalar-order addition. Final exact incorporation requires a successor and the separate non-contributor decision. The finite-group theorems, prior disjointness construction, Chebotarev, Selmer-size theorem, deformation representability and later patching retain their own source records. No live file or prior packet was changed.
