"""Shared logic for the regulatory overlay of the SbD-ToE Manual.

Data (see sbd-ai-runtime handover 2026-09-27-cobertura-cross-check/SCHEMAS-finais-contexto-e-matriz.md):

- ``002-cross-check-normativo/_contextos-regulatorios.yaml`` — schema ``sbdtoe-overlay/1``, ``tipo_overlay: regulatorio``:
  contexts, grades, floors (``pisos``), additions and the generated ``lista_ids``.
- ``002-cross-check-normativo/_matriz/<acto>.yaml`` — schema ``sbdtoe-reg-coverage/1``: obligation -> strength -> answer.
- ``translation/sources/eurlex/obrigacoes/<acto>.json`` — official text (PT, sic) of every obligation.

The master is the set of requirement catalogues: every table whose header is ``ID | Nome | L1 | L2 | L3 | …`` in a
non-generated page. The overlay selects and elevates ids of the master; it never defines a master requirement.

Used by ``scripts/gen_reg_views.py`` (writes) and ``scripts/check_reg_context.py`` (verifies, CI).
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "manuals_src/docs/sbd-toe"
EN_DOCS = ROOT / "manuals_src/i18n/en/docusaurus-plugin-content-docs/current"
XC = "002-cross-check-normativo"
CTX_FILE = DOCS / XC / "_contextos-regulatorios.yaml"
MATRIZ_DIR = DOCS / XC / "_matriz"
EURLEX = ROOT / "translation/sources/eurlex"
REGISTRY = ROOT / "translation/terms/registry.yaml"
GEN_MARKER = "# --- GERADO por scripts/gen_reg_views.py — não editar abaixo desta linha ---"
GENERATED_KEY = "sbdtoe_generated"
VIEW_NAME = "reg-requirements-view"
LEVELS = ("L1", "L2", "L3")
REQ_ID = r"[A-Z]{2,4}(?:-[A-Z]{2,4})?-\d{3}"
ACTOS = ("cra", "dora", "nis2", "aiact", "rgpd", "csa")
# context -> folder of its cross-check pages (the generated view lives there)
CTX_FOLDER = {"CTX-NIS2": "nis2", "CTX-DORA": "dora", "CTX-CRA": "cra", "CTX-AIA-RE": "ai-act", "CTX-RGPD": "gdpr"}
VIEW_FILE = "90-requisitos-aplicaveis.md"

sys.path.insert(0, str(ROOT / "translation/scripts"))
import common  # noqa: E402  (i18n helpers: hashing, translation block, glossary hash)


def norm_ws(text: str) -> str:
    return re.sub(r"\s+", " ", common.nfc(text)).strip()


def rel_docs(path: Path) -> str:
    return path.relative_to(DOCS).as_posix()


def is_generated(text: str) -> bool:
    return re.search(r"^" + GENERATED_KEY + r":", text, re.M) is not None


# --------------------------------------------------------------------------- master


def _catalogue_rows(text: str):
    """Yield (id, cells) of every row of a requirement table (header ID | <name> | L1 | L2 | L3 | …)."""
    in_table = False
    for line in text.split("\n"):
        if not line.startswith("|"):
            in_table = False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[0] == "ID" and cells[2:5] == list(LEVELS):
            in_table = True
            continue
        if in_table:
            m = re.fullmatch(r"\**`?(" + REQ_ID + r")`?\**", cells[0])
            if m:
                yield m.group(1), cells


def _strip_md(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[*`]", "", text)).strip()


def load_master() -> Dict[str, dict]:
    """{id: {ficheiro, cap, niveis, nome{pt,en}}} from the PT catalogues (EN names from the mirror)."""
    master: Dict[str, dict] = {}
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if is_generated(text):
            continue
        rel = rel_docs(path)
        rows = list(_catalogue_rows(text))
        if not rows:
            continue
        en_names = {}
        en_path = EN_DOCS / rel
        if en_path.exists():
            en_names = {rid: _strip_md(cells[1]) for rid, cells in _catalogue_rows(en_path.read_text(encoding="utf-8"))}
        m = re.match(r"010-sbd-manual/(\d\d)-", rel)
        cap = m.group(1) if m else None
        for rid, cells in rows:
            if rid in master:
                raise ValueError(f"requisito {rid} definido duas vezes: {master[rid]['ficheiro']} e {rel}")
            master[rid] = {
                "ficheiro": rel,
                "cap": cap,
                "niveis": [lvl for lvl, c in zip(LEVELS, cells[2:5]) if c == "✔"],
                "nome": {"pt": _strip_md(cells[1]), "en": en_names.get(rid)},
            }
    return master


# --------------------------------------------------------------------------- data


def load_contexts_text() -> Tuple[str, str]:
    """(authored part, generated part) of _contextos-regulatorios.yaml."""
    text = CTX_FILE.read_text(encoding="utf-8")
    if GEN_MARKER not in text:
        raise ValueError(f"{CTX_FILE.name}: falta o marcador do bloco gerado")
    head, tail = text.split(GEN_MARKER, 1)
    return head, tail


def load_contexts() -> dict:
    return yaml.safe_load(CTX_FILE.read_text(encoding="utf-8"))


def load_matrices() -> Dict[str, dict]:
    return {a: yaml.safe_load((MATRIZ_DIR / f"{a}.yaml").read_text(encoding="utf-8")) for a in ACTOS}


def load_obligations(path: str) -> Tuple[bytes, dict]:
    raw = (ROOT / path).read_bytes()
    return raw, json.loads(raw)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# --------------------------------------------------------------------------- lista_ids


def _entry(rid: str, origem: str, master: dict, pisos=None, obrigacoes=None, grau=None) -> dict:
    e = {"id": rid, "origem": origem}
    cap = master.get(rid, {}).get("cap")
    if cap and cap != "02":
        e["cap"] = cap
    if grau:
        e["grau"] = grau
    if pisos:
        e["pisos"] = sorted(pisos)
        e["obrigacoes"] = sorted(obrigacoes)
    return e


def build_lists(ctx_doc: dict, master: dict) -> dict:
    """lista_ids per context and grade (see regra_lista in the data)."""
    order = list(master)  # catalogue order (path, then table order)
    base_sel = {lvl: [rid for rid in order if lvl in master[rid]["niveis"]] for lvl in LEVELS}
    graus = {g["id"]: g for g in ctx_doc.get("graus") or []}
    out = {}
    for ctx in ctx_doc["contextos"]:
        per_grade = {}
        keys = [None] + list(ctx.get("graus_admitidos") or [])
        for grade in keys:
            cumulative = grade is None or graus[grade].get("cumulativo", True)
            wanted = {None, grade} if (grade is not None and cumulative) else {grade}
            lists = {}
            for lvl in LEVELS:
                elevated: Dict[str, Tuple[set, set, Optional[str]]] = {}
                for p in ctx.get("pisos") or []:
                    if p["alvo"]["tipo"] != "requisito" or p.get("grau") not in wanted:
                        continue
                    if p.get("niveis") and lvl not in p["niveis"]:
                        continue
                    rid = p["alvo"]["alvo"]
                    ps, obs, g = elevated.get(rid, (set(), set(), None))
                    ps.add(p["id"])
                    obs.update(p["base"]["obrigacoes"])
                    g = p.get("grau") or g
                    elevated[rid] = (ps, obs, g)
                added = [a for a in ctx_doc.get("acrescentos") or [] if a.get("contexto") == ctx["id"]
                         and a.get("grau") in wanted and lvl in (a.get("niveis") or LEVELS)]
                ids = []
                seen = set()
                for rid in base_sel[lvl]:
                    seen.add(rid)
                    if rid in elevated:
                        ps, obs, g = elevated[rid]
                        ids.append(_entry(rid, "elevado", master, ps, obs, g))
                    else:
                        ids.append(_entry(rid, "base", master))
                for rid in order:
                    if rid in elevated and rid not in seen:
                        ps, obs, g = elevated[rid]
                        ids.append(_entry(rid, "elevado", master, ps, obs, g))
                for a in added:
                    ids.append(_entry(a["id"], "acrescentado", master, [a["id"]], a["base"]["obrigacoes"], a.get("grau")))
                lists[lvl] = ids
            per_grade["base" if grade is None else grade] = lists
        out[ctx["id"]] = per_grade
    return out


def render_lists_yaml(lists: dict) -> str:
    lines = [GEN_MARKER, "lista_ids:"]
    for cid, grades in lists.items():
        lines.append(f"  {cid}:")
        for g, levels in grades.items():
            lines.append(f"    {g}:")
            for lvl, ids in levels.items():
                lines.append(f"      {lvl}:")
                for e in ids:
                    parts = [f"id: {e['id']}", f"origem: {e['origem']}"]
                    if "cap" in e:
                        parts.append(f"cap: '{e['cap']}'")
                    if "grau" in e:
                        parts.append(f"grau: {e['grau']}")
                    if "pisos" in e:
                        parts.append("pisos: [" + ", ".join(e["pisos"]) + "]")
                        parts.append("obrigacoes: [" + ", ".join(e["obrigacoes"]) + "]")
                    lines.append("        - {" + ", ".join(parts) + "}")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- matrix <-> floors


def floor_contexts(ctx_doc: dict) -> Dict[str, dict]:
    """obligation id -> {id: CTX, grau} for every obligation that grounds a floor or an addition.

    grau is null when any floor grounded on the obligation has no grade (the least restrictive wins)."""
    out: Dict[str, dict] = {}
    for ctx in ctx_doc["contextos"]:
        items = list(ctx.get("pisos") or []) + [a for a in ctx_doc.get("acrescentos") or [] if a.get("contexto") == ctx["id"]]
        for p in items:
            for oid in p["base"]["obrigacoes"]:
                cur = out.get(oid)
                g = p.get("grau")
                if cur is None:
                    out[oid] = {"id": ctx["id"], "grau": g}
                elif cur["grau"] is not None and cur["grau"] != g:
                    cur["grau"] = None
    return out


# --------------------------------------------------------------------------- pages


T = {
    "pt": {
        "title": "Requisitos aplicáveis — {nome}",
        "desc": "Vista gerada: requisitos do Manual que se aplicam sob o contexto {cid}, por nível e grau, com os pisos que o regime eleva e a base legal de cada um.",
        "h1": "Requisitos aplicáveis: {nome}",
        "gen": "> **Página gerada** por `scripts/gen_reg_views.py` a partir dos catálogos de requisitos e de `002-cross-check-normativo/_contextos-regulatorios.yaml`. Não se edita à mão: o catálogo de cada requisito é a fonte canónica, e esta página é uma vista do overlay regulatório.",
        "intro": "Esta página junta, para o contexto **{cid}**, a selecção base do Manual por nível e os **pisos** que o regime eleva, cada um com a obrigação que o fundamenta. Um contexto nunca baixa um mínimo do Manual.",
        "h_decl": "Quando se aplica",
        "h_graus": "Graus",
        "h_pisos": "Pisos do contexto",
        "h_act": "Como se lê a lista",
        "h_acr": "Requisitos acrescentados pelo regime",
        "acr_intro": "Estes requisitos só fazem sentido sob o regime e por isso não vivem nos catálogos do Manual; definem-se aqui, com a base legal de cada um.",
        "cols_acr": "| Requisito | Nome | Critério de aceitação | Base legal |",
        "h_lista": "Lista de requisitos — {grau}",
        "h_fora": "Obrigações do regime por força de cobertura",
        "base_label": "contexto (sem grau)",
        "cols_pisos": "| Piso | Alvo | Grau | Piso exigido | Âmbito | Base legal | Justificação de não aplicabilidade |",
        "cols_lista": "| Requisito | Nome | L1 | L2 | L3 | Pisos |",
        "cols_forca": "| Força | Obrigações |",
        "obrig": "obrigatório",
        "sim": "admitida",
        "nao": "não admitida",
        "todos": "todos os níveis",
        "legend": "Legenda: ✔ selecção base do nível; ▲ elevado ou acrescentado pelo regime (aplica-se pelo regime; se o componente não existir, exige justificação documentada de não aplicabilidade); — não seleccionado.",
        "act_rule": "Regra de activação",
        "declara": {"entidade": "Declara-se por entidade e é herdado por todas as aplicações.", "aplicacao": "Declara-se por aplicação."},
        "no_pisos": "Sem pisos neste grau por enquanto.",
        "matrix_note": "Contagem das obrigações da matriz `_matriz/{acto}.yaml` (excluídas as dirigidas às autoridades). A secção «O que este Manual cobre e o que fica de fora» da página do cross-check detalha-as.",
        "graus_cum": "cumulativo com o contexto",
        "graus_ind": "declarável sozinho",
    },
    "en": {
        "title": "Applicable requirements — {nome}",
        "desc": "Generated view: the Manual's requirements that apply under context {cid}, by level and grade, with each floor that the regime elevates and its legal basis.",
        "h1": "Applicable requirements: {nome}",
        "gen": "> **Generated page**, produced by `scripts/gen_reg_views.py` from the requirement catalogues and from `002-cross-check-normativo/_contextos-regulatorios.yaml`. It is not edited by hand: each requirement's catalogue is the canonical source, and this page is a view of the regulatory overlay.",
        "intro": "For context **{cid}**, this page brings together the Manual's base selection per level and each **floor** that the regime elevates, with the obligation that grounds it. A context never lowers a minimum of the Manual.",
        "h_decl": "When it applies",
        "h_graus": "Grades",
        "h_pisos": "Context floor list",
        "h_act": "How to read the list",
        "h_acr": "Requirements added by the regime",
        "acr_intro": "These requirements only make sense under the regime, so they do not live in the Manual's catalogues; they are defined here, each with its legal basis.",
        "cols_acr": "| Requirement | Name | Acceptance criterion | Legal basis |",
        "h_lista": "Requirement list — {grau}",
        "h_fora": "Obligations of the regime by coverage strength",
        "base_label": "context (no grade)",
        "cols_pisos": "| Floor | Target | Grade | Required floor | Scope | Legal basis | Justification of non-applicability |",
        "cols_lista": "| Requirement | Name | L1 | L2 | L3 | Floor ids |",
        "cols_forca": "| Strength | Obligations |",
        "obrig": "mandatory",
        "sim": "admitted",
        "nao": "not admitted",
        "todos": "all levels",
        "legend": "Key: ✔ base selection for the level; ▲ elevated or added by the regime (applies by the regime; if the component does not exist, a documented justification of non-applicability is required); — not selected.",
        "act_rule": "Activation rule",
        "declara": {"entidade": "Declared per entity and inherited by all applications.", "aplicacao": "Declared per application."},
        "no_pisos": "No floor at this grade for now.",
        "matrix_note": "Count of the obligations in the matrix `_matriz/{acto}.yaml` (excluding those addressed to the authorities). The section “What this Manual covers and what stays out” of the cross-check page details them.",
        "graus_cum": "cumulative with the context",
        "graus_ind": "declarable on its own",
    },
}

CTX_ACTO = {"CTX-NIS2": "nis2", "CTX-DORA": "dora", "CTX-CRA": "cra", "CTX-AIA-RE": "aiact", "CTX-RGPD": "rgpd"}


def _cell(text) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def _link_policy(ficheiro: str, ancora: str, rotulo: str) -> str:
    # Docusaurus drops numeric prefixes in URL paths; policies live under /sbd-toe/assets/policies/<id>
    text = (DOCS / ficheiro).read_text(encoding="utf-8")
    m = re.search(r"^id:\s*(\S+)\s*$", text.split("\n---", 1)[0], re.M)
    slug = m.group(1) if m else re.sub(r"^\d+_", "", Path(ficheiro).stem)
    return f"[{rotulo}](/sbd-toe/assets/policies/{slug}#{ancora})"


def _link_req(rid: str, master: dict) -> str:
    return f"`{rid}`"


def _piso_text(p: dict, lang: str, vocab: dict) -> str:
    t = T[lang]
    piso = p["piso"]
    parts = []
    if piso.get("obrigatorio"):
        parts.append(t["obrig"])
    par = piso.get("parametro")
    if par:
        if par.get("escala") and par["escala"] in vocab["escalas"] and vocab["escalas"][par["escala"]].get("nomes"):
            val = vocab["escalas"][par["escala"]]["nomes"][str(par["valor"])][lang]
        else:
            unit = next((u["nome"][lang] for u in vocab.get("unidades", []) if u["id"] == par.get("unidade")), par.get("unidade") or "")
            val = f"{par['valor']} {unit}".strip()
        op = "≥" if par.get("sentido") == "min" else "≤"
        parts.append(f"{par['nome'][lang]} {op} {val} (“{par['texto'][lang]}”)" if lang == "en" else f"{par['nome'][lang]} {op} {val} («{par['texto'][lang]}»)")
    return "; ".join(parts)


def _target_text(p: dict, lang: str) -> str:
    a = p["alvo"]
    if a["tipo"] == "requisito":
        return f"`{a['alvo']}`"
    return _link_policy(a["ficheiro"], a["ancora"], a["rotulo"][lang])


def render_view(ctx: dict, ctx_doc: dict, lists: dict, master: dict, matrix: dict, lang: str) -> str:
    t = T[lang]
    cid = ctx["id"]
    nome = ctx["nome"][lang]
    graus = {g["id"]: g for g in ctx_doc.get("graus") or []}
    vocab = ctx_doc["vocabulario"]
    q = ("“", "”") if lang == "en" else ("«", "»")
    derived = sorted({master[r]["ficheiro"] for r in master}) + [f"{XC}/_contextos-regulatorios.yaml", f"{XC}/{ctx['matriz']}"]
    fm = [
        "---",
        "id: requisitos-aplicaveis",
        f"title: {json.dumps(t['title'].format(nome=nome), ensure_ascii=False)}",
        f"description: {json.dumps(t['desc'].format(cid=cid), ensure_ascii=False)}",
        "sidebar_position: 90",
        f"tags: [cross-check, {CTX_FOLDER[cid]}, requisitos, overlay, gerado]",
        f"{GENERATED_KEY}: {VIEW_NAME}",
        "derived_from:",
    ] + [f"  - {d}" for d in derived] + ["---", ""]
    body = [f"# {t['h1'].format(nome=nome)}", "", t["gen"], "", t["intro"].format(cid=cid), ""]
    # when it applies
    body += [f"## {t['h_decl']} {{#quando-se-aplica}}", ""]
    cr = ctx["criterio"]
    body += [cr["texto"][lang] + " " + t["declara"][ctx["declara_se_em"]], "",
             f"> {cr['referencia'] if lang == 'pt' else _ref_en(cr['referencia'])}: {q[0]}{cr['citacao'][lang]}{q[1]}", ""]
    # grades
    if ctx.get("graus_admitidos"):
        body += [f"## {t['h_graus']} {{#graus}}", ""]
        for gid in ctx["graus_admitidos"]:
            g = graus[gid]
            kind = t["graus_cum"] if g.get("cumulativo", True) else t["graus_ind"]
            body.append(f"- **{gid}** — {g['nome'][lang]} ({kind}). {g['criterio']['texto'][lang]}")
        body.append("")
    # floors
    body += [f"## {t['h_pisos']} {{#pisos}}", "", t["cols_pisos"], "|---|---|---|---|---|---|---|"]
    for p in ctx.get("pisos") or []:
        g = p.get("grau") or "—"
        amb = p["ambito"][lang] if p.get("ambito") else "—"
        ref = p["base"]["referencia"] if lang == "pt" else _ref_en(p["base"]["referencia"])
        basis = f"{ref}: {q[0]}{p['base']['citacao'][lang]}{q[1]} ({', '.join(p['base']['obrigacoes'])})"
        just = t["sim"] if p.get("admite_justificacao") else t["nao"]
        body.append(f"| {p['id']} | {_target_text(p, lang)} | {g} | {_cell(_piso_text(p, lang, vocab))} | {_cell(amb)} | {_cell(basis)} | {just} |")
    body.append("")
    for gid, note in (ctx.get("nota_graus") or {}).items():
        body += [f"> **{gid}.** {note[lang]}", ""]
    # additions (regime-only requirements)
    adds = [a for a in ctx_doc.get("acrescentos") or [] if a.get("contexto") == cid]
    if adds:
        body += [f"## {t['h_acr']} {{#acrescentos}}", "", t["acr_intro"], "", t["cols_acr"], "|---|---|---|---|"]
        for a in adds:
            ref = a["base"]["referencia"] if lang == "pt" else _ref_en(a["base"]["referencia"])
            basis = f"{ref}: {q[0]}{a['base']['citacao'][lang]}{q[1]} ({', '.join(a['base']['obrigacoes'])})"
            body.append(f"| `{a['id']}` | {_cell(a['nome'][lang])} | {_cell(a['criterio_aceitacao'][lang])} | {_cell(basis)} |")
        body.append("")
    # how to read
    body += [f"## {t['h_act']} {{#como-se-le}}", "", t["legend"], "",
             f"**{t['act_rule']}.** {ctx_doc['regra_lista']['activacao'][lang]}", ""]
    # lists
    for gkey, levels in lists[cid].items():
        label = t["base_label"] if gkey == "base" else gkey
        anchor = "lista-" + ("contexto" if gkey == "base" else gkey.lower())
        body += [f"## {t['h_lista'].format(grau=label)} {{#{anchor}}}", "", t["cols_lista"], "|---|---|:--:|:--:|:--:|---|"]
        rows: Dict[str, dict] = {}
        for lvl, ids in levels.items():
            for e in ids:
                rows.setdefault(e["id"], {})[lvl] = e
        for rid in [r for r in master if r in rows] + [r for r in rows if r not in master]:
            marks = []
            pisos = set()
            for lvl in LEVELS:
                e = rows[rid].get(lvl)
                if not e:
                    marks.append("—")
                elif e["origem"] == "base":
                    marks.append("✔")
                else:
                    marks.append("▲")
                    pisos.update(e.get("pisos", []))
            add = next((a for a in adds if a["id"] == rid), None)
            name = master[rid]["nome"][lang] if rid in master else (add["nome"][lang] if add else rid)
            body.append(f"| `{rid}` | {_cell(name)} | {' | '.join(marks)} | {', '.join(sorted(pisos)) or '—'} |")
        body.append("")
    # strength summary
    acto = CTX_ACTO[cid]
    counts: Dict[str, List[str]] = {}
    for it in matrix["itens"]:
        counts.setdefault(it["forca"], []).append(it["id"])
    fnames = {f["id"]: f["nome"][lang] for f in vocab["forca"]}
    body += [f"## {t['h_fora']} {{#forca}}", "", t["matrix_note"].format(acto=acto), "", t["cols_forca"], "|---|--:|"]
    for f in [x["id"] for x in vocab["forca"]]:
        body.append(f"| {fnames[f]} | {len(counts.get(f, []))} |")
    body.append("")
    return "\n".join(fm + body)


_REF_EN = [
    (r"Reg\. Delegado \(UE\)", "Delegated Regulation (EU)"),
    (r"Reg\. de Execução \(UE\)", "Implementing Regulation (EU)"),
    (r"Reg\. \(UE\)", "Regulation (EU)"),
    (r"Diretiva \(UE\)", "Directive (EU)"),
    (r"anexo I, parte I, ponto (\d+), al\. (\w)\), e parte II, pontos (\d+), (\d+) e (\d+)", r"Annex I, Part I, point (\1)(\2), and Part II, points (\3), (\4) and (\5)"),
    (r"anexo I, parte II, pontos (\d+) e (\d+)", r"Annex I, Part II, points (\1) and (\2)"),
    (r"anexo I, parte II, ponto (\d+)", r"Annex I, Part II, point (\1)"),
    (r"anexo II, ponto (\d+), als\. (\w)\) e (\w)\)", r"Annex II, point (\1)(\2) and (\3)"),
    (r"anexo II, ponto (\d+)", r"Annex II, point (\1)"),
    (r"anexo VII, ponto (\d+)", r"Annex VII, point (\1)"),
    (r"art\. (\d+)\.º, n\.os (\d+), (\d+), (\d+) e (\d+)", r"Article \1(\2), (\3), (\4) and (\5)"),
    (r"anexo I, parte I, ponto (\d+), al\. (\w)\)", r"Annex I, Part I, point (\1)(\2)"),
    (r"anexo, pontos ([\d.]+) e ([\d.]+)", r"Annex, points \1 and \2"),
    (r"anexo, ponto ([\d.]+), al\. (\w)\)", r"Annex, point \1(\2)"),
    (r"anexo, ponto ([\d.]+)", r"Annex, point \1"),
    (r"art\. (\d+)\.º, al\. (\w)\), subal\. (\w+)\)", r"Article \1, point (\2)(\3)"),
    (r"art\. (\d+)\.º, n\.º (\d+), al\. (\w)\), e segundo parágrafo", r"Article \1(\2), point (\3), and second subparagraph"),
    (r"art\. (\d+)\.º, n\.º (\d+), al\. (\w)\)", r"Article \1(\2), point (\3)"),
    (r"art\. (\d+)\.º, al\. (\w)\)", r"Article \1, point (\2)"),
    (r"art\. (\d+)\.º, n\.os (\d+) a (\d+)", r"Article \1(\2) to (\3)"),
    (r"art\. (\d+)\.º, n\.os (\d+) e (\d+)", r"Article \1(\2) and (\3)"),
    (r"art\. (\d+)\.º, n\.º (\d+)", r"Article \1(\2)"),
    (r"art\. (\d+)\.º", r"Article \1"),
    (r" \(regime simplificado\)", " (simplified framework)"),
    (r"; ", "; "),
    (r" e Article", " and Article"),
]


def _ref_en(ref: str) -> str:
    out = ref
    for pat, rep in _REF_EN:
        out = re.sub(pat, rep, out)
    return out


def translation_block(pt_text: str, en_body: str, previous: Optional[str]) -> str:
    """Front-matter translation block for a generated EN view (hashes computed like translate.py assemble)."""
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) if REGISTRY.exists() else None
    stamp = None
    if previous:
        m = re.search(r"^  translated_at: (\S+)$", previous, re.M)
        stamp = m.group(1) if m else None
    meta = {
        "source_locale": "pt",
        "source_path": None,
        "source_sha256": common.content_sha256(pt_text),
        "source_commit": None,
        "target_sha256": common.content_sha256(en_body),
        "engine": "gen_reg_views",
        "prompt_sha256": None,
        "terms_sha256": common.file_sha256(REGISTRY) if REGISTRY.exists() else None,
        "glossary_keys": [],
        "glossary_sha256": common.glossary_sha256(registry, []) if registry is not None else None,
        "translated_at": stamp or "2026-09-27T00:00:00Z",
        "stamped_at": stamp or "2026-09-27T00:00:00Z",
        "reviewed_by": None,
    }
    return meta
