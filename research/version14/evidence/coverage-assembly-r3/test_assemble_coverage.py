"""Synthetic unit tests only. No fixture is actual operator or reviewer evidence."""
import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import assemble_coverage as a

g, c = a.load_validator(a.DEFAULT_VALIDATOR)
fixture_module = importlib.import_module("test_coverage_gate")


def fixture():
    case = fixture_module.Case()
    data = {
        "author_run": "synthetic-test-author",
        "profile": copy.deepcopy(case.profile),
        "scope": case.dossier["scope"],
        "initial": copy.deepcopy(case.initial),
        "initial_pin": copy.deepcopy(case.dossier["initial"]),
        "applications": copy.deepcopy([app for app in case.p["applications"] if app["id"] != c.COVERAGE_ID]),
        "uses": copy.deepcopy(case.dossier["reconciled_uses"]),
        "coverage_index": copy.deepcopy(case.dossier["coverage_index"]),
        "declared_edges_before": copy.deepcopy(case.dossier["declared_edges_before"]),
        "edge_reasons": {"B->A": case.dossier["declared_edges"][0]["reason"]},
        "reconciliation_histories": [],
        "preserved_reconciliation": [],
        "findings": copy.deepcopy(case.p["findings"]),
        "reconstruction": copy.deepcopy(case.dossier["reconstruction"]),
        "proof_inventory": {"sources": copy.deepcopy(case.initial["sources"])},
    }
    blobs = {(side, path, a.sha(raw)): raw for side in case.files
             for path, (_, raw) in case.files[side].items()}
    return case, data, blobs


