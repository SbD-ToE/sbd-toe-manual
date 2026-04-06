---
id: rastreabilidade
title: Rastreabilidade — Capítulo 09: Containers e Imagens
description: Rastreabilidade das práticas de segurança de containers face a frameworks normativos com pilot formal
tags: [rastreabilidade, containers, imagens, ssdf, slsa, capec, asvs]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 09: Containers e Imagens

Este capítulo define práticas de **construção, assinatura, proveniência, hardening e execução segura de containers e imagens** — desde o build até ao runtime.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SCBI — Supply Chain & Build Integrity | Container supply chain, imagens base, digest pinning, SBOM de containers, assinatura e proveniência |
| ACO-IAT — Identity, Access & Session Trust | Container identity, workload identity, OIDC, RBAC e ServiceAccounts em execução |

> **Nota adjunct:** ASVS `secure_configuration_baseline_gap` tem pressão aqui — containers têm semantics de configuração segura (securityContext, policies) mas sem secção dedicada. Candidato ao adjunct `secure_configuration_baseline_integrity` (pendente de promoção).

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF PW.5 | Create Source Code with Secure Coding Techniques | ✅ Explícito | Integridade de imagem; digest pinning; reprodutibilidade | addon (medium): Imagens Base Seguras e Minimalistas |
| SSDF PS.1 | Protect Code and Data from Unauthorized Access | ✅ Explícito | Manifesto e aprovação formal antes de deploy | aplicacao_lifecycle (strong): US-03 — Assinatura e verificação de proveniência |
| SSDF RV.1 | Identify and Confirm Vulnerabilities | ✅ Explícito | Image scanning contínuo com bloqueios por severidade | aplicacao_lifecycle (strong): US-02 — Validação automática de vulnerabilidades |
| SSDF RV.2 | Assess, Prioritize, and Remediate Vulnerabilities | ✅ Explícito | Scanning + critérios de aceitação formais | addon (medium): Deteção e Tratamento de Vulnerabilidades em Imagens |
| SLSA-BUILD-L1 | Provenance exists | ✅ Explícito | Artefactos assinados; proveniência presente | addon (medium): Assinatura de Imagens e Cadeia de Confiança |
| SLSA-BUILD-L3 | Hardened builds | ⚠️ Parcial | Hardening presente; L3 exige isolamento mais específico | addon (medium): Hardening e Restrições de Execução em Containers |
| SLSA-PRINCIPLE-PREFER-ATTESTATIONS | Prefer attestations | ✅ Explícito | Atestações e proveniência de imagens | addon (medium): Assinatura de Imagens e Cadeia de Confiança |
| SLSA-PRODUCER-DISTRIBUTE-PROVENANCE | Distribute provenance | ✅ Explícito | Proveniência distribuída com imagens assinadas | addon (medium): SBOM de Containers e Rastreabilidade de Runtime |
| SLSA-BUILD-PLATFORM-PROVENANCE-GENERATION | Provenance generation | ✅ Explícito | Container provenance gerada no build | aplicacao_lifecycle (strong): US-12 — Builders e Runners Ephemerais, Assinados e com Auditoria |
| SLSA-BUILD-PLATFORM-ISOLATION | Isolation | ⚠️ Parcial | Container isolation semântica | addon (medium): Runners, Execução Isolada e Ambientes Controlados |
| SLSA-VERIFY-DEPENDENCIES | Check dependencies | ⚠️ Parcial | Container deps e SBOM presentes | addon (medium): SBOM de Containers e Rastreabilidade de Runtime |
| CAPEC-206 | Signing Malicious Code | ✅ Semântico | Artefactos assinados com verificação | addon (medium): Assinatura de Imagens e Cadeia de Confiança |
| CAPEC-186 | Malicious Software Update | ✅ Semântico | Promoção verificada via digest pinning | aplicacao_lifecycle (strong): US-01 — Imagens base pinned por digest |
| ASVS secure_configuration_baseline_gap | Secure configuration baseline | ✅ Semântico | securityContext (runAsNonRoot, allowPrivilegeEscalation:false), OPA/Gatekeeper, Kyverno e admission controllers confirmados em units dedicadas; conteúdo substancial em dois addons distintos | addon (medium): Enforcement Técnico de Políticas no Runtime com OPA e Kyverno; addon (medium): Execução Segura de Containers em Clusters Kubernetes |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 05** — inventário de componentes e vulnerabilidades herdadas pelas imagens base
- **Cap. 07** — gates de controlo automático no pipeline (policy enforcement, proveniência)
- **Cap. 08** — manifests de deploy coerentes com a infraestrutura provisionada
- **Cap. 10** — scanners e testes funcionais de segurança integrados
- **Cap. 14** — políticas de operação de registos, retenção e auditoria
