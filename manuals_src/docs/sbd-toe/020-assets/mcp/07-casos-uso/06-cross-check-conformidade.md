---
id: cross-check-conformidade
title: Cross-check normativo
description: Cruzar SbD-ToE com AI Act, CRA, DORA, NIS2, GDPR — combinando o MCP (canon 00–14) com o manual web (cross-checks).
sidebar_label: Cross-check normativo
sidebar_position: 6
tags:
  - mcp
  - casos-uso
  - compliance
  - ai-act
  - cra
  - dora
  - nis2
  - gdpr
---

# Caso de uso — Cross-check normativo

Mais cedo ou mais tarde, alguém na empresa — *legal*, auditoria interna, um cliente B2B no contrato — vai querer ver, em papel, como é que as práticas de engenharia respondem a um regulamento específico. AI Act, CRA, DORA, NIS2, RGPD. A pergunta não é "estamos compliant?" (essa é jurídica) — é "como é que o SbD-ToE responde a este artigo?" (essa é técnica).

Esta receita serve para a segunda. Combina o MCP (onde estão indexados a maior parte dos cross-checks normativos do manual) com a leitura directa do manual web (necessária para o **AI Act**, ainda fora do *snapshot* `0.9.0`). O resultado é um relatório técnico que cita o regulamento *verbatim*, os capítulos e controlos do SbD-ToE com IDs reais, e marca explicitamente o que não está coberto — sem nunca derrapar para uma declaração de conformidade.

## Cobertura actual no MCP — o que está dentro e fora

O *snapshot* publicado em **`@shiftleftpt/sbd-toe-mcp@0.9.0`** já inclui canon (capítulos 00–14), ontologia *AppSec Core v1* **e** os cross-checks **CRA**, **DORA**, **NIS2**, **GDPR** e **ENISA/CSA** indexados no KG. Para esses, podes (e deves) usar o MCP — `search_sbd_toe_manual` devolve os intros, playbooks e notas de convergência directamente.

