---
id: cross-check-conformidade
title: Cross-check normativo
description: Cruzar SbD-ToE com AI Act, CRA, DORA, NIS2, GDPR — com o MCP (canon e cross-checks indexados) e o manual web para conteúdo posterior ao snapshot.
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

Esta receita serve para a segunda. Combina o MCP (onde estão indexados os cross-checks normativos publicados) com a leitura directa do manual web (necessária para conteúdo posterior ao *snapshot* publicado). O resultado é um relatório técnico que cita o regulamento *verbatim*, os capítulos e controlos do SbD-ToE com IDs reais, e marca explicitamente o que não está coberto — sem nunca derrapar para uma declaração de conformidade.

## Cobertura actual no MCP — o que está dentro e fora {#cobertura-actual-no-mcp--o-que-está-dentro-e-fora}

O *snapshot* servido inclui canon (capítulos 00–14), ontologia *AppSec Core v1* **e** os cross-checks publicados — **CRA**, **DORA**, **NIS2**, **GDPR**, **AI Act** e **ENISA/CSA** — indexados no KG; a versão exata está em `sbd://toe/version`. Para esses, o MCP é a fonte recomendada: `get_sbd_toe_playbook` devolve os playbooks publicados por diploma, com a autoridade declarada; `map_sbd_toe_regulatory_activation` / `resolve_entities` expõem o overlay regulatório (frameworks, obrigações, mapeamentos); e `search_sbd_toe_manual` devolve os intros, playbooks e notas de convergência com citações.

