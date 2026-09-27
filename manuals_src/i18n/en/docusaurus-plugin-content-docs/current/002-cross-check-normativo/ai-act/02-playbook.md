---
id: playbook
title: "SbD-ToE 4 AI Act: Implementation Playbook"
description: Practical roadmap for implementing SbD-ToE in line with the requirements of Regulation (EU) 2024/1689 (AI Act) - mapping of articles to actions, by role and risk category
tags: [playbook, ai-act, regulamento-ia, implementacao, roadmap, gpai]
sidebar_position: 2
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/ai-act/02-playbook.md
  source_sha256: 2d739d5b031657083f782285e7ad72148e6aa15f2c38ac13b3006dd750bb7904
  source_commit: 5caf1bb9d128df1f7fb0b1e5b2a5603db3e6127f
  target_sha256: e3d1bd99ad756d0907a3e3a82f4e1fe378373bfff5d38bb1a3ae83c0f28eadbf
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, esquema_regime, eu_ai_deployer, eu_ai_high_risk_system, eu_ai_human_oversight, eu_ai_literacy, eu_ai_post_market_monitoring, eu_ai_qms, eu_ai_system, eu_ai_widespread_infringement, eu_ce_marking, eu_market_surveillance_authority, framework_source_corpus, layer, lifecycle_phase, llm, mapping, maturity, mcp, mcp_reading_programa, papel_suporte, practitioner_manual, programme_line, provenance, requirement_runtime, role_juridico, role_tech_lead, sbdtoe_sbd, schema, slug_threat_modeling, trilho_formativo, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 90b2c2790f46bebc3a998e3c9463cf7fc84a6271d33f8bb8dab1b33633726b36
  translated_at: 2026-09-27T08:34:17Z
  stamped_at: 2026-09-27T08:34:17Z
  reviewed_by: null
---

# SbD-ToE 4 AI Act: Implementation Playbook

## Overview {#visão-geral}

This playbook maps **AI Act requirements (Regulation (EU) 2024/1689) to practical SbD-ToE actions**, focusing on the technical obligations for **high-risk** AI systems and **general-purpose AI (GPAI)** models.

**Principle:** SbD-ToE covers the **technical core** of the AI Act - accuracy, robustness, cybersecurity (Art. 15), logging (Art. 12), risk management (Art. 9), QMS (Art. 17), post-market monitoring (Art. 72) and incidents (Art. 73). The **AI-domain** dimensions (data/bias, human oversight, transparency) and the **legal** ones (risk classification, FRIA, conformity assessment, CE marking) require coordination with data science, product, legal and compliance teams.

**Structure:** Each section shows:
- AI Act requirement (article)
- Applicable SbD-ToE chapter/addon
- What to do (concrete action)
- Regulatory evidence

> 📚 **Supporting Resources:** For practical templates and implementation examples, see [Example Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options), with reusable toolchains, KPIs, RACI and incident reports for the AI Act and other frameworks.

---

## Step 0: Determine role and risk category (prior requirement) {#passo-0-determinar-papel-e-categoria-de-risco-pré-requisito}

Before any technical action, the legal framing must be established - **compliance/legal work, not AppSec work**, but it conditions the whole playbook:

1. **What is the role?** Provider, deployer, importer or distributor (AI Act, Article 3, points (3), (4), (6) and (7)). The bulk of the technical obligations falls on the **provider of high-risk AI systems** (Article 16).
2. **What is the risk category?**
   - **Unacceptable** (Art. 5) → prohibited; no technical playbook can legitimise it.
   - **High-risk** (Art. 6, Annexes I/III) → most of this playbook applies.
   - **Certain AI systems** (Art. 50 — direct interaction with people, synthetic content, emotion recognition or biometric categorisation, deep fakes) → transparency obligations, which add to those of Chapter III when the system is also high-risk (Article 50(6)).
   - **Other AI systems** → none of the Chapter III requirements; Art. 4 (AI literacy), addressed to providers and deployers of AI systems, nevertheless applies.
