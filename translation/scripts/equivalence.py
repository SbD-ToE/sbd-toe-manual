#!/usr/bin/env python3
"""Extraction-equivalence test between a source page and its translation.

For every translated file present in the target-locale mirror, the structural
fingerprint (``fingerprint.py``) of the source page is compared with that of
the translation. Any divergence outside natural-language text (front matter
identity, heading tree, tables, code blocks, admonitions, lists, internal
links, images, protected tokens, MDX statements) is reported with the
dimension, the expected and the obtained value and, when possible, the line.

This is *the* acceptance criterion for a translated page (README rule 7).

Usage::

    python translation/scripts/equivalence.py --all
    python translation/scripts/equivalence.py --path 010-sbd-manual/00-fundamentos
    python translation/scripts/equivalence.py --path 010-sbd-manual/00-fundamentos/index.md

Exit status: 0 when every checked pair is equivalent (or when ``--all`` finds
no translated file yet, which is reported as a warning), 1 when at least one
divergence was found, 2 on usage or I/O errors.
"""

from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

import common  # noqa: E402
import fingerprint as fingerprint_mod  # noqa: E402

Divergence = Dict[str, object]


def _div(dimension: str, expected, actual, *, line_source: Optional[int] = None, line_target: Optional[int] = None, detail: str = "") -> Divergence:
    return {
        "dimension": dimension,
        "expected": expected,
        "actual": actual,
        "line_source": line_source,
        "line_target": line_target,
        "detail": detail,
    }


