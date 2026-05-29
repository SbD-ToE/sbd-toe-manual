---
id: policy-mandates-agentes
title: Política de Mandates de Agentes AI
description: Política organizacional que define o ciclo de vida do mandate de cada agente AI em uso operacional — registo, ownership, níveis de autonomia A0-A4, escopo de tools, revisão periódica e revogação, em alinhamento com REQ-AGN-001..004 do Cap. 02 e ARC-015 do Cap. 04, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, agentic, AI, mandates, autonomy, governance, REQ-AGN, ARC-015, L1, L2, L3, cap02, cap04, cap14]
grupo: governacao
sidebar_position: 38
---

# Política de Mandates de Agentes AI

## 1. Objetivo

Esta política define o **ciclo de vida do *mandate*** de cada agente AI em uso operacional na organização: como se regista, quem é o *owner*, que nível de autonomia (A0–A4) lhe atribuímos, que *tools* pode invocar, em que ambientes opera, e com que cadência revemos.

Operacionaliza directamente o requisito [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia) do Cap. 02 e suporta o requisito arquitectónico [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) do Cap. 04. A [Policy 16 — Uso de Ferramentas de Apoio ao Desenvolvimento](./policy-uso-ferramentas-apoio) (secção 11) cobre as regras operacionais para agentes A2+; esta Policy 38 cobre o *contrato* sob o qual o agente opera.

> 🧭 **Em duas frases:** a Policy 16 diz *o que* o agente pode e não pode fazer; esta Policy 38 diz *quem decidiu*, *com que autoridade*, *durante quanto tempo*, e *quando voltamos a perguntar*.

## 2. Âmbito

Esta política aplica-se a **qualquer agente AI** em uso operacional na organização que opere em **nível A1 ou superior**, incluindo (sem carácter exclusivo):

- Clientes AI com capacidade de tool-use que actuam em recursos da organização (Claude Code, Cursor agent mode, Copilot Workspace, Devin, agentes construídos sobre Anthropic SDK ou OpenAI Assistants API)
- Agentes integrados em CI/CD (auto-fix de findings SAST, geração e merge de PRs, atualização de dependências assistida)
- Agentes de operação (remediação de alertas, *moderation*, manutenção automatizada)
- Agentes de produto que actuam em sistemas internos por instrução de utilizador final

Não está no âmbito:
- Uso A0 (consulta sem execução), que continua coberto pela Policy 16 secções 1–10
- Modelos AI que são parte do produto sem capacidade de tool-use externa (caem em Cap. 04 ARC-014 e cross-check AI Act)

## 3. Princípio fundamental: o mandate é um acto formal de autorização

Um *mandate* é a forma como a organização declara, por escrito e versionada, que **autoriza este agente, com este nível de autonomia, a actuar neste escopo, durante este período, sob este *owner*, com este *kill-switch***. Não é metadado — é um contrato interno entre quem opera o agente e quem responde pelo seu efeito.

:::warning
Operar um agente A1+ sem *mandate* válido é o equivalente a dar acesso *production* a uma identidade não-humana sem revisão IAM. Esta prática é proibida em qualquer nível de criticidade.
:::

A4 exige adicionalmente **mandate assinado pelo `CISO`** (ou equivalente); sem essa assinatura, o agente não opera em A4.

## 4. Conteúdo mínimo de um mandate

Cada *mandate* é um documento versionado em VCS (formato Markdown ou YAML, à escolha da organização — o conteúdo é que importa) com, no mínimo:

| Campo | Conteúdo | Notas |
|---|---|---|
| `agent_id` | Identificador único do agente | Distinto por agente e por ambiente (e.g. `sbd-toe-pr-auditor@staging`) |
| `agent_runtime` | Cliente AI e versão; modelo subjacente e versão pinned | E.g. *Claude Code 1.x + claude-opus-4-7*; `latest` proibido |
| `autonomy_level` | A0 / A1 / A2 / A3 / A4 | Conforme [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia) |
| `scope` | Repositórios, *namespaces*, sistemas, dados sobre os quais opera | Lista positiva; sem wildcards desnecessários |
| `tools_allowlist` | Tools permitidas com argumentos máximos e *destrutividade* | Cada *tool* etiquetada como `read` / `write` / `destructive` / `external` |
| `environments` | Onde opera (`dev`, `staging`, `prod`, …) | Identidade dedicada por ambiente (Cap. 04 `ARC-011` + `ARC-015`) |
| `identity_ref` | Workload identity / *service account* / OIDC subject | Sem reuso de credenciais humanas |
| `owner` | Humano responsável pela operação | Necessariamente humano; com *backup* nomeado |
| `approver` | Quem aprovou o mandate | `tech lead` (L1), `appsec + tech lead` (L2), `CISO + appsec + grc` (L3 ou A4) |
| `kill_switch` | Procedimento + responsável + tempo máximo de efeito | Documentado e exercitável (`REQ-AGN-003`) |
| `intent_audit_sink` | Onde aterram os *intent events* (`REQ-AGN-004`) | Sistema observável (Cap. 12) |
| `review_cadence` | Quando voltamos a perguntar | A1: anual · A2: anual · A3: semestral · A4: trimestral |
| `effective_from` / `effective_until` | Janela de validade do mandate | `effective_until` obrigatório; sem mandates "para sempre" |
| `risk_residual` | O que esta autorização não cobre / aceita | Honesto sobre limites |

