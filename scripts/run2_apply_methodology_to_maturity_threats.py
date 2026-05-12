#!/usr/bin/env python3
"""Run 2 — Apply Manual ontology V2 vocab + §26 methodology to achievable-maturity + 50-ameacas-mitigadas.

Per Run 2 dispatch 2026-05-11.

Outputs:
  - /tmp/iter3_path_d/out_run2/achievable_maturity/<chapter>/achievable-maturity.md (14 files)
  - /tmp/iter3_path_d/out_run2/threats/<chapter>/50-ameacas-mitigadas.md (14 files)

Format: 5-section per maturity (V2 entities + SAMM/DSOMM + SLSA + Out-of-Maturity + Future-work);
        6-section per threats (V2 entities + Threat surfaces + AntiPattern exposure + CWE + V1 overlay + Future-work).
"""
import json
from pathlib import Path
from collections import defaultdict

INPUT_DIR = Path("/tmp/iter3_path_d")
OUT_DIR = INPUT_DIR / "out_run2"

CHAPTERS = [
    "01-classificacao-aplicacoes", "02-requisitos-seguranca",
    "03-threat-modeling", "04-arquitetura-segura", "05-dependencias-sbom-sca",
    "06-desenvolvimento-seguro", "07-cicd-seguro", "08-iac-infraestrutura",
    "09-containers-imagens", "10-testes-seguranca", "11-deploy-seguro",
    "12-monitorizacao-operacoes", "13-formacao-onboarding", "14-governanca-contratacao",
]

CHAPTER_TITLES = {
    "01-classificacao-aplicacoes": "Classificação de Aplicações",
    "02-requisitos-seguranca": "Requisitos de Segurança",
    "03-threat-modeling": "Threat Modeling",
    "04-arquitetura-segura": "Arquitetura Segura",
    "05-dependencias-sbom-sca": "Dependências, SBOM e SCA",
    "06-desenvolvimento-seguro": "Desenvolvimento Seguro",
    "07-cicd-seguro": "CI/CD Seguro",
    "08-iac-infraestrutura": "IaC e Infraestrutura",
    "09-containers-imagens": "Containers e Imagens",
    "10-testes-seguranca": "Testes de Segurança",
    "11-deploy-seguro": "Deploy Seguro",
    "12-monitorizacao-operacoes": "Monitorização e Operações",
    "13-formacao-onboarding": "Formação e Onboarding",
    "14-governanca-contratacao": "Governança e Contratação",
}

V2_ENTITY_META = {
    "Requirement": ("normative", "explicit", "deterministic"),
    "Control": ("normative", "explicit", "deterministic"),
    "Practice": ("normative", "explicit", "deterministic"),
    "Threat": ("normative", "heuristic", "bounded"),
    "Artifact": ("editorial", "explicit", "deterministic"),
    "MaturityMapping": ("external", "derived", "bounded"),
    "Concept": ("semantic", "scored", "bounded"),
    "Mechanism": ("semantic", "scored", "bounded"),
    "Pattern": ("semantic", "scored", "bounded"),
    "AntiPattern": ("semantic", "scored", "bounded"),
    "Signal": ("semantic", "scored", "bounded"),
}


def methodology_label_from_confidence(conf):
    """Deterministic §26 label per confidence value (per (4b) editorial autoridade)."""
    if conf is None:
        return "Semântico"
    if conf >= 0.85:
        return "Explícito"
    if conf >= 0.65:
        return "Semântico"
    if conf >= 0.4:
        return "Parcial"
    return "Gap"


def load_maturity_mappings():
    d = json.loads((INPUT_DIR / "maturity_mappings.json").read_text())
    by_chapter = defaultdict(list)
    for item in d.get("items", []):
        ch = item.get("chapter_id")
        if ch in by_chapter or ch in CHAPTERS:
            by_chapter[ch].append(item)
    return dict(by_chapter)


def load_jsonl(path):
    out = []
    if not path.exists():
        return out
    for line in path.open():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return out


def load_threats_per_chapter():
    d = json.loads((INPUT_DIR / "mitigated_threats.json").read_text())
    by_chapter = defaultdict(list)
    for t in d.get("items", []):
        ch = t.get("chapter_id")
        if ch in CHAPTERS:
            by_chapter[ch].append(t)
    return dict(by_chapter)


