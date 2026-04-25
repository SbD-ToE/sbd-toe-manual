---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 02: Requisitos de Segurança"
description: Rastreabilidade das práticas de requisitos de segurança face a frameworks normativos com pilot formal
tags: [rastreabilidade, requisitos, ssdf, asvs, slsa, nis2]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 02: Requisitos de Segurança

Este capítulo define **requisitos de segurança proporcionais ao risco**, rastreáveis e testáveis, integrados no backlog de produto. É o capítulo com maior volume de referências externas verificadas.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-IVF — Input Validation, Safe Parsing & Controlled Failure | Requisitos de validação de input, parsing seguro e gestão de erros (primário — VAL/ERR) |
| ACO-IAT — Identity, Access & Session Trust | Requisitos de autenticação, autorização e gestão de sessões (secundário — AUT/ACC/SES) |
| ACO-ITS — Integration Trust & Service-to-Service Security | Requisitos de confiança inter-serviço, trusted transport e boundaries de integração como scaffold secundário de rastreabilidade (INT/ARC) |
| ACO-ATB — Architecture & Trust Boundaries | Scaffold secundário de requisitos e rastreabilidade para critérios de segmentação, diagramas, trustworthiness especializada e boundary controls de arquitetura; não constitui âncora primária |
| ACO-RPR — Release Promotion, Controlled Rollout & Rollback Readiness | Scaffold secundário de requisitos e rastreabilidade para defaults seguros, hardening de runtime / cabeçalhos, tratamento de erros e deploy controlado; não constitui âncora primária |
| ACO-SLG — Security Event Logging, Audit Trail & Centralized Logging | Scaffold secundário de requisitos e rastreabilidade para alerting, thresholds, time-setting, wrappers de audit trail e obrigações de review / retenção; não constitui âncora primária |
| ACO-TSV — Testing, Security Validation & Empirical Assurance | Scaffold secundário de requisitos e rastreabilidade para verificação de configuração / TLS, boundary support de empirical assurance e requirement headers de testes; não constitui âncora primária |
| ACO-SPC — Secret Handling, Protected Configuration & Operational Identities | Requisitos de configuração segura e protecção de dados sensíveis como scaffold secundário de rastreabilidade (CFG/ENC) |

> **Nota adjunct:** A família ASVS `secure_configuration_baseline_gap` e SSDF PW.9 apontam para pressão de configuração segura por omissão — tema coberto parcialmente aqui mas sem secção dedicada. Candidato ao adjunct `secure_configuration_baseline_integrity` (pendente de promoção).

> **Nota Wave 2 ACO-IAT:** neste capítulo, `ACO-IAT` funciona apenas como **scaffold de requisitos e rastreabilidade**, suportando a âncora bounded em Cap. `04`, a diversificação autorizada em Cap. `08` e os wrappers support-only em Cap. `14`. O Cap. 02 não substitui a âncora primária de `ACO-IAT`, não promove o boundary cluster excluído `CIS-5`, `CIS-5.1`, `CIS-5.5`, `CIS-6.6` e `PCI-7.2.1` para execução, e não reabre qualquer lane fora do freeze de Wave 2.

> **Nota Wave 2 ACO-ITS:** neste capítulo, `ACO-ITS` funciona apenas como **scaffold de requisitos e rastreabilidade**, suportando a execução bounded em Cap. `04` e a diversificação autorizada em Cap. `08`. O Cap. 02 não substitui a âncora primária de `ACO-ITS`, não ganha autoridade autónoma para rows de wireless/channel boundary e não reabre qualquer lane fora do freeze de Wave 2.

> **Nota Wave 3 ACO-ATB:** neste capítulo, `ACO-ATB` funciona apenas como **scaffold de requisitos e rastreabilidade**, suportando a âncora bounded em Cap. `04` e as diversificações autorizadas em Cap. `08` e `11` para critérios de segmentação, diagramas de arquitetura / data flow, trustworthiness especializada e boundary controls que o freeze de Wave 3 reteve em `ACO-ATB`. O Cap. 02 não substitui a âncora primária de `ACO-ATB`, não ganha autoridade autónoma de arquitetura ou deploy, não força qualquer uso de Cap. `14`, e não reabre qualquer lane fora do freeze de Wave 3.

