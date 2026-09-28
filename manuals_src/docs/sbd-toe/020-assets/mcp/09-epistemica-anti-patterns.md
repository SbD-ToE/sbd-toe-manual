---
id: epistemica-anti-patterns
title: Disciplina epistémica e anti-patterns
description: Como rotular respostas geradas com o MCP — manual-grounded vs observed vs inferred vs not verified — e os erros mais comuns a evitar.
sidebar_label: Epistémica & anti-patterns
sidebar_position: 9
tags:
  - mcp
  - epistemica
  - anti-patterns
  - rigor
---

# Disciplina epistémica e anti-patterns

O servidor MCP devolve **dados estruturados**; o LLM **gera conteúdo a partir deles**. A junção dos dois cria uma tentação: apresentar *inferências do LLM* como se fossem *factos do manual*. Para que o output mereça a confiança dos auditores, *legal counsel*, *security champions* — toda afirmação deve ser **rotulável**. E um rótulo `manual-grounded` diz de onde vem o requisito, não que o código o cumpre: a verificação da implementação exige testes e revisão.

## Os 4 rótulos epistémicos {#os-4-rótulos-epistémicos}

| Rótulo | Definição | Sinal verde para o utilizador |
|---|---|---|
| **manual-grounded** | Recuperado via MCP — citar `chapterId` ou ID (`CTRL-*`, `<CAT>-NNN`, `MT-*`, `ART-*`) | "O manual diz: `AUT-001` (MFA obrigatório). `<texto verbatim ou parafraseado fielmente>`." |
| **observed** | Visível directamente no repositório / codebase | "No ficheiro `src/auth/login.ts:42`, observo: `<…>`." |
| **inferred** | Conclusão lógica a partir de *grounded* + *observed* — marcar explicitamente | "Inferência: dado que `AUT-001` exige MFA, e o código só valida password, falta o segundo factor." |
| **not verified** | Não confirmado | "Não verificado: `<…>`. Recomenda-se inspeção humana / teste / log." |

### Regra de ouro {#regra-de-ouro}

> **Em dúvida, preferir `not verified` a apresentar como facto.**
>
> Marcar como `not verified` permite ao utilizador agir; marcar erradamente como `manual-grounded` cria *false positives* que custam revisão e credibilidade.

---

## Onde aplicar cada rótulo {#onde-aplicar-cada-rótulo}

### `manual-grounded` {#manual-grounded}

Permitido apenas quando:
- Devolvido por uma tool MCP (`consult_*`, `get_*`, `query_*`, `resolve_*`, `prepare_*`)
- ID citado existe no output da chamada
- Texto reflete o que o output diz (não amplifica nem reduz)

❌ **Não** marcar como *grounded*:
- Resultados de `search_sbd_toe_manual` que **não foram lidos** (apenas vistos como *snippet*) — esses são pista, não evidência
- Síntese cross-tool (ex.: "`AUT-001` + `LOG-003` implicam X") — isso é `inferred`

### `observed` {#observed}

Permitido apenas quando:
- O ficheiro/linha foi lido (não inferido do nome do ficheiro)
- A observação é literalmente verificável

❌ **Não** marcar como *observed*:
- "Provavelmente o sistema faz X" — sem ter lido o código
- Comportamento esperado por causa do *framework* — isso é `inferred`

### `inferred` {#inferred}

Sempre marcar explicitamente quando:
- Combinas `manual-grounded` + `observed` para chegar a uma conclusão
- Aplicas conhecimento geral de segurança a um contexto específico
- Uma ligação sem `mitigation_confidence: "derived"` é estendida a outra situação

Forma recomendada: **"Inferência: `<conclusão>`. Baseado em: `<grounded ID>` + `<observação>`."**

### `not verified` {#not-verified}

Usar generosamente. Casos:
- A tool devolveu lista vazia (`controls: []`, `threats: []`, `assignments: []`)
- O *risk level* não foi confirmado pelo utilizador
- O resultado precisa de teste / scan / log que ainda não correu
- A pergunta toca em conteúdo posterior ao *snapshot* servido (ver `sbd://toe/version`)

---

## Confidence flags específicos do MCP {#confidence-flags-específicos-do-mcp}

Algumas tools devolvem campos próprios de confiança. Traduzi-los para rótulos:

| Campo do MCP | Tradução |
|---|---|
| `mitigation_confidence: "derived"` | `manual-grounded` (ligação estrutural) |
| ligação sem `mitigation_confidence: "derived"` | `inferred` — flag explicitamente |
| `completeness_report.m_recall < 1.0` | sinalizar **cobertura parcial** — o que falta é `not verified` |
| `coverage.hasMore: true` / `coverage_gaps` | resultado **paginado / com lacunas declaradas** — continuar via `nextOffset`; o servidor é *coverage-preserving* (nada truncado em silêncio), mas "página 1" ≠ "tudo" |
| `rule_trace` sem `CONCERNS_FILTER_*` quando concerns foram passadas | sinal de problema — pode estar a devolver mais do que se filtrou |

---

## Anti-patterns gerais {#anti-patterns-gerais}

### 1. Inventar IDs {#1-inventar-ids}

❌ "O controlo `CTRL-09-99` cobre isto."
✅ Verificar via `query_sbd_toe_entities({query: "CTRL-09-99"})` antes de citar. Se não existe, dizer: *"Nenhum controlo aplicável encontrado no manual para este caso — flag para revisão humana."*

### 2. Declarar conformidade regulatória {#2-declarar-conformidade-regulatória}

❌ "Este código é compliant com NIS2 Art. 21."
✅ "O cross-check NIS2 do manual mapeia Art. 21 ↔ capítulos N e M. Não declaração de conformidade — requer avaliação de *legal counsel* + evidência operacional."