A **excepção** é o cross-check do **AI Act** (Reg. (UE) 2024/1689), adicionado ao manual web na release **v1.3.0** posterior à publicação do servidor. Para perguntas sobre AI Act, consultar **directamente o manual web** até nova publicação do MCP (ver [content lag](../10-troubleshooting-faq.md#content-lag)).

| Pergunta | Fonte recomendada |
|---|---|
| "Que controlos `CTRL-*` se aplicam a `auth` em L2?" | **MCP** (`consult_security_requirements`) |
| "Que threats existem para `encryption` em L3?" | **MCP** (`get_threat_landscape`) |
| "Como o SbD-ToE responde ao CRA Art. 12?" | **MCP** (`search_sbd_toe_manual`) — cross-check **CRA** indexado |
| "Como o SbD-ToE mapeia o NIS2 Art. 21?" | **MCP** (`search_sbd_toe_manual`) — cross-check **NIS2** indexado |
| "Que obrigações DORA / GDPR aplicam ao meu projecto?" | **MCP** — cross-checks **DORA** e **GDPR** indexados |
| "Como o SbD-ToE responde ao Art. 15 do AI Act?" | **Manual web** ([cross-check AI Act](/sbd-toe/cross-check-normativo/ai-act/intro)) — **ainda fora do MCP `0.9.0`** |

### Como confirmar antes de responder

Em caso de dúvida sobre se um framework está no KG, correr:

```json
inspect_sbd_toe_retrieval({"question": "<framework>", "topK": 5})
```

Se os top-ranked records apontam a `002-cross-check-normativo/<framework>/...` → indexado. Caso contrário → consultar o manual web.

## Fluxo

### 1. Identificar a obrigação regulatória

Da fonte primária (EUR-Lex / texto do regulamento), extrair:
- Artigo (ex.: AI Act Art. 15 — *accuracy, robustness and cybersecurity*)
- Conceitos-chave (ex.: *adversarial examples*, *model evasion*, *data poisoning*)

### 2. Localizar a resposta

Duas vias consoante o framework:

**Via MCP** (CRA, DORA, NIS2, GDPR, ENISA/CSA — indexados):

```json
search_sbd_toe_manual({"question": "Art. 12 CRA presumição de conformidade", "topK": 8})
```

Devolve os excertos relevantes do cross-check com `chapter_id`, `Document path`, `Localização` (linhas) e link para o manual web.

**Manual web** (sempre disponível; **obrigatório** para AI Act):

- [AI Act](/sbd-toe/cross-check-normativo/ai-act/intro) · [Playbook](/sbd-toe/cross-check-normativo/ai-act/playbook) · [Convergência CRA](/sbd-toe/cross-check-normativo/ai-act/convergencia-cra) — **só aqui**
- [CRA](/sbd-toe/cross-check-normativo/cra/intro) · [Playbook](/sbd-toe/cross-check-normativo/cra/playbook)
- [DORA](/sbd-toe/cross-check-normativo/dora/intro) · [Playbook](/sbd-toe/cross-check-normativo/dora/playbook) · [Convergência](/sbd-toe/cross-check-normativo/dora/convergencia-dora)
- [NIS2](/sbd-toe/cross-check-normativo/nis2/intro) · [Playbook](/sbd-toe/cross-check-normativo/nis2/playbook)
- [GDPR](/sbd-toe/cross-check-normativo/gdpr/intro)
- [ENISA & CSA](/sbd-toe/cross-check-normativo/enisa-csa/intro)

### 3. Anchorar nos controlos do canon (via MCP)

Para os controlos que o cross-check refere:

```json
query_sbd_toe_entities({"query": "CTRL-04", "entity_type": "control"})
```

→ extrai descrição actualizada + domínio + capítulo.

### 4. Estruturar o relatório

```markdown
# Cross-check SbD-ToE × <Regulamento> Art. <N>

## Obrigação regulatória
- **Fonte:** <regulamento, artigo, número, alínea>
- **Texto:** <verbatim do regulamento>
- **Conceitos-chave:** <lista>

## Resposta SbD-ToE (manual-grounded)

### Cobertura por capítulo
- Cap. <N> "<título>" — <controlos relevantes CTRL-*>
- ...

### Controlos citáveis
| ID | Descrição | Capítulo |
|---|---|---|
| CTRL-... | ... | ... |

## Convergências
<se aplicável — ex.: CRA Art. 12 + AI Act Art. 15>

## Resíduo / gap
<o que o SbD-ToE não cobre directamente>
```

### 5. **Não declarar conformidade**

O cross-check **mostra como o manual responde** ao regulamento — **não** declara conformidade jurídica. Conformidade requer:

- **Evidência operacional** (logs, attestations, audit reports)
- **Decisão do *legal counsel*** ou DPO/CISO
- **Avaliação externa** quando a regulação assim o exige (ex.: AI Act high-risk Art. 43)

Marcar **sempre** o relatório como *"cross-check técnico — não declaração de conformidade"*.

## Disciplina de output

- IDs `CTRL-*` apenas se devolvidos por `query_sbd_toe_entities` ou `consult_security_requirements`.
- Citações do regulamento **verbatim** com referência precisa (artigo, número, alínea).
- Diferenciar:
  - **manual-grounded** (do canon SbD-ToE ou de cross-check indexado, via MCP — citar `Document path` e `chapter_id` exactos)
  - **cross-check-web-grounded** (do manual web — usar quando o cross-check **não está** no MCP, hoje o AI Act)
  - **inferred** (deduzido — marcar)
  - **not verified** (não confirmado — não usar como facto)

## Skill / subagent — Claude Code

`.claude/agents/sbd-toe-compliance.md`:

```markdown
---
name: sbd-toe-compliance
description: Cross-check SbD-ToE × regulamento UE. Usa MCP para frameworks indexados (CRA, DORA, NIS2, GDPR, ENISA-CSA); usa manual web para AI Act. NUNCA declara conformidade.
tools: WebFetch, Read, mcp__sbd-toe__*
---

# Workflow

1. Identificar regulamento + artigo alvo. Validar contra EUR-Lex se possível.
2. Validar indexação no MCP com inspect_sbd_toe_retrieval(question="<framework>", topK=5).
3. Se indexado: usar search_sbd_toe_manual para extrair excertos do cross-check.
4. Se NÃO indexado (AI Act actualmente): WebFetch a /sbd-toe/cross-check-normativo/<framework>/.
5. Para cada CTRL-* / capítulo referido, validar via MCP (query_sbd_toe_entities).
6. Estruturar relatório com 4 rótulos: manual-grounded, cross-check-web-grounded, inferred, not verified.
7. Marcar como "cross-check técnico — não declaração de conformidade".
8. Em dúvida: preferir "not verified" a inventar uma ligação.
```

## Anti-patterns

- ❌ Inventar ligações SbD-ToE ↔ regulamento que não estejam no cross-check publicado.
- ❌ Declarar "compliant with X" — o cross-check **demonstra cobertura técnica**, não conformidade jurídica.
- ❌ Confiar **apenas** no MCP para o **AI Act** — não está indexado em `0.9.0`; consultar o manual web.
- ❌ Esquecer-se de procurar via MCP os cross-checks que **estão** indexados (CRA, DORA, NIS2, GDPR, ENISA/CSA) — duplica trabalho desnecessariamente.
- ❌ Esquecer convergências (AI Act ↔ CRA, NIS2 ↔ DORA) — duplicação de trabalho e *gaps* invisíveis.

## Relacionado

- [Casos de uso — Bootstrap de governança](./governance-bootstrap) — para criar o repo já com placeholders dos artefactos regulatórios.
- [Troubleshooting / FAQ](../10-troubleshooting-faq.md#content-lag) — sobre o *content lag* do MCP.
