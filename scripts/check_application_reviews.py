"""Check review records and exact revisions. This does not check mathematical truth."""
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
CURRENT = 'docs/audit-history/current.json'
OBLIGATIONS = {
    'source_hypotheses', 'constructed_objects', 'index_domain_coverage',
    'transition_maps', 'limiting_object_identity', 'coefficient_conventions',
    'local_conditions', 'exceptional_cases', 'downstream_consumption',
}
ROLES = {'construction', 'application', 'consumer'}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def pin_read(pin, read):
    path = pin['path']
    need(isinstance(path, str) and '\\' not in path and ':' not in path and
         not PurePosixPath(path).is_absolute() and '..' not in PurePosixPath(path).parts,
         'Unsafe repository path')
    raw = read(path)
    need(sha(raw) == pin['sha256'], 'Changed bound file: ' + path)
    return raw


def validate(record, read):
    need(record['schema'] == 1, 'Unknown current-review schema')
    manuscript = pin_read(record['manuscript'], read)
    baseline = pin_read(record['baseline'], read)
    builder = read('scripts/build_paper.py').decode()
    selected = re.findall(r'''^\s*source\s*=\s*ROOT\s*/\s*["']([^"']+)["']\s*/\s*["']([^"']+)["']\s*$''', builder, re.M)
    need(len(selected) == 1 and '/'.join(selected[0]) == record['manuscript']['path'],
         'Current builder has no matching review binding')
    need(record['scope_limitation'].strip(), 'Missing review scope limitation')
    contracts = {}
    for entry in record['contracts']:
        payload = json.loads(pin_read(entry['contract'], read))
        approval = json.loads(pin_read(entry['approval'], read))
        cid = payload['id']
        need(cid not in contracts, 'Duplicate application contract')
        contracts[cid] = payload
        need(payload['manuscript'] == record['manuscript'], 'Contract belongs to another revision')
        need(payload['authors'] and len(set(payload['authors'])) == len(payload['authors']), 'Missing or duplicate authors')
        need(approval['decision'] == 'accepted', 'Application not independently accepted: ' + cid)
        need(approval['reviewer'].strip() and approval['reviewer'] not in payload['authors'],
             'Author cannot independently accept own application')
        need(approval['contract_sha256'] == entry['contract']['sha256'], 'Approval covers another contract')
        need(approval['manuscript_sha256'] == record['manuscript']['sha256'], 'Approval covers another manuscript')
        pin_read(approval['report'], read)
        need(approval['scope'].strip(), 'Missing acceptance scope')
        sources = payload['sources']
        need(sources and len({s['id'] for s in sources}) == len(sources), 'Missing or duplicate primary sources')
        source_ids = {s['id'] for s in sources}
        for source in sources:
            need(source['url'].startswith('https://') and source['version'].strip() and
                 source['locator'].strip() and re.fullmatch('[0-9a-f]{64}', source['sha256']),
                 'Incomplete exact primary-source reference')
        evidence = payload['evidence']
        need(evidence, 'No source-comparison evidence')
        for p in evidence.values():
            pin_read(p, read)
        spans = payload['manuscript_spans']
        need(ROLES <= {s['role'] for s in spans}, 'Missing construction, application or consumer')
        lines = manuscript.decode().splitlines(keepends=True)
        for span in spans:
            a, b = span['start_line'], span['end_line']
            need(isinstance(a, int) and isinstance(b, int) and 1 <= a <= b <= len(lines), 'Invalid reviewed span')
            need(sha(''.join(lines[a-1:b]).encode()) == span['sha256'], 'Changed reviewed span')
        need(set(payload['obligations']) == OBLIGATIONS, 'Missing or unknown interface obligation')
        for name, obligation in payload['obligations'].items():
            need(obligation['status'] in {'checked', 'not_applicable'}, 'Unresolved obligation: ' + name)
            need(obligation['required'].strip() and obligation['constructed'].strip() and
                 obligation['justification'].strip(), 'Missing source-to-construction comparison: ' + name)
            need(obligation['evidence'] and set(obligation['evidence']) <= set(evidence), 'Missing obligation evidence')
            need(obligation['sources'] and set(obligation['sources']) <= source_ids, 'Missing obligation source')
        need(payload['dependency_impact'].strip(), 'Missing downstream impact review')

    text = baseline.decode()
    edits = record['edits']
    need(edits and len({e['id'] for e in edits}) == len(edits), 'Missing or duplicate revision edits')
    consumed = set()
    reviewed_edits = {}
    for edit in edits:
        old, new = edit['old'], edit['new']
        need(old and old != new and text.count(old) == 1, 'Ambiguous, empty or ineffective revision edit')
        if edit['kind'] == 'administrative':
            # Administrative changes cannot conceal a changed mathematical passage.
            # Released editions through 12 use a period. The author requires
            # edition 13 onward to omit it. Only this exact title fragment is
            # administrative; appended text still requires a reviewed edit.
            def title_fragment(value):
                match = re.fullmatch(r'\\large Version ([1-9][0-9]*)(\.)?', value)
                return bool(match) and bool(match[2]) == (int(match[1]) <= 12)
            date = r'\\date\{[A-Za-z]+ [0-9]{1,2}, [0-9]{4}\}'
            need((title_fragment(old) and title_fragment(new)) or
                 (re.fullmatch(date, old) and re.fullmatch(date, new)),
                 'Non-administrative text requires an application contract')
        else:
            need(edit['kind'] in {'mathematical', 'source'}, 'Unknown edit classification')
            need(edit['contract_id'] in contracts, 'Changed application has no accepted contract')
            consumed.add(edit['contract_id'])
            reviewed_edits.setdefault(edit['contract_id'], {})[edit['id']] = sha(encoded(edit))
        text = text.replace(old, new, 1)
    need(text.encode() == manuscript, 'Manuscript contains changes outside the reviewed edits')
    need(consumed == set(contracts), 'Contract is not connected to an actual revision edit')
    for cid, payload in contracts.items():
        need(payload['reviewed_edits'] == reviewed_edits[cid],
             'Contract does not explicitly review these exact edits: ' + cid)

    # Preserve all nine legacy dispositions as historical, not fresh mathematical acceptance.
    legacy = json.loads(pin_read(record['legacy_register'], read))
    need(legacy['manuscript'] == record['baseline'], 'Legacy register does not cover the baseline')
    need(set(record['legacy_carry_forward']) == {str(i['number']) for i in legacy['items']},
         'Missing legacy disposition coverage')
    for row in legacy['items']:
        carry = record['legacy_carry_forward'][str(row['number'])]
        if carry['mode'] == 're_reviewed':
            need(carry['contract_id'] in contracts, 'No fresh acceptance for changed legacy application')
        else:
            need(carry['mode'] == 'unchanged_historical', 'Unknown carry-forward mode')
            base_lines = baseline.decode().splitlines(keepends=True)
            for span in row['application_spans']:
                passage = ''.join(base_lines[span['start_line']-1:span['end_line']]).encode()
                need(sha(passage) == span['sha256'] and passage in manuscript,
                     'Changed legacy passage cannot inherit historical disposition')
        need(carry['impact_assessment'].strip(), 'Missing legacy dependency-impact assessment')
    findings = record['followups']
    need(findings and len({f['url'] for f in findings}) == len(findings), 'Missing or duplicate follow-up ledger')
    snapshot = json.loads(pin_read(record['issue_snapshot'], read))
    required = snapshot['required_comment_ids']
    comments = {c['id']: c for c in snapshot['comments']}
    need(required and set(required) <= set(comments), 'Missing required source comment')
    latest = max(snapshot['comments'], key=lambda c: c['updated_at'])
    need(latest['id'] in required, 'Snapshot latest comment missing from required findings')
    need({f['url'] for f in findings} == {comments[i]['url'] for i in required},
         'Follow-up ledger omits or changes a required source finding')
    for finding in findings:
        need(finding['url'].startswith('https://') and finding['claim'].strip(), 'Missing follow-up identity')
        need(finding['status'] == 'addressed' and finding['contracts'] and
             set(finding['contracts']) <= set(contracts), 'Unresolved follow-up or missing acceptance')
    return len(contracts)


