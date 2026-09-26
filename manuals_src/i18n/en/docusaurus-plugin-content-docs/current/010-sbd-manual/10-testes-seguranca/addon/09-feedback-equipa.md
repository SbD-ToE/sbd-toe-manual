---
id: feedback-equipa
title: Integrating Findings with the Teams
description: Mechanisms for continuous feedback of security test results to development and product teams.
tags: [feedback, findings, comunicação, equipas, segurança]
sidebar_position: 10
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/09-feedback-equipa.md
  source_sha256: e522db8e27d0aba5e9c24d53a56ea7c3b981dc3c51cf55e5baf8c41d40ef0b42
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: eddf49c709dd65e04ff8623cefd9e2d401236f69ae0fd37c78c9cd4f7849ad5b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, maturity]
  glossary_sha256: cb3678cf0362a9c66766c626a784d8b9238542bda3d36bdeb7ee7808053c826f
  translated_at: 2026-09-26T10:31:30Z
  reviewed_by: null
---


# Feedback to the Team on Security Results

## 🌟 Objective {#-objetivo}

To ensure that security test results are **delivered to the teams in a clear, contextualised and actionable way**, promoting:

- Technical and functional understanding of the findings;
- Accountability for fixes and improvements;
- Integration of security into the team's workflow and culture;
- Reduced response time and friction between AppSec and Dev.

> A finding is only addressed when it is **understood, accepted and prioritised** by the responsible team.

---

## 🔍 What “giving feedback to the team” means {#-o-que-significa-dar-feedback-à-equipa}

Giving feedback to the team involves:

- **Making findings available with context and impact**, not just tool IDs;
- **Avoiding noise**, false positives and redundancies;
- **Communicating in the channels where the team already operates** (e.g. PR, backlog, Slack);
- **Establishing mechanisms for continuous improvement and visibility**;
- **Fostering ownership and a constructive culture**.

> 💡 Security feedback should be an extension of the quality process, not a parallel channel.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Automate the delivery of findings at the team's points of contact**:
   - Automatic comments on pull requests (e.g. via Semgrep, SonarQube, GitHub Actions);
   - Contextual alerts (Slack, Teams, IDE notifications);
   - Security dashboards per project or release;
2. **Classify findings by severity and expected action** (e.g. “Fix now”, “Accept with justification”);
3. **Include technical and functional context** in the communication (e.g. CWE, stack trace, affected code);
4. **Integrate findings in the technical backlog with defined tags and owners**;
5. **Hold regular collaborative triage sessions with AppSec and Dev**;
6. **Ask the teams for feedback on the clarity and usefulness of the reports**.

---

## ✅ Good practices {#-boas-práticas}

- Use **inline comments on PRs** for SAST findings with clear context;
- Avoid PDF reports or manual exports - use live, integrated channels;
- Bring security into sprint review or refinement meetings;
- Establish tagging conventions in the backlog (e.g. `#security`, `#review-required`);
- Measure the average reaction and resolution time (lead time) per team or type of finding;
- Celebrate quick fixes, zero regressions and coverage milestones.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Strategic relevance                           |
|--------------------------------|---------------------------------------------------|
| `08-gestao-findings.md`        | Ensures the lifecycle of findings with technical context |
| Chapter 06 - Development  | Brings security closer to agile cycles and code ownership |
| Chapter 07 - Secure CI/CD     | Feedback delivery integrated in the pipeline         |
| Chapter 14 - Governance       | Management and maturity KPIs                      |

---

> 🧠 Effective feedback turns findings into decisions. **It is in the way risks are communicated that trust and security maturity are built.**
