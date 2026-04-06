---
id: rastreabilidade
title: Rastreabilidade — Capítulo 03: Threat Modeling
description: Rastreabilidade das práticas de threat modeling face a frameworks normativos com pilot formal
tags: [rastreabilidade, threat-modeling, ssdf, asvs, cis]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 03: Threat Modeling

Este capítulo define **metodologias de análise de ameaças** sistemáticas (STRIDE, OCTAVE e outras) integradas no SDLC, com outputs rastreáveis para requisitos e arquitetura.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-TMR — Threat Modeling, Risk Disposition & Mitigation Traceability | Processo formal de modelação de ameaças como prática central (primário) |
| ACO-ATB — Architecture & Trust Boundaries | Identificação e delimitação de superfícies de ataque e fronteiras de confiança |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento de requisito canónico. "Parcial" = sem unit dedicado no capítulo.

| Framework | Requisito / Prática | Cobertura | Fonte verificada | Nota |
|-----------|--------------------|-----------|-----------------|----|
| SSDF PW.2 | Review the Software Design | ✅ Semântico | aplicacao_lifecycle (strong): US-02 — Validação de arquitetura com threat modeling | Threat modeling como prática de revisão de design |
| SSDF PW.9 | Use Well-Secured Settings by Default | ⚠️ Parcial | addon (medium): Boas Práticas (metodologias e ferramentas) | Recomendações avançadas contêm semantics de secure defaults |
| ASVS business_logic_security | Business logic security | ⚠️ Parcial | addon (medium): Mapeamento de Ameaças para Requisitos de Segurança | Threat modeling e derivação de requisitos adjacentes |
| ASVS encoding_architecture | Encoding architecture | ⚠️ Parcial | addon (medium): Metodologias e Ferramentas de Threat Modeling | Threat modeling semantics de encoding |
| CIS-16 | Application Software Security | ⚠️ Parcial | aplicacao_lifecycle (strong): US-01 — Criação do modelo de ameaça | Threat modeling como prática formal de design (16.8) |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota AI/LLM:** OWASP MCP Top 10 (MCP06, MCP10) e ENISA AI referenciam threat modeling para contextos agentic/LLM. Este tema é abordado nas recomendações avançadas mas representa pressão para um addon dedicado a AI/LLM threat patterns (futuro).

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco determina obrigatoriedade e profundidade do threat modeling
- **Cap. 02** — outputs do threat modeling alimentam e validam requisitos de segurança
- **Cap. 04** — arquitetura segura é validada como output do processo de threat modeling
- **Cap. 07** — threat modeling integrado em pipelines CI/CD
- **Cap. 10** — vetores identificados no threat modeling tornam-se casos de teste
