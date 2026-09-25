---
id: operacoes
title: Operations (Ops)
sidebar_label: 🔧 Operations (Ops)
description: Responsibilities of Operations in SbD-ToE
tags: [operacoes, ops, runtime, incident-response, responsabilidades]
sidebar_position: 7
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/operacoes.md
  source_sha256: f8af5c2ee7d4403761f19c67dfda2d0bafa8aa0bf945cb3b24ee7f6ffe753fa1
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 45091c5c915986e045d6229c5cc5c00f136a6fa3cff79b7bb5fb9f1ed8cc260f
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: a23b4b0245c8f70929c4cf8742f32b3c89fb297f85b057d601b8189193ae0417
  glossary_keys: [chapter_role, framework_source_corpus, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: f2fb12fcf56dd55200e4a32b9af4adf8b4af08fab225182d4f60e2e11e863a0f
  translated_at: 2026-09-25T17:57:22Z
  reviewed_by: null
---

# Operations (Ops)

## Overview {#visão-geral}

Ops maintains **runtime integrity**, ensuring availability, patch application and coordinated incident response.  
Responsible for **continuous monitoring**, alert configuration and execution of response playbooks.

### Key Responsibilities {#responsabilidades-principais}
- Ensure secure execution at runtime
- Apply patches and regular updates
- Coordinate incident response (Ch. 12)
- Maintain availability and operational resilience

### Organisational Context {#contexto-organizacional}
Ops is the **front line in complying with NIS2** (incident response, 24-hour notification) and **DORA** (operational continuity and management of critical events).

## Regulatory Framework {#enquadramento-regulatório}

Front line in:
- **NIS2**: Incident notification within 24 hours
- **DORA**: Operational continuity and resilience

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 09 - Containers and Images {#cap-09---containers-e-imagens}
Keep the **container baseline** up to date and apply security patches to base images systematically.

### Ch. 11 - Secure Deployment {#cap-11---deploy-seguro}
Ensure **resilience in deploys**, coordinate rollback when necessary, and validate recovery procedures.

### Ch. 12 - Monitoring and Operations {#cap-12---monitorização-e-operações}
Configure **critical alerts with SLAs**, integrate alerts with incident response playbooks, correlate multi-source events, tune alerts to reduce false positives, coordinate incident response, work with metrics and maintain availability.

**User Stories:**
- [US-03: Critical alerts with SLAs](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-03---alertas-com-slas-definidos) - Timely incident response
- [US-10: Incident response playbooks](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-10---validação-e-tuning-de-alertas) - Fast, coordinated action
- [US-05: Event correlation](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-05---métricas-de-eficácia-mttdmttr) - Detection of suspicious patterns (with AppSec Engineer)
- [US-06: Alert validation and tuning](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-06---classificação-e-cobertura-de-domínios-de-monitorização) - Reduce false positives (with AppSec Engineer)

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
Take part in **incident simulations** (war room, tabletop exercises) to validate response processes.

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Document **incidents and lessons learned**, ensuring continuous improvement of response processes.

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 09 - Containers and Images](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
