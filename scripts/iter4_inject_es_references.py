#!/usr/bin/env python3
"""Iter 4 — Recreate 25-rastreabilidade.md with 4-section tabular structure.

Per Iter 4 dispatch 2026-05-11: rastreabilidade richness extension demonstrating
P8 pipeline primitive (Core-mapped + Manual-only + Out-of-AppSec + Future-work).

Inputs (same as Iter 3 + editorial declarations inline):
  - V1 instance index (slice → entity_ids)
  - 10 slice + 10 components drafts (entity_id → display name)
  - per_entity_source_map.json (entity → contributing sources + exemplars)
  - slice_to_chapter_map.yaml (slice → primary chapter)
  - phase23 classification (Phase 2/3 per-entity status)
  - editorial declarations (Manual-only + Out-of-AppSec per chapter, hardcoded)

Output: 15 markdown files at /tmp/iter3_path_d/out_iter4/<chapter>/25-rastreabilidade.md

Format: 4-section tabular per chapter (per dispatch vision 2026-05-11).
"""
import json
import re
from pathlib import Path

INPUT_DIR = Path("/tmp/iter3_path_d")
OUT_DIR = INPUT_DIR / "out_iter4"

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

# Short labels for ES grounding cells (compact)
ES_SHORT_LABELS = {
    "asvs_v5_0_0": "ASVS v5",
    "capec_v3_9": "CAPEC v3.9",
    "cis_controls_v8_1_2": "CIS Controls v8.1.2",
    "cwe_software_development_view_v4_19_1": "CWE SDV v4.19.1",
    "enisa_multilayer_ai_cybersecurity_practices_2023": "ENISA AI 2023",
    "eu_cra": "EU CRA",
    "eu_dora": "EU DORA",
    "eu_nis2": "EU NIS2",
    "eu_rgpd": "EU GDPR",
    "hipaa_security_rule": "HIPAA",
    "mcp_official_security_foundations_2025": "MCP Official 2025",
    "mitre_atlas": "MITRE ATLAS",
    "nist_ai_100_2_e2025": "NIST AI 100-2 e2025",
    "nist_ai_rmf_1_0": "NIST AI RMF 1.0",
    "nist_sp800_53_rev5": "SP 800-53 r5",
    "owasp_dsomm": "DSOMM",
    "owasp_llm_top_10": "OWASP LLM Top 10",
    "owasp_mcp_secure_server_development_v1_0": "OWASP MCP SSD v1.0",
    "owasp_mcp_third_party_servers_v1_0": "OWASP MCP 3P v1.0",
    "owasp_mcp_top_10_v0_1_2025_beta": "OWASP MCP Top 10",
    "owasp_ml_top_10": "OWASP ML Top 10",
    "owasp_proactive_controls_2018": "OWASP Proactive Controls",
    "owasp_samm_v2_1": "SAMM v2.1",
    "owasp_top_10_2021": "OWASP Top 10",
    "pci_dss_v4_0_1": "PCI DSS v4.0.1",
    "pci_sslc_v1_1": "PCI SSLC v1.1",
    "safecode_agile_2012": "SAFECode Agile",
    "safecode_fpssd_2018": "SAFECode FPSSD",
    "safecode_sic_2010": "SAFECode SIC",
    "slsa_spec_v1_0_build_track": "SLSA v1.0",
    "ssdf_sp800_218_v1_1": "SSDF v1.1",
}

