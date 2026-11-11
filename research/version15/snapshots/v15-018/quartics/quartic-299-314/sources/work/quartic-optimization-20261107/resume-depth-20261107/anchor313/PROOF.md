# Choosing the common inverse on the anchor quadric

Author: `/root/astra_quartic_opt03_depth`, November 7, 2026. The anchor reuse proposal and the local targets are due to agent05. This note supplies the explicit simultaneous approximation argument and verifies its order of choices. It is a contributed proof, not independent acceptance. No frozen shared314 file is changed.

The arithmetic source is shared314 `PROOF.md`, SHA256 `a8b3adc8ed7103aea1fc65cff5654632534fe151ec5ba157ad4413f79cceb4eb`, independently reviewed by agent05 at SHA256 `99630a50aac94071d7001d04afd1dcf5fa68209b34bbebff092db926720a5e33`. Its original IR is `7805ee1ebd5fec7ac20b2b5590afe9b5891c85aff8eee5f58b104a888bb9e6f5`. Agent05 plans the literal substitution on its sparse equivalent, IR `aa546258e21f0274a5baf1786c4f15d47f4d6b7ffd6d38a925bad823f0de6382`; this note does not certify that transport or its count.

## Statement and exact circuit

The retained anchor, after the existing exact unscaling, is

    u^2+6v^2-2(w+C)^2 = 3T^2-2C^2,
    T=Fs+Cq, Fs=2g0g1,
    q=48v83^2+48v87^2+432v89^2,
    C=3^(2^25).

The private anchor coordinate u is v55. None of u,v,w enters the root, scalar or comparison inputs. Put t=T/C, N=3T^2-2C^2 and z=w+C. Since t is rational, N is nonzero. The accepted quaternion criterion supplies a rational point on Q(u,v,z)=N, where Q(u,v,z)=u^2+6v^2-2z^2, whenever t is integral at2 and3.

Replace the independent common parameter gamma by1/u. Use eight new rational coordinates

    a2=u^2, a4=a2^2, a8=a4^2, a16=a8^2,
    a16*J=1, g40*a8=J^2, g80=g40^2, g160=g80^2.

These equations force u nonzero and give J=gamma^16, g40=gamma^40, g80=gamma^80, g160=gamma^160. The detector guard uses J*E8. All equations are quadratic. Thus any solution of this new circuit restores the complete shared314 circuit by setting gamma=1/u and its old powers accordingly. The anchor is unchanged. Soundness follows from shared314 without any new prime or local assumption.

Completeness is the substantive issue. For every integer input, we prove that the existing choices can be made with an anchor point satisfying

    1/(2lambda)<u<1/lambda,
    v_p(u)=-1 at every selected contact prime,
    v_p(u)=nu_p at p=2,3,17.

Its inverse then has exactly the real and finite properties required by shared314.

## Preparation before contact primes

The exact scalar source is Version13 `manuscripts/quartic_v13.tex`, SHA256 `9db71bbfcefb37db56eabcf40a5f9dd85de9ed58294635da3dbf6d4f5caa8fcd`, lines21430-21439. After fixing the prepared point H0, it chooses a multiple N0 of6m0 imposing the anchor and scalar finite depths. The formal subgroups have finite index, and the source explicitly permits arbitrary further depths. The positive progression remains dense in the required real identity component.

At this stage require Fs=f1([s]P) in8Z2. This is an additional finite depth on the already prepared scalar point, not a new arithmetic input. It is compatible with the existing3-adic anchor requirement and all finite scalar depths. The source still chooses s arbitrarily large in the same kind of positive progression and achieves its strict real scalar inequalities. Set a=s+1 and choose the remaining odd Lucas root labels as in the source. All these points and the scalar Fs are now fixed, before the contact primes.

The accepted abscissa359 calculation gives v2(X_i)=-1 for the three odd roots, with X_A=2v83, X_T=2v87, X_Z=2v89. Therefore

    q=3(2X_A)^2+3(2X_T)^2+27(2X_Z)^2 =1 modulo8.

Each 2X_i is an odd2-adic integer. Since C is odd and Fs is divisible by8, t is odd, in fact1 modulo8. The accepted anchor construction also gives t integral at3. The quaternion criterion now supplies a rational anchor point P. Fix one such P; no formula for its coordinates beyond the existing rational witnesses is assumed or needed.

Choose the finite and real neighborhoods of the comparison functions and the scales exactly as in shared314. Enlarge the permitted denominator depths so that nu2>=1, nu17>=1 and nu3>2^25, as well as all the existing detector bounds. These are finite requirements with positive slopes in the source small-prime estimates. They are imposed after the roots and test bounds are fixed and before the contact primes. Exclude the finitely many prime divisors of the denominator of the fixed T when applying the same simultaneous-prime theorem. No root or scalar datum depends on a later anchor-witness choice.

## Explicit local anchor targets

At2 set u=2^nu2, v=T/2 and

    z=(C/2)*sqrt(4-3t^2+2(u/C)^2).

The radicand is1 modulo8 because t is odd and nu2>=1. It is therefore a2-adic square. Direct substitution gives Q(u,v,z)=N. The target has exactly the required valuation of u.

At3 set u=3^nu3, v=0 and

    z=C*sqrt(1-3t^2/2+(u/C)^2/2).

Here t is3-integral and nu3>v3(C)=2^25. The radicand is1 modulo3 and is a square in Q3. Substitution again gives Q=N. This also covers t=0.

