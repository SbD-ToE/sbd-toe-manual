---
id: troubleshooting-faq
title: Troubleshooting & FAQ
description: Sintomas, causas e soluções para problemas comuns com o SbD-ToE MCP — content lag, versões, debug, integração com clientes AI.
sidebar_label: Troubleshooting / FAQ
sidebar_position: 10
tags:
  - mcp
  - troubleshooting
  - faq
---

# Troubleshooting & FAQ

A maior parte das dúvidas que aparecem nas primeiras semanas de uso do MCP não são *bugs* — são desalinhamentos previsíveis: uma chamada que devolve mais (ou menos) do que esperavas, um cliente que não reconhece o servidor, ou conteúdo que existe no manual web mas não aparece na pesquisa do MCP. Esta página reúne esses casos, com sintoma, causa e solução directa.

## Estado do servidor

### Como saber a versão actual

Ler o resource:

```
sbd://toe/version
```

Devolve `{name, version, description}`. A versão é incrementada a cada *publish* no npm.

Verificação local:

```bash
npx -y @shiftleftpt/sbd-toe-mcp --version 2>/dev/null
# ou — em alternativa:
npm view @shiftleftpt/sbd-toe-mcp version
```

### Como saber se o servidor está a correr no cliente

| Cliente | Verificação |
|---|---|
| Claude Code | `claude mcp list` |
| Claude Desktop | Painel de ferramentas mostra `sbd-toe.*` na conversa |
| Cursor | Settings → Features → MCP, *badge* verde em `sbd-toe` |
| VS Code (Copilot) | Em *Agent mode*, `@workspace` mostra MCP ligados |
| Windsurf | Painel MCP, status `running` |

---

## Content lag {#content-lag}

### Sintoma

`search_sbd_toe_manual` não devolve conteúdo do **AI Act**, embora a página exista no manual web (`/sbd-toe/cross-check-normativo/ai-act/...`).

### Causa

O *snapshot* do manual que o servidor (**`@shiftleftpt/sbd-toe-mcp@0.10.0`**) serve já inclui o cross-check do AI Act (manual `v1.6.4`, posterior à v1.3.0 onde foi adicionado). No entanto, o **índice KG** construído a partir desse *snapshot* **ainda não cobre** o bundle `ai-act/` — é uma lacuna de **indexação**, não de versão do manual. Por isso o AI Act não aparece em consultas MCP até nova indexação.

Os restantes cross-checks (**CRA**, **DORA**, **NIS2**, **GDPR**, **ENISA/CSA**) **estão indexados** e funcionam normalmente.

### Como confirmar o que está indexado

```
inspect_sbd_toe_retrieval({"question": "<nome do regulamento>", "topK": 5})
```

Se os top-ranked records apontam a `002-cross-check-normativo/<framework>/...` → indexado. Se apontam apenas a documentos do `010-sbd-manual/...` (sem hit em `002-cross-check-normativo/<framework>`) → fora do índice (caso actual do AI Act).

### Solução

Para perguntas sobre **AI Act**, consultar directamente o manual web:

- [Cross-check AI Act](/sbd-toe/cross-check-normativo/ai-act/intro)

Para CRA / DORA / NIS2 / GDPR / ENISA-CSA e canon 00–14, usar o MCP normalmente.

### Quando será resolvido

Quando o KG for re-indexado a incluir o bundle `ai-act/` e o servidor fizer nova publicação. Não há ETA público.

---

## Performance

### Sintoma — `consult_security_requirements(L3)` é lento ou estoura o contexto

Output de L3 sem `concerns` é ~36k chars — pode exceder o contexto do cliente.

### Solução

**Sempre passar `concerns`** em L2 / L3:

```json
consult_security_requirements({"risk_level": "L3", "concerns": ["auth", "encryption"]})
```

Reduz para ~9k chars por *concern set*. Iterar por *concern* se precisares de coverage completa.

---

## Resultados inesperados

### Sintoma — `search_sbd_toe_manual` devolve resultados *off-topic*

### Causa(s) possíveis

1. *Vocabulary mismatch* — usaste `authentication` em vez de `auth` (vocabulário ontológico)
2. Pergunta narrativa demasiado vaga
3. Pergunta estruturada que devia ir a `consult_security_requirements`

### Diagnóstico

```json
inspect_sbd_toe_retrieval({"query": "<query original>"})
```

Devolve ranking, *scores*, *rule_trace*. Identifica se é *vocabulary* ou *intent*.

### Solução

