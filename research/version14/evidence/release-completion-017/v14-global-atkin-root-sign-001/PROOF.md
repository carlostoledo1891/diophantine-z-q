# Global Atkin–Lehner sign at weight two

Fix the normalized primitive weight-two form f on Gamma0(N) with trivial character attached to the actual elliptic curve E. Use the determinant-normalized slash action (f|g)(z)=det(g)(cz+d)^(-2)f(gz). This is source parameter k=1 in Atkin–Lehner1970 p135, not source k=2.

Atkin–Lehner, Lemma9 and the sentence following it on p139, identifies the product of the exact-prime-power operators W_(p^e) modulo Gamma0(N) with W_N=(0,-1;N,0). Theorem3(iii), p147, gives f|W_(p^e)=w_(p^e)f with w_(p^e) in{1,-1}. Multiplicativity of the slash action and invariance under Gamma0(N) therefore give f|W_N=lambda f, lambda=product_(p^e||N)w_(p^e). This includes p=2 and arbitrary e. Scalar representatives do not change the determinant-normalized action.

Put F(t)=f(it/sqrt(N)) for t>0. The displayed W_N action gives F(1/t)=-lambda*t^2*F(t), since (it/sqrt(N))^2=-t^2/N. The cusp conditions at infinity and zero give exponential decay at both ends after this transformation. Hence I(s)=integral_0^infinity F(t)t^s dt/t is entire, with differentiation on compact s-sets justified by that decay. For Re(s) sufficiently large, termwise integration of the Fourier series gives I(s)=(sqrt(N)/(2*pi))^s Gamma(s)L(f,s).

Changing variable t=1/u in the convergent integral yields I(s)=-lambda I(2-s). Thus the sign in the completed functional equation is -lambda. The separately established equality of the elliptic L-function with L(f,s) identifies this sign with w(E). Consequently w(E)=-product_(p^e||N)w_(p^e), as used at main15181.

This calculation supplies only the global sign normalization. The quadratic-twist root-number formula, nonzero central value, local norm-character factors, and existence or normalization of the elliptic modular parametrization are separate inputs. No operator at a proper prime-power level is identified with a Fourier-block operator by this argument.
