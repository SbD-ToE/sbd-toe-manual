---
id: anotacoes-evidencia
title: Annotations and Evidence of Validations
sidebar_position: 9
description: Strategies for annotating security validation decisions and evidence in the code itself or in the development cycle
tags: [evidência, anotação, validação, rastreabilidade, SDLC]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/09-anotacoes-evidencia.md
  source_sha256: c66d2cc4dcd6b5be96ca965975fc0dad9f42e2f2610d32617412df8c7c5c1494
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 3e583e0dab9784aebe3f1335ef1b6f34f4b1c8ef771e05c87da0bfd295e67991
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, cycle_iteration, framework_source_corpus, practitioner_manual, requirement_runtime, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: e3f175002bf6d1733d671d9e25117226bcc721eb7cbb94286454410042b98741
  translated_at: 2026-09-26T08:57:13Z
  stamped_at: 2026-09-26T18:34:05Z
  reviewed_by: null
---

# Annotations and Evidence of Validations

> 💡 **Practical note**:  
> Tools such as **GitHub**, **GitLab**, **Xygeni**, **SonarQube**, **Semgrep**, or even simple editors such as **VSCode** allow the use of **structured comments, labels and special markings** indicating that a security validation has been carried out - or that an exception has been accepted.  
> These annotations make review more effective, help build traceability and serve as auditable evidence of the practical application of the security guidelines.

---

## 📌 Objectives {#-objetivos}

- Make the application of security validations visible and traceable.
- Facilitate technical reviews and internal audits.
- Reinforce the culture of explicit validation and accountability for technical decisions.
- Support exception processes, review of findings and quality control.

---

## 👥 Who should apply it {#-quem-deve-aplicar}

- **Developers**: when writing or reviewing sensitive code.
- **Technical reviewers**: when accepting PRs with a security impact.
- **Security / AppSec**: when assessing exceptions, justifications and traceability.

---

## ⏱️ When to apply it {#️-quando-aplicar}

- During development, in code with security requirements or risk.
- At the time of review of sensitive PRs and pull requests.
- When justifying findings from SAST/SCA tools.
- Whenever an exception is accepted or mitigated by design.

---

## 🧱 Good annotation practices {#-boas-práticas-de-anotação}

1. **Use standardised and searchable markings**
   - E.g. `@sec:input-validated`, `@sec:auth-required`, `@sec:checked`, `@sec:waived`

2. **Annotate directly in the code, next to the critical function**
   - Preferably before blocks of sensitive logic.

3. **Associate the annotation with the formal reference (requirement, exception, finding)**
   - E.g. `@sec:justificado #SEC-EXC-014`, `@sec:reviewed-CWE79`

4. **Reuse comments in reviews and reports**
   - Annotations serve as a source for generating evidence and reports.

5. **Do not overuse - only where there is an explicit decision**
   - Useless comments reduce the signal-to-noise ratio and lose technical value.

---

## ✅ How to validate {#-como-validar}

- Automated verification by script (e.g. `grep @sec:` or verification in CI).
- Technical review checklist with a mark for the presence of tags.
- Manual confirmation by a reviewer that the annotation is justified.
- Integration with traceability panels (e.g. Xygeni, internal dashboards).

---

## 🧾 How to evidence it {#-como-evidenciar}

- Presence of the annotations in versioned code (per commit or PR).
- Scan logs that reference or extract these markings.
- Release reports indicating annotated blocks and their function.
- Traceability table `@sec:*` → requirement/finding → justification (if an exception).

---

## 🔄 Link to other practices {#-ligação-a-outras-práticas}

| Theme                                      | Associated file               |
|-------------------------------------------|----------------------------------|
| Justification of exceptions                  | `addon/05-excecoes-e-justificacoes.md` |
| Code review and validation             | `addon/08-validacoes-codigo.md` |
| Development and team guidelines    | `addon/01`, `addon/07`           |
| Integrated linters and scanners             | `addon/02`, tools with tagging |

---

> 📌 Annotations are a lightweight but powerful means of **making validations auditable, traceable and collaborative**.  
> They must be part of the normal technical process and respect conventions well defined by the team or organisation.
