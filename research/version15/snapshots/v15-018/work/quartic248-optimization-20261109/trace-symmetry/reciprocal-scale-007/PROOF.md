# Reciprocal scale: 239-variable author proposal

This is an author proposal by /root/v14_final_disjoint_assembly_review. It builds on the independently accepted root-product240 presentation. No arithmetic premise, point model, or order of completeness choices is changed. Independent review is required.

The parent lambda coordinate occurs only in r=(lambda-1)^2 and t1=lambda*T. The parent T coordinate occurs only in its quadratic root-trace definition and the latter scaling equation. T is positive on every solution: T=(1/4)Tr(sum h_l^2), and each root h_l is nonzero by the accepted model. Therefore the trace is strictly positive under the rational real embedding.

Replace lambda by rho=1/lambda and delete T as a coordinate. Replace the scaling relation by

rho*t1=(1/4)Tr(sum h_l^2).

Its right side is quadratic in the unchanged root-product coordinates, so this is one quadratic equation. It forces rho nonzero without an added guard.

Let F(t) be the parent's exact monic degree-ten contact polynomial. Its five-coefficient expression in r=(t-1)^2 is copied exactly from the parent contact definition. Define G(rho)=rho^10 F(1/rho). Retain q and every downstream coordinate. Reinterpret the parent's three detector0 power coordinates as rho^2, rho^4, rho^5, with three quadratic definitions. Reinterpret its contact-polynomial coordinate as G(rho). Impose

G(rho)*(1+q)=(1-rho)^10.

Every polynomial of degree at most ten has a quadratic expression in rho,rho^2,rho^4,rho^5: choose monomials for degrees0,...,10 respectively

1, rho, rho^2, rho*rho^2, rho^4, rho^5, rho*rho^5, rho^2*rho^5, (rho^4)^2, rho^4*rho^5, (rho^5)^2.

Thus both G and the numerator have exact quadratic expressions using the same three power auxiliaries. This changes five detector0 rows (three powers, contact definition and weight relation) without adding a coordinate. All q powers, residue factors, norm equations and the second detector remain unchanged.

Forward witness map: parent lambda cannot vanish, since F(0)=0 while the parent cleared weight relation would require F(0)*(1+q)=(-1)^10=1. Set rho=1/lambda, its three powers as above, and G=rho^10*F(lambda); forget T. The new weight relation follows by multiplying the old one by rho^10. The scaling relation follows from t1=lambda*T. Every unchanged witness has exactly its old value, including q.

Inverse witness map: the new scaling equation and positivity of its quadratic trace force rho nonzero. Set lambda=1/rho, restore T as the quadratic trace, and restore the old three powers (lambda-1)^2,(lambda-1)^4,(lambda-1)^6 and contact value F(lambda)=G/rho^10. Dividing the new weight relation by rho^10 gives the parent relation. All parent rows follow. These maps are inverse on rational solutions with input and parameter fixed.

No exceptional contact is silently inverted: rho=0 is excluded by the positive trace; rho=1 corresponds exactly to lambda=1 and retains q=-1; q=0 is left untouched. In particular this is a coordinate rewrite of the established completeness construction, not a new selection of contact primes or a new height estimate. N0 remains ineffective.

The deleted T coordinate and its separate definition give239 total rational coordinates,238 quantified witnesses and213 quadratic rows. The exact finite polynomial expansion is recorded separately. The accepted240 packet is preserved.
