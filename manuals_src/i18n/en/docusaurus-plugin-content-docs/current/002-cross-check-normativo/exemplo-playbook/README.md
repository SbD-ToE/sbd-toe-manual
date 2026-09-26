---
id: indice
title: Supporting Examples for the Playbooks
description: Reusable templates and practical examples for implementing SbD-ToE principles in any normative framework
tags: [playbook, exemplos, dora, nis2, iso27001, cra, gdpr, templates]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/exemplo-playbook/README.md
  source_sha256: 9fa78611b8a756c649ee5ca0e6a06dfce9bdd1b0e48b6fd3950cdf53eaff3035
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e97528d4d29b56dbb432448914d5c6dcc887a6287078e0c0a9e7f49d2f8640dc
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, framework_source_corpus, lifecycle_phase, maturity, normative_empirical, practitioner_manual, role_juridico, sbdtoe_sbd, traceability]
  glossary_sha256: 9053b641651a969706a59eb8e62170db5c2fc63079d736cd8d2e403901801db5
  translated_at: 2026-09-26T18:12:02Z
  stamped_at: 2026-09-26T18:32:19Z
  reviewed_by: null
---

# Supporting Examples for the Playbooks

## 📚 File Structure {#-estrutura-de-ficheiros}

This folder (`exemplo-playbook`) contains **example files** that show how to implement the principles that SbD-ToE prescribes.

**Important:** 
- These are examples, not prescriptions
- Each organisation must adapt them to its own context
- The examples are **reusable across multiple regulations** (DORA, NIS2, ISO 27001, etc.)

---

## 📖 Available Files {#-ficheiros-disponíveis}

### 1. **README.md** (This file) {#1-readmemd-este-ficheiro}
Overview, structure and instructions for use

---

### 2. **[Toolchain Options](exemplo-toolchain-options)** {#2-opções-de-toolchain}
**What it covers:** Tools for implementing IaC principles, logs, SCA/SAST

