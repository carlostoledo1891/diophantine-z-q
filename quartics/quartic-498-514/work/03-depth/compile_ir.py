"""Exact, certificate-producing quadratic residual compiler.

S is a fixed integer parameter, not a coordinate.  No operation evaluates S.
This module uses only the Python standard library.  Coordinate ids are stable.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import reduce
import hashlib
import json
from math import gcd, lcm
from pathlib import Path
import time

# A key is (power of fixed S, sorted tuple of coordinate ids).
Poly = dict[tuple[int, tuple[int, ...]], Fraction]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def terms(poly: Poly) -> list[dict]:
    return [{"monomial": list(m), "sPower": s, "coefficient": fraction_text(c)}
            for (s, m), c in sorted(poly.items(), key=lambda item: (item[0][1], item[0][0])) if c]


def polynomial(source: list[dict]) -> Poly:
    result: Poly = {}
    for term in source:
        s = term.get("sPower", 0)
        m = tuple(term["monomial"])
        if not isinstance(s, int) or s < 0 or list(m) != sorted(m):
            raise ValueError("Invalid S power or unsorted coordinate monomial")
        c = Fraction(term["coefficient"])
        key = s, m
        result[key] = result.get(key, Fraction()) + c
        if not result[key]:
            del result[key]
    return result


def add(a: Poly, b: Poly, scale: Fraction = Fraction(1)) -> Poly:
    result = a.copy()
    for key, c in b.items():
        result[key] = result.get(key, Fraction()) + scale * c
        if not result[key]:
            del result[key]
    return result


def multiply(a: Poly, b: Poly, degree_limit: int | None = None) -> Poly:
    result: Poly = {}
    for (s, m), c in a.items():
        for (t, n), d in b.items():
            key = s + t, tuple(sorted(m + n))
            result[key] = result.get(key, Fraction()) + c * d
    result = {key: c for key, c in result.items() if c}
    if degree_limit is not None and degree(result) > degree_limit:
        raise ValueError("Degree bound exceeded")
    return result


def degree(poly: Poly) -> int:
    return max((len(m) for _, m in poly), default=0)


def variables(poly: Poly) -> set[int]:
    return {v for _, m in poly for v in m}


def substitute(poly: Poly, coordinate: int, replacement: Poly) -> Poly:
    result: Poly = {}
    powers = [{(0, ()): Fraction(1)}, replacement]
    for (s, m), c in poly.items():
        n = m.count(coordinate)
        while len(powers) <= n:
            powers.append(multiply(powers[-1], replacement))
        rest = tuple(v for v in m if v != coordinate)
        result = add(result, multiply({(s, rest): c}, powers[n]))
    return result


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Compiler:
    def __init__(self, data: dict, source_hash: str = ""):
        self.data = data
        self.coordinates = {c["id"]: c for c in data["coordinates"]}
        self.meta = {r["id"]: r for r in data["residuals"]}
        self.rows = {rid: polynomial(r["terms"]) for rid, r in self.meta.items()}
        if len(self.coordinates) != len(data["coordinates"]) or len(self.rows) != len(data["residuals"]):
            raise ValueError("Duplicate coordinate or residual id")
        for row in self.rows.values():
            if degree(row) > 2 or not variables(row).issubset(self.coordinates):
                raise ValueError("Input row is not a declared-coordinate quadratic")
        self.protected = {v for v, c in self.coordinates.items()
                          if c.get("protected", False) or c.get("kind") == "input"}
        if 0 in self.coordinates:
            self.protected.add(0)
        self.certificate = {"schema": "brox-reduction-v1", "inputSha256": source_hash,
                            "fixedParameter": "S = 3^(2^26)", "operations": []}
        self.incidence: dict[int, set] = defaultdict(set)
        for rid, row in self.rows.items():
            for v in variables(row):
                self.incidence[v].add(rid)

    def replace_row(self, rid, row: Poly):
        for v in variables(self.rows[rid]):
            self.incidence[v].discard(rid)
        self.rows[rid] = row
        for v in variables(row):
            self.incidence[v].add(rid)

    def row_add(self, target, source, factor: Fraction):
        if target == source or not factor:
            raise ValueError("Row addition requires distinct rows and nonzero multiplier")
        result = add(self.rows[target], self.rows[source], factor)
        if degree(result) > 2:
            raise AssertionError("Quadratic row operation raised degree")
        self.replace_row(target, result)
        self.certificate["operations"].append({"kind": "row_add", "target": target,
                                               "source": source, "factor": fraction_text(factor)})

    def pivot_replacement(self, coordinate, rid):
        row = self.rows[rid]
        key = (0, (coordinate,))
        a = row.get(key)
        if not a or any(coordinate in m and (s, m) != key for s, m in row):
            return None
        q = {k: -c / a for k, c in row.items() if k != key}
        return a, q

    def elimination(self, coordinate, rid):
        if coordinate in self.protected:
            return None
        pivot = self.pivot_replacement(coordinate, rid)
        if pivot is None:
            return None
        a, replacement = pivot
        affected = sorted(self.incidence[coordinate] - {rid}, key=str)
        # A quadratic replacement cannot survive a genuine nonlinear occurrence.
        # Reject early; still check the exact final degree below for all accepted cases.
        if degree(replacement) == 2:
            for other in affected:
                if any(coordinate in m and len(m) > 1 for _, m in self.rows[other]):
                    return None
        changes = {other: substitute(self.rows[other], coordinate, replacement) for other in affected}
        if any(degree(row) > 2 for row in changes.values()):
            return None
        return a, replacement, affected, changes

    def eliminate(self, coordinate, rid):
        result = self.elimination(coordinate, rid)
        if result is None:
            return False
        a, replacement, affected, changes = result
        for other, row in changes.items():
            self.replace_row(other, row)
        self.replace_row(rid, {})
        del self.rows[rid]
        del self.coordinates[coordinate]
        self.incidence.pop(coordinate, None)
        self.certificate["operations"].append({"kind": "eliminate", "coordinate": coordinate,
                                               "pivot": rid, "coefficient": fraction_text(a),
                                               "replacement": terms(replacement), "affected": affected})
        return True

    def reduce(self, max_growth: int = 400, quadratic_row_pass: bool = True):
        """Greedy deterministic elimination, with optional quadratic-row cancellation.

        max_growth limits expression blow-up, not a mathematical acceptance rule.
        Every accepted elimination is independently degree checked.
        """
        n_eliminated = 0
        n_row_adds = 0
        rounds = 0
        while True:
            rounds += 1
            candidates = []
            for v in sorted(self.coordinates, reverse=True):
                if v in self.protected or not self.incidence[v]:
                    continue
                nonlinear = any(v in m and len(m) > 1
                                for rid in self.incidence[v] for _, m in self.rows[rid])
                for rid in sorted(self.incidence[v], key=str):
                    replacement = self.pivot_replacement(v, rid)
                    if replacement is None:
                        continue
                    _, q = replacement
                    if nonlinear and degree(q) == 2:
                        continue
                    cost = (len(q) - 1) * (len(self.incidence[v]) - 1) - len(self.rows[rid])
                    if cost > max_growth:
                        continue
                    # Prefer sparse substitutions; break ties by newest coordinate.
                    candidates.append((cost, len(q), -v, str(rid), v, rid))
            if candidates:
                candidates.sort()
                _, _, _, _, v, rid = candidates[0]
                if self.eliminate(v, rid):
                    n_eliminated += 1
                    continue
                raise AssertionError("Candidate selection missed a degree failure")
            if quadratic_row_pass:
                # Cancel proportional quadratic parts.  Their difference is affine,
                # so it can expose a further degree-preserving substitution.
                signatures = {}
                changed = False
                for rid in sorted(self.rows, key=str):
                    quad = {key: c for key, c in self.rows[rid].items() if len(key[1]) == 2}
                    if not quad:
                        continue
                    first = min(quad)
                    lead = quad[first]
                    signature = tuple((key, c / lead) for key, c in sorted(quad.items()))
                    if signature in signatures:
                        source, source_lead = signatures[signature]
                        affine = add(self.rows[rid], self.rows[source], -lead / source_lead)
                        if affine and variables(affine) - self.protected:
                            self.row_add(rid, source, -lead / source_lead)
                            n_row_adds += 1
                            changed = True
                            break
                    else:
                        signatures[signature] = (rid, lead)
                if changed:
                    continue
            break
        return {"eliminations": n_eliminated, "rowAdditions": n_row_adds,
                "rounds": rounds, "heuristicMaxGrowth": max_growth}

    def normalize(self):
        """Make each row primitive in Z[S][coordinates], retaining an exact multiplier."""
        for rid in sorted(self.rows, key=str):
            row = self.rows[rid]
            if not row:
                continue
            denominator = reduce(lcm, (c.denominator for c in row.values()), 1)
            divisor = reduce(gcd, (abs(c.numerator * (denominator // c.denominator))
                                   for c in row.values()), 0)
            multiplier = Fraction(denominator, divisor)
            # Sign is canonical at the first serialized term.
            first_key = min(row, key=lambda key: (key[1], key[0]))
            if row[first_key] < 0:
                multiplier = -multiplier
            if multiplier != 1:
                self.replace_row(rid, {key: c * multiplier for key, c in row.items()})
                self.certificate["operations"].append({"kind": "normalize", "residual": rid,
                                                       "multiplier": fraction_text(multiplier)})

    def output(self):
        result = {key: value for key, value in self.data.items()
                  if key not in {"coordinates", "residuals", "gates"}}
        result.update({"schema": "brox-quadratic-ir-v1", "coordinates": list(self.coordinates.values()),
                       "residuals": [{**{k: v for k, v in self.meta[rid].items() if k != "terms"},
                                      "terms": terms(row)} for rid, row in self.rows.items()],
                       "sourceGates": self.data.get("gates", []),
                       "sourceGateStatus": "Historical metadata; definitions may be eliminated or transformed."})
        return result

    def sum_of_squares(self):
        result: Poly = {}
        for row in self.rows.values():
            result = add(result, multiply(row, row, 4))
        return result


def write_json(path: Path, data, *, newline: str = "\n"):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline=newline)


def specialization_analysis(poly: Poly):
    """Certify signs/comparisons at the fixed S by a small dominance bound.

    If x>1+sum_{i<d}|a_i/a_d|, a_d*x^d+... has sign(a_d).
    S=3^(2^26)>2^(2^27), so a bound S>2^b with b<=2^27
    does not require constructing S.  All arithmetic below stays small.
    """
    coefficients = defaultdict(dict)
    for (s, m), c in poly.items():
        coefficients[m][s] = c
    max_required_bits = 0

    def sign(p):
        nonlocal max_required_bits
        p = {s: a for s, a in p.items() if a}
        if not p:
            return 0
        d = max(p)
        leading = p[d]
        ratio = sum((abs(a / leading) for s, a in p.items() if s != d), Fraction())
        threshold = ratio.numerator // ratio.denominator + 2
        bits = threshold.bit_length()
        if bits > 2**27:
            raise ValueError("Specialization sign bound exceeds available symbolic lower bound")
        max_required_bits = max(bits, max_required_bits)
        return 1 if leading > 0 else -1

    maximal = {}
    maximal_monomial = None
    for m, coefficient in sorted(coefficients.items()):
        direction = sign(coefficient)
        absolute = {s: a * direction for s, a in coefficient.items()}
        difference = absolute.copy()
        for s, a in maximal.items():
            difference[s] = difference.get(s, Fraction()) - a
        if sign(difference) > 0:
            maximal = absolute
            maximal_monomial = m
    fixed_only = [next(iter(p.values())) for p in coefficients.values() if set(p) == {0}]
    return {"schema": "brox-fixed-specialization-v1", "fixedParameter": "S = 3^(2^26)",
            "method": "For every comparison, leading term dominates when S > 1 + sum(abs(lower/leading)).",
            "universalParameterLowerBound": "S > 2^(2^27)",
            "requiredPowerOfTwoLowerBound": max_required_bits,
            "allComparisonBoundsSatisfied": max_required_bits <= 2**27,
            "maximumAbsoluteCoefficient": [{"sPower": s, "coefficient": fraction_text(a)}
                                            for s, a in sorted(maximal.items())],
            "attainedAtMonomial": list(maximal_monomial) if maximal_monomial is not None else None,
            "maximumSIndependentCoefficientBits": max((abs(a.numerator).bit_length() for a in fixed_only), default=0),
            "integralityProof": "Every displayed scalar coefficient is an integer and S is an integer.",
            "specializationProof": "Evaluation Z[S] -> Z is a ring homomorphism; all replayed identities remain identities at this fixed S."}


def run(source: Path, destination: Path, no_reduce=False, max_growth=400):
    started = time.monotonic()
    data = json.loads(source.read_text(encoding="utf-8-sig"))
    compiler = Compiler(data, digest(source))
    initial = {"coordinates": len(compiler.coordinates), "residuals": len(compiler.rows),
               "gates": len(data.get("gates", []))}
    reduction = compiler.reduce(max_growth=max_growth) if not no_reduce else {}
    compiler.normalize()
    output = compiler.output()
    sos = compiler.sum_of_squares()
    active = variables(sos)
    if 0 in compiler.coordinates and 0 not in active:
        raise ValueError("Input coordinate is absent from final polynomial")
    live_ids = sorted(active)
    compact_ids = {old: new for new, old in enumerate(live_ids)}
    compact_coordinates = [{**compiler.coordinates[old], "id": new, "sourceId": old}
                           for old, new in compact_ids.items()]
    compact_sos = {(s, tuple(compact_ids[v] for v in m)): a for (s, m), a in sos.items()}
    free_ids = sorted(set(compiler.coordinates) - active)
    coordinate_map = {"schema": "brox-coordinate-map-v1",
                      "mapping": [{"sourceId": old, "compactId": new,
                                   "name": compiler.coordinates[old].get("name", str(old))}
                                  for old, new in compact_ids.items()],
                      "omittedFreeCoordinates": free_ids,
                      "freeReconstructionValue": "0",
                      "freeExtensionProof": "Omitted coordinates occur in no final residual or polynomial term. Every solution extends by assigning zero to them; forgetting them preserves every residual."}
    # A sum of real squares cannot hide dependence on a coordinate.  Check the
    # stronger syntactic statement too so the free-extension certificate is direct.
    if any(variables(row) & set(free_ids) for row in compiler.rows.values()):
        raise AssertionError("Polynomial-inactive coordinate still occurs in a residual")
    destination.mkdir(parents=True, exist_ok=True)
    write_json(destination / "compiled-ir.json", output)
    write_json(destination / "reduction-certificate.json", compiler.certificate)
    write_json(destination / "coordinate-map.json", coordinate_map)
    write_json(destination / "polynomial.json", {"schema": "brox-sparse-polynomial-v1",
               "fixedParameter": "S = 3^(2^26)", "coordinates": compact_coordinates,
               "terms": terms(compact_sos), "sosMultiplier": "1",
               "construction": "Exact sum of normalized residual squares, with coordinate ids compacted by coordinate-map.json"},
               newline="\r\n")  # Preserve the published polynomial bytes on every platform.
    write_json(destination / "specialization-certificate.json", specialization_analysis(compact_sos))
    # Only monomials having no other S-power give actual S-independent coefficients.
    dependent_monomials = {m for s, m in sos if s}
    independent_values = [abs(c.numerator) for (s, m), c in sos.items()
                          if s == 0 and m not in dependent_monomials and c.denominator == 1]
    report = {"schema": "brox-compiler-report-v1", "inputSha256": digest(source), "initial": initial,
              "final": {"coordinates": len(compact_coordinates), "compiledCoordinatesBeforeFreeOmission": len(compiler.coordinates),
                        "residuals": len(compiler.rows),
                        "activeCoordinates": len(variables(sos)),
                        "ordinaryCoordinateMonomials": len({m for _, m in sos}),
                        "parameterCoefficientTerms": len(sos), "degree": degree(sos),
                        "maxSPower": max((s for s, _ in sos), default=0),
                        "integerCoefficients": all(c.denominator == 1 for c in sos.values()),
                        "sIndependentCoefficientGcd": reduce(gcd, independent_values, 0)},
              "reduction": reduction,
              "omittedFreeCoordinateIds": free_ids,
              "normalizationNote": "Primitive over Z[S]; fixed-S content is 1 if S-independent coefficient gcd is 1.",
              "sourceGateNote": "Raw gate metadata is retained historically, not presented as final gate definitions.",
              "elapsedSeconds": round(time.monotonic() - started, 3)}
    report["artifacts"] = {name: digest(destination / name) for name in
                           ("compiled-ir.json", "reduction-certificate.json", "polynomial.json", "coordinate-map.json",
                            "specialization-certificate.json")}
    write_json(destination / "compiler-report.json", report)
    return report


def self_test():
    # v=x*y, w=v+z; structural w=0 allows eliminating w then v without degree growth.
    def t(m, c=1, s=0):
        return {"monomial": m, "sPower": s, "coefficient": str(c)}
    data = {"coordinates": [{"id": i, "name": str(i), "protected": i in (0, 1, 2)} for i in range(5)],
            "residuals": [{"id": "v", "terms": [t([3]), t([0, 1], -1)]},
                          {"id": "w", "terms": [t([4]), t([3], -1), t([2], -1)]},
                          {"id": "constraint", "terms": [t([4])]}], "gates": []}
    c = Compiler(data)
    assert c.reduce()["eliminations"] == 2
    assert len(c.rows) == 1 and degree(c.sum_of_squares()) == 4
    # Do not eliminate v=x*y if v*z also occurs: that would create a cubic.
    data["coordinates"] = data["coordinates"][:4]
    data["residuals"] = [data["residuals"][0], {"id": "blocked", "terms": [t([2, 3]), t([], -1)]}]
    c = Compiler(data)
    assert c.elimination(3, "v") is None
    # A fixed parameter has degree zero; normalize rational coefficients exactly.
    p = polynomial([t([0], "1/2", 1), t([], "-1/3")])
    assert degree(multiply(p, p)) == 2
    data = {"coordinates": [{"id": 0, "kind": "input"}],
            "residuals": [{"id": 0, "terms": terms(p)}]}
    c = Compiler(data)
    c.normalize()
    assert all(x.denominator == 1 for x in c.rows[0].values())
    assert c.rows[0] == {(1, (0,)): Fraction(-3), (0, ()): Fraction(2)}
    # Proportional quadratic rows expose an affine relation and one elimination.
    data = {"coordinates": [{"id": i, "protected": i < 3} for i in range(4)],
            "residuals": [{"id": "a", "terms": [t([0, 1]), t([2, 3]), t([2])]},
                          {"id": "b", "terms": [t([0, 1], 2), t([2, 3], 2), t([3])]}]}
    c = Compiler(data)
    r = c.reduce()
    assert r["rowAdditions"] == 1 and r["eliminations"] == 1
    print("compiler self-tests passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, nargs="?")
    parser.add_argument("destination", type=Path, nargs="?")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--no-reduce", action="store_true")
    parser.add_argument("--max-growth", type=int, default=400)
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.source is None or args.destination is None:
        parser.error("source and destination are required unless --self-test")
    else:
        print(json.dumps(run(args.source, args.destination, args.no_reduce, args.max_growth), indent=2))
