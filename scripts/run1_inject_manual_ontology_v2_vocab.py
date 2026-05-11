#!/usr/bin/env python3
"""Run 1 amendment — inject Manual ontology V2 vocab layer em 15 25-rastreabilidade.md.

Per Run 1 dispatch 2026-05-11. Iter 4 baseline (commit 16dfa5ae) extended with:
- NEW § Manual ontology V2 entities (per chapter, from KG canonical data)
- AMEND § Core-mapped: add Manual ontology V2 anchor + Authority class + Source mode + §26 label columns
- AMEND § Manual-only: add Manual ontology V2 anchor + Authority columns
- AMEND § Out-of-AppSec: add Manual ontology V2 anchor (if any) column
- PRESERVE § Future-work register

Inputs (same as Iter 3+4 + KG canonical files):
  - V1 instance index + slice + components drafts
  - per_entity_source_map.json
  - phase2_3_per_entity_classification.json
  - slice_to_chapter_map.yaml (implicit via SLICE_TO_CHAPTER)
  - sbd-toe-knowledge-graph canonical files (Requirements/Controls/Practices/MitigatedThreats + Concepts/Mechanisms/Patterns/AntiPatterns/Signals)

Output: 15 markdown files at /tmp/iter3_path_d/out_run1/<chapter>/25-rastreabilidade.md
"""
import json
import re
from pathlib import Path

INPUT_DIR = Path("/tmp/iter3_path_d")
KG_DIR = Path("/Volumes/G-DRIVE/Shared/SecurityByDesign-TheoryOfEverything/sbd-toe-knowledge-graph")
OUT_DIR = INPUT_DIR / "out_run1"

CHAPTERS = [
    "00-fundamentos", "01-classificacao-aplicacoes", "02-requisitos-seguranca",
    "03-threat-modeling", "04-arquitetura-segura", "05-dependencias-sbom-sca",
    "06-desenvolvimento-seguro", "07-cicd-seguro", "08-iac-infraestrutura",
    "09-containers-imagens", "10-testes-seguranca", "11-deploy-seguro",
    "12-monitorizacao-operacoes", "13-formacao-onboarding", "14-governanca-contratacao",
]

