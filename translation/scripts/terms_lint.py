#!/usr/bin/env python3
"""Lint around the terms registry (``translation/terms/registry.yaml``).

Sub-commands (all exit 1 on findings of severity *error*, 0 otherwise)::

    terms_lint.py validate       --registry R
    terms_lint.py spelling       --path FILE-OR-DIR [--registry R] [--fix]
    terms_lint.py pending-blocks --path FILE-OR-DIR --registry R [--json]
    terms_lint.py consistency    --path DIR-EN --registry R
    terms_lint.py export-pending --registry R --out translation/terms/pending-export.md
    terms_lint.py hash           --registry R

``validate`` checks the schema of the registry (required keys, enumerations,
conditional fields, unique keys, ``false_friends`` references).

``spelling`` applies the en-GB rule of ``translation/terms/README.md`` to the
EN prose: outside code, comments, structural front matter, protected tokens
(``protected_tokens.py``) and every ``en``/``en_variants`` form of a
``do-not-translate`` entry (matched case-sensitively) or of an ``in-record`` /
``coined`` / ``changed`` entry (case-insensitively, **in its en-GB spelling**:
spelling is style, so a registry form recorded as the papers wrote it —
``normalization`` — exempts ``normalisation`` in the prose, never
``normalization``; the registry entry is not ``changed`` for that). ``pending``
entries have no authority over the prose, so their forms are not exempt. The
rules live in the single ``SPELLING_RULES`` mapping so the Manual agent can
extend them. A single summary line counts the AmE-spelled registry forms.

``pending-blocks`` finds, in the source-locale text, every block (paragraph,
list item, table cell, heading, admonition title, front-matter title /
description) containing a ``pt``/``pt_variants`` form of an entry with
``state: pending`` and ``blocks_translation: true`` (whole word,
case-insensitive, NFC).

``consistency`` checks that a source-locale form of an ``in-record`` /
``coined`` / ``changed`` entry is rendered in the mirror with ``en`` or one of
``en_variants`` (block-aligned when both files have the same number of
blocks, per file otherwise). A source form left untranslated in the mirror is
a warning. Without mirror files the command succeeds with a warning.

``export-pending`` writes the pending queue as Markdown, one table per owner,
deterministically. ``hash`` prints the SHA-256 ``sync_state.py`` uses for
``terms_sha256`` (``common.file_sha256`` over the registry).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
import protected_tokens  # noqa: E402

# --------------------------------------------------------------------------- #
# Schema vocabulary
# --------------------------------------------------------------------------- #

SPECIES = (1, 2, 3)
STATES = ("in-record", "coined", "pending", "changed", "do-not-translate", "withdrawn")
OWNERS = ("manual-agent", "archon", "lead")
PENDING_REASONS = ("polysemy", "en-vs-en-collision", "unborn", "v26-collision")
AUTHORITATIVE_STATES = ("in-record", "coined", "changed")
REQUIRED_ENTRY_KEYS = (
    "key", "species", "state", "owner", "en", "en_variants", "pt", "pt_variants", "ontology_id", "sense",
    "senses", "evidence", "counts", "change_cost", "curator", "previous", "proposal", "false_friends",
    "pending_reason", "blocks_translation", "notes",
)
REQUIRED_META_KEYS = ("version", "spelling", "source_locale", "target_locale")
PREVIOUS_KEYS = ("en", "used_in", "reason", "date", "ratified_by")
KEY_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
OWNER_ORDER = ("archon", "lead", "manual-agent")


# --------------------------------------------------------------------------- #
# Registry loading
# --------------------------------------------------------------------------- #


def load_registry(path: Path) -> dict:
    data = common.yaml_load(common.read_text(path))
    if not isinstance(data, dict) or not isinstance(data.get("terms"), list):
        raise common.TranslationToolError(f"{path}: not a registry (expected a mapping with a 'terms' list)")
    return data


def registry_sha256(path: Path) -> str:
    """The hash ``sync_state.py`` records as ``terms_sha256``."""
    return common.file_sha256(path)


def _forms(entry: dict, which: str) -> List[str]:
    forms: List[str] = []
    canonical = entry.get(which)
    if isinstance(canonical, str) and canonical.strip():
        forms.append(canonical.strip())
    for variant in entry.get(f"{which}_variants") or ():
        if isinstance(variant, str) and variant.strip():
            forms.append(variant.strip())
    return forms


def _word_regex(forms: Iterable[str], *, ignore_case: bool) -> Optional[re.Pattern]:
    """Whole-word alternation of ``forms`` (longest first); spaces match any whitespace."""
    cleaned = sorted({common.nfc(f) for f in forms if f}, key=lambda s: (-len(s), s))
    if not cleaned:
        return None
    parts = [re.escape(f).replace(r"\ ", r"\s+") for f in cleaned]
    pattern = r"(?<![\w])(?:" + "|".join(parts) + r")(?![\w])"
    return re.compile(pattern, re.IGNORECASE if ignore_case else 0)


# --------------------------------------------------------------------------- #
# validate
# --------------------------------------------------------------------------- #


def validate_registry(registry: dict) -> List[str]:
    problems: List[str] = []
    meta = registry.get("meta")
    if not isinstance(meta, dict):
        problems.append("meta: missing or not a mapping")
    else:
        for key in REQUIRED_META_KEYS:
            if key not in meta:
                problems.append(f"meta: missing '{key}'")
    terms = registry.get("terms") or []
    keys = [e.get("key") for e in terms if isinstance(e, dict)]
    known = set(k for k in keys if isinstance(k, str))
    seen: Set[str] = set()
    for index, entry in enumerate(terms):
        where = f"terms[{index}]"
        if not isinstance(entry, dict):
            problems.append(f"{where}: not a mapping")
            continue
        key = entry.get("key")
        where = f"{key!s}" if isinstance(key, str) else where
        if not isinstance(key, str) or not KEY_RE.match(key):
            problems.append(f"{where}: key must be lower-case snake_case ASCII")
        elif key in seen:
            problems.append(f"{where}: duplicate key")
        else:
            seen.add(key)
        for required in REQUIRED_ENTRY_KEYS:
            if required not in entry:
                problems.append(f"{where}: missing '{required}'")
        unknown = [k for k in entry if k not in REQUIRED_ENTRY_KEYS]
        if unknown:
            problems.append(f"{where}: unknown keys {unknown}")
        species = entry.get("species")
        state = entry.get("state")
        owner = entry.get("owner")
        reason = entry.get("pending_reason")
        if species not in SPECIES:
            problems.append(f"{where}: species must be one of {SPECIES}, got {species!r}")
        if state not in STATES:
            problems.append(f"{where}: state must be one of {STATES}, got {state!r}")
        if owner not in OWNERS:
            problems.append(f"{where}: owner must be one of {OWNERS}, got {owner!r}")
        if reason is not None and reason not in PENDING_REASONS:
            problems.append(f"{where}: pending_reason must be one of {PENDING_REASONS} or null, got {reason!r}")
        if state == "pending" and reason is None:
            problems.append(f"{where}: pending_reason is required when state is 'pending'")
        if state != "pending" and reason is not None:
            problems.append(f"{where}: pending_reason must be null unless state is 'pending'")
        if reason == "polysemy" and not entry.get("senses"):
            problems.append(f"{where}: senses is required when pending_reason is 'polysemy'")
        en = entry.get("en")
        if en is None:
            if (not (species == 2 and state == "pending")) and entry.get("state") != "withdrawn":
                problems.append(f"{where}: en may be null only for a species-2 entry in state 'pending'")
        elif not isinstance(en, str) or not en.strip():
            problems.append(f"{where}: en must be a non-empty string or null")
        if state == "changed":
            previous = entry.get("previous")
            if not isinstance(previous, dict):
                problems.append(f"{where}: previous is required (mapping) when state is 'changed'")
            else:
                for k in PREVIOUS_KEYS:
                    if k not in previous:
                        problems.append(f"{where}: previous is missing '{k}'")
        if species == 2 and state == "pending":
            proposal = entry.get("proposal")
            if not isinstance(proposal, str) or not proposal.strip():
                problems.append(f"{where}: proposal is required for a species-2 entry in state 'pending'")
            if not isinstance(entry.get("false_friends"), list):
                problems.append(f"{where}: false_friends must be a list (possibly empty) for a species-2 entry in state 'pending'")
        for list_key in ("en_variants", "pt_variants", "false_friends", "senses"):
            value = entry.get(list_key)
            if value is not None and not isinstance(value, list):
                problems.append(f"{where}: {list_key} must be a list")
        for friend in entry.get("false_friends") or ():
            if friend not in known:
                problems.append(f"{where}: false_friends refers to unknown key {friend!r}")
            elif friend == key:
                problems.append(f"{where}: false_friends refers to itself")
        pt = entry.get("pt")
        if pt is not None and (not isinstance(pt, str) or not pt.strip()):
            problems.append(f"{where}: pt must be a non-empty string or null")
        if not isinstance(entry.get("blocks_translation"), bool):
            problems.append(f"{where}: blocks_translation must be a boolean")
        if entry.get("notes") is not None and not isinstance(entry.get("notes"), str):
            problems.append(f"{where}: notes must be a string")
    return problems


# --------------------------------------------------------------------------- #
# Prose extraction (shared by spelling, pending-blocks, consistency, species 3)
# --------------------------------------------------------------------------- #

_CODE_SPAN_RE = common._CODE_SPAN_RE
_HTML_TAG_RE = re.compile(r"</?[A-Za-z][^>]*>")
_LINK_DEST_RE = re.compile(r"\]\([^)]*\)")
_REF_LINK_RE = re.compile(r"\]\[[^\]]*\]")
_URL_RE = re.compile(r"(?:https?://|www\.)\S+")
_HEADING_ID_RE = re.compile(r"\{#[^}]*\}")
_INLINE_COMMENT_RE = re.compile(r"<!--.*?-->")
_FM_LINE_RE = re.compile(r"^(?P<key>title|description)\s*:\s*(?P<value>.*)$")


def _blank(match: re.Match) -> str:
    return " " * len(match.group(0))


def mask_line(raw: str) -> str:
    """The prose of a line with everything non-prose replaced by spaces
    (same length, so columns map 1:1 onto the original line)."""
    text = raw
    close = text.find("-->")
    open_ = text.find("<!--")
    if close >= 0 and (open_ < 0 or close < open_):
        text = " " * (close + 3) + text[close + 3 :]
    text = _INLINE_COMMENT_RE.sub(_blank, text)
    open_ = text.find("<!--")
    if open_ >= 0:
        text = text[:open_] + " " * (len(text) - open_)
    text = _CODE_SPAN_RE.sub(_blank, text)
    text = _URL_RE.sub(_blank, text)
    text = _LINK_DEST_RE.sub(_blank, text)
    text = _REF_LINK_RE.sub(_blank, text)
    text = _HTML_TAG_RE.sub(_blank, text)
    text = _HEADING_ID_RE.sub(_blank, text)
    return text


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


@dataclass
class Block:
    kind: str  # paragraph · item · cell · heading · admonition · frontmatter
    line: int
    text: str


@dataclass
class ProseLine:
    line: int
    text: str  # masked
    kind: str  # frontmatter · body


def extract_prose(text: str, *, where: str = "<text>") -> Tuple[List[ProseLine], List[Block]]:
    """Masked prose lines (for column-exact findings) and blocks (for block-level
    matching) of a Markdown/MDX document, outside code, comments and structural
    front matter."""
    doc = common.parse_markdown(text, where=where)
    if text.startswith("﻿"):
        text = text[1:]
    raw_lines = text.split("\n")
    lines: List[ProseLine] = []
    blocks: List[Block] = []

    # Front matter: only title / description are prose.
    fm_text, _body, body_start = common.split_frontmatter(text)
    if fm_text is not None:
        for offset, fm_line in enumerate(fm_text.split("\n")):
            match = _FM_LINE_RE.match(fm_line)
            if match:
                value = _unquote(match.group("value"))
                if value and not value.startswith(("|", ">")):
                    lineno = offset + 2  # line 1 is the opening '---'
                    raw_value = match.group("value")
                    padded = " " * (len(fm_line) - len(raw_value)) + raw_value  # value is the line's suffix
                    lines.append(ProseLine(lineno, mask_line(padded), "frontmatter"))
                    blocks.append(Block("frontmatter", lineno, value))

    heading_lines = {h.line: h for h in doc.headings}
    admonition_lines = {a.line: a for a in doc.admonitions}
    table_lines: Dict[int, str] = {}
    for table in doc.tables:
        table_lines[table.line] = "header"
        table_lines[table.line + 1] = "delimiter"
        for i in range(table.rows):
            table_lines[table.line + 2 + i] = "row"

    current: Optional[Block] = None

    def close() -> None:
        nonlocal current
        if current is not None and current.text.strip():
            blocks.append(current)
        current = None

    for lineno, _prose in doc.prose_lines:
        raw = raw_lines[lineno - 1] if 0 < lineno <= len(raw_lines) else ""
        masked = mask_line(raw)
        if lineno in table_lines and table_lines[lineno] == "delimiter":
            continue
        if common._ESM_RE.match(masked.lstrip()):
            close()
            continue
        lines.append(ProseLine(lineno, masked, "body"))
        if lineno in heading_lines:
            close()
            heading = heading_lines[lineno]
            blocks.append(Block("heading", lineno, mask_line(heading.text).strip()))
            continue
        if lineno in admonition_lines:
            close()
            title = admonition_lines[lineno].title
            if title:
                blocks.append(Block("admonition", lineno, mask_line(title).strip()))
            continue
        if common._ADMONITION_CLOSE_RE.match(masked):
            close()
            continue
        if lineno in table_lines:
            close()
            for cell in common._split_cells(masked):
                if cell.strip():
                    blocks.append(Block("cell", lineno, cell.strip()))
            continue
        if not masked.strip():
            close()
            continue
        item = common._LIST_ITEM_RE.match(masked)
        if item:
            close()
            current = Block("item", lineno, (item.group("content") or "").strip())
            continue
        if current is None:
            current = Block("paragraph", lineno, masked.strip())
        else:
            current.text = f"{current.text} {masked.strip()}"
    close()
    return lines, blocks


def iter_files(path: Path) -> List[Path]:
    path = common.existing_path(path)
    if path.is_file():
        return [path]
    if not path.is_dir():
        raise common.TranslationToolError(f"path not found: {path}")
    return [path / rel for rel in common.iter_corpus(path)]


def display_path(path: Path, root: Optional[Path]) -> str:
    try:
        return common.nfc(Path(path).resolve().relative_to((root or Path.cwd()).resolve()).as_posix())
    except ValueError:
        return common.nfc(str(path))


# --------------------------------------------------------------------------- #
# spelling — en-GB rules
# --------------------------------------------------------------------------- #

IZE_EXCEPTIONS = {
    # -ize is the only British spelling
    "size", "sizes", "sized", "sizing", "resize", "resizes", "resized", "resizing", "oversize", "oversized",
    "downsize", "downsized", "downsizing", "prize", "prizes", "prized", "seize", "seizes", "seized", "seizing",
    "capsize", "capsizes", "capsized", "capsizing", "maize", "assize", "assizes",
}

_OUR_STEMS = "col|behavi|flav|hon|lab|fav|neighb|endeav|harb|hum|rum|arm|vap|vig|sav|od|val"
_OUR_RE = re.compile(rf"^({_OUR_STEMS})or(s|ed|ing|al|ally|able|ably|ful|ite|ites|ism)?$")
_LL_STEMS = (
    "model|label|travel|cancel|signal|channel|level|total|fuel|marvel|dial|equal|panel|tunnel|funnel|counsel|"
    "jewel|initial|spiral|rival|quarrel|libel|pedal"
)
_LL_RE = re.compile(rf"^({_LL_STEMS})(ed|ing|er|ers)$")
_RE_FORMS = {
    "center": "centre", "centers": "centres", "centered": "centred", "centering": "centring",
    "liter": "litre", "liters": "litres", "fiber": "fibre", "fibers": "fibres", "theater": "theatre",
    "theaters": "theatres", "caliber": "calibre", "kilometer": "kilometre", "kilometers": "kilometres",
    "millimeter": "millimetre", "millimeters": "millimetres", "centimeter": "centimetre",
    "centimeters": "centimetres", "micrometer": "micrometre", "micrometers": "micrometres",
    "nanometer": "nanometre", "nanometers": "nanometres",
}
_SINGLE_L_FORMS = {
    "counselor": "counsellor", "counselors": "counsellors", "enroll": "enrol", "enrolls": "enrols",
    "enrollment": "enrolment", "enrollments": "enrolments", "fulfill": "fulfil", "fulfills": "fulfils",
    "fulfillment": "fulfilment", "installment": "instalment", "installments": "instalments",
    "skillful": "skilful", "skillfully": "skilfully", "willful": "wilful", "willfully": "wilfully",
    "distill": "distil", "distills": "distils", "instill": "instil", "instills": "instils",
}
_MISC_ERRORS = {
    "defense": "defence", "defenses": "defences", "offense": "offence", "offenses": "offences",
    "pretense": "pretence", "catalog": "catalogue", "catalogs": "catalogues", "cataloged": "catalogued",
    "cataloging": "cataloguing", "aluminum": "aluminium", "jewelry": "jewellery", "maneuver": "manoeuvre",
    "maneuvers": "manoeuvres", "maneuvered": "manoeuvred", "maneuvering": "manoeuvring", "skeptic": "sceptic",
    "skeptical": "sceptical", "skepticism": "scepticism", "skeptics": "sceptics", "mustache": "moustache",
    "pajamas": "pyjamas", "plow": "plough", "gray": "grey", "grays": "greys",
}
_MISC_WARNINGS = {
    "meter": "metre (unit) — 'meter' is correct for a measuring device",
    "meters": "metres (unit) — 'meters' is correct for measuring devices",
    "dialog": "dialogue — 'dialog' is tolerated for a UI dialog box",
    "analog": "analogue — 'analog' is tolerated in electronics",
    "aging": "ageing",
    "toward": "towards",
    "math": "maths",
    "specialty": "speciality",
    "acknowledgment": "acknowledgement",
    "acknowledgments": "acknowledgements",
    "mold": "mould (unless the verb 'to mold' is intended)",
    "airplane": "aeroplane",
}
_LICENCE_DETERMINERS = {
    "a", "an", "the", "this", "that", "these", "those", "its", "their", "our", "your", "his", "her", "my", "no",
    "any", "each", "every", "same", "such", "another", "open", "open-source", "software", "code", "mit", "apache",
    "dual", "permissive", "copyleft", "under", "of", "per", "content", "data", "creative", "commons", "cc",
    "documentation", "licence", "licenses", "same", "one", "single", "separate", "different",
}


def _match_first_case(template: str, original: str) -> str:
    if original[:1].isupper():
        return template[:1].upper() + template[1:]
    return template


def _rule_ize(token: str, lower: str, before: str, after: str):
    if not re.match(r"^[a-z]+iz(e|es|ed|ing|er|ers|ation|ations|ational|ationally|able)$", lower):
        return None
    if lower in IZE_EXCEPTIONS:
        return None
    idx = lower.rfind("iz")
    return "error", _match_first_case(lower[:idx] + "is" + lower[idx + 2 :], token)


def _rule_yze(token: str, lower: str, before: str, after: str):
    if not re.match(r"^[a-z]+lyz(e|es|ed|ing|er|ers)$", lower):
        return None
    return "error", _match_first_case(lower.replace("lyz", "lys"), token)


def _rule_our(token: str, lower: str, before: str, after: str):
    match = _OUR_RE.match(lower)
    if not match:
        return None
    return "error", _match_first_case(match.group(1) + "our" + (match.group(2) or ""), token)


def _rule_re(token: str, lower: str, before: str, after: str):
    if lower in _RE_FORMS:
        return "error", _match_first_case(_RE_FORMS[lower], token)
    return None


def _rule_ll(token: str, lower: str, before: str, after: str):
    match = _LL_RE.match(lower)
    if match:
        return "error", _match_first_case(match.group(1) + "l" + match.group(2), token)
    if lower in _SINGLE_L_FORMS:
        return "error", _match_first_case(_SINGLE_L_FORMS[lower], token)
    return None


_PROGRAM_SOFTWARE_NEXT = {
    "code", "runs", "run", "running", "ran", "executes", "executed", "execution", "file", "files", "binary",
    "binaries", "source", "crashes", "crashed", "exits", "exited", "starts", "started", "terminates", "terminated",
    "counter", "listing", "output", "loads", "loaded", "compiles", "compiled", "text", "memory", "logic", "flow",
}
_PROGRAM_SOFTWARE_PREV = {
    "computer", "software", "executable", "compiled", "running", "python", "javascript", "typescript", "java",
    "source", "sample", "example", "test", "main", "host", "target", "user", "client", "server", "calling",
    "malicious", "untrusted", "compiler", "interpreter", "console", "command-line", "cli",
}


def _rule_programme(token: str, lower: str, before: str, after: str):
    """``programme`` unless the word is used in a software context (``program
    code``, ``the program runs``, ``a Python program``); then it is accepted."""
    if lower not in ("program", "programs"):
        return None
    previous = re.findall(r"[A-Za-z][A-Za-z-]*", before)
    following = re.findall(r"[A-Za-z][A-Za-z-]*", after)
    if (following and following[0].lower() in _PROGRAM_SOFTWARE_NEXT) or (previous and previous[-1].lower() in _PROGRAM_SOFTWARE_PREV):
        return None
    return "error", _match_first_case("programme" + ("s" if lower.endswith("s") else ""), token)


def _rule_licence(token: str, lower: str, before: str, after: str):
    if lower not in ("license", "licenses"):
        return None
    previous = re.findall(r"[A-Za-z][A-Za-z-]*", before)
    suggestion = _match_first_case("licence" + ("s" if lower.endswith("s") else ""), token)
    if previous and previous[-1].lower() in _LICENCE_DETERMINERS:
        return "error", suggestion
    return "warning", f"{suggestion} if a noun ('to license' is correct in en-GB)"


def _rule_artefact(token: str, lower: str, before: str, after: str):
    # Lower-case only: ``Artifact`` is an entity type name, ``ArtifactRequirement``
    # and ``artifact_types`` are identifiers (never tokenised as prose words).
    if token in ("artifact", "artifacts"):
        return "error", "artefact" + ("s" if token.endswith("s") else "")
    return None


def _rule_misc(token: str, lower: str, before: str, after: str):
    if lower in _MISC_ERRORS:
        return "error", _match_first_case(_MISC_ERRORS[lower], token)
    if lower in _MISC_WARNINGS:
        return "warning", _MISC_WARNINGS[lower]
    return None


Rule = Callable[[str, str, str, str], Optional[Tuple[str, str]]]

# The single place where the en-GB rules live. Each rule receives the token as
# written, its lower-case form, and the masked text before/after it on the
# line; it returns (severity, suggestion) or None. ``fixable`` marks rules whose
# suggestion is an unambiguous replacement (used by ``--fix``; warnings are
# never fixed).
SPELLING_RULES: Dict[str, Dict[str, object]] = {
    "ise": {"rule": _rule_ize, "message": "-ise / -isation (en-GB); exceptions: size, prize, seize, capsize", "fixable": True},
    "yse": {"rule": _rule_yze, "message": "-yse (analyse, catalyse, paralyse)", "fixable": True},
    "our": {"rule": _rule_our, "message": "-our (colour, behaviour, flavour, honour, labour, favour, neighbour)", "fixable": True},
    "re": {"rule": _rule_re, "message": "-re (centre, litre, fibre, kilometre)", "fixable": True},
    "ll": {"rule": _rule_ll, "message": "-ll- before a suffix (modelling, labelled, travelled, cancelled); single l in enrol, fulfil", "fixable": True},
    "programme": {"rule": _rule_programme, "message": "programme — 'program' only in a software context (program code, the program runs)", "fixable": False},
    "licence": {"rule": _rule_licence, "message": "licence is the noun in en-GB; license is the verb", "fixable": True},
    "artefact": {"rule": _rule_artefact, "message": "artefact in prose (Artifact / ArtifactRequirement / artifact_types are identifiers)", "fixable": True},
    "misc": {"rule": _rule_misc, "message": "miscellaneous en-GB spellings", "fixable": True},
}

_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_])([A-Za-z]+)(?![A-Za-z0-9_])")


def _prose_cased(token: str) -> bool:
    """Only all-lower or Capitalised words are prose; ``CamelCase``/``ALLCAPS`` are identifiers."""
    return token.islower() or (token[:1].isupper() and token[1:].islower())


@dataclass
class Finding:
    path: str
    line: int
    col: int
    rule: str
    token: str
    suggestion: str
    severity: str
    message: str

    def format(self) -> str:
        flag = "" if self.severity == "error" else f"  [{self.severity}]"
        return f"{self.path}:{self.line}:{self.col}  {self.rule}  {self.token!r} -> {self.suggestion!r}{flag}"


def normalise_form_en_gb(form: str) -> str:
    """The en-GB spelling of a registry form: every prose-cased word that a rule
    flags as an error with a one-word suggestion is replaced (``normalized
    ontology`` -> ``normalised ontology``). Spelling is style, never terminology,
    so the registry keeps the papers' form and the prose must use this one."""
    out = form
    for match in reversed(list(_TOKEN_RE.finditer(form))):
        token = match.group(1)
        if not _prose_cased(token):
            continue
        start, end = match.span(1)
        for spec in SPELLING_RULES.values():
            result = spec["rule"](token, token.lower(), form[:start], form[end:])  # type: ignore[operator]
            if result and result[0] == "error" and " " not in result[1]:
                out = out[:start] + result[1] + out[end:]
                break
    return out


