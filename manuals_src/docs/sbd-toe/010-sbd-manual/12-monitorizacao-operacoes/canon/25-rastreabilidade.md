---
id: rastreabilidade
title: Rastreabilidade — Capítulo 12: Monitorização e Operações
description: Rastreabilidade das práticas de monitorização e resposta face a frameworks normativos com pilot formal
tags: [rastreabilidade, monitorizacao, logging, resposta, ssdf, asvs, cis, dora, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 12: Monitorização e Operações

Este capítulo define práticas de **logging estruturado, deteção de ameaças e resposta operacional** — a fundação de segurança contínua e visibilidade em runtime.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-ITS — Incident, Triage & Security Response | Deteção de incidentes, resposta, playbooks, triage |
| ACO-SLG — Security Lifecycle & Governance | Métricas operacionais (MTTD/MTTR), governação contínua |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF RV.1 | Identify and Confirm Vulnerabilities | ✅ Explícito | Logging e correlação como mecanismo de identificação |
| CIS-7 | Continuous Vulnerability Management | ⚠️ Parcial | Monitoring adjacent; CIS cobre âmbito mais largo |
| CIS-8 | Audit Log Management | ✅ Explícito | Row publicada; logging estruturado e seguro |
| CIS-18 | Penetration Testing | ✅ Explícito | Monitoring traceability de resultados |
| ASVS log_integrity_and_protection | Log integrity | ✅ Explícito | Row publicada |
| ASVS security_event_logging_coverage | Security event logging | ✅ Explícito | Row publicada |
| ASVS structured_logging_shape | Structured logging | ✅ Explícito | Row publicada |
| ASVS error_handling_logging_hygiene | Error handling / logging hygiene | ⚠️ Parcial | Monitoring adjacent |
| ASVS logging_documentation | Logging documentation | ⚠️ Parcial | Monitoring presente |
| ASVS anti_automation | Anti-automation controls | ⚠️ Parcial | Monitoring adjacent |
| DORA | Monitorização e resposta operacional | ✅ Explícito | Overlay regulatório publicado |
| NIS2 | Monitorização e conformidade | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Operations → Incident Management |
| OWASP DSOMM | Operations (Logging, Monitoring, Alert Tuning, IR Integration) |
| BSIMM13 | Deployment (TDI1.1, TDI2.2, IR1.4) |

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco determina âmbito e profundidade da monitorização
- **Cap. 02 / 03** — requisitos e ameaças que devem ser detetáveis via logging
- **Cap. 07** — geração de logs e rastreabilidade nos pipelines CI/CD
- **Cap. 09** — observabilidade e execução segura em ambientes containerizados
- **Cap. 14** — suporte à auditoria e validação contínua de exceções operacionais
