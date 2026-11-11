# Reference-domain resources for the accepted 232 family

Author-proved conditional lemma, not a smaller candidate or independent acceptance. The proof below assumes the already independently accepted reconstructed reference equations and parity conclusion; it does not reprove those premises. Retain the accepted parity criterion and intended A_N family; no assertion for arbitrary symbolic A. Work in K=Q(sqrt(2)), with d=3-sqrt(2), D=d^2, a=57-28sqrt(2), b=8-14sqrt(2), and c=88-48sqrt(2). These are physical reference variables, before sparse affine changes.

The accepted reconstruction supplies f*S^2+D*f^2=1, g^2=f*v, (b*S-d0)*g=a*f-8, and (a+c*f)*g+b*f*S+d0*f=0, where d0=39-36sqrt(2) is the reference coefficient (not d). At the inert prime149 the accepted scalar criterion gives v149(Norm(f))>0, so ord149(f)>0. This is used only after the accepted H reconstruction; it is not an alternative proof of that reconstruction.

Nonvanishing: g=0 forces f=8/a, whose norm64/1681 is a149-unit, contradiction. S=0 forces f=+/-1/d, whose norm1/7 is a149-unit, contradiction. Therefore g,S,v and v^2 are nonzero K-elements. No assertion that their individual rational components are nonzero follows. The real component of v^2 is v0^2+2v1^2>0 and hence is nonzero.

Residues: set m=ord149(f)>0. The H equation gives 2ord149(S)=-m, so m is even. The a+c*f coefficient is a unit. In the last equation the b*f*S term has order m/2, strictly below the d0*f term, so ord149(g)=m/2. Dividing its square by f and reducing modulo149 gives v congruent to b^2/a^2=8/a, because f*S^2 is congruent to1 and b^2=8a. Thus Re(v^2) reduces to308288/1681^2, a nonzero residue modulo149. Rational components of integral K-elements are149-integral since149 is unramified and2 is a unit. The real component is therefore a149-unit.

Limits: only the forced prime149 has been treated. No unit claim at every possible detector prime, no pole rescaling, no disappearance of a coordinate, and no guard deletion are justified by this note. Exact constant checks are in CHECKS.json. These resources may support a changed chart if every remaining consumer is transformed and both projection directions are established.

## Explicit inert-prime details

149 is prime and149 is5 modulo8, so2 is a nonsquare and149 is inert inQ(sqrt(2)). The valuation on the unramified quadratic completion is normalized byord(149)=1. Hence v149(Norm(f))=2ord(f). The constants a,b and b²/a² are units: Norm(a)=1681, Norm(b)=-328. Thus the leading-term comparison in the proof is strict and cannot cancel. Re((8/a)²)=308288/2825761 has numerator7 and denominator125 modulo149. This proves the claimed unit, not just its nonvanishing. The deduction uses no inverse of g or S before their nonvanishing has been proved.

## Exact same-count inverse chart and its outstanding consumers

Put h=1/g,t=f/g. The inverse is g=1/h and S=(a*t-8*h+d0)/b. The reference F/E equations become f*h=t and a+c*f+b*t*S+d0*t=0. Substituting the displayed affine S leaves quadratic equations. Conversely these equations with h nonzero imply the original F/E. For inherited intended-family tuples h is nonzero by construction; on a wholly new circuit this domain still must be derived or enforced. These equations alone do not enforce it: h=t=0,f=-a/c solves them. The accepted original scalar test would exclude that f only if its unchanged physical inputs are recovered independently.

The map has the same three K coordinates (f,h,t) as (f,S,g), so saves no variable. Moreover v=g²/f=1/(h*t), and the retained w=v² relation becomes w*h²*t²=1, of total degree5. Introducing J=h*t and K=J² gives three quadratic equations J=h*t,K=J²,w*K=1 but adds two K coordinates. Retaining g and replacing only f by t=f/g gives w*t²=g², cubic, and B=f²=t²*g², quartic. Neither direct chart is a smaller degree-four SOS system. Changing the whole reciprocal-output/pole schedule is outside these tests and remains open.
