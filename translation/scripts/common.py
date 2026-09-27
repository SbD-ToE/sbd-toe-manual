"""Shared helpers for the SbD-ToE translation tooling.

Everything the other scripts agree on lives here: the content hash defined in
``translation/README.md``, repository-root resolution, source <-> mirror path
mapping, front-matter reading, a language-independent Markdown scanner, and a
faithful port of ``github-slugger`` as used by Docusaurus.

Only the standard library and PyYAML are used. Direction (source/target locale)
is always a parameter; nothing here assumes PT -> EN.

Path normalisation: every corpus-relative path is normalised to Unicode NFC
before it is used as a key, compared, or mapped between source and mirror.
APFS (macOS) returns some names in NFD (e.g. ``06-manual-formação-por-capitulo.md``)
while the version-control index and Linux check-outs carry NFC; without
normalisation the ``sync-state.json`` keys and their ordering would differ
between machines. When a file is opened, the NFC path is tried first and the
NFD spelling second, so both filesystems resolve.
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Iterator, List, Optional, Sequence, Tuple

import yaml

# --------------------------------------------------------------------------- #
# Layout constants (see translation/README.md, "Layout" and rule 2)
# --------------------------------------------------------------------------- #

DEFAULT_SOURCE_LOCALE = "pt"
DEFAULT_TARGET_LOCALE = "en"
MANUALS_SUBDIR = "manuals_src"
DOCS_SUBDIR = "docs/sbd-toe"  # the docs plugin has path: 'docs/sbd-toe'
I18N_SUBDIR = "i18n"
DOCS_PLUGIN_MIRROR = "docusaurus-plugin-content-docs/current"
PAGES_PLUGIN_MIRROR = "docusaurus-plugin-content-pages"
PAGES_SUBDIR = "src/pages"  # standalone pages (about, faq, licenciamento, tldr): mirrored under PAGES_PLUGIN_MIRROR
PLUGIN_MIRRORS = {"docs": DOCS_PLUGIN_MIRROR, "pages": PAGES_PLUGIN_MIRROR}
_plugin = "docs"


def use_plugin(name: str) -> None:
    """Select which Docusaurus content plugin the mirror helpers target (``docs`` by default; ``pages`` for src/pages)."""
    global _plugin
    if name not in PLUGIN_MIRRORS:
        raise ValueError(f"unknown content plugin {name!r} (expected one of {sorted(PLUGIN_MIRRORS)})")
    _plugin = name


def current_plugin() -> str:
    return _plugin
TERMS_REGISTRY_RELPATH = "translation/terms/registry.yaml"
SYNC_STATE_RELPATH = "translation/state/sync-state.json"
MARKDOWN_EXTENSIONS = (".md", ".mdx")

# Front-matter keys whose values are expected to differ between locales.
TRANSLATED_FRONTMATTER_KEYS = ("title", "description", "sidebar_label")
# Front-matter key that only exists on translated files.
TRANSLATION_BLOCK_KEY = "translation"

PENDING_MARKER_RE = re.compile(r"<!--\s*i18n:pending\b")


class TranslationToolError(Exception):
    """Base class for errors raised by the translation tooling."""


class FrontmatterError(TranslationToolError):
    """Raised when a front-matter block cannot be parsed."""


# --------------------------------------------------------------------------- #
# Repository root and paths
# --------------------------------------------------------------------------- #


def repo_root(start: Optional[Path] = None) -> Path:
    """Return the repository root.

    The scripts live in ``<root>/translation/scripts``; that location is tried
    first, then the current working directory is walked upwards looking for a
    directory that contains both ``manuals_src`` and ``translation``.
    """
    candidates: List[Path] = []
    here = Path(__file__).resolve()
    candidates.append(here.parents[2] if len(here.parents) >= 3 else here.parent)
    cwd = (start or Path.cwd()).resolve()
    candidates.extend([cwd, *cwd.parents])
    for candidate in candidates:
        if (candidate / MANUALS_SUBDIR).is_dir() and (candidate / "translation").is_dir():
            return candidate
    raise TranslationToolError(
        "could not locate the repository root (expected a directory containing "
        f"'{MANUALS_SUBDIR}/' and 'translation/')"
    )


def default_docs_dir(root: Optional[Path] = None) -> Path:
    """Directory holding the canonical (source-locale) corpus (src/pages when the ``pages`` plugin is selected)."""
    return (root or repo_root()) / MANUALS_SUBDIR / (PAGES_SUBDIR if _plugin == "pages" else DOCS_SUBDIR)


def default_i18n_dir(root: Optional[Path] = None) -> Path:
    """Docusaurus ``i18n/`` directory holding the translated mirrors."""
    return (root or repo_root()) / MANUALS_SUBDIR / I18N_SUBDIR


def nfc(text: str) -> str:
    """Unicode NFC form of a path or path fragment."""
    return unicodedata.normalize("NFC", text)


def existing_path(path: Path) -> Path:
    """Return ``path`` if it exists, else its NFD spelling if that exists
    (APFS may have stored the name decomposed), else ``path`` unchanged."""
    path = Path(path)
    if path.exists():
        return path
    decomposed = Path(unicodedata.normalize("NFD", str(path)))
    if decomposed.exists():
        return decomposed
    return path


def mirror_dir(i18n_dir: Path, target_locale: str) -> Path:
    """Root of the mirror for ``target_locale`` (README rule 2): docs by default, pages under ``use_plugin("pages")``."""
    return Path(i18n_dir) / target_locale / PLUGIN_MIRRORS[_plugin]


def mirror_path(rel_path: str, i18n_dir: Path, target_locale: str) -> Path:
    """Mirror file for a corpus-relative path (NFC key; on-disk spelling resolved)."""
    return existing_path(mirror_dir(i18n_dir, target_locale) / Path(nfc(rel_path)))


def source_path(rel_path: str, docs_dir: Path) -> Path:
    """Source file for a corpus-relative path (NFC key; on-disk spelling resolved)."""
    return existing_path(Path(docs_dir) / Path(nfc(rel_path)))


def rel_to_docs(path: Path, docs_dir: Path) -> str:
    """NFC corpus-relative POSIX path of ``path`` (which must live under ``docs_dir``)."""
    rel = Path(path).resolve().relative_to(Path(docs_dir).resolve())
    return nfc(rel.as_posix())


def resolve_corpus_path(path_arg: str, docs_dir: Path) -> Path:
    """Accept a path relative to ``docs_dir``, relative to the CWD, or absolute.
    The argument is NFC-normalised; the on-disk spelling is resolved either way."""
    candidate = Path(nfc(path_arg))
    if candidate.is_absolute():
        found = existing_path(candidate)
        if found.exists():
            return found
    in_docs = existing_path(Path(docs_dir) / candidate)
    if in_docs.exists():
        return in_docs
    local = existing_path(candidate)
    if local.exists():
        return local.resolve()
    raise TranslationToolError(f"path not found: {path_arg} (tried {in_docs})")


def is_markdown(path: Path) -> bool:
    return Path(path).suffix.lower() in MARKDOWN_EXTENSIONS


def iter_corpus(docs_dir: Path) -> List[str]:
    """Sorted, NFC-normalised corpus-relative POSIX paths of every ``.md``/``.mdx``
    under ``docs_dir``.

    Symbolic links are followed (the corpus contains one file-level symlink),
    matching Docusaurus, which resolves them when it globs the docs folder.
    Sorting happens on the NFC form so the order is the same on every platform.
    """
    docs_dir = Path(docs_dir)
    found: List[str] = []
    for dirpath, dirnames, filenames in os.walk(docs_dir, followlinks=True):
        dirnames.sort()
        for name in filenames:
            if name.lower().endswith(MARKDOWN_EXTENSIONS):
                full = Path(dirpath) / name
                found.append(nfc(full.relative_to(docs_dir).as_posix()))
    return sorted(found)


def iter_mirror(i18n_dir: Path, target_locale: str) -> List[str]:
    """Sorted corpus-relative paths of every Markdown file in the mirror (may be empty)."""
    root = mirror_dir(i18n_dir, target_locale)
    if not root.is_dir():
        return []
    return iter_corpus(root)


# --------------------------------------------------------------------------- #
# Hashing (README, "Hashes")
# --------------------------------------------------------------------------- #


def normalise_text(text: str) -> str:
    """Normalise content before hashing: no BOM, LF line ends, no trailing
    whitespace on any line, exactly one trailing newline."""
    if text.startswith("﻿"):
        text = text[1:]
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip(" \t\f\v") for line in text.split("\n")]
    body = "\n".join(lines).rstrip("\n")
    return body + "\n"


def content_sha256(text: str) -> str:
    """SHA-256 (hex) of the normalised content. The one hash function all scripts share."""
    return hashlib.sha256(normalise_text(text).encode("utf-8")).hexdigest()


def read_text(path: Path) -> str:
    """Read a UTF-8 file, tolerating a BOM."""
    with open(path, "r", encoding="utf-8-sig", newline="") as handle:
        return handle.read()


def file_sha256(path: Path) -> str:
    return content_sha256(read_text(path))


# --------------------------------------------------------------------------- #
# Applied-glossary hash (README, "Contrato do frontmatter"; sync_state `stale-terms`)
# --------------------------------------------------------------------------- #

# The only registry fields that can change what a translation *did* with a
# term. `notes`, `evidence`, `counts`, `sense`, `proposal`, … never enter the
# hash: editing them never makes a translation stale.
GLOSSARY_HASH_FIELDS = ("key", "state", "en", "en_variants", "pt", "pt_variants", "blocks_translation")


def _glossary_row(key: str, entry: Optional[dict]) -> dict:
    if entry is None:
        # A key that has left the registry can never hash like a present one.
        return {"key": key, "missing": True}
    row = {}
    for name in GLOSSARY_HASH_FIELDS:
        value = entry.get(name)
        if name.endswith("_variants"):
            value = sorted({str(v) for v in (value or ()) if v is not None and str(v) != ""})
        row[name] = value
    row["key"] = key
    return row


def glossary_sha256(registry: Optional[dict], keys: Iterable[str]) -> str:
    """SHA-256 of the glossary a translation applied: the registry entries named
    by ``keys`` (sorted, unique), reduced to ``GLOSSARY_HASH_FIELDS`` and
    serialised canonically (JSON, sorted keys, ``ensure_ascii=False``, no
    whitespace). A key missing from ``registry`` is serialised as
    ``{"key": …, "missing": true}`` so that its removal counts as a change.
    Variants are compared as sorted sets: reordering them is not a change.
    """
    by_key = {}
    for entry in (registry or {}).get("terms", []) or []:
        if isinstance(entry, dict) and entry.get("key") is not None:
            by_key[str(entry["key"])] = entry
    rows = [_glossary_row(key, by_key.get(key)) for key in sorted({str(k) for k in keys})]
    canonical = json.dumps(rows, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------- #
# Front matter
# --------------------------------------------------------------------------- #


class _StringSafeLoader(yaml.SafeLoader):
    """SafeLoader that keeps timestamps as strings (ISO dates in ``translated_at``
    must survive a round trip unchanged)."""


_StringSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for (tag, regexp) in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def yaml_load(text: str):
    return yaml.load(text, Loader=_StringSafeLoader)


_FM_OPEN_RE = re.compile(r"^---[ \t]*$")
# gray-matter (used by Docusaurus) closes at the first line that *starts* with
# "---"; whatever follows the three dashes on that line belongs to the body.
_FM_CLOSE_RE = re.compile(r"^---")


def split_frontmatter(text: str) -> Tuple[Optional[str], str, int]:
    """Split a document into (front-matter text or None, body, body_start_line).

    ``body_start_line`` is the 1-based line number of the first body line.
    Files without front matter are handled (front matter is ``None``).
    """
    if text.startswith("﻿"):
        text = text[1:]
    lines = text.split("\n")
    if not lines or not _FM_OPEN_RE.match(lines[0]):
        return None, text, 1
    for idx in range(1, len(lines)):
        if _FM_CLOSE_RE.match(lines[idx]):
            fm_text = "\n".join(lines[1:idx])
            remainder = lines[idx][3:]
            if remainder:
                body = "\n".join([remainder, *lines[idx + 1 :]])
                return fm_text, body, idx + 1
            body = "\n".join(lines[idx + 1 :])
            return fm_text, body, idx + 2
    # An opening '---' without a closing one is a thematic break, not front matter.
    return None, text, 1


def parse_frontmatter(text: str, *, where: str = "<text>") -> Tuple[Optional[dict], str, int]:
    """Return (front-matter mapping or None, body, body_start_line)."""
    fm_text, body, start = split_frontmatter(text)
    if fm_text is None:
        return None, body, start
    try:
        data = yaml_load(fm_text)
    except yaml.YAMLError as exc:  # pragma: no cover - exercised only on broken input
        raise FrontmatterError(f"{where}: invalid front matter YAML: {exc}") from exc
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise FrontmatterError(f"{where}: front matter is not a mapping")
    return data, body, start


def strip_translation_block(text: str) -> str:
    """Return the document without the top-level ``translation:`` mapping in its
    front matter, textually (no YAML re-serialisation), so the result hashes
    stably. This is the "body without this block" of the README contract.
    """
    if text.startswith("﻿"):
        text = text[1:]
    lines = text.split("\n")
    if not lines or not _FM_OPEN_RE.match(lines[0]):
        return text
    close = None
    for idx in range(1, len(lines)):
        if _FM_CLOSE_RE.match(lines[idx]):
            close = idx
            break
    if close is None:
        return text
    out = lines[:1]
    idx = 1
    key_re = re.compile(rf"^{TRANSLATION_BLOCK_KEY}\s*:")
    while idx < close:
        line = lines[idx]
        if key_re.match(line):
            idx += 1
            # Skip the nested mapping: indented lines and blank lines inside it.
            while idx < close and (lines[idx].strip() == "" or lines[idx][0] in " \t"):
                idx += 1
            continue
        out.append(line)
        idx += 1
    out.extend(lines[close:])
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Document ids (Docusaurus DefaultNumberPrefixParser)
# --------------------------------------------------------------------------- #

_IGNORED_PREFIX_RE = re.compile(r"^\d+[-_.]\d+")
_NUMBER_PREFIX_RE = re.compile(r"^(?P<numberPrefix>\d+)\s*[-_.]+\s*(?P<suffix>[^-_.\s].*)$")


def strip_number_prefix(name: str) -> str:
    """Docusaurus' default number-prefix parser (``03-foo`` -> ``foo``; ``7.0-foo`` kept)."""
    if _IGNORED_PREFIX_RE.match(name):
        return name
    match = _NUMBER_PREFIX_RE.match(name)
    return match.group("suffix") if match else name