3. **Is it a GPAI model?** If so, Art. 53 (with the paragraph 2 exception for models released under a free and open-source licence without systemic risk) and Art. 55 (systemic risk) apply - see Phase 7.

> ⚠️ **Outside the SbD-ToE scope:** risk classification and role qualification are legal determinations. SbD-ToE takes the outcome of this analysis as an input.

---

## Quick Map: AI Act Art. → SbD-ToE {#mapa-rápido-ai-act-art--sbd-toe}

> ✏️ **Refresh 2026-05-30.** Map updated with the agentic layer — `REQ-AGN-*` (Ch. 02), [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (Ch. 04), `DEP-012..014` (Ch. 05), `OPS-012..014` (Ch. 12), Policy 38 (*mandates*), Policy 39 (AI BOM).

| AI Act Article | Requirement | SbD-ToE Chapter | Main Action |
|---|---|---|---|
| **4** | AI literacy (measures to support its development — wording of Regulation (EU) 2026/1744) | [Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro) + [Policy 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca) | Training track per *role*; mandatory with A1+ agents (the Manual's choice) |
| **9** | Risk management | [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Ch. 02 §A0–A4](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia), [Ch. 03 agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) | Classify L1–L3 + level A0–A4; threat model with ATLAS |
| **10** | Data and data governance | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) (`DEP-011..014`) + [Policy 39](/sbd-toe/assets/policies/policy-ai-bom-supply-chain) | AI BOM (CycloneDX 1.6 *ml-bom*) + *pinning* + approved *providers* |
| **11 / Annex IV** | Technical documentation | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Policy 38](/sbd-toe/assets/policies/policy-mandates-agentes) (mandate) | Annex IV index + *model card* + mandate + AI BOM |
| **12 / 19** | Logging and retention | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) + `OPS-011..014` + Ch. 12 US-13 | Inference logs + audit per *tool invocation* |
| **13** | Transparency and provision of information to deployers | Ch. 04 + [Policy 38](/sbd-toe/assets/policies/policy-mandates-agentes) (mandate) | *Mandate* as the source of capabilities/limitations/oversight |
| **14** ⚡ | Human oversight | [Ch. 02 §A0–A4](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia) + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + Policy 38 | Autonomy level model + *kill-switch* + *intent declaration* + OOB approval |
| **15** | Accuracy, robustness and cybersecurity | [Ch. 03 playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic), `ARC-014/015`, [Ch. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) (*eval suites*), [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak*) | Continuous *eval suites* + threat library + *off-policy detection* |
| **17** | QMS | [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), Ch. 14, Policy 38 (mandate lifecycle), Policy 39 (AI BOM lifecycle) | Map gates + formal cycles to Art. 17 |
| **25** | Responsibilities along the AI value chain | `DEP-013/014` + Policy 39 + Ch. 14 US-21 | *Pinning* + approved *providers* + clauses |
| **26** | Obligations of deployers | Policy 38 (mandate) + Ch. 00 (composite function) + Ch. 12 US-13 | *Deployer* mandate + qualified oversight + logs under control |
| **53 / 55** | GPAI | [Ch. 03 playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) + Ch. 05 (`DEP-011..014`) + [Ch. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Ch. 14 US-21 | AI red teaming via *eval suites* + protection of weights + Art. 53/55 clauses |
| **72** | Post-market monitoring | Ch. 12 + `OPS-011..014` + Ch. 12 US-13 | Agentic telemetry + *drift detection* + improvement cycle |
| **73** | Serious incidents | Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 16 §11.4 + Policy 30 §9.3 + Policy 39 §7 | *Runbook* + agentic incident classes + *upstream* IR |

---

## How to Implement (Logical Order) {#como-implementar-ordem-lógica}

### Phase 1: Governance and QMS (M0–M3) {#fase-1-governação-e-qms-m0m3}
**AI Act Art. 17** - Establish a quality management system

1. **Define AI governance**
   - Members: CISO, AI/ML lead, GRC, legal, product
   - **Evidence:** Minutes, approved AI policy
   - Reference: [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

2. **Map SbD-ToE gates to the elements of the QMS (Art. 17)**
   - Development procedures → [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)
   - Quality control and validation → [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)
   - Reuse **ISO/IEC 42001** if it already exists
   - 📄 **Template:** [RACI and Governance](../exemplo-playbook/exemplo-raci-governance)

3. **Define the AI RACI**
   - Who approves a model release, who signs off exceptions, who reports incidents (Art. 73)

---

### Phase 2: Classification and risk management (M2–M5) {#fase-2-classificação-e-gestão-de-risco-m2m5}
**AI Act Art. 9** - Continuous risk management system

1. **Inventory AI systems**
   - Purpose, data processed, model(s), inference service, dependencies
   - Reference: [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classify criticality (L1–L3) and align with the AI Act category**
   - High-risk AI system (Annex III) → typically L3
   - Document that proportionality follows the AI Act category

3. **Threat model extended to the adversarial vector**
   - Base: STRIDE / MITRE ATT&CK ([Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro))
   - Extension: **MITRE ATLAS** and **OWASP ML/LLM Top 10**
   - Cover (Article 15(5)): data poisoning, model poisoning, adversarial examples or model evasion (*adversarial examples* / *model evasion*), confidentiality attacks, model flaws
   - **Evidence:** Documented threat model, residual risk and measures (Art. 9)

---

### Phase 3: Data and documentation (M3–M6) {#fase-3-dados-e-documentação-m3m6}
**AI Act Art. 10, 11, Annex IV**

1. **Provenance and integrity of data and models (AI-BOM)**
   - Extend the [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) inventory to *datasets*, *checkpoints* and models
   - Integrity verification (mitigates *poisoning* and compromised models from public repositories)

2. **AI data governance (delegated to the data team)**
   - Representativeness, bias detection, statistical quality (Art. 10)
   - *Datasheets for datasets* / *data cards*
   - **Outside the AppSec scope** - SbD-ToE ensures integrity/provenance, not fairness

3. **Technical documentation (Annex IV)**
   - Build an "Annex IV index" pointing to SbD-ToE artefacts (architecture, requirements, threat model, pipeline/test evidence) + **model card**
   - Reference: [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro)

---

### Phase 4: Technical security and robustness (M5–M10) — CORE {#fase-4-segurança-técnica-e-robustez-m5m10--núcleo}
**AI Act Art. 15** - Accuracy, robustness and cybersecurity

#### 4.1 Defensive architecture {#41-arquitetura-defensiva}
- **What:** Trust boundaries (including the *agentic boundary* — [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)), input validation, isolation of the inference service, surface reduction. Where there are AI agents with *tool-use*, apply [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (agent as an isolated *principal*): dedicated identity via OIDC, minimal *scope* per *tool*, *intent declaration*, OOB approval, exercised *kill-switch*.
- **Reference:** [Ch. 04 — `ARC-014`/`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [Ch. 09 — Containers/Runtime](/sbd-toe/sbd-manual/containers-imagens/intro)

#### 4.2 Threat modelling + *eval suites* + *red teaming* (CRITICAL FOR Art. 15) {#42-threat-modeling--eval-suites--red-teaming-crítico-para-art-15}
- **What:** The test catalogue now includes continuous *eval suites* (Ch. 10 §C5) — prompt/skill regression, *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*), *drift detection*, *A/B testing*. For systems with A2+ agents, the suite is mandatory; for A4 in GPAI with systemic risk, monthly cadence.
- **Threat model:** [Ch. 03 agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) with the MITRE ATLAS threat library already included — canonical DFD (5 participants / 4 *trust boundaries*) + *threats* per boundary (`AML.T0051.001`, `T0086`, `T0101`, `T0109`, `T0110`, LLM01/06/07).
- **Reference:** [Ch. 10 §C5 — *Eval suites*](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites), [Policy 19 §7](/sbd-toe/assets/policies/policy-estrategia-testes)
- 📄 **Template:** [Toolchain Options](../exemplo-playbook/exemplo-toolchain-options)

#### 4.3 Secure ML pipeline + agents as *principals* {#43-pipeline-seguro-de-ml--agentes-como-principals}
- **What:** Security gates in the pipeline (SAST/SCA, *secrets*, artefact integrity) + AI agents operating the pipeline with ephemeral OIDC *workload identity*, per-*tool* *scope*, *audit per tool invocation* (Ch. 07 US-19).
- **Reference:** [Ch. 07 — US-19](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle), [Ch. 08 — IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Policy 18 §9](/sbd-toe/assets/policies/policy-gestao-segredos)

#### 4.4 Accuracy (delegated to the AI team) {#44-exatidão-delegado-à-equipa-de-ia}
- Declare accuracy metrics and acceptable thresholds — **AI-domain content**, supported by *eval suite* evidence (Ch. 10 §C5) and operational telemetry (Ch. 12 US-13).

---

### Phase 5: Logging and post-market monitoring (M8–M12) {#fase-5-logging-e-monitorização-pós-mercado-m8m12}
**AI Act Art. 12, 19, 72**

#### 5.1 Inference logging + audit per *tool invocation* {#51-logging-de-inferência--audit-per-tool-invocation}
- **What:** Log schema extended with inference metadata (model id/version, relevant *features*, decision and confidence, *correlation id*) + **audit per *tool invocation*** ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) where there are AI agents: `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII redacted), `intent_event_ref`, `outcome`, `external_effect`.
- **Retention:** A period appropriate to the intended purpose of the system, of at least six months (AI Act, Articles 19(1) and 26(6)); in SbD-ToE, 1 year at L2 and 2 years at L3 (the Manual's choice; [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs)); retention limited by the GDPR where personal data are involved; immutability.
- **Reference:** [Ch. 12 — `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) + [Ch. 12 US-13](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)

#### 5.2 Post-market monitoring plan (Art. 72) {#52-plano-de-monitorização-pós-mercado-art-72}
- **What:** *Dashboards* for performance, *model drift*, *token budget* ([`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013)) and detection of *jailbreak* / *off-policy actions* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)). For systems with agents at A2+, agentic telemetry (Ch. 12 US-13) is the evidential basis.
- **Triggers:** Degradation, *drift*, *budget overrun* or *off-policy* feed the reassessment under Art. 9.
- **Reference:** [Ch. 12 US-13](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle), [Policy 30 §9](/sbd-toe/assets/policies/policy-monitorizacao-seguranca)

---

### Phase 6: Serious incidents (M10–M12) {#fase-6-incidentes-graves-m10m12}
**AI Act Art. 73**

- **What:** Parameterise the *runbook* and the incident schema with the typology and time limits of Art. 73 (immediately after establishing the causal link and, at the latest, ≤15 days as a rule; ≤10 days in the event of death; ≤2 days in the event of a widespread infringement or of a serious incident under Article 3, point (49)(b); time limits counted from awareness by the provider or the deployer; an incomplete initial report is allowed). **Agentic-specific incident classes** (Policy 16 §11.4): *off-policy action*, *intent-action divergence*, successful *prompt injection*, *kill-switch* failure, *credential exposure*. ***Upstream* incidents** (Policy 39 §7): *rug pull*, *dataset poisoning*, *MCP tool poisoning*, *provider outage*.
- **How:** SIEM/ITSM exporters → notification ready for the market surveillance authority. [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) feeds the IR flow (Ch. 12 US-04).
- **Reference:** [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Policy 16 §11.4](/sbd-toe/assets/policies/policy-uso-ferramentas-apoio), [Policy 30 §9.3](/sbd-toe/assets/policies/policy-monitorizacao-seguranca), [Policy 39 §7](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)
- 📄 **Template:** [Incident Report](../exemplo-playbook/exemplo-relatorio-incidentes)

---

### Phase 7: GPAI (where applicable) {#fase-7-gpai-quando-aplicável}
**AI Act Art. 53, 55**

#### 7.1 Model protection (Art. 55 — cybersecurity) {#71-proteção-do-modelo-art-55--cibersegurança}
- **What:** Treat weights, *checkpoints*, *datasets*, MCP *tools* and embedded prompts as critical *supply chain* assets: provenance, integrity, *pinning* ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)), approved *providers* ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)), AI BOM per *release* ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)), access control.
- **Reference:** [Ch. 05 — `DEP-011..014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [Ch. 04 `ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [Policy 39](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)

#### 7.2 Continuous AI red teaming (Art. 55) {#72-ai-red-teaming-contínuo-art-55}
- **What:** A continuous adversarial evaluation programme materialised in [Ch. 10 §C5 — *eval suites*](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites): prompt/skill regression, *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*), *drift detection*, *A/B*. For agents at level A4 (internal scale of SbD-ToE) — and, regardless of level, when the organisation is a provider of GPAI with systemic risk (Art. 51) —, a monthly cadence of *kill-switch* drills and updates to the detection corpus [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014).
- **Reference:** [Ch. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites), [Policy 19 §7](/sbd-toe/assets/policies/policy-estrategia-testes)

