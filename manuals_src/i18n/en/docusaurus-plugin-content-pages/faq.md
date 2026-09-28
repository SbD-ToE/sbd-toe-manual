---
id: faq
title: FAQ - Frequently Asked Questions
description: Quick answers on the applicability, scope, compliance and implementation of SbD-ToE
tags: [faq, aplicabilidade, compliance, implementacao]
sidebar_position: 7
translation:
  source_locale: pt
  source_path: faq.md
  source_sha256: a6a10b506190b19cf9cc3db2cd1039dcf09145f31a9d1725f47128bd5d86df23
  source_commit: e36462f7473256b7e66033011a59ffd3d1223f83
  target_sha256: a56a5d393fd0ce7b6cedf88423b804228c6d11f5fae52ceaea281bae1f15d22a
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, chapter_role, como_fazer, dora_register_of_information, esquema_regime, eu_ce_marking, eu_notified_body, framework_source_corpus, gdpr_security_of_processing, mapping, maturity, normative_empirical, practitioner_manual, requirement_runtime, role_juridico, sbdtoe_sbd, schema, validation_evaluation]
  glossary_sha256: 7d985466cd668bce39b65b513434341f3f92a67fb2d239f7facb0449cecc27c3
  translated_at: 2026-09-28T09:13:00Z
  stamped_at: 2026-09-28T09:13:00Z
  reviewed_by: null
---

# FAQ - Frequently Asked Questions

## Scope and Applicability {#âmbito-e-aplicabilidade}

### Who is SbD-ToE for? {#para-quem-é-o-sbd-toe}

Organisations that:
- **Develop** software (own products, internal tools, apps for clients).
- **Contract out** development (outsourcing, contractors, system integrators).
- **Acquire** critical SaaS/PaaS/IaaS and need to validate the supplier's security.
- **Operate** critical ICT infrastructure (on-prem, cloud, hybrid).
- Are subject to **regulation** (NIS2, DORA, CRA, GDPR) and need technical evidence of compliance.

SbD-ToE is **not** only for software companies. It is for any organisation with **critical ICT systems**.

---

### My organisation does not develop software. Is SbD-ToE relevant? {#a-minha-organização-não-desenvolve-software-o-sbd-toe-é-relevante}

**Yes, very probably.**

Even without in-house development, most organisations:
- **Acquire or contract** software (ERP, CRM, core systems, SaaS).
- **Operate** infrastructure (servers, cloud, network).
- **Manage sensitive data** (customers, employees, financial).

SbD-ToE helps to:
- **Classify** applications by criticality (Ch. 01).
- **Define security requirements** for suppliers (Ch. 02, 14).
- **Validate the security** of acquired software (Ch. 10: pentests, audits).
- **Manage suppliers** in line with DORA/NIS2 (Ch. 05, 14: SBOM, contracts, SLAs).
- **Operate with resilience** (Ch. 12: logs, backups, incidents, monitoring).

**Example:** A bank that uses SAP/Oracle (and does not develop) still needs to:
- Classify the ERP as L3 (critical).
- Require an SBOM and patch SLAs from the supplier.
- Integrate logs into the corporate SIEM.
- Run annual pentests.
- Document everything for the DORA audit.

→ **Applicable chapters:** 01, 02, 05, 10, 12, 14.

---

### What is the difference between SbD-ToE and ISO 27001? {#qual-a-diferença-entre-sbd-toe-e-iso-27001}

| Aspect | SbD-ToE | ISO 27001 |
|--------|---------|-----------|
| **Focus** | **Application** and pipeline security (development, acquisition, operation of software) | **Organisational** information security management (ISMS) |
| **Level** | Detailed technical-operational | High-level, abstract (generic controls) |
| **Structure** | 14 chapters by technical domain (SBOM, CI/CD, IaC, threat modelling, testing) | 93 controls in 4 themes (Annex A of ISO/IEC 27001:2022) |
| **Certifiable?** | No (it is an internal framework) | Yes (certification by an accredited CAB) |
| **Relationship** | **Contributes** to Annex A controls with technical detail (e.g. A.8.8, A.8.25–A.8.29); there is no published cross-check and no control-by-control mapping | **Requires** controls; leaves the "how" open |