def effective_id(rel_path: str, frontmatter: Optional[dict]) -> str:
    """Declared ``id`` or the file stem without its numeric prefix."""
    if frontmatter and isinstance(frontmatter.get("id"), (str, int)):
        return str(frontmatter["id"])
    stem = Path(rel_path).name
    for ext in MARKDOWN_EXTENSIONS:
        if stem.lower().endswith(ext):
            stem = stem[: -len(ext)]
            break
    return strip_number_prefix(stem)


# --------------------------------------------------------------------------- #
# github-slugger port (as wrapped by @docusaurus/utils createSlugger)
# --------------------------------------------------------------------------- #

_KEEP_CATEGORIES = {"Lu", "Ll", "Lt", "Lm", "Lo", "Mn", "Mc", "Me", "Nd", "Nl", "Pc"}


def _slug_keep(ch: str) -> bool:
    if ch in (" ", "-"):
        return True
    return unicodedata.category(ch) in _KEEP_CATEGORIES


def github_slug(value: str, maintain_case: bool = False) -> str:
    """Stateless ``github-slugger`` ``slug()``: lower-case (unless
    ``maintain_case``), drop every character outside letters/marks/decimal
    digits/letter numbers/connector punctuation/space/hyphen, then spaces -> ``-``.
    """
    if not isinstance(value, str):
        return ""
    if not maintain_case:
        value = value.lower()
    return "".join(ch for ch in value if _slug_keep(ch)).replace(" ", "-")


