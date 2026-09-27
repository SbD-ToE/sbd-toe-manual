---
id: policy-release-seguro
title: Secure Release Policy
description: Organisational policy that defines the requirements for the formal approval of software releases, including a pre-release security checklist, an automated compliance gate, go/no-go criteria, an immutable decision artefact and end-to-end commit→pipeline→release traceability, proportional to the criticality level (L1, L2, L3).
tags: [policy, release, go/no-go, checklist, gate, aprovação, artefacto imutável, rastreabilidade, cap10, cap11, L1, L2, L3, governance]
grupo: pipeline-entrega
sidebar_position: 20
translation:
  source_locale: pt
  source_path: 020-assets/policies/20_policy-release-seguro.md
  source_sha256: cb962889fec6b8feaf79c74e1375d51a9c7926562f76c8ae42bfec5589158afe
  source_commit: dd613d67894f2b585927cbcec942859cd49a4dcb
  target_sha256: d0961a2145074e38afdbd7744ef259f308b04fa48df38938f4ef12b5713cf32a
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [candidate, cycle_iteration, framework_source_corpus, role_tech_lead, sbdtoe_sbd, traceability]
  glossary_sha256: ff0aea7d4dc0b904848dd2e4c716156ed9c048b8e7db11901db5c3e4813a7341
  translated_at: 2026-09-27T13:29:45Z
  stamped_at: 2026-09-27T13:29:45Z
  reviewed_by: null
---

# Secure Release Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **formal approval of software releases**, ensuring that no version is promoted to production without documented evidence of compliance with the applicable security requirements.

A release is a risk decision - not merely a technical operation. Without explicit go/no-go criteria, the decision to promote to production is taken implicitly, by default, with no visibility of the real security status. This policy formalises that process: promotion to production is a deliberate act, with aggregated evidence, recorded approval and assigned accountability.

The objective of this policy is to ensure that:

- Each release has a security checklist that is verified and recorded
- The pre-release security gate is automated and produces a binary result (Approved/Rejected)
- The go/no-go decision is taken by a person with appropriate authority and recorded with identity and timestamp
- The artefact promoted to production is immutable - it is the same one that went through the tests, not a new build
- Commit→pipeline→release traceability is verifiable at any time

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Mandatory; simplified checklist; automated security gates; explicit approval by the Tech Lead, recorded |
| L2 | Mandatory; full checklist; automated gate; formal approval |
| L3 | Mandatory; full checklist; automated gate; dual approval; immutable decision artefact |

---

## 3. Pre-release security gate {#3-gate-de-segurança-pré-release}

The pipeline must include a `release-security-gate` job, run before any promotion to production, that:

- [ ] Aggregates the results of all the security gates of the build cycle (SAST, SCA, DAST, secret detection)
- [ ] Verifies that no blocking finding is open without an approved formal exception
- [ ] Verifies that the SBOM is generated and signed (L2/L3)
- [ ] Verifies that the candidate artefact has a valid signature (L2/L3)
- [ ] Produces a binary result report: **APPROVED** or **REJECTED**
- [ ] Archives the report as an immutable artefact of the release (linked to the tag/version)

The gate does not replace human approval - it blocks promotion if the automated criteria are not met, and provides evidence so that the human approval is informed.

---

## 4. Pre-release security checklist {#4-checklist-de-segurança-pré-release}

Before each release, the following checklist must be completed and archived:

### 4.1 Mandatory criteria {#41-critérios-obrigatórios}

| Criterion | L2 | L3 |
|---|---|---|
| Open Critical findings: 0 (or approved exception) | Mandatory | Mandatory |
| Open High findings: 0 (or approved exception) | Mandatory | Mandatory |
| Open Medium findings without exception | Tolerated with a record | Blocking |
| Secret detection: no open finding | Mandatory | Mandatory |
| SBOM generated and signed for this version | Mandatory | Mandatory |
| Artefact signed and verifiable | Mandatory | Mandatory |
| DAST run in staging for this release | Mandatory | Mandatory |
| DAST coverage ≥ defined threshold | Recommended | Mandatory |
| CVE exceptions: all within validity | Mandatory | Mandatory |
| Regression tests passed | Mandatory | Mandatory |
| Threat model updated (if there was an architectural change) | Mandatory | Mandatory |
| PenTest completed (if mandatory for this cycle) | Not applicable | Mandatory (annually or per major release) |
| Security documentation updated | Recommended | Mandatory |

### 4.2 Residual risk acceptance {#42-aceitação-de-risco-residual}

If the release is approved with open findings (with a formal exception), there must be a residual risk acceptance record that includes:

