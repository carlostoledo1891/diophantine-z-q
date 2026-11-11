# Root-product coordinate model: author proposal

Status: proposed exact quadratic presentation; independent review required. This is an author contribution by /root/v14_final_disjoint_assembly_review, not an independent acceptance. The parent is the accepted scalar-S245 construction. No V14 files are changed. All arithmetic premises and the ineffective defining threshold remain unchanged.

Put K=Q(r), r^2=2, d=3-r, D=d^2=11-6r. Every block in the parent has h,j,x,V,Q,W,I,Kout satisfying x=h^2, j^2=x^2-D and

h I=j V+D V W+x Q,
h Kout=-j Q-x V-D Q W,
VQ=xW,
V^2+Q^2+2jW+DW^2=1.

It also retains FU,FV with I^2=x(1-D FU), Kout^2=x(1-D FV); the two coefficients of FU and FV are parent coordinates with imaginary component scaled by2. The parent reciprocal and primary ratios are Q+Kout*zV=0 and V*S_H=I*L. Every alternate ratio is left unchanged.

## New equations

Replace the eight field coordinates h,j,x,V,Q,W,I,Kout by seven A,B,C,E,i,k,u. Retain FU,FV,zV,L and every other coordinate. Impose:

(1) A^2+B^2+2CE=0;
(2) AC=d(i-k);
(3) BE=d(i+k);
(4) (A+B)^2=4D u;
(5) FU=u^2;
(6) i^2+D FU=1;
(7) k^2+D FV=1;
(8) A-B+2d k*zV=0;
(9) (A+B)S_H=2d i*L.

All are quadratic over K. No division by A+B, A-B, i, k, C or E is used. In particular V=0 and Q=0 strata are retained.

## Forward map

h is nonzero: otherwise j^2=-D contradicts either real embedding. Set

A=d(V+Q)/h, B=d(V-Q)/h,
C=(x+j+DW)/h, E=C-2h,
i=I/h, k=Kout/h, u=(A+B)^2/(4D).

The old circle equation gives (j+DW)^2+D(V^2+Q^2)=x^2. Together with VQ=xW it gives equation(1). The two old linear equations for I,Kout give (2),(3). Equations(4),(8),(9) follow directly. To obtain (5), the parent equations imply I^2=x(1-D(V/h)^4): this identity is also verified by expanding the displayed old equations using VQ=xW and the circle equation. Since x is nonzero, FU=(V/h)^4=u^2. Equations(6),(7) are exactly the old test equations divided by x. All other witnesses remain unchanged.

## Inverse map and no extra solutions

Set

h=(C-E)/2, x=h^2,
j=(B^2+C^2-A^2-E^2)/4,
V=h(A+B)/(2d), Q=h(A-B)/(2d),
I=h i, Kout=h k, W=(A^2-B^2)/(4D).

Write alpha=(B^2+C^2)/2, beta=(A^2+E^2)/2. Equation(1) gives alpha+beta=2h^2. The identity

(B^2+C^2)(A^2+E^2)=(AB-CE)^2+(AC+BE)^2

and equations(1)-(6) give alpha*beta=D: AB-CE=(A+B)^2/2=2D u and AC+BE=2d i. Thus j^2=h^4-D. In particular h cannot vanish over the real field K. Also j cannot vanish: h^4=d^2 would imply h^2=d under either positive embedding, but Norm(d)=7 is not a rational square, so d is not a square in K. This uses only the original field and fixed constant, not a new arithmetic assumption.

Direct substitution gives j+DW=(C^2-E^2)/4, x+j+DW=hC, j-x+DW=hE. Equations(2),(3), by addition/subtraction, imply the two old I,Kout equations. VQ=xW follows immediately. Equation(1) gives

D(V^2+Q^2)+(j+DW)^2=x^2,

and j^2=x^2-D then gives the old circle equation. Equations(6),(7) give exactly the two old test equations. Equations(8),(9), multiplied by h/(2d), give exactly the old reciprocal and primary ratios. All untouched parent equations therefore hold once their retained scalar root outputs below are restored.

These maps compose to the identity. For the nontrivial root j component, substitution of forward A,B,C,E gives j using VQ=xW; W similarly follows from VQ=xW. Conversely the displayed inverse gives x+j+DW=hC and h nonzero, so recovers C, hence E, and every other new coordinate. Thus this is an isomorphism of rational witness sets, with the parent input and parameter fixed.

## Remaining consumers and complete count

The only parent root consumers outside the four blocks are the aggregate trace and scalar-S direct ratio. Retain jS as one field coordinate, impose its displayed quadratic formula, and substitute hS=(CS-ES)/2 linearly into Z*jS=hS*S_H. No xS output is needed in the scalar-S parent. Add one rational T and impose T=(1/4)Tr_K/Q(sum h_l^2), a quadratic equation; then the old detector1 scaling becomes t=T*lambda, still quadratic. All four h_l are linear expressions, so no hidden lift is needed.

Each block removes16 rational coordinates and introduces14, saving8 rational across four blocks. Retaining jS adds2, and T adds1: 245-8+2+1=240 total rational coordinates (including input),239 quantified witnesses. Each block replaces the parent8 field root/pair/test equations by7, saving8 rational equations overall; jS adds2, T adds1. Thus219-8+2+1=214 quadratic equations. Reciprocal and primary ratio replacements preserve counts. Exact expansion and consumer checks are recorded separately.

The defining-property theorem follows by this fixed-input witness bijection from the scalar-S parent. Its arithmetic and aggregate-height assumptions are unchanged. N0 remains ineffective. A finite coefficient-stability threshold is not a sufficient defining threshold.
