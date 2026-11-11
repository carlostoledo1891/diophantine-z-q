# Good-prime modular model and extension of the fixed map

Author: /root/v14_arithmetic_author. Two bounded source applications; pending independent review and source adoption.

## Published inputs

Diamond and Im, Modular forms and modular curves, Canadian Mathematical Society Conference Proceedings17(1995),39–133, section9.3 printed79: the analogous generalized elliptic-curve level functor G0(N) has a smooth proper model X0(N) over Z[1/N], interpreted as a coarse moduli scheme. Its elliptic-curve open part is Y0(N). The paragraph treats X0(N), including small N, separately from the N>4 fine-representability assertion for X1(N).

Bosch, Luetkebohmert and Raynaud, Neron Models, Springer1990, Definition1.2/1 printed12: a Neron model extends each generic-fibre map from a smooth base scheme uniquely. Proposition1.2/8 printed15 says that an abelian scheme over the Dedekind base is a Neron model of its generic fibre. No assumption that the source is a group scheme occurs.

## Actual local application

Fix the good new prime ell outside6dND_K of the current Heegner construction. In particular ell does not divide N. Base change the published smooth proper coarse modular model to Z_ell. This is the actual model of X0(N) with its generalized elliptic-curve level interpretation. Its generic fibre is the same X0(N) used by the fixed Q-map pi, not a replacement curve.

The actual elliptic target E has good reduction at this stipulated good prime, so its smooth proper group model over Z_ell is an abelian scheme. By BLR Proposition1.2/8 it is the Neron model. Since the source modular model is smooth over Z_ell, Definition1.2/1 extends the fixed generic map pi uniquely to a Z_ell morphism. This does not require pi to be a group homomorphism.

For a CM point over a finite extension of Q_ell, properness of the modular model supplies its unique integral section. Evaluating the extended pi on that section agrees generically with pi of the original point, so specializes to the reduction of that image. The reduction of pi is defined over F_ell and therefore commutes with arithmetic ell-power Frobenius on geometric points. Consequently an equality of reduced modular points by Frobenius passes through this same pi.

## Separate premises

The modular-point equality itself still uses CM supersingularity and the specialization of the raising isogenies and level structure. Those are not consequences of smoothness or of the Neron mapping property. The target is assumed good because the current new prime is explicitly chosen good; no claim at bad primes or arbitrary ramified-model base change is made. Properness extends point sections, while the Neron mapping property extends the morphism; these are distinct steps.