**In practical terms:**
- ISO 27001 says: "Technical vulnerabilities must be managed" (control A.8.8 in the 2022 edition).
- SbD-ToE says: "Ch. 05 - How to do SBOM, SCA, patching with SLAs, formal exceptions, CI/CD integration".

**Can they coexist?** Yes, and they should. SbD-ToE provides the "technical how" that can support ISO 27001 implementation and audit.

---

## Compliance and Regulation {#compliance-e-regulação}

### Does SbD-ToE cover DORA/NIS2/CRA/GDPR? {#o-sbd-toe-cobre-doranis2cragdpr}

**Yes, but in a different way:**

| Regulation | SbD-ToE coverage | Intentional gaps | Cross-check |
|-------------|-------------------|---------------------|-------------|
| **DORA** | 80–90% of the technical requirements (Art. 5/18/19–20/26–28) | ITS templates, formal board approval, supplier concentration | [02-dora.md](/sbd-toe/cross-check-normativo/dora/intro) |
| **NIS2** | 80–90% of the technical requirements (Art. 20/21/23) | Registration with the national authority, reporting templates | [NIS2.md](/sbd-toe/cross-check-normativo/nis2/intro) |
| **CRA** | 70–80% (SBOM, patching, disclosure, testing) | CE marking, declaration of conformity, notified bodies | [05-cra.md](/sbd-toe/cross-check-normativo/cra/intro) |
| **GDPR** | 60–70% (Art. 25/32: PbD, security of processing) | ROPA, legal basis, full DPIA, international transfers | [07-gdpr.md](/sbd-toe/cross-check-normativo/gdpr/intro) |

**Principle:** SbD-ToE provides the reusable **technical core**. The legal-administrative parts (contracts, legal bases, formal declarations) are handled by Legal/GRC.

---

### Can I use SbD-ToE as compliance evidence? {#posso-usar-o-sbd-toe-como-evidência-de-compliance}

**As supporting evidence, yes.** Each chapter produces reusable artefacts:

- **L1–L3 classification matrix** → supports DORA Art. 8, NIS2 Art. 21 and GDPR Arts. 25 and 32.
- **SBOM per release** → evidence for the CRA (Annex I, Part II, point 1; technical documentation in Annex VII); supports DORA Art. 28, without replacing the register of information.
- **SAST/DAST/pentest reports** → support DORA Arts. 24 and 25, NIS2 Art. 21 and CRA Annex VII, point 6.
- **Incident runbook** → supports DORA Arts. 17 to 19, NIS2 Art. 23 and GDPR Arts. 33 and 34 (deadlines in Policy 32 §6).
- **Supplier contracts** → support DORA Arts. 28 to 30, NIS2 Art. 21(2)(d) and GDPR Art. 28.

**The same set of evidence can support several regimes and audits;** compliance remains the organisation's judgement. What each regime requires, obligation by obligation, is in the [normative cross-check](/sbd-toe/cross-check-normativo/intro).

---

### What about certification? Is there an SbD-ToE certification? {#e-certificação-há-certificação-sbd-toe}

**No.** SbD-ToE is not a certification scheme. It is an **internal operational framework**.

**But:** SbD-ToE evidence can be reused to **accelerate and simplify** external certifications:
- **ISO 27001** (ISMS) - Annex A technical controls (no control-by-control mapping)
- **EUCC** (adopted European scheme; EUCS and EU5G are not yet adopted) - product/service security evidence
- **SOC 2 Type II** (for cloud/SaaS) - demonstration of Trust Service Criteria

**Important:** Reusing evidence reduces the effort (80–90%), but does not replace the independent audit/assessment required for formal certification.

See: [ENISA/CSA Certification](/sbd-toe/cross-check-normativo/enisa-csa/intro)

---

## Implementation {#implementação}

### How long does it take to implement SbD-ToE? {#quanto-tempo-demora-implementar-o-sbd-toe}

It depends on the initial maturity:

