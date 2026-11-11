"""Assemble a Version 14 manuscript/navigation overlay for independent review."""
import argparse
from datetime import date
import json
from pathlib import Path
import re

from release_common import (
    PACKAGE, REGISTER, REVISION, V13_TEX, V13_TEX_SHA, V14_TEX,
    blob, commit, git, json_bytes, output_dir, pinned, put, read, sha,
)

PROTOCOL_MANIFEST_SHA = '2d5d9f5eb02ca11ac145d53b02f3c722ffb2e3e375464dd040b923227fa45a8d'
PROTOCOL_PATH = 'docs/research-review/PROTOCOL.md'
HISTORICAL_PROTOCOL = 'docs/research-review/protocol-v1.2.md'

INTRO = r'''Version 14 gives a quartic in 299 total variables and an ordinary
 decimal-coefficient quartic in 314 total variables. Section~\ref{sec:v14}
 proves the reductions and specifies their exact coefficient tables.
 The Version 13 constructions and their arithmetic inputs remain as proof
 baselines. Version 11's index-set and retained-class identification in the
 published Kato application is unchanged.'''.replace('\n ', '\n')


def replace_once(text, old, new, label):
    if text.count(old) != 1:
        raise ValueError('Expected exactly one ' + label)
    return text.replace(old, new, 1)


def assemble_manuscript(baseline, addition, day, decimal_bytes, register):
    text = baseline.decode('utf-8')
    proof = addition.decode('utf-8')
    if proof.count(r'\label{sec:v14}') != 1 or any(
        marker in proof for marker in (r'\begin{document}', r'\end{document}', r'\begin{thebibliography}')
    ):
        raise ValueError('Addition must be an independently reviewed Version 14 section')
    edits = []

    def edit(name, old, new, kind):
        nonlocal text
        text = replace_once(text, old, new, name)
        record = {'id': name, 'old': old, 'new': new, 'kind': kind}
        if kind == 'mathematical':
            record['contract_id'] = 'QUARTIC-299-COMPOSITION'
        edits.append(record)

    edit('v14-title', r'\large Version 13', r'\large Version 14', 'administrative')
    dates = re.findall(r'\\date\{[^}]+\}', text)
    if len(dates) != 1:
        raise ValueError('Unexpected baseline date field')
    new_date = r'\date{' + day + '}'
    if dates[0] != new_date:
        edit('v14-date', dates[0], new_date, 'administrative')
    start = text.index('We show the minimum degree')
    end = text.index('\n\nWell-known consequences', start)
    amount = format(decimal_bytes, ',').replace(',', r'\,')
    abstract = r'''We show the minimum degree of a Diophantine definition for $\Z$ in $\Q$
is 4 and specify two smaller quartics. The first has $314$ variables,
$6\,672$ nonzero monomials, and coefficients of magnitude below $2^{6496}$.
Its complete decimal coefficient table occupies $TABLEBYTES$ bytes.
The second has $299$ variables, $6\,630$ nonzero monomials, and largest
absolute coefficient $186624\cdot3^{2^{26}}$. Its table writes coefficients
relative to the fixed integer $C=3^{2^{25}}$.
Both rational zero projections are exactly $\Z$.'''.replace('TABLEBYTES', amount)
    edit('v14-abstract', text[start:end], abstract, 'mathematical')
    start = text.index('Version 13 gives a quartic')
    end = text.index('\n\nVersion 10 clarified', start)
    edit('v14-introduction', text[start:end], INTRO, 'mathematical')
    bibliography = r'\begin{thebibliography}{99}'
    edit('v14-proof-addition', bibliography, proof.rstrip('\n') + '\n\n' + bibliography, 'mathematical')
    old_edits = register['edits']
    if set(x['id'] for x in old_edits) & set(x['id'] for x in edits):
        raise ValueError('Version 14 edit ID already present')
    return text.encode('utf-8'), old_edits + edits, edits


