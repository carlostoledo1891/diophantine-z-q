# Independent review of the shared alternate ratio

Scope: the new raw232-to-226 transformation, its denominator order, deleted-coordinate census and exact finite polynomial. This is not a reproof of inherited arithmetic. The reviewer authored earlier scalar/domain contributions; the separately accepted raw232 and GLOBAL domain022 receipts are reused explicitly, not self-approved here. Accepted within the new-transformation and finite-check scope against author manifest704af5b908e8dcb12f1b0b6ea1aab0d387b428ea175225f25bdb6c805e59e367. The inherited arithmetic premises and ineffective defining threshold remain explicit.

## Algebra and all branches
In the actual raw parent let S=x19+sqrt(2)x20 and g=x134+sqrt(2)x135. Set alpha=156+(69/2)sqrt(2), beta=118+60sqrt(2), N=alpha*S-288-128sqrt(2)+(252-672sqrt(2))*g and D=beta*S+alpha. For all four pairs the existing alternate equations are exactly the real and twice-imaginary components of N*z+D*L=0. Their existing root equations are exactly the components of E+2(3-sqrt(2))*k*z=0. This includes the first R-normalized block: no generic scaling guess was used.

Add the field coordinate T and D*T-N=0. Replace each root equation by E*T-2(3-sqrt(2))*k*L=0, remove all four z pairs and their alternate equations. Forward: T=N/D. Reverse: z=-L/T. In reverse, N*z+D*L=0 identically, and dividing the new root equation by T recovers the old root equation. No division by k, E, L or a rational component occurs. In particular L=0 gives z=0 and E=0; k=0 would also cause no algebraic failure. All identity/zero numerator strata are preserved.

## Denominator order and noncircularity
The unchanged reference reconstruction plus unchanged scalar normalizer, parity core and pole predicate give m=ord149(f)>0 and ord149(S)=-m/2, ord149(g)=m/2. Here S denotes the reference y/x coordinate, not the scalar point. This is exactly the separately accepted domain022 premise; its author is the present reviewer, so its earlier independent acceptance is essential.

Norm(alpha)=43911/2 and Norm(beta)=6724 are149-units. Thus alpha*S is the unique lowest-valuation summand of N, and beta*S the unique lowest-valuation summand of D. Consequently ord149(N)=ord149(D)=-m/2 and ord149(T)=0. N,D,T are nonzero field elements. This deduction needs none of the deleted z coordinates or their alternate equations. The same unchanged rows prove it on a candidate tuple BEFORE reverse reconstruction. This avoids assuming the old complete solution in order to justify the new denominator.

## Source idea versus proof dependency
Pinned Jose commit34454098637ba9100b19071da55a38199589f5e0, fixed_difference_charts_20261110_v18.tex lines197-210, writes z=-x/y and the direct comparisons L*I=V*S, Lprime*K=Q*T. The sign convention is consistent: z(H-P)=-1/T, hence Lprime=-T*z(V). Our acceptance does not import that source's new common-point chart or a new arithmetic theorem. The exact old-parent equations above independently establish the required representation change; the interpretation of T as the shared negative reciprocal formal parameter is inherited from that exact old ratio formula.

## Finite checks
The independent Python checker builds the two shared definitions and eight root replacements from field multiplication over Q(sqrt(2)); compares every remaining parent row after explicit index deletion; scans every old coordinate consumer; and independently expands all200 residual squares. It verifies the full emitted polynomial coefficient by coefficient. It does not run the author's generator. All226 coordinates occur, input1 and the fixed parameter are unchanged. The coefficient profile has only x114^2 carrying A^2, with coefficient A^2+1; linear parameter maximum44402 and parameter-free maximum below149^214+1. Thus the exact height is A_N^2+1 for N>=53, a coefficient-only threshold. Raw counts are not compared with the previously optimized sparse232 term count as if they had the same presentation.

No extra square-attainment hypothesis from conditional226/229 studies is used. The ineffective defining threshold is retained; no effective defining N is asserted.
