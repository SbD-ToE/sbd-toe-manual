---
id: agentic-sdlc
title: Agentic SDLC via MCP
description: Como usar o MCP server SbD-ToE para suportar o processo de desenvolvimento agentic ponta-a-ponta — o agente consulta o manual via MCP em cada paragem do fluxo, do mandate ao kill-switch.
sidebar_label: Agentic SDLC via MCP
sidebar_position: 7
tags:
  - mcp
  - casos-uso
  - agentic
  - sdlc
  - mandate
  - eval-suite
---

# Caso de uso — Agentic SDLC via MCP

Há uma simetria útil neste caso de uso: o MCP serve para que **o próprio agente que opera o processo agentic** consulte o manual antes de cada decisão. O agente que classifica o nível A0–A4 de outro agente; o agente que produz o *threat model* de outro agente; o agente que regista o *mandate*; o agente que gera a *eval suite*. Em cada paragem do [processo agentic transversal](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-agentic-sdlc), o MCP serve como fonte canónica do que o manual diz — para que a decisão fique *grounded*, não improvisada.

O exemplo de cross-check (`exemplo-playbook/exemplo-agentic-sdlc`) descreve **o que** acontece em cada paragem do processo; este caso de uso descreve **como** o MCP é invocado em cada uma. Os dois são deliberadamente acoplados mas separados — a vista regulatória vive no cross-check, a vista operacional via MCP vive aqui.

## Pré-requisitos

- MCP instalado (ver [Instalação](../03-instalacao.md))
- Skill canónica em `.claude/skills/sbd-toe.md` (ver [Skills](../04-skills-agentes.md))
- Familiaridade com o [processo agentic transversal](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-agentic-sdlc) — esta receita assume que estás a percorrê-lo

## Mapa MCP por paragem do processo

A tabela mostra, para cada paragem do fluxo agentic, qual *tool* / *resource* / *prompt* do MCP usar e o resultado esperado.

| Paragem | Tool MCP | Output esperado |
|---|---|---|
| **1. Classificar nível A0–A4** | `setup_sbd_toe_agent(riskLevel, projectRole)` + `consult_security_requirements(risk_level, ["requirements"])` | Lista activa de requisitos `REQ-AGN-*`; capítulos activos para o nível |
| **2. Threat model agentic** | `get_threat_landscape(risk_level, concerns=["auth","api","integrity","distribution"])` + `search_sbd_toe_manual("playbook agentic threat library")` | Threat library MITRE ATLAS aplicável + mitigações citáveis (Cap. 03) |
| **3. Validar arquitectura ARC-015** | `query_sbd_toe_entities(query="ARC-015")` + `consult_security_requirements(risk_level, ["architecture"])` | Critério de aceitação completo de `ARC-015` + controlos arquitectónicos `ARC-001..014` complementares |
| **4. Registar mandate** | `plan_sbd_toe_repo_governance()` filtrando por capítulos 02+14 + `get_sbd_toe_chapter_brief("02-requisitos-seguranca")` (para `artifact_ids` reais) | Artefactos que o manual exige; template de mandate ancorado em Policy 38 |
| **5. Pipeline com agente principal** | `map_sbd_toe_review_scope(changed_files=["pipeline/agent-runner.yaml"])` + `consult_security_requirements(risk_level, ["auth","logging","distribution"])` | Controlos de CI/CD aplicáveis (cap. 07); gates de CI; padrão US-04 (segredos) herdado |
| **6. Prompts/skills como código** | `search_sbd_toe_manual("prompts como código revisão skill files")` + `consult_security_requirements(risk_level, ["validation","integrity"])` | Controlos de revisão de código aplicáveis; anti-padrões documentados |
| **7. AI BOM + supply chain** | `search_sbd_toe_manual("AI BOM CycloneDX ml-bom providers")` + `query_sbd_toe_entities(query="DEP-012")` + `query_sbd_toe_entities(query="DEP-014")` | Formato CycloneDX 1.6 + lista de providers aprovados; ciclo de aprovação |
| **8. Eval suite** | `get_guide_by_role(risk_level, role="appsec-engineer", phase="test")` + `search_sbd_toe_manual("C5 eval suites continuous")` | Práticas de teste aplicáveis; composição mínima da suite por nível |
| **9. Release gates** | `consult_security_requirements(risk_level, ["distribution"])` + `get_guide_by_role(risk_level, role="devops-sre", phase="deploy")` | Critérios de release para A2+; *gates* de eval + rollback de modelo |
| **10. Telemetria** | `query_sbd_toe_entities(query="OPS-011")` + `consult_security_requirements(risk_level, ["logging"])` | `OPS-011..014` com critério de aceitação; integração SIEM |
| **11. Revisão de mandate** | `get_guide_by_role(risk_level, role="appsec-engineer")` + `inspect_sbd_toe_retrieval("revisão periódica mandate")` | Cadência por nível; itens de checklist da revisão |

