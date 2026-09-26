---
id: intro
title: DORA - Normative cross-check
description: Analysis of how SbD-ToE covers the technical requirements of Regulation (EU) 2022/2554 (DORA)
tags: [cross-check, dora, regulamentacao, ict-risk, resiliencia, finanças]
sidebar_position: 1
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/dora/01-intro.md
  source_sha256: 41e68e472bc45a9141257ebfe964fd81ec13dd060470921fd3e40a895f0105fa
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 1e8476c2b31d67f3a75e730279cca589b85f06ac9145869b16a65628c6025e6b
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, dora_digital_operational_resilience, dora_financial_entity, dora_ict_risk, eu_management_body, gap_family, lifecycle_phase, mapping, maturity, mcp_reading_programa, normative_empirical, practitioner_manual, programme_line, requirement_runtime, sbdtoe_sbd, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: 72798e51c5d3462fe72ce1b41c5794884546ef3f9e517dec5585541425ed8204
  translated_at: 2026-09-26T18:01:06Z
  reviewed_by: null
---

# DORA: Normative cross-check

> For practical implementation, see the [SbD-ToE 4 DORA Playbook](/sbd-toe/cross-check-normativo/dora/playbook).
> 
> For internal practical examples, see the `exemplo-playbook/` folder.

## General Framework {#enquadramento-geral}

The **Digital Operational Resilience Act (DORA)** - **Regulation (EU) 2022/2554** (CELEX: [32022R2554](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022R2554)) - marks a historic turning point in the way the European Union approaches **digital resilience** in the financial sector.  
From January 2025, it is no longer enough for financial entities to protect data or follow general good practice: they are required to demonstrate, with evidence and consistent mechanisms, that they **can identify, prevent, detect, respond to and learn from technological risks**.

SbD-ToE was conceived as a **universal application security model** and naturally covers the technical pillars of DORA. This document consolidates:

1. **Normative cross-check:** How SbD-ToE maps to DORA
2. **Practical playbook:** 12–18-month implementation roadmap

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
  - In SbD-ToE this intersects directly with the chapters on security testing, _red teaming_, _chaos engineering_ and continuous pipeline validation.

- **ICT third-party risk management (Art. 28–30).**  
  - It requires an inventory of critical ICT third-party service providers, risk assessment, specific contractual clauses and ongoing oversight.  
  - The Manual covers these aspects in the chapters on dependencies, SBOM/SCA, supply chain, _outsourcing_ and governance/contracting.

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

**Intentional gap:** SbD-ToE does not fix the hierarchical level of approval (it preserves organisational flexibility). DORA compliance requires mapping SbD-ToE policies to formal approval by the management body, with a documentary record of the decision.

---

### Incidents, Classification and Reporting (DORA Articles 17–23) {#incidentes-classificação-e-reporte-artigos-1723-dora}

It requires an end-to-end process: detection, recording, classification, formal reporting and integration with harmonised templates/fields.

**SbD-ToE coverage:**
- **[Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Incident detection and response processes
- **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Reporting and escalation responsibilities

**Intentional gap:** SbD-ToE does not define a priority taxonomy (P0–P3) or DORA-specific templates, preserving universality. Compliance requires configuring incident fields according to the DORA RTS/ITS and integrating with automated reporting systems (e.g. SIEM).

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
- **Technical solution:** SBOM (Software Bill of Materials) identifies dependencies and their respective suppliers
- **Characteristic:** Implicit suppliers - component authors are often unaware that they are part of the supply chain
- **Operational management:** Continuous SCA (vulnerability analysis), security update management, licence tracking
- **DORA prior requirement:** Without SBOM, the organisation cannot identify its software suppliers

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
- Both categories require inventory and oversight - there is no optionality
- SBOM feeds the technical component risk inventory
- Contractual suppliers feed the organisational risk inventory
- **Intentional gap:** SbD-ToE does not include ITS templates or DORA concentration-analysis formulas. Compliance requires: maintaining an up-to-date SBOM ([Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)), a formal contractor inventory ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)) and contractual templates with security clauses aligned with DORA.

