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
VIEW_FILE = "90-requisitos-aplicaveis.md"
COVERAGE_FILE = "90-cobertura.md"

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
    """One lista_ids entry. «pisos» carries only floor ids (CTX-*-Pnn); an «acrescentado» entry has no pisos,
    only the obligations that ground it."""
    e = {"id": rid, "origem": origem}
    cap = master.get(rid, {}).get("cap")
    if cap and cap != "02":
        e["cap"] = cap
    if grau:
        e["grau"] = grau
    if pisos:
        e["pisos"] = sorted(pisos)
    if obrigacoes:
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
                    ids.append(_entry(a["id"], "acrescentado", master, None, a["base"]["obrigacoes"], a.get("grau")))
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
                    if "obrigacoes" in e:
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
        "desc": "Requisitos do Manual que se aplicam sob o contexto {cid}, por nível e grau, com os pisos que o regime eleva e a base legal de cada um.",
        "h1": "Requisitos aplicáveis: {nome}",
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
        "h_mapa": "Mapa de evidência da documentação técnica",
        "mapa_intro": "Obrigações documentais do regime ({anexo}) ligadas aos artefactos do Manual que as alimentam. «Apoia evidência»: o Manual produz a evidência de engenharia e a redacção do documento é de quem coloca o produto no mercado. As lacunas e o que fica fora de âmbito aparecem com a razão. A lista vem da matriz de cobertura do Manual.",
        "cols_mapa": "| Obrigação | Referência | Força | Como o Manual responde | Nota |",
        "h_cob": "O que este Manual cobre e o que fica de fora",
        "cob_intro": "Todas as obrigações do regime, na matriz de cobertura do Manual, em três categorias: o que o Manual **cobre**, e de que forma; as **lacunas declaradas** (o que não cobre por omissão); e o que fica **fora de âmbito**, com a razão. Nenhuma obrigação fica em silêncio. As {n_exc} obrigações dirigidas às autoridades não criam dever para a organização e não entram nas listas.",
        "h_cobre": "Cobre",
        "cobre_intro": "Força «cobre» ou «apoia evidência». A forma é a resposta do Manual: requisito do catálogo, política, secção, piso ou requisito acrescentado pelo regime.",
        "h_lacuna": "Lacuna declarada",
        "lacuna_intro": "Força «parcial» ou «lacuna»: o Manual não cobre, ou cobre só em parte, e diz o que falta. As lacunas pendentes de uma ronda do AppSec Core estão marcadas com o nome da ronda.",
        "h_foracob": "Fora de âmbito",
        "fora_intro": "Obrigações que o Manual declara fora de âmbito, com a razão.",
        "cols_cobre": "| Obrigação | Referência | Força | Forma |",
        "cols_lacuna": "| Obrigação | Referência | Força | Como o Manual responde | O que falta |",
        "cols_foracob": "| Obrigação | Referência | Razão |",
        "cov_title": "Cobertura — {nome}",
        "cov_desc": "O que o Manual cobre, as lacunas declaradas e o que fica fora de âmbito, a partir da matriz de cobertura do {nome}.",
        "cov_h1": "Cobertura: {nome}",
        "cov_gen": "Este regime não tem contexto no overlay regulatório (não eleva nem acrescenta requisitos); responde só nas três categorias.",
        "matrix_note": "Contagem das obrigações do regime na matriz de cobertura (excluídas as dirigidas às autoridades). A secção [«O que este Manual cobre e o que fica de fora»](#cobertura) lista-as.",
        "graus_cum": "cumulativo com o contexto",
        "graus_ind": "declarável sozinho",
    },
    "en": {
        "title": "Applicable requirements — {nome}",
        "desc": "The Manual's requirements that apply under context {cid}, by level and grade, with each floor that the regime elevates and its legal basis.",
        "h1": "Applicable requirements: {nome}",
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
        "h_mapa": "Evidence map for the technical documentation",
        "mapa_intro": "Documentary obligations of the regime ({anexo}) linked to the Manual artefacts that feed them. “Supports evidence”: the Manual produces the engineering evidence and drafting the document is for whoever places the product on the market. Gaps and what stays out of scope appear with the reason. The list comes from the Manual's coverage matrix.",
        "cols_mapa": "| Obligation | Reference | Strength | How the Manual responds | Note |",
        "h_cob": "What this Manual covers and what stays out",
        "cob_intro": "All the obligations of the regime, in the Manual's coverage matrix, in three categories: what the Manual **covers**, and in what form; the **declared gaps** (what it does not cover by omission); and what is **out of scope**, with the reason. No obligation is left in silence. The {n_exc} obligations addressed to the authorities create no duty for the organisation and are not listed.",
        "h_cobre": "Covers",
        "cobre_intro": "Strength “covers” or “supports evidence”. The form is the Manual's response: catalogue requirement, policy, section, floor or requirement added by the regime.",
        "h_lacuna": "Declared gap",
        "lacuna_intro": "Strength “partial” or “gap”: the Manual does not cover, or covers only in part, and says what is missing. Gaps pending an AppSec Core round are marked with the name of the round.",
        "h_foracob": "Out of scope",
        "fora_intro": "Obligations that the Manual declares out of scope, with the reason.",
        "cols_cobre": "| Obligation | Reference | Strength | Form |",
        "cols_lacuna": "| Obligation | Reference | Strength | How the Manual responds | What is missing |",
        "cols_foracob": "| Obligation | Reference | Reason |",
        "cov_title": "Coverage — {nome}",
        "cov_desc": "What the Manual covers, the declared gaps and what stays out of scope, from the coverage matrix of the {nome}.",
        "cov_h1": "Coverage: {nome}",
        "cov_gen": "This regime has no context in the regulatory overlay (it neither elevates nor adds requirements); it answers only in the three categories.",
        "matrix_note": "Count of the regime's obligations in the coverage matrix (excluding those addressed to the authorities). The section [“What this Manual covers and what stays out”](#cobertura) lists them.",
        "graus_cum": "cumulative with the context",
        "graus_ind": "declarable on its own",
    },
}