> 📌 Quando uma paragem se dirige a tema fora do **canon 00-14** do MCP (e.g. cláusulas contratuais detalhadas com providers AI — fica fora porque o conteúdo legal-específico vive no manual web, em Cap. 14 US-21 e Policy 33), o agente deve usar `WebFetch` para o manual web em vez de inventar — ver [Caso de uso: Cross-check normativo](./06-cross-check-conformidade.md) e [troubleshooting / content lag](../10-troubleshooting-faq.md#content-lag).

## Disciplina de output

Em cada paragem do processo, o agente que executa via MCP deve:

1. **Citar o ID exacto** retornado pela tool (`REQ-AGN-001`, `ARC-015`, `DEP-012`, `OPS-014`) — nunca improvisar.
2. **Marcar rótulo epistémico** (ver [Epistemica & anti-patterns](../09-epistemica-anti-patterns.md)):
   - `manual-grounded` — recuperado via MCP, com `Document path` arquivado
   - `observed` — verificado directamente no repositório / sistema (e.g. `tools_allowlist` no IaC)
   - `inferred` — combinação de `manual-grounded` + `observed`
   - `not verified` — em dúvida, preferir isto a apresentar como facto
3. **Preservar `mandate_ref`** em qualquer artefacto que gere — pipeline manifests, *audit events*, eval reports — para que a auditoria reconstrua "que agente, sob que mandate, com que autoridade".
4. **Distinguir três classes de artefacto** (cross-link [Casos de uso — Codegen grounded §disciplina](./codegen-grounded)): código, testes, evidência. *Tests* são evidência; código não é.

## Sequência típica numa sessão

Para uma decisão concreta — por exemplo, "este agente pode subir de A2 para A3?" — a sequência MCP é:

1. `setup_sbd_toe_agent("L2", "appsec")` — carrega capítulos activos + regras de role
2. Ler `sbd://toe/agent-guide` (uma vez por sessão)
3. `consult_security_requirements("L2", ["requirements"])` — confirma se `REQ-AGN-002` está activo (sim, em L1+)
4. `search_sbd_toe_manual("A0 A4 níveis de autonomia subir nível critérios")` — extrai a regra de promoção
5. `get_guide_by_role("L2", "appsec", "operate")` — práticas de revisão aplicáveis
6. Combinar com o que está em VCS: ler o *mandate* actual; verificar se *kill-switch* foi exercitado conforme cadência; verificar se *eval suite* confirma o nível pretendido
7. Decidir — `manual-grounded` (regra do manual) + `observed` (estado real do repo) → recomendação final ao humano

O passo 7 é onde o agente devolve a resposta ao humano que pediu — citando IDs reais (`REQ-AGN-002`, regra X), referindo o que verificou (`observed`: kill-switch exercitado 2026-04-15), e indicando se a subida pode avançar (`inferred`: condições satisfeitas) ou se há bloqueio (`not verified`: falta evidência de Y).

## Skill / subagent — Claude Code

`.claude/agents/sbd-toe-agentic-sdlc.md`:

```markdown
---
name: sbd-toe-agentic-sdlc
description: Suporta o processo agentic SDLC ponta-a-ponta consultando o MCP em cada paragem. Não inventa decisões; recolhe evidência grounded e propõe ao humano.
tools: Read, Glob, Grep, mcp__sbd-toe__*
---

# Workflow

1. Ler sbd://toe/agent-guide (1x por sessão).
2. Identificar a paragem do processo agentic em causa (usar o exemplo
   cross-check /sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-agentic-sdlc
   como referência).
3. Para essa paragem, invocar a(s) tool(s) MCP indicada(s) na tabela
   "Mapa MCP por paragem".
4. Combinar com leitura do repositório (mandates em VCS, eval reports,
   audit logs) — distinguir manual-grounded vs observed.
5. Devolver ao humano:
   - IDs do manual citados (manual-grounded)
   - Estado observado (observed)
   - Inferência sustentada (inferred)
   - Itens em falta (not verified)
   - Recomendação final, sem omitir as dúvidas

# Hard rules

- citation_map (quando `prepare_sbd_toe_codegen_context` é usado) é
  mundo fechado de IDs válidos — não inventar.
- Em dúvida, marcar `not verified` em vez de assumir.
- Em decisões A3/A4, propor mas nunca decidir; escalação ao CISO via
  Policy 38 §5.3 é obrigatória.
- mandate_ref preservado em qualquer artefacto produzido.
```

## Anti-patterns

- ❌ **"O Claude consultou o MCP e disse que sim"** sem citar IDs concretos — desperdiça a vantagem do MCP, que é grounding citável.
- ❌ **Não distinguir `manual-grounded` de `observed`** — o manual diz X, o repo está em estado Y; estes são dois factos diferentes e a sua conjugação é uma inferência.
- ❌ **Saltar paragens "porque já está coberto"** — cada paragem tem critério de aceitação próprio; "implícito" não conta como evidência.
- ❌ **Promover de nível A com base em interacções soltas no chat sem audit `mandate_ref`** — viola Policy 38 §5.5 (sem *amendments* informais).
- ❌ **Tratar o MCP como oráculo** — o MCP devolve o que o manual diz; a interpretação para o caso concreto continua ser de quem opera (humano + agente como assistente).

## Relacionado

- **Vista regulatória do mesmo processo**: [Cross-check — Agentic SDLC ponta-a-ponta](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-agentic-sdlc) — descreve **o quê** e mapeia para AI Act/NIS2/DORA/CRA
- [Caso de uso — Codegen grounded](./codegen-grounded) — disciplina de `citation_map` aplicada a *codegen*
- [Caso de uso — Threat modeling](./threat-modeling) — paragem 2 detalhada
- [Caso de uso — Bootstrap de governança](./governance-bootstrap) — paragem 4 detalhada (mandate scaffolding)
- [Caso de uso — Auditoria de PR](./auditoria-pr) — caso operacional realista de agente A2
- [Epistemica & anti-patterns](../09-epistemica-anti-patterns.md) — rótulos `manual-grounded` / `observed` / `inferred` / `not verified`
