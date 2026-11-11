"""Portable V14 author-inventory validator. Structural checks are not proof review."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

OBLIGATIONS = (
    'required_inputs', 'constructed_inputs', 'domain_and_index_coverage',
    'transition_maps_and_scalars', 'identity_of_consumed_object',
    'exceptional_cases', 'affected_downstream_claims',
    'source_version_and_conventions', 'validation_and_acceptance_scope')
ROLES = {'current_consumer', 'supporting_derivation', 'archived'}
HASH = re.compile(r'[0-9a-f]{64}\Z')
PREFIX = 'docs/manuscript-revisions/version14/'


class Invalid(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise Invalid(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                      allow_nan=False).encode('utf-8')


def identical(a, b):
    """Unlike Python equality, keep JSON booleans, integers and floats distinct."""
    return canonical(a) == canonical(b)


def parse(data):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'duplicate JSON key: ' + key)
            result[key] = value
        return result
    def invalid_constant(value):
        raise Invalid('non-finite JSON number: ' + value)
    return json.loads(data, object_pairs_hook=pairs, parse_constant=invalid_constant)


def path_ok(name):
    require(isinstance(name, str) and name and '\\' not in name and ':' not in name,
            'not a portable relative path')
    p = PurePosixPath(name)
    require(not p.is_absolute() and str(p) == name and
            all(x not in ('', '.', '..') for x in name.split('/')),
            'noncanonical relative path')
    return name


def text(value, name):
    require(isinstance(value, str) and value.strip(), 'missing ' + name)
    require(value.strip().lower() not in {'todo', 'pending', 'tbd', 'unchanged'},
            'placeholder ' + name)
    return value


class Files:
    """Read a staging overlay and a read-only existing repository."""
    def __init__(self, root, overlay=None):
        self.root = Path(root).resolve()
        self.overlay = {} if overlay is None else dict(overlay)
        self.used = set()

    def read(self, name):
        path_ok(name)
        self.used.add(name)
        if name in self.overlay:
            return self.overlay[name]
        path = (self.root / name).resolve()
        require(path.is_relative_to(self.root), 'path escapes repository')
        require(path.is_file(), 'missing file: ' + name)
        return path.read_bytes()

    def pin(self, pin):
        require(isinstance(pin, dict) and isinstance(pin.get('sha256'), str)
                and HASH.fullmatch(pin['sha256']), 'invalid file pin')
        data = self.read(pin['path'])
        require(digest(data) == pin['sha256'], 'stale file: ' + pin['path'])
        return data

    def span(self, span):
        data = self.pin(span)
        # A raw UTF-8 span retains CRLF or LF bytes, including the final newline.
        data.decode('utf-8')
        lines = data.splitlines(keepends=True)
        start, end = span.get('start_line'), span.get('end_line')
        require(type(start) is int and type(end) is int and
                1 <= start <= end <= len(lines), 'invalid line interval')
        raw = b''.join(lines[start - 1:end])
        require(digest(raw) == span.get('sha256_raw_utf8_span'), 'stale raw span')
        if 'label' in span:
            needle = ('\\label{' + text(span['label'], 'label') + '}').encode()
            require(data.count(needle) == 1 and needle in raw,
                    'missing, duplicated or out-of-span label')
        return raw


def bind_span(files, pin, start, end, label=None):
    data = files.pin(pin)
    lines = data.splitlines(keepends=True)
    require(type(start) is int and type(end) is int and
            1 <= start <= end <= len(lines), 'invalid binding interval')
    result = dict(pin, start_line=start, end_line=end,
                  sha256_raw_utf8_span=digest(b''.join(lines[start-1:end])))
    if label is not None:
        result['label'] = label
    files.span(result)
    return result


def validate(inv, schema, files):
    require(inv.get('schema') == 'portable-application-inventory-v3', 'inventory schema')
    require(inv.get('status') == 'author_records_pending_independent_review',
            'author inventory must not assert acceptance')
    require(identical(inv.get('selected'), schema['selected']), 'wrong selected candidate pair')
    baseline = parse(files.pin(inv['baselineInventory']))
    require(identical(inv['baselineInventory'], schema['baselineInventory']), 'baseline pin changed')
    route = parse(files.pin(inv['routeSelection']))
    require(identical(inv['routeSelection'], schema['routeSelection']), 'route pin changed')
    relation = parse(files.pin(inv['r6Relation']))
    require(identical(inv['r6Relation'], schema['r6Relation']), 'R6 relation changed')
    require(identical(inv['r6Manifest'], schema['r6Manifest']), 'R6 archive changed')
    files.pin(inv['r6Manifest'])
    require(identical(inv['repairHistory'], schema['repairHistory']), 'repair history changed')
    files.pin(inv['repairHistory'])
    require(identical(inv['baselineManuscript'], schema['baselineManuscript']), 'wrong baseline text')
    files.pin(inv['baselineManuscript'])
    manuscript = files.pin(inv['manuscript'])
    addition = files.pin(inv['addition'])
    require(inv['manuscript']['path'] == 'manuscripts/quartic_v14.tex', 'wrong manuscript')
    require(inv['addition']['path'] == PREFIX + 'addition.tex', 'wrong addition')
    require(addition and manuscript.count(addition) == 1,
            'addition must occur byte-for-byte exactly once in manuscript')
    for label in schema['requiredLabels']:
        needle = ('\\label{' + label + '}').encode()
        require(addition.count(needle) == 1 and manuscript.count(needle) == 1,
                'missing or duplicate required label: ' + label)

    baseline_apps = {a['id']: a for a in baseline['applications']}
    apps = inv['applications']
    ids = [a['id'] for a in apps]
    require(ids == schema['applicationIds'] and len(ids) == len(set(ids)) == 39,
            'must retain the 39 ordered baseline application identities')
    require(set(baseline_apps) == set(ids), 'baseline application set differs')
    for app in apps:
        old = baseline_apps[app['id']]
        require(app['priorRecordSha256'] == digest(canonical(old)), 'stale prior record')
        require(set(app['obligations']) == set(OBLIGATIONS), 'nine obligations required')
        require(set(app['dependencyDisposition']) == set(OBLIGATIONS),
                'nine explicit dependency dispositions required')
        require(identical(app['sourceVersionAndConventions'], old['source']),
                'historical source/convention record must be retained exactly')
        for key in OBLIGATIONS:
            text(app['obligations'][key], key)
            d = app['dependencyDisposition'][key]
            require(d['mode'] in {'preserved', 'replaced'}, 'dependency mode')
            text(d['justification'], 'dependency justification')
            if d['mode'] == 'preserved':
                require(app['obligations'][key] == old['obligations'][key],
                        'preserved obligation text changed')
            require(d['sourceSpans'] and d['consumerSpans'],
                    'every obligation needs actual source and current consumer spans')
            for span in d['sourceSpans']:
                files.span(span)
            for span in d['consumerSpans']:
                require(span['path'] == inv['manuscript']['path'] and
                        span['sha256'] == inv['manuscript']['sha256'],
                        'consumer must bind current assembled manuscript')
                files.span(span)

    entries = {e['entryId']: e for e in route['entryDispositions']}
    expected = {(e['applicationId'], e['entryId']) for e in relation['edges']}
    require(len(expected) == len(relation['edges']) == 263, 'R6 relation not canonical')
    seen = set()
    active_entries = set()
    counts = {r: 0 for r in ROLES}
    for edge in inv['edgeBindings']:
        pair = (edge['applicationId'], edge['entryId'])
        require(pair in expected and pair not in seen, 'unknown or duplicate R6 edge')
        seen.add(pair)
        role = edge['role']
        require(role in ROLES, 'unknown edge role')
        counts[role] += 1
        text(edge['justification'], 'edge disposition')
        original_role = entries[edge['entryId']]['role']
        if original_role in {'unused_alternative', 'superseded_intermediate_circuit',
                             'artifact_repair_history'}:
            require(role == 'archived', 'archived route relabeled as current use')
        if original_role == 'supporting_source':
            require(role != 'current_consumer', 'supporting source relabeled direct')
        if role == 'archived':
            require(edge['sourceSpans'] == [] and edge['consumerSpans'] == [],
                    'archived edge must not assert current consumption')
        else:
            require(edge['sourceSpans'] and edge['consumerSpans'], 'unbound selected edge')
            for span in edge['sourceSpans']:
                files.span(span)
            for span in edge['consumerSpans']:
                require(span['path'] == inv['manuscript']['path'] and
                        span['sha256'] == inv['manuscript']['sha256'], 'stale edge consumer')
                files.span(span)
            if role == 'current_consumer':
                active_entries.add(edge['entryId'])
    require(seen == expected, 'missing R6 edge dispositions')
    require(active_entries == {k for k,v in entries.items() if v['role']=='current_application'},
            'every selected current entry needs an actual current consumer')
    require(inv['assemblyOrder'] == route['assemblyTopologicalOrder'], 'assembly chain changed')
    require(identical(inv['externalSources'], baseline['externalSources']) and
            identical(inv['existingSourceCatalog'], baseline['existingSourceCatalog']),
            'external source qualifications changed')
    require(identical(inv['finalArtifacts'], schema['finalArtifacts']), 'artifact identity/count/bound changed')
    for item in inv['finalArtifacts'].values():
        for pin in item['files']:
            files.pin(pin)
    # The artifact's independent checker remains responsible for recomputing the
    # SOS; this module binds the exact files/counts already reviewed, not new IRs.
    require(inv.get('mathematicalAcceptanceClaim') is False,
            'structural inventory cannot assert mathematical acceptance')
    return {'applications':39, 'obligations':351, 'edgeDispositions':counts,
            'assemblyIRs':len(inv['assemblyOrder']), 'status':'structural_pass_only'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--inventory', default=PREFIX+'APPLICATIONS.json')
    ap.add_argument('--schema', default=PREFIX+'validation-schema.json')
    ap.add_argument('--self-test', action='store_true')
    args = ap.parse_args()
    files = Files(args.repo)
    inv = parse(files.read(args.inventory))
    schema = parse(files.read(args.schema))
    result = validate(inv, schema, files)
    if args.self_test:
        from copy import deepcopy
        mutations = [
            lambda x: x['applications'].pop(),
            lambda x: x['applications'][0]['obligations'].pop('required_inputs'),
            lambda x: x['edgeBindings'].pop(),
            lambda x: x.update(mathematicalAcceptanceClaim=True),
            lambda x: x['selected'].update(ordinary='ordinaryReciprocal299_315'),
        ]
        for mutate in mutations:
            changed = deepcopy(inv); mutate(changed)
            try:
                validate(changed, schema, Files(args.repo))
            except (Invalid, KeyError):
                continue
            raise Invalid('self-test mutation was not rejected')
        result['negativeSelfTests'] = len(mutations)
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
