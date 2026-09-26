---
id: intro
title: GDPR - Normative cross-check
description: How SbD-ToE covers the technical requirements of the GDPR (EU 2016/679)
tags: [cross-check, gdpr, privacidade, protecao-dados, art32, privacy-by-design]
sidebar_position: 7
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/gdpr/01-intro.md
  source_sha256: 9f31ae0c46b078f69ee647e4f3b96b039c400b3cf38573aa565f25c73bc7cf97
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 83c1362a76b56900dd6a2be7b012cd95168029be01d7b161592d533369cd23b2
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [avaliacao, cycle_iteration, gap_family, gdpr_pseudonymisation, gdpr_security_of_processing, lifecycle_phase, normative_empirical, role_juridico, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: a28d6ef83c6735d802775f3bbc6c4d1802b43b1dc9acdf7f5dc8ad5a00f0fb46
  translated_at: 2026-09-26T17:57:37Z
  reviewed_by: null
---

# GDPR: Normative cross-check

> For practical implementation, see the [SbD-ToE 4 GDPR Playbook](/sbd-toe/cross-check-normativo/gdpr/playbook).
>
> For universal application patterns, see the SbD-ToE core chapters (01–14).

## Scope {#âmbito}

The **General Data Protection Regulation (GDPR)** - **Regulation (EU) 2016/679** (CELEX: [32016R0679](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32016R0679)) - lays down principles and obligations for the processing of personal data. This cross-check focuses on the **technical dimension** aligned with SbD-ToE (security and engineering), recognising that several obligations are **legal-organisational** (legal basis, rights of the data subject, international transfers).

It is suggested that SbD-ToE be used as the technical core for the articles that require security measures, privacy-by-design and incident management, working with Legal/GRC for the rest.

---

## PART I: NORMATIVE ANALYSIS (GDPR → SbD-ToE) {#parte-i-análise-normativa-gdpr--sbd-toe}

### Principles (Art. 5) {#princípios-art-5}
They require: data minimisation, purpose limitation, accuracy, storage limitation, integrity and confidentiality, accountability.

SbD-ToE coverage:
- Ch. 01: Classification and identification of data by criticality (supports minimisation/retention)
- Ch. 02: Security requirements (confidentiality, integrity, availability)
- Ch. 04: Secure architecture (segregation, encryption, proportionate logging)
- Ch. 11: Validation before production (confirmation of requirements)

Intentional gap: Definition of legal bases, retention policies and purposes → outside the technical scope; handle in governance/DPO.

---

### Privacy by Design/Default (Art. 25) {#privacy-by-designdefault-art-25}
Requires privacy to be embedded in the design and default settings to be the most protective.

SbD-ToE coverage:
- Ch. 04: Secure architectural patterns (pseudonymisation, segmentation)
- Ch. 06–07: Pipelines with gates to prevent exposures (secrets, excessive data)
- Ch. 11: Pre-deploy checklists (privacy parameters by default)

Intentional gap: Catalogue of privacy patterns (e.g. LINDDUN) not included by default. Action: Add a Privacy Threat Modelling addon.

---

### Records of Processing Activities (Art. 30) {#registos-de-atividades-art-30}
Requires a ROPA (Record of Processing Activities).

SbD-ToE coverage (partial):
- Ch. 14: Governance and contracting (can host the ROPA process)
- Ch. 01: Application and data inventory supports the ROPA

Intentional gap: SbD-ToE does not provide a ROPA template. Action: Keep the ROPA in a GRC/Legal tool and reference SbD-ToE app IDs.

---

### Security of Processing (Art. 32) {#segurança-do-tratamento-art-32}
Requires appropriate technical and organisational measures: pseudonymisation, encryption, resilience, regular testing of effectiveness.

SbD-ToE coverage:
- Ch. 02: Minimum requirements per level (includes encryption, IAM, hardening)
- Ch. 04: Architecture (segregation, key management)
- Ch. 05: Vulnerability and dependency management (SBOM/SCA)
- Ch. 10: Security testing and continuous assessment
- Ch. 12: Monitoring, continuity and exercises

Intentional gap: Legal criteria of “appropriateness” and contextual risk analysis → integrate with the legal risk matrix.

---

### Personal Data Breach Notification (Art. 33/34) {#notificação-de-violação-art-3334}
Requires notifying the competent supervisory authority within 72h (Art. 33) and, where applicable, communicating the breach to the data subjects (Art. 34).

SbD-ToE coverage:
- Ch. 12: Incident detection, classification and response; runbooks
- Ch. 14: RACI for decisions and communications

Intentional gap: Formal notification templates and legal criteria for communication to data subjects → handled by Legal/DPO; integrate the fields into the runbook.

---

### DPIA - Data Protection Impact Assessment (Art. 35) {#dpia---avaliação-de-impacto-art-35}
Requires a DPIA where the processing is likely to result in a high risk.

SbD-ToE coverage (partial):
- Ch. 03: Threat Modelling (can serve as a technical basis)
- Ch. 04: Technical mitigation measures

Intentional gap: Complete DPIA methodology (includes risk analysis for data subjects, consultation of the DPO/authority). Action: Integrate TM artefacts into the DPIA report; add a Privacy TM add-on (LINDDUN) if needed.

---

### Processors (Art. 28) and Contracts {#subcontratantes-art-28-e-contratos}
Requires contracts with processors containing data protection clauses.

SbD-ToE coverage:
- Ch. 14: Supplier/contractor lifecycle and security clauses
- Ch. 05: Component transparency (SBOM) and third-party risk

Intentional gap: Specific data protection clauses (SCCs, processing annexes) → Legal/DPO.

---

## PART II: Convergences/Interactions {#parte-ii-convergênciasinterações}

- Incidents involving personal data may require dual notification: GDPR (72h) + sectoral regimes (e.g. NIS2/DORA). A single runbook with a reporting fork is suggested.
- Art. 32 measures complement NIS2/DORA controls (same technical basis; reusable evidence).

---

## Intentional Gaps (Summary) {#lacunas-intencionais-resumo}

| Area | Why it falls outside SbD-ToE | Recommended Action |
|------|------------------------------|------------------|
| Legal basis, purposes, rights | Legal matter | Process with the DPO; record in GRC |
| ROPA (Art. 30) | Administrative | GRC tool; reference app IDs |
| Complete DPIA | Legal-organisational methodology | Legal template; incorporate technical annexes |
| International transfers | Legal (Clauses, TIAs) | Legal; complementary technical measures |
| Formal notifications | Legal/communication | DPO templates; integration with the technical runbook |

---

## Simple Metric (Self-Assessment) {#métrica-simples-autoavaliação}

Answer YES:
1. Are the apps that process personal data classified, with the Art. 32 requirements implemented? ✓
2. Is privacy by default configured (minimal logs, limited retention, encryption by default)? ✓
3. Is there a DPIA process with technical annexes (TM, controls) where applicable? ✓
4. Is there an incident runbook with an active 72h timer and GDPR fields? ✓
5. Processors: contracts with technical clauses and verified security? ✓

≥4/5 → Good technical coverage. `<`3 → Prioritise Art. 32, PbD and 72h incidents.

---

## References {#referências}

- **GDPR**: Regulation (EU) 2016/679 (CELEX: [32016R0679](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32016R0679))
- ENISA - Guidelines on Security of Personal Data Processing
- EDPB - Guidelines (DPIA, Breach Notification)
- SbD-ToE Chapters 01–14

**Version:** 1.0  
**Date:** November 2025  
**Next review:** May 2026
