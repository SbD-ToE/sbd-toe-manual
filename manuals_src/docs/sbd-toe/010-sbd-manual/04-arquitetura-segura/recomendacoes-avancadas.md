---
id: recomendacoes-avancadas
title: Recomendações Avançadas - Arquitetura Segura
description: Práticas avançadas para contextos de elevada maturidade em arquitetura segura
tags: [avancado, arquitetura, maturidade, zero-trust, sbomm]
sidebar_position: 30
---

# 🧠 Recomendações Avançadas - Arquitetura Segura

Este documento complementa as práticas fundamentais do capítulo com recomendações orientadas a contextos de **elevada maturidade organizacional**, sistemas críticos ou ambientes regulamentados.

> As recomendações aqui descritas são opcionais, mas altamente desejáveis para equipas que já aplicam os requisitos ARC de forma consistente.

---

## 🧱 Recomendações Arquitetónicas Avançadas

| Prática / Recomendação                             | Benefício direto                             | Requisitos reforçados |
|------------------------------------------------------|------------------------------------------------|------------------------|
| Adotar o princípio de Zero Trust entre microserviços  | Reduz risco de lateral movement                | ARC-002, ARC-006       |
| Aplicar OPA ou rego para enforcement dinâmico        | Governa políticas de acesso da arquitetura       | ARC-001, ARC-008       |
| Usar sidecars para segurança e comunicação interservice | Cria controlo de rede e logging distribuído   | ARC-002, ARC-003       |
| Aplicar segmentação em ambiente de CI/CD             | Garante que a execução reflete o desenho arquitetónico | ARC-004, ARC-007 |
| Integrar threat modeling em stories e epics          | Deteta falhas antes do desenho detalhado       | ARC-005, ARC-010       |
| Formalizar ADRs para todas as decisões de arquitetura  | Melhora auditabilidade e revisão futura        | ARC-004, ARC-011       |
| Validar consistência entre arquitetura e SBOMs       | Garante que o SBOM reflete a arquitetura planeada | ARC-006, ARC-007       |

---

## 🧩 Modelos e Frameworks Recomendados

- **Modelo de Confiança por Contexto** (Context-Aware Trust Models)
- **Architecture Decision Records (ADRs)** com integração Git
- **Modelos de Zoneamento Baseado em Risco**
- **Threat Modeling como parte da Definition of Done**
- **Frameworks**: SABSA, ISO/IEC 42010, NIST SP 800-160 Vol 1
- **SBOMM** (Security BOM Maturity Model) - integração entre arquitetura e composição de software

---

## ✅ Quando aplicar estas recomendações?

- Ambientes regulamentados (financeiro, saúde, defesa)
- Arquiteturas distribuídas de alta complexidade (ex: multicloud, event-driven)
- Plataformas com alto volume de integração externa
- Organizações com função de arquitetura ou segurança dedicada

> 🧭 Estas recomendações alinham com os níveis mais elevados de maturidade em SAMM, SSDF e DSOMM.

---

## 🤖 Padrões arquitetónicos para sistemas AI/ML {#ai-ml}