class Slugger:
    """Stateful slugger: repeats get ``-1``, ``-2``, ... exactly like github-slugger."""

    def __init__(self) -> None:
        self.occurrences: dict = {}

    def slug(self, value: str, maintain_case: bool = False) -> str:
        slug = github_slug(value, maintain_case)
        original = slug
        while slug in self.occurrences:
            self.occurrences[original] += 1
            slug = f"{original}-{self.occurrences[original]}"
        self.occurrences[slug] = 0
        return slug


# Docusaurus parseMarkdownHeadingId, classic syntax.
_HEADING_ID_RE = re.compile(r"\s*\{#(?P<id>(?:.(?!\{#|\}))*.)\}$")


def parse_heading_id(heading: str) -> Tuple[str, Optional[str]]:
    """Split ``Some heading {#some-id}`` into (text, id). MDX-escaped ``\\{#id}`` is accepted."""
    match = _HEADING_ID_RE.search(heading)
    if not match:
        return heading, None
    text = heading[: match.start()]
    if text.endswith("\\"):
        text = text[:-1]
    return text.rstrip(), match.group("id").strip()


_MD_LINK_RE = re.compile(r"\[(?P<alt>[^\]]+)\]\([^)]+\)")
_MD_IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\([^)]+\)")
_INLINE_HTML_RE = re.compile(r"</?[A-Za-z][^>]*>")
_HTML_COMMENT_RE = re.compile(r"<!--.*?--!?>", re.S)
_UNDERSCORE_EMPHASIS_RE = re.compile(r"(?<![\w])_{1,3}(?P<inner>[^_\s](?:[^_]*?[^_\s])?)_{1,3}(?![\w])")
_MD_ESCAPE_RE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|<>~])")
_CODE_SPAN_RE = re.compile(r"(`+)(.+?)\1")