> 💡 Templates de exemplo: ver `020-assets/templates/mandate-agente.yaml` quando estiver publicado. Até lá, o esquema acima é suficiente para começar.

## 5. Ciclo de vida do mandate

```
[Proposta] → [Avaliação] → [Aprovação] → [Activação] → [Operação] → [Revisão / Renovação | Revogação]
```

### 5.1 Proposta

Quem quer operar um agente em A1+ submete proposta de *mandate* contendo todos os campos da secção 4 e justificação do nível de autonomia escolhido. A justificação responde a *"porquê A2 e não A1?"* — não basta declarar; é preciso fundamentar.

### 5.2 Avaliação

| Critério | Quem avalia |
|---|---|
| Adequação técnica do nível ao trabalho real | `tech lead` + `appsec` |
| Adequação do *scope* e da *tools_allowlist* (least privilege) | `appsec` |
| Adequação do *kill-switch* e tempo de efeito | `appsec` + `devops` |
| Cobertura de testes de revert (A3+) | `qa` + `tech lead` |
| Conformidade regulatória (AI Act, RGPD, etc., se aplicável) | `grc` / `compliance` |

### 5.3 Aprovação

| Nível | Aprovador exigido |
|---|---|
| A1 | `tech lead` |
| A2 | `tech lead` + `appsec` |
| A3 | `tech lead` + `appsec` + `grc` |
| A4 | `CISO` (assinatura formal) + `appsec` + `grc` |

A aprovação é registada no próprio *mandate* (campo `approver` + commit assinado em VCS).

### 5.4 Activação

Ao activar, verificamos pré-requisitos operacionais:

- [ ] Identidade efémera do agente criada (`identity_ref` resolve a workload identity real)
- [ ] *Scope* e *tools_allowlist* configurados na infraestrutura (não apenas declarados no doc)
- [ ] *Kill-switch* testado em sandbox/staging com cronómetro registado
- [ ] Sink de *intent events* a receber eventos de teste
- [ ] Notificação a *owner* + *backup* configurada

Sem todos os pré-requisitos, o agente fica em A1; não opera no nível pedido.

### 5.5 Operação

Durante a operação o *mandate* é a fonte da verdade do que o agente pode fazer. Qualquer alteração de *scope*, *tools_allowlist* ou *autonomy_level* obriga a **novo ciclo Proposta → Aprovação** — não há *amendments* informais.

### 5.6 Revisão / Renovação

Na cadência declarada (`review_cadence`), o *owner* + `appsec` revêem:

- [ ] *Intent events* da janela: *intent-action divergence* observada?
- [ ] *Off-policy actions* registadas?
- [ ] *Kill-switch* exercitado conforme cadência exigida (A3 trimestral, A4 mensal)?
- [ ] Provider de modelo manteve a versão pinned?
- [ ] *Tools_allowlist* continua proporcional ao trabalho real?

Resultado: renovação (com ou sem alterações), descida de nível, ou revogação.

### 5.7 Revogação

Revogação é executada **imediatamente** pelo *kill-switch* nas situações:

- *Off-policy action* com efeito material
- *Prompt injection* bem-sucedida resultando em tool call não autorizada
- *Credential exposure* da identidade do agente
- Falha de *kill-switch* (mesmo sem incidente material — quebra de confiança operacional)
- Alteração silenciosa do provider/modelo (e.g. *AI supply chain "rug pull"*, `AML.T0109`)

Revogação não é sinónimo de extinção definitiva — pode haver re-emissão após análise *post-mortem* e *mandate* novo.

## 6. Revisão periódica obrigatória do registo organizacional

Independentemente das revisões por *mandate*, a organização revê **o conjunto** dos *mandates* activos com cadência:

| Nível de risco | Cadência da revisão organizacional |
|---|---|
| L1 | Anual |
| L2 | Semestral |
| L3 | Trimestral |

A revisão organizacional cobre: *mandates* sem *owner* activo (ex: pessoa saiu da empresa), *mandates* com `effective_until` ultrapassado, agentes operacionais sem *mandate* correspondente, e *mandates* em níveis que não justificam (sub-uso ou *overprivilege*).

