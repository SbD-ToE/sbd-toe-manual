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

## Estado do servidor {#estado-do-servidor}

### Como saber a versão actual {#como-saber-a-versão-actual}

Ler o resource:

```
sbd://toe/version
```

Devolve `name`, `version` e a *provenance* do que é servido — `manual`, `kg`, `ontology`, `serving_contract` e `surface_history`. A versão é incrementada a cada *publish* no npm.

Verificação local:

```bash
npm view @shiftleftpt/sbd-toe-mcp version
```

O pacote não tem uma *flag* `--version`: `npx -y @shiftleftpt/sbd-toe-mcp` arranca o servidor. Para a versão que o cliente está de facto a usar, a fonte é o resource `sbd://toe/version`.

### Como saber se o servidor está a correr no cliente {#como-saber-se-o-servidor-está-a-correr-no-cliente}

| Cliente | Verificação |
|---|---|
| Claude Code | `claude mcp list` |
| Claude Desktop | Painel de ferramentas mostra `sbd-toe.*` na conversa |
| Cursor | Settings → Features → MCP, *badge* verde em `sbd-toe` |
| VS Code (Copilot) | Em *Agent mode*, `@workspace` mostra MCP ligados |
| Windsurf | Painel MCP, status `running` |

---

## Content lag {#content-lag}

### Sintoma {#sintoma}

Uma página existe no manual web, mas o MCP não a devolve (`search_sbd_toe_manual`, `query_sbd_toe_entities` ou `inspect_sbd_toe_retrieval` sem *hits* nesse documento).

### Causa {#causa}

O servidor serve um *snapshot* do manual e o índice KG construído a partir dele; a versão do manual, do KG e da ontologia está em `sbd://toe/version`. Conteúdo adicionado ao manual web **depois** desse *snapshot* só entra no MCP na publicação seguinte.

### Como confirmar o que está indexado {#como-confirmar-o-que-está-indexado}

```
inspect_sbd_toe_retrieval({"question": "<nome do regulamento ou da página>", "topK": 5})
```

Se os *top-ranked records* apontam a `002-cross-check-normativo/<framework>/...` (ou ao documento esperado) → indexado. Se apontam apenas a outros documentos, a página pode estar fora do índice — confirmar a versão em `sbd://toe/version` antes de concluir; uma pergunta mais específica (artigo, título da secção) melhora o *ranking*.

### Solução {#solução}

Ler `sbd://toe/version`. Se o conteúdo procurado é posterior ao *snapshot* indicado, consultar o manual web (por exemplo, [cross-check normativo](/sbd-toe/cross-check-normativo/intro)) até nova publicação do MCP. Para tudo o que está no *snapshot*, usar o MCP normalmente.

### Quando ocorre {#quando-ocorre}

