---
id: legal
title: Legal
sidebar_label: ⚖️ Legal
description: What SbD-ToE requires to exist on the Legal side
tags: [juridico, legal, contratos, dpo, responsabilidades]
sidebar_position: 11.7
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/legal.md
  source_sha256: 0b9dd6a98807776c72df2b780fc9f0aac54839e03e07acb7fada2b166ae41725
  source_commit: ae767ad0c676d5e086f60faac073845c8c77e0f3
  target_sha256: dd64b16feaf53bfa8d84534a038544df4321b31e58807160c9ba1251f7f3483c
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: fe18815f5e1e72cf3b21cbab85b700034933fdb346f1f87246bf671279c357f3
  glossary_keys: [chapter_role, eu_ai_system, papel_suporte, practitioner_manual, risk_level, role_juridico, role_juridico_dpo, role_procurement, sbdtoe_sbd, slug_threat_modeling, validation_evaluation]
  glossary_sha256: a8996bfc257e487ff141d36007d226c313262492df4d341c386bda356766903a
  translated_at: 2026-09-26T17:44:45Z
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
