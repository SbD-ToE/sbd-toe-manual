---
id: tlpt-readiness
title: TLPT - Readiness and Regulatory Framework (DORA)
description: Technical and governance preconditions for Threat-Led Penetration Testing (TLPT) in a DORA context, and how SbD-ToE supports the preparation and baseline documentation for regulatory attestation.
tags: [tlpt, dora, pentest, threat-intelligence, resiliência, regulatório, attestation, tiber-eu]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/14-tlpt-readiness.md
  source_sha256: c251b82baa8779450b51041d79ec37bc97eb8e367f0115ba189304906c44c0e5
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c347d24179f8719ff9a9124d9637184bac6bf6ff1ae6c75548ed5710d59cc08b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, chapter_role, cycle_iteration, dora_financial_entity, framework_source_corpus, gap_family, layer, lifecycle_phase, mapping, maturity, mcp_reading_programa, normative_empirical, papel_suporte, practitioner_manual, programme_line, requirement_runtime, sbdtoe_sbd, threat, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 8cad1e1713526ba736fd6262a3c297ec235d99a2b203d1671bff4746c75b8195
  translated_at: 2026-09-26T10:31:33Z
  stamped_at: 2026-09-26T18:35:13Z
  reviewed_by: null
---

# TLPT - Readiness and Regulatory Framework (DORA)

**Threat-Led Penetration Testing (TLPT)** is the most demanding level of offensive validation provided for in the European regulatory framework. Unlike conventional PenTest - described in [addon 11](./pen-testing) -, TLPT is not an optional maturity practice: it is a **regulatory obligation** for entities identified by the competent authority, with specific requirements on scope, methodology, qualification of the executors and formal attestation by the designated TLPT authority.

This addon defines what TLPT is, what SbD-ToE already covers as a preparation baseline, and what is **explicitly outside the scope of the Manual** - being the responsibility of the legal, compliance and supervisor-relations teams.

> **Convention used in this document:**
> - 📜 **Regulatory** - requirement or provision directly provided for in DORA or in the RTS
> - 🛠️ **SbD-ToE good practice** - technical-maturity recommendation that supports the TLPT process, without being an explicit legal obligation

---

## 1) Normative framework {#1-enquadramento-normativo}

### The DORA Regulation {#regulamento-dora}

TLPT is regulated by **Regulation (EU) 2022/2554** (DORA), in force since 17 January 2025:

| Article | Content |
|--------|----------|
| **Art. 26** | TLPT requirements - scope, production environment, frequency, pooled testing, attestation |
| **Art. 27** | Requirements for TLPT executors (testers) - independence, competences, qualification |

The regulatory technical standards (RTS) that detail the TLPT methodology were published as Commission **Delegated Regulation (EU) 2025/1190**, in force since **8 July 2025**.

### Methodological basis: TIBER-EU {#base-metodológica-tiber-eu}

The TLPT provided for in DORA is compatible with the **TIBER-EU framework** (Threat Intelligence-Based Ethical Red Teaming), published by the European Central Bank (ECB, 2018). Several national central banks have published national variants (e.g. TIBER-PT, TIBER-NL, TIBER-DE).

> TIBER-EU is not replaced by DORA - it is the baseline methodological reference that the RTS formalise. Entities that have already conducted TIBER exercises may use those results as input to the DORA process, **provided that the exercises are recognised as aligned with Delegated Reg. (EU) 2025/1190 and accepted by the designated TLPT authority**. This equivalence is not automatic.

### Who is subject to TLPT {#quem-está-sujeito-a-tlpt}

📜 TLPT **does not apply to all financial entities** covered by DORA. Subjection is determined by the competent authorities on the basis of risk and systemic-impact criteria, under Art. 26 DORA and the RTS:

- Identification is made by the competent authority, not by the entity;
- The criteria include size, risk profile, systemic impact and interconnectedness;
- The obligation has a minimum periodicity of **once every 3 years** (Art. 26 DORA);
- The authorities may adjust the frequency on the basis of the entity's risk profile.

> ⚠️ **Explicit gap of SbD-ToE:** The criteria for identifying entities subject to TLPT and the notification process by the competent authority are outside the scope of this Manual. Consult the national supervisor and Delegated Reg. (EU) 2025/1190.

