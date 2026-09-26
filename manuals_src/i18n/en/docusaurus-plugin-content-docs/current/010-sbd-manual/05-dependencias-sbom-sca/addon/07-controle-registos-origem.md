---
id: controle-registos-origem
title: Control of Registries and Package Origin
description: Policies for internal repositories, proxies, mirrors and provenance validation
tags: [dependencias, sbom, sca, supply-chai, invetario]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/07-controle-registos-origem.md
  source_sha256: 9c7e2c54199db7635a8b73bda16bdb19ccd396cc1c35f0b199662017fa314aba
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b354a83a09e3e160043df242d7065aa75f4e87cec775f8c7c9f9c22c92254627
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [framework_source_corpus, mirror_osf, provenance, validation_evaluation]
  glossary_sha256: b909cd447626667c96fedf18d490eef8e68ff128ac40800b9116804a557a9bf3
  translated_at: 2026-09-26T08:45:25Z
  stamped_at: 2026-09-26T18:33:50Z
  reviewed_by: null
---

# Control of Registries and Package Origin

## 🌟 Objective {#-objetivo}

Ensure that all third-party dependencies are obtained from **controlled, audited and trusted origins**, minimising the risk of attacks via public registries or unverified sources.

> ⚠️ The simple act of installing a package from a public repository may execute malicious code without any alert. This control is critical.

---

## 🔢 Concept of a trusted repository {#-conceito-de-repositório-confiável}

A repository is considered trusted when it:

- Is **internal or proxied**, controlled by the organisation
- Allows **auditing the history** of the packages used
- Implements **replication, caching and quarantine policies**
- Prevents direct access to external sources without validation

---

## 🏠 Technical options for an internal registry {#-opções-técnicas-para-registo-interno}

| Technology         | Languages / Formats       | Main characteristics                         |
|--------------------|------------------------------|-----------------------------------------------------|
| **Verdaccio**      | npm / Yarn (Node.js)         | Docker-ready, simple, caching + controlled fallback |
| **Sonatype Nexus** | Maven, npm, PyPI, Docker     | Enterprise-ready, RBAC, auditing and CI integration    |
| **JFrog Artifactory** | Multiple ecosystems     | Scalable, retention policies and replicators        |
| **GitHub Packages**| npm, Maven, Container        | Integration with GitHub Actions                      |

---

## 🚀 Controlled fallback strategy {#-estratégia-de-fallback-controlado}

1. The repository tries to obtain the package **locally**.
2. If it does not exist, it tries an external source **under policy validation** (domain whitelist or GPG keys).
3. The package is **cached locally** for future builds.
4. All accesses are **audited and tracked**.

> This approach drastically reduces exposure to compromised packages.

---

## 📝 Configuration recommendations {#-recomendações-de-configuração}

- Disable external `--registry` by default
- Provide `.npmrc`, `.pip.conf`, `settings.xml` with a predefined origin
- Prohibit installation with `latest` or without fixed versioning
- Validate package hashes or signatures (where supported)

---

## ✅ Additional benefits {#-benefícios-adicionais}

- Reproducibility of builds
- Less dependence on external availability (resilience)
- Faster build time with local caching
- Compliance with audit requirements (CRA, NIS2, ISO 27001)

---

## 🔗 Links to other files {#-ligações-com-outros-ficheiros}

| Document                   | Link to origin registries                      |
|-----------------------------|-----------------------------------------------------------|
| `06-risco-supply-chain.md`  | Mitigates typosquatting and downloads of unknown origin  |
| `04-integracao-ci-cd.md`    | Pipelines must use trusted registries only           |
| `03-governanca-libs-terceiros.md` | Defines who approves packages and which ones may be replicated |

---

> 🔒 The use of internal repositories with controlled fallback is a **structural** security measure, not an optional one. It must be part of the baseline of any secure pipeline.
