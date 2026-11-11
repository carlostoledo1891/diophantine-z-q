# Final composition review: frozen394

Accepted. The exact 394-variable candidate below has the same rational input projection as the independently accepted395 system. It therefore defines the integers over the rationals on the same inherited arithmetic inputs. It has 393 existential witnesses, 364 quadratic residuals and 6,338 quartic monomials. Degree, integer content and maximum coefficient are four, one and 16*3^(2^26).

Reviewer: `/root/astra_quartic_opt03_depth`. I authored neither the anchor rescaling nor this numerical composition. This acceptance concerns the exact polynomial and its mathematical composition. An integrated manuscript is a separate, subsequent review; no manuscript acceptance is asserted here.

## Frozen bindings

All paths below are relative to `work/quartic-under400-20261107`.

| Object | SHA-256 |
| --- | --- |
| `10-combination/combined395-ir.json` | `440282e5b3b8a9a19d5d7009399736257a5279105485a1bec073138a64758e6a` |
| `03-depth/integrated395/REVIEW.md` | `c8db82b3b77886a7a289e7eb81ecefc39c8a6fc05928cd3176e4bc2d81a216bf` |
| Component `02-squares/beyond399/candidate398-ir.json` | `9f0b668f42878cb1bf113680052a51b466d6b00966c3bb7ef540688316f5b79b` |
| Component review `01-elimination/review398/REVIEW.md` | `0e7082164559fa84f38435b188ea3eaa673e7c2ccca5666a21adedcccdf9f1be` |
| `10-combination/combined394-ir.json` | `7eb02f9913b55d60a790a287616f1bb80d9f93523e9f11e12481c9ab955746a5` |
| `10-combination/combined394-polynomial.json` | `39e1f5c05a1a26be26b006703bccc2e1c23b8a15876fbd6d43749d5d464d3193` |
| `10-combination/REPORT394.md` | `2dc77daf8681904518cc80d04be10d4a47e57603e50b0a13aa4eeac463282fea` |

I read the component proposal and its independent review, and the actual source coefficient lemma and scalar difference proof in `quartic_v12.tex`, SHA `5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9`. The relevant statements are `lem:v12-anchor-coefficient` and the reciprocal subtraction identities and exceptional cases around lines20385–20445. My new checker imports no author implementation, prior reviewer code, or prior checker.

## Restore the old anchor before using any of its consequences

The unchanged odd root S=(x,h*j), x=h^2, j^2=x^2-D gives S=[a]P for an odd integer a. This comes from the root chart and is independent of the scalar anchor and the H-domain argument. The actual scalar reciprocal rows impose

    (cP*x+D)*g=aP*j-bP*h.

My checker matches these physical rows, including x=v84+2*v85*sqrt(2). The denominator is positive at both real embeddings. The new guard g0*tau=1 gives g0!=0 and hence g!=0. Thus these rows identify the genuine scalar difference R=S-P and f(R)=g^2 without either old inverse or any anchor divisibility hypothesis.

The equal-abscissa cases remain part of this inference. If S=P, the quotient is zero, contradicting the new guard. If S=-P, the explicit duplication formula in the source gives R=-2P with the same reciprocal output. It is not necessary to exclude this branch by an anchor consequence before applying the coefficient lemma. Therefore R=[s]P for a nonzero even integer s=a-1 in every full new solution.

The source lemma applies to every such s, not just indices already satisfying the anchor. It gives v3(f1([s]P))=2+2v3(s), so F=f1(R)=2*g0*g1 is nonzero. The proof writes s=2*3^k*u with 3 not dividing u, including negative u. Its initial z(2P)/3 residue is 2+sqrt(2), whose square is sqrt(2); odd integral multiplication series preserve the asserted leading term under multiplication by3 and prime-to3 integers. The curve identity f=z^2*(1-D*f^2) then gives the coefficient valuation. No inverse or anchor is used in that argument. My checker independently verifies the stated starting residue and square.

It follows that g1!=0 and the old inverse of F can be restored. This is the required order: identify a nonzero even scalar point, apply the unconditional coefficient lemma, restore the old subsystem, then apply the accepted395 proof. In particular, the old anchor lower bound is available before the accepted395 exceptional-H exclusion uses it. There is no circular dependence on that exclusion or on the scalar height bound.

## Exact maps and all consumers

The old private subsystem is

    F=2*g0*g1, F*sigma=1,
    u^2+6*v^2-2*w^2-3*F^2-4*C*w=0.

The new subsystem is

    g0*tau=1,
    U^2+6*V^2-2*W^2-12*g1^2-4*C*tau*W=0.

For an old solution set tau=1/g0 and (U,V,W)=(u,v,w)/g0, and forget F. For a full new solution, the preceding arithmetic establishes F=2*g0*g1!=0; set sigma=1/F and (u,v,w)=g0*(U,V,W). The exact identity is

    q_old(substitution)-g0^2*q_new
      =4*C*g0*W*(g0*tau-1).

These are inverse maps on the full systems. They keep the input and every nonprivate coordinate fixed. No division uses an anchor witness, H, a logarithm, or a scalar pole value. Zero private witness values remain permitted. The isolated new anchor would admit g1=0; only the full scalar-point argument excludes that branch, and this review does not claim a polynomial equivalence for arbitrary g.

The old private incidence is exactly: 55,56,57 each occur only in the anchor row; F=505 occurs only in its definition, inverse and anchor; sigma=549 occurs only in its inverse row. The composition removes505 and its definition, replaces the inverse row by the g0 inverse row, and repurposes55,56,57,549. Every other residual and coordinate object is literally unchanged from accepted395. In particular the S/g equations, scalar ratio and pole, normalized private pole coordinates, all H/V0 equations, root scales, biquadratic outputs, and logarithm consumers are preserved. The preparation-zero and pole-normalization changes have no shared private coordinate with this rescaling.

The accepted395 soundness proof can therefore be applied after the reverse reconstruction, with all its pre-ratio exclusions and half-index identities intact. Conversely, every complete395 witness maps forward, so its simultaneous real/finite/CRT construction remains sufficient. No new global choice or local arithmetic premise is introduced.

## Independent finite result

Run `python -B check.py` here. It checks the frozen source/result/review hashes, exact private incidence, all outside objects, coordinate and row uniqueness, literal old/new equations, the unconditional scaling identity, the unchanged physical scalar chart, and every coefficient in the complete primitive SOS. It writes only the local `CHECKS.json`.

The unique C-squared term is now

    16*C^2*W^2*tau^2.

Its coordinate monomial has no constant or C-linear contribution. All other C-linear multipliers have absolute value at most96, and all constant coefficients have at most1,520 bits. Since C=3^(2^25), these are strictly smaller than16*C^2. The symbolic terms also have distinct ordinary coordinate monomials after C is substituted, so the 6,338 count does not hide collisions. Every retained coordinate occurs.

The exact394 composition is accepted. No later artifact or integrated manuscript is accepted by this report.
