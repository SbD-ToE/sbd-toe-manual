---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 01
tags: [canon, maturidade, SAMM, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Classificação da Criticidade Aplicacional

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 01** do manual SbD-ToE e os requisitos de frameworks reconhecidas: **OWASP SAMM**, **OWASP DSOMM** e **SLSA**.

A prática de classificação da criticidade aplicacional é **fundacional para o modelo SbD-ToE**. Ela define **quando e com que intensidade os controlos de segurança devem ser aplicados**, suportando uma abordagem proporcional, rastreável e auditável.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                         | Práticas ou Objetos Cobertos                                  | Avaliação de Maturidade             |
|------------------|----------------------------------------------|----------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Governance → Risk Management                 | Classificação de risco por eixos, integração no SDLC           | **2 / 3**                           |
| OWASP DSOMM      | Risk, Security Requirements, Compliance      | Derivação de requisitos, rastreabilidade, decisão proporcional | **2 / 3** (média dos domínios)      |
| SLSA v1.0        | Supply Chain Risk Awareness                  | Definição proporcional de requisitos à criticidade             | **Nível 1 / 4**                     |

---

## 🧱 OWASP SAMM - Governance → Risk Management

| Nível | Descrição SAMM                                                           | Cobertura pelo Cap. 01                  |
|-------|--------------------------------------------------------------------------|------------------------------------------|
| 1     | Realiza-se classificação básica dos riscos das aplicações                | ✅ Modelo de eixos aplicável             |
| 2     | Integração com processos organizacionais e rastreabilidade               | ✅ Com suporte a versão e auditoria      |
| 3     | Análise quantitativa e retroalimentação contínua                         | ❌ Fora do âmbito do capítulo            |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Governance, Risk Management, Requirements

| Domínio                  | Níveis cobertos | Justificação técnica                                                   |
|--------------------------|----------------|------------------------------------------------------------------------|
| Risk Management          | 2 / 3          | Modelo de classificação estruturado e aplicado sistematicamente       |
| Security Requirements    | 2 / 3          | Permite derivação proporcional baseada em risco                       |
| Compliance Mapping       | 2 / 3          | Rastreabilidade a frameworks de referência presente                    |
| Governance & Metrics     | 1 / 3          | Não define KPIs quantitativos nem reporting formal                     |

> A estrutura proposta é compatível com práticas DevSecOps guiadas por risco.

---

## 🧱 SLSA - Supply Chain Levels for Software Artifacts

| Nível | Requisitos principais                   | Cobertura pelo Cap. 01         |
|-------|------------------------------------------|--------------------------------|
| 1     | Consciência de risco                     | ✅ Classificação por eixos      |
| 2     | Proveniência do software                 | ❌ Fora do âmbito               |
| 3     | Build controlado                         | ❌ Coberto noutros capítulos    |
| 4     | Cadeia totalmente verificável            | ❌ Coberto noutros capítulos    |

**🔐 Nível máximo suportado por este capítulo: SLSA 1 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