def ame_registry_forms(registry: Optional[dict]) -> List[Tuple[str, str, str]]:
    """(key, form, en-GB form) for every authoritative registry form whose
    spelling is not en-GB. Sorted; informative only."""
    found: Set[Tuple[str, str, str]] = set()
    for entry in (registry or {}).get("terms", []):
        if not isinstance(entry, dict) or entry.get("state") not in AUTHORITATIVE_STATES:
            continue
        for form in _forms(entry, "en"):
            normalised = normalise_form_en_gb(form)
            if normalised != form:
                found.add((str(entry.get("key")), form, normalised))
    return sorted(found)


class ExemptionIndex:
    """Spans of a line that spelling must not touch: protected tokens,
    ``do-not-translate`` forms verbatim, and authoritative registry forms in
    their en-GB spelling (an AmE-spelled registry form exempts nothing as
    written: the prose has to use the en-GB spelling)."""

    def __init__(self, registry: Optional[dict]) -> None:
        dnt: List[str] = []
        auth: List[str] = []
        for entry in (registry or {}).get("terms", []):
            if not isinstance(entry, dict):
                continue
            state = entry.get("state")
            if state == "do-not-translate":
                dnt.extend(_forms(entry, "en"))
            elif state in AUTHORITATIVE_STATES:
                auth.extend(normalise_form_en_gb(f) for f in _forms(entry, "en"))
        self.ame_forms = ame_registry_forms(registry)
        self.patterns: List[re.Pattern] = [protected_tokens.ID_PATTERN, protected_tokens.ACRONYM_PATTERN]
        for pattern in (_word_regex(dnt, ignore_case=False), _word_regex(auth, ignore_case=True)):
            if pattern is not None:
                self.patterns.append(pattern)

    def spans(self, text: str) -> List[Tuple[int, int]]:
        out: List[Tuple[int, int]] = []
        for pattern in self.patterns:
            out.extend(m.span() for m in pattern.finditer(text))
        return out