---

## 2) What distinguishes TLPT from conventional PenTest {#2-o-que-distingue-tlpt-de-pentest-convencional}

| Dimension | PenTest (addon 11) | TLPT |
|----------|-------------------|------|
| **Origin of the scenarios** | Technical scope defined internally | 📜 Scenarios derived from real threat intelligence on the sector and the entity |
| **Execution environment** | Preferably staging | 📜 **Real production** - mandatory (Art. 26(2) DORA) |
| **Executors** | Internal or external, with no formal requirement | 📜 Testers qualified under Art. 27 DORA and the RTS; internal possible with specific safeguards |
| **Confidentiality** | Normally documented process | 📜 **Restricted need-to-know** - a very limited number of people know that the exercise is under way |
| **Third-party suppliers** | Out of scope | 📜 May be included via **pooled testing** with consent (Art. 26 DORA) |
| **Outcome** | Internal report + remediation | 📜 Report + **formal attestation by the designated TLPT authority** (Art. 26(7) DORA) |
| **Frequency** | Recommended (L3: annual) | 📜 Mandatory - at least every 3 years |
| **Regulatory basis** | Good practice / internal requirement | 📜 Legal obligation (DORA) |

---

## 3) Readiness preconditions {#3-pré-condições-de-readiness}

SbD-ToE does not establish TLPT itself, but the technical and documentary maturity it produces **is relevant to the quality and sustainment of the exercise**. This section explicitly distinguishes what is a regulatory obligation from what is good preparation practice.

### 3.1 Threat Model → Ch. 03 {#31-threat-model--cap-03}

🛠️ TLPT is "threat-led" because the scenarios are derived from real threat intelligence. For those scenarios to be applied to the entity effectively, it is useful to have:

- An approved baseline threat model (see US-09, Ch. 03);
- Identification of the critical functions and high-value assets (*crown jewels*);
- An up-to-date attack surface mapping.

> There is no provision in the RTS that formally requires an internal threat model as a precondition. However, its absence tends to produce generic TLPT scenarios with lower coverage of the entity's real risks.

### 3.2 Application security testing programme → Ch. 10 {#32-programa-de-testes-de-segurança-aplicacional--cap-10}

🛠️ The existence of a testing programme - SAST, DAST, IAST, fuzzing, PenTest - is not a regulatory precondition for carrying out TLPT. An entity is identified for TLPT by its systemic relevance and ICT risk profile, regardless of the state of its testing programme.

What TLPT does, among other things, is **make that state visible**: it exposes coverage gaps, measures the real effectiveness of the controls in production and underpins the remediation plan. In that sense, the exercise also has a diagnostic function.

Understanding what each testing technique covers - and what it does not cover - helps to interpret TLPT results more precisely and to structure remediation in a more targeted way. Addons 01–08 and 11 of this chapter provide that technical framing.

> The absence of SAST, DAST, PenTest etc. does not legally prevent TLPT from being carried out - it will, however, be reflected in the results of the exercise and in the remediation plan required for attestation.

### 3.3 Monitoring and incident response → Ch. 12 {#33-monitorização-e-resposta-a-incidentes--cap-12}

🛠️ TLPT is executed in real production. The presence of operational monitoring makes it possible to distinguish exercise activity from a real threat, and is a safety condition for controlled execution:

- SIEM/log aggregation in production;
- Documented and tested IR playbooks;
- Critical alerts with a defined response SLA.

> The existence of monitoring in production is not a formal requirement in the RTS for carrying out TLPT, but it is an operational safeguard that the security teams and the qualified testers will consider in the planning phase.

### 3.4 Contractual framework with third parties → Ch. 14 {#34-framework-contratual-com-terceiros--cap-14}

📜 TLPT involves qualified external testers and, potentially, ICT suppliers via pooled testing. The RTS establish independence and qualification requirements for the executors (Art. 27 DORA).

🛠️ The contractual governance framework of Ch. 14 can support the preparation of:

- NDAs and access agreements for testers;
- Security clauses in contracts with relevant ICT third-party providers;
- A process for managing temporary privileged access.

---

## 4) What TLPT requires beyond SbD-ToE {#4-o-que-o-tlpt-exige-além-do-sbd-toe}

