---
id: rastreabilidade
title: Rastreabilidade — Capítulo 06: Desenvolvimento Seguro
description: Rastreabilidade das práticas de desenvolvimento seguro face a frameworks normativos com pilot formal
tags: [rastreabilidade, desenvolvimento, codificacao, ssdf, asvs, cis, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 06: Desenvolvimento Seguro

Este capítulo define práticas de **codificação segura** — guidelines, linters, revisão de código, controlo automático e humano — integradas no ciclo de desenvolvimento.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SCBI — Secure Coding & Build Integrity | Codificação segura, guidelines, controlo de qualidade de código |
| ACO-IVF — Integrity Verification & Findings | Validação automatizada, findings de revisão de código |

> **Nota:** O gap `secure_coding_discipline_gap` (ASVS) aponta para ausência de uma family unificadora de "disciplina de codificação segura". O conteúdo existe disperso — candidato a addon dedicado (e.g., `addon/02-disciplina-de-codigo-seguro.md`).

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PW.5 | Create Source Code with Secure Coding Techniques | ✅ Explícito | Guidelines, linters e revisão formal |
| SSDF PW.7 | Review and/or Analyze Human-Readable Code | ✅ Explícito | Revisão estruturada com critérios e rastreabilidade |
| ASVS injection_and_sanitization | Injection prevention | ✅ Explícito | Row publicada |
| ASVS input_contract_validation | Input contract validation | ✅ Explícito | Row publicada |
| ASVS validation_before_internal_use | Validation before use | ✅ Explícito | Row publicada |
| ASVS secure_coding_discipline_gap | Generic secure coding discipline | 🔴 Gap | Conteúdo existe mas não exposto como family; candidato a addon |
| ASVS controlled_failure_and_non_revealing_errors | Controlled failure | ⚠️ Parcial | Secure development semantics |
| ASVS error_handling_and_sensitive_logging_hygiene | Error handling hygiene | ⚠️ Parcial | Desenvolvimento e testing adjacent |
| ASVS encoding_architecture | Encoding architecture | ⚠️ Parcial | Secure development semantics |
| ASVS file_download_content_serving | File download & content serving | ⚠️ Parcial | Secure development adjacent |
| ASVS secure_coding_architecture_documentation | Secure coding documentation | ⚠️ Parcial | Architecture e development |
| CIS-16 | Application Software Security | ✅ Explícito | Linters, scanners, revisão estruturada (16.3, 16.11, 16.12) |
| NIS2 | Práticas seguras de desenvolvimento | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Implementation → Secure Build, Secure Code Review |
| OWASP DSOMM | Design & Development, Build |
| BSIMM13 | Code Review (CR1–CR3) |

---

## Ligações com outros capítulos

- **Cap. 01** — exigência proporcional de práticas com base no nível L1–L3
- **Cap. 02** — requisitos REQ-XXX implementados e verificados neste capítulo
- **Cap. 05** — componentes usados no desenvolvimento validados via SCA
- **Cap. 07** — práticas de codificação integradas como passos automatizados no pipeline
- **Cap. 10** — validação final com testes e métricas de cobertura
