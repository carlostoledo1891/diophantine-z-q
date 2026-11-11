"""Prepare reviewed CI/build deltas as local files, preserving required job names."""
import argparse
from datetime import date, datetime, time, timezone
from pathlib import Path
import re

from prepare_manuscript import replace_once
from release_common import PACKAGE, REVISION, blob, commit, json_bytes, output_dir, put, sha

PAPER = 'scripts/build_paper.py'
WORKFLOWS = ('.github/workflows/research-checks.yml', '.github/workflows/manuscript-integration.yml')
REPLAY = 'python -B ' + PACKAGE + '/verify_lineage.py'
INVENTORY = 'python -B ' + REVISION + '/validate-applications.py --repo . --self-test'


def paper(text, day):
    if text.count('quartic_v13') != 6:
        raise ValueError('Pinned paper builder markers changed')
    text = text.replace('quartic_v13', 'quartic_v14')
    text = replace_once(text, '"manuscript_version": 13', '"manuscript_version": 14', 'manuscript version')
    epoch = int(datetime.combine(day, time.min, timezone.utc).timestamp())
    return replace_once(text, 'env["SOURCE_DATE_EPOCH"] = "1794009600"',
        f'env["SOURCE_DATE_EPOCH"] = "{epoch}"', 'fixed reproducibility date')


def workflow(text, render):
    anchor = '      - run: python -B scripts/check_audit_history.py --self-test\n'
    # Only the selected quartic matrix gets the new commands. Other jobs and
    # the legacy matrix display names stay byte-identical.
    start = text.index('  quartic394:\n')
    end = re.search(r'(?m)^  [a-z][a-z0-9_]*:\n', text[start+len('  quartic394:\n'):])
    if not end:
        raise ValueError('Missing following workflow job')
    stop = start + len('  quartic394:\n') + end.start()
    job = replace_once(text[start:stop], anchor,
        '      - run: ' + REPLAY + '\n      - run: ' + INVENTORY + '\n' + anchor,
        'selected quartic job audit step')
    result = text[:start] + job + text[stop:]
    if render is not None:
        pages, expected = render
        old = 'python scripts/render_quartic_review.py --pdf build/paper/quartic_v13.pdf --edition v13 --pages 1,276-288 --expected-pages 296'
        new = f'python scripts/render_quartic_review.py --pdf build/paper/quartic_v14.pdf --edition v14 --pages {pages} --expected-pages {expected}'
        result = replace_once(result, old, new, 'PDF review command')
        result = replace_once(result, 'Compile the exact Version 13 manuscript', 'Compile the exact Version 14 manuscript', 'compile step')
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', required=True, type=Path)
    p.add_argument('--base', required=True)
    p.add_argument('--date', required=True, type=date.fromisoformat)
    p.add_argument('--render-pages', required=True)
    p.add_argument('--expected-pages', required=True, type=int)
    p.add_argument('--output', required=True, type=Path)
    args = p.parse_args()
    if not re.fullmatch(r'[1-9][0-9]*(?:-[1-9][0-9]*)?(?:,[1-9][0-9]*(?:-[1-9][0-9]*)?)*', args.render_pages):
        raise ValueError('Invalid reviewed PDF page selection')
    values = [int(x) for x in re.findall(r'[0-9]+', args.render_pages)]
    if max(values) > args.expected_pages or 1 not in values:
        raise ValueError('PDF render selection must include page one and fit the final page count')
    base = commit(args.repo, args.base)
    get = lambda name: blob(args.repo, base, name).decode('utf-8')
    files = {PAPER: paper(get(PAPER), args.date).encode('utf-8')}
    for name, render in zip(WORKFLOWS, (None, (args.render_pages, args.expected_pages))):
        files[name] = workflow(get(name), render).encode('utf-8')
    output = output_dir(args.output)
    for name, raw in files.items():
        put(output, name, raw)
    put(output, 'CI-PREPARATION.json', json_bytes({'base': base,
        'files': {name: sha(raw) for name, raw in files.items()},
        'status': 'requires independent workflow review and protected source-policy transition'}))


if __name__ == '__main__':
    main()