- [ ] Identification of the accepted findings and reference to the formal exceptions
- [ ] Business justification for proceeding with residual risk
- [ ] Person responsible for the acceptance and date
- [ ] Resolution plan with a deadline

---

## 5. Go/no-go decision {#5-decisão-gono-go}

### 5.1 Automatic blocking criteria (no-go) {#51-critérios-de-bloqueio-automático-no-go}

Promotion to production is automatically blocked if:

- The automated pre-release gate returns the REJECTED status
- There is an open Critical or High finding without a valid formal exception
- The candidate artefact does not have a valid signature (L2/L3)
- The SBOM has not been generated for this version (L2/L3)
- DAST has not been run in staging for this release candidate (L2/L3)

### 5.2 Human approval {#52-aprovação-humana}

Even when the automated gate returns APPROVED, promotion to production requires explicit human approval:

| Level | Minimum approver | Format |
|---|---|---|
| L1 | Tech Lead | Comment or approved release PR |
| L2 | Tech Lead + AppSec Engineer | Formal record in the release system or approved deploy PR |
| L3 | Tech Lead + AppSec Engineer (dual approval) | Formal record with identity, timestamp and reference to the gate report |

The approval must be recorded with:

- [ ] Identity of the approver (not delegable to a shared account)
- [ ] Timestamp
- [ ] Reference to the automated gate report
- [ ] Reference to the approved artefact (tag, digest or hash)
- [ ] Status of the security checklist

---

## 6. Artefact immutability {#6-imutabilidade-do-artefacto}

The artefact promoted to production must be exactly the same one that went through all the tests - not a new build of the same code:

- [ ] Promotion consists of moving the already built and tested artefact to production, not of rebuilding
- [ ] The artefact is identified by an immutable digest or hash, not only by a tag
- [ ] The artefact's signature is verified at the start of the deploy process
- [ ] Any rebuild means restarting the full testing cycle

:::warning
"Rebuild from source" as a substitute for promoting the tested artefact is prohibited at L2/L3. A new build, even from the same commit, may produce different artefacts (dependencies resolved at a different moment, different environment variables, etc.) and has no security equivalence to the previously tested artefact.
:::

---

## 7. End-to-end traceability {#7-rastreabilidade-ponta-a-ponta}

For any release in production it must be possible, at any future moment, to reconstruct the chain:

```
commit SHA → pipeline run → artefacto (digest) → SBOM → testes executados → aprovação de release
```

To ensure this traceability:

- [ ] Each production artefact is associated with the commit SHA it originated from
- [ ] The pipeline run that produced the artefact is referenced
- [ ] The SBOM and the test reports are associated with the artefact
- [ ] The approval record references the digest of the approved artefact

---

## 8. Historical release register {#8-registo-histórico-de-releases}

For each release, a record must be kept in `releases.md` (or an equivalent system) with:

| Field | Description |
|---|---|
| Version | Release identifier (semantic tag) |
| Approval date | Timestamp of the go/no-go decision |
| Approver(s) | Identity(ies) that approved |
| Gate status | APPROVED / REJECTED (before human override) |
| Open findings | Number and reference to exceptions |
| Artefact | Digest or hash of the promoted artefact |
| SBOM | Reference to the associated SBOM |
| Notes | Residual risk acceptance, if applicable |

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Ensure that all blocking findings are resolved before requesting a release |
| Tech Lead | Coordinate the release process; verify the checklist; approve at L1/L2 |
| AppSec Engineer | Verify security reports; approve at L2/L3; validate active exceptions |
| DevOps / SRE | Configure the automated gate; ensure artefact immutability; perform the deploy with the approved artefact |
| Product Manager | Decide on residual risk acceptance when there is a conflict between deadline and security |
| GRC / Compliance | Audit release records; verify traceability; validate evidence retention |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- An incident originating from a release approved with known, undocumented findings
- A change to the deploy process that affects artefact immutability
- A regulatory change that imposes additional approval requirements

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 10 - Security Testing | Pre-release security gate, checklist, risk acceptance |
| SbD-ToE Ch. 11 - Secure Deployment | Deploy approval, artefact immutability |
| SbD-ToE Ch. 07 - Secure CI/CD | Commit→pipeline→release traceability |
| Test Strategy Policy (`19_policy-estrategia-testes.md`) | SAST/DAST/SCA gates and thresholds |
| SBOM Policy (`11_policy-sbom.md`) | SBOM as release evidence |
| Release Approval Policy (`26_policy-aprovacao-release.md`) | Detailed approval process at L3 |
| SLSA Framework | Build integrity and artefact promotion |
| NIST SP 800-218 (SSDF) PW.8 | Archive and protect each software release |
| ISO/IEC 27001 - A.12.1 | Operational procedures and responsibilities |
