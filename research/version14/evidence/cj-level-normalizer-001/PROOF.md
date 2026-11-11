# The split local level normalizer

Fix the already supplied split local Eichler model R=[[Z_p,Z_p],[p^e Z_p,Z_p]], e>=1, with its cyclic level line. No assertion identifying a geometric curve with this model is proved here.

Put n=p^e and w=[[0,1],[-n,0]]. Its determinant is n and w^2=-n I. For y=[[a,b],[n c,d]], multiplication gives w y w^-1=[[d,-c],[-n b,a]]. Thus w normalizes R, exchanges the two diagonal characters modulo n, and has reduced-norm valuation e.

For an actual split unit trace-zero vector x with selected eigenvalue r, let P be the integral projector onto the r-eigenline. At odd p, P=(x+r)/(2r). In the dyadic support use e_x=(1+x)/2 and P=(e_x-(1-r)/2)/r; this is integral because r is odd. In either case P belongs to R, has trace1, and is an idempotent. On the cyclic level line its first diagonal entry is1 modulo n when r is the selected root; its second is0, since the trace is1. Conjugating P by w exchanges these entries. Therefore the r-projector acts as0 on the fixed level line for w x w^-1, and its complementary projector acts as1. The selected eigenvalue becomes -r. This projector argument also applies at p=2 when the residues of r and -r alone cannot distinguish the two projectors.

For the prescribed root character alpha_p, the root-weight ratio is alpha_p(-r)/alpha_p(r)=alpha_p(-1). By its chosen parity this is w_(p^e)*chi_hstar(p)^e. If chi_hstar is unramified at p then its value on the reduced norm of w is chi_hstar(p)^e. Both are the factors used in the orientation comparison; the actual eigen-action of the modular parametrization remains a separate input.

This establishes the local matrix, selected-root and norm assertions only. The global adelic/geometric identification of this local normalizer with the actual Atkin-Lehner correspondence, the actual character choices, and the principal newform eigen-action are not consequences of the matrix computation.
