---
id: tecnicas-formativas
title: Training Techniques Adapted to Technical Reality
description: Set of effective pedagogical approaches for promoting retention, applicability and motivation.
tags: [formacao, tecnicas, pedagogia, segurança aplicada, exemplos]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/04-tecnicas-formativas.md
  source_sha256: 39883087bb1b267c476e447d8b322ae06382e431ade9ea7b270f077dd9ae5208
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 7603dfb632fff8192340a8097178e40c586af122653a21dfb91f9ce8f8721a0d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, maturity, threat, v1_entity_tmr_peer_review, validation_evaluation]
  glossary_sha256: c2a04eff6a353937fac6d25ba5b4e9ed147715706f2c68446ba37edf3c24a160
  translated_at: 2026-09-26T11:44:18Z
  stamped_at: 2026-09-26T18:35:54Z
  reviewed_by: null
---


# Advanced Training Techniques

## 🌟 Objective {#-objetivo}

To strengthen practical learning in security through **active training methods**, applicable in the real context of the technical teams.

These techniques are especially useful in organisations with distributed teams or with growing maturity, where traditional training is not enough.

The training techniques described aim to strengthen people's understanding and critical capacity,
complementing - and not replacing - the existing automated mechanisms.


---

## 🧬 What advanced training techniques are {#-o-que-são-técnicas-formativas-avançadas}

They are approaches centred on **practical experience**, which connect knowledge to execution:

- Contextualised: based on real risks or errors
- Iterative: incorporated into sprints, reviews, incidents
- Engaging: labs, simulations, clinics, peer-led sessions
- Facilitated: with the support of Champions or designated people

---

## 🛠️ How to apply - Suggested techniques {#️-como-aplicar---técnicas-sugeridas}

### 1. CTF (Capture The Flag) {#1-ctf-capture-the-flag}

| Aspect            | Details                                                                 |
|-------------------|--------------------------------------------------------------------------|
| 🎯 Objective       | Explore intentional flaws and solve security challenges            |
| 👥 Target audience   | Developers, QA, AppSec, Champions                                         |
| 🛠️ Format        | Internal or external (public or organised platform)                    |
| 💡 Recommendations  | Real labs, leaderboard, themes by stack or threat                       |

> Ideal for strengthening technical knowledge and detecting gaps in real practice.

---

### 2. War Room / Incident Simulation {#2-war-room--simulação-de-incidente}

| Aspect            | Details                                                                 |
|-------------------|--------------------------------------------------------------------------|
| 🎯 Objective       | Assess incident response in real time                              |
| 👥 Target audience   | Dev, QA, PO, DevOps, AppSec                                               |
| 🛠️ Format        | Simulation of real incidents, focusing on communication and validation           |
| 💡 Recommendations  | Use real history as the basis, hold an educational debrief                   |

> Excellent for aligning behaviours and processes under pressure.

---

### 3. Code Clinics / PR Live Reviews {#3-code-clinics--pr-live-reviews}

| Aspect            | Details                                                                 |
|-------------------|--------------------------------------------------------------------------|
| 🎯 Objective       | Learn from real reviews, strengthen secure standards                    |
| 👥 Target audience   | Developers, QA, Champions                                                |
| 🛠️ Format        | Regular sessions with collective reviews (30–45 min)                     |
| 💡 Recommendations  | Real PRs with good practices and common errors                               |

> Low friction, highly effective. It can be part of the sprint review.

---

### 4. Threat Modeling Peer-led {#4-threat-modeling-peer-led}

| Aspect            | Details                                                                 |
|-------------------|--------------------------------------------------------------------------|
| 🎯 Objective       | Analyse technical risks in the design in a participatory way                |
| 👥 Target audience   | Technical team with the support of a Champion                                     |
| 🛠️ Format        | Regular sessions (per epic, sprint or release)                         |
| 💡 Recommendations  | Templates + repository of outputs (e.g. draw.io, markdown)               |

> A technique that trains and applies at the same time.

---

### 5. Learning Logs / Repository of Real Failures {#5-learning-logs--repositório-de-falhas-reais}

| Aspect            | Details                                                                 |
|-------------------|--------------------------------------------------------------------------|
| 🎯 Objective       | Learn from documented incidents or errors                            |
| 👥 Target audience   | The whole technical organisation                                                |
| 🛠️ Format        | Wiki or internal page (no blame), integrated into labs                    |
| 💡 Recommendations  | Validate as part of internal quizzes or labs                           |

> Encourages a culture of continuous improvement based on real failures.

---

### 6. Guided Labs {#6-labs-dirigidos-guided-labs}

| Aspect            | Details                                                                 |
|-------------------|--------------------------------------------------------------------------|
| 🎯 Objective       | Perform specific tasks in a controlled environment                      |
| 👥 Target audience   | All technical roles                                                  |
| 🛠️ Tools    | Juice Shop, Secure Code Warrior, internal labs, etc.                     |
| 💡 Recommendations  | Integrate into onboarding, validate before permissions (deploy, merge)      |

> Ideal for technical onboarding and validation of competences.

---

## ✅ Good practices {#-boas-práticas}

- Start with 1 or 2 techniques adapted to the team's maturity
- Define learning objectives per technique
- Maintain a repository of examples by stack or type of threat
- Involve Security Champions in facilitation
- Measure impact: participation, feedback and observed improvement

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relevance                                       |
|-----------------------------------|--------------------------------------------------|
| `03-programa-champions.md`        | Champions as facilitators                     |
| `01-catalogo-formativo.md`        | Techniques aligned with the training themes      |
| `15-aplicacao-lifecycle.md`       | Continuous application of these techniques in the rituals   |
| `90-indicadores-metricas.md`      | Assessment of the impact of and adherence to the techniques        |

---

> 🧠 Continuous practical learning is the true catalyst of security maturity. These techniques help to turn knowledge into action - and culture into behaviour.
