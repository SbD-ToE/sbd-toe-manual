---
id: convergencia-dora
title: Note - DORA & NIS2 Convergence
description: Guidance for organisations potentially within the scope of both DORA and NIS2
sidebar_position: 4
tags: [dora, nis2, convergencia, lex-specialis, governação]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/nis2/03-convergencia-dora.md
  source_sha256: d4a00c6bf9c22f19e7a70a549fed5dd03a13cecde32e2761e9844ca0193e93dd
  source_commit: 5bc57a2de453d4a50f78edcfb2b9546615b20690
  target_sha256: 86350f257ed9bdf57e0860db37ae663520fae07e16b8638a8920276eea8c9d82
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, avaliacao, dora_financial_entity, dora_ict_risk, dora_ict_tpp, eu_management_body, gap_family, mcp_reading_programa, nis2_essential_entity, piso_limiar, piso_relacao, practitioner_manual, programme_line, requirement_runtime, sbdtoe_sbd]
  glossary_sha256: e6e2e32b513d79d4060532412b2aad0690cde60fbc65ce2dadf7a18b0770b730
  translated_at: 2026-09-27T23:08:56Z
  stamped_at: 2026-09-27T23:08:56Z
  reviewed_by: null
---

# Note: Organisations Covered by Both DORA and NIS2

## Scope {#âmbito}

This note is intended for financial-sector organisations (banks, insurers, market infrastructures, intermediaries) that appear in NIS2 transpositions but are regulated primarily by DORA (Regulation (EU) 2022/2554). It summarises **lex specialis** principles, avoids duplication and guides integration into SbD-ToE.

What the Manual covers, the gaps it declares and what stays out of scope, obligation by obligation, are in the generated lists for each regime: [DORA — What this Manual covers and what stays out](/sbd-toe/cross-check-normativo/dora/requisitos-aplicaveis#cobertura) and [NIS2 — What this Manual covers and what stays out](/sbd-toe/cross-check-normativo/nis2/requisitos-aplicaveis#cobertura).

## The Lex Specialis Principle {#princípio-lex-specialis}

DORA is lex specialis for ICT risk management, resilience testing and incident reporting in regulated financial entities. Where there is thematic overlap:

| Topic | NIS2 Articles | DORA Articles | Which prevails |
|------|--------------|--------------|----------------|
| ICT governance | 20 | 5 | DORA (more financially specific) |
| Technical risk management | 21 | 6–16 | DORA |
| Testing/Resilience | 21 (generic) | 24–27 (testing, incl. TLPT in Art. 26–27); 11 (continuity) | DORA |
| Incident reporting | 23 (24h/72h/1M) | 17–20 (classification in Art. 18; reporting in Art. 19; RTS/ITS templates in Art. 20) | DORA (format / supervisory circuit) |
| Supply chain | 21 | 28–30 | DORA for ICT third-party service providers (reinforced when they support critical or important functions); NIS2 may complement general requirements |
| Threat sharing | 29 | 45 | DORA |

## What remains relevant from NIS2 {#o-que-continua-relevante-da-nis2}

Even under DORA, NIS2 aspects may retain value:
- A common language for interaction with non-financial essential/important entities (e.g. health, energy) that depend on banking services.
- Expectations of an **all-hazards approach** help justify the breadth of the controls. SbD-ToE covers the application part; the physical environment, business continuity and crisis management stay out of its scope.
- National requirements on **points of contact** or **registers of critical dependencies** may require documentary harmonisation.

## Duplication Risks (Avoid) {#riscos-de-duplicação-evitar}

| Potential duplication | Why avoid it | Recommended single form |
|----------------------|---------------|--------------------------|
| Two reporting flows (incidents) | Risk of inconsistent deadlines/data | Adopt the DORA flow; map NIS2 fields as a subset |
| Two control catalogues | Overhead, textual divergence | Use the SbD-ToE catalogue; the regulatory origin of each floor requirement and each added requirement is in the regulatory overlay (`_contextos-regulatorios.yaml`) and in the “Applicable requirements” pages |
| Two criticality classifications | Confusion in risk matrices | Keep L1–L3 per application (Ch. 01 axes). The regimes do not create parallel classes: they add floor requirements by context (CTX-DORA, CTX-NIS2) and by grade (FCI in DORA; PERTINENTE in NIS2). L1–L3 is not equivalent to a critical or important function, nor to an essential/important entity |
| Logs with different retention periods | Costs and ambiguity | Define and document the retention period per log type based on the ICT risk assessment (DORA: Delegated Regulation (EU) 2024/1774, Article 12(2), point (a); NIS2: Implementing Regulation (EU) 2024/2690, Annex, point 3.2.5, where applicable; national/sectoral legislation), applying a single period that satisfies both and respects the GDPR storage limitation where personal data are involved |

## Single Implementation Strategy (SbD-ToE) {#estratégia-de-implementação-única-sbd-toe}

1. **Master Digital Resilience Policy** - Integrates governance, testing, reporting and suppliers (references DORA Art. 5–6, 17–20, 24–27, 28–30; notes that, under Article 4 of NIS2 and Article 1(2) of DORA, the NIS2 risk-management and notification obligations do not apply to the financial entities covered).
2. **Regulatory origin** - The requirements catalogue ([Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)) has no regulatory origin column: the origin of each floor requirement and each added requirement is in the regulatory overlay (`_contextos-regulatorios.yaml`) and in each regime's “Applicable requirements” pages, generated from it.
3. **Incident record** - Common impact data (Policy 32 §4.3); the criterion and content follow DORA (CTX-DORA-R02; Policy 32 §6.1, with the templates of Implementing Regulation (EU) 2025/302); the NIS2 fields remain as an annotation for clients who ask for them.
4. **Exception process** - Approval authorities of Policy 05 §6 (in the Manual, the top is the CISO, and Critical is not acceptable at L3). Oversight of L3 exceptions by the management body is formalisation by the entity: it is out of scope of the Manual under DORA (Article 5) and a declared gap against NIS2.
5. **Supplier inventory** - Unify: SBOM (components), contractors ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)), ICT third-party service providers that support critical or important functions (flag whether required by DORA or by NIS2 clients).
6. **Training** - Policy 37 covers technical roles. Training of the management body (DORA Article 5(4); NIS2 Article 20(2)) and of non-technical staff belongs to the entity: out of scope of the Manual under DORA and a declared gap under NIS2. One track, two labels.