# Editorial: Manual-only sections per chapter (out-of-Core-scope; ES-grounded direct).
# Heuristic-driven + Manual Agent judgment.
MANUAL_ONLY_PER_CHAPTER = {
    "03-threat-modeling": [
        ("achievable-maturity.md", "SAMM v2.1 maturity dimensions (D_TA, V_AA); DSOMM activities maturity levels"),
        ("policies-relevantes.md", "Política de Threat Modeling (organizational policy framing)"),
        ("addon/11-kpis-metricas.md", "KPIs e métricas operacionais de threat modeling (não-Core)"),
    ],
    "04-arquitetura-segura": [
        ("achievable-maturity.md", "SAMM v2.1 maturity (DM, AA, SR); DSOMM architecture activities"),
        ("policies-relevantes.md", "Política de Arquitetura Segura (organizational)"),
        ("addon/07-termos-e-glossario-arquitetura.md", "Glossário e terminologia (editorial reference)"),
        ("addon/10-kpis-metricas.md", "KPIs e métricas operacionais de arquitetura"),
    ],
    "05-dependencias-sbom-sca": [
        ("achievable-maturity.md", "SAMM v2.1 SCA maturity; DSOMM dependency activities"),
        ("policies-relevantes.md", "Política de SBOM e Gestão de Dependências"),
        ("addon/10-kpis-metricas.md", "KPIs operacionais SBOM/SCA"),
    ],
    "06-desenvolvimento-seguro": [
        ("achievable-maturity.md", "SAMM v2.1 SSDF practices maturity; DSOMM secure dev activities"),
        ("policies-relevantes.md", "Política de Desenvolvimento Seguro"),
        ("addon/07-guidelines-equipa.md", "Guidelines operacionais de equipa (organizational)"),
    ],
    "10-testes-seguranca": [
        ("achievable-maturity.md", "SAMM v2.1 ST maturity; DSOMM testing activities"),
        ("policies-relevantes.md", "Política de Testes de Segurança"),
        ("addon/00-catalogo-requisitos.md", "Catálogo de requisitos com componentes meta-testing (não-Core)"),
    ],
    "11-deploy-seguro": [
        ("achievable-maturity.md", "SAMM v2.1 OE maturity; DSOMM deploy activities"),
        ("policies-relevantes.md", "Política de Deploy Seguro"),
    ],
    "12-monitorizacao-operacoes": [
        ("achievable-maturity.md", "SAMM v2.1 OE/IM maturity; DSOMM operations activities"),
        ("policies-relevantes.md", "Política de Monitorização e Resposta a Incidentes"),
        ("addon/04-integracao-siem.md", "Integração SIEM/SOAR (operacional, vendor-specific)"),
    ],
}

# Editorial: Out-of-AppSec sections per chapter (pure editorial; no ES grounding).
OUT_OF_APPSEC_PER_CHAPTER = {
    "03-threat-modeling": [
        ("exemplo-privacidade.md", "Worked example: LINDDUN privacy threat modeling case"),
        ("exemplos-aplicacao-stride.md", "Worked examples: STRIDE application per architecture pattern"),
        ("addon/02-riscos-processo-threat-modeling.md", "Process-level reflections / lessons learned"),
        ("addon/10-integracao-iriusrisk.md", "Tooling integration example (IriusRisk-specific)"),
    ],
    "04-arquitetura-segura": [
        ("aplicacao-lifecycle.md", "User stories reutilizáveis (illustrative narrative)"),
        ("addon/02-casos-praticos.md", "Casos práticos worked examples"),
        ("addon/04-diagramas-referencia.md", "Diagramas de referência (illustrative)"),
        ("addon/09-decisao-evidencia-arquitetural.md", "ADR examples e narrativa de decisão"),
    ],
    "05-dependencias-sbom-sca": [
        ("addon/04-integracao-ci-cd.md", "Integração CI/CD examples (tooling-specific)"),
        ("addon/07-controle-registos-origem.md", "Registros de origem worked examples"),
    ],
    "06-desenvolvimento-seguro": [
        ("addon/01-boas-praticas-codigo.md", "Best practices narrative com code snippets"),
        ("addon/05-excecoes-e-justificacoes.md", "Exception cases narrative"),
        ("addon/09-anotacoes-evidencia.md", "Anotação semântica examples"),
    ],
    "10-testes-seguranca": [
        ("addon/11-pen-testing.md", "Pen-testing narrative e operacional"),
        ("addon/13-ia-nos-testes.md", "AI in testing — operational guidance (covered also in Iter 2 prose)"),
    ],
    "11-deploy-seguro": [
        ("addon/04-incident-response-playbook.md", "IR playbooks examples"),
    ],
    "12-monitorizacao-operacoes": [
        ("casos-praticos-monitorizacao.md", "Worked examples: incident response cases"),
        ("addon/09-exemplos-eventos.md", "Examples of security events"),
    ],
}