def navigation(get, day, decimal_bytes):
    count = format(decimal_bytes, ',')
    edits = {}

    def set_text(path, edit):
        text = get(path).decode('utf-8')
        updated = edit(text)
        if updated == text:
            raise ValueError('Unchanged current pointer: ' + path)
        edits[path] = updated.encode('utf-8')

    def readme(text):
        opening, rest = text.split('\n\nThe project uses', 1)
        if '## Version 13' not in opening or 'Version 9 starting reductions' not in opening:
            raise ValueError('README opening has changed')
        text = f'''# Z is Diophantine in Q

## Version 14

This repository contains *Z is Diophantine in Q*, Version 14, dated {day}. It gives quartics in **299 total variables** with exact symbolic coefficients and **314 total variables** with every coefficient written out in decimal. The original large construction, earlier quartic proofs and Version 11 Kato index-set and limiting-class repair remain in the manuscript. The Version 9 starting reductions were contributed by Gabriel Conant with ChatGPT.

The project uses''' + rest
        text = replace_once(text, '| Read Version 13 | [Manuscript PDF](manuscripts/quartic_v13.pdf), [TeX source](manuscripts/quartic_v13.tex) |',
            '| Read Version 14 | [Manuscript PDF](manuscripts/quartic_v14.pdf), [TeX source](manuscripts/quartic_v14.tex) |', 'current manuscript link')
        row = '| Reproduce the 394/411-variable quartics |'
        text = replace_once(text, row, '| Reproduce the 299/314-variable quartics | [Tables, proof inventory and review scopes](docs/manuscript-revisions/version14/GUIDE.md) |\n' + row, 'quartic navigation')
        text = replace_once(text, '[Version 13 supplement and guide](research/version13/README.md), [Version 12 archive](research/version12/README.md)',
            '[Version 14 cumulative supplement](research/version14/README.md), [Version 13 archive](research/version13/README.md)', 'current supplement link')
        row = '| Version 13, decimal table |'
        text = replace_once(text, row, r'''| Version 14, decimal table | 314 | 4 | 6,672 | Less than $2^{6496}$ |
| Version 14, symbolic table | 299 | 4 | 6,630 | Maximum $186624\cdot3^{2^{26}}$ |
''' + row, 'current table rows')
        marker = 'The [411-variable decimal table]'
        text = replace_once(text, marker, f'''The [314-variable decimal table](quartics/quartic-314-fully-expanded.txt) contains every coefficient in decimal and occupies {count} bytes. The [299-variable table](quartics/quartic-299-symbolic-coefficients.json) uses the fixed integer $C=3^{{2^{{25}}}}$. See the [Version 14 guide](docs/manuscript-revisions/version14/GUIDE.md) for the construction, inventory and review scopes.

''' + marker, 'table description')
        return replace_once(text, 'The manuscript supplies that arithmetic argument. ',
            'The manuscript supplies that arithmetic argument. The [Version 14 guide](docs/manuscript-revisions/version14/GUIDE.md) records the exact current constructions and separates the finite checks from their mathematical review. ', 'review scope')

    set_text('README.md', readme)

    def manuscripts(text):
        header, archive = text.split('## Earlier versions\n', 1)
        header = header.replace('Version 13', 'Version 14').replace('November 7, 2026', day).replace('quartic_v13', 'quartic_v14').replace('version13', 'version14')
        return header + '## Earlier versions\n' + replace_once(archive, '| 12 |',
            '| 13 | [PDF](quartic_v13.pdf) | [TeX](quartic_v13.tex) |\n| 12 |', 'archive row')

    set_text('manuscripts/README.md', manuscripts)

    def quartics(text):
        row = '| 394 |'
        text = replace_once(text, row, '''| 299 | [quartic-299-symbolic-coefficients.json](quartic-299-symbolic-coefficients.json), [text](quartic-299-symbolic-coefficients.txt) | Exact coefficients, `C=3^(2^25)` | [Version 14 guide](../docs/manuscript-revisions/version14/GUIDE.md) |
| 314 | [quartic-314-fully-expanded.txt](quartic-314-fully-expanded.txt) | Fully written decimal integers | [Version 14 guide](../docs/manuscript-revisions/version14/GUIDE.md) |
''' + row, 'quartic index row')
        return replace_once(text, 'The 411-variable quartic is the smallest here with every coefficient written out in decimal.',
            f'The 314-variable decimal table has 6,672 monomials, occupies {count} bytes and has coefficient magnitudes below `2^6496`. The 299-variable symbolic table has 6,630 monomials.\n\nThe 411-variable quartic is the Version 13 decimal companion.', 'quartic index description')

    set_text('quartics/README.md', quartics)

    def citation(text):
        first, rest = text.split('\n}\n', 1)
        if 'Version 13' not in first:
            raise ValueError('Unexpected current citation')
        current = first.replace('Version 13', 'Version 14').replace('November 7, 2026', day).replace('394 and 411', '299 and 314')
        historic = first.replace('@misc{z_in_q_2026,', '@misc{z_in_q_version13_2026,')
        return current + '\n}\n\n' + historic + '\n}\n' + rest

    set_text('CITATION.bib', citation)

    def guide(text):
        first, tail = text.split('\n\nThe [research handoff guide]', 1)
        if 'Version 13' not in first:
            raise ValueError('Unexpected research guide introduction')
        current = f"""# Research guide

The current manuscript is [*Z is Diophantine in Q*, Version 14](../manuscripts/quartic_v14.pdf), dated {day}, with [TeX source](../manuscripts/quartic_v14.tex). Start with the [299/314-variable constructions and review scopes](manuscript-revisions/version14/GUIDE.md), [application inventory](manuscript-revisions/version14/APPLICATIONS.json) and [cumulative supplement](../research/version14/README.md). The original construction and earlier proof baselines remain in the manuscript.

The [Version 13 guide](manuscript-revisions/version13/GUIDE.md) and [supplement](../research/version13/README.md) preserve the 394/411-variable edition."""
        historical = first.split('Continue with the [Version 12', 1)[1]
        return current + ' Continue with the [Version 12' + historical + '\n\nThe [research handoff guide]' + tail

    set_text('docs/research-guide.md', guide)

    def archiving(text):
        old, tail = text.split('\n\nThe manuscript author field', 1)
        if 'Version 13' not in old:
            raise ValueError('Unexpected archive current pointer')
        old = old.replace('Version 13', 'Version 14').replace('November 7, 2026', day).replace('quartic_v13', 'quartic_v14')
        text = old + '\n\nThe manuscript author field' + tail
        return replace_once(text, '## Version 13 supplement',
            '## Version 14 cumulative supplement\n\nThe [Version 14 supplement guide](../research/version14/README.md) identifies the exact manuscript, selected coefficient tables, inventory, checks and cumulative research evidence. It preserves the Version 13 supplement as a hash-verified historical layer.\n\n## Version 13 supplement', 'archive supplement section')

    set_text('docs/archiving.md', archiving)
    def building(text):
        start = text.index('## Version 13 manuscript')
        end = text.index('## Manuscript inventories', start)
        text = text[:start] + '''## Version 14 manuscript

Run `python scripts/build_paper.py` to build the current Version 14 TeX with the pinned Tectonic engine and bundle. The build writes `quartic_v14.pdf`, its logs and the build receipt under `build/paper/`; it does not replace the checked-in PDF. Review the exact rendered pages and total page count recorded in the Version 14 PDF QA receipt and reviewed workflow. Historical Version 13 receipts retain their original scope.

''' + text[end:]
        return replace_once(text, '## Current 394- and 411-variable quartics',
            '## Current 299- and 314-variable quartics\n\n'
            'Run the exact replay and inventory commands in the [Version 14 guide](manuscript-revisions/version14/GUIDE.md). '
            'Its finite checks, manuscript review and inherited arithmetic inputs have separate scopes.\n\n'
            '## Historical 394- and 411-variable quartics', 'build guide current quartics')

    set_text('docs/building.md', building)
    set_text('docs/release-policy.md', lambda text: replace_once(text,
        'The next thresholds are strictly below 300, 200, then 100.',
        'Version 14 records the below-300 milestone with 299 total variables. The next thresholds are strictly below 200, then 100.',
        'publication threshold'))
    return edits