#### 7.3 Hardening of physical and logical infrastructure (Art. 55) {#73-hardening-de-infraestrutura-física-e-lógica-art-55}
- **Reference:** [Ch. 08 — IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Ch. 09 — Containers/Runtime](/sbd-toe/sbd-manual/containers-imagens/intro), [Ch. 04 `ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)

#### 7.4 Declared contractual compliance (Art. 53/55 *providers*) {#74-conformidade-contratual-declarada-art-5355-providers}
- **What:** When GPAI is consumed from a *provider*, the contract declares compliance with Art. 53 (technical documentation, *summary of training data*, *copyright* policy) and — where applicable — Art. 55 (model evaluation with documented adversarial testing, assessment and mitigation of systemic risks, reporting of serious incidents to the AI Office, cybersecurity of the model and of the physical infrastructure).
- **Reference:** [Ch. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle), [Policy 33 §10](/sbd-toe/assets/policies/policy-contratacao-segura)

#### 7.5 GPAI documentation, copyright and data summary (delegated) {#75-documentação-gpai-copyright-e-resumo-de-dados-delegado}
- **Outside the AppSec scope** — domain and legal obligations (Art. 53). Applies when the organisation is a GPAI *provider*.

---

## Technical Alignment Checklist (AI Act) {#checklist-de-alinhamento-técnico-ai-act}

The list below makes it possible to validate the **technical alignment** of the SbD-ToE programme with the requirements of the AI Act — it does not issue the legal compliance judgement. Periodic review is recommended:

- [ ] **Framing:** Role and risk category determined (legal)
- [ ] **Literacy (Art. 4):** Training track activated in accordance with [Policy 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca) (mandatory with A1+ agents — the Manual's choice)
- [ ] **Governance/QMS (Art. 17):** AI policy approved; gates mapped; Policy 38 (mandates) + Policy 39 (AI BOM lifecycle) operational
- [ ] **Classification:** AI systems inventoried and classified (L1–L3); levels A0–A4 declared in the *mandates*
- [ ] **Risk management (Art. 9):** Threat model with the [agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) carried out; MITRE ATLAS + OWASP LLM Top 10 threat library already included
- [ ] **Oversight (Art. 14):** `REQ-AGN-001..004` operational; [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) validated; *kill-switch* exercised with recorded cadence
- [ ] **Data (Art. 10):** AI BOM CycloneDX 1.6 *ml-bom* generated per *build* ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)); approved *providers* ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)); AI *data governance* under way
- [ ] **Documentation (Art. 11/Annex IV):** Annex IV index + *model card* + *mandate* + AI BOM
- [ ] **Robustness (Art. 15):** Continuous *eval suites* operational (Ch. 10 §C5); *off-policy* / *jailbreak detection* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014))
- [ ] **Supply chain (Art. 25):** *Pinning* ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)); list of approved *providers* ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)); contractual clauses (Ch. 14 US-21)
- [ ] **Deployer (Art. 26):** Deployer *mandate* documented when the organisation uses the AI system under its own authority (Article 3, point (4)) without being its provider
- [ ] **Logging (Art. 12/19):** Inference logs + audit per *tool invocation* ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) with retention and immutability
- [ ] **Monitoring (Art. 72):** Agentic telemetry + *dashboards* for *drift*, *budget*, *off-policy*
- [ ] **Incidents (Art. 73):** Parameterised *runbook* + agentic classes (Policy 16 §11.4) + *upstream* IR (Policy 39 §7)
- [ ] **GPAI (Art. 53/55, if applicable):** AI BOM + *eval suites* + *kill-switch* exercised monthly + declared clauses
- [ ] **Evidence:** *Data room* with technical documentation, *mandates*, AI BOMs, eval reports, audit trails, telemetry

---

## What Each SbD-ToE Chapter Covers (Quick Reference) {#o-que-cada-capítulo-sbd-toe-cobre-referência-rápida}

> ✏️ **Refresh 2026-05-30.** Table updated to reflect the agentic layer. Where it said "extensible to", it now says "incorporates" — several extensions proposed in 2026-05 are already within the canon.

| Chapter | AI Act Articles | What It Does |
|---|---|---|
| **[Ch. 00 — Fundamentals](/sbd-toe/sbd-manual/fundamentos/intro)** | Art. 4, 26 | Canonical roles + composite function "AI Reliability Engineer" |
| **[Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 9 | Criticality classification (L1–L3) |
| **[Ch. 02 §A0–A4 + `REQ-AGN`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos)** | Art. 9, 14 | Autonomy level model A0–A4 + mandate + *intent declaration* |
| **[Ch. 03 agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic)** | Art. 9, 15 | Threat modelling with MITRE ATLAS + OWASP LLM Top 10 2025 |
| **[Ch. 04 — `ARC-014`/`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)** | Art. 14, 15 | Defensive architecture + agent as an isolated *principal* + *kill-switch* |
| **[Ch. 05 — `DEP-011..014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011)** | Art. 10, 15, 25, 55 | AI BOM + *pinning* + approved *providers* |
| **[Ch. 06 — Prompts as code](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#prompts-como-codigo)** | Art. 15, 17 | Versioning + review of *system prompts*, *skill files*, *agent files* |
| **[Ch. 07 US-19](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle)** | Art. 15, 17 | Secure pipeline + AI agents as *principals* with OIDC + audit |
| **[Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro)** | Art. 15, 55 | Runtime/inference hardening |
| **[Ch. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites)** | Art. 15, 55 | Continuous *eval suites* (regression, abuse, drift, A/B) |
| **[Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 17 | Release gate, pre-production validation |
| **[Ch. 12 US-13 + `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)** | Art. 12, 19, 72, 73 | Agentic telemetry + audit per tool + jailbreak detection |
| **[Ch. 13 (training)](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 4 | AI literacy per *role* |
| **[Ch. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle)** | Art. 17, 25, 26, 73 | Governance + contracting of AI *providers* + escalation |

---

## Simple Metric: Am I Aligned? {#métrica-simples-estou-alinhado}

These questions are a **technical** self-diagnosis — answering them does not issue the legal compliance judgement. If all of them can be answered YES, the technical core is aligned:

1. **Framing:** Do I know my role and the risk category?
2. **Risk Management:** Do I have a threat model that covers the adversarial vector (ATLAS)?
3. **Robustness (Art. 15):** Do I carry out adversarial testing / AI red teaming?
4. **Chain:** Do I have provenance and integrity of datasets and models?
5. **Logging:** Do I record inference events with adequate retention?
6. **Monitoring:** Do I have a post-market monitoring plan with drift detection?
7. **Incidents:** Can I report a serious incident within the Art. 73 deadlines?
8. **QMS:** Do my gates map to the elements of Art. 17?
9. **Documentation:** Do I have an Annex IV index + model card?
10. **Evidence:** Can I demonstrate all of this in an audit?

≥8/10 → Good technical maturity with respect to the AI Act (technical maturity, **not legal compliance**). `<`6 → Prioritise Art. 15 (robustness and cybersecurity), logging (Art. 12) and risk management (Art. 9).

> ⚠️ **Note:** this metric covers the **technical core**. Full compliance additionally requires data governance (Art. 10), human oversight (Art. 14), transparency (Art. 13/50) and conformity assessment, EU declaration of conformity, CE marking and registration (Art. 43, 47–49) - dimensions outside the SbD-ToE scope.

---

## Critical Note: Exception Management under the AI Act {#nota-crítica-gestão-de-exceções-no-ai-act}

The AI Act requires high-risk AI systems to comply with the requirements of Chapter III, Section 2 (Article 8(1)). Exceptions (deviations) must be formal and audited, with a documentary trail and appropriate approval. An **internal** exception does not change the legal obligation under the AI Act — it merely documents an accepted technical risk for the evidence dossier; the legal obligation remains.

What characterises an exception in SbD-ToE/AI Act:
- Formal deviation from a requirement (e.g. adversarial vector mitigated by a compensating measure while *retraining* is prepared)
- Formal approval, justification, TTL (Time-To-Live), remediation plan

Who approves (by criticality level):
- L1 (low risk): Tech Lead / AppSec Engineer
- L2 (medium risk): CISO / AI lead
- L3 (high-risk under the AI Act): AI governance + management (accountable)

Regulatory implication:
- Exceptions without formal approval compromise the evidence of risk management (Art. 9) and of the QMS (Art. 17)
- **Some situations can never be made exceptions** - first and foremost, any use that falls under the prohibited practices of Art. 5
- An audited trail is mandatory to demonstrate control to the authority

**Reference:** [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro) (exceptions addon) and [Ch. 14 - Governance](/sbd-toe/sbd-manual/governanca-contratacao/intro) (formalised exceptions).

---

## Next Steps {#próximos-passos}

1. **Legal framing:** Determine role and risk category (legal/compliance)
2. **Current technical audit:** Check [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) against the technical requirements of the AI Act
3. **Define the roadmap:** Sequence the phases according to context and risk category
4. **Coordinate with the domain:** Coordinate with data science, product and legal the dimensions outside the AppSec scope
5. **Implement and validate:** Iterate and demonstrate the **technical evidence** in an audit

Full documentation: see SbD-ToE chapters 01–14 for technical and operational detail.

---

## References {#referências}

- **SbD-ToE Manual:** Chapters 01–14 (technical detail by domain)
- **Cross-Check AI Act:** [Full normative analysis](/sbd-toe/cross-check-normativo/ai-act/intro)
- **AI Act:** Regulation (EU) 2024/1689
- **Reference Frameworks:** ISO/IEC 42001, ISO/IEC 23894, NIST AI RMF 1.0, MITRE ATLAS, OWASP ML Security Top 10, OWASP Top 10 for LLM Applications

---

**Version:** 1.0
**Date:** May 2026
**Note:** This playbook complements the [AI Act normative analysis](intro) with practical implementation.
