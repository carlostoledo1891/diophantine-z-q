# Frozen 498-variable quartic

The final frozen symbolic candidate has 498 total rational variables, including the input, 497 existential witnesses, 467 quadratic residuals, and 24,669 monomials. Its degree is four, its primitive content is one, and its largest absolute coefficient is exactly `16*3^(2^26)`. The fixed parameter is `C=3^(2^25)`.

The ordinary-coefficient lift has 514 total variables, 513 witnesses, 483 residuals, and 24,716 monomials. It has degree four, content one, and largest absolute coefficient `3^2048+1005072314676622`, which has 3,247 bits. Its sixteen extra coordinates uniquely satisfy c0=3^1024 and c(j+1)=cj^2 for j=0,...,14, so c15=C.

| Frozen artifact | SHA-256 |
| --- | --- |
| candidate498-ir.json | 7682a1229149c75e27322e86dec424449b55321b06c48e468f90fa78bcebb61a |
| polynomial498.json | 817fec936dee3b358fc8b5b0b9a5570694adf009b134432467ef0be914aeedc4 |
| candidate514-ir.json | 5d7ed675b3ee255d9c09dec4ee4f80ea94d6dac747c8f255bac68e81b73484ba |
| polynomial514.json | d247a27709afda5f2be626390cffa1a175c3dfcbee1a5c832a1c457b32629bd5 |

## Exact chain

The source523 becomes519 by the mixed order12/40 logarithm and test circuit. Three detector pole scalings, five comparison half-trace guards, the single-coefficient anchor, and the new scalar norm tree give505. The scalar fixed-target reciprocal chart gives504. The mixed-depth seven-equation toric circuit gives501. Cancelling the scalar denominator-square coordinates gives499. Reusing the existing square of f(H) removes the final scalar norm coordinate and gives498.

The staged sources and their certificates remain intact. REPORT.md covers523 to505, REPORT504.md covers the scalar reciprocal chart and excludes its extra S=-P branch with the retained anchor, and REPORT501.md covers the mixed toric circuit. The final candidate retains the order12/40 system and the scaled two-conic detector poles. It includes neither the later order10 proposal nor the later factored-detector proposal.

## The last three eliminations

For the scalar reciprocal chart, use d=cx+D, c=a^2, N=aj-bh, and M=-2aDh(x+c)-bj(cx-D). The old equations are dg=N, d2=d^2, d2*k=M. Replace the two components of the last equation by

```
a*d*k + 2D*h + a*b*j - 2D*b*g = 0.
```

The exact polynomial identity is

```
d*(a*d*k + 2D*h + a*b*j - 2D*b*g)
  = a*(d^2*k-M) - 2D*b*(d*g-N).
```

It uses b^2=c^2-D. Both a and d are nonzero: a is the fixed nonzero field constant, and d is positive under both real embeddings since c,D are positive and x=h^2. The identity gives both directions. The reverse map uniquely sets d2=d^2. The deleted d2 coordinates have no other consumers. This is an exact rational equivalence and changes no arithmetic or completeness condition.

For the final elimination, write f(H)=f0+f1*sqrt(2). The previously introduced coordinate q=f0^2-2f1^2 occurs only in its defining row and r(A-1)=q^2. The retained mixed-depth test-square circuit already gives coordinates F=f0^2+2f1^2 and G=f0*f1, including the actual normalization of the imaginary component. Use

```
(f0^2-2f1^2)^2 = F^2-8G^2.
```

Replace the scalar row by r(A-1)=F^2-8G^2 and delete q. The certificate writes this as an exact pivot substitution followed by polynomial multiples of the two retained test-square rows. It checks the actual coordinate IDs140,141,311,312 and their coefficients, rather than inferring the normalization from a name. The reverse map uniquely restores q=f0^2-2f1^2. No reciprocal-chart row or deleted d2 coordinate enters this certificate, so the last two transformations commute.

These last changes have only polynomial identities and proven nonzero denominators as inputs. They preserve every coordinate outside the named private blocks and therefore preserve exactly the input projection already established for505.

## Verification and scope

The producer-free `verify498.py` replays the final constant-pivot certificate with complete affected-row coverage, confirms that every added row multiple is an unaffected retained equation, and independently expands the entire498 polynomial. It also checks all sixteen ordinary lift equations, exact C substitution, and every514 coefficient using a separately organized multiplication. The checks passed. `verify504.py`, `verify501.py`, and `verify499.py` check the earlier local changes and complete expansions; `depth_recheck.py` checks the mixed source and compiler certificates. The portable release package additionally regenerates the raw mixed source from its exact builder edits before replaying that chain.

All498 coordinates occur. There is an S-independent coefficient equal to one. Only the anchor contains C; its sole quadratic-C coefficient is16 at w^2, with no lower-C contribution at that monomial. Every fixed coefficient has fewer than2048 bits and every linear-C multiplier has magnitude at most48. These facts prove the symbolic maximum without expanding C. In the ordinary table the maximum is the constant coefficient stated above, checked as a modest 3,247-bit integer.

I accept the scalar denominator cancellation and norm-square reuse as exact algebraic equivalences. I previously independently reviewed the contributor arithmetic transformations, conditional on the inherited manuscript inputs. Separate agents have reviewed the505 finite chain, the single-coefficient anchor, the scalar reciprocal extension, and the final finite composition. Their actual reports, not this description, determine their acceptance scope. This report is authored by the final composer and does not self-approve the final arithmetic theorem, manuscript integration, or a public release.

No inherited global arithmetic result or external literature application has been silently strengthened. No new conjecture or prime-pattern assumption is used. The manuscript and repository remain unchanged by this packet. The target is frozen; further optimization belongs to a separate future candidate.