# Future-work register entries (P8 §10 candidates).
FUTURE_WORK = [
    ("ACM-IVF-004", "Centralized Error Translation And Redaction",
     "06-desenvolvimento-seguro",
     "Authoring pending — Phase 2/3 confirmed_content_gap; programme-lead 2026-05-11 ratified defer to future-cycle. "
     "Topic partially covered by Cap. 02 VAL-006/ERR family + Iter 2 §11 LLM input handling. "
     "Future authoring should consolidate into single Cap. 06 section."),
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


def load_per_entity_map():
    return json.loads((INPUT_DIR / "per_entity_source_map.json").read_text())


def load_phase23():
    return json.loads((INPUT_DIR / "phase23_classification.json").read_text())


def manual_section_anchor(eid, chapter, phase23_entry):
    """Determine Manual section anchor string for V1 entity."""
    if phase23_entry:
        cls = phase23_entry.get("refined_classification", "")
        if cls == "candidate_claim_gap":
            exp_match = phase23_entry["per_chapter_matches"].get(chapter, {})
            kws = exp_match.get("keywords_matched", [])[:3]
            kws_str = ", ".join(kws)
            return f"chapter prose ({kws_str} kws verified)"
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
    # Default: based on entity type
    if eid.startswith("ACO-"):
        return "intro.md; aplicacao-lifecycle.md"
    elif eid.startswith("ACP-"):
        return "addon/00-catalogo-requisitos.md"
    elif eid.startswith("ACM-"):
        return "addon/00-catalogo-requisitos.md (mechanism)"
    return "chapter primary"


def es_grounding_cell(sources_dict, top_n=4):
    """Build compact ES grounding string for table cell."""
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
            ids_str = ", ".join(exemplars)
            parts.append(f"{label}: {ids_str}")
        else:
            parts.append(label)
    if len(sorted_sources) > top_n:
        parts.append(f"+ {len(sorted_sources) - top_n} more sources")
    return "; ".join(parts)


def gen_chapter(chapter, slice_abbrs, entity_names, entity_sources, phase23_by_entity):
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
        # Out-of-AppSec / Manual-only if any declared for placeholder
        # (typically empty; placeholders are pure pointer chapters)
        _append_provenance(lines)
        return "\n".join(lines) + "\n"

    # Substantive chapter — 4 sections
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
        "Estrutura abaixo expõe four-way routing (per P8 pipeline primitive demonstration 2026-05-11):"
    )
    lines.append("")
    lines.append("- **§ Core-mapped coverage** — V1 entity → Manual section anchor → ES grounding")
    lines.append("- **§ Manual-only coverage** — Manual sections out-of-Core-scope mas com ES grounding direct")
    lines.append("- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) sem ES grounding")
    lines.append("- **§ Future-work register** — Content gaps registered as P8 §10 candidates")
    lines.append("")
    lines.append("---")
    lines.append("")

    # § Core-mapped
    lines.append("## § Core-mapped coverage")
    lines.append("")
    lines.append(
        "Tabela exposing V1 entity-level coverage with Manual section anchor + "
        "substrate v7 ES grounding. Three-way alignment per row: V1 (ontology) ↔ Manual (prose) ↔ ES (substrate)."
    )
    lines.append("")
    for sa in slice_abbrs:
        ents = entity_names.get(sa, {})
        if not ents:
            continue
        lines.append(f"### Slice `{sa}` — {SLICE_DESCRIPTIONS[sa]}")
        lines.append("")
        lines.append("| V1 entity | Type | Manual section anchor | ES grounding |")
        lines.append("|---|---|---|---|")
        for eid in sorted(eid for eid in ents if eid.startswith(("ACO-", "ACP-", "ACM-"))):
            name = ents[eid]
            entity_type = (
                "CO" if eid.startswith("ACO-")
                else "P" if eid.startswith("ACP-")
                else "M"
            )
            p23 = phase23_by_entity.get(eid)
            anchor = manual_section_anchor(eid, chapter, p23)
            src_data = entity_sources.get(eid, {})
            grounding = es_grounding_cell(src_data.get("sources", {}))
            # Use one cell with entity + name
            lines.append(f"| `{eid}` — {name} | {entity_type} | {anchor} | {grounding} |")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § Manual-only
    lines.append("## § Manual-only coverage (out-of-Core-scope; ES-grounded direct)")
    lines.append("")
    manual_only = MANUAL_ONLY_PER_CHAPTER.get(chapter, [])
    if manual_only:
        lines.append(
            "Manual sections that cover topics outside V1 AppSec Core ontology scope "
            "(maturity models, organizational policies, KPIs/metrics, glossaries) but with "
            "direct ES grounding to substrate v7 sources."
        )
        lines.append("")
        lines.append("| Manual section | ES grounding (direct) |")
        lines.append("|---|---|")
        for section, grounding in manual_only:
            lines.append(f"| `{section}` | {grounding} |")
        lines.append("")
    else:
        lines.append("_(Sem secções Manual-only declaradas para este capítulo nesta iteração.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § Out-of-AppSec
    lines.append("## § Out-of-AppSec coverage (pure editorial)")
    lines.append("")
    out_of_appsec = OUT_OF_APPSEC_PER_CHAPTER.get(chapter, [])
    if out_of_appsec:
        lines.append(
            "Manual sections that are pure editorial content (worked examples, narratives, "
            "illustrative cases, vendor-specific tooling integration). Sem ES grounding."
        )
        lines.append("")
        lines.append("| Manual section | Content type |")
        lines.append("|---|---|")
        for section, content_type in out_of_appsec:
            lines.append(f"| `{section}` | {content_type} |")
        lines.append("")
    else:
        lines.append("_(Sem secções Out-of-AppSec declaradas para este capítulo nesta iteração.)_")
        lines.append("")
    lines.append("---")
    lines.append("")

    # § Future-work register
    lines.append("## § Future-work register (P8 §10 candidates)")
    lines.append("")
    chapter_fw = [fw for fw in FUTURE_WORK if fw[2] == chapter]
    if chapter_fw:
        lines.append("Content gaps registered for future-cycle authoring; honest documentation per P8 §10 limitations.")
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
        "- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)"
    )
    lines.append("- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` em sbd-toe-ontology")
    lines.append(
        "- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`"
    )
    lines.append(
        "- **Phase 2/3 gap analysis:** `phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`"
    )
    lines.append("- **Slice → chapter map:** `slice_to_chapter_map.yaml` @ ESI commit `adbe4e0`")
    lines.append("- **Generated by:** Manual Agent Iter 4 (rastreabilidade richness extension)")
    lines.append(
        "- **Format:** 4-section tabular (Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11"
    )
    lines.append("- **Cycle:** Cycle B Iteration 4 (P8 pipeline primitive demonstration)")


def main():
    print("Loading inputs...")
    entity_names_per_slice = {}
    for sa in SLICE_FILES:
        entity_names_per_slice[sa] = parse_slice_draft(sa)
        print(f"  {sa}: {len(entity_names_per_slice[sa])} entities")

    per_entity = load_per_entity_map()
    entity_sources = per_entity.get("entities", {})

    phase23 = load_phase23()
    phase23_by_entity = {
        e["entity_id"]: e for e in phase23.get("per_entity_refined_classifications", [])
    }

    chapter_to_slices = {ch: [] for ch in CHAPTERS}
    for sa, ch in SLICE_TO_CHAPTER.items():
        chapter_to_slices[ch].append(sa)

    OUT_DIR.mkdir(exist_ok=True)
    for ch in CHAPTERS:
        slice_abbrs = sorted(chapter_to_slices[ch])
        content = gen_chapter(ch, slice_abbrs, entity_names_per_slice, entity_sources, phase23_by_entity)
        chdir = OUT_DIR / ch
        chdir.mkdir(exist_ok=True)
        outf = chdir / "25-rastreabilidade.md"
        outf.write_text(content)
        print(f"  {ch}: {len(content):>7} bytes")


if __name__ == "__main__":
    main()