def heading_text_runtime(content: str) -> str:
    """Approximate ``mdast-util-to-string`` of the heading node as the Docusaurus
    runtime plugin sees it: HTML/JSX nodes dropped, links and images unwrapped,
    emphasis markers dropped, code spans reduced to their content, entities decoded."""
    text = _HTML_COMMENT_RE.sub("", content)
    text = _INLINE_HTML_RE.sub("", text)
    text = _MD_IMAGE_RE.sub(lambda m: m.group("alt"), text)
    text = _MD_LINK_RE.sub(lambda m: m.group("alt"), text)
    text = _CODE_SPAN_RE.sub(lambda m: m.group(2), text)
    text = _UNDERSCORE_EMPHASIS_RE.sub(lambda m: m.group("inner"), text)
    text = _MD_ESCAPE_RE.sub(lambda m: m.group(1), text)
    text = html.unescape(text)
    return text.strip()


def heading_text_cli(content: str) -> str:
    """Heading text as ``docusaurus write-heading-ids`` sees it: links unwrapped only."""
    return _MD_LINK_RE.sub(lambda m: m.group("alt"), content).strip()


# --------------------------------------------------------------------------- #
# Minimal, robust Markdown scanner (line based, outside fenced code)
# --------------------------------------------------------------------------- #


