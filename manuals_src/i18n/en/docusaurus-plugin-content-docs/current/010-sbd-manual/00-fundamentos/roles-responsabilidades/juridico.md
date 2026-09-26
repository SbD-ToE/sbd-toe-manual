---
id: juridico
title: Legal
sidebar_label: ⚖️ Legal
description: What SbD-ToE requires to exist on the Legal side
tags: [juridico, legal, contratos, dpo, responsabilidades]
sidebar_position: 11.7
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/juridico.md
  source_sha256: 20afb0122010f254374521cc59b9afe4236660d8d03835b204a50fbf640f93d0
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: f863c05dddbfe94ff0407d636a105d0dc882039802f825f0c503bbc0ac20b4ce
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [chapter_role, papel_suporte, practitioner_manual, risk_level, role_juridico, role_juridico_dpo, role_procurement, sbdtoe_sbd, slug_threat_modeling, validation_evaluation]
  glossary_sha256: a26d2737ead7fbab0b7318f500d30cf92a857635d4abf0117a67c8244d62279f
  translated_at: 2026-09-26T17:23:57Z
  reviewed_by: null
---

# Legal

## Overview {#visão-geral}

Legal is **another domain of the organisation**. The Manual does not say how Legal drafts; it says what must exist: security clauses in contracts, legal validation where the risk level requires it, and the DPO where there is personal data.

It is a frequent partner of GRC / Compliance, but it is a role of its own: drafting and validating clauses is a competence that GRC does not claim.

### Key Responsibilities {#responsabilidades-principais}
- Integrate the security clauses into contracts with suppliers and contractors
- Validate clauses on data handling, location and *audit rights* with AI model providers
- Through the DPO, independently validate the privacy analysis at L3

**Specialisation:** Legal (DPO) — the data protection officer, who may be external.

### Organisational Context {#contexto-organizacional}
The contract is where a supplier's obligation is born. Without clauses, the Manual has no way to ask those who deliver from outside for demonstrable alignment.

## Regulatory Framework {#enquadramento-regulatório}

Supports:
- **GDPR**: Contracts with processors (Art. 28) and independence of the DPO (Art. 38)
- **DORA**: Contractual arrangements with ICT third parties
- **AI Act**: Contractual responsibilities along the AI system value chain

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}
Through the DPO, **independently review the LINDDUN analysis** at L3.

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Include **SbD-ToE clauses in contracts** and the minimum clauses of contracts with AI model providers.

**User Stories:**
- [US-02: Contractual security clauses](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-02---cláusulas-contratuais-de-segurança) - Supplier compliance (with Procurement)
- [US-21: Contracting AI model providers](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-21) - Legally and technically sustainable use (with GRC / Compliance and Procurement)

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
