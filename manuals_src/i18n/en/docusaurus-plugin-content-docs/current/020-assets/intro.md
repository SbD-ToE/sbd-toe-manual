---
id: intro
title: Organisational Assets
description: Policies, templates and guides for implementing the SbD-ToE framework
translation:
  source_locale: pt
  source_path: 020-assets/intro.md
  source_sha256: 1214980d232d650d6c6772187829128aa91ae40cf7eba7fd053e03544870a51d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 54bc804c100243643e688906a0dd316cfb8549ed93261043a816ac06f1c821b6
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [chapter_role, framework_source_corpus, practitioner_manual, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 3073458b9deb1843aa713ee6609ea5bcf32342bfecdc9dc878d07b693aa18b29
  translated_at: 2026-09-26T14:10:41Z
  reviewed_by: null
---

# Organisational Assets

Welcome to the central repository of **organisational policies** and **implementation templates** for the **Security by Design – Theory of Everything (SbD-ToE)** framework.

## 📌 What is found here {#-o-que-encontra-aqui}

### **Organisational Policies** {#políticas-organizacionais}

These are **formal policies** that legitimise, operationalise and audit the security practices described in the 14 chapters of the SbD-ToE Manual.

**Why do policies matter?**
- ✅ They make practices **binding** across the whole organisation
- ✅ They serve as the basis for **internal and external audits**
- ✅ They enable **traceability** of security decisions
- ✅ They ensure **consistency** across processes

**Examples of available policies:**
- 🎯 Risk Classification and Acceptance
- 📋 Security Requirements
- 🏗️ Secure Architecture
- 🔄 Secure CI/CD
- 📦 Dependency Management
- 🐳 Secure Containers
- 📊 Monitoring and Operations
- 🎓 Training and Onboarding

Each policy is **reusable**, **adaptable** to each organisation and **aligned** with standards such as ISO/IEC 27005, NIST SSDF, OWASP SAMM and CIS Controls.

---

## 🔗 Cross-Reference {#-referência-cruzada}

The policies are **mapped to the chapters of the Manual**:

| Chapter | Recommended Policies |
|----------|------------------------|
| 1. Application Classification | Risk Classification, Periodic Review, Traceability |
| 2. Security Requirements | Security Requirements, Backlog Integration |
| 3. Threat Modelling | Threat Modelling, Model Validation |
| 4. Secure Architecture | Secure Architecture, Technical Design Approval |
| 5. Dependencies (SBOM/SCA) | Dependencies, SBOM, CVE Exceptions, Automatic Updates |
| 6. Secure Development | Development Guidelines, Code Review, GenAI |
| 7. Secure CI/CD | Secure CI/CD, Secrets Management |
| 8. IaC & Infrastructure | Secure IaC, Plan Approval |
| 9. Containers and Images | Secure Containers, Golden Base Images |
| 10. Security Testing | Testing Strategy, PenTesting |
| 11. Secure Deployment | Secure Deployment, Release Approval, Rollback |
| 12. Monitoring and Operations | Monitoring, Logging, Alerts, Incident Response |
| 13. Training and Onboarding | Security Training, Training KPIs |
| 14. Governance and Contracting | Secure Contracting, Governance, Organisational Traceability |

---

## 📂 Structure {#-estrutura}

```
020-assets/
├── intro.md (este ficheiro)
└── policies/
    ├── 01_policy-dast-fuzzing.md
    ├── 02_policy-classificacao-risco.md
    ├── 03_policy-aceitacao-risco.md
    └── ... (mais 34 políticas)
```

---

## 🚀 How to Use {#-como-usar}

1. **Identify the chapter**: Select which chapter of the SbD-ToE Manual is relevant to the initiative at hand
2. **Consult the corresponding policy**: Each chapter points to the recommended policies
3. **Adapt to the organisation**: Use the policies as a basis, tailoring them to the context
4. **Implement and audit**: Ensure compliance through periodic audits

---

## 💡 Aligned Standards & Frameworks {#-normas--frameworks-alinhados}

The policies documented here are aligned with:

- 🔒 **ISO/IEC 27005** – Information Security Risk Management
- 🛡️ **NIST SSDF** – Secure Software Development Framework
- 📋 **OWASP SAMM** – Software Assurance Maturity Model
- 🎯 **CIS Controls v8** – Critical Security Controls
- 🌐 **ENISA Risk Management** – European Recommendations

---

## 📞 Support {#-suporte}

For questions, contributions or feedback on these policies, consult:
- **Manual Documentation**: [Security by Design – Complete Manual](/sbd-toe/sbd-manual/)
- **Repository**: https://github.com/Shiftleftpt/SbD-ToE-Manual

**Last updated**: 30 March 2026
