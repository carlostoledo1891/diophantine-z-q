"use strict";

// Assemble the actual variable-shift graph. The original ordinary-input
// universal equation and its fixed-width input bridge remain separate files.
const fs = require("node:fs");
const path = require("node:path");
const { Translator, composition, constructorDefinitions, hash } = require("./rational-circuit-translator.js");
const { buildFiniteModel, finiteArtifact, auditFiniteLibrary } = require("./finite-polynomial-expressions.js");
const { auditEvaluation, auditComposition } = require("./audit-rational-expression.js");

const point = start => Array.from({ length: 5 }, (_, i) => ["var", start + i]);
const variable = i => ["var", i];
const assert = (ok, message) => { if (!ok) throw Error(message); };
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);

function ordinaryDefinitions() {
  const definitions = constructorDefinitions();
  definitions.expressionSemantics = "Every variable ranges over Q. All calls mean literal polynomial substitution with disjoint witness blocks. Model-evaluation and sum-of-squares recipes conjoin their constraints by summing squared polynomials. A product-composition recipe multiplies its callee polynomials. Finite expansion gives one polynomial in Z[t,w].";
  definitions.compositionMeaning = "For sum-of-squares-composition-v1, each call contributes its callee polynomial at call.parameters and call.witnessStart; sum their squares. For product-composition-v1, multiply the same callee polynomials instead. Empty sums and products are 0 and 1. kind=template selects a library template, kind=recipe a named earlier recipe. Parameters [var,i] select local variable i. All witness blocks remain disjoint, including unused disjunction branches.";
  definitions.rootVariableOrdering = "The integers recipe has the one free rational variable t at index 0. Every other variable is an existential rational witness. The value recipe has five code coordinates followed by t.";
  return definitions;
}

