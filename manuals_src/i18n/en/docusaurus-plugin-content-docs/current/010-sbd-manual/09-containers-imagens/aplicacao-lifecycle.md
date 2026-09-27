---
id: aplicacao-lifecycle
title: How to Do It
description: How to apply the prescribed container security practices throughout the development and operations lifecycle
tags: [tipo:aplicacao, ciclo-vida, containers, imagens, seguranca, isolamento, sbom, supply-chain]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/aplicacao-lifecycle.md
  source_sha256: a589f923c640b81d1961d1f1c6d5d6c33043145281a73ac8ef04553c619cdb4d
  source_commit: c4dc5e0ab3a1644a96f34a49ecae3686b35086ed
  target_sha256: ee75854902e1f27d80f7a66749e782fdd3882b8228e4d5cf4822a12ee992aa46
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [audit_trail, chapter_role, como_fazer, cra_support_period, cycle_iteration, discipline, lifecycle_phase, papel_suporte, practitioner_manual, provenance, risk_level, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: c2753e8f6683dd662128141b2367ef4a76a91da340ee5e3eaff416993b57e772
  translated_at: 2026-09-27T08:02:48Z
  stamped_at: 2026-09-27T08:02:48Z
  reviewed_by: null
---

# Application to the Lifecycle - Containers and Isolated Execution

Securing *containers* is not merely a runtime concern: it involves decisions from the selection of the base image to the way these images are run, monitored and audited.  
This chapter shows, in a prescriptive and integrated way, how to apply technical and governance controls at each phase of the lifecycle.

---

## 🧭 When to apply {#-quando-aplicar}

The risks associated with containers arise at different moments: in the choice of the base image, in the way it is built, in the policies applied in production and even in the reaction to incidents.  
The following table summarises **when each practice must be applied** and the justification that supports the need for it.

| SDLC Phase | Action | Justification |
|-----------|------|--------------|
| Design / Planning | Define a security baseline for images and runtime | Avoid vulnerabilities from conception |
| Development | Building images from trusted, **pinned** bases | Mitigate supply chain risk |
| CI/CD | Linters, SCA and automatic image scanners in pipelines | *Shift-left* of vulnerabilities and misconfigs |
| Pre-production | Image signing, provenance validation, Admission Control policies | Ensure integrity before go-live |
| Production | Execution monitoring, runtime enforcement and incident response | Minimise the impact of exploitation during execution |

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

Container security requires a **shared responsibility**.  
Each role contributes one part of the chain of trust, and only collaboration between teams ensures that the lifecycle remains intact.

| Role | Key responsibilities |
|-------|-------------------------------|
| **Developer** | Specify dependencies, build secure images, fix identified vulnerabilities |
| **DevOps / SRE** | Maintain trusted image repositories, configure pipelines, *enforcing* Admission Control |
| **AppSec Engineer** | Define policies, review critical alerts, validate compliance with the security baseline |
| **GRC / Compliance** | Validate compliance records, exceptions and governance over images and runtime |

---

## ✅ Human decision gates and minimum evidence {#-gates-de-decisão-humana-e-evidência-mínima}

In this chapter, the automatic mechanisms (scanners, linters, policies, signatures, SBOM) produce **technical signals**.  
**Authorisation for use**, **promotion between environments** and the **granting of exceptions** are always explicit human decisions, traceable and time-bound.

**Canonical rule:** no image should reach production (L2/L3) without auditable evidence of:
- who decided (role and identity);
- on the basis of which signals (links to logs/reports);
- what the scope is (image/digest, namespace, workload);
- what the validity is (TTL / expiry condition);
- which compensating measures were applied (if there is an exception).

User stories US-15 to US-17 operationalise these gates.

---

## 📖 Reusable User Stories {#-user-stories-reutilizáveis}

### US-01 - Building images from secure, minimal bases pinned by digest {#us-01---construção-de-imagens-a-partir-de-bases-seguras-minimalistas-e-pinned-por-digest}

**Context.**  
Images built on untrusted bases or with floating versions inherit vulnerabilities. The starting point is critical for the whole chain of trust.

:::userstory
**Story.**   
As the **Dev Team**, I want to build images from trusted bases, versioned by SHA256 digest and without unnecessary components, so as to reduce the attack surface and ensure traceability from the very first byte.

**Acceptance criteria (BDD).**  
- **Given** that I start building a container image  
  **When** I select the base image  
  **Then** the referenced image has a trusted origin (official repository) and a fixed digest (`sha256:...`)
- **Given** a new Dockerfile  
  **When** it is submitted  
  **Then** the linter (Hadolint) reports no unnecessary packages (`curl`, `bash`, `wget`, `ping`) at runtime
- **Given** a built image  
  **When** it is published  
  **Then** it contains only the binaries and libraries needed for the application to work

**Checklist.**  
- [ ] Base image from a trusted official repository (e.g. `gcr.io/distroless`, `alpine:3.19` with hash)
- [ ] Fixed SHA256 digest in the Dockerfile (no `latest` or floating tags)
- [ ] No interactive tools installed (shells, debug tools)
- [ ] Multi-stage build used to remove compilation residue
- [ ] Non-root user defined in the image (`USER nobody` or equivalent)
- [ ] Dockerfile validated by Hadolint

:::

**🧾 Artefacts & evidence.**  
- `Dockerfile` with fixed digest in the Git repository
- Output of `hadolint Dockerfile` with no critical blockers
- Layer report of the published image

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Official images with a version (not `latest`) |
| L2 | Yes | Fixed digest + Hadolint validation + no interactive tools |
| L3 | Yes | Fixed digest + Hadolint + multi-stage + Distroless + scanner integrated into the build |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Development | Initial build of the image | Developer | Immediate |

**Useful links.**  
[Secure Base Images](/sbd-toe/sbd-manual/containers-imagens/addon/imagens-base)  

---

### US-02 - Automatic validation of image vulnerabilities in the CI/CD pipeline {#us-02---validação-automática-de-vulnerabilidades-em-imagens-no-pipeline-cicd}

**Context.**  
Vulnerabilities discovered late in the cycle have an exponential cost. Shift-left is imperative: identify CVEs during the build, not in production.

:::userstory
**Story.**   
As **DevOps / SRE**, I want the pipeline to run vulnerability scanners (SCA) on every image build and block automatically if the risk exceeds the defined threshold, so as to reduce supply chain risk.

**Acceptance criteria (BDD).**  
- **Given** that an image is built in the pipeline  
  **When** the SCA scanner (e.g. Trivy) runs  
  **Then** it generates a report with CVEs catalogued by severity (Critical, High, Medium, Low)
- **Given** a CVE with severity above the threshold (e.g. High at L2)  
  **When** the scanner identifies it  
  **Then** the pipeline fails and the build is blocked
- **Given** a vulnerability with an available fix  
  **When** it is reported  
  **Then** the report includes the recommended version for the update

**Checklist.**  
- [ ] SCA scanner (Trivy, Grype, or similar) integrated into CI/CD
- [ ] Threshold defined by risk level (L1: block Critical; L2: block High+; L3: block Medium+)
- [ ] Report attached to the PR or build artefact
- [ ] Automatic block if the threshold is breached (not just a warning)
- [ ] Report exported in a structured format (JSON/SARIF) for audit

:::

**🧾 Artefacts & evidence.**  
- Scanner logs in the pipeline
- Trivy/Grype JSON report
- Automatic comment on the PR with the results

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Warning for Critical + Medium |
| L2 | Yes | Block on High/Critical |
| L3 | Yes | Block on Medium+ |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Image build | DevOps / SRE | Automatic |

**Useful links.**  
[Vulnerabilities in Images](/sbd-toe/sbd-manual/containers-imagens/addon/vulnerabilidades-imagens)  

---

### US-03 - Signing and provenance verification of images with Cosign and Rekor {#us-03---assinatura-e-verificação-de-proveniência-de-imagens-com-cosign-e-rekor}

**Context.**  
Without verifiable provenance, images can be tampered with or replaced. Signing is the second pillar of trust (after secure building).

:::userstory
**Story.**   
As an **AppSec Engineer**, I want all produced images to be digitally signed and to have verifiable provenance recorded in a transparency log, so as to ensure integrity and origin across every deploy.

**Acceptance criteria (BDD).**  
- **Given** that an image has been built and published  
  **When** the pipeline completes the build  
  **Then** the image is signed with `cosign sign` using a federated identity (OIDC) or a private key
- **Given** a signed image  
  **When** it is published  
  **Then** the signature is recorded in the Rekor transparency log (public or private) with a timestamp and the image hash
- **Given** a Kubernetes cluster  
  **When** a pod tries to use an unsigned image (at L2/L3)  
  **Then** Admission Control (Kyverno/OPA) rejects the creation

**Checklist.**  
- [ ] Cosign signing active in the pipeline
- [ ] Federated OIDC configured (e.g. GitHub Actions, GitLab CI) to issue tokens without static keys
- [ ] Transparency log (Rekor) integrated
- [ ] Automatic verification before deploy
- [ ] Admission Control policy configured (OPA/Kyverno) to reject unsigned images at L2/L3

:::

**🧾 Artefacts & evidence.**  
- Cosign signature attached to the image in the registry
- Rekor entry with provenance
- Cosign verification logs in the pipeline

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Optional signing, warning if unsigned |
| L2 | Recommended | Signing recommended, verification in Admission Control |
| L3 | Yes | Mandatory signing, blocking verification |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Pre-production | Publication to the registry | AppSec Engineer + DevOps / SRE | Before deploy |

**Useful links.**  
[Signing and Chain of Trust](/sbd-toe/sbd-manual/containers-imagens/addon/assinatura-cadeia-trust)  

> **Common Pattern:** Signing and provenance verification take place in **multiple contexts** 
> (CI/CD, IaC, container images, deploy). This US focuses on the context of **container images** with 
> *Cosign* and *Rekor*; see also [Ch. 07-US-06: Signing and provenance of CI/CD artefacts] 
> and [Ch. 08-US-09: Signing of IaC modules]. All apply the **same principle** (sign → validate → use).

---

### US-04 - Enforcing formal security policies at runtime with OPA/Kyverno {#us-04---aplicação-de-políticas-formais-de-segurança-no-runtime-com-opakyverno}

**Context.**  
A container without execution restrictions expands the attack surface exponentially. Formal policies ensure automatic compliance with the security baseline.

:::userstory
**Story.**   
As **DevOps / SRE**, I want every container execution in Kubernetes to be validated by formal policies (OPA/Kyverno), so as to ensure that only workloads compliant with the security baseline are allowed.

**Acceptance criteria (BDD).**  
- **Given** that a pod is created in the cluster  
  **When** the admission policy validates it  
  **Then** it rejects any pod that does not comply with: `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, `capabilities: drop: ["ALL"]`
- **Given** a pod that violates the policy  
  **When** an attempt is made to create it  
  **Then** it is blocked and the event is audited
- **Given** a *bypass* attempt (e.g. `privileged: true`)  
  **When** it is detected  
  **Then** the attempt is recorded and raises an alert

**Checklist.**  
- [ ] OPA/Kyverno installed in the cluster
- [ ] Policies written in Rego (OPA) or YAML (Kyverno) and versioned
- [ ] `audit` mode first (logging without blocking), then `enforce` (active blocking)
- [ ] Specific rules per namespace or label (e.g. `tier=production` more restrictive)
- [ ] Clear documentation of the policies and examples of compliance

:::

**🧾 Artefacts & evidence.**  
- OPA/Kyverno policy manifests in the repository
- Logs of pod rejections and acceptances
- Audit report of violating attempts

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Basic validation (non-root) in audit mode |
| L2 | Yes | Restrictive policies in enforce mode |
| L3 | Yes | Complete policies + detailed audit + periodic review |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Production | Pod creation | DevOps / SRE | Immediate |

**Useful links.**  
[Container Hardening](/sbd-toe/sbd-manual/containers-imagens/addon/hardening-containers), [OPA Runtime Policies](/sbd-toe/sbd-manual/containers-imagens/addon/policies-runtime-opa)  

---

### US-05 - Runtime Monitoring and Incident Response {#us-05---monitorização-e-resposta-a-incidentes-em-runtime}

**Context.**  
Runtime attacks are only detected with continuous active monitoring. The absence of alerts allows compromises to persist silently.

:::userstory
**Story.**   
As **AppSec + GRC**, I want to monitor the behaviour of running containers and generate alerts for suspicious events, so as to enable rapid detection of and response to security incidents.

**Acceptance criteria (BDD).**  
- **Given** that a container is running in production  
  **When** suspicious behaviour occurs (e.g. access to critical files, modification of binaries, an escape attempt)  
  **Then** the event must be recorded in a centralised log and raise an immediate alert
- **Given** a detected critical incident  
  **When** it occurs  
  **Then** alerts are sent to the configured channels (Slack, PagerDuty, etc.) with full context
- **Given** an incident investigation  
  **When** traceability is required  
  **Then** the complete logs include: timestamp, pod, namespace, container, process, actor, action, result

**Checklist.**  
- [ ] Runtime monitoring tool (e.g. Falco, Sysdig, AppArmor) installed
- [ ] Detection policies based on anomalous behaviour
- [ ] Alerts for critical events (privilege escalation, file modifications, network escape)
- [ ] Integration with the alerting system (SIEM, Prometheus, webhooks)
- [ ] Incident response playbook documented and tested
- [ ] Log retention in line with Policy 29 (security logs: 1 year at L2, 2 years at L3)
- [ ] Real-time event dashboard

:::

**🧾 Artefacts & evidence.**  
- Runtime monitor configuration versioned in Git
- Centralised structured logs (JSON)
- Alerts configured in the SIEM
- Incident response playbook
- Report of detected/investigated incidents

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Basic monitoring, critical alerts |
| L2 | Yes | Critical alerts configured, playbook documented |
| L3 | Yes | Full coverage, automatic response, correlated investigation |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Production | Container execution | AppSec Engineer + GRC / Compliance | Continuous, response within minutes |

**Useful links.**  
[Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-06 - Generation and Traceability of SBOM in Images {#us-06---geração-e-rastreabilidade-de-sbom-em-imagens}

**Context.**  
Without an SBOM, there is no visibility of the components present nor rapid analysis of the impact of CVEs. The SBOM is a prerequisite for supply chain integrity.

:::userstory
**Story.**   
As **DevOps / SRE**, I want to generate the SBOM (Software Bill of Materials) automatically on every image build and store it versioned, so as to enable component traceability, vulnerability analysis and auditable compliance.

**Acceptance criteria (BDD).**  
- **Given** that an image is built in the pipeline  
  **When** the build completes  
  **Then** an SBOM is generated in CycloneDX/SPDX JSON format with all layers and dependencies
- **Given** a generated SBOM  
  **When** it is stored  
  **Then** it is versioned with the image (tag, digest, timestamp) and accessible for audit
- **Given** a vulnerability analysis  
  **When** it is run  
  **Then** it uses the SBOM as input and correlates CVEs with specific components

**Checklist.**  
- [ ] SBOM generated automatically (Syft, Trivy, or similar)
- [ ] CycloneDX or SPDX JSON format (compatible with the ecosystem)
- [ ] SBOM attached to the build artefact (registry label, separate storage)
- [ ] All direct and transitive dependencies included
- [ ] Versioned with the image hash and build identifier
- [ ] Retention according to level (Policy 11: 1 year at L2, 2 years at L3; for products within the scope of the CRA, at least 10 years or the support period, if longer)
- [ ] Query available for audit and compliance

:::

**🧾 Artefacts & evidence.**  
- `sbom.json` file (or similar) versioned per image
- Metadata in the registry (labels/annotations with SBOM reference)
- SBOM correlated with build ID and pipeline logs

> **Reference:** This US specialises [Ch. 05-US-02: SBOM on every build]
> for the context of images and containers. The SBOM of images must include all layers and system dependencies, complementing the SBOM of application dependencies.

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Basic SBOM, Syft JSON format |
| L2 | Yes | Complete SBOM in CycloneDX, 1-year retention |
| L3 | Yes | SBOM in CycloneDX, integration with provenance (signed), retention of 2+ years |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Image build | DevOps / SRE | On every build |

**Useful links.**  
[Inventory and SBOM](/sbd-toe/sbd-manual/containers-imagens/addon/sbom-containers),[Dependencies, SBOM and SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)  

---

### US-07 - Registry Governance with Allowlist and Digest-Only {#us-07---governação-de-registries-com-allowlist-e-digest-only}

**Context.**  
Pulls from untrusted registries or with mutable tags expose the supply chain to typosquatting and image tampering attacks. Formal governance is imperative.

:::userstory
**Story.**   
As **DevOps + AppSec**, I want to impose an allowlist of trusted registries and ***enforce* references by SHA256 digest** (never by tag), so as to prevent the use of unverified or tampered images.

**Acceptance criteria (BDD).**  
- **Given** that a workload references an image  
  **When** the Admission Control policy checks the origin  
  **Then** it rejects it if the image is not on the allowlist or if it is referenced by tag (it accepts only digest `sha256:...`)
- **Given** an attempted pull from an untrusted registry  
  **When** it is executed  
  **Then** it is blocked with a clear policy violation message
- **Given** a floating tag (e.g. `latest`, `v1`)  
  **When** it is referenced in a workload  
  **Then** it is rejected; a fixed digest is required

**Checklist.**  
- [ ] Allowlist of trusted registries documented and published
- [ ] OPA/Kyverno policy requiring references by digest
- [ ] Blocking of mutable tags (latest, stable, master, v1.x, etc.)
- [ ] Exceptions formalised and audited (with a deadline)
- [ ] Integrity validation (e.g. signature verification, SBOM)
- [ ] Automatic rejection of unsigned images at L2/L3
- [ ] Monthly reports of blocked attempts

:::

**🧾 Artefacts & evidence.**  
- `registry-allowlist.yaml` versioned in the repository
- OPA/Kyverno policy applied and audited
- Admission Controller logs with rejections
- Exceptions recorded with justification and deadline

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Warning for untrusted registries |
| L2 | Yes | Allowlist with blocking by origin, digest recommended |
| L3 | Yes | Restrictive allowlist + mandatory digest-only + verified signature |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy | Workload definition | DevOps / SRE + AppSec Engineer | Before go-live |

**Useful links.**  
[Signing and Chain of Trust](/sbd-toe/sbd-manual/containers-imagens/addon/assinatura-cadeia-trust), [OPA Runtime Policies](/sbd-toe/sbd-manual/containers-imagens/addon/policies-runtime-opa)

---

### US-08 - Management of Secrets Outside the Image with OIDC and Workload Identity {#us-08---gestão-de-segredos-fora-da-imagem-com-oidc-e-workload-identity}

**Context.**  
Secrets embedded in images create exposure that is hard to revoke. Long-lived credentials in pipelines are vulnerable to compromise. Ephemeral workload identity is the modern standard.

:::userstory
**Story.**   
As **DevOps / SRE**, I want to prohibit static credentials in images and use ephemeral identities via OIDC/Workload Identity, so as to eliminate the exposure of long-lived secrets.

**Acceptance criteria (BDD).**  
- **Given** that an image is built  
  **When** the pipeline analyses the layers  
  **Then** it fails if it finds embedded credentials (AWS keys, GCP tokens, DB passwords, API keys)
- **Given** a running container  
  **When** it needs to access resources (AWS, GCP, Kubernetes API)  
  **Then** it receives an ephemeral token via OIDC (TTL ≤ 1h) with no stored credentials
- **Given** that the container session ends  
  **When** the token expires  
  **Then** the container can neither reuse the credential nor escalate privileges

**Checklist.**  
- [ ] Secret scanning in layers (e.g. TruffleHog, Gitleaks)
- [ ] Automatic build failure if a credential is detected
- [ ] OIDC/Workload Identity configured (e.g. GitHub OIDC, Kubernetes SA OIDC)
- [ ] Token TTL configured to ≤ 1h
- [ ] `imagePullSecrets` audited (no hardcoded secret)
- [ ] Access to resources via a dedicated role/service account (not the default)
- [ ] No credentials in environment variables (use mounted secrets at most)
- [ ] Automatic rotation of long-lived credentials if needed

:::

**🧾 Artefacts & evidence.**  
- Secret scanning reports in the pipeline
- OIDC and Workload Identity configuration
- IAM/RBAC policies showing restrictive access
- Token issuance logs

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Secret scanning, credentials not in env vars |
| L2 | Yes | Mandatory secret scanning, OIDC with short TTL |
| L3 | Yes | Secret scanning + OIDC + automatic rotation + continuous audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Build/Deploy | Build and deploy | DevOps / SRE | On every execution |

**Useful links.**  
[Runners and Isolation](/sbd-toe/sbd-manual/containers-imagens/addon/runners-isolamento)

---

### US-09 - Minimal RBAC and Dedicated ServiceAccounts {#us-09---rbac-mínimo-e-serviceaccounts-dedicadas}

**Context.**  
Workloads with excessive permissions or using the default ServiceAccount widen the impact of a compromise. Minimal RBAC reduces the "blast radius" of security failures.

:::userstory
**Story.**   
As **DevOps + AppSec**, I want to ***enforce* the use of dedicated ServiceAccounts with minimal RBAC per workload**, so as to reduce the impact of compromised credentials and isolate the blast radius.

**Acceptance criteria (BDD).**  
- **Given** that a workload is defined  
  **When** I specify the ServiceAccount  
  **Then** a dedicated SA is created (not the default) with the minimum permissions required
- **Given** a workload at L2/L3  
  **When** it tries to use the default ServiceAccount  
  **Then** it is rejected by an Admission Control policy
- **Given** a dedicated SA  
  **When** it is configured  
  **Then** it includes only the necessary permissions (e.g. read-only on specific configmaps, no privilege escalation)

**Checklist.**  
- [ ] Dedicated ServiceAccount per workload (not reused across applications)
- [ ] Role/RoleBinding with minimal permissions (principle of least privilege)
- [ ] Default SA prohibited at L2/L3 by Admission Control
- [ ] Permissions audit documented (what each workload can do)
- [ ] No role with `*` wildcard at L2/L3
- [ ] Periodic review of permissions (every four months)
- [ ] SA usage metrics (which were used, which never were)

:::

**🧾 Artefacts & evidence.**  
- Versioned ServiceAccount/Role/RoleBinding manifests
- Audit of permissions per SA
- OPA/Kyverno policy blocking the default SA
- RBAC coverage dashboard

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Dedicated SAs, reasonable permissions |
| L2 | Yes | Dedicated SA mandatory, minimal RBAC validated |
| L3 | Yes | Dedicated SA + minimal RBAC + periodic review + no wildcard permissions |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy | Workload definition | Software Architects approve; DevOps / SRE executes | Before go-live |

**Useful links.**  
[Kubernetes and Execution](/sbd-toe/sbd-manual/containers-imagens/addon/kubernetes-execucao)

---

### US-10 - Network Segmentation and NetworkPolicy {#us-10---segmentação-de-rede-e-networkpolicy}

**Context.**  
Without network segmentation, compromised workloads exfiltrate data and propagate attacks laterally. NetworkPolicy implements network zero-trust, blocking unauthorised flows.

:::userstory
**Story.**   
As **DevOps / SRE + Software Architects**, I want to apply NetworkPolicy with explicit ingress/egress in every namespace, so as to limit communications to what is strictly necessary and detect anomalies.

**Acceptance criteria (BDD).**  
- **Given** that a workload tries to contact an unauthorised service **When** the flow is not in a NetworkPolicy **Then** the connection is blocked and recorded in audit logs
- **Given** that a new namespace is created **When** there is no default NetworkPolicy **Then** deny-all is applied automatically (L2+)
- **Given** that DNS traffic is observed **When** a name cannot be resolved **Then** the attempt is blocked and alerted in the SIEM

**Checklist.**  
- [ ] Default deny-all NetworkPolicy per namespace (L2+)
- [ ] Ingress whitelist per service/port (e.g. `from:\n  - podSelector: {app: payment}` port 443)
- [ ] Controlled egress to external APIs (L3: digest-only registry, NTP, audit + SIEM)
- [ ] Exceptions documented with expiry (e.g. maintenance, expiring in 30d)
- [ ] Validation in the admission controller (Gatekeeper/Kyverno)
- [ ] Reports of blocked flows (10x/day if voluminous → aggregated)
- [ ] Failure test: `nsenter` in a pod, validate the blocks

:::

**Artefacts & evidence.**  
- `networkpolicy/*.yaml` (organised by namespace and type: deny-default, ingress, egress)
- Rejection logs in the SIEM (volume of blocked packets, top 10 unauthorised destinations)
- Prometheus metrics: `calico_denied_packets`, `cilium_policy_drop`
- Quarterly audit report: connectivity vs prescriptions
- Exceptions documented with TTL and reviews

**Proportionality L1–L3.**  
| Level | Prescription | Examples | Validation SLA |
|-------|-----------|----------|---------------|
| **L1** | Documenting flows recommended | Manual; observed flows | Quarterly |
| **L2** | Default deny-all + critical ingress | Namespace mandatory; egress to registry+DNS | Monthly; annual audit |
| **L3** | Full egress + continuous audit | Per-service whitelist; no exceptions without GRC approval | Weekly; `<1h` alerts |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Design | Survey of dependencies | Developer | Before specifying pods |
| Deploy | Manifest application | DevOps / SRE + Admission Controller | Before workload scheduling |
| Ops | Flow audit | DevOps / SRE + AppSec Engineer | Audit log retention in line with Policy 29 |
| GRC | Exceptions vs compliance | GRC / Compliance | Quarterly review |

**Useful links.**  
[Kubernetes and Execution](/sbd-toe/sbd-manual/containers-imagens/addon/kubernetes-execucao)

---

### US-11 - Golden Base Images with Automatic Patching {#us-11---golden-base-images-com-patching-automático}

**Context.**  
Heterogeneous bases increase operational cost and configuration risk. A patching SLA ensures that vulnerabilities do not propagate.

:::userstory
**Story.**   
As **DevOps + AppSec**, I want to maintain a catalogue of Golden Base Images with semantic versioning and a patching SLA, so as to standardise security and reduce configuration drift.

**Acceptance criteria (BDD).**  
- **Given** that an Ubuntu 22.04 base receives a critical CVE (CVSS≥9) **When** the patch is available **Then** a new tag is cut (e.g. ubuntu-22.04:v1.2.3→v1.2.4) and propagated within ≤ 3 days (L3) or ≤ 7 days (L2), in line with Policy 24
- **Given** that a microservice builds on a discontinued base **When** the pipeline validation runs **Then** the build fails with a clear end-of-life message
- **Given** that the node:20 base is updated **When** a new release is published **Then** a changelog is added to `golden-images-catalog.md` with an SBOM diff

**Checklist.**  
- [ ] `golden-images-catalog.md` catalogue with semantic versioning (ubuntu-22.04:v1.2.3, alpine:v3.19.1)
- [ ] Signing of every golden image (Cosign + OIDC via Rekor)
- [ ] Patching SLA defined by criticality (Policy 24: critical 7 days at L2, 3 days at L3; L1 recommended)
- [ ] Integration with a CVE feed (e.g. Trivy API, Red Hat advisories)
- [ ] Deprecation policy with notice on the deprecation date and removal of the tag ≤ 60 days later (Policy 24)
- [ ] Record of every push with SBOM (CycloneDX JSON in `image:tag@digest.sbom.json`)
- [ ] Dashboard: time-to-patch by criticality, adoption rate of old images

:::

**Artefacts & evidence.**  
- `golden-images-catalog.md` (table: base, latest tag, release date, EOL date, SBOM, signing status)
- Security changelog (e.g. "ubuntu-22.04:v1.2.4 - patch CVE-2024-12345 expat")
- SBOM of each golden image (CycloneDX format, stored in the registry via the `.sbom.json` tag or a custom attribute)
- Patching logs: date/time, criticality, author, link to the upstream advisory
- Adoption metrics (% of applications using latest, % using deprecated)

**Proportionality L1–L3.**  
| Level | Prescription | Patch SLA | Signing | Deprecation | Audit |
|-------|-----------|----------|-----------|------------|-----------|
| **L1** | Recommended; informal catalogue | Ad hoc | No | Manual | Annual |
| **L2** | Mandatory for prod; published catalogue | 7d critical | Cosign recommended | Notice at deprecation; removal ≤ 60d | Half-yearly |
| **L3** | Mandatory; strict SLA | 3d critical | Cosign + OIDC mandatory | Notice at deprecation; removal ≤ 60d + validation | Monthly |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Cataloguing | Base submission | AppSec Engineer | Review within 5d |
| Patching | CVE published | DevOps / SRE (automatic if via Dependabot) | Per SLA |
| Validation | New tag | CI/CD pipeline | `<2h` for approval |
| Sunsetting | EOL reached | DevOps / SRE + GRC / Compliance | Notice at deprecation; removal ≤ 60d |

**Useful links.**  
[Secure Base Images](/sbd-toe/sbd-manual/containers-imagens/addon/imagens-base)

---

### US-12 - Ephemeral, Signed and Audited Builders and Runners {#us-12---builders-e-runners-ephemerais-assinados-e-com-auditoria}

**Context.**  
Compromised builders compromise every release. Shared or persistent runners are critical points of attack in the supply chain. Traceability is essential for post-incident investigation.

:::userstory
**Story.**   
As **DevOps/AppSec**, I want builders and runners to be minimal, ephemeral (destroyed after each execution), signed and audited, so as to protect the CI/CD pipeline and ensure cryptographic traceability of every execution.

**Acceptance criteria (BDD).**  
- **Given** that the pipeline starts **When** a runner executes jobs **Then** it uses a signed (Cosign), minimal builder, is destroyed on completion and every operation is recorded with timestamp/actor
- **Given** a running runner **When** it tries to access `/var/run/docker.sock`, elevated privileges (CAP_SYS_ADMIN) or an unauthorised network **Then** it is blocked by the security configuration + an alert is generated
- **Given** a tool needed on the runner **When** an attempt is made to install it dynamically **Then** it is checked against the allowlist before installation and recorded (sha256, source, timestamp)
- **Given** a builder destroy event **When** it occurs **Then** it records: pod ID, exit status, duration, consolidated logs with a content hash

**Checklist.**  
- [ ] Ephemeral runner: created per job, mandatorily destroyed on completion (max 24h TTL even in case of a bug)
- [ ] Runner with a non-root user (e.g. `runAsUser: 1000`, `runAsNonRoot: true`)
- [ ] Builder image signed with Cosign + OIDC, versioned and immutable (digest-only)
- [ ] Minimised builder image (e.g. 50MB vs 500MB stock) with Dockerfile linting (Hadolint)
- [ ] Allowlist of approved tools (e.g. `curl`, `git`, `gcc` only if needed), blocking of interactive shells
- [ ] No access to the Docker socket (`/var/run/docker.sock` blocked), no `privileged: true`, no `hostPath` mount
- [ ] Signed builder logs (severity ≥DEBUG, consolidated in journald or stdout with JSON structuring)
- [ ] Builder cache controlled and isolated per job (e.g. cache key = `${CI_COMMIT_SHA}`, 7d expiry)
- [ ] Metrics: average duration, failure rate by type, log volume (alert if >1GB)

:::

**Artefacts & evidence.**  
- Runner configuration (YAML/HCL versioned in Git, signed tag for each release)
- Builder image manifest with Cosign signature (e.g. `builder:v2.1.0@sha256:abc123...`)
- Runner creation and destruction logs (retention of 1+ years, indexed in ELK/Splunk)
- Published tool allowlist (`tools-allowlist.yaml` with semantic versioning)
- SBOM of the builder image (CycloneDX JSON with build dependencies)
- Dashboard: build time, failures, log volume, cache hit rate
- Quarterly audit: compliance vs policy, builder incidents, hardening recommendations

**Proportionality L1–L3.**  
| Level | Runners | Builder | Signing | Audit | Multi-platform Support |
|-------|---------|---------|-----------|-----------|----------------------|
| **L1** | Ephemeral recommended | Public image | No | Basic logs | No |
| **L2** | Ephemeral mandatory, non-root | Minimised, versioned image | Cosign recommended | Centralised logs, half-yearly audit | Yes (Intel + ARM) |
| **L3** | Ephemeral mandatory, max 24h TTL, segmented by team | Minimised image + strict allowlist | Cosign + OIDC mandatory | Structured JSON logs, monthly audit + `<1h` alerts | Yes (Intel, ARM, IBM Z) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Definition | Pipeline creation | Developer | Before go-live |
| Implementation | Runner configuration | DevOps / SRE | Validation by AppSec |
| Execution | Each pipeline job | Runner (automatic) | `<2h` for destruction cleanup |
| Audit | Periodic review | DevOps / SRE + GRC / Compliance | Quarterly; immediate alerts for violations |

**Useful links.**  
[Runners and Isolation](/sbd-toe/sbd-manual/containers-imagens/addon/runners-isolamento)

---

### US-13 - Centralised and Auditable Policy Enforcement at Runtime {#us-13---enforcement-centralizado-e-auditável-de-políticas-no-runtime}

**Context.**  
To ensure that policies are applied systematically and that violations are tracked, formal enforcement with centralised logs and periodic review is required.

:::userstory
**Story.**  
As **DevOps/AppSec**, I want the enforcement of security policies to be **central, auditable and periodic**, so as to ensure that no execution escapes the controls and that every violating attempt is recorded and reviewed.

**Acceptance criteria (BDD).**  
- **Given** that runtime policies are active  
  **When** a workload is created  
  **Then** the policy is evaluated, the result is recorded in a centralised log and cannot be ignored
- **Given** a policy violation  
  **When** it occurs  
  **Then** it is blocked, audited with timestamp/actor/pod details and raises an alert
- **Given** a periodic review (e.g. monthly)  
  **When** it is carried out  
  **Then** it produces a report of blocked attempts, the compliance rate and adjustment recommendations

**Checklist.**  
- [ ] Centralised Admission Controller logs (e.g. Prometheus, ELK, Datadog)
- [ ] Automatic alerts for critical violations
- [ ] Monthly/quarterly enforcement report with metrics
- [ ] Full traceability: pod, namespace, image, timestamp, actor
- [ ] Integration with a SIEM or audit platform
- [ ] Policies versioned in Git, review by PR before application
- [ ] Compliance dashboard public/accessible to auditors

:::

**🧾 Artefacts & evidence.**  
- Prometheus/Grafana dashboard with enforcement metrics
- Structured rejection logs (JSON)
- Monthly compliance report
- Alerts configured in the notification system

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Basic logging, no automatic alerts |
| L2 | Yes | Logging + alerts for critical ones |
| L3 | Yes | Logging + alerts + dashboard + monthly review |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy/Production | Workload creation | DevOps / SRE + AppSec Engineer + GRC / Compliance | Continuous |

**Useful links.**  
[OPA Runtime Policies](/sbd-toe/sbd-manual/containers-imagens/addon/policies-runtime-opa), [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)


---

### US-14 - Advanced Sandboxing with gVisor/Kata for Critical Workloads {#us-14---sandboxing-avançado-com-gvisorkata-para-workloads-críticas}

**Context.**  
Applications that process critical data (payments, personal data) require reinforced isolation for protection against privilege escalation or access to the host.

:::userstory
**Story.**  
As **DevOps / SRE + AppSec Engineer + Software Architects**, I want to configure advanced sandboxes (gVisor, Kata Containers, Firecracker) via RuntimeClass on sensitive workloads, so as to ensure reinforced syscall isolation and protection against privilege escalation.

**Acceptance criteria (BDD).**  
- **Given** that a sensitive pod is created (e.g. with the label `sandbox=required`)  
  **When** it is scheduled in the cluster  
  **Then** it uses a RuntimeClass with an advanced sandbox (`gvisor` or `kata`)
- **Given** a sandboxed workload  
  **When** it tries to make a dangerous syscall (e.g. `ptrace`, `mount`)  
  **Then** it is blocked by the sandbox, not by the host
- **Given** a container escape attack  
  **When** it is attempted  
  **Then** the sandbox isolation rejects it, even if the securityContext lets it through

**Checklist.**  
- [ ] gVisor/Kata RuntimeClass installed in the cluster
- [ ] Sensitive pods labelled with `sandbox=required`
- [ ] Extra CPU/memory allocated for sandbox overhead
- [ ] Audit of pods that use a sandbox
- [ ] Performance tested and approved (acceptable overhead)
- [ ] Documentation of workloads that require a sandbox (e.g. payment processing)

:::

**🧾 Artefacts & evidence.**  
- Manifests with `runtimeClassName: gvisor` or `kata`
- Sandbox logs of blocked syscalls
- Performance and escape tests
- Report of sandboxed workloads

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | No | Optional, exploratory |
| L2 | Recommended | For sensitive workloads |
| L3 | Mandatory | For critical workloads (payments, sensitive data, PII) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy | Creation of a sensitive pod | DevOps / SRE + AppSec Engineer | Before deploy to production |

**Useful links.**  
[Kubernetes and Execution](/sbd-toe/sbd-manual/containers-imagens/addon/kubernetes-execucao)

---

### US-15 - Approval, deprecation and revocation of Golden Base Images (organisational catalogue) {#us-15---aprovação-depreciação-e-revogação-de-golden-base-images-catálogo-organizacional}

**Context.**  
Approved base images are **organisational trust assets**. Approval is not permanent: it requires criteria, a decision record, a review cadence and a rapid revocation mechanism.

:::userstory
**Story.**  
As **DevOps / SRE + AppSec Engineer**, I want to manage a catalogue of Golden Base Images with a formal process of **approval**, **periodic review**, **deprecation** and **revocation**, so as to ensure that the organisation only builds on bases with known and governed risk.

**Acceptance criteria (BDD).**  
- **Given** that a new base image is proposed  
  **When** it is evaluated for entry into the catalogue  
  **Then** there is an explicit human decision (approved/rejected) with associated evidence
- **Given** an approved base image  
  **When** it enters deprecation (EOL, recurring critical CVE, change of criteria)  
  **Then** there is a deprecation record with a deadline and a recommended alternative
- **Given** a critical event (upstream compromise, exploitable CVE without mitigation)  
  **When** revocation is decided  
  **Then** the image is marked as revoked and its use is blocked by policy (L2/L3)

**Checklist.**  
- [ ] Catalogue versioned in Git (image, digest/tag, owner, approval date, review, state: active/deprecated/revoked)
- [ ] Minimum approval criteria documented (SBOM, scan, provenance where applicable, known EOL)
- [ ] Review cadence defined (L2: half-yearly; L3: monthly or upon an event)
- [ ] Revocation process with triggers and communication (includes a rollback/patch plan)
- [ ] Automatic blocking at L2/L3 for revoked bases (admission/pipeline gate)

:::

**🧾 Artefacts & evidence.**  
- `golden-images-catalog.md` (or equivalent) with history and states  
- Approval/deprecation/revocation PR with identified reviewers  
- Attached evidence: SBOM, scan report, decision (reason + TTL if applicable)

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Simple catalogue + ad hoc review |
| L2 | Yes | Formal approval + quarterly review + deprecation with deadlines |
| L3 | Yes | Formal approval + monthly/event-driven review + rapid blocking revocation |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Design/Platform | Proposal of a new base | Software Architects approve; DevOps / SRE + AppSec Engineer execute | 5 working days |
| Operations | CVE/EOL/incident | DevOps / SRE + AppSec Engineer + GRC / Compliance | according to severity |

---

### US-16 - Staged promotion with explicit approval and per-environment revalidation {#us-16---promoção-por-estágios-com-aprovação-explícita-e-revalidação-por-ambiente}

**Context.**  
Automatic DEV→QA→PROD promotions create implicit acceptance of risk. At L2/L3, each promotion is a human decision supported by evidence, and validation must take the **context of the environment** into account.

:::userstory
**Story.**  
As **Release Manager/DevOps + AppSec**, I want the promotion of an image between environments to be an explicit gate (with human approval) and to revalidate provenance/policies in the context of the target environment, so as to prevent the automatic propagation of risk.

**Acceptance criteria (BDD).**  
- **Given** an image that is a candidate for promotion  
  **When** I promote it from DEV to QA/PROD (L2/L3)  
  **Then** there is a recorded explicit approval, referencing the digest, signals and justification
- **Given** the target environment (QA/PROD)  
  **When** the promotion is requested  
  **Then** the pipeline re-runs the minimum validations (policy compliance, signing/provenance where applicable, defined CVE thresholds)
- **Given** an approved promotion  
  **When** the deploy takes place  
  **Then** execution is blocked if the digest diverges from the approved one or if the target policies fail

**Checklist.**  
- [ ] Approval gate (manual step) for L2/L3 with the approver's identity and a mandatory comment
- [ ] Promotion always by digest (immutable) and never by floating tag
- [ ] Per-environment revalidation: policies, allowlist, thresholds, provenance where applicable
- [ ] Consolidated evidence (links to logs, reports, policy/admission entries)
- [ ] Approval TTL (e.g. 30 days) and need for re-approval after relevant changes

:::

**🧾 Artefacts & evidence.**  
- Promotion record (pipeline run + approval metadata + digest)  
- Per-environment validation reports (scan/policy/provenance)  
- Deploy manifest referencing the approved digest

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Automated promotion with logging and traceability |
| L2 | Yes | Explicit approval + minimum per-environment revalidation |
| L3 | Yes | Explicit approval + reinforced revalidation + short TTL + audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Pre-prod/Release | Promotion request | DevOps / SRE + AppSec Engineer | Before go-live |

---

### US-17 - Temporary exceptions to findings/policies with TTL, compensations and revalidation {#us-17---exceções-temporárias-a-findingspolicies-com-ttl-compensações-e-revalidação}

**Context.**  
Exceptions are inevitable (false positives, operational constraints, patch window), but they are also one of the greatest vectors of governance failure. An exception without TTL and without evidence is implicit acceptance of risk.

:::userstory
**Story.**  
As **AppSec + GRC**, I want to manage exceptions to findings/policies as formal, temporary and auditable decisions (TTL + compensations + revalidation), so as to allow operational continuity without losing control of risk.

**Acceptance criteria (BDD).**  
- **Given** a finding or policy violation that blocks a release  
  **When** an exception is requested  
  **Then** there is a record with: reason, scope (image/digest/workload), severity, risk, compensations and TTL
- **Given** an approved exception  
  **When** the TTL expires or the context changes (new CVE, change of exposure, incident)  
  **Then** the exception is automatically invalidated and requires re-approval
- **Given** an active exception  
  **When** a mitigation alternative exists (patch/config)  
  **Then** there is a plan and an owner with deadlines and evidence of execution

**Checklist.**  
- [ ] Versioned exception record (ticket/PR) with owner and approver  
- [ ] TTL in line with Policy 05 §7 (L3: 30 days Low/Medium, 14 days High, Critical not acceptable; L2: 60 / 30 days)  
- [ ] Compensating measures documented (e.g. egress restriction, runtime sandbox, reinforced monitoring)  
- [ ] Revalidation per event (new CVE, incident, change of architecture/runtime)  
- [ ] Periodic report of active exceptions (inventory + aggregate risk)

:::

**🧾 Artefacts & evidence.**  
- Exception record/ticket with TTL and approval signature  
- Evidence of the compensations applied (policies, alerts, configs)  
- Remediation plan and proof of execution (PRs, logs, releases)

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Exceptions recorded, TTL optional but encouraged |
| L2 | Yes | Mandatory TTL + minimum compensations + monthly review |
| L3 | Yes | Short TTL + reinforced compensations + weekly/monthly review + audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD/Release | Block due to a finding/policy | AppSec Engineer + GRC / Compliance + DevOps / SRE | Before go-live |


---

### US-18 - Self-hosted AI model weights treated as a critical asset {#us-18---pesos-de-modelo-ai-self-hosted-tratados-como-ativo-crítico}

The weights of an internally served model are the core of the product materialised in bytes, not configuration.  

**Context.** In *self-hosted* AI inference (vLLM, TGI, Ollama, Triton, llama.cpp), the weight files (`.safetensors`, `.gguf`, `.onnx`, *checkpoints*) live *at rest* in the infrastructure and receive the same treatment as secrets at runtime. Without encryption, integrity verification and access control, a model swapped in *storage* silently compromises inference (`AML.T0109` local *Supply Chain Rug Pull*).  

:::userstory
**Story.**   
As **DevOps / SRE + AppSec Engineer**, I want the weights of *self-hosted* models to be encrypted *at rest*, verified by hash at *startup* and served by an *artefact registry* with restricted and audited access, so as to ensure the confidentiality, integrity and traceability of the product's central asset.  

**Acceptance criteria (BDD).**  
- **Given** a weight file in the *volume* or *object store*  
  **When** it is stored  
  **Then** it is encrypted *at rest* with a key managed in the organisation's vault  
- **Given** the startup of an *inference runtime*  
  **When** it loads the weights  
  **Then** it validates the SHA-256 hash declared in the AI BOM and refuses to load if it diverges  
- **Given** a *download* of weights from the *artefact registry*  
  **When** it occurs  
  **Then** it is limited to the runtimes' *service accounts* and authorised operators, with a record of who/when/environment  

**Checklist.**  
- [ ] Weights encrypted *at rest* with the key in the vault (not in clear on the *volume*)  
- [ ] SHA-256 hash declared in the AI BOM (`DEP-012`) and validated at runtime *startup*  
- [ ] Access to the weights *artefact registry* restricted to *service accounts* + operators (not the whole team)  
- [ ] *Download* audit (who, when, which environment) — mandatory at L3 and for models under a licence with restrictions  

:::

**Artefacts & evidence.** AI BOM with *pinned* hash/provider/licence/version; integrity validation logs at *startup*; *artefact registry* access policy; audit trail of *downloads*.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Encryption and hash recommended; basic restricted access | Encryption *at rest* + hash at *startup* mandatory; access by *service account* | All of L2 + mandatory *download* audit + rapid access revocation |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Build/Provisioning | Publication/update of weights in the registry | DevOps / SRE + AppSec Engineer | Before serving |
| Production | Runtime *startup* | Runtime (automatic) | Blocking if the hash diverges |

**Useful links.** [Self-Hosted AI Inference](/sbd-toe/sbd-manual/containers-imagens/addon/self-hosted-inference)

---

### US-19 - GPU isolation and separation of sensitive inference workloads {#us-19---isolamento-de-gpu-e-separação-de-workloads-de-inferência-sensíveis}

A shared GPU without explicit isolation is a posture gap, not a neutral cost optimisation.  

**Context.** Inference typically runs on GPUs, and shared GPUs have an isolation posture that is still maturing (*cross-tenant side-channels* have been an area of active research since 2023). Mixing sensitive inference with user workloads on the same node creates a co-located adversary; the absence of resource limits allows DoS through an extreme `max_tokens`.  

:::userstory
**Story.**   
As **DevOps / SRE + AppSec Engineer + Software Architects**, I want to isolate the inference workload at GPU level and separate sensitive inference from user workloads, so as to prevent *cross-tenant* interference and service degradation.  

**Acceptance criteria (BDD).**  
- **Given** a sensitive inference pod  
  **When** it is scheduled  
  **Then** it receives a dedicated GPU via *MIG* (or the AMD/Intel equivalent) or, where that is not feasible, *process-level* isolation (*MPS* + cgroup limits + namespaces)  
- **Given** a node that runs sensitive inference  
  **When** workloads are scheduled  
  **Then** it does not share the node with workloads where the end user executes code (e.g. *JupyterHub*)  
- **Given** a *prompt* with extreme consumption  
  **When** it is processed  
  **Then** explicit limits (`--gpu-memory-utilization`, VRAM and *batch size* *quota*) prevent service degradation  

**Checklist.**  
- [ ] *Hard isolation* (dedicated GPU via MIG/equivalent) for sensitive workloads where feasible  
- [ ] *Process-level isolation* (MPS + cgroup + namespaces) as defence in depth when *hard isolation* is not possible  
- [ ] Sensitive inference separated from nodes with co-located user workloads  
- [ ] Explicit limits on VRAM, *batch size* and *GPU memory utilisation* configured  

:::

**Artefacts & evidence.** Manifests with `RuntimeClass`/GPU Operator and *resource limits*; MIG/MPS configuration; *node affinity*/*taints* policy that separates sensitive inference; documentation of the operational limits per model.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Isolation not required; resource limits recommended | *Hard* or *process-level isolation* recommended; node separation + limits mandatory | *Hard isolation* mandatory when sensitive workloads share hardware; full separation |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Design/Platform | Provisioning of the inference cluster | Software Architects approve; DevOps / SRE + AppSec Engineer execute | Before go-live |
| Production | Scheduling of a sensitive pod | DevOps / SRE (automatic) | Immediate |

**Useful links.** [Self-Hosted AI Inference](/sbd-toe/sbd-manual/containers-imagens/addon/self-hosted-inference)

---

### US-20 - Hardening of the AI inference API and container {#us-20---hardening-da-api-e-do-container-de-inferência-ai}

The "internal network" includes too many *principals* to be the only line of defence of an *inference runtime*.  

**Context.** Several runtimes (classic Ollama, *llama.cpp server*) start **without authentication** by default, and several *upstream* images run as root. Inference APIs expose new consumption semantics (*chat completions*, *embeddings*, SSE/WebSocket *streaming*) that conventional HTTP *rate limiting* does not cover — a `max_tokens` entrusted to the client alone is a ready-made DoS.  

:::userstory
**Story.**   
As **DevOps + AppSec**, I want the inference container and API to apply specific *hardening* — *non-root*, *read-only FS*, *drop capabilities*, restrictive *network policy*, mandatory authentication, consumption-based *rate limiting* and server-side `max_tokens`/prompt/timeout limits — so as to reduce the attack surface and prevent consumption abuse.  

**Acceptance criteria (BDD).**  
- **Given** the runtime container  
  **When** it is run  
  **Then** it runs *non-root*, with a *read-only root filesystem* (except required *paths*), `cap_drop: ALL` and a *network policy* that only accepts the consuming *gateway* and only allows egress to the *artefact registry*, telemetry and vault (no public *registries* at runtime)  
- **Given** any inference API *endpoint*  
  **When** it receives a request  
  **Then** it requires authentication (even on an "internal" network) and applies *rate limiting* by tokens/window and inference time, cross-checked against the *token budget* (`OPS-013`)  
- **Given** a request with an excessive `max_tokens` or *prompt*, or a long *streaming* connection  
  **When** it is processed  
  **Then** the server enforces a `max_tokens` limit, a *prompt* size limit and a *timeout*/limit on concurrent connections per *principal*  

**Checklist.**  
- [ ] *Non-root* container + *read-only FS* + `cap_drop: ALL` (override of root *upstream* images when necessary)  
- [ ] Restrictive *network policy*: ingress only from the *gateway*; egress only to the *artefact registry*/telemetry/vault  
- [ ] Mandatory authentication on all *endpoints* (configured before exposure)  
- [ ] Consumption-based *rate limiting* (tokens/window, inference time) + server-side limit on `max_tokens` and *prompt size*  
- [ ] *Streaming endpoints* with a maximum *timeout* and a limit on concurrent connections per *principal*  
- [ ] Consumption audit per *principal* (who, prompt size, `max_tokens`, model/version) → `OPS-011..014`  
- [ ] *Pinned* runtime version (`DEP-003`) with SCA active on the base images  

:::

**Artefacts & evidence.** Versioned `securityContext` and *network policy*; runtime auth and *rate limiting* configuration; consumption audit logs per *principal*; runtime manifest with the version *pinned* by digest and SCA report.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Authentication **always** mandatory; container *hardening* and limits recommended | Container *hardening* + *network policy* + *rate limit*/`max_tokens` + *pinning*/SCA mandatory | All of L2 + reinforced audit per *principal* and periodic review |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Build/Deploy | Build and deploy of the runtime | DevOps / SRE + AppSec Engineer | Before exposure |
| Production | API invocation | Runtime (automatic) | Continuous |

**Useful links.** [Self-Hosted AI Inference](/sbd-toe/sbd-manual/containers-imagens/addon/self-hosted-inference), [Container Hardening](/sbd-toe/sbd-manual/containers-imagens/addon/hardening-containers)

---

### US-21 - seccomp/AppArmor profiles and hardening drift verification {#us-21---perfis-seccompapparmor-e-verificação-de-drift-de-hardening}

A hardening *baseline* that is declared but not verified in execution is implicit trust, not control.  

**Context.** `CNT-006` requires `drop: ALL` plus an active seccomp/AppArmor profile and the blocking of `--privileged`/`hostPID`/`hostNetwork`. Without syscall confinement, minimal capabilities are insufficient against escape; and without *drift* verification, the effective runtime state may silently diverge from the declared one after manual changes or *upgrades*.  

:::userstory
**Story.**   
As **DevOps + AppSec**, I want to impose seccomp/AppArmor profiles on all workloads and periodically verify the effective hardening state against the declared one (drift), so as to ensure syscall confinement and detect divergences before they are exploited.  

**Acceptance criteria (BDD).**  
- **Given** a pod at L2/L3  
  **When** it is created  
  **Then** it has an active seccomp profile (runtime default or custom) and/or AppArmor, with `cap_drop: ALL` and justified additions  
- **Given** an unjustified attempt at `--privileged`, `hostPID` or `hostNetwork`  
  **When** it is submitted  
  **Then** the admission controller rejects and audits it  
- **Given** the effective hardening state at runtime  
  **When** the periodic *drift* verification runs  
  **Then** it compares it with the declared *baseline* and flags any divergence for review  

**Checklist.**  
- [ ] Active seccomp profile (default or custom) per workload at L2/L3  
- [ ] AppArmor/SELinux configured where applicable to the runtime/distro  
- [ ] `--privileged`, `hostPID`, `hostNetwork` and the Docker socket blocked by admission  
- [ ] Periodic *drift* verification of the effective state vs. the declared *baseline*, with flagging  

:::

**Artefacts & evidence.** Versioned seccomp/AppArmor profiles; admission policies that require the profile and block privilege; periodic *drift* report (effective vs. declared) with divergences and actions.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Default seccomp recommended; ad hoc *drift* verification | Mandatory seccomp + blocking of privilege + *drift* verification | All of L2 + custom profiles + continuous/automated *drift* verification |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Production | Pod creation | DevOps / SRE + Admission Controller | Immediate |
| Ops | *Drift* verification | AppSec Engineer + DevOps / SRE | Periodic (L3: continuous) |

**Useful links.** [Container Hardening](/sbd-toe/sbd-manual/containers-imagens/addon/hardening-containers), [OPA Runtime Policies](/sbd-toe/sbd-manual/containers-imagens/addon/policies-runtime-opa)

---

### US-22 - Image retention and clean-up with periodic renewal by SLA {#us-22---retenção-e-limpeza-de-imagens-com-renovação-periódica-por-sla}

Obsolete images accumulated in the registry are a latent attack surface and an audit cost.  

**Context.** `CNT-010` requires periodic rebuilds (or a trigger on base update) to incorporate patches, with flagging of images not rebuilt for more than X days. Without a retention/clean-up policy, the registry accumulates reusable vulnerable tags and dilutes the traceability of the commit → pipeline → image → execution chain.  

:::userstory
**Story.**   
As **DevOps / SRE**, I want an image retention/clean-up policy with periodic renewal by patching SLA and flagging of stagnant images, so as to avoid the accumulation of vulnerable artefacts and keep the registry auditable.  

**Acceptance criteria (BDD).**  
- **Given** a base image with a security patch available  
  **When** the renewal SLA applies  
  **Then** a rebuild (or automatic trigger) takes place within the time limit (L3: ≤30 days; L2: ≤60 days; L1: ≤90 days)  
- **Given** an image not rebuilt for longer than the defined limit  
  **When** the periodic verification runs  
  **Then** it is flagged and subject to renewal or deprecation  
- **Given** an obsolete or superseded tag in the registry  
  **When** the retention policy is applied  
  **Then** it is removed/archived while preserving traceability (digest → build → decision)  

**Checklist.**  
- [ ] Renewal SLA per risk level documented and met (`CNT-010`)  
- [ ] Automatic flagging of images not rebuilt beyond the limit  
- [ ] Retention/clean-up policy for obsolete tags in the registry (with criteria and archive)  
- [ ] Traceability preserved after clean-up (digest → pipeline → promotion decision)  

:::

**Artefacts & evidence.** Versioned retention/renewal policy; report of flagged stagnant images; registry clean-up/archive logs; traceability matrix preserved by digest.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Renewal ≤90 days recommended; ad hoc clean-up | Mandatory renewal + flagging + defined retention | Renewal ≤30 days + automated clean-up + traceability preserved and audited |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Ops | Base patch / renewal window | DevOps / SRE | Per SLA (L1 ≤90d; L2 ≤60d; L3 ≤30d) |
| GRC | Retention audit | GRC / Compliance | Periodic |

**Useful links.** [Secure Base Images](/sbd-toe/sbd-manual/containers-imagens/addon/imagens-base), [Inventory and SBOM](/sbd-toe/sbd-manual/containers-imagens/addon/sbom-containers)

---
## 📦 Expected artefacts {#-artefactos-esperados}

Each practice leaves a verifiable footprint - the artefacts.  
Without them, there is no way to prove compliance or carry out effective audits.  
The following table consolidates the main outputs that must be present in any containerised project.

| Artefact | Responsible | Evidence |
|-----------|-------------|-----------|
| `Dockerfile` with fixed digest | Developer | Git repo |
| SCA scanner reports | DevOps / SRE | Pipeline logs |
| Provenance + Cosign signature | AppSec Engineer | Metadata in the registry, Rekor entry |
| Versioned OPA/Kyverno policies | DevOps / SRE | Git repository, validated manifests |
| Admission Controller logs | GRC / Compliance | Reports of rejections and acceptances |
| **Image SBOM (CycloneDX/SPDX)** | DevOps / SRE | File attached to the artefact |
| **registry-allowlist.yaml** | DevOps / SRE | Admission policy applied |
| **Secret scan reports** | DevOps / SRE | CI logs + secret blocks |
| **RBAC/SA manifests** | DevOps / SRE | Permissions audit |
| **networkpolicy/*.yaml** | DevOps / SRE | Audit of intra-cluster flows |
| **golden-images-catalog.md** | DevOps / SRE / AppSec Engineer | Patching SLA + changelog |
| **Runner/builder config** | DevOps / SRE | Signing + ephemeral logs |
| **Enforcement dashboard** | DevOps / SRE / AppSec Engineer | Prometheus/Grafana with metrics |
| **Monthly compliance report** | GRC / Compliance | Blocked attempts, compliance rate |
| **RuntimeClass manifests (gVisor/Kata)** | DevOps / SRE | Pod specs with sandbox configured |
| **Audit of sensitive workloads** | DevOps / SRE / GRC / Compliance | Report of sandboxed pods |

---

## ⚖️ L1–L3 proportionality matrix {#️-matriz-de-proporcionalidade-l1l3}

Proportionality ensures that controls are not uniform, but rather adjusted to the real risk of each application.  
An L1 application does not require the same investment as a critical application (L3).  
The following table shows how to scale each practice.

| Practice | L1 | L2 | L3 |
|---------|----|----|----|
| Trusted base images | Yes | Yes | Yes |
| Pinning by digest | Recommended | Mandatory | Mandatory |
| Image scanning | Warning | Block High/Critical | Block Medium+ |
| Signing & provenance | Optional | Recommended | Mandatory |
| Runtime policies | Basic (non-root) | Restrictive | Complete + audit |
| Runtime monitoring | Basic | Critical | Full + automatic response |
| **SBOM per image** | Recommended | Mandatory | Mandatory (+ with provenance) |
| **Registry allowlist/digest-only** | Warning | Block by origin | Block + digest-only |
| **Secrets outside the image / OIDC** | Recommended | Mandatory | Mandatory + automatic rotation |
| **Minimal RBAC / dedicated SA** | Recommended | Mandatory | Mandatory + periodic review |
| **NetworkPolicy (ingress/egress)** | Basic | Critical ingress+egress | Full ingress+egress + audit |
| **Golden base + patch SLA** | Recommended | Mandatory | Mandatory + accelerated rollout |
| **Ephemeral/signed builders/runners** | Recommended | Mandatory | Mandatory + network segmentation |
| **Centralised enforcement with audit** | Recommended | Yes (logging + alerts) | Yes (logging + alerts + dashboard + review) |
| **Advanced sandboxing (gVisor/Kata)** | Optional | Recommended (sensitive workloads) | Mandatory (critical workloads) |

---

## 🏁 Final recommendations {#-recomendações-finais}

Container security must be understood as a **continuous cycle** and not as a list of isolated checks.  
More important than applying scattered controls is ensuring that they are integrated with one another, from the selection of the base image to incident response in production.

- **Containers are critical software artefacts**: they must be treated with SBOM, provenance, execution policies and audit like any business code.
- **Shift-left is imperative**: integrating scanners, linters and policies into CI/CD reduces risk and cost exponentially.
- **Signing and provenance (SLSA, Sigstore)** are practices in rapid adoption - they must already be included in new projects, especially at L2/L3.
- **Formal enforcement with audit** ensures that no execution escapes the controls; centralised metrics enable periodic review and compliance reporting.
- **Reinforced isolation** (gVisor/Kata sandboxes) is mandatory at L3 for critical workloads (payments, PII) - the complexity is justified by the risk.
- **Prevention + detection coexist**: restrictive policies in the cluster are essential, but runtime monitoring is equally critical for rapid response.
- **Governance must include clear metrics**: % of signed images, % of pipelines with active scanners, % of incidents detected/resolved, rate of compliance with policies.
- **Golden base images + allowlist + ephemeral and signed builders** are the security tripod - standardisation reduces supply chain risk.

In short: **containers are enablers of agility and portability, but only when treated with the same scientific discipline applied to any other critical software artefact**. Container security is not just the responsibility of DevOps: it is a cross-cutting concern of the Dev Team, AppSec, Platform and GRC.

---