def spelling_findings_for_text(text: str, path: str, exemptions: ExemptionIndex, *, where: str = "<text>") -> List[Finding]:
    lines, _blocks = extract_prose(text, where=where)
    findings: List[Finding] = []
    for prose in lines:
        exempt = exemptions.spans(prose.text)
        for match in _TOKEN_RE.finditer(prose.text):
            token = match.group(1)
            start, end = match.span(1)
            if any(s <= start and end <= e for s, e in exempt):
                continue
            if not _prose_cased(token):
                continue
            lower = token.lower()
            before = prose.text[:start]
            after = prose.text[end:]
            for name, spec in SPELLING_RULES.items():
                result = spec["rule"](token, lower, before, after)  # type: ignore[operator]
                if result is None:
                    continue
                severity, suggestion = result
                findings.append(Finding(path, prose.line, start + 1, name, token, suggestion, severity, str(spec["message"])))
                break
    return findings


def apply_fixes(text: str, findings: List[Finding]) -> str:
    """Replace fixable error tokens in the raw text (columns are exact because
    the masked line has the same length as the raw line)."""
    lines = text.split("\n")
    by_line: Dict[int, List[Finding]] = {}
    for f in findings:
        if f.severity != "error" or not SPELLING_RULES[f.rule]["fixable"]:
            continue
        by_line.setdefault(f.line, []).append(f)
    for lineno, items in by_line.items():
        line = lines[lineno - 1]
        for f in sorted(items, key=lambda x: -x.col):
            start = f.col - 1
            end = start + len(f.token)
            if line[start:end] != f.token:
                continue
            line = line[:start] + f.suggestion + line[end:]
        lines[lineno - 1] = line
    return "\n".join(lines)