## Convergence Checklist (YES = ready) {#checklist-de-convergência-sim--pronto}

- [ ] Regulatory origin of each floor requirement and added requirement confirmed in the overlay (the DORA and NIS2 “Applicable requirements” pages).
- [ ] The master policy includes a section "Lex Specialis: DORA as a sector-specific act (NIS2 Art. 4; DORA Art. 1(2)) — NIS2 risk-management and notification obligations (and the related supervision) not applicable".
- [ ] Incident record with the impact data of Policy 32 §4.3 and the DORA content of §6.1; NIS2 fields as an annotation.
- [ ] Log retention defined per record type, with a single period that satisfies DORA and NIS2 and is grounded in the risk assessment (in SbD-ToE, at L3: 2 years for security logs and 3 years for audit, the Manual's choice).
- [ ] The supplier inventory indicates criticality + regulatory origin.
- [ ] Annual management training recorded by the entity (DORA and NIS2 content integrated; outside the Manual).
- [ ] Formal exception process (Policy 05), with periodic reporting of L3 exceptions to the management body defined by the entity.
- [ ] No divergent parallel playbooks exist (only annotations of differences).

## Frequently Asked Questions {#perguntas-frequentes}

**Q1. Do I need to report an incident twice?**  
No. The DORA circuit is followed. If the national authority requires an aggregated NIS2 view, the export in the DORA format is reused.

**Q2. What if a non-financial supplier invokes NIS2?**  
The supplier's demand is mapped to a control already satisfied under DORA; a SoA with the regulatory origin is sent.

**Q3. Is 1 year of logs enough for NIS2?**  
Neither DORA nor NIS2 sets a number: under DORA, the entity establishes the retention period taking into account the results of the ICT risk assessment (Delegated Regulation (EU) 2024/1774, Article 12(2)); Implementing Regulation (EU) 2024/2690 requires logs to be maintained «for a predefined period» (Annex, point 3.2.5). For convergence, a single period per record type reduces debate — in SbD-ToE, 2 years for security logs and 3 years for audit at L3 (the Manual's choice). Document the rationale.

**Q4. TLPT vs. NIS2 testing?**  
Carrying out TLPT, when the authority requires it, is strong evidence of the assessment of effectiveness, but does not exhaust it: NIS2 (Article 21(2)(f)) calls for the assessment of the measures as a whole. For the financial entity in scope, the DORA testing programme (Articles 24–27) counts, as a sector-specific act.

## References {#referências}

- Regulation (EU) 2022/2554 (DORA)
- Directive (EU) 2022/2555 (NIS2) Annexes I/II
- ENISA - NIS2 technical guidance (2024/2025)
- SbD-ToE Manual ([Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))

## Final Note {#nota-final}

SbD-ToE already abstracts technical controls. DORA/NIS2 convergence is achieved by **annotating the regulatory origin** and always using the **most demanding** form as the baseline - avoiding redundancy and maintaining operational elegance.
