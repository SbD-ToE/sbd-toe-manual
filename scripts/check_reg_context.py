#!/usr/bin/env python3
"""Verify the regulatory overlay data of the SbD-ToE Manual (CI).

Checks, failing explicitly (never guessing):

- ``_matriz/<acto>.yaml`` (sbdtoe-reg-coverage/1): header; sha256 of the obligations file; items ∪ excluded = every
  obligation of the text, disjoint; references equal to the text's; enumerations; answers resolve (requirement ids in the
  master with the catalogue's levels, US ids, files and explicit anchors in PT and EN, quotations found verbatim in the
  PT and EN pages); bilingual texts complete; ``contexto`` consistent with the floors; ``substitui`` in the legacy
  framework's id space.
- ``_contextos-regulatorios.yaml`` (sbdtoe-overlay/1, regulatorio): enumerations; contexts, grades, floors and additions;
  targets resolve; floor bases exist in the context's matrix; legal quotations found verbatim in the EUR-Lex texts
  (translation/sources/eurlex, PT and EN); parameters valid against the declared scales and units; no «remover».
- ``lista_ids`` and the «Requisitos aplicáveis» pages equal what ``scripts/gen_reg_views.py`` would write.

Usage: ``python scripts/check_reg_context.py`` (exit 1 on any finding).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import reg_context_lib as L  # noqa: E402
import gen_reg_views  # noqa: E402

FORCA = {"cobre", "parcial", "apoia_evidencia", "lacuna", "fora_de_ambito"}
CLASSE = {"engenharia", "organizacional", "juridico-contratual"}
CONFIANCA = {"alta", "media", "baixa"}
TIPO = {"requisito", "us", "politica", "pagina", "acrescento"}
ADDITIONS: set = set()  # CTX-<regime>-Rnn ids declared in _contextos-regulatorios.yaml
CELEX_RE = re.compile(r"3\d{4}[RLD]\d{4}")

problems: list = []


def fail(where: str, msg: str) -> None:
    problems.append(f"{where}: {msg}")


def squash(text: str) -> str:
    """Whitespace-free, NFC, without EUR-Lex consolidation markers (▼B, ▼M1…)."""
    text = re.sub(r"▼[A-Z]\d*", "", L.common.nfc(text))
    return re.sub(r"\s+", "", text)


def bilingual(obj, where: str, optional: bool = False) -> None:
    if obj is None:
        if not optional:
            fail(where, "texto {pt, en} em falta")
        return
    if not isinstance(obj, dict) or set(obj) != {"pt", "en"} or not all(isinstance(obj[k], str) and obj[k].strip() for k in ("pt", "en")):
        fail(where, f"texto {{pt, en}} malformado: {obj!r:.160}")


def walk_bilingual(x, where: str) -> None:
    if isinstance(x, dict):
        if "pt" in x or "en" in x:
            bilingual(x, where)
        for k, v in x.items():
            walk_bilingual(v, f"{where}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            walk_bilingual(v, f"{where}[{i}]")


_files: dict = {}


def page(rel: str, en: bool) -> str | None:
    key = (rel, en)
    if key not in _files:
        p = (L.EN_DOCS if en else L.DOCS) / rel
        _files[key] = p.read_text(encoding="utf-8") if p.exists() else None
    return _files[key]


def explicit_ids(text: str) -> set:
    return {m.group(1).strip() for m in re.finditer(r"\{#([^}]+)\}", text)}


def check_target(t: dict, where: str, master: dict, quote: bool = True) -> None:
    tipo = t.get("tipo")
    if tipo not in TIPO:
        fail(where, f"tipo inválido {tipo!r}")
        return
    if tipo == "acrescento":
        if t.get("alvo") not in ADDITIONS:
            fail(where, f"acrescento {t.get('alvo')!r} não declarado em _contextos-regulatorios.yaml")
        if t.get("ficheiro") or t.get("ancora"):
            fail(where, "acrescento usa só alvo (sem ficheiro/ancora)")
        return
    if tipo == "requisito":
        rid = t.get("alvo")
        if rid not in master:
            fail(where, f"requisito {rid!r} não existe no master")
        elif "niveis" in t and (t["niveis"] or []) != master[rid]["niveis"]:
            fail(where, f"{rid}: niveis {t['niveis']} ≠ catálogo {master[rid]['niveis']}")
    elif tipo == "us":
        m = re.fullmatch(r"(\d\d-[a-z0-9-]+)-us-(\d+)", t.get("alvo") or "")
        if not m:
            fail(where, f"id de US inválido {t.get('alvo')!r}")
        elif not (t.get("ficheiro", "").startswith(f"010-sbd-manual/{m.group(1)}/") and (t.get("ancora") or "").startswith(f"us-{m.group(2)}")):
            fail(where, f"US {t['alvo']} não corresponde a {t.get('ficheiro')}#{t.get('ancora')}")
    else:
        if "alvo" in t:
            fail(where, f"«alvo» reservado (tipo {tipo} usa ficheiro + ancora)")
        bilingual(t.get("rotulo"), where + "/rotulo")
        if tipo == "politica" and not (t.get("ficheiro") or "").startswith("020-assets/policies/"):
            fail(where, f"política fora de 020-assets/policies: {t.get('ficheiro')}")
    rel, anc = t.get("ficheiro"), t.get("ancora")
    if tipo in ("politica", "pagina") or rel or anc:
        if not rel or not anc:
            fail(where, "ficheiro e ancora obrigatórios")
            return
        if anc.startswith("{#"):
            fail(where, f"ancora com {{#}}: {anc}")
        for en in (False, True):
            text = page(rel, en)
            if text is None:
                fail(where, f"ficheiro inexistente ({'EN' if en else 'PT'}): {rel}")
            elif anc not in explicit_ids(text):
                fail(where, f"âncora inexistente ({'EN' if en else 'PT'}): {rel}#{anc}")
        cit = t.get("citacao")
        if quote and cit is not None:
            bilingual(cit, where + "/citacao")
            if isinstance(cit, dict):
                for lang, en in (("pt", False), ("en", True)):
                    text = page(rel, en)
                    if text and cit.get(lang) and squash(cit[lang]) not in squash(text):
                        fail(where, f"citação {lang.upper()} não encontrada em {rel}: {cit[lang][:80]!r}")


def check_matrices(master: dict, ctx_doc: dict, matrices: dict) -> None:
    ctx_ids = {c["id"] for c in ctx_doc["contextos"]}
    rondas = {r["id"] for r in (ctx_doc.get("vocabulario") or {}).get("rondas") or []}
    floor_ctx = L.floor_contexts(ctx_doc)
    for acto, m in matrices.items():
        w = f"_matriz/{acto}.yaml"
        if m.get("schema") != "sbdtoe-reg-coverage/1" or m.get("acto") != acto or not isinstance(m.get("version"), int):
            fail(w, "cabeçalho inválido (schema/acto/version)")
        fo = m.get("fonte_obrigacoes") or {}
        try:
            raw, obl = L.load_obligations(fo.get("caminho", ""))
        except (OSError, ValueError) as exc:
            fail(w, f"fonte_obrigacoes ilegível: {exc}")
            continue
        if L.sha256(raw) != fo.get("sha256"):
            fail(w, "sha256 de fonte_obrigacoes não confere")
        O = {o["id"]: o for o in obl["obrigacoes"]}
        pasta = m.get("pasta")
        if not (isinstance(pasta, str) and (L.DOCS / L.XC / pasta).is_dir()):
            fail(w, f"pasta de cross-check inexistente ou em falta: {pasta!r}")
        if acto not in {Path(c["matriz"]).stem for c in ctx_doc.get("contextos") or []}:
            bilingual(m.get("nome"), w + "/nome (obrigatório numa matriz sem contexto)")
        me = m.get("mapa_evidencia")
        if me is not None:
            pref = me.get("prefixos") if isinstance(me, dict) else None
            if not pref or not all(isinstance(x, str) and x for x in pref):
                fail(w, "mapa_evidencia.prefixos em falta ou inválido")
            else:
                for x in pref:
                    if not any(it.get("id", "").startswith(x) for it in m.get("itens") or []):
                        fail(w, f"mapa_evidencia: prefixo {x!r} sem obrigações")
            bilingual((me or {}).get("titulo") if isinstance(me, dict) else None, w + "/mapa_evidencia/titulo")
        legacy = m.get("framework_legado")
        seen = set()
        for i, it in enumerate(m.get("itens") or []):
            iw = f"{w} {it.get('id', f'#{i}')}"
            oid = it.get("id")
            if oid in seen:
                fail(iw, "id duplicado")
            seen.add(oid)
            if oid not in O:
                if not it.get("retirado"):
                    fail(iw, "obrigação inexistente no texto")
                continue
            if it.get("retirado"):
                if not it.get("data"):
                    fail(iw, "retirado sem data")
                bilingual(it.get("razao"), iw + "/razao")
                continue
            ref = it.get("referencia")
            bilingual(ref, iw + "/referencia")
            if not isinstance(ref, dict) or ref.get("pt") != O[oid]["referencia"]:
                fail(iw, "referencia.pt ≠ texto oficial")
            pend = it.get("pendente")
            if pend is not None:
                if not isinstance(pend, dict) or set(pend) != {"ronda"} or pend.get("ronda") not in rondas:
                    fail(iw, f"pendente inválido {pend!r}: ronda fora de vocabulario.rondas")
                elif it.get("forca") == "cobre":
                    fail(iw, "pendente numa obrigação coberta")
            af = it.get("acto_fonte")
            if not (isinstance(af, str) and CELEX_RE.fullmatch(af)) and not (isinstance(af, list) and af and all(CELEX_RE.fullmatch(x) for x in af)):
                fail(iw, f"acto_fonte não é CELEX: {af!r}")
            if it.get("classe") not in CLASSE:
                fail(iw, f"classe inválida {it.get('classe')!r}")
            if it.get("forca") not in FORCA:
                fail(iw, f"forca inválida {it.get('forca')!r}")
            if it.get("confianca") not in CONFIANCA:
                fail(iw, f"confianca inválida {it.get('confianca')!r}")
            if it.get("contexto") != floor_ctx.get(oid):
                fail(iw, f"contexto {it.get('contexto')} ≠ pisos {floor_ctx.get(oid)}")
            if it.get("contexto") and it["contexto"]["id"] not in ctx_ids:
                fail(iw, f"contexto inexistente {it['contexto']['id']}")
            resp = it.get("resposta") or []
            if it.get("forca") in ("cobre", "parcial", "apoia_evidencia") and not resp:
                fail(iw, f"forca {it['forca']} sem resposta")
            for j, r in enumerate(resp):
                check_target(r, f"{iw} resposta[{j}]", master)
                if r.get("tipo") != "acrescento":
                    bilingual(r.get("citacao"), f"{iw} resposta[{j}]/citacao")
            if it.get("forca") == "fora_de_ambito":
                bilingual(it.get("razao_fora_de_ambito"), iw + "/razao_fora_de_ambito")
            elif it.get("razao_fora_de_ambito") is not None:
                fail(iw, "razao_fora_de_ambito só com forca fora_de_ambito")
            for k in ("falta", "nota"):
                bilingual(it.get(k), f"{iw}/{k}", optional=True)
            if not isinstance(it.get("conflito"), bool):
                fail(iw, "conflito tem de ser booleano")
            elif it["conflito"]:
                bilingual(it.get("explicacao_conflito"), iw + "/explicacao_conflito")
            elif it.get("explicacao_conflito") is not None:
                fail(iw, "explicacao_conflito sem conflito")
            for s in it.get("substitui") or []:
                if not legacy or not s.startswith(legacy + "-OBL-"):
                    fail(iw, f"substitui {s} fora do espaço {legacy}-OBL-")
        excl = set()
        for e in m.get("excluidas") or []:
            ew = f"{w} excluida {e.get('id')}"
            if e.get("id") not in O:
                fail(ew, "obrigação inexistente no texto")
            elif O[e["id"]].get("classe") != "autoridade":
                fail(ew, "só se excluem obrigações dirigidas às autoridades")
            bilingual(e.get("razao"), ew + "/razao")
            if e.get("id") in seen:
                fail(ew, "está também em itens")
            excl.add(e.get("id"))
        missing = set(O) - seen - excl
        if missing:
            fail(w, f"{len(missing)} obrigação(ões) nem em itens nem em excluidas: {sorted(missing)[:5]}")


def eurlex_corpus(lang: str) -> str:
    parts = []
    for p in sorted(L.EURLEX.rglob(f"*-{lang}*")):
        if p.suffix == ".json":
            parts.extend(json.loads(p.read_text(encoding="utf-8")).values())
        elif p.suffix == ".txt":
            parts.append(p.read_text(encoding="utf-8"))
    return squash(" ".join(parts))


def check_contexts(master: dict, ctx_doc: dict, matrices: dict) -> None:
    w = "_contextos-regulatorios.yaml"
    if ctx_doc.get("schema") != "sbdtoe-overlay/1":
        fail(w, "schema ≠ sbdtoe-overlay/1")
    if ctx_doc.get("tipo_overlay") != "regulatorio":
        fail(w, f"tipo_overlay {ctx_doc.get('tipo_overlay')!r}: o repositório do Manual só admite overlays regulatórios")
    walk_bilingual({k: v for k, v in ctx_doc.items() if k != "lista_ids"}, w)
    vocab = ctx_doc.get("vocabulario") or {}
    for key, expected in (("forca", FORCA), ("classe", CLASSE), ("confianca", CONFIANCA), ("tipo", TIPO)):
        if {x["id"] for x in vocab.get(key) or []} != expected:
            fail(w, f"vocabulario.{key} ≠ enumeração do schema")
    escalas = vocab.get("escalas") or {}
    unidades = {u["id"] for u in vocab.get("unidades") or []}
    pt_corpus, en_corpus = eurlex_corpus("PT"), eurlex_corpus("EN")

    def legal_quote(cit, where):
        bilingual(cit, where)
        if isinstance(cit, dict):
            for lang, corpus in (("pt", pt_corpus), ("en", en_corpus)):
                if cit.get(lang) and squash(cit[lang]) not in corpus:
                    fail(where, f"citação {lang.upper()} não encontrada no texto oficial EUR-Lex: {cit[lang][:80]!r}")

    ctx_by_id = {}
    for c in ctx_doc.get("contextos") or []:
        if not re.fullmatch(r"CTX-[A-Z0-9-]+", c.get("id", "")) or c["id"] in ctx_by_id:
            fail(w, f"id de contexto inválido ou duplicado: {c.get('id')}")
        ctx_by_id[c["id"]] = c
    graus = {}
    for g in ctx_doc.get("graus") or []:
        gw = f"{w} grau {g.get('id')}"
        if g.get("id") in graus:
            fail(gw, "duplicado")
        graus[g.get("id")] = g
        if g.get("contexto") not in ctx_by_id:
            fail(gw, "contexto inexistente")
        if g.get("declara_se_em") not in ("entidade", "aplicacao"):
            fail(gw, "declara_se_em inválido")
        if not isinstance(g.get("cumulativo"), bool):
            fail(gw, "cumulativo tem de ser booleano")
        bilingual((g.get("criterio") or {}).get("referencia"), gw + " criterio/referencia")
    matrix_ids = {}
    for acto, m in matrices.items():
        matrix_ids[f"_matriz/{acto}.yaml"] = {it["id"] for it in m.get("itens") or []}
    for c in ctx_by_id.values():
        cw = f"{w} {c['id']}"
        mids = matrix_ids.get(c.get("matriz"))
        if mids is None:
            fail(cw, f"matriz inexistente {c.get('matriz')}")
            mids = set()
        if c.get("declara_se_em") not in ("entidade", "aplicacao"):
            fail(cw, "declara_se_em inválido")
        for gid in c.get("graus_admitidos") or []:
            if graus.get(gid, {}).get("contexto") != c["id"]:
                fail(cw, f"grau {gid} não pertence a este contexto")
            for oid in graus.get(gid, {}).get("criterio", {}).get("obrigacoes") or []:
                if oid not in mids:
                    fail(cw, f"grau {gid}: obrigação {oid} fora da matriz")
            legal_quote(graus.get(gid, {}).get("criterio", {}).get("citacao"), f"{cw} grau {gid}/citacao")
        for oid in c["criterio"].get("obrigacoes") or []:
            if oid not in mids:
                fail(cw, f"criterio: obrigação {oid} fora da matriz")
        legal_quote(c["criterio"].get("citacao"), cw + " criterio/citacao")
        bilingual(c["criterio"].get("referencia"), cw + " criterio/referencia")
        seen = set()
        for p in c.get("pisos") or []:
            pw = f"{cw} {p.get('id')}"
            if not re.fullmatch(re.escape(c["id"]) + r"-P\d\d", p.get("id", "")) or p["id"] in seen:
                fail(pw, "id de piso inválido ou duplicado")
            seen.add(p.get("id"))
            if p.get("operador") != "elevar":
                fail(pw, f"operador {p.get('operador')!r}: um piso regulatório só eleva")
            if p.get("grau") is not None and p["grau"] not in (c.get("graus_admitidos") or []):
                fail(pw, f"grau {p['grau']} não admitido")
            if p.get("niveis") is not None and not set(p["niveis"]) <= set(L.LEVELS):
                fail(pw, "niveis inválidos")
            check_target(p.get("alvo") or {}, pw + " alvo", master, quote=False)
            piso = p.get("piso") or {}
            if not piso.get("obrigatorio") and not piso.get("parametro"):
                fail(pw, "piso sem obrigatorio nem parametro")
            par = piso.get("parametro")
            if par:
                if par.get("sentido") not in ("min", "max"):
                    fail(pw, "parametro.sentido inválido")
                esc = par.get("escala")
                if esc not in escalas:
                    fail(pw, f"escala {esc!r} não declarada")
                elif escalas[esc].get("tipo") == "ordinal" and par.get("valor") not in escalas[esc]["ordem"]:
                    fail(pw, f"valor {par.get('valor')!r} fora da escala {esc}")
                elif escalas[esc].get("tipo") == "quantidade" and (par.get("unidade") not in unidades or not isinstance(par.get("valor"), (int, float))):
                    fail(pw, "parâmetro de quantidade sem unidade declarada ou valor numérico")
                legal_quote(par.get("texto"), pw + " parametro/texto")
            for oid in p.get("base", {}).get("obrigacoes") or []:
                if oid not in mids:
                    fail(pw, f"base: obrigação {oid} fora da matriz {c.get('matriz')}")
            if not p.get("base", {}).get("obrigacoes"):
                fail(pw, "base sem obrigações")
            legal_quote(p.get("base", {}).get("citacao"), pw + " base/citacao")
            bilingual(p.get("base", {}).get("referencia"), pw + " base/referencia")
            if not isinstance(p.get("admite_justificacao"), bool):
                fail(pw, "admite_justificacao tem de ser booleano")
    for a in ctx_doc.get("acrescentos") or []:
        aw = f"{w} acrescento {a.get('id')}"
        if a.get("contexto") not in ctx_by_id or not re.fullmatch(re.escape(a.get("contexto", "")) + r"-R\d\d", a.get("id", "")):
            fail(aw, "id ou contexto inválido (CTX-<regime>-Rnn)")
        if a.get("id") in master or re.fullmatch(L.REQ_ID, a.get("id", "")):
            fail(aw, "colide com o espaço de ids do master")
        for k in ("nome", "criterio_aceitacao"):
            bilingual(a.get(k), f"{aw}/{k}")
        mids_a = matrix_ids.get((ctx_by_id.get(a.get("contexto")) or {}).get("matriz"), set())
        for oid in (a.get("base") or {}).get("obrigacoes") or []:
            if oid not in mids_a:
                fail(aw, f"base: obrigação {oid} fora da matriz do contexto")
        if not (a.get("base") or {}).get("obrigacoes"):
            fail(aw, "base sem obrigações")
        legal_quote((a.get("base") or {}).get("citacao"), aw + " base/citacao")
        bilingual((a.get("base") or {}).get("referencia"), aw + " base/referencia")
        if a.get("grau") is not None and a["grau"] not in ((ctx_by_id.get(a.get("contexto")) or {}).get("graus_admitidos") or []):
            fail(aw, f"grau {a['grau']} não admitido")
        if a.get("controlos") == [] :
            bilingual(a.get("sem_controlo_razao"), aw + "/sem_controlo_razao")
        if "controlos" not in a or (a.get("controlos") == [] and not a.get("sem_controlo_razao")):
            fail(aw, "ligação a controlos não declarada (controlos: [...] ou sem_controlo_razao)")
    if "remover" in json.dumps(ctx_doc.get("contextos"), ensure_ascii=False):
        fail(w, "«remover» não existe em overlays regulatórios")


def check_lists(ctx_doc: dict) -> None:
    """lista_ids: «pisos» only carries floor ids (CTX-*-Pnn) that exist; «acrescentado» entries carry no pisos."""
    floors = {p["id"] for c in ctx_doc.get("contextos") or [] for p in c.get("pisos") or []}
    for cid, grades in (ctx_doc.get("lista_ids") or {}).items():
        for g, levels in (grades or {}).items():
            for lvl, ids in (levels or {}).items():
                for e in ids or []:
                    w = f"lista_ids {cid}/{g}/{lvl} {e.get('id')}"
                    for pid in e.get("pisos") or []:
                        if not re.fullmatch(r"CTX-[A-Z0-9-]+-P\d\d", pid) or pid not in floors:
                            fail(w, f"pisos só leva ids de pisos declarados (CTX-*-Pnn): {pid}")
                    if e.get("origem") == "acrescentado" and e.get("pisos"):
                        fail(w, "entrada acrescentada não leva pisos")
                    if e.get("origem") == "elevado" and not e.get("pisos"):
                        fail(w, "entrada elevada sem pisos")


def check_views() -> None:
    for path, text in gen_reg_views.planned_outputs().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            fail(str(path.relative_to(L.ROOT)), "difere do que scripts/gen_reg_views.py gera (correr o gerador)")
        if path.suffix == ".md" and f"{L.GENERATED_KEY}: {L.VIEW_NAME}" not in text:
            fail(str(path.relative_to(L.ROOT)), "vista gerada sem sbdtoe_generated")


def main() -> int:
    try:
        master = L.load_master()
        ctx_doc = L.load_contexts()
        matrices = L.load_matrices()
    except Exception as exc:  # noqa: BLE001 — report, never trace
        print(f"check_reg_context: erro a carregar os dados: {exc}")
        return 1
    ADDITIONS.update(a.get("id") for a in ctx_doc.get("acrescentos") or [])
    check_matrices(master, ctx_doc, matrices)
    check_contexts(master, ctx_doc, matrices)
    check_lists(ctx_doc)
    if problems:
        problems.append("vistas geradas não verificadas: corrigir primeiro os problemas acima")
    else:
        check_views()
    for p in problems:
        print(p)
    n_items = sum(len(m.get("itens") or []) for m in matrices.values())
    n_floors = sum(len(c.get("pisos") or []) for c in ctx_doc["contextos"])
    print(f"check_reg_context: master {len(master)} requisitos, {len(matrices)} matrizes, {n_items} obrigações, "
          f"{len(ctx_doc['contextos'])} contextos, {n_floors} pisos — {len(problems)} problema(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
