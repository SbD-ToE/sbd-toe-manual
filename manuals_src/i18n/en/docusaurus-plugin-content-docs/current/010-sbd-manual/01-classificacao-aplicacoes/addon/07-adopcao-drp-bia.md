---
id: adopcao-drp-bia
title: Alternative - adopting DRP, BIA or other Existing Classifications
sidebar_position: 7
tags: [tipo:ligacao, tema:drp, bia, classificacao, risco]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/07-adopcao-drp-bia.md
  source_sha256: 64b514dca43a26450e677339fefa8c02de1f321905ec5fd8b06b54ec181a1c03
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e13b1fe6439524d92828f61b6d953810d09d949e7d688048daebe9ac3632f176
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [avaliacao, mapping, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 8c378d40579c44d0b2e69359b9060696f5ba61aebb76922b975150c14b53e3e5
  translated_at: 2026-09-25T20:18:47Z
  reviewed_by: null
---
<!--template: sbdtoe-addon -->

# Alternative model via Adoption of Existing Classifications (e.g. DRP/BIA)


## 🎯 Objective {#-objetivo}

To guide the reuse of existing classifications - namely **DRP (Disaster Recovery Plan)** and **BIA (Business Impact Analysis)** - as a basis for **application risk classification**, avoiding duplicated effort and promoting consistency in the assessment of criticality.

---

## 📘 Context {#-contexto}

Many organisations already carry out an **impact classification** based on business continuity, within processes such as DRP or BIA, among others. These classifications generally include attributes such as:

- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)
- Financial, reputational or operational impact
- Recovery priority

Although they do not focus directly on security, these data are **strongly correlatable** with application risk and can be used as **initial input or justification** for the risk classification prescribed in SbD-ToE.

---

## 🔁 Practical mapping between DRP/BIA and security risk {#-mapeamento-prático-entre-drpbia-e-risco-de-segurança}

| DRP/BIA classification     | Interpretation in the SbD-ToE context |
|---------------------------|------------------------------------|
| **Critical**               | High Risk                     |
| **Important / Medium**    | Medium Risk                       |
| **Non-essential / Low** | Low Risk                       |

> ⚠️ This mapping must be **confirmed by security analysis**, considering the nature of the data and the exposure of the application.

---

## 📝 Practical example {#-exemplo-prático}

A system classified as **Critical** in the DRP, with the following parameters:

- **RTO:** < 4h  
- **RPO:** < 1h  
- Personal and billing data  
- Integration with third parties  
- Exposed to the internet

→ Must automatically be classified as **High Risk**, requiring:

- Formal threat modelling  
- Complete security requirements  
- Continuous automated testing  
- Active monitoring

---

## 📌 Recommendations {#-recomendações}

- Validate that the DRP/BIA classification is up to date and corresponds to the scope of the current application
- Attach or reference the impact classification in the repository where the risk classification is documented
- If the application is composed of multiple modules, consider classification **per component**, not only globally
- In case of divergence between the DRP classification and the one observed in security, record both rationales and discuss with the teams involved

---

## 🧩 Operational integration {#-integração-operacional}

In practice, these classifications can be reused in three ways:

1. **Direct import of the data** into the risk register (e.g. file, wiki, tool)
2. **Cross-linking** between artefacts (e.g. link to the DRP record in the risk register)
3. **Single template** that includes business impact and security risk fields

> A good practice is to include this validation as one of the criteria in the classification *checklist*.

---
