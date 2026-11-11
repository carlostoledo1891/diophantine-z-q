"""Prepare unsigned schema-2 research packets from exact Git objects.

No candidate code, credentials, network, author observations or reviewer receipts
are executed or created. Full authenticated coverage acceptance stays in the gate.
"""
from pathlib import Path
import argparse
import contextlib
import copy
import hashlib
import io
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ADAPTER = HERE.parent / 'integration-author/tree/adapter'
PINS = {
    'coverage_gate.py': '510ce66ee8d89e3fcb1358304c8ef2bbe3cfbeecf05f902cf4fb040b9a232e55',
    'offline_manifest_gate.py': '978d954e18b3cbde2ed3440581259aa025def63e2835c12cd6210396b71375da',
    'ledger_evidence_bridge.py': '73c81da423a173dcbdf0249a6026fbfcf55f20c78de7b6f91b6bf33bd0380e75',
    'git_manifest.py': '8ca4d7b1ffb49d1a329f5ab8f423b1e415b3c5616f8e6d03a052348f75f9fcef',
    'operator_ledger.py': '5e2cec65c3b516f62ec4bbd9ae071c431c11ab7456edd4d7000c986782c072d7',
}
for name, expected in PINS.items():
    if hashlib.sha256((ADAPTER / name).read_bytes()).hexdigest() != expected:
        raise ValueError('reviewed preparation dependency changed: ' + name)
sys.path.insert(0, str(ADAPTER))
import offline_manifest_gate as core
import coverage_gate as coverage
import git_manifest as gm
import ledger_evidence_bridge as bridge

need = core.require

def read_json(path):
    return core.parse_json_bytes(Path(path).read_bytes())

def authors(values, name):
    return core.string_set(values, name, True)

