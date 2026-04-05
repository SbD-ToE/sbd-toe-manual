---
id: rastreabilidade
title: Rastreabilidade — Capítulo 02: Requisitos de Segurança
description: Rastreabilidade das práticas de requisitos de segurança face a frameworks normativos com pilot formal
tags: [rastreabilidade, requisitos, ssdf, asvs, slsa, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 02: Requisitos de Segurança

Este capítulo define **requisitos de segurança proporcionais ao risco**, rastreáveis e testáveis, integrados no backlog de produto. É o capítulo com maior volume de referências externas verificadas.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-IVF — Input Validation, Safe Parsing & Controlled Failure | Requisitos de validação de input, parsing seguro e gestão de erros (primário — VAL/ERR) |
| ACO-IAT — Identity, Access & Session Trust | Requisitos de autenticação, autorização e gestão de sessões (secundário — AUT/ACC/SES) |
| ACO-SPC — Secret Handling, Protected Configuration & Operational Identities | Requisitos de configuração segura e protecção de dados sensíveis (secundário — CFG/ENC) |

> **Nota adjunct:** A família ASVS `secure_configuration_baseline_gap` e SSDF PW.9 apontam para pressão de configuração segura por omissão — tema coberto parcialmente aqui mas sem secção dedicada. Candidato ao adjunct `secure_configuration_baseline_integrity` (pendente de promoção).

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento de requisito canónico. "Parcial" = sem unit dedicado no capítulo.

| Framework | Requisito / Prática | Cobertura | Fonte verificada | Nota |
|-----------|--------------------|-----------|-----------------|----|
| SSDF PW.1 | Design Software to Meet Security Requirements | ✅ Explícito | requirements_catalog (strong): AUT, ACC, LOG, SES, VAL, ERR, CFG, ENC, API, INT, REQ, DST, IDE | Catálogo estruturado de requisitos por domínio |
| SSDF PW.4 | Establish Security Criteria | ✅ Explícito | aplicacao_lifecycle (strong): US-05 — Definição de critérios de validação | Critérios de aceitação por nível de risco (L1–L3) |
| ASVS injection_and_sanitization | Injection prevention | ✅ Explícito | requirements_catalog (strong): VAL — Validação de Dados | Row publicada; cobertura de validação de input |
| ASVS input_contract_validation | Structured input validation | ✅ Explícito | requirements_catalog (strong): VAL — Validação de Dados | Row publicada |
| ASVS validation_before_internal_use | Validation before deserialization | ✅ Explícito | requirements_catalog (strong): VAL — Validação de Dados | Row publicada |
| ASVS secure_coding_discipline_gap | Generic secure coding discipline | 🔴 Gap | — | Semantics presentes mas sem family dedicada; candidato a addon |
| ASVS secure_configuration_baseline_gap | Secure defaults & baseline | 🔴 Gap | — | Semantics presentes mas sem secção dedicada |
| ASVS authentication_strength_and_assurance | Authentication strength | ⚠️ Parcial | requirements_catalog (strong): AUT — Autenticação e Identidade | Presente; não embalado como family ASVS |
| CIS-5 | Account Management | ⚠️ Parcial | requirements_catalog (strong): ACC — Controlo de Acesso | Semantics presentes; CIS cobre âmbito empresarial mais largo |
| CIS-6 | Access Control Management | ✅ Explícito | requirements_catalog (strong): ACC — Controlo de Acesso | Row publicada |
| SLSA-VERIFY-EXPECTATIONS | Check verification expectations | ⚠️ Parcial | aplicacao_lifecycle (strong): US-07 — Validação e aprovação final | Critérios de aceitação presentes |
| SLSA-VERIFY-BUILD-LEVEL | Check SLSA Build level | ⚠️ Parcial | requirements_catalog (strong): DST — Distribuição de Artefactos | Critérios de proveniência |
| NIS2 | Medidas técnicas de segurança | ✅ Explícito | policy_reference (medium): Políticas Organizacionais — Requisitos de Segurança > Enquadramento | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização formal

> ⏳ pendente de normalização formal. Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Design → Security Requirements |
| OWASP DSOMM | Requirements, Architecture, Verification |
| BSIMM13 | Intelligence → Requirements and Attack Models |

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco determina o catálogo de requisitos aplicáveis (L1/L2/L3)
- **Cap. 03** — threat modeling alimenta e valida os requisitos definidos aqui
- **Cap. 06** — requisitos implementados e verificados no desenvolvimento
- **Cap. 10** — requisitos testados com critérios de aceitação formais
- **Cap. 14** — exceções a requisitos requerem aprovação formal