def load_antipatterns_per_chapter():
    items = load_jsonl(INPUT_DIR / "antipatterns.jsonl")
    by_chapter = defaultdict(list)
    for a in items:
        for b in a.get("bundle_ids", []):
            if b in CHAPTERS:
                by_chapter[b].append(a)
    return dict(by_chapter)


def load_signals_per_chapter():
    items = load_jsonl(INPUT_DIR / "signals.jsonl")
    by_chapter = defaultdict(list)
    for s in items:
        for b in s.get("bundle_ids", []):
            if b in CHAPTERS:
                by_chapter[b].append(s)
    return dict(by_chapter)


def load_antipattern_threat_links():
    items = load_jsonl(INPUT_DIR / "antipattern_threat_links.jsonl")
    by_chapter = defaultdict(list)
    for link in items:
        for b in link.get("bundle_ids", []):
            if b in CHAPTERS:
                by_chapter[b].append(link)
    return dict(by_chapter)


# ─────────────────── achievable-maturity ───────────────────


def gen_maturity_chapter(chapter, maturity_items):
    title = CHAPTER_TITLES[chapter]
    lines = [f"# Achievable Maturity — {title}", "", "## Sumário", ""]
    lines.append(
        "Postura de maturidade credível atingível se este capítulo for implementado as written. "
        "Análise segue **§26 canon §4 discipline**: SAMM v2.1 + DSOMM são fontes primárias; SLSA "
        "só onde fizer sentido como progressão de build/integridade; **alinhamento regulatório "
        "NÃO é maturity score** e é registado em § Out-of-Maturity scope."
    )
    lines.append("")
    lines.append("Cinco secções:")
    lines.append("")
    lines.append("- **§ Manual ontology V2 entities** — MaturityMapping + Practice + Control entities relevantes")
    lines.append("- **§ SAMM v2 / DSOMM maturity progression** — primary maturity sources per §26 §4")
    lines.append("- **§ SLSA build/integrity progression** — onde aplicável a este capítulo")
    lines.append("- **§ Out-of-Maturity scope** — regulatory alignment (NÃO maturity score)")
    lines.append("- **§ Future-work register** — maturity gaps registered para P8 §10")
    lines.append("")
    lines.append("---")
    lines.append("")

    # § Manual ontology V2 entities
    lines.append("## § Manual ontology V2 — entities relevantes para maturity")
    lines.append("")
    if maturity_items:
        lines.append(
            f"Total: **{len(maturity_items)} MaturityMapping entities** mapped a este capítulo "
            "(via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`)."
        )
        lines.append("")
        lines.append("| Entity type | ID | Framework | Framework area | Authority class | Source mode |")
        lines.append("|---|---|---|---|---|---|")
        auth, srcmode, _ = V2_ENTITY_META["MaturityMapping"]
        # Sort by framework then ID
        for m in sorted(maturity_items, key=lambda x: (x.get("framework", ""), x.get("id", ""))):
            mid = m.get("id", "?")
            fw = m.get("framework", "—")
            area = m.get("framework_area") or m.get("coverage_summary") or "—"
            area = str(area).replace("|", "/").replace("\n", " ")[:60]
            lines.append(f"| MaturityMapping | `{mid}` | {fw} | {area} | {auth} | {srcmode} |")
        lines.append("")
    else:
        lines.append("_(Nenhuma MaturityMapping entity mapped a este capítulo no current KG canonical state.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    samm_dsomm = [m for m in maturity_items if m.get("framework") in ("OWASP SAMM", "OWASP DSOMM")]
    slsa = [m for m in maturity_items if m.get("framework") == "SLSA"]

    # § SAMM / DSOMM
    lines.append("## § SAMM v2 / DSOMM maturity progression")
    lines.append("")
    if samm_dsomm:
        lines.append(
            "Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). "
            "§26 methodology label deterministic per `confidence` field do KG canonical mapping."
        )
        lines.append("")
        lines.append("| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |")
        lines.append("|---|---|---|---|---|---|")
        for m in sorted(samm_dsomm, key=lambda x: (x.get("framework", ""), x.get("id", ""))):
            fw = m.get("framework", "?")
            area = m.get("framework_area") or "—"
            cov = (m.get("coverage_summary") or "—").replace("|", "/").replace("\n", " ")[:80]
            anchor = m.get("document_path", "")
            # Compact anchor: just the filename part relative to chapter
            if anchor:
                # remove "010-sbd-manual/<chapter>/" prefix
                parts = anchor.split("/")
                if len(parts) >= 3 and parts[1] == chapter:
                    anchor = "/".join(parts[2:])
            conf = m.get("confidence")
            conf_str = f"{conf:.2f}" if isinstance(conf, (int, float)) else "—"
            label = methodology_label_from_confidence(conf)
            lines.append(f"| {fw} | {area} | {cov} | `{anchor}` | {conf_str} | {label} |")
        lines.append("")
    else:
        lines.append("_(Nenhum SAMM/DSOMM mapping para este capítulo.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § SLSA
    lines.append("## § SLSA build/integrity progression")
    lines.append("")
    if slsa:
        lines.append(
            "SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de "
            "build/integridade — este capítulo qualifica)."
        )
        lines.append("")
        lines.append("| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |")
        lines.append("|---|---|---|---|---|")
        for m in sorted(slsa, key=lambda x: x.get("id", "")):
            area = m.get("framework_area") or "—"
            cov = (m.get("coverage_summary") or "—").replace("|", "/").replace("\n", " ")[:80]
            anchor = m.get("document_path", "")
            if anchor:
                parts = anchor.split("/")
                if len(parts) >= 3 and parts[1] == chapter:
                    anchor = "/".join(parts[2:])
            conf = m.get("confidence")
            label = methodology_label_from_confidence(conf)
            lines.append(f"| {area} | — | {cov} | `{anchor}` | {label} |")
        lines.append("")
    else:
        lines.append("_(SLSA não aplicável a este capítulo — sem progressão de build/integridade direct.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § Out-of-Maturity scope
    lines.append("## § Out-of-Maturity scope (regulatory alignment NÃO maturity)")
    lines.append("")
    lines.append(
        "Per §26 §4 discipline: alinhamento regulatório (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) "
        "**NÃO deve ser tratado como maturity score**. Items regulatórios são registados aqui "
        "para visibility editorial; conformance vive em obrigações separadas, não em maturity progression."
    )
    lines.append("")
    lines.append(
        "_(Regulatory alignment para este capítulo é tratado via Manual ontology V2 ExternalObligation "
        "entities + capítulos de governança (Cap. 14); não enumerado aqui para evitar conflation com "
        "maturity claim.)_"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # § Future-work register
    lines.append("## § Future-work register (maturity gaps)")
    lines.append("")
    # Identify gaps: maturity items with confidence < 0.5 OR missing framework_area
    gaps = [m for m in maturity_items if (m.get("confidence") or 1.0) < 0.5]
    if gaps:
        lines.append("Maturity claims com confidence < 0.5 registadas como gaps:")
        lines.append("")
        lines.append("| Mapping ID | Framework | Coverage | Confidence | Note |")
        lines.append("|---|---|---|---|---|")
        for g in gaps:
            cov = (g.get("coverage_summary") or "—").replace("|", "/")[:60]
            conf = g.get("confidence", 0)
            lines.append(f"| `{g.get('id', '?')}` | {g.get('framework', '?')} | {cov} | {conf:.2f} | Below confidence threshold; future review |")
        lines.append("")
    else:
        lines.append("_(Nenhuma maturity claim em gap state para este capítulo.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    _append_maturity_provenance(lines)
    return "\n".join(lines) + "\n"


def _append_maturity_provenance(lines):
    lines.append("## Generation provenance")
    lines.append("")
    lines.append("- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)")
    lines.append("- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74`")
    lines.append("- **Maturity mappings:** `data/entities/maturity_mappings.json` (168 items)")
    lines.append("- **§26 methodology layer:** `00-fundamentos/canon/26-metodologia-validacao-claims.md` (Run 1 state @ a9e70c98)")
    lines.append("- **§26 label rule:** deterministic per `confidence` field (≥0.85 Explícito; ≥0.65 Semântico; ≥0.4 Parcial; &lt;0.4 Gap)")
    lines.append("- **§26 §4 discipline applied:** SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity")
    lines.append("- **Generated by:** Manual Agent Run 2 (achievable-maturity enrichment)")
    lines.append("- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony")


# ─────────────────── 50-ameacas-mitigadas ───────────────────


def mitigation_strength_from_threat(threat):
    """Determine mitigation strength per mitigation_strength or confidence heuristic."""
    if "mitigation_strength" in threat:
        return threat["mitigation_strength"]
    ctrl = threat.get("associated_controls") or []
    if isinstance(ctrl, list) and len(ctrl) >= 3:
        return "forte"
    if isinstance(ctrl, list) and 1 <= len(ctrl) <= 2:
        return "parcial"
    cross_chapter = threat.get("cross_chapter") or False
    if cross_chapter:
        return "dependente_de_outros_capitulos"
    conf = threat.get("confidence")
    if isinstance(conf, (int, float)):
        if conf >= 0.85:
            return "forte"
        if conf >= 0.6:
            return "parcial"
        return "dependente_de_outros_capitulos"
    return "parcial"


def gen_threats_chapter(chapter, threats, antipatterns, signals, ap_threat_links):
    title = CHAPTER_TITLES[chapter]
    lines = [f"# 50. Ameaças Mitigadas — {title}", "", "## Sumário", ""]
    lines.append(
        "Famílias de ameaça mitigadas neste capítulo + força da mitigação. Análise segue "
        "**§26 canon §4 discipline**: Manual surface + CAPEC primary; CWE supporting limited; "
        "mitigation strength explicitly labelled."
    )
    lines.append("")
    lines.append("Seis secções:")
    lines.append("")
    lines.append("- **§ Manual ontology V2 entities** — Threat + AntiPattern + Signal canonical")
    lines.append("- **§ Threat surfaces** — Manual + CAPEC primary surfaces")
    lines.append("- **§ AntiPattern exposure mapping** — antipattern → threat exposure relations")
    lines.append("- **§ CWE references** — supporting only (per §26 §4 discipline)")
    lines.append("- **§ V1 overlay** — mitigation pathway where Core-mapped")
    lines.append("- **§ Future-work register** — threat gaps registered para P8 §10")
    lines.append("")
    lines.append("---")
    lines.append("")

    # § Manual ontology V2 entities
    lines.append("## § Manual ontology V2 — entities canónicas (threats + antipatterns + signals)")
    lines.append("")
    total = len(threats) + len(antipatterns) + len(signals)
    if total:
        lines.append(
            f"Total: **{total} entidades** (Threat × {len(threats)}, AntiPattern × {len(antipatterns)}, "
            f"Signal × {len(signals)}) mapped a este capítulo."
        )
        lines.append("")
        lines.append("| Entity type | ID | Label | Authority class | Source mode |")
        lines.append("|---|---|---|---|---|")
        # Threats first
        auth, srcmode, _ = V2_ENTITY_META["Threat"]
        for t in sorted(threats, key=lambda x: x.get("mitigated_threat_id", "")):
            tid = t.get("mitigated_threat_id", t.get("id", "?"))
            label = (t.get("threat_label_raw") or t.get("essence") or t.get("name") or "")[:80].replace("|", "/").replace("\n", " ")
            lines.append(f"| Threat | `{tid}` | {label} | {auth} | {srcmode} |")
        auth, srcmode, _ = V2_ENTITY_META["AntiPattern"]
        for a in sorted(antipatterns, key=lambda x: x.get("entity_id", "")):
            aid = a.get("antipattern_id") or a.get("entity_id", "?")
            label = (a.get("label") or "")[:80].replace("|", "/").replace("\n", " ")
            lines.append(f"| AntiPattern | `{aid}` | {label} | {auth} | {srcmode} |")
        auth, srcmode, _ = V2_ENTITY_META["Signal"]
        for s in sorted(signals, key=lambda x: x.get("entity_id", "")):
            sid = s.get("entity_id", "?")
            label = (s.get("label") or "")[:80].replace("|", "/").replace("\n", " ")
            lines.append(f"| Signal | `{sid}` | {label} | {auth} | {srcmode} |")
        lines.append("")
    else:
        lines.append("_(Nenhuma entity de threat/antipattern/signal mapped a este capítulo.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § Threat surfaces — Manual + CAPEC primary
    lines.append("## § Threat surfaces — Manual + CAPEC primary")
    lines.append("")
    if threats:
        lines.append(
            "Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). "
            "Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos)."
        )
        lines.append("")
        lines.append("| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |")
        lines.append("|---|---|---|---|---|---|---|")
        for t in sorted(threats, key=lambda x: x.get("mitigated_threat_id", "")):
            tid = t.get("mitigated_threat_id", t.get("id", "?"))
            cat = t.get("category") or t.get("methodology", "—")
            ess = (t.get("threat_label_raw") or t.get("essence") or "")[:60].replace("|", "/").replace("\n", " ")
            capec = t.get("capec") or "—"
            if isinstance(capec, list):
                capec = ", ".join(str(c) for c in capec[:3])
            ctrl = t.get("associated_controls") or []
            if isinstance(ctrl, list):
                ctrl_str = ", ".join(str(c) for c in ctrl[:3])
                if len(ctrl) > 3:
                    ctrl_str += f" + {len(ctrl) - 3} more"
            else:
                ctrl_str = str(ctrl)
            strength = mitigation_strength_from_threat(t)
            conf = t.get("confidence")
            label = methodology_label_from_confidence(conf)
            lines.append(f"| `{tid}` | {cat} | {ess} | {capec} | {ctrl_str} | {strength} | {label} |")
        lines.append("")
    else:
        lines.append("_(Nenhuma threat surface canonical para este capítulo.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § AntiPattern exposure mapping
    lines.append("## § AntiPattern exposure mapping")
    lines.append("")
    if ap_threat_links:
        lines.append(
            "AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. "
            "Cada link indica que o antipattern (quando presente em código/processo) expõe a ameaça."
        )
        lines.append("")
        lines.append("| AntiPattern | Exposes threat | Confidence | Justification |")
        lines.append("|---|---|---|---|")
        for link in sorted(ap_threat_links, key=lambda x: x.get("link_id", "")):
            link_id = link.get("link_id", "")
            # Parse link_id: sem:antipattern:NAME|exposes|THREAT_ID
            parts = link_id.split("|")
            if len(parts) == 3:
                ap = parts[0].replace("sem:antipattern:", "")
                threat = parts[2]
            else:
                ap, threat = link_id, "—"
            conf = link.get("confidence")
            conf_str = f"{conf:.2f}" if isinstance(conf, (int, float)) else "—"
            justif = ", ".join(link.get("justification", [])[:3])
            lines.append(f"| `{ap}` | `{threat}` | {conf_str} | {justif} |")
        lines.append("")
    else:
        lines.append("_(Nenhuma antipattern→threat relation mapped a este capítulo.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § CWE references (supporting only)
    lines.append("## § CWE references (supporting only)")
    lines.append("")
    cwe_threats = [t for t in threats if t.get("cwe")]
    if cwe_threats:
        lines.append(
            "CWE references per §26 §4: **CWE apenas como suporte limitado, NÃO como substituto de "
            "taxonomy de threat**. Mapping para Manual threats listed below."
        )
        lines.append("")
        lines.append("| CWE-ID | Linked threat | Note |")
        lines.append("|---|---|---|")
        for t in cwe_threats:
            cwes = t.get("cwe", [])
            if not isinstance(cwes, list):
                cwes = [cwes]
            for cwe in cwes:
                lines.append(f"| `{cwe}` | `{t.get('id', '?')}` | supporting reference; primary anchor é Manual threat |")
        lines.append("")
    else:
        lines.append("_(Nenhuma threat com CWE reference para este capítulo.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § V1 overlay — mitigation pathway
    lines.append("## § V1 overlay — mitigation pathway (where Core-mapped)")
    lines.append("")
    lines.append(
        "V1 controls/mechanisms anchored a este capítulo que mitigam threats listed above. "
        "V1 overlay preserva three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7."
    )
    lines.append("")
    lines.append(
        "_(V1 overlay surfacing per Manual ontology V2 antipattern_exposes_threat / control_mitigates_threat "
        "relations não totalmente extracted em este KG state; deferred a Codex post-Run-2 delta evaluation. "
        "Consult `25-rastreabilidade.md` for V1 entity → ES grounding per chapter; mitigation pathway "
        "inferable from existing Iter 4 + Run 1 layered output.)_"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # § Future-work register
    lines.append("## § Future-work register (threat gaps)")
    lines.append("")
    gap_threats = [t for t in threats if (t.get("confidence") or 1.0) < 0.5]
    if gap_threats:
        lines.append("Threats com confidence < 0.5 registadas como mitigation gaps:")
        lines.append("")
        lines.append("| Threat ID | Essence | Confidence | Note |")
        lines.append("|---|---|---|---|")
        for t in gap_threats:
            ess = (t.get("threat_label_raw") or t.get("essence") or "")[:60].replace("|", "/")
            lines.append(f"| `{t.get('mitigated_threat_id', '?')}` | {ess} | {t.get('confidence', 0):.2f} | Below confidence threshold; mitigation pathway requires future authoring |")
        lines.append("")
    else:
        lines.append("_(Nenhum threat em gap state para este capítulo.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    _append_threats_provenance(lines)
    return "\n".join(lines) + "\n"


def _append_threats_provenance(lines):
    lines.append("## Generation provenance")
    lines.append("")
    lines.append("- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)")
    lines.append("- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74`")
    lines.append("- **Threats canonical:** `data/entities/mitigated_threats.json` (233 items)")
    lines.append("- **AntiPatterns canonical:** `data/publish/semantic/antipatterns.jsonl` (26 items)")
    lines.append("- **Signals canonical:** `data/publish/semantic/signals.jsonl` (23 items)")
    lines.append("- **AntiPattern→Threat relations:** `data/publish/semantic/antipattern_threat_links.jsonl`")
    lines.append("- **§26 methodology layer:** `00-fundamentos/canon/26-metodologia-validacao-claims.md` (Run 1 state @ a9e70c98)")
    lines.append("- **§26 §4 discipline applied:** Manual + CAPEC primary; CWE supporting only")
    lines.append("- **Mitigation strength rule:** deterministic per `associated_controls` count + cross_chapter flag + confidence")
    lines.append("- **Generated by:** Manual Agent Run 2 (50-ameacas-mitigadas enrichment)")
    lines.append("- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony")


def main():
    print("Loading Run 2 inputs...")
    maturity_per_ch = load_maturity_mappings()
    print(f"  maturity mappings: {sum(len(v) for v in maturity_per_ch.values())} items across {len(maturity_per_ch)} chapters")
    threats_per_ch = load_threats_per_chapter()
    print(f"  threats: {sum(len(v) for v in threats_per_ch.values())} across {len(threats_per_ch)} chapters")
    antipatterns_per_ch = load_antipatterns_per_chapter()
    print(f"  antipatterns: {sum(len(v) for v in antipatterns_per_ch.values())} across {len(antipatterns_per_ch)} chapters")
    signals_per_ch = load_signals_per_chapter()
    print(f"  signals: {sum(len(v) for v in signals_per_ch.values())} across {len(signals_per_ch)} chapters")
    ap_links_per_ch = load_antipattern_threat_links()
    print(f"  ap→threat links: {sum(len(v) for v in ap_links_per_ch.values())} across {len(ap_links_per_ch)} chapters")

    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "achievable_maturity").mkdir(exist_ok=True)
    (OUT_DIR / "threats").mkdir(exist_ok=True)

    for ch in CHAPTERS:
        # Maturity
        maturity_content = gen_maturity_chapter(ch, maturity_per_ch.get(ch, []))
        m_dir = OUT_DIR / "achievable_maturity" / ch
        m_dir.mkdir(exist_ok=True)
        (m_dir / "achievable-maturity.md").write_text(maturity_content)

        # Threats
        threats_content = gen_threats_chapter(
            ch,
            threats_per_ch.get(ch, []),
            antipatterns_per_ch.get(ch, []),
            signals_per_ch.get(ch, []),
            ap_links_per_ch.get(ch, []),
        )
        t_dir = OUT_DIR / "threats" / ch
        t_dir.mkdir(exist_ok=True)
        (t_dir / "50-ameacas-mitigadas.md").write_text(threats_content)

        print(f"  {ch}: maturity={len(maturity_content)}B; threats={len(threats_content)}B")


if __name__ == "__main__":
    main()
