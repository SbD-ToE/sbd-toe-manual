---
id: rastreabilidade
title: Rastreabilidade — Capítulo 03: Threat Modeling
description: Rastreabilidade das práticas de threat modeling face a frameworks normativos com pilot formal
tags: [rastreabilidade, threat-modeling, ssdf, asvs, cis]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 03: Threat Modeling

Este capítulo define **metodologias de análise de ameaças** sistemáticas (STRIDE, OCTAVE e outras) integradas no SDLC, com outputs rastreáveis para requisitos e arquitetura.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-TMR — Threat Modeling & Risk | Processo formal de modelação de ameaças como prática central |
| ACO-ATB — Attack Surface & Threat Boundaries | Identificação e delimitação de superfícies de ataque |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PW.2 | Review the Software Design | ✅ Semântico | Threat modeling como prática de revisão de design |
| SSDF PW.9 | Use Well-Secured Settings by Default | ⚠️ Parcial | Recomendações avançadas contêm semantics de secure defaults |
| ASVS business_logic_security | Business logic security | ⚠️ Parcial | Threat modeling e derivação de requisitos adjacentes |
| ASVS encoding_architecture | Encoding architecture | ⚠️ Parcial | Threat modeling semantics de encoding |
| CIS-16 | Application Software Security | ⚠️ Parcial | Threat modeling como prática formal de design (16.8) |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota AI/LLM:** OWASP MCP Top 10 (MCP06, MCP10) e ENISA AI referenciam threat modeling para contextos agentic/LLM. Este tema é abordado nas recomendações avançadas mas representa pressão para um addon dedicado a AI/LLM threat patterns (futuro).

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Design → Threat Assessment |
| OWASP DSOMM | Design & Development |
| BSIMM13 | Architecture Analysis (AA1–AA3) |

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco determina obrigatoriedade e profundidade do threat modeling
- **Cap. 02** — outputs do threat modeling alimentam e validam requisitos de segurança
- **Cap. 04** — arquitetura segura é validada como output do processo de threat modeling
- **Cap. 07** — threat modeling integrado em pipelines CI/CD
- **Cap. 10** — vetores identificados no threat modeling tornam-se casos de teste
