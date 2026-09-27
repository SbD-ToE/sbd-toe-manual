---
id: intro
title: ENISA/CSA Certification (EUCC, EUCS, EU5G) - Framing Note
description: When to use it and how to map it to SbD-ToE (evidence, decision and reuse)
tags: [certificacao, enisa, csa, eucc, eucs, eu5g, procurement]
sidebar_position: 9
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/enisa-csa/01-intro.md
  source_sha256: 25549f953174aec799b59160752dfb45d53042b434f696f2db8ae59e7b710226
  source_commit: be49273442123786a27c269d98751832652acabb
  target_sha256: 0897dc1e480003fb4054f47ead7578de93385bf0746774a194647e96aef85348
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, cra_pde, csa_assurance_level, csa_certification_scheme, esquema_regime, eu_ce_marking, layer, mapping, maturity, practitioner_manual, requirement_runtime, role_procurement, sbdtoe_sbd, schema, traceability]
  glossary_sha256: adee14336371e09a6aa3ffbea429a07e1d77ba52180aa9766019790067b5cb10
  translated_at: 2026-09-26T23:27:17Z
  stamped_at: 2026-09-26T23:27:17Z
  reviewed_by: null
---

# ENISA/CSA certification: when to use it and how to map it to SbD‑ToE

> See also: [CRA](/sbd-toe/cross-check-normativo/cra/intro), [DORA](/sbd-toe/cross-check-normativo/dora/intro), [NIS2](/sbd-toe/cross-check-normativo/nis2/intro) and the [DORA & NIS2 Convergence Note](/sbd-toe/cross-check-normativo/dora/convergencia-dora).

## Scope {#âmbito}

### 🏛️ ENISA and the Cybersecurity Act (CSA) {#️-enisa-e-cybersecurity-act-csa}

The **Cybersecurity Act** is **Regulation (EU) 2019/881** (CELEX: [32019R0881](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019R0881)), which:

- strengthens the mandate of **ENISA** as the European Union Agency for Cybersecurity; and
- establishes a **European cybersecurity certification framework** for ICT products, ICT services and ICT processes.

several **European cybersecurity certification schemes** («schemes», in common usage)

- **EUCC** - for ICT products (the evolutionary European successor to the Common Criteria);
- **EUCS** - for cloud computing services;
- **EU5G** - for 5G networks and services.

> 📅 **Status in 2025.**  
> In 2025, the EUCC is at a more mature stage, close to operationalisation, while the EUCS and the EU5G are still at different stages of development and approval.  
> SbD-ToE acknowledges this reality: it uses the schemes as **good-practice references and sources of requirements**, not as a closed list of obligations already in force in every Member State.

From the SbD-ToE perspective, certification under the CSA typically entails:

- a **clear mapping between the security requirements** of the schemes and concrete controls (including technical evidence);
- **robust documentation** of architecture, _threat modelling_, _hardening_, _secure development_ and _testing_;
- repeatable processes for **vulnerability management**, _patching_, monitoring and incident response;
- **clear governance and _ownership_** of assets, pipelines, environments and risk decisions.

The SbD-ToE Manual provides the "engineering layer" that makes it possible to:

- design and operate systems aligned with the assurance levels expected by the schemes (‘basic’, ‘substantial’, ‘high’);
- produce **evidence artefacts** (SBOM, test reports, _runbooks_, traceability matrices) that can be used in conformity assessment processes under the CSA.

---

European cybersecurity certification schemes, under the **Cybersecurity Act (CSA)**, aim at **EU recognition** that products/services meet security requirements. **ENISA** prepares the candidate schemes at the request of the Commission, which adopts them by means of implementing acts; certification is carried out by accredited **conformity assessment bodies (CABs)** and supervised by **national authorities**.

This note explains "who it is for", when it is useful/necessary and how to **reuse SbD‑ToE controls and evidence**.

## Who it is for {#para-quem-se-destina}

- **Manufacturers of ICT products** → **EUCC** scheme (Implementing Regulation (EU) 2024/482; based on the Common Criteria). Assurance levels: «substantial» (AVA_VAN 1–2) and «high» (AVA_VAN 3–5); the EUCC does not provide for the «basic» level.
- **Cloud service providers** → **EUCS** scheme (for cloud services). Levels: Basic, Substantial, High.
- **5G suppliers/operators** → **EU5G** scheme (for 5G networks and components). Levels: aligned with risk.
- **CABs/Laboratories** → apply the criteria of the schemes.
- **National cybersecurity certification authorities** → supervise and enforce the rules of the schemes (and, at the «high» level, issue certificates); ENISA publishes the certificates on its website.
- **Buyers (incl. the public sector)** → use certificates as a procurement criterion.

Notes:
- As a general rule, certification is **voluntary**, unless sectoral legislation, implementing acts or **tender specifications** make it mandatory for certain markets/contracts.
- Certification **does not replace** the **CRA** (CE marking and regulatory obligations for products). It may, however, serve as **strong evidence** of security practices.

