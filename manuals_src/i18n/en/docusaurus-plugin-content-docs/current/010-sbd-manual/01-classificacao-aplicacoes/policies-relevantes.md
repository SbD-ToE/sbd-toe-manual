---
id: policies-relevantes
title: Relevant policies
tags: [canon, politicas, risco, classificacao, excecao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/policies-relevantes.md
  source_sha256: 55b234ea202a9995d2f827e3c5e06df944998446b5d88267740439de6e58f6b7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 39c4e1c49590ce826c769b3c34203c2ae433fa483f0115be7e499ed68126691d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: f3ae07385fc10c458f9087ea5ea231fd2bbf0e4852b0e4c0e84ec84618762443
  glossary_keys: [avaliacao, categorize_sw, chapter_role, framework_source_corpus, maturity, practitioner_manual, traceability]
  glossary_sha256: 5ad65c1e9e9d3455e023629d5e9dbc0f5733c5bcc54408a6669e1ab81e4ad272
  translated_at: 2026-09-25T18:00:16Z
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
| [Periodic Risk Review Policy](/sbd-toe/assets/policies/policy-revisao-periodica-risco)             | ✅ Yes       | The whole organisation                     | Minimum frequency (e.g. 6 months); mandatory triggers; required evidence.                                   |
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
