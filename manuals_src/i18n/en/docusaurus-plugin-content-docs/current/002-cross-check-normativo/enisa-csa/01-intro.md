---
id: intro
title: ENISA/CSA Certification (EUCC, EUCS, EU5G) - Framing Note
description: When to use it and how to map it to SbD-ToE (evidence, decision and reuse)
tags: [certificacao, enisa, csa, eucc, eucs, eu5g, procurement]
sidebar_position: 9
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/enisa-csa/01-intro.md
  source_sha256: 92209b9a40a522f6372b2b3d16b8a77c720736f05e84c2fe9bbc8a95d833a4e5
  source_commit: 5bc57a2de453d4a50f78edcfb2b9546615b20690
  target_sha256: ad46eeb6a82ce6ed9f367469ff762deaafb25034476b3a11aa268d7183e355d2
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, cra_pde, cra_support_period, csa_assurance_level, csa_certification_scheme, esquema_regime, eu_ce_marking, gap_family, layer, mapping, maturity, mcp_reading_programa, piso_limiar, piso_relacao, practitioner_manual, programme_line, requirement_runtime, role_juridico, role_procurement, sbdtoe_sbd, schema, traceability]
  glossary_sha256: da0f05606e22222963e4fb95d6645c47b050f8cadb465ef395ad38c164edfe47
  translated_at: 2026-09-27T23:03:32Z
  stamped_at: 2026-09-27T23:03:32Z
  reviewed_by: null
---

# ENISA/CSA certification: when to use it and how to map it to SbD‑ToE

> See also: [CRA](/sbd-toe/cross-check-normativo/cra/intro), [DORA](/sbd-toe/cross-check-normativo/dora/intro), [NIS2](/sbd-toe/cross-check-normativo/nis2/intro) and the [DORA & NIS2 Convergence Note](/sbd-toe/cross-check-normativo/dora/convergencia-dora).
>
> Obligation-by-obligation coverage: [CSA/EUCC Coverage](/sbd-toe/cross-check-normativo/enisa-csa/cobertura).

## Scope {#âmbito}

### 🏛️ ENISA and the Cybersecurity Act (CSA) {#️-enisa-e-cybersecurity-act-csa}

The **Cybersecurity Act** is **Regulation (EU) 2019/881** (CELEX: [32019R0881](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019R0881)), which:

- strengthens the mandate of **ENISA** as the European Union Agency for Cybersecurity; and
- establishes a **European cybersecurity certification framework** for ICT products, ICT services and ICT processes.

The framework provides for several **European cybersecurity certification schemes** (“schemes”, in common usage), including:

- **EUCC** - for ICT products (the evolutionary European successor to the Common Criteria);
- **EUCS** - for cloud computing services;
- **EU5G** - for 5G networks and services.

> 📅 **Status in 2026.**  
> The EUCC was adopted by Implementing Regulation (EU) 2024/482 and is mapped obligation by obligation in the coverage matrix, together with the CSA (Articles 51 to 56). The EUCS and EU5G are not mapped: they remain as reference, with no coverage answer.

From the SbD-ToE perspective, certification under the CSA typically entails:

- a **clear mapping between the security requirements** of the schemes and concrete controls (including technical evidence);
- **robust documentation** of architecture, _threat modelling_, _hardening_, _secure development_ and _testing_;
- repeatable processes for **vulnerability management**, _patching_, monitoring and incident response;
- **clear governance and _ownership_** of assets, pipelines, environments and risk decisions.

The SbD-ToE Manual provides the "engineering layer" that makes it possible to:

- design and operate systems aligned with the assurance levels defined in each scheme (in the EUCC: substantial and high);
- produce **evidence artefacts** (SBOM, test reports, _runbooks_, traceability matrices) that can be used in conformity assessment processes under the CSA.

---

European cybersecurity certification schemes, under the **Cybersecurity Act (CSA)**, aim at **EU recognition** that products/services meet security requirements. **ENISA** prepares the candidate schemes at the request of the Commission, which adopts them by means of implementing acts; certification is carried out by accredited **conformity assessment bodies (CABs)** and supervised by **national authorities**.

This note explains "who it is for", when it is useful/necessary and how to **reuse SbD‑ToE controls and evidence**.

