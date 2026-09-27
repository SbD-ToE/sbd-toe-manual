---
id: mapeamento-ameacas-risco
title: Threat Mapping for Risk Validation
sidebar_position: 6
tags: [tipo:mapeamento, ameacas, risco, validacao, controlo]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/06-mapeamento-ameacas-risco.md
  source_sha256: 8601028d6e9bb4d95ce836e7dea4cdea4559715382e36496ea3c2c174fa712ef
  source_commit: 2323948c2926b1a6da69a7dc962e4d0d66bc6a88
  target_sha256: ddfc5395976c2cdc8924e3294ddd341d0132d6767187d1cd399df5a04365e7a4
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, lifecycle_phase, mapping, papel_suporte, risk_level, sbdtoe_sbd, threat, traceability, validation_evaluation]
  glossary_sha256: e386a71541afa431331f530649604daccec5ab63b2a2d9fb4183b788d6eb822f
  translated_at: 2026-09-27T21:29:57Z
  stamped_at: 2026-09-27T21:29:57Z
  reviewed_by: null
---

<!--template: sbdtoe-core -->

# Threat Mapping for Risk Validation

Mapping known threats is an **essential mechanism for validating the risk analysis**, ensuring that the identified risks reflect **real, plausible and documented attack vectors**.

In *Security by Design – Theory of Everything (SbD-ToE)*, threats **do not determine the application's risk level**, but are used to:

- validate the risk classification carried out (E/D/I);
- identify gaps in the analysis or in the applied controls;
- justify control reinforcement or rejection of risk acceptance;
- ground decisions in recognised catalogues.

---

## 🧠 Framing within the SbD-ToE model {#-enquadramento-no-modelo-sbd-toe}

The role of threat mapping in SbD-ToE is **complementary and validatory**:

1. The application is classified according to the **E/D/I** model.
2. Relevant risks and their attributes are identified.
3. Known threats are mapped to those risks.
4. Controls are defined or adjusted.
5. Residual risk is assessed and, where applicable, accepted.

> 📌 The absence of mappable threats for an identified risk  
> is a **warning sign** that requires the analysis to be reviewed.

---

## 🛡️ Why map threats {#️-porque-mapear-ameaças}

Systematic threat mapping makes it possible to:

- confirm that the analysed risks **correspond to real scenarios**;
- reduce subjectivity in risk assessment;
- increase traceability between risk, threat and control;
- support audits, architecture reviews and exception decisions.

---

## 🧩 Relevant threat catalogues {#-catálogos-de-ameaças-relevantes}

The following models are recognised in SbD-ToE as valid sources of threats:

| Model        | Role in SbD-ToE                                              | When to use                                   |
|---------------|---------------------------------------------------------------|-----------------------------------------------|
| **STRIDE**    | Application-level threat modelling                    | Design, architecture, initial threat modelling  |
| **MITRE ATT&CK** | Validation of real attack vectors and operational exposure | Exposed applications, cloud, APIs, enterprise  |
| **CAPEC**     | Vulnerability exploitation patterns                     | Justification of specific technical controls|
| **OSC&R**     | Offensive techniques against software                            | Local runtime, agents, clients, SDKs        |
| **D3FEND**    | Defensive techniques associated with threats                      | Planning and justification of controls       |

> These catalogues **are not mutually exclusive** and should be used according to the technical context.

---

## 🧩 Example: STRIDE as risk validation {#-exemplo-stride-como-validação-de-risco}

| STRIDE Category       | Typical threat                    | Validated risk                       | Associated controls                |
|------------------------|----------------------------------|--------------------------------------|------------------------------------|
| Spoofing               | Identity forgery       | Improper access to critical functions   | MFA, session management              |
| Tampering              | Data manipulation             | Loss of integrity                 | Signing, input validation     |
| Information Disclosure | Data exfiltration             | Breach of confidentiality        | Encryption, RBAC                  |
| Denial of Service      | Resource saturation            | Unavailability                    | Rate limiting, perimeter protection |

This mapping confirms that the identified risks **correspond directly to known attack vectors**.

---

## 🧩 Using ATT&CK to validate exposure {#-uso-de-attck-para-validação-de-exposição}

| ATT&CK Technique            | Attack vector                | Associated risk                 | Typical controls                 |
|---------------------------|-------------------------------|----------------------------------|----------------------------------|
| Initial Access: Phishing  | Credential compromise     | Unauthorised access            | Phishing-resistant MFA (`AUT-001`, L3), awareness |
| Execution: Scripting      | Remote execution                | Arbitrary execution              | Hardening, validation             |
| Discovery: Cloud Services | Resource enumeration         | Excessive exposure              | Restrictive IAM, logging          |
| Impact: Data Destruction  | Data sabotage             | Loss of integrity             | Backups, change control  |

ATT&CK is particularly useful for validating whether **the exposure assumed in the E/D/I model is realistic**.

---

## 🔐 Link with controls and residual risk {#-ligação-com-controlos-e-risco-residual}

Each mapped threat must result in:

- one or more **associated risks**;
- definition of **mitigating controls**;
- assessment of the **residual risk** after control.

When a relevant threat **has no effective control**, the residual risk:
- increases,
- or becomes **not acceptable**, especially in L3 applications.

---

## ⚠️ Normative rules {#️-regras-normativas}

- Every identified risk **must be validatable** by at least one known threat.
- Risk acceptance **is not valid** if plausible threats remain without effective control.
- In L3 applications, threats mapped in recognised catalogues **require explicit mitigation or formal justification of an exception**.

---

## 🔄 Integration into the lifecycle {#-integração-no-ciclo-de-vida}

Threat mapping must be reviewed:

- whenever there are changes in architecture, data or exposure;
- when new automation or delegation mechanisms are introduced;
- after relevant incidents or findings;
- before formal decisions on residual risk acceptance.

---

## 📌 Final note {#-nota-final}

Threat mapping is not there to “list attacks”,  
it is there to **anchor the risk analysis in technical reality**.

In SbD-ToE, threats are **validation instruments**,  
not mechanisms for automatic risk classification.
