---
id: guidelines-equipa
title: Team Guidelines and Shared Practices
sidebar_position: 7
description: Documenting and aligning security practices across teams, promoting coherence and a common technical baseline
tags: [equipa, guidelines, alinhamento, práticas seguras, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/07-guidelines-equipa.md
  source_sha256: 126c6a2b88e9fdecd4397a41b34227187064f89611d6052eae5df5b6cd7ec50d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e4c8ffb04ca49464409fb51f1290678d0cef38a43797972b3df24d6aaef0ba5f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [mapping, traceability, validation_evaluation]
  glossary_sha256: 0a704914492e5a71993701e9c07ae7f3cfd56d1a38711767a2ad60ec965325ef
  translated_at: 2026-09-26T08:57:12Z
  reviewed_by: null
---


# Team Guidelines and Shared Practices

> 💡 **Practical note**:  
> The dissemination of secure development practices depends not only on technical rules, but also on **culture, practical examples and active sharing among team members**.  
> Platforms such as **Confluence, GitHub Wiki, Notion, Google Docs** or even Markdown files versioned in the repository can be used to keep guidelines accessible and contextualised.  
> These guidelines must evolve over time and reflect both organisational policy and the real errors and improvements observed in projects.

---

## 📌 Objectives {#-objetivos}

- Consolidate and disseminate secure development practices among team members.
- Reduce reliance on repetitive manual validations.
- Make recurring security decisions and technical validation criteria explicit.
- Support the technical onboarding of new developers.
- Promote continuous improvement and living documentation.

---

## 👥 Who should apply it {#-quem-deve-aplicar}

- **The whole development team**: contributes to the improvement and adoption of the guidelines.
- **Technical leads (tech leads, senior devs)**: curation, validation and regular updating.
- **Security / AppSec**: ensures alignment with organisational policies.

---

## ⏱️ When to apply it {#️-quando-aplicar}

- During the initial technical planning of a project or component.
- As part of the onboarding of new team members.
- After incidents, reviews or internal audits.
- Whenever recurring patterns of failures or exceptions emerge.

---

## 🧱 Recommended requirements {#-requisitos-recomendados}

1. **Document secure practices, examples and accepted patterns**
   - By technology stack or type of application (frontend, backend, API, etc.)

2. **Keep the guidelines versioned and accessible**
   - Ideally alongside the code or in an integrated knowledge base.

3. **Update the guidelines based on real errors**
   - Include real examples of findings and how to avoid or fix them.

4. **Integrate the guidelines into team rituals**
   - E.g. weekly review, pull request clinic, tech talks or retros.

5. **Promote sharing across teams**
   - Reuse patterns, secure snippets, avoidable anti-patterns.

---

## ✅ How to validate {#-como-validar}

- Explicit reference to the guidelines in PR templates.
- Inclusion of a link to the relevant guideline section in technical reviews.
- Records of periodic review and updating of the document.
- Visible adoption in code examples and in the most recent projects.

---

## 🧾 How to evidence it {#-como-evidenciar}

- `guidelines/` repository versioned per project or per stack.
- Wiki or shared document with revision history.
- Mapping between recurring findings and guideline sections.
- Inclusion in the onboarding plan or in the new-member checklist.

---

## 🔄 Link to other practices {#-ligação-a-outras-práticas}

| Theme                                | Associated file               |
|-------------------------------------|----------------------------------|
| Secure coding good practices | `addon/01-boas-praticas-codigo.md` |
| Validation by linters and reviewers   | `addon/02-linters-validacoes.md`, `addon/08-validacoes-codigo.md` |
| Justification of exceptions            | `addon/05-excecoes-e-justificacoes.md` |
| Traceability of validations       | `addon/09-anotacoes-evidencia.md` |

---

> 📌 Guidelines are the link between organisational policy and the team's concrete practice.  
> They must be useful, living and continuously improved based on the technical reality of projects.
