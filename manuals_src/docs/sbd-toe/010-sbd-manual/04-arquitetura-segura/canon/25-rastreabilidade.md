---
id: rastreabilidade
title: Rastreabilidade — Capítulo 04: Arquitetura Segura
description: Rastreabilidade das práticas de arquitetura segura face a frameworks normativos com pilot formal
tags: [rastreabilidade, arquitetura, ssdf, asvs, slsa, cis]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 04: Arquitetura Segura

Este capítulo define **padrões de arquitetura segura** — zonas de confiança, separação de funções, controlo de acesso por design — como fundação técnica verificável e rastreável.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-ATB — Architecture & Trust Boundaries | Zonas de confiança, fronteiras e superfícies de ataque por design (primário) |
| ACO-ITS — Integration Trust & Service-to-Service Security | Integrações entre serviços e padrões de confiança inter-serviço (secundário) |
| ACO-IAT — Identity, Access & Session Trust | Autenticação e autorização por design; princípio do menor privilégio |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento de requisito canónico. "Parcial" = sem unit dedicado no capítulo.

| Framework | Requisito / Prática | Cobertura | Fonte verificada | Nota |
|-----------|--------------------|-----------|-----------------|----|
| SSDF PW.2 | Review the Software Design | ✅ Semântico | aplicacao_lifecycle (strong): US-03 — Revisão formal do design arquitetural | Revisão de arquitetura como disciplina de security review |
| ASVS authorization_and_least_privilege | Authorization & least privilege | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Presente; não embalado explicitamente como family ASVS |
| ASVS backend_component_authentication | Backend component auth | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Architecture e infra semantics |
| ASVS backend_least_privilege | Backend least privilege | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Presente; não embalado |
| ASVS architecture_and_dependency_hardening | Architecture hardening | ⚠️ Parcial | addon (medium): Modelos de Arquitetura Segura Reutilizáveis | Presente; embalagem mais específica necessária |
| ASVS identity_provider_and_federated_auth | Federated authentication | ⚠️ Parcial | addon (medium): Rastreabilidade Arquitetural | OAuth/OIDC semantics presentes |
| ASVS oauth_and_oidc_service_trust | OAuth & OIDC trust | ⚠️ Parcial | addon (medium): Rastreabilidade Arquitetural | Architecture e deploy semantics |
| ASVS secure_transport | Secure transport | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Architecture e deploy semantics |
| ASVS service_to_service_auth | Service-to-service auth | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Architecture e IaC |
| ASVS session_and_token_trust | Session & token trust | ⚠️ Parcial | addon (medium): Rastreabilidade Arquitetural | Architecture e deploy |
| ASVS frontend_browser_security | Frontend/browser security | ⚠️ Parcial | addon (medium): Modelos de Arquitetura Segura Reutilizáveis | Requirements e architecture |
| ASVS api_protocol_specific | API protocol specifics | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Architecture e deploy |
| CIS-4 | Secure Configuration of Enterprise Assets | ⚠️ Parcial | addon (medium): Plano de Validação Arquitetural | Semantics presentes; CIS inclui hardening empresarial além do âmbito |
| SLSA-BUILD-L3 | Hardened builds | ⚠️ Parcial | aplicacao_lifecycle (strong): US-07 — Validação arquitetural automatizável no CI/CD | Isolation semantics de arquitetura |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota:** Este capítulo é o mais referenciado pelos pilots MCP e ASVS em cobertura parcial. Não há gap de conteúdo — a pressão é de embalagem e referenciação cruzada mais explícita.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — zonas de confiança e validações proporcionais ao risco
- **Cap. 02** — requisitos de arquitetura derivados dos REQ-XXX
- **Cap. 03** — arquitetura segura como output primário de threat modeling
- **Cap. 09** — arquitetura lógica sustenta modelo de segmentação de containers
- **Cap. 10** — arquitetura é input principal de testes estruturais
