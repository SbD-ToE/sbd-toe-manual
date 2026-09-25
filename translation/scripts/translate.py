#!/usr/bin/env python3
"""Front 6 — deterministic scaffolding around an external translation step.

``translate.py`` never calls a model. It splits the work into three
deterministic steps around a translation step performed by an external agent
or model, so that provenance and structure are reproducible whoever
translates::

    translate.py prepare  --path <file|dir relative to docs/sbd-toe> --out <jobs dir> [--only-stale] [--force]
    <external translator reads <jobs>/<path>.job.json, writes <jobs>/<path>.out.json>
    translate.py assemble --job <job> [--out-json <out>] --engine <name> [--write]
    translate.py check    --path <file|dir>

``prepare`` produces, for every eligible source file, a **job**: the file's
skeleton (the ordered sequence of segments — front matter, headings,
paragraphs, list items, table rows, admonitions, code blocks, comments, MDX
statements, blank lines), the protected tokens replaced by ``⟦Pn⟧`` markers in
the translatable text, the applicable glossary (registry entries whose
source-locale forms occur in the file) and the provenance hashes
(``source_sha256``, ``source_commit``, ``terms_sha256``, ``prompt_sha256``,
plus ``glossary_keys`` / ``glossary_sha256`` — the hash of the applied
glossary, ``common.glossary_sha256``, which is what decides ``stale-terms``).
Blocks that contain a ``pending`` term with ``blocks_translation: true`` are
marked ``translate: false`` with ``blocked_by``.

``assemble`` rebuilds the target file from the skeleton and the translations:
markers are restored (and the step fails if any marker is missing, duplicated
or unknown), blocked segments stay in the source language preceded by an
``<!-- i18n:pending key=… -->`` comment, the front matter is generated per
``translation/README.md``, the pair is checked with ``equivalence.py`` (and
the en-GB spelling lint) and nothing is written when a check fails. A source
symlink is mirrored as an identical relative symlink, never as a copy.

``check`` runs equivalence, spelling and consistency over existing target
files — the CI shortcut.

Direction is a parameter (``--source-locale`` / ``--target-locale``); nothing
here assumes PT -> EN. Only the standard library and PyYAML are used.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

import common  # noqa: E402
import equivalence  # noqa: E402
import fingerprint  # noqa: E402
import protected_tokens  # noqa: E402
import sync_state  # noqa: E402
import terms_lint  # noqa: E402

JOB_SCHEMA = 1
PROMPT_RELPATH = "translation/prompts/translate-v1.md"
MARKER_RE = re.compile(r"⟦P(\d+)⟧")  # ⟦Pn⟧
PENDING_COMMENT = "<!-- i18n:pending key={keys} -->"

KINDS = (
    "frontmatter", "heading", "paragraph", "list_item", "table_row", "admonition_open", "admonition_close",
    "code_block", "html_comment", "esm", "blank", "raw",
)
# Sync states that make a source file eligible for (re)translation.
ELIGIBLE_DEFAULT = ("untranslated", sync_state.STATE_SOURCE_AHEAD, "stale-terms")
ELIGIBLE_STALE = (sync_state.STATE_SOURCE_AHEAD, "stale-terms")

PROTECTED_KINDS = ("code_span", "html_comment", "link_dest", "ref_link", "html_tag", "url", "id", "acronym", "dnt", "line_break")


class TranslateError(common.TranslationToolError):
    """Raised on a job/assembly problem (reported, never traced)."""


def marker(n: int) -> str:
    return f"⟦P{n}⟧"


# --------------------------------------------------------------------------- #
# Protected spans inside a line of translatable text
# --------------------------------------------------------------------------- #

_INLINE_COMMENT_RE = re.compile(r"<!--.*?-->")
_REF_LINK_RE = re.compile(r"(?<=\])\[[^\]]*\]")
_HTML_TAG_RE = re.compile(r"</?[A-Za-z][^>]*>|<[A-Za-z][A-Za-z0-9+.-]*:[^>\s]*>")
_URL_RE = re.compile(r"(?:https?://|www\.)[^\s<>\]\)]+")
_URL_TRAIL = ".,;:!?'\""
_LETTER_RE = re.compile(r"[^\W\d_]")
_WORD_RE = re.compile(r"\S*[^\W\d_]\S*")
_THEMATIC_BREAK_RE = re.compile(r"^ {0,3}([-*_])(?:[ \t]*\1){2,}[ \t]*$")
_QUOTE_PREFIX_RE = re.compile(r"^[ \t]*(?:>[ \t]?)*")
_STYLE_OPEN_RE = re.compile(r"^\s*<(style|script)\b", re.I)
_STYLE_CLOSE_RE = re.compile(r"</(style|script)\s*>\s*$", re.I)


def dnt_pattern(registry: Optional[dict], target_locale: str) -> Optional[re.Pattern]:
    """Case-sensitive whole-word alternation of every ``do-not-translate``
    target-locale form of the registry (names, not patterns — README)."""
    forms: List[str] = []
    for entry in (registry or {}).get("terms", []):
        if isinstance(entry, dict) and entry.get("state") == "do-not-translate":
            forms.extend(terms_lint._forms(entry, target_locale))
    return terms_lint._word_regex(forms, ignore_case=False)


def protected_spans(text: str, dnt: Optional[re.Pattern]) -> List[Tuple[int, int, str]]:
    """Non-overlapping ``(start, end, kind)`` spans to protect in ``text``, in
    order of appearance. Families are tried in priority order; a span is kept
    only when it does not overlap one already accepted."""
    accepted: List[Tuple[int, int, str]] = []

    def free(start: int, end: int) -> bool:
        return all(end <= s or start >= e for s, e, _ in accepted)

    def add(pattern: re.Pattern, kind: str, span_of=None) -> None:
        for match in pattern.finditer(text):
            start, end = span_of(match) if span_of else match.span()
            if end > start and free(start, end):
                accepted.append((start, end, kind))

    def link_dest_span(match: re.Match) -> Tuple[int, int]:
        # Protect what sits between "](" and ")" — destination and title.
        whole = match.group(0)
        open_ = whole.rfind("](", 0, len(whole))
        # The link text may itself contain "](": take the last "](" before the dest group.
        dest_start = match.start("dest") if match.group("dest") is not None else None
        if dest_start is not None:
            open_ = text.rfind("](", match.start(), dest_start) - match.start()
        return match.start() + open_ + 2, match.end() - 1

    def url_span(match: re.Match) -> Tuple[int, int]:
        start, end = match.span()
        while end > start and text[end - 1] in _URL_TRAIL:
            end -= 1
        return start, end

    add(common._CODE_SPAN_RE, "code_span")
    add(_INLINE_COMMENT_RE, "html_comment")
    add(common._INLINE_LINK_RE, "link_dest", link_dest_span)
    add(_REF_LINK_RE, "ref_link")
    add(_HTML_TAG_RE, "html_tag")
    add(_URL_RE, "url", url_span)
    add(protected_tokens.ID_PATTERN, "id")
    add(protected_tokens.ACRONYM_PATTERN, "acronym")
    if dnt is not None:
        add(dnt, "dnt")
    return sorted(accepted)


# --------------------------------------------------------------------------- #
# Units and segments
# --------------------------------------------------------------------------- #


@dataclass
class Unit:
    """A translatable unit: a segment's text, a table cell or a front-matter field."""

    id: str
    text: str = ""  # with ⟦Pn⟧ markers
    protected: List[dict] = field(default_factory=list)
    translate: bool = True
    blocked_by: List[str] = field(default_factory=list)
    reason: Optional[str] = None  # why translate is false when not blocked
    _parts: List[Tuple[str, str, str]] = field(default_factory=list, repr=False)  # (kind, text, pkind)

    def add_text(self, piece: str, dnt: Optional[re.Pattern]) -> None:
        cursor = 0
        for start, end, kind in protected_spans(piece, dnt):
            if start > cursor:
                self._parts.append(("text", piece[cursor:start], ""))
            self._parts.append(("protected", piece[start:end], kind))
            cursor = end
        if cursor < len(piece):
            self._parts.append(("text", piece[cursor:], ""))

    def add_protected(self, original: str, kind: str) -> None:
        self._parts.append(("protected", original, kind))

    def finish(self) -> None:
        out: List[str] = []
        self.protected = []
        for kind, piece, pkind in self._parts:
            if kind == "text":
                out.append(piece)
            else:
                m = marker(len(self.protected))
                self.protected.append({"marker": m, "kind": pkind, "text": piece})
                out.append(m)
        self.text = "".join(out)
        if not _LETTER_RE.search(MARKER_RE.sub(" ", self.text)):
            self.translate = False
            self.reason = "no-prose"

    def source_text(self) -> str:
        return restore(self.text, self.protected)

    def haystack(self) -> str:
        """The unit's prose with protected tokens blanked (what the pending detector sees)."""
        return common.nfc(MARKER_RE.sub(" ", self.text))

    def to_json(self) -> dict:
        data = {"id": self.id, "translate": self.translate, "text": self.text, "protected": self.protected, "blocked_by": self.blocked_by}
        if self.reason:
            data["reason"] = self.reason
        return data