def ctx_acto(ctx: dict) -> str:
    """The matrix a context rests on, from the overlay data (``matriz: _matriz/<acto>.yaml``)."""
    return Path(ctx["matriz"]).stem


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


def _link_page(ficheiro: str, ancora: Optional[str], rotulo: str) -> str:
    # Docusaurus drops numeric prefixes at every path level; the last segment is the front-matter id when present
    text = (DOCS / ficheiro).read_text(encoding="utf-8")
    m = re.search(r"^id:\s*(\S+)\s*$", text.split("\n---", 1)[0], re.M)
    parts = [re.sub(r"^\d+[-_]", "", x) for x in Path(ficheiro).parent.parts]
    last = m.group(1) if m else re.sub(r"^\d+[-_]", "", Path(ficheiro).stem)
    url = "/sbd-toe/" + "/".join(parts + [last])
    return f"[{rotulo}]({url}{'#' + ancora if ancora else ''})"


def _resp_text(r: dict, lang: str) -> str:
    tipo = r.get("tipo")
    if tipo in ("requisito", "acrescento", "contexto"):
        return f"`{r['alvo']}`"
    if tipo == "politica":
        return _link_policy(r["ficheiro"], r["ancora"], r["rotulo"][lang])
    if tipo in ("pagina", "us"):
        rot = (r.get("rotulo") or {}).get(lang) or r.get("alvo") or r["ficheiro"]
        return _link_page(r["ficheiro"], r.get("ancora"), rot)
    return r.get("alvo") or ""


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


def render_coverage(matrix: dict, vocab: dict, acto: str, lang: str) -> List[str]:
    """Three-category coverage section (lead decision 2026-09-27): covers / declared gap / out of scope."""
    t = T[lang]
    fn = {f["id"]: f["nome"][lang] for f in vocab["forca"]}
    rn = {r["id"]: r["nome"][lang] for r in vocab.get("rondas") or []}
    itens = [it for it in matrix["itens"] if not it.get("retirado")]
    out = [f"## {t['h_cob']} {{#cobertura}}", "", t["cob_intro"].format(acto=acto, n_exc=len(matrix.get("excluidas") or [])), ""]
    resp = lambda it: "; ".join(_resp_text(r, lang) for r in it.get("resposta") or []) or "—"
    cob = [it for it in itens if it["forca"] in ("cobre", "apoia_evidencia")]
    out += [f"### {t['h_cobre']} ({len(cob)}) {{#cobre}}", "", t["cobre_intro"], "", t["cols_cobre"], "|---|---|---|---|"]
    out += [f"| {it['id']} | {_cell(it['referencia'][lang])} | {fn[it['forca']]} | {_cell(resp(it))} |" for it in cob]
    lac = [it for it in itens if it["forca"] in ("parcial", "lacuna")]
    out += ["", f"### {t['h_lacuna']} ({len(lac)}) {{#lacuna}}", "", t["lacuna_intro"], "", t["cols_lacuna"], "|---|---|---|---|---|"]
    for it in lac:
        falta = (it.get("falta") or {}).get(lang, "—")
        if it.get("pendente"):
            ronda = it["pendente"].get("ronda")
            falta = f"**{rn.get(ronda, ronda)}.** " + falta
        out.append(f"| {it['id']} | {_cell(it['referencia'][lang])} | {fn[it['forca']]} | {_cell(resp(it))} | {_cell(falta)} |")
    fora = [it for it in itens if it["forca"] == "fora_de_ambito"]
    out += ["", f"### {t['h_foracob']} ({len(fora)}) {{#fora-de-ambito}}", "", t["fora_intro"], "", t["cols_foracob"], "|---|---|---|"]
    out += [f"| {it['id']} | {_cell(it['referencia'][lang])} | {_cell((it.get('razao_fora_de_ambito') or {}).get(lang, '—'))} |" for it in fora]
    out.append("")
    return out