| Scenario | Estimated duration | Priority phases |
|---------|------------------|-------------------|
| **Greenfield** (new organisation/product) | 3–6 months | Ch. 01–02 (classification/requirements) → 06–07 (SDLC/CI-CD) → 12 (ops) |
| **Brownfield with low maturity** | 6–12 months | Ch. 01 (inventory) → 05 (SBOM/SCA) → 10 (testing) → 12 (incidents) → 14 (governance) |
| **Brownfield with medium maturity** (already has CI/CD, logs, etc.) | 4–8 months | Gap analysis → Ch. 03 (TM) → 05 (SBOM) → 10 (advanced testing) → 14 (suppliers) |
| **Compliance-driven** (DORA/NIS2 deadline) | 6–18 months | Use specific playbooks ([DORA](/sbd-toe/cross-check-normativo/dora/playbook), [NIS2](/sbd-toe/cross-check-normativo/nis2/playbook)) |

**Note:** Implementation is **iterative** (not "big bang"). It starts with critical apps (L3) and expands progressively.

---

### Do I need to implement every chapter? {#preciso-implementar-todos-os-capítulos}

**Not necessarily.** It depends on the context:

**Mandatory for all:**
- Ch. 01 (Classification)
- Ch. 02 (Minimum requirements)
- Ch. 12 (Monitoring and operations)
- Ch. 14 (Governance)

**Conditional:**
- **Developing software?** → Ch. 06–07 (SDLC/CI-CD), Ch. 10 (testing).
- **Using containers?** → Ch. 09.
- **Using IaC?** → Ch. 08.
- **L3 (critical) apps?** → Ch. 03 (Threat Modelling), Ch. 04 (Architecture).
- **DORA/CRA?** → Ch. 05 (SBOM mandatory).

**Principle:** Implement what is **relevant and proportional** to the risk.

---

### How much does it cost to implement SbD-ToE? {#quanto-custa-implementar-o-sbd-toe}

There is no licence cost (it is an open framework). The costs are **internal** (team time) and **tools**:

| Item | Estimate |
|------|-----------|
| Team time (analysis, policies, setup) | 200–500 hours (1–3 FTEs × 3–6 months) |
| Tools (SAST/DAST/SCA) | €5k–50k/year (depends on scale; open-source options exist) |
| SIEM/logging | €10k–100k/year (or included with cloud-native) |
| Training (technical team + management) | €5k–20k |
| External audit/validation (optional) | €10k–50k |

**ROI:** Fewer incidents, faster compliance, reuse of evidence, lower audit costs.

---

## Exceptions and Deviations {#exceções-e-desvios}

### What are "exceptions" in SbD-ToE? {#o-que-são-exceções-no-sbd-toe}

**Exception** = a formal deviation from a security requirement, with:
- Technical or business justification.
- Approval by a designated authority (AppSec/CISO/Board, depending on criticality).
- Validity period (TTL).
- Remediation or compensation plan.
- Audited trail.

**Example:** "Deploy of an L3 app with a known High CVE, but with a compensating WAF, approved by the CISO, TTL 30 days, patch scheduled."

See: Ch. 02 addon 08, Ch. 05 addon 09, Ch. 14.

---

### Are all exceptions allowed? {#todas-as-exceções-são-permitidas}

**No.** There are categories of **unacceptable exceptions**:

- Critical RCE vulnerabilities without compensation.
- Absence of MFA in L3 apps.
- Unencrypted sensitive data.
- Regulatory compliance violations (e.g. DORA/NIS2/GDPR).

**Rule:** If the regulator or the criticality does not allow it, it is not an exception - it is **non-compliance**.

