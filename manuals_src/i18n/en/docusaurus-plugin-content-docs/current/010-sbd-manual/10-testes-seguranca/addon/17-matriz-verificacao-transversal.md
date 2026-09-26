---
id: matriz-verificacao-transversal
title: Cross-cutting Verification Matrix
sidebar_position: 17
description: The single index of all security verification in SbD-ToE — activity × type × oracle × chapter × risk level — distinguishing testing (behavioural oracle) from analysis/scanning (lookup/policy oracle).
tags: [verificacao, matriz, testes, sca, sast, dast, iac, oraculo, transversal, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/17-matriz-verificacao-transversal.md
  source_sha256: 2e275f4af08be4cea59133bb2f2fd6d7a0d3aa3438d215557b9d4e69e92bec74
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 170d35e2fb9a6e548075226e64bb9d5b4472a3e71d8f5274f41b910c6057c31d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, oracle, provenance, requirement_runtime, risk_level, sbdtoe_sbd, slug_threat_modeling, threat, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 839c41df5bd01421cb1345fecef361309031b8b15eca90fb1e28d440d01c6a55
  translated_at: 2026-09-26T10:31:35Z
  stamped_at: 2026-09-26T18:35:16Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Cross-cutting Verification Matrix

Security verification does not live in a single chapter. It is distributed across the lifecycle — a requirement is validated in Ch. 02, a *threat model* is reviewed in Ch. 03, SCA runs in Ch. 05, IaC *scanning* is done in Ch. 08, DAST is executed in Ch. 10, a runtime anomaly is detected in Ch. 12. Each activity belongs to the chapter of its domain, where it is prescribed with its requirement, its applicability by risk level and its evidence. This page does not duplicate any of those prescriptions: it is the **single index** that gathers them, so that the audit question — *"is everything verified for this risk level?"* — can be answered in one go.

What organises the matrix is the **oracle**: the reference against which what is observed is confronted. A **test** has a *behavioural* oracle — it confronts observed behaviour with expected behaviour (SAST, DAST, IAST, fuzzing, PenTesting). An **analysis** or *scanning* has a *lookup* oracle (it confronts an inventory with a CVE database — that is SCA) or a *policy* oracle (it confronts a configuration with a rule or *baseline* — secrets, IaC, container images). **Functional validation** has an *acceptance criterion* oracle (it confronts the system with the functional security requirement). **Review** has an *expert judgement* oracle against patterns (*threat modelling*, architecture). **Runtime detection** has a *signal* oracle against an operational *baseline*. The distinction is not academic: it is what justifies SCA living in the dependencies chapter and not in the testing chapter.

Ch. 10 (Security Testing) covers only the **behavioural oracle** slice — the tests proper. All the rest of verification lives in its chapter of origin. This matrix is where the two halves come back together, without any control being prescribed in two places.

## The taxonomy of oracles {#a-taxonomia-de-oráculos}

| Type of verification | Oracle | Question it answers | Examples |
|---|---|---|---|
| **Test** | Behavioural — observed vs. expected behaviour | "Does the system behave insecurely when confronted?" | SAST, DAST, IAST, fuzzing, PenTesting |
| **Analysis / scanning (lookup)** | CVE database — inventory vs. known vulnerabilities | "Does any component in the inventory have a known vulnerability?" | SCA (*vulnerability verdict*) on SBOM, image scanning |
| **Analysis / scanning (policy)** | Rule or *baseline* — configuration vs. policy | "Does the configuration violate any prescribed rule?" | Secrets scanning, IaC scanning, *policy-as-code*, *admission control* |
| **Functional validation** | Acceptance criterion — system vs. functional requirement | "Is the security requirement effectively satisfied?" | Requirements validation, security regression tests |
| **Review / design review** | Expert judgement against patterns | "Does the design introduce risk that the pattern would avoid?" | *Threat model* review, architecture review, code review |
| **Runtime detection** | Signal vs. operational *baseline* | "Does behaviour in production deviate from normal?" | Behavioural detection, SIEM correlation, *detection engineering* |

> **SCA has two faces.** *Composition analysis* — generating the SBOM, inventorying direct and transitive dependencies — **has no oracle**: it is a survey, not verification. The *vulnerability verdict* — confronting that inventory with a CVE database — **has a lookup oracle**. It is the second face that makes SCA an *analysis* and not a *test*: there is no behaviour being confronted, there is an inventory compared with a list. That is why SCA lives in Ch. 05, anchored in [`DEP-001`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias) (SBOM, inventory) and [`DEP-002`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias) (*verdict* and blocking by severity), and not in Ch. 10.

## The matrix {#a-matriz}

Each row is a verification activity prescribed in a chapter. The L1/L2/L3 columns indicate applicability by risk level — `✔` mandatory, `rec.` recommended, `—` not required —, exactly as stated in the catalogue of origin. The *Grounding* column cites the requirement that prescribes the activity. The rows follow the order of the lifecycle.

| Activity | Type | Oracle | Chapter | L1 | L2 | L3 | Grounding |
|---|---|---|---|---|---|---|---|
| Functional validation of security requirements | Functional validation | Acceptance criterion | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | ✔ | ✔ | ✔ | `REQ-001`, `REQ-002` |
| Formal security review of the requirements | Review | Expert judgement | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | ✔ | ✔ | ✔ | `REQ-002` |
| Traceability requirement → threat → test | Functional validation | Acceptance criterion | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | — | ✔ | ✔ | `REQ-006` |
| Formal *threat model* review (STRIDE/LINDDUN/PASTA) | Review | Expert judgement against patterns | [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro) | — | ✔ | ✔ | `THR-001`, `THR-003` |
| Independent *threat model* review by AppSec before go-live | Review | Expert judgement | [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro) | — | ✔ | ✔ | `THR-007` |
| Validation of *threat model* evidence (DFDs, *trust boundaries*) | Review | Expert judgement against patterns | [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro) | — | ✔ | ✔ | `THR-002`, `THR-004` |
| Architecture review with a security focus | Review | Expert judgement against patterns | [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | — | ✔ | ✔ | `ARC-003` |
| Validation of trust zones and isolation between domains | Review | Expert judgement | [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | ✔ | ✔ | ✔ | `ARC-001`, `ARC-006` |
| Automatic topology validation (*diagrams-as-code*, Cartography) | Analysis (policy) | Rule / *baseline* | [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | — | — | ✔ | `ARC-013` |
| Security linters and *rulesets* *enforced* | Analysis (policy) | Rule / *ruleset* | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | ✔ | ✔ | ✔ | `DEV-002` |
| SAST as an integration *gate* | Test | Behavioural (static) | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | ✔ | ✔ | ✔ | `DEV-003`, `TST-002` |
| Code review with a security checklist on critical components | Review | Expert judgement against patterns | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | ✔ | ✔ | ✔ | `DEV-004` |
| Quality profiles with minimum *thresholds* by risk level | Analysis (policy) | Quality *baseline* | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | — | ✔ | ✔ | `DEV-008` |
| SBOM generation per *build* (*composition analysis*) | Analysis (no oracle) | Inventory | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | ✔ | ✔ | ✔ | `DEP-001` |
| SCA — *vulnerability verdict* with blocking by severity | Analysis (lookup) | CVE database | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | ✔ | ✔ | ✔ | `DEP-002` |
| Verification of pinned versions and dependency integrity | Analysis (policy) | Rule (*lockfile*, *hash*) | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | ✔ | ✔ | ✔ | `DEP-003`, `DEP-004` |
| Traceability SBOM → CVE → fix | Analysis (lookup) | CVE database | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | — | ✔ | ✔ | `DEP-010` |
| Inventory and provenance of AI/ML dependencies (AI BOM) | Analysis (no oracle) | Inventory | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | — | ✔ | ✔ | `DEP-011`, `DEP-012` |
| *Pinned* version and approved AI *providers* (anti *rug-pull*) | Analysis (policy) | Policy (pinned version / approved list) | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | — | ✔ | ✔ | `DEP-013`, `DEP-014` |
| Secrets scanning in the code and in the pipeline | Analysis (policy) | Rule (secret patterns) | [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | ✔ | ✔ | ✔ | `IAC-011`, `CIC-003` |
| Blocking security *gates* before promotion (SAST, SCA, lint, secrets) | Analysis (policy) | Pipeline policy | [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | ✔ | ✔ | ✔ | `CIC-004` |
| Verification of artefact integrity and provenance (signature, *hash*) | Analysis (policy) | Policy (signature / provenance) | [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | — | ✔ | ✔ | `CIC-007` |
| Verification of pipeline *triggers* and authorised sources | Analysis (policy) | Authorised-source rule | [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | ✔ | ✔ | ✔ | `CIC-002` |
| IaC scanning (tfsec, checkov) mandatory in the pipeline | Analysis (policy) | Rule / configuration *baseline* | [Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | ✔ | ✔ | ✔ | `IAC-003` |
| *Policy-as-code* — automatic policy *enforcement* (OPA/Rego, Sentinel) | Analysis (policy) | Codified policy | [Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | — | — | ✔ | `IAC-009` |
| Verification of the approved *plan* before *apply* | Analysis (policy) | Approval rule | [Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | — | ✔ | ✔ | `IAC-007` |
| *Drift* detection between IaC and real state | Runtime detection | Signal vs. declared state | [Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | — | ✔ | ✔ | `IAC-012` |
| Vulnerability scanning of container images | Analysis (lookup) | CVE database | [Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | ✔ | ✔ | ✔ | `CNT-002` |
| SBOM per published image | Analysis (no oracle) | Inventory | [Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | — | ✔ | ✔ | `CNT-008` |
| Verification of image signature and provenance (Cosign/Notary) | Analysis (policy) | Signing policy | [Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | — | ✔ | ✔ | `CNT-007` |
| *Admission control* — *policy-as-code* on containers (OPA/Gatekeeper, Kyverno) | Analysis (policy) | Codified policy | [Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | — | ✔ | ✔ | `CNT-009` |
| Verification of container *hardening* (non-root, *readonly FS*, *capabilities*) | Analysis (policy) | Rule / configuration *baseline* | [Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | rec. | ✔ | ✔ | `CNT-004`, `CNT-005`, `CNT-006` |
| DAST in *staging* before promotion | Test | Behavioural (dynamic) | [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | ✔ | ✔ | `TST-005` |
| IAST instrumented in *staging* | Test | Behavioural (instrumented runtime) | [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | — | ✔ | `TST-010` |
| Fuzzing of complex input-processing components | Test | Behavioural (adversarial input) | [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | — | ✔ | `TST-009` |
| Periodic PenTesting with defined scope and methodology | Test | Behavioural (real exploitation) | [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | ✔ | ✔ | `TST-008` |
| Security regression tests for fixed vulnerabilities | Functional validation | Acceptance criterion | [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | — | ✔ | ✔ | `TST-006` |
| *Eval suite* as a release gate for agentic systems | Test | Behavioural (offline *eval*) | [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | — | ✔ | ✔ | `DPL-010` |
| Detection of critical security events at runtime | Runtime detection | Signal (event catalogue) | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | ✔ | ✔ | ✔ | `OPS-002`, `OPS-005` |
| Event correlation across multiple sources (SIEM) | Runtime detection | Correlated signal | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | — | — | ✔ | `OPS-008` |
| Behavioural detection against a *baseline* of normal activity (UEBA) | Runtime detection | Signal vs. *baseline* | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | — | — | ✔ | `OPS-009` |
| Observability and audit of AI/agentic systems at runtime (*tool-call audit*, *token runaway*) | Runtime detection | Signal vs. *baseline* / *mandate* | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | — | ✔ | ✔ | `OPS-011`, `OPS-012`, `OPS-013` |
| Detection of *jailbreak* and *off-policy actions* in AI agents | Runtime detection | Signal vs. *mandate* / adversarial pattern | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | — | — | ✔ | `OPS-014` |
| Periodic review of third-party access (*least privilege*) | Analysis (policy) | Policy (*least privilege*) | [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | ✔ | ✔ | ✔ | `GOV-014` |

## Reading by oracle {#leitura-por-oráculo}

### Behavioural — the tests proper {#comportamental--os-testes-propriamente-ditos}

They confront observed behaviour with expected behaviour. SAST (`DEV-003`/`TST-002`) on the static code; DAST (`TST-005`) on the running application; IAST (`TST-010`) instrumented at runtime; fuzzing (`TST-009`) with adversarial input; PenTesting (`TST-008`) with real exploitation. It is the slice that lives in Ch. 10 — and almost the only one that lives there: the *eval suite* as a release gate for agentic systems (`DPL-010`) is also a behavioural oracle, but it is executed at *deploy* (Ch. 11), because that is where the model/*prompt* change enters production.

### Lookup — confrontation with a CVE database {#lookup--confronto-com-base-de-cve}

They confront an inventory with known vulnerabilities. The *vulnerability verdict* of SCA (`DEP-002`), the traceability SBOM → CVE → fix (`DEP-010`) and the scanning of container images (`CNT-002`). No behaviour is confronted: there is an inventory compared with a list. This is why SCA is **analysis** and not testing — the oracle is the CVE database, not the behaviour of the system.

### Policy — confrontation with a rule or *baseline* {#política--confronto-com-regra-ou-baseline}

They confront a configuration with a prescribed rule. Secrets scanning (`IAC-011`/`CIC-003`), IaC scanning (`IAC-003`), *policy-as-code* (`IAC-009`, `CNT-009`), signature and provenance verification (`CIC-007`, `CNT-007`), container *hardening* (`CNT-004`/`CNT-005`/`CNT-006`), pipeline *gates* (`CIC-004`), linters (`DEV-002`) and the periodic review of third-party access (`GOV-014`), which confronts the access granted with the *least privilege* rule. The oracle is the rule or *baseline*, not behaviour.

### Acceptance criterion — confrontation with the functional requirement {#critério-de-aceitação--confronto-com-o-requisito-funcional}

They confront the system with the functional security requirement. Requirements validation (`REQ-001`/`REQ-002`), traceability requirement → threat → test (`REQ-006`) and security regression tests (`TST-006`), which confirm that the fix satisfies the criterion and prevent recurrence.

### Signal / runtime — confrontation with an operational *baseline* {#sinal--runtime--confronto-com-baseline-operacional}

They confront behaviour in production with a *baseline*. Detection of critical events (`OPS-002`/`OPS-005`), SIEM correlation (`OPS-008`), behavioural detection (`OPS-009`) and IaC *drift* detection (`IAC-012`). The oracle is the operational signal against the expected state. In AI/agentic systems, this oracle extends to the *mandate*: dedicated observability and the *audit* per *tool invocation* (`OPS-011`/`OPS-012`/`OPS-013`) confront the real action with the declared intent, and the detection of *jailbreak* and *off-policy actions* (`OPS-014`, mandatory at L3) confronts the agent's behaviour with the *scope* signed in its *mandate* — the operational counterpart of the `intent declaration` required in requirements.

### Expert judgement — review and design review {#juízo-perito--revisão-e-design-review}

They confront the design with patterns, mediated by human expertise. *Threat model* review (`THR-001`/`THR-003`/`THR-007`), architecture review (`ARC-001`/`ARC-003`/`ARC-006`) and code review with a checklist (`DEV-004`). The oracle is expert judgement against established patterns.

## How to use the matrix {#como-usar-a-matriz}

**For the auditor.** It is read from top to bottom, fixing one risk column: for an L2 system, every row with `✔` in the L2 column must have evidence; those marked `rec.` are recommended but not blocking; those marked `—` are not required. The answer to *"is everything verified for this risk level?"* is obtained without traversing ten chapters.

**For the Testing chapter.** The *boundary item* of the Ch. 10 review checklist points here: Ch. 10 verifies the behavioural oracle, and refers the remaining verification to this matrix, which gathers it without duplicating it.

**On duplication.** No control is prescribed in two places. Each activity has a single requirement of origin, in its chapter. This matrix is an index, not a source — the requirement is changed in the chapter, and the matrix merely references it.

:::tip L1–L3 proportionality
The matrix does not require everything of everyone. The L1/L2/L3 columns are the expression of proportionality: L1 concentrates on low-cost, high-return baseline verification (SBOM, SCA, SAST, linters, critical events); L2 adds the depth of review (*threat model*, architecture, DAST, PenTesting); L3 adds exception verification (fuzzing, IAST, correlation, exception *policy-as-code*). Verifying is proportional to risk — this matrix shows, in one go, where that threshold lies for each activity.
:::
