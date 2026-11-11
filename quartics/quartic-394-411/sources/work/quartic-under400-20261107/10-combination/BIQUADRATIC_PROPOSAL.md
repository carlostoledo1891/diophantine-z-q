# Scaled biquadratic comparison charts

This is an exact rational change of witnesses for one reciprocal primary comparison block. It uses the already accepted domain of the reciprocal primary charts, including their identity points. It does not extend that domain. The implementing 427-to-411 candidate and its complete physical consumer audit are separate obligations.

Work over K=Q(sqrt(2)). The retained root chart supplies a,b,c with c=a^2, b^2=c^2-D, and a nonzero. Here D=11-6sqrt(2) is positive in both real embeddings and nonzero. Hence c is positive in both embeddings. Put d=c+D*r^2 and e=c+D*g^2; both are nonzero for all r,g in K, including zero.

The old block has r,J,fU,g,k,u,fV and equations

```
fU=r^2,              J^2+D*fU^2=1,
d*g=a*J-b*r,        u=c*r+b*g,
d*k=b*J-2*a*u,      fV=g^2,
k*z=-g,             J*L=r*s.
```

Retained outputs YU and YV are the actual field elements fU^2 and fV^2. Their stored component normalizations must be respected. In the proposed replacement every external use of fU and fV must factor through these outputs; the implementation must check this from all physical rows, not just semantic metadata.

Use five field elements V,Q,I,K,W, defined from an old witness by

```
V=a*r, Q=a*g, I=a*J, K=a*k, W=r*g.
```

Replace the seven old field elements and their equations by

```
V*Q=c*W,
V^2+Q^2+D*W^2+2*b*W=1,
a*I=b*V+c*Q+D*V*W,
a*K=-b*Q-c*V-D*Q*W,
I*L=V*s,
K*z=-Q,
D*c*YU+I^2=c,
D*c*YV+K^2=c.
```

Each equation is quadratic in retained and new coordinates. D is a fixed field constant. The expression c*YU is quadratic even though c=a^2, because c is retained. Removing fU and fV saves four rational coordinates in each block, sixteen over four blocks. This replaces the separate u-elimination reduction and must not be added to it.

For the proof define

```
F=c*(r^2+g^2)+D*r^2*g^2+2*b*r*g-1,
G=a*J-b*r-d*g,
A=a*k+b*g+e*r,
H=d*k-b*J+2*a*(c*r+b*g).
```

The following identities hold using only c=a^2 and b^2=c^2-D:

```
(b*r+d*g)^2+c*D*r^4-c = d*F,
(b*g+e*r)^2+c*D*g^4-c = e*F,
a*H = d*A-b*G-D*r*F.
```

The first two are the two discriminant identities. The third fixes the sign of the inverse addition equation. The accompanying check_biquadratic.py expands these identities exactly, including the two root relations.

For the forward map, G=0 and the old J curve give d*F=c*(J^2+D*r^4-1)=0. Since d is nonzero, F=0. The third identity and H=G=F=0 give d*A=0, hence A=0. The second identity now gives k^2+D*g^4=1 since c is nonzero. Substitution of V,Q,I,K,W gives all eight new equations. The two output equations follow from the old squared outputs.

For the reverse map set r=V/a, g=Q/a, J=I/a and k=K/a. Because c=a^2 is nonzero, the first equation forces W=r*g. The second then gives F=0. The third and fourth give G=0 and A=0. The first discriminant identity gives J^2+D*r^4=1. The second gives k^2+D*g^4=1. The third identity gives H=0. Restore fU=r^2, fV=g^2 and u=c*r+b*g. The last two equations, compared with the reconstructed curve equations, give c*D*(YU-r^4)=0 and c*D*(YV-g^4)=0. Thus both squared outputs agree exactly. Dividing the ratio equations by a restores the old L and z equations.

These maps are mutually inverse and fix every retained coordinate. They never divide by r, g, J, k, W, L or z. In particular r=0 and g=0 are included. Only the already retained root a and the everywhere nonzero real-positive d are divided by. No new integrality, parity, local or height premise is introduced.

The component candidate must independently verify every old fU/fV consumer, the exact output scales, the coordinate incidence of all seven old field elements, and the full squared residual polynomial. The whole composition must then be checked against its selected accepted source.
