---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 06: Desenvolvimento Seguro"
description: Rastreabilidade das práticas de desenvolvimento seguro face a frameworks normativos com pilot formal
tags: [rastreabilidade, desenvolvimento, codificacao, ssdf, asvs, cis, nis2]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 06: Desenvolvimento Seguro

Este capítulo define práticas de **codificação segura** — guidelines, linters, revisão de código, controlo automático e humano — integradas no ciclo de desenvolvimento.

---

## Camada AppSec Core

| Slice AppSec Core | Âncora principal | Relevância |
|-------------------|-----------------|-----------|
| ACO-IVF — Input Validation, Safe Parsing & Controlled Failure | Primária | Validação de entrada, injeção, falha segura, gestão de erros — VAL + ERR requirements |
| ACO-SCBI — Supply Chain & Build Integrity | Secundária | Segurança de dependências, proveniência do código |

> **Nota de mapeamento:** ACO-IVF é o principal espaço de normalização deste capítulo via `CTRL-code-integrity-desenvolvimento-seguro-e-validacao-de-codigo`. ACO-SCBI é ativado pelo addon de dependências e proveniência.

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.  
> Coluna **Fonte verificada** indica o `document_role` e `normative_weight` do unit que confirma a cobertura.

| Framework | Requisito / Prática | Cobertura | Fonte verificada | Nota |
|-----------|--------------------|-----------|----|---|
| SSDF PW.5 | Create Source Code with Secure Coding Techniques | ✅ Explícito | addon (medium): Boas Práticas + Guidelines de Equipa + Linters | Guidelines, linters e práticas proibidas |
| SSDF PW.7 | Review and/or Analyze Human-Readable Code | ✅ Explícito | aplicacao_lifecycle (strong): US-02 Revisão de Código Segura | Revisão estruturada com critérios e rastreabilidade |
| ASVS injection_and_sanitization | Injection prevention | ✅ Explícito | addon (medium): Boas Práticas; req VAL-004 via ACO-IVF-003 | Práticas proibidas + sanitização explícita |
| ASVS input_contract_validation | Input contract validation | ✅ Explícito | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema, validação de entrada |
| ASVS validation_before_internal_use | Validation before use | ✅ Explícito | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validação antes de uso interno |
| ASVS secure_coding_discipline | Generic secure coding discipline | ✅ Semântico | addon (medium): Boas Práticas de Escrita; aplicacao_lifecycle (strong): US-13 Anti-patterns | Claim gap resolvido — conteúdo existe em addons |
| ASVS controlled_failure_and_non_revealing_errors | Controlled failure | ✅ Semântico | requirements_catalog (strong): ERR-001–004 via ACO-IVF-005; addon (medium): Boas Práticas | Falha segura e erros não reveladores |
| ASVS error_handling_and_sensitive_logging_hygiene | Error handling hygiene | ✅ Semântico | requirements_catalog (strong): ERR-005–007 via ACO-IVF-006 | Gestão centralizada, logs pseudonimizados |
| ASVS encoding_architecture | Encoding architecture | ⚠️ Parcial | addon (medium): Boas Práticas (cobertura implícita) | Sem secção dedicada a encoding; coberto parcialmente |
| ASVS file_download_content_serving | File download & content serving | ⚠️ Parcial | Sem unit dedicado em Cap. 06 | Mais relevante em Cap. 10 (testes) |
| ASVS secure_coding_architecture_documentation | Secure coding documentation | ✅ Semântico | addon (medium): Anotações e Evidência + Guidelines de Equipa | Documentação de validações e práticas de equipa |
| ASVS v4 | ASVS4-REQ-V5.1.2 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V5.1.4 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V5.2.2 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V5.3.9 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V5.4.2 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V5.5.4 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V11.1.4 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V12.2.1 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V12.3.4 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V12.3.6 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V12.5.2 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V12.6.1 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V13.2.2 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v4 | ASVS4-REQ-V13.3.1 | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| ASVS v5 | ASVS-REQ-V15.3.1 — V15.3.1 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| ASVS v5 | ASVS-REQ-V15.3.2 — V15.3.2 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| ASVS v5 | ASVS-REQ-V15.3.3 — V15.3.3 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| ASVS v5 | ASVS-REQ-V15.3.4 — V15.3.4 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| ASVS v5 | ASVS-REQ-V15.3.5 — V15.3.5 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| ASVS v5 | ASVS-REQ-V15.3.6 — V15.3.6 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| ASVS v5 | ASVS-REQ-V15.3.7 — V15.3.7 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| ASVS v5 | ASVS-REQ-V16.5.2 — V16.5.2 | 🔧 Reparação | requirements_catalog (strong): ERR-005–007 via ACO-IVF-006 | Error-handling hygiene, logging restraint e centralização de erro já explícitas na família ERR-005–007 do capítulo |
| ASVS v5 | ASVS-REQ-V16.5.3 — V16.5.3 | 🔧 Reparação | requirements_catalog (strong): ERR-005–007 via ACO-IVF-006 | Error-handling hygiene, logging restraint e centralização de erro já explícitas na família ERR-005–007 do capítulo |
| ASVS v5 | ASVS-REQ-V16.5.4 — V16.5.4 | 🔧 Reparação | requirements_catalog (strong): ERR-005–007 via ACO-IVF-006 | Error-handling hygiene, logging restraint e centralização de erro já explícitas na família ERR-005–007 do capítulo |
| CIS v8.1.2 | CIS-9.2 — Use DNS Filtering Services | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| CIS v8.1.2 | CIS-9.5 — Implement DMARC | 🔧 Reparação | requirements_catalog (strong): VAL-001–003 via ACO-IVF-001/002 | Whitelist, schema e input-contract validation semantics já explícitas no catálogo VAL do capítulo |
| CIS v8.1.2 | CIS-16.9 — Train Developers in Application Security Concepts and Secure Coding | 🔧 Reparação | addon (medium): Boas Práticas + Guidelines de Equipa + Linters | Secure-coding discipline, guidelines de equipa e governance de validação já cobertas nos addons operacionais do capítulo |
| CWE | CWE-212 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| CWE | CWE-22 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| CWE | CWE-41 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| CWE | CWE-59 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| CWE | CWE-66 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| CWE | CWE-73 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| CWE | CWE-804 | 🔧 Reparação | requirements_catalog (strong): VAL-005 via ACO-IVF-004 | Validation-before-internal-use semantics já explícitas em VAL-005 do capítulo |
| HIPAA | HIPAA-164-312c1 — Integrity | 🔧 Reparação | addon (medium): Boas Práticas + Guidelines de Equipa + Linters | Compliance/regulatory packaging de secure-coding discipline e governance de validação já está suportado nos addons operacionais do capítulo |
| MCP Official | MCP-AUTH-ERROR-HANDLING | 🔧 Reparação | requirements_catalog (strong): ERR-001–004 via ACO-IVF-005; addon (medium): Boas Práticas | Controlled failure e non-revealing error semantics já explícitas na família ERR-001–004 do capítulo |
| CIS-16 | Application Software Security | ✅ Explícito | addon (medium): Linters; aplicacao_lifecycle (strong): US-04 CI/CD, US-12 pre-commit | Linters, SAST, validações locais obrigatórias |
| NIS2 | Práticas seguras de desenvolvimento | ✅ Explícito | overlay regulatório publicado | — |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit de normative_weight strong/medium com heading_path directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento de requisito canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — exigência proporcional de práticas com base no nível L1–L3
- **Cap. 02** — requisitos VAL + ERR implementados e verificados neste capítulo; CFG-001–007 como baseline de configuração segura
- **Cap. 05** — componentes usados no desenvolvimento validados via SCA
- **Cap. 07** — práticas de codificação integradas como passos automatizados no pipeline
- **Cap. 10** — validação final com testes; file_download_content_serving mais coberto aqui
