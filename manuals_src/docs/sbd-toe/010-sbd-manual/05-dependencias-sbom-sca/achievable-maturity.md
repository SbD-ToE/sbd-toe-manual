---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 05
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Dependências, SBOM e SCA

Este documento apresenta o mapeamento entre as práticas descritas no Capítulo 05 do SbD-ToE - *Gestão de Dependências, SBOM e SCA* - e os principais frameworks de segurança e maturidade:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

O capítulo prescreve práticas formais para identificação, validação e governação contínua de dependências externas e componentes de terceiros, com integração de SBOM, políticas e SCA.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                              | Práticas ou Objetos Cobertos                                              | Avaliação de Maturidade        |
|------------------|---------------------------------------------------|---------------------------------------------------------------------------|--------------------------------|
| OWASP SAMM v2.1  | Construction → Dependency Management              | SBOM, políticas de aceitação, exceções, validação e bloqueio              | **2 / 3**                      |
| OWASP DSOMM      | Policy, Build & Deploy, Tooling                   | Políticas de risco, hardening, bloqueios CI/CD, rastreabilidade SCA       | **2 / 3** (média dos domínios) |
| SLSA v1.0        | Provenance, Build Integrity, Dependency Control   | SBOM, pinning, proveniência de dependências                               | **Nível 2 / 4**                |

---

## 🧱 OWASP SAMM - Construction → Dependency Management

| Nível | Descrição SAMM                                                     | Cobertura pelo Cap. 05                                |
|-------|--------------------------------------------------------------------|--------------------------------------------------------|
| 1     | Identificação e listagem manual de dependências                    | ✅ SBOM obrigatória por build                          |
| 2     | Processo formal de aceitação, rastreio e controlo de risco         | ✅ Políticas, exceções e integração com SCA            |
| 3     | Automação e integração contínua                                    | ❌ Parcial - ferramentas integráveis, mas não automatizado no core |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Policy, Build & Deploy, Tooling

| Domínio        | Nível | Justificação técnica                                               |
|----------------|-------|--------------------------------------------------------------------|
| Policy         | 2 / 3 | Definição formal de critérios de aceitação e exceções              |
| Build & Deploy | 2 / 3 | Geração e publicação de SBOM com integração na pipeline            |
| Tooling        | 2 / 3 | Ferramentas recomendadas para SCA, validação de findings           |

---

## 🧱 SLSA - Provenance & Dependency Control

| Nível | Requisitos principais                                  | Cobertura pelo Cap. 05                    |
|-------|---------------------------------------------------------|-------------------------------------------|
| 1     | Listagem e rastreio básico de dependências              | ✅ SBOM gerado por build                   |
| 2     | Proveniência e pinning de versões                       | ✅ Critérios de controlo formal            |
| 3+    | Builds verificáveis e reprodutibilidade                 | ❌ Fora do âmbito (ver Cap. 06 e 08)       |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