@dataclass
class Segment:
    id: str
    kind: str
    line: int
    raw: str  # verbatim source lines joined with "\n"
    prefix: str = ""
    suffix: str = ""
    unit: Optional[Unit] = None
    cells: List[Unit] = field(default_factory=list)  # table_row
    fields: List[dict] = field(default_factory=list)  # frontmatter: [{unit, key, index, quoted}]
    table: Optional[int] = None  # table_row: table index
    row: Optional[str] = None  # header · delimiter · body
    indent: Optional[int] = None  # list_item: marker column
    first_item: Optional[bool] = None  # list_item: first item of its list
    depth: Optional[int] = None  # list_item

    def to_json(self) -> dict:
        data: dict = {"id": self.id, "kind": self.kind, "line": self.line, "raw": self.raw}
        if self.unit is not None:
            data.update(self.unit.to_json())
            data["id"] = self.id
            data["prefix"] = self.prefix
            data["suffix"] = self.suffix
        else:
            data["translate"] = any(c.translate for c in self.cells) or any(f["unit"].translate for f in self.fields)
        if self.kind == "table_row":
            data["table"] = self.table
            data["row"] = self.row
            data["cells"] = [dict(c.to_json(), start=c_start, end=c_end) for c, (c_start, c_end) in zip(self.cells, self._cell_spans)]
        if self.kind == "frontmatter":
            data["fields"] = [dict(f["unit"].to_json(), key=f["key"], index=f["index"], quoted=f["quoted"]) for f in self.fields]
        if self.kind == "list_item":
            data["indent"] = self.indent
            data["first_item"] = self.first_item
            data["depth"] = self.depth
        return data

    _cell_spans: List[Tuple[int, int]] = field(default_factory=list, repr=False)


def restore(text_out: str, protected: List[dict]) -> str:
    """Put the protected originals back. Fails when a marker is missing,
    duplicated, unknown, or when the text carries a literal line break."""
    expected = [p["marker"] for p in protected]
    problems: List[str] = []
    if "\n" in text_out or "\r" in text_out:
        problems.append("literal line break in the translated text (line breaks are markers)")
    counts = {m: text_out.count(m) for m in expected}
    missing = [m for m, c in counts.items() if c == 0]
    duplicated = [m for m, c in counts.items() if c > 1]
    unknown = sorted({marker(int(n)) for n in MARKER_RE.findall(text_out)} - set(expected))
    if missing:
        problems.append("missing marker(s): " + ", ".join(missing))
    if duplicated:
        problems.append("duplicated marker(s): " + ", ".join(duplicated))
    if unknown:
        problems.append("unknown marker(s): " + ", ".join(unknown))
    if problems:
        raise TranslateError("; ".join(problems))
    originals = {p["marker"]: p["text"] for p in protected}
    return MARKER_RE.sub(lambda m: originals[m.group(0)], text_out)


# --------------------------------------------------------------------------- #
# Table cells with offsets
# --------------------------------------------------------------------------- #


def split_cells_with_spans(row: str) -> List[Tuple[int, int]]:
    """``(start, end)`` of the trimmed content of every cell of a GFM row,
    honouring ``\\|`` and pipes inside code spans (same rules as ``common._split_cells``)."""
    boundaries: List[int] = []  # positions of separating pipes
    in_code = False
    idx = 0
    while idx < len(row):
        ch = row[idx]
        if ch == "\\" and idx + 1 < len(row) and row[idx + 1] == "|":
            idx += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            boundaries.append(idx)
        idx += 1
    edges = [-1, *boundaries, len(row)]
    spans = [(edges[i] + 1, edges[i + 1]) for i in range(len(edges) - 1)]
    # Leading/trailing pipes produce empty edge cells; drop them like GFM does.
    if spans and row[spans[0][0] : spans[0][1]].strip() == "" and row.lstrip().startswith("|"):
        spans = spans[1:]
    if spans and row[spans[-1][0] : spans[-1][1]].strip() == "" and row.rstrip().endswith("|") and not row.rstrip().endswith("\\|"):
        spans = spans[:-1]
    trimmed: List[Tuple[int, int]] = []
    for start, end in spans:
        content = row[start:end]
        lead = len(content) - len(content.lstrip())
        trail = len(content) - len(content.rstrip())
        trimmed.append((start + lead, end - trail))
    return trimmed


# --------------------------------------------------------------------------- #
# Segmenter
# --------------------------------------------------------------------------- #

_FM_FIELD_RE = re.compile(r"^(?P<key>[A-Za-z_][\w-]*)\s*:\s*(?P<value>.*)$")


def _fm_value(raw_value: str) -> Tuple[Optional[str], bool]:
    """(scalar value, quoted) of a single-line front-matter value; ``None`` for block scalars."""
    stripped = raw_value.strip()
    if stripped.startswith(("|", ">")):
        return None, False
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in "\"'":
        try:
            value = common.yaml_load(stripped)
        except Exception:  # pragma: no cover - malformed quoting
            return None, False
        return (value if isinstance(value, str) else None), True
    return stripped, False


