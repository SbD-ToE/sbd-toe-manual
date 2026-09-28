---
id: intro
title: DORA - Normative cross-check
description: Analysis of how SbD-ToE covers the technical requirements of Regulation (EU) 2022/2554 (DORA)
tags: [cross-check, dora, regulamentacao, ict-risk, resiliencia, finanças]
sidebar_position: 1
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/dora/01-intro.md
  source_sha256: afdf41ee684f6b166fac67f528c81107c7360645850233753090990539538acb
  source_commit: f2e7be9ecdd9179e9770d80bc6363f7da7f1d9aa
  target_sha256: 8287fa5337c8dd7ce8e052a37cd3569affa446ffea71ee2243957fce6b1e382f
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, avaliacao, chapter_role, cycle_iteration, dora_digital_operational_resilience, dora_financial_entity, dora_ict_risk, dora_ict_rmf, dora_ict_tpp, dora_major_ict_incident, dora_register_of_information, eu_management_body, gap_family, lifecycle_phase, mapping, maturity, mcp_reading_programa, normative_empirical, piso_limiar, piso_relacao, practitioner_manual, programme_line, provenance, requirement_runtime, role_tech_lead, sbdtoe_sbd, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: 37a767a0aaf3e6e727307302a88a116b162e46089f41049d18578083946eea4f
  translated_at: 2026-09-28T09:11:47Z
  stamped_at: 2026-09-28T09:11:47Z
  reviewed_by: null
---

# DORA: Normative cross-check

> For practical implementation, see the [SbD-ToE 4 DORA Playbook](/sbd-toe/cross-check-normativo/dora/playbook).
> 
> For internal practical examples, see the `exemplo-playbook/` folder.

## General Framework {#enquadramento-geral}

The **Digital Operational Resilience Act (DORA)** - **Regulation (EU) 2022/2554** (CELEX: [32022R2554](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554)) - marks a historic turning point in the way the European Union approaches **digital resilience** in the financial sector.  
From January 2025, it is no longer enough for financial entities to protect data or follow general good practice: they are required to demonstrate, with evidence and consistent mechanisms, that they **can identify, prevent, detect, respond to and learn from technological risks**.

SbD-ToE was designed as an **application security model**. It covers much of DORA's technical baseline on the application side, declares the gaps where it falls short, and leaves out of scope, with the reason, what belongs to the entity as a whole. This document consolidates:

1. **Normative cross-check:** How SbD-ToE maps to DORA
2. **Practical playbook:** 12–18-month implementation roadmap

## What this Manual covers and what stays out {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

SbD-ToE is centred on the application: requirements, architecture, code, dependencies, pipeline, deploy and operation of the software. For each DORA obligation, the Manual answers in one of three categories, and no obligation is left unanswered:

- **Covers**, and states how: catalogue requirement, policy, floor or requirement added by the regime, or engineering evidence for a duty that sits on another plane.
- **Declared gap**: what the Manual does not cover by default, with what is missing.
- **Out of scope**: what the Manual does not address, with the reason.

