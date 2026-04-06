---
id: rastreabilidade
title: Rastreabilidade — Capítulo 13: Formação e Onboarding
description: Rastreabilidade das práticas de formação e onboarding face a frameworks normativos com pilot formal
tags: [rastreabilidade, formacao, onboarding, ssdf, cis, nis2]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 13: Formação e Onboarding Seguro

Este capítulo define **programas de formação por papel** — contínuos, rastreáveis, com validação de conhecimento — como componente crítica da adoção do SbD-ToE.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SLG — Security Event Logging, Audit Trail & Centralized Logging | Formação como componente do ciclo de vida organizacional de segurança; rastreabilidade e audit trail de capacitação |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF PO.2 | Implement Roles and Responsibilities | ✅ Semântico | PO.2.1/PO.2.2 cobertos via formação por função; conteúdo primário de PO.2 está em Cap. 00 | addon (medium): Manual de Formação por Perfil |
| SSDF PO.2.1 | Each role receives security training | ✅ Explícito | Formação obrigatória por papel com rastreabilidade | aplicacao_lifecycle (strong): US-02 - Formação contínua e atualização + US-01 - Onboarding seguro |
| SSDF PO.2.2 | Validate security knowledge before access | ✅ Explícito | Validação de conhecimento antes de atribuição de privilégios | aplicacao_lifecycle (strong): US-11 - Validação Formal de Conclusão + US-12 - Validação de Conhecimento |
| CIS-14 | Security Awareness and Skills Training | ✅ Explícito | 14.1/14.2/14.3 — formação proporcional ao risco, validação, formação contínua | aplicacao_lifecycle (strong): US-01 a US-05 + addon (medium): Trilhos Formativos por Função e Risco |
| ASVS authentication_lifecycle | Auth lifecycle & recovery | ⚠️ Parcial | Onboarding semântico; sem unit dedicado | addon (medium): Checklist de Onboarding Técnico Seguro |
| NIS2 | Capacitação e onboarding de segurança | ✅ Explícito | Overlay regulatório publicado | intro (strong): Formação e Capacitação |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota SSDF PO.2:** O conteúdo primário de PO.2 (definição formal de papéis e responsabilidades) reside em `00-fundamentos/roles-responsabilidades/`. Cap. 13 cobre os sub-requisitos de formação e validação (PO.2.1, PO.2.2). A rastreabilidade completa de PO.2 requer leitura conjunta de Cap. 00 + Cap. 13 + Cap. 14.

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 00** — papéis definidos aqui recebem a formação prescrita em Cap. 13
- **Cap. 01** — formação obrigatória com base na classificação de risco da aplicação
- **Cap. 14** — controlo de formação aplicado a terceiros e fornecedores
- **Cap. 02–12** — cada capítulo tem trilha de formação correspondente