class Segmenter:
    """Line-based segmentation of a document into ordered segments, using the
    same fences/comments/blocks rules as ``common.parse_markdown``."""

    def __init__(self, text: str, rel_path: str, dnt: Optional[re.Pattern], translated_keys: Sequence[str]) -> None:
        self.text = text.replace("\r\n", "\n").replace("\r", "\n")
        if self.text.startswith("﻿"):
            self.text = self.text[1:]
        self.rel_path = rel_path
        self.dnt = dnt
        self.translated_keys = tuple(translated_keys)
        self.segments: List[Segment] = []
        self.tables = 0
        self.frontmatter_present = False
        self.frontmatter: Optional[dict] = None
        self._body_start = 1

    def _new_id(self) -> str:
        return f"s{len(self.segments) + 1:04d}"

    def _segment(self, kind: str, line: int, raw_lines: List[str], **extra) -> Segment:
        seg = Segment(id=self._new_id(), kind=kind, line=line, raw="\n".join(raw_lines), **extra)
        self.segments.append(seg)
        return seg

    def _unit(self, seg_id: str, pieces: List[Tuple[str, str]]) -> Unit:
        """``pieces``: ordered list of ("text", s) or ("break", original)."""
        unit = Unit(id=seg_id)
        for kind, piece in pieces:
            if kind == "text":
                unit.add_text(piece, self.dnt)
            else:
                unit.add_protected(piece, "line_break")
        unit.finish()
        return unit

    # -- front matter ------------------------------------------------------ #

    def _frontmatter(self) -> Tuple[List[str], int]:
        """Emit the front-matter segment; return (body lines, first body line number)."""
        fm_text, body, body_start = common.split_frontmatter(self.text)
        lines = self.text.split("\n")
        if fm_text is None:
            return lines, 1
        self.frontmatter_present = True
        self.frontmatter, _b, _s = common.parse_frontmatter(self.text, where=self.rel_path)
        fm_lines = fm_text.split("\n")
        close_index = 1 + len(fm_lines)
        raw_lines = lines[: close_index + 1]
        seg = self._segment("frontmatter", 1, raw_lines)
        for index, fm_line in enumerate(fm_lines):
            match = _FM_FIELD_RE.match(fm_line)
            if not match or match.group("key") not in self.translated_keys:
                continue
            value, quoted = _fm_value(match.group("value"))
            unit = Unit(id=f"{seg.id}.{match.group('key')}")
            if value is None:
                unit.translate = False
                unit.reason = "block-scalar"
                unit.text = ""
            else:
                unit.add_text(value, self.dnt)
                unit.finish()
            seg.fields.append({"unit": unit, "key": match.group("key"), "index": index + 1, "quoted": quoted})
        body_lines = lines[close_index + 1 :]
        if body_start == close_index + 1:  # closing line carried body text ("---foo")
            body_lines = [lines[close_index][3:], *body_lines]
        return body_lines, body_start

    # -- body -------------------------------------------------------------- #

    def run(self) -> "Segmenter":
        body_lines, body_start = self._frontmatter()
        total = len(body_lines)
        # Pass 1: classify lines — "code" (grouped), "comment" (full-line, grouped), or prose text.
        klass: List[Optional[str]] = [None] * total  # None = prose
        groups: List[Tuple[str, int, int]] = []  # (kind, start offset, end offset inclusive)
        in_fence: Optional[Tuple[str, int]] = None
        fence_start = 0
        in_comment = False
        comment_start = 0
        offset = 0
        while offset < total:
            line = body_lines[offset]
            if in_fence is not None:
                char, length = in_fence
                stripped = line.strip()
                if stripped and set(stripped) == {char} and len(stripped) >= length:
                    groups.append(("code_block", fence_start, offset))
                    in_fence = None
                offset += 1
                continue
            if in_comment:
                end = line.find("-->")
                if end >= 0:
                    remainder = line[end + 3 :]
                    if remainder.strip():
                        # The comment closes mid-line: keep the line as prose (comment becomes an inline marker).
                        groups.append(("html_comment", comment_start, offset - 1))
                        body_lines[offset] = line  # unchanged; the leading "...-->" part is protected inline
                        in_comment = False
                        klass[offset] = "prose-after-comment"
                    else:
                        groups.append(("html_comment", comment_start, offset))
                        in_comment = False
                offset += 1
                continue
            fence_match = common._FENCE_RE.match(line)
            if fence_match:
                fence = fence_match.group("fence")
                info = fence_match.group("info")
                if fence[0] == "~" or "`" not in info:
                    in_fence = (fence[0], len(fence))
                    fence_start = offset
                    offset += 1
                    continue
            work = line
            starts_comment = work.lstrip().startswith("<!--")
            first = work.find("<!--")
            if first >= 0:
                end = work.find("-->", first + 4)
                if end < 0:
                    if starts_comment:
                        in_comment = True
                        comment_start = offset
                        offset += 1
                        continue
                    # A comment opening mid-line and spanning lines: treat the rest as a comment group.
                    in_comment = True
                    comment_start = offset
                    klass[offset] = "prose-open-comment"
                    offset += 1
                    continue
                if starts_comment and not _INLINE_COMMENT_RE.sub("", work).strip():
                    groups.append(("html_comment", offset, offset))
                    klass[offset] = "comment"
                    offset += 1
                    continue
            offset += 1
        if in_fence is not None:
            groups.append(("code_block", fence_start, total - 1))
        if in_comment:
            groups.append(("html_comment", comment_start, total - 1))
        for kind, start, end in groups:
            for i in range(start, end + 1):
                if klass[i] is None or klass[i] == "comment":
                    klass[i] = kind

        # Pass 2: block structure over prose lines.
        offset = 0
        list_stack: List[int] = []  # indent columns of the open list levels
        in_list = False

        def lineno(off: int) -> int:
            return body_start + off

        def is_prose(off: int) -> bool:
            return 0 <= off < total and klass[off] in (None, "prose-after-comment", "prose-open-comment")

        def prose_break(off: int) -> bool:
            """A line that ends a paragraph/item/table (or is not prose)."""
            if not is_prose(off):
                return True
            line = body_lines[off]
            return (
                line.strip() == ""
                or common._HEADING_RE.match(line) is not None
                or common._ADMONITION_OPEN_RE.match(line) is not None
                or common._ADMONITION_CLOSE_RE.match(line) is not None
                or common._ESM_RE.match(line) is not None
            )

        def is_table_start(off: int) -> bool:
            if not is_prose(off) or not is_prose(off + 1):
                return False
            nxt = body_lines[off + 1]
            return "|" in body_lines[off] and common._TABLE_DELIM_RE.match(nxt) is not None and "-" in nxt

        while offset < total:
            line = body_lines[offset]
            start = offset
            if klass[offset] in ("code_block", "html_comment"):
                kind = klass[offset]
                while offset + 1 < total and klass[offset + 1] == kind and not any(g[1] == offset + 1 for g in groups):
                    offset += 1
                self._segment(kind, lineno(start), body_lines[start : offset + 1])
                in_list = False
                list_stack = []
                offset += 1
                continue
            if line.strip() == "":
                self._segment("blank", lineno(start), [line])
                offset += 1
                continue
            if common._ESM_RE.match(line):
                while offset + 1 < total and is_prose(offset + 1) and body_lines[offset + 1].strip() != "":
                    offset += 1
                self._segment("esm", lineno(start), body_lines[start : offset + 1])
                in_list = False
                list_stack = []
                offset += 1
                continue
            adm_open = common._ADMONITION_OPEN_RE.match(line)
            if adm_open:
                seg = self._segment("admonition_open", lineno(start), [line])
                title = adm_open.group("title") or ""
                if title.strip():
                    title_start = adm_open.start("title")
                    seg.prefix = line[:title_start]
                    seg.suffix = line[title_start + len(title.rstrip()) :]
                    seg.unit = self._unit(seg.id, [("text", title.rstrip())])
                in_list = False
                list_stack = []
                offset += 1
                continue
            if common._ADMONITION_CLOSE_RE.match(line):
                self._segment("admonition_close", lineno(start), [line])
                in_list = False
                list_stack = []
                offset += 1
                continue
            heading = common._HEADING_RE.match(line)
            if heading:
                seg = self._segment("heading", lineno(start), [line])
                content = heading.group("content") or ""
                content_start = heading.start("content") if content else len(line)
                content = common._CLOSING_HASHES_RE.sub("", content) if not content.rstrip().endswith("}") else content
                text, explicit = common.parse_heading_id(content.strip())
                if explicit is not None:
                    id_pos = line.rfind("{#")
                    if id_pos > 0 and line[id_pos - 1] == "\\":
                        id_pos -= 1
                    text_part = line[content_start:id_pos].rstrip()
                else:
                    text_part = line[content_start:].rstrip()
                    if text_part.endswith("#") and not text_part.endswith("}"):
                        text_part = common._CLOSING_HASHES_RE.sub("", text_part).rstrip()
                seg.prefix = line[:content_start]
                seg.suffix = line[content_start + len(text_part) :]
                seg.unit = self._unit(seg.id, [("text", text_part)])
                in_list = False
                list_stack = []
                offset += 1
                continue
            if is_table_start(offset):
                table_index = self.tables
                self.tables += 1
                self._table_row(lineno(offset), body_lines[offset], table_index, "header")
                self._table_row(lineno(offset + 1), body_lines[offset + 1], table_index, "delimiter")
                offset += 2
                while offset < total and not prose_break(offset):
                    self._table_row(lineno(offset), body_lines[offset], table_index, "body")
                    offset += 1
                in_list = False
                list_stack = []
                continue
            if _THEMATIC_BREAK_RE.match(line) and (offset == 0 or not is_prose(offset - 1) or body_lines[offset - 1].strip() == ""):
                self._segment("raw", lineno(start), [line])
                in_list = False
                list_stack = []
                offset += 1
                continue
            if _STYLE_OPEN_RE.match(line):
                while offset < total and not _STYLE_CLOSE_RE.search(body_lines[offset]):
                    offset += 1
                self._segment("raw", lineno(start), body_lines[start : min(offset, total - 1) + 1])
                in_list = False
                list_stack = []
                offset += 1
                continue
            if line.lstrip().startswith("{"):
                while offset + 1 < total and is_prose(offset + 1) and body_lines[offset + 1].strip() != "":
                    offset += 1
                self._segment("raw", lineno(start), body_lines[start : offset + 1])
                offset += 1
                continue
            item = common._LIST_ITEM_RE.match(line)
            if item:
                indent = len(item.group("indent").expandtabs(4))
                if not in_list:
                    list_stack = [indent]
                    first = True
                else:
                    first = False
                    if indent > list_stack[-1]:
                        list_stack.append(indent)
                        first = True
                    else:
                        while len(list_stack) > 1 and indent < list_stack[-1]:
                            list_stack.pop()
                in_list = True
                content = item.group("content") or ""
                content_start = item.start("content") if content else len(line)
                offset = self._paragraph_like("list_item", start, content_start, body_lines, klass, total, is_prose, prose_break, is_table_start, extra={"indent": indent, "first_item": first, "depth": len(list_stack)})
                continue
            # Paragraph (including block quotes and inline JSX/HTML lines).
            if in_list and not line[:1].isspace():
                in_list = False
                list_stack = []
            prefix_len = _QUOTE_PREFIX_RE.match(line).end()
            offset = self._paragraph_like("paragraph", start, prefix_len, body_lines, klass, total, is_prose, prose_break, is_table_start)
        self._self_check()
        return self

    def _paragraph_like(self, kind, start, content_start, body_lines, klass, total, is_prose, prose_break, is_table_start, extra=None) -> int:
        """Collect a paragraph / list item with its continuation lines; return the next offset."""
        offset = start
        while (
            offset + 1 < total
            and not prose_break(offset + 1)
            and not is_table_start(offset + 1)
            and common._LIST_ITEM_RE.match(body_lines[offset + 1]) is None
            and not _STYLE_OPEN_RE.match(body_lines[offset + 1])
            and not body_lines[offset + 1].lstrip().startswith("{")
        ):
            offset += 1
        raw_lines = body_lines[start : offset + 1]
        seg = self._segment(kind, self._body_start + start, raw_lines, **(extra or {}))
        first = raw_lines[0]
        seg.prefix = first[:content_start]
        pieces: List[Tuple[str, str]] = []
        content = first[content_start:]
        body_text = content.rstrip(" \t")
        trailing = content[len(body_text) :]
        pieces.append(("text", body_text))
        for nxt in raw_lines[1:]:
            nxt_prefix_len = _QUOTE_PREFIX_RE.match(nxt).end()
            nxt_content = nxt[nxt_prefix_len:]
            nxt_body = nxt_content.rstrip(" \t")
            pieces.append(("break", trailing + "\n" + nxt[:nxt_prefix_len]))
            pieces.append(("text", nxt_body))
            trailing = nxt_content[len(nxt_body) :]
        seg.suffix = trailing
        seg.unit = self._unit(seg.id, pieces)
        return offset + 1

    def _table_row(self, line_no: int, line: str, table_index: int, row: str) -> Segment:
        seg = self._segment("table_row", line_no, [line], table=table_index, row=row)
        if row == "delimiter":
            return seg
        for col, (start, end) in enumerate(split_cells_with_spans(line)):
            unit = Unit(id=f"{seg.id}.c{col}")
            unit.add_text(line[start:end], self.dnt)
            unit.finish()
            seg.cells.append(unit)
            seg._cell_spans.append((start, end))
        return seg

    def _self_check(self) -> None:
        """The segmentation must agree with the fingerprint parser on the structural counts."""
        doc = common.parse_markdown(self.text, where=self.rel_path)
        counts = {
            "headings": (len(doc.headings), sum(1 for s in self.segments if s.kind == "heading")),
            "tables": (len(doc.tables), self.tables),
            "table_rows": (sum(t.rows for t in doc.tables), sum(1 for s in self.segments if s.kind == "table_row" and s.row == "body")),
            "code_blocks": (len(doc.code_blocks), sum(1 for s in self.segments if s.kind == "code_block")),
            "admonitions": (len(doc.admonitions), sum(1 for s in self.segments if s.kind == "admonition_open")),
        }
        bad = {k: v for k, v in counts.items() if v[0] != v[1]}
        if bad:
            raise TranslateError(f"{self.rel_path}: segmenter disagrees with the fingerprint parser: " + ", ".join(f"{k} parser={v[0]} segmenter={v[1]}" for k, v in bad.items()))
        # Restoring the untranslated text must reproduce every segment verbatim.
        for seg in self.segments:
            if seg.unit is not None and seg.unit.protected is not None:
                rebuilt = seg.prefix + seg.unit.source_text() + seg.suffix
                if rebuilt != seg.raw:
                    raise TranslateError(f"{self.rel_path}: segment {seg.id} ({seg.kind}, line {seg.line}) does not round-trip: {rebuilt!r} != {seg.raw!r}")
            for cell, (start, end) in zip(seg.cells, seg._cell_spans):
                if cell.source_text() != seg.raw[start:end]:
                    raise TranslateError(f"{self.rel_path}: cell {cell.id} does not round-trip")
        reassembled = "\n".join(s.raw for s in self.segments)
        if reassembled != self.text:
            raise TranslateError(f"{self.rel_path}: segments do not reassemble the source verbatim")


