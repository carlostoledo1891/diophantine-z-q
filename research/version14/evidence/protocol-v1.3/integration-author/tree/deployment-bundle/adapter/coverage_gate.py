"""Structural v1.3 coverage checks. Profiles are protected operator inputs.

No field proves source completeness, independent reasoning, or mathematics.
The signed coverage receipt attests those review judgments within its scope.
"""
import datetime
import offline_manifest_gate as g

PROTOCOL_SHA256 = 'd3eb878bb3fb12d3b27d157e33f417f6f81bf2a873370f2758e8ccb1e5314d0a'
PROTOCOL_PATH = 'docs/research-review/PROTOCOL.md'
COVERAGE_ID = 'protocol-v1.3-coverage'
LEGACY_PROTOCOL_HASHES = frozenset((
    'f2111f716457de7f45183fdeeb0a801d9c53e8378e20d7ae94bcb3f479e0b003',
    'b5365b3d9cd9a782bf7fd0b6020403d5d400eac13dc7e60875484a8769d3d925'))


def select_profile(packet, profile):
    # This guard also blocks accidental legacy dispatch during the upgrade.
    seen = any(row['sha256'] == PROTOCOL_SHA256 for s in (packet['base'], packet['head'])
               for row in s['files'].values())
    has_coverage = any(a.get('kind') == 'coverage' or a.get('id') == COVERAGE_ID
                       for a in packet['applications'])
    if profile is None:
        g.require(not seen and not has_coverage, 'coverage-profile-required')
        g.require(all(PROTOCOL_PATH not in s['files'] or s['files'][PROTOCOL_PATH]['sha256'] in LEGACY_PROTOCOL_HASHES
                      for s in (packet['base'], packet['head'])), 'unknown-governing-protocol-without-profile')
        return None
    g.fields(profile, 'schema protocol_version governing_protocol runtime_policy_sha256 mode claim_ids proof_paths allowed_nonmath_paths', 'coverage-profile')
    g.require(profile['schema'] == 'protocol-coverage-policy/v1' and profile['protocol_version'] == '1.3', 'unknown-coverage-profile')
    g.fields(profile['governing_protocol'], 'path sha256', 'governing-protocol')
    p = profile['governing_protocol']
    g.require(p['path'] == PROTOCOL_PATH and p['sha256'] == PROTOCOL_SHA256, 'unapproved-governing-protocol')
    g.require(packet['head']['files'].get(p['path'], {}).get('sha256') == PROTOCOL_SHA256,
              'changed-or-missing-governing-protocol')
    g.require(profile['runtime_policy_sha256'] == packet['policy_sha256'], 'coverage-runtime-policy-mismatch')
    g.require(profile['mode'] in ('substantive', 'non_substantive'), 'coverage-mode')
    claims = g.string_set(profile['claim_ids'], 'profile-claims')
    paths = g.string_set(profile['proof_paths'], 'profile-proof-paths', True)
    allowed = g.string_set(profile['allowed_nonmath_paths'], 'profile-nonmath-paths')
    g.require(all(g.path_ok(p) for p in paths | allowed) and not paths & allowed, 'profile-paths')
    g.require(bool(claims) if profile['mode'] == 'substantive' else not claims, 'profile-claim-scope')
    g.require(not allowed if profile['mode'] == 'substantive' else bool(allowed), 'profile-nonmath-scope')
    return profile


def timestamp(value):
    g.require(g.text(value), 'reconstruction-time')
    try:
        result = datetime.datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        raise g.Invalid('reconstruction-time') from None
    g.require(result.tzinfo is not None, 'reconstruction-time-zone')
    return result


