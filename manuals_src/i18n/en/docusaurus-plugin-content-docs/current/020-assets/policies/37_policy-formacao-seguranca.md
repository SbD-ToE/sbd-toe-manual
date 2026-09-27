---
id: policy-formacao-seguranca
title: Security Training and Upskilling Policy
description: Organisational policy that defines the requirements for the security training and upskilling programme, including mandatory onboarding, training tracks by profile and risk level, the Security Champions programme, practical exercises, content updates, effectiveness KPIs and integration with individual performance objectives, proportionate to the criticality level (L1, L2, L3).
tags: [policy, formação, capacitação, onboarding, Security Champions, trilhos formativos, labs, CTF, KPIs formação, cap13, L1, L2, L3, governance, SSDF, SAMM]
grupo: governacao
sidebar_position: 37
translation:
  source_locale: pt
  source_path: 020-assets/policies/37_policy-formacao-seguranca.md
  source_sha256: 09a172b6a99b298c33191a63f1e6f0c11dfbf363c309dc31b60bc03c36d11207
  source_commit: 5caf1bb9d128df1f7fb0b1e5b2a5603db3e6127f
  target_sha256: 44bcda4508f2573549e4bd7b84823adb365de6373f1d6940dd948093870b5e65
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [avaliacao, capacitacao, chapter_role, eu_ai_deployer, eu_ai_literacy, framework_source_corpus, gap_family, llm, maturity, mcp_reading_programa, papel_suporte, practitioner_manual, programme_line, provenance, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, threat, traceability, trilho_formativo, validation_evaluation]
  glossary_sha256: 87768844743d61be242731bbc49002197ed38d006846bd7c658dd3f46b56902f
  translated_at: 2026-09-27T08:34:27Z
  stamped_at: 2026-09-27T08:34:27Z
  reviewed_by: null
---

# Security Training and Upskilling Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the organisation's **security training and upskilling programme**, covering the onboarding of new staff, continuous training tracks by profile and risk level, the Security Champions programme, practical exercises and the mechanisms for effectiveness assessment.

Security policies, tools and processes are ineffective without the people who operate them. Security training is not an annual compliance exercise - it is the mechanism that turns technical prescriptions into daily operational practice. A developer who understands the security implications of code decisions makes better decisions in every pull request. A DevOps engineer who understands the threat model of their infrastructure configures it more securely. A Security Champion who has authority, knowledge and institutional support is able to disseminate and sustain the security culture in their team. Without deliberate investment in upskilling, human risk remains the hardest vector to mitigate.

The objective of this policy is to ensure that:

- All staff with technical responsibilities receive security training proportionate to their profile and to the risk level of the applications they work on
- The onboarding of new staff includes security training before full technical access
- The training tracks are kept up to date and reflect the relevant risks and technologies
- The Security Champions programme is operational and has institutional support
- Practical exercises replace or complement purely theoretical training
- The effectiveness of training is measured with defined KPIs

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

This policy applies to all staff with technical functions who take part in the development, operation, testing, architecture or governance of the organisation's systems. It includes internal staff, contractors and suppliers with ongoing technical access.

| Level | Applicability |
|---|---|
| L1 | Basic onboarding training; security awareness; access to training resources |
| L2 | Mandatory; training tracks by profile; structured onboarding; designated Security Champion; annual content review |
| L3 | Mandatory; complete tracks with mandatory practical exercises; Security Champion with advanced training; periodic simulations; effectiveness KPIs monitored |

---

## 3. Onboarding of new staff {#3-onboarding-de-novos-colaboradores}

Every new staff member with technical functions must complete the security onboarding process before receiving full technical access:

### 3.1 Minimum onboarding content {#31-conteúdos-mínimos-de-onboarding}

| Topic | Description | Applicability |
|---|---|---|
| The organisation's security policies | Presentation of the policies applicable to the function (secrets management, data access, credential management, IRP) | All levels |
| Secure credential management | Use of a vault, prohibition of hardcoding, rotation of personal credentials | All levels |
| Data classification and minimum access | Principle of least privilege; data categories; what may and may not be shared | L2/L3 |
| Reporting of incidents and anomalies | Reporting channel, what to report, individual responsibility | All levels |
| Secure development practices (baseline) | Fundamentals relevant to the function | L2/L3 |
| The organisation's security tools and process | SAST, SCA, secrets management, security pipeline | L2/L3 |

