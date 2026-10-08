#!/usr/bin/env python3
"""Dependency-free documentation checks for the VCDS-ARM64 repository.

Python 3 standard library only. No network access. Exit code 0 = all checks pass.

Checks:
  1. Every relative link in Markdown resolves to an existing file/directory.
  2. Every '#fragment' on a local Markdown link matches a heading in the target file.
  3. Every http(s) link is well-formed; other schemes are flagged.
  4. Every Markdown file under docs/ is linked from README.md (index completeness).
  5. No absolute user-profile paths (e.g. C:\\Users\\..., /home/..., /Users/...) in docs.
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOC_FILES = [ROOT / 'README.md'] + sorted((ROOT / 'docs').rglob('*.md'))

LINK_RE = re.compile(r'\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
AUTOLINK_RE = re.compile(r'<((?:https?|mailto):[^>\s]+)>')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)\s*$', re.M)
SCHEME_RE = re.compile(r'^[a-zA-Z][a-zA-Z0-9+.-]*:')
URL_BLANK_RE = re.compile(r'https?://\S+')
BAD_PATH_RE = re.compile(r'[A-Za-z]:\\Users\\|[A-Za-z]:/Users/|/home/[A-Za-z]|/Users/[A-Za-z]')


def slugify(text):
    """Approximate GitHub heading slugs: lowercase, drop punctuation, spaces -> hyphens."""
    text = text.strip().lower()
    text = re.sub(r'[^\w\- ]', '', text, flags=re.UNICODE)
    return text.replace(' ', '-')


def heading_slugs(text):
    seen = {}
    slugs = set()
    for match in HEADING_RE.finditer(text):
        base = slugify(re.sub(r'\s*#+\s*$', '', match.group(2)))
        if not base:
            continue
        count = seen.get(base, 0)
        seen[base] = count + 1
        slugs.add(base if count == 0 else '{}-{}'.format(base, count))
    return slugs


def iter_content_lines(text):
    """Yield (line number, line) skipping fenced code blocks."""
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield lineno, line


def find_targets(line):
    for match in LINK_RE.finditer(line):
        yield match.group(1)
    for match in AUTOLINK_RE.finditer(line):
        yield match.group(1)


def line_of(text, index):
    return text.count('\n', 0, index) + 1


def check_link(relfile, lineno, target, errors, counts):
    target = target.strip()
    if target.startswith('<') and target.endswith('>'):
        target = target[1:-1]
    if target.startswith('mailto:'):
        return
    if SCHEME_RE.match(target):
        if target.startswith(('http://', 'https://')):
            counts['external'] += 1
        else:
            errors.append('{}:{}: unsupported link scheme: {}'.format(relfile, lineno, target))
        return
    if ' ' in target:
        errors.append('{}:{}: raw space in link target: {}'.format(relfile, lineno, target))
        return
    counts['relative'] += 1
    path_part, _, fragment = target.partition('#')
    source = (ROOT / relfile)
    resolved = (source.parent / unquote(path_part)).resolve() if path_part else source
    if not path_part:
        resolved = source
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        errors.append('{}:{}: relative link escapes the repository: {}'.format(relfile, lineno, target))
        return
    if not resolved.exists():
        errors.append('{}:{}: broken relative link: {}'.format(relfile, lineno, target))
        return
    if fragment and resolved.suffix.lower() == '.md':
        slugs = heading_slugs(resolved.read_text(encoding='utf-8'))
        if fragment.lower() not in slugs:
            errors.append('{}:{}: missing heading #{} in {}'.format(relfile, lineno, fragment, path_part))


def check_private_paths(relfile, text, errors):
    masked = URL_BLANK_RE.sub(lambda m: ' ' * len(m.group()), text)
    for match in BAD_PATH_RE.finditer(masked):
        errors.append('{}:{}: absolute user-profile path: {}'.format(
            relfile, line_of(masked, match.start()), match.group(0)))


def check_index(readme_text, errors):
    linked = set()
    for _, line in iter_content_lines(readme_text):
        for target in find_targets(line):
            if SCHEME_RE.match(target) or target.startswith(('mailto:', '<')):
                continue
            path_part = target.split('#')[0]
            if not path_part:
                continue
            resolved = (ROOT / unquote(path_part)).resolve()
            try:
                linked.add(resolved.relative_to(ROOT).as_posix())
            except ValueError:
                continue
    for doc in DOC_FILES[1:]:
        rel = doc.relative_to(ROOT).as_posix()
        if rel not in linked:
            errors.append('README.md: docs file missing from the README index: {}'.format(rel))


def main():
    errors = []
    counts = {'external': 0, 'relative': 0}
    for file in DOC_FILES:
        relfile = file.relative_to(ROOT).as_posix()
        text = file.read_text(encoding='utf-8')
        for lineno, line in iter_content_lines(text):
            for target in find_targets(line):
                check_link(relfile, lineno, target, errors, counts)
        check_private_paths(relfile, text, errors)
    check_index((ROOT / 'README.md').read_text(encoding='utf-8'), errors)

    print('checked {} Markdown files: {} relative links, {} external links'.format(
        len(DOC_FILES), counts['relative'], counts['external']))
    if errors:
        print('FAILED:')
        for error in errors:
            print('  ' + error)
        return 1
    print('OK: all documentation checks passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