The complete list, obligation by obligation, is generated from the coverage matrix and is in [Applicable requirements — What this Manual covers and what stays out](./requisitos-aplicaveis#cobertura). Where this page and the list diverge, the list prevails.

**Out of scope, by programme decision:**
- Security of the entity as a whole (corporate network and administration channels, EDR, patching of operating systems and equipment, inventory and classification of all assets): the Manual is centred on the application.
- The entity's business continuity, crisis management and BIA. The Manual covers backups, tested restoration and recovery of the application (OPS-016, OPS-017).

---

## PART I: NORMATIVE ANALYSIS {#parte-i-análise-normativa}

### 🔍 What DORA requires, in operational terms {#-o-que-dora-exige-em-termos-operacionais}

> ⚖️ **Editorial note.**  
> This section is an **operational synthesis** of the relevant DORA articles, not a literal quotation of the regulation.  
> It draws, in particular, on Articles 5–6 (governance and ICT risk management), 8–15 (protection, prevention, detection, response and recovery), 17–23 (incidents and reporting), 24–27 (resilience testing) and 28–30 (ICT third-party service providers). Information sharing on cyber threats (Art. 45) and the simplified ICT risk management framework (Art. 16) serve as complementary framing, not as main landing blocks.

In practical terms, DORA translates into obligations that directly affect SbD-ToE practices:

- **Management body with explicit responsibility (Art. 5).**  
  - The management body approves the ICT risk management strategy, oversees its implementation and is responsible for ensuring that policies, procedures, documentation and evidence are in place.  
  - In SbD-ToE this connects to overall governance, policies and the requirement for _accountability_ over risk decisions.

- **Structured and documented ICT risk management (Art. 6).**  
  - The regulation requires the identification of critical assets, impact assessment, the definition of controls and continuous monitoring.  
  - SbD-ToE provides the technical building blocks (chapters 01–14) that can be used as a control catalogue to meet this obligation.

- **Incident management, classification and structured reporting (Art. 17–23).**  
  - DORA sets minimum requirements for the classification, recording, escalation and reporting of ICT-related incidents to competent authorities, within defined time limits.  
  - The Manual provides practices for detection, _logging_, technical evidence and _runbooks_ that support these flows.

- **Digital operational resilience testing (Art. 24–27).**  
  - It requires a programme of regular testing, proportionate to risk (including _threat-led penetration testing_ for the most critical entities).  
  - In SbD-ToE, this intersects with application security testing (Ch. 10), TLPT readiness and continuous validation of pipelines. Performance, continuity and scenario-based testing are a declared gap; regulated TLPT stays out of scope.

- **ICT third-party risk management (Art. 28–30).**  
  - It requires a register of information on all contractual arrangements with ICT third-party service providers (distinguishing those that support critical or important functions), risk assessment, specific contractual clauses and ongoing monitoring.  
  - The Manual covers the technical part: SBOM and SCA, due diligence and security clauses, and the lifecycle of suppliers with access. The register of information (Implementing Regulation (EU) 2024/2956), DORA-specific contractual content and the oversight of critical providers stay out of scope. Full due diligence under Delegated Regulation (EU) 2024/1773, the programme of audits of providers and the transition plans are declared gaps.

- **Exception decisions and unremediated vulnerabilities.**  
  - Although the regulation does not use exactly this wording, the combination of requirements on risk management, testing, incidents and third parties implies that:  
    - **exceptions to resilience testing**,  
    - **acceptance of unremediated vulnerabilities**, and  
    - **deviations from approved security policies**  
    must be **formally analysed, contextualised, approved at the appropriate level and documented** (including justification, deadline, _owner_ and compensating measures).  
  - SbD-ToE materialises this in Risk Acceptance _playbooks_, approval flows, structured records and KPIs.

In practice, DORA provides the "regulatory umbrella" and the accountability criteria; SbD-ToE works as the **technical manual** that makes those obligations executable across the development and operations lifecycle.

---

### Governance and ICT Risk Management (DORA Articles 5–6) {#governação-e-gestão-de-risco-tic-artigos-56-dora}

**SbD-ToE coverage:**
- **[Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro):** Application criticality classification (L1–L3)
- **[Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro):** Catalogue of security requirements by level
- **[Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro):** Threat Modelling for risk identification
- **[Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Detection, response and continuous improvement
- **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Governance and policy approval

**Out of scope:** SbD-ToE does not set the hierarchical level of approval above the CISO: the duties of the management body and the internal governance structure (Article 5; Article 6(4)) belong to the entity. The Manual requires formal approval of the governance model and the policies by senior management (GOV-001) and sets the approval authorities for exceptions and risk acceptance (Policies 03 §7 and 05 §6). For DORA, the entity maps these policies to formal approval by the management body, with a documentary record of the decision.

---

### Protection, detection, response and recovery (DORA Articles 8–16) {#proteção-deteção-resposta-e-recuperação-artigos-816-dora}

**SbD-ToE coverage:**
- Backups with tested restoration on separate systems (OPS-016; CTX-DORA-P11)
- Recovery objectives and procedure for the application (OPS-017; also at L1 for critical or important functions, CTX-DORA-P12)
- Redundant capacities and switchover testing (CTX-DORA-R01)
- Key lifecycle and certificate register (ENC-007; CTX-DORA-P15, P16); cryptographic inventory and agility (ENC-003; CTX-DORA-P17)
- Half-yearly review of network filtering rules for critical or important functions (ARC-006; CTX-DORA-P18)
- Strong authentication, privileged accounts and identity management (AUT-001, GOV-016, GOV-017; CTX-DORA-P07, P13, P14)
- Access review, annual, and half-yearly for critical or important functions (ACC-010; CTX-DORA-P05, P06)
- Responsible vulnerability disclosure (GOV-015; CTX-DORA-P10) and weekly automated vulnerability scanning of the assets supporting critical or important functions (Policy 10 §9; CTX-DORA-P08)
- Dynamic testing at any level (TST-005; CTX-DORA-P03); alarm on logging failures (LOG-008; CTX-DORA-P04) and automatic alerts for critical or important functions (OPS-005; CTX-DORA-P09)

**Declared gaps:** the ICT asset management policy beyond applications and components (hardware, network, licences, end of support), capacity management, the entity's network security policy and dedicated network administration plan, data leakage prevention and the protection of data in use.

**Out of scope:** business continuity and crisis management (Articles 11(1) and (7), and 14), physical and workstation security, and the corporate network infrastructure: the Manual is centred on the application.

---

### Incidents, Classification and Reporting (DORA Articles 17–23) {#incidentes-classificação-e-reporte-artigos-1723-dora}

It requires an end-to-end process: detection, recording, classification, formal reporting and integration with harmonised templates/fields.

**SbD-ToE coverage:**
- **[Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Incident detection and response processes
- **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Reporting and escalation responsibilities

**Coverage, declared gap and out of scope:** The P1–P4 scale (Policy 31) defines internal severity, but not DORA incident classification (Delegated Regulation (EU) 2024/1772) nor DORA-specific templates: those come from the DORA context and Policy 32. The incident record collects the impact data (Policy 32 §4.3). In the DORA context, the incident management process is mandatory at any level (CTX-DORA-P01); incidents are classified using the criteria of Article 18(1) and the thresholds of Delegated Regulation (EU) 2024/1772, with a monthly assessment of recurring incidents (CTX-DORA-R02), and significant cyber threats are recorded (CTX-DORA-R03). Deadlines and content follow Policy 32 §6 and §6.1, with the templates of Implementing Regulation (EU) 2025/302. The relationship with the authority (channels, submission, procedures) stays out of scope. Reporting of major ICT-related incidents to the management body (Article 17(3)(e)) is a declared gap.

---

### Resilience Testing (DORA Articles 24–27) {#testes-de-resiliência-artigos-2427-dora}

It requires a continuous testing programme, culminating in Threat-Led Penetration Testing (TLPT) for eligible entities.

**SbD-ToE coverage:**
- **[Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro):** Threat Modelling (realistic attack scenarios)
- **[Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro):** Test catalogue (SAST, DAST, fuzzing, etc.)
- **[Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro):** Pre-production security validation

**Partial coverage - see [Ch. 10 → addon 14: TLPT Readiness](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness):** SbD-ToE frames what TLPT is, what distinguishes it from a conventional PenTest and how the maturity of the testing programme relates to the exercise. What remains outside the Manual's scope are the eligibility criteria (identification by the competent authority), the formal qualification of testers and providers under Delegated Regulation (EU) 2025/1190, and the attestation process by the designated TLPT authority - these aspects fall within the remit of the compliance teams and the relationship with the supervisor.

---

### Management of Critical Suppliers (DORA Articles 28–30) {#gestão-de-fornecedores-críticos-artigos-2830-dora}

Articles 28–30 set requirements for a formal inventory, risk assessment, mandatory contractual clauses, ongoing oversight and tested exit plans.

**SbD-ToE coverage (Two categories of suppliers, one strategy):**

**Category 1: Software Component Suppliers ([Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) - SBOM)**
- **DORA context:** Third-party software components (libraries, frameworks) constitute implicit technology suppliers
- **Technical solution:** the SBOM (Software Bill of Materials) identifies components and their origin (project, author or publisher)
- **Characteristic:** Implicit suppliers - component authors are often unaware that they are part of the supply chain
- **Operational management:** Continuous SCA (vulnerability analysis), security update management, licence tracking
- **Relation to DORA:** the SBOM is complementary evidence. The authors of open-source components are not, as a rule, third-party ICT service providers with which the entity has a contractual arrangement; the register of information in Art. 28(3) covers contractual arrangements (Implementing Regulation (EU) 2024/2956), and the SBOM does not replace it

**Category 2: Contractual Suppliers ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) - Governance)**
- Formally contracted entities: contractors, outsourcing, service providers
- **Characteristic:** Explicit suppliers with formally documented contracts and responsibilities
- Structured lifecycle: preparation → onboarding → monitoring → offboarding
- User Stories US-15 to US-20: contractor/supplier management processes

**Supporting artefacts (Ch. 14):**
- Pre-access contractor validation template
- Sandbox technical preparation guide
- Secure offboarding checklist

**DORA compliance (Art. 28–30):**
- These are four distinct things: the component inventory (SBOM), the provenance of those components, the third-party ICT service providers and the contractual arrangements with them
- The SBOM feeds the technical risk inventory of components; the providers and the contractual arrangements feed the register of information and third-party risk management, which belong to the entity
- **Out of scope:** SbD-ToE does not include ITS templates or DORA concentration analysis formulas. The register of information (Implementing Regulation (EU) 2024/2956), the analysis of concentration risk (Article 29), DORA-specific contractual content and the oversight of critical ICT third-party service providers belong to the entity and its relationship with the supervisor.
- **Declared gaps:** full due diligence under Delegated Regulation (EU) 2024/1773 (provider capacity and continuity, location, fitness), the programme of audits of providers with risk-based frequency, and the transition and full data migration plans (Article 28(4) to (6) and (8)).
- **Manual basis:** up-to-date SBOM ([Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)), formal inventory of contractors and security clauses proportionate to risk ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro); GOV-006, GOV-007).

