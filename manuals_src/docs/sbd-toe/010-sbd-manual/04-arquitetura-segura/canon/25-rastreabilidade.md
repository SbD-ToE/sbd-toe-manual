---
id: rastreabilidade
title: Rastreabilidade — Capítulo 04: Arquitetura Segura
description: Rastreabilidade das práticas de arquitetura segura face a frameworks normativos com pilot formal
tags: [rastreabilidade, arquitetura, ssdf, asvs, slsa, cis]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 04: Arquitetura Segura

Este capítulo define **padrões de arquitetura segura** — zonas de confiança, separação de funções, controlo de acesso por design — como fundação técnica verificável e rastreável.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-ATB — Attack Surface & Threat Boundaries | Zonas de confiança, fronteiras e superfícies de ataque por design |
| ACO-IAT — Identity, Access & Trust | Autenticação e autorização por design; princípio do menor privilégio |
| ACO-SCBI — Secure Coding & Build Integrity | Padrões de arquitetura como input de design de código seguro |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PW.2 | Review the Software Design | ✅ Semântico | Revisão de arquitetura como disciplina de security review |
| ASVS authorization_and_least_privilege | Authorization & least privilege | ⚠️ Parcial | Presente; não embalado explicitamente como family ASVS |
| ASVS backend_component_authentication | Backend component auth | ⚠️ Parcial | Architecture e infra semantics |
| ASVS backend_least_privilege | Backend least privilege | ⚠️ Parcial | Presente; não embalado |
| ASVS architecture_and_dependency_hardening | Architecture hardening | ⚠️ Parcial | Presente; embalagem mais específica necessária |
| ASVS identity_provider_and_federated_auth | Federated authentication | ⚠️ Parcial | OAuth/OIDC semantics presentes |
| ASVS oauth_and_oidc_service_trust | OAuth & OIDC trust | ⚠️ Parcial | Architecture e deploy semantics |
| ASVS secure_transport | Secure transport | ⚠️ Parcial | Architecture e deploy semantics |
| ASVS service_to_service_auth | Service-to-service auth | ⚠️ Parcial | Architecture e IaC |
| ASVS session_and_token_trust | Session & token trust | ⚠️ Parcial | Architecture e deploy |
| ASVS frontend_browser_security | Frontend/browser security | ⚠️ Parcial | Requirements e architecture |
| ASVS api_protocol_specific | API protocol specifics | ⚠️ Parcial | Architecture e deploy |
| CIS-4 | Secure Configuration of Enterprise Assets | ⚠️ Parcial | Semantics presentes; CIS inclui hardening empresarial além do âmbito |
| SLSA-BUILD-L3 | Hardened builds | ⚠️ Parcial | Isolation semantics de arquitetura |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota:** Este capítulo é o mais referenciado pelos pilots MCP e ASVS em cobertura parcial. Não há gap de conteúdo — a pressão é de embalagem e referenciação cruzada mais explícita.

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Design → Security Architecture |
| OWASP DSOMM | Design & Development |
| BSIMM13 | Architecture Analysis (AA1–AA3) |

---

## Ligações com outros capítulos

- **Cap. 01** — zonas de confiança e validações proporcionais ao risco
- **Cap. 02** — requisitos de arquitetura derivados dos REQ-XXX
- **Cap. 03** — arquitetura segura como output primário de threat modeling
- **Cap. 09** — arquitetura lógica sustenta modelo de segmentação de containers
- **Cap. 10** — arquitetura é input principal de testes estruturais
