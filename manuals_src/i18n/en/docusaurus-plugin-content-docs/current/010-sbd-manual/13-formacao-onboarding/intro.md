---
id: intro
title: Training and Upskilling
description: Strategies and practices to ensure that teams, profiles and stakeholders are prepared to apply Security by Design
tags: [formacao, capacitacao, onboarding, champions, aprendizagem, DSOMM, SAMM, ]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/intro.md
  source_sha256: 1a249a710fe66831d4f8b70eec77124fd12f9abe904ba5a4167876261d3bc13c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 8c0e13fe839372cac91f6eca036ad41be434c4df5d36d13a7a3ebafe7f000fb5
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [basilar, capacitacao, chapter_role, cycle_iteration, lifecycle_phase, mapping, maturity, practitioner_manual, programme_line, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: bb1601a52c4ddd27ee6b026c2a74f89efec9bdcc2f36bb5361c4dbb2081614d9
  translated_at: 2026-09-26T11:44:30Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="organizacional" title="Capítulo Organizacional">

This chapter is considered **organisational** in the *Security by Design - Theory of Everything (SbD-ToE)* model.
Its function is to **ensure the adoption, governance and sustainable evolution** of the security practices defined in the foundational and operational chapters.

The organisational chapters establish the human and procedural structure that makes it possible to consolidate the SbD-ToE in the organisation.
Without these elements, security by design becomes ad hoc and dependent on individuals, losing the **organisational consistency and resilience** needed for long-term maturity.

</ChapterTypeCallout>


# Training and Upskilling

**Security training** is the link that turns technical prescriptions into operational practice, for example:  
- **Ch. 12 - Monitoring and Operations** guarantees visibility at runtime, but depends on trained teams to interpret alerts and react.  
- **Ch. 14 - Governance and Contracting** defines organisational commitments, but is only effective if the teams have the knowledge to meet them.  

To ensure that "security is lived and breathed" and is part of the organisation's DNA, it is essential to cultivate that body. This chapter defines how Security becomes something intrinsic to the organisation through:

- Onboarding programmes for new members.  
- Continuous training for Dev, QA, DevOps, AppSec, Management.  
- Security *champions* programmes.  
- Practical exercises (labs, CTFs, simulations).  
- Training effectiveness KPIs.  
- Integration into backlog and individual development plans.  

👉 What makes this chapter exceptional is that it places **people** as the vector of resilience: an organisation may have secure pipelines and defined requirements, but if the engineers, testers, DevOps or managers have no training, security, in practice, degrades.

The extensive use of automated tools throughout the lifecycle
does not reduce the need for human understanding of the processes,
their limits and the associated responsibilities.

The training defined in this chapter ensures that all the parties involved
understand how the adopted operating model really works,
regardless of the degree of automation in place.

---

## 🧪 2. Practical prescription {#-2-prescrição-prática}

- **What to do:** continuous training plan, onboarding with security, labs, effectiveness metrics.  
- **How:** LMS with training tracks per profile, champions per team, periodic reviews.  
- **When:** initial onboarding, quarterly cycles, whenever new controls are introduced.  
- **Why:** reduce human error, create a security culture, meet regulatory requirements.  

---

## 👥 Roles involved {#-papéis-envolvidos}

- **Developer** → receive practical training in SAST, dependencies, IaC.  
- **QA** → upskilling in fuzzing, regressions, validation.  
- **AppSec Engineer** → produce content, deliver training, manage champions.  
- **DevOps / SRE** → upskilling in secure pipelines and monitoring.  
- **Executive Management** → training in risk acceptance and governance.  
- **Security Champion (HR)** → manage the LMS, onboarding and individual plans.  
- **Security Champion** → evangelise and support teams.  
- **Suppliers / Third Parties** → suppliers with access must receive minimum training.  

---

## 🔗 Integration in the cycle {#-integração-no-ciclo}

Upskilling must be present throughout the cycle:  
- **Planning:** definition of training requirements for each profile.  
- **Development:** labs and specific tracks integrated into the backlog.  
- **Testing/Release:** validation exercises linked to secure practices.  
- **Operations:** incident simulations for response training.  
- **Audit:** collection of effectiveness metrics (KPIs, internal audits).  

👉 In this way, training stops being an “extra” and becomes an **intrinsic part of the SDLC**.

---

## 📊 Organisational traceability {#-rastreabilidade-organizacional}

- **Upskilling KPIs**: completion rate, knowledge retention, practical application in audits.  
- **Effectiveness metrics**: reduction of repeated findings in code, decrease in incidents attributed to human error.  
- **Governance**: periodic reports to GRC and integration into individual performance objectives.  
- **Compliance**: direct mapping to SSDF PO.3/PO.7 and SAMM PO2/PO3, guaranteeing normative coverage.  

---

## 🏁 Conclusion {#-conclusão}

Training is what **turns processes into culture**.  
- Without secure onboarding, the organisation accumulates basic failures.  
- Without continuous training, practices become obsolete.  
- Without champions, teams are left without security leadership.  
- Without metrics, there is no continuous improvement.  

👉 That is why this chapter is considered **foundational**: it is here that it is guaranteed that the SbD-ToE is not merely documentation, but living practice.

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy | Mandatory? | Application | Minimum content |
|----------|--------------|-----------|-----------------|
| [Security Training and Upskilling Policy](/sbd-toe/assets/policies/policy-formacao-seguranca) | Yes | Security Champion (HR) + AppSec Engineer | Annual plan, LMS, periodic review |
| [Security Training and Upskilling Policy — Onboarding](/sbd-toe/assets/policies/policy-formacao-seguranca) | Yes | Security Champion (HR) + Executive Management | Mandatory training at the start |
| [Training and Upskilling Policy — Security Champions](/sbd-toe/assets/policies/policy-formacao-seguranca) | Recommended | AppSec Engineer + Developer | Formal programme with clear roles |
| [Security Governance KPIs Policy](/sbd-toe/assets/policies/policy-kpis-governacao) | Yes | GRC / Compliance | KPIs, effectiveness, audit reports |
| [Training and Upskilling Policy — Practical Exercises](/sbd-toe/assets/policies/policy-formacao-seguranca) | Recommended | AppSec Engineer + QA + Developer | Labs, CTFs, simulations |

In the printed version, consult the **Manual's Organisational Policies Annex**, where these policies are consolidated on a cross-cutting basis.

---