function buildOrdinaryIntegerPolynomial(precisionPath, expectedHash) {
  const bytes = fs.readFileSync(precisionPath);
  assert(hash(bytes) === expectedHash, "Precision polynomial hash mismatch");
  const precisionSource = JSON.parse(bytes);
  const inputs = precisionSource.variables.filter(v => v.kind === "input");
  assert(inputs.length === 5 && inputs.every((v, i) => v.index === i), "Five ordered natural inputs required");
  assert(precisionSource.variableDomain === "nonnegative integers", "Wrong precision source domain");
  assert(precisionSource.templates.length === 1, "One explicit power template required");
  const { addVariableShiftTemplates } = require("./variable-shift-polynomial-library.js");
  const library = buildFiniteModel();
  addVariableShiftTemplates(library);
  const translator = new Translator(library);
  const sourceFile = "precision-natural-polynomial.json"; // Stable provenance label.
  const powerSource = precisionSource.templates[0];
  const power = translator.translate(powerSource, {
    name: "power_value", sourceInputCount: 3, naturalInputs: false,
    outputMode: "value", sourceFile: sourceFile + "#templates/0",
    sourceHash: hash(JSON.stringify(powerSource))
  });
  const precision = translator.translate(precisionSource, {
    name: "precision", sourceInputCount: 5, naturalInputs: true,
    outputMode: "zero", sourceFile, sourceHash: expectedHash, powerRecipe: power
  });
  const ids = Object.fromEntries([
    "member", "value.signed_encode", "value.close_coordinates", "value.test", "value.exceptions"
  ].map(name => [name, library.id(name)]));
  const templateCall = (call, name, parameters) => {
    const id = ids[name];
    call("template", id, parameters, library.templates[id].witnessCount);
  };

  // Parameters N,Kappa,t. A,L,J are signed model codes; their five encoded
  // natural inputs occur in exactly the reference recognizer's order.
  const close = composition("close", 11, (fresh, call) => {
    const A = fresh(5), L = fresh(5), J = fresh(5);
    const signed = [0, 5, A, L, J];
    const encoded = signed.map(() => fresh(5));
    signed.forEach((s, i) => templateCall(call, "value.signed_encode", point(s).concat(point(encoded[i]))));
    call("recipe", "precision", encoded.flatMap(point), precision.witnessCount);
    templateCall(call, "value.close_coordinates", point(A).concat(point(L), point(J), [variable(10)]));
  });
  // The same Kappa coordinates occur in Close and Test.
  const main = composition("main", 6, (fresh, call) => {
    const Kappa = fresh(5), parameters = point(0).concat(point(Kappa), [variable(5)]);
    call("recipe", "close", parameters, close.witnessCount);
    templateCall(call, "value.test", parameters);
  });
  const union = composition("value_union", 6, (_fresh, call) => {
    const parameters = point(0).concat([variable(5)]);
    templateCall(call, "value.exceptions", parameters);
    call("recipe", "main", parameters, main.witnessCount);
  });
  union.format = "product-composition-v1";
  const value = composition("value", 6, (_fresh, call) => {
    templateCall(call, "member", point(0));
    call("recipe", "value_union", point(0).concat([variable(5)]), union.witnessCount);
  });
  const integers = composition("integers", 1, (fresh, call) => {
    const N = fresh(5);
    call("recipe", "value", point(N).concat([variable(0)]), value.witnessCount);
  });

  const definitions = ordinaryDefinitions();
  const bundle = {
    format: "ordinary-integer-polynomial-expression-v1",
    status: "Specified candidate; arithmetic dependencies and independent assembly review remain necessary.",
    parameterNames: ["t"], parameterDomain: "rational numbers", witnessDomain: "rational numbers",
    witnessCount: integers.witnessCount, rootRecipe: "integers", definitions,
    library: finiteArtifact(library, translator.extraConstants, {
      meaning: "Fixed integer model and actual variable-shift coordinate predicates."
    }),
    recipes: { power_value: power, precision, close, main, value_union: union, value, integers },
    sourceHashes: { [sourceFile]: expectedHash },
    precisionInputOrder: ["n_code", "kappa_code", "a_code", "ell_code", "j_code"],
    intendedTheorem: "For every rational t, existence of rational witnesses is equivalent to t being an integer, conditional on the exact G,H,L,RC arithmetic inputs and the source recognizer/compiler theorems.",
    limitations: [
      "The source precision polynomial and signed encodings concern integer indices, never the external rational t.",
      "No proof that Z is Diophantine in Q is claimed by this artifact alone.",
      "Finite polynomial constructors define literal finite substitutions; the monomial expansion is not materialized."
    ]
  };
  const checks = auditOrdinaryIntegerPolynomial(bundle, precisionSource, expectedHash);
  return { bundle, checks };
}