def prepare(repository, context, contract, reports, findings, finding_bodies, profile):
    """Return unaccepted data and exact target requests, never review decisions."""
    core.fields(context, 'repository repository_id pr base head', 'actual-context')
    need(type(context['repository']) is str and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', context['repository']), 'repository-name')
    need(type(context['repository_id']) is int and context['repository_id'] > 0 and
         type(context['pr']) is int and context['pr'] > 0, 'numeric-real-context')
    core.fields(contract, 'schema policy_sha256 policy_paths changes applications coverage_record coverage_author_runs assembly_author_runs', 'release-contract')
    need(contract['schema'] == 'unsigned-research-release/v1' and core.hexhash(contract['policy_sha256']), 'release-contract-version')
    policy_paths = core.string_set(contract['policy_paths'], 'policy-paths', True)
    need(all(gm.path_ok(p[:-1] if p.endswith('/') else p) for p in policy_paths), 'policy-path')
    base = gm.collect(str(Path(repository).resolve()), context['base'])
    head = gm.collect(str(Path(repository).resolve()), context['head'])
    need(base['git_hash'] == head['git_hash'], 'object-format-changed')
    packet = {'schema': 2, 'repository_id': context['repository_id'], 'pull_request': context['pr'],
        'git_hash': head['git_hash'], 'policy_sha256': contract['policy_sha256'], 'base': base, 'head': head,
        'changes': [], 'applications': copy.deepcopy(contract['applications']), 'findings': copy.deepcopy(findings)}
    apps = core.unique(packet['applications'], 'id', 'applications')
    need(apps and coverage.COVERAGE_ID not in apps and all(a.get('kind') in core.KINDS for a in apps.values()), 'ordinary-applications-required')
    reader = core.GitBlobReader({'base': repository, 'head': repository})
    cache = {}
    def pin(value, read=False):
        core.fields(value, 'side path sha256', 'pin')
        side, path = value['side'], value['path']
        need(side in ('base', 'head') and gm.path_ok(path) and core.hexhash(value['sha256']), 'invalid-pin')
        entry = packet[side]['files'].get(path)
        need(entry is not None and entry['sha256'] == value['sha256'], 'stale-file-pin')
        if read:
            need(entry['size'] <= 16 * 1024 * 1024, 'coverage-blob-too-large')
            key = (side, path)
            if key not in cache:
                with contextlib.closing(reader.open(side, path, entry)) as stream:
                    raw = stream.read(16 * 1024 * 1024 + 1)
                gm.verify_blob(io.BytesIO(raw), entry, packet['git_hash'])
                cache[key] = raw
            return cache[key]
        return side, path
    app_pins = {}
    all_authors = set()
    for aid, app in apps.items():
        core.fields(app, 'id kind authors dependencies files obligations', 'application')
        all_authors |= authors(app['authors'], 'application-authors')
        need(core.string_set(app['dependencies'], 'application-dependencies') <= set(apps), 'missing-ordinary-dependency')
        need(type(app['files']) is list and app['files'], 'application-files')
        pairs = [pin(p) for p in app['files']]
        need(len(set(pairs)) == len(pairs), 'duplicate-file-pin')
        app_pins[aid] = set(pairs)
        need(type(app['obligations']) is dict and set(app['obligations']) == core.OBLIGATIONS, 'missing-obligation')
        for obligation in app['obligations'].values():
            core.fields(obligation, 'status required constructed justification evidence', 'obligation')
            # Preserve unresolved author claims as unresolved; never turn them green.
            need(core.text(obligation['status']) and all(core.text(obligation[k]) for k in ('required', 'constructed', 'justification')), 'incomplete-obligation')
            need(type(obligation['evidence']) is list and obligation['evidence'] and
                 all(pin(p) in app_pins[aid] for p in obligation['evidence']), 'unbound-obligation-evidence')
    # Hashing the ordinary graph already detects cycles without any receipt data.
    bridge.targets(dict(packet, findings=[]))
    changed = {p for p in set(base['files']) | set(head['files']) if base['files'].get(p) != head['files'].get(p)}
    changes = core.unique(contract['changes'], 'path', 'reviewed-changes')
    need(set(changes) == changed, 'unlisted-or-missing-change')
    for path, row in changes.items():
        core.fields(row, 'path kind applications base head', 'reviewed-change')
        need(core.canonical(row['base']) == core.canonical(base['files'].get(path)) and
             core.canonical(row['head']) == core.canonical(head['files'].get(path)), 'reviewed-file-entry-changed')
        ids = core.string_set(row['applications'], 'change-applications', True)
        need(ids <= set(apps) and row['kind'] in core.KINDS, 'change-application-or-kind')
        required = {(s, path) for s in ('base', 'head') if path in packet[s]['files']}
        need(all(apps[a]['kind'] == row['kind'] and required <= app_pins[a] for a in ids), 'unbound-change')
        is_policy = any(path == p or (p.endswith('/') and path.startswith(p)) for p in policy_paths)
        need(not is_policy or row['kind'] == 'policy', 'policy-misclassification')
        packet['changes'].append({k: copy.deepcopy(row[k]) for k in ('path', 'kind', 'applications')})
    coverage_authors = authors(contract['coverage_author_runs'], 'coverage-authors')
    all_authors |= coverage_authors
    record = contract['coverage_record']
    need(record['side'] == 'head', 'coverage-record-must-be-head')
    dossier = core.parse_json_bytes(pin(record, True), 'coverage-dossier')
    core.fields(dossier, 'schema profile_sha256 mode sources scope coverage_index initial reconstruction reconciled_uses declared_edges_before declared_edges reconciliation', 'substantive-dossier')
    need(dossier['schema'] == 'protocol-coverage/v1' and dossier['mode'] == 'substantive' and core.text(dossier['scope']), 'substantive-dossier-required')
    coverage.select_profile(packet, profile)
    need(profile['mode'] == 'substantive' and dossier['profile_sha256'] == core.digest(profile), 'substantive-profile-binding')
    need(set(profile['claim_ids']) <= set(apps), 'unknown-announced-claim')
    sources = core.unique(dossier['sources'], 'path', 'coverage-sources')
    need(set(sources) == set(profile['proof_paths']) and all(p['side'] == 'head' for p in sources.values()), 'incomplete-proof-sources')
    for p in sources.values():
        pin(p, True)
    initial = core.parse_json_bytes(pin(dossier['initial'], True), 'initial-reconstruction')
    core.fields(initial, 'schema sources uses', 'initial-reconstruction')
    need(initial['schema'] == 'protocol-source-first/v1' and initial['sources'] == dossier['sources'], 'stale-initial-reconstruction')
    core.unique(initial['uses'], 'id', 'initial-uses')
    core.fields(dossier['reconstruction'], 'run_id method prior_exposure limitations frozen_at compared_at', 'reconstruction-attestation')
    reconstruction = dossier['reconstruction']
    need(all(core.text(reconstruction[k]) for k in ('run_id', 'method', 'prior_exposure', 'limitations')), 'missing-reconstruction-attestation')
    need(coverage.timestamp(reconstruction['frozen_at']) < coverage.timestamp(reconstruction['compared_at']), 'reconstruction-chronology')
    need(reconstruction['run_id'] not in all_authors, 'declared-coverage-reviewer-is-author')
    # Check all nested location/pin bindings without inventing the receipt needed
    # to call the authenticated gate's full coverage validation entry point.
    def walk(value):
        if isinstance(value, dict):
            if set(value) == {'side', 'path', 'sha256'}:
                pin(value)
            elif set(value) == {'pin', 'start_line', 'end_line', 'excerpt_sha256'}:
                raw = pin(value['pin'], True)
                start, end = value['start_line'], value['end_line']
                lines = raw.splitlines(keepends=True)
                need(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), 'location-range')
                need(core.sha(b''.join(lines[start-1:end])) == value['excerpt_sha256'], 'stale-location-excerpt')
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(dossier)
    index = core.unique(dossier['coverage_index'], 'id', 'coverage-index')
    uses = core.unique(dossier['reconciled_uses'], 'id', 'reconciled-uses')
    reconciliation = core.unique(dossier['reconciliation'], 'id', 'reconciliation')
    covered = {path: set() for path in sources}
    indexed_claims = set()
    for passage in index.values():
        core.fields(passage, 'id claim_ids location status reason use_ids no_imports_reason', 'coverage-passage')
        location = passage['location']
        path = location['pin']['path']
        need(path in sources and location['pin'] == sources[path], 'unbound-coverage-source')
        covered[path].update(range(location['start_line'], location['end_line'] + 1))
        claims = core.string_set(passage['claim_ids'], 'passage-claims')
        need(claims <= set(apps) and core.string_set(passage['use_ids'], 'passage-uses') <= set(uses), 'unknown-passage-claim-or-use')
        need(passage['status'] in ('reviewed', 'outside_claimed_proof') and core.text(passage['reason']), 'incomplete-coverage-passage')
        if passage['status'] == 'reviewed':
            need(claims, 'reviewed-passage-without-claim')
            indexed_claims |= claims
        else:
            need(not claims and not passage['use_ids'], 'outside-passage-claims-use')
    need(set(profile['claim_ids']) <= indexed_claims, 'announced-claim-not-indexed')
    for path, source in sources.items():
        lines = pin(source, True).splitlines()
        need(covered[path] == set(range(1, len(lines) + 1)) and covered[path], 'unindexed-proof-lines')
    for key in ('declared_edges_before', 'declared_edges'):
        need(type(dossier[key]) is list, 'edge-list')
    expected_edges = {(a, d) for a, app in apps.items() for d in app['dependencies']}
    actual_edges = [(e['consumer'], e['supplier']) for e in dossier['declared_edges']]
    need(len(actual_edges) == len(set(actual_edges)) and set(actual_edges) == expected_edges, 'edge-inventory-mismatch')
    initial_uses = core.unique(initial['uses'], 'id', 'initial-uses')
    changed_rows = {'use:' + k: (initial_uses.get(k), uses.get(k)) for k in set(initial_uses) | set(uses)
                    if initial_uses.get(k) != uses.get(k)}
    old_edges = {e['consumer'] + '->' + e['supplier']: e for e in dossier['declared_edges_before']}
    new_edges = {e['consumer'] + '->' + e['supplier']: e for e in dossier['declared_edges']}
    need(len(old_edges) == len(dossier['declared_edges_before']), 'duplicate-prior-edge')
    changed_rows.update({'edge:' + k: (old_edges.get(k), new_edges.get(k)) for k in set(old_edges) | set(new_edges)
                         if old_edges.get(k) != new_edges.get(k)})
    need(set(changed_rows) <= set(reconciliation), 'missing-reconciliation-row')
    for key, (old, new) in changed_rows.items():
        row = reconciliation[key]
        core.fields(row, 'id before_sha256 after_sha256 history', 'reconciliation-row')
        need(row['before_sha256'] == (None if old is None else core.digest(old)) and
             row['after_sha256'] == (None if new is None else core.digest(new)), 'stale-reconciliation')
        need(type(row['history']) is list and row['history'], 'missing-reconciliation-history')
    coverage_pins = [copy.deepcopy(record), {'side': 'head', **profile['governing_protocol']}, copy.deepcopy(dossier['initial'])]
    coverage_pins += copy.deepcopy(dossier['sources'])
    dedup = {}
    for p in coverage_pins:
        dedup[pin(p)] = p
    packet['applications'].append({'id': coverage.COVERAGE_ID, 'kind': 'coverage',
        'authors': sorted(coverage_authors), 'dependencies': sorted(apps),
        'files': list(dedup.values()), 'coverage_record': copy.deepcopy(record)})
    evidence = core.unique(reports, 'path', 'actual-reports')
    need(evidence, 'actual-report-manifest-required')
    for path, report in evidence.items():
        core.fields(report, 'path sha256 bytes author_runs scope', 'actual-report')
        all_authors |= authors(report['author_runs'], 'report-authors')
        need(core.text(report['scope']) and type(report['bytes']) is int, 'report-scope')
        raw = pin({'side': 'head', 'path': path, 'sha256': report['sha256']}, True)
        need(len(raw) == report['bytes'] and head['files'][path]['mode'] == '100644', 'report-bytes-or-mode')
        need(path not in base['files'] or base['files'][path] == head['files'][path], 'historical-report-replaced')
    fs = core.unique(findings, 'id', 'findings')
    need(type(finding_bodies) is dict and set(finding_bodies) == set(fs), 'finding-body-inventory')
    for fid, finding in fs.items():
        core.fields(finding, 'id body_sha256 status reason authors applications duplicate_of', 'finding')
        need(type(finding_bodies[fid]) is str and core.sha(finding_bodies[fid].encode()) == finding['body_sha256'], 'changed-finding-body')
        all_authors |= authors(finding['authors'], 'finding-authors')
        need(core.text(finding['status']) and core.text(finding['reason']), 'finding-disposition')
        need(core.string_set(finding['applications'], 'finding-applications') <= set(apps) | {coverage.COVERAGE_ID}, 'unknown-finding-application')
        need(finding['duplicate_of'] is None or finding['duplicate_of'] in fs, 'unknown-duplicate-finding')
    declared_assembly = authors(contract['assembly_author_runs'], 'assembly-authors')
    need(all_authors <= declared_assembly, 'incomplete-assembly-authors')
    target_map = bridge.targets(packet)  # Existing exact recursive digest and cycle checks.
    bm = core.snapshot(base, packet['git_hash'])[0]
    hm = core.snapshot(head, packet['git_hash'])[0]
    binding = core.binding(packet, bm, hm)
    targets = []
    by_id = {a['id']: a for a in packet['applications']}
    for key, (kind, target, digest, dependency) in target_map.items():
        declared = by_id[target]['authors'] if kind == 'application' else fs[target]['authors'] if kind == 'finding' else sorted(declared_assembly)
        targets.append({'selection_key': key, 'target_kind': kind, 'target_id': target,
            'target_sha256': digest, 'dependency_sha256': dependency, 'binding': binding,
            'declared_author_runs': declared, 'status': 'awaiting actual independent final-target review'})
    metadata = {'schema': 'unsigned-substantive-packet/v1', 'repository': context['repository'],
        'packet_sha256': core.digest(packet), 'binding': binding, 'coverage_profile_sha256': core.digest(profile),
        'claim_ids': profile['claim_ids'], 'contract_sha256': core.digest(contract), 'report_manifest_sha256': core.digest(reports),
        'checks': ['complete Git manifests', 'exact declared changes and file entries', 'authored obligations and pins',
                   'actual report bytes and original findings', 'profile and initial source binding', 'nested locations', 'dependency target digests'],
        'full_coverage_validation': 'deferred to the existing gate with actual authenticated receipts',
        'source_first_process_authenticated': False, 'authorship_authenticated': False,
        'live_origin_authenticated': False, 'receipts_created': False, 'merge_authorized': False,
        'historical_acceptance': 'No prior receipt is copied or relabeled; a real reviewer may explicitly adopt prior content for the exact new target.'}
    return {'packet.json': packet, 'coverage-profile.json': copy.deepcopy(profile), 'targets.json': targets,
        'report-manifest.json': copy.deepcopy(reports), 'finding-bodies.json': copy.deepcopy(finding_bodies),
        'base-manifest.json': base, 'head-manifest.json': head, 'PREPARATION.json': metadata}

def write_outputs(output, objects):
    output = Path(output).resolve()
    need(output.is_relative_to(HERE) and output != HERE, 'output-must-be-isolated')
    raws = {name: core.canonical(obj) + b'\n' for name, obj in objects.items()}
    for name, raw in raws.items():
        need(not (output / name).exists() or (output / name).read_bytes() == raw, 'frozen-output-differs')
    output.mkdir(parents=True, exist_ok=True)
    for name, raw in raws.items():
        (output / name).write_bytes(raw)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repository', 'context', 'contract', 'reports', 'findings', 'finding-bodies', 'profile', 'output'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    objects = prepare(args.repository, read_json(args.context), read_json(args.contract),
        read_json(args.reports), read_json(args.findings), read_json(args.finding_bodies), read_json(args.profile))
    write_outputs(args.output, objects)
    print(json.dumps({'packet_sha256': objects['PREPARATION.json']['packet_sha256'], 'signed': False}))

if __name__ == '__main__':
    main()