def render_coverage_page(acto: str, matrix: dict, ctx_doc: dict, lang: str) -> str:
    """Coverage-only page for a regime with a matrix but no context in the overlay (e.g. CSA)."""
    t = T[lang]
    nome = matrix["nome"][lang]
    fm = [
        "---",
        "id: cobertura",
        f"title: {json.dumps(t['cov_title'].format(nome=nome), ensure_ascii=False)}",
        f"description: {json.dumps(t['cov_desc'].format(nome=nome), ensure_ascii=False)}",
        "sidebar_position: 90",
        f"tags: [cross-check, {matrix['pasta']}, cobertura]",
        f"{GENERATED_KEY}: {VIEW_NAME}",
        "generated_by: scripts/gen_reg_views.py  # não se edita à mão: editar os catálogos, o overlay e a matriz",
        "derived_from:",
        f"  - {XC}/_matriz/{acto}.yaml",
        "---",
        "",
    ]
    body = [f"# {t['cov_h1'].format(nome=nome)}", "", t["cov_gen"].format(acto=acto), ""]
    body += render_coverage(matrix, ctx_doc["vocabulario"], acto, lang)
    return "\n".join(fm + body)


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
        f"tags: [cross-check, {matrix['pasta']}, requisitos, overlay]",
        f"{GENERATED_KEY}: {VIEW_NAME}",
        "generated_by: scripts/gen_reg_views.py  # não se edita à mão: editar os catálogos, o overlay e a matriz",
        "derived_from:",
    ] + [f"  - {d}" for d in derived] + ["---", ""]
    body = [f"# {t['h1'].format(nome=nome)}", "", t["intro"].format(cid=cid), ""]
    # when it applies
    body += [f"## {t['h_decl']} {{#quando-se-aplica}}", ""]
    cr = ctx["criterio"]
    body += [cr["texto"][lang] + " " + t["declara"][ctx["declara_se_em"]], "",
             f"> {cr['referencia'][lang]}: {q[0]}{cr['citacao'][lang]}{q[1]}", ""]
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
        ref = p["base"]["referencia"][lang]
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
            ref = a["base"]["referencia"][lang]
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
    acto = ctx_acto(ctx)
    # evidence map (documentary obligations)
    em = matrix.get("mapa_evidencia")
    if em:
        fn = {f["id"]: f["nome"][lang] for f in vocab["forca"]}
        rn = {r["id"]: r["nome"][lang] for r in vocab.get("rondas") or []}
        body += [f"## {t['h_mapa']} {{#mapa-evidencia}}", "", t["mapa_intro"].format(anexo=em["titulo"][lang], acto=acto), "", t["cols_mapa"], "|---|---|---|---|---|"]
        for it in matrix["itens"]:
            if it.get("retirado") or not it["id"].startswith(tuple(em["prefixos"])):
                continue
            resp = "; ".join(_resp_text(r, lang) for r in it.get("resposta") or []) or "—"
            note = dict(it.get("razao_fora_de_ambito") or it.get("falta") or {})
            if it.get("pendente"):
                note[lang] = f"**{rn.get(it['pendente'].get('ronda'), it['pendente'].get('ronda'))}.** " + note.get(lang, "")
            ref = it["referencia"][lang]
            body.append(f"| {it['id']} | {_cell(ref)} | {fn[it['forca']]} | {_cell(resp)} | {_cell(note.get(lang, '—') if note else '—')} |")
        body.append("")
    # strength summary
    counts: Dict[str, List[str]] = {}
    for it in matrix["itens"]:
        counts.setdefault(it["forca"], []).append(it["id"])
    fnames = {f["id"]: f["nome"][lang] for f in vocab["forca"]}
    body += [f"## {t['h_fora']} {{#forca}}", "", t["matrix_note"].format(acto=acto), "", t["cols_forca"], "|---|--:|"]
    for f in [x["id"] for x in vocab["forca"]]:
        body.append(f"| {fnames[f]} | {len(counts.get(f, []))} |")
    body.append("")
    body += render_coverage(matrix, vocab, acto, lang)
    return "\n".join(fm + body)


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
