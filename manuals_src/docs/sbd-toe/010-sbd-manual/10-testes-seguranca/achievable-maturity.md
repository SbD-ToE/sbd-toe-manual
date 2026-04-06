---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 10
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Testes de Segurança

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 10 - Testes de Segurança**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

As práticas abrangem testes automatizados (SAST, DAST, IAST), fuzzing, análise de resultados, rastreabilidade, gestão de findings, testes manuais (ex: PenTesting) e integração contínua no SDLC.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework     | Domínios Relevantes                  | Práticas Cobertas                                                     | Avaliação de Maturidade        |
|---------------|---------------------------------------|------------------------------------------------------------------------|--------------------------------|
| **SAMM v2.1** | Verification → Security Testing       | Testes automatizados, gates de validação, gestão de findings          | **2 / 3**                      |
| **SLSA v1.0** | Build/Test Coverage                   | Cobertura limitada, validação de artefactos antes de deploy           | **Nível 2 / 4**                |
| **DSOMM**     | Testing, Design & Development         | Integração contínua, rastreabilidade por release, gates automáticos   | **2 / 3**                      |

---

## 🧱 OWASP SAMM - Verification → Security Testing

| Nível | Descrição SAMM                                  | Cobertura pelo Cap. 10                                 |
|-------|--------------------------------------------------|--------------------------------------------------------|
| 1     | Testes manuais básicos de segurança              | ✅ Inclui Pentesting e casos adversariais manuais      |
| 2     | Integração de testes automatizados no pipeline   | ✅ SAST, DAST, fuzzing, cobertura e regressão          |
| 3     | Gestão ativa de findings e feedback contínuo     | ❌ Parcial - não garante formalização organizacional   |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Domínios Testing + Design & Development

| Domínio               | Nível | Justificação técnica                                              |
|-----------------------|-------|-------------------------------------------------------------------|
| Testing               | 2 / 3 | SAST/DAST integrados, fuzzing, feedback, gates                    |
| Design & Development  | 2 / 3 | Validação por release, controlo de findings, reporting técnico    |

---

## 🧱 SLSA - Build/Test Coverage

| Nível | Requisitos principais                                             | Cobertura pelo Cap. 10                                 |
|-------|------------------------------------------------------------------|--------------------------------------------------------|
| 1     | Execução de testes em CI                                         | ✅ Cobertura mínima via pipelines                      |
| 2     | Cobertura definida e evidência de testes                         | ✅ Evidência e análise rastreável                      |
| 3     | Cobertura exigida e enforcement                                  | ❌ Parcial - depende de governance                     |
| 4     | Testes e resultados com garantia de integridade                  | ❌ Não abrangido pelo capítulo                         |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

