# Four-contact scalar normalizer: candidate232

Author proposal, not independently accepted. The parent is corrected raw233, SHA26d9a2aef8b92fb7fa7d42a24c185ac71d889c0952a0e0bf4b44d09ea9e67691. This changes the scalar arithmetic schedule. It is not a coordinate bijection between all old and new witnesses.

## Equations and count

Keep beta=2504+51X² and A_N=149^(2N+1). Replace only the definition of the scalar contact product by

 r4=beta(beta-1)(beta-2401)(32beta+343), R=A_N*r4/(1+149²*r4).

The original extra factor2beta-1 is removed. M5(beta) has finite contacts0,1,2401,-343/32, so all its finite contacts remain. The fifth contact is infinity, not1/2.

Use parent coordinate t=x63=X² and u=x121=(51t+2501)²/4. Delete parent x122 and its defining row71. Replace parent row72 by

 x123 +14315517724+291790992t+15531948tu+767410608u-512u²=0.

This equals x123-r4=0. All other205 parent rows are unchanged except index compaction. New indices above122 decrease by1. The input1 and coefficient parameter are fixed. There are232 total rational variables and206 quadratic residuals. The full unweighted SOS is degree4 and content1. The larger raw monomial count is not a sparse presentation claim.

## Positivity and denominator domains, including X=0

For every rational X, beta>=2504. Every factor of r4 is positive, r4>=1, and1+149²r4>0. Hence R>0 and A_N/(1+149²)<=R<A_N/149². None of these assertions excludes a rational input or uses integrality. All retained R-rescaling maps remain valid. The parent H recovery F=E=0 is independent of the contact polynomial and still yields f!=0 before the scalar extraction. After forced149, the existing A=a+cf nonzero exclusion and recovery of deleted reference v proceed unchanged. No component is assumed nonzero.

## Forced149 for every rational input

The four residues (theta-2504)/51 for theta=0,1,2401,-343/32 are59,97,109,108 modulo149. Their74th powers equal-1. Thus if v149(X)>=0, r4 is a unit. If v149(X)<0, each factor has valuation2v149(X), so v149(r4)=8v149(X). In this second case v149(1+149²r4)=2+8v149(X)<0. Therefore v149(R) is2N+1 or2N-1, respectively, positive odd forN>=1. The unchanged parity237 core gives v149(Norm(f))>7v149(R)/4, excludes the same H/reference exceptional cases, and yields v149(a)>9v149(R)/4. This invokes the already independently reviewed237 lemma, without changing its proof or order.

## Other contacts and soundness

For p>76176 in M5(beta), beta is integral atp and exactly one of the four finite contact factors has positive odd valuation. Their fixed differences and32 have no prime divisors above the cutoff, as in the retained five-contact height input. Thus v_p(r4)>0 is odd,1+149²r4 is a unit, and v_p(R)=v_p(r4). If beta is nonintegral, its valuation equals2v_p(X), which is even; infinity contributes no odd contact. The unchanged scalar extraction yields p³|a. Consequently, with c=|a| and L_N=floor(9(2N-1)/4)+1,

 149^L_N M5(beta)^3 divides c.

This is precisely the scalar divisibility and height premise used in the accepted233 proof. Both subsequent height/Lucas contradictions and X-integrality argument are unchanged. In particular the same form of an ineffective uniform sufficiently largeN0 proves that every rational zero of the new system has integer distinguished input. No assertion is made for arbitrary independent symbolicA.

## Integer completeness and the changed small-prime preparation

Fix integerX. r4 is a positive integer. At2, ifX is even putX=2k: beta=4(51k²+626), whose valuation is2 for oddk and3 for evenk. The other factors are odd. IfX is odd, beta=3 mod4, both beta-1 and beta-2401 have valuation1, and the other factors are odd. Thus v2(r4) is2or3. The denominator1+149²r4 is odd, giving v2(R) in{2,3}.

At3, beta=2, beta-1=1, beta-2401=1,32beta+343=2 modulo3, so r4=1 and1+149²r4=2 modulo3. Therefore v3(R)=0, replacing the old value1. At17, beta=5, r4=13,149²=16 and1+149²r4=5 modulo17. Therefore v17(R)=0.

Since9792=2^6*3²*17, these results give v2(9792/R)>=3,v3(9792/R)=2,v17(9792/R)=1. Hence1+9792/R is a square in Q2,Q3,Q17, and R(R+9792)=R²(1+9792/R) is a square at all three preparation primes. This is the actual local-square requirement; v3(R)=1 itself is not a necessary assumption.

Write R=A_N r4/D withD=1+149²r4. gcd(A_N r4,D)=1 becausegcd(r4,D)=1 andD=1mod149. Alsogcd(A_N r4+9792D,D)=1. Thus the reduced denominator of R(R+9792) isD², a square.

Use the same real compact neighborhoods forH andS as in the accepted scalar-S/parity proof. Uniformly boundedZ0,Z1,F give W=Z0^4/R^10+Z1²/R^5+F²/R^4=O(R^-4), and b=R(R+9792)W²=O(R^-6)>0. The lower bound onR is uniform in integerX, so0<b<17 eventually for one fixed threshold inN. At the finite support of R(R+9792), chooseH sufficiently formal then the scalar indexa still deeper; all terms ofW can be made arbitrarily integral. This meets the same pole-realization requirements. The retained compact recurrence and progression argument supplies these choices together with the real neighborhoods. Later contact-prime selection avoids this finite support, in the unchanged order. Thus every integerX has a rational witness for all sufficiently largeN. Fillu=(beta-3)²/4 andr4 as above, and all retained coordinates by the original construction with thisR. This is a construction of new witnesses, not a relabeling of arbitrary old ones.

## Scope

The only new arithmetic facts are removal of a redundant contact and the explicit2/3/17/149 checks. Existing scalar extraction, height input, elliptic preparation, prime selection and233 inverse order are retained. Full-system finite verification checks205 unchanged rows and the new quadratic contact equation, but does not replace this arithmetic argument. N0 remains ineffective. No manuscript or accepted artifact is changed.
