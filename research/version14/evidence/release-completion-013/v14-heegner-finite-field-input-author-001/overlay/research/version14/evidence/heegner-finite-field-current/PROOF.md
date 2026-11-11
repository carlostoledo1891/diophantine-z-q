# Additive finite-field input for formal cocycle correction

Author: /root/v14_arithmetic_author. New local proof; pending independent review and explicit source extension.

## Claim and elementary proof

Let k have q elements and kprime have q^r elements, with r>=1, and let sigma(x)=x^q generate Gal(kprime/k). The additive trace T=1+sigma+...+sigma^(r-1) maps kprime to k. Its polynomial X+X^q+...+X^(q^(r-1)) is nonzero and has degree q^(r-1)<q^r (also when r=1), so it cannot vanish on all of kprime. Thus T is a nonzero k-linear map to the one-dimensional k-space k and is surjective.

The kernel of sigma-1 is exactly k: its elements solve X^q-X=0, whose q roots are the elements of k. Therefore im(sigma-1) has k-dimension r-1. The telescoping identity T(sigma-1)=sigma^r-1=0 and the dimension of ker(T) show im(sigma-1)=ker(T). This includes r=1, when both spaces are zero.

An additive cyclic cocycle is determined by its value x at sigma. The cocycle relation at sigma^r=1 says T(x)=0. Hence x=(sigma-1)y for some y in kprime. The cocycle and the coboundary of y agree at the generator, so agree on the whole cyclic group. Consequently H1(Gal(kprime/k),kprime)=0. No division by r is used, even when the characteristic divides r.

## Actual formal-quotient application

In the existing Heegner local proof, Fprime/F is finite unramified and a uniformizer pi of F remains a uniformizer of Fprime, fixed by the Galois group. The formal parameter is defined over F. The already supplied formal-filtration identification takes the nth quotient to pi^n O_Fprime/pi^(n+1) O_Fprime, and multiplication by pi^n identifies this Galois module with the additive residue field kprime with its usual Frobenius action. The preceding calculation therefore kills H1 of each quotient used in the successive cocycle correction.

This is a direct replacement for invoking normal-basis inducedness at this particular H1 step. It neither claims a normal-basis theorem nor supplies unrelated higher cohomology statements. The exact formal-filtration identification is a separate source input. Lifting each quotient correction and passing to the limit uses completeness and the existing formal-group argument; the Lang step, Neron geometry, and component bound remain separate.