The following elements are **obligations of the TLPT process** (📜 regulatory) that are outside the coverage scope of SbD-ToE and must be managed by the compliance, GRC and supervisor-relations teams:

| Element | Description | Responsible |
|----------|-----------|-------------|
| **Identification of subjection** | 📜 Notification by the competent authority that the entity is subject to TLPT | Compliance / Executive Management |
| **Threat intelligence provider** | 📜 Provider qualified and validated under the criteria of Delegated Reg. (EU) 2025/1190 | GRC / CISO |
| **Qualification of the testers** | 📜 Verification of compliance with Art. 27 DORA and the RTS (experience, references, certifications, assessment by the entity and the authority) | GRC / Legal |
| **Notification to the authority** | 📜 Formal communication before the start of the exercise | Compliance |
| **Pooled testing process** | 📜 Coordination with in-scope ICT suppliers, with consent (Art. 26 DORA) | GRC / Legal |
| **Remediation plan with SLAs** | 📜 Post-exercise documentation required for attestation | CISO / Executive Management |
| **Attestation** | 📜 Formal validation of the exercise and its outcome by the **designated TLPT authority** (Art. 26(7) DORA) | TLPT authority + Executive Management |

> The reports and evidence produced within the scope of SbD-ToE (threat model, test findings, release gates, remediation evidence) **can support the baseline documentation** of the attestation process. The traceability that the Manual establishes is adequate to contextualise the entity's security posture before the supervisor - it does not replace the regulatory artefacts specific to the TLPT process.

---

## 5) Explicit integration with this chapter {#5-integração-explícita-com-este-capítulo}

This addon articulates with the rest of Ch. 10 as follows:

| Addon / section | Contribution to TLPT readiness |
|----------------|----------------------------------|
| **00 - Testing strategy** | 🛠️ Defines the base programme; TLPT is the top layer |
| **01–04 (SAST/DAST/IAST/Fuzzing)** | 🛠️ Technical maturity that eases the interpretation of TLPT results |
| **08 - Findings management** | 🛠️ Auditable record that can support documentation for attestation |
| **11 - PenTest** | 🛠️ Base methodology and governance reusable in the preparation of the exercise |
| **10 - Evidence and reproducibility** | 🛠️ Principle cross-cutting to the TLPT exercise |

---

## 6) Readiness checklist (binary) {#6-checklist-de-readiness-binário}

| Item | Regulatory / Good practice | Yes/No |
|------|:-------------------------:|:-------:|
| Subjection to TLPT confirmed by the competent authority | 📜 | |
| Qualified threat intelligence provider identified and validated under the RTS | 📜 | |
| External testers verified against the qualification requirements (Art. 27 DORA + RTS) | 📜 | |
| Notification process to the TLPT authority prepared | 📜 | |
| Pooled testing process assessed (relevant ICT providers identified) | 📜 | |
| Post-exercise remediation plan with SLAs defined | 📜 | |
| Need-to-know process defined (who knows, when and how) | 📜 | |
| Approved baseline threat model with critical functions identified (Ch. 03) | 🛠️ | |
| Crown jewels / high-value assets documented | 🛠️ | |
| Application security testing programme assessed - maturity level documented (Ch. 10) | 🛠️ | |
| Monitoring and IR in production with tested playbooks (Ch. 12) | 🛠️ | |
| SbD-ToE evidence organised as documentary support for the attestation process | 🛠️ | |

---

## ✅ Conclusion {#-conclusão}

TLPT is the most demanding expression of the principle *"test the way the adversary attacks"*. The regulatory dimension - identification by the authority, qualification of testers and providers, attestation - is strictly the remit of the supervisor and of the compliance teams, and is outside the scope of SbD-ToE.

The role of SbD-ToE is different but complementary: **to build and document the technical base** that gives a TLPT exercise substance - more realistic scenarios, more targeted coverage, better-founded remediation.

> 📌 The reports and evidence produced throughout the SbD-ToE cycle (approved threat model, tracked findings, release gates, remediation plans) are adequate to support the context documentation in the DORA attestation process. Maintaining traceability from the start is not overhead - it is what makes TLPT auditable and remediation credible.
