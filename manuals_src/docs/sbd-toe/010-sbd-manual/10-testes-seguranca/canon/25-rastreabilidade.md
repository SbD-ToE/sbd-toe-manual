---
id: rastreabilidade
title: Rastreabilidade — Capítulo 10: Testes de Segurança
description: Rastreabilidade das práticas de testes de segurança face a frameworks normativos com pilot formal
tags: [rastreabilidade, testes, validacao, ssdf, asvs, cis, slsa, dora]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 10: Testes de Segurança

Este capítulo define uma **estratégia de testes de segurança proporcional ao risco** — SAST, DAST, IAST, fuzzing, pentesting — integrada no pipeline CI/CD com critérios de aceitação formais e gestão de findings.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-IVF — Integrity Verification & Findings | Estratégia de testes, execução, gestão de findings e rastreabilidade |
| ACO-ATB — Attack Surface & Threat Boundaries | Cobertura de testes baseada em vetores de ataque identificados |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PO.4 | Define Security Check Criteria | ✅ Semântico | Estratégia de testes proporcional ao risco |
| SSDF PW.7 | Review and/or Analyze Code | ✅ Explícito | Validação automatizada integrada no pipeline |
| SSDF RV.1 | Identify and Confirm Vulnerabilities | ✅ Explícito | Row publicada; gestão de vulnerabilidades |
| SSDF RV.3 | Analyze Vulnerabilities to Root Causes | ✅ Explícito | Row publicada; correção e validação |
| CIS-7 | Continuous Vulnerability Management | ⚠️ Parcial | Testing adjacent; CIS cobre âmbito mais largo |
| CIS-18 | Penetration Testing | ✅ Explícito | Row publicada; pentesting formal e planeado |
| ASVS injection_and_sanitization | Injection testing | ✅ Explícito | Row publicada |
| ASVS validation_before_internal_use | Validation testing | ✅ Explícito | Row publicada |
| ASVS controlled_failure | Controlled failure testing | ⚠️ Parcial | Testing adjacent |
| ASVS error_handling_logging_hygiene | Error handling testing | ⚠️ Parcial | Testing adjacent |
| SLSA-VERIFY-BUILD-LEVEL | Build level verification | ⚠️ Parcial | Test evidence e critérios de maturidade |
| DORA | Testes de segurança baseados em risco | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Verification → Security Testing |
| OWASP DSOMM | Testing, Design & Development |
| BSIMM13 | Security Testing (ST1–ST3) |

---

## Ligações com outros capítulos

- **Cap. 01** — estratégia de testes proporcional à classificação de risco L1–L3
- **Cap. 02** — requisitos testados com critérios de aceitação formais
- **Cap. 03** — vetores de threat modeling traduzidos em casos de teste
- **Cap. 06** — testes complementam as validações em desenvolvimento
- **Cap. 07** — testes integrados como gates obrigatórios no pipeline
- **Cap. 14** — findings ligados a processos de exceção e auditoria