@dataclass
class Heading:
    level: int
    text: str  # raw content without the {#id} suffix
    explicit_id: Optional[str]
    line: int
    derived_id: Optional[str] = None  # filled by assign_heading_ids

    @property
    def id(self) -> str:
        return self.explicit_id if self.explicit_id is not None else (self.derived_id or "")


@dataclass
class CodeBlock:
    lang: str
    content: str
    line: int
    fence: str


@dataclass
class Table:
    line: int
    header_cells: int
    columns: int
    rows: int
    alignments: List[str]
    ragged_rows: int


@dataclass
class Admonition:
    type: str
    title: str
    line: int
    end_line: Optional[int] = None


@dataclass
class ListBlock:
    line: int
    ordered: bool
    items: int  # top-level items
    total_items: int  # items at every depth
    max_depth: int  # 1 for a flat list


@dataclass
class Link:
    dest: str
    line: int
    kind: str  # "md" or "html"


@dataclass
class Image:
    src: str
    line: int


@dataclass
class Comment:
    text: str
    line: int


@dataclass
class Document:
    frontmatter: Optional[dict]
    frontmatter_present: bool
    body_start_line: int
    headings: List[Heading] = field(default_factory=list)
    code_blocks: List[CodeBlock] = field(default_factory=list)
    tables: List[Table] = field(default_factory=list)
    admonitions: List[Admonition] = field(default_factory=list)
    lists: List[ListBlock] = field(default_factory=list)
    links: List[Link] = field(default_factory=list)
    images: List[Image] = field(default_factory=list)
    comments: List[Comment] = field(default_factory=list)
    esm: List[str] = field(default_factory=list)  # MDX import/export statements
    prose_lines: List[Tuple[int, str]] = field(default_factory=list)
    pending_markers: int = 0


