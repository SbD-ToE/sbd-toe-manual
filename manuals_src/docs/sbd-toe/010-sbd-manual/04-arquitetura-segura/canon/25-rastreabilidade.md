---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 04: Arquitetura Segura"
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
| ASVS v4 | ASVS4-REQ-V1.4.1 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Landing zone ACO-IAT-001 confirmado; cross-ref ASVS específico agora exposto |
| ASVS v4 | ASVS4-REQ-V1.4.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Landing zone ACO-IAT-001 confirmado; cross-ref ASVS específico agora exposto |
| ASVS v4 | ASVS4-REQ-V1.4.3 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Landing zone ACO-IAT-001 confirmado; cross-ref ASVS específico agora exposto |
| ASVS v4 | ASVS4-REQ-V1.4.4 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Landing zone ACO-IAT-001 confirmado; cross-ref ASVS específico agora exposto |
| ASVS v4 | ASVS4-REQ-V1.10.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Accountability e rastreabilidade arquitetural publicados; cross-ref ASVS específico agora exposto |
| ASVS v4 | ASVS4-REQ-V2.3.3 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication lifecycle e trust controls revistos ao nível de arquitetura |
| ASVS v4 | ASVS4-REQ-V2.7.4 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication lifecycle e trust controls revistos ao nível de arquitetura |
| ASVS v4 | ASVS4-REQ-V2.8.1 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication lifecycle e trust controls revistos ao nível de arquitetura |
| ASVS v4 | ASVS4-REQ-V2.8.4 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication lifecycle e trust controls revistos ao nível de arquitetura |
| ASVS v4 | ASVS4-REQ-V2.8.7 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication lifecycle e trust controls revistos ao nível de arquitetura |
| ASVS v4 | ASVS4-REQ-V2.9.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication lifecycle e trust controls revistos ao nível de arquitetura |
| ASVS v4 | ASVS4-REQ-V4.2.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Controlos de fronteira e proteção de fluxos autenticados já existem; cross-ref agora publicado |
| ASVS v4 | ASVS4-REQ-V4.3.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Exposição externa minimizada e fronteiras de confiança já cobertas no catálogo ARC |
| ASVS v4 | ASVS4-REQ-V5.1.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Superfície de entrada e controlo de fronteiras já cobertos no catálogo ARC |
| ASVS v4 | ASVS4-REQ-V5.1.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Superfície de entrada e controlo de fronteiras já cobertos no catálogo ARC |
| ASVS v4 | ASVS4-REQ-V6.1.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Domínios sensíveis, isolamento e proteção estrutural já cobertos no catálogo ARC |
| ASVS v4 | ASVS4-REQ-V7.2.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Logging de decisões de acesso surge na revisão de trust boundaries e controlos por integração |
| ASVS v4 | ASVS4-REQ-V7.4.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Robustez estrutural e tratamento seguro de fluxos já cobertos no catálogo ARC |
| ASVS v4 | ASVS4-REQ-V8.1.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Minimização de exposição e de superfícies já cobertas no catálogo ARC |
| ASVS v4 | ASVS4-REQ-V8.2.3 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Session trust e proteção de dados autenticados revistos nas fronteiras de confiança |
| ASVS v4 | ASVS4-REQ-V10.2.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Exposição indevida de dados e capacidades ocultas entram no controlo estrutural da arquitetura |
| ASVS v4 | ASVS4-REQ-V10.2.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Exposição indevida de dados e capacidades ocultas entram no controlo estrutural da arquitetura |
| ASVS v4 | ASVS4-REQ-V10.2.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Exposição indevida de dados e capacidades ocultas entram no controlo estrutural da arquitetura |
| ASVS v4 | ASVS4-REQ-V12.4.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Isolamento de componentes e minimização de exposição já cobertos no catálogo ARC |
| ASVS v4 | ASVS4-REQ-V13.4.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authorization by design já revisto nas integrações e trust boundaries do capítulo |
| ASVS v5 | ASVS-REQ-V6.1.1 — V6.1.1 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.1.2 — V6.1.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.1.3 — V6.1.3 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.1 — V6.2.1 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.2 — V6.2.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.3 — V6.2.3 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.4 — V6.2.4 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.5 — V6.2.5 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.6 — V6.2.6 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.7 — V6.2.7 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.8 — V6.2.8 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.9 — V6.2.9 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.10 — V6.2.10 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.11 — V6.2.11 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.2.12 — V6.2.12 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.3.1 — V6.3.1 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.3.2 — V6.3.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.3.3 — V6.3.3 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.3.4 — V6.3.4 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.3.5 — V6.3.5 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.3.6 — V6.3.6 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.3.7 — V6.3.7 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.3.8 — V6.3.8 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.4.1 — V6.4.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Authentication lifecycle, renewal e recovery semantics já entram nos triggers de atualização e rastreabilidade arquitetural |
| ASVS v5 | ASVS-REQ-V6.4.2 — V6.4.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Authentication lifecycle, renewal e recovery semantics já entram nos triggers de atualização e rastreabilidade arquitetural |
| ASVS v5 | ASVS-REQ-V6.4.3 — V6.4.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Authentication lifecycle, renewal e recovery semantics já entram nos triggers de atualização e rastreabilidade arquitetural |
| ASVS v5 | ASVS-REQ-V6.4.4 — V6.4.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Authentication lifecycle, renewal e recovery semantics já entram nos triggers de atualização e rastreabilidade arquitetural |
| ASVS v5 | ASVS-REQ-V6.4.5 — V6.4.5 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Authentication lifecycle, renewal e recovery semantics já entram nos triggers de atualização e rastreabilidade arquitetural |
| ASVS v5 | ASVS-REQ-V6.4.6 — V6.4.6 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Authentication lifecycle, renewal e recovery semantics já entram nos triggers de atualização e rastreabilidade arquitetural |
| ASVS v5 | ASVS-REQ-V6.5.1 — V6.5.1 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.5.2 — V6.5.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.5.3 — V6.5.3 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.5.4 — V6.5.4 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.5.5 — V6.5.5 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.5.6 — V6.5.6 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.5.7 — V6.5.7 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.5.8 — V6.5.8 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.6.1 — V6.6.1 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.6.2 — V6.6.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.6.3 — V6.6.3 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.6.4 — V6.6.4 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.7.1 — V6.7.1 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.7.2 — V6.7.2 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Authentication strength and identity-assurance semantics já revistas nas trust boundaries e integrações do capítulo |
| ASVS v5 | ASVS-REQ-V6.8.1 — V6.8.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V6.8.2 — V6.8.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V6.8.3 — V6.8.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V6.8.4 — V6.8.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.1.1 — V7.1.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.1.2 — V7.1.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.1.3 — V7.1.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.2.1 — V7.2.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.2.2 — V7.2.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.2.3 — V7.2.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.2.4 — V7.2.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.3.1 — V7.3.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.3.2 — V7.3.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.4.1 — V7.4.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.4.2 — V7.4.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.4.3 — V7.4.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.4.4 — V7.4.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.4.5 — V7.4.5 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.5.1 — V7.5.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.5.2 — V7.5.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.5.3 — V7.5.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.6.1 — V7.6.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V7.6.2 — V7.6.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.1.1 — V8.1.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.1.2 — V8.1.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.1.3 — V8.1.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.1.4 — V8.1.4 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.2.1 — V8.2.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.2.2 — V8.2.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.2.3 — V8.2.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.2.4 — V8.2.4 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.3.1 — V8.3.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.3.2 — V8.3.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.3.3 — V8.3.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.4.1 — V8.4.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V8.4.2 — V8.4.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V9.1.1 — V9.1.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V9.1.2 — V9.1.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V9.1.3 — V9.1.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V9.2.1 — V9.2.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V9.2.2 — V9.2.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V9.2.3 — V9.2.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V9.2.4 — V9.2.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Session e token trust-boundary semantics já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.1.1 — V10.1.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.1.2 — V10.1.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.2.1 — V10.2.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.2.2 — V10.2.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.2.3 — V10.2.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.3.1 — V10.3.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.3.2 — V10.3.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.3.3 — V10.3.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.3.4 — V10.3.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.3.5 — V10.3.5 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.1 — V10.4.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.2 — V10.4.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.3 — V10.4.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.4 — V10.4.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.5 — V10.4.5 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.6 — V10.4.6 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.7 — V10.4.7 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.8 — V10.4.8 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.9 — V10.4.9 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.10 — V10.4.10 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.11 — V10.4.11 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.12 — V10.4.12 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.13 — V10.4.13 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.14 — V10.4.14 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.15 — V10.4.15 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.4.16 — V10.4.16 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.5.1 — V10.5.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.5.2 — V10.5.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.5.3 — V10.5.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.5.4 — V10.5.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.5.5 — V10.5.5 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.6.1 — V10.6.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.6.2 — V10.6.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.7.1 — V10.7.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.7.2 — V10.7.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V10.7.3 — V10.7.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Federated identity, caller trust e service-boundary enforcement já presentes na rastreabilidade arquitetural; cross-ref ASVS específico agora exposto |
| ASVS v5 | ASVS-REQ-V13.2.2 — V13.2.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy e least-privilege semantics já presentes no catálogo ARC; cross-ref ASVS específico agora exposto |
| CIS v8.1.2 | CIS-5 — Account Management | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Account inventory, revocation e ownership-change semantics já entram nos critérios de actualização e disciplina de revisão arquitetural |
| CIS v8.1.2 | CIS-5.1 — Establish and Maintain an Inventory of Accounts | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Account inventory, revocation e ownership-change semantics já entram nos critérios de actualização e disciplina de revisão arquitetural |
| CIS v8.1.2 | CIS-5.5 — Establish and Maintain an Inventory of Service Accounts | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Account inventory, revocation e ownership-change semantics já entram nos critérios de actualização e disciplina de revisão arquitetural |
| CIS v8.1.2 | CIS-6.6 — Establish and Maintain an Inventory of Authentication and Authorization Systems | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural > Critérios de actualização | Account inventory, revocation e ownership-change semantics já entram nos critérios de actualização e disciplina de revisão arquitetural |
| CIS v8.1.2 | CIS-12.5 — Centralize Network Authentication, Authorization, and Auditing (AAA) | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| CIS v8.1.2 | CIS-13.5 — Manage Access Control for Remote Assets | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| CIS v8.1.2 | CIS-14.2 — Train Workforce Members to Recognize Social Engineering Attacks | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Identity, authentication and access-boundary semantics já revistos nas trust boundaries e integrações do capítulo |
| CIS v8.1.2 | CIS-14.3 — Train Workforce Members on Authentication Best Practices | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Identity, authentication and access-boundary semantics já revistos nas trust boundaries e integrações do capítulo |
| HIPAA | HIPAA-164-308a4 — Information Access Management | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Compliance/regulatory packaging de identity and authentication controls já está suportado na revisão de trust boundaries do capítulo |
| HIPAA | HIPAA-164-312a1 — Access Control | 🔧 Reparação | intro (strong): 📜 Políticas Organizacionais Relevantes | Compliance/regulatory packaging de governance and policy para identity/access control já está suportado nas políticas organizacionais relevantes do capítulo |
| HIPAA | HIPAA-164-312d — Person or Entity Authentication | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Compliance/regulatory packaging de identity and authentication controls já está suportado na revisão de trust boundaries do capítulo |
| MCP Official | MCP-AUTH-SCOPE-NEGOTIATION | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| MCP Official | MCP-SCOPE-MINIMIZATION | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-1 | 🔧 Reparação | intro (strong): 📜 Políticas Organizacionais Relevantes | Governance and policy packaging para identity/access control já está suportado nas políticas organizacionais relevantes do capítulo |
| NIST SP800-53 | SP800-53-AC-8 | 🔧 Reparação | aplicacao_lifecycle (strong): US-05 — Revisão de fronteiras de confiança e integrações | Identity, authentication and access-boundary semantics já revistos nas trust boundaries e integrações do capítulo |
| NIST SP800-53 | SP800-53-AC-9 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Access-event accountability, review e evidência auditável já entram na rastreabilidade arquitetural do capítulo |
| NIST SP800-53 | SP800-53-AC-9.1 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Access-event accountability, review e evidência auditável já entram na rastreabilidade arquitetural do capítulo |
| NIST SP800-53 | SP800-53-AC-9.2 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Access-event accountability, review e evidência auditável já entram na rastreabilidade arquitetural do capítulo |
| NIST SP800-53 | SP800-53-AC-9.3 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Access-event accountability, review e evidência auditável já entram na rastreabilidade arquitetural do capítulo |
| NIST SP800-53 | SP800-53-AC-9.4 | 🔧 Reparação | addon (medium): Rastreabilidade Arquitetural | Access-event accountability, review e evidência auditável já entram na rastreabilidade arquitetural do capítulo |
| NIST SP800-53 | SP800-53-AC-14 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-14.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-15 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.4 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.5 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.6 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.7 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.8 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.9 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-16.10 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-19 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-19.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-19.2 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-19.3 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-19.4 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-AC-19.5 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-IA-1 | 🔧 Reparação | intro (strong): 📜 Políticas Organizacionais Relevantes | Governance and policy packaging para identity/access control já está suportado nas políticas organizacionais relevantes do capítulo |
| NIST SP800-53 | SP800-53-SA-21 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-SA-21.1 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
| NIST SP800-53 | SP800-53-SC-41 | 🔧 Reparação | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Authorization-policy, least-privilege e access-rule semantics já presentes no catálogo ARC; cross-ref específico agora exposto |
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
