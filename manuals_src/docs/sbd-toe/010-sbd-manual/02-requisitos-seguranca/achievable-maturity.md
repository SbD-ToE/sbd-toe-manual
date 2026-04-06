---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 02
sidebar_position: 10
tags: [canon, maturidade, SAMM, DSOMM, SLSA]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Requisitos de Segurança

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 02** do manual SbD-ToE e os requisitos de frameworks reconhecidas: **OWASP SAMM**, **OWASP DSOMM** e **SLSA**.

A definição e validação de requisitos de segurança é um **pilar central na engenharia de software seguro**. Este capítulo fornece os mecanismos para garantir que os requisitos são proporcionais ao risco, rastreáveis, testáveis e auditáveis.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                            | Práticas ou Objetos Cobertos                                        | Avaliação de Maturidade             |
|------------------|--------------------------------------------------|----------------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Design → Security Requirements                  | Requisitos proporcionais, rastreáveis, com validação formal         | **2 / 3**                           |
| OWASP DSOMM      | Requirements, Architecture, Verification        | Catálogo validado, derivação por risco, critérios de aceitação      | **2 / 3** (média dos domínios)      |
| SLSA v1.0        | Build, Verification, Criteria Definition         | Definição de critérios de aceitação com base em requisitos          | **Nível 1 / 4**                     |

---

## 🧱 OWASP SAMM - Design → Security Requirements

| Nível | Descrição SAMM                                                                 | Cobertura pelo Cap. 02                      |
|-------|----------------------------------------------------------------------------------|----------------------------------------------|
| 1     | Definir requisitos de segurança mínimos                                         | ✅ Catálogo estruturado por domínio          |
| 2     | Requisitos definidos com base em riscos                                         | ✅ Derivação por níveis L1–L3                |
| 3     | Requisitos ligados a métricas e controlos de eficácia                          | ❌ Fora do âmbito imediato                   |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Requirements, Architecture, Verification

| Domínio                  | Níveis cobertos | Justificação técnica                                                    |
|--------------------------|----------------|-------------------------------------------------------------------------|
| Requirements             | 2 / 3          | Requisitos testáveis, rastreáveis e validados                          |
| Architecture             | 2 / 3          | Mapeamento por risco e dependência com arquitetura                     |
| Verification             | 2 / 3          | Critérios definidos para validação dos requisitos                      |

> O capítulo fornece os alicerces para práticas maduras de definição e teste de requisitos, reutilizáveis por produto.

---

## 🧱 SLSA - Build & Verification Requirements

| Nível | Requisitos principais                     | Cobertura pelo Cap. 02              |
|-------|--------------------------------------------|-------------------------------------|
| 1     | Definição de critérios de validação        | ✅ Aplicação explícita de critérios |
| 2     | Proveniência e rastreabilidade             | ❌ Fora do âmbito                   |
| 3     | Verificação reforçada no pipeline          | ❌ Implementado noutros capítulos   |

**🔐 Nível máximo suportado por este capítulo: SLSA 1 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

