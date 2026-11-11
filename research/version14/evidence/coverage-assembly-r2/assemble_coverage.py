"""Unsigned deterministic dossier assembly and diagnostics; never a review decision.

The deployed gate owns acceptance rules. Local diagnostics make incomplete inputs
reviewable before authenticated evidence exists; they do not replace that gate.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib
import io
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DEFAULT_VALIDATOR = ROOT / "work/protocol-v13-20261107/gate-author/adapter"
REF_INPUTS = ("applications", "uses", "coverage_index", "declared_edges_before",
              "edge_reasons", "reconciliation_histories", "preserved_reconciliation",
              "findings", "reconstruction", "proof_inventory")
USE_FIELDS = "id consumer passages assertion classification reason shared_contract_justification supplier application_id inline_argument"
ASSERTION_FIELDS = "statement objects hypotheses quantifiers parameter_range uniformity constants normalizations exceptional_cases limit_order"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def protect_inputs(outputs, inputs):
    """Reject output aliases, including existing hard links, before writing."""
    inputs = [Path(path).resolve() for path in inputs]
    for output in outputs:
        output = Path(output).resolve()
        for source in inputs:
            if output == source or (output.exists() and source.exists() and output.samefile(source)):
                raise ValueError("output would overwrite a pinned input")


def load_validator(directory):
    directory = Path(directory).resolve()
    sys.path.insert(0, str(directory))
    g = importlib.import_module("offline_manifest_gate")
    c = importlib.import_module("coverage_gate")
    for module in (g, c):
        if Path(module.__file__).resolve().parent != directory:
            raise ValueError("validator module already loaded from a different directory")
    return g, c


def strict_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON key: " + key)
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError("nonfinite JSON: " + value)))


def read_reference(ref, directory, consumed, label):
    if type(ref) is not dict or set(ref) != {"file", "sha256"}:
        raise ValueError(label + " needs exactly file and sha256")
    path = (directory / ref["file"]).resolve()
    raw = path.read_bytes()
    if sha(raw) != ref["sha256"]:
        raise ValueError(label + " input hash mismatch")
    consumed.append({"label": label, "file": str(path), "sha256": sha(raw), "bytes": len(raw)})
    return raw


def load_input(path, g):
    path = Path(path).resolve()
    raw = path.read_bytes()
    cfg = strict_json(raw)
    required = {"schema", "author_run", "profile", "scope", "initial", "blobs", *REF_INPUTS}
    if type(cfg) is not dict or set(cfg) != required or cfg["schema"] != "coverage-assembly-input/v1":
        raise ValueError("input keys must be exactly: " + ", ".join(sorted(required)))
    if not g.text(cfg["author_run"]):
        raise ValueError("actual assembly author_run is required")
    consumed = [{"label": "assembly-input", "file": str(path), "sha256": sha(raw), "bytes": len(raw)}]
    data = {key: strict_json(read_reference(cfg[key], path.parent, consumed, key)) for key in REF_INPUTS}
    if type(cfg["initial"]) is not dict or set(cfg["initial"]) != {"file", "sha256", "pin"}:
        raise ValueError("initial needs exactly file, sha256, pin")
    initial_raw = read_reference({key: cfg["initial"][key] for key in ("file", "sha256")},
                                 path.parent, consumed, "initial")
    if cfg["initial"]["pin"].get("sha256") != sha(initial_raw):
        raise ValueError("initial target pin must preserve the exact initial bytes")
    data.update(profile=cfg["profile"], scope=cfg["scope"], author_run=cfg["author_run"],
                initial=strict_json(initial_raw), initial_pin=cfg["initial"]["pin"])
    blobs = {}
    for n, item in enumerate(cfg["blobs"]):
        if type(item) is not dict or set(item) != {"pin", "file"}:
            raise ValueError("each blob needs exactly pin and file")
        pin = item["pin"]
        g.fields(pin, "side path sha256", "input-blob-pin")
        if pin["side"] not in ("base", "head") or not g.path_ok(pin["path"]) or not g.hexhash(pin["sha256"]):
            raise ValueError("invalid input blob pin")
        blob = read_reference({"file": item["file"], "sha256": pin["sha256"]}, path.parent, consumed, "blob:" + str(n))
        key = (pin["side"], pin["path"], pin["sha256"])
        if key in blobs:
            raise ValueError("duplicate blob pin")
        blobs[key] = blob
    blobs[tuple(data["initial_pin"][k] for k in ("side", "path", "sha256"))] = initial_raw
    if isinstance(data["applications"], dict) and set(data["applications"]) == {"applications"}:
        data["applications"] = data["applications"]["applications"]
    return data, blobs, consumed


def assemble(data, blobs, g, c):
    """Pure assembly. Input objects are never mutated, and no history is invented."""
    issues = []
    def issue(code, **details):
        issues.append({"code": code, **details})
    def check_fields(obj, fields, where):
        try:
            g.fields(obj, fields, where)
            return True
        except (g.Invalid, TypeError, KeyError) as error:
            issue("schema", where=where, detail=str(error))
            return False
    def unique(rows, key, where):
        try:
            return g.unique(rows, key, where)
        except (g.Invalid, TypeError, KeyError) as error:
            issue("schema", where=where, detail=str(error))
            return {}
    def string_set(value, where, nonempty=False):
        try:
            return g.string_set(value, where, nonempty)
        except (g.Invalid, TypeError, KeyError) as error:
            issue("schema", where=where, detail=str(error))
            return set()
    def raw_pin(pin, where):
        if not check_fields(pin, "side path sha256", where):
            return None
        if pin["side"] not in ("base", "head") or not g.path_ok(pin["path"]) or not g.hexhash(pin["sha256"]):
            issue("invalid-pin", where=where)
            return None
        raw = blobs.get((pin["side"], pin["path"], pin["sha256"]))
        if raw is None:
            issue("missing-blob", where=where, pin=pin)
        elif sha(raw) != pin["sha256"] or len(raw) > 16 * 1024 * 1024:
            issue("invalid-blob", where=where, pin=pin)
            return None
        return raw
    def location(loc, where):
        if not check_fields(loc, "pin start_line end_line excerpt_sha256", where):
            return None
        raw = raw_pin(loc["pin"], where + ":pin")
        if raw is None:
            return None
        lines = raw.splitlines(keepends=True)
        a, b = loc["start_line"], loc["end_line"]
        if loc["pin"]["side"] != "head" or type(a) is not int or type(b) is not int or not 1 <= a <= b <= len(lines):
            issue("invalid-location-range", where=where)
            return None
        if sha(b"".join(lines[a-1:b])) != loc["excerpt_sha256"]:
            issue("stale-excerpt", where=where)
            return None
        return a, b

    profile = data["profile"]
    if not check_fields(profile, "schema protocol_version governing_protocol runtime_policy_sha256 mode claim_ids proof_paths allowed_nonmath_paths", "profile"):
        raise ValueError("profile schema invalid; see required schema documentation")
    # Call the deployed profile selector against only the exact supplied hashes.
    # This is a profile syntax/binding check, not an invented packet or receipt.
    governing = profile["governing_protocol"]
    selector_context = {"base": {"files": {}}, "head": {"files": {
        pin[1]: {"sha256": pin[2]} for pin in blobs if pin[0] == "head"}},
        "applications": data["applications"], "policy_sha256": profile["runtime_policy_sha256"]}
    try:
        c.select_profile(selector_context, profile)
    except (g.Invalid, TypeError, KeyError) as error:
        issue("deployed-profile-check", detail=str(error))
    if profile["mode"] != "substantive":
        issue("unsupported-assembly-mode", expected="substantive")
    raw_pin(dict(side="head", **governing), "governing-protocol")
    initial = data["initial"]
    check_fields(initial, "schema sources uses", "initial")
    if initial.get("schema") != "protocol-source-first/v1":
        issue("initial-schema")
    sources = initial.get("sources", [])
    inventory = data["proof_inventory"]
    if not isinstance(inventory, dict) or inventory.get("sources") != sources:
        issue("proof-inventory-pin-mismatch")
    if isinstance(inventory, dict) and inventory.get("initial_sha256") not in (None, data["initial_pin"]["sha256"]):
        issue("proof-inventory-initial-mismatch")
    if set(profile["proof_paths"]) != {p.get("path") for p in sources}:
        issue("proof-path-inventory-mismatch")
    if len(sources) != len({p.get("path") for p in sources}):
        issue("duplicate-proof-source")
    source_map = {}
    for pin in sources:
        raw = raw_pin(pin, "proof-source")
        if pin.get("side") != "head":
            issue("proof-source-not-head", pin=pin)
        if raw is not None:
            source_map[pin["path"]] = (pin, raw)
    if not g.text(data["scope"]):
        issue("missing-scope")
    reconstruction = data["reconstruction"]
    if check_fields(reconstruction, "run_id method prior_exposure limitations frozen_at compared_at", "reconstruction"):
        if not all(g.text(v) for v in reconstruction.values()):
            issue("incomplete-reconstruction")
        try:
            if c.timestamp(reconstruction["frozen_at"]) >= c.timestamp(reconstruction["compared_at"]):
                issue("reconstruction-chronology")
        except (g.Invalid, TypeError) as error:
            issue("reconstruction-time", detail=str(error))
    apps = unique(data["applications"], "id", "applications")
    for aid, app in apps.items():
        if app.get("kind") == "coverage" or aid == c.COVERAGE_ID:
            issue("coverage-app-in-ordinary-catalog", application=aid)
        if not check_fields(app, "id kind authors dependencies files obligations", "application:" + aid):
            continue
        if app["kind"] not in g.KINDS:
            issue("invalid-application-kind", application=aid)
        string_set(app["authors"], "application-authors:" + aid, True)
        if type(app["files"]) is not list or not app["files"]:
            issue("missing-application-files", application=aid)
        else:
            seen_pins = set()
            for pin in app["files"]:
                if check_fields(pin, "side path sha256", "application-pin:" + aid):
                    pair = pin["side"], pin["path"]
                    if pair in seen_pins:
                        issue("duplicate-application-pin", application=aid, path=pin["path"])
                    seen_pins.add(pair)
                    if pin["side"] not in ("base", "head") or not g.path_ok(pin["path"]) or not g.hexhash(pin["sha256"]):
                        issue("invalid-application-pin", application=aid)
        obligations = app["obligations"]
        if type(obligations) is not dict or set(obligations) != g.OBLIGATIONS:
            issue("missing-application-obligation", application=aid)
        else:
            for name, obligation in obligations.items():
                if not check_fields(obligation, "status required constructed justification evidence", "obligation:" + aid + ":" + name):
                    continue
                if obligation["status"] not in ("checked", "not_applicable"):
                    issue("unresolved-application-obligation", application=aid, obligation=name)
                if not all(g.text(obligation[k]) for k in ("required", "constructed", "justification")):
                    issue("incomplete-application-obligation", application=aid, obligation=name)
                evidence = obligation["evidence"]
                if type(evidence) is not list or not evidence or not all(p in app["files"] for p in evidence):
                    issue("unbound-obligation-evidence", application=aid, obligation=name)
    graph = {aid: string_set(app.get("dependencies"), "dependencies:" + aid) for aid, app in apps.items()}
    for aid, deps in graph.items():
        for dep in sorted(deps - set(apps)):
            issue("unknown-dependency-id", consumer=aid, supplier=dep)
    visiting, visited, cycles = [], set(), []
    def visit(aid):
        if aid in visiting:
            cycle = visiting[visiting.index(aid):] + [aid]
            if cycle not in cycles:
                cycles.append(cycle)
            return
        if aid in visited:
            return
        visiting.append(aid)
        for dep in sorted(graph.get(aid, set()) & set(apps)):
            visit(dep)
        visiting.pop()
        visited.add(aid)
    for aid in sorted(apps):
        visit(aid)
    for cycle in cycles:
        issue("dependency-cycle", cycle=cycle)
    claims = string_set(profile["claim_ids"], "profile-claims", True)
    for aid in sorted(claims - set(apps)):
        issue("unknown-claim-id", application=aid)
    uses = unique(data["uses"], "id", "uses")
    old_uses = unique(initial.get("uses"), "id", "initial-uses")
    for uid, use in old_uses.items():
        if check_fields(use, USE_FIELDS, "initial-use:" + uid):
            if check_fields(use["assertion"], ASSERTION_FIELDS, "initial-assertion:" + uid):
                if not all(g.text(v) for v in use["assertion"].values()):
                    issue("incomplete-initial-assertion", use=uid)
    index = unique(data["coverage_index"], "id", "coverage-index")
    covered = {path: set() for path in source_map}
    indexed_claims = set()
    for pid, row in index.items():
        if not check_fields(row, "id claim_ids location status reason use_ids no_imports_reason", "passage:" + pid):
            continue
        span = location(row["location"], "passage:" + pid)
        path = row["location"].get("pin", {}).get("path")
        if path not in source_map or row["location"].get("pin") != source_map[path][0]:
            issue("passage-outside-pinned-proof", passage=pid)
        elif span:
            covered[path].update(range(span[0], span[1] + 1))
        linked_claims = string_set(row["claim_ids"], "passage-claims:" + pid)
        linked_uses = string_set(row["use_ids"], "passage-uses:" + pid)
        for aid in sorted(linked_claims - set(apps)):
            issue("unknown-passage-claim", passage=pid, application=aid)
        for uid in sorted(linked_uses - set(uses)):
            issue("unknown-passage-use", passage=pid, use=uid)
        if not g.text(row["reason"]):
            issue("missing-passage-reason", passage=pid)
        if row["status"] == "reviewed":
            indexed_claims.update(linked_claims)
            if not linked_claims:
                issue("reviewed-passage-without-claim", passage=pid)
            imports = any(uses[u].get("classification") == "dependency" for u in linked_uses & set(uses))
            if (imports and row["no_imports_reason"] is not None) or (not imports and not g.text(row["no_imports_reason"])):
                issue("passage-import-classification", passage=pid)
        elif row["status"] == "outside_claimed_proof":
            if linked_claims or linked_uses:
                issue("claimed-passage-marked-outside", passage=pid)
        else:
            issue("unreviewed-passage", passage=pid, status=row["status"])
    for aid in sorted(claims - indexed_claims):
        issue("uncovered-claim-id", application=aid)
    for path, (_, raw) in source_map.items():
        missing = sorted(set(range(1, len(raw.splitlines()) + 1)) - covered[path])
        ranges = []
        for line in missing:
            if ranges and ranges[-1][1] + 1 == line:
                ranges[-1][1] = line
            else:
                ranges.append([line, line])
        if ranges or not raw.splitlines():
            issue("missing-proof-lines", path=path, ranges=ranges)
    required_edges = {}
    for uid, use in uses.items():
        if not check_fields(use, USE_FIELDS, "use:" + uid):
            continue
        assertion = use["assertion"]
        if check_fields(assertion, ASSERTION_FIELDS, "assertion:" + uid) and not all(g.text(v) for v in assertion.values()):
            issue("incomplete-assertion", use=uid)
        if use["consumer"] not in apps:
            issue("unknown-consumer-id", use=uid, application=use["consumer"])
        passages = string_set(use["passages"], "use-passages:" + uid, True)
        linked_back = {pid for pid, row in index.items() if uid in row.get("use_ids", [])}
        if passages != linked_back:
            issue("use-passage-links", use=uid, declared=sorted(passages), linked=sorted(linked_back))
        for pid in sorted(passages):
            if pid not in index or use["consumer"] not in index[pid].get("claim_ids", []):
                issue("missing-consuming-passage", use=uid, passage=pid)
        if not g.text(use["reason"]) or (len(passages) > 1 and not g.text(use["shared_contract_justification"])):
            issue("missing-use-explanation", use=uid)
        if use["classification"] not in ("dependency", "notation", "background", "unused_reference"):
            issue("unknown-use-classification", use=uid)
        if use["classification"] != "dependency":
            if any(use[k] is not None for k in ("supplier", "application_id", "inline_argument")):
                issue("nondependency-contract", use=uid)
            continue
        supplier = use["supplier"]
        if not check_fields(supplier, "kind application_id location statement publication", "supplier:" + uid):
            continue
        location(supplier["location"], "supplier:" + uid)
        if supplier["kind"] not in ("internal", "published_external", "computation", "inline") or not g.text(supplier["statement"]):
            issue("unresolved-supplier", use=uid)
        sid = supplier["application_id"]
        if supplier["kind"] == "internal":
            required_edges.setdefault((use["consumer"], sid), []).append(uid)
            if sid not in apps:
                issue("unknown-supplier-id", use=uid, application=sid)
            if sid not in graph.get(use["consumer"], set()):
                issue("missing-direct-edge", use=uid, consumer=use["consumer"], supplier=sid)
            if supplier["location"]["pin"] not in apps.get(sid, {}).get("files", []):
                issue("supplier-pin-not-bound", use=uid, application=sid)
        elif sid is not None:
            issue("noninternal-application-id", use=uid)
        if supplier["kind"] == "published_external":
            publication = supplier["publication"]
            if check_fields(publication, "title authors venue authoritative_version locator corrections", "publication:" + uid) and not all(g.text(v) for v in publication.values()):
                issue("incomplete-publication", use=uid)
        elif supplier["publication"] is not None:
            issue("unexpected-publication", use=uid)
        aid = use["application_id"]
        if aid is None:
            if use["inline_argument"] is None:
                issue("unchecked-use", use=uid)
            else:
                location(use["inline_argument"], "inline:" + uid)
        else:
            if aid not in apps or use["inline_argument"] is not None:
                issue("invalid-application-match", use=uid, application=aid)
            pins = [supplier["location"]["pin"]] + [index[p]["location"]["pin"] for p in passages if p in index]
            if not all(p in apps.get(aid, {}).get("files", []) for p in pins):
                issue("application-pins-not-bound", use=uid, application=aid)
    reasons = data["edge_reasons"]
    if type(reasons) is not dict:
        raise ValueError("edge_reasons must be an object keyed by CONSUMER->SUPPLIER")
    edges = {}
    for aid in sorted(graph):
        for dep in sorted(graph[aid]):
            key = aid + "->" + dep
            reason = reasons.get(key)
            if not g.text(reason):
                issue("missing-edge-explanation", edge=key)
            edges[key] = {"consumer": aid, "supplier": dep,
                          "use_ids": sorted(required_edges.get((aid, dep), [])), "reason": reason}
    for key in sorted(set(reasons) - set(edges)):
        issue("unused-edge-explanation", edge=key)
    def keyed_edges(rows, where):
        result = {}
        if type(rows) is not list:
            issue("schema", where=where, detail="expected a list")
            return result
        for row in rows:
            if not check_fields(row, "consumer supplier use_ids reason", where):
                continue
            key = row["consumer"] + "->" + row["supplier"]
            if key in result:
                issue("duplicate-edge", where=where, edge=key)
            if row["consumer"] not in apps or row["supplier"] not in apps:
                issue("unknown-prior-edge-id", edge=key)
            result[key] = row
        return result
    old_edges = keyed_edges(data["declared_edges_before"], "prior-edge")
    diffs = {"use:" + k: (old_uses.get(k), uses.get(k)) for k in set(old_uses) | set(uses) if old_uses.get(k) != uses.get(k)}
    diffs.update({"edge:" + k: (old_edges.get(k), edges.get(k)) for k in set(old_edges) | set(edges) if old_edges.get(k) != edges.get(k)})
    for key, edge in edges.items():
        if not edge["use_ids"]:
            diffs["edge:" + key] = old_edges.get(key), edge
    supplied = unique(data["reconciliation_histories"], "id", "reconciliation-histories")
    preserved = unique(data["preserved_reconciliation"], "id", "preserved-reconciliation")
    findings = unique(data["findings"], "id", "findings")
    for fid, finding in findings.items():
        check_fields(finding, "id body_sha256 status reason authors applications duplicate_of", "finding:" + fid)
        if finding.get("status") not in ("repaired", "rebutted", "duplicate", "out_of_scope"):
            issue("open-finding", finding=fid, status=finding.get("status"))
        for aid in sorted(set(finding.get("applications", [])) - set(apps)):
            issue("unknown-finding-application", finding=fid, application=aid)
        if finding.get("status") == "duplicate" and finding.get("duplicate_of") not in findings:
            issue("unknown-duplicate-finding", finding=fid, target=finding.get("duplicate_of"))
    reconciliation = []
    for key in sorted(set(diffs) | set(supplied) | set(preserved)):
        if key not in diffs:
            collection = (old_uses, uses) if key.startswith("use:") else (old_edges, edges) if key.startswith("edge:") else ({}, {})
            identifier = key.split(":", 1)[-1]
            if identifier not in collection[0] or identifier not in collection[1]:
                issue("unbound-reconciliation", id=key)
                continue
            pair = collection[0][identifier], collection[1][identifier]
        else:
            pair = diffs[key]
        bindings = {"before_sha256": None if pair[0] is None else g.digest(pair[0]),
                    "after_sha256": None if pair[1] is None else g.digest(pair[1])}
        old = preserved.get(key)
        old_history = [] if old is None else old.get("history", [])
        safe_history = True
        if old is not None:
            if not check_fields(old, "id before_sha256 after_sha256 history", "preserved-reconciliation:" + key):
                safe_history = False
            if type(old_history) is not list or any(old.get(k) is not None and not g.hexhash(old[k]) for k in bindings):
                issue("invalid-preserved-reconciliation", id=key)
                safe_history = False
            if type(old_history) is not list:
                old_history = []
        if key not in supplied:
            # Never bind an earlier resolved disposition to a new target just
            # because it is the last preserved entry. The preserved file remains
            # intact, and the empty proposed history fails the deployed gate.
            history = []
            issue("missing-current-reconciliation-explanation", id=key,
                  preserved_history=old_history)
        else:
            row = supplied[key]
            if not check_fields(row, "id before_sha256 after_sha256 history", "reconciliation-history:" + key):
                safe_history = False
            if any(k not in row or row[k] != v for k, v in bindings.items()):
                issue("current-reconciliation-binding-mismatch", id=key, expected=bindings)
                safe_history = False
            history = row.get("history", [])
        if type(history) is not list or not history:
            issue("missing-disposition-history", id=key)
            history = history if type(history) is list else []
        if key in supplied and history[:len(old_history)] != old_history:
            issue("erased-reconciliation-history", id=key)
            safe_history = False
        if old is not None and any(old.get(k) != v for k, v in bindings.items()) and len(history) <= len(old_history):
            issue("changed-target-needs-new-disposition", id=key, preserved_bindings={k: old.get(k) for k in bindings})
            safe_history = False
        for item in history:
            if not check_fields(item, "status reason finding_ids", "history:" + key):
                safe_history = False
                continue
            ids = string_set(item["finding_ids"], "history-findings:" + key)
            if item["status"] not in ("disputed", "rejected", "resolved") or not g.text(item["reason"]):
                issue("invalid-disposition", id=key)
            if not ids <= set(findings) or (not ids and item["status"] != "resolved"):
                issue("unrecorded-finding", id=key, finding_ids=sorted(ids))
        if history and isinstance(history[-1], dict) and history[-1].get("status") != "resolved":
            issue("unresolved-reconciliation", id=key)
        # Fail closed in the actual dossier, not only in local diagnostics.
        # Original supplied/preserved histories remain in the hashed inputs.
        reconciliation.append({"id": key, **bindings, "history": history if safe_history else []})
    dossier = {"schema": "protocol-coverage/v1", "profile_sha256": g.digest(profile),
               "mode": "substantive", "sources": sources, "scope": data["scope"],
               "coverage_index": sorted(data["coverage_index"], key=lambda row: row.get("id", "")), "initial": data["initial_pin"],
               "reconstruction": reconstruction, "reconciled_uses": sorted(data["uses"], key=lambda row: row.get("id", "")),
               "declared_edges_before": data["declared_edges_before"],
               "declared_edges": [edges[k] for k in sorted(edges)], "reconciliation": reconciliation}
    report = {"schema": "coverage-assembly-diagnostics/v1",
              "status": "unresolved" if issues else "local-preflight-clean",
              "scope": "Unsigned structural assembly only. No authenticated gate result, review acceptance, or mathematical conclusion.",
              "issues": sorted(issues, key=lambda value: g.canonical(value)),
              "counts": {"applications": len(apps), "uses": len(uses), "passages": len(index),
                         "reconciliation_rows": len(reconciliation), "issues": len(issues)},
              "deferred": ["Authenticated operator evidence and receipt checks",
                           "Independent source coverage and mathematical review",
                           "Exact immutable Git snapshot validation by the deployed gate"]}
    return dossier, report


class FileBlobReader:
    def __init__(self, mapping):
        self.mapping = mapping
    def open(self, side, path, entry):
        file = self.mapping.get((side, path, entry["sha256"]))
        if file is None:
            raise OSError("missing mapped immutable blob: " + side + ":" + path)
        return Path(file).open("rb")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validator-dir", type=Path, default=DEFAULT_VALIDATOR)
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("assemble")
    build.add_argument("--input", required=True, type=Path)
    build.add_argument("--out", required=True, type=Path)
    validate = sub.add_parser("validate-records", help="Call the unmodified deployed record validator on actual supplied evidence")
    for name in ("packet", "evidence", "profile", "blob-map", "out"):
        validate.add_argument("--" + name, required=True, type=Path)
    args = parser.parse_args()
    g, c = load_validator(args.validator_dir)
    if args.command == "validate-records":
        packet, evidence, profile = (strict_json(p.read_bytes()) for p in (args.packet, args.evidence, args.profile))
        rows = strict_json(args.blob_map.read_bytes())
        mapping = {}
        for row in rows:
            pin = row["pin"]
            key = tuple(pin[k] for k in ("side", "path", "sha256"))
            if key in mapping:
                raise ValueError("duplicate validation blob mapping")
            mapping[key] = (args.blob_map.parent / row["file"]).resolve()
        protect_inputs([args.out], [args.packet, args.evidence, args.profile, args.blob_map, *mapping.values()])
        try:
            result = {"status": "deployed-record-check-completed", "result": g.check_records(packet, evidence, FileBlobReader(mapping), profile)}
            code = 0
        except (g.Invalid, g.IntegrationMissing, OSError) as error:
            result = {"status": "deployed-record-check-rejected", "error": str(error)}
            code = 2
        result["authentication"] = "Not authenticated by this command. Evidence is supplied to check_records; use the real protected intake for authentication."
        args.out.write_bytes(g.canonical(result))
        return code
    data, blobs, consumed = load_input(args.input, g)
    dossier, report = assemble(data, blobs, g, c)
    args.out.mkdir(parents=True, exist_ok=True)
    outputs = {"profile.json": data["profile"], "dossier.json": dossier, "unresolved.json": report,
               "preserved-findings.json": data["findings"],
               "preserved-reconciliation.json": data["preserved_reconciliation"]}
    protect_inputs([args.out / name for name in (*outputs, "manifest.json")], [item["file"] for item in consumed])
    for name, value in outputs.items():
        (args.out / name).write_bytes(g.canonical(value))
    manifest = {"schema": "coverage-assembly-output/v1", "assembly_author_run": data["author_run"],
                "input_files": consumed,
                "validator_files": [{"file": name, "sha256": sha((args.validator_dir / name).read_bytes())}
                                    for name in ("COVERAGE-V1.3.md", "coverage_gate.py", "offline_manifest_gate.py")],
                "outputs": [{"file": name, "sha256": sha((args.out / name).read_bytes())} for name in sorted(outputs)],
                "identity_limit": "The author_run is supplied by the operator; this tool does not authenticate or manufacture observations.",
                "review_decisions_created": False}
    (args.out / "manifest.json").write_bytes(g.canonical(manifest))
    print(json.dumps(report["counts"], sort_keys=True))
    return 2 if report["issues"] else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as error:
        print("assembly input error: " + str(error), file=sys.stderr)
        raise SystemExit(2)