### 3.2 Onboarding validation {#32-validação-de-onboarding}

- [ ] Completion documented in the LMS or HR system
- [ ] Quiz or assessment with a minimum score of 80%
- [ ] Record archived and associated with the staff member's identity
- [ ] Full technical access conditional on completion of onboarding (L2/L3)

---

## 4. Training tracks by profile and risk level {#4-trilhos-formativos-por-perfil-e-nível-de-risco}

The training tracks are the set of mandatory and optional modules recommended for each technical profile, calibrated by the risk level of the application the staff member works on.

### 4.1 Matrix of tracks by profile and risk level {#41-matriz-de-trilhos-por-perfil-e-nível-de-risco}

| Function | L1 | L2 | L3 |
|---|---|---|---|
| **Developer** | Basic secure coding; dependency management | Lightweight threat modelling; SCA; secure code review | Formal threat modelling; secure architecture; labs on vulnerable applications |
| **QA / Testing** | Basic security testing | Security acceptance criteria; lightweight fuzzing | Advanced fuzzing; validation of exceptions; SAST/DAST |
| **DevOps / SRE** | Secrets management; environment configuration | Secure integration in CI/CD; pipelines with security gates | SLSA; provenance; continuous monitoring; secure IaC |
| **Product Owner** | Minimum security requirements; secure backlog | Risk classification; exception management | Formal risk acceptance process; review with AppSec |
| **AppSec Engineer** | - | Threat modelling facilitation; PR review; tool operation | Advanced threat modelling; SBOM analysis; programme management |
| **Security Champion** | General awareness | SbD-ToE policies and practices; basic mentoring | Advanced track; threat modelling; leading CTFs; participation in war rooms |
| **Management / Tech Lead** | Executive awareness | Risk classification; exceptions and approvals | Maturity metrics; executive reporting; post-mortems |

### 4.2 Mandatory vs. optional modules {#42-módulos-obrigatórios-vs-opcionais}

Each training track must explicitly identify:

- **Mandatory modules**: a condition for access to systems (onboarding) or for keeping access (annual renewal)
- **Recommended modules**: deepening proportionate to the risk level and to the function
- **Optional modules**: voluntary advanced upskilling or upskilling for progression to Security Champion

---

## 5. Security Champions programme {#5-programa-de-security-champions}

The Security Champions programme aims to distribute security competences across the development teams, creating points of accountability and dissemination that do not depend on centralisation in the AppSec Engineer.

### 5.1 Programme requirements {#51-requisitos-do-programa}

| Requirement | Description |
|---|---|
| Formal designation | Security Champion designated per L2/L3 application (see Organisational Traceability Policy) |
| Specific training track | Additional training beyond the function's base track - threat modelling, exception management, leading exercises |
| Documented responsibilities | Mentoring the team; taking part in code reviews; coordination with AppSec; submission of exceptions; maintenance of the compliance repository |
| Champions community | Regular meetings among all active Champions (at least monthly at L3); dedicated communication channel; sharing of good practices and anti-patterns |
| Institutional recognition | The Security Champion function must have visibility and formal recognition (e.g. mention in performance assessments, participation in security conferences) |

### 5.2 Renewal and updating {#52-renovação-e-actualização}

Security Champion training must be renewed annually. A Security Champion with expired training must complete the renewal within 60 days, during which the responsibilities may be shared with the AppSec Engineer while the update is completed.

---

## 6. Practical exercises and simulations {#6-exercícios-práticos-e-simulações}

Purely theoretical training has a low retention rate and does not develop the capacity to respond in real scenarios. Practical exercises are a mandatory component of the L3 tracks and recommended at L2:

| Exercise type | Description | L2 | L3 |
|---|---|---|---|
| Labs on vulnerable applications | Controlled environments with real vulnerabilities for identification and exploitation (e.g. OWASP WebGoat, Juice Shop, DVWA) | Recommended | Mandatory |
| CTF (Capture the Flag) | Competitions or structured exercises with security challenges by category | Recommended | Mandatory (minimum 1/year) |
| Threat modelling simulation | Practical threat modelling session on a real or fictitious architecture, with a documented result | Recommended | Mandatory |
| Incident response tabletop | Incident simulation exercise without real activation of systems (see IRP Policy) | Mandatory (half-yearly; Policy 32 §8) | Mandatory (half-yearly) |
| Guided security code review | Code review with injected anti-patterns, in a training context | Recommended | Mandatory |

