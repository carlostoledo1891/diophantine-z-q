"""v1.4 recorded relationships only; never a mathematical implication checker.

Called after all v1.3 checks. Receipt authenticity is supplied by the existing
trusted adapter, not by this module or its synthetic test fixtures.
"""
import offline_manifest_gate as g

ASSERTION = 'statement objects hypotheses quantifiers parameter_range uniformity constants normalizations exceptional_cases limit_order'
COVERAGE_ID = 'protocol-v1.3-coverage'  # stable historical application identifier
LIMITATION = ('Checks exact declared relationships, evidence bytes and reviewer bindings only. '
              'Does not establish mathematical truth, inventory/search completeness, honest review '
              'or independence of thought. No release or publication authorization.')


def validate(packet, profile, dossier, apps, by_target, read_pin):
    pin = dossier['protocol14_record']
    g.fields(pin, 'side path sha256', 'connection-record-pin')
    g.require(pin['side'] == 'head' and pin['path'] == profile['connection_record_path']
              and pin in apps[COVERAGE_ID]['files'], 'unbound-connection-record')
    record = g.parse_json_bytes(read_pin(pin), 'connections-record')
    g.fields(record, 'schema profile_sha256 coverage_sources connections findings scope limitations', 'connections-record')
    g.require(record['schema'] == 'protocol-connections/v1' and record['profile_sha256'] == g.digest(profile)
              and record['coverage_sources'] == dossier['sources'], 'stale-connections-record')
    g.require(g.text(record['scope']) and g.text(record['limitations']), 'connections-scope-or-limitations')
    all_pins = [p for a in apps.values() for p in a['files']]

    def location(loc):
        g.fields(loc, 'pin start_line end_line excerpt_sha256', 'connection-location')
        g.require(loc['pin'] in all_pins and loc['pin']['side'] == 'head', 'unbound-connection-location')
        raw = read_pin(loc['pin'])
        lines = raw.splitlines(keepends=True)
        a, b = loc['start_line'], loc['end_line']
        g.require(type(a) is int and type(b) is int and 1 <= a <= b <= len(lines), 'connection-location-range')
        g.require(g.sha(b''.join(lines[a-1:b])) == loc['excerpt_sha256'], 'stale-connection-excerpt')

    def locations(rows, nonempty=True):
        g.require(type(rows) is list and (rows or not nonempty), 'connection-locations')
        g.require(len({g.digest(r) for r in rows}) == len(rows), 'duplicate-connection-location')
        for loc in rows:
            location(loc)

    def assertion(value):
        g.fields(value, ASSERTION, 'connection-assertion')
        g.require(all(g.text(v) for v in value.values()), 'incomplete-connection-assertion')

    uses = {u['id']: u for u in dossier.get('reconciled_uses', []) if u['classification'] == 'dependency'}
    index = {p['id']: p for p in dossier.get('coverage_index', [])}
    connections = g.unique(record['connections'], 'use_id', 'connections')
    g.require(set(connections) == set(uses), 'missing-or-extra-required-connection')
    subjects = {}
    for uid, conn in connections.items():
        g.fields(conn, 'use_id use_sha256 supplier_passage_role available_assertion needed_assertion required_capabilities available_capabilities derived_capabilities connecting_derivation adverse_cases consumer_locations', 'connection')
        use = uses[uid]
        g.require(conn['use_sha256'] == g.digest(use), 'stale-connection-use')
        g.require(conn['supplier_passage_role'] in ('statement','proof','construction','application','inline_derivation','computation_certificate'), 'supplier-passage-is-not-evidence')
        assertion(conn['available_assertion'])
        assertion(conn['needed_assertion'])
        g.require(conn['available_assertion']['statement'] == use['supplier']['statement'], 'available-supplier-contract-mismatch')
        g.require(conn['needed_assertion'] == use['assertion'], 'needed-consumer-contract-mismatch')
        expected_locs = [index[p]['location'] for p in use['passages']]
        g.require(conn['consumer_locations'] == expected_locs, 'incomplete-connection-consumers')
        locations(conn['consumer_locations'])
        required = g.string_set(conn['required_capabilities'], 'required-capabilities', True)
        available = g.string_set(conn['available_capabilities'], 'available-capabilities')
        derived = g.string_set(conn['derived_capabilities'], 'derived-capabilities')
        g.require(required <= available | derived, 'weaker-recorded-supplier-without-derivation')
        deriv = conn['connecting_derivation']
        g.fields(deriv, 'kind location application_id output_assertion', 'connecting-derivation')
        g.require(deriv['kind'] in ('identification','derivation','reviewed_lemma'), 'missing-connecting-derivation')
        location(deriv['location'])
        assertion(deriv['output_assertion'])
        g.require(deriv['output_assertion'] == conn['needed_assertion'], 'connection-output-too-weak-or-different')
        aid = deriv['application_id']
        if aid is None:
            g.require(use['inline_argument'] == deriv['location'], 'unmatched-inline-connection')
        else:
            g.require(aid in apps and aid != COVERAGE_ID and
                      (aid == use['application_id'] or aid in apps[use['consumer']]['dependencies']), 'unmatched-connection-application')
            g.require(deriv['location']['pin'] in apps[aid]['files'], 'connection-application-does-not-bind-derivation')
        if deriv['kind'] == 'identification':
            g.require(conn['available_assertion'] == conn['needed_assertion'] and not derived,
                      'nonidentical-contract-needs-derivation')
        adverse = conn['adverse_cases']
        g.fields(adverse, 'status reason evidence', 'adverse-cases')
        g.require(adverse['status'] in ('checked','not_applicable') and g.text(adverse['reason']), 'unresolved-adverse-cases')
        locations(adverse['evidence'])
        subjects['connection:'+uid] = (g.digest(conn), False)

    findings = {f['id']: f for f in packet['findings']}
    reviews = g.unique(record['findings'], 'finding_id', 'related-use-reviews')
    g.require(set(reviews) == set(findings), 'unclassified-or-extra-finding')
    for fid, review in reviews.items():
        g.fields(review, 'finding_id finding_sha256 classification mechanism search_scope scope_reason exclusions occurrences correction limitations', 'related-use-review')
        f = findings[fid]
        g.require(review['finding_sha256'] == g.digest(f), 'stale-related-finding')
        g.require(review['classification'] in ('substantive_failure','not_substantive_failure'), 'unclassified-failure')
        g.require(all(g.text(review[k]) for k in ('mechanism','scope_reason','limitations')), 'related-use-scope-or-limitations')
        locations(review['search_scope'])
        g.require(type(review['exclusions']) is list, 'related-use-exclusions')
        for exclusion in review['exclusions']:
            g.fields(exclusion, 'location reason', 'related-use-exclusion')
            location(exclusion['location'])
            g.require(g.text(exclusion['reason']), 'unexplained-related-use-exclusion')
        occurrences = g.unique(review['occurrences'], 'id', 'related-occurrences')
        if review['classification'] == 'substantive_failure':
            g.require(profile['mode'] == 'substantive' and occurrences, 'missing-related-failure-occurrences')
        for occurrence in occurrences.values():
            g.fields(occurrence, 'id use_ids location inclusion_reason disposition evidence', 'related-occurrence')
            location(occurrence['location'])
            g.require(g.string_set(occurrence['use_ids'], 'related-use-ids') <= set(uses), 'unknown-related-use')
            g.require(g.text(occurrence['inclusion_reason']), 'missing-related-inclusion-reason')
            g.require(occurrence['disposition'] in ('justified','corrected_reviewed','inapplicable'), 'unresolved-required-related-occurrence')
            locations(occurrence['evidence'])
        correction = review['correction']
        if f['status'] == 'repaired':
            g.require(correction is not None, 'missing-current-representation-check')
        if correction is not None:
            g.fields(correction, 'rejected_assertion current_assertion canonical_location representations scope limitations', 'correction-consistency')
            g.require(all(g.text(correction[k]) for k in ('rejected_assertion','current_assertion','scope','limitations')),
                      'correction-scope-or-assertion')
            g.require(correction['rejected_assertion'] != correction['current_assertion'], 'uncorrected-rejected-assertion')
            location(correction['canonical_location'])
            reps = g.unique(correction['representations'], 'id', 'current-representations')
            g.require(reps, 'missing-current-representations')
            current_locations = []
            for rep in reps.values():
                g.fields(rep, 'id location status recorded_assertion reason', 'current-representation')
                location(rep['location'])
                g.require(rep['status'] in ('current','retired') and g.text(rep['reason']), 'representation-status')
                g.require(g.text(rep['recorded_assertion']), 'missing-representation-assertion')
                if rep['status'] == 'current':
                    g.require(rep['recorded_assertion'] == correction['current_assertion'], 'stale-current-representation')
                    current_locations.append(rep['location'])
            g.require(correction['canonical_location'] in current_locations, 'canonical-current-representation-missing')
        subjects['finding:'+fid] = (g.digest(review), review['classification'] == 'not_substantive_failure')

    # Report bytes are bound by the already verified receipt. Author-supplied
    # favorable fields cannot stand in for a reviewer-authored exact decision.
    def report(receipt, expected):
        value = g.parse_json_bytes(read_pin(receipt['report']), 'protocol14-review-report')
        g.fields(value, 'schema scope limitations decisions', 'protocol14-review-report')
        g.require(value['schema'] == 'protocol14-review/v1' and g.text(value['scope']) and g.text(value['limitations']),
                  'protocol14-review-scope')
        decisions = g.unique(value['decisions'], 'subject', 'protocol14-decisions')
        g.require(set(decisions) == set(expected), 'missing-or-extra-protocol14-acceptance')
        for name, (expected_hash, consistency_allowed) in expected.items():
            decision = decisions[name]
            g.fields(decision, 'subject subject_sha256 outcome review_basis prior_review scope limitations', 'protocol14-decision')
            g.require(decision['subject_sha256'] == expected_hash, 'stale-protocol14-acceptance')
            g.require(decision['outcome'] == 'accepted_within_scope' and g.text(decision['scope']) and g.text(decision['limitations']),
                      'protocol14-not-accepted')
            bases = ('reconstructed','reused_exact_derivation','consistency_only') if consistency_allowed else ('reconstructed','reused_exact_derivation')
            g.require(decision['review_basis'] in bases, 'consistency-cannot-accept-connection')
            if decision['review_basis'] == 'reused_exact_derivation':
                g.require(decision['prior_review'] is not None, 'missing-exact-prior-review')
                read_pin(decision['prior_review'])
            else:
                g.require(decision['prior_review'] is None, 'unexpected-prior-review')

    rhash = g.digest(record)
    subjects['inventory'] = (rhash, profile['mode'] == 'non_substantive')
    report(by_target['application', COVERAGE_ID], subjects)
    report(by_target['assembly','complete'], {'assembly': (rhash, profile['mode'] == 'non_substantive')})
    return {'protocol_coverage':'1.4-'+('substantive-records-reviewed' if profile['mode'] == 'substantive' else 'non-substantive-scope-only'),
            'connection_record_sha256':rhash, 'connection_count':len(connections),
            'related_finding_count':len(reviews), 'protocol14_limitation':LIMITATION}