_FENCE_RE = re.compile(r"^(?P<indent>\s*)(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
_HEADING_RE = re.compile(r"^ {0,3}(?P<hashes>#{1,6})(?:[ \t]+(?P<content>.*?))?[ \t]*$")
_CLOSING_HASHES_RE = re.compile(r"(?:^|\s+)#+\s*$")
_ADMONITION_OPEN_RE = re.compile(r"^\s*(?P<colons>:{3,})(?P<type>[A-Za-z][\w-]*)(?:[ \t]+(?P<title>.*?))?\s*$")
_ADMONITION_CLOSE_RE = re.compile(r"^\s*(?P<colons>:{3,})\s*$")
_TABLE_DELIM_RE = re.compile(r"^\s*\|?\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)*\|?\s*$")
_LIST_ITEM_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<marker>[-*+]|\d{1,9}[.)])(?:[ \t]+(?P<content>.*))?$")
_ESM_RE = re.compile(r"^(import|export)\s")
_INLINE_LINK_RE = re.compile(
    r"(?P<bang>!?)\[(?P<text>(?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*(?P<dest><[^>]*>|[^\s)]+)?(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
_HTML_HREF_RE = re.compile(r"<a\b[^>]*?\bhref\s*=\s*(?:\"(?P<d1>[^\"]*)\"|'(?P<d2>[^']*)'|(?P<d3>[^\s>]+))", re.I)
_HTML_IMG_RE = re.compile(r"<img\b[^>]*?\bsrc\s*=\s*(?:\"(?P<d1>[^\"]*)\"|'(?P<d2>[^']*)'|(?P<d3>[^\s>]+))", re.I)


def _is_blank(line: str) -> bool:
    return line.strip() == ""


def _split_cells(row: str) -> List[str]:
    """Split a GFM table row into cells, honouring ``\\|`` and pipes inside code spans."""
    cells: List[str] = []
    buf: List[str] = []
    in_code = False
    idx = 0
    while idx < len(row):
        ch = row[idx]
        if ch == "\\" and idx + 1 < len(row) and row[idx + 1] == "|":
            buf.append("|")
            idx += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
        idx += 1
    cells.append("".join(buf))
    # Leading/trailing pipes produce empty edge cells; drop them like GFM does.
    if cells and cells[0].strip() == "" and row.lstrip().startswith("|"):
        cells = cells[1:]
    if cells and cells[-1].strip() == "" and row.rstrip().endswith("|") and not row.rstrip().endswith("\\|"):
        cells = cells[:-1]
    return cells


def _alignment(cell: str) -> str:
    cell = cell.strip()
    left = cell.startswith(":")
    right = cell.endswith(":")
    if left and right:
        return "center"
    if left:
        return "left"
    if right:
        return "right"
    return "none"


def _strip_code_spans(text: str) -> str:
    return _CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), text)