**Related to (SbD-ToE):**
- [Ch. 08 - IaC and Infrastructure](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

**Deliberate abstention covered:**
- ❌ The manual does NOT prescribe "Use Terraform" or "Use Splunk"
- ✓ Example: How to implement "IaC" with Terraform, CloudFormation or Helm
- ✓ Example: How to centralise logs with ELK, Datadog or Azure Sentinel

**When to use:**
- Assessing which technology stack to adopt
- Comparing tool options
- Validating that a choice implements SbD-ToE principles

**Deliverables:**
- Comparison of 3 options per dimension (IaC, Logs, SCA, SAST, CI/CD)
- Code examples
- Audit trail for each option

---

### 3. **[KPIs and Targets](exemplo-kpis-targets)** {#3-kpis-e-targets}
**What it covers:** KPIs and targets for different organisational profiles

**Related to (SbD-ToE):**
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

**Deliberate abstention covered:**
- ❌ The manual does NOT prescribe "Target: Zero critical vulns"
- ✓ Example: Fintech (small) - aggressive targets, short timeline
- ✓ Example: Bank (large) - conservative targets, long timeline
- ✓ Example: SME (distributed) - pragmatic targets

**When to use:**
- Setting targets for the organisation
- Communicating with executives ("Why not 100%?")
- Adjusting according to maturity

**Deliverables:**
- Visual KPI dashboards (per scenario)
- Target tables (per dimension)
- Target-setting process

---

### 4. **[RACI and Governance](exemplo-raci-governance)** {#4-raci-e-governance}
**What it covers:** RACI and governance structure

**Related to (SbD-ToE):**
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

**Deliberate abstention covered:**
- ❌ The manual does NOT prescribe "CISO reports to CTO" or "7 meetings/week"
- ✓ Example: Fintech (small) - lean RACI, fortnightly meetings
- ✓ Example: Bank (large) - structured RACI, multiple levels
- ✓ Example: SME (distributed) - hybrid RACI, remote communication

**When to use:**
- Designing the governance structure
- Defining responsibilities
- Structuring communication/meetings

**Deliverables:**
- Organisation charts (per scenario)
- RACI matrices (per activity)
- Meeting calendars
- Approval procedures

---

### 5. **[Incident Report](exemplo-relatorio-incidentes)** {#5-relatório-de-incidentes}
**What it covers:** Incident reporting template

**Related to (SbD-ToE):**
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

**Deliberate abstention covered:**
- ❌ The manual does NOT prescribe "Official DORA ITS template"
- ✓ Example: How to structure a report (what, when, how, who, impact, action)
- ✓ Example: Fields for traceability

**When to use:**
- Configuring an incident tool (Jira, ServiceNow, etc.)
- Aligning the team on the definition of an incident
- Preparing for a DORA audit

---

### 6. **05-exemplo-rto-rpo.md** *(next to be created)* {#6-05-exemplo-rto-rpomd-próximo-a-criar}
**What it covers:** Definition of RTO/RPO per app

**Related to (SbD-ToE):**
- [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Ch. 08 - IaC and Infrastructure](/sbd-toe/sbd-manual/iac-infraestrutura/intro)

**Deliberate abstention covered:**
- ❌ The manual does NOT prescribe "RTO: `<1h`" or "RPO: `<15min`"
- ✓ Example: How to define per L1/L2/L3 app
- ✓ Example: How to implement (backups, replicas, failover)

**When to use:**
- Designing the availability architecture
- Communicating criticality internally

---

### 7. **06-exemplo-roadmap-adaptado.md** *(next to be created)* {#7-06-exemplo-roadmap-adaptadomd-próximo-a-criar}
**What it covers:** Roadmaps adapted to different scenarios

**Related to (SbD-ToE):**
- [DORA Playbook](../dora/playbook) - Phases 0-5

**Deliberate abstention covered:**
- ❌ The manual does NOT prescribe "Phase 0 always 2 months"
- ✓ Example: Short timeline (Fintech: DORA urgency)
- ✓ Example: Long timeline (Bank: complexity + governance)
- ✓ Example: Pragmatic timeline (SME: resources)

**When to use:**
- Planning the implementation
- Communicating the executive timeline
- Adapting to the real context

---

### 8. **07-exemplo-politica-seguranca.md** *(next to be created)* {#8-07-exemplo-politica-segurancamd-próximo-a-criar}
**What it covers:** Security Policy template

**Related to (SbD-ToE):**
- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

**Deliberate abstention covered:**
- ❌ The manual does NOT prescribe a "Generic Security Policy"
- ✓ Example: Structure, minimum content, signature
- ✓ Example: Reference to SbD-ToE and DORA

**When to use:**
- Drafting an internal policy
- Validating essential content
- Preparing for Board approval

---

### 9. **08-exemplo-contrato-fornecedor.md** *(next to be created)* {#9-08-exemplo-contrato-fornecedormd-próximo-a-criar}
**What it covers:** Technical security clauses in contracts

**Related to (SbD-ToE):**
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
- [Ch. 05 - Dependencies, SBOM and SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

**Deliberate abstention covered:**
- ❌ The manual does NOT prescribe "Specific legal clauses"
- ✓ Example: Technical requirements (SbD compliance, training, etc.)
- ✓ Example: Response SLAs (incidents, remediation, etc.)

**When to use:**
- Negotiating with suppliers
- Including security requirements
- Aligning with DORA Articles 26-28

---

## 🔍 How to Find What Is Needed {#-como-encontrar-o-que-procura}

### "I need to choose tools" {#preciso-escolher-ferramentas}
→ **[Toolchain Options](exemplo-toolchain-options)**

### "How do I set security targets?" {#como-defino-targets-de-segurança}
→ **[KPIs and Targets](exemplo-kpis-targets)**

### "How do I structure governance?" {#como-estruturo-governança}
→ **[RACI and Governance](exemplo-raci-governance)**

### "How do I report incidents?" {#como-reporto-incidentes}
→ **[Incident Report](exemplo-relatorio-incidentes)**

### "How do I define RTO/RPO?" {#como-defino-rtorpo}
→ **RTO/RPO Example** *(to be created)*

### "How do I plan the implementation?" {#como-planejo-a-implementação}
→ **Adapted Roadmap Example** *(to be created)* + [**DORA Playbook**](../dora/playbook)

### "How do I write the policy?" {#como-escrevo-a-política}
→ **Security Policy Example** *(to be created)*

### "How do I close a secure contract?" {#como-fecho-um-contrato-seguro}
→ **Supplier Contract Example** *(to be created)*

---

## 📋 Usage Checklist {#-checklist-de-uso}

When using these examples:

- [ ] **Read the README** - Understand the purpose
- [ ] **Select the relevant example** - By context/abstention
- [ ] **Adapt to the context** - Do not copy directly
- [ ] **Validate with stakeholders** - GRC, Legal, Compliance
- [ ] **Test before implementing** - Validate the audit trail
- [ ] **Document decisions** - Why X was chosen over Y
- [ ] **Iterate** - Adjust according to lessons learned

---

## 🔗 Relationship with the Manual's Chapters {#-relação-com-capítulos-do-manual}

```
SbD-ToE Manual
├─ [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro) - Classificação de Aplicações
│  └─ Exemplo: 05-rto-rpo.md, 06-roadmap.md
├─ [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) - Requisitos de Segurança
│  └─ Exemplo: 07-politica-seguranca.md
├─ [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) - Dependências, SBOM e SCA
│  └─ Exemplo: 01-toolchain (SCA)
├─ [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) - IaC e Infraestrutura
│  └─ Exemplo: 01-toolchain (IaC options)
├─ [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) - Monitorização e Operações
│  └─ Exemplo: 01-toolchain (logs), 02-kpis, 04-incidentes
├─ [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) - Governança e Contratação
│  └─ Exemplo: 03-raci-governance.md, 07-politica.md, 08-contrato.md
└─ Playbook DORA
   └─ Exemplo: Todos (implementar princípios)
```

---

## ⚠️ Important Warnings {#️-avisos-importantes}

1. **These examples are illustrative**
   - Do not copy them directly
   - Adapt them to the legal, regulatory and operational context

2. **Consult specialists**
   - GRC/Compliance for policies
   - Legal for contracts
   - Security for architecture

3. **Test before using in production**
   - Validate the audit trail
   - Verify compliance with DORA
   - Confirm integration

4. **Update regularly**
   - DORA evolves (RTS/ITS)
   - Tools evolve
   - Best practices evolve

---

## 🔄 Update Process {#-processo-de-atualização}

These examples will be updated when:
- DORA RTS/ITS change
- New major version of SbD-ToE
- Feedback from real implementations
- Changes in best practices

**Next scheduled review:** June 2026

---

## 📞 Feedback {#-feedback}

If any of the following is found:
- ❓ Ambiguity in the examples
- 🐛 Technical error
- ✨ Suggestion for improvement
- 🔄 New example needed

**Contact:** [reserved for future releases]

---

**Version:** 1.0  
**Date:** November 2025  
**Next update:** June 2026
