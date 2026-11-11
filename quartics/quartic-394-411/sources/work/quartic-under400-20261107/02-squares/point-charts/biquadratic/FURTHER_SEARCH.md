# Remaining chart observations

The accepted411 component is recorded in `REPORT411.md` and independently accepted in `03-depth/review-biquadratic411.md`. This note proposes no additional variable reduction.

## A component nonvanishing fact

Let d0=3-sqrt(2), D=d0² and k²+D*g⁴=1 over K=Q(sqrt(2)). Then Re(k) is always nonzero, and Im(k)=0 exactly when g=0. The same statement applies to J²+D*r⁴=1.

To prove it, suppose k² is rational. Then z=d0*g² has rational square. Writing z=z0+z1*sqrt(2), its square has irrational coefficient 2*z0*z1, so z is either rational or a rational multiple of sqrt(2). If g is nonzero, Norm(z)=7*Norm(g)² is positive. The imaginary alternative has negative norm and is impossible. In the rational alternative Norm(z)=z0² would make 7 a rational square. Therefore g=0. Now k²=1, so k=±1. In particular Re(k)=0 is never possible, while Im(k)=0 occurs exactly at g=0.

This fact is about the unscaled k and J. It does not automatically apply to the scaled coordinates K=a*k and I=a*J used in411. No saving has yet been obtained from it, and any future use should be independently reviewed.

## Parametrizations and overlap

The ordinary circle parameter t=D^(1/2)*f/(1+J) gives J=(1-t²)/(1+t²) and f=2*t/(D^(1/2)*(1+t²)). Combined with f=r², its equation contains the cubic product f*t². A new field product restores quadratic degree but removes the apparent coordinate saving. A single parameter chart also needs to account for J=-1. This is a failed direct presentation, not an impossibility theorem.

Before411, deleting the unsquared f-values via k²+D*YV=1 and deleting the private u-values by inverse addition each saved eight from427. Those changes overlapped because inverse addition used r*fV. Replacing fV by g² made that product cubic. The scaled biquadratic411 presentation resolves precisely this overlap; it saves sixteen total rather than adding sixteen to the419 result.

In411 put T=b+D*W. The equations become a*I=V*T+c*Q and a*K=-Q*T-c*V, with T²+D*(V²+Q²)=c² and D*V*Q=c*(T-b). This change is invertible because D is nonzero, but it does not save a coordinate. Directly eliminating T restores cubic products V²*Q and Q²*V. Rescaling I or K alone also changes the physical L and z equations and does not supply a free elimination.
