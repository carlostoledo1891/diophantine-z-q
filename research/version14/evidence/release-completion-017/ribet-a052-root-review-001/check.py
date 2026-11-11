"""Independent byte/provenance checks for the bounded Ribet replacement.

These checks do not establish any mathematical assertion.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("proposal")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    proposal = ROOT / args.proposal
    manifest_path = proposal / "MANIFEST.json"
    manifest = read_json(manifest_path)
    checked = []
    failures = []

    def check_pin(pin, where):
        path = ROOT / pin["path"]
        try:
            raw = path.read_bytes()
        except OSError as exc:
            failures.append({"where": where, "error": str(exc)})
            return
        ok = digest(raw) == pin["sha256"]
        if "bytes" in pin:
            ok = ok and len(raw) == pin["bytes"]
        if "excerpt_sha256" in pin:
            a, b = pin["start_line"], pin["end_line"]
            excerpt = b"".join(raw.splitlines(keepends=True)[a - 1:b])
            ok = ok and digest(excerpt) == pin["excerpt_sha256"]
        checked.append({"where": where, "path": pin["path"], "ok": ok})
        if not ok:
            failures.append({"where": where, "error": "pin or excerpt mismatch"})

    def walk(value, where):
        if isinstance(value, dict):
            if isinstance(value.get("path"), str) and isinstance(value.get("sha256"), str):
                check_pin(value, where)
            for key, child in value.items():
                walk(child, where + "/" + key)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, where + "/" + str(index))

    walk(manifest, "MANIFEST")
    records = {}
    inherited = {}
    lineage_path, lineage = manifest_path, manifest
    seen = set()
    while lineage_path not in seen:
        seen.add(lineage_path)
        for pin in lineage.get("files", []):
            inherited.setdefault(Path(pin["path"]).name, ROOT / pin["path"])
        prior_path = lineage_path.parent / "PRIOR-RECORDS.json"
        if prior_path.exists():
            prior_records = read_json(prior_path)
            walk(prior_records, str(prior_path.relative_to(ROOT)))
            for pin in prior_records["records"]:
                inherited.setdefault(Path(pin["path"]).name, ROOT / pin["path"])
        if "prior" not in lineage:
            break
        lineage_path = ROOT / lineage["prior"]["path"]
        lineage = read_json(lineage_path)
        walk(lineage, str(lineage_path.relative_to(ROOT)))
    for name in ["APPLICATIONS.json", "EDIT-MAP.json", "SOURCE-PINS.json", "RELATED-USES.json"]:
        path = proposal / name
        if not path.exists() and name in inherited:
            path = inherited[name]
        if path.exists():
            records[name] = read_json(path)
            walk(records[name], name)
    edits = records["EDIT-MAP.json"]
    base_raw = (ROOT / edits["base"]["path"]).read_bytes()
    current = ROOT / "work/quartic-v14-release/preview-repository/manuscripts/quartic_v14.tex"
    current_equal_base = current.read_bytes() == base_raw
    raw = base_raw
    replay = []
    for edit in edits["edits"]:
        before, after = edit["old_utf8"].encode(), edit["new_utf8"].encode()
        count = raw.count(before)
        ok = count == 1 and digest(before) == edit["old_sha256"] and digest(after) == edit["new_sha256"]
        replay.append({"id": edit["id"], "unique_before": count, "hashes_and_unique": ok})
        if not ok:
            failures.append({"where": edit["id"], "error": "edit not unique or fragment hash mismatch"})
        else:
            raw = raw.replace(before, after, 1)
    actual = (ROOT / edits["candidate"]["path"]).read_bytes()
    if raw != actual:
        failures.append({"where": "candidate", "error": "exact edit replay differs"})
    apps = records["APPLICATIONS.json"]["applications"]
    ten_fields = ["statement", "objects", "hypotheses", "quantifiers", "parameter_range", "uniformity", "constants", "normalizations", "exceptional_cases", "limit_order"]
    for app in apps:
        if not all(app.get("assertion", {}).get(field) for field in ten_fields):
            failures.append({"where": app["id"], "error": "missing assertion contract field"})
    result = {
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "reviewer": "/root",
        "proposal": args.proposal,
        "proposal_manifest_sha256": digest(manifest_path.read_bytes()),
        "current_manuscript_equals_reviewed_base": current_equal_base,
        "current_manuscript_sha256": digest(current.read_bytes()),
        "candidate_sha256": digest(actual),
        "exact_edit_replay": raw == actual,
        "application_count": len(apps),
        "nine_obligation_keys": list(records["APPLICATIONS.json"].get("nine_obligations", {})),
        "pin_occurrences_checked": len(checked),
        "pins": checked,
        "edits": replay,
        "failures": failures,
        "scope": "Byte/provenance evidence only; independent source reading and mathematical reasoning are recorded separately.",
    }
    target = OUT / args.output
    if target.exists():
        raise SystemExit("Refusing to overwrite an existing check record")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["proposal_manifest_sha256", "current_manuscript_equals_reviewed_base", "candidate_sha256", "exact_edit_replay", "application_count", "pin_occurrences_checked", "failures"]}))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
