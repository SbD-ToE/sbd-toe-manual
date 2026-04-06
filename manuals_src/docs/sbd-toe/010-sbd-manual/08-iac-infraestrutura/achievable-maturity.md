---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 08
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Infraestrutura como Código (IaC)

Este documento estabelece o **alinhamento entre as práticas descritas no Capítulo 08** do manual SbD-ToE e os domínios equivalentes nos principais frameworks de segurança e maturidade de software:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

As práticas visam garantir que projetos IaC sejam tratados como **produtos de software seguros**, com requisitos, validações, rastreabilidade e governação - totalmente integrados no ciclo de desenvolvimento e operação.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                               | Práticas ou Objetos Cobertos                                                    | Avaliação de Maturidade        |
|------------------|----------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------|
| OWASP SAMM v2.1  | Implementation → Secure Build                      | Controlo de pipelines IaC, linting, enforcement                                | **2 / 3**                      |
| OWASP DSOMM      | Design & Development, Build & Test, Tooling        | Validação, segregação de ambientes, controlo de estado                          | **3 / 4**                      |
| SLSA v1.0        | Source L2, Build L2, Provenance, Policy Enforcement| Validação de planos, proveniência, segregação, controlo de builds               | **Nível 2 / 4**                |

---

## 🧱 OWASP SAMM - Secure Build para IaC

| Nível | Descrição SAMM                                       | Cobertura pelo Cap. 08                              |
|-------|-------------------------------------------------------|-----------------------------------------------------|
| 1     | Configuração manual, sem rastreabilidade              | ❌ Fora do âmbito - prática não recomendada         |
| 2     | Uso de linters, controlo automatizado e pipelines     | ✅ Validadores de IaC e enforcement automatizado    |
| 3     | Integração contínua com artefactos rastreáveis        | ❌ Parcial - depende do ecossistema DevOps          |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Aplicação a Projetos IaC

| Domínio             | Nível | Justificação técnica                                               |
|---------------------|-------|--------------------------------------------------------------------|
| Design & Dev        | 3 / 4 | Requisitos IaC, separação de ambientes, arquitetura segura         |
| Build & Test        | 3 / 4 | Linting, validação de planos, pipelines de teste                   |
| Tooling             | 3 / 4 | Ferramentas de análise estática e validação automatizada           |

---

## 🧱 SLSA - Fonte, Build e Proveniência

| Nível | Requisitos principais                                      | Cobertura pelo Cap. 08                              |
|-------|-------------------------------------------------------------|-----------------------------------------------------|
| 1     | Proveniência básica e controle manual                      | ✅ Validadores e aprovação manual formal             |
| 2     | Proveniência verificável e trusted source control          | ✅ Controlo de planos e ambientes                    |
| 3     | Build reprodutível, assinaturas, isolamento de ambiente    | ❌ Fora do âmbito deste capítulo                     |
| 4     | Reprovação por auditor externo e sandboxing total          | ❌ Fora do âmbito deste capítulo                     |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

