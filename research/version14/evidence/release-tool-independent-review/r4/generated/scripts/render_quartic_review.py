"""Locate and render the current manuscript sections for visual inspection."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parents[1]


def unique_heading(pages, text):
    matches = [i for i, page in enumerate(pages) if i > 10 and text in page]
    if len(matches) != 1:
        raise ValueError(f'Expected one body occurrence of {text!r}; got {[i + 1 for i in matches]}')
    return matches[0]


def automatic_selection(pages, edition):
    last = len(pages) - 1
    if edition == 'v14':
        current = unique_heading(pages, 'A quartic presentation with 299 variables')
        references = next((i for i in range(current, len(pages))
                           if re.search(r'\bReferences\b', pages[i])), None)
        if references is None:
            raise ValueError('Version 14 reference boundary is missing')
        groups = {'front_matter': list(range(min(4, len(pages)))),
                  'quartic_299': list(range(current, references + 1))}
        return sorted({i for group in groups.values() for i in group}), groups
    if edition == 'v13':
        current = unique_heading(pages, 'A quartic presentation with 394 variables')
        references = next((i for i in range(current, len(pages))
                           if re.search(r'\bReferences\b', pages[i])), None)
        if references is None:
            raise ValueError('Version 13 reference boundary is missing')
        groups = {'front_matter': list(range(min(4, len(pages)))),
                  'quartic_394': list(range(current, references + 1))}
        return sorted({i for group in groups.values() for i in group}), groups
    old_start = unique_heading(pages, 'This is the second final polynomial')
    old_end = unique_heading(pages, 'The finite checks do not replace')
    source = unique_heading(pages, 'Arithmetic interfaces for the smaller quartic')
    dependency = unique_heading(pages, 'Dependency order in the arithmetic argument')
    appendix = unique_heading(pages, 'Simultaneous primes with coprime adjacent norms')
    if not old_start <= old_end < source <= dependency < appendix <= last:
        raise ValueError('Manuscript section order differs from the review profile')
    groups = {
        'front_matter': list(range(min(4, len(pages)))),
        'retained_quartic': list(range(old_start, old_end + 1)),
        'arithmetic_source': list(range(source, dependency + 1)),
        'prime_pattern_appendix_and_references': list(range(appendix, last + 1)),
        'theta_convolution': [i for i, page in enumerate(pages)
                              if 'We check every theta convolution term' in page],
    }
    if edition in ('v6', 'v7', 'v8', 'v9', 'v12'):
        quartic = unique_heading(pages, 'The shared-point quartic in 962 variables')
        degree = unique_heading(pages, 'Why a single defining polynomial must have degree at least four')
        gaussian = unique_heading(pages, 'Gaussian ray weights and their progression main terms')
        if not source < quartic < degree < dependency < appendix < gaussian <= last:
            raise ValueError('Version 6 section order differs from the review profile')
        groups['quartic_962'] = list(range(quartic, degree + 1))
        groups['degree_lower_bound'] = list(range(degree, dependency + 1))
        groups['gaussian_analytic_replacement'] = list(range(gaussian, last + 1))
    selected = sorted({i for group in groups.values() for i in group})
    return selected, groups


def explicit_selection(value, count):
    selected = set()
    for item in value.split(','):
        item = item.strip()
        match = re.fullmatch(r'(\d+)(?:-(\d+))?', item)
        if not match:
            raise ValueError('Page selection must look like 1,140-155,212-249')
        first = int(match[1]); last = int(match[2] or match[1])
        if not 1 <= first <= last <= count:
            raise ValueError(f'Page selection {item!r} is outside this {count}-page PDF')
        selected.update(range(first - 1, last))
    return sorted(selected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', type=Path, help='Defaults to the manuscript for the selected edition, including archived versions')
    parser.add_argument('--edition', choices=['v5', 'v6', 'v7', 'v8', 'v9', 'v12', 'v13', 'v14'], default='v13')
    parser.add_argument('--expected-pages', type=int, help='Reject a PDF with a different page count')
    parser.add_argument('--out', type=Path, default=ROOT / 'build/pdf-review')
    parser.add_argument('--pages', help='Render these one-based pages/ranges instead of automatic section selection')
    parser.add_argument('--select-only', action='store_true', help='Check and record selection without rendering images')
    parser.add_argument('--pypdf', action='store_true', help='Extract text with optional pypdf instead of pdftotext')
    parser.add_argument('--pdftotext', default='pdftotext', help='Poppler text extractor executable')
    parser.add_argument('--pdftoppm', default='pdftoppm', help='Poppler renderer executable')
    parser.add_argument('--dpi', type=int, default=105)
    args = parser.parse_args()
    if args.dpi <= 0:
        parser.error('--dpi must be positive')
    pdf = (args.pdf or ROOT / ('manuscripts/quartic_v14.pdf' if args.edition == 'v14' else 'manuscripts/quartic_v13.pdf' if args.edition == 'v13' else 'manuscripts/quartic_v12.pdf' if args.edition == 'v12' else 'manuscripts/quartic_v9.pdf' if args.edition == 'v9' else 'manuscripts/archive/quartic_v8.pdf' if args.edition == 'v8' else 'manuscripts/archive/quartic_v7.pdf' if args.edition == 'v7' else 'quartic_962.pdf' if args.edition == 'v6' else 'manuscripts/archive/quartic_1272.pdf')).resolve()
    out = args.out.resolve(); out.mkdir(parents=True, exist_ok=True)
    if args.pypdf:
        from pypdf import PdfReader
        page_text = [page.extract_text() or '' for page in PdfReader(pdf).pages]
        (out / 'paper.txt').write_text('\f'.join(page_text), encoding='utf-8', newline='\n')
    else:
        subprocess.run([args.pdftotext, '-layout', str(pdf), str(out / 'paper.txt')], check=True)
        page_text = (out / 'paper.txt').read_text(encoding='utf-8').split('\f')
        if page_text and not page_text[-1].strip():
            page_text.pop()  # pdftotext terminates the last actual page with a form feed.
    if not page_text or (args.expected_pages is not None and len(page_text) != args.expected_pages):
        raise ValueError(f'Expected {args.expected_pages} pages; found {len(page_text)}')
    normalized = [re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text)) for text in page_text]
    if args.pages:
        selected = explicit_selection(args.pages, len(page_text)); groups = {'explicit': selected}
    else:
        selected, groups = automatic_selection(normalized, args.edition)
    rendered = []
    if not args.select_only:
        for index in selected:
            subprocess.run([args.pdftoppm, '-png', '-r', str(args.dpi), '-singlefile',
                            '-f', str(index + 1), '-l', str(index + 1), str(pdf),
                            str(out / f'page-{index + 1:03}')], check=True)
            rendered.append(index + 1)
    report = {'edition': args.edition, 'pages': len(page_text),
              'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
              'selection_method': 'explicit' if args.pages else 'body headings',
              'section_pages': {name: [i + 1 for i in indices] for name, indices in groups.items()},
              'selected_pages': [i + 1 for i in selected], 'rendered_pages': rendered,
              'visual_inspection': 'PENDING'}
    (out / 'rendered.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
