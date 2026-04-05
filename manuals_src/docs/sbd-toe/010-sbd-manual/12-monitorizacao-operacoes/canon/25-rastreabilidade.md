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
| ACO-SLG — Security Event Logging, Audit Trail & Centralized Logging | Logging estruturado, eventos de segurança, audit trail, centralização |
| ACO-ITS — Integration Trust & Service-to-Service Security | Deteção de incidentes, resposta, integração com SIEM/SOAR |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF RV.1 | Identify and Confirm Vulnerabilities | ✅ Explícito | Logging e correlação como mecanismo de identificação | aplicacao_lifecycle (strong): US-01 - Logging estruturado + addon (medium): Logging Estruturado e Centralizado |
| CIS-7 | Continuous Vulnerability Management | ⚠️ Parcial | Monitoring adjacent; CIS cobre âmbito mais largo | addon (medium): Domínios e Abrangência da Monitorização |
| CIS-8 | Audit Log Management | ✅ Explícito | Logging estruturado e seguro com integridade | addon (medium): Logging Estruturado e Centralizado |
| CIS-18 | Penetration Testing | ✅ Explícito | Monitoring traceability de resultados e rastreabilidade | addon (medium): Monitorização como Suporte à Resposta |
| ASVS log_integrity_and_protection | Log integrity | ✅ Explícito | Segurança e integridade dos logs | addon (medium): Logging Estruturado e Centralizado > Segurança e integridade dos logs |
| ASVS security_event_logging_coverage | Security event logging | ✅ Explícito | Eventos mínimos obrigatórios e cobertura | aplicacao_lifecycle (strong): US-01 - Logging estruturado e eventos críticos |
| ASVS structured_logging_shape | Structured logging | ✅ Explícito | Estrutura recomendada dos eventos de log | addon (medium): Logging Estruturado e Centralizado > Estrutura recomendada dos eventos |
| ASVS error_handling_logging_hygiene | Error handling / logging hygiene | ⚠️ Parcial | Monitoring adjacent; sem unit dedicado | addon (medium): Logging Estruturado e Centralizado |
| ASVS logging_documentation | Logging documentation | ⚠️ Parcial | Monitoring presente; sem unit dedicado | addon (medium): Logging Estruturado e Centralizado |
| ASVS anti_automation | Anti-automation controls | ⚠️ Parcial | Monitoring adjacent; correlação de anomalias | addon (medium): Correlação e Deteção de Anomalias |
| DORA | Monitorização e resposta operacional | ✅ Explícito | Overlay regulatório publicado | requirements_catalog (strong): Catálogo OPS - Monitorização e Operações |
| NIS2 | Monitorização e conformidade | ✅ Explícito | Overlay regulatório publicado | requirements_catalog (strong): Catálogo OPS - Monitorização e Operações |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Modelos de maturidade — pendente de normalização formal

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
