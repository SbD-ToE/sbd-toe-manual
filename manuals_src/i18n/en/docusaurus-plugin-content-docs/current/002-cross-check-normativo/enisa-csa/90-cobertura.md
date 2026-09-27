---
id: cobertura
title: "Coverage — Cybersecurity Act (CSA)"
description: "Generated view: what the Manual covers, the declared gaps and what stays out of scope, from the coverage matrix of the Cybersecurity Act (CSA)."
sidebar_position: 90
tags: [cross-check, enisa-csa, cobertura, gerado]
sbdtoe_generated: reg-requirements-view
derived_from:
  - 002-cross-check-normativo/_matriz/csa.yaml
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/enisa-csa/90-cobertura.md
  source_sha256: 862187fbc03e2a6081625a140e32bd4aff0a0ca2a0d3341b34371edee56cf8d5
  source_commit: null
  target_sha256: c23bed8d15768bcd83b3b5b3d79194fcdaae72b562e54e1156ea29a9a2a0880a
  engine: gen_reg_views
  prompt_sha256: null
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: []
  glossary_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
  translated_at: 2026-09-27T00:00:00Z
  stamped_at: 2026-09-27T00:00:00Z
  reviewed_by: null
---

# Coverage: Cybersecurity Act (CSA)

> **Generated page**, produced by `scripts/gen_reg_views.py` from the matrix `002-cross-check-normativo/_matriz/csa.yaml`. It is not edited by hand. This regime has no context in the regulatory overlay (it neither elevates nor adds requirements); it answers only in the three categories.

## What this Manual covers and what stays out {#cobertura}

All the obligations of the matrix `_matriz/csa.yaml` in three categories: what the Manual **covers**, and in what form; the **declared gaps** (what it does not cover by omission); and what is **out of scope**, with the reason. Generated from the matrix; no obligation is left in silence. The 19 obligations addressed to the authorities create no duty for the organisation and are not listed.

### Covers (32) {#cobre}

Strength “covers” or “supports evidence”. The form is the Manual's response: catalogue requirement, policy, section, floor or requirement added by the regime.