def self_test(record, read):
    """Mutate the accepted record and its bound files to test meaningful rejection paths."""
    cases = []
    def changed(label, mutate):
        item = copy.deepcopy(record)
        mutate(item)
        cases.append((label, item, read))
    changed('unreviewed edit', lambda r: r['edits'].append({'id':'bad','old':'absent','new':'changed','kind':'mathematical','contract_id':'absent'}))
    changed('missing follow-up', lambda r: r.update(followups=[]))
    changed('latest finding omitted but older one retained', lambda r: r['followups'][0].update(url='https://example.com/older-finding'))
    changed('open follow-up', lambda r: r['followups'][0].update(status='open'))
    changed('missing carry-forward', lambda r: r['legacy_carry_forward'].pop(next(iter(r['legacy_carry_forward']))))
    changed('missing contract', lambda r: r.update(contracts=[]))
    def contract_case(label, mutate, fresh_approval=True):
        item = copy.deepcopy(record)
        entry = item['contracts'][0]
        payload = json.loads(read(entry['contract']['path']))
        mutate(payload)
        raw = encoded(payload)
        entry['contract']['sha256'] = sha(raw)
        altered = {entry['contract']['path']: raw}
        if fresh_approval:
            approval = json.loads(read(entry['approval']['path']))
            approval['contract_sha256'] = sha(raw)
            altered[entry['approval']['path']] = encoded(approval)
            entry['approval']['sha256'] = sha(altered[entry['approval']['path']])
        cases.append((label, item, lambda p: altered[p] if p in altered else read(p)))
    contract_case('missing index-domain check', lambda p: p['obligations'].pop('index_domain_coverage'))
    contract_case('missing limiting-class identity', lambda p: p['obligations'].pop('limiting_object_identity'))
    contract_case('missing transition check', lambda p: p['obligations'].pop('transition_maps'))
    contract_case('unsupported obligation', lambda p: p['obligations']['index_domain_coverage'].update(evidence=[]))
    contract_case('unresolved obligation', lambda p: p['obligations']['index_domain_coverage'].update(status='open'))
    contract_case('missing construction', lambda p: p.update(manuscript_spans=[s for s in p['manuscript_spans'] if s['role']!='construction']))
    contract_case('contract reused for unreviewed edits', lambda p: p.update(reviewed_edits={}))
    contract_case('changed input with stale approval', lambda p: p.update(dependency_impact=p['dependency_impact']+' changed'), False)
    # Even a rehashed approval must name a different reviewer and remain affirmative.
    for label, mutate in [('self-review', lambda a,p: a.update(reviewer=p['authors'][0])),
                          ('pending independent review', lambda a,p: a.update(decision='pending'))]:
        item = copy.deepcopy(record); entry = item['contracts'][0]
        approval = json.loads(read(entry['approval']['path']))
        mutate(approval, json.loads(read(entry['contract']['path'])))
        raw = encoded(approval); entry['approval']['sha256'] = sha(raw)
        target = entry['approval']['path']
        cases.append((label, item, lambda p,t=target,b=raw: b if p==t else read(p)))
    for path in [record['manuscript']['path'], record['contracts'][0]['contract']['path']]:
        cases.append(('changed bound bytes', record, lambda p,t=path: read(p)+b'\nchanged' if p==t else read(p)))
    builder_path = 'scripts/build_paper.py'
    cases.append(('new edition without acceptance', record, lambda p: b'source = ROOT / "manuscripts" / "unreviewed.tex"\n' if p==builder_path else read(p)))
    for label, item, reader in cases:
        try:
            validate(item, reader)
        except ValueError:
            continue
        raise ValueError('Negative control unexpectedly accepted: ' + label)
    print(f'PASS: {len(cases)} application-review negative controls rejected.')


def check_current(read, test=False):
    record = json.loads(read(CURRENT))
    count = validate(record, read)
    if test:
        self_test(record, read)
    print(f'PASS: {count} current application contracts, revision and follow-up records. Not a proof check.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    check_current(lambda p: (ROOT / p).read_bytes(), args.self_test)
