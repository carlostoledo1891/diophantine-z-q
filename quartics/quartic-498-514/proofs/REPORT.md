# Combined candidate with 505 variables

This packet combines the mixed-depth, pole-scaling, half-trace guard, single-coefficient anchor, and scalar norm proposals. I independently read the arguments of their authors and the actual consuming passages of Version 11. I accept those five transformations under the inherited arithmetic hypotheses of that manuscript. The new composition itself still needs an independent reviewer before integration or release. No main-theorem or external-source revalidation is claimed.

| Candidate | Variables including input | Witnesses | Quadratic residuals | Quartic monomials | Largest coefficient magnitude |
| --- | ---: | ---: | ---: | ---: | --- |
| Preserved intermediate | 510 | 509 | 479 | 24,881 | `16*3^(2^26)` |
| All five transformations | 505 | 504 | 474 | 24,748 | `16*3^(2^26)` |
| Ordinary-coefficient lift | 521 | 520 | 490 | 24,795 | `3^2048 + 1005072314881896 < 2^3247` |

Every polynomial has degree exactly four and primitive content one. All coordinates occur. The symbolic parameter is the fixed integer `C=3^(2^25)`, not a variable. The complete coefficient tables and residuals are present locally. No enormous power was expanded. The 16-coordinate ordinary lift starts at `3^1024` and applies fifteen squarings, so it reaches exactly C.

## What was checked

`depth_recheck.py` freshly replayed the mixed-depth raw source's gate certificate, complete first compilation, final reversible substitutions, and complete 519-coordinate sum of squares. This script is the contributor's verification driver adapted to write only here; its independent engines are the existing source checker and final checker. It is not a newly authored proof checker.

`build.py` starts with that 519-coordinate system and transports the other proposals by exact coordinate and residual names. Before every replacement, it checks equality of the relevant baseline and mixed-depth residuals up to primitive rational normalization. `certificate505.json` and `certificate510.json` record the input hashes and complete transport maps.

`verify.py` imports no producer. It reconstructs the expected changes separately, checks every unchanged and changed residual, proves the pole substitution identities, checks the concrete nonzero guards and inverse-coordinate incidence, reconstructs all eight new scalar equations with their actual normalization, checks the duplication numerator identity, checks the anchor's actual f1 coordinate and private witnesses, and independently computes the local 3-adic starting direction from the literal curve and point. It collects every squared residual coefficient using an upper-triangular expansion and compares the full symbolic table. For the ordinary lift it separately checks all sixteen defining equations, the exact C substitution, and every coefficient using full polynomial multiplication.

The maximum fixed coefficient has 1,520 bits. The only C-squared coefficient is `16*C^2`, attached to `w^2`, and all linear-C multipliers have magnitude at most 48. The C-squared monomial has no lower-C summand. Since C exceeds every fixed coefficient and 48, the stated maximum is exact. This corrects the anchor proposal's claim `16*C^2+4`: the `4` is attached to `w^4`, not `w^2`.

Reproduce from this directory:

```
python -B depth_recheck.py
python -B build.py
python -B verify.py
python -B build.py --product
python -B ordinary.py
python -B verify.py --product
```

## Independent arithmetic review and application contract

The source version is `manuscripts/quartic_v11.tex`; its exact hash and all proposal hashes are in `SOURCES.json`. I read the actual Version 9 soundness, completeness, local-depth, and deeper-completeness passages; the original scalar32 proof; the local anchor subgroup calculation; the three-witness quaternion argument; and the current source generators and checkers. I did not infer correctness from their existing PASS labels.

1. Required inputs. The mixed logarithms need nonidentity formal points at unramified places over p>76176, with v(p)=1. The trace guard argument needs a split contact prime, primary formal membership, and opposite finite reduction. The anchor needs R=[a-1]P with nonzero even index and the integral odd formal group at 3. The scalar argument needs the same contact valuations, correction unit, pole obstruction, nonzero integer indices, and formal logarithm isometry as the original scalar32 proof.

2. Constructed inputs. All point charts, the rational coefficient basis 1,sqrt(2), direct root targets, contact tests, correction choices, and point domains are unchanged. The mixed-depth source changes only the V1 numerator to ell12, two test orders to 12, and their evaluation circuit. Odd root charts force a odd, and the retained scalar subtraction guard gives a-1 nonzero. The new anchor and new norm block both consume the same literal R=S-P; neither substitutes a related point.

3. Domain coverage. Mixed-depth soundness works at split and inert unramified places. The trace guard uses only completeness's split places and handles all five differences, including H-P. It excludes some old witness assignments but preserves a witness for every integer input. The anchor's residue induction covers every nonzero even integer, including negative indices. The scalar norm only needs one place above each consumed rational prime; both possible branches with positive z valuation are treated by doubling. No integer restrictions are added to existential rational coordinates.

