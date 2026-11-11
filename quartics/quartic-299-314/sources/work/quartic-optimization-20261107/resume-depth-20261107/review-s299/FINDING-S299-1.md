# S299-1: wrong alternate-square cache

The provisional candidate `ab42bc98539b072ff99f5b6e1a70a1867735175612782b26b2fba169b47581fd` is rejected as an implementation of the proposed299-variable system.

Its S alternate square and regular ratio use202/203. These IDs are absent from the coordinate inventory. The actual source301 alternate-square cache is196/197, as rows148/149 show directly through `D*c*B+K^2-c=0`, with `B=v196+2*rho*v197`. The unchanged logarithm and detector consume that actual cache.

The complete active-variable check finds exactly two undeclared active IDs,202 and203. Merely declaring them would not repair the mathematical interface: the genuine cache would remain disconnected. The required correction is to use196/197 in the new S alternate-square and regular-ratio equations, regenerate the polynomial and certificate, and repeat all checks against the new hashes.

This finding was independently detected by agent03 and sent to the author, parent and complete-artifact reviewer before acceptance. Universal algebra and orientation checks were not the failing part. The source301 file remains unchanged.