---

### Information Sharing on Cyber Threats (DORA Article 45, complementary context) {#partilha-de-informação-sobre-ameaças-artigo-45-dora-contexto-complementar}

DORA Article 45 establishes information-sharing arrangements on cyber threat information and intelligence, promoting cooperation among financial entities and with the competent authorities.

**SbD-ToE coverage:**
- **[Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Integration of threat intelligence indicators into monitoring processes
- **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Governance structures and reporting responsibilities

**Intentional gap:** SbD-ToE does not prescribe specific institutional arrangements or processes for notifying the supervisor. The integration of threat intelligence feeds (e.g. STIX/TAXII, MISP) and the formalisation of sharing channels with competent authorities must be established in accordance with sector guidance and DORA regulatory requirements.

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
- **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** RACI structure for approvals (implicitly defines the authority for exceptions)

**Intentional gap:** SbD-ToE does not define:
- Authority levels for approving exceptions in a DORA context (board, CISO, compliance officer)
- Categories of admissible exceptions under DORA (some may be inadmissible)
- Templates for reporting exceptions to the regulator
- Remediation SLA by exception type

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
| **SQLi in production (L3) without a documented exception** | Exploitation, data breach, notifiable incident | Unassigned responsibility, lost trail | ❌ **SEVERE** - Breach of oversight and tracking in a defensible DORA scenario |
| **Critical CVE ignored without justification** | Continuous exposure, compliance gap | ICT risk management failure | ❌ **SEVERE** - May run counter to risk management, validation and continuous remediation duties under DORA |
| **Exception approved verbally (on Teams/informal email)** | Loss of trail, lack of formal authority, ad hoc renegotiation | Impossible to audit decisions | ❌ **CRITICAL** - No governance evidence; the regulator asks: "who approved?" |
| **Expired exception without reassessment** | Accepted risk becomes unaccepted risk (drift), silent technical breach | The application continues with risk above the threshold | ❌ **CRITICAL** - Breach of Art. 5 (lack of continuous oversight) |

---

#### What DORA Explicitly Requires {#o-que-dora-exige-explicitamente}

**Art. 5 (ICT Risk Management):**
> "Members of the management body approve the strategy and oversee the implementation of policies, including responses to emerging risks."

**Operational translation:**
- Risk acceptance decisions (exceptions) require documented approval from a formal authority
- The regulator interprets prior knowledge of an exploited vulnerability without documented approval as negligent oversight
- Exceptions require periodic reassessment - the absence of reassessment constitutes indefinite tacit approval, amounting to a failure of oversight

**Art. 17–23 (Incidents and reporting):**
> Exceptions with an impact on incident management, classification or reporting must be contextualised and handled with a documentary trail compatible with the applicable regulatory regime.

**Art. 24–27 (Testing):**
> The continuous testing programme must cover realistic scenarios. Exceptions (e.g. an untestable legacy component) require documented compensation and a bounded reading in relation to the TLPT regime.

**Art. 28–30 (Suppliers):**
> Exceptions to supplier SLAs, critical dependencies or unmitigated CVEs must be escalated in line with the applicable risk and governance model.

---

#### SbD-ToE Coverage (Strong, but with Explicit Gaps) {#cobertura-sbd-toe-forte-mas-com-gaps-explícitos}

**What SbD-ToE ALREADY PRESCRIBES (excellent):**

| Chapter | What it prescribes | Level of detail |
|----------|-----------------|-----------------|
| **[Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | L1–L3 classification (basis for exception criticality) | ✅ Clear E+D+I model; L1/L2/L3 criteria defined |
| **[Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), addon 03** | Risk acceptance criteria (thresholds per level) | ✅ L1≤9, L2≤6, L3≤4; requires validation by 2+ profiles at L2/L3 |
| **[Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), addon 08** | Management of exceptions to requirements (formal process) | ✅ Identification, justification, assessment, compensation, periodic review |
| **[Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), addon 03** | Exceptions to architectural requirements | ✅ Register model with a time horizon; designated owners |
| **[Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), addon 09** | Exceptions to CVEs (formalisation, owner, TTL, impact) | ✅ Complete process: identification → justification → acceptance → TTL → revalidation |
| **[Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Exceptions to security testing (with formal approval) | ✅ Explicit mention: "formally approved exceptions" |
| **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Exception governance (RACI, approval flow, audit) | ⚠️ **PARTIAL** - User Stories define roles, but do not explain the DORA implications |
| **[Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Waivers and temporary exceptions (during training) | ✅ "Formal documented justification, approved by AppSec/GRC/management" |

---

#### Identified Gaps (Inconsistencies with DORA) {#gaps-identificados-incoerências-com-dora}

**Gap 1: Lack of Explicit Mapping of DORA-Compatible Authority**

| Level | SbD-ToE Prescribes | DORA Requires | Gap |
|-------|------------------|-----------|-----|
| **L1** | Validation by AppSec Engineer (informal) | Approval by a formally designated authority | ⚠️ Developer-friendly, but clear escalation is missing |
| **L2** | Formal validation by AppSec + GRC | Approval by the CISO or a formal equivalent | ✅ Adequate, but the Manual does not say so explicitly |
| **L3** | Approval by Executive Management/CISO | **Approval by the board or CRO (DORA requirement)** | ❌ **CRITICAL GAP** - The Manual does not specify "board-level approval" |

**How it manifests:** The organisation accepts an L3 exception with CISO approval; the regulator asks: "was it approved by the board?" → no minutes = **governance failure**.

---

**Gap 2: No Description of Unacceptability under DORA**

| Exception | SbD-ToE | DORA |
|---------|---------|------|
| "Not implementing MFA because it is complex" | Technically acceptable with TTL at L1 | ❌ **May run counter to minimum strong authentication and ICT risk management measures under DORA** |
| "SQLi in a legacy endpoint, stays as is" | Acceptable with compensation (e.g. WAF) at L1/L2 | ❌ **May breach DORA** (SQLi is never acceptable at any L) |
| "P0 CVE at runtime, with no fix plan" | Acceptable if compensated at L1 | ❌ **May run counter to remediation, validation and continuous oversight duties under DORA** |

**How it manifests:** The organisation formally records the exception in SbD-ToE; the regulator rejects it: "this exception is not admissible under DORA" → lost time, forced review.

---

**Gap 3: No TTL Tracking vs. Continuous Oversight**

| Process | SbD-ToE | DORA Requirement | Gap |
|----------|---------|----------------|-----|
| **Exception creation** | Documents with owner, TTL, criteria | ✅ Good | ✅ Aligned |
| **Periodic reassessment** | Review 30 days before expiry; mandatory re-approval | ✅ Good | ✅ Aligned |
| **Centralised tracking** | GRC tool; audit trail per application | ✅ Good | ⚠️ The Manual does not describe the reporting format for DORA |
| **Escalation to the regulator** | Not mentioned in the Manual | ❌ DORA requires exceptions to be reported in the context of incidents | ❌ **GAP** - No guidance on when to escalate to the regulator |

**How it manifests:** A security incident; the regulator asks: "show me the relevant exceptions" → the organisation has no consolidated view or does not know whether it must report.

---

**Gap 4: No Formal Organisational Policy on Unacceptability**

SbD-ToE describes **how** to manage exceptions, but does not establish **which categories are unacceptable under DORA**:

- **Never acceptable in a defensible DORA reading:**
  - Exceptions without documented approval
  - Expired exceptions without reassessment
  - Breaches of regulatory compliance (e.g. SQLi, command injection)

- **Acceptable with restrictions (compatible with DORA):**
  - Exceptions with TTL, a fix plan and compensation
  - Exceptions approved by the board/CRO
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
   - Vulnerabilidades exploráveis sem compensação (ex: SQLi, injeção)
   - Violações de requisitos obrigatórios de conformidade
   ➜ Ação: REJEITAR; forçar mitigação

B. Exceções ACEITÁVEIS com aprovação board-level (L3 DORA):
   - Componentes legados sem patch aplicável
   - CVEs com "no fix available" + compensação (ex: isolamento de rede)
   - Arquitetura herdada em transição
   ➜ Ação: APROVAR se board/CRO assina; TTL ≤ 90 dias; reavaliação obrigatória

C. Exceções ACEITÁVEIS com aprovação CISO-level (L2 DORA):
   - Requisitos técnicos com compensação equivalente
   - Testes legítimos de resiliência suspensos (ex: TLPT adiado)
   ➜ Ação: APROVAR se CISO/AppSec assina; TTL ≤ 180 dias; reavaliação obrigatória

D. Exceções ACEITÁVEIS com aprovação AppSec-level (L1):
   - MVP com funcionalidade reduzida de segurança
   - Prototipagem com dados não-sensíveis
   ➜ Ação: APROVAR se AppSec assina; TTL ≤ 365 dias; reavaliação obrigatória

Rastreamento:
- Ferramenta GRC centralizada (SAP GRC, AuditBoard, ou custom)
- Campos: ID | Aplicação | Nível | Exceção | Justificação | Aprovador | Data | TTL | Status | Observações regulatórias
- Reporte trimestral a CISO/board
- Reporte ad-hoc a regulador se incidente relacionado
```

---

**2. Clarify in the SbD-ToE Manual**

Add a dedicated section to [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) (Governance):

```markdown
## Compatibilidade DORA: Exceções Inaceitáveis vs. Aceitáveis

[Tabela acima com categorias A–D]

### Implicações Regulatórias

Se um incidente ocorre e há exceção relacionada:
- **Com aprovação documentada** → Demostra supervisão; mitigação regulatória
- **Sem aprovação documentada** → Evidência de negligência; penalidade potencial

### Processo de Escalada ao Regulador

[Template de como reportar exceção ao supervisor em contexto de incidente]
```

---

**3. Integrate into the User Stories of [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)**

Expand `US-15 (Processo formal de exceções)` with:
- DORA-compatible Approval Matrix
- Unacceptability categories
- Template for reporting to the regulator

---

#### Summary: Why the Absence of Formal Management = DORA Inconsistency {#resumo-por-que-ausência-de-gestão-formal--incoerência-dora}

| Aspect | Without Formal Management | With SbD-ToE Management + DORA Mapping |
|--------|-------------------|----------------------------------|
| **Regulatory discovery** | No documentation of exceptions, or unknown location ❌ | Formal process in a GRC system with board-level approval ✅ |
| **Audited trail** | Exceptions in informal channels (Slack/Teams/email) ❌ | Exceptions in a GRC tool with a complete audit trail ✅ |
| **Board oversight** | The board is unaware of critical exceptions ❌ | The board receives quarterly reporting on L3 exceptions ✅ |
| **Incident response** | Unawareness of an exploited vulnerability ❌ | Vulnerability recorded in an approved exception with a correction plan; escalated according to protocol ✅ |
| **Audit findings** | Critical finding: governance failure ❌ | Minor finding: operational improvement opportunities ✅ |

---

### Practical Compliance {#conformidade-prática}

**Alignment of SbD-ToE with DORA:**
1. ✅ Apply the formal SbD-ToE exceptions process ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) addon 09)
2. ✅ Map criticality levels to DORA-compatible approvers (L1→AppSec, L2→CISO, L3→Board/CRO)
3. ✅ Define unacceptability categories (organisational policy)
4. ✅ Implement centralised tracking with an audit trail (GRC tool)
5. ✅ Establish quarterly reporting to governance structures (DORA Art. 5 requirement)
6. ✅ Define a protocol for escalation to the regulator in an incident context (Art. 17–23)

---

## CROSS-CHECK CONCLUSION {#conclusão-do-cross-check}

**SbD-ToE covers the technical core of DORA**. The gaps observed are not failures of the model, but **deliberate abstentions** to preserve universality and applicability across diverse organisational contexts.

**Requirements for full compliance:**
- Mapping of SbD-ToE policies to formal management body approvals
- Configuration of incident fields according to the DORA RTS/ITS
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

**Version:** 1.0  
**Date:** November 2025  
**Next review:** June 2026
