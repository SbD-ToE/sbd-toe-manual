---
id: rastreabilidade
title: Rastreabilidade — Capítulo 08: IaC e Infraestrutura como Código
description: Rastreabilidade das práticas de IaC face a frameworks normativos com pilot formal
tags: [rastreabilidade, iac, infraestrutura, ssdf, slsa, capec, asvs, cis, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 08: IaC e Infraestrutura como Código

Este capítulo define práticas de **infraestrutura definida como código** — validação, enforcement de políticas, gestão de segredos e segregação de ambientes — como camada de enforcement contínuo.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SCBI — Supply Chain & Build Integrity | IaC como código sujeito às mesmas práticas de revisão, validação e controlo de origem de módulos |
| ACO-SPC — Secret Handling, Protected Configuration & Operational Identities | Policy-as-code, OPA/Conftest, gestão de segredos em IaC, enforcement de políticas de segurança |

> **Nota adjunct:** CIS-4 e ASVS `secure_configuration_baseline_gap` têm pressão significativa aqui. IaC tem semantics de configuração segura mas sem secção dedicada a baseline integrity. Candidato ao adjunct `secure_configuration_baseline_integrity` (pendente de promoção).

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF PO.3 | Implement Supporting Toolchains | ✅ Explícito | IaC como toolchain formal e controlado | requirements_catalog (strong): Catálogo IAC — Infraestrutura como Código |
| SSDF PW.3 | Verify Third-Party Software | ✅ Explícito | Módulos IaC externos validados | addon (medium): Governação de Módulos Reutilizáveis em IaC |
| SSDF PW.6 | Configure the Build and Test Environments | ✅ Explícito | Ambientes definidos e validados via IaC | aplicacao_lifecycle (strong): US-02 — Segregação de ambientes, tagging e permissões mínimas |
| SSDF RV.3 | Analyze Vulnerabilities to Root Causes | ✅ Explícito | Análise de vulnerabilidades em IaC; validações automáticas | addon (medium): Validações Automáticas e Controlo de Qualidade no Projeto IaC |
| SLSA-BUILD-L2 | Hosted build platform | ✅ Explícito | IaC e pipeline integrados | aplicacao_lifecycle (strong): US-09 — Assinatura e Proveniência de artefactos IaC |
| SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM | Choose build platform | ⚠️ Parcial | IaC e runners controlados | addon (medium): Planeamento de Execução e Controlo de Estado |
| SLSA-BUILD-PLATFORM-ISOLATION | Isolation strength | ⚠️ Parcial | IaC segmentation semântica | aplicacao_lifecycle (strong): US-02 — Segregação de ambientes |
| CAPEC-511 | Infiltration of Software Development Environment | ⚠️ Parcial | IaC infrastructure compromise | addon (medium): Princípios de Security by Design aplicados a Projetos IaC |
| CIS-4 | Secure Configuration of Enterprise Assets | ⚠️ Parcial | IaC hardening; enterprise config além do âmbito AppSec | addon (medium): Enforcement Contínuo de Políticas e Regras de Segurança em IaC |
| ASVS protected_secret_storage | Secret storage | ⚠️ Parcial | IaC e gestão de cofres | aplicacao_lifecycle (strong): US-10 — Gestão de segredos e identidades para IaC |
| ASVS secret_leak_prevention | Secret leak prevention | ⚠️ Parcial | IaC e prevenção de exposição | addon (medium): Uso de Ferramentas Automatizadas e Assistidas na Autoria de IaC |
| ASVS secret_usage_isolation | Secret usage isolation | ⚠️ Parcial | IaC e isolamento de segredos | aplicacao_lifecycle (strong): US-10 — Gestão de segredos e identidades para IaC |
| ASVS secure_transport | Secure transport | ⚠️ Parcial | IaC e deploy | addon (medium): Exemplos de Estrutura e Práticas Seguras em Projetos IaC |
| ASVS service_to_service_auth | Service-to-service auth | ⚠️ Parcial | IaC | addon (medium): Princípios de Security by Design aplicados a Projetos IaC |
| ASVS secure_configuration_baseline_gap | Secure configuration baseline | ⚠️ Parcial | CLAIM GAP — conteúdo existe no addon `04-principios-sbd-iac.md` (fail securely, privilege minimum, immutability, secure defaults); sem secção dedicada a baseline integrity no catálogo de requisitos | addon (medium): Princípios de Security by Design aplicados a Projetos IaC |
| NIS2 | Infraestrutura como código governada | ✅ Explícito | Overlay regulatório publicado | aplicacao_lifecycle (strong): US-08 — Enforcement automático de políticas |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Modelos de maturidade — pendente de normalização

> ⏳ pendente — Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Implementation → Environment Hardening |
| OWASP DSOMM | Design & Development, Build & Test |
| BSIMM13 | Configuration & Deployment (CD1–CD3) |

---

## Ligações com outros capítulos

- **Cap. 01** — proporcionalidade de validação por risco de ambiente
- **Cap. 02** — requisitos IAC-XXX definidos e validados aqui
- **Cap. 07** — controlos IaC aplicados e orquestrados no pipeline
- **Cap. 09** — containers dependem da infraestrutura provisionada aqui
- **Cap. 14** — exceções técnicas de IaC legitimadas pelo processo de governação