def validate_decimal_table(raw, expected_count):
    terms = set()
    for row in raw.decode('ascii').splitlines():
        if row.startswith('#'):
            continue
        coefficient, power, variables = row.split(' | ')
        if not re.fullmatch(r'-?[1-9][0-9]*', coefficient) or power != '0':
            raise ValueError('Invalid ordinary coefficient row')
        coordinate_ids = tuple(map(int, variables.split(','))) if variables else ()
        if (len(coordinate_ids) > 4 or any(not 1 <= x <= 314 for x in coordinate_ids)
                or tuple(sorted(coordinate_ids)) != coordinate_ids or coordinate_ids in terms):
            raise ValueError('Invalid or duplicate compact monomial')
        terms.add(coordinate_ids)
    if len(terms) != expected_count:
        raise ValueError('Unexpected ordinary term count')


def add_protocol(files, source, repo, base):
    raw = pinned(read(source, 'MANIFEST.json'), PROTOCOL_MANIFEST_SHA, 'accepted v1.3 document manifest')
    reviewed = json.loads(raw)['files']
    expected = {'.github/pull_request_template.md', 'CONTRIBUTING.md', 'README.md',
        PROTOCOL_PATH, 'docs/research-review/README.md', HISTORICAL_PROTOCOL}
    if {row['path'] for row in reviewed} != expected or len(reviewed) != len(expected):
        raise ValueError('Unexpected v1.3 documentation scope')
    for row in reviewed:
        name = row['path']
        approved = pinned(read(source, 'files/' + name), row['candidate_sha256'], name)
        if len(approved) != row['bytes']:
            raise ValueError('Unexpected v1.3 file size: ' + name)
        if row['base_sha256'] is None:
            if git(repo, 'ls-tree', '--full-tree', base, '--', name):
                raise ValueError('Historical v1.2 destination already exists')
        else:
            pinned(blob(repo, base, name), row['base_sha256'], name + ' base preimage')
        if name != 'README.md':
            files[name] = approved
            continue
        old_line = '| Inspect the current repair and review protocol | [Version 11 source audit](docs/manuscript-revisions/version11/README.md), [protocol](docs/audit-history/PROTOCOL.md) |'
        approved_lines = approved.decode('utf-8').splitlines()
        pointer = next(i for i, line in enumerate(approved_lines) if line.startswith('| Follow the current mathematical research review protocol |'))
        new_lines = '\n'.join(approved_lines[pointer:pointer+2])
        files[name] = replace_once(files[name].decode('utf-8'), old_line, new_lines, 'approved v1.3 README link delta').encode('utf-8')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', required=True, type=Path)
    p.add_argument('--base', required=True)
    p.add_argument('--addition', required=True, type=Path)
    p.add_argument('--addition-sha256', required=True)
    p.add_argument('--package', required=True, type=Path)
    p.add_argument('--artifacts-sha256', required=True)
    p.add_argument('--protocol-documents', required=True, type=Path)
    p.add_argument('--date', required=True, type=date.fromisoformat)
    p.add_argument('--output', required=True, type=Path)
    args = p.parse_args()
    base = commit(args.repo, args.base)
    get = lambda name: blob(args.repo, base, name)
    baseline = pinned(get(V13_TEX), V13_TEX_SHA, V13_TEX)
    addition = pinned(args.addition.read_bytes(), args.addition_sha256, 'independent TeX addition')
    package = args.package.resolve()
    artifacts_raw = pinned(read(package, 'ARTIFACTS.json'), args.artifacts_sha256, 'reviewed artifact statistics')
    artifacts = json.loads(artifacts_raw)
    stats = artifacts['statistics']
    table_name = 'quartic-314-ordinary-coefficients.txt'
    table_pin = artifacts['files'][table_name]
    table = pinned(read(package, table_name), table_pin['sha256'], table_name)
    if (artifacts['inputCoordinate'] != 1 or artifacts['coordinateRange'] != '1..totalVariables'
            or stats['299']['variables'] != 299 or stats['299']['monomials'] != 6630
            or stats['299']['maximumCoefficient'] != '186624*3^(2^26)'
            or stats['314']['variables'] != 314 or stats['314']['monomials'] != 6672
            or stats['314']['maximumCoefficientBits'] != 6496
            or stats['314']['compactTextBytes'] != len(table) or table_pin['bytes'] != len(table)):
        raise ValueError('Selected compact tables or statistics differ from the reviewed Version 14 selection')
    validate_decimal_table(table, 6672)
    day = args.date.strftime('%B ') + str(args.date.day) + args.date.strftime(', %Y')
    registry_raw = get(REGISTER)
    registry = json.loads(registry_raw)
    if registry['manuscript'] != {'path': V13_TEX, 'sha256': V13_TEX_SHA}:
        raise ValueError('Base current register must name exact Version 13')
    manuscript, edits, new_edits = assemble_manuscript(baseline, addition, day, len(table), registry)
    files = navigation(get, day, len(table))
    add_protocol(files, args.protocol_documents.resolve(), args.repo, base)
    files.update({V14_TEX: manuscript, REVISION + '/addition.tex': addition,
        REVISION + '/edits.json': json_bytes(edits), REVISION + '/new-edits.json': json_bytes(new_edits),
        REVISION + '/v13-review-record.json': registry_raw})
    output = output_dir(args.output)
    for name, raw in sorted(files.items()):
        put(output, name, raw)
    receipt = {'schema': 'quartic-v14-manuscript-preparation/v1', 'base': base, 'date': day,
        'baseline_sha256': V13_TEX_SHA, 'addition_sha256': args.addition_sha256,
        'artifacts_sha256': args.artifacts_sha256, 'decimal_table_sha256': table_pin['sha256'], 'decimal_table_bytes': len(table),
        'files': {name: {'sha256': sha(raw), 'bytes': len(raw)} for name, raw in sorted(files.items())},
        'protocol_docs_manifest_sha256': PROTOCOL_MANIFEST_SHA,
        'status': 'assembly candidate for independent review; current audit register unchanged'}
    put(output, 'PREPARATION.json', json_bytes(receipt))


if __name__ == '__main__':
    main()
