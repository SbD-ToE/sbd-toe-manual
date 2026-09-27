---
id: convergencia-dora
title: Note - DORA & NIS2 Convergence
description: Guidance for organisations potentially within the scope of both DORA and NIS2
sidebar_position: 4
tags: [dora, nis2, convergencia, lex-specialis, governação]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/nis2/03-convergencia-dora.md
  source_sha256: 332618a06a23efffa5db92550264e321ae115a160c1daa2a8628e34f26c9971d
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: e64f0722fe1198033b40da3cc56af6d91ddff319c752e733a489a8b87983dbe3
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, dora_financial_entity, dora_ict_risk, dora_ict_tpp, esquema_regime, nis2_essential_entity, practitioner_manual, requirement_runtime, sbdtoe_sbd, schema]
  glossary_sha256: efa6d8e8dc98c6c39d5f5fd9b08904c5e4a19c91b85e04b586ed217c83b1e114
  translated_at: 2026-09-27T07:05:57Z
  stamped_at: 2026-09-27T07:05:57Z
  reviewed_by: null
---

# Note: Organisations Covered by Both DORA and NIS2

## Scope {#âmbito}

This note is intended for financial-sector organisations (banks, insurers, market infrastructures, intermediaries) that appear in NIS2 transpositions but are regulated primarily by DORA (Regulation (EU) 2022/2554). It summarises **lex specialis** principles, avoids duplication and guides integration into SbD-ToE.

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
- Expectations of an **all-hazards approach** help justify the breadth of controls (already present in SbD-ToE).
- National requirements on **points of contact** or **registers of critical dependencies** may require documentary harmonisation.

## Duplication Risks (Avoid) {#riscos-de-duplicação-evitar}

| Potential duplication | Why avoid it | Recommended single form |
|----------------------|---------------|--------------------------|
| Two reporting flows (incidents) | Risk of inconsistent deadlines/data | Adopt the DORA flow; map NIS2 fields as a subset |
| Two control catalogues | Overhead, textual divergence | Use the SbD-ToE catalogue + mark the origin (DORA/NIS2/ISO) |
| Two criticality classifications | Confusion in risk matrices | Keep the SbD-ToE L1–L3; document that it meets the DORA & NIS2 classes |
| Logs with different retention periods | Costs and ambiguity | Define and document the retention period per log type based on the ICT risk assessment (DORA: Delegated Regulation (EU) 2024/1774, Article 12(2), point (a); NIS2: Implementing Regulation (EU) 2024/2690, Annex, point 3.2.5, where applicable; national/sectoral legislation), applying a single period that satisfies both and respects the GDPR storage limitation where personal data are involved |

## Single Implementation Strategy (SbD-ToE) {#estratégia-de-implementação-única-sbd-toe}

1. **Master Digital Resilience Policy** - Integrates governance, testing, reporting and suppliers (references DORA Art. 5–6, 17–20, 24–27, 28–30; notes that, under Article 4 of NIS2 and Article 1(2) of DORA, the NIS2 risk-management and notification obligations do not apply to the financial entities covered).
2. **Regulatory origin matrix** - For each technical requirement ([Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)), a new `Fonte` column with the enum: `DORA`, `NIS2`, `Ambas`, `Outras`.
3. **Incident schema** - Base = DORA RTS/ITS; mark additional NIS2 fields (e.g. significant impact on the provision of services) as optional.
4. **Exceptions process** - L3 escalation always with board oversight (covers DORA & NIS2 governance simultaneously).
5. **Supplier inventory** - Unify: SBOM (components), contractors ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)), ICT third-party service providers that support critical or important functions (flag whether required by DORA or by NIS2 clients).
6. **Training** - Annual board module (DORA governance) + all-hazards cyber module (NIS2), integrated; one track, two labels.

## Convergence Checklist (YES = ready) {#checklist-de-convergência-sim--pronto}

- [ ] The SbD-ToE requirements catalogue has the `Fonte` column filled in.
- [ ] The master policy includes a section "Lex Specialis: DORA as a sector-specific act (NIS2 Art. 4; DORA Art. 1(2)) — NIS2 risk-management and notification obligations (and the related supervision) not applicable".
- [ ] Incident schema based on the DORA RTS/ITS, with optional NIS2 fields.
- [ ] Log retention defined per record type, with a single period that satisfies DORA and NIS2 and is grounded in the risk assessment (in SbD-ToE, at L3: 2 years for security logs and 3 years for audit, the Manual's choice).
- [ ] The supplier inventory indicates criticality + regulatory origin.
- [ ] Annual management training recorded (DORA + NIS2 content integrated).
- [ ] Formal exceptions process with board approval for L3.
- [ ] No divergent parallel playbooks exist (only annotations of differences).

## Frequently Asked Questions {#perguntas-frequentes}

**Q1. Do I need to report an incident twice?**  
No. The DORA circuit is followed. If the national authority requires an aggregated NIS2 view, the export in the DORA format is reused.

**Q2. What if a non-financial supplier invokes NIS2?**  
The supplier's demand is mapped to a control already satisfied under DORA; a SoA with the regulatory origin is sent.

**Q3. Is 1 year of logs enough for NIS2?**  
Neither DORA nor NIS2 sets a number: under DORA, the entity establishes the retention period taking into account the results of the ICT risk assessment (Delegated Regulation (EU) 2024/1774, Article 12(2)); Implementing Regulation (EU) 2024/2690 requires logs to be maintained «for a predefined period» (Annex, point 3.2.5). For convergence, a single period per record type reduces debate — in SbD-ToE, 2 years for security logs and 3 years for audit at L3 (the Manual's choice). Document the rationale.

**Q4. TLPT vs. NIS2 testing?**  
Running TLPT (where applicable) satisfies and exceeds the generic NIS2 requirement to assess effectiveness.

## References {#referências}

- Regulation (EU) 2022/2554 (DORA)
- Directive (EU) 2022/2555 (NIS2) Annexes I/II
- ENISA - NIS2 technical guidance (2024/2025)
- SbD-ToE Manual ([Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))

## Final Note {#nota-final}

SbD-ToE already abstracts technical controls. DORA/NIS2 convergence is achieved by **annotating the regulatory origin** and always using the **most demanding** form as the baseline - avoiding redundancy and maintaining operational elegance.
