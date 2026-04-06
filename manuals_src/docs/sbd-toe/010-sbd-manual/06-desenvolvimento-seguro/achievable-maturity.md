---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 06
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Desenvolvimento Seguro

Este documento apresenta o grau de alinhamento entre as práticas descritas no Capítulo 06 do SbD-ToE - *Desenvolvimento Seguro* - e os principais frameworks de segurança e maturidade de software:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

O capítulo foca-se na adoção de práticas seguras no desenvolvimento, validação contínua do código, rastreabilidade de decisões técnicas e políticas formais de exceção e ownership, garantindo evidência auditável da aplicação das boas práticas.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                             | Práticas ou Objetos Cobertos                                              | Avaliação de Maturidade        |
|------------------|--------------------------------------------------|---------------------------------------------------------------------------|--------------------------------|
| OWASP SAMM v2.1  | Implementation → Secure Build / Verification     | Linters, validação automática, rastreabilidade, PR validation             | **2 / 3**                      |
| OWASP DSOMM      | Design & Development, Tooling, Metrics           | Práticas estruturadas, validações automáticas, evidência e ownership      | **2 / 3**                      |
| SLSA v1.0        | Provenance, Build Integrity                      | Integração de validações e proveniência no build                          | **Nível 2 / 4**                |

---

## 🧱 OWASP SAMM - Implementation

| Nível | Descrição SAMM                                      | Cobertura pelo Cap. 06                           |
|-------|------------------------------------------------------|--------------------------------------------------|
| 1     | Práticas básicas de verificação manual              | ✅ Revisão de código e boas práticas             |
| 2     | Integração de validações automatizadas no pipeline  | ✅ SAST, linters, PR validation                  |
| 3     | Integração contínua e testes estruturados           | ❌ Parcial - Cap. foca-se em boas práticas, não test coverage |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Design & Development, Tooling, Metrics

| Domínio         | Nível | Justificação técnica                                              |
|------------------|-------|-------------------------------------------------------------------|
| Design & Dev     | 2 / 3 | Práticas estruturadas de desenvolvimento seguro                  |
| Tooling          | 2 / 3 | Linters, validações automáticas integráveis                      |
| Metrics          | 2 / 3 | Rastreabilidade, evidência, ownership e tratamento de exceções   |

---

## 🧱 SLSA - Build Validation & Provenance

| Nível | Requisitos principais                               | Cobertura pelo Cap. 06                       |
|-------|------------------------------------------------------|----------------------------------------------|
| 1     | Validações básicas no pipeline                       | ✅ Linters e PR validation                    |
| 2     | Proveniência e rastreabilidade de decisões           | ✅ Tracking de alterações e ownership         |
| 3–4   | Isolamento e builds reproduzíveis                    | ❌ Fora do âmbito deste capítulo              |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

