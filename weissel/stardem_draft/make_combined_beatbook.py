#!/usr/bin/env python3
"""
Combine sport prototype Markdown files into a single beat book Markdown.

Usage:
  python3 make_combined_beatbook.py \
    -i weissel/stardem_draft/combined \
    -o weissel/stardem_draft/Eastern_Shore_Sports_Beat_Book.md \
    -t "Eastern Shore Sports Beat Book" \
    --author "Your Name"

What it does:
- Reads all `*.md` files from the input directory (default: `weissel/stardem_draft/combined`).
- Extracts a sensible section title (first H1 or H2 heading or filename fallback).
- Builds a Table of Contents (GitHub-style anchors).
- Concatenates sections in a deterministic order (alphabetical by default or custom order).
- Writes a single Markdown output file with a title page, TOC, and all sections.

This script uses only the standard library.
"""

from pathlib import Path
import re
import argparse
import datetime
import sys


def slugify(text: str) -> str:
    """Create a GitHub-style anchor from heading text."""
    text = text.strip().lower()
    # remove backticks and angle brackets
    text = re.sub(r'[`<>]', '', text)
    # replace non-alphanumeric with hyphens
    text = re.sub(r"[^a-z0-9\s-]", '', text)
    text = re.sub(r"\s+", '-', text)
    text = re.sub(r"-+", '-', text)
    text = text.strip('-')
    return text


def extract_title_and_body(md_text: str, fallback: str) -> (str, str):
    """Return (title, body). Title is first H1/H2 (strip #s). If none, use fallback."""
    for line in md_text.splitlines():
        m = re.match(r'^(#{1,2})\s*(.+?)\s*$', line)
        if m:
            title = m.group(2).strip()
            # remove the first heading line from body to avoid duplicate H1s
            body = md_text.replace(line + '\n', '', 1)
            return title, body
    # fallback to filename-like string
    return fallback, md_text


def read_md_files(input_dir: Path, pattern: str = 'prototype_*.md'):
    files = sorted(input_dir.glob(pattern))
    sections = []
    for p in files:
        text = p.read_text(encoding='utf-8')
        # derive fallback title from filename
        fallback = p.stem.replace('prototype_', '').replace('_', ' ').title()
        title, body = extract_title_and_body(text, fallback)
        sections.append({'path': p, 'title': title, 'body': body})
    return sections


def build_toc(sections):
    toc_lines = []
    for s in sections:
        anchor = slugify(s['title'])
        toc_lines.append(f"- [{s['title']}](#{anchor})")
        s['anchor'] = anchor
    return '\n'.join(toc_lines)


def ensure_heading(section):
    """Return a section string that starts with an H2 using the title (so TOC links match)."""
    title = section['title']
    body = section['body'].lstrip('\n')
    # If body already starts with the same heading, keep as-is
    first_line = body.splitlines()[0] if body.strip() else ''
    if re.match(rf'^(#{{1,6}}\s*{re.escape(title)}\s*$)', first_line, flags=re.I):
        return body
    else:
        return f"## {title}\n\n" + body


def combine(sections, title, author=None, date=None, intro=None):
    date = date or datetime.date.today().isoformat()
    header_lines = [f"# {title}"]
    if author:
        header_lines.append(f"**Author:** {author}")
    header_lines.append(f"**Generated:** {date}")
    header = '\n\n'.join(header_lines) + '\n\n---\n\n'

    toc = build_toc(sections)
    intro_text = intro or 'This consolidated beat book combines sport‑specific prototypes into a single reference for reporters covering the Eastern Shore.'

    output_parts = [header, '## Table of Contents\n\n' + toc + '\n\n---\n\n', intro_text + '\n\n---\n\n']

    for s in sections:
        section_md = ensure_heading(s)
        # Add an anchor explicitly to be safe for title duplicates
        anchor = s.get('anchor', slugify(s['title']))
        output_parts.append(f"<a name=\"{anchor}\"></a>\n\n" + section_md + '\n\n---\n\n')

    return '\n'.join(output_parts)


def main(argv=None):
    parser = argparse.ArgumentParser(description='Combine sport prototype .md files into a single beat book')
    parser.add_argument('-i', '--input-dir', default='weissel/stardem_draft/combined', help='Directory containing prototype_*.md files')
    parser.add_argument('-o', '--output', default='weissel/stardem_draft/Eastern_Shore_Sports_Beat_Book.md', help='Output Markdown file')
    parser.add_argument('-t', '--title', default='Eastern Shore Sports Beat Book', help='Title for the beat book')
    parser.add_argument('--author', default=None, help='Author name to put on title page')
    parser.add_argument('--pattern', default='prototype_*.md', help='Glob pattern to match input files')
    parser.add_argument('--order', nargs='*', default=None, help='Optional ordering of sport names (case-insensitive); any files not listed will be appended alphabetically')
    parser.add_argument('--intro', default=None, help='Optional short intro paragraph')

    args = parser.parse_args(argv)
    input_dir = Path(args.input_dir)

    if not input_dir.exists():
        print(f"Input directory does not exist: {input_dir}", file=sys.stderr)
        sys.exit(2)

    sections = read_md_files(input_dir, pattern=args.pattern)

    if args.order:
        # reorder sections according to provided order list (case-insensitive match to title or filename fallback)
        order_map = [o.lower() for o in args.order]
        ordered = []
        remainder = []
        for s in sections:
            key = s['title'].lower()
            if key in order_map:
                idx = order_map.index(key)
                ordered.append((idx, s))
            else:
                remainder.append(s)
        ordered.sort(key=lambda x: x[0])
        sections = [s for (_, s) in ordered] + sorted(remainder, key=lambda x: x['title'].lower())

    combined_md = combine(sections, args.title, author=args.author, intro=args.intro)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(combined_md, encoding='utf-8')
    print(f"Wrote combined beat book to: {out_path}")


if __name__ == '__main__':
    main()
