# Independent review of the frozen 486-variable composition

Reviewer: `/root/astra_bl5_models`. Date: 2026-11-07. Decision: accepted within the scope below.

I authored none of this candidate or its component transformations. This is internal model review of a research candidate, not approval to change the released manuscript. It does not satisfy the requested under-400 publication threshold and does not cover later candidates.

## Exact artifacts and scope

- Source `inputs/released498.json`: SHA-256 `7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a`.
- Candidate `combined486-ir.json`: SHA-256 `55043867418ca00c68add72560b11055c71d082747d6bea61522168885875787`.
- Certificate `combined486-certificate.json`: SHA-256 `eb83f2c9551544e792ab499a3944380b82744a030447733b4357297ba6fd3ca1`.
- Polynomial `combined486-polynomial.json`: SHA-256 `d3ad1576dba0a077ae22ec6091c110744dad8b932b2009bf19d0d180e2c1b3ec`.

The accepted chain consists of the order-ten source/weight change, four factored poles, scalar reciprocal `k` elimination, the scalar preparation conic, and forward scalar powers. The candidate has 486 total variables, 485 witnesses, 455 quadratic residuals, degree four, 24,699 monomials, content one and maximum absolute coefficient `16*3^(2^26)`.

I read the actual lower-order arithmetic argument and toric equations, the factored-pole equations and their sign conventions, `SCALAR_REPORT.md`, the preparation-conic argument, and the forward-power argument. I read the bound component reviews and checked their reasoning rather than relying on their acceptance labels. I also read the relevant verifier implementations, inspected the combined preparation and power equations, and reran the checks listed below. The released 498 proof and its inherited qualifications remain the baseline; this review does not re-prove those inherited arithmetic theorems.

## Order ten and its circuit

Only the two input tests change order. The alternate numerator remains the order-twelve `G2` approximation and its denominator remains the order-forty `G9` approximation. A positive-order cross test first transfers integrality of the two full ratios using the fact that one of `h,h-1` is a unit. Primary depth at least twenty then gives order eighty, while the alternate error is still at least twelve. Thus the weaker order-ten comparison is valid, and the other label and Lucas comparisons retain order forty.

The revised height calculation is sufficient. With the same anchor, `h(beta)<|a|/40` and `log(48H)<|a|/40`. A nonzero numerator of `n-beta` would give `log B<10 log(48H)+19 h(beta)<(29/40)|a|`. The anchor makes this strictly smaller than `|a|-3`, contradicting the unchanged Lucas lower bound. No stronger logarithm approximation or weaker anchor estimate has been silently used.

For each detector the six toric equations give successively

`a=q/E`, `b=q^2/E^3`, `c=q^3/E^6`, `d=q^2 E^6`, `q10=q E^18`, and `q40=q E^78`.

The nonzero conditions for `E` and `q` come from unchanged exterior detector rows, not from an inverse equation removed with the old circuit. The retained norm quotient cannot vanish when the rational coefficient `w0` has its inverse. The row relating that quotient's square to `E*delta*B` forces `E!=0`, and `q*delta^3=E` forces `q!=0`. The divisions by `c` are consequently legitimate. The retained `q^5` and `q10^2` coordinates are checked at their actual consumers.

Completeness must recompute the detector products and pole witnesses at order ten. It is not a claim that arbitrary old pole assignments survive. The original estimates apply to this fixed positive order: the real decay remains of order `lambda^-3`, and the local divisibility coefficient is `10m-8=92>0`. The continuity conditions can still be fixed before prime selection.

## Four factored poles and zero witnesses

The factored equations reconstruct the old equations polynomially with `F=t*v`, `q=t*Q`, `q2=t^2*Q2`, and `t2=t^2`. This proves soundness even when `t=0`. For completeness, division gives the new witnesses when `t!=0`. When `t=0`, positivity of the actual pole input forces the old `q` and `F` to vanish, and the three new factor witnesses may all be set to zero.