The results of the exercises must be recorded with date, participants, exercise type and performance metrics (where applicable).

---

## 7. Updating of training content {#7-actualização-de-conteúdos-formativos}

Training tracks reflect the state of the art at a given moment - without updating, they become obsolete and create false confidence. The content must be reviewed:

| Cadence | Scope |
|---|---|
| Annual (minimum) | Complete review of all modules; removal of obsolete content; addition of newly identified risks |
| After a security incident | Review of the modules relevant to the root cause; addition of the lesson learned to the track |
| After a significant technological change | Update of the affected modules (e.g. new platform, new framework, new regulation) |
| After feedback from Security Champions | Incorporation of anti-patterns identified in a real context |

The content review must be coordinated by the AppSec Engineer with input from the Security Champions and from GRC. The changes are communicated to the teams and to the HR system so that completion records are updated where applicable.

---

## 8. Training effectiveness KPIs {#8-kpis-de-eficácia-formativa}

The effectiveness of training must be measured on the basis of indicators that go beyond the completion rate:

| KPI | Description | Target |
|---|---|---|
| Mandatory training completion rate | % of staff with the mandatory training track completed | > 90% |
| Quiz pass rate | % of participants with a score ≥ 80% | > 85% |
| Average time to complete a track | Indicator of the accessibility and suitability of the training load | Internal reference |
| % of Security Champions with valid training | Champions with non-expired training | 100% |
| Recurrence rate of findings of the same type | Reduction of recurring vulnerabilities attributable to knowledge gaps | Downward trend |
| Average resolution time in exercises | MTTR in incident simulations - improvement over time | Downward trend |
| % of topics failed in the quiz | Identification of the knowledge areas with the largest gap - informs content review | Downward trend per topic |

Training KPIs must be reported quarterly to GRC and integrated into the security governance reports.

---

## 9. Integration with individual performance objectives {#9-integração-com-objectivos-de-performance-individuais}

At L3, active participation in the security programme must be formally recognised:

- [ ] Completion of mandatory training integrated as a performance assessment criterion
- [ ] Security Champion role recognised in the staff member's performance assessments
- [ ] Participation in practical exercises recorded as professional development
- [ ] Budget for external training and security certifications made available for technical profiles with security responsibilities

---

## 10. Responsibilities {#10-responsabilidades}

| Role | Responsibility |
|---|---|
| AppSec Engineer | Define and maintain the training tracks; coordinate the Security Champions programme; facilitate practical exercises; analyse effectiveness KPIs |
| GRC / Compliance | Manage the LMS or training record system; monitor KPIs; produce periodic reports; audit compliance |
| HR | Integrate mandatory training into the onboarding process; record completion; integrate metrics into performance assessments |
| Security Champion | Complete the specific training track; mentor the team; take part in exercises; report identified knowledge gaps |
| Tech Lead | Ensure that the team has time allocated for training; promote participation in exercises; escalate identified gaps |
| Management / CISO | Ensure budget and resources for the training programme; institutionally recognise the Security Champion role; analyse effectiveness reports |

---

## 11. Training on AI agents and pervasive tooling (mandatory module) {#11-formação-em-agentes-ai-e-tooling-pervasivo-módulo-obrigatório}

When the organisation adopts AI agents with *tool-use* in the SDLC (Policy 38), all directly involved *roles* are subject to mandatory minimum training on the subject. It is not optional training — it is part of the competence *baseline*, on a par with what is required on OWASP Top 10 or basic *secure coding*.

### 11.1 Minimum coverage per *role* {#111-cobertura-mínima-por-role}

| Role | Minimum content | Cadence |
|---|---|---|
| **Developer** | Secure assisted use (mandatory review of the output, *secret scanning*, licences); prompts and *skill files* as code; anti-patterns; when to escalate to `appsec` | Onboarding + annual update |
| **AppSec Engineer** | A0–A4 model + `REQ-AGN-*`; agentic threat modelling (Ch. 03 playbook); MITRE ATLAS + OWASP LLM Top 10; eval suites; response to *off-policy actions* and *intent-action divergence* | Onboarding + half-yearly update |
| **DevOps / SRE** | *Workload* identity for agents (OIDC); per-tool *scoping*; operational *kill-switch* + exercises; agentic telemetry (OPS-012/013/014) | Onboarding + half-yearly update |
| **GRC / Compliance** | Policy 38 (mandates); AI contractual clauses (Policy 33 §10); AI Act Art. 14 + 26 + 53 + 55; organisational review of mandates | Onboarding + half-yearly update |
| **Tech Lead / Software Architect** | [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) patterns; agentic architecture (intent declaration, out-of-band approval, kill-switch); AI supply chain (`DEP-011..014`) | Onboarding + annual update |
| **Product Owner / Scrum Master** | Implications of the A0–A4 levels for requirements and *acceptance criteria*; when a feature requires a new *mandate* | Onboarding + annual update |
| **CISO / Executive Management** | Operational and regulatory risk of agents; A4 approval; periodic review of the mandate register | Annual |

