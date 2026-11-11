# Discriminant-one supplier for the determinant characters

This author supplement preserves constructions14 and15. It supplies an exact published statement and the narrow connecting argument; independent source/application review remains required.

## Published input

Odlyzko's final1990 paper, printed119 (PDF2), defines n as the degree of an arbitrary number field K and D as its absolute discriminant. In the introduction it explicitly recalls Minkowski's result that D>1 for n>1. The paper's later conditional analytic bounds are not used. The available source is the official Numdam final scan with its bibliographic/copyright cover, not lecture notes or an inferred final edition. This is a published statement of the classical theorem; no original-Minkowski proof audit is claimed.

## Connecting argument

Let theta:G_Q->A be a continuous character with finite image, where A may be the multiplicative group of a finite coefficient field or a finite group of roots of unity. Assume theta is trivial on inertia at every finite rational prime. Let L be the fixed field of its open normal kernel. Then L/Q is a finite Galois extension, and every finite-prime inertia group in Gal(L/Q) is trivial.

Consequently, for each rational prime p, the algebra O_L tensor Z_p is a product of rings of integers of finite unramified extensions of Q_p. Its trace pairing is perfect: reducing modulo p gives the trace pairings of finite separable residue-field extensions, whose determinants are nonzero; lifting makes each determinant a p-adic unit. Computing with a global integral basis shows that the integer disc(L) is a p-adic unit for every p. Thus abs(disc(L))=1. This argument includes p=2. It imposes no condition at the infinite place.

The published Minkowski statement forces [L:Q]=1. Therefore theta is trivial. The use of finite separable trace pairings, completion of the ring of integers, and the integral discriminant is the standard algebraic definition/trace criterion, not a class-field-theory or modularity hypothesis.

## Exact consumers

In construction14 Section2, take theta=det(r)*omega_P^(1-k_r), over the original finite coefficient field. The given ordinary inertia makes theta trivial at P; r and omega_P are unramified at all other finite primes. The preceding lemma gives det(r)=omega_P^(k_r-1). Hence the chosen finite psi=omega_P^(k_r-2) has psi*epsilon_P reducing to det(r). The parity/ordinary/local-ring conclusions continue to be checked in construction14.

In second-family15 Section3, take theta to be det(rbar) divided by the reduction of psi*epsilon_l, where psi=omega_P^j. At P this is trivial by the explicitly required old-character reduction; at l it is trivial because det(rbar)|I_l=omega_l and psi is unramified there; away from l,P both characters are unramified. Thus theta is trivial and the proposed fixed determinant really lifts the original residual determinant. This does not prove existence of j, the weight-two criterion, or the second family's existence.

No new claim is made about the rest of Odlyzko's survey, general source ancestry, full caller coverage, or the independence of KWI/KWII from every earlier Khare input. The proof PDFs and images in local-only are review evidence and are not proposed for public redistribution.
