# Exact 233-variable reference-square construction

This candidate starts from accepted raw235/209 IR53b3296814c84d5a7f695829957cfbcd8829018b5799f58339f8518f2e35e395. The selected author proof is global/reference-square-elimination-233-018/AUTHOR-PROOF.md SHA5c408c1777417ab96106e3339b8864f9dadce5a0635c05fb10d416f62cbb74cd, manifestfc28511590c5a4093588e966d18189a939692bc50fd4a9d377d7ed6505294162. Local review0780bd483f04eae7bc0914510abf817374a89873ee69b3c1c50df9344982690c is separate from full finite acceptance.

Use parent235 coordinates f=x17+sqrt(2)x18,g=x137+sqrt(2)x138,v=x21+sqrt(2)x22,B=x84+2sqrt(2)x85=f²,w=x31+2sqrt(2)x32=v². Let a=57-28sqrt(2),c=88-48sqrt(2),d=39-36sqrt(2),A=a+cf,N=8-af-2dg. Remove precisely coordinates21/22 and rows5/6/7/8. Those are all occurrences of either removed coordinate, checked directly. Insert the two rational components of

    (a²+2ac f+c²B)*w-N²=0.

Every term is at most quadratic because B is already stored. All205 other rows are unchanged through i↦i for i<21 and i↦i-2 for i>22. MAP.json contains every index and row correspondence plus exact nonzero denominator/content normalization for the two new rows. VERIFICATION.json hashes every unchanged transported row.

Forward, discard parentv and renumber. Backward, reconstruct v=N/A in K. In final233 coordinates f0=x17,f1=x18,g0=x135,g1=x136. Set A0=57+88f0-96f1,A1=-28+88f1-48f0,N0=8-57f0+56f1-78g0+144g1,N1=28f0-57f1+72g0-78g1. Recover parent21=(N0*A0-2N1*A1)/(A0²-2A1²), parent22=(N1*A0-N0*A1)/(A0²-2A1²). Carry every other value through the inverse index map.

The cited proof establishes A!=0 before this inverse, using only retained F/E equations, f-square and scalar parity/forced149 inputs. It does not assume a meaning for removedv or the retainedw. Hence the norm denominator is nonzero; individual A components, S,g,w may vanish. The new equation givesw=v², and the retained identities recoverg²=fv. Conversely the accepted235 equations giveA*v=N and therefore the new equation. Thus both maps are inverse for the admitted fixed-parameter family, fixing input and A_N. No equivalence for arbitrary symbolic A_N is asserted. The defining threshold remains ineffective.

The complete quartic is the sum of squares of207 primitive integer quadratics. All233 coordinates occur. A separately ordered integer convolution matches the entire delivered polynomial:3209 coordinate monomials,3210 parameter-separated terms, degree4,content1. The maximal coefficient remains A_N²+1 forN>=53; full profile bounds were checked, and this is only a coefficient-size threshold. Twelve exact field inverse tests include a zero real or imaginary component ofA andg=0. No V14/V15 or release files changed.