function auditOrdinaryIntegerPolynomial(bundle, source, expectedHash) {
  assert(bundle.format === "ordinary-integer-polynomial-expression-v1", "Wrong artifact format");
  assert(same(bundle.parameterNames, ["t"]) && bundle.parameterDomain === "rational numbers" &&
    bundle.witnessDomain === "rational numbers", "Wrong external quantifiers");
  assert(bundle.rootRecipe === "integers", "Wrong root recipe");
  assert(same(bundle.definitions, ordinaryDefinitions()), "Polynomial interpretation changed");
  assert(same(Object.keys(bundle.recipes), ["power_value", "precision", "close", "main", "value_union", "value", "integers"]), "Recipe dependency order changed");
  assert(same(bundle.precisionInputOrder, ["n_code", "kappa_code", "a_code", "ell_code", "j_code"]), "Precision input meanings changed");
  const finite = auditFiniteLibrary(bundle.library);
  const ts = bundle.library.templates;
  const id = name => { const n = ts.findIndex(t => t.name === name); assert(n >= 0, "Missing template " + name); return n; };
  const powerSource = source.templates[0];
  const evaluations = [
    auditEvaluation(bundle, bundle.recipes.power_value, powerSource, {
      inputs: 3, naturalInputs: false, mode: "value", sourceHash: hash(JSON.stringify(powerSource))
    }),
    auditEvaluation(bundle, bundle.recipes.precision, source, {
      inputs: 5, naturalInputs: true, mode: "zero", sourceHash: expectedHash
    })
  ];
  const checks = [];
  checks.push(auditComposition(bundle, bundle.recipes.close, 11, ranges => {
    assert(ranges.length === 8 && ranges.every(r => r[1] === 5), "Close variables changed");
    const [A, L, J, ...encoded] = ranges.map(r => r[0]);
    const signed = [0, 5, A, L, J];
    return signed.map((s, i) => ({ kind: "template", target: id("value.signed_encode"), parameters: point(s).concat(point(encoded[i])) })).concat([
      { kind: "recipe", target: "precision", parameters: encoded.flatMap(point) },
      { kind: "template", target: id("value.close_coordinates"), parameters: point(A).concat(point(L), point(J), [variable(10)]) }
    ]);
  }));
  checks.push(auditComposition(bundle, bundle.recipes.main, 6, ranges => {
    assert(ranges.length === 1 && ranges[0][1] === 5, "Main shift allocation changed");
    const parameters = point(0).concat(point(ranges[0][0]), [variable(5)]);
    return [{ kind: "recipe", target: "close", parameters }, { kind: "template", target: id("value.test"), parameters }];
  }));
  assert(bundle.recipes.value_union.format === "product-composition-v1", "Exceptional union must be a product");
  // auditComposition checks bindings and partitions independently of the
  // connective; its expected marker is normalized only in this local copy.
  checks.push(auditComposition(bundle, { ...bundle.recipes.value_union, format: "sum-of-squares-composition-v1" }, 6, ranges => {
    assert(ranges.length === 0, "Unexpected union variables");
    const parameters = point(0).concat([variable(5)]);
    return [{ kind: "template", target: id("value.exceptions"), parameters }, { kind: "recipe", target: "main", parameters }];
  }));
  checks.push(auditComposition(bundle, bundle.recipes.value, 6, ranges => {
    assert(ranges.length === 0, "Unexpected value variables");
    return [{ kind: "template", target: id("member"), parameters: point(0) },
      { kind: "recipe", target: "value_union", parameters: point(0).concat([variable(5)]) }];
  }));
  checks.push(auditComposition(bundle, bundle.recipes.integers, 1, ranges => {
    assert(ranges.length === 1 && ranges[0][1] === 5, "Integer code allocation changed");
    return [{ kind: "recipe", target: "value", parameters: point(ranges[0][0]).concat([variable(0)]) }];
  }));
  assert(bundle.witnessCount === bundle.recipes.integers.witnessCount, "Root witness count changed");
  return { valid: true, evaluations, compositions: checks, witnessCount: bundle.witnessCount,
    finiteConstructorCount: finite.finitePolynomialConstructors.length,
    scope: "Source evaluation wiring and witness partitions; separate template/source and arithmetic proofs required." };
}

module.exports = { buildOrdinaryIntegerPolynomial, auditOrdinaryIntegerPolynomial, ordinaryDefinitions };
if (require.main === module) {
  const [precisionPath, expectedHash, outputPath] = process.argv.slice(2);
  assert(precisionPath && /^[a-f0-9]{64}$/.test(expectedHash || "") && outputPath,
    "Usage: node ordinary-integer-polynomial.js PRECISION_FILE SHA256 OUTPUT_FILE");
  const { bundle, checks } = buildOrdinaryIntegerPolynomial(precisionPath, expectedHash);
  const data = JSON.stringify(bundle) + "\n";
  fs.writeFileSync(outputPath, data, { flag: "wx" });
  const report = { ...checks, artifactSha256: hash(data), bytes: Buffer.byteLength(data), arithmeticTheoremProved: false };
  fs.writeFileSync(outputPath + ".checks.json", JSON.stringify(report, null, 2) + "\n", { flag: "wx" });
  console.log(JSON.stringify(report));
}