def validate(packet, profile, apps, app_agents, runs, by_target, read_pin):
    """Called only after ordinary records, authenticated identities and receipts check.

    read_pin returns verified immutable bytes, never candidate filesystem paths.
    """
    if profile is None:
        return {'protocol_coverage': 'legacy-records-only'}
    g.require(set(a for a in apps if apps[a]['kind'] == 'coverage') == {COVERAGE_ID}, 'separate-coverage-application-required')
    app = apps[COVERAGE_ID]
    ordinary = set(apps) - {COVERAGE_ID}
    g.require(set(app['dependencies']) == ordinary, 'coverage-must-bind-all-applications')
    forbidden = set().union(*(app_agents[a] for a in ordinary))
    receipt = by_target['application', COVERAGE_ID]
    reviewer = runs[receipt['run_id']]['agent_id']
    g.require(reviewer not in forbidden, 'coverage-author-cannot-review')
    g.require(app['coverage_record']['side'] == 'head' and app['coverage_record'] in app['files'], 'unbound-coverage-record')
    dossier = g.parse_json_bytes(read_pin(app['coverage_record']), 'coverage-record')
    common = 'schema profile_sha256 mode sources scope'
    if profile['mode'] == 'substantive':
        common += ' coverage_index initial reconstruction reconciled_uses declared_edges_before declared_edges reconciliation'
    g.fields(dossier, common, 'coverage-record')
    g.require(dossier['schema'] == 'protocol-coverage/v1' and dossier['profile_sha256'] == g.digest(profile)
              and dossier['mode'] == profile['mode'], 'coverage-profile-binding')
    g.require(g.text(dossier['scope']), 'coverage-scope')
    sources = {}
    g.require(type(dossier['sources']) is list, 'coverage-sources')
    for p in dossier['sources']:
        g.require(p['side'] == 'head' and p['path'] not in sources, 'coverage-source-side-or-duplicate')
        sources[p['path']] = (p, read_pin(p))
    g.require(set(sources) == set(profile['proof_paths']), 'incomplete-proof-source-inventory')
    # Pin the human governing document as well as the runtime policy identity.
    read_pin(dict(side='head', **profile['governing_protocol']))
    if profile['mode'] == 'non_substantive':
        g.require(all(apps[a]['kind'] in ('policy', 'editorial') for a in ordinary), 'nonmath-substantive-application')
        g.require(set(c['path'] for c in packet['changes']) <= set(profile['allowed_nonmath_paths']), 'nonmath-change-outside-reviewed-scope')
        for path in sources:
            g.require(packet['base']['files'].get(path) == packet['head']['files'][path], 'nonmath-proof-source-changed')
            read_pin({'side':'base', 'path':path, 'sha256':sources[path][0]['sha256']})
        return {'protocol_coverage':'1.3-non-substantive-scope-only', 'coverage_profile_sha256':g.digest(profile)}

    claims = set(profile['claim_ids'])
    g.require(claims <= ordinary, 'missing-announced-claim-application')
    g.fields(dossier['reconstruction'], 'run_id method prior_exposure limitations frozen_at compared_at', 'reconstruction')
    reconstruction = dossier['reconstruction']
    # One supported route: the coverage reviewer attests their own reconstruction.
    # Timestamps record the assertion; they are not an independent clock attestation.
    g.require(reconstruction['run_id'] == receipt['run_id'], 'reconstruction-reviewer-mismatch')
    g.require(all(g.text(reconstruction[k]) for k in ('method','prior_exposure','limitations')), 'incomplete-reconstruction-attestation')
    g.require(timestamp(reconstruction['frozen_at']) < timestamp(reconstruction['compared_at']), 'reconstruction-not-frozen-before-comparison')
    initial = g.parse_json_bytes(read_pin(dossier['initial']), 'initial-reconstruction')
    g.fields(initial, 'schema sources uses', 'initial-reconstruction')
    g.require(initial['schema'] == 'protocol-source-first/v1' and initial['sources'] == dossier['sources'], 'stale-initial-proof-sources')
    before = g.unique(initial['uses'], 'id', 'initial-uses')
    for use in before.values():
        g.fields(use, 'id consumer passages assertion classification reason shared_contract_justification supplier application_id inline_argument', 'initial-source-use')
        g.require(g.text(use['consumer']) and g.text(use['reason']), 'incomplete-initial-use')
        g.string_set(use['passages'], 'initial-use-passages', True)
        g.fields(use['assertion'], 'statement objects hypotheses quantifiers parameter_range uniformity constants normalizations exceptional_cases limit_order', 'initial-required-assertion')
        g.require(all(g.text(v) for v in use['assertion'].values()), 'incomplete-initial-required-assertion')
    uses = g.unique(dossier['reconciled_uses'], 'id', 'reconciled-uses')
    index = g.unique(dossier['coverage_index'], 'id', 'coverage-index')
    covered = {p:set() for p in sources}
    index_claims = set()

    def location(loc, expected_path=None):
        g.fields(loc, 'pin start_line end_line excerpt_sha256', 'source-location')
        raw = read_pin(loc['pin'])
        g.require(loc['pin']['side'] == 'head', 'stale-source-location')
        if expected_path is not None:
            g.require(loc['pin'] == sources[expected_path][0], 'coverage-location-source')
        start, end = loc['start_line'], loc['end_line']
        lines = raw.splitlines(keepends=True)
        g.require(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), 'source-location-range')
        g.require(g.sha(b''.join(lines[start-1:end])) == loc['excerpt_sha256'], 'stale-source-excerpt')
        return start, end

    for pid, row in index.items():
        g.fields(row, 'id claim_ids location status reason use_ids no_imports_reason', 'coverage-passage')
        path = row['location']['pin']['path']
        g.require(path in sources, 'passage-outside-proof-sources')
        start, end = location(row['location'], path)
        covered[path].update(range(start, end+1))
        linked_claims = g.string_set(row['claim_ids'], 'passage-claims')
        linked_uses = g.string_set(row['use_ids'], 'passage-uses')
        g.require(linked_claims <= ordinary and linked_uses <= set(uses), 'missing-passage-claim-or-use')
        g.require(row['status'] in ('reviewed', 'outside_claimed_proof'), 'unreviewed-proof-passage')
        g.require(g.text(row['reason']), 'passage-specific-reason-required')
        if row['status'] == 'outside_claimed_proof':
            g.require(not linked_claims and not linked_uses, 'claimed-passage-marked-outside')
        else:
            g.require(linked_claims, 'reviewed-passage-without-claim')
            has_import = any(uses[u].get('classification') == 'dependency' for u in linked_uses)
            g.require(row['no_imports_reason'] is None if has_import else g.text(row['no_imports_reason']), 'missing-explicit-no-imports-statement')
            index_claims.update(linked_claims)
    g.require(claims <= index_claims, 'announced-claim-not-covered')
    for path, (_, raw) in sources.items():
        g.require(covered[path] == set(range(1, len(raw.splitlines())+1)) and covered[path], 'unindexed-proof-lines')

    for uid, use in uses.items():
        g.fields(use, 'id consumer passages assertion classification reason shared_contract_justification supplier application_id inline_argument', 'source-use')
        g.require(use['consumer'] in ordinary, 'unknown-consuming-claim')
        passages = g.string_set(use['passages'], 'use-passages', True)
        g.require(passages <= set(index), 'missing-use-passage')
        for pid in passages:
            g.require(uid in index[pid]['use_ids'] and use['consumer'] in index[pid]['claim_ids'], 'unlinked-source-use')
        g.require(all((pid in passages) == (uid in row['use_ids']) for pid,row in index.items()), 'incomplete-repeated-use-locations')
        g.require(g.text(use['reason']) and (len(passages) == 1 or g.text(use['shared_contract_justification'])), 'use-reason-or-shared-contract')
        g.fields(use['assertion'], 'statement objects hypotheses quantifiers parameter_range uniformity constants normalizations exceptional_cases limit_order', 'required-assertion')
        g.require(all(g.text(v) for v in use['assertion'].values()), 'incomplete-required-assertion')
        g.require(use['classification'] in ('dependency','notation','background','unused_reference'), 'use-classification')
        if use['classification'] != 'dependency':
            g.require(use['supplier'] is None and use['application_id'] is None and use['inline_argument'] is None, 'nondependency-contract')
            continue
        supplier = use['supplier']
        g.fields(supplier, 'kind application_id location statement publication', 'supplier')
        g.require(supplier['kind'] in ('internal','published_external','computation','inline'), 'unresolved-supplier')
        g.require(g.text(supplier['statement']), 'missing-supplier-statement')
        location(supplier['location'])
        sid = supplier['application_id']
        if supplier['kind'] == 'internal':
            g.require(sid in ordinary and sid in apps[use['consumer']]['dependencies'], 'missing-direct-internal-dependency')
            g.require(supplier['location']['pin'] in apps[sid]['files'], 'supplier-not-bound-to-application')
        else:
            g.require(sid is None, 'noninternal-supplier-application')
        if supplier['kind'] == 'published_external':
            g.fields(supplier['publication'], 'title authors venue authoritative_version locator corrections', 'publication')
            g.require(all(g.text(v) for v in supplier['publication'].values()), 'incomplete-published-source')
        else:
            g.require(supplier['publication'] is None, 'unexpected-publication')
        if use['application_id'] is not None:
            aid = use['application_id']
            g.require(aid in ordinary and use['inline_argument'] is None, 'invalid-application-match')
            g.require(supplier['location']['pin'] in apps[aid]['files'], 'application-does-not-bind-supplier')
            g.require(all(index[p]['location']['pin'] in apps[aid]['files'] for p in passages), 'application-does-not-bind-consumer')
        else:
            g.require(use['inline_argument'] is not None, 'unchecked-genuine-use')
            location(use['inline_argument'])

    def edges(rows, where):
        result = {}
        g.require(type(rows) is list, 'edge-list')
        for edge in rows:
            g.fields(edge, 'consumer supplier use_ids reason', where)
            key = edge['consumer'] + '->' + edge['supplier']
            g.require(edge['consumer'] in ordinary and edge['supplier'] in ordinary and key not in result, 'invalid-or-duplicate-edge')
            g.string_set(edge['use_ids'], 'edge-uses')
            g.require(g.text(edge['reason']), 'edge-reason')
            result[key] = edge
        return result
    old_edges = edges(dossier['declared_edges_before'], 'prior-edge')
    new_edges = edges(dossier['declared_edges'], 'current-edge')
    expected = {a+'->'+d for a in ordinary for d in apps[a]['dependencies']}
    g.require(set(new_edges) == expected, 'incomplete-declared-edge-inventory')
    extras = set()
    for key, edge in new_edges.items():
        expected_uses = {u for u,v in uses.items() if v['classification'] == 'dependency'
                         and v['supplier']['kind'] == 'internal' and v['consumer'] == edge['consumer']
                         and v['supplier']['application_id'] == edge['supplier']}
        g.require(set(edge['use_ids']) == expected_uses, 'edge-use-mismatch')
        if not expected_uses:
            extras.add('edge:'+key)
    diffs = {'use:'+k:(before.get(k),uses.get(k)) for k in set(before)|set(uses) if before.get(k) != uses.get(k)}
    diffs.update({'edge:'+k:(old_edges.get(k),new_edges.get(k)) for k in set(old_edges)|set(new_edges) if old_edges.get(k) != new_edges.get(k)})
    for key in extras:
        k = key[5:]
        diffs[key] = (old_edges.get(k),new_edges[k])
    reconciled = g.unique(dossier['reconciliation'], 'id', 'reconciliation')
    g.require(set(diffs) <= set(reconciled), 'unresolved-reconciliation-difference')
    findings = {f['id'] for f in packet['findings']}
    for key, row in reconciled.items():
        g.fields(row, 'id before_sha256 after_sha256 history', 'reconciliation-row')
        if key in diffs:
            old, new = diffs[key]
        elif key.startswith('use:') and key[4:] in before and key[4:] in uses:
            old,new = before[key[4:]],uses[key[4:]]
        elif key.startswith('edge:') and key[5:] in old_edges and key[5:] in new_edges:
            old,new = old_edges[key[5:]],new_edges[key[5:]]
        else:
            raise g.Invalid('unbound-reconciliation-row')
        g.require(row['before_sha256'] == (None if old is None else g.digest(old)) and
                  row['after_sha256'] == (None if new is None else g.digest(new)), 'stale-reconciliation')
        g.require(type(row['history']) is list and row['history'], 'missing-disposition-history')
        for item in row['history']:
            g.fields(item, 'status reason finding_ids', 'disposition')
            g.require(item['status'] in ('disputed','rejected','resolved') and g.text(item['reason']), 'invalid-disposition')
            ids = g.string_set(item['finding_ids'], 'disposition-findings')
            g.require(ids <= findings and (ids or item['status'] == 'resolved'), 'unrecorded-substantive-doubt')
        g.require(row['history'][-1]['status'] == 'resolved', 'unresolved-reconciliation')
    return {'protocol_coverage':'1.3-substantive-records-reviewed', 'coverage_profile_sha256':g.digest(profile),
            'coverage_passages':len(index), 'source_uses':len(uses),
            'coverage_limitation':'Source completeness, source-first chronology and mathematical correctness remain reviewer attestations.'}