class AssemblyTests(unittest.TestCase):
    def setUp(self):
        self.case, self.data, self.blobs = fixture()

    def run_assembly(self):
        return a.assemble(self.data, self.blobs, g, c)

    def codes(self):
        return {item["code"] for item in self.run_assembly()[1]["issues"]}

    def bound_use_history(self, history):
        return {"id": "use:U", "before_sha256": g.digest(self.data["initial"]["uses"][0]),
                "after_sha256": g.digest(self.data["uses"][0]), "history": history}

    def test_clean_and_deterministic_without_mutation(self):
        before = g.canonical(self.data)
        one = self.run_assembly()
        two = self.run_assembly()
        self.assertEqual(one[1]["issues"], [])
        self.assertEqual(g.canonical(one), g.canonical(two))
        self.assertEqual(before, g.canonical(self.data))

    def test_assembled_fixture_passes_unmodified_deployed_validator(self):
        dossier, report = self.run_assembly()
        self.assertEqual(report["issues"], [])
        self.case.dossier = dossier
        self.case.sync()
        result = self.case.run()
        self.assertEqual(result["protocol_coverage"], "1.3-substantive-records-reviewed")
        self.assertFalse(result["merge_authorized"])

    def test_missing_lines_reported_without_filling_index(self):
        self.data["coverage_index"].pop()
        dossier, report = self.run_assembly()
        self.assertIn("missing-proof-lines", {i["code"] for i in report["issues"]})
        self.assertEqual(len(dossier["coverage_index"]), 1)

    def test_unknown_claim_and_uncovered_claim(self):
        self.data["profile"]["claim_ids"].append("UNKNOWN")
        self.assertTrue({"unknown-claim-id", "uncovered-claim-id"} <= self.codes())

    def test_missing_direct_edge_not_added(self):
        next(x for x in self.data["applications"] if x["id"] == "B")["dependencies"] = []
        dossier, report = self.run_assembly()
        self.assertIn("missing-direct-edge", {i["code"] for i in report["issues"]})
        self.assertEqual(dossier["declared_edges"], [])

    def test_unknown_supplier(self):
        self.data["uses"][0]["supplier"]["application_id"] = "UNKNOWN"
        self.assertIn("unknown-supplier-id", self.codes())

    def test_unresolved_catalog_obligation_preserved(self):
        app = self.data["applications"][0]
        name = next(iter(app["obligations"]))
        app["obligations"][name]["status"] = "unresolved"
        self.assertIn("unresolved-application-obligation", self.codes())
        self.assertEqual(app["obligations"][name]["status"], "unresolved")

    def test_cycle_is_reported(self):
        next(x for x in self.data["applications"] if x["id"] == "A")["dependencies"] = ["B"]
        self.assertIn("dependency-cycle", self.codes())

    def test_missing_explanation_not_resolved(self):
        self.data["uses"][0]["assertion"]["statement"] = "Different synthetic assertion"
        dossier, report = self.run_assembly()
        row = next(x for x in dossier["reconciliation"] if x["id"] == "use:U")
        self.assertEqual(row["history"], [])
        self.assertEqual(row["before_sha256"], g.digest(self.data["initial"]["uses"][0]))
        self.assertEqual(row["after_sha256"], g.digest(self.data["uses"][0]))
        self.assertIn("missing-current-reconciliation-explanation", {i["code"] for i in report["issues"]})

    def test_actual_explanation_copied_and_deployed_checked(self):
        self.data["uses"][0]["assertion"]["statement"] = "Different synthetic assertion"
        history = [{"status": "resolved", "reason": "Synthetic author explanation for this exact changed statement.", "finding_ids": []}]
        self.data["reconciliation_histories"] = [self.bound_use_history(history)]
        dossier, report = self.run_assembly()
        self.assertEqual(report["issues"], [])
        self.assertEqual(dossier["reconciliation"][0]["history"], history)
        self.case.dossier = dossier
        self.case.sync()
        self.assertEqual(self.case.run()["source_uses"], 1)

    def test_disputed_history_preserved_and_remains_open(self):
        fid = self.data["findings"][0]["id"]
        history = [{"status": "disputed", "reason": "Synthetic unresolved objection.", "finding_ids": [fid]}]
        self.data["preserved_reconciliation"] = [self.bound_use_history(history)]
        self.data["reconciliation_histories"] = [self.bound_use_history(history)]
        dossier, report = self.run_assembly()
        self.assertEqual(dossier["reconciliation"][0]["history"], history)
        self.assertIn("unresolved-reconciliation", {i["code"] for i in report["issues"]})

    def test_erased_history_detected(self):
        old = [{"status": "disputed", "reason": "Old synthetic objection.", "finding_ids": ["F"]}]
        self.data["preserved_reconciliation"] = [self.bound_use_history(old)]
        self.data["reconciliation_histories"] = [self.bound_use_history([{"status": "resolved", "reason": "New synthetic text.", "finding_ids": []}])]
        self.assertIn("erased-reconciliation-history", self.codes())

    def test_old_resolved_history_cannot_resolve_a_new_target(self):
        old = [{"status": "resolved", "reason": "An earlier target was resolved.", "finding_ids": []}]
        self.data["preserved_reconciliation"] = [self.bound_use_history(old)]
        self.data["uses"][0]["reason"] = "Changed synthetic target."
        dossier, report = self.run_assembly()
        row = next(r for r in dossier["reconciliation"] if r["id"] == "use:U")
        self.assertEqual(row["history"], [])
        self.assertEqual(self.data["preserved_reconciliation"][0]["history"], old)
        self.assertTrue(any(i.get("preserved_history") == old for i in report["issues"]))

    def test_copied_resolution_with_current_bindings_cannot_resolve_changed_target(self):
        old = [{"status": "resolved", "reason": "Earlier synthetic target.", "finding_ids": []}]
        self.data["preserved_reconciliation"] = [self.bound_use_history(old)]
        self.data["uses"][0]["reason"] = "Changed synthetic target."
        self.data["reconciliation_histories"] = [self.bound_use_history(old)]
        dossier, report = self.run_assembly()
        self.assertIn("changed-target-needs-new-disposition", {i["code"] for i in report["issues"]})
        self.assertEqual(dossier["reconciliation"][0]["history"], [])
        self.case.dossier = dossier
        self.case.sync()
        with self.assertRaises(g.Invalid):
            self.case.run()

    def test_old_binding_rejected_even_with_appended_resolution(self):
        old = [{"status": "resolved", "reason": "Earlier synthetic target.", "finding_ids": []}]
        row = self.bound_use_history(old)
        self.data["uses"][0]["reason"] = "Changed synthetic target."
        row["history"] = old + [{"status": "resolved", "reason": "New synthetic disposition.", "finding_ids": []}]
        self.data["reconciliation_histories"] = [row]
        dossier, report = self.run_assembly()
        self.assertIn("current-reconciliation-binding-mismatch", {i["code"] for i in report["issues"]})
        self.assertEqual(dossier["reconciliation"][0]["history"], [])

    def test_duplicated_old_terminal_disposition_fails_deployed_gate(self):
        old = [{"status": "resolved", "reason": "Earlier synthetic target.", "finding_ids": []}]
        self.data["preserved_reconciliation"] = [self.bound_use_history(old)]
        self.data["uses"][0]["reason"] = "Changed synthetic target."
        self.data["reconciliation_histories"] = [self.bound_use_history(old + copy.deepcopy(old))]
        dossier, report = self.run_assembly()
        self.assertIn("changed-target-repeats-old-disposition", {i["code"] for i in report["issues"]})
        self.assertEqual(dossier["reconciliation"][0]["history"], [])
        self.case.dossier = dossier
        self.case.sync()
        with self.assertRaises(g.Invalid):
            self.case.run()

    def test_changed_target_with_bound_appended_disposition_passes(self):
        old = [{"status": "resolved", "reason": "Earlier synthetic target.", "finding_ids": []}]
        self.data["preserved_reconciliation"] = [self.bound_use_history(old)]
        self.data["uses"][0]["reason"] = "Changed synthetic target."
        history = old + [{"status": "resolved", "reason": "Synthetic explicit disposition of the changed target.", "finding_ids": []}]
        self.data["reconciliation_histories"] = [self.bound_use_history(history)]
        dossier, report = self.run_assembly()
        self.assertEqual(report["issues"], [])
        self.assertEqual(dossier["reconciliation"][0]["history"], history)
        self.case.dossier = dossier
        self.case.sync()
        self.assertEqual(self.case.run()["source_uses"], 1)

    def test_unchanged_target_preserves_bound_history(self):
        history = [{"status": "resolved", "reason": "Same synthetic target.", "finding_ids": []}]
        self.data["preserved_reconciliation"] = [self.bound_use_history(history)]
        self.data["reconciliation_histories"] = [self.bound_use_history(history)]
        dossier, report = self.run_assembly()
        self.assertEqual(report["issues"], [])
        self.assertEqual(dossier["reconciliation"][0]["history"], history)

    def test_missing_bindings_fail_closed(self):
        self.data["uses"][0]["reason"] = "Changed synthetic target."
        self.data["reconciliation_histories"] = [{"id": "use:U", "history": [{"status": "resolved", "reason": "Unbound synthetic resolution.", "finding_ids": []}]}]
        dossier, report = self.run_assembly()
        self.assertIn("current-reconciliation-binding-mismatch", {i["code"] for i in report["issues"]})
        self.assertEqual(dossier["reconciliation"][0]["history"], [])

    def test_changed_edge_also_requires_new_disposition(self):
        key = "B->A"
        prior = self.data["declared_edges_before"][0]
        old = [{"status": "resolved", "reason": "Earlier synthetic edge.", "finding_ids": []}]
        self.data["preserved_reconciliation"] = [{"id": "edge:" + key, "before_sha256": g.digest(prior), "after_sha256": g.digest(prior), "history": old}]
        self.data["edge_reasons"][key] = "Changed synthetic edge explanation."
        changed = dict(prior, reason=self.data["edge_reasons"][key])
        self.data["reconciliation_histories"] = [{"id": "edge:" + key, "before_sha256": g.digest(prior), "after_sha256": g.digest(changed), "history": old}]
        dossier, report = self.run_assembly()
        self.assertIn("changed-target-needs-new-disposition", {i["code"] for i in report["issues"]})
        self.assertEqual(dossier["reconciliation"][0]["history"], [])

    def test_duplicate_uses_reported_and_not_silently_deduplicated(self):
        self.data["uses"].append(copy.deepcopy(self.data["uses"][0]))
        dossier, report = self.run_assembly()
        self.assertEqual(len(dossier["reconciled_uses"]), 2)
        self.assertTrue(any(i["code"] == "schema" for i in report["issues"]))

    def test_cli_round_trip_and_determinism(self):
        import subprocess
        import sys
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cfg = {"schema": "coverage-assembly-input/v1", "author_run": self.data["author_run"],
                   "profile": self.data["profile"], "scope": self.data["scope"]}
            for key in a.REF_INPUTS:
                raw = g.canonical(self.data[key])
                path = root / (key + ".json")
                path.write_bytes(raw)
                cfg[key] = {"file": path.name, "sha256": a.sha(raw)}
            initial_raw = g.canonical(self.data["initial"])
            (root / "initial.json").write_bytes(initial_raw)
            cfg["initial"] = {"file": "initial.json", "sha256": a.sha(initial_raw), "pin": self.data["initial_pin"]}
            cfg["blobs"] = []
            for n, ((side, path, digest), raw) in enumerate(sorted(self.blobs.items())):
                name = "blob-" + str(n)
                (root / name).write_bytes(raw)
                cfg["blobs"].append({"pin": {"side": side, "path": path, "sha256": digest}, "file": name})
            (root / "input.json").write_bytes(g.canonical(cfg))
            command = [sys.executable, "-B", str(a.HERE / "assemble_coverage.py"), "assemble",
                       "--input", str(root / "input.json"), "--out", str(root / "out")]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            first = {p.name: p.read_bytes() for p in (root / "out").iterdir()}
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            second = {p.name: p.read_bytes() for p in (root / "out").iterdir()}
            self.assertEqual(first, second)

    def test_open_finding_unchanged(self):
        self.data["findings"][0]["status"] = "open"
        before = copy.deepcopy(self.data["findings"])
        self.assertIn("open-finding", self.codes())
        self.assertEqual(before, self.data["findings"])

    def test_stale_excerpt(self):
        self.data["coverage_index"][0]["location"]["excerpt_sha256"] = "0" * 64
        self.assertIn("stale-excerpt", self.codes())

    def test_stale_inventory_sources(self):
        self.data["proof_inventory"]["sources"][0]["sha256"] = "0" * 64
        self.assertIn("proof-inventory-pin-mismatch", self.codes())

    def test_missing_edge_reason_not_invented(self):
        self.data["edge_reasons"] = {}
        dossier, report = self.run_assembly()
        self.assertIsNone(dossier["declared_edges"][0]["reason"])
        self.assertIn("missing-edge-explanation", {i["code"] for i in report["issues"]})

    def test_extra_edge_requires_its_own_reconciliation(self):
        next(x for x in self.data["applications"] if x["id"] == "P")["dependencies"] = ["A"]
        self.data["edge_reasons"]["P->A"] = "Synthetic non-use administrative dependency."
        dossier, report = self.run_assembly()
        self.assertTrue(any(row["id"] == "edge:P->A" and not row["history"] for row in dossier["reconciliation"]))
        self.assertIn("missing-current-reconciliation-explanation", {i["code"] for i in report["issues"]})

    def test_added_deleted_use_hashes(self):
        self.data["uses"][0]["id"] = "U2"
        self.data["coverage_index"][0]["use_ids"] = ["U2"]
        dossier, _ = self.run_assembly()
        rows = {r["id"]: r for r in dossier["reconciliation"]}
        self.assertIsNone(rows["use:U"]["after_sha256"])
        self.assertIsNone(rows["use:U2"]["before_sha256"])

    def test_duplicate_json_and_nonfinite_rejected(self):
        for raw in (b'{"x":1,"x":2}', b'{"x":NaN}'):
            with self.assertRaises(ValueError):
                a.strict_json(raw)

    def test_input_hash_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data.json").write_text("{}")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                a.read_reference({"file": "data.json", "sha256": "0" * 64}, root, [], "test")

    def test_validate_output_cannot_overwrite_any_input_or_mapped_blob(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("packet", "evidence", "profile", "blob"):
                (root / (name + ".json")).write_bytes(b"{}")
            rows = [{"pin": {"side": "head", "path": "test", "sha256": "0" * 64}, "file": "blob.json"}]
            (root / "map.json").write_bytes(g.canonical(rows))
            command = [sys.executable, "-B", str(a.HERE / "assemble_coverage.py"), "validate-records",
                       "--packet", str(root / "packet.json"), "--evidence", str(root / "evidence.json"),
                       "--profile", str(root / "profile.json"), "--blob-map", str(root / "map.json")]
            paths = list(root.iterdir())
            original = {p: p.read_bytes() for p in paths}
            for path in paths:
                with self.subTest(output=path.name):
                    result = subprocess.run(command + ["--out", str(path)], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("output would overwrite a pinned input", result.stderr)
                    self.assertEqual({p: p.read_bytes() for p in paths}, original)
            linked = root / "hardlink.json"
            os.link(root / "blob.json", linked)
            result = subprocess.run(command + ["--out", str(linked)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("output would overwrite a pinned input", result.stderr)
            self.assertEqual({p: p.read_bytes() for p in paths}, original)

    def test_output_symlink_alias_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input"
            source.write_bytes(b"synthetic input")
            alias = root / "output"
            try:
                alias.symlink_to(source)
            except OSError:
                self.skipTest("OS does not permit creating symlinks")
            with self.assertRaisesRegex(ValueError, "overwrite a pinned input"):
                a.protect_inputs([alias], [source])
            self.assertEqual(source.read_bytes(), b"synthetic input")


if __name__ == "__main__":
    unittest.main()