Sistemas que integram componentes de inteligência artificial — LLMs em interface conversacional, modelos preditivos, sistemas de retrieval-augmented generation (RAG), agentes autónomos com tool invocation — introduzem padrões arquitetónicos com superfícies de ataque qualitativamente distintas das aplicações tradicionais. As recomendações nesta secção complementam (não substituem) ARC-001..ARC-013 e operacionalizam o requisito [ARC-014](./addon/catalogo-requisitos#arc-014).

### Trust zones em arquitecturas AI/ML

Componentes AI/ML introduzem três classes de fronteira de confiança que devem ser explicitamente marcadas em DFDs:

| Boundary | Descrição | Ameaças canónicas | Controlos arquitectónicos típicos |
|---|---|---|---|
| **Training-time** | Entre datasets externos e pipeline de treino | Training data poisoning (`AML.T0020`); Publish Poisoned Datasets (`AML.T0019`); ML02-2023 Data Poisoning | Curadoria de fontes; checksum/signature de datasets; isolamento de pipeline de treino; revisão humana antes de retraining |
| **Inference-time** | Entre input externo (utilizador, RAG retrieval, file ingestion) e contexto do modelo | Prompt injection directa e indirecta (LLM01-2025; `AML.T0051.001`); `AML.T0093` Prompt Infiltration via Public-Facing App | Input sanitization específico para prompt context; separação clara entre system prompt e user input; output filtering anti-extracção de system prompt |
| **Agentic** | Entre output do modelo e tool invocations executadas (functions, MCP servers, APIs) | Exfiltration via AI Agent Tool Invocation (`AML.T0086`); AI Agent Tool Poisoning (`AML.T0110`); Data Destruction via AI Agent (`AML.T0101`); LLM06-2025 Excessive Agency | Aprovação humana para acções write/mutativas; rate limiting por tool; allowlist de tool scopes; logging completo de tool calls (ver Cap. 12 — observabilidade AI) |

### Boundary controls para prompt injection

Prompt injection é a vulnerabilidade arquitectónica mais comum em aplicações LLM. Controlos arquitectónicos relevantes:

- **Separar canalmente** system prompt (configuração da aplicação) de user input (dados não confiáveis) — usar mensagens estruturadas (ex: roles `system`/`user`/`assistant`) em vez de string concatenation
- **Tratar todo conteúdo retrieval-augmented como user-level untrusted** — em sistemas RAG, documentos retornados são dados externos; aplicar mesmos controlos que ao input directo do utilizador (`AML.T0051.001` Indirect Prompt Injection)
- **Output filtering** anti-extracção de system prompt (`AML.T0069.002`); detectar padrões de exfiltração de instruções
- **Confidentialidade de system prompts** — não assumir que o conteúdo é secreto; arquitectar como se fosse público

### LLM ↔ backend tool invocation security

Agentes AI com capacidade de invocar tools backend (APIs, file systems, databases via MCP, function calls) exigem isolamento arquitectónico análogo a controlo de privilégios em sistemas tradicionais:

- **Princípio de menor privilégio aplicado a agentes** — cada tool exposta a um agente AI deve ter scope mínimo necessário; agentes não devem operar com credentials de utilizador real (LLM06-2025 Excessive Agency)
- **Aprovação humana out-of-band** para tool calls com impacto crítico (delete, transfer, send) — particularmente relevante em workflows em que o agente é autónomo
- **Auditoria completa de tool invocations** — cada chamada com timestamp, contexto, agent identity, scope; integrar com pipeline de observabilidade do Cap. 12 (`AML.M0024` AI Telemetry Logging)
- **Validação de MCP servers e tools** como dependências de supply chain — ver Cap. 5 §AI/ML para framing supply chain (`AML.T0110` AI Agent Tool Poisoning)

### Considerações de design

- **AI components NÃO são bibliotecas opacas** — devem aparecer como participantes distintos em DFDs de arquitectura, com inputs, outputs, dependências (modelos, datasets, prompts) e trust boundaries explicitamente modeladas
- **Cross-zone propagation** — outputs de modelos AI podem propagar-se a zonas de confiança elevada (ex: model output usado para tomar decisões automáticas em sistemas críticos); aplicar mesma análise de propagation que aplicaria a inputs externos não confiáveis
- **Resiliência a model degradation** — design considera fallback para quando o modelo está indisponível, retorna outputs degradados, ou foi comprometido (`AML.T0031` Erode AI Model Integrity)

> A análise de threat modeling para arquitecturas AI/ML usa MITRE ATLAS como complemento a STRIDE — ver [Cap. 03 — Metodologias AI/ML](../03-threat-modeling/addon/metodologias-e-ferramentas#ai-ml).

---

## 📌 Consideração Final

Estas práticas não substituem os requisitos normativos (ARC), mas representam **próximos passos naturais para equipas que já aplicam arquitetura segura de forma estruturada e consistente**.

> Aplicar estas recomendações de forma seletiva pode acelerar a maturidade e prepara a organização para modelos de governaça baseados em evidência e controlo distribuído.