## 7. Responsabilidades

| Role | Responsabilidade |
|---|---|
| **Owner do agente** | Submeter proposta de mandate; operar dentro do scope; reportar incidentes; participar em revisões; exercitar o kill-switch conforme cadência |
| **AppSec Engineer** | Avaliar adequação técnica e least privilege; rever intent events; aprovar A2+; auditar mandates activos |
| **Tech Lead** | Aprovar A1/A2; garantir que a equipa segue esta política; nomear *owner* e *backup* |
| **DevOps / SRE** | Provisionar workload identity efémera, kill-switch operacional, sink de intent events; garantir tempo de efeito do kill-switch |
| **GRC / Compliance** | Avaliar conformidade regulatória; aprovar A3/A4; conduzir revisão organizacional periódica |
| **CISO** | Assinar mandates A4; aprovar política e revisões; arbitrar conflitos de escopo |
| **Auditores** | Auditar registo de mandates + intent events vs acções reais; flag de divergências |

## 8. Proporcionalidade por nível de criticidade

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Mandate registado para A1+ | Obrigatório | Obrigatório | Obrigatório |
| A2 permitido em produção | Não | Sim (com guardrails) | Sim (com guardrails reforçados) |
| A3 permitido em produção | Não | Sim (com revert demonstrado) | Sim (apenas com auditoria mensal informal) |
| A4 permitido | Não | Não (excepto excepção formal aprovada pelo `CISO`) | Sim (com mandate assinado) |
| Revisão organizacional do registo de mandates | Anual | Semestral | Trimestral |
| Mandate assinado pelo `CISO` | Apenas A4 (raro) | Apenas A4 | A4 sempre; A3 recomendado |

## 9. Gestão de exceções

Excepções a esta política seguem o processo formal definido no Cap. 14 e na [`Policy 05 — Gestão de Excepções`](./policy-gestao-excecoes):

- Excepção tem TTL explícito (recomendado ≤ 90 dias).
- Excepção em A3/A4 exige aprovação adicional do `CISO`.
- Excepções acumuladas (>2 sobre o mesmo agente em 12 meses) obrigam a revisão do *mandate*.

## 10. Revisão e auditoria desta política

Esta política deve ser **revista semestralmente** dada a rápida evolução das capacidades de agentes AI, ou após qualquer um dos seguintes eventos:

- Incidente envolvendo *off-policy action*, *intent-action divergence* ou *prompt injection* bem-sucedida em agente A1+
- Alteração regulatória aplicável (AI Act, NIS2, DORA, RGPD) com impacto em autonomia de agentes
- Mudança significativa nas capacidades dos *runtimes* AI suportados (e.g. nova classe de tool-use)
- Revisão da [Policy 16 — Uso de Ferramentas de Apoio ao Desenvolvimento](./policy-uso-ferramentas-apoio) com impacto no perímetro

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 02 (addon `09-governaca-automatismos`) | Modelo A0–A4 e requisitos `REQ-AGN-001..004` |
| SbD-ToE Cap. 03 (playbook agentic) | Threat library para agentes com tool-use |
| SbD-ToE Cap. 04 (`ARC-015`) | Padrões arquitectónicos: agente como *principal* isolado |
| SbD-ToE Cap. 14 — Governança e Contratação | Excepções, contratação, auditoria |
| [Policy 16 — Uso de Ferramentas de Apoio ao Desenvolvimento](./policy-uso-ferramentas-apoio) | Regras operacionais A2+ |
| [Policy 05 — Gestão de Excepções](./policy-gestao-excecoes) | Processo formal de excepções |
| [Policy 18 — Gestão de Segredos](./policy-gestao-segredos) | Identidade efémera (OIDC) — padrão herdado |
| MITRE ATLAS | Catálogo de tactics/techniques adversariais (Threats `AML.T*` referenciadas em Cap. 03 playbook agentic) |
| OWASP Top 10 for LLM Applications (2025) | LLM06-2025 Excessive Agency, LLM01-2025 Prompt Injection |
| NIST AI RMF 1.0 (2023) + Generative AI Profile (2024) | GOVERN-1.x (políticas e ownership); MANAGE-4.x (revisão e revogação) |
| NIST SP 800-207 | Zero Trust — agente como *principal* não-humano |
| NIST SP 800-218A | SSDF Profile for GenAI |
| ISO/IEC 42001:2023 | AI Management System — ciclo de vida, ownership, revisão |
| EU AI Act (Reg. (UE) 2024/1689) | Art. 14 (Human oversight); Art. 26 (Obrigações de *deployers*) — ver [cross-check AI Act](/sbd-toe/cross-check-normativo/ai-act/intro) |