def segment_document(text: str, rel_path: str, dnt: Optional[re.Pattern], translated_keys: Sequence[str] = common.TRANSLATED_FRONTMATTER_KEYS) -> Segmenter:
    seg = Segmenter(text, rel_path, dnt, translated_keys)
    fm_text, _body, body_start = common.split_frontmatter(seg.text)
    seg._body_start = body_start
    return seg.run()


# --------------------------------------------------------------------------- #
# Units, blocking and glossary
# --------------------------------------------------------------------------- #


def iter_units(segments: Iterable[Segment]) -> Iterable[Tuple[Segment, Unit]]:
    for seg in segments:
        if seg.unit is not None:
            yield seg, seg.unit
        for cell in seg.cells:
            yield seg, cell
        for f in seg.fields:
            yield seg, f["unit"]


def apply_blocking(segments: List[Segment], needles: Dict[str, re.Pattern]) -> Dict[str, int]:
    per_key: Dict[str, int] = {}
    for _seg, unit in iter_units(segments):
        if not unit.translate:
            continue
        hay = unit.haystack()
        keys = [key for key in sorted(needles) if needles[key].search(hay)]
        if keys:
            unit.blocked_by = keys
            unit.translate = False
            for key in keys:
                per_key[key] = per_key.get(key, 0) + 1
    return per_key


