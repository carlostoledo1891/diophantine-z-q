"""Prepare unsigned v1.3 adoption packets from actual committed Git objects.

No checkout, signature, observation, reviewer decision or remote operation is made.
The operator supplies the reviewed documentation manifest and coverage profile.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
ADAPTER = HERE.parents[1] / 'protocol-ruleset-20261107/adapter'
sys.path.insert(0, str(ADAPTER))
import git_manifest as gm
import offline_manifest_gate as core
import ledger_evidence_bridge as bridge

PROTOCOL = 'docs/research-review/PROTOCOL.md'
HISTORY = 'docs/research-review/protocol-v1.2.md'
PROTOCOL_SHA256 = 'd3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a'
HISTORY_SHA256 = 'b5365b3d9cd9a782bf7fd0b6020403d5d400eac13dc7e60875484a8769d3d925'
DOCUMENT_PATHS = {PROTOCOL, HISTORY, 'README.md', 'docs/research-review/README.md',
                  'CONTRIBUTING.md', '.github/pull_request_template.md'}
POLICY_ID = 'protocol-v1.3-documentation'
COVERAGE_ID = 'protocol-v1.3-coverage'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def file_digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_labels(values, description):
    require(type(values) is list and values and
            all(type(v) is str and v.strip() for v in values) and len(set(values)) == len(values),
            description + ' requires unique actual run labels')
    return values


def pin(manifest, side, path):
    return {'side': side, 'path': path, 'sha256': manifest['files'][path]['sha256']}


def validate_profile(profile, policy_sha256, changed, base, head, dossier):
    core.fields(profile, 'schema protocol_version governing_protocol runtime_policy_sha256 mode claim_ids proof_paths allowed_nonmath_paths',
                'coverage profile')
    require(profile['schema'] == 'protocol-coverage-policy/v1' and
            profile['protocol_version'] == '1.3' and profile['mode'] == 'non_substantive',
            'this builder supports only v1.3 non-substantive adoption')
    require(profile['governing_protocol'] == {'path': PROTOCOL, 'sha256': PROTOCOL_SHA256} and
            profile['runtime_policy_sha256'] == policy_sha256, 'coverage policy binding differs')
    require(profile['claim_ids'] == [], 'non-substantive adoption cannot declare mathematical claims')
    proof_paths = profile['proof_paths']
    allowed = profile['allowed_nonmath_paths']
    require(type(proof_paths) is list and proof_paths and len(proof_paths) == len(set(proof_paths)) and
            all(gm.path_ok(p) for p in proof_paths), 'explicit reviewed proof-path inventory required')
    require(type(allowed) is list and len(allowed) == len(set(allowed)) and
            all(gm.path_ok(p) for p in allowed) and set(allowed) == set(changed),
            'profile must allow exactly the reviewed changed paths')
    require(not set(proof_paths) & set(allowed), 'proof paths overlap nonmathematical changes')
    core.fields(dossier, 'schema profile_sha256 mode sources scope', 'non-substantive coverage dossier')
    require(dossier['schema'] == 'protocol-coverage/v1' and dossier['mode'] == 'non_substantive' and
            dossier['profile_sha256'] == core.digest(profile), 'coverage dossier profile binding differs')
    require(type(dossier['scope']) is str and dossier['scope'].strip(), 'actual reviewed scope required')
    require(type(dossier['sources']) is list, 'coverage sources must be a list')
    sources = {}
    for source in dossier['sources']:
        core.fields(source, 'side path sha256', 'coverage source')
        path = source['path']
        require(path not in sources and path in proof_paths and source['side'] == 'head',
                'unexpected or duplicate coverage source')
        require(path in head['files'] and base['files'].get(path) == head['files'][path],
                'non-substantive proof artifact changed')
        require(source == pin(head, 'head', path), 'coverage proof source hash differs')
        sources[path] = source
    require(set(sources) == set(proof_paths), 'coverage dossier omits a protected proof artifact')


def prepare(repository, context, policy_sha256, document_manifest, reports,
            dossier_path, dossier_source, profile, text_author_run, integrator_run,
            coverage_author_runs, findings, finding_bodies):
    core.fields(context, 'repository repository_id pr base head', 'actual PR context')
    require(type(context['repository']) is str and context['repository'].strip(), 'repository name required')
    require(type(context['repository_id']) is int and context['repository_id'] > 0 and
            type(context['pr']) is int and context['pr'] > 0, 'numeric repository and PR required')
    require(core.hexhash(policy_sha256), 'protected runtime policy digest required')
    run_labels([text_author_run, integrator_run], 'text and integration authors')
    run_labels(coverage_author_runs, 'coverage dossier authors')
    require(type(document_manifest) is dict and type(document_manifest.get('files')) is list,
            'reviewed documentation manifest required')
    documents = {}
    for row in document_manifest['files']:
        core.fields(row, 'path base_sha256 candidate_sha256 bytes', 'reviewed document')
        path = row['path']
        require(gm.path_ok(path) and path not in documents, 'unsafe or duplicate document path')
        require(core.hexhash(row['candidate_sha256']) and
                (row['base_sha256'] is None or core.hexhash(row['base_sha256'])) and
                type(row['bytes']) is int and row['bytes'] > 0, 'invalid document pin')
        documents[path] = row
    require(set(documents) == DOCUMENT_PATHS, 'exact six reviewed documentation paths required')
    require(documents[PROTOCOL]['candidate_sha256'] == PROTOCOL_SHA256 and
            documents[HISTORY]['candidate_sha256'] == HISTORY_SHA256,
            'supplied v1.3 or historical v1.2 bytes differ')
    require(type(reports) is list and reports, 'actual review report files required')
    additions = {}
    report_authors = []
    for report in reports:
        core.fields(report, 'path source author_run', 'actual report')
        path = report['path']
        require(gm.path_ok(path) and path.startswith('docs/research-review/') and
                path not in DOCUMENT_PATHS and path not in additions, 'unsafe or duplicate report path')
        run_labels([report['author_run']], 'report author')
        additions[path] = file_digest(Path(report['source']))
        report_authors.append(report['author_run'])
    require(gm.path_ok(dossier_path) and dossier_path.startswith('docs/research-review/') and
            dossier_path not in DOCUMENT_PATHS and dossier_path not in additions, 'coverage dossier path overlaps')
    dossier_raw = dossier_source.read_bytes()
    dossier = json.loads(dossier_raw)
    additions[dossier_path] = hashlib.sha256(dossier_raw).hexdigest()
    base = gm.collect(str(repository.resolve()), context['base'])
    head = gm.collect(str(repository.resolve()), context['head'])
    require(base['git_hash'] == head['git_hash'], 'Git object format changed')
    changed = sorted(path for path in set(base['files']) | set(head['files'])
                     if base['files'].get(path) != head['files'].get(path))
    require(set(changed) == DOCUMENT_PATHS | set(additions), 'unlisted or missing changed path')
    for path, row in documents.items():
        before = base['files'].get(path)
        require(head['files'][path]['mode'] == '100644' and
                (before is None or before['mode'] == '100644'), 'document file mode differs')
        require((before['sha256'] if before else None) == row['base_sha256'], 'reviewed document base changed')
        require(head['files'][path]['sha256'] == row['candidate_sha256'] and
                head['files'][path]['size'] == row['bytes'], 'reviewed document head changed')
    require(base['files'][PROTOCOL]['sha256'] == head['files'][HISTORY]['sha256'], 'v1.2 history not preserved')
    for path, digest in additions.items():
        require(path not in base['files'], 'new report/dossier must not replace prior evidence')
        require(head['files'][path]['mode'] == '100644', 'evidence file mode differs')
        require(head['files'][path]['sha256'] == digest, 'committed report/dossier differs from supplied bytes')
    validate_profile(profile, policy_sha256, changed, base, head, dossier)
    changed_pins = [pin(manifest, side, path) for side, manifest in [('base', base), ('head', head)]
                    for path in changed if path in manifest['files']]
    # The policy application includes the dossier as an authored policy artifact.
    # Conservative author attribution includes its authors as well as the integrator.
    ordinary_authors = sorted(set([text_author_run, integrator_run] + coverage_author_runs))
    evidence = [p for p in changed_pins if p['side'] == 'head']
    explanations = {
        'source_hypotheses': ('Use the supplied v1.3 protocol verbatim and retain v1.2 history.',
                              'The exact supplied source and reviewed six-file adaptation are pinned.'),
        'constructed_objects': ('Install only reviewed policy documents, actual reports and the supplied dossier.',
                                'Complete Git manifests show exactly the declared additions and document changes.'),
        'index_domain_coverage': ('Give the adoption its explicit non-substantive coverage scope.',
                                  'The separately bound dossier names every protected proof artifact in the reviewed profile.'),
        'transition_maps': ('Connect contributor entry points to the current and historical policy.',
                            'The reviewed documentation bytes preserve those links and explanations.'),
        'consumed_object_identity': ('Bind actual committed report and dossier bytes to the final targets.',
                                     'Both before/after document pins and all newly supplied evidence hashes are checked.'),
        'coefficient_conventions': ('Preserve the existing mathematical artifacts and their conventions.',
                                    'All files outside the documentation/evidence allowlist have identical Git entries.'),
        'local_conditions': ('Retain the protected runtime-policy identity and state actual implementation scope.',
                             'The external reviewed profile binds that runtime policy and the supplied human protocol.'),
        'exceptional_cases': ('Justify why this policy-only adoption makes no full mathematical closure claim.',
                              'The supplied non-substantive dossier gives its actual scope and unchanged proof-source pins.'),
        'downstream_consumption': ('Make v1.3 coverage requirements usable without recertifying historical work.',
                                   'The reviewed guide and template require separate source-first coverage and reconciliation.'),
    }
    policy_app = {'id': POLICY_ID, 'kind': 'policy', 'authors': ordinary_authors, 'dependencies': [],
                  'files': changed_pins, 'obligations': {
                      name: {'status': 'checked', 'required': terms[0], 'constructed': terms[1],
                             'justification': 'This is an authored preparation claim requiring final non-author review.',
                             'evidence': evidence} for name, terms in explanations.items()}}
    coverage_pins = [pin(head, 'head', dossier_path), pin(head, 'head', PROTOCOL)]
    coverage_pins += [pin(head, 'head', path) for path in profile['proof_paths']]
    coverage_app = {'id': COVERAGE_ID, 'kind': 'coverage',
                    'authors': sorted(set(coverage_author_runs + [integrator_run])),
                    'dependencies': [policy_app['id']], 'files': coverage_pins,
                    'coverage_record': pin(head, 'head', dossier_path)}
    require(type(findings) is list and type(finding_bodies) is dict, 'explicit findings and bodies required')
    seen = set()
    for finding in findings:
        core.fields(finding, 'id body_sha256 status reason authors applications duplicate_of', 'finding')
        fid = finding['id']
        require(type(fid) is str and fid and fid not in seen and fid in finding_bodies, 'missing or duplicate finding')
        seen.add(fid)
        require(type(finding_bodies[fid]) is str and
                finding['body_sha256'] == hashlib.sha256(finding_bodies[fid].encode()).hexdigest(),
                'original finding body changed')
        run_labels(finding['authors'], 'finding authors')
        require(type(finding['applications']) is list and finding['applications'] and
                set(finding['applications']) <= {POLICY_ID, COVERAGE_ID}, 'unknown finding application')
        require(type(finding['status']) is str and finding['status'] and
                type(finding['reason']) is str and finding['reason'].strip(), 'finding disposition required')
    require(set(finding_bodies) == seen, 'unregistered supplied finding body')
    require(all(f['duplicate_of'] is None or f['duplicate_of'] in seen for f in findings), 'unknown duplicate target')
    packet = {'schema': 2, 'repository_id': context['repository_id'], 'pull_request': context['pr'],
              'git_hash': head['git_hash'], 'policy_sha256': policy_sha256, 'base': base, 'head': head,
              'changes': [{'path': path, 'kind': 'policy', 'applications': [POLICY_ID]} for path in changed],
              'applications': [policy_app, coverage_app], 'findings': copy.deepcopy(findings)}
    binding = core.binding(packet, core.snapshot(base, packet['git_hash'])[0], core.snapshot(head, packet['git_hash'])[0])
    assembly_authors = sorted(set(ordinary_authors + report_authors +
                                  [r for f in findings for r in f['authors']]))
    authors = {POLICY_ID: ordinary_authors, COVERAGE_ID: coverage_app['authors']}
    targets = []
    for key, (kind, target, digest, dependencies) in bridge.targets(packet).items():
        target_authors = assembly_authors
        if kind == 'application':
            target_authors = authors[target]
        elif kind == 'finding':
            target_authors = next(f['authors'] for f in findings if f['id'] == target)
        targets.append({'selection_key': key, 'target_kind': kind, 'target_id': target,
                        'target_sha256': digest, 'dependency_sha256': dependencies, 'binding': binding,
                        'declared_author_runs': target_authors,
                        'status': 'awaiting independent final-target review and authenticated observation'})
    metadata = {'schema': 'unsigned-v13-adoption/v1', 'repository': context['repository'],
                'packet_sha256': core.digest(packet), 'binding': binding, 'changed_paths': changed,
                'coverage_profile_sha256': core.digest(profile), 'coverage_mode': 'non_substantive',
                'reported_run_labels_authenticated_here': False, 'intake_complete': False,
                'receipts_created': False, 'observations_created': False, 'merge_authorized': False,
                'added_evidence_sha256': additions, 'findings_supplied_by_operator': True}
    return {'packet.json': packet, 'coverage-profile.json': copy.deepcopy(profile),
            'base-manifest.json': base, 'head-manifest.json': head,
            'targets.json': targets, 'PREPARATION.json': metadata}


def write_outputs(output, objects):
    require(output.resolve().is_relative_to(HERE.resolve()), 'outputs must remain inside packet-author')
    encoded = {name: core.canonical(value) + b'\n' for name, value in objects.items()}
    for name, raw in encoded.items():
        require(not (output / name).exists() or (output / name).read_bytes() == raw,
                'refusing to replace a different frozen output')
    output.mkdir(parents=True, exist_ok=True)
    for name, raw in encoded.items():
        (output / name).write_bytes(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repository', 'context', 'reports', 'dossier-source', 'coverage-profile',
                 'coverage-author-runs', 'findings', 'finding-bodies', 'output'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--document-manifest', type=Path, default=HERE.parent / 'docs-author/r2/MANIFEST.json')
    for name in ('policy-sha256', 'dossier-path', 'text-author-run', 'integrator-run'):
        parser.add_argument('--' + name, required=True)
    args = parser.parse_args()
    objects = prepare(args.repository, load(args.context), args.policy_sha256,
                      load(args.document_manifest), load(args.reports), args.dossier_path,
                      args.dossier_source, load(args.coverage_profile), args.text_author_run,
                      args.integrator_run, load(args.coverage_author_runs), load(args.findings),
                      load(args.finding_bodies))
    write_outputs(args.output, objects)
    print(json.dumps({'packet_sha256': core.digest(objects['packet.json']),
                      'signed': False, 'observations_created': False}, indent=2))


if __name__ == '__main__':
    main()
