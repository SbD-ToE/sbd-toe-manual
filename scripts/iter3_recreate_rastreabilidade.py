#!/usr/bin/env python3
"""Iter 3 Path D — Recreate 15 25-rastreabilidade.md entity-first.

Inputs (canonical):
  - V1 instance index (slice → entity_ids list)
  - 10 slice drafts (entity_id → display name)
  - per_entity_source_map.json (entity → contributing sources + counts + exemplars)
  - slice_to_chapter_map.yaml (slice → primary chapter)

Output: 15 markdown files at /tmp/iter3_path_d/out/<chapter>/25-rastreabilidade.md

Format: entity-first (recreate, not patch — discards Bundle G2).
"""
import json
import re
from pathlib import Path

INPUT_DIR = Path("/tmp/iter3_path_d")
OUT_DIR = INPUT_DIR / "out"

CHAPTERS = [
    "00-fundamentos",
    "01-classificacao-aplicacoes",
    "02-requisitos-seguranca",
    "03-threat-modeling",
    "04-arquitetura-segura",
    "05-dependencias-sbom-sca",
    "06-desenvolvimento-seguro",
    "07-cicd-seguro",
    "08-iac-infraestrutura",
    "09-containers-imagens",
    "10-testes-seguranca",
    "11-deploy-seguro",
    "12-monitorizacao-operacoes",
    "13-formacao-onboarding",
    "14-governanca-contratacao",
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

# Slice → primary chapter (from slice_to_chapter_map.yaml, manually extracted)
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

# Slice abbreviation → display description (PT, for sumário)
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

# Slice file mapping
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

# Source pretty names (matches Cartographer's ES_DISPLAY_NAMES)
ES_DISPLAY_NAMES = {
    "asvs_v5_0_0": "OWASP ASVS v5.0.0",
    "capec_v3_9": "MITRE CAPEC v3.9",
    "cis_controls_v8_1_2": "CIS Controls v8.1.2",
    "cwe_software_development_view_v4_19_1": "MITRE CWE — Software Development View (v4.19.1)",
    "enisa_multilayer_ai_cybersecurity_practices_2023": "ENISA — Multilayer AI Cybersecurity Practices (2023)",
    "eu_cra": "EU Cyber Resilience Act (CRA)",
    "eu_dora": "EU Digital Operational Resilience Act (DORA)",
    "eu_nis2": "EU NIS2 Directive",
    "eu_rgpd": "EU GDPR (RGPD)",
    "hipaa_security_rule": "HIPAA Security Rule",
    "mcp_official_security_foundations_2025": "Anthropic MCP — Official Security Foundations (2025)",
    "mitre_atlas": "MITRE ATLAS — Adversarial Threat Landscape for AI Systems",
    "nist_ai_100_2_e2025": "NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy",
    "nist_ai_rmf_1_0": "NIST AI RMF 1.0",
    "nist_sp800_53_rev5": "NIST SP 800-53 Rev. 5",
    "owasp_dsomm": "OWASP DSOMM",
    "owasp_llm_top_10": "OWASP LLM Top 10 (2025)",
    "owasp_mcp_secure_server_development_v1_0": "OWASP MCP — Secure Server Development v1.0",
    "owasp_mcp_third_party_servers_v1_0": "OWASP MCP — Third-Party Servers v1.0",
    "owasp_mcp_top_10_v0_1_2025_beta": "OWASP MCP Top 10 (v0.1, 2025 beta)",
    "owasp_ml_top_10": "OWASP Machine Learning Top 10",
    "owasp_proactive_controls_2018": "OWASP Proactive Controls (2018)",
    "owasp_samm_v2_1": "OWASP SAMM v2.1",
    "owasp_top_10_2021": "OWASP Top 10 (2021)",
    "pci_dss_v4_0_1": "PCI DSS v4.0.1",
    "pci_sslc_v1_1": "PCI Secure SLC v1.1",
    "safecode_agile_2012": "SAFECode — Practical Security Stories and Tasks for Agile Development (2012)",
    "safecode_fpssd_2018": "SAFECode — Fundamental Practices for Secure Software Development (2018)",
    "safecode_sic_2010": "SAFECode — Software Integrity Controls (2010)",
    "slsa_spec_v1_0_build_track": "SLSA Specification v1.0 — Build Track",
    "ssdf_sp800_218_v1_1": "NIST SSDF (SP 800-218 v1.1)",
}


def parse_slice_draft(slice_abbr):
    """Extract entity_id → name from slice + components drafts."""
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


def parse_v1_index():
    """Parse V1 index — return slice_abbr → [entity_ids ordered: CO, P, M]."""
    path = INPUT_DIR / "v1_index.yaml"
    text = path.read_text()
    # Find slice_instances blocks
    slices = {}
    # Match per-slice block
    slice_blocks = re.findall(
        r"- slice_id: (ASC-\d+)\n.*?scope: (\w+)(.*?)(?=- slice_id:|\Z)",
        text, re.DOTALL,
    )
    # Better: parse line-by-line
    current_slice_abbr = None
    current_ids = {"control_objectives": [], "practices": [], "mechanisms": []}
    in_slice_instances = False
    for line in text.split("\n"):
        if line.strip() == "slice_instances:":
            in_slice_instances = True
            continue
        if not in_slice_instances:
            continue
        # New slice
        m = re.match(r"^  - slice_id: (ASC-\d+)", line)
        if m:
            # save previous
            if current_slice_abbr:
                slices[current_slice_abbr] = current_ids
            current_slice_abbr = None
            current_ids = {"control_objectives": [], "practices": [], "mechanisms": []}
        # scope determines slice_abbr
        m = re.match(r"^    scope: (\w+)", line)
        if m:
            scope = m.group(1)
            # Map scope → slice_abbr
            scope_to_abbr = {
                "supply_chain_and_build_integrity": "ACO-SCBI",
                "identity_access_and_session_trust": "ACO-IAT",
                "architecture_and_trust_boundaries": "ACO-ATB",
                "testing_security_validation_and_empirical_assurance": "ACO-TSV",
                "threat_modeling_risk_disposition_and_mitigation_traceability": "ACO-TMR",
                "secret_handling_protected_configuration_and_operational_identities": "ACO-SPC",
                "input_output_data_safety_and_controlled_failure": "ACO-IVF",
                "integration_trust_and_service_to_service_security": "ACO-ITS",
                "release_promotion_controlled_rollout_and_rollback_readiness": "ACO-RPR",
                "security_event_logging_audit_trail_and_centralized_logging": "ACO-SLG",
            }
            current_slice_abbr = scope_to_abbr.get(scope)
        # control_objectives, practices, mechanisms lists
        for key in ("control_objectives", "practices", "mechanisms"):
            m = re.match(rf"^    {key}:\s*\[(.+)\]", line)
            if m:
                ids = [x.strip() for x in m.group(1).split(",")]
                current_ids[key] = ids
    if current_slice_abbr:
        slices[current_slice_abbr] = current_ids
    return slices


def load_per_entity_map():
    return json.loads((INPUT_DIR / "per_entity_source_map.json").read_text())


def load_phase23():
    return json.loads((INPUT_DIR / "phase23_classification.json").read_text())


def gen_chapter(chapter, slice_abbrs, entity_names, entity_sources, phase23_by_entity):
    """Generate one chapter's 25-rastreabilidade.md content."""
    title = CHAPTER_TITLES[chapter]
    lines = [f"# 25. Rastreabilidade — {title}", "", "## Sumário", ""]

    if not slice_abbrs:
        # Placeholder chapter — no primary anchor
        lines.append(
            f"Este capítulo **não é âncora primária** de nenhuma slice AppSec Core V1. "
            "As referências externas relevantes para este domínio encontram-se nos capítulos "
            "onde cada slice ancora primariamente, listados abaixo."
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
        _append_provenance(lines)
        return "\n".join(lines) + "\n"

    # Substantive chapter
    total_co = total_p = total_m = 0
    for sa in slice_abbrs:
        for eid in entity_names.get(sa, {}):
            if eid.startswith("ACO-"):
                total_co += 1
            elif eid.startswith("ACP-"):
                total_p += 1
            elif eid.startswith("ACM-"):
                total_m += 1

    slice_list = ", ".join(f"`{sa}` ({SLICE_DESCRIPTIONS[sa]})" for sa in slice_abbrs)
    lines.append(
        f"Este capítulo é a **âncora primária** das slices AppSec Core V1: {slice_list}."
    )
    lines.append("")
    lines.append(
        f"Cobertura V1 entity-level: **{total_co + total_p + total_m} entidades** "
        f"primárias ({total_co} ControlObjectives + {total_p} Practices + {total_m} Mechanisms). "
        "Cada entidade é listada abaixo com cobertura no Manual (prose anchor) e fontes "
        "externas substrate v7 que contribuem para a sua substantive coverage."
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per slice
    for sa in slice_abbrs:
        ents = entity_names.get(sa, {})
        if not ents:
            continue
        lines.append(f"## Slice `{sa}` — {SLICE_DESCRIPTIONS[sa]}")
        lines.append("")
        # Group by type
        cos = sorted(eid for eid in ents if eid.startswith("ACO-"))
        ps = sorted(eid for eid in ents if eid.startswith("ACP-"))
        ms = sorted(eid for eid in ents if eid.startswith("ACM-"))
        for type_label, group in (("ControlObjective", cos), ("Practice", ps), ("Mechanism", ms)):
            if not group:
                continue
            lines.append(f"### {type_label}s ({len(group)})")
            lines.append("")
            for eid in group:
                name = ents[eid]
                lines.append(f"#### `{eid}` — {name}")
                lines.append("")
                # Manual prose anchor — Phase 2/3 info if available
                p23 = phase23_by_entity.get(eid)
                if p23:
                    cls = p23.get("refined_classification", "")
                    if cls == "candidate_claim_gap":
                        exp_ch = p23["expected_chapter"]
                        exp_match = p23["per_chapter_matches"].get(exp_ch, {})
                        nkw = exp_match.get("n_keywords_matched", 0)
                        nocc = exp_match.get("total_occurrences", 0)
                        kws = ", ".join(exp_match.get("keywords_matched", [])[:5])
                        lines.append(
                            f"- **Manual prose:** coberto neste capítulo "
                            f"(verificação Phase 2/3 deterministic kw-match: {nkw} keywords × "
                            f"{nocc} ocorrências; principais: {kws})"
                        )
                    elif cls == "candidate_cross_reference_gap":
                        exp_ch = p23["expected_chapter"]
                        others = [
                            ch for ch, m in p23["per_chapter_matches"].items()
                            if ch != exp_ch
                            and m.get("n_keywords_matched", 0) >= 3
                            and m.get("total_occurrences", 0) >= 5
                        ]
                        lines.append(
                            f"- **Manual prose:** cobertura **cross-chapter** — content "
                            f"encontrado em " + ", ".join(f"Cap. {c.split('-')[0]} (`{c}`)" for c in others) +
                            f". Cap. expected ({exp_ch}) tem cobertura fraca; ler em chapter(s) listada(s)."
                        )
                    elif cls == "confirmed_content_gap":
                        lines.append(
                            f"- **Manual prose:** ⚠️ **content gap confirmado** — Phase 2/3 "
                            "kw-match não encontrou cobertura substantive. Registado como "
                            "future-work P8 §10 limitations (decisão programme-lead 2026-05-11)."
                        )
                else:
                    # No Phase 2/3 entry — assume covered (Phase 1 classification)
                    lines.append(
                        f"- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo "
                        "(Phase 1 baseline classification)."
                    )
                # Sources contributing
                src_data = entity_sources.get(eid, {})
                sources = src_data.get("sources", {})
                if sources:
                    total_claims = sum(s.get("grounded_claim_count", 0) for s in sources.values())
                    lines.append(
                        f"- **Substrate v7 contributing sources** ({total_claims} grounded claims em "
                        f"{len(sources)} fontes):"
                    )
                    sorted_sources = sorted(
                        sources.items(),
                        key=lambda kv: -kv[1].get("grounded_claim_count", 0),
                    )
                    for src_id, sdata in sorted_sources:
                        cnt = sdata.get("grounded_claim_count", 0)
                        exemplars = sdata.get("exemplar_item_ids", [])
                        pretty = ES_DISPLAY_NAMES.get(src_id, src_id)
                        exemplar_str = ", ".join(f"`{x}`" for x in exemplars[:3])
                        more = f" + {len(exemplars) - 3} more" if len(exemplars) > 3 else ""
                        lines.append(f"  - {pretty} — {cnt} refs ({exemplar_str}{more})")
                else:
                    lines.append(
                        "- **Substrate v7 contributing sources:** _(nenhuma fonte externa "
                        "directamente grounded a esta entidade no substrate v7; entidade existe "
                        "ontologically mas substrate v7 não a atinge — pode acontecer em "
                        "Practices/Mechanisms abstractos)_"
                    )
                lines.append("")
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
        "- **Phase 2/3 gap analysis:** `data/p8_gap_analysis/phase2_3/phase2_3_per_entity_classification.json` "
        "@ ESI commit `b8cd401`"
    )
    lines.append("- **Slice → chapter map:** `data/p7_olir_audit/p7_v2_corrected/canon_rewrite/slice_to_chapter_map.yaml`")
    lines.append("- **Generated by:** Manual Agent Iter 3 Path D (recreate; Bundle G2 deprecated)")
    lines.append("- **Format:** entity-first (per V1 entity → Manual prose anchor + substrate v7 contributing sources)")
    lines.append("- **Cycle:** Cycle B Iteration 3 (Stage 5 Editorial Feedback applied)")


def main():
    print("Loading inputs...")
    slices_idx = parse_v1_index()
    print(f"  V1 index: {len(slices_idx)} slices loaded")
    entity_names = {}
    for sa in slices_idx:
        entity_names[sa] = parse_slice_draft(sa)
        print(f"  {sa}: {len(entity_names[sa])} entities with names")

    per_entity = load_per_entity_map()
    entity_sources = per_entity.get("entities", {})
    print(f"  per_entity_source_map: {len(entity_sources)} entities")

    phase23 = load_phase23()
    phase23_by_entity = {
        e["entity_id"]: e for e in phase23.get("per_entity_refined_classifications", [])
    }
    print(f"  phase23: {len(phase23_by_entity)} gap entities")

    # Build chapter → [slices anchored]
    chapter_to_slices = {ch: [] for ch in CHAPTERS}
    for sa, ch in SLICE_TO_CHAPTER.items():
        chapter_to_slices[ch].append(sa)

    # Generate
    OUT_DIR.mkdir(exist_ok=True)
    for ch in CHAPTERS:
        slice_abbrs = sorted(chapter_to_slices[ch])
        content = gen_chapter(ch, slice_abbrs, entity_names, entity_sources, phase23_by_entity)
        chdir = OUT_DIR / ch
        chdir.mkdir(exist_ok=True)
        outf = chdir / "25-rastreabilidade.md"
        outf.write_text(content)
        size = len(content)
        n_slices = len(slice_abbrs)
        print(f"  {ch}: {size:>7} bytes ({n_slices} slices)")


if __name__ == "__main__":
    main()