> **Nota Wave 3 ACO-RPR:** neste capítulo, `ACO-RPR` funciona apenas como **scaffold de requisitos e rastreabilidade**, suportando a âncora bounded em Cap. `11` e a diversificação autorizada em Cap. `04` para defaults seguros, debug desativado em produção, mensagens de erro controladas, headers / transporte seguros e deploy apenas via pipeline validado já cobertos em `CFG`, `ERR`, `ENC`, `API`, `INT` e `DST`. O Cap. 02 não substitui a âncora primária de `ACO-RPR`, não ganha autoridade autónoma de release, não força qualquer uso de Cap. `14`, e não reabre qualquer lane fora do freeze de Wave 3.

> **Nota Wave 3 ACO-SLG:** neste capítulo, `ACO-SLG` funciona apenas como **scaffold de requisitos e rastreabilidade**, suportando a âncora bounded em Cap. `12`, as diversificações autorizadas em Cap. `04` e `06`, e o suporte governativo limitado em Cap. `14` para alerting criteria, thresholds, time-setting, audit identity/disassociability, requirement headers e wrappers de incident handling que o freeze de Wave 3 reteve em `ACO-SLG`. O Cap. 02 não substitui a âncora primária de `ACO-SLG`, não ganha autoridade autónoma de monitorização ou governação, não força qualquer uso de Cap. `13`, e não reabre qualquer lane fora do freeze de Wave 3.

> **Nota Wave 3 ACO-TSV:** neste capítulo, `ACO-TSV` funciona apenas como **scaffold de requisitos e rastreabilidade**, suportando a âncora bounded em Cap. `10`, a diversificação autorizada em Cap. `04` e o suporte governativo limitado em Cap. `14` para verificação de configuração / TLS, requirement headers e boundary support do row `SP800-53-SC-44` que o freeze de Wave 3 reteve em `ACO-TSV`. O Cap. 02 não substitui a âncora primária de `ACO-TSV`, não ganha autoridade autónoma de testes ou avaliação, não força qualquer uso de Cap. `06` ou `13`, e não reabre qualquer lane fora do freeze de Wave 3.

> **Nota Wave 1 ACO-SPC:** neste capítulo, `ACO-SPC` funciona apenas como **scaffold de requisitos e rastreabilidade**, suportando a execução bounded em Cap. 06 e as diversificações autorizadas em `04`, `08`, `11`, `12` e `14`. O Cap. 02 não substitui a âncora primária de `ACO-SPC` nem passa a landing surface principal.

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
| ASVS secure_coding_discipline_gap | Generic secure coding discipline | ⚠️ Parcial | Conteúdo de coding discipline está em Cap. 06 `addon/01-boas-praticas-codigo.md` (CWE Top 25, funções perigosas, práticas proibidas); Cap. 02 cobre o âmbito VAL-001→007 (validação/sanitização) | addon (medium, Cap. 06): Boas Práticas de Escrita de Código Seguro |
| ASVS secure_configuration_baseline_gap | Secure defaults & baseline | ✅ Semântico | Família CFG-001→007 confirmada em unit `addon/07-validacao-requisitos.md` (CFG-DEBUG, CFG-ENV, CFG-HARD, CFG-VAULT, CFG-DRIFT) | addon (medium): Validação de Requisitos de Segurança > CFG — Configuração Segura |
| ASVS authentication_strength_and_assurance | Authentication strength | ⚠️ Parcial | requirements_catalog (strong): AUT — Autenticação e Identidade | Presente; não embalado como family ASVS |
| CIS-5 | Account Management | ⚠️ Parcial | requirements_catalog (strong): ACC — Controlo de Acesso | Semantics presentes; CIS cobre âmbito empresarial mais largo |
| CIS-6 | Access Control Management | ✅ Explícito | requirements_catalog (strong): ACC — Controlo de Acesso | Row publicada |
| SLSA-VERIFY-EXPECTATIONS | Check verification expectations | ⚠️ Parcial | aplicacao_lifecycle (strong): US-07 — Validação e aprovação final | Critérios de aceitação presentes |
| SLSA-VERIFY-BUILD-LEVEL | Check SLSA Build level | ⚠️ Parcial | requirements_catalog (strong): DST — Distribuição de Artefactos | Critérios de proveniência |
| NIS2 | Medidas técnicas de segurança | ✅ Explícito | policy_reference (medium): Políticas Organizacionais — Requisitos de Segurança > Enquadramento | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco determina o catálogo de requisitos aplicáveis (L1/L2/L3)
- **Cap. 03** — threat modeling alimenta e valida os requisitos definidos aqui
- **Cap. 06** — requisitos implementados e verificados no desenvolvimento
- **Cap. 10** — requisitos testados com critérios de aceitação formais
- **Cap. 14** — exceções a requisitos requerem aprovação formal
