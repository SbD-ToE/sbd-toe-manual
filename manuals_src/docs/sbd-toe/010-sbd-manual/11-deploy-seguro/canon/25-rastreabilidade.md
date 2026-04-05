---
id: rastreabilidade
title: Rastreabilidade — Capítulo 11: Deploy Seguro
description: Rastreabilidade das práticas de deploy seguro face a frameworks normativos com pilot formal
tags: [rastreabilidade, deploy, execucao, ssdf, slsa, capec, asvs, cis, dora, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 11: Deploy Seguro e Controlo de Execução

Este capítulo define práticas de **entrega, ativação e execução segura** de software — o capítulo com maior volume total de referências externas verificadas.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-RPR — Release Process & Readiness | Gestão de release, gates de promoção, rollback, readiness checks |
| ACO-SPC — Security Policy & Controls | Políticas de autorização de execução, separação de ambientes |

> **Nota adjunct:** SSDF PW.9 e ASVS `secure_configuration_baseline_gap` têm pressão significativa aqui — o deploy addon (`addon/01-modelo-controle-execucao.md`) toca no tema mas sem secção dedicada. Candidato prioritário ao adjunct `secure_configuration_baseline_integrity` (pendente de promoção).

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PO.5 | Implement and Maintain Secure Environments | 🔧 Reparação | Semantics em deploy addon; sem row explícita SSDF publicada |
| SSDF PS.1 | Protect Code and Data from Unauthorized Access | ✅ Explícito | Row publicada via containers |
| SSDF RV.3 | Analyze Vulnerabilities to Root Causes | ✅ Explícito | Row publicada; monitorização pós-deploy |
| SSDF PW.9 | Use Well-Secured Settings by Default | 🔴 Gap | Deploy addon tem semantics; sem row explícita publicada |
| SLSA-BUILD-L1 | Provenance exists | ✅ Explícito | Artefacto assinado antes de deploy |
| SLSA-PRODUCER-DISTRIBUTE-PROVENANCE | Distribute provenance | ✅ Explícito | Row publicada |
| SLSA-PRINCIPLE-TRUST-PLATFORMS | Trust platforms | ✅ Semântico | Verificação antes de deploy |
| SLSA-PRODUCER-CONSISTENT-BUILD | Consistent build | ✅ Semântico | Deployment controlado e reprodutível |
| SLSA-VERIFY-BUILD-LEVEL | Check SLSA Build level | ⚠️ Parcial | Proveniência verificada antes de promoção |
| CAPEC-186 | Malicious Software Update | ✅ Semântico | Promoção verificada, rollback |
| CAPEC-669 | Alteration of Software Update | ✅ Semântico | Promoção verificada, rastreabilidade |
| CIS-4 | Secure Configuration of Enterprise Assets | ⚠️ Parcial | Deploy config semantics; enterprise config além do âmbito |
| CIS-6 | Access Control Management | ✅ Explícito | Row publicada |
| ASVS authentication_lifecycle | Auth lifecycle | ⚠️ Parcial | Deploy semantics |
| ASVS authorization_and_least_privilege | Authorization | ⚠️ Parcial | Deploy semantics |
| ASVS secure_transport | Secure transport | ⚠️ Parcial | Deploy e architecture |
| ASVS secure_configuration_baseline_gap | Secure configuration baseline | 🔴 Gap | Semantics em deploy addon; sem secção dedicada |
| DORA | Deploy seguro e reversível | ✅ Explícito | Overlay regulatório publicado |
| NIS2 | Deploy controlado | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Implementation → Release Management, Environment Management |
| OWASP DSOMM | Design & Development (deploy practices) |
| BSIMM13 | Deployment (DR1–DR3, SE2.5) |

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco identifica onde execução controlada é mandatória
- **Cap. 02** — critérios técnicos de deploy derivados de requisitos
- **Cap. 07** — pipeline automatiza gates, rollback e validações
- **Cap. 09** — containers produzidos e assinados, promovidos por este capítulo
- **Cap. 12** — observabilidade ativa do runtime pós-deploy