The scalar pole has a different stored sign. Its semantic input is `B=-K*b_stored` and its semantic product is `H=-17K*f_stored`, with the positive integer `K` in the pinned certificate. The zero-branch equation is `-17B*q^2-3H^2=0`. It has the required implication because scalar preparation gives semantic `B>0`; it would be incorrect to assume the stored `b` itself positive. Detector positivity and scalar positivity are both available from the same completeness construction before these factorizations are applied.

## Scalar reciprocal and preparation replacements

For scalar `k` elimination the exact identity is

`L=a*d*Z-z*K-a*G`,

where `G=d*g-N`, `K=a*d*k-T`, `Z=k*z+g` and `L=T*z+a*N`. The retained point chart gives `d=a^2*h^2+D>0` in both real embeddings and `a!=0`. Therefore the reverse assignment `k=T/(a*d)` restores all deleted equations. It does not divide by `T`, `g` or `z`, so it adds no zero-case exception. The previously reviewed reciprocal point and anchor arguments remain applicable after reinsertion.

For preparation, the old equations are `t^2=t2`, `B*(T-t2)=1`, `T*W=2`, and `(W-B)^2=N`. The replacement is `U^2=N`, `B*J=1`, and `N*J+Y^2=B`. The forward map is `U=W-B`, `J=T-t2`, `Y=t*W`. If `B+U!=0`, the reverse map has `W=B+U`, `t=Y/W`, `t2=t^2`, and `T=t2+J`. If `U=-B`, the equations give `Y=0` and `N=B^2`; choose instead `W=2B`, `t=t2=0`, `T=J`. This changes a private unsquared value's sign but preserves `N`, which is the only preparation value consumed outside the block. The factored scalar pole also consumes this squared value, so the exceptional reverse map remains valid after composition. No sign assumption on `B` is needed for this preparation equivalence.

## Forward powers and interaction checks

The retained input and contact gates give `beta=2X^2+3` and

`r=beta*(beta-1)*(beta-2401)*(32beta+343)*(2beta-1)`.

For every rational input this is nonzero. The only possible factor not immediately excluded by `beta>=3` would force `X^2=1199`, impossible for a rational square. This argument concerns all rational solutions of the retained gates and still holds after the explicit inverse of `r` is removed.

The new powers uniquely compute `r^2` through `r^64`, and the final equation is `r^64*B=z0^2+r*z1^2`. Dividing by the established nonzero `r^64` restores the exact old norm node. Its value, its square, the scalar root and the pole input are preserved. Neither sign of `r` nor zero values of the ratio coefficients cause an exception.

The certificate's transport check compares each patch against the currently accumulated system, including coordinate meanings in affected rows. It therefore verifies compatibility rather than merely adding the component savings. In particular, the preparation patch starts from the already factored pole source; the reciprocal patch and forward-power patch preserve the scalar outputs consumed by both. The complete reverse sequence reconstructs a solution of the order-ten semantic source, which has the soundness proof above. Forward completeness first obtains the positive-input order-ten witnesses, then factors the poles and applies the exact local maps. No new prime choice is required by those maps.

## Replayed finite checks

I reran `verify_order10.py`, `verify_factored491.py`, `verify_scalar496.py` and `verify_combination.py 486`. I also reran `06-product/verify.py` and `02-squares/verify493.py` after reading their exact equation checks. All passed. Their file writes were redirected into this review folder, and their stdout logs are retained here. These are reruns of separately implemented existing checkers, not a claim that I authored six new engines.

The final replay checks every declared patch, coordinate and row change, protected input, fixed parameter, the full sum-of-squares coefficient expansion, and the stated count and coefficient bounds. The component replays additionally check the polynomial identities, scalar normalization, private consumer incidence and contact-polynomial expansion used in the mathematical argument.

No actionable defect was found in this frozen 486 candidate. Acceptance is confined to this research composition and its unchanged inherited hypotheses. It covers neither pending guard, hybrid or Padé candidates nor any future manuscript or publication contract.
