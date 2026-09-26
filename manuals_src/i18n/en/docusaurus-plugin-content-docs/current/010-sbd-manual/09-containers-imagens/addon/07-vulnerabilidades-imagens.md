---
id: vulnerabilidades-imagens
title: Detection and Handling of Vulnerabilities in Images
description: Identification and technical analysis of vulnerabilities in containers as a risk signal, not as an automatic decision
tags: [containers, vulnerabilidades, cve, sca, trivy, syft, imagem]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/07-vulnerabilidades-imagens.md
  source_sha256: 600ee1864bd60f4c835c0617558117e2e079c2f24744ec0e72503510cc331aff
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: a6324f4631c69d45181f55fa64a2c8401c513806bc6434585104fd0f217b9b34
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, chapter_role, papel_suporte, sbdtoe_sbd, traceability]
  glossary_sha256: 72912f1ca34fe53d791abbf3637123c3bda2e6ebfd865070ab2b47640092c3e6
  translated_at: 2026-09-26T12:48:47Z
  stamped_at: 2026-09-26T18:34:52Z
  reviewed_by: null
---

# Detection and Handling of Vulnerabilities in Images

## 🌟 Objective {#-objetivo}

Ensure that all container images used in pipelines, test environments or production **are analysed for known vulnerabilities (CVEs)**, producing **objective technical signals** that support informed decisions on mitigation, acceptance or blocking.

This file defines **how to detect and classify vulnerabilities**, not how to decide automatically on the acceptability of risk.

---

## 🧬 What vulnerabilities in images are {#-o-que-são-vulnerabilidades-em-imagens}

Each container image includes potentially vulnerable **libraries, runtimes and binaries**, introduced through different routes:

- Inherited from the base image;
- Introduced by application dependencies;
- Transitive (dependencies of dependencies);
- Resulting from the build process itself.

A vulnerability identified by a scanner indicates:
- the presence of an affected component,
- association with a known CVE,
- potential technical impact.

> ⚠️ The presence of a CVE **does not automatically imply exploitable risk** in the real context of the application.

---

## ⚠️ Detection is not risk assessment {#️-deteção-não-é-avaliação-de-risco}

It is fundamental to avoid the following incorrect equivalence:

- ✔️ CVE detected → valid technical signal  
- ❌ CVE detected ≠ automatically unacceptable risk  
- ❌ High CVSS ≠ guaranteed real impact

Risk assessment requires additional context:
- code actually exposed;
- available attack vectors;
- runtime permissions and hardening;
- criticality of the application and data processed.

This file deals with **technical detection and classification**, not with the final decision.

---

## 📘 Analysis tools (SCA for containers) {#-ferramentas-de-análise-sca-para-containers}

| Tool        | Technical function                                  | Role in SbD-ToE                     |
|-------------------|-------------------------------------------------|--------------------------------------|
| **Trivy**         | Fast detection of CVEs                          | Initial signal                         |
| **Grype**         | SBOM ↔ vulnerability correlation              | Precision and traceability            |
| **Snyk Container**| Additional contextualisation (SaaS)               | Support for triage                       |
| **Docker Scout**  | Visualisation of layers and dependencies           | Exploratory analysis                  |

These tools **detect presence**, not exploitability or real impact.

---

## 🛠️ How to apply detection correctly {#️-como-aplicar-a-deteção-corretamente}

1. **Generate the SBOM of the final image** (see `06-inventario-sbom.md`);
2. **Run an SCA scanner** on the real image;
3. **Produce a technical report**, including:
   - CVE;
   - affected package;
   - version;
   - CVSS;
   - fix available or not;
4. **Classify the vulnerabilities technically**:
   - with a fix available;
   - without a fix available;
   - inherited from the base image;
5. **Preserve the results as versioned evidence**;
6. **Route the results to human analysis**, where applicable.

Automation **does not eliminate the need for interpretation**.

---

## 📂 Storage and traceability of results {#-armazenamento-e-rastreabilidade-dos-resultados}

To ensure auditability:

- Store reports per image and digest;
- Version results per build;
- Associate scanner, database and timestamp;
- Correlate with the SBOM and the image signature.

Untraceable results **have no operational or auditable value**.

---

## 🔍 Correct use of scanning results {#-utilização-correta-dos-resultados-de-scanning}

In SbD-ToE, vulnerability results must be used to:

- Prioritise fixes;
- Detect security regressions;
- Support documented acceptance or mitigation decisions;
- Feed continuous improvement metrics.

They must not be used as:
- a substitute for risk analysis;
- proof of security;
- a sole blocking mechanism without context.

---

## ✅ Good practices {#-boas-práticas}

- Define **initial technical thresholds** (e.g. CVSS ≥ 7) as a *trigger*, not as a verdict;
- Distinguish exploitable vulnerabilities from theoretical ones;
- Regularly review vulnerabilities inherited from the base image;
- Automate remediation when a fix is available;
- Document risk acceptance where applicable;
- Review decisions after incidents or new information.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relation to vulnerabilities                 |
|----------------------------------|----------------------------------------------|
| `01-imagens-base.md`             | Minimisation reduces the CVE surface         |
| `06-inventario-sbom.md`          | Scanner uses the SBOM as its basis                   |
| `03-assinatura-cadeia-trust.md` | Integrity of the analysed image              |
| `09-riscos-processo-imagens.md` | Scanners as a signal, not a decision             |
| `15-aplicacao-lifecycle.md`     | Integration into the SSDLC                          |

> 🚨 Detected vulnerabilities are **technical signals**, not sentences.  
> Real risk only exists when the signal is interpreted in the correct context.