| Obligation | Reference | Strength | Form |
|---|---|---|---|
| CSA-51-a | Article 51, point (a) | Covers | `ENC-001`; `ENC-002`; `ACC-001`; `ACC-006` |
| CSA-51-c | Article 51, point (c) | Covers | `ACC-001`; `ACC-002`; `ACC-003` |
| CSA-51-d | Article 51, point (d) | Covers | `DEP-001`; `DEP-010`; [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| CSA-51-e | Article 51, point (e) | Covers | `LOG-001`; `LOG-002`; `OPS-002` |
| CSA-51-f | Article 51, point (f) | Covers | `LOG-003`; [Policy 29 §8](/sbd-toe/assets/policies/policy-logging-estruturado#8-integridade-e-imutabilidade) |
| CSA-51-g | Article 51, point (g) | Covers | `DEP-002`; `DPL-003`; `TST-005`; [Policy 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go) |
| CSA-51-i | Article 51, point (i) | Covers | [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `CFG-001`; `THR-001` |
| CSA-51A-a | Article 51a, point (a) | Supports evidence | `TRN-001`; `GOV-001` |
| CSA-51A-b | Article 51a, point (b) | Supports evidence | `GOV-001`; `GOV-010` |
| CSA-51A-c | Article 51a, point (c) | Covers | `ENC-001`; `ENC-002`; `ACC-006` |
| CSA-51A-e | Article 51a, point (e) | Covers | `ACC-001`; `ACC-002` |
| CSA-51A-f | Article 51a, point (f) | Covers | `LOG-001`; `LOG-002`; `LOG-003` |
| CSA-52-1 | Article 52(1) | Supports evidence | `CLA-001`; `CLA-003` |
| CSA-52-6 | Article 52(6) | Supports evidence | `DEP-002`; [Policy 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `TST-002`; `TST-005`; [Policy 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release) |
| CSA-52-7 | Article 52(7) | Supports evidence | `TST-008` |
| CSA-53-3 | Article 53(3) | Supports evidence | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Policy 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta) |
| CSA-55-1-c | Article 55(1), point (c) | Covers | `GOV-015` |
| CSA-56-7 | Article 56(7) | Supports evidence | [Policy 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release); [Policy 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta); `ARC-010` |
| CSA-56-8 | Article 56(8) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| CSA-EUCC-7-1 | Article 7(1) | Supports evidence | `TST-001`; `TST-008`; `CIC-005`; `ARC-004` |
| CSA-EUCC-8-2 | Article 8(2) | Supports evidence | `ARC-010`; `ARC-004`; [Policy 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta); `CIC-005` |
| CSA-EUCC-8-5 | Article 8(5) | Supports evidence | `DEP-001` |
| CSA-EUCC-8-6-b | Article 8(6), point (b) | Covers | [Policy 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias); [Policy 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal); `DEP-010`; `GOV-015` |
| CSA-EUCC-9-2-e | Article 9(2), point (e) | Covers | [Policy 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto); `DPL-002`; `CIC-007` |
| CSA-EUCC-27-1-a | Article 27(1), point (a) | Covers | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Ch. 05 US-11](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados); `DEP-002`; [KEV — confirmed exploitation](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#kev--exploração-confirmada); `GOV-015` |
| CSA-EUCC-27-1-b | Article 27(1), point (b) | Supports evidence | [Policy 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica); `GOV-010`; [Policy 04 §1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#1-objetivo) |
| CSA-EUCC-33-2 | Article 33(2) | Covers | `GOV-015` |
| CSA-EUCC-33-5 | Article 33(5) | Supports evidence | `DEP-010`; [Policy 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias) |
| CSA-EUCC-35-7 | Article 35(7) | Covers | [Policy 12 §6.2](/sbd-toe/assets/policies/policy-excecoes-cve#62-reavaliação); [Policy 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação) |
| CSA-EUCC-36 | Article 36 | Supports evidence | `TST-003`; `DEP-010`; `TST-006` |
| CSA-EUCC-AnxIV-2-1 | Annex IV, point IV.2, (1) | Supports evidence | [Policy 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica); `CLA-004` |
| CSA-EUCC-AnxIV-3-1 | Annex IV, point IV.3, (1) | Supports evidence | `ARC-009`; [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) |

### Declared gap (26) {#lacuna}

Strength “partial” or “gap”: the Manual does not cover, or covers only in part, and says what is missing. Gaps pending an AppSec Core round are marked with the name of the round.

| Obligation | Reference | Strength | How the Manual responds | What is missing |
|---|---|---|---|---|
| CSA-51-b | Article 51, point (b) | Partial | `ENC-009`; `LOG-003`; `DPL-005`; [Policy 27 §3.3](/sbd-toe/assets/policies/policy-rollback#33-rollback-de-base-de-dados) | Integrity and rollback prescribed; data backups with tested restore are missing (see RGPD-32-1-c). |
| CSA-51-h | Article 51, point (h) | Partial | `DPL-005`; [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); `OPS-015` | Recovery and rollback prescribed; no backups with RPO/RTO and restore tests. |
| CSA-51-j | Article 51, point (j) | Partial | `DEP-002`; [Policy 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `DST-003`; `DPL-002` | No known vulnerabilities at release and integrity of artefacts; the secure update mechanism in the product delivered to the user is prescribed only for CRA products (CTX-CRA-R02); there is no CSA context. |
| CSA-51A-d | Article 51a, point (d) | Partial | `DPL-005`; [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) | No tested backups/restore. |
| CSA-51A-g | Article 51a, point (g) | Partial | `DEP-002`; [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura) | Applies to own products; does not require that third-party ICT tools used in providing the service be assessed as secure by design and free of known vulnerabilities. |
| CSA-55-1-a | Article 55(1), point (a) | Gap | — | No guidance on secure configuration, installation, deployment, operation and maintenance for end users (gap identical to that of the CRA, Annex II, point (8)(a)). |
| CSA-55-1-b | Article 55(1), point (b) | Gap | — | No definition or publication of the security support period (the Manual only uses “support period” as a CRA retention reference). |
| CSA-55-1-d | Article 55(1), point (d) | Gap | [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) | No public reference to the product's vulnerability repositories nor security advisories; there is only the security section of the technical changelog (L2/L3). |
| CSA-55-2 | Article 55(2) | Gap | — | No supplementary information published, hence no rule on electronic format and updating until expiry. |
| CSA-EUCC-8-6-a | Article 8(6), point (a) | Gap | — | Depends on the supplementary information of Article 55, which the Manual does not provide for (CSA-55-1-a…d). |
| CSA-EUCC-8-7 | Article 8(7) | Partial | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) | The Manual's retention periods (max. 3 years at L3) are shorter than 5 years after expiry; the precedence clause makes the EUCC period prevail, but the retention map does not identify it. |
| CSA-EUCC-33-1 | Article 33(1) | Partial | [Policy 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias); [Policy 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal); `TST-003`; `DEP-010`; `GOV-015` | Internal process and reception of external reports prescribed (TST-003, GOV-015); no explicit alignment with EN ISO/IEC 30111. |
| CSA-EUCC-33-3 | Article 33(3) | Partial | [Policy 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação); [Policy 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal); `DEP-010` | Recording and triage of detected vulnerabilities (tests, SCA) prescribed; those reported by third parties have no entry point. |
| CSA-EUCC-33-4 | Article 33(4) | Partial | `DST-007` | Notification to dependants is provided for only for compromised versions (DST-007); not for vulnerabilities affecting composite products with their own certificate. |
| CSA-EUCC-34-1 | Article 34(1) | Partial | [Policy 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação); [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); [Integration into remediation prioritisation](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#integração-na-priorização-de-remediação) | Triage and remediation deadlines according to severity/exploitation (KEV, EPSS); the analysis is not referred to the target of evaluation nor to the certificate's claims. |
| CSA-EUCC-34-2 | Article 34(2) | Gap | — | No calculation of attack potential according to CC/CEM (the Manual uses CVSS/EPSS/KEV). |
| CSA-EUCC-35-1 | Article 35(1) | Partial | [Policy 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias); [Policy 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal) | There is documented technical justification per CVE/finding; there is no report analysing the impact on conformity with the certificate. |
| CSA-EUCC-35-2 | Article 35(2) | Partial | [Policy 12 §5.1](/sbd-toe/assets/policies/policy-excecoes-cve#51-etapas-obrigatórias); [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); [Integration into remediation prioritisation](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#integração-na-priorização-de-remediação) | Impact, exploitability and mitigation are assessed; proximity/feasibility of the attack in CC terms and the conclusion on remediability with respect to the certificate are missing. |
| CSA-EUCC-35-3 | Article 35(3) | Partial | [Policy 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) | Confidentiality is prescribed for pentest reports (including PoC); not for means of exploitation in vulnerability reports in general nor with limited distribution. |
| CSA-EUCC-39 | Article 39 | Gap | [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) | No public disclosure of fixed vulnerabilities nor entry in the European vulnerability database (NIS2 Article 12). |
| CSA-EUCC-41-1 | Article 41(1) | Gap | — | Depends on the information of Article 55, which does not exist (CSA-55-1-a…d). |
| CSA-EUCC-41-2 | Article 41(2) | Partial | [Policy 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto); [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) | Artefacts immutable and retained, but for 1–2 years (build artefacts/SBOM); keeping a sample of the certified product and the certification records ≥ 5 years after withdrawal is not provided for. |
| CSA-EUCC-AnxIV-3-2 | Annex IV, point IV.3, (2) | Partial | `ARC-004`; `ARC-009`; [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) | Changes described (ADR, changelog) and review upon significant change; identifying changes to the developer's evidence elements and concluding on the impact on assurance are missing. |
| CSA-EUCC-AnxIV-4-4 | Annex IV, point IV.4, (4) | Partial | `DEP-007`; [Policy 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto); `DPL-002`; `TST-006` | Controlled development and release of fixes and regression tests; the technical mechanism for adopting updates in the product and the assessment of their effectiveness are missing. |
| CSA-EUCC-AnxIV-4-5 | Annex IV, point IV.4, (5) | Partial | `DPL-002`; `DST-003` | Integrity and provenance of update artefacts verifiable; no description of the procedure nor separation of the TOE boundaries. |
| CSA-EUCC-AnxIV-4-6 | Annex IV, point IV.4, (6) | Gap | — | No certification-aware corrective update route (classification outside the TOE / minor change / critical vulnerability and submission to the ITSEF within 5 working days). |

### Out of scope (22) {#fora-de-ambito}

Obligations that the Manual declares out of scope, with the reason.

| Obligation | Reference | Reason |
|---|---|---|
| CSA-53-1 | Article 53(1) | Provision on the architecture of the certification scheme (self-assessment, levels, withdrawal); does not create an engineering duty. |
| CSA-53-2 | Article 53(2) | EU statement of conformity and assumption of responsibility: legal plane of conformity. |
| CSA-EUCC-6 | Article 6 | Provision on the architecture of the certification scheme (self-assessment, levels, withdrawal); does not create an engineering duty. |
| CSA-EUCC-8-1 | Article 8(1) | Formal relationship with the certification body/ITSEF/national authority (certification plane), outside the scope of an engineering manual; the ENISA/CSA cross-check refers it to the certification dossier. |
| CSA-EUCC-9-2-a | Article 9(2), point (a) | Formal relationship with the certification body/ITSEF/national authority (certification plane), outside the scope of an engineering manual; the ENISA/CSA cross-check refers it to the certification dossier. |
| CSA-EUCC-9-2-b | Article 9(2), point (b) | Promotion, mark and label of the certificate: legal-commercial plane of certification. |
| CSA-EUCC-9-2-c | Article 9(2), point (c) | Promotion, mark and label of the certificate: legal-commercial plane of certification. |
| CSA-EUCC-9-2-d | Article 9(2), point (d) | Promotion, mark and label of the certificate: legal-commercial plane of certification. |
| CSA-EUCC-9-2-f | Article 9(2), point (f) | Promotion, mark and label of the certificate: legal-commercial plane of certification. |
| CSA-EUCC-11-1 | Article 11(1) | Promotion, mark and label of the certificate: legal-commercial plane of certification. |
| CSA-EUCC-11-2 | Article 11(2) | Promotion, mark and label of the certificate: legal-commercial plane of certification. |
| CSA-EUCC-11-3 | Article 11(3) | Promotion, mark and label of the certificate: legal-commercial plane of certification. |
| CSA-EUCC-11-4 | Article 11(4) | Promotion, mark and label of the certificate: legal-commercial plane of certification. |
| CSA-EUCC-16 | Article 16 | Certification of protection profiles: an activity of those who develop profiles, not of the product engineering process. |
| CSA-EUCC-27-2 | Article 27(2) | Formal relationship with the certification body/ITSEF/national authority (certification plane), outside the scope of an engineering manual; the ENISA/CSA cross-check refers it to the certification dossier. |
| CSA-EUCC-28-3 | Article 28(3) | Formal relationship with the certification body/ITSEF/national authority (certification plane), outside the scope of an engineering manual; the ENISA/CSA cross-check refers it to the certification dossier. |
| CSA-EUCC-29-1 | Article 29(1) | Formal relationship with the certification body/ITSEF/national authority (certification plane), outside the scope of an engineering manual; the ENISA/CSA cross-check refers it to the certification dossier. |
| CSA-EUCC-30-3 | Article 30(3) | Communication of the certificate's suspension to purchasers and the public: legal-commercial plane of certification. |
| CSA-EUCC-35-4 | Article 35(4) | Formal relationship with the certification body/ITSEF/national authority (certification plane), outside the scope of an engineering manual; the ENISA/CSA cross-check refers it to the certification dossier. |
| CSA-EUCC-35-6 | Article 35(6) | Provision on the architecture of the certification scheme (self-assessment, levels, withdrawal); does not create an engineering duty. |
| CSA-EUCC-41-3 | Article 41(3) | Joint retention of certificate documentation: documentary plane of certification. |
| CSA-EUCC-41-4 | Article 41(4) | Formal relationship with the certification body/ITSEF/national authority (certification plane), outside the scope of an engineering manual; the ENISA/CSA cross-check refers it to the certification dossier. |