def _compare_sequences(dimension: str, src: Sequence[dict], tgt: Sequence[dict], key, fields: Sequence[str], describe) -> List[Divergence]:
    """Compare two ordered sequences of structural items.

    When the counts differ, the missing/extra items are located with a diff on
    ``key``; when they match, items are compared pairwise on ``fields``.
    """
    out: List[Divergence] = []
    if len(src) != len(tgt):
        out.append(_div(f"{dimension}.count", len(src), len(tgt)))
        matcher = difflib.SequenceMatcher(a=[key(x) for x in src], b=[key(x) for x in tgt], autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            for item in src[i1:i2]:
                out.append(_div(f"{dimension}.missing", describe(item), None, line_source=item.get("line")))
            for item in tgt[j1:j2]:
                out.append(_div(f"{dimension}.extra", None, describe(item), line_target=item.get("line")))
        return out
    for s_item, t_item in zip(src, tgt):
        for field in fields:
            if s_item.get(field) != t_item.get(field):
                out.append(
                    _div(
                        f"{dimension}.{field}",
                        s_item.get(field),
                        t_item.get(field),
                        line_source=s_item.get("line"),
                        line_target=t_item.get("line"),
                        detail=describe(s_item),
                    )
                )
    return out


def _compare_multisets(dimension: str, src: Dict[str, List[int]], tgt: Dict[str, List[int]]) -> List[Divergence]:
    out: List[Divergence] = []
    for key in sorted(set(src) | set(tgt)):
        s_lines = src.get(key, [])
        t_lines = tgt.get(key, [])
        if len(s_lines) != len(t_lines):
            out.append(
                _div(
                    dimension,
                    len(s_lines),
                    len(t_lines),
                    line_source=s_lines[0] if s_lines else None,
                    line_target=t_lines[0] if t_lines else None,
                    detail=key,
                )
            )
    return out


def _compare_headings(src: List[dict], tgt: List[dict]) -> List[Divergence]:
    out: List[Divergence] = []

    def key(h: dict) -> Tuple[int, str]:
        return (h["level"], h["id"] if h["explicit"] else "*")

    def describe(h: dict) -> str:
        return f"{'#' * h['level']} #{h['id']}{'' if h['explicit'] else ' (derived)'}"

    if len(src) != len(tgt):
        out.append(_div("headings.count", len(src), len(tgt)))
        matcher = difflib.SequenceMatcher(a=[key(h) for h in src], b=[key(h) for h in tgt], autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            for h in src[i1:i2]:
                out.append(_div("headings.missing", describe(h), None, line_source=h["line"]))
            for h in tgt[j1:j2]:
                out.append(_div("headings.extra", None, describe(h), line_target=h["line"]))
        return out
    for s_h, t_h in zip(src, tgt):
        if s_h["level"] != t_h["level"]:
            out.append(_div("headings.level", s_h["level"], t_h["level"], line_source=s_h["line"], line_target=t_h["line"], detail=describe(s_h)))
        if s_h["explicit"]:
            if not t_h["explicit"] or s_h["id"] != t_h["id"]:
                out.append(_div("headings.id", s_h["id"], t_h["id"] if t_h["explicit"] else f"{t_h['id']} (derived)", line_source=s_h["line"], line_target=t_h["line"]))
        elif t_h["explicit"] and t_h["id"] != s_h["id"]:
            # A translation may pin the source's derived anchor explicitly, but not a different one.
            out.append(_div("headings.id", f"{s_h['id']} (derived)", t_h["id"], line_source=s_h["line"], line_target=t_h["line"]))
        # Both derived: the id depends on the language and is not compared.
    return out


def _compare_frontmatter(src: dict, tgt: dict) -> List[Divergence]:
    out: List[Divergence] = []
    if src["id"] != tgt["id"]:
        out.append(_div("frontmatter.id", src["id"], tgt["id"]))
    if src["present"]:
        if src["sidebar_position"] != tgt["sidebar_position"]:
            out.append(_div("frontmatter.sidebar_position", src["sidebar_position"], tgt["sidebar_position"]))
        s_keys, t_keys = set(src["keys"]), set(tgt["keys"])
        if s_keys != t_keys:
            out.append(_div("frontmatter.keys", sorted(s_keys), sorted(t_keys), detail=f"missing={sorted(s_keys - t_keys)} extra={sorted(t_keys - s_keys)}"))
    else:
        # A source without front matter gets a minimal one in the mirror (README):
        # only `id` (plus the translation block, ignored by the fingerprint).
        extra = set(tgt["keys"]) - {"id"}
        if extra:
            out.append(_div("frontmatter.keys", ["id"], sorted(tgt["keys"]), detail="source has no front matter; only a minimal `id` is allowed"))
    return out


def compare_fingerprints(src: dict, tgt: dict) -> List[Divergence]:
    """All divergences between two fingerprints (empty list = equivalent)."""
    out: List[Divergence] = []
    out.extend(_compare_frontmatter(src["frontmatter"], tgt["frontmatter"]))
    out.extend(_compare_headings(src["headings"], tgt["headings"]))
    out.extend(
        _compare_sequences(
            "tables",
            src["tables"],
            tgt["tables"],
            key=lambda t: (t["columns"], t["rows"], tuple(t["alignments"])),
            fields=("columns", "header_cells", "rows", "alignments", "ragged_rows"),
            describe=lambda t: f"table {t['columns']}x{t['rows']} align={','.join(t['alignments'])}",
        )
    )
    out.extend(
        _compare_sequences(
            "code_blocks",
            src["code_blocks"],
            tgt["code_blocks"],
            key=lambda c: (c["lang"], c["sha256"]),
            fields=("lang", "sha256"),
            describe=lambda c: f"code lang={c['lang'] or '-'} sha256={c['sha256'][:12]}",
        )
    )
    out.extend(
        _compare_sequences(
            "admonitions",
            src["admonitions"],
            tgt["admonitions"],
            key=lambda a: a["type"],
            fields=("type",),
            describe=lambda a: f":::{a['type']}",
        )
    )
    out.extend(
        _compare_sequences(
            "lists",
            src["lists"],
            tgt["lists"],
            key=lambda l: (l["ordered"], l["items"], l["total_items"]),
            fields=("ordered", "items", "total_items", "max_depth"),
            describe=lambda l: f"list {'ordered' if l['ordered'] else 'unordered'} items={l['items']} total={l['total_items']}",
        )
    )
    out.extend(_compare_multisets("internal_links", src["internal_links"], tgt["internal_links"]))
    out.extend(_compare_multisets("images", src["images"], tgt["images"]))
    out.extend(_compare_multisets("protected_tokens", src["protected_tokens"], tgt["protected_tokens"]))
    if src["esm"] != tgt["esm"]:
        out.append(_div("esm", src["esm"], tgt["esm"]))
    if src["html_comments"] != tgt["html_comments"]:
        out.append(_div("html_comments", src["html_comments"], tgt["html_comments"]))
    return out


def compare_files(source: Path, target: Path, rel_path: str, *, slugger_mode: str = "runtime") -> List[Divergence]:
    src_fp = fingerprint_mod.fingerprint_file(source, rel_path, slugger_mode=slugger_mode)
    tgt_fp = fingerprint_mod.fingerprint_file(target, rel_path, slugger_mode=slugger_mode)
    return compare_fingerprints(src_fp, tgt_fp)


def format_divergence(d: Divergence) -> str:
    where = []
    if d.get("line_source") is not None:
        where.append(f"source L{d['line_source']}")
    if d.get("line_target") is not None:
        where.append(f"target L{d['line_target']}")
    loc = f" [{', '.join(where)}]" if where else ""
    detail = f" — {d['detail']}" if d.get("detail") else ""
    return f"    {d['dimension']}{loc}: expected {d['expected']!r}, got {d['actual']!r}{detail}"


def select_pairs(docs_dir: Path, i18n_dir: Path, target_locale: str, path_arg: Optional[str], all_files: bool) -> Tuple[List[Tuple[str, Path, Path]], List[str]]:
    """Return ([(rel, source, target)], orphans) for the files to compare."""
    corpus = common.iter_corpus(docs_dir)
    if path_arg is not None:
        selected_path = common.resolve_corpus_path(path_arg, docs_dir)
        prefix = common.rel_to_docs(selected_path, docs_dir)
        if selected_path.is_dir():
            corpus = [rel for rel in corpus if rel == prefix or rel.startswith(prefix.rstrip("/") + "/")]
        else:
            corpus = [rel for rel in corpus if rel == prefix]
    elif not all_files:
        raise common.TranslationToolError("nothing selected: pass --all or --path <file-or-dir>")
    pairs = []
    for rel in corpus:
        target = common.mirror_path(rel, i18n_dir, target_locale)
        if target.is_file():
            pairs.append((rel, common.source_path(rel, docs_dir), target))
    orphans: List[str] = []
    if all_files:
        source_set = set(common.iter_corpus(docs_dir))
        orphans = [rel for rel in common.iter_mirror(i18n_dir, target_locale) if rel not in source_set]
    return pairs, orphans


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source-locale", default=common.DEFAULT_SOURCE_LOCALE)
    parser.add_argument("--target-locale", default=common.DEFAULT_TARGET_LOCALE)
    parser.add_argument("--docs-dir", type=Path, default=None, help="source corpus root (default: <repo>/manuals_src/docs/sbd-toe)")
    parser.add_argument("--i18n-dir", type=Path, default=None, help="i18n root (default: <repo>/manuals_src/i18n)")
    parser.add_argument("--path", default=None, help="file or directory, relative to --docs-dir")
    parser.add_argument("--all", action="store_true", help="every translated file in the mirror")
    parser.add_argument("--slugger", choices=("runtime", "cli"), default="runtime")
    parser.add_argument("--json", action="store_true", help="machine-readable report on stdout")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = common.repo_root()
        docs_dir = args.docs_dir or common.default_docs_dir(root)
        i18n_dir = args.i18n_dir or common.default_i18n_dir(root)
        pairs, orphans = select_pairs(docs_dir, i18n_dir, args.target_locale, args.path, args.all)
    except common.TranslationToolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    report = {"source_locale": args.source_locale, "target_locale": args.target_locale, "files": {}, "orphans": orphans}
    failed = 0
    for rel, source, target in pairs:
        try:
            divergences = compare_files(source, target, rel, slugger_mode=args.slugger)
        except common.TranslationToolError as exc:
            divergences = [_div("error", None, str(exc))]
        report["files"][rel] = divergences
        if divergences:
            failed += 1
            if not args.json:
                print(f"FAIL {rel}")
                for d in divergences:
                    print(format_divergence(d))
        elif not args.json:
            print(f"OK   {rel}")
    for rel in orphans:
        failed += 1
        if not args.json:
            print(f"FAIL {rel}")
            print(f"    mirror.orphan: translated file has no source in {docs_dir}")

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    if not pairs and not orphans:
        common.warn(f"no translated files found in {common.mirror_dir(i18n_dir, args.target_locale)}; nothing to compare")
        return 0
    if not args.json:
        print(f"\n{len(pairs) - (failed - len(orphans))} equivalent, {failed} divergent ({args.source_locale} -> {args.target_locale})")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
