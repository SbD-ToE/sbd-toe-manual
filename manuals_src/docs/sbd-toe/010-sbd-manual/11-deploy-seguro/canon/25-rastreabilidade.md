---
id: rastreabilidade
title: Rastreabilidade — Capítulo 11: Deploy Seguro
description: Rastreabilidade das práticas de deploy seguro face a frameworks normativos com pilot formal
tags: [rastreabilidade, deploy, execucao, ssdf, slsa, capec, asvs, cis, dora, nis2]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 11: Deploy Seguro e Controlo de Execução

Este capítulo define práticas de **entrega, ativação e execução segura** de software — o capítulo com maior volume total de referências externas verificadas.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-RPR — Release Promotion, Controlled Rollout & Rollback Readiness | Gestão de release, gates de promoção, rollback, readiness checks |
| ACO-SPC — Secret Handling, Protected Configuration & Operational Identities | Políticas de autorização de execução, separação de ambientes |

> **Nota adjunct:** `SSDF PW.9` e `ASVS secure_configuration_baseline_gap` são CLAIM GAPSs — o conteúdo existe em `addon/04-validacoes-pre-deploy.md` (misconfig check) e `addon/08-segregacao-e-validacao-operacional.md` (config auditing), mas sem row explícita publicada. Candidatos a reparação no próximo ciclo.

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF PO.5 | Implement and Maintain Secure Environments | 🔧 Reparação | Semântico em addons; sem row explícita SSDF publicada | addon (medium): Segregação de Ambientes e Validação Operacional |
| SSDF PS.1 | Protect Code and Data from Unauthorized Access | ✅ Explícito | Deploy apenas de artefactos verificados | aplicacao_lifecycle (strong): US-01 - Deploy apenas de artefactos verificados |
| SSDF RV.3 | Analyze Vulnerabilities to Root Causes | ✅ Explícito | Monitorização pós-deploy e reação a incidentes | addon (medium): Monitorização e Reação a Incidentes de Runtime |
| SSDF PW.9 | Use Well-Secured Settings by Default | 🔧 Reparação | Conteúdo canónico em Cap. 02 `addon/07` família CFG-001→007 (debug off, env sep, no hardcoded, vault, drift); Cap. 11 não referencia esses critérios como validação pré-deploy explícita | addon (medium): Validações de Segurança antes de Deploy; → ver Cap. 02 addon CFG-001→007 |
| SLSA-BUILD-L1 | Provenance exists | ✅ Explícito | Artefacto assinado e verificado antes de deploy | aplicacao_lifecycle (strong): US-01 - Deploy apenas de artefactos verificados |
| SLSA-PRODUCER-DISTRIBUTE-PROVENANCE | Distribute provenance | ✅ Explícito | Rastreabilidade end-to-end publicada | aplicacao_lifecycle (strong): US-05 - Rastreabilidade end-to-end |
| SLSA-PRINCIPLE-TRUST-PLATFORMS | Trust platforms | ✅ Semântico | Verificação antes de deploy | addon (medium): Validações de Segurança antes de Deploy |
| SLSA-PRODUCER-CONSISTENT-BUILD | Consistent build | ✅ Semântico | Deployment controlado e reprodutível | addon (medium): Controlo de Versão e Rollback Seguro |
| SLSA-VERIFY-BUILD-LEVEL | Check SLSA Build level | ⚠️ Parcial | Proveniência verificada antes de promoção | addon (medium): Validações de Segurança antes de Deploy |
| CAPEC-186 | Malicious Software Update | ✅ Semântico | Promoção verificada, rollback estruturado | aplicacao_lifecycle (strong): US-04 - Rollback rápido e testado |
| CAPEC-669 | Alteration of Software Update | ✅ Semântico | Promoção verificada, rastreabilidade end-to-end | aplicacao_lifecycle (strong): US-05 - Rastreabilidade end-to-end |
| CIS-4 | Secure Configuration of Enterprise Assets | ⚠️ Parcial | Deploy config semântico; enterprise config além do âmbito | addon (medium): Segregação de Ambientes e Validação Operacional |
| CIS-6 | Access Control Management | ✅ Explícito | Controlo de execução e gates de aprovação | aplicacao_lifecycle (strong): US-07 - Controlo de execução com aprovação |
| ASVS authentication_lifecycle | Auth lifecycle | ⚠️ Parcial | Deploy semântico; sem unit dedicado | addon (medium): Modelo de Controlo de Execução em Runtime |
| ASVS authorization_and_least_privilege | Authorization | ⚠️ Parcial | Deploy semântico; sem unit dedicado | addon (medium): Modelo de Controlo de Execução em Runtime |
| ASVS secure_transport | Secure transport | ⚠️ Parcial | Deploy e architecture; sem unit dedicado | sem unit dedicado no capítulo |
| ASVS secure_configuration_baseline_gap | Secure configuration baseline | 🔧 Reparação | Conteúdo canónico em Cap. 02 `addon/07` família CFG-001→007; Cap. 09 cobre enforcement técnico (OPA/Kyverno); Cap. 11 não referencia como critério explícito de validação pré-deploy | addon (medium): Validações de Segurança antes de Deploy; → ver Cap. 02 addon CFG-001→007 e Cap. 09 addon OPA/Kyverno |
| DORA | Deploy seguro e reversível | ✅ Explícito | Overlay regulatório publicado | requirements_catalog (strong): Catálogo DPL + addon (medium): Práticas de Release Management |
| NIS2 | Deploy controlado | ✅ Explícito | Overlay regulatório publicado | requirements_catalog (strong): Catálogo DPL - Deploy Seguro |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo. "Reparação" = CLAIM GAP — conteúdo existe mas sem row publicada.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco identifica onde execução controlada é mandatória
- **Cap. 02** — critérios técnicos de deploy derivados de requisitos
- **Cap. 07** — pipeline automatiza gates, rollback e validações
- **Cap. 09** — containers produzidos e assinados, promovidos por este capítulo
- **Cap. 12** — observabilidade ativa do runtime pós-deploy
