---
id: achievable-maturity
title: Mapeamento de Maturidade - Threat Modeling
description: Alinhamento entre as práticas deste capítulo e os principais frameworks de segurança
tags: [maturidade, threat-modeling, SAMM, SLSA, DSOMM]
---

> **Método:** Ver [Metodologia de Validação de Claims](../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# 📈 Maturidade - Threat Modeling

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 03** do manual SbD-ToE e os requisitos de frameworks reconhecidas: **OWASP SAMM**, **OWASP DSOMM** e **SLSA**.

O Threat Modeling é uma prática estruturante do ciclo de vida seguro. Permite antecipar riscos, definir requisitos proporcionais e justificar a aplicação de controlos de segurança. Este capítulo fornece uma abordagem repetível, rastreável e proporcional baseada em **STRIDE**, **DFDs**, *threat maps* e critérios de validação. Quando existe tratamento de dados pessoais, aplica-se **LINDDUN** de forma complementar.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento não mede a maturidade global de uma organização. Mede apenas o contributo deste capítulo para domínios de maturidade reconhecidos nas frameworks selecionadas.

| Framework   | Avaliação usada                 | Justificação                                      |
|-------------|----------------------------------|---------------------------------------------------|
| OWASP SAMM  | `n / 3`                          | Modelo prescritivo com progressão explícita       |
| OWASP DSOMM | `n / m`                          | Níveis formais por domínio técnico                |
| SLSA        | Nível máximo suportado (1–4)     | Leitura bounded de supply chain / build / release |

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                         | Práticas ou Objetos Cobertos                                     | Avaliação de Maturidade             |
|------------------|----------------------------------------------|------------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Design → Threat Assessment                   | Modelação estruturada com STRIDE, DFDs e análise por risco       | **2 / 3**                           |
| OWASP DSOMM      | Architecture, Requirements, Risk Analysis    | Integração no SDLC, rastreabilidade, *threat maps* reutilizáveis | **2 / 4** (média dos domínios)      |
| SLSA v1.0        | Risk Awareness (Supply Chain)                | Apoio indireto à definição proporcional de controlos             | **Nível 1 / 4**                     |

---

## 🧱 OWASP SAMM - Design → Threat Assessment

| Nível | Descrição SAMM                                                            | Cobertura pelo Cap. 03                     |
|------:|---------------------------------------------------------------------------|--------------------------------------------|
| 1     | Ameaças identificadas de forma sistemática                                | ✅ Processo baseado em STRIDE               |
| 2     | Análise estruturada com modelos formais e rastreabilidade                 | ✅ DFD, *threat map*, aceitação de risco    |
| 3     | Integração contínua e automação organizacional                            | ❌ Fora do âmbito deste capítulo (ver `30`) |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Architecture, Risk Analysis, Requirements

| Domínio       | Níveis cobertos | Justificação técnica                                                   |
|---------------|-----------------|------------------------------------------------------------------------|
| Architecture  | 2 / 4           | Análise de arquitetura e dependências com mapeamento de ameaças       |
| Risk Analysis | 2 / 4           | Integração com classificação e aceitação de risco                     |
| Requirements  | 2 / 4           | Geração de requisitos a partir do threat modeling e sua validação     |

> A abordagem prescrita permite a reutilização de modelos de ameaça e sua rastreabilidade a requisitos e controlos. Métricas globais e *gating* automatizado pertencem ao `30-recomendacoes-avancadas.md`.

---

## 🧱 SLSA - Supply Chain Risk Awareness

| Nível | Requisitos principais                              | Cobertura pelo Cap. 03                   |
|------:|-----------------------------------------------------|------------------------------------------|
| 1     | Consciência de risco e ameaça                       | ✅ Classificação e threat modeling        |
| 2     | Requisitos formais de proveniência                   | ❌ Fora do âmbito                         |
| 3+    | Controlo reforçado na cadeia de fornecimento        | ❌ Tratado noutros capítulos (CI/CD)      |

**🔐 Nível máximo suportado por este capítulo: SLSA 1 / 4**

---

## ✅ Conclusão

- Este capítulo sustenta uma leitura de maturidade principalmente ancorada em **OWASP SAMM** e **OWASP DSOMM**;
- Quando aplicável, também suporta uma leitura bounded em **SLSA**, sem pretender medir a maturidade global da organização;
- A avaliação apresentada é **chapter-scoped** e contributiva, não substituindo uma avaliação formal framework-native.