def cmd_spelling(args) -> int:
    registry = load_registry(args.registry) if args.registry else None
    exemptions = ExemptionIndex(registry)
    root = _root_or_none()
    files = iter_files(args.path)
    all_findings: List[Finding] = []
    for path in files:
        text = common.read_text(path)
        shown = display_path(path, root)
        findings = spelling_findings_for_text(text, shown, exemptions, where=shown)
        if args.fix and findings:
            fixed = apply_fixes(text, findings)
            if fixed != text:
                with open(path, "w", encoding="utf-8", newline="") as handle:
                    handle.write(fixed)
        all_findings.extend(findings)
    all_findings.sort(key=lambda f: (f.path, f.line, f.col))
    for f in all_findings:
        print(f.format())
    errors = sum(1 for f in all_findings if f.severity == "error")
    warnings = len(all_findings) - errors
    if exemptions.ame_forms:
        print(f"note: {len(exemptions.ame_forms)} registry forms are AmE-spelled; en-GB expected in prose")
    print(f"spelling: {len(files)} file(s), {errors} error(s), {warnings} warning(s)" + (" — fixes applied" if args.fix else ""))
    return 1 if errors and not args.fix else 0


# --------------------------------------------------------------------------- #
# pending-blocks
# --------------------------------------------------------------------------- #