def build_glossary(registry: Optional[dict], segments: List[Segment], source_locale: str, target_locale: str) -> dict:
    """Registry entries applicable to the file: authoritative ``source -> target``
    pairs whose source forms occur, ``do-not-translate`` names present (in
    either language) and the ``pending`` entries that block a unit."""
    glossary = {"terms": [], "do_not_translate": [], "pending": []}
    if not registry:
        return glossary
    prose = common.nfc(" \n ".join(unit.haystack() for _s, unit in iter_units(segments)))
    raw = common.nfc(" \n ".join(unit.source_text() for _s, unit in iter_units(segments)))
    blocking = {key for _s, unit in iter_units(segments) for key in unit.blocked_by}
    for entry in registry.get("terms", []):
        if not isinstance(entry, dict):
            continue
        state = entry.get("state")
        key = str(entry.get("key"))
        src_forms = terms_lint._forms(entry, source_locale)
        tgt_forms = terms_lint._forms(entry, target_locale)
        if state in terms_lint.AUTHORITATIVE_STATES:
            pattern = terms_lint._word_regex(src_forms, ignore_case=True)
            if pattern is not None and pattern.search(prose):
                glossary["terms"].append({"key": key, "state": state, "source": entry.get(source_locale), "source_variants": list(entry.get(f"{source_locale}_variants") or []), "target": entry.get(target_locale), "target_variants": list(entry.get(f"{target_locale}_variants") or []), "sense": entry.get("sense") or ""})
        elif state == "do-not-translate":
            src_pattern = terms_lint._word_regex(src_forms, ignore_case=True)
            tgt_pattern = terms_lint._word_regex(tgt_forms, ignore_case=False)
            if (src_pattern is not None and src_pattern.search(prose)) or (tgt_pattern is not None and tgt_pattern.search(raw)):
                glossary["do_not_translate"].append({"key": key, "target": entry.get(target_locale), "target_variants": list(entry.get(f"{target_locale}_variants") or []), "source": entry.get(source_locale), "source_variants": list(entry.get(f"{source_locale}_variants") or [])})
        elif state == "pending" and key in blocking:
            glossary["pending"].append({"key": key, "source": entry.get(source_locale), "source_variants": list(entry.get(f"{source_locale}_variants") or []), "pending_reason": entry.get("pending_reason"), "owner": entry.get("owner")})
    for section in glossary.values():
        section.sort(key=lambda e: e["key"])
    return glossary


def glossary_key_list(glossary: dict) -> List[str]:
    """Sorted, unique keys of every entry in the applicable glossary (terms,
    do-not-translate and pending) — the set ``glossary_sha256`` is taken over."""
    return sorted({e["key"] for section in ("terms", "do_not_translate", "pending") for e in glossary.get(section, [])})


def word_count(text: str) -> int:
    return len(_WORD_RE.findall(MARKER_RE.sub(" ", text)))


# --------------------------------------------------------------------------- #
# Git provenance
# --------------------------------------------------------------------------- #


def git_source_commit(path: Path) -> Tuple[Optional[str], bool]:
    """(last commit touching ``path``, dirty) or (None, False) outside a repository."""
    path = Path(path)
    try:
        result = subprocess.run(["git", "log", "-n", "1", "--format=%H", "--", path.name], cwd=path.parent, capture_output=True, text=True, check=False)
        if result.returncode != 0 or not result.stdout.strip():
            return None, False
        status = subprocess.run(["git", "status", "--porcelain", "--", path.name], cwd=path.parent, capture_output=True, text=True, check=False)
        return result.stdout.strip(), bool(status.stdout.strip())
    except OSError:
        return None, False


# --------------------------------------------------------------------------- #
# prepare
# --------------------------------------------------------------------------- #


def build_job(
    *,
    text: str,
    rel: str,
    source_locale: str,
    target_locale: str,
    registry: Optional[dict],
    terms_sha256: Optional[str],
    prompt_sha256: str,
    source_commit: Optional[str],
    source_dirty: bool = False,
) -> dict:
    dnt = dnt_pattern(registry, target_locale)
    seg = segment_document(text, rel, dnt)
    needles = terms_lint.pending_needles(registry, source_locale) if registry else {}
    blocked_by_key = apply_blocking(seg.segments, needles)
    glossary = build_glossary(registry, seg.segments, source_locale, target_locale)
    glossary_keys = glossary_key_list(glossary)
    units = [unit.id for _s, unit in iter_units(seg.segments) if unit.translate]
    words = sum(word_count(unit.text) for _s, unit in iter_units(seg.segments) if unit.translate)
    markers = sum(len(unit.protected) for _s, unit in iter_units(seg.segments) if unit.translate)
    blocked_units = sum(1 for _s, unit in iter_units(seg.segments) if unit.blocked_by)
    job = {
        "schema": JOB_SCHEMA,
        "kind": "document",
        "direction": {"source_locale": source_locale, "target_locale": target_locale},
        "source_path": rel,
        "source_sha256": common.content_sha256(text),
        "source_commit": source_commit,
        "source_dirty": source_dirty,
        "terms_sha256": terms_sha256,
        "glossary_keys": glossary_keys,
        "glossary_sha256": common.glossary_sha256(registry, glossary_keys),
        "prompt_sha256": prompt_sha256,
        "prompt_path": PROMPT_RELPATH,
        "frontmatter_present": seg.frontmatter_present,
        "effective_id": common.effective_id(rel, seg.frontmatter),
        "translated_frontmatter_keys": list(common.TRANSLATED_FRONTMATTER_KEYS),
        "stats": {
            "segments": len(seg.segments),
            "translatable_units": len(units),
            "words": words,
            "protected_markers": markers,
            "blocked_units": blocked_units,
            "blocked_by_key": dict(sorted(blocked_by_key.items())),
            "glossary_terms": len(glossary["terms"]),
            "glossary_do_not_translate": len(glossary["do_not_translate"]),
            "glossary_pending": len(glossary["pending"]),
        },
        "units": units,
        "glossary": glossary,
        "segments": [s.to_json() for s in seg.segments],
    }
    return job


def symlink_job(rel: str, link_target: str, source_locale: str, target_locale: str) -> dict:
    return {
        "schema": JOB_SCHEMA,
        "kind": "symlink",
        "direction": {"source_locale": source_locale, "target_locale": target_locale},
        "source_path": rel,
        "link_target": link_target,
    }


def dump_job(job: dict) -> str:
    return json.dumps(job, indent=2, ensure_ascii=False) + "\n"


def job_path(out_dir: Path, rel: str) -> Path:
    return Path(out_dir) / (rel + ".job.json")


def out_path_for(job_file: Path) -> Path:
    name = str(job_file)
    if name.endswith(".job.json"):
        return Path(name[: -len(".job.json")] + ".out.json")
    return Path(name + ".out.json")


def select_sources(docs_dir: Path, path_arg: str) -> List[str]:
    selected = common.resolve_corpus_path(path_arg, docs_dir)
    prefix = common.rel_to_docs(selected, docs_dir)
    corpus = common.iter_corpus(docs_dir)
    if selected.is_dir():
        return [rel for rel in corpus if rel == prefix or rel.startswith(prefix.rstrip("/") + "/")]
    return [rel for rel in corpus if rel == prefix]


