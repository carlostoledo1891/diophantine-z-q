# Shared alternate-ratio construction: 226 rational variables

Author-frozen candidate, pending independent review. This is a direct transformation of the accepted raw232 family, with the same rational input and fixed parameter A_N=149^(2N+1). The defining threshold remains ineffective. No additional arithmetic theorem or prime-selection hypothesis is introduced.

## Source and attribution

Jose Brox's public commit 34454098637ba9100b19071da55a38199589f5e0, fixed_difference_charts_20261110_v18.tex, section “Direct equations for formal-parameter ratios” (lines197–218), supplies the useful idea of eliminating each alternate numerator parameter by a shared reference ratio. The current adaptation retains our already accepted reference equations instead of adopting the new four-coordinate chart. In particular, it proves the shared denominator domain from our retained scalar149 criterion. Source comparison and exact copies are in ../jose-public-refresh-001. No new public arithmetic claim is imported. The builder here was written independently for our raw232 IR.

## Exact equations and all consumers

Let K=Q(r), r^2=2, d=3-r. All coordinates in this paragraph refer to the parent raw232 IDs. Put S=x19+r*x20 and g=x134+r*x135. Define

alpha=156+(69/2)r, beta=118+60r, gamma=-288-128r, delta=252-672r,
N=alpha*S+gamma+delta*g, D=beta*S+alpha.

For i=0,1,2,3 put z_i=x(21+2i)+r*x(22+2i), L_i'=x(49+4i)+r*x(50+4i), k_i=x(187+14i)+r*x(188+14i), and E_i=(x(177+14i)+r*x(178+14i))-(x(179+14i)+r*x(180+14i)). Write K_i=2d*k_i.

The actual parent equations are N*z_i+D*L_i'=0 and E_i+K_i*z_i=0. Their rational components are respectively parent rows(9+4i,10+4i) and(144+18i,145+18i). The second alternate row is twice the imaginary component. Literal coefficient comparison in build.py verifies this, including the first root's existing R normalization. The eight z components have exactly these16 row consumers and no others.

Delete the eight z components. Introduce one field coordinate T (two rational components), impose D*T-N=0, and replace the four root equations by E_i*T-K_i*L_i'=0. These are quadratic field equations. Retain every other row and coordinate without changing its meaning. The count is232-8+2=226 rational variables and206-8-8+8+2=200 rational residuals. Input x1 and A_N are fixed. MAPS.json gives the complete compaction; T has new IDs225,226. There are190 unchanged parent residuals.

## Domain proof before either inverse

This argument applies equally to an old full solution and a new full solution. The accepted reference reconstruction, scalar normalizer, scalar core and pole rows are unchanged, and their proofs do not use any of the16 removed/replaced rows. Thus the accepted raw232 arithmetic and reference-domain-normalization-022 imply, at the inert unramified prime149, m=ord(f)>0, ord(S)=-m/2<0 and ord(g)=m/2>0. Here f=x17+r*x18. Explicitly the retained H identity is f*S^2+D_curve*f^2=1; in (a+c*f)g+b*f*S+d0*f=0, a and b are149-units, so the leading valuations give the claims. This is the same conditional premise independently checked in reference-domain-review-001, not a new global unit assumption.

Norm(alpha)=43911/2 and Norm(beta)=6724 are149-units. gamma and delta are149-integral. Consequently alpha*S is the unique least-valuation summand of N, and beta*S is the unique least-valuation summand of D. Hence ord(N)=ord(D)=-m/2, so N and D are nonzero. On a new solution D*T=N forces T nonzero and ord(T)=0. No division by any k_i, E_i, L_i', rational component, or g is used here. The domain argument does not assume recovered z_i or any ratio interpretation involving them.

## Two directions, including zero numerators

Old to new: set T=N/D and omit z_i. Since D is nonzero, the alternate equation gives T*z_i=-L_i'. Multiplying E_i+K_i*z_i=0 by T proves E_i*T-K_i*L_i'=0.

New to old: after the domain argument, put z_i=-L_i'/T and forget T. The old root equation is (E_i*T-K_i*L_i')/T. The old alternate equation is L_i'*(D*T-N)/T. Both vanish. These maps are rational and inverse. They include E_i=0, L_i'=0, k_i=0, and zero rational components without further assumptions: no canceled factor among them is needed. In particular a zero numerator remains zero. The nonzero denominator T is proved on the whole admitted-family solution set, not imposed as an additional restriction.

The exact polynomial certificate checked for every i is
D*(E_i*T-K_i*L_i')=D*T*(E_i+K_i*z_i)-K_i*(N*z_i+D*L_i')-K_i*z_i*(D*T-N).

## Full polynomial and limits

Each rational residual is independently cleared to primitive integer coefficients. Their200 unweighted squares form the supplied polynomial. Exact unordered-pair expansion gives degree4, content1,2902 coordinate monomials and2903 parameter terms; all226 coordinates occur. Only the coefficient of x114^2 contains A^2, and it is A^2+1. Linear parameter coefficients have absolute value at most44402. STATISTICS.json records the maximum parameter-free coefficient and checks it is smaller than149^214. Therefore the exact coefficient height is A_N^2+1 for N>=53. This numeric coefficient threshold is not a sufficient defining threshold.

The old family theorem transfers only within its admitted A_N range and inherited arithmetic premises. No new effectivity, minimality, or manuscript adoption is asserted. Independent review must bind this proof, the exact IR and complete expanded polynomial before acceptance.
