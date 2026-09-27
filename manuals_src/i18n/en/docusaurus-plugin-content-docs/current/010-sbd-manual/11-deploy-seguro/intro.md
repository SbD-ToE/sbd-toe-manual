---
id: intro
title: Secure Deployment
description: Principles and controls to ensure a secure, validated and traceable deployment process in production environments
tags: [deploy, seguranca, producao, rollback, gates, sdlc]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/intro.md
  source_sha256: f697bb3cc8987c761dbacd610ccc8a5047117a11d09cd463934625720fa9d6e1
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 537a07a5bb266700032736c8411085679adf48cf23641a8300ac2e090d3c6756
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [audit_trail, basilar, chapter_role, como_fazer, cycle_iteration, lifecycle_phase, papel_suporte, practitioner_manual, provenance, role_tech_lead, sbdtoe_sbd, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 2f72bf25038fa5c0520ab79fd6e18609ad7e5dfbf2ae2a150befa1773c40d3f0
  translated_at: 2026-09-27T07:53:54Z
  stamped_at: 2026-09-27T07:53:54Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="operacional" title="Capítulo Operacional">

This chapter is considered **operational** in the *Security by Design – Theory of Everything (SbD-ToE)* model.
Its function is to **apply, automate and validate** practices defined in the foundational chapters, ensuring their continuous and measurable execution.

The operational chapters implement the SbD-ToE in specific technical contexts, translating foundational prescriptions into practices of **verifiable execution**, with **auditable evidence** throughout the software lifecycle.

</ChapterTypeCallout>

# Secure Deployment

## Context and objective {#contexto-e-objetivo}

The moment of *deployment* is, by nature, one of the most delicate in the entire lifecycle. Until the last instant, the application may be intact, tested and audited; but if the transition to production is carried out insecurely, the earlier investment loses its value.

The evidence gathered in incident reports and analyses shows that significant compromises frequently occur in the *release* and initial operation phase, through failures of traceability, absence of *rollback*, excessive permissions, poor secrets management or promotion of artefacts without verifiable provenance.

This chapter is not limited to “running the pipeline”. It seeks to establish practices that make each *deployment* **auditable, reversible and proportional to the application's risk**.  
The security of the *deployment* is also governance: it translates into the ability to explain, before an audit or an incident, **who decided**, **what was approved**, **what evidence supported the decision** and **how the integrity of what reached production was guaranteed**.

👉 This chapter complements:
- **Secure CI/CD** - where the integrity of the *build*, technical traceability and control of the pipeline are guaranteed.  
- **Monitoring and Operations** - where the detection of anomalies, incident response and validation at *runtime* are covered.

---

## 🧭 What it covers technically {#-o-que-cobre-tecnicamente}

The technical scope of secure deployment includes, at least, the following axes:

- Formal approval and automatic *release* *gates*, with criteria defined by severity and criticality (L1–L3).  
- Promotion only from signed artefacts, with verifiable provenance and an associated SBOM.  
- Functional and security validation in *staging* before promotion.  
- Rigorous management of the credentials and secrets used at the moment of *deployment* (least privilege, short duration, auditing).  
- Secure *rollback*, configured and tested periodically.  
- *End-to-end* traceability, making it possible to trace each incident back to the original *commit* and artefact.  
- Post-*deployment* monitoring, to assess health and integrity in good time and support containment decisions.

These elements must be applied as a **coherent set of controls**: the robustness of the process results from the complementarity between prevention (*gates* and provenance), detection (monitoring), containment (*rollback* and *feature flags*) and audit (traceability and evidence).

---

## Automation and Governance in Deployment {#-automação-e-governação-no-deploy}

Secure deployment combines **extensive automation** with **explicit governance**, distinguishing between:

### Deterministic Decisions (Sovereign Automation) {#decisões-determinísticas-automação-soberana}

When criteria are **objective, reproducible and context-free**, automation may operate without human intervention:

- **Technical gates**: SAST detects a critical CVE → automatic block
- **Provenance**: Invalid artefact signature → automatic rejection
- **Automatic rollback**: Error metric >threshold → immediate rollback
- **Secret scanning**: Credential detected → build interrupted

**Principle**: Deterministic automation **may operate without human approval** if the criteria are formally defined and versioned.

### Non-Deterministic Decisions (Mandatory Governance) {#decisões-não-determinísticas-governação-obrigatória}

⚠️ **CRITICAL**: Non-deterministic automation **MUST NOT** operate without human governance.

When decisions involve **context, trade-offs or heuristics**, they require human validation and traceability:

- **Exceptions to findings**: Non-applicable CVE → AppSec approves + justification + time validity
- **Go/no-go approval**: Residual risk accepted → Product Owner approves + evidence
- **Database rollback**: Migration reversible but with data loss → SRE + Management decide

**Principle**: Every non-deterministic decision requires:
- **Who** (responsible role)
- **When** (timestamp + validity)
- **Why** (technical justification)
- **Evidence** (auditable documentation)

**Principle**: Non-deterministic decisions **MUST NOT** be automated without human validation, approval and traceability. Automation may **assist**, but never **decide alone**.

### Automation Guardrails {#guardrails-de-automação}

Even automated decisions have **explicit limits** for irreversible actions:

| Action | Limit | Reason |
|------|--------|-------|
| Automatic rollback | Up to version N-1 only | Prevent cascading rollbacks |
| Data purge | Always manual + approval | Irreversible |
| Permission changes | Always manual + review | High lateral impact |
| Secret injection | Approved environments only | Prevent leakage |

**Principle**: Automation **MUST NOT** execute irreversible actions or actions with critical lateral impact without human intervention. Even in deterministic contexts, high-risk actions require approval.

---

## 🔐 Exception Management {#-gestão-de-exceções}

Exceptions to automatic gates (e.g. non-applicable CVE, SAST false positive) follow a formal process:

1. **Exception template** (versioned in the repo):
   ```yaml
   exception_id: EX-2026-001
   finding_id: SAST-SQL-001
   justification: "Query parametrizada, não-vulnerável"
   approved_by: "AppSec Engineer (email@example.com)"
   approved_date: "2026-01-04"
   expiration_date: "2026-03-05"  # Tecto da Política 05 §7 (p. ex. 60 dias em L2, Low/Medium)
   evidence: "link/to/code-review-PR-123"
   ```

2. **Approver by severity**:
   - CRITICAL: AppSec Engineer + Executive Management
   - HIGH: AppSec Engineer
   - MEDIUM: Tech Lead

3. **Time validity**: Exceptions expire automatically (ceilings of Policy 05 §7: L1 90 days; L2 60 days (Low/Medium) and 30 days (High); L3 30 days (Low/Medium) and 14 days (High); Critical 7 days with a remediation plan, not acceptable at L3)

4. **Reassessment**: Before expiry, a new analysis is mandatory

---

## 🧪 Practical prescription {#-prescrição-prática}

What distinguishes mature organisations is not only *what* they do at *deployment*, but **how they operationalise the process as a repeatable mechanism of validation and risk containment**, with objective evidence.

- **What to do**  
  Ensure that all *deployments* occur only from trusted artefacts, pass through *gates* and validations in *staging*, and have an operational *rollback* ready.

- **How to do it**  
  Automate pipelines with versioned configuration, apply the principle of least privilege, rehearse *rollback* at a defined cadence and integrate *deployment* telemetry with monitoring and incident response.

- **When**  
  At each *release*, on relevant infrastructure/configuration changes and whenever an incident requires containment or rollback.

- **Why**  
  Because *deployment* is the point where a failure can have an immediate impact on availability, integrity and exposure. These practices align with reference controls (e.g. NIST SSDF in validation and verification; SLSA in provenance), and support the typical demands of frameworks and cybersecurity obligations applicable to software in production.

---

## 👥 Roles involved {#-papéis-envolvidos}

No secure *deployment* is the responsibility of a single profile. The practice requires cross-cutting coordination:

- **Dev** → ensures that the artefact is ready, versioned and documented.  
- **QA/Testing** → runs functional and security validations in *staging*.  
- **AppSec** → defines *gates*, criteria and the exceptions process with traceability and time validity.  
- **DevOps/SRE** → runs pipelines, prepares *rollback* and ensures technical traceability and evidence.  
- **Product Owner** → takes the final *go/no-go* decision and documents acceptance of residual risk.

This matrix is not optional: it is what guarantees that each *deployment* is simultaneously **technical and governed**, capable of withstanding operational failures and regulatory scrutiny.

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy | Mandatory? | Application | Minimum content |
|----------|--------------|-----------|-----------------|
| [Secure Deployment Policy](/sbd-toe/assets/policies/policy-deploy-seguro) | Yes | DevOps/SRE + AppSec | Promotion only of signed and traceable artefacts; minimum validations; evidence |
| [Release Approval Policy](/sbd-toe/assets/policies/policy-aprovacao-release) | Yes | Product Owner + AppSec | Formal *gates*; criteria by criticality; recorded, time-limited exceptions |
| [Rollback Policy](/sbd-toe/assets/policies/policy-rollback) | Yes | DevOps/SRE | *Rollback* defined by type, tested periodically, with evidence |
| [Secure Deployment Policy — Validation in Staging](/sbd-toe/assets/policies/policy-deploy-seguro) | Recommended | QA/Testing | Functional + security validation before promotion; controlled data |
| [Post-Deployment Monitoring Policy](/sbd-toe/assets/policies/policy-monitorizacao-pos-deploy) | Yes | DevOps/SRE | Metrics/alerts; correlation with *deployment* events; response process |

In the printed version, consult the **Manual's Organisational Policies Annex**, where these policies are consolidated on a cross-cutting basis.