CHAPTER_TITLES = {
    "00-fundamentos": "Fundamentos",
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

SLICE_TO_CHAPTER = {
    "ACO-ATB": "04-arquitetura-segura",
    "ACO-IAT": "04-arquitetura-segura",
    "ACO-ITS": "04-arquitetura-segura",
    "ACO-IVF": "06-desenvolvimento-seguro",
    "ACO-RPR": "11-deploy-seguro",
    "ACO-SCBI": "05-dependencias-sbom-sca",
    "ACO-SLG": "12-monitorizacao-operacoes",
    "ACO-SPC": "06-desenvolvimento-seguro",
    "ACO-TMR": "03-threat-modeling",
    "ACO-TSV": "10-testes-seguranca",
}

SLICE_DESCRIPTIONS = {
    "ACO-ATB": "Arquitetura segura e fronteiras de confiança",
    "ACO-IAT": "Identidade, autenticação e gestão de sessões",
    "ACO-ITS": "Integração e segurança service-to-service",
    "ACO-IVF": "Validação de input, parsing seguro e tratamento controlado de erros",
    "ACO-RPR": "Release promotion, rollout controlado e readiness para rollback",
    "ACO-SCBI": "Integridade da supply chain de software e do build",
    "ACO-SLG": "Logging de eventos de segurança e audit trail",
    "ACO-SPC": "Gestão de segredos, configuração protegida e identidades operacionais",
    "ACO-TMR": "Threat modeling, gestão de risco e rastreabilidade de mitigações",
    "ACO-TSV": "Testes de segurança e validação empírica",
}

SLICE_FILES = {
    "ACO-ATB": "architecture-trust-boundaries",
    "ACO-IAT": "identity-access-session-trust",
    "ACO-IVF": "input-validation-safe-failure",
    "ACO-ITS": "integration-trust-service-security",
    "ACO-RPR": "release-promotion-controlled-rollout",
    "ACO-SCBI": "supply-chain-build-integrity",
    "ACO-SLG": "security-event-logging-audit-trail",
    "ACO-SPC": "secrets-protected-config",
    "ACO-TMR": "threat-modeling-risk-disposition",
    "ACO-TSV": "testing-security-validation",
}

ES_SHORT_LABELS = {
    "asvs_v5_0_0": "ASVS v5", "capec_v3_9": "CAPEC v3.9",
    "cis_controls_v8_1_2": "CIS Controls v8.1.2",
    "cwe_software_development_view_v4_19_1": "CWE SDV v4.19.1",
    "enisa_multilayer_ai_cybersecurity_practices_2023": "ENISA AI 2023",
    "eu_cra": "EU CRA", "eu_dora": "EU DORA", "eu_nis2": "EU NIS2", "eu_rgpd": "EU GDPR",
    "hipaa_security_rule": "HIPAA", "mcp_official_security_foundations_2025": "MCP Official 2025",
    "mitre_atlas": "MITRE ATLAS", "nist_ai_100_2_e2025": "NIST AI 100-2 e2025",
    "nist_ai_rmf_1_0": "NIST AI RMF 1.0", "nist_sp800_53_rev5": "SP 800-53 r5",
    "owasp_dsomm": "DSOMM", "owasp_llm_top_10": "OWASP LLM Top 10",
    "owasp_mcp_secure_server_development_v1_0": "OWASP MCP SSD v1.0",
    "owasp_mcp_third_party_servers_v1_0": "OWASP MCP 3P v1.0",
    "owasp_mcp_top_10_v0_1_2025_beta": "OWASP MCP Top 10",
    "owasp_ml_top_10": "OWASP ML Top 10", "owasp_proactive_controls_2018": "OWASP Proactive Controls",
    "owasp_samm_v2_1": "SAMM v2.1", "owasp_top_10_2021": "OWASP Top 10",
    "pci_dss_v4_0_1": "PCI DSS v4.0.1", "pci_sslc_v1_1": "PCI SSLC v1.1",
    "safecode_agile_2012": "SAFECode Agile", "safecode_fpssd_2018": "SAFECode FPSSD",
    "safecode_sic_2010": "SAFECode SIC", "slsa_spec_v1_0_build_track": "SLSA v1.0",
    "ssdf_sp800_218_v1_1": "SSDF v1.1",
}

# Manual ontology V2 — authority class + source mode + confidence per entity type
# (Inferred from sbdtoe-ontology.yaml + dispatch example table)
V2_ENTITY_META = {
    "Requirement": ("normative", "explicit", "deterministic"),
    "Control": ("normative", "explicit", "deterministic"),
    "Practice": ("normative", "explicit", "deterministic"),
    "Threat": ("normative", "heuristic", "bounded"),
    "Artifact": ("editorial", "explicit", "deterministic"),
    "Concept": ("semantic", "scored", "bounded"),
    "Mechanism": ("semantic", "scored", "bounded"),
    "Pattern": ("semantic", "scored", "bounded"),
    "AntiPattern": ("semantic", "scored", "bounded"),
    "Signal": ("semantic", "scored", "bounded"),
}

# V1 entity prefix → Manual ontology V2 anchor (semantic correspondence per dispatch)
V1_TO_V2_ANCHOR = {
    "ACO-": "Control / Requirement",
    "ACP-": "Practice",
    "ACM-": "Mechanism",
    "ACA-": "Artifact",
}

# §26 methodology label per Phase 1/2/3 classification (deterministic mapping)
METHODOLOGY_LABEL = {
    "phase_1_covered": "Explícito",
    "candidate_claim_gap": "Semântico",
    "candidate_cross_reference_gap": "Parcial",
    "confirmed_content_gap": "Gap",
    "scope_exclusion": "Scope boundary",
}

MANUAL_ONLY_PER_CHAPTER = {
    "03-threat-modeling": [
        ("achievable-maturity.md", "MaturityMapping", "SAMM v2.1 maturity dimensions; DSOMM activities"),
        ("policies-relevantes.md", "PolicyReference", "Política de Threat Modeling (organizational)"),
        ("addon/11-kpis-metricas.md", "ExternalFramework", "KPIs e métricas operacionais"),
    ],
    "04-arquitetura-segura": [
        ("achievable-maturity.md", "MaturityMapping", "SAMM v2.1 (DM, AA, SR); DSOMM architecture activities"),
        ("policies-relevantes.md", "PolicyReference", "Política de Arquitetura Segura"),
        ("addon/07-termos-e-glossario-arquitetura.md", "DocumentUnit", "Glossário e terminologia"),
        ("addon/10-kpis-metricas.md", "ExternalFramework", "KPIs operacionais de arquitetura"),
    ],
    "05-dependencias-sbom-sca": [
        ("achievable-maturity.md", "MaturityMapping", "SAMM v2.1 SCA maturity; DSOMM dependency activities"),
        ("policies-relevantes.md", "PolicyReference", "Política de SBOM e Gestão de Dependências"),
        ("addon/10-kpis-metricas.md", "ExternalFramework", "KPIs operacionais SBOM/SCA"),
    ],
    "06-desenvolvimento-seguro": [
        ("achievable-maturity.md", "MaturityMapping", "SAMM v2.1 SSDF practices maturity; DSOMM secure dev activities"),
        ("policies-relevantes.md", "PolicyReference", "Política de Desenvolvimento Seguro"),
        ("addon/07-guidelines-equipa.md", "OverlayPlaybook", "Guidelines operacionais de equipa"),
    ],
    "10-testes-seguranca": [
        ("achievable-maturity.md", "MaturityMapping", "SAMM v2.1 ST maturity; DSOMM testing activities"),
        ("policies-relevantes.md", "PolicyReference", "Política de Testes de Segurança"),
        ("addon/00-catalogo-requisitos.md", "ExternalFramework", "Catálogo requisitos com componentes meta-testing"),
    ],
    "11-deploy-seguro": [
        ("achievable-maturity.md", "MaturityMapping", "SAMM v2.1 OE maturity; DSOMM deploy activities"),
        ("policies-relevantes.md", "PolicyReference", "Política de Deploy Seguro"),
    ],
    "12-monitorizacao-operacoes": [
        ("achievable-maturity.md", "MaturityMapping", "SAMM v2.1 OE/IM maturity; DSOMM operations activities"),
        ("policies-relevantes.md", "PolicyReference", "Política de Monitorização e Resposta a Incidentes"),
        ("addon/04-integracao-siem.md", "ExternalObligation", "Integração SIEM/SOAR (operacional)"),
    ],
}

OUT_OF_APPSEC_PER_CHAPTER = {
    "03-threat-modeling": [
        ("exemplo-privacidade.md", "Worked example: LINDDUN privacy threat modeling", "DocumentUnit"),
        ("exemplos-aplicacao-stride.md", "Worked examples: STRIDE per architecture pattern", "DocumentUnit"),
        ("addon/02-riscos-processo-threat-modeling.md", "Process-level reflections / lessons learned", "DocumentUnit"),
        ("addon/10-integracao-iriusrisk.md", "Tooling integration example (IriusRisk)", "—"),
    ],
    "04-arquitetura-segura": [
        ("aplicacao-lifecycle.md", "User stories reutilizáveis (illustrative narrative)", "UserStory"),
        ("addon/02-casos-praticos.md", "Casos práticos worked examples", "DocumentUnit"),
        ("addon/04-diagramas-referencia.md", "Diagramas de referência (illustrative)", "DocumentUnit"),
        ("addon/09-decisao-evidencia-arquitetural.md", "ADR examples e narrativa de decisão", "DocumentUnit"),
    ],
    "05-dependencias-sbom-sca": [
        ("addon/04-integracao-ci-cd.md", "Integração CI/CD examples (tooling-specific)", "—"),
        ("addon/07-controle-registos-origem.md", "Registros de origem worked examples", "DocumentUnit"),
    ],
    "06-desenvolvimento-seguro": [
        ("addon/01-boas-praticas-codigo.md", "Best practices narrative com code snippets", "DocumentUnit"),
        ("addon/05-excecoes-e-justificacoes.md", "Exception cases narrative", "DocumentUnit"),
        ("addon/09-anotacoes-evidencia.md", "Anotação semântica examples", "DocumentUnit"),
    ],
    "10-testes-seguranca": [
        ("addon/11-pen-testing.md", "Pen-testing narrative e operacional", "DocumentUnit"),
        ("addon/13-ia-nos-testes.md", "AI in testing — operational guidance", "DocumentUnit"),
    ],
    "11-deploy-seguro": [
        ("addon/04-incident-response-playbook.md", "IR playbooks examples", "DocumentUnit"),
    ],
    "12-monitorizacao-operacoes": [
        ("casos-praticos-monitorizacao.md", "Worked examples: incident response cases", "DocumentUnit"),
        ("addon/09-exemplos-eventos.md", "Examples of security events", "DocumentUnit"),
    ],
}

FUTURE_WORK = [
    ("ACM-IVF-004", "Centralized Error Translation And Redaction",
     "06-desenvolvimento-seguro",
     "Authoring pending — Phase 2/3 confirmed_content_gap; programme-lead 2026-05-11 ratified defer. "
     "Topic partially covered by Cap. 02 VAL-006/ERR family + Iter 2 §11 LLM input handling."),
]


def parse_slice_draft(slice_abbr):
    fname = SLICE_FILES[slice_abbr]
    names = {}
    for prefix in ("slice", "components"):
        path = INPUT_DIR / f"{prefix}_{fname}.yaml"
        if not path.exists():
            continue
        text = path.read_text()
        pattern = re.compile(
            r"^  ((?:ACO|ACP|ACM|ACA)-[A-Z]+-\d+):\n    name:\s*(.+)$",
            re.MULTILINE,
        )
        for m in pattern.finditer(text):
            names[m.group(1)] = m.group(2).strip()
    return names


def load_kg_entities_per_chapter():
    """Build per-chapter index of Manual ontology V2 entities."""
    by_chapter = {ch: {
        "Requirement": [], "Control": [], "Practice": [], "Threat": [],
        "Concept": [], "Mechanism": [], "Pattern": [], "AntiPattern": [], "Signal": [],
    } for ch in CHAPTERS}

    def map_chapter(num):
        for ch in CHAPTERS:
            if ch.startswith(f"{num:02d}-"):
                return ch
        return None

    # Requirements (source_chapter int + source_bundle str)
    try:
        d = json.loads((KG_DIR / "data/entities/canonical_requirements_s7.json").read_text())
        for r in d.get("requirements", []):
            ch_bundle = r.get("source_bundle")
            if ch_bundle in by_chapter:
                by_chapter[ch_bundle]["Requirement"].append({
                    "id": r.get("requirement_id"),
                    "label": r.get("name", ""),
                })
    except Exception as e:
        print(f"WARN requirements: {e}")

    # Controls (chapter_ids list)
    try:
        d = json.loads((KG_DIR / "data/entities/canonical_controls.json").read_text())
        for c in d.get("items", []):
            for ch_id in c.get("chapter_ids", []):
                # chapter_ids may be int or str
                if isinstance(ch_id, int):
                    ch = map_chapter(ch_id)
                else:
                    ch = ch_id if ch_id in by_chapter else None
                if ch:
                    by_chapter[ch]["Control"].append({
                        "id": c.get("control_id"),
                        "label": c.get("label", c.get("name", "")),
                    })
    except Exception as e:
        print(f"WARN controls: {e}")

    # Practices (chapter_id str)
    try:
        d = json.loads((KG_DIR / "data/entities/practices.json").read_text())
        for p in d.get("items", []):
            ch_id = p.get("chapter_id")
            if isinstance(ch_id, int):
                ch = map_chapter(ch_id)
            else:
                ch = ch_id if ch_id in by_chapter else None
            if ch:
                by_chapter[ch]["Practice"].append({
                    "id": p.get("id"),
                    "label": p.get("label", p.get("normalized_label", "")),
                })
    except Exception as e:
        print(f"WARN practices: {e}")

    # Mitigated threats
    try:
        d = json.loads((KG_DIR / "data/entities/mitigated_threats.json").read_text())
        for t in d.get("items", []):
            ch_id = t.get("chapter_id")
            if isinstance(ch_id, int):
                ch = map_chapter(ch_id)
            else:
                ch = ch_id if ch_id in by_chapter else None
            if ch:
                by_chapter[ch]["Threat"].append({
                    "id": t.get("id"),
                    "label": (t.get("essence", "") or "")[:80],
                })
    except Exception as e:
        print(f"WARN threats: {e}")

    # Semantic entities (bundle_ids list)
    for sem_kind, sem_file in [
        ("Concept", "concepts.jsonl"),
        ("Mechanism", "mechanisms.jsonl"),
        ("Pattern", "patterns.jsonl"),
        ("AntiPattern", "antipatterns.jsonl"),
        ("Signal", "signals.jsonl"),
    ]:
        try:
            path = KG_DIR / "data/publish/semantic" / sem_file
            if not path.exists():
                continue
            for line in path.open():
                line = line.strip()
                if not line:
                    continue
                e = json.loads(line)
                for bundle in e.get("bundle_ids", []):
                    if bundle in by_chapter:
                        by_chapter[bundle][sem_kind].append({
                            "id": e.get("entity_id"),
                            "label": e.get("label", e.get("concept_id", e.get("entity_id", "")))[:80] if e.get("label") else e.get("entity_id", "")[:80],
                        })
        except Exception as e:
            print(f"WARN {sem_kind}: {e}")
    return by_chapter


def manual_section_anchor(eid, chapter, phase23_entry):
    if phase23_entry:
        cls = phase23_entry.get("refined_classification", "")
        if cls == "candidate_claim_gap":
            exp_match = phase23_entry["per_chapter_matches"].get(chapter, {})
            kws = exp_match.get("keywords_matched", [])[:3]
            return f"chapter prose ({', '.join(kws)} kws verified)"
        elif cls == "candidate_cross_reference_gap":
            exp_ch = phase23_entry["expected_chapter"]
            others = [
                ch for ch, m in phase23_entry["per_chapter_matches"].items()
                if ch != exp_ch
                and m.get("n_keywords_matched", 0) >= 3
                and m.get("total_occurrences", 0) >= 5
            ]
            return "cross-chapter → " + ", ".join(f"Cap. {c.split('-')[0]}" for c in others)
        elif cls == "confirmed_content_gap":
            return "⚠️ future-work (P8 §10)"
    if eid.startswith("ACO-"):
        return "intro.md; aplicacao-lifecycle.md"
    elif eid.startswith("ACP-"):
        return "addon/00-catalogo-requisitos.md"
    elif eid.startswith("ACM-"):
        return "addon/00-catalogo-requisitos.md (mechanism)"
    return "chapter primary"


def methodology_label_for(eid, phase23_entry):
    if phase23_entry:
        cls = phase23_entry.get("refined_classification", "")
        return METHODOLOGY_LABEL.get(cls, "—")
    if eid.startswith("ACA-"):
        return METHODOLOGY_LABEL["scope_exclusion"]
    return METHODOLOGY_LABEL["phase_1_covered"]


def v2_anchor_for(eid):
    for prefix, anchor in V1_TO_V2_ANCHOR.items():
        if eid.startswith(prefix):
            return anchor
    return "—"


def v2_authority_for(eid):
    """Return primary authority class for V1 entity per V1→V2 anchor."""
    if eid.startswith("ACO-"):
        return V2_ENTITY_META["Control"][0]
    elif eid.startswith("ACP-"):
        return V2_ENTITY_META["Practice"][0]
    elif eid.startswith("ACM-"):
        return V2_ENTITY_META["Mechanism"][0]
    elif eid.startswith("ACA-"):
        return V2_ENTITY_META["Artifact"][0]
    return "—"


def v2_source_mode_for(eid):
    if eid.startswith("ACO-"):
        return V2_ENTITY_META["Control"][1]
    elif eid.startswith("ACP-"):
        return V2_ENTITY_META["Practice"][1]
    elif eid.startswith("ACM-"):
        return V2_ENTITY_META["Mechanism"][1]
    elif eid.startswith("ACA-"):
        return V2_ENTITY_META["Artifact"][1]
    return "—"


def es_grounding_cell(sources_dict, top_n=4):
    if not sources_dict:
        return "_(ontological only; no substrate v7 grounding)_"
    sorted_sources = sorted(
        sources_dict.items(),
        key=lambda kv: -kv[1].get("grounded_claim_count", 0),
    )
    parts = []
    for src_id, sdata in sorted_sources[:top_n]:
        label = ES_SHORT_LABELS.get(src_id, src_id)
        exemplars = sdata.get("exemplar_item_ids", [])[:2]
        if exemplars:
            parts.append(f"{label}: {', '.join(exemplars)}")
        else:
            parts.append(label)
    if len(sorted_sources) > top_n:
        parts.append(f"+ {len(sorted_sources) - top_n} more sources")
    return "; ".join(parts)


def gen_v2_entities_section(by_chapter_kg, chapter):
    """Generate § Manual ontology V2 entities section for a chapter."""
    lines = ["## § Manual ontology V2 — entities canónicas deste capítulo", ""]
    entities = by_chapter_kg.get(chapter, {})
    total = sum(len(v) for v in entities.values())
    if total == 0:
        lines.append("_(Nenhuma entidade Manual ontology V2 directamente mapped a este capítulo nos canonical files actuais.)_")
        lines.append("")
        return lines
    lines.append(
        f"Total: **{total} entidades** Manual ontology V2 mapped a este capítulo via "
        "`sbd-toe-knowledge-graph` canonical data (post-merge 5550a74)."
    )
    lines.append("")
    lines.append("| Entity type | ID | Label | Authority class | Source mode | Confidence |")
    lines.append("|---|---|---|---|---|---|")
    # Order: normative first, then editorial, then semantic
    order = ["Requirement", "Control", "Practice", "Threat", "Concept", "Mechanism", "Pattern", "AntiPattern", "Signal"]
    for ekind in order:
        items = entities.get(ekind, [])
        if not items:
            continue
        auth, srcmode, conf = V2_ENTITY_META.get(ekind, ("—", "—", "—"))
        # Sort by ID; cap at 50 per type for compactness
        items = sorted(items, key=lambda x: (x.get("id") or ""))
        # Dedupe by id
        seen = set()
        for it in items:
            eid = it.get("id")
            if eid in seen:
                continue
            seen.add(eid)
            label = (it.get("label") or "").replace("|", "/").replace("\n", " ")[:80]
            lines.append(f"| {ekind} | `{eid}` | {label} | {auth} | {srcmode} | {conf} |")
    lines.append("")
    lines.append("> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).")
    lines.append("")
    return lines


def gen_chapter(chapter, slice_abbrs, entity_names, entity_sources, phase23_by_entity, by_chapter_kg):
    title = CHAPTER_TITLES[chapter]
    lines = [f"# 25. Rastreabilidade — {title}", "", "## Sumário", ""]

    if not slice_abbrs:
        lines.append(
            "Este capítulo **não é âncora primária** de nenhuma slice AppSec Core V1. "
            "As referências externas relevantes para este domínio encontram-se nos capítulos "
            "onde cada slice ancora primariamente."
        )
        lines.append("")
        lines.append("| Slice | Descrição | Anchored em |")
        lines.append("|---|---|---|")
        for sa, desc in SLICE_DESCRIPTIONS.items():
            ch = SLICE_TO_CHAPTER[sa]
            lines.append(f"| `{sa}` | {desc} | Cap. {ch.split('-')[0]} ({ch}) |")
        lines.append("")
        lines.append("---")
        lines.append("")
        # Add V2 entities section even for placeholder (KG may still have entities)
        lines.extend(gen_v2_entities_section(by_chapter_kg, chapter))
        lines.append("---")
        lines.append("")
        _append_provenance(lines)
        return "\n".join(lines) + "\n"

    slice_list = ", ".join(f"`{sa}` ({SLICE_DESCRIPTIONS[sa]})" for sa in slice_abbrs)
    total_entities = sum(
        len([eid for eid in entity_names.get(sa, {})
             if eid.startswith(("ACO-", "ACP-", "ACM-"))])
        for sa in slice_abbrs
    )
    lines.append(
        f"Este capítulo é a **âncora primária** das slices AppSec Core V1: {slice_list}."
    )
    lines.append("")
    lines.append(
        f"Cobertura V1 entity-level: **{total_entities} entidades** primárias. "
        "Estrutura abaixo expõe **five-section routing** (per Run 1 amendment 2026-05-11; "
        "P8 pipeline primitive demonstration):"
    )
    lines.append("")
    lines.append("- **§ Manual ontology V2 entities** — entidades canónicas Manual ontology V2 mapped a este capítulo (KG canonical data)")
    lines.append("- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding")
    lines.append("- **§ Manual-only coverage** — Manual sections out-of-Core-scope mas ES-grounded direct")
    lines.append("- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) sem ES grounding")
    lines.append("- **§ Future-work register** — Content gaps registered as P8 §10 candidates")
    lines.append("")
    lines.append("---")
    lines.append("")

    # NEW § Manual ontology V2 entities
    lines.extend(gen_v2_entities_section(by_chapter_kg, chapter))
    lines.append("---")
    lines.append("")

    # § Core-mapped (AMENDED with V2 anchor + Authority + Source mode + §26 label)
    lines.append("## § Core-mapped coverage")
    lines.append("")
    lines.append(
        "Tabela expondo cobertura V1 entity-level com Manual ontology V2 anchor + "
        "Manual section anchor + §26 methodology label + substrate v7 ES grounding."
    )
    lines.append("")
    for sa in slice_abbrs:
        ents = entity_names.get(sa, {})
        if not ents:
            continue
        lines.append(f"### Slice `{sa}` — {SLICE_DESCRIPTIONS[sa]}")
        lines.append("")
        lines.append(
            "| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |"
        )
        lines.append("|---|---|---|---|---|---|---|---|")
        for eid in sorted(eid for eid in ents if eid.startswith(("ACO-", "ACP-", "ACM-"))):
            name = ents[eid]
            entity_type = (
                "CO" if eid.startswith("ACO-")
                else "P" if eid.startswith("ACP-")
                else "M"
            )
            p23 = phase23_by_entity.get(eid)
            anchor = manual_section_anchor(eid, chapter, p23)
            v2_anchor = v2_anchor_for(eid)
            authority = v2_authority_for(eid)
            srcmode = v2_source_mode_for(eid)
            label = methodology_label_for(eid, p23)
            src_data = entity_sources.get(eid, {})
            grounding = es_grounding_cell(src_data.get("sources", {}))
            lines.append(
                f"| `{eid}` — {name} | {entity_type} | {v2_anchor} | {anchor} | {authority} | {srcmode} | {label} | {grounding} |"
            )
        lines.append("")
    lines.append("---")
    lines.append("")

    # § Manual-only (AMENDED with V2 anchor + Authority)
    lines.append("## § Manual-only coverage (out-of-Core-scope; ES-grounded direct)")
    lines.append("")
    manual_only = MANUAL_ONLY_PER_CHAPTER.get(chapter, [])
    if manual_only:
        lines.append(
            "Manual sections que cobrem tópicos fora do scope V1 AppSec Core ontology "
            "(maturity models, organizational policies, KPIs/metrics, glossaries) mas com ES grounding direct."
        )
        lines.append("")
        lines.append("| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |")
        lines.append("|---|---|---|---|")
        for section, v2_anchor, grounding in manual_only:
            # Determine authority based on V2 anchor type
            if v2_anchor in ("PolicyReference", "OverlayPlaybook"):
                authority = "editorial / external"
            elif v2_anchor in ("ExternalFramework", "ExternalObligation"):
                authority = "external"
            elif v2_anchor == "MaturityMapping":
                authority = "external"
            else:
                authority = "editorial"
            lines.append(f"| `{section}` | {v2_anchor} | {authority} | {grounding} |")
        lines.append("")
    else:
        lines.append("_(Sem secções Manual-only declaradas para este capítulo nesta iteração.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § Out-of-AppSec (AMENDED with V2 anchor if any)
    lines.append("## § Out-of-AppSec coverage (pure editorial)")
    lines.append("")
    out_of_appsec = OUT_OF_APPSEC_PER_CHAPTER.get(chapter, [])
    if out_of_appsec:
        lines.append(
            "Manual sections que são pure editorial content (worked examples, narrativas, "
            "illustrative cases, vendor-specific tooling integration). Sem ES grounding."
        )
        lines.append("")
        lines.append("| Manual section | Content type | Manual V2 anchor (if any) |")
        lines.append("|---|---|---|")
        for section, content_type, v2_anchor in out_of_appsec:
            lines.append(f"| `{section}` | {content_type} | {v2_anchor} |")
        lines.append("")
    else:
        lines.append("_(Sem secções Out-of-AppSec declaradas para este capítulo nesta iteração.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § Future-work register (PRESERVED)
    lines.append("## § Future-work register (P8 §10 candidates)")
    lines.append("")
    chapter_fw = [fw for fw in FUTURE_WORK if fw[2] == chapter]
    if chapter_fw:
        lines.append("Content gaps registered para future-cycle authoring; honest documentation per P8 §10 limitations.")
        lines.append("")
        lines.append("| V1 entity / topic | Status |")
        lines.append("|---|---|")
        for eid, name, _, status in chapter_fw:
            lines.append(f"| `{eid}` — {name} | {status} |")
        lines.append("")
    else:
        lines.append("_(Sem entradas no future-work register para este capítulo.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    _append_provenance(lines)
    return "\n".join(lines) + "\n"


def _append_provenance(lines):
    lines.append("## Generation provenance")
    lines.append("")
    lines.append(
        "- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)"
    )
    lines.append("- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74` (`kg-v1-cycle-b-iter-3-aligned-2026-05-11`)")
    lines.append("- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)")
    lines.append("- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` em sbd-toe-ontology")
    lines.append(
        "- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`"
    )
    lines.append(
        "- **Phase 2/3 gap analysis:** `phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`"
    )
    lines.append("- **Generated by:** Manual Agent Run 1 (Iter 4 baseline @ `16dfa5ae` + Manual ontology V2 vocab layer injection)")
    lines.append(
        "- **Format:** 5-section (Manual V2 entities + Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11"
    )
    lines.append("- **§26 methodology labels:** per `00-fundamentos/canon/26-metodologia-validacao-claims.md` (post Run 1 Step 0 refresh)")
    lines.append("- **Cycle:** Cycle B Run 1 (post Iter 4)")


def main():
    print("Loading inputs...")
    entity_names_per_slice = {}
    for sa in SLICE_FILES:
        entity_names_per_slice[sa] = parse_slice_draft(sa)
        print(f"  {sa}: {len(entity_names_per_slice[sa])} entities")

    per_entity = json.loads((INPUT_DIR / "per_entity_source_map.json").read_text())
    entity_sources = per_entity.get("entities", {})

    phase23 = json.loads((INPUT_DIR / "phase23_classification.json").read_text())
    phase23_by_entity = {
        e["entity_id"]: e for e in phase23.get("per_entity_refined_classifications", [])
    }

    print("Loading KG canonical entities per chapter...")
    by_chapter_kg = load_kg_entities_per_chapter()
    for ch, ents in by_chapter_kg.items():
        total = sum(len(v) for v in ents.values())
        if total > 0:
            print(f"  {ch}: {total} V2 entities")

    chapter_to_slices = {ch: [] for ch in CHAPTERS}
    for sa, ch in SLICE_TO_CHAPTER.items():
        chapter_to_slices[ch].append(sa)

    OUT_DIR.mkdir(exist_ok=True)
    for ch in CHAPTERS:
        slice_abbrs = sorted(chapter_to_slices[ch])
        content = gen_chapter(
            ch, slice_abbrs, entity_names_per_slice, entity_sources,
            phase23_by_entity, by_chapter_kg,
        )
        chdir = OUT_DIR / ch
        chdir.mkdir(exist_ok=True)
        outf = chdir / "25-rastreabilidade.md"
        outf.write_text(content)
        print(f"  {ch}: {len(content):>7} bytes")


if __name__ == "__main__":
    main()