def cmd_prepare(args) -> int:
    root = common.repo_root()
    docs_dir = args.docs_dir or common.default_docs_dir(root)
    i18n_dir = args.i18n_dir or common.default_i18n_dir(root)
    registry_path = args.registry or (root / common.TERMS_REGISTRY_RELPATH)
    prompt_path = args.prompt or (root / PROMPT_RELPATH)
    if not prompt_path.is_file():
        raise TranslateError(f"prompt not found: {prompt_path}")
    prompt_sha = common.file_sha256(prompt_path)
    registry = terms_lint.load_registry(registry_path) if registry_path.is_file() else None
    terms_sha = terms_lint.registry_sha256(registry_path) if registry_path.is_file() else None
    if registry is None:
        common.warn(f"no terms registry at {registry_path}; glossary empty, no block is pending")
    rels = select_sources(docs_dir, args.path)
    if not rels:
        raise TranslateError(f"no source files under {args.path}")
    out_dir = Path(args.out)
    eligible_states = None if args.force else (ELIGIBLE_STALE if args.only_stale else ELIGIBLE_DEFAULT)

    summary = {"files": {}, "skipped": {}, "totals": {"files": 0, "symlinks": 0, "translatable_units": 0, "words": 0, "protected_markers": 0, "blocked_units": 0, "blocked_by_key": {}, "glossary_terms": 0, "glossary_do_not_translate": 0, "glossary_pending": 0}}
    warnings: List[str] = []
    glossary_keys: set = set()
    for rel in rels:
        source = common.source_path(rel, docs_dir)
        target = common.mirror_path(rel, i18n_dir, args.target_locale)
        if eligible_states is not None:
            entry = sync_state.file_entry(rel, source, target, terms_sha, args.source_locale, warnings, registry=registry)
            if entry["state"] not in eligible_states:
                summary["skipped"][rel] = entry["state"]
                continue
        if source.is_symlink():
            link_target = os.readlink(source)
            job = symlink_job(rel, link_target, args.source_locale, args.target_locale)
            summary["totals"]["symlinks"] += 1
            summary["files"][rel] = {"kind": "symlink", "link_target": link_target}
        else:
            text = common.read_text(source)
            commit, dirty = (args.source_commit, False) if args.source_commit else git_source_commit(source)
            if dirty:
                warnings.append(f"{rel}: uncommitted changes in the working tree; source_commit is the last commit that touched the file")
            job = build_job(text=text, rel=rel, source_locale=args.source_locale, target_locale=args.target_locale, registry=registry, terms_sha256=terms_sha, prompt_sha256=prompt_sha, source_commit=commit, source_dirty=dirty)
            if registry:
                # Cross-check the block detector of terms_lint (same registry, same text).
                _total, hits = terms_lint.pending_blocks_for_text(text, terms_lint.pending_needles(registry, args.source_locale), where=rel)
                lint_keys = {key for _b, key, _e in hits}
                job_keys = set(job["stats"]["blocked_by_key"])
                if lint_keys != job_keys:
                    warnings.append(f"{rel}: blocked keys differ from terms_lint pending-blocks (job={sorted(job_keys)}, lint={sorted(lint_keys)})")
            stats = job["stats"]
            summary["files"][rel] = {"kind": "document", **{k: stats[k] for k in ("segments", "translatable_units", "words", "protected_markers", "blocked_units", "blocked_by_key")}}
            for key in ("translatable_units", "words", "protected_markers", "blocked_units"):
                summary["totals"][key] += stats[key]
            for key, n in stats["blocked_by_key"].items():
                summary["totals"]["blocked_by_key"][key] = summary["totals"]["blocked_by_key"].get(key, 0) + n
            for section in ("terms", "do_not_translate", "pending"):
                glossary_keys.update((section, e["key"]) for e in job["glossary"][section])
        summary["totals"]["files"] += 1
        path = job_path(out_dir, rel)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(dump_job(job))
    summary["totals"]["glossary_terms"] = sum(1 for s, _k in glossary_keys if s == "terms")
    summary["totals"]["glossary_do_not_translate"] = sum(1 for s, _k in glossary_keys if s == "do_not_translate")
    summary["totals"]["glossary_pending"] = sum(1 for s, _k in glossary_keys if s == "pending")
    summary["totals"]["blocked_by_key"] = dict(sorted(summary["totals"]["blocked_by_key"].items()))
    summary["glossary_keys"] = {section: sorted(k for s, k in glossary_keys if s == section) for section in ("terms", "do_not_translate", "pending")}
    for message in warnings:
        common.warn(message)
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True))
        return 0
    for rel, info in summary["files"].items():
        if info["kind"] == "symlink":
            print(f"{rel}: symlink -> {info['link_target']}")
        else:
            blocked = f", blocked {info['blocked_units']} ({', '.join(f'{k}={v}' for k, v in info['blocked_by_key'].items())})" if info["blocked_units"] else ""
            print(f"{rel}: {info['translatable_units']} units, {info['words']} words, {info['protected_markers']} markers{blocked}")
    for rel, state in summary["skipped"].items():
        print(f"{rel}: skipped ({state})")
    t = summary["totals"]
    print()
    print(f"prepare: {t['files']} job(s) written to {out_dir} ({t['symlinks']} symlink(s)); {len(summary['skipped'])} skipped")
    print(f"  translatable units: {t['translatable_units']}   words: {t['words']}   protected markers: {t['protected_markers']}")
    print(f"  blocked units: {t['blocked_units']}" + (" — " + ", ".join(f"{k}={v}" for k, v in t["blocked_by_key"].items()) if t["blocked_by_key"] else ""))
    print(f"  glossary entries applicable: {t['glossary_terms']} terms, {t['glossary_do_not_translate']} do-not-translate, {t['glossary_pending']} pending")
    return 0


# --------------------------------------------------------------------------- #
# assemble
# --------------------------------------------------------------------------- #

_YAML_SPECIAL_START = tuple("-?:,[]{}#&*!|>'\"%@`")
_YAML_RESERVED = {"true", "false", "null", "yes", "no", "on", "off", "~", ""}


