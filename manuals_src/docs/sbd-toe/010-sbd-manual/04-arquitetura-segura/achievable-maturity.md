---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 04
sidebar_position: 10
tags: [canon, maturidade, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Arquitetura Segura

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 04** do manual SbD-ToE e os requisitos das principais frameworks de segurança e maturidade:

- **OWASP SAMM**
- **OWASP DSOMM**
- **SLSA**

O capítulo propõe uma abordagem prescritiva à definição e validação de arquiteturas seguras, com base em requisitos formais (`ARC-001` a `ARC-011`), segmentação por zonas de confiança, princípios de defesa em profundidade e critérios de rastreabilidade e exceção.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                    | Práticas ou Objetos Cobertos                                       | Avaliação de Maturidade          |
|------------------|-----------------------------------------|--------------------------------------------------------------------|----------------------------------|
| OWASP SAMM v2.1  | Design → Architecture & Design          | Princípios formais, validação e documentação da arquitetura          | **2 / 3**                        |
| OWASP DSOMM      | Architecture, Risk, Requirements         | Requisitos `ARC-XXX`, rastreabilidade, zonas de confiança          | **3 / 4** (média dos domínios)   |
| SLSA v1.0        | Build System, Provenance                | Segmentação e isolamento da arquitetura                              | **Nível 2 / 4**                  |

---

## 🧱 OWASP SAMM - Design → Architecture & Design

| Nível | Descrição SAMM                                             | Cobertura pelo Cap. 04                              |
|-------|------------------------------------------------------------|-----------------------------------------------------|
| 1     | Arquitetura definida informalmente                         | ✅ Requisitos mínimos `ARC-001` a `ARC-004`         |
| 2     | Documentação com validação proporcional                    | ✅ Validação rastreável, zonas de confiança         |
| 3     | Integração contínua e revisão automatizada                 | ❌ Fora do âmbito (requer automação e pipelines)    |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Architecture, Requirements, Risk

| Domínio       | Níveis cobertos | Justificação técnica                                               |
|---------------|----------------|----------------------------------------------------------------------|
| Architecture  | 3 / 4          | Segmentação, zonas de confiança, tratamento explícito               |
| Requirements  | 3 / 4          | Requisitos formais por tipo de componente (`ARC-XXX`)               |
| Risk Analysis | 3 / 4          | Integração com threat modeling e aceitação de risco por exceção     |

> O capítulo cobre a maioria dos aspetos de arquitetura relevantes à segurança em ambientes modernos.

---

## 🧱 SLSA - Provenance & Isolation

| Nível | Requisitos principais                          | Cobertura pelo Cap. 04                  |
|-------|-------------------------------------------------|-----------------------------------------|
| 1     | Princípios básicos de isolamento                | ✅ Segmentação e zonas de confiança      |
| 2     | Arquitetura formal com proveniência             | ✅ Requisitos documentados               |
| 3–4   | Cadeias verificáveis, builds isolados           | ❌ Fora do âmbito (ver Cap. 06 e 08)     |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

