#!/usr/bin/env python3
"""Generate the regulatory overlay views of the SbD-ToE Manual.

Writes, from the requirement catalogues (master) and ``002-cross-check-normativo/_contextos-regulatorios.yaml``:

1. the ``lista_ids`` block at the end of ``_contextos-regulatorios.yaml`` (below the GERADO marker);
2. one «Requisitos aplicáveis» page per context, in PT (``002-cross-check-normativo/<pasta>/90-requisitos-aplicaveis.md``)
   and in EN (same path in the i18n mirror, with a ``translation`` block whose hashes follow translate.py assemble).
   Both pages carry ``sbdtoe_generated: reg-requirements-view`` and ``derived_from`` in the front matter.

Usage::

    python scripts/gen_reg_views.py            # write
    python scripts/gen_reg_views.py --check    # exit 1 if anything differs from what would be written
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import reg_context_lib as L  # noqa: E402

sys.path.insert(0, str(L.ROOT / "translation/scripts"))
import common  # noqa: E402
import translate  # noqa: E402


def planned_outputs() -> dict:
    master = L.load_master()
    ctx_doc = L.load_contexts()
    matrices = L.load_matrices()
    lists = L.build_lists(ctx_doc, master)
    head, _tail = L.load_contexts_text()
    out = {L.CTX_FILE: head + L.render_lists_yaml(lists)}
    pages = []
    for ctx in ctx_doc["contextos"]:
        matrix = matrices[L.ctx_acto(ctx)]
        rel = f"{L.XC}/{matrix['pasta']}/{L.VIEW_FILE}"
        pages.append((rel, L.render_view(ctx, ctx_doc, lists, master, matrix, "pt"), L.render_view(ctx, ctx_doc, lists, master, matrix, "en")))
    with_ctx = {L.ctx_acto(c) for c in ctx_doc["contextos"]}
    for acto, matrix in matrices.items():
        if acto not in with_ctx:
            rel = f"{L.XC}/{matrix['pasta']}/{L.COVERAGE_FILE}"
            pages.append((rel, L.render_coverage_page(acto, matrix, ctx_doc, "pt"), L.render_coverage_page(acto, matrix, ctx_doc, "en")))
    for rel, pt, en_body in pages:
        en_path = L.EN_DOCS / rel
        previous = en_path.read_text(encoding="utf-8") if en_path.exists() else None
        meta = L.translation_block(pt, en_body, previous)
        meta["source_path"] = rel
        meta["target_sha256"] = common.content_sha256(en_body)
        lines = en_body.split("\n")
        close = next(i for i in range(1, len(lines)) if lines[i] == "---")
        en = "\n".join(lines[:close] + translate.translation_block_lines(meta) + lines[close:])
        assert common.content_sha256(common.strip_translation_block(en)) == meta["target_sha256"]
        out[L.DOCS / rel] = pt
        out[en_path] = en
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="do not write; exit 1 if any output differs")
    args = ap.parse_args(argv)
    outputs = planned_outputs()
    diffs = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            diffs.append(path)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
    for p in diffs:
        print(("differs: " if args.check else "wrote: ") + str(p.relative_to(L.ROOT)))
    if args.check and diffs:
        print(f"gen_reg_views --check: {len(diffs)} generated file(s) out of date — run python scripts/gen_reg_views.py")
        return 1
    print(f"gen_reg_views: {len(outputs)} file(s), {len(diffs)} {'out of date' if args.check else 'written'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
