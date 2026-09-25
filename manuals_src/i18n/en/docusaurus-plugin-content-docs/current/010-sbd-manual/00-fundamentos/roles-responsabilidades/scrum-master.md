---
id: scrum-master
title: Scrum Master / Team Lead
sidebar_label: 🧭 Scrum Master / Team Lead
description: Responsibilities of the Scrum Master/Team Lead in SbD-ToE
tags: [scrum-master, team-lead, agile, responsabilidades]
sidebar_position: 9
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/scrum-master.md
  source_sha256: b67181e2c8f99ee9d27a2aa015c985b836a36ba6d931efe9bbbe2748ba5ed5d8
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 035e878f41eac3c17c4087cded5d41d9468fac4cc10f9267119b45924aac7f62
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 1bfef9a72816fbf492eb0960150a7457c7572375ed258eed99a7d94ef48cf520
  glossary_keys: [capacitacao, chapter_role, cycle_iteration, discipline, sbdtoe_sbd, threat, traceability]
  glossary_sha256: b9429fe07fecd6b5e3e15da5591f2992106908ba95b15dd4ceb8eb7915373d48
  translated_at: 2026-09-25T17:10:46Z
  reviewed_by: null
---

# Scrum Master / Team Lead

## Overview {#visão-geral}

The Scrum Master/Team Lead is the **guardian of agile discipline**.  
The role ensures that security is not relegated to "when there is time" but **integrated into the teams' daily planning and execution**.

### Key Responsibilities {#responsabilidades-principais}
- Facilitate the integration of security into the agile cycle
- Remove blockers that hinder the implementation of secure practices
- Promote discipline in applying review checklists
- Moderate threat modelling sessions

### Organisational Context {#contexto-organizacional}
Help operationalise the requirement for **executive governance over digital security** set out in NIS2 and DORA, ensuring that teams act according to defined processes.

## Regulatory Framework {#enquadramento-regulatório}

Operationalises:
- **NIS2** and **DORA**: Implementation of executive governance over security practices
- Translates organisational policies into concrete actions in the sprint

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 01-02 - Classification and Requirements {#cap-01-02---classificação-e-requisitos}
Facilitate **discussions on criticality and requirements**, ensuring that the whole team understands the risk context. Review the classification on critical integrations or relevant changes.

**User Stories:**
- [US-02: Review on critical changes](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-02---revisão-por-alteração-relevante) - Update controls and traceability (with Software Architects)

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}
**Moderate threat modelling sessions**, create the initial threat model with DFDs and STRIDE/LINDDUN, and ensure participation of the whole team.

**User Stories:**
- [US-01: Initial threat model](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-01---criação-do-modelo-de-ameaça) - Risks visible from the start (with Software Architects)

### Ch. 06 - Secure Development {#cap-06---desenvolvimento-seguro}
Ensure that **every PR is reviewed against a mandatory security checklist**, preventing vulnerabilities and keeping a compliance record.

**User Stories:**
- [US-01: Security checklist in PRs](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-01---guidelines-de-desenvolvimento-seguro) - Prevent vulnerabilities

### Ch. 06-07 - Development and CI/CD {#cap-06-07---desenvolvimento-e-cicd}
Ensure that **secure practices enter sprint planning**, with a DoD that includes security criteria that can be validated.

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
Promote **upskilling and continuous training**, support a security culture, and remove impediments to learning time.

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Ch. 06 - Secure Development](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