## What this Manual covers and what stays out {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

The SbD-ToE is centred on the application: requirements, architecture, code, dependencies, pipeline, deployment and operation of the software. For each obligation of the CSA and the EUCC, the Manual answers in one of three categories, and no obligation is left in silence:

- **Covers**, and states how: catalogue requirement, policy, floor or requirement added by the regime, or engineering evidence for a duty that sits on another plane.
- **Declared gap**: what the Manual does not cover by default, stating what is missing.
- **Out of scope**: what the Manual does not deal with, with the reason.

The full list, obligation by obligation, is generated from the coverage matrix and is in [Coverage](./cobertura#cobertura). Where this page and the list diverge, the list prevails.

Certification is voluntary, unless Union or Member State law makes it mandatory (CSA, Article 56(2)). For this reason, this regime has no context in the regulatory overlay: it neither raises nor adds requirements, and answers only in the three categories.

The Manual covers, among others, the security objectives of Article 51 and Article 51a (encryption, access control, logging, SBOM, backups with tested restore and application recovery), the point of contact of Article 55(1)(c) (`GOV-015`) and the incident notification of Article 56(8) ([Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória)).

**Declared gaps, in summary:**
- the supplementary cybersecurity information of Article 55 (secure use guidance, support period, vulnerability repositories and advisories) and the EUCC obligations that depend on it. When the product is also under the CRA, the support period is prescribed by `CTX-CRA-R01`;
- public disclosure of fixed vulnerabilities and registration in the European vulnerability database (EUCC, Article 39); the public advisory on fixed vulnerabilities is prescribed only in the CRA context (`CTX-CRA-R03`);
- calculation of attack potential according to the Common Criteria and the CEM (EUCC, Article 34(2)) and vulnerability analysis referred to the target of evaluation and the certificate (Articles 33 to 35);
- a certification-aware corrective update route (EUCC, Annex IV);
- retention of records for 5 years after the certificate expires (EUCC, Articles 8(7) and 41(2));
- a secure update mechanism in the product delivered to the user, prescribed only for CRA products (`CTX-CRA-R02`), and assessment of the third-party ICT tools used in providing the service (Article 51(j) and Article 51a(g)).

**Out of scope, by programme decision:**
- Security of the entity as a whole (corporate network and administration channels, EDR, patching of operating systems and equipment, inventory and classification of all assets): the Manual is centred on the application.
- Formal relations with the certification body, the ITSEF and the national authority: the certification plane, which this cross-check refers to the certification dossier.
- Promotion, mark and label of the certificate and communication of its suspension: the legal and commercial plane of certification.
- EU statement of conformity and assumption of responsibility (CSA, Article 53(2)): the legal plane of conformity.
- Certification of protection profiles: an activity of whoever develops profiles, not of the product's engineering process.
- Provisions on the architecture of the certification scheme (self-assessment, levels, withdrawal): they create no engineering duty.

## Who it is for {#para-quem-se-destina}

- **Manufacturers of ICT products** → **EUCC** scheme (Implementing Regulation (EU) 2024/482; based on the Common Criteria). Assurance levels: «substantial» (AVA_VAN 1–2) and «high» (AVA_VAN 3–5); the EUCC does not provide for the «basic» level.
- **Cloud service providers** → **EUCS** scheme (for cloud services; not mapped in the matrix).
- **5G suppliers/operators** → **EU5G** scheme (for 5G networks and components). Levels: aligned with risk.
- **CABs/Laboratories** → apply the criteria of the schemes.
- **National cybersecurity certification authorities** → supervise and enforce the rules of the schemes (and, at the «high» level, issue certificates); ENISA publishes the certificates on its website.
- **Buyers (incl. the public sector)** → use certificates as a procurement criterion.

Notes:
- Certification is **voluntary**, unless Union or Member State law makes it mandatory (CSA, Article 56(2)); **tender specifications** may require it by contract.
- Certification **does not exempt** from the obligations of the **CRA** (EU declaration, CE marking, post-market obligations). A European certificate covering essential requirements of Annex I to the CRA gives a presumption of conformity with those requirements (CRA, Article 27(8)); with an assurance level of at least “substantial”, under a scheme specified by delegated act, it removes the need for third-party assessment for the corresponding requirements (CRA, Article 27(9)).

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
- The **CRA** imposes requirements and **CE marking** for products with digital elements; CSA certification can give a presumption of conformity with the essential requirements it covers (CRA, Article 27(8) and (9)), but does not replace the manufacturer's other obligations.
- **NIS2/DORA** demand technical maturity; certification can **speed up audits** and allow **certificates to be accepted as proof** in procurement/regulation.

## Decision trees (simplified) {#árvores-de-decisão-simplificadas}

1) What is my main object?
- ICT product (software/firmware/hardware with SW) → consider **EUCC**
- Cloud service (IaaS/PaaS/SaaS) → consider **EUCS**
- 5G supplier/operator → consider **EU5G**
- Other → CSA certification may not be applicable

