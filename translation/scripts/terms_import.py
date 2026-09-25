#!/usr/bin/env python3
"""Seed or refresh ``translation/terms/registry.yaml`` from the Curator's survey.

The importer is mechanical: it applies the seeding rules of
``translation/terms/README.md`` ("Espécie 1 — como se semeia a partir do
Curator") and decides no terminology. The YAML survey is authoritative; the CSV
is only hashed (both files are immutable inputs, so their SHA-256 is recorded
in ``meta.curator_input_sha256``).

Rules applied to every survey row (see ``seed_entry``):

* ``key``: the Curator ``id`` normalised to lower-case ASCII snake_case
  (``ControlObjective`` -> ``control_objective``). One override exists,
  ``AppSecCore`` -> ``appsec_core``, because that is the programme's own
  snake_case spelling of the name (``formal/appsec_core/``); a plain CamelCase
  split would give ``app_sec_core``. The original id is kept in ``curator.id``.
* ``state``: ``do-not-translate`` for ``origem: nao-traduzir``; ``pending`` +
  ``pending_reason: polysemy`` for ``multiplos_sentidos: true`` (``senses``
  filled from the survey); ``traversal`` is ``pending`` +
  ``en-vs-en-collision`` (it is also polysemous, so its ``senses`` are kept);
  everything else ``in-record``.
* ``contract_generic`` unfolds into ``manual_mapping_contract`` and
  ``consumer_contract`` (the second and third forms of its ``termo_en``);
  ``slice_contract`` and ``retrieval_contract`` already exist as rows.
* ``en``: first form of ``termo_en`` before `` / `` with any parenthetical
  removed; ``en_variants``: the survey ``variantes`` without counts,
  de-duplicated case-insensitively (first spelling kept), minus the canonical
  form.
* ``pt``: ``pt_conceito`` only when ``pt_status == inequivoco`` (verbatim, even
  when it lists alternatives with `` / ``), otherwise ``null``;
  ``pt_variants`` is always empty at seeding.
* ``evidence`` from ``citacao``; ``counts`` from ``por_paper`` plus ``total``
  (= ``total_manuscritos_P0_P7``); ``change_cost`` from ``custo_de_mudanca``.

Re-running never overwrites ``state``, ``en``, ``en_variants``, ``pt``,
``pt_variants``, ``previous``, ``proposal``, ``false_friends``,
``pending_reason``, ``blocks_translation``, ``notes`` (nor ``sense``,
``senses``, ``ontology_id``, ``owner``, ``species``) of an existing entry; only
``counts``, ``evidence``, ``curator`` and ``change_cost`` are refreshed, as the
README prescribes.

Output is deterministic: schema key order, entries sorted by ``key``,
``allow_unicode``, width 100, block style with flow-style lists of scalars, a
single trailing newline.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402

# --------------------------------------------------------------------------- #
# Schema (translation/terms/README.md)
# --------------------------------------------------------------------------- #

ENTRY_KEYS: Tuple[str, ...] = (
    "key",
    "species",
    "state",
    "owner",
    "en",
    "en_variants",
    "pt",
    "pt_variants",
    "ontology_id",
    "sense",
    "senses",
    "evidence",
    "counts",
    "change_cost",
    "curator",
    "previous",
    "proposal",
    "false_friends",
    "pending_reason",
    "blocks_translation",
    "notes",
)

# Fields the importer never touches on an existing entry (README, "Espécie 1").
PRESERVED_ON_RERUN: Tuple[str, ...] = tuple(k for k in ENTRY_KEYS if k not in ("counts", "evidence", "curator", "change_cost"))

META_DEFAULTS = {"version": 1, "spelling": "en-GB", "source_locale": "pt", "target_locale": "en"}

# Curator id -> registry key when the mechanical CamelCase split would not give
# the programme's own snake_case spelling of the name.
KEY_OVERRIDES: Dict[str, str] = {"AppSecCore": "appsec_core"}

# Rows that unfold into several entries: Curator id -> [(key, index of the form
# in ``termo_en`` that becomes ``en``)]. Forms are counted after parentheticals
# are removed and the string is split on " / ".
UNFOLD: Dict[str, List[Tuple[str, int]]] = {
    "contract_generic": [("manual_mapping_contract", 1), ("consumer_contract", 2)],
}

# Rows whose EN already collides with an EN name inside the programme
# (README: "traversal -> pending, en-vs-en-collision").
EN_VS_EN_COLLISION: Tuple[str, ...] = ("traversal",)

STATE_DO_NOT_TRANSLATE = "do-not-translate"
STATE_PENDING = "pending"
STATE_IN_RECORD = "in-record"


class ImportError_(common.TranslationToolError):
    """Raised when the survey cannot be applied mechanically."""


# --------------------------------------------------------------------------- #
# Normalisation helpers
# --------------------------------------------------------------------------- #

_CAMEL_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
_NON_KEY_RE = re.compile(r"[^a-z0-9]+")
_PAREN_RE = re.compile(r"\s*\([^()]*\)")


def normalise_key(curator_id: str) -> str:
    """Lower-case ASCII snake_case of a Curator id (``ControlObjective`` -> ``control_objective``)."""
    if curator_id in KEY_OVERRIDES:
        return KEY_OVERRIDES[curator_id]
    text = _CAMEL_RE.sub("_", curator_id)
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = _NON_KEY_RE.sub("_", text).strip("_")
    if not text:
        raise ImportError_(f"cannot derive a key from Curator id {curator_id!r}")
    return text


def termo_en_forms(termo_en: str) -> List[str]:
    """Forms of ``termo_en``: parentheticals removed, split on " / ", stripped."""
    text = _PAREN_RE.sub("", termo_en)
    forms = [part.strip() for part in text.split(" / ")]
    return [f for f in forms if f]


def canonical_en(termo_en: str, form_index: int = 0) -> str:
    forms = termo_en_forms(termo_en)
    if form_index >= len(forms):
        raise ImportError_(f"termo_en {termo_en!r} has no form #{form_index}")
    return forms[form_index]


def en_variants_from(variantes, en: str) -> List[str]:
    """Survey ``variantes`` (mapping form -> count, in survey order) without
    counts, de-duplicated case-insensitively, minus the canonical form."""
    seen = {en.casefold()}
    out: List[str] = []
    for form in variantes or ():
        form = str(form).strip()
        folded = form.casefold()
        if not form or folded in seen:
            continue
        seen.add(folded)
        out.append(form)
    return out


def evidence_from(citacao: Optional[dict]) -> Optional[dict]:
    if not citacao:
        return None
    return {
        "paper": citacao.get("paper"),
        "line": citacao.get("line"),
        "section": citacao.get("section"),
        "quote": citacao.get("text"),
    }


def senses_from(sentidos) -> List[dict]:
    out: List[dict] = []
    for item in sentidos or ():
        where = evidence_from(item.get("q")) if isinstance(item, dict) else None
        out.append({"sense": item.get("s") if isinstance(item, dict) else str(item), "where": where})
    return out


def counts_from(row: dict) -> dict:
    counts = {}
    for paper, value in (row.get("por_paper") or {}).items():
        counts[str(paper)] = int(value)
    counts["total"] = int(row.get("total_manuscritos_P0_P7") or 0)
    return counts


# --------------------------------------------------------------------------- #
# Seeding
# --------------------------------------------------------------------------- #


def seed_entry(row: dict, *, key: Optional[str] = None, form_index: int = 0, note: str = "") -> dict:
    """Build a fresh registry entry for one survey row (or one unfolded form)."""
    curator_id = str(row["id"])
    en = canonical_en(str(row["termo_en"]), form_index)
    origem = row.get("origem")
    polysemous = bool(row.get("multiplos_sentidos"))
    pt_status = row.get("pt_status")

    if origem == "nao-traduzir":
        state, reason = STATE_DO_NOT_TRANSLATE, None
    elif curator_id in EN_VS_EN_COLLISION:
        state, reason = STATE_PENDING, "en-vs-en-collision"
    elif polysemous:
        state, reason = STATE_PENDING, "polysemy"
    else:
        state, reason = STATE_IN_RECORD, None

    pt = row.get("pt_conceito") if pt_status == "inequivoco" else None

    return {
        "key": key or normalise_key(curator_id),
        "species": 1,
        "state": state,
        "owner": "manual-agent",
        "en": en,
        "en_variants": en_variants_from(row.get("variantes"), en),
        "pt": pt,
        "pt_variants": [],
        "ontology_id": None,
        "sense": row.get("sentido"),
        "senses": senses_from(row.get("sentidos")) if polysemous else [],
        "evidence": evidence_from(row.get("citacao")),
        "counts": counts_from(row),
        "change_cost": row.get("custo_de_mudanca"),
        "curator": {"id": curator_id, "grupo": row.get("grupo"), "origem": origem, "pt_status": pt_status},
        "previous": None,
        "proposal": None,
        "false_friends": [],
        "pending_reason": reason,
        "blocks_translation": True,
        "notes": note,
    }


def seed_entries(rows: List[dict]) -> List[dict]:
    """All fresh entries for the survey, unfolding where the README says so."""
    entries: List[dict] = []
    for row in rows:
        curator_id = str(row["id"])
        if curator_id in UNFOLD:
            for key, form_index in UNFOLD[curator_id]:
                note = f"Unfolded from Curator row `{curator_id}` (README, Espécie 1)."
                entries.append(seed_entry(row, key=key, form_index=form_index, note=note))
        else:
            entries.append(seed_entry(row))
    keys = [e["key"] for e in entries]
    duplicates = sorted({k for k in keys if keys.count(k) > 1})
    if duplicates:
        raise ImportError_(f"duplicate registry keys derived from the survey: {duplicates}")
    return entries


def merge(existing: Optional[dict], fresh: dict) -> dict:
    """Existing entry wins for every preserved field; the rest is refreshed."""
    if existing is None:
        return order_entry(fresh)
    merged = dict(fresh)
    for field in PRESERVED_ON_RERUN:
        if field in existing:
            merged[field] = existing[field]
    return order_entry(merged)


def order_entry(entry: dict) -> dict:
    ordered = {k: entry.get(k) for k in ENTRY_KEYS}
    extra = [k for k in entry if k not in ENTRY_KEYS]
    for k in extra:  # unknown keys are kept (validate reports them), after the schema ones
        ordered[k] = entry[k]
    return ordered


def raw_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_registry(rows: List[dict], existing: Optional[dict], input_hashes: Dict[str, str]) -> dict:
    existing_terms = {e["key"]: e for e in (existing or {}).get("terms", []) if isinstance(e, dict) and "key" in e}
    fresh = seed_entries(rows)
    fresh_keys = {e["key"] for e in fresh}
    merged = [merge(existing_terms.get(e["key"]), e) for e in fresh]
    # Entries that exist in the registry but not in the survey (species 2/3,
    # authored by hand) are kept untouched.
    merged.extend(order_entry(e) for k, e in existing_terms.items() if k not in fresh_keys)
    merged.sort(key=lambda e: e["key"])

    meta = dict(META_DEFAULTS)
    if existing and isinstance(existing.get("meta"), dict):
        for k, v in existing["meta"].items():
            if k != "curator_input_sha256":
                meta[k] = v
    meta["curator_input_sha256"] = {k: input_hashes[k] for k in sorted(input_hashes)}
    return {"meta": meta, "terms": merged}


# --------------------------------------------------------------------------- #
# Deterministic YAML
# --------------------------------------------------------------------------- #


class _Dumper(yaml.SafeDumper):
    pass


def _represent_none(dumper, _value):
    return dumper.represent_scalar("tag:yaml.org,2002:null", "null")


def _represent_list(dumper, value):
    flow = all(isinstance(v, (str, int, float, bool)) or v is None for v in value)
    return dumper.represent_sequence("tag:yaml.org,2002:seq", value, flow_style=flow)


def _represent_dict(dumper, value):
    # Small flat mappings (counts, curator, hashes) read better on one line.
    scalars = all(isinstance(v, (int, float, bool)) or v is None or (isinstance(v, str) and "\n" not in v) for v in value.values())
    width = sum(len(str(k)) + len(str(v)) + 4 for k, v in value.items())
    return dumper.represent_mapping("tag:yaml.org,2002:map", value, flow_style=bool(value) and scalars and width <= 90)


def _represent_str(dumper, value):
    style = None
    if "\n" in value:
        style = "|"
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(type(None), _represent_none)
_Dumper.add_representer(list, _represent_list)
_Dumper.add_representer(dict, _represent_dict)
_Dumper.add_representer(str, _represent_str)


def dump_registry(registry: dict) -> str:
    text = yaml.dump(
        registry,
        Dumper=_Dumper,
        sort_keys=False,
        allow_unicode=True,
        width=100,
        default_flow_style=False,
    )
    return common.normalise_text(text)


def load_registry(path: Path) -> Optional[dict]:
    if not path.is_file():
        return None
    data = common.yaml_load(common.read_text(path))
    if data is None:
        return None
    if not isinstance(data, dict) or "terms" not in data:
        raise ImportError_(f"{path}: not a registry (expected a mapping with 'terms')")
    return data


def load_survey(path: Path) -> List[dict]:
    data = common.yaml_load(common.read_text(path))
    rows = data.get("termos") if isinstance(data, dict) else None
    if not isinstance(rows, list) or not rows:
        raise ImportError_(f"{path}: expected a 'termos' list")
    for row in rows:
        for required in ("id", "termo_en", "origem", "pt_status"):
            if required not in row:
                raise ImportError_(f"{path}: row without '{required}': {row.get('id')!r}")
    return rows


def sibling_csv(yaml_path: Path) -> Optional[Path]:
    csv_path = yaml_path.with_suffix(".csv")
    return csv_path if csv_path.is_file() else None


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, required=True, help="Curator survey YAML (authoritative)")
    parser.add_argument("--csv", type=Path, default=None, help="Curator survey CSV (hashed only; default: sibling of --input)")
    parser.add_argument("--registry", type=Path, default=None, help=f"registry to seed/refresh (default: <repo>/{common.TERMS_REGISTRY_RELPATH})")
    parser.add_argument("--dry-run", action="store_true", help="print a summary and the diff status; write nothing")
    parser.add_argument("--quiet", action="store_true", help="print nothing on success")
    return parser


def summarise(registry: dict) -> str:
    terms = registry["terms"]
    by_state: Dict[str, int] = {}
    by_species: Dict[int, int] = {}
    for e in terms:
        by_state[e["state"]] = by_state.get(e["state"], 0) + 1
        by_species[e["species"]] = by_species.get(e["species"], 0) + 1
    lines = [f"entries: {len(terms)}"]
    lines.append("by species: " + ", ".join(f"{k}={v}" for k, v in sorted(by_species.items())))
    lines.append("by state: " + ", ".join(f"{k}={v}" for k, v in sorted(by_state.items())))
    lines.append(f"pt filled: {sum(1 for e in terms if e['pt'] is not None)}, pt null: {sum(1 for e in terms if e['pt'] is None)}")
    return "\n".join(lines)


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = common.repo_root()
    except common.TranslationToolError:
        root = Path.cwd()
    registry_path = args.registry or (root / common.TERMS_REGISTRY_RELPATH)
    csv_path = args.csv or sibling_csv(args.input)

    try:
        rows = load_survey(args.input)
        existing = load_registry(registry_path)
        hashes = {"yaml": raw_sha256(args.input)}
        if csv_path is not None:
            hashes["csv"] = raw_sha256(csv_path)
        registry = build_registry(rows, existing, hashes)
        text = dump_registry(registry)
    except common.TranslationToolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    before = common.read_text(registry_path) if registry_path.is_file() else None
    changed = before is None or common.normalise_text(before) != text
    if not args.quiet:
        print(summarise(registry))
        print(f"registry: {registry_path} ({'new' if before is None else 'changed' if changed else 'unchanged'})")
    if args.dry_run:
        return 0
    if changed:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        with open(registry_path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