See: [DORA cross-check - Exceptions](/sbd-toe/cross-check-normativo/dora/intro#gestão-de-exceções-e-desvios-artigos-5-1723-2427-2830-dora)

---

## Relationship with Other Frameworks {#relação-com-outros-frameworks}

### SbD-ToE vs. OWASP SAMM/BSIMM/SSDF? {#sbd-toe-vs-owasp-sammbsimmssdf}

| Framework | Type | Relationship with SbD-ToE |
|-----------|------|---------------------|
| **OWASP SAMM** | Maturity model (self-assessment) | SbD-ToE **implements** SAMM practices with operational detail |
| **BSIMM** | Descriptive observation (what others do) | SbD-ToE uses BSIMM insights as inspiration; goes further with prescription |
| **NIST SSDF** | Secure development practices (high level) | SbD-ToE maps and **details** each SSDF practice |

**Convergence:** They all speak of threat modelling, SAST/DAST, SBOM, testing. SbD-ToE **operationalises** it with addons, templates, checklists.

---

### Can I use SbD-ToE with DevSecOps? {#posso-usar-sbd-toe-com-devsecops}

**Yes, it is the core of SbD-ToE.**

- Ch. 06–07: Integration of security into pipelines (shift-left).
- Ch. 10: Continuous testing (SAST/DAST/fuzzing).
- Ch. 08–09: IaC and containers (secure infrastructure-as-code).
- Ch. 12: Observability and rapid response.

**Principle:** Automated security, not manual.

---

## Multi-Jurisdictional Regulation {#regulação-multi-jurisdicional}

### I am subject to DORA + NIS2 + GDPR. Is there duplication? {#estou-sujeito-a-dora--nis2--gdpr-há-duplicação}

**Very little.** Most technical controls converge:

- **Vulnerability management** → DORA Art. 5, NIS2 Art. 21, CRA (SBOM/patching).
- **Incidents** → DORA Art. 18 (24h), NIS2 Art. 23 (24h/72h/1M), GDPR Art. 33 (72h).
- **Suppliers** → DORA Art. 26–28, NIS2 Art. 21, GDPR Art. 28.
- **Testing** → DORA Art. 19–20, NIS2 Art. 21.

**Strategy:**
1. Implement SbD-ToE Ch. 01–14 (common technical core).
2. Use specific playbooks for adjustments (reporting fields, templates).
3. A single incident runbook with channel branching (DORA → EBA, NIS2 → CSIRT, GDPR → DPO).

See: [DORA & NIS2 Convergence](/sbd-toe/cross-check-normativo/dora/convergencia-dora)

---

## Metrics and Continuous Improvement {#métricas-e-melhoria-contínua}

### How can I measure whether I am "SbD-ToE compliant"? {#como-medir-se-estou-sbd-toe-compliant}

Key metrics by chapter:

| Chapter | Metric |
|----------|---------|
| **Ch. 01** | % of apps classified (L1–L3) |
| **Ch. 02** | % of apps with minimum requirements implemented |
| **Ch. 05** | % of releases with an SBOM; MTTP (mean time to patch) |
| **Ch. 07** | % of commits with security gates passed |
| **Ch. 10** | SAST/DAST coverage; % of releases blocked by a critical CVE |
| **Ch. 12** | MTTD/MTTR (time to detection/response); % of backups tested |
| **Ch. 14** | % of suppliers with audited contracts; % of exceptions within deadline |

**Single dashboard** with aggregated KPIs: "SbD-ToE Compliance Score".

---

### Is SbD-ToE "one-time" or continuous? {#o-sbd-toe-é-one-time-ou-contínuo}

**Continuous.**

- New apps → classify (Ch. 01).
- New CVEs → patch/exception (Ch. 05).
- Architectural changes → re-TM (Ch. 03).
- New suppliers → onboarding (Ch. 14).
- Quarterly exercises → incidents/DR (Ch. 12).

**Formal review:** Annual (policies, exceptions, gaps).

---

## Next Steps {#próximos-passos}

### Where do I start? {#por-onde-começo}

1. **Read:** [How to use this manual](/sbd-toe/sbd-manual/fundamentos/como-usar)
2. **Inventory:** Ch. 01 - List and classify critical apps.
3. **Gap analysis:** Compare the current state vs. the Ch. 02 requirements.
4. **Quick wins:** Ch. 05 (SBOM), Ch. 12 (centralised logs), Ch. 14 (RACI).
5. **Roadmap:** Choose the relevant playbook ([DORA](/sbd-toe/cross-check-normativo/dora/playbook), [NIS2](/sbd-toe/cross-check-normativo/nis2/playbook), [CRA](/sbd-toe/cross-check-normativo/cra/playbook), [GDPR](/sbd-toe/cross-check-normativo/gdpr/playbook)).

---

### Where can I get support? {#onde-obter-suporte}

- **Complete documentation:** SbD-ToE Chapters 01–14
- **Normative cross-checks:** Section 002
- **Practical playbooks:** See each regulation
- **Community:** (to be defined - forum, GitHub Discussions, etc.)

---

**Version:** 1.0  
**Date:** November 2025  
**Next review:** May 2026
