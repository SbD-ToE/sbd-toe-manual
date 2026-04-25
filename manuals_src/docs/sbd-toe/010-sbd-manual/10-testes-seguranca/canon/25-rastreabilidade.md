---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 10: Testes de Segurança"
description: Rastreabilidade das práticas de testes de segurança face a frameworks normativos com pilot formal
tags: [rastreabilidade, testes, validacao, ssdf, asvs, cis, slsa, dora]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 10: Testes de Segurança

Este capítulo define uma **estratégia de testes de segurança proporcional ao risco** — SAST, DAST, IAST, fuzzing, pentesting — integrada no pipeline CI/CD com critérios de aceitação formais e gestão de findings.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-TSV — Testing, Security Validation & Empirical Assurance | Estratégia de testes, execução, gestão de findings e rastreabilidade |
| ACO-ATB — Architecture & Trust Boundaries | Cobertura de testes baseada em vetores de ataque identificados |

> **Nota Wave 3 ACO-TSV:** esta leitura funciona como âncora bounded para os rows autorizados de vulnerability scanning, penetration testing, retesting, methodology wrappers, lifecycle / strategy testing e requirement-header packaging que o freeze de Wave 3 reteve em `ACO-TSV`. A leitura permanece **bounded**, mantém o Cap. `04` apenas para os edges de empirical assurance architecture-heavy e wireless / segmentation support, mantém o Cap. `02` apenas como scaffold de requisitos e rastreabilidade para TLS / configuration verification e requirement support, mantém o Cap. `14` apenas como suporte de governação / periodic evaluation wrappers, não força qualquer uso de Cap. `06` ou `13`, e não converte `ASVS v4`, `CIS`, `HIPAA`, `NIST`, `DSOMM` ou `PCI` em autoridade family-blind de testing.

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF PO.4 | Define Security Check Criteria | ✅ Semântico | Estratégia de testes proporcional ao risco | addon (medium): Estratégia de Testes de Segurança no Ciclo de Vida |
| SSDF PW.7 | Review and/or Analyze Code | ✅ Explícito | Validação automatizada integrada no pipeline | aplicacao_lifecycle (strong): US-02 - SAST obrigatório em Pull Request |
| SSDF RV.1 | Identify and Confirm Vulnerabilities | ✅ Explícito | Gestão de vulnerabilidades e findings | aplicacao_lifecycle (strong): US-10 - Gestão Centralizada de Findings com Triagem e SLA |
| SSDF RV.3 | Analyze Vulnerabilities to Root Causes | ✅ Explícito | Correção, validação empírica e rastreabilidade | aplicacao_lifecycle (strong): US-13 - Validação Empírica de Exploitabilidade de Findings |
| CIS-7 | Continuous Vulnerability Management | ⚠️ Parcial | Testing adjacent; CIS cobre âmbito mais largo | sem unit dedicado no capítulo |
| CIS-18 | Penetration Testing | ✅ Explícito | Pentesting formal e planeado | aplicacao_lifecycle (strong): US-08 - PenTesting ofensivo baseado em risco |
| ASVS injection_and_sanitization | Injection testing | ✅ Semântico | Coberto via SAST e DAST | addon (medium): Testes Estáticos de Segurança (SAST) + Testes Dinâmicos de Segurança (DAST) |
| ASVS validation_before_internal_use | Validation testing | ✅ Semântico | Coberto via estratégia de testes e catálogo | requirements_catalog (strong): Catálogo TST + addon (medium): Estratégia de Testes |
| ASVS controlled_failure | Controlled failure testing | ⚠️ Parcial | Testing adjacent; sem unit dedicado | sem unit dedicado no capítulo |
| ASVS error_handling_logging_hygiene | Error handling testing | ⚠️ Parcial | Testing adjacent; sem unit dedicado | sem unit dedicado no capítulo |
| SLSA-VERIFY-BUILD-LEVEL | Build level verification | ⚠️ Parcial | Test evidence e critérios de maturidade | maturity (weak): SLSA - Build/Test Coverage |
| DORA | Testes de segurança baseados em risco (TLPT) | ✅ Explícito | Overlay regulatório TLPT publicado | addon (medium): TLPT - Readiness e Enquadramento Regulatório (DORA) |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — estratégia de testes proporcional à classificação de risco L1–L3
- **Cap. 02** — requisitos testados com critérios de aceitação formais
- **Cap. 03** — vetores de threat modeling traduzidos em casos de teste
- **Cap. 06** — testes complementam as validações em desenvolvimento
- **Cap. 07** — testes integrados como gates obrigatórios no pipeline
- **Cap. 14** — findings ligados a processos de exceção e auditoria