At17 set u=17^nu17, v=T/sqrt(2) and

    z=C*sqrt(1+u^2/(2C^2)).

Two is a square in Q17, with residue roots6 and11. C is a17-unit and nu17>=1, so the second radicand is1 modulo17 and has a square root. The formula is valid even if T is not17-integral or T=0.

Now let p be any selected contact prime. It is greater than76176 and avoids the denominator of T, hence N is p-integral. Set u=p^-1. With V=pv and Z=pz the required equation is

    6V^2-2Z^2=p^2N-1.

Modulo p its right side is-1, which is nonzero. If3 is a nonsquare, Z^2-3V^2 is the norm from F_(p^2), whose multiplicative norm map is surjective: the multiplicative group is cyclic and the map has exponent p+1 and image size p-1. If3 is a square, the same form factors as two independent linear coordinates and represents every residue. Thus there is a solution modulo p. At least one of V,Z is nonzero, so at least one partial derivative12V,-4Z is nonzero. Ordinary one-variable Hensel lifting, fixing the other coordinate, gives an exact Qp solution. This supplies u of valuation-1. Repeated contact incidences at the same prime use this one target, not repeated valuations.

At the real place, choose any u in the nonempty interval (1/(2lambda),1/lambda). Take v sufficiently large in absolute value that u^2+6v^2-N>0 and set z=sqrt((u^2+6v^2-N)/2). This is a real point of Q=N. All required valuation and real conditions are open subsets of their local quadrics. Every point is smooth because Q is nondegenerate and N is nonzero.

## Explicit simultaneous rational approximation

Write B for the polar bilinear form u*u'+6v*v'-2z*z'. For the fixed rational point P, define the rational map

    Phi(d)=P-2*B(P,d)/Q(d)*d, for d in F^3 with Q(d) nonzero.

It takes values on Q=N over every field F in use. If X is a point on Q=N and Q(X-P) is nonzero, then B(P,X-P)=-Q(X-P)/2, so Phi(X-P)=X. Thus this one rational map, with rational coefficients fixed by P, covers the complement of the tangent section Q(X-P)=0.

We verify directly that each of the chosen open local target sets meets that complement. Suppose first X is already outside the tangent section; nothing is needed. Otherwise B(P,X)=N. If P is not proportional to X, nondegeneracy gives a tangent vector h with B(X,h)=0 but B(P,h) nonzero. For sufficiently small local s, set

    X(s)=sqrt(1-s^2*Q(h)/N)*X+s*h.

The square root near1 exists over the reals and every Qp, including2 after making s sufficiently small. This curve lies on Q=N and tends to X. The value B(P,X(s)) has nonzero linear term s*B(P,h), so for all sufficiently small nonzero s it differs from N. If P is proportional to X, the equations Q(P)=Q(X)=N and B(P,X)=N imply P=X. The restriction of Q to the tangent plane X-perp is nondegenerate, so choose h there with Q(h) nonzero. The same curve then has B(P,X(s))=N*sqrt(1-s^2*Q(h)/N), different from N for nonzero sufficiently small s. This proves the required density without invoking weak approximation on quadrics.

For every prescribed place choose such an X in the original open target set and put d=X-P. The rational map Phi is continuous at d. It therefore suffices to approximate the three coordinates of these finitely many local direction vectors by rational numbers, closely enough that Q(d) stays nonzero and Phi(d) stays in the target sets.

Here is the elementary approximation argument for one coordinate. Choose an integer D that clears the finitely many local denominators of the target numbers. Choose sufficiently large prime-power precisions and a common modulus M, and use CRT to obtain an integer A approximating all the D-scaled local targets modulo those powers. Take an arbitrarily large positive integer L congruent to1 modulo M. Integers A+Mk have fixed required finite residues, while (A+Mk)/(D*L) have real spacing M/(D*L), tending to zero. They can therefore be chosen in any prescribed real interval. Since L is a unit congruent to1 at all the finite precisions, division by D*L preserves the required local approximations. Increasing M first absorbs the valuations of D and the desired errors. Repeat independently for the three coordinates. This proves the simultaneous rational approximation used here directly from CRT and real intervals.

Applying Phi to the resulting rational direction gives a rational anchor point satisfying every exact valuation condition and the strict real interval. Recover w=z-C. The proof's direction parameters are tools for choosing an existing rational witness; they are not new quantified coordinates in the compiled quartic.

## Final order and consequences

The order is scalar preparation with its extra2-adic depth; scalar and odd root choices; fixed T and a rational anchor basepoint; finite comparison neighborhoods, real bounds and denominator depths; contact primes avoiding fixed denominators; the original lambda choice; the anchor approximation just proved; and finally H in the unchanged Pi19/continuity progression and fixed real neighborhood.

The anchor selection imposes no new congruence on H. It changes none of Fs,T, the roots, scales or test bounds. Its u gives gamma=1/u with gamma/lambda in(1,2), valuation1 at the selected contacts and valuation-nu at2,3,17. All shared314 estimates are uniform in those conditions, so their strict real bounds, finite margins, squareclasses and pole witnesses follow exactly as before. Extra primes in the rational anchor coordinates or gamma remain harmless by the same even-denominator-support argument. No assumption on their prime support is made for arbitrary witnesses.

This establishes the proposed completeness extension at the source level. The literal eight-coordinate transport, actual anchor-private incidence, full sum of squares and resulting total count are separate compiler-review obligations. The authors of this construction cannot supply its independent acceptance.