def parse_markdown(text: str, *, where: str = "<text>") -> Document:
    """Scan a Markdown/MDX document and collect its language-independent structure.

    The scanner is deliberately line based and conservative: it never raises on
    odd input, ignores everything inside fenced code (which is captured as a
    block), and tolerates MDX ``import``/``export`` statements and inline JSX.
    """
    frontmatter, body, body_start = parse_frontmatter(text, where=where)
    doc = Document(frontmatter=frontmatter, frontmatter_present=frontmatter is not None, body_start_line=body_start)
    lines = body.split("\n")
    total = len(lines)

    # Pass 1: fenced code, HTML comments, and a "prose" view of the remaining lines.
    prose: List[Optional[str]] = [None] * total  # None = not prose (code/comment)
    in_fence: Optional[Tuple[str, int, int]] = None  # (fence char, fence length, indent)
    fence_lang = ""
    fence_buf: List[str] = []
    fence_start = 0
    in_comment = False
    comment_buf: List[str] = []
    comment_start = 0

    for offset, raw in enumerate(lines):
        lineno = body_start + offset
        line = raw.rstrip("\r")
        if in_fence is not None:
            char, length, _indent = in_fence
            stripped = line.strip()
            if stripped and set(stripped) == {char} and len(stripped) >= length:
                doc.code_blocks.append(
                    CodeBlock(lang=fence_lang, content="\n".join(fence_buf), line=fence_start, fence=char * length)
                )
                in_fence = None
                fence_buf = []
            else:
                fence_buf.append(line)
            continue
        if in_comment:
            end = line.find("-->")
            if end >= 0:
                comment_buf.append(line[:end])
                doc.comments.append(Comment(text="\n".join(comment_buf), line=comment_start))
                in_comment = False
                remainder = line[end + 3 :]
                prose[offset] = remainder if remainder.strip() else None
                if PENDING_MARKER_RE.search("<!--" + "\n".join(comment_buf)):
                    doc.pending_markers += 1
                comment_buf = []
            else:
                comment_buf.append(line)
            continue
        fence_match = _FENCE_RE.match(line)
        if fence_match:
            fence = fence_match.group("fence")
            info = fence_match.group("info")
            if fence[0] == "~" or "`" not in info:
                in_fence = (fence[0], len(fence), len(fence_match.group("indent")))
                fence_lang = info.strip().split()[0] if info.strip() else ""
                fence_start = lineno
                fence_buf = []
                continue
        # Inline (single-line) HTML comments are removed from the prose view; a
        # comment that opens without closing on the same line spans lines.
        work = line
        while True:
            start = work.find("<!--")
            if start < 0:
                break
            end = work.find("-->", start + 4)
            if end < 0:
                in_comment = True
                comment_start = lineno
                comment_buf = [work[start + 4 :]]
                work = work[:start]
                break
            comment_text = work[start + 4 : end]
            doc.comments.append(Comment(text=comment_text, line=lineno))
            if PENDING_MARKER_RE.search(work[start : end + 3]):
                doc.pending_markers += 1
            work = work[:start] + work[end + 3 :]
        prose[offset] = work

    if in_fence is not None:  # unterminated fence: keep what we have
        doc.code_blocks.append(CodeBlock(lang=fence_lang, content="\n".join(fence_buf), line=fence_start, fence=in_fence[0] * in_fence[1]))
    if in_comment:
        doc.comments.append(Comment(text="\n".join(comment_buf), line=comment_start))

    # Pass 2: block structure over the prose view.
    admonition_stack: List[Admonition] = []
    list_state: Optional[dict] = None
    offset = 0

    def close_list() -> None:
        nonlocal list_state
        if list_state is not None:
            doc.lists.append(
                ListBlock(
                    line=list_state["line"],
                    ordered=list_state["ordered"],
                    items=list_state["items"],
                    total_items=list_state["total"],
                    max_depth=list_state["max_depth"],
                )
            )
            list_state = None

    while offset < total:
        work = prose[offset]
        lineno = body_start + offset
        if work is None:
            # Code or comment line. A fence ends a list only if it is not indented.
            if list_state is not None and offset < total and lines[offset].strip() != "" and not lines[offset][:1].isspace():
                close_list()
            offset += 1
            continue
        line = work
        doc.prose_lines.append((lineno, line))

        if _is_blank(line):
            if list_state is not None:
                # Look ahead: the list continues if the next non-blank prose line is an item or indented.
                nxt = offset + 1
                while nxt < total and prose[nxt] is not None and _is_blank(prose[nxt]):
                    nxt += 1
                if nxt >= total:
                    close_list()
                else:
                    candidate = prose[nxt]
                    if candidate is None:
                        # Fenced block after a blank line: part of the list only if indented.
                        if not lines[nxt][:1].isspace():
                            close_list()
                    elif not (_LIST_ITEM_RE.match(candidate) or candidate[:1] in (" ", "\t")):
                        close_list()
            offset += 1
            continue

        esm_match = _ESM_RE.match(line)
        if esm_match:
            close_list()
            doc.esm.append(line.strip())
            offset += 1
            continue

        adm_open = _ADMONITION_OPEN_RE.match(line)
        if adm_open:
            close_list()
            adm = Admonition(type=adm_open.group("type").lower(), title=(adm_open.group("title") or "").strip(), line=lineno)
            doc.admonitions.append(adm)
            admonition_stack.append(adm)
            offset += 1
            continue
        adm_close = _ADMONITION_CLOSE_RE.match(line)
        if adm_close:
            close_list()
            if admonition_stack:
                admonition_stack.pop().end_line = lineno
            offset += 1
            continue

        heading_match = _HEADING_RE.match(line)
        if heading_match:
            close_list()
            content = heading_match.group("content") or ""
            content = _CLOSING_HASHES_RE.sub("", content) if not content.rstrip().endswith("}") else content
            text, explicit = parse_heading_id(content.strip())
            doc.headings.append(Heading(level=len(heading_match.group("hashes")), text=text, explicit_id=explicit, line=lineno))
            offset += 1
            continue

        # Tables: a row followed by a delimiter row.
        if "|" in line and offset + 1 < total and prose[offset + 1] is not None and _TABLE_DELIM_RE.match(prose[offset + 1]) and "-" in prose[offset + 1]:
            close_list()
            header_cells = _split_cells(line)
            delim_cells = _split_cells(prose[offset + 1])
            columns = len(delim_cells)
            alignments = [_alignment(c) for c in delim_cells]
            rows = 0
            ragged = 0
            cursor = offset + 2
            while cursor < total:
                row = prose[cursor]
                if row is None or _is_blank(row) or _HEADING_RE.match(row) or _ADMONITION_OPEN_RE.match(row) or _ADMONITION_CLOSE_RE.match(row):
                    break
                rows += 1
                if len(_split_cells(row)) != columns:
                    ragged += 1
                doc.prose_lines.append((body_start + cursor, row))
                cursor += 1
            doc.tables.append(Table(line=lineno, header_cells=len(header_cells), columns=columns, rows=rows, alignments=alignments, ragged_rows=ragged))
            offset = cursor
            continue

        item_match = _LIST_ITEM_RE.match(line)
        if item_match:
            indent = len(item_match.group("indent").expandtabs(4))
            marker = item_match.group("marker")
            ordered = marker[0].isdigit()
            if list_state is None:
                list_state = {"line": lineno, "ordered": ordered, "items": 0, "total": 0, "max_depth": 1, "stack": [indent]}
            stack: List[int] = list_state["stack"]
            if indent > stack[-1]:
                stack.append(indent)
            else:
                while len(stack) > 1 and indent < stack[-1]:
                    stack.pop()
            depth = len(stack)
            if depth == 1:
                list_state["items"] += 1
            list_state["total"] += 1
            list_state["max_depth"] = max(list_state["max_depth"], depth)
            offset += 1
            continue

        if list_state is not None and not line[:1].isspace():
            close_list()
        offset += 1

    close_list()
    while admonition_stack:
        admonition_stack.pop()

    # Pass 3: inline links and images over the prose view (code spans blanked).
    for lineno, line in doc.prose_lines:
        scan = _strip_code_spans(line)
        for match in _INLINE_LINK_RE.finditer(scan):
            dest = (match.group("dest") or "").strip()
            if dest.startswith("<") and dest.endswith(">"):
                dest = dest[1:-1].strip()
            if match.group("bang"):
                doc.images.append(Image(src=dest, line=lineno))
            else:
                doc.links.append(Link(dest=dest, line=lineno, kind="md"))
        for match in _HTML_HREF_RE.finditer(scan):
            dest = match.group("d1") or match.group("d2") or match.group("d3") or ""
            doc.links.append(Link(dest=dest.strip(), line=lineno, kind="html"))
        for match in _HTML_IMG_RE.finditer(scan):
            src = match.group("d1") or match.group("d2") or match.group("d3") or ""
            doc.images.append(Image(src=src.strip(), line=lineno))

    return doc


