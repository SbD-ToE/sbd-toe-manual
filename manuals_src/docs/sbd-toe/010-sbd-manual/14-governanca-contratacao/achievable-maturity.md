---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 14
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Governança e Contratação

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 14 - Governança e Contratação**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

As práticas cobrem papéis críticos, exceções, contratos, rastreabilidade organizacional, onboarding e validação de fornecedores, métricas e integração com modelos de maturidade.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework     | Domínios Relevantes                      | Práticas Cobertas                                          | Avaliação de Maturidade                          |
|---------------|-------------------------------------------|-------------------------------------------------------------|--------------------------------------------------|
| **SAMM v2.1** | Governance, Education, Incident Management | Ownership, exceções, rastreabilidade, formação             | **2 / 3**                                        |
| **SLSA v1.0** | Supply Chain Governance                   | Requisitos contratuais, aceitação de risco, rastreabilidade| **Contributo indireto - Nível 2 / 4**            |
| **DSOMM**     | Governance, 3rd Party, Tooling, Training, Metrics | Exceções, KPIs, onboarding, validação, maturidade       | **4 / 5**                                        |

---

## 🧱 OWASP SAMM - Governance e Education

| Domínio               | Nível | Implementação no Cap. 14                                 |
|-----------------------|-------|----------------------------------------------------------|
| Governance            | 2 / 3 | Papéis definidos, exceções formais, contratos seguros    |
| Education & Guidance  | 2 / 3 | Formação de fornecedores e rastreio organizacional       |
| Incident Management   | 1 / 3 | Parciais - rastreabilidade e canais de reporte definidos |

---

## 🧱 OWASP DSOMM

| Domínio         | Nível | Justificação técnica                                               |
|------------------|-------|--------------------------------------------------------------------|
| Governance       | 3 / 3 | Definição clara de ownership, políticas, controlo contínuo         |
| 3rd Party        | 4 / 4 | Validação de fornecedores, requisitos contratuais, rastreabilidade |
| Tooling & Metrics| 4 / 5 | KPIs de governação e feedback contínuo                             |
| Training         | 3 / 3 | Onboarding formal de stakeholders                                 |

---

## 🧱 SLSA - Supply Chain

| Nível | Requisitos principais                            | Cobertura pelo Cap. 14                       |
|-------|--------------------------------------------------|----------------------------------------------|
| 1     | Cadeia de fornecimento minimamente identificada  | ✅ Papéis e terceiros registados              |
| 2     | Requisitos contratuais definidos                 | ✅ Cláusulas de segurança formais             |
| 3     | Verificação independente                         | ❌ Parcial - validações sem atestado externo |
| 4     | Governação contínua e auditável                  | ❌ Não aplicável                             |

**🔐 Nível suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

