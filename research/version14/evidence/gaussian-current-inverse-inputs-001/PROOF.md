# Current relative inverse and interval norm inputs

These are author source/application proposals for the current Gaussian proof. The historical DK route supplies no input here.

## Published source

Green and Tao, Linear equations in primes, Annals of Mathematics 171 (2010), 1753-1850, final published PDF SHA256 ec126f9c9e189cc0308b83fb4f9f93c29a47d11ad875391aff4ce4c42aef1001. Proposition10.1 is on printed p.1791. AppendixB equations(B.12)-(B.15) and LemmaB.5 are on pp.1817-1818. The local extracted text has SHA256 47e13fe836546ba61717b0873bab6bea35d5b99fee8b67f485baf5592b25f1e4. The directory named final-source-dk is only historical storage; it does not identify the theorem used.

## Relative inverse source

Assuming GI(k), for each fixed 0<delta<=1 and C>=20, Proposition10.1 gives a finite family of k-step nilmanifolds depending only on k,delta,C. If Q in [CL,2CL] is prime, nu is an (k+2)2^(k+1)-pseudorandom measure on Z/QZ, f:[L]->R satisfies |f|<=nu and its normalized U^(k+1)[L] norm is at least delta, then f has correlation bounded below by a positive constant depending only on k,delta,C with a 1-bounded k-step linear nilsequence from this family, of bounded Lipschitz constant depending only on the same parameters. The full pseudorandomness includes both the linear-forms and correlation conditions.

## Relative inverse connection

In the current proof set r=max(s,4), k=r-1 and select S>=(r+1)2^r and fixed C_*>2^r, C_*>=20 before the norm threshold. The independently supplied full-majorant lemma gives one fixed alpha and the required S-pseudorandom measure dominating the real function f=alpha 1_[L^(3/5),L] h. The separately supplied local GI proof supplies GI(k). Truncation and the interval-norm conversion give U^r[L] norm at least alpha delta/(4C_*). Apply Proposition10.1 at threshold min(alpha delta/(4C_*),1/2). Its finite family and correlation lower bound are independent of L, the unit residue, and the cutoff once these parameters are fixed. The existing centered-nilsequence bound and the separate stagewise cutoff construction contradict such a correlation. This source input alone does not prove the majorant lemma, GI(k), the nilsequence estimate, or the cutoff argument.

## Interval norm source

AppendixB defines the local norm by averaging over cubes wholly inside a nonempty finite set A. Equation(B.14) is the exact identity ||f||_(U^r(A))=||f 1_A||_(U^r(Z))/||1_A||_(U^r(Z)) when A lies in a finite additive group. Equation(B.12) gives the finite-group Gowers-Cauchy-Schwarz inequality. LemmaB.5 and(B.15) identify the integer interval norm with the normalized zero-extension norm in a cyclic group when alpha Q<=|I|<=Q/2, with comparison constants depending only on alpha and r, not on f.

## Interval norm connection

Take I=[L] in Z/QZ with Q in [C_*L,2C_*L]. Thus |I|/Q is between 1/(2C_*) and 1/C_*, and the interval comparison applies. Finite-group Gowers-Cauchy-Schwarz gives monotonicity of the group norms and ||1_I||_(U^s)>=|I|/Q, while ||1_I||_(U^r)<=1. Substituting the exact normalized identity gives ||f||_(U^r[I])>=||f||_(U^s[I]) L/Q. The truncated scaled lower bound alpha delta/2 therefore becomes alpha delta/(4C_*). This does not assume constant-one monotonicity of normalized interval norms. The removed interval estimate and slow-cutoff construction remain separate current arguments.

## Current locations and limits

The relative theorem is stated at main19418-19440 and applied at19645-19653. The norm convention is at19438-19440 and its actual conversion at19631-19643. All imports retain the original fixed E, actual real centered function and current cyclic ambient group. No historical DK conclusion is promoted, and no published theorem is claimed to supply the independently required GI proof.
