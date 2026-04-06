---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 12
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Monitorização e Operações

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 12 - Monitorização e Operações**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

As práticas abordam logging estruturado, métricas de segurança, alertas, integração com resposta a incidentes, correlação de eventos e observabilidade contínua.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework     | Domínios Relevantes                  | Práticas Cobertas                                              | Avaliação de Maturidade        |
|---------------|---------------------------------------|------------------------------------------------------------------|--------------------------------|
| **SAMM v2.1** | Operations → Incident Management      | Logging, alertas, KPIs, integração com resposta                 | **3 / 3**                      |
| **SLSA v1.0** | Observability                         | Logging e métricas integradas                                   | **Nível 2 / 4**                |
| **DSOMM**     | Operations                            | Monitorização, deteção, alertas, IR, correlação                 | **5 / 5**                      |

---

## 🧱 OWASP SAMM - Operations → Incident Management

| Nível | Descrição SAMM                                  | Implementação no Cap. 12                          |
|-------|--------------------------------------------------|---------------------------------------------------|
| 1     | Logging básico e manual                          | ✅ Logging estruturado                             |
| 2     | Monitorização contínua e alertas                 | ✅ Alertas automatizados e dashboards              |
| 3     | Integração com resposta a incidentes             | ✅ Correlação e canal de resposta definido         |

**🧮 Maturidade atingida: 3 / 3**

---

## 🧱 OWASP DSOMM - Operations

| Domínio     | Nível | Justificação técnica                                              |
|-------------|-------|-------------------------------------------------------------------|
| Operations  | 5 / 5 | Cobertura completa: logging, deteção, correlação, integração IR   |

---

## 🧱 SLSA - Observabilidade

| Nível | Requisitos principais                                | Cobertura pelo Cap. 12                             |
|-------|------------------------------------------------------|----------------------------------------------------|
| 1     | Logging básico de build/test                         | ✅ Logging mínimo em pipelines                     |
| 2     | Logging com métricas e alertas                       | ✅ KPIs operacionais e deteção automatizada        |
| 3     | Observabilidade com integridade garantida            | ❌ Parcial - não aborda verificação criptográfica  |
| 4     | Telemetria auditável e controlada externamente       | ❌ Não aplicável neste contexto                    |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

