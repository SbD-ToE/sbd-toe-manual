---
id: quiz-terceiros
title: Validation Quiz - Training for Third Parties
sidebar_position: 22
description: Minimum questionnaire to validate the knowledge of external staff with technical permissions
tags: [formacao, terceiros, quiz, validacao, onboarding, contratados, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/22-template-quiz-terceiros.md
  source_sha256: 19cf82e1b740cd558fb450a8f5ccfdb7acddd1cf5a11aa32d04cb820f716fe87
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: da9cc081bed465839b192e4575a11be9ddf150cef325dfda349f13813ed7f205
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, papel_suporte, validation_evaluation]
  glossary_sha256: edf732e059ccc796c6bba209e0644e6ecf4e575fd9be139616030058fdb2a625
  translated_at: 2026-09-26T11:44:26Z
  stamped_at: 2026-09-26T18:36:03Z
  reviewed_by: null
---


# Validation Quiz - Training for Third Parties

This questionnaire is intended to validate whether third parties (suppliers, contractors or external teams) **have understood the minimum mandatory content** before receiving technical permissions.

> 📌 A minimum score of 80% and a formal record of the results are recommended.

---

## 🧪 Validation questions (base example) {#-perguntas-de-validação-exemplo-base}

1. **When may a third party receive access to repositories or pipelines?**
   - a) As soon as the contract is signed  
   - b) After validation of the training and a formal record  
   - c) When the PO so decides  
   - d) If it is read-only access  

   > ✅ Correct answer: **b)**

---

2. **What should be done on finding a secret (e.g. token, password) in a `.env` file committed to the repository?**
   - a) Ignore it, since it is in an ordinary file  
   - b) Delete it locally only  
   - c) Notify the team and follow the secret rotation process  
   - d) Note in the README that it is temporary  

   > ✅ Correct answer: **c)**

---

3. **Which of these behaviours is considered secure in a PR?**
   - a) Adding libraries without prior analysis  
   - b) Leaving security comments without context  
   - c) Using a PR template with a complete checklist  
   - d) Merging even with failures in the validators  

   > ✅ Correct answer: **c)**

---

4. **Who should be contacted in case of doubts about permissions or secure practices?**
   - a) Another third party on the same project  
   - b) GitHub directly  
   - c) The SPOC or internal channel indicated by the organisation  
   - d) Nobody, so as not to delay the work  

   > ✅ Correct answer: **c)**

---

## 📋 Record of result (template) {#-registo-de-resultado-modelo}

- Name: __________________________  
- Company / Entity: __________________________  
- Email: __________________________  
- Date: __________________________  
- Result (%): _________  
- Internal validator (name): __________________________  
- Access granted: ✅ / ❌  

---

## 🧭 Notes on use {#-notas-de-utilização}

- The quiz may be applied on paper, as a digital form, or embedded in the LMS
- It is recommended to keep the record per project or contract, with the date and the internal owner
- The training may be repeated in the event of failure or after contract renewal

> 💡 This quiz is an integral part of the formal third-party onboarding process. It may be adjusted by role or level of access, always keeping the basic validation principles.