2) Is there an external requirement?
- Does a regulator/law/sector require it? → proceed with certification
- Do customers/tenders ask for it? → assess cost/benefit and the assurance level provided for in the scheme (in the EUCC: substantial or high)
- No requirement? → maintain “readiness” and evidence; decide strategically

3) Which level?
- Market and low risk → the lowest level provided for in the scheme (in the EUCC: substantial)
- Critical/highly regulated markets → substantial or high

## SbD‑ToE → Certification mapping (typical evidence) {#mapeamento-sbdtoe--certificação-evidência-típica}

| SbD‑ToE domain | What it demonstrates | CSA relevance |
|-----------------|-----------------|----------------|
| Ch. 02 - Requirements | Minimum policies and controls per level | Documented security criteria |
| Ch. 04 - Architecture | Secure design, IAM, encryption, key management | Functional and design controls |
| Ch. 05 - SBOM/SCA | Component inventory, CVE management | Vulnerability management and supply chain |
| Ch. 06–07 - SDLC/CI‑CD | Gates, review, traceability, SoD | Secure lifecycle and build integrity |
| Ch. 08–09 - IaC/Containers | Secure configurations and runtime | Hardening and consistency |
| Ch. 10–11 - Testing/Release | SAST/DAST/fuzzing; gate with no known vulnerabilities at release (`DEP-002`); the secure update mechanism on the user's side is prescribed only for CRA products | Effectiveness of controls before release |
| Ch. 12 - Operations | Monitoring, response, application recovery and backups with tested restore (`OPS-016`, `OPS-017`) | Operational resilience (the entity's business continuity: out of scope) |
| Ch. 13 - Training | Skills and awareness | Organisational capability |
| Ch. 14 - Governance | RACI, suppliers, audit | Management and traceability |

It is suggested to create a **certification dossier** with cross-references (control matrix) between the requirements of the scheme (EUCC/EUCS/EU5G) and SbD‑ToE artefacts.

## Evidence checklist (minimum viable) {#checklist-de-evidências-mínimo-viável}

- [ ] Security policy (version, approval, scope)
- [ ] Architecture and data model (includes IAM/crypto/segregation)
- [ ] SBOM per release + SCA records + patch SLAs
- [ ] Pipelines with gates; build/signing logs, SoD (segregation of duties)
- [ ] Test records (SAST/DAST/fuzzing/pen)
- [ ] Release quality reports and reports of the gate with no known vulnerabilities at release (`DEP-002`)
- [ ] Monitoring, runbooks, incident exercises and restore tests (`OPS-016`)
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
2. Select the scheme and target level (in the EUCC: substantial or high).  
3. Build a requirement→evidence mapping matrix (SbD‑ToE).  
4. Fill the declared gaps in the [coverage](/sbd-toe/cross-check-normativo/enisa-csa/cobertura) (supplementary information of Article 55, public disclosure of fixed vulnerabilities, CC/CEM attack potential, certification-aware correction route, retention).  
5. Internal pre‑audit; then select a CAB and schedule the evaluation.  

## References {#referências}

- **Cybersecurity Act**: Regulation (EU) 2019/881 (CELEX: [32019R0881](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019R0881))
- ENISA - Certification scheme pages (EUCC, EUCS, EU5G)
- SbD‑ToE Chapters 01–14; CRA/NIS2/DORA cross‑checks

**Version:** 1.1  
**Date:** September 2026 (aligned with the coverage matrix of the CSA and the EUCC)
