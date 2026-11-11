# Sparse Lucas presentation with the same 320 variables

This is a secondary exact-map proposal, not a variable-count improvement. It reduces the full quartic table from5,659 to5,598 monomials. The320 variables,290 quadratic residuals, degree four, content one and maximum coefficient16*3^(2^26) are unchanged. It is not included in the accepted320 snapshot.

The source is `../combined320/candidate320-ir.json`, SHA `d1171bc47ed8ec15aac10ca6708208e9de9c2dfa7a973732ede76269a1bee02f`. The new IR has SHA `2b18e4196a8366bc6cbaa6854b14d74a29997b76857da6f231eb7540cec34a02`; the polynomial has SHA `5e65508c848abf42c54cf95d25c4949f61dc419f953b5e43d9a78f75e5dac390`.

Write A,T,Z for the three Lucas field inputs. The source has private products C=A*Z and V=A*T, and computes

```
F+1=T^2+4Z^2-4ZC+2ZV+C^2-CV.
```

Replace the private C by S=C-2Z. Then

```
S=(A-2)*Z,  F+1=T^2+S^2-SV.
```

The forward coordinate map is new249=old249-2*old244 and new250=old250-2*old245. Its inverse adds those same terms. Every other coordinate is fixed. These are invertible affine maps over Q without guards, exceptional cases or new arithmetic premises.

Only rows201,202,205,206 consume the changed coordinates. The old imaginary output scaling of F is retained: physical F+1 has components v253 and2*v254. The checker writes the new field equations with this normalization and verifies both substitutions against all four complete old rows. Every other residual and all other coordinate metadata are identical. Thus all logarithm, detector, local and global consumers receive exactly the old F value.

`verify.py` imports no builder and checks the complete private incidence, both inverse maps, all unchanged objects and the full primitive SOS. All checks pass. Because no changed row contains the fixed anchor constant, its existing coefficient maximum remains; all changed constant coefficients are below the same bound. The61-monomial decrease is a representation-size result only. No independent acceptance is claimed or needed for the currently selected unchanged candidate; use in a later selected artifact requires its own finite review.
