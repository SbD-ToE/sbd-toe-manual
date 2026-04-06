---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 11
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Deploy Seguro

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 11 - Deploy Seguro**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

As práticas cobrem: validação de readiness, controlo de triggers de deploy, rollback seguro, registo de decisões, gates automatizados e rastreabilidade organizacional em ambientes de produção.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework     | Domínios Relevantes                  | Práticas Cobertas                                                  | Avaliação de Maturidade        |
|---------------|---------------------------------------|----------------------------------------------------------------------|--------------------------------|
| **SAMM v2.1** | Verification → Security Testing       | Gates, validação final, rollback                                    | **3 / 3**                      |
| **SLSA v1.0** | Provenance, Build Triggers            | Controlos de promoção e artefactos, validações                      | **Nível 2 / 4**                |
| **DSOMM**     | Design & Development                  | Deploy seguro, rastreabilidade, controlo formal de produção         | **4 / 5**                      |

---

## 🧱 OWASP SAMM - Verification → Security Testing

| Nível | Descrição SAMM                                | Implementação no Cap. 11                           |
|-------|------------------------------------------------|----------------------------------------------------|
| 1     | Validação manual antes de produção             | ✅ Checklist e gates de readiness                  |
| 2     | Automatização e rollback validado              | ✅ Rollback com validação integrada                |
| 3     | Controlo formalizado e política de exceções    | ✅ Justificação de deploy, bloqueio e auditoria    |

**🧮 Maturidade atingida: 3 / 3**

---

## 🧱 OWASP DSOMM - Deploy Seguro como Domínio Técnico

| Domínio               | Nível | Justificação técnica                                              |
|-----------------------|-------|-------------------------------------------------------------------|
| Design & Development  | 4 / 5 | Deploy seguro, rollback rastreável, controlo de exceções          |

---

## 🧱 SLSA - Controlo de Build e Proveniência

| Nível | Requisitos principais                                      | Cobertura pelo Cap. 11                                |
|-------|------------------------------------------------------------|--------------------------------------------------------|
| 1     | Deploy controlado manualmente                              | ✅ Pré-condições e triggers definidos                  |
| 2     | Controlo de promoção e validação de artefactos             | ✅ Validação de release e rollback rastreável          |
| 3     | Validação de proveniência e runtime                        | ❌ Parcial - depende de integração com Cap. 07 e 12    |
| 4     | Controlo externo e sandboxing                              | ❌ Não abordado                                         |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

