---
id: intro
title: Governance and Contracting
description: Structures, policies and practices to ensure organisational governance, supplier integration and transparency in the SbD-ToE cycle
tags: [governanca, contratacao, fornecedores, excecoes, rastreabilidade, conformidade, KPIs]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/intro.md
  source_sha256: 6eacb0e2283482ee354854b5fcecf834a7615185596701f2e5b22a6e0d90fe0a
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 648dbd3b8b6f4b22c0eb4375d942c9636cdb00a0b6bc08267814afcdfe74e8f7
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [audit_trail, basilar, chapter_role, como_fazer, cycle_iteration, layer, maturity, mcp_reading_normativa, papel_suporte, practitioner_manual, role_juridico, role_procurement, sbdtoe_sbd, traceability, transversal, validation_evaluation, verification_taxonomy]
  glossary_sha256: 4a37a34fe44061e28d79b0330d6c818d9e6bae1140d0f531388ece1a541da66f
  translated_at: 2026-09-26T17:23:55Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="organizacional" title="Capítulo Organizacional">

This chapter is considered **organisational** in the *Security by Design - Theory of Everything (SbD-ToE)* model.
Its function is to **ensure the adoption, governance and sustainable evolution** of the security practices defined in the foundational and operational chapters.

The organisational chapters establish the human, procedural and decision-making structure
that makes it possible to consolidate the SbD-ToE in the organisation.
Without these elements, security by design becomes ad hoc and dependent on individuals,
losing the **organisational consistency, authority and resilience** needed for long-term maturity.

</ChapterTypeCallout>


# Governance and Contracting

This chapter plays an **exceptional and foundational** role in the SbD-ToE.
Whereas earlier chapters prescribe *what* must be done at the technical level,
it is here that it is defined **how those practices become mandatory, visible,
auditable and governed** at the organisational level.

This chapter explicitly establishes the **governance and authority model** that frames all the security practices of the SbD-ToE, defining **who decides**, **with what legitimacy**, **under what conditions** and **with what evidence**.

It provides the structure to **unify the dispersed efforts** of technical teams, ensuring that security is controlled as an organisational responsibility, and introduces formal mechanisms of **exceptions**, **contracting**, **traceability**
and **measurement**, which turn security from a local exercise into a **system of corporate governance and accountability**, through:

- Definition of **formal governance models** for security.  
- An explicit process of **exception management and risk acceptance**, with recording and approval.  
- Mandatory integration of **security contractual clauses** in procurement and outsourcing.  
- **Continuous supplier validation** (audits, due diligence).  
- **Organisational traceability**: a consolidated view of practices per project.  
- Definition, collection and analysis of **governance KPIs** (exceptions, incidents, training coverage, etc.).  

In highly automated contexts, the organisation must explicitly define which types of decisions may be executed automatically, what their limits are and who retains final responsibility for their effects.

Delegating execution to processes or systems is always a conscious, documented and revocable organisational decision.

👉 It is this chapter that makes it possible to answer, objectively and defensibly, the critical question:  
*“Can the organisation demonstrate, with evidence, what is being done in security by all teams and suppliers?”*

---

## 🧪 2. Practical prescription {#-2-prescrição-prática}

- **What to do:**  
  - Create a **formal and approved** security governance model.  
  - Establish an **explicit flow** of exceptions and risk acceptance - canonical process in [`addon/12-processo-excecoes.md`](./addon/processo-excecoes).
  - Integrate **SbD-ToE contractual clauses** with suppliers and partners.  
  - Define audits and mechanisms of **continuous validation of third parties**.  
  - Collect, analyse and report **governance KPIs** systematically.  

- **How to do it:**  
  - Through governance documents **approved by management**.  
  - Using a **GRC** tool to track exceptions, decisions and metrics.  
  - Involving legal and procurement in the contracting processes.  
  - Ensuring **periodic reporting** to management and decision-making bodies.  

- **When:**  
  - In all new projects and contracting processes.  
  - Whenever there are exceptions to the prescribed practices.  
  - In regular (e.g. quarterly) governance and review cycles.  

- **Why:**  
  - Turn security into an **institutionalised and governed practice**.  
  - Make the state of adoption **visible, measurable and auditable**.  
  - Ensure regulatory compliance (ISO 27001, NIS2, SSDF, among others).  

---

## 👥 Roles involved {#-papéis-envolvidos}

Effective governance requires clearly defined roles, with proportional authority and explicit responsibilities.

- **Developer** → records exceptions and applies the agreed practices.  
- **AppSec Engineer** → validates exceptions and oversees traceability.  
- **DevOps / SRE** → ensures practical application in pipelines and deploy.  
- **Executive Management** → approves residual risk and governs organisational adoption.  
- **Legal + Procurement** → integrates security clauses into contracts.  
- **GRC / Compliance** → collects evidence, manages metrics and audits.  

👉 Each role exercises authority **derived from the defined governance model**
and has **associated user stories** in the `aplicacao-lifecycle.md`.

---

## 🔗 Integration in the cycle {#-integração-no-ciclo}

Governance acts as a **horizontal and cross-cutting** layer throughout the SbD-ToE cycle:

- **Planning:** definition of clauses, policies and metrics.  
- **Execution:** recording of exceptions, contractual integration, continuous reporting.  
- **Validation:** supplier audits, verification of KPIs.  
- **Operations:** integration with incidents and monitoring.  
- **Organisational audit:** consolidated evidence of adoption per chapter.  

The existence of automated technical mechanisms does not, in itself, create authority, nor does it replace the governance models defined here.

---

## 📊 Organisational traceability {#-rastreabilidade-organizacional}

Effective governance requires complete and consistent traceability:

- **Exceptions recorded and approved** in a GRC tool.  
- **Contractual clauses tracked** in supplier contracts.  
- **KPIs consolidated** in an organisational dashboard
  (e.g. % of teams with champions, no. of approved exceptions, mean time to resolution).  
- **Explicit linkage to regulatory frameworks**
  (ISO, NIS2, SSDF) ensures completeness and compliance.  

---

## 🏁 Conclusion {#-conclusão}

This chapter is the one that **closes and legitimises the SbD-ToE cycle**:

- It turns isolated practices into a **governed and auditable organisational process**.  
- It gives management **authority, visibility and transparency**.  
- It makes it possible to **measure real effectiveness** through KPIs.  
- It explicitly integrates security into **suppliers and contracts**.  

👉 Without this chapter, the SbD-ToE remains limited to local technical practice.  
👉 With it, it becomes an **explicit, defensible and sustainable
system of organisational governance**.

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy | Mandatory? | Application | Minimum content |
|----------|--------------|-----------|-----------------|
| [Security Exception Management Policy](/sbd-toe/assets/policies/policy-gestao-excecoes) | Yes | AppSec Engineer + Executive Management | Formal request, approval and deadline flow |
| [Secure Contracting Policy](/sbd-toe/assets/policies/policy-contratacao-segura) | Yes | Legal + Procurement | SbD-ToE clauses, continuous validation |
| [Organisational Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional) | Yes | GRC / Compliance | Centralised register, dashboards |
| [Secure Contracting Policy — Supplier Audit](/sbd-toe/assets/policies/policy-contratacao-segura) | Recommended | Procurement + AppSec Engineer | Periodic security audits |
| [Security Governance KPIs Policy](/sbd-toe/assets/policies/policy-kpis-governacao) | Yes | GRC / Compliance + Executive Management | Metrics, reports, objectives |

In the printed version, consult the **Manual's Organisational Policies Annex**,
where these policies are consolidated on a cross-cutting basis.