def pending_needles(registry: dict, source_locale: str = "pt") -> Dict[str, re.Pattern]:
    """key -> whole-word regex over the source-locale forms of blocking pending entries."""
    needles: Dict[str, re.Pattern] = {}
    for entry in registry.get("terms", []):
        if not isinstance(entry, dict) or entry.get("state") != "pending" or not entry.get("blocks_translation"):
            continue
        pattern = _word_regex(_forms(entry, source_locale), ignore_case=True)
        if pattern is not None:
            needles[str(entry["key"])] = pattern
    return needles


def _excerpt(text: str, match: re.Match, width: int = 90) -> str:
    start = max(0, match.start() - width // 2)
    end = min(len(text), match.end() + width // 2)
    piece = text[start:end].strip()
    return ("…" if start > 0 else "") + piece + ("…" if end < len(text) else "")


def pending_blocks_for_text(text: str, needles: Dict[str, re.Pattern], *, where: str = "<text>") -> Tuple[int, List[Tuple[Block, str, str]]]:
    """(total blocks, [(block, key, excerpt)]) for one document."""
    _lines, blocks = extract_prose(text, where=where)
    hits: List[Tuple[Block, str, str]] = []
    for block in blocks:
        haystack = common.nfc(block.text)
        for key in sorted(needles):
            match = needles[key].search(haystack)
            if match:
                hits.append((block, key, _excerpt(haystack, match)))
    return len(blocks), hits


def cmd_pending_blocks(args) -> int:
    registry = load_registry(args.registry)
    needles = pending_needles(registry, args.source_locale)
    root = _root_or_none()
    files = iter_files(args.path)
    per_file: Dict[str, Tuple[int, int]] = {}
    per_key: Dict[str, int] = {k: 0 for k in needles}
    report: Dict[str, List[dict]] = {}
    for path in files:
        shown = display_path(path, root)
        total, hits = pending_blocks_for_text(common.read_text(path), needles, where=shown)
        blocked_lines: Set[int] = set()
        for block, key, excerpt in hits:
            blocked_lines.add(id(block))
            per_key[key] += 1
            if not args.json:
                print(f"{shown}:{block.line}  {key}  {excerpt}")
            report.setdefault(shown, []).append({"line": block.line, "kind": block.kind, "key": key, "excerpt": excerpt})
        per_file[shown] = (total, len(blocked_lines))
    if args.json:
        print(json.dumps({"files": {k: {"blocks": v[0], "blocked": v[1], "hits": report.get(k, [])} for k, v in per_file.items()}, "keys": per_key}, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    print()
    print("per file (blocks / blocked):")
    for shown in sorted(per_file):
        total, blocked = per_file[shown]
        if blocked or args.all_files:
            print(f"  {shown}: {total} / {blocked}")
    print("per key:")
    for key in sorted(per_key):
        print(f"  {key}: {per_key[key]}")
    files_blocked = sum(1 for v in per_file.values() if v[1])
    total_blocks = sum(v[0] for v in per_file.values())
    total_blocked = sum(v[1] for v in per_file.values())
    print(f"pending-blocks: {len(files)} file(s), {files_blocked} with blocks blocked; {total_blocked} / {total_blocks} blocks blocked; {len(needles)} blocking key(s)")
    return 1 if (args.fail_on_block and total_blocked) else 0


# --------------------------------------------------------------------------- #
# consistency
# --------------------------------------------------------------------------- #


def cmd_consistency(args) -> int:
    registry = load_registry(args.registry)
    root = _root_or_none()
    docs_dir = args.docs_dir or common.default_docs_dir(root or common.repo_root())
    mirror_root = common.existing_path(args.path)
    if not mirror_root.exists():
        common.warn(f"no {args.target_locale} files under {args.path}; nothing to check")
        print("consistency: 0 file(s)")
        return 0
    files = iter_files(mirror_root)
    if not files:
        common.warn(f"no {args.target_locale} files under {args.path}; nothing to check")
        print("consistency: 0 file(s)")
        return 0

    checks: List[Tuple[str, re.Pattern, re.Pattern, str]] = []  # key, source needle, expected forms, pt canonical
    for entry in registry.get("terms", []):
        if not isinstance(entry, dict) or entry.get("state") not in AUTHORITATIVE_STATES:
            continue
        source_forms = _forms(entry, args.source_locale)
        target_forms = _forms(entry, args.target_locale)
        source_re = _word_regex(source_forms, ignore_case=True)
        target_re = _word_regex(target_forms, ignore_case=True)
        if source_re is None or target_re is None:
            continue
        untranslated = None
        leftovers = [f for f in source_forms if f.casefold() not in {t.casefold() for t in target_forms}]
        if leftovers:
            untranslated = _word_regex(leftovers, ignore_case=True)
        checks.append((str(entry["key"]), source_re, target_re, untranslated))

    errors = 0
    warnings = 0
    mirror_base = mirror_root if mirror_root.is_dir() else mirror_root.parent
    for target_path in files:
        shown = display_path(target_path, root)
        if mirror_root.is_dir():
            rel = common.rel_to_docs(target_path, mirror_base)
        else:
            rel = common.nfc(target_path.name)
        source_path = common.source_path(rel, docs_dir) if mirror_root.is_dir() else (args.source_path or None)
        if source_path is None or not Path(source_path).exists():
            common.warn(f"{shown}: no source counterpart under {docs_dir}; checked per file only for untranslated forms")
            source_blocks = None
        else:
            _l, source_blocks = extract_prose(common.read_text(source_path), where=str(source_path))
        _l, target_blocks = extract_prose(common.read_text(target_path), where=shown)
        target_all = common.nfc(" ".join(b.text for b in target_blocks))
        aligned = source_blocks is not None and len(source_blocks) == len(target_blocks)
        for key, source_re, target_re, untranslated in checks:
            if source_blocks is not None:
                for index, sblock in enumerate(source_blocks):
                    if not source_re.search(common.nfc(sblock.text)):
                        continue
                    haystack = common.nfc(target_blocks[index].text) if aligned else target_all
                    if not target_re.search(haystack):
                        errors += 1
                        line = target_blocks[index].line if aligned else sblock.line
                        scope = "block" if aligned else "file"
                        print(f"{shown}:{line}  {key}  source form present, no en form in the {scope}")
                        if not aligned:
                            break
            if untranslated is not None:
                for tblock in target_blocks:
                    match = untranslated.search(common.nfc(tblock.text))
                    if match:
                        warnings += 1
                        print(f"{shown}:{tblock.line}  {key}  source form {match.group(0)!r} left in the {args.target_locale} text  [warning]")
    print(f"consistency: {len(files)} file(s), {errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


# --------------------------------------------------------------------------- #
# export-pending
# --------------------------------------------------------------------------- #


def _cell(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return "; ".join(_cell(v) for v in value)
    text = str(value).replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    return re.sub(r"\s+", " ", text).strip()


def _truncate(text: str, width: int = 140) -> str:
    return text if len(text) <= width else text[: width - 1].rstrip() + "…"


def export_pending_markdown(registry: dict, registry_hash: Optional[str] = None) -> str:
    by_key = {e.get("key"): e for e in registry.get("terms", []) if isinstance(e, dict)}
    pending = [e for e in by_key.values() if e.get("state") == "pending"]
    lines: List[str] = []
    lines.append("# Fila de termos `pending` — export para o hub")
    lines.append("")
    lines.append("Gerado por `translation/scripts/terms_lint.py export-pending` a partir de `translation/terms/registry.yaml`.")
    if registry_hash:
        lines.append(f"`terms_sha256` do registo: `{registry_hash}`.")
    lines.append("")
    lines.append("**Como responder:** no hub (`sbd-ai-runtime/handover/em-curso/`), por chave → EN decidido (e, se aplicável, PT). ")
    lines.append("O Manual agent regista a decisão no registo: espécie 2 passa a `coined` (com `ratified_by` e `date`); espécie 1 passa a ")
    lines.append("`in-record` ou `changed` (com `previous`). Enquanto `pending`, os blocos da fonte que contêm o termo não são traduzidos.")
    lines.append("")
    lines.append(f"Total pendente: {len(pending)}.")
    for owner in OWNER_ORDER:
        items = sorted((e for e in pending if e.get("owner") == owner), key=lambda e: str(e.get("key")))
        lines.append("")
        lines.append(f"## `owner: {owner}` ({len(items)})")
        lines.append("")
        if not items:
            lines.append("_Sem entradas._")
            continue
        lines.append("| chave | espécie | razão | PT | EN actual | proposal | false_friends | senses |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for e in items:
            friends = []
            for friend in e.get("false_friends") or ():
                ref = by_key.get(friend)
                sense = _truncate(_cell(ref.get("sense")), 80) if ref else "chave desconhecida"
                friends.append(f"`{friend}` ({sense})" if sense else f"`{friend}`")
            senses = " · ".join(_truncate(_cell(s.get("sense") if isinstance(s, dict) else s), 100) for s in (e.get("senses") or ()))
            pt = _cell(e.get("pt"))
            if e.get("pt_variants"):
                pt = f"{pt} ({_cell(e.get('pt_variants'))})" if pt else _cell(e.get("pt_variants"))
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{_cell(e.get('key'))}`",
                        _cell(e.get("species")),
                        _cell(e.get("pending_reason")),
                        pt,
                        _cell(e.get("en")),
                        _cell(e.get("proposal")),
                        "; ".join(friends),
                        senses,
                    ]
                )
                + " |"
            )
    lines.append("")
    return "\n".join(lines)


def cmd_export_pending(args) -> int:
    registry = load_registry(args.registry)
    text = export_pending_markdown(registry, registry_sha256(args.registry))
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(common.normalise_text(text))
        print(f"export-pending: wrote {args.out}")
    else:
        print(text, end="")
    return 0


# --------------------------------------------------------------------------- #
# validate / hash commands
# --------------------------------------------------------------------------- #


def cmd_validate(args) -> int:
    registry = load_registry(args.registry)
    problems = validate_registry(registry)
    for problem in problems:
        print(f"error: {problem}")
    terms = registry.get("terms", [])
    print(f"validate: {len(terms)} entries, {len(problems)} problem(s)")
    return 1 if problems else 0


def cmd_hash(args) -> int:
    digest = registry_sha256(args.registry)
    raw = hashlib.sha256(Path(args.registry).read_bytes()).hexdigest()
    if raw != digest:
        common.warn("registry bytes are not normalised (BOM / CRLF / trailing whitespace); sync_state.py hashes the normalised content — re-run terms_import.py to normalise")
    print(digest)
    return 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _root_or_none() -> Optional[Path]:
    try:
        return common.repo_root()
    except common.TranslationToolError:
        return None


def _default_registry() -> Optional[Path]:
    root = _root_or_none()
    return (root / common.TERMS_REGISTRY_RELPATH) if root else None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    def add_registry(p, required: bool) -> None:
        p.add_argument("--registry", type=Path, default=_default_registry() if not required else None, required=required and _default_registry() is None,
                       help=f"terms registry (default: <repo>/{common.TERMS_REGISTRY_RELPATH})")

    p = sub.add_parser("validate", help="check the registry against the schema")
    add_registry(p, True)
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("spelling", help="en-GB spelling over EN prose")
    p.add_argument("--path", type=Path, required=True, help="EN file or directory")
    add_registry(p, False)
    p.add_argument("--fix", action="store_true", help="apply unambiguous replacements in place (errors of fixable rules only)")
    p.set_defaults(func=cmd_spelling)

    p = sub.add_parser("pending-blocks", help="blocks of the source text that contain a blocking pending term")
    p.add_argument("--path", type=Path, required=True, help="source-locale file or directory")
    add_registry(p, True)
    p.add_argument("--source-locale", default=common.DEFAULT_SOURCE_LOCALE)
    p.add_argument("--json", action="store_true", help="machine-readable report")
    p.add_argument("--all-files", action="store_true", help="list every file in the per-file summary, not only those with blocked blocks")
    p.add_argument("--fail-on-block", action="store_true", help="exit 1 when any block is blocked")
    p.set_defaults(func=cmd_pending_blocks)

    p = sub.add_parser("consistency", help="same source form -> registered en form in the mirror")
    p.add_argument("--path", type=Path, required=True, help="mirror directory (or a single mirror file with --source-path)")
    add_registry(p, True)
    p.add_argument("--source-locale", default=common.DEFAULT_SOURCE_LOCALE)
    p.add_argument("--target-locale", default=common.DEFAULT_TARGET_LOCALE)
    p.add_argument("--docs-dir", type=Path, default=None, help="source corpus root (default: <repo>/manuals_src/docs/sbd-toe)")
    p.add_argument("--source-path", type=Path, default=None, help="source file when --path is a single file")
    p.set_defaults(func=cmd_consistency)

    p = sub.add_parser("export-pending", help="Markdown queue of pending entries, one table per owner")
    add_registry(p, True)
    p.add_argument("--out", type=Path, default=None, help="output file (default: stdout)")
    p.set_defaults(func=cmd_export_pending)

    p = sub.add_parser("hash", help="SHA-256 of the registry as sync_state.py records it")
    add_registry(p, True)
    p.set_defaults(func=cmd_hash)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if getattr(args, "registry", None) is None and args.command != "spelling":
        print("error: --registry is required (repository root not found)", file=sys.stderr)
        return 2
    try:
        return args.func(args)
    except common.TranslationToolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
