---
id: policies-relevantes
title: Relevant policies
tags: [canon, politicas, risco, classificacao, excecao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/policies-relevantes.md
  source_sha256: 572a8a3b8e9493c2bdfb9631cd83415f5445e3bcb0da0a72ac4297b8cf9b3f9e
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 11401a40b7a5a871665826a0b162ff06e6d33f2a33a197938ea097a3008a16d7
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [avaliacao, categorize_sw, chapter_role, framework_source_corpus, maturity, practitioner_manual, traceability]
  glossary_sha256: 35da5116b0bd7b0369ceb0fa7cdd9e3bb1bc2cd08f4b7580a76763aa7f89afd5
  translated_at: 2026-09-27T07:53:39Z
  stamped_at: 2026-09-27T07:53:39Z
  reviewed_by: null
---

# Organisational Policies - Risk Management

The effective adoption of Chapter 01 - Risk Management - requires the existence of **formal organisational policies** that **frame, legitimise and sustain the application of the practices described in this chapter**.

---

## 📌 Fundamental note {#-nota-fundamental}

> ⚠️ The operational practices prescribed in this chapter (classification, review, acceptance, traceability) **must be formally legitimised by approved organisational policies**.

These policies:

- Make the practice of application risk management **visible and binding** within the organisation;
- Allow security decisions to stop depending on individual initiative;
- Serve as the normative basis for **internal and external audits**.

> 📎 The requirement for formal risk classification and acceptance policies is an **explicit expectation** in standards such as **ISO/IEC 27005**, **ENISA Risk Management**, **NIST SSDF** and **CIS Controls v8**.

> 🧩 This chapter **implements, in practice, what the policies define** - the policy approves, the chapter operationalises.

---

## 🧾 Recommended policies {#-políticas-recomendadas}

| Policy Name                                   | Mandatory? | Application                             | Minimum expected content                                                                                      |
|----------------------------------------------------|--------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [Application Risk Classification Policy](/sbd-toe/assets/policies/policy-classificacao-risco)    | ✅ Yes       | All projects and product teams | Mandatory classification model (exposure, data, impact); moments of application; recording and tracking. |
| [Residual Risk Acceptance Policy](/sbd-toe/assets/policies/policy-aceitacao-risco)            | ✅ Yes       | Security, management, product owners    | Formal criteria for acceptance; those responsible; temporal validity; recording and traceability.               |
| [Periodic Risk Review Policy](/sbd-toe/assets/policies/policy-revisao-periodica-risco)             | ✅ Yes       | The whole organisation                     | Minimum frequency per level (12 / 6 / 3 months); mandatory triggers; evidence required.                                   |
| [Security Decision Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade) | ⚠️ Optional | Organisations subject to audit      | Versioning of classifications; link to architecture, requirements and controls.                           |

---

## 🧩 Correspondence with normative frameworks {#-correspondência-com-frameworks-normativas}

| Framework              | Requirements covered by the policies above                                       |
|------------------------|----------------------------------------------------------------------------------|
| **ISO/IEC 27005**      | Identification (8.2), Assessment (8.3), Acceptance (8.5)                            |
| **NIST SP 800-30**     | Steps 1–4 (Characterisation, Threats, Vulnerabilities, Impact)                 |
| **NIST SSDF**          | RM.1 (Categorize SW), RM.2 (Assess Risk), RM.3 (Manage Risk)                    |
| **ENISA Risk Management** | Sec. 2.3, 3.1 - formal definition of risk assessment and acceptance policies |
| **CIS Controls v8**    | Controls 2, 4 - policies for inventory, risk assessment and acceptance         |
| **OWASP SAMM**         | Governance > Risk Management (levels 1 and 2)                                      |


---

## 🧱 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each organisational policy must contain, at a minimum:

- **Objective and scope** of the policy;
- **Scope of application**: who, where and when it applies;
- **Mandatory rules and criteria** (e.g. when to apply, how to classify, who approves);
- **Roles and responsibilities** (security, product, architecture, management);
- **Documentation and traceability requirement**;
- **Review periodicity of the policy itself** (e.g. annual).

---

## ✅ Final recommendations {#-recomendações-finais}

- These policies must be **officially approved** by security management and by the organisation's management;
- They must be **published and accessible** to all teams;
- Their existence is a **precondition for guaranteeing coherence, auditability and real security-by-design maturity**;
- Their application must be aligned with the practices described in this chapter.

> 📌 Templates for these policies may be made available as complementary `60-*.md` files in future versions of the manual.
