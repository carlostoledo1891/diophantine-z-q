# Independent review of the four odd norm charts

Reviewer: agent03. Author: agent02. This is a non-author mathematical and implementation review of the specific 453-to-449 component. I accept this component on the inherited arithmetic inputs stated below. I found no mathematical error in the proposed replacement. This is not a fresh validation of the inherited Mordell-Weil theorem or of a subsequently combined polynomial.

## Exact reviewed artifacts

The files are in ../02-squares/point-charts, except the named input.

| Artifact | SHA-256 |
| --- | --- |
| 10-combination/rational453-ir.json | f90ee69b7f26d43e94f6a7bb255d3cf2e040d5a2746d79c3b13e08a35185998f |
| candidate449-ir.json | f5a9471dd06bfdfe382b10481fdcf0c7ddfd7184386f1e667a00efdae4ea115e |
| polynomial449.json | 4589dfb06d75f3b136c6ac2b72809aa110c85c4b61c70abd9f2153ec81a149e1 |
| certificate449.json | 917875a8f093b602f64492783000d5cb9e317276bbc6f04964d6fb6ccfef9ab3 |
| REPORT.md | c7d8d9b544689d6b39e0ab324a45be5cb8e388e45e4c033be9cee27d66a40689 |
| manuscripts/quartic_v12.tex | 5ba3f8774732251c178dfabd732d56a41361a73e265666edbd64d49089ebcfd9 |

I read the actual author argument, builder, and verifier, and wrote and ran the separate read-only checker check_odd_norm_review.py in this review directory. It imports neither the producer nor the author's checker. It passed literal old/new equations, exact chart scaling, all private-variable incidences, all outside rows and coordinates, and the complete sum of squares. The result is 449 total rational variables, 426 quadratic residuals, and 6,536 nonzero quartic monomials.

## Sources and conventions checked

The retained field is K=Q(rho), rho^2=2. Put epsilon=1+rho, d=3-rho, D=d^2=11-6rho, and E:y^2=x^3-Dx. The manuscript's chart proof at lines 19331-19408 gives x=h^2, j^2=x^2-D and Q=(x,hj), with h,j,x nonzero. Its nonvanishing argument uses the real embeddings and Norm(d)=7. The normalized group input at lines 7993-8006 and the same-model identification at lines 19450-19455 give 2E(K)=ZP and P=2R0, with R0=(epsilon,2rho). The addition appendix contains the same normalized R0 and odd-chart argument, rather than an unrelated curve model.

I read the squareclass argument at lines 19539-19581. Its homomorphism alpha has alpha(O)=1, alpha(T0)=[-D]=[-1], and alpha((a,b))=[a] when a is nonzero. The exceptional addition cases are addressed there. E[2](K) consists of O, (0,0), (d,0), and (-d,0). For any R, 2R=mP implies R-mR0 is in E[2](K), so the required decomposition R=mR0+eT0+fTd follows with m an integer and e,f in {0,1}. The relevant classes are alpha(R0)=[epsilon], alpha(T0)=[-1], alpha(Td)=[d]. Their norms are -1, 1, and 7, respectively. These facts cover every possible newly constructed R; no integrality or positivity restriction is inserted.

The historical chart and squareclass proof supply the inputs. The norm predicate, its reverse construction, and its implementation are a new application reviewed here. They are not justified merely by the historical odd-chart acceptance.

## Exact equivalence with outside coordinates fixed

Write s=x+j. The old private equations are t^2=2s and th+s=epsilon*r^2, with t,r in K. The new private equations are

    a^2-2sa-D=0,
    Norm(a)=-u^2,

with a in K and u in Q. These are two plus one rational quadratic equations. Only their private witnesses change.

Forward, put a=th+s=epsilon*r^2 and u=Norm(r). The chart identities give a^2-2sa-D=t^2 h^2-s^2-D=2sx-s^2-D=0. Norm(epsilon)=-1 gives the second equation. No denominator or choice is required.

Reverse, h is nonzero by the retained chart. Also s is nonzero since (x+j)(x-j)=D. The first new equation rules out a=0, and the norm equation then rules out u=0. Define t=(a-s)/h. The exact identity

    (a-s)^2 = D+s^2 = 2xs

gives t^2=2s, hence t is nonzero. Put R=(a,at). Since a*t^2=a^2-D, R is on E, has nonzero abscissa and ordinate, and is a legitimate input to the tangent formula. Its tangent slope is h+t: using a=th+s and t^2=2s gives 2at(h+t)=3a^2-D. Direct duplication then gives x(2R)=(h+t)^2-2a=x and y(2R)=(h+t)(a-x)-at=hj. Thus it is the exact stored Q that is doubled, with its exact stored chart representation.

The inherited decomposition now gives

    [a]=[epsilon]^m[-1]^e[d]^f.

Taking norms modulo rational squares yields [(-1)^m 7^f]=[-1], because u is nonzero. The sign forces m odd. Then 7^f must be a rational square, forcing f=0. This leaves exactly the two possibilities [a]=[epsilon] and [a]=[-epsilon]. Negative integers m cause no exception.

If [a]=[epsilon], choose r in K with r^2=a/epsilon. This recovers the old private equations. If [a]=[-epsilon], set a'=2s-a and t'=-t. The new quadratic gives a*a'=-D, so a'=-D/a is nonzero and [a']=[-1][a]=[epsilon]. Choose r with r^2=a'/epsilon. Then (t')^2=2s and t'h+s=a'. This recovers the old private equations without changing h, j, x, or Q. The operation is translation of R by T0, not negation of the stored Q. The associated ordinate is a't'=-a't=D*t/a, which agrees with the addition-by-T0 formula.

The reverse step chooses an existential field square root. It is not a unique rational-function inverse. The author correctly states equality of projections onto all outside rational coordinates, which is sufficient and is precisely what the proof establishes. In particular it does not require a sign change of h or j that could alter a scalar or comparison consumer.

## Implementation and quantifier coverage

The four changed blocks are exactly A, S, T, and Z. Their old private ID tuples are (66,67,68,69), (70,71,72,73), (74,75,76,77), and (78,79,80,81). In each tuple the first two coordinates become the components of a, the third becomes u, and the fourth is deleted. Four old component equations become the three stated new equations.

My checker derives each actual x component directly from its retained chart-square row. It therefore independently handles the nontrivial scale in the T real component and the factor two in the imaginary components; it does not assume the stored x-coordinate IDs are the literal field components. It matches all old odd equations and all new equations against those exact field expressions.

Every old private coordinate occurs only in its own four odd equations. Every row outside the sixteen replaced rows is byte-for-byte identical as a parsed JSON object. Every outside coordinate object is identical. Thus the sign choice in each reverse construction has no hidden consumer. The four replacements can be performed independently while retaining all shared root, comparison, scalar, logarithm, height-product, detector, and input coordinates. The forward and reverse constructions use the same quantified field K with rational components. No primality, local congruence, real-sign, or integrality assumption has been added.

The complete polynomial check is structural evidence, separate from the arithmetic argument above. Together they support acceptance of this frozen 453-to-449 component. Composition with the 445 primary-reciprocal candidate still requires checking the actual combined rows and hashes.