4. Maps and scalar factors. Pole scaling uses e=bE, p=bP, s=bT, q=b^2Q, p2=b^2P2, s2=b^2T2, q2=b^4Q2, f=b^2F. The stored pole f is Bh/17, not Bh. The retained norm/inverse equations imply b nonzero over Q. The exact polynomial identities and factors b^2 or b^4 are checked on the mixed system. Trace-guard soundness restores the original field inverse as (A,-B)/(A^2-2B^2), and its new rational inverse is 1/A. The scalar W-squared attachment keeps the actual rational multiplier encoded in `scalar.W2`. The new anchor uses f1/C and multiplies the three quaternion witnesses by C. Translation w_old=w+C changes the equation to u^2+6v^2-2w^2-4Cw-3f1^2=0.

5. Downstream object. Mixed logarithms still yield exactly L1=n modulo p^12 and L2,L3,L4 equal their labels modulo p^40. The original height contradiction for n-beta consumes only order 12, while the Lucas contradiction consumes order 40. The trace inverses guard the unchanged subtraction slope denominator. The anchor imposes precisely the original semilocal condition on both coefficients of f(R)/C. The scalar norm still gives M5(beta)^32 dividing a-1, the exact input to the exponent-19 height estimate.

6. Local arithmetic. For mixed depth, first transfer integrality between the two approximate ratios, using their equal valuations with the full ratios and the fact that h or h-1 is a unit. Only then deduce primary depth at least 20 and turn relative errors into absolute orders 12 or 40. This avoids circular depth assumptions. For trace guards, enlarge the finite prime cutoff after fixing P and the four roots. At one selected split prime, d=x(U)-x(Q) has negative primary valuation and nonnegative opposite valuation. Conjugation exchanges those valuations, so d+conjugate(d) cannot vanish. For the anchor, z(2P)/3 is 2+sqrt(2) modulo 3 and its square is sqrt(2). The integral odd multiplication series preserve that leading direction under multiplication by 3 and multiply it by a nonzero F3 unit under a 3-unit integer. Thus f1 has valuation 2+2v3(a-1), while f0 has strictly larger valuation. Both coefficients are already 2-integral by the inherited formal-branch proof. The three-witness lemma therefore applies to the single rational coefficient without changing the allowed subgroup.

7. Scalar norm review. Put rho=v_p(r), odd, and q=Norm(f(H)). The new tree is W=N_r(N_r(1,q/r),N_r(z0/r^32,z1/r^32)). Opposite parity prevents cancellation at every node. Its constant-left path excludes rho<0. The pole bound rho+2v(W)>0 then gives v(q)>3rho/8, v(z0)>(32-3/8)rho, and v(z1)>(32-7/8)rho. Consequently v(q)>0 and both ratio coefficients have valuation at least 32. A positive norm valuation supplies at least one place with f(H) of positive valuation; it need not supply every place. At that place H is formal and z(R) is deeper by at least 32. Positive z(R) can describe the branch near (0,0), so it would be incorrect to infer R formal. The exact duplication formula instead proves [2]R formal with v(z([2]R))=v(z(R)) on either branch. Applying the formal logarithm to [h]([2]R)=[2(a-1)]H and using that 2 is a unit gives v_p(a-1)>=32. This justifies the one-place consumer and does not use a general norm-only detector claim.

8. Completeness and compatibility. The old scalar preparation makes all old normalized leaves integral at primes dividing r and divisible at primes dividing c outside r. These bounds also make q/r and the two retained new leaves satisfy the required bounds. The new tree is a unit on the support of cr and supplies new pole witnesses using the same pole-completeness lemma. The new anchor has exactly the old allowed subgroup and imposes no new divisibility. After scalar preparation, fix roots, scales, and a sufficiently small continuity modulus for the new scalar functions and the mixed numerator. Enlarge the prime cutoff for the five fixed root abscissas. The same separated-prime CRT then gives primary depth and opposite finite reductions. This single construction satisfies all five changes simultaneously. Pole normalization is a bijection on those witnesses. No incompatible order of choices has been merged.

9. Acceptance and affected claims. I accept the five contributor transformations by independent internal model review, conditional on the original manuscript inputs and their existing qualifications. The composition is my own construction and is not independently accepted by this report. No repository manuscript, register, contract acceptance record, release file, or public post was changed. A separate reviewer must accept the new composition and its bound application before release. The global arithmetic theorem, external literature, and historical priority remain outside this packet's acceptance scope.

## Toric proposal and remaining limits

The seven-equation toric proposal from `07-toric` removes q12 because the 523-variable source does not consume it. The mixed-depth source does consume q12 in the order-12 polynomial evaluation. Its deletion is therefore incompatible with this composition. The pole scalings themselves do not conflict with that toric proposal. A new toric circuit retaining q12, or a different choice between mixed depth and toric savings, requires a separate check. No additional savings from it are included in 505.

Historical classification is limited. The inherited local, height, and completeness arguments were found in the actual Version 11 text. The new five changes occur in the supplied proposal packets and are not incorporated in that manuscript. I have not searched beyond this source set for prior occurrences of the new ideas. This report does not classify them as globally new or close any historical audit item.
