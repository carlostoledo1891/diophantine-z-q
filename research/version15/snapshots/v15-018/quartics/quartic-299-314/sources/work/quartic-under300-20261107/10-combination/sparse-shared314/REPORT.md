# Sparse Lucas transport onto shared314

This frozen candidate applies the already independently reviewed affine Lucas change to accepted shared314. It has 314 total variables, 283 quadratic residuals, 6074 monomials and 6077 entries separated by powers of C. Its maximum coefficient remains 186624*C^2+64, with C=3^(2^25). The full polynomial has degree four and content one. This new composition awaits independent review.

The source IR is `work/quartic-optimization-20261107/resume-elimination-20261107/shared-scale314/candidate314-ir.json`, SHA256 `7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5`. Its new arithmetic was independently accepted in `resume-review-shared314-20261107/REVIEW.md`, SHA256 `99630a50aac94071d7001d04afd1dcf5fa68209b34bbebff092db926720a5e33`, and its construction in `10-combination/review-shared314/REVIEW.md`, SHA256 `5e2f0c7091bce7144e7b9659bab52451958ed9d395c9ba7dd8647b7bd3045d82`.

The reused sparse315 review is `work/quartic-optimization-20261107/resume-sol-review-sparse315-20261107/REVIEW.md`, SHA256 `1e28140d377e9f2b63e27f96ee4c5dbf649823300fec80fba1ea0ca476cb53ca`. No acceptance of that earlier target is asserted to cover this target automatically.

The output IR hash is `aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382`; the complete polynomial hash is `1fc9ba1e03e5134bd3173f22d80ecc5c29838996c1cb58839264844f6358d77e`.

## Exact map and physical interface

Let the old field pair in coordinates249/250 be C_L=A*Z, where A=L2 and Z=L4. Replace its meaning by S=C_L-2Z. In coordinates the forward map is new249=old249-2*old244 and new250=old250-2*old245; the reverse adds those same terms. Both maps are polynomial and require no guard. The new defining equation is S=(A-2)Z, and the Lucas output is

    F+1=T^2+S^2-S*(A*T).

The stored output remains (v253,2*v254)=F+1. Every physical point, ratio, F value, scaled shared output, gamma power, group, product and pole variable stays fixed. In particular the shared314 H bootstrap still consumes exactly F(L2,L3,L4), with F(0,0,0)=-1. Its root restoration actions, finite and real choices and gamma nonzero guard are untouched.

The literal complete consumer set of coordinates249/250 is rows201,202,205,206. These are precisely the four replaced rows. Only the names of those two coordinates change. All other row objects, coordinate objects and top-level semantic data are identical apart from status. The verifier checks both directions of substitution separately, as well as the displayed field equations. Thus no additional arithmetic application or completeness choice is introduced.

## Finite checks

`build.py` emits the candidate and polynomial. `verify.py` imports no producer and independently checks both maps, every unaffected object, the complete consumer set, degree, active coordinates, and every coefficient of the primitive-residual sum of squares. It checks the exact symbolic maximum and specialization count without expanding C in decimal. `CERTIFICATE.json`, `VERIFICATION.json` and `MANIFEST.json` provide the exact evidence and source pins.

The reduction is 61 polynomial monomials and zero variables. Shared314 and all earlier accepted artifacts remain unchanged. No manuscript or publication change is included.