---

### Information Sharing on Cyber Threats (DORA Article 45, complementary context) {#partilha-de-informação-sobre-ameaças-artigo-45-dora-contexto-complementar}

DORA Article 45 establishes information-sharing arrangements on cyber threat information and intelligence, promoting cooperation among financial entities and with the competent authorities.

**SbD-ToE coverage:**
- **[Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Integration of threat intelligence indicators into monitoring processes
- **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Governance structures and reporting responsibilities

**Out of scope:** SbD-ToE does not prescribe specific institutional arrangements or processes for notifying the supervisor: participation in information-sharing arrangements and their notification to the authority (Article 45) belong to the entity. In the DORA context, significant cyber threats are recorded (CTX-DORA-R03). Integration of threat intelligence feeds (e.g. STIX/TAXII, MISP) and formalisation of sharing channels with competent authorities follow sectoral guidance.

---

### Exception and Deviation Management (DORA Articles 5, 17–23, 24–27, 28–30) {#gestão-de-exceções-e-desvios-artigos-5-1723-2427-2830-dora}

DORA does not explicitly mention "exceptions"; however, in **regulatory compliance**, exceptions constitute **formal deviations from requirements** that require:
- Documented approval by a formally designated authority
- Technical and business justification
- A defined validity period
- A structured remediation plan

**SbD-ToE coverage (Partial):**
- **[Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro):** Management of exceptions in security testing with formal approval (e.g. known vulnerabilities with justification)
- **[Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro):** Tracking of configuration exceptions in IaC
- **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** RACI structure for approvals
- **[Policy 05](/sbd-toe/assets/policies/policy-gestao-excecoes):** formal exception process, approval authorities by level and severity (§6) and validity periods (§7)

**What the Manual defines and what is left to the entity.** The Manual defines the approval authorities by level and severity (Policy 05 §6), the validity periods (Policy 05 §7) and the remediation SLAs (Policy 19 §4.3), and records every non-application of a control with justification, compensation, approver and deadline (GOV-004). Escalation to the management body, the categories the supervisor considers inadmissible and the reporting of exceptions to the regulator are left to the entity.

**DORA compliance:**
- Establish a formal exceptions policy with a governance structure and traceability
- Document each exception: justification, approver, expiry date, correction plan
- Maintain an audited trail of exceptions (open to regulatory inspection)
- Validate admissibility with the supervisor (some exceptions may breach Art. 5)

---

### Formal Exceptions and Compliance Deviations (DORA Articles 5, 17–23, 24–27, 28–30) {#exceções-formais-e-desvios-de-conformidade-artigos-5-1723-2427-2830-dora}

#### The Problem: Informal Exceptions = Inconsistency with DORA {#o-problema-exceções-informais--incoerência-com-dora}

DORA Art. 5 establishes that **digital resilience is the ultimate responsibility of the management body** (board), and **oversight of implementation** means:
- Knowing **all deviations** from security policies
- Formally approving exceptions to controls
- Documenting reasons, validity period and remediation plan
- Maintaining an audited trail to demonstrate to the regulator

**Critical scenario (inconsistency with DORA):**
| Situation | Risk | Impact | DORA Position |
|----------|-------|--------|-------------|
| **SQLi in production (L3) without a documented exception** | Exploitation, data breach, notifiable incident | Unassigned responsibility, lost trail | ❌ **SEVERE** - Unmanaged deviation: with no record, no approval authority and no trail, the entity cannot show the oversight that Art. 5 requires |
| **Critical CVE ignored without justification** | Continuous exposure, compliance gap | ICT risk management failure | ❌ **SEVERE** - May run counter to risk management, validation and continuous remediation duties under DORA |
| **Exception approved verbally (on Teams/informal email)** | Loss of trail, lack of formal authority, ad hoc renegotiation | Impossible to audit decisions | ❌ **CRITICAL** - No governance evidence; the regulator asks: "who approved?" |
| **Expired exception without reassessment** | Accepted risk becomes unaccepted risk (drift), silent technical breach | The application continues with risk above the threshold | ❌ **CRITICAL** - Breach of Art. 5 (lack of continuous oversight) |

---

#### What DORA Explicitly Requires {#o-que-dora-exige-explicitamente}

**Art. 5 (Governance and organisation):**
> «The management body of the financial entity shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework […]» (Article 5(2))

**Operational translation:**
- Risk acceptance decisions (exceptions) require documented approval from a formal authority
- Knowing of an exploited vulnerability without a documented decision leaves the entity without evidence of oversight (the Manual's reading; the regulation does not use this wording)
- Exceptions require periodic reassessment - the absence of reassessment constitutes indefinite tacit approval, amounting to a failure of oversight

**Art. 17–23 (Incidents and reporting):**
> Exceptions with an impact on incident management, classification or reporting must be contextualised and handled with a documentary trail compatible with the applicable regulatory regime.

**Art. 24–27 (Testing):**
> The continuous testing programme must cover realistic scenarios. Exceptions to application testing (e.g. an untestable legacy component) require documented compensation. The TLPT frequency cannot be waived internally: Art. 26(1) sets it at least every three years, and only the competent authority can require the entity to reduce or increase it. An internal decision plans the preparation and the scope, but never postpones the obligation.

**Art. 28–30 (Suppliers):**
> Exceptions to supplier SLAs, critical dependencies or unmitigated CVEs must be escalated in line with the applicable risk and governance model.

---

#### SbD-ToE Coverage (Strong, but with Explicit Gaps) {#cobertura-sbd-toe-forte-mas-com-gaps-explícitos}

**What SbD-ToE ALREADY PRESCRIBES (excellent):**

| Chapter | What it prescribes | Level of detail |
|----------|-----------------|-----------------|
| **[Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | L1–L3 classification (basis for exception criticality) | ✅ Clear E+D+I model; L1/L2/L3 criteria defined |
| **[Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), addon 03** | Risk acceptance criteria (thresholds per level) | ✅ L1≤9, L2≤6, L3≤4; at L2, formal validation and recording; at L3, exception only with the risk manager's approval |
| **[Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), addon 08** | Management of exceptions to requirements (formal process) | ✅ Identification, justification, assessment, compensation, periodic review |
| **[Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), addon 03** | Exceptions to architectural requirements | ✅ Register model with a time horizon; designated owners |
| **[Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), addon 09** | Exceptions to CVEs (formalisation, owner, TTL, impact) | ✅ Complete process: identification → justification → acceptance → TTL → revalidation |
| **[Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Exceptions to security testing (with formal approval) | ✅ Explicit mention: "formally approved exceptions" |
| **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Exception governance (RACI, approval flow, audit) | ⚠️ **PARTIAL** - User Stories define roles, but do not explain the DORA implications |
| **[Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Waivers and temporary exceptions (during training) | ✅ "Formal documented justification, approved by AppSec/GRC/management" |
| **[Policy 05](/sbd-toe/assets/policies/policy-gestao-excecoes)** | Approval authorities by level and severity (§6) and validity periods (§7) | ✅ Top of the approval authority at the CISO; Critical not acceptable as an exception at L3 |

---

#### Identified Gaps (Inconsistencies with DORA) {#gaps-identificados-incoerências-com-dora}

**Point 1: The Manual's approval authorities and escalation to the management body**

| Level | SbD-ToE Prescribes | DORA Requires | Status |
|-------|------------------|-----------|-----|
| **L1** | Tech Lead or AppSec Engineer, by severity (Policy 05 §6) | Exceptions to the application of policies recorded, with resilience ensured (Delegated Regulation (EU) 2024/1774, Article 2(2)(c)) | ✅ Formal approval authority defined |
| **L2** | AppSec Engineer; High with Product Management; Critical with the CISO (Policy 05 §6) | Same | ✅ Formal approval authority defined |
| **L3** | AppSec Engineer with GRC (Medium); CISO (High); Critical not acceptable (Policy 05 §6) | Acceptance of residual risk above the tolerance approved by the management body, by a formally designated function/owner, with a justified inventory and annual review (RTS 2024/1774, Art. 3, points (a) and (d); DORA Articles 5(2) and 6(4)) | ✅ The roles for accepting, recording and expiring accepted residual risks are prescribed (Policy 03 §7–§8; CLA-007; GOV-004). Escalation to the management body belongs to the entity (DORA Article 5; out of scope of the Manual). |

**How it shows:** if the entity decides that L3 exceptions go up to the management body, that escalation and its record belong to the entity: in the Manual, the approval authority stops at the CISO.

---

**Gap 2: No Description of Unacceptability under DORA**

| Exception | SbD-ToE | DORA |
|---------|---------|------|
| "Not implementing MFA because it is complex" | In the DORA context, this is not an admissible exception: strong authentication is a floor at any level (AUT-001, CTX-DORA-P07, which only admits a justification of non-applicability; remote and privileged access: GOV-016, CTX-DORA-P13, with no justification admitted) | ❌ **May run counter to minimum strong authentication and ICT risk management measures under DORA** |
| "SQLi in a legacy endpoint, stays as is" | Follows Policy 05 like any vulnerability: by severity and level, with the approval authorities and deadlines of Policy 05 §6 and §7 and with compensation (e.g. WAF). An exploitable SQLi of Critical severity is not acceptable in L3; in L2, only with CISO approval, a remediation plan and a 7-day TTL | ⚠️ DORA does not list inadmissible vulnerabilities or exceptions; the decision is Policy 05's, and nothing is attributed to the regulation |
| "Critical CVE in runtime, with no fix plan" | Not acceptable at any level without an active remediation plan (Policy 03 §5); TTL of 7 days at L1 and L2 and not acceptable at L3 (Policy 05 §7) | ❌ **May run counter to remediation, validation and continuous oversight duties under DORA** |

**How it manifests:** The organisation formally records the exception in SbD-ToE; the regulator rejects it: "this exception is not admissible under DORA" → lost time, forced review.

---

**Gap 3: No TTL Tracking vs. Continuous Oversight**

| Process | SbD-ToE | DORA Requirement | Gap |
|----------|---------|----------------|-----|
| **Exception creation** | Documents with owner, TTL, criteria | ✅ Good | ✅ Aligned |
| **Periodic reassessment** | Revalidation on the expiry date, with an alert 15 days before (Policy 05 §7, the Manual's choice); re-approval mandatory | ✅ Good | ✅ Aligned |
| **Centralised tracking** | GRC tool; audit trail per application | ✅ Good | ⚠️ The Manual does not describe the reporting format for DORA |
| **Escalation to the regulator** | Incident notification is in Policy 32 §6 (DORA Article 19); linking relevant exceptions to the incident report is not prescribed | ⚠️ DORA requires the reporting of major ICT-related incidents (Art. 19); related exceptions must be recorded in the supporting documentation | ⚠️ Partial gap - no guidance for attaching exceptions to the incident documentation |

**How it manifests:** A security incident; the regulator asks: "show me the relevant exceptions" → the organisation has no consolidated view or does not know whether it must report.

---

**Gap 4: No Formal Organisational Policy on Unacceptability**

SbD-ToE describes **how** to manage exceptions and sets some limits (Critical is not acceptable at L3, Policy 05 §6; the DORA context floor admits no exception for convenience), but does not establish **all the unacceptable categories under a DORA reading**:

- **Never acceptable in a defensible DORA reading:**
  - Exceptions without documented approval
  - Expired exceptions without reassessment
  - Exceptions to obligations that follow directly from the regulation (e.g. the TLPT frequency, Art. 26(1)), which an internal decision cannot set aside

- **Acceptable with restrictions (compatible with DORA):**
  - Exceptions with TTL, a fix plan and compensation
  - Exceptions approved by the approval authority of Policy 05 §6 (and, if the entity so decides, ratified by the management body)
  - Exceptions with an audited trail

**How it manifests:** An organisation without a formal policy accepts an inadmissible exception; a regulatory audit identifies a critical finding.

---

#### How to Resolve the Inconsistency {#como-resolver-a-incoerência}

**1. Establish a Formal Exceptions Policy Compatible with DORA**

```
POLÍTICA: Gestão de Exceções e Desvios de Conformidade

Objetivo: Garantir que todas as exceções a requisitos de segurança são aprovadas por autoridade formal, documentadas com trilho auditado, e compatíveis com exigências regulatórias (DORA).

Categorias de exceção:

A. Exceções INACEITÁVEIS (incompatíveis com uma leitura DORA defensável):
   - Exceções sem aprovação documentada
   - Exceções expiradas sem reavaliação
   - Vulnerabilidades fora das alçadas e dos prazos da Política 05 (ex: Critical em L3; Critical em L2 sem CISO, plano e TTL)
   - Exceções a obrigações que decorrem diretamente do regulamento (ex: a periodicidade do TLPT)
   ➜ Ação: REJEITAR; forçar mitigação

B. Exceções ACEITÁVEIS em L3 (alçada da Política 05 §6):
   - Componentes legados sem patch aplicável
   - CVEs com "no fix available" + compensação (ex: isolamento de rede)
   - Arquitetura herdada em transição
   ➜ Ação: APROVAR pela alçada da Política 05 §6 e, se a entidade o exigir, com ratificação do órgão de administração; TTL da Política 05 §7 (L3: 30 dias; High 14 dias; Critical não aceitável); reavaliação obrigatória

C. Exceções ACEITÁVEIS em L2 (alçada da Política 05 §6):
   - Requisitos técnicos com compensação equivalente
   ➜ Ação: APROVAR pela alçada da Política 05 §6 (AppSec Engineer; High com Gestão de Produto; Critical com CISO); TTL da Política 05 §7 (L2: 60 dias; High 30 dias; Critical 7 dias); reavaliação obrigatória

D. Exceções ACEITÁVEIS com aprovação AppSec-level (L1):
   - MVP com funcionalidade reduzida de segurança
   - Prototipagem com dados não-sensíveis
   ➜ Ação: APROVAR pela alçada da Política 05 §6 (Tech Lead ou AppSec Engineer); TTL da Política 05 §7 (L1: 90 dias; Critical 7 dias); reavaliação obrigatória

Rastreamento:
- Ferramenta GRC centralizada (SAP GRC, AuditBoard, ou custom)
- Campos: ID | Aplicação | Nível | Exceção | Justificação | Aprovador | Data | TTL | Status | Observações regulatórias
- Reporte periódico ao CISO e, se a entidade o decidir, ao órgão de administração (periodicidade definida pela entidade)
- Reporte ad-hoc a regulador se incidente relacionado
```

---

**2. What stays outside the Manual.** The categories of inadmissibility and escalation to the management body are decisions of the entity, and the Manual does not prescribe them (DORA Article 5; out of scope). Reporting to the regulator follows Policy 32 §6; the forms and channels belong to the authority.

---

#### Summary: Why the Absence of Formal Management = DORA Inconsistency {#resumo-por-que-ausência-de-gestão-formal--incoerência-dora}

| Aspect | Without Formal Management | With SbD-ToE Management + DORA Mapping |
|--------|-------------------|----------------------------------|
| **Regulatory discovery** | No documentation of exceptions, or unknown location ❌ | Formal process (Policy 05) in a GRC system, with the approval authorities defined ✅ |
| **Audited trail** | Exceptions in informal channels (Slack/Teams/email) ❌ | Exceptions in a GRC tool with a complete audit trail ✅ |
| **Board oversight** | The board is unaware of critical exceptions ❌ | The management body receives the reporting of L3 exceptions, through the route and at the frequency the entity defines ✅ |
| **Incident response** | Unawareness of an exploited vulnerability ❌ | Vulnerability recorded in an approved exception with a correction plan; escalated according to protocol ✅ |
| **Audit findings** | Critical finding: governance failure ❌ | Minor finding: operational improvement opportunities ✅ |

---

### Practical Compliance {#conformidade-prática}

**Alignment of SbD-ToE with DORA:**
1. Apply the formal exception process of SbD-ToE (Policy 05; [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) addon 09)
2. Keep the approval authorities of Policy 05 §6 and, where the entity so decides, add escalation to the management body for L3 exceptions (the entity's decision, out of scope of the Manual)
3. Define categories of unacceptability (organisational policy)
4. Implement centralised tracking with an audit trail (GRC tool)
5. Establish periodic reporting to the management body (DORA Article 5(2)(i) requires reporting channels; quarterly frequency is an organisational option)
6. Follow Policy 32 §6 and §6.1 for incident notification; the channels and forms belong to the authority

---

## CROSS-CHECK CONCLUSION {#conclusão-do-cross-check}

SbD-ToE covers the technical core of DORA on the application side. The answer has three parts: what the Manual covers, in the form stated for each requirement; the gaps it declares; and what it leaves out of scope, with the reason, because it belongs to the entity as a whole (business continuity and crisis management, physical security, workstations, corporate network) or to the relationship with the supervisor (register of information, regulated TLPT, reporting templates and channels).

**Requirements for full compliance:**
- Mapping of SbD-ToE policies to formal management body approvals
- Linking the content of Policy 32 §6.1 to the channels and forms of the competent authority
- Closing the declared gaps that matter to the entity (see [Applicable requirements](./requisitos-aplicaveis#cobertura))
- Extension of inventories with specific regulatory data
- Calculation of DORA supplier concentration metrics
- Formalisation of threat information-sharing arrangements

---

## References {#referências}

- SbD-ToE Manual (Chapters 01–14)
- Regulation (EU) 2022/2554 (DORA)
- NIST SP 800-53, OWASP SAMM, BSIMM, SSDF
- [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) SbD-ToE: User Stories US-15 to US-20 (suppliers/contractors)

---

**Version:** 1.1  
**Date:** September 2026  
**Next review:** March 2027
