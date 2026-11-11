# Quadratic Gauss basis normalization

Let chi be a primitive quadratic Dirichlet character of conductor D>1, extended by zero to nonunits, and put zeta=exp(2*pi*i/D), S(a)=sum_x chi(x) zeta^(a*x), and tau=S(1). All sums here are over Z/DZ. We use the actual primitive conductor, not an inflated character at a larger modulus.

If a is a unit, substituting y=a*x gives S(a)=chi(a)^(-1) tau=chi(a) tau.

If a is not a unit, set d=gcd(a,D)>1 and m=D/d. There is a unit b modulo D with b=1 modulo m and chi(b) not equal to one. Otherwise chi would factor through the reduction map (Z/DZ)^times -> (Z/mZ)^times, contrary to primitivity. This reduction map is surjective: lift a unit modulo m and choose its residue nonzero at the primes dividing D but not m, by the Chinese remainder theorem; at primes already dividing m every lift is a unit. Thus triviality on its kernel really would give a character of the proper divisor m.

For this b, a*b=a modulo D. Substitution x -> b*x in S(a) now gives S(a)=chi(b) S(a), so S(a)=0. This includes a=0, for which m=1 and the nontrivial primitive character cannot be trivial on all units.

Finite Fourier orthogonality gives sum_a |S(a)|^2 = D sum_x |chi(x)|^2 = D phi(D). Indeed, after expanding the square, sum_a zeta^(a*(x-y)) is D if x=y modulo D and zero otherwise, by the finite geometric series formula. The unit and nonunit formulas above make the left side phi(D)|tau|^2. Therefore |tau|^2=D.

Since chi is real, conjugating tau and substituting x -> -x gives conjugate(tau)=chi(-1) tau. Consequently tau^2=chi(-1)D. The same unit-change calculation gives the Galois transformation sigma_a(tau)=chi(a) tau.

For the primitive quadratic character chi_h of an odd squarefree signed h, use its signed fundamental discriminant Delta_h and conductor D=|Delta_h|. The character convention is chi_h(-1)=sign(Delta_h); hence tau(chi_h)^2=Delta_h. With the chosen complex square root of h, the ratio tau(chi_h)/sqrt(h) has square Delta_h/h, which is either one or four. It is therefore plus or minus one, or plus or minus two. The possible ratios belong to the fixed set {1,-1,2,-2}, independent of the number of odd conductor primes. Both tau(chi_h)*e_chi and sqrt(h)*e_chi are invariant when e_chi carries this quadratic action.

For the trivial conductor-one character, set tau=1 and Delta_h=h=1; the same ratio conclusion holds directly. The argument does not claim an exact positive Gauss-sum sign. It supplies the signed square, Galois character, and basis-change factor up to sign used in the current valuation comparison. The quadratic-field discriminant convention and the actual choice of chi_h remain the stated input; no reciprocity or Euler-system assertion is proved here.
