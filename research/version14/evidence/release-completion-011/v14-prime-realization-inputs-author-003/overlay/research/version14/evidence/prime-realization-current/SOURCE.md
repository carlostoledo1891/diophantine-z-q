# Prime realization inputs

## Published progression source
Bennett, Martin, O'Bryant and Rechnitzer, Explicit bounds for primes in arithmetic progressions, Illinois Journal of Mathematics62 (2018),427–532, Theorem1.2 printed431: for q>=3 and gcd(a,q)=1 there are positive constants c_theta(q),x_theta(q) such that |theta(x;q,a)-x/phi(q)|<c_theta(q)x/log(x) for x>=x_theta(q). Theta is the sum of log(p) over primes p<=x congruent a modq (definition1.5 printed429). Only this qualitative consequence is used: for fixedq, choose log(x)>2c_theta(q)phi(q); then theta>x/(2phi(q)), which tends to infinity. Thus infinitely many distinct positive primes occur in the reduced class, and any finite set can be avoided. This is a sufficient published input, not a claim that BMOR is the original Dirichlet source.

## CRT source and explicit construction
Milne, Algebraic Number Theory, author course notes version3.08,19July2020, printed19, states the classical CRT for pairwise coprime integer moduli. Here is the entire needed construction: let q_i be positive pairwise coprime moduli and residues a_i units. For Q=product(q_i), Q_i=Q/q_i, choose b_i with b_i Q_i=1 modq_i by Bezout, and set a=sum(a_i b_i Q_i). Then a=a_i modq_i for eachi, and gcd(a,Q)=1. No primality follows from CRT alone. The source is author notes, not a peer-reviewed publication.

## Signed initial prime
At main2858–2866, a unit squareclass at an odd p in S is specified by a nonzero residue modp; at2 it is specified mod8. Pick residues realizing the given classes, and let epsilon be the prescribed real sign. Apply CRT to epsilon times these residues, then the progression input to obtain a positive prime r outside S unionB. The signed prime q0=epsilon r has exactly the prescribed unit classes and sign. The modulus includes8, so q>=3. This does not supply the subsequent HL/BFH theorem or its prime-count conclusion.

## Successive finite realization
At main3026–3049 fix the realizable type residue modulo the support modulus containing8. The old prime vertices are distinct and outside that support. For each prescribed forward Legendre bit, choose a nonzero residue of the requested quadratic character at that odd prime (the squaring map on F_p^* has kernel{1,-1}, so squares have index2). CRT combines the type with these residues to one reduced class. The progression consequence supplies infinitely many fresh positive primes; discard the finite avoidance set and previous choices. Repeat for finitely many new vertices. This supplies forward bits and type only; the classical reciprocity law supplies reverse bits separately. Product-template symbol invariance is likewise a separate graph premise. At main3249–3254 the same procedure realizes each fixed dummy label after h is fixed, excluding support(h) and earlier choices. This is not a prime-size bound uniform in h.

## Boundaries
No analytic threshold uniform over varyingmoduli, no prime-size bound, and no new nonvanishing or Selmer claim are asserted. Realizability and compatibility of each type, fixedsupport representation by unit residues, reciprocity, graph dependence and dummy-label preparation remain explicit incoming premises.