A fronteira é o *snapshot*: conteúdo adicionado ao manual web **depois** dele vive só no manual web até nova publicação. A versão servida está em `sbd://toe/version` (ver [content lag](../10-troubleshooting-faq.md#content-lag)).

| Pergunta | Fonte recomendada |
|---|---|
| "Que controlos `CTRL-*` se aplicam a `auth` em L2?" | **MCP** (`consult_security_requirements`) |
| "Que threats existem para `encryption` em L3?" | **MCP** (`get_threat_landscape`) |
| "Que playbook publica o manual para o NIS2?" | **MCP** (`get_sbd_toe_playbook`) — playbook por diploma, autoridade declarada |
| "Há cross-check publicado para ISO, PCI ou SOC2?" | **MCP** (`get_sbd_toe_playbook`) — para ISO, PCI, SOC2, … a resposta declara `no_cross_check` |
| "Como o SbD-ToE responde ao CRA Art. 12?" | **MCP** (`search_sbd_toe_manual`) — cross-check **CRA** indexado |
| "Como o SbD-ToE mapeia o NIS2 Art. 21?" | **MCP** (`search_sbd_toe_manual`) — cross-check **NIS2** indexado |
| "Que obrigações DORA / GDPR aplicam ao meu projecto?" | **MCP** — cross-checks **DORA** e **GDPR** indexados |
| "Como o SbD-ToE responde ao Art. 15 do AI Act?" | **MCP** (`search_sbd_toe_manual`) — cross-check **AI Act** indexado; o [cross-check web](/sbd-toe/cross-check-normativo/ai-act/intro) para leitura integral |

### Como confirmar antes de responder {#como-confirmar-antes-de-responder}

Em caso de dúvida sobre se um framework está no KG, correr:

```json
inspect_sbd_toe_retrieval({"question": "<framework>", "topK": 5})
```

Se os top-ranked records apontam a `002-cross-check-normativo/<framework>/...` → indexado. Caso contrário → consultar o manual web.

## Fluxo {#fluxo}

### 1. Identificar a obrigação regulatória {#1-identificar-a-obrigação-regulatória}

Da fonte primária (EUR-Lex / texto do regulamento), extrair:
- Artigo (ex.: AI Act Art. 15 — «Exatidão, solidez e cibersegurança»)
- Conceitos-chave (ex.: «exemplos antagónicos ou evasão de modelos», «contaminação de dados» — art. 15.º, n.º 5)

### 2. Localizar a resposta {#2-localizar-a-resposta}

Duas vias consoante o framework:

**Via MCP — caminho principal** (CRA, DORA, NIS2, GDPR, AI Act, ENISA/CSA — indexados):

1. `get_sbd_toe_playbook` — o playbook publicado para o diploma, com a autoridade declarada. Para referenciais sem cross-check publicado (ISO, PCI, SOC2, …), a resposta declara `no_cross_check`: é o sinal para não improvisar uma correspondência.
2. `map_sbd_toe_regulatory_activation(framework)` — que capítulos do manual o *framework* ativa.
3. `search_sbd_toe_manual` para os excertos do cross-check sobre um artigo concreto:

```json
search_sbd_toe_manual({"question": "Art. 12 CRA presumição de conformidade", "topK": 8})
```

Devolve os excertos relevantes do cross-check com `chapter_id`, `Document path`, `Localização` (linhas) e link para o manual web.

**Manual web** (sempre disponível; para leitura integral e para conteúdo posterior ao *snapshot*):

- [AI Act](/sbd-toe/cross-check-normativo/ai-act/intro) · [Playbook](/sbd-toe/cross-check-normativo/ai-act/playbook) · [Convergência CRA](/sbd-toe/cross-check-normativo/ai-act/convergencia-cra)
- [CRA](/sbd-toe/cross-check-normativo/cra/intro) · [Playbook](/sbd-toe/cross-check-normativo/cra/playbook)
- [DORA](/sbd-toe/cross-check-normativo/dora/intro) · [Playbook](/sbd-toe/cross-check-normativo/dora/playbook) · [Convergência](/sbd-toe/cross-check-normativo/dora/convergencia-dora)
- [NIS2](/sbd-toe/cross-check-normativo/nis2/intro) · [Playbook](/sbd-toe/cross-check-normativo/nis2/playbook)
- [GDPR](/sbd-toe/cross-check-normativo/gdpr/intro)
- [ENISA & CSA](/sbd-toe/cross-check-normativo/enisa-csa/intro)

### 3. Anchorar nos controlos do canon (via MCP) {#3-anchorar-nos-controlos-do-canon-via-mcp}

Para os controlos que o cross-check refere:

```json
query_sbd_toe_entities({"query": "ARC-001"})
```

→ resolve o id exacto (requisito/controlo) e extrai nome + domínio + capítulo. Para os controlos derivados, usar `consult_security_requirements(risk_level, concerns)`.

### 4. Estruturar o relatório {#4-estruturar-o-relatório}

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

### 5. **Não declarar conformidade** {#5-não-declarar-conformidade}

O cross-check **mostra como o manual responde** ao regulamento — **não** declara conformidade jurídica. Conformidade requer:

- **Evidência operacional** (logs, attestations, audit reports)
- **Decisão do *legal counsel*** ou DPO/CISO
- **Avaliação externa** quando a regulação assim o exige (ex.: AI Act, art. 43.º, nos casos em que o procedimento de avaliação da conformidade envolve um organismo notificado — anexo VII; os sistemas do anexo III, pontos 2 a 8, seguem o controlo interno do anexo VI — art. 43.º, n.º 2)

Marcar **sempre** o relatório como *"cross-check técnico — não declaração de conformidade"*.

## Disciplina de output {#disciplina-de-output}

- IDs `CTRL-*` apenas se devolvidos por `query_sbd_toe_entities` ou `consult_security_requirements`.
- Citações do regulamento **verbatim** com referência precisa (artigo, número, alínea).
- Diferenciar:
  - **manual-grounded** (do canon SbD-ToE ou de cross-check indexado, via MCP — citar `Document path` e `chapter_id` exactos)
  - **cross-check-web-grounded** (do manual web — usar quando o conteúdo **não está** no MCP, por ser posterior ao *snapshot*)
  - **inferred** (deduzido — marcar)
  - **not verified** (não confirmado — não usar como facto)

## Skill / subagent — Claude Code {#skill--subagent--claude-code}

`.claude/agents/sbd-toe-compliance.md`:

```markdown
---
name: sbd-toe-compliance
description: Cross-check SbD-ToE × regulamento UE. Usa MCP para os frameworks indexados (CRA, DORA, NIS2, GDPR, AI Act, ENISA-CSA); usa manual web para conteúdo posterior ao snapshot. NUNCA declara conformidade.
tools: WebFetch, Read, mcp__sbd-toe__*
---

# Workflow

1. Identificar regulamento + artigo alvo. Validar contra EUR-Lex se possível.
2. Validar indexação no MCP com inspect_sbd_toe_retrieval(question="<framework>", topK=5).
3. Se indexado: get_sbd_toe_playbook para o playbook do diploma (no_cross_check → não improvisar), map_sbd_toe_regulatory_activation para os capítulos ativados, search_sbd_toe_manual para excertos do cross-check.
4. Se NÃO indexado (conteúdo posterior ao snapshot): WebFetch a /sbd-toe/cross-check-normativo/<framework>/.
5. Para cada CTRL-* / capítulo referido, validar via MCP (query_sbd_toe_entities).
6. Estruturar relatório com 4 rótulos: manual-grounded, cross-check-web-grounded, inferred, not verified.
7. Marcar como "cross-check técnico — não declaração de conformidade".
8. Em dúvida: preferir "not verified" a inventar uma ligação.
```

## Anti-patterns {#anti-patterns}

- ❌ Inventar ligações SbD-ToE ↔ regulamento que não estejam no cross-check publicado.
- ❌ Declarar "compliant with X" — o cross-check **demonstra cobertura técnica**, não conformidade jurídica.
- ❌ Confiar **apenas** no MCP para conteúdo posterior ao *snapshot* — confirmar em `sbd://toe/version`; consultar o manual web para o que ainda não foi publicado.
- ❌ Esquecer-se de procurar via MCP os cross-checks que **estão** indexados (CRA, DORA, NIS2, GDPR, AI Act, ENISA/CSA) — duplica trabalho desnecessariamente.
- ❌ Esquecer convergências (AI Act ↔ CRA, NIS2 ↔ DORA) — duplicação de trabalho e *gaps* invisíveis.

## Relacionado {#relacionado}

- [Casos de uso — Bootstrap de governança](./governance-bootstrap) — para criar o repo já com placeholders dos artefactos regulatórios.
- [Troubleshooting / FAQ](../10-troubleshooting-faq.md#content-lag) — sobre o *content lag* do MCP.
