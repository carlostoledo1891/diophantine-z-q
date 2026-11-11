"""Conservative degree and l1 coefficient bounds, without expanding constants."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "ordinary-integer-definition.json"
EXPECTED = "4d639d4c44e69ea360d36d4591b8fdc82269d68b9363af0157d1e5c1174c7af6"


def main():
    raw = SOURCE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED
    bundle = json.loads(raw)
    library = bundle["library"]
    literals = []
    def fixed_literals(expr):
        if expr[0] == "literal":
            literals.append(expr[1].lstrip("-"))
        elif expr[0] != "ref":
            for argument in expr[1:]:
                fixed_literals(argument)
    for expr in library["fixedConstants"].values():
        fixed_literals(expr)
    max_fixed_digits = max(map(len, literals))
    assert max_fixed_digits < 5_000_000  # fewer than 20 million binary digits
    assert len(library["fixedConstants"]["W"][1]) < 250
    # A template of height h satisfies degree <= B^(8h) and
    # log2(max(1, coefficient_l1_norm)) <= B^(8h).
    # Here B is the explicit fixed integer specified in the companion proof.
    heights = []
    table = []
    const_count = 0
    macro_count = 0
    for template in library["templates"]:
        nodes = []
        for i, node in enumerate(template["nodes"]):
            op, args = node["op"], node["args"]
            if op == "var":
                h = 0
            elif op == "const":
                int(args[0])
                assert len(args[0].lstrip("-")) < 5_000_000
                const_count += 1
                h = 1
            elif op in ("add", "mul"):
                assert len(args) == 2 and all(0 <= j < i for j in args)
                h = 1 + max(nodes[j] for j in args)
            elif op == "call":
                target = args[0]
                assert 0 <= target < len(heights)
                refs = args[1:-1]
                assert all(0 <= j < i for j in refs)
                h = heights[target] + max([0] + [nodes[j] for j in refs]) + 1
            elif op == "fixed_integer":
                macro_count += 1
                h = 1
            elif op in ("psi_component", "finite_guard_product"):
                macro_count += 1
                refs = args[1:5] if op == "psi_component" else args[1:]
                assert all(0 <= j < i for j in refs)
                h = 1 + max([0] + [nodes[j] for j in refs])
            else:
                raise ValueError(op)
            nodes.append(h)
        height = nodes[template["root"]]
        heights.append(height)
        table.append({"name": template["name"], "height": height,
                      "nodes": len(nodes)})
    recipes = {}
    for name, recipe in bundle["recipes"].items():
        form = recipe["format"]
        if form == "model-evaluation-polynomial-recipe-v1":
            calls = []
            count = 8  # three generator equations and five coordinate equations
            for row in recipe["sourceVariables"]:
                if row[2] is not None:
                    calls.append(heights[recipe["operationTemplates"]["natural"]])
                    count += 1
            for entry in recipe["constantDefinitions"]:
                calls.append(heights[entry["template"]])
                count += 1
            for row in recipe["operations"]:
                if row[0] == 2:
                    calls.append(recipes[recipe["operationTemplates"]["power"]]["height"])
                else:
                    key = "addition" if row[0] == 0 else "multiplication"
                    calls.append(heights[recipe["operationTemplates"][key]])
                count += 1
            # Every point argument is a variable or a constant or minus a
            # generator variable: height at most two. Square, then finite sum.
            assert count <= 2**20
            height = max([2] + [h + 3 for h in calls]) + 2
        elif form in ("sum-of-squares-composition-v1", "product-composition-v1"):
            calls = []
            for call in recipe["calls"]:
                assert all(a[0] == "var" for a in call["parameters"])
                calls.append(heights[call["target"]] if call["kind"] == "template"
                             else recipes[call["target"]]["height"])
            count = len(calls)
            assert 1 <= count <= 2**20
            height = max(calls) + (2 if form == "sum-of-squares-composition-v1" else 1)
        else:
            raise ValueError(form)
        recipes[name] = {"height": height, "constraint_count": count}
    height = recipes[bundle["rootRecipe"]]["height"]
    result = {
        "candidate_sha256": EXPECTED,
        "total_variables": bundle["witnessCount"] + 1,
        "rational_witnesses": bundle["witnessCount"],
        "templates": table,
        "recipes": recipes,
        "explicit_constant_nodes": const_count,
        "finite_constructor_nodes": macro_count,
        "root_height_bound": height,
        "degree_bound": f"B^{8 * height}",
        "largest_absolute_coefficient_bound": f"2^(B^{8 * height})",
        "B": "max(2^20, T+1, 1+abs(c) for every fixedConstant value, every explicit scalar constant node, and every evaluated fixed_integer or psi index expression)",
        "simplified_B": "T+1, by the companion proof and the literal digit checks",
        "max_fixed_literal_decimal_digits": max_fixed_digits,
        "scope": "Syntactic size bounds for the specified candidate; not a proof of its proposed Diophantine zero set. Companion proof justifies finite-constructor and substitution bounds."
    }
    target = ROOT / "ordinary-integer-polynomial-size-bounds.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("templates", "recipes")}, indent=2))


if __name__ == "__main__":
    main()
