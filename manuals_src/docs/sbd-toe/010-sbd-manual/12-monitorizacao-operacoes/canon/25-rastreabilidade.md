---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 12: Monitorização e Operações"
description: Rastreabilidade das práticas de monitorização e resposta face a frameworks normativos com pilot formal
tags: [rastreabilidade, monitorizacao, logging, resposta, ssdf, asvs, cis, dora, nis2]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 12: Monitorização e Operações

Este capítulo define práticas de **logging estruturado, deteção de ameaças e resposta operacional** — a fundação de segurança contínua e visibilidade em runtime.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SLG — Security Event Logging, Audit Trail & Centralized Logging | Logging estruturado, eventos de segurança, audit trail, centralização |
| ACO-ITS — Integration Trust & Service-to-Service Security | Deteção de incidentes, resposta, integração com SIEM/SOAR |
| ACO-IVF — Input Validation, Safe Parsing & Controlled Failure | Diversificação caveated para filtragem de spam, atualização automática e capacidade adaptativa (`SP800-53-SI-8`, `SP800-53-SI-8.2`, `SP800-53-SI-8.3`) sem promover o capítulo a âncora primária |
| ACO-SPC — Secret Handling, Protected Configuration & Operational Identities | Diversificação caveated para proteção de configuração e telemetria de informação sensível (`CIS-3.6`, `CIS-3.13`, `SC-42.1`) sem promover o capítulo a âncora principal |

> **Nota Wave 2 ACO-IVF:** esta superfície é limitada aos rows autorizados `nist_sp800_53_rev5::SP800-53-SI-8`, `nist_sp800_53_rev5::SP800-53-SI-8.2` e `nist_sp800_53_rev5::SP800-53-SI-8.3`. A leitura continua **bounded** a filtragem operacional de conteúdo abusivo e atualização adaptativa, enquanto a âncora primária de `ACO-IVF` permanece em Cap. `06` e o scaffold de requisitos permanece em Cap. `02`.

> **Nota Wave 1 ACO-SPC:** esta superfície é limitada aos rows autorizados `cis_controls_v8_1_2::CIS-3.6`, `cis_controls_v8_1_2::CIS-3.13` e `nist_sp800_53_rev5::SP800-53-SC-42.1`. As variantes `SC-42`, `SC-42.2`, `SC-42.4` e `SC-42.5` permanecem fora da execução por serem non-core / privacy-only e não constituírem autoridade positiva de `ACO-SPC`.

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
| NIST SP800-53 | SP800-53-SI-8 — SP800-53-SI-8 | ✅ Semântico | NIST SI-8; Source: SP800-53-SI-8; Manual: Catálogo de Requisitos de Monitorização e Operações | requirements_catalog (strong): Catálogo de Requisitos de Monitorização e Operações |
| NIST SP800-53 | SP800-53-SI-8.1 — SP800-53-SI-8.1 | ✅ Semântico | O subcontrolo SI-8.1 encaixa na mesma disciplina de filtragem e monitorização contínua | requirements_catalog (strong): Catálogo de Requisitos de Monitorização e Operações |
| NIST SP800-53 | SP800-53-SI-8.2 — SP800-53-SI-8.2 | ✅ Semântico | O subcontrolo SI-8.2 cai no mesmo padrão de deteção e tratamento operacional de mensagens abusivas | requirements_catalog (strong): Catálogo de Requisitos de Monitorização e Operações |
| NIST SP800-53 | SP800-53-SI-8.3 — SP800-53-SI-8.3 | ✅ Semântico | O subcontrolo SI-8.3 mantém-se coberto por filtros, eventos e resposta operacional contínua | requirements_catalog (strong): Catálogo de Requisitos de Monitorização e Operações |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco determina âmbito e profundidade da monitorização
- **Cap. 02 / 03** — requisitos e ameaças que devem ser detetáveis via logging
- **Cap. 07** — geração de logs e rastreabilidade nos pipelines CI/CD
- **Cap. 09** — observabilidade e execução segura em ambientes containerizados
- **Cap. 14** — suporte à auditoria e validação contínua de exceções operacionais