### 11.2 Recommended practical exercises {#112-exercícios-práticos-recomendados}

- **Tabletop**: simulation of an *off-policy action* in production — who triggers the *kill-switch*, who communicates, who escalates (cross-link Ch. 12 Monitoring and Operations, IRP).
- **Hands-on**: PR review exercise with GenAI output — identify problematic patterns.
- **Red team**: attempt *prompt injection* against an agent in a sandbox; observe detection in OPS-014.
- **Mandate exercise**: receive a realistic scope, classify the A0–A4 level, write the mandate.

### 11.3 Where it lands {#113-onde-aterra}

This training is part of the Ch. 13 track ([addon 12 — Training in the Secure Use of AI and Pervasive Tooling](/sbd-toe/sbd-manual/formacao-onboarding/addon/formacao-uso-seguro-ia-tooling)). This policy makes it **mandatory** (instead of recommended) when there are AI agents at A1+ in the organisation's SDLC.

### 11.4 Proportionality {#114-proporcionalidade}

| Organisational risk level | Mandatory coverage |
|---|---|
| L1 | Developer + AppSec + DevOps (essential) |
| L2 | + GRC + Tech Lead/SWA + PO/SM |
| L3 | All *roles* in table 11.1 + half-yearly practical exercises |

---

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- A security incident in which a root cause was a knowledge gap or an inadequate practice by a staff member
- A significant change in the technology portfolio that introduces new competence requirements
- A regulatory change that imposes new training requirements (e.g. DORA, NIS2, AI Act Art. 4)
- A training effectiveness KPI that indicates systematic degradation
- Operational adoption of AI agents at A1+ that activates section 11

---

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 13 - Training and Upskilling | US-03: Security Champions; US-04: practical exercises; US-09: updating of tracks; US-10: risk-proportionate tracks; US-14: upskilling KPIs |
| SbD-ToE Ch. 13 (addon 12) — Training in the Secure Use of AI and Pervasive Tooling | Detailed content of the agentic module |
| AI Agent Mandates Policy (`38_policy-mandates-agentes.md`) | Activation of section 11 |
| Support Tools Usage Policy (`16_policy-uso-ferramentas-apoio.md`) | A0–A4 usage rules |
| Organisational Traceability Policy (`34_policy-rastreabilidade-organizacional.md`) | Formal designation of Security Champions |
| Secure Contracting Policy (`33_policy-contratacao-segura.md`) | Minimum training for contractors and suppliers |
| IRP Policy (`32_policy-irp.md`) | Incident response tabletops and simulations |
| NIST SSDF - PO.3, PO.7 | Training requirements for secure software development |
| NIST AI RMF 1.0 — GOVERN-3.x | AI workforce education |
| OWASP SAMM - Education and Guidance | Security training and awareness practices |
| OWASP Top 10 for LLM Applications (2025) | Syllabus content for AppSec |
| MITRE ATLAS | Catalogue of adversarial tactics/techniques for AppSec / red team |
| OWASP WebGoat / Juice Shop / DVWA | Reference platforms for labs on vulnerable applications |
| DORA - Art. 13(6) | ICT-related training requirements for financial entities |
| NIS2 - Art. 21 | Cybersecurity training obligations |
| ISO/IEC 27001 - A.7.2.2 | Information security awareness, education and training |
| ISO/IEC 42001:2023 | AI Management System — workforce competence |
| EU AI Act (Regulation (EU) 2024/1689) - Art. 4 (AI literacy), as worded by Regulation (EU) 2026/1744 | Providers and deployers «shall take measures to support the development of AI literacy» of their staff, without an obligation to guarantee «any specific level of AI literacy»; the mandatory training in §11 is the Manual's choice |