A cada publicação npm o *snapshot* avança. A diferença entre a tag do manual e a versão do servidor é esperada e está documentada em [versionamento & roadmap](./11-versionamento-roadmap.md#relação-com-versões-do-manual).

---

## Performance {#performance}

### Sintoma — `consult_security_requirements(L3)` é lento ou estoura o contexto {#sintoma--consult_security_requirementsl3-é-lento-ou-estoura-o-contexto}

O output de L3 sem `concerns` pode exceder o contexto do cliente. Cada resposta declara o seu tamanho em `size_estimate`, e o guia (`sbd://toe/agent-guide`) publica os tamanhos medidos na *build* servida.

### Solução {#solução-1}

**Sempre passar `concerns`** em L2 / L3:

```json
consult_security_requirements({"risk_level": "L3", "concerns": ["auth", "encryption"]})
```

A resposta fica muito mais pequena. Quando for precisa a cobertura completa, iterar por *concern*.

---

## Resultados inesperados {#resultados-inesperados}

### Sintoma — `search_sbd_toe_manual` devolve resultados *off-topic* {#sintoma--search_sbd_toe_manual-devolve-resultados-off-topic}

### Causa(s) possíveis {#causas-possíveis}

1. *Vocabulary mismatch* — usaste `authentication` em vez de `auth` (vocabulário ontológico)
2. Pergunta narrativa demasiado vaga
3. Pergunta estruturada que devia ir a `consult_security_requirements`

### Diagnóstico {#diagnóstico}

```json
inspect_sbd_toe_retrieval({"question": "<pergunta original>"})
```

Devolve ranking, *scores*, *rule_trace*. Identifica se é *vocabulary* ou *intent*.

### Solução {#solução-2}

- Para *vocabulary*: usar termos canónicos (ver [concerns](./01-intro.md#vocabul%C3%A1rio-controlado))
- Para *intent estruturado*: preferir `consult_security_requirements` ou `get_*`

---

### Sintoma — `get_guide_by_role(L2)` devolve só contagens {#sintoma--get_guide_by_rolel2-devolve-só-contagens}

### Causa {#causa-1}

Chamaste sem `role` nem `phase`. Por design, sem nenhum dos dois, devolve apenas `role_summary{}` + `phase_summary{}`.

### Solução {#solução-3}

```json
get_guide_by_role({"risk_level": "L2", "role": "developer"})
// ou
get_guide_by_role({"risk_level": "L2", "phase": "implement"})
```

---

### Sintoma — `get_threat_landscape` devolve `threats: []` {#sintoma--get_threat_landscape-devolve-threats-}

### Causa(s) {#causas}

1. *Risk level* / *concerns* combinação demasiado restrita
2. O escopo é genuinamente sem threats catalogados no canon
3. Os *concerns* não estão no vocabulário (typo)

### Solução {#solução-4}

1. Alargar — remover *concerns*, ou subir *risk level* se aplicável
2. Se persistir vazio: **não inventar threats** — escrever na resposta *"Manual-grounded: sem threats no canon para este escopo. Não confundir com ausência de risco — inspeção humana recomendada."*
3. Validar os *concerns* contra a [tabela canónica](./01-intro.md#vocabul%C3%A1rio-controlado)

---

## `prepare_sbd_toe_codegen_context` {#prepare_sbd_toe_codegen_context}

### Sintoma — devolve `needs_decomposition` em ciclo {#sintoma--devolve-needs_decomposition-em-ciclo}

### Causa {#causa-2}

Duas causas possíveis. A seleção declarada passa do que o nível de `detail` promete caber — e então a resposta traz em `requirement_ceiling.batches` os lotes executáveis cuja união é a seleção inteira (os lotes podem partilhar requisitos). Ou a tarefa-mãe é demasiado conceptual / aberta. Em ambos os casos, *brute-force* (re-chamar com pequenos *tweaks*) não passa o gate.

### Solução {#solução-5}

1. Se a resposta traz `requirement_ceiling.batches`: seguir os lotes, um de cada vez — não redesenhar a decomposição à mão. Caso contrário, aceitar uma das sub-tarefas sugeridas e re-chamar **apenas para essa**
2. Se a sub-tarefa também devolver `needs_decomposition` → **STOP**, escalar com o utilizador
3. Recomeçar a sessão com uma decomposição manual antes da primeira chamada

Ver [Padrão 5 — Iteração de codegen com falhas](./08-padroes-avancados.md#padrao-5).

---

### Sintoma — `unsupported_scope` {#sintoma--unsupported_scope}

### Significado {#significado}

O servidor instalado não tem a capacidade que pediste. Possíveis sub-causas:

| Causa | Acção |
|---|---|
| `AppSec Core v1 runtime ausente` | Instalação incompleta — reinstalar ou atualizar o pacote publicado e reportar ao operador. |
| `Overlay regulatório ausente` | Remover `regulatory_frameworks` / `include_regulatory_overlay`, ou esperar publicação. |
| `Framework regulatório desconhecida` | Listar os *short codes* suportados em `regulatory_overlay.frameworks`. |

**Não fabricar** IDs para "continuar" — o gate é por design.

---

### Sintoma — devolve `needs_input` {#sintoma--devolve-needs_input}

**Causa.** Nada foi declarado. Em modo declarativo (o *default*), o servidor não infere *concerns* nem outros campos a partir do `task`: o `task` é registado, não interpretado.

**Solução.** A resposta traz o vocabulário aceite, os candidatos a confirmar e, para declarações inertes, os `valid_values`. Confirmar os candidatos com o utilizador e voltar a chamar com a declaração completa — `risk_level`, `concerns`, `exposure`, `data_sensitivity`, `technologies`, `changed_files`, consoante o que se sabe. Os valores aceites estão em `sbd://toe/activation-vocabulary`.

---

### Sintoma — `detail: "minimal"` ou `detail: "ultrathin"` é recusado {#sintoma--detail-minimal-ou-detail-ultrathin-é-recusado}

**Causa.** Os dois níveis foram retirados, cada um por uma razão:

- `minimal` passou a chamar-se `lista`. Herdou o mesmo envelope de tokens e passou a trazer inline, por requisito, a descrição, `verify` e `evidence`.
- `ultrathin` foi retirado de vez. Existia para cortar a descrição publicada, e a descrição deixou de ser negociável: não sai de nenhum nível.

**Solução.** Quem vem de docs antigos usa `lista` em qualquer dos dois casos. O erro devolvido pelo servidor diz isto mesmo, e diz para onde cada um foi. `get_threat_landscape` e `select_sbd_toe_requirements` aceitam o mesmo eixo (`lista`/`standard`/`full`) e também recusam `minimal` com o mesmo aviso. O que cada nível põe *inline* está na [referência de `prepare_sbd_toe_codegen_context`](./05-tools-reference.md#prepare_sbd_toe_codegen_context).

---

### Sintoma — `size_estimate.within_envelope: false` {#sintoma--size_estimatewithin_envelope-false}

**Causa.** A resposta declara que o seu tamanho excede o envelope previsto. É uma declaração, não um erro: o servidor avisa em vez de truncar em silêncio.

**Solução.** Não ignorar o aviso. Um nível de `detail` mais compacto, ou uma declaração mais estreita (menos *concerns*, menos categorias), reduz a resposta. Se a seleção passar do que o nível promete caber, a resposta passa a `needs_decomposition` com lotes — ver acima.

---

## Instalação / cliente {#instalação--cliente}

### Sintoma — `claude mcp add` falha com `Cannot find package` {#sintoma--claude-mcp-add-falha-com-cannot-find-package}

### Causa {#causa-3}

Node.js `< 20.9.0` ou npm sem acesso ao registo público.

### Solução {#solução-6}

```bash
node --version          # confirmar ≥ 20.9.0
npm config get registry # confirmar https://registry.npmjs.org/
```

---

### Sintoma — Cursor / Claude Desktop não reconhece o servidor {#sintoma--cursor--claude-desktop-não-reconhece-o-servidor}

### Causa(s) {#causas-1}

1. Ficheiro de configuração em caminho errado
2. JSON inválido (trailing comma, aspas erradas)
3. Cliente não reiniciado após edição

### Solução {#solução-7}

1. Confirmar caminho (ver [Instalação](./03-instalacao.md))
2. Validar JSON: `jq . < /path/to/config.json` — erros aparecem
3. **Reiniciar o cliente** após cada alteração da configuração MCP

---

### Sintoma — Tools `sbd-toe.*` aparecem mas todas as chamadas falham {#sintoma--tools-sbd-toe-aparecem-mas-todas-as-chamadas-falham}

### Diagnóstico {#diagnóstico-1}

Executar o comando manualmente para isolar:

```bash
npx -y @shiftleftpt/sbd-toe-mcp
```

O servidor não escreve nada no *stderr* ao arrancar — o silêncio não é sinal de erro. Para validar, enviar-lhe uma mensagem `initialize` do protocolo MCP ou, no Claude Code, correr `claude mcp list`. Se a mensagem `initialize` não tiver resposta, o problema é do servidor / Node / dependências.

---

## Operacional {#operacional}

### Sintoma — output do MCP é em PT, mas o utilizador escreve EN {#sintoma--output-do-mcp-é-em-pt-mas-o-utilizador-escreve-en}

### Não é bug — é arquitectura {#não-é-bug--é-arquitectura}

O conteúdo canónico do manual está em PT. O *agent guide* diz explicitamente:

> *Always respond in the user's language. The manual content is in Portuguese — translate, summarise, and explain in whatever language the user writes in.*

**Solução:** o LLM deve **traduzir / sumarizar** o conteúdo PT para a língua do utilizador. Não passar a falar PT só porque o manual o está.

---

### Sintoma — utilizador discorda do *risk level* {#sintoma--utilizador-discorda-do-risk-level}

### Acção {#acção}

Não decidir unilateralmente. Apresentar:

1. O que `map_sbd_toe_applicability` sugere
2. O que mudaria se `risk_level` fosse X vs Y (custo: a exigência de cada capítulo muda; o conjunto de capítulos é o mesmo)
3. Quem assina a decisão (`CISO`, `executive_management`, `appsec`)

Marcar como `inferred` enquanto não há decisão.

---

## *Upgrades* e versionamento {#upgrades-e-versionamento}

### Quando re-correr `generate_sbd_toe_skill` {#quando-re-correr-generate_sbd_toe_skill}

Após cada *upgrade* do servidor MCP (releases minor/patch no npm). O conteúdo do *agent guide* pode mudar; a skill em disco está desactualizada até regenerar.

### Como saber se a skill está desactualizada {#como-saber-se-a-skill-está-desactualizada}

A skill em disco começa com:

```
<!-- SbD-ToE skill content — source: sbd://toe/agent-guide (@shiftleftpt/sbd-toe-mcp) -->
```

Não inclui versão explícita — comparar `sbd://toe/version` com a versão usada na última geração (manter como entrada de *changelog* do projecto).

---

## Quando reportar bug {#quando-reportar-bug}

Reportar em [github.com/SbD-ToE/sbd-toe-mcp/issues](https://github.com/SbD-ToE/sbd-toe-mcp/issues) se:

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

## A seguir {#a-seguir}

- [Versionamento e roadmap](./11-versionamento-roadmap.md) — release notes + futuro.