- Para *vocabulary*: usar termos canónicos (ver [concerns](./01-intro.md#vocabul%C3%A1rio-controlado))
- Para *intent estruturado*: preferir `consult_security_requirements` ou `get_*`

---

### Sintoma — `get_guide_by_role(L2)` devolve só contagens

### Causa

Chamaste sem `role` nem `phase`. Por design, sem nenhum dos dois, devolve apenas `role_summary{}` + `phase_summary{}`.

### Solução

```json
get_guide_by_role({"risk_level": "L2", "role": "developer"})
// ou
get_guide_by_role({"risk_level": "L2", "phase": "implement"})
```

---

### Sintoma — `get_threat_landscape` devolve `threats: []`

### Causa(s)

1. *Risk level* / *concerns* combinação demasiado restrita
2. O escopo é genuinamente sem threats catalogados no canon
3. Os *concerns* não estão no vocabulário (typo)

### Solução

1. Alargar — remover *concerns*, ou subir *risk level* se aplicável
2. Se persistir vazio: **não inventar threats** — escrever na resposta *"Manual-grounded: sem threats no canon para este escopo. Não confundir com ausência de risco — inspeção humana recomendada."*
3. Validar os *concerns* contra a [tabela canónica](./01-intro.md#vocabul%C3%A1rio-controlado)

---

## `prepare_sbd_toe_codegen_context`

### Sintoma — devolve `needs_decomposition` em ciclo

### Causa

A tarefa-mãe é demasiado conceptual / aberta. *Brute-force* (re-chamar com pequenos *tweaks*) não passa o gate.

### Solução

1. Aceitar uma das sub-tarefas sugeridas e re-chamar **apenas para essa**
2. Se a sub-tarefa também devolver `needs_decomposition` → **STOP**, escalar com o utilizador
3. Recomeçar a sessão com uma decomposição manual antes da primeira chamada

Ver [Padrão 5 — Iteração de codegen com falhas](./08-padroes-avancados.md#padrao-5).

---

### Sintoma — `unsupported_scope`

### Significado

O servidor instalado não tem a capacidade que pediste. Possíveis sub-causas:

| Causa | Acção |
|---|---|
| `AppSec Core v1 runtime ausente` | Deploy incompleto — re-correr `npm run checkout:backend` ou *pin* outra KG snapshot. |
| `Overlay regulatório ausente` | Remover `regulatory_frameworks` / `include_regulatory_overlay`, ou esperar publicação. |
| `Framework regulatório desconhecida` | Listar os *short codes* suportados em `regulatory_overlay.frameworks`. |

**Não fabricar** IDs para "continuar" — o gate é por design.

---

## Instalação / cliente

### Sintoma — `claude mcp add` falha com `Cannot find package`

### Causa

Node.js `< 20.9.0` ou npm sem acesso ao registo público.

### Solução

```bash
node --version          # confirmar ≥ 20.9.0
npm config get registry # confirmar https://registry.npmjs.org/
```

---

### Sintoma — Cursor / Claude Desktop não reconhece o servidor

### Causa(s)

1. Ficheiro de configuração em caminho errado
2. JSON inválido (trailing comma, aspas erradas)
3. Cliente não reiniciado após edição

### Solução

1. Confirmar caminho (ver [Instalação](./03-instalacao.md))
2. Validar JSON: `jq . < /path/to/config.json` — erros aparecem
3. **Reiniciar o cliente** após cada alteração da configuração MCP

---

### Sintoma — Tools `sbd-toe.*` aparecem mas todas as chamadas falham

### Diagnóstico

Executar o comando manualmente para isolar:

```bash
npx -y @shiftleftpt/sbd-toe-mcp
```

Deve mostrar logs *stderr* a indicar "MCP server listening on stdio" (ou equivalente). Se não — problema do servidor / Node / dependências.

---

## Operacional

### Sintoma — output do MCP é em PT, mas o utilizador escreve EN

### Não é bug — é arquitectura

O conteúdo canónico do manual está em PT. O *agent guide* diz explicitamente:

> *Always respond in the user's language. The manual content is in Portuguese — translate, summarise, and explain in whatever language the user writes in.*

**Solução:** o LLM deve **traduzir / sumarizar** o conteúdo PT para a língua do utilizador. Não passar a falar PT só porque o manual o está.

---

### Sintoma — utilizador discorda do *risk level*

### Acção

Não decidir unilateralmente. Apresentar:

1. O que `map_sbd_toe_applicability` sugere
2. O que mudaria se `risk_level` fosse X vs Y (custo: capítulos adicionais)
3. Quem assina a decisão (`CISO`, `executive_management`, `appsec`)

Marcar como `inferred` enquanto não há decisão.

---

## *Upgrades* e versionamento

### Quando re-correr `generate_sbd_toe_skill`

Após cada *upgrade* do servidor MCP (releases minor/patch no npm). O conteúdo do *agent guide* pode mudar; a skill em disco está desactualizada até regenerar.

### Como saber se a skill está desactualizada

A skill em disco começa com:

```
<!-- SbD-ToE skill content — source: sbd://toe/agent-guide (@shiftleftpt/sbd-toe-mcp) -->
```

Não inclui versão explícita — comparar `sbd://toe/version` com a versão usada na última geração (manter como entrada de *changelog* do projecto).

---

## Quando reportar bug

Reportar em [github.com/Shiftleftpt/sbd-toe-mcp-poc/issues](https://github.com/Shiftleftpt/sbd-toe-mcp-poc/issues) se:

- `inspect_sbd_toe_retrieval` mostra *rule_trace* incoerente
- Output contradiz directamente o que o manual web diz para um capítulo canon
- Tool retorna *schema* diferente do documentado
- Tools listadas como disponíveis falham 100% das chamadas

Incluir no report:
- Versão do MCP (`sbd://toe/version`)
- Cliente e versão
- Input exacto da chamada
- Output recebido
- Output esperado

## A seguir

- [Versionamento e roadmap](./11-versionamento-roadmap.md) — release notes + futuro.
