---
id: rastreabilidade
title: Rastreabilidade — Capítulo 00: Fundamentos e Papéis
description: Rastreabilidade das práticas de papéis, responsabilidades e fundamentos face a frameworks normativos com pilot formal
tags: [rastreabilidade, roles, responsabilidades, governanca, ssdf, nis2, dora]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 00: Fundamentos e Papéis

Este capítulo define os **13 papéis do modelo SbD-ToE** com responsabilidades por capítulo, User Stories associadas e mapeamento regulatório. É o âncora de ownership do ciclo de vida de segurança.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SLG — Security Event Logging, Audit Trail & Centralized Logging | Papéis formais, ownership de práticas, ciclo de vida organizacional |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento de requisito canónico. "Parcial" = sem unit dedicado no capítulo.

| Framework | Requisito / Prática | Cobertura | Fonte verificada | Nota |
|-----------|--------------------|-----------|-----------------|----|
| SSDF PO.2 | Implement Roles and Responsibilities | ✅ Semântico | intro (strong): Papéis e Responsabilidades Organizacionais | 13 papéis com responsabilidades por capítulo; sem row de rastreabilidade SSDF explícita publicada |
| SSDF PO.2.1 | Each role has defined security responsibilities | ✅ Explícito | intro (strong): Papéis e Responsabilidades Organizacionais > Os 13 Roles | Definido em `roles-responsabilidades/` — responsabilidades per capita por capítulo |
| SSDF PO.2.2 | Personnel have security knowledge for their role | ✅ Semântico | supporting_reference (weak): Enquadramento Regulatório (múltiplos roles) | Requisitos de conhecimento implícitos; formação explícita em Cap. 13 |
| NIS2 | Responsabilidades de gestão e papéis de segurança | ✅ Explícito | policy_reference (medium): GRC / Compliance > Enquadramento Regulatório | Overlay regulatório publicado; papéis mapeados para NIS2, DORA, GDPR, AI Act |
| DORA | Roles de segurança em operações digitais | ✅ Explícito | policy_reference (medium): GRC / Compliance > Enquadramento Regulatório | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

### Nota sobre SSDF PO.2

O conteúdo primário para SSDF PO.2 reside neste capítulo — em `roles-responsabilidades/` — e não em Cap. 13 ou 14. A ausência de `canon/25-rastreabilidade.md` tornava este capítulo invisível ao pipeline de rastreabilidade. Esta entrada repara essa omissão.

---

## Modelos de maturidade — pendente de normalização formal

> ⏳ pendente de normalização formal. Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) quando disponível.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Governance → Strategy & Metrics, Education & Guidance |
| OWASP DSOMM | Governance, Education & Training |
| BSIMM13 | Strategy & Metrics (SM1–SM3) |

---

## Ligações com outros capítulos

- **Cap. 13 — Formação**: aplica os requisitos de conhecimento definidos pelos papéis neste capítulo
- **Cap. 14 — Governança**: formaliza exceções, ownership e rastreabilidade organizacional
- **Cap. 01–12** — cada capítulo referencia os papéis definidos aqui para aplicação proporcional das práticas
