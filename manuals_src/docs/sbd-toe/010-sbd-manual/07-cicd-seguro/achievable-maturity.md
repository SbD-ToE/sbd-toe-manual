---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 07
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - CI/CD Seguro

Este documento apresenta o mapeamento entre as práticas descritas no Capítulo 07 do SbD-ToE - *CI/CD Seguro* - e os principais frameworks de segurança e maturidade:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

O capítulo define práticas para proteger pipelines CI/CD contra execução não autorizada, adulteração, perda de proveniência e outras ameaças à cadeia de fornecimento de software.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                              | Práticas ou Objetos Cobertos                                                  | Avaliação de Maturidade        |
|------------------|---------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------|
| OWASP SAMM v2.1  | Implementation → Build & Deployment Automation    | Segurança integrada no pipeline, segregação de ambientes                      | **2 / 3**                      |
| OWASP DSOMM      | Build, Test, Release, Operate                     | Execução segura, validação de artefactos, assinaturas, rastreabilidade        | **3 / 4**                      |
| SLSA v1.0        | Levels 1–3: Provenance, Policy, Isolation         | Proveniência, trusted builders, controlo de execução, hardening de pipelines  | **Nível 3 / 4**                |

---

## 🧱 OWASP SAMM - Build & Deployment Automation

| Nível | Descrição SAMM                                                  | Cobertura pelo Cap. 07                                  |
|-------|------------------------------------------------------------------|----------------------------------------------------------|
| 1     | Processos de build manuais e não auditáveis                     | ✅ Formalização mínima exigida                           |
| 2     | Pipelines automatizadas com validações e autenticação           | ✅ Execução autenticada e validada                       |
| 3     | Ambientes segregados com integração de controlos contínuos      | ❌ Parcial - depende de controlo externo à pipeline      |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Build, Test, Release, Operate

| Domínio  | Nível | Justificação técnica                                              |
|----------|-------|-------------------------------------------------------------------|
| Build    | 3 / 4 | Execução autenticada, trusted runners, proveniência               |
| Test     | 3 / 4 | Validação e rastreabilidade contínua dos resultados               |
| Release  | 3 / 4 | Assinatura e integridade do artefacto                             |
| Operate  | 3 / 4 | Logs, auditoria e controlo de fluxo CI/CD                         |

---

## 🧱 SLSA - Provenance & CI/CD Control

| Nível | Requisitos principais                                  | Cobertura pelo Cap. 07                              |
|-------|---------------------------------------------------------|-----------------------------------------------------|
| 1     | Build controlado e rastreável                           | ✅ Execução autenticada com logs                    |
| 2     | Proveniência e controlo de configuração                 | ✅ Validação e assinatura de artefactos             |
| 3     | Builds reprodutíveis e trusted builders                 | ✅ Trusted environments e runners                   |
| 4     | Isolamento hermético e verificações externas            | ❌ Fora do âmbito do capítulo (ver Cap. 08 e 09)    |

**🔐 Nível máximo suportado por este capítulo: SLSA 3 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

