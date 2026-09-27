#!/usr/bin/env python3
"""Language-independent structural fingerprint of a Manual page.

The fingerprint captures everything that must be identical between a source
page and its translation (brief §6): front-matter identity, heading tree,
tables, code blocks, admonitions, lists, internal links, images, protected
tokens and ``i18n:pending`` markers. Natural-language text is deliberately
absent, so two pages in different languages with the same structure produce
comparable fingerprints.

Usage::

    python translation/scripts/fingerprint.py <file> [--json] [--slugger runtime|cli]

``<file>`` may be absolute, relative to the CWD, or relative to the corpus
root (``--docs-dir``, default ``manuals_src/docs/sbd-toe``).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

import common  # noqa: E402
from protected_tokens import find_protected_tokens  # noqa: E402

SCHEMA_VERSION = 1

# Front-matter keys whose presence is not part of the structural identity.
IGNORED_FRONTMATTER_KEYS = set(common.TRANSLATED_FRONTMATTER_KEYS) | {common.TRANSLATION_BLOCK_KEY}


def fingerprint_text(text: str, rel_path: str, *, slugger_mode: str = "runtime") -> Dict:
    """Fingerprint of a document given as text. ``rel_path`` is used for the
    effective id and is echoed in the output."""
    doc = common.parse_markdown(text, where=rel_path)
    common.assign_heading_ids(doc, mode=slugger_mode)
    fm = doc.frontmatter or {}

    sidebar_position = fm.get("sidebar_position")
    if not isinstance(sidebar_position, (int, float, str)) or isinstance(sidebar_position, bool):
        sidebar_position = None

    # Multisets are represented as {key: [line, line, ...]} so that divergences
    # can be located; the multiplicity is the length of the list.
    internal_links: Dict[str, List[int]] = {}
    for link in doc.links:
        if common.is_internal_link(link.dest):
            internal_links.setdefault(common.normalise_link(link.dest), []).append(link.line)
    images: Dict[str, List[int]] = {}
    for img in doc.images:
        images.setdefault(img.src.strip(), []).append(img.line)
    # Protected tokens are counted in the body prose (outside code and comments)
    # and in the translated front-matter fields, whose ids must survive too.
    token_lines: List[Tuple[int, str]] = list(doc.prose_lines)
    for key in common.TRANSLATED_FRONTMATTER_KEYS:
        value = fm.get(key)
        if isinstance(value, str):
            token_lines.append((0, value))
    protected: Dict[str, List[int]] = {}
    for lineno, line in token_lines:
        for token, count in find_protected_tokens(line).items():
            protected.setdefault(token, []).extend([lineno] * count)

    return {
        "schema": SCHEMA_VERSION,
        "path": rel_path,
        "slugger": slugger_mode,
        "frontmatter": {
            "present": doc.frontmatter_present,
            "id": common.effective_id(rel_path, doc.frontmatter),
            "sidebar_position": sidebar_position,
            "keys": sorted(k for k in fm.keys() if k not in IGNORED_FRONTMATTER_KEYS),
        },
        "headings": [
            {
                "level": h.level,
                "id": h.id,
                "explicit": h.explicit_id is not None,
                "line": h.line,
            }
            for h in doc.headings
        ],
        "tables": [
            {
                "columns": t.columns,
                "header_cells": t.header_cells,
                "rows": t.rows,
                "ragged_rows": t.ragged_rows,
                "alignments": list(t.alignments),
                "line": t.line,
            }
            for t in doc.tables
        ],
        "code_blocks": [
            {
                "lang": c.lang,
                "sha256": hashlib.sha256(common.normalise_text(c.content).encode("utf-8")).hexdigest(),
                "lines": (c.content.count("\n") + 1) if c.content else 0,
                "line": c.line,
            }
            for c in doc.code_blocks
        ],
        "admonitions": [{"type": a.type, "line": a.line} for a in doc.admonitions],
        "lists": [
            {
                "ordered": l.ordered,
                "items": l.items,
                "total_items": l.total_items,
                "max_depth": l.max_depth,
                "line": l.line,
            }
            for l in doc.lists
        ],
        "internal_links": {k: internal_links[k] for k in sorted(internal_links)},
        "images": {k: images[k] for k in sorted(images)},
        "protected_tokens": {k: protected[k] for k in sorted(protected)},
        "esm": list(doc.esm),
        "html_comments": len(doc.comments) - doc.pending_markers,
        "pending_markers": doc.pending_markers,
    }


def fingerprint_file(path: Path, rel_path: Optional[str] = None, *, slugger_mode: str = "runtime") -> Dict:
    text = common.read_text(path)
    return fingerprint_text(text, rel_path or Path(path).name, slugger_mode=slugger_mode)


def to_json(fp: Dict) -> str:
    """Deterministic JSON: sorted keys, stable indentation, UTF-8 verbatim."""
    return json.dumps(fp, indent=2, sort_keys=True, ensure_ascii=False)


def summary(fp: Dict) -> str:
    lines = [
        f"path: {fp['path']}",
        f"frontmatter: present={fp['frontmatter']['present']} id={fp['frontmatter']['id']} "
        f"sidebar_position={fp['frontmatter']['sidebar_position']} keys={','.join(fp['frontmatter']['keys'])}",
        f"headings: {len(fp['headings'])} (explicit ids: {sum(1 for h in fp['headings'] if h['explicit'])})",
    ]
    for h in fp["headings"]:
        marker = "" if h["explicit"] else " (derived)"
        lines.append(f"  L{h['line']}: {'#' * h['level']} #{h['id']}{marker}")
    lines.append(f"tables: {len(fp['tables'])}")
    for t in fp["tables"]:
        lines.append(f"  L{t['line']}: {t['columns']} cols x {t['rows']} rows, align={','.join(t['alignments'])}, ragged={t['ragged_rows']}")
    lines.append(f"code_blocks: {len(fp['code_blocks'])}")
    for c in fp["code_blocks"]:
        lines.append(f"  L{c['line']}: lang={c['lang'] or '-'} lines={c['lines']} sha256={c['sha256'][:12]}…")
    lines.append(f"admonitions: {len(fp['admonitions'])} " + " ".join(a["type"] for a in fp["admonitions"]))
    lines.append(f"lists: {len(fp['lists'])} " + " ".join(f"L{l['line']}:{l['items']}/{l['total_items']}" for l in fp["lists"]))
    lines.append(f"internal_links: {sum(len(v) for v in fp['internal_links'].values())} ({len(fp['internal_links'])} distinct)")
    lines.append(f"images: {sum(len(v) for v in fp['images'].values())}")
    lines.append(f"protected_tokens: {sum(len(v) for v in fp['protected_tokens'].values())} ({len(fp['protected_tokens'])} distinct)")
    lines.append(f"esm: {len(fp['esm'])}  html_comments: {fp['html_comments']}  pending_markers: {fp['pending_markers']}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file", help="page to fingerprint (absolute, CWD-relative, or relative to --docs-dir)")
    parser.add_argument("--json", action="store_true", help="emit the full JSON fingerprint (sorted keys)")
    parser.add_argument("--slugger", choices=("runtime", "cli"), default="runtime", help="derived-id algorithm (default: runtime)")
    parser.add_argument("--source-locale", default=common.DEFAULT_SOURCE_LOCALE, help="accepted for interface symmetry; unused here")
    parser.add_argument("--target-locale", default=common.DEFAULT_TARGET_LOCALE, help="accepted for interface symmetry; unused here")
    parser.add_argument("--docs-dir", type=Path, default=None, help="corpus root (default: <repo>/manuals_src/docs/sbd-toe)")
    parser.add_argument("--i18n-dir", type=Path, default=None, help="i18n root (default: <repo>/manuals_src/i18n)")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = common.repo_root()
        docs_dir = args.docs_dir or common.default_docs_dir(root)
        path = common.resolve_corpus_path(args.file, docs_dir)
        try:
            rel = common.rel_to_docs(path, docs_dir)
        except ValueError:
            rel = Path(path).name
        fp = fingerprint_file(path, rel, slugger_mode=args.slugger)
    except common.TranslationToolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(to_json(fp) if args.json else summary(fp))
    return 0


if __name__ == "__main__":
    sys.exit(main())
