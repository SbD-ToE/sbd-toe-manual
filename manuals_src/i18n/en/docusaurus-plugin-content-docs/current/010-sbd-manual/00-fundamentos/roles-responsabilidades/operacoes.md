---
id: operacoes
title: SecOps (Security Operations)
sidebar_label: 🔧 SecOps (Security Operations)
description: Responsibilities of SecOps (Security Operations) in SbD-ToE
tags: [operacoes, secops, runtime, incident-response, responsabilidades]
sidebar_position: 7
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/operacoes.md
  source_sha256: 68f8469ff5c0aedd8cf2e8371a57ceeb74e9f979e544aede890e4bc12620a9ab
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 0ab76865a3c4641afa13b35beec7d00d3669235e3e675ea0efe937c4b0ecbdc0
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [chapter_role, framework_source_corpus, role_secops, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 0c4cb135b66401d73e1986756948b09914e8a20264b8133e205d97c506454622
  translated_at: 2026-09-26T17:23:41Z
  reviewed_by: null
---

# SecOps (Security Operations)

## Overview {#visão-geral}

SecOps maintains **security at runtime**: detection, security alerts and coordinated incident response.  
Responsible for **continuous security monitoring**, alert configuration and execution of response playbooks. General operations — availability, routine patching, rollback — belong to [DevOps / SRE](devops-sre).

**Specialisations:** SecOps (IR), also called Incident Response; SecOps (SOC); SecOps (Incident Commander); and the security on-call. The availability on-call belongs to DevOps / SRE.

### Key Responsibilities {#responsabilidades-principais}
- Ensure the detection of security events at runtime
- Trigger the security patch when a vulnerability in running systems requires it
- Coordinate incident response (Ch. 12)
- Ensure incident notification within the regulatory deadlines

### Organisational Context {#contexto-organizacional}
SecOps is the **front line in complying with NIS2** (incident response, notification within 24h) and **DORA** (operational continuity and management of critical events).

## Regulatory Framework {#enquadramento-regulatório}

Front line in:
- **NIS2**: Incident notification within 24 hours
- **DORA**: Operational continuity and resilience

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 09 - Containers and Images {#cap-09---containers-e-imagens}
Track **vulnerabilities in running images** and trigger the security patch; maintaining the baseline belongs to DevOps / SRE.

### Ch. 11 - Secure Deployment {#cap-11---deploy-seguro}
Trigger the **rollback when a deploy introduces a security incident**; executing the rollback belongs to DevOps / SRE.

### Ch. 12 - Monitoring and Operations {#cap-12---monitorização-e-operações}
Configure **critical alerts with SLAs**, integrate alerts with incident response playbooks, correlate multi-source events, tune alerts to reduce false positives, coordinate incident response and work with detection and response metrics.

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
