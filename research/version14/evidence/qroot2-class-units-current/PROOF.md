# Class group and unit squareclasses of Q(sqrt2)

This is a new local proof for the fixed field K=Q(s), s^2=2, with the first real embedding s>0. It replaces the general Minkowski and unit-rank inputs for this field only.

## Ring of integers

Let z=a+bs be integral, with rational a,b. Its trace m=2a and norm h=a^2-2b^2 are integers. If b=u/v in lowest terms with v>0, then 8u^2/v^2=m^2-4h is an integer, so v^2 divides8 and v divides2. Thus k=2b is an integer. Now m^2-2k^2=4h; reducing modulo4 forces k even (otherwise the left side is2 or3 modulo4), and then forces m even. Hence a,b are integers. Conversely s and all integer polynomials in s are integral. Therefore O_K=Z[s]. The trace matrix on1,s is diag(2,4), so its discriminant is8. This uses only the elementary facts that traces/norms of algebraic integers are integers and algebraic integers form a ring.

## Euclidean division and class number

For alpha,beta in Z[s], beta!=0, write alpha/beta=x+ys with rational x,y. Choose integers a,b with |x-a|<=1/2 and |y-b|<=1/2. Put q=a+bs and r=alpha-beta q. With X=x-a and Y=y-b, one has |N(X+Ys)|=|X^2-2Y^2|<=1/2<1, because 0<=X^2<=1/4 and0<=2Y^2<=1/2. Multiplicativity of the norm gives |N(r)|<|N(beta)| unless r=0, which already gives exact division. Nonzero integral elements have positive integer absolute norm.

Every nonzero integral ideal I contains a nonzero beta of least absolute norm. Divide any alpha in I by beta as above. Its remainder lies in I, so minimality forces the remainder to be zero. Thus I=(beta). Clearing one denominator reduces a fractional ideal to an integral ideal, so every fractional ideal is principal and the class group is trivial. No general Minkowski bound is used.

## Units and their signs

Put epsilon=1+s. Its norm is-1 and epsilon inverse is s-1, so it is a unit and epsilon>1 in the first embedding. An element of Z[s] is a unit if and only if its norm is+1 or-1: one direction follows by taking norms of an inverse, and the other from the integral conjugate.

Take any unit u. Multiply it by a sign to make its first embedding positive, then by an integer power of epsilon so that the resulting unit v satisfies1<=v<epsilon. Such a power exists because epsilon>1. Its conjugate vprime is+1/v or-1/v. Writing v=a+bs with integers a,b gives b=(v-vprime)/(2s). This is nonnegative, and it is at most(v+1/v)/(2s). The function t+1/t is increasing on[1,infinity); since epsilon+epsilon inverse=2s and v<epsilon, this upper bound is strictly less than1. Thus b=0. Then v is a positive rational integer of norm1, hence v=1. Consequently every unit is uniquely of the form (-1)^e epsilon^k with e in{0,1} and k an integer.

The square subgroup consists exactly of epsilon^(2k). Thus there are four unit squareclasses, represented by1,-1,epsilon,-epsilon. At the two embeddings the signs of -1 are(-,-), and those of epsilon are(+,-), since1-s<0. These two sign vectors are independent. A unit is positive at both embeddings exactly when e=0 and k is even, which is exactly the condition that it is a square of a unit.

## Actual use and boundaries

This supplies precisely the integral-ring, class-number-one and unit-squareclass/sign inputs in main344–346 and elementary-inputs-current/PROOF.md28. It also proves that epsilon generates the units positive at the first embedding; epsilon^2 generates the totally positive units, but no broader field-uniform theorem is claimed or needed. The elliptic-curve rank, torsion, local descent, chosen point and height/saturation arguments remain separate. The old Minkowski numerical expression is a superseded method, not a premise of this proof.