def yaml_scalar(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    needs_quotes = (
        text.strip() != text
        or text.lower() in _YAML_RESERVED
        or text.startswith(_YAML_SPECIAL_START)
        or ": " in text
        or " #" in text
        or text.endswith(":")
        or "\n" in text
        or re.fullmatch(r"[-+]?(\d[\d_]*(\.\d*)?|\.\d+)([eE][-+]?\d+)?", text) is not None
        or re.fullmatch(r"\d{4}-\d{2}-\d{2}.*", text) is not None and "T" not in text
    )
    return json.dumps(text, ensure_ascii=False) if needs_quotes else text


TRANSLATION_BLOCK_KEYS = (
    "source_locale", "source_path", "source_sha256", "source_commit", "target_sha256", "engine", "prompt_sha256",
    "terms_sha256", "glossary_keys", "glossary_sha256", "translated_at", "reviewed_by",
)


def yaml_flow_list(values) -> str:
    if values is None:
        return "null"
    return "[" + ", ".join(yaml_scalar(v) for v in values) + "]"


def translation_block_lines(meta: dict) -> List[str]:
    lines = [f"{common.TRANSLATION_BLOCK_KEY}:"]
    for key in TRANSLATION_BLOCK_KEYS:
        value = meta.get(key)
        rendered = yaml_flow_list(value) if key == "glossary_keys" else yaml_scalar(value)
        lines.append(f"  {key}: {rendered}")
    return lines


def pending_comment(keys: Iterable[str]) -> str:
    return PENDING_COMMENT.format(keys=",".join(sorted(set(keys))))


def load_translations(out_doc: dict) -> Dict[str, str]:
    segments = out_doc.get("segments")
    if not isinstance(segments, list):
        raise TranslateError("out file: expected {\"segments\": [{\"id\", \"text\"}, …]}")
    translations: Dict[str, str] = {}
    for item in segments:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not isinstance(item.get("text"), str):
            raise TranslateError(f"out file: malformed entry {item!r}")
        if item["id"] in translations:
            raise TranslateError(f"out file: duplicated id {item['id']}")
        translations[item["id"]] = item["text"]
    return translations


def _render_unit(unit: dict, translations: Dict[str, str], problems: List[str], *, cell: bool = False) -> Optional[str]:
    """Restored translated text of a unit, or ``None`` when the unit is not translated."""
    if not unit.get("translate"):
        return None
    text_out = translations.get(unit["id"])
    if text_out is None:
        problems.append(f"{unit['id']}: no translation in the out file")
        return None
    if not text_out.strip() and unit["text"].strip():
        problems.append(f"{unit['id']}: empty translation")
        return None
    try:
        restored = restore(text_out, unit["protected"])
    except TranslateError as exc:
        problems.append(f"{unit['id']}: {exc}")
        return None
    if cell:
        unescaped = re.sub(r"\\\|", "", common._CODE_SPAN_RE.sub("", restored))
        if "|" in unescaped:
            problems.append(f"{unit['id']}: unescaped '|' in a table cell")
            return None
    return restored


def assemble_text(job: dict, translations: Dict[str, str], meta: dict) -> Tuple[str, str, List[str]]:
    """Return (final text, text without the translation block, problems)."""
    problems: List[str] = []
    segments = job["segments"]
    known = set(job.get("units", []))
    extra = sorted(set(translations) - known)
    if extra:
        problems.append("out file has ids that are not translatable units: " + ", ".join(extra[:10]) + (" …" if len(extra) > 10 else ""))

    # Blocked keys per table (comment goes before the header row).
    table_keys: Dict[int, set] = {}
    for seg in segments:
        if seg["kind"] == "table_row":
            for cell in seg.get("cells", []):
                if cell["blocked_by"]:
                    table_keys.setdefault(seg["table"], set()).update(cell["blocked_by"])

    body_lines: List[str] = []
    fm_lines: List[str] = []
    fm_pending: List[str] = []
    for seg in segments:
        kind = seg["kind"]
        if kind == "frontmatter":
            lines = seg["raw"].split("\n")
            for f in seg.get("fields", []):
                rendered = _render_unit(f, translations, problems)
                if f["blocked_by"]:
                    fm_pending.extend(f["blocked_by"])
                if rendered is None:
                    continue
                lines[f["index"]] = f"{f['key']}: " + (json.dumps(rendered, ensure_ascii=False) if f["quoted"] else yaml_scalar(rendered))
            fm_lines = lines
            continue
        if kind == "table_row":
            if seg["row"] == "header" and seg["table"] in table_keys:
                body_lines.append(pending_comment(table_keys[seg["table"]]))
            row = seg["raw"]
            for cell in sorted(seg.get("cells", []), key=lambda c: -c["start"]):
                rendered = _render_unit(cell, translations, problems, cell=True)
                if rendered is not None:
                    row = row[: cell["start"]] + rendered + row[cell["end"] :]
            body_lines.append(row)
            continue
        if "text" in seg and seg.get("protected") is not None and seg["kind"] in ("heading", "paragraph", "list_item", "admonition_open"):
            if seg["blocked_by"]:
                indent = ""
                if kind == "list_item":
                    indent = " " * (0 if (seg["first_item"] and seg["depth"] == 1) else (seg["indent"] if seg["first_item"] else len(seg["prefix"])))
                elif kind == "paragraph":
                    indent = seg["prefix"][: len(seg["prefix"]) - len(seg["prefix"].lstrip(" \t"))]
                body_lines.append(indent + pending_comment(seg["blocked_by"]))
                body_lines.append(seg["raw"])
                continue
            rendered = _render_unit(seg, translations, problems)
            body_lines.append(seg["raw"] if rendered is None else seg["prefix"] + rendered + seg["suffix"])
            continue
        body_lines.append(seg["raw"])

    if fm_pending:
        body_lines.insert(0, pending_comment(fm_pending))
    if not job.get("frontmatter_present"):
        fm_lines = ["---", f"id: {yaml_scalar(job['effective_id'])}", "---"]
        if body_lines and body_lines[0].strip() != "":
            body_lines.insert(0, "")
    closing = len(fm_lines) - 1
    while closing > 0 and not common._FM_CLOSE_RE.match(fm_lines[closing]):
        closing -= 1
    without_block = "\n".join([*fm_lines, *body_lines])
    target_sha = common.content_sha256(without_block)
    meta = dict(meta, target_sha256=target_sha)
    with_block = "\n".join([*fm_lines[:closing], *translation_block_lines(meta), *fm_lines[closing:], *body_lines])
    if common.content_sha256(common.strip_translation_block(with_block)) != target_sha:
        problems.append("internal: target_sha256 does not survive strip_translation_block")
    return with_block, without_block, problems


def validate_pair(source_text: str, target_text: str, rel: str, registry: Optional[dict]) -> Tuple[List[dict], List[terms_lint.Finding]]:
    src_fp = fingerprint.fingerprint_text(source_text, rel)
    tgt_fp = fingerprint.fingerprint_text(target_text, rel)
    divergences = equivalence.compare_fingerprints(src_fp, tgt_fp)
    exemptions = terms_lint.ExemptionIndex(registry)
    findings = [f for f in terms_lint.spelling_findings_for_text(target_text, rel, exemptions, where=rel) if f.severity == "error"]
    return divergences, findings


def write_symlink(job: dict, i18n_dir: Path, target_locale: str) -> Path:
    mirror = common.mirror_dir(i18n_dir, target_locale) / Path(common.nfc(job["source_path"]))
    link_target = job["link_target"]
    if mirror.is_symlink():
        if os.readlink(mirror) == link_target:
            return mirror
        raise TranslateError(f"{mirror} is a symlink to {os.readlink(mirror)!r}, expected {link_target!r}")
    if mirror.exists():
        raise TranslateError(f"{mirror} exists and is not a symlink; refusing to replace it")
    mirror.parent.mkdir(parents=True, exist_ok=True)
    os.symlink(link_target, mirror)
    return mirror


def cmd_assemble(args) -> int:
    root = common.repo_root()
    docs_dir = args.docs_dir or common.default_docs_dir(root)
    i18n_dir = args.i18n_dir or common.default_i18n_dir(root)
    registry_path = args.registry or (root / common.TERMS_REGISTRY_RELPATH)
    registry = terms_lint.load_registry(registry_path) if registry_path.is_file() else None
    terms_sha = terms_lint.registry_sha256(registry_path) if registry_path.is_file() else None
    job_file = Path(args.job)
    job = json.loads(common.read_text(job_file))
    if job.get("schema") != JOB_SCHEMA:
        raise TranslateError(f"{job_file}: unsupported job schema {job.get('schema')!r}")
    rel = job["source_path"]
    direction = job.get("direction") or {}
    source_locale = direction.get("source_locale", args.source_locale)
    target_locale = direction.get("target_locale", args.target_locale)
    mirror = common.mirror_dir(i18n_dir, target_locale) / Path(common.nfc(rel))

    if job.get("kind") == "symlink":
        if args.write:
            path = write_symlink(job, i18n_dir, target_locale)
            print(f"symlink {path} -> {job['link_target']}")
        else:
            print(f"dry run: would create symlink {mirror} -> {job['link_target']}")
        return 0

    if not args.engine:
        raise TranslateError("--engine is required (free string naming who/what translated)")
    source = common.source_path(rel, docs_dir)
    source_text = common.read_text(source)
    if common.content_sha256(source_text) != job["source_sha256"]:
        message = f"{rel}: the source changed since the job was prepared (hash {common.content_sha256(source_text)[:12]}… != job {job['source_sha256'][:12]}…)"
        if not args.ignore_source_change:
            raise TranslateError(message + "; re-run prepare or pass --ignore-source-change")
        common.warn(message)
    if terms_sha != job.get("terms_sha256"):
        common.warn(f"{rel}: the terms registry changed since the job was prepared; the front matter records the job's terms_sha256")
    if not isinstance(job.get("glossary_keys"), list) or not isinstance(job.get("glossary_sha256"), str):
        raise TranslateError(f"{job_file}: job has no glossary_keys/glossary_sha256 (prepared before applied-glossary provenance); re-run prepare")
    out_file = Path(args.out_json) if args.out_json else out_path_for(job_file)
    if not out_file.is_file():
        raise TranslateError(f"out file not found: {out_file}")
    translations = load_translations(json.loads(common.read_text(out_file)))
    translated_at = args.translated_at or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = {
        "source_locale": source_locale,
        "source_path": rel,
        "source_sha256": job["source_sha256"],
        "source_commit": job.get("source_commit"),
        "engine": args.engine,
        "prompt_sha256": job.get("prompt_sha256"),
        "terms_sha256": job.get("terms_sha256"),
        "glossary_keys": list(job["glossary_keys"]),
        "glossary_sha256": job["glossary_sha256"],
        "translated_at": translated_at,
        "reviewed_by": None,
    }
    final_text, _without, problems = assemble_text(job, translations, meta)
    for problem in problems:
        print(f"FAIL {rel}: {problem}")
    divergences, findings = ([], [])
    if not problems:
        divergences, findings = validate_pair(source_text, final_text, rel, registry)
        for d in divergences:
            print(f"FAIL {rel}: equivalence")
            print(equivalence.format_divergence(d))
        for f in findings:
            print(f"{'FAIL' if not args.allow_spelling_errors else 'warn'} {rel}: spelling {f.line}:{f.col} {f.token!r} -> {f.suggestion!r}")
    failed = bool(problems or divergences or (findings and not args.allow_spelling_errors))
    if args.print:
        sys.stdout.write(final_text)
        if not final_text.endswith("\n"):
            sys.stdout.write("\n")
    if failed:
        print(f"assemble: {rel} not written ({len(problems)} problem(s), {len(divergences)} divergence(s), {len(findings)} spelling error(s))")
        return 1
    pending = len(common.PENDING_MARKER_RE.findall(final_text))
    if args.write:
        mirror.parent.mkdir(parents=True, exist_ok=True)
        with open(mirror, "w", encoding="utf-8", newline="") as handle:
            handle.write(final_text)
        warnings: List[str] = []
        entry = sync_state.file_entry(rel, source, mirror, terms_sha, source_locale, warnings, registry=registry)
        for message in warnings:
            common.warn(message)
        print(f"wrote {mirror}")
        print(f"sync state: {entry['state']} (pending_blocks={entry['pending_blocks']}, target_sha256={entry['target_sha256'][:12]}…)")
    else:
        print(f"assemble: {rel} OK — equivalent, {pending} pending marker(s); dry run, pass --write to save to {mirror}")
    return 0


# --------------------------------------------------------------------------- #
# check
# --------------------------------------------------------------------------- #


def cmd_check(args) -> int:
    root = common.repo_root()
    docs_dir = args.docs_dir or common.default_docs_dir(root)
    i18n_dir = args.i18n_dir or common.default_i18n_dir(root)
    registry_path = args.registry or (root / common.TERMS_REGISTRY_RELPATH)
    rels = select_sources(docs_dir, args.path)
    targets = [(rel, common.mirror_path(rel, i18n_dir, args.target_locale)) for rel in rels]
    targets = [(rel, t) for rel, t in targets if t.is_file()]
    if not targets:
        common.warn(f"no {args.target_locale} files for {args.path}; nothing to check")
        return 0
    common_args = ["--source-locale", args.source_locale, "--target-locale", args.target_locale, "--docs-dir", str(docs_dir), "--i18n-dir", str(i18n_dir)]
    status = 0
    print("== equivalence")
    status |= equivalence.main(["--path", args.path, *common_args])
    selected = common.resolve_corpus_path(args.path, docs_dir)
    if selected.is_dir():
        mirror_sel = common.mirror_dir(i18n_dir, args.target_locale) / Path(common.rel_to_docs(selected, docs_dir))
        spelling_paths = [mirror_sel]
        consistency = [["consistency", "--path", str(mirror_sel), "--registry", str(registry_path), "--source-locale", args.source_locale, "--target-locale", args.target_locale, "--docs-dir", str(docs_dir)]]
    else:
        spelling_paths = [t for _r, t in targets]
        consistency = [["consistency", "--path", str(t), "--source-path", str(common.source_path(r, docs_dir)), "--registry", str(registry_path), "--source-locale", args.source_locale, "--target-locale", args.target_locale, "--docs-dir", str(docs_dir)] for r, t in targets]
    print("== spelling")
    for path in spelling_paths:
        status |= terms_lint.main(["spelling", "--path", str(path), "--registry", str(registry_path)])
    print("== consistency")
    for argv in consistency:
        status |= terms_lint.main(argv)
    print("check: " + ("OK" if status == 0 else "FAILED"))
    return 1 if status else 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _add_common(p: argparse.ArgumentParser) -> None:
    p.add_argument("--source-locale", default=common.DEFAULT_SOURCE_LOCALE)
    p.add_argument("--target-locale", default=common.DEFAULT_TARGET_LOCALE)
    p.add_argument("--docs-dir", type=Path, default=None, help="source corpus root (default: <repo>/manuals_src/docs/sbd-toe)")
    p.add_argument("--i18n-dir", type=Path, default=None, help="i18n root (default: <repo>/manuals_src/i18n)")
    p.add_argument("--registry", type=Path, default=None, help=f"terms registry (default: <repo>/{common.TERMS_REGISTRY_RELPATH})")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("prepare", help="write one job per eligible source file")
    p.add_argument("--path", required=True, help="file or directory, relative to --docs-dir")
    p.add_argument("--out", required=True, help="jobs directory (<out>/<path>.job.json)")
    p.add_argument("--only-stale", action="store_true", help=f"only files already translated whose state is {ELIGIBLE_STALE}")
    p.add_argument("--force", action="store_true", help="every selected file regardless of its sync state")
    p.add_argument("--prompt", type=Path, default=None, help=f"versioned prompt (default: <repo>/{PROMPT_RELPATH})")
    p.add_argument("--source-commit", default=None, help="override the commit recorded as source_commit (default: last commit touching the file)")
    p.add_argument("--json", action="store_true", help="machine-readable summary")
    _add_common(p)
    p.set_defaults(func=cmd_prepare)

    p = sub.add_parser("assemble", help="rebuild the target file from a job and its translations")
    p.add_argument("--job", required=True, help="job file written by prepare")
    p.add_argument("--out-json", default=None, help="translations file (default: the job's path with .out.json)")
    p.add_argument("--engine", default=None, help="who/what translated (free string; recorded in the front matter)")
    p.add_argument("--write", action="store_true", help="save to the mirror path when every check passes")
    p.add_argument("--print", action="store_true", help="print the assembled file to stdout")
    p.add_argument("--translated-at", default=None, help="override the ISO-8601 timestamp (tests)")
    p.add_argument("--allow-spelling-errors", action="store_true", help="report en-GB spelling errors without blocking the write")
    p.add_argument("--ignore-source-change", action="store_true", help="assemble even if the source changed since prepare")
    _add_common(p)
    p.set_defaults(func=cmd_assemble)

    p = sub.add_parser("check", help="equivalence + spelling + consistency over existing target files")
    p.add_argument("--path", required=True, help="file or directory, relative to --docs-dir")
    _add_common(p)
    p.set_defaults(func=cmd_check)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except common.TranslationToolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