### 3. Tratar código como evidência {#3-tratar-código-como-evidência}

❌ "Implementei o lockout, logo o controlo está coberto."
✅ "Implementação proposta. **Evidência esperada:** teste em `test/auth/lockout.spec.ts` + log entry `auth.lockout.activated` com schema X."

### 4. Fundir manual-grounded com inferred {#4-fundir-manual-grounded-com-inferred}

❌ "O manual diz que rate limiting + monitoring previnem credential stuffing."
✅ "Manual-grounded: o output liga `MT-NNN` (credential stuffing) a `CTRL-<domain>-<slug>-<hash>` com `mitigation_confidence: derived`. Inferência (minha): aplicados juntos cobrem o threat — marcado como inferência, não como facto do manual."

### 5. Saltar gate `needs_clarification` / `needs_decomposition` {#5-saltar-gate-needs_clarification--needs_decomposition}

❌ Re-chamar `prepare_sbd_toe_codegen_context` com o mesmo payload para "tentar de novo".
✅ Parar, dialogar com o utilizador, **re-chamar só após inputs novos**.

### 6. Mostrar uma ligação inferida como certeza {#6-mostrar-mitigation_confidence-heuristic-como-certeza}

❌ "`CTRL-…` mitiga `MT-NNN`." — apresentado como certeza, sem `mitigation_confidence: "derived"`.
✅ "`CTRL-…` mitiga `MT-NNN` — ligação **inferida** (sem `mitigation_confidence: derived`); validar com teste / revisão humana."

### 7. Assumir a cobertura do *snapshot* sem a confirmar {#7-assumir-a-cobertura-do-snapshot-sem-a-confirmar}

❌ Responder sobre um cross-check normativo (ou qualquer página) assumindo que o MCP a serve — ou que não a serve.
✅ Ler `sbd://toe/version` (manual, KG, ontologia) e, em dúvida, validar com `inspect_sbd_toe_retrieval` se o documento aparece nos *top-ranked records*. Os cross-checks publicados — **CRA / DORA / NIS2 / GDPR / AI Act / ENISA-CSA** — estão indexados no *snapshot* servido; conteúdo posterior ao *snapshot* vive só no manual web até nova publicação (ver [content lag](./10-troubleshooting-faq.md#content-lag)).

### 8. Confundir *concerns* (ontológicos) com domínios STRIDE {#8-confundir-concerns-ontológicos-com-domínios-stride}

❌ `concerns: ["spoofing", "tampering"]`
✅ `concerns: ["auth", "integrity"]` — o vocabulário ontológico é fechado e mapeia para domínios STRIDE indirectamente.

### 9. Saltar `setup_sbd_toe_agent` no início da sessão {#9-saltar-setup_sbd_toe_agent-no-início-da-sessão}

❌ Começar a chamar tools sem inicializar.
✅ Primeira mensagem da sessão de segurança: `setup_sbd_toe_agent(riskLevel, projectRole)` — carrega a exigência por capítulo e as regras do *role*. Em clientes que não expõem *prompts* (como o Claude Desktop), começar por `sbd://toe/quick-start` e pela declaração em `select_sbd_toe_requirements`.

### 10. Re-gerar a skill no início de cada sessão {#10-re-gerar-a-skill-no-início-de-cada-sessão}

❌ Chamar `generate_sbd_toe_skill()` cada vez.
✅ Gerar uma vez, guardar no caminho canónico (`.claude/skills/sbd-toe.md`, etc.), re-gerar **apenas após upgrade do MCP**.

### 11. Confundir "consumir MCP" com "expor MCP server" (escopo de segurança distinto) {#11-confundir-consumir-mcp-com-expor-mcp-server-escopo-de-segurança-distinto}

Este mini-site cobre o uso do MCP server SbD-ToE — o consumo. Quando a organização passa a **expor um MCP server próprio** (não consumir), entra num escopo de segurança adicional que **não é coberto** por este mini-site nem pelo SbD-ToE manual em geral.

❌ Assumir que ler este mini-site cobre a segurança de um MCP server a publicar pela organização.
✅ Para MCP servers expostos, consultar o **OWASP MCP Top 10 (2025)** — catálogo dedicado que cobre prompt injection em contexto MCP, *tool poisoning*, *excessive permissions*, autenticação/autorização inadequadas, transporte inseguro, validação de input, *output handling*, monitorização insuficiente, defaults inseguros. Os controlos SbD-ToE relevantes (`ARC-015`, `REQ-AGN-001..004`, `OPS-011..014`, Policy 38, Policy 39) aplicam-se directamente — o OWASP MCP Top 10 funciona como *checklist de cobertura específica*, complementar ao threat modeling do [Cap. 03 §playbook-agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic).

---

## Checklist de rigor antes de submeter qualquer output {#checklist-de-rigor-antes-de-submeter-qualquer-output}

1. Cada afirmação tem um dos 4 rótulos?
2. Todos os IDs citados existem em outputs MCP da sessão?
3. Ligações sem `mitigation_confidence: derived` estão marcadas como inferidas?
4. `m_recall < 1.0` foi sinalizado?
5. Não há declaração de conformidade?
6. Código não foi apresentado como evidência?
7. Para perguntas regulatórias — a cobertura do *snapshot* foi confirmada em `sbd://toe/version` (e o manual web consultado para conteúdo posterior)?

Se algum check falha → **rever antes de entregar**.

## A seguir {#a-seguir}

- [Troubleshooting / FAQ](./10-troubleshooting-faq.md) — sintomas vs soluções.
- [Padrões avançados](./08-padroes-avancados.md) — para combinar tools sem perder rigor.