## Schemes in focus {#esquemas-em-foco}

### EUCC - ICT products (Common Criteria basis) {#eucc---ict-products-base-common-criteria}
Objective: to demonstrate that an ICT product meets requirements and has been evaluated against a **Target of Evaluation** and **Security Functional/Assurance Requirements**. 
The assurance level affects the **depth of testing** and the **independence**.

### EUCS - Cloud services {#eucs---cloud-services}
Objective: to demonstrate the security controls and governance of cloud services. It covers **risk management, IAM, encryption, operations, continuity**, etc.

### EU5G - 5G networks {#eu5g---redes-5g}
Objective: to demonstrate security requirements for suppliers/operators in the 5G chain (equipment, software, management, supply chain).

## How it relates to DORA/NIS2/CRA {#como-se-relaciona-com-doranis2cra}

- They share the same “technical language” (encryption, IAM, vulnerability management, testing, monitoring, continuity).
- The **CRA** imposes requirements and **CE marking** for products with digital elements; CSA certification can **complement** it as evidence (it does not replace it).
- **NIS2/DORA** demand technical maturity; certification can **speed up audits** and allow **certificates to be accepted as proof** in procurement/regulation.

## Decision trees (simplified) {#árvores-de-decisão-simplificadas}

1) What is my main object?
- ICT product (software/firmware/hardware with SW) → consider **EUCC**
- Cloud service (IaaS/PaaS/SaaS) → consider **EUCS**
- 5G supplier/operator → consider **EU5G**
- Other → CSA certification may not be applicable

2) Is there an external requirement?
- Does a regulator/law/sector require it? → proceed with certification
- Do customers/tenders ask for it? → assess cost/benefit and level (Basic/Substantial/High)
- No requirement? → maintain “readiness” and evidence; decide strategically

3) Which level?
- Low market and risk exposure → Basic/Substantial
- Critical/highly regulated markets → Substantial/High

## SbD‑ToE → Certification mapping (typical evidence) {#mapeamento-sbdtoe--certificação-evidência-típica}

| SbD‑ToE domain | What it demonstrates | CSA relevance |
|-----------------|-----------------|----------------|
| Ch. 02 - Requirements | Minimum policies and controls per level | Documented security criteria |
| Ch. 04 - Architecture | Secure design, IAM, encryption, key management | Functional and design controls |
| Ch. 05 - SBOM/SCA | Component inventory, CVE management | Vulnerability management and supply chain |
| Ch. 06–07 - SDLC/CI‑CD | Gates, review, traceability, SoD | Secure lifecycle and build integrity |
| Ch. 08–09 - IaC/Containers | Secure configurations and runtime | Hardening and consistency |
| Ch. 10–11 - Testing/Release | SAST/DAST/fuzzing; “no‑critical” gate | Effectiveness of controls before release |
| Ch. 12 - Operations | Monitoring, response, continuity | Operational resilience |
| Ch. 13 - Training | Skills and awareness | Organisational capability |
| Ch. 14 - Governance | RACI, suppliers, audit | Management and traceability |

It is suggested to create a **certification dossier** with cross-references (control matrix) between the requirements of the scheme (EUCC/EUCS/EU5G) and SbD‑ToE artefacts.

## Evidence checklist (minimum viable) {#checklist-de-evidências-mínimo-viável}

- [ ] Security policy (version, approval, scope)
- [ ] Architecture and data model (includes IAM/crypto/segregation)
- [ ] SBOM per release + SCA records + patch SLAs
- [ ] Pipelines with gates; build/signing logs, SoD (segregation of duties)
- [ ] Test records (SAST/DAST/fuzzing/pen)
- [ ] Release quality reports and “no‑critical known”
- [ ] Monitoring, runbooks, exercises (incident/DR)
- [ ] Training and records (technical/management)
- [ ] Supplier management (contracts, clauses, assessments)
- [ ] Audited trail (who approved, when, why)

## Useful metrics {#métricas-úteis}

- % of versions with a published SBOM
- MTTP (mean time to patch) by severity
- % of releases blocked by a security gate (and subsequently fixed)
- Test coverage (SAST/DAST/fuzzing) per application
- % of controls mapped to the chosen scheme

## Next steps {#próximos-passos}

1. Confirm the object (product/service) and the external requirement (law/customer).  
2. Select the scheme and target level (Basic/Substantial/High).  
3. Build a requirement→evidence mapping matrix (SbD‑ToE).  
4. Fill gaps (e.g. independence of testing, sampling).  
5. Internal pre‑audit; then select a CAB and schedule the evaluation.  

## References {#referências}

- **Cybersecurity Act**: Regulation (EU) 2019/881 (CELEX: [32019R0881](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019R0881))
- ENISA - Certification scheme pages (EUCC, EUCS, EU5G)
- SbD‑ToE Chapters 01–14; CRA/NIS2/DORA cross‑checks

**Version:** 1.0  
**Date:** November 2025  
**Next review:** May 2026