def assign_heading_ids(doc: Document, mode: str = "runtime") -> None:
    """Fill ``derived_id`` for headings without an explicit id.

    ``runtime`` (default) mirrors the Docusaurus MDX heading plugin: one slugger
    per page, headings visited in order, explicit ids used verbatim and *not*
    registered in the slugger. ``cli`` mirrors ``docusaurus write-heading-ids``:
    explicit ids are registered first, then the rest are generated in order.
    """
    slugger = Slugger()
    if mode == "cli":
        for heading in doc.headings:
            if heading.explicit_id is not None:
                slugger.slug(heading.explicit_id)
        for heading in doc.headings:
            if heading.explicit_id is None:
                heading.derived_id = slugger.slug(heading_text_cli(heading.text))
        return
    if mode != "runtime":
        raise TranslationToolError(f"unknown slugger mode: {mode}")
    for heading in doc.headings:
        if heading.explicit_id is None:
            heading.derived_id = slugger.slug(heading_text_runtime(heading.text))


_SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def is_internal_link(dest: str) -> bool:
    """True for site-relative, file-relative and anchor-only destinations."""
    dest = dest.strip()
    if not dest:
        return False
    if dest.startswith("//") or _SCHEME_RE.match(dest):
        return False
    return True


def normalise_link(dest: str) -> str:
    """Canonical form of an internal destination: whitespace trimmed, an empty
    fragment dropped, nothing else (paths and anchors must match verbatim)."""
    dest = dest.strip()
    if dest.endswith("#"):
        dest = dest[:-1]
    return dest


def warn(message: str) -> None:
    print(f"warning: {message}", file=sys.stderr)
